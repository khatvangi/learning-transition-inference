# Kramers Theory Connection to Grokking Arrhenius Kinetics

**Date**: 2026-03-16
**Status**: Working derivation — needs experimental validation

---

## 1. The Empirical Finding

From the EPT grokking experiments (5 WD values, 5 seeds each):

```
ln(t_grok) = 0.115 / λ_WD + 9.59    (R² = 0.976)
```

This is **Arrhenius form**: ln(t) = A / control_parameter + B

The question: **why does grokking time follow this specific functional form?**

---

## 2. Kramers' Escape Rate Theory

### The Setup

Kramers (1940) studied a Brownian particle in a double-well potential, escaping from one minimum (reactant) to another (product) across an energy barrier.

The **overdamped** Kramers rate (relevant for SGD which is heavily damped):

```
k_escape = (ω_R · ω_bar) / (2π · ζ) × exp(−ΔE / k_B T)
```

Where:
- ω_R = √(U''(x_min)) = curvature at the starting minimum
- ω_bar = √(|U''(x_saddle)|) = curvature at the barrier
- ζ = friction coefficient (damping)
- ΔE = U(x_saddle) - U(x_min) = barrier height
- k_B T = thermal energy = noise intensity

The **escape time** is t = 1/k:

```
t_escape = (2π ζ) / (ω_R · ω_bar) × exp(ΔE / k_B T)
```

Taking logarithms:

```
ln(t_escape) = ΔE / (k_B T) + ln(2π ζ / (ω_R · ω_bar))
```

### Identifying the Components in Grokking

| Kramers | Grokking |
|---------|----------|
| Particle position x | Network weights W |
| Reactant minimum | Memorization state (high-norm, unstructured) |
| Product minimum | Fourier generalization state (low-norm, structured) |
| Potential U(x) | Loss landscape L(W) + (λ_WD/2)||W||² |
| Barrier ΔE | Energy barrier between memo and Fourier solutions |
| Temperature k_B T | SGD noise (from mini-batch stochasticity) |
| Friction ζ | Implicit in optimizer dynamics |

---

## 3. Three Candidate Mappings

### Mapping A: WD as Temperature

**Claim**: λ_WD acts as effective temperature T_eff = α · λ_WD

**Derivation**:
- Barrier ΔE ≈ ΔE_0 (approximately constant, structural property)
- T_eff = α · λ_WD
- Then: ln(t) = ΔE_0 / (α · λ_WD) + B = A / λ_WD + B ✓

**Physical argument**: Weight decay in AdamW acts as:
```
W_{t+1} = (1 - η·λ_WD) · W_t - η · ∇L
```

The multiplicative decay (1 - η·λ_WD) pushes weights toward zero. Combined with SGD noise, this creates an effective Ornstein-Uhlenbeck process. The equilibrium "temperature" of this process is:

```
T_eff = T_SGD / (1 - (1-η·λ_WD)²) ≈ T_SGD / (2η·λ_WD)   for small η·λ_WD
```

Wait — this gives T_eff ∝ 1/λ_WD (DECREASING with WD), not T_eff ∝ λ_WD.

**Problem**: The Ornstein-Uhlenbeck temperature argument gives the wrong direction. More WD = tighter confinement = LOWER effective temperature. But we need MORE WD = FASTER escape = HIGHER effective temperature.

**Resolution**: The OU analysis applies to the equilibrium distribution, not to the escape dynamics. Weight decay doesn't just change the noise level — it fundamentally reshapes the potential. The distinction matters.

### Mapping B: WD Reshapes the Barrier

**Claim**: λ_WD changes the barrier height ΔE(λ_WD)

**Derivation**: The total loss landscape is:
```
L_total(W) = L_task(W) + (λ_WD / 2) · ||W||²
```

The memorization solution has ||W_memo|| >> ||W_fourier|| (memorization requires large weights to encode each training example independently, while the Fourier solution uses compact structured weights).

The barrier modification:
```
ΔE(λ_WD) = ΔE(0) + (λ_WD/2)(||W_saddle||² - ||W_memo||²)
```

Since ||W_memo|| > ||W_saddle|| (the saddle is between two solutions, both with smaller norm than pure memorization), we get:

```
ΔE(λ_WD) = ΔE(0) - c · λ_WD    where c = (||W_memo||² - ||W_saddle||²)/2 > 0
```

The barrier DECREASES linearly with λ_WD. This gives:

```
ln(t) = (ΔE_0 - c·λ_WD) / T_SGD = ΔE_0/T_SGD - (c/T_SGD)·λ_WD
```

This is **LINEAR in λ_WD**, not Arrhenius (1/λ_WD). **Does not match the data.**

### Mapping C: WD Creates the Fourier Basin (Topology Change)

**Claim**: At λ_WD = 0, the Fourier minimum doesn't exist (or is infinitely shallow). WD creates it by changing the topology of the loss landscape.

**Derivation**: At λ_WD = 0:
- The loss landscape has the memorization solution as a global minimum
- There may be NO Fourier minimum at all (our data: WD=0 never groks, even after 500k epochs)
- The barrier is effectively infinite

At λ_WD > 0:
- The weight penalty raises the memorization basin (high ||W||)
- A new Fourier basin appears (low ||W||)
- The barrier between them is finite

If the barrier scales as:
```
ΔE(λ_WD) = A' / λ_WD   (barrier diverges as WD → 0)
```

Then: ln(t) = A' / (T_SGD · λ_WD) + B = A / λ_WD + B ✓

**When would ΔE ∝ 1/λ_WD?**

