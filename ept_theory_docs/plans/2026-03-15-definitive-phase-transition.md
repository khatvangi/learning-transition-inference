# Definitive Phase Transition Experiment

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Run a single, internally consistent experiment that either confirms or falsifies grokking as a first-order phase transition, with proper power (n>=20), correct metrics (C at full bandwidth), and all claims testable from one dataset.

**Architecture:** Fork v8 codebase into `/storage/EPT/ept_definitive/`. Fix the C(k=5) bug to use C(k=48). Run four experimental stages sequentially: Arrhenius scaling (10 WD values x 20 seeds), WD=0 control (20 seeds x 500k epochs), hysteresis (re-run all grokked checkpoints with WD=0), and cosθ sweep (5 values x 20 seeds). All from one frozen config. Compute AIC/BIC for model comparison. Generate publication-ready figures.

**Tech Stack:** PyTorch, numpy, scipy (for stats), matplotlib. Conda env `ept`. 2x TITAN RTX on boron.

**Frozen experiment parameters:**
- p=97, train_fraction=0.3, embed_dim=128, hidden_dim=128, n_hidden_layers=2
- lr=1e-3, batch_size=512, AdamW optimizer
- eval_every=100 epochs
- grok threshold: test_acc >= 0.95 sustained for 3 evals, train_acc >= 0.99
- C metric: full bandwidth k=48 (NOT k=5)

These match the v8 WD bisection (the only experiment with consistent, trustworthy data).

---

## Task 1: Fork and fix codebase

**Files:**
- Create: `/storage/EPT/ept_definitive/` (copy from v8)
- Modify: `config.py` — freeze parameters, fix k_C
- Modify: `trainer.py` — fix compute_fourier_C to use full bandwidth
- Modify: `fourier_subspace.py` — add IPR computation
- Modify: `data.py` — fix train_fraction default

**Step 1: Copy v8 codebase**

```bash
cp -r /storage/EPT/ept_grokking_v8/ept_grokking/ /storage/EPT/ept_definitive/
rm -rf /storage/EPT/ept_definitive/results/
rm -rf /storage/EPT/ept_definitive/__pycache__/
rm -f /storage/EPT/ept_definitive/*.log
```

**Step 2: Fix config.py — freeze all parameters**

In `config.py`, change:
```python
# FROZEN PARAMETERS — DO NOT CHANGE
k_C: int = 48  # was 5 — CRITICAL FIX: full bandwidth Fourier content
train_fraction: float = 0.3  # was 0.5 — matches manuscript and v8 bisection
hidden_dim: int = 128  # was 256 — matches manuscript
weight_decay_base: float = 0.1  # default for most experiments
```

**Step 3: Fix trainer.py compute_fourier_C**

In `trainer.py`, the function `compute_fourier_C` (line ~96) restricts to k_C modes:
```python
# REMOVE THESE LINES:
k_C = CONFIG.k_C
F_cos = F_cos[:, :k_C]
F_sin = F_sin[:, :k_C]
```

Replace with:
```python
# use full bandwidth — all (p-1)/2 = 48 modes
# the k_C restriction was discovered to be flawed (see RESULTS.md polymorph diagnostic)
```

This makes compute_fourier_C use ALL modes, matching compute_alignment_from_embeddings.

**Step 4: Add IPR computation to fourier_subspace.py**

Add after `compute_fourier_power`:
```python
def compute_ipr(power_per_freq: torch.Tensor) -> float:
    """
    inverse participation ratio of Fourier power spectrum.
    IPR = (sum |c_k|^2)^2 / sum |c_k|^4
    IPR = K for uniform, IPR = 1 for single mode.
    """
    weights = power_per_freq / (power_per_freq.sum() + 1e-10)
    ipr = 1.0 / (weights ** 2).sum().item()
    return ipr
```

**Step 5: Add IPR to trainer evaluate method**

In `trainer.py` `evaluate()`, after computing C, also compute IPR and per-frequency power. Store in eval point.

**Step 6: Update data.py default**

Change `get_dataloaders` default `train_fraction=0.5` to `train_fraction=0.3`.
Change `get_probe_set` default `train_fraction=0.5` to `train_fraction=0.3`.

**Step 7: Verify the fix**

```bash
cd /storage/EPT/ept_definitive && conda run -n ept python -c "
from fourier_subspace import get_dft_matrix, compute_fourier_power, compute_ipr
import torch
p = 97
F_cos, F_sin = get_dft_matrix(p, 'cpu')
print(f'Full bandwidth modes: {F_cos.shape[1]}')  # should be 48
# test IPR on uniform
uniform_power = torch.ones(48)
print(f'IPR uniform: {compute_ipr(uniform_power):.1f}')  # should be 48
# test IPR on single mode
single_power = torch.zeros(48); single_power[3] = 1.0
print(f'IPR single: {compute_ipr(single_power):.1f}')  # should be 1
"
```

Expected: `Full bandwidth modes: 48`, `IPR uniform: 48.0`, `IPR single: 1.0`

---

## Task 2: Create unified experiment runner

