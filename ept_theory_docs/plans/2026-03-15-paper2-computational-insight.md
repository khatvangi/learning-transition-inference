# Paper 2: Computational Validation of Phase-Transition Diagnostics Across Learning Domains

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Validate the (Ψ, F) diagnostic framework across three computational domains — grokking (from Paper 1), dictionary learning, and feature switching — with prospectively defined task structure, demonstrating that phase-transition signatures (velocity spikes, hysteresis, dose-response) appear in systems with different microscopic dynamics.

**Architecture:** Three self-contained experiments sharing one analysis framework. Each domain has: (1) a known task-aligned subspace W_task derivable before training, (2) a disordered pre-transition state, (3) a parametric "seed" that modulates transition probability or timing. The CTRNN model provides the theoretical scaffold (not validation — it's illustrative). Human predictions are stated but not tested (deferred to Paper 3).

**Tech Stack:** PyTorch, numpy, scipy, scikit-learn, matplotlib. Conda env `ept`.

**Target venue:** NeurIPS / ICML (computational learning theory track)

---

## Paper structure

1. **Introduction**: Phase transitions in learning — the (Ψ, F) framework
2. **Framework**: CTRNN model (brief, illustrative, not "validated")
3. **Domain 1 — Grokking**: Results from Paper 1 definitive experiment (import, don't rerun)
4. **Domain 2 — Dictionary Learning**: Sparse coding with planted dictionary
5. **Domain 3 — Feature Switching**: Spurious correlation → true features
6. **Cross-domain analysis**: Shared signatures, quantitative comparison
7. **Discussion**: What the framework predicts for biological learning (untested)

---

## Task 1: Dictionary Learning Experiment

**Files:**
- Create: `/storage/EPT/ept_paper2/dictionary_learning/run_dictlearn.py`
- Create: `/storage/EPT/ept_paper2/dictionary_learning/analyze_dictlearn.py`

### Design

**Task**: Learn a dictionary D_true ∈ R^{m×k} from sparse signals x = D_true·α + noise, where α is sparse.

**Known structure**:
- W_task = D_true (known by construction — we plant it)
- F_task(D_learned) = ||P_{D_true} D_learned||_F / ||D_learned||_F (projection onto true dictionary column space)
- Ψ = ||D_t - D_{t-1}||_F (weight velocity of learned dictionary)

**Seed**: L1 sparsity regularization on activations. Higher λ_sparse → stronger push toward sparse solutions → faster convergence to D_true.

**Hysteresis protocol**:
- Train with λ_sparse for 500 epochs
- Remove λ_sparse (set to 0) at epoch 500
- Continue training for 200 more epochs
- Measure: does F_task persist after seed removal?

**Parameters**:
- m = 64 (signal dimension)
- k = 20 (dictionary atoms)
- n_samples = 5000
- sparsity: 3 nonzero coefficients per signal
- noise: σ = 0.1
- λ_sparse ∈ {0, 0.01, 0.05, 0.1, 0.5, 1.0} (dose-response)
- 25 seeds per condition
- cosθ analog: rotate D_initial by angle θ from D_true

**Metrics per eval**:
- F_task: alignment with true dictionary
- Ψ: dictionary weight velocity
- reconstruction_error: ||x - D·α||²
- sparsity: mean ||α||_0

**Implementation**: Use PyTorch with custom sparse coding layer. Dictionary update via gradient descent on reconstruction + sparsity loss.

### Step 1: Implement dictionary learning

```python
# model: learnable dictionary D ∈ R^{m×k}
# forward: given x, solve for sparse α via ISTA, then reconstruct
# loss: ||x - D·α||² + λ·||α||_1
# F_task: subspace alignment between learned D and planted D_true
```

### Step 2: Run dose-response sweep

- 6 λ_sparse values × 25 seeds = 150 runs
- ~5 min per run = ~12 hours total

### Step 3: Run hysteresis protocol

- For each converged run: remove λ_sparse, continue 200 epochs
- Measure persistence of F_task

### Step 4: Compute cross-domain metrics

- Velocity spike timing relative to F_task transition
- Persistence ratio after seed removal
- Dose-response curve (λ_sparse vs transition probability and timing)

---

## Task 2: Feature Switching Experiment

**Files:**
- Create: `/storage/EPT/ept_paper2/feature_switching/run_featswitch.py`
- Create: `/storage/EPT/ept_paper2/feature_switching/analyze_featswitch.py`

### Design

**Task**: Binary classification on colored MNIST variant. Training data has spurious color-label correlation (90% reliable). Test data has no correlation. Network must switch from color shortcut (Glass) to shape features (Crystal).

**Known structure**:
- W_task = shape feature subspace (known from task construction)
- W_glass = color feature subspace (the spurious shortcut)
- F_task = accuracy on color-randomized test set (measures reliance on true features)
- Ψ = ||W_t - W_{t-1}|| (weight velocity)

**Seed**: Anti-shortcut regularization — penalize correlation between intermediate representations and color features.

**Hysteresis protocol**:
- Train with anti-shortcut λ_anti for 1000 epochs
- Remove at epoch 1000 (set to 0)
- Continue on ORIGINAL (spuriously correlated) data for 500 epochs
- Measure: does the network retain true features or revert to shortcuts?

**Parameters**:
- Architecture: small CNN (2 conv + 2 FC)
- Dataset: simplified colored MNIST (digits 0-4 vs 5-9, background colored)
- Spurious correlation: 90% in train, 50% in test
- λ_anti ∈ {0, 0.01, 0.05, 0.1, 0.5, 1.0}
- 25 seeds per condition
- Training: 1500 epochs, eval every 10

**Metrics per eval**:
- F_task: test accuracy on color-randomized data
- F_shortcut: accuracy attributable to color alone (on a color-only probe set)
- Ψ: weight velocity
- train_acc, test_acc_standard, test_acc_unbiased

### Step 1: Create colored MNIST dataset

```python
# take MNIST digits, add colored backgrounds
# training: P(color=red|digit<5) = 0.9
# test_standard: same bias
# test_unbiased: P(color|digit) = 0.5
# test_reversed: P(color=red|digit<5) = 0.1 (adversarial)
```

### Step 2: Implement anti-shortcut regularizer

```python
# penalize mutual information between hidden activations and color
# approximated as: ||mean_red_hidden - mean_blue_hidden||² should be small
```

### Step 3: Run dose-response + hysteresis

- 6 λ_anti values × 25 seeds = 150 runs
- Hysteresis on all converged runs

---

## Task 3: CTRNN Illustration (brief, not validation)

**Files:**
- Create: `/storage/EPT/ept_paper2/ctrnn/run_ctrnn.py`

### Design

Simplified from current manuscript. 50 trials each of Coherent and Rigid conditions. Used ONLY as Figure 1 illustration — "here is what the framework predicts in a controlled setting." NOT presented as validation.

**Parameters**: Same as current manuscript (N=100, k=4, p=30, g_task=1.8, g_glass=2.0).

### Output
- Figure: single-trial trajectories in (Ψ, F) space for Coherent vs Rigid
- Note in caption: "This simulation demonstrates the framework's predictions; the grokking, dictionary learning, and feature switching experiments test them."

---

## Task 4: Cross-Domain Analysis

**Files:**
- Create: `/storage/EPT/ept_paper2/cross_domain_analysis.py`

### Analyses

1. **Shared signature table**

| Feature | Grokking | Dict Learning | Feature Switching |
|---------|----------|---------------|-------------------|
| Velocity spike at transition | ? | ? | ? |
| Spike duration < 1% of training | ? | ? | ? |
| F_task persistent after seed removal | ? | ? | ? |
| Dose-response (seed strength vs timing) | ? | ? | ? |
| Spearman ρ (seed vs F_task) | ? | ? | ? |

2. **Normalized comparison**
- Normalize time to [0, 1] (fraction of training)
- Normalize Ψ to z-scores within each domain
- Plot all three domains in the same (Ψ, F) phase space
- This is the KEY FIGURE of Paper 2

3. **Statistical rigor**
- Report ALL correlations with exact p-values (not just "significant")
- Use Bonferroni correction for 3 domains × 5 metrics = 15 tests
- Report effect sizes throughout
- Show individual runs, not just means

---

## Task 5: Write Paper 2 Manuscript

**Files:**
- Create: `/storage/EPT/ept_paper2/manuscript/paper2.tex`

### Key differences from current manuscript

| Current manuscript | Paper 2 |
|---|---|
| CTRNN as "validation" | CTRNN as illustration only |
| Human insight in title | No human claims |
| C(k=48) as metric | IPR as order parameter |
| Mixed parameter configs | Each domain: one frozen config |
| Dictionary/feature switching: 2 sentences | Full experiments with data |
| Grokking Spearman p=0.058 buried | All p-values prominent |

### Predictions for Paper 3 (stated, not tested)

1. Human insight tasks should show behavioral velocity spike (KL divergence of strategy) time-locked to breakthrough
2. Mooney image pop-out should exhibit contrast hysteresis
3. EEG gamma burst should coincide with velocity spike
4. Cognitive load should degrade pseudo-insight (Glass) but not genuine insight (Crystal)

---

## Compute Budget

| Experiment | Runs | Est. time |
|---|---|---|
| Dictionary learning | 150 + 150 hysteresis | ~24 hours |
| Feature switching | 150 + 150 hysteresis | ~36 hours |
| CTRNN illustration | 100 | ~10 minutes |
| Grokking | From Paper 1 | Already running |
| **Total** | ~600 | ~60 hours |

---

## Dependencies

- **Paper 1 definitive experiment** must complete first (provides grokking data)
- Dictionary learning and feature switching can run in parallel
- CTRNN is fast, run last
- Cross-domain analysis after all data collected

## Execution Order

1. Wait for Paper 1 Stage 1 results (Arrhenius) — ~2-3 days
2. Implement dictionary learning experiment — 1 day coding
3. Implement feature switching experiment — 1 day coding
4. Run both in parallel — ~2 days compute
5. Run CTRNN — 10 minutes
6. Cross-domain analysis — 1 day
7. Write manuscript — 3-5 days

**Total: ~2-3 weeks from now** (assuming Paper 1 data is ready)
