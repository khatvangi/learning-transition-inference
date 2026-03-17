# Kinetics Analysis — Revised After 10-Point and 50-Point Fits

**Date**: 2026-03-17
**Status**: Critical revision — Arrhenius claim retracted, correct picture emerging

---

## 1. What Happened

### Original (5 group means)
- Arrhenius: R² = 0.976, ΔAICc = +4.64 vs power law
- Conclusion: "Arrhenius is the best model"

### Extended (10 group means)
- Arrhenius: R² = 0.955, ΔAICc = +7.43 WORSE than power law
- Power law WINS. VFT wins by even more.
- Stretched exponential β = 0.37 (glass range)

### Individual seeds (50 data points)
- Arrhenius: R² = 0.816, AICc = -125.3
- Power law: R² = 0.842, AICc = -132.8, ΔAICc = -7.5 (PL better)
- Generalized power: α = 0.34, CI [0.01, 0.73]. α=1 EXCLUDED.
- All 3-parameter models beat Arrhenius by ΔAICc > 8

### What This Means
The Arrhenius claim (ln(t) ∝ 1/λ_WD) was an artifact of fitting 2 parameters to 5 points. With more data, the relationship is SUBLINEAR in 1/λ_WD. The exponent α ≈ 0.34 is closer to a cube-root than linear dependence on 1/WD.

---

## 2. The Honest Picture

**What we can say with confidence (robust to functional form):**

1. t_grok decreases monotonically with λ_WD — MORE weight decay = FASTER grokking
2. The relationship is superlinear (faster than t ∝ 1/λ)
3. WD=0 never groks (3 seeds, 500k epochs) — the transition REQUIRES the control parameter
4. ANY nonzero WD produces grokking with 100% rate (50/50 runs)
5. The ordered state shows hysteresis (persists at WD=0)
6. Phase coexistence: different seeds in different phases at matched epochs

**What we CANNOT say with current data:**

1. Whether the kinetics are Arrhenius, power law, VFT, or stretched exponential
2. What the barrier-crossing mechanism is (if there is a single barrier)
3. Whether the "barrier height" scales as 1/λ, λ^{-0.34}, or something else

**The range problem:** Our WD values span only 1 order of magnitude (0.03-0.5). To distinguish ln(t) ∝ 1/λ from ln(t) ∝ λ^{-0.34}, we'd need 2+ orders of magnitude. This is physically limited: WD too low → grokking takes millions of epochs; WD too high → training may not converge.

---

## 3. What This Does and Doesn't Change

### DOES NOT CHANGE (still strong):
- **Hysteresis** (G3) — topological fact, independent of kinetics
- **Phase coexistence** (I1) — different seeds in different phases
- **Feature-space bottleneck** (F1-F3) — independent of kinetics
- **Depth non-monotonicity** (D1-D6) — independent of kinetics
- **Velocity spike** (G1) — independent of kinetics
- **Fourier crystallization** (G2) — independent of kinetics

### CHANGES:
- **G5: "Arrhenius kinetics" → "superlinear kinetics with undetermined functional form"**
- **T3: "Kramers escape" → demoted from "consistent" to "one possible interpretation"**
- **The glass relaxation counter-argument** weakened for kinetics (β ≈ 0.34 is glass-like) but strengthened for topology (hysteresis asymmetry)

### The Revised Kramers Picture
If we interpret via Kramers, the generalized power α ≈ 0.34 would mean:
- ΔE_effective / T ∝ λ_WD^{-0.34}
- This could arise from: (a) a distribution of barrier heights (not a single barrier), or (b) the effective temperature depending on WD in a complex way, or (c) the landscape being fractal/multiscale (consistent with Ly & Gong 2025)

The Ly & Gong (2025, Nature Comms) multifractal loss landscape framework predicts anomalous scaling exponents — their Hurst exponent H controls the diffusion/escape dynamics. α ≈ 0.34 could be a consequence of the multifractal landscape structure.

---

## 4. Revised Manuscript Language

### Old (RETRACT):
> "The relationship ln(t_grok) = A/λ_WD + B follows an Arrhenius law (R² = 0.976), indicating that weight decay modulates an effective free energy barrier between memorization and generalization basins."

### New (REPLACE WITH):
> "Grokking time decreases superlinearly with weight decay strength. Fitting the generalized power law ln(t_grok) = A · λ_WD^{-α} + B to 50 individual runs across 10 weight decay values yields α = 0.34 (95% CI: [0.01, 0.73]). The pure Arrhenius form (α = 1) is excluded from the confidence interval. Multiple functional forms — power law, Vogel-Fulcher-Tammann, and stretched exponential — fit comparably over the available range (ΔAICc < 9 between the best and worst 2-parameter models). With weight decay values spanning only one order of magnitude (0.05-0.50), the data are insufficient to discriminate the kinetic mechanism definitively. What the data establish unambiguously is: (i) WD = 0 never produces grokking, (ii) any nonzero WD produces grokking with 100% probability, (iii) the transition timing depends continuously on WD strength, and (iv) the ordered state exhibits classical hysteresis after WD removal. The first three observations require a control-parameter-dependent transition; the fourth confirms irreversibility."

### Old Proposition 3 (RETRACT):
> "If ΔV(λ) = A₀/λ... then ln⟨t_grok⟩ = A/λ_WD + B"

### New Proposition 3 (REPLACE WITH):
> "The grokking time follows ln(t) = A · λ^{-α} + B with α ∈ (0, 1). This is consistent with barrier-crossing dynamics where either (a) the effective barrier scales sublinearly with the inverse control parameter, (b) a distribution of barrier heights produces an averaged sublinear response, or (c) the escape dynamics occur on a multifractal landscape (Ly & Gong, 2025). The exponent α distinguishes barrier-crossing from critical slowing: critical phenomena predict t ∝ |λ - λ_c|^{-z} with a finite critical point λ_c, while our data show divergence at λ = 0 with no evidence of a finite critical point."

---

## 5. Dense WD Sweep (PLANNED)

**Script**: `/storage/EPT/ept_definitive/dense_wd_sweep.py`
**Design**: 60 WD values (log-spaced, 0.03-1.0) × 2 seeds = 120 runs
**Purpose**: 120 individual data points spanning 1.5 orders of magnitude
**Estimated time**: 12-20 hours

**What this will tell us:**
- Is α stable across the full range?
- Does the relationship curve differently at low vs high WD?
- Is there a critical WD value below which behavior changes qualitatively?
- With 120 points, can we distinguish power law from stretched exponential?

**Launch after current experiments finish.**

---

## 6. Key Takeaway

The Arrhenius claim was overclaimed. The kinetics are underdetermined. But the FIRST-ORDER TOPOLOGICAL evidence (hysteresis, coexistence, discontinuity) is independent of kinetics and remains solid. The paper should lead with topology, not kinetics.

The kinetics section becomes: "here's what we measured, here's the exponent, here's what we can't determine, here's what we'd need to resolve it." This is honest and scientifically stronger than overclaiming Arrhenius.