**Files:**
- Create: `/storage/EPT/ept_definitive/run_definitive.py`

This single script runs all four stages sequentially, saving results in a clean structure.

**Design:**

```
results/
  config.json                    # frozen config, git hash, timestamp
  stage1_arrhenius/
    raw/                         # per-run JSON files
    summary.json                 # aggregated results
    checkpoints/                 # grokked model checkpoints (for hysteresis)
  stage2_wd0_control/
    raw/
    summary.json
  stage3_hysteresis/
    raw/
    summary.json
  stage4_costheta/
    raw/
    summary.json
    checkpoints/
```

**Stage 1: Arrhenius Scaling** (priority 1)
- WD ∈ {0.05, 0.07, 0.1, 0.12, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5}
- 20 seeds per WD (seeds 0-19)
- 200 runs total
- max_epochs: 200k for WD <= 0.1, 100k for WD > 0.1
- cosθ = None (no alignment regularizer, λ_align = 0)
- save checkpoint at grok detection + 2000 epochs (for hysteresis)
- record: t_grok, C(k=48), IPR, weight_norm, velocity timeseries

**Stage 2: WD=0 Control** (priority 2)
- WD = 0
- 20 seeds (seeds 0-19)
- max_epochs: 500k
- record: final_test_acc, final_C, weight_norm, velocity (expect: all zero grok)

**Stage 3: Hysteresis** (priority 1, depends on Stage 1)
- for each grokked checkpoint from Stage 1:
  - load checkpoint
  - set WD = 0, λ_align = 0
  - continue training for 20k additional epochs
  - record: test_acc every 100 epochs, C(k=48), IPR, weight_norm
- expected: ~200 hysteresis tests (if all grok)

**Stage 4: cosθ Sweep** (priority 3)
- WD = 0.1 (frozen)
- cosθ ∈ {0.0, 0.25, 0.5, 0.75, 1.0}
- λ_align = 0.1
- 20 seeds per cosθ (seeds 0-19)
- 100 runs total
- max_epochs: 100k
- save checkpoint at grok + 2000 for hysteresis
- record: t_grok, C(k=48), IPR, frequency spectrum, weight_norm

**Per-run JSON output:**
```json
{
  "seed": 0,
  "weight_decay": 0.1,
  "cos_theta": null,
  "grokked": true,
  "grok_epoch": 44800,
  "final_test_acc": 1.0,
  "final_train_acc": 1.0,
  "C_k5": 0.20,
  "C_k48": 0.997,
  "IPR": 3.2,
  "weight_norm": 63.4,
  "top_freqs": [[5, 0.55], [4, 0.31], [3, 0.14]],
  "total_epochs": 46900,
  "elapsed_s": 904.3,
  "timeseries": {
    "epochs": [0, 100, 200, ...],
    "test_acc": [0.01, 0.01, ...],
    "train_acc": [0.01, 0.5, ...],
    "C_k48": [0.02, 0.02, ...],
    "IPR": [47.2, 46.8, ...],
    "weight_velocity": [0.0, 0.1, ...],
    "weight_norm": [5.1, 5.0, ...]
  },
  "checkpoint_path": "checkpoints/wd0.10_seed0_grokked.pt"
}
```

**Implementation notes:**
- sequential execution (one run at a time, one GPU)
- incremental checkpoint: save progress after each run so we can resume
- flush prints (not tqdm) for nohup compatibility
- estimate: ~15 min per run at WD=0.1, ~5 min at WD=0.3 → Stage 1 ≈ 40 hours

---

## Task 3: Create analysis script

**Files:**
- Create: `/storage/EPT/ept_definitive/analyze_definitive.py`

**Analyses:**

1. **Arrhenius model comparison** (AIC/BIC, not just R²)
   - fit 3 models to median t_grok vs WD:
     - Arrhenius: ln(t) = A/WD + B
     - power law: ln(t) = α·ln(WD) + B
     - linear: t = a·WD + b
   - compute AIC = n·ln(RSS/n) + 2k for each
   - compute BIC = n·ln(RSS/n) + k·ln(n)
   - report ΔAIC and ΔBIC relative to best model
   - with 10 WD values, this is a meaningful comparison

2. **Hysteresis analysis**
   - for each run: did accuracy stay > 0.95 for all 20k epochs at WD=0?
   - for each run: did C(k=48) stay > 0.95?
   - aggregate: what fraction of grokked runs show persistent hysteresis?
   - plot: accuracy and C over time for representative runs

3. **CV analysis with proper bootstrap**
   - for each WD value: compute CV of t_grok across 20 seeds
   - bootstrap 95% CI (10000 resamples)
   - with n=20, bootstrap is reliable

4. **Frequency analysis**
   - for each grokked run: compute power spectrum, top-5 frequencies
   - cluster runs by frequency selection pattern
   - show that cosθ controls which harmonics (Stage 4) while WD-only shows random selection (Stage 1)