Consider: at λ_WD = 0, the Fourier basin doesn't exist. As λ_WD increases from 0, the Fourier basin appears and deepens. The barrier height is the difference between the saddle energy and the memorization energy.

The saddle energy (landscape maximum between the two basins) depends on how much WD has reshaped the landscape. Near the critical point where the Fourier basin just appears:

The Fourier minimum energy: E_fourier ≈ (λ_WD/2) · ||W_fourier||²  (small)
The memo minimum energy: E_memo ≈ (λ_WD/2) · ||W_memo||²  (large)
The saddle energy: E_saddle depends on the landscape geometry

In a simple double-well model where WD tilts the landscape:
```
U(x) = x⁴/4 - x²/2 - h·x
```

where h ∝ λ_WD is the "tilt" (WD favoring the low-norm basin), the barrier height near h=0 scales as:

```
ΔE ∝ (something) - h^(3/2) for small h
```

This is the standard scaling for first-order transitions near the spinodal, NOT 1/h.

**For ΔE ∝ 1/λ_WD**, we need a different mechanism. One possibility: the barrier is NOT between the memo and Fourier basins directly, but involves a third mechanism (e.g., a saddle in weight space that requires coordinated changes in embeddings + hidden layers).

---

## 4. The Most Honest Assessment

None of the three mappings cleanly derives the Arrhenius form from first principles.

- **Mapping A** (WD as temperature): Gets the functional form but the physical argument is shaky — the OU equilibrium temperature goes the wrong way.
- **Mapping B** (WD modifies barrier linearly): Gives the wrong functional form (linear, not 1/λ).
- **Mapping C** (WD creates the basin, ΔE ∝ 1/λ): Gets the functional form but the 1/λ scaling is assumed, not derived.

### What We Can Say Rigorously

1. The Arrhenius form ln(t) = A/λ_WD + B is empirically robust (R² = 0.976, 5 conditions).
2. This is **consistent with** Kramers escape theory if the effective barrier/temperature ratio scales as 1/λ_WD.
3. The Arrhenius form rules out **critical slowing** (second-order), which would give power-law scaling: t ∝ λ_WD^{-z}.
4. The barrier crossing mechanism is supported by the quasi-deterministic timing (CV = 0.14-0.21, not the CV ≈ 1 expected for stochastic nucleation).
5. The WD=0 case (never groks) is consistent with an infinite effective barrier at λ_WD = 0.

### A Testable Prediction

If the Arrhenius scaling comes from T_eff ∝ λ_WD (Mapping A), then:
- The slope A = ΔE_0 / α depends on the structural barrier ΔE_0 and the proportionality constant α
- Changing the learning rate should change the SGD noise component without changing the barrier
- Therefore: the Arrhenius slope should be INDEPENDENT of learning rate (the barrier is structural)

If instead the Arrhenius scaling comes from ΔE ∝ 1/λ_WD (Mapping C), then:
- The slope A = A' / T_SGD
- Changing learning rate (which changes T_SGD) SHOULD change the slope
- Specifically: slope × T_SGD should be constant

**These two predictions are experimentally distinguishable.** Run the Arrhenius sweep at different learning rates and see whether the slope changes.

---

## 5. Connection to the Black Hole Paper (2506.07074)

Relevant methodological insight: they apply Kramers theory to first-order transitions in multi-critical systems (black holes with coexisting phases), showing that escape rate cycles precisely delimit phase transition regimes.

Key formula from their work:
```
K_{e-r} = D · √(|U''(x_max) · U''(x_min)|) / (2π k_B T) × exp(-(U_max - U_min) / k_B T)
```

where D = k_B T / γ (Einstein relation), U is the Gibbs free energy.

For our setting, U = L_total(W) (total loss including WD penalty), and the "reaction coordinate" is a path through weight space from memorization to Fourier solution.

The pre-exponential factor depends on curvatures at the minimum and saddle — these are Hessian eigenvalues of the loss landscape, which are in principle computable. The multi-task grokking paper (Feb 2026) actually computes Hessian eigenvalues during grokking, finding deep curvature at high WD (λ_min ≈ -63) and shallow curvature at low WD (λ_min ≈ -17). This curvature data could be used to test whether the Kramers pre-factor matches the observed escape times.

---

## 6. What to Put in the Manuscript

### Claim (stated honestly)

> "The Arrhenius scaling of grokking time with weight decay strength (ln(t_grok) = A/λ_WD + B, R² = 0.976) is the kinetic signature of barrier-crossing dynamics, consistent with Kramers' escape rate theory in the overdamped regime. The effective barrier height diverges as λ_WD → 0, consistent with the observation that WD=0 never produces grokking. The exact mechanism by which weight decay enters the barrier/temperature ratio — whether as an effective temperature or through barrier topology modification — remains an open question that is experimentally distinguishable via Arrhenius sweeps at different learning rates."

This is honest, substantive, and generates a testable prediction. It doesn't overclaim a derivation we don't have.

---

## 7. References

- Kramers, H. A. (1940). Brownian motion in a field of force and the diffusion model of chemical reactions. Physica, 7(4), 284-304.
- Hänggi, P., Talkner, P., & Borkovec, M. (1990). Reaction-rate theory: fifty years after Kramers. Reviews of Modern Physics, 62(2), 251. https://doi.org/10.1103/RevModPhys.62.251
- Pollak, E. (2023). Recent Developments in Kramers' Theory of Reaction Rates. ChemPhysChem, e202300272. https://doi.org/10.1002/cphc.202300272
- [Authors] (2025). Overcoming Barriers: Kramers' Escape Rate Analysis of Metastable Dynamics in First-Order Multi-Phase Transitions. arXiv:2506.07074.