5. **Publication figures**
   - Fig 1: Arrhenius plot (ln(t_grok) vs 1/WD) with 3 model fits + AIC
   - Fig 2: Hysteresis (accuracy + C + weight_norm over 20k post-grok epochs, n=20+ traces)
   - Fig 3: Phase boundary (grok rate vs WD, showing sharp boundary at WD=0)
   - Fig 4: Frequency symmetry-breaking (power spectra at different cosθ)
   - Fig 5: Representative training curves (accuracy, C, velocity for typical run)

---

## Task 4: Run Stage 1 (Arrhenius)

```bash
cd /storage/EPT/ept_definitive
nohup conda run -n ept python -u run_definitive.py --stage 1 > stage1.log 2>&1 &
```

**Expected duration:** ~40-50 hours on one GPU

**Monitor:**
```bash
tail -f /storage/EPT/ept_definitive/stage1.log
cat results/stage1_arrhenius/summary.json | python3 -m json.tool | head -30
```

**Success criteria:**
- All 200 runs complete
- WD >= 0.1: expect 100% grok rate (confirmed by v8 bisection)
- WD = 0.05: may or may not grok within 200k epochs — this is new data
- WD = 0.07: similarly uncertain — this is the interesting regime

---

## Task 5: Run Stage 2 (WD=0 control)

```bash
cd /storage/EPT/ept_definitive
nohup conda run -n ept python -u run_definitive.py --stage 2 > stage2.log 2>&1 &
```

Can run in parallel with Stage 1 on second GPU.

**Expected duration:** ~24 hours (20 runs × 500k epochs × ~3 min per 100k)

**Success criteria:**
- 0/20 grok (confirming WD=0 is the boundary)
- all test_acc < 0.01 at 500k epochs
- all weight_velocity → 0 (dead fixed point)

---

## Task 6: Run Stage 3 (Hysteresis) — after Stage 1 completes

```bash
cd /storage/EPT/ept_definitive
nohup conda run -n ept python -u run_definitive.py --stage 3 > stage3.log 2>&1 &
```

**Expected duration:** ~10-15 hours (200 checkpoints × 20k epochs × ~3 min each)

**Success criteria:**
- ≥ 95% of grokked runs maintain test_acc > 0.95 at WD=0 for 20k epochs
- ≥ 90% maintain C(k=48) > 0.90
- weight_norm grows (expected) but solution structure preserved

---

## Task 7: Run Stage 4 (cosθ sweep)

```bash
cd /storage/EPT/ept_definitive
nohup conda run -n ept python -u run_definitive.py --stage 4 > stage4.log 2>&1 &
```

Can run after Stage 1 completes (or in parallel on second GPU).

**Expected duration:** ~25 hours

**Success criteria:**
- 100% grok rate at all cosθ (confirmed by prior experiments)
- monotonic decrease in t_grok with cosθ
- C(k=48) > 0.95 for all grokked runs
- clear frequency separation: cosθ=0 → high-freq, cosθ=1 → low-freq

---

## Task 8: Run analysis and generate figures

```bash
cd /storage/EPT/ept_definitive
conda run -n ept python analyze_definitive.py
```

**Key outputs:**
- `results/analysis/arrhenius_comparison.json` — AIC/BIC for 3 models
- `results/analysis/hysteresis_summary.json` — persistence rates
- `results/analysis/cv_bootstrap.json` — CV with 95% CIs
- `results/figures/fig1_arrhenius.pdf`
- `results/figures/fig2_hysteresis.pdf`
- `results/figures/fig3_phase_boundary.pdf`
- `results/figures/fig4_frequency_symmetry.pdf`
- `results/figures/fig5_training_curves.pdf`

---

## Task 9: Write clean results document

After all stages complete, write `results/DEFINITIVE_RESULTS.md` documenting:
1. Exact parameters used (one table, no ambiguity)
2. All results with proper statistics
3. Which claims are supported and which are not
4. Honest assessment of evidence strength per claim

---

## Compute budget estimate

| Stage | Runs | Max epochs | Est. time (1 GPU) |
|-------|------|------------|-------------------|
| 1: Arrhenius | 200 | 100k-200k | ~40 hours |
| 2: WD=0 | 20 | 500k | ~24 hours |
| 3: Hysteresis | ~200 | 20k | ~12 hours |
| 4: cosθ | 100 | 100k | ~25 hours |
| **Total** | **~520** | — | **~100 hours** |

With 2 GPUs and running Stages 1+2 in parallel, then 3+4 in parallel: **~65 hours ≈ 3 days.**

---

## What this experiment will definitively answer

| Claim | Test | What would falsify it |
|-------|------|-----------------------|
| First-order phase transition | Hysteresis on n=200 | <80% of runs show persistent crystal at WD=0 |
| Arrhenius kinetics | AIC/BIC on 10 WD values | Power law or linear has lower AIC by >10 |
| WD=0 is exact boundary | 20 seeds at 500k epochs | Any grokking at WD=0 |
| Universal Fourier structure | C(k=48) on all grokked | Any run with C(k=48) < 0.90 |
| Frequency symmetry-breaking | Power spectra at different cosθ | No frequency separation between cosθ=0 and cosθ=1 |
| Quasi-deterministic timing | CV with n=20 per condition | CV > 0.5 (stochastic nucleation territory) |
