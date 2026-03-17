# EPT Theorem Development — Working Document

**Date**: 2026-03-16
**Status**: T4 experiment completed — results analyzed with self-critique

---

## Current State of the Theory

The EPT manuscript (v3) has:
- A Hopfield-like CTRNN: τ ds/dt = -s + tanh(Ws + u + ξ)
- Crystal/Glass decomposition: W = g_task V_task V_task^T + g_glass V_glass V_glass^T
- Energy: E(s) = -½ s^T W s - u^T s (symmetric case)
- Order parameters: Ψ (velocity), F (alignment)
- Four empirical controls confirming hysteresis, Arrhenius, velocity spikes

What's missing: **formal theorems connecting the model to the empirical signatures.** The model is illustrative, not predictive. Adding theorems makes it predictive — the empirical results become confirmations rather than standalone observations.

---

## Theorem 1: Hysteresis Conditions in the Crystal/Glass Model

### The Physics

Hysteresis means: the forward transition (glass → crystal) requires a seed, but the reverse transition (crystal → glass) does not occur when the seed is removed. This happens when:
- The crystal is a **local** minimum of the energy landscape (stable without seed)
- The glass is the **global** minimum (preferred from random initialization)
- The seed temporarily makes the crystal basin accessible
- After seed removal, the system remains in the crystal basin

### The Math

**Setup**: Consider the continuous Hopfield model with k=1 task direction and p glass patterns. Let V_task = v_c (a single unit vector) and V_glass = [v_1, ..., v_p] (p orthonormal vectors, all orthogonal to v_c).

The connectivity is:
W = g_c v_c v_c^T + g_g Σ_j v_j v_j^T

For the Hopfield model with tanh activation, a pattern v becomes an attractor when the gain exceeds the leak threshold. Projecting onto the pattern direction, the self-consistency equation for the overlap m = v^T s is:

m = tanh(g · m)

This has:
- Only the trivial solution m = 0 when g ≤ 1
- Three solutions (0, ±m*) when g > 1, where m* = tanh(g · m*) > 0

The nontrivial solution m* exists and is stable when g > 1. The energy at this fixed point (within the pattern subspace) is approximately:

E(m*) ≈ -½ g · (m*)² + [entropic/nonlinear correction]

### Statement

**Proposition 1 (Bistability)**: For the Crystal/Glass model with g_c > 1, g_g > 1, and V_task ⊥ V_glass:

(a) The crystal state s_c* with overlap m_c* = tanh(g_c m_c*) along v_c is a **stable fixed point** of the noiseless dynamics.

(b) Each glass state s_j* with overlap m_g* = tanh(g_g m_g*) along v_j is a **stable fixed point**.

(c) Both types of fixed points coexist for all g_c > 1, g_g > 1, regardless of their relative magnitude.

**Proposition 2 (Hysteresis)**: When g_g > g_c > 1:

(a) The glass states are the **global energy minima** (deeper basins).

(b) From random initialization (s ≈ 0), the system falls into a glass basin with probability → 1 as p → ∞ (entropic dominance: p glass attractors vs 1 crystal attractor).

(c) A seed u = s_seed · v_c applied for duration T_seed > T_crit (computable) pushes the system into the crystal basin.

(d) After seed removal (u → 0), the crystal state remains stable — the system does not return to glass.

(e) Therefore, the forward transition (glass → crystal) requires the seed, but the reverse transition does not occur spontaneously. This is **classical hysteresis**.

### Proof Sketch for (a)-(d)

**(a)** The energy at a glass state is E_g = -½ g_g (m_g*)². The energy at the crystal state is E_c = -½ g_c (m_c*)². Since g_g > g_c and m* is monotonically increasing in g (for g > 1), we have E_g < E_c. Glass is deeper.

**(b)** Near s = 0, the linearized dynamics are ds/dt = (W - I)s. The eigenvalues of W - I are (g_c - 1) along v_c and (g_g - 1) along each v_j. The fastest-growing direction is v_j (since g_g > g_c), and there are p such directions vs 1 crystal direction. By a counting argument (volume of basins of attraction), the probability of falling into a glass basin is p/(p+1) → 1.

**(c)** With seed u = s_seed · v_c, the dynamics along v_c become:
dm_c/dt = -m_c + tanh(g_c m_c + s_seed)

The seed shifts the effective "field" along v_c, making the crystal direction preferred. For s_seed > s_crit (computable from the tanh self-consistency), the crystal becomes the unique stable state along v_c.

**(d)** After seed removal, the crystal fixed point m_c* still satisfies m_c* = tanh(g_c m_c*) with g_c > 1. The fixed point exists independently of the seed. The seed is needed to **reach** the crystal basin, not to **maintain** it.

### What This Proves

This proves hysteresis is a **necessary consequence** of the Crystal/Glass model with g_g > g_c > 1. It's not an accidental feature of the simulation — it's guaranteed by the mathematics.

### What This Does NOT Prove

- Does not prove hysteresis for the actual grokking system (which has different dynamics)
- Requires orthogonality assumption (V_task ⊥ V_glass) — real systems have correlations
- The Hopfield model is symmetric; real networks are not
- The correspondence between g_c/g_g and weight decay is informal

### Critique

The proposition is correct but unsurprising — it's essentially restating well-known Hopfield physics in the Crystal/Glass language. What makes it valuable is: (1) connecting it explicitly to the hysteresis signature that no competing paper tests, and (2) providing the computable critical seed strength s_crit and duration T_crit.

**Enhancement**: Compute s_crit and T_crit explicitly in terms of g_c, g_g, p. This gives a **quantitative prediction** about how strong and how long the seed must be.

---

## Theorem 2: Kramers' Escape Rate → Arrhenius Kinetics

### The Physics

The system starts in a glass basin (memorization). Noise (from SGD) enables stochastic barrier crossing to the crystal basin (generalization). The mean escape time follows Kramers' theory. The question is: what role does weight decay play?

### Two Competing Interpretations

**Interpretation A: WD as temperature.**

Weight decay provides the effective fluctuation energy for barrier crossing. SGD noise alone is insufficient to cross the barrier; weight decay adds a systematic bias toward low-norm states that effectively increases the "thermal exploration" of the landscape.

In this picture:
- Barrier height ΔE is approximately constant (structural property of the landscape)
- Effective temperature T_eff ∝ λ_WD
- Kramers: t ∝ exp(ΔE / T_eff) = exp(ΔE / (α · λ_WD)) = exp(A / λ_WD)
- This gives: ln(t) = A / λ_WD + B ← **matches the data**

**Interpretation B: WD modifies barrier height.**

Weight decay reshapes the loss landscape, lowering the barrier between memorization and generalization.

In this picture:
- Barrier height ΔE(λ_WD) = ΔE_0 - c · λ_WD (barrier decreases linearly)
- Temperature T is fixed (SGD noise)
- Kramers: t ∝ exp(ΔE(λ_WD) / T) = exp((ΔE_0 - c · λ_WD) / T)
- This gives: ln(t) = ΔE_0/T - (c/T) · λ_WD + const ← **LINEAR in λ_WD, not 1/λ_WD**
- **Does NOT match the data**

**Interpretation C: WD creates the crystal basin.**

At λ_WD = 0, the crystal minimum does not exist (or is infinitely shallow). Weight decay creates it. The barrier height is not just modified — the entire landscape topology changes.

In this picture:
- At λ_WD = 0: only glass minimum exists, barrier is infinite → never groks ✓
- At λ_WD > 0: crystal minimum appears, barrier is finite
- The barrier could scale as ΔE ∝ 1/λ_WD if the crystal minimum's depth grows slowly
- Combined with fixed SGD noise: ln(t) = A / λ_WD + B ✓

### Statement

**Proposition 3 (Arrhenius from Kramers)**: Consider the Crystal/Glass model with additive noise ξ of intensity D. Let ΔE(λ) denote the energy barrier between the glass minimum and the nearest saddle point leading to the crystal basin, parameterized by a control parameter λ (analogous to weight decay).

If the effective barrier satisfies ΔE(λ) = A/λ for some constant A > 0 (the barrier diverges as λ → 0), then the mean first-passage time from glass to crystal follows:

> τ_escape = (2π / √(ω_min · |ω_saddle|)) · exp(A / (D · λ))

Taking logarithms:

> ln(τ_escape) = A / (D · λ) + ln(2π / √(ω_min · |ω_saddle|))

which is the Arrhenius form ln(t) = A' / λ + B.

**Corollary**: If λ corresponds to weight decay strength and D to SGD noise intensity:
- At λ = 0: τ_escape → ∞ (the system never escapes memorization)
- At λ > 0: τ_escape is finite and decreases exponentially with λ
- The fit parameter A' = A/D encodes both the barrier structure and the noise level

### What Remains to Show

The proposition above is essentially applying Kramers' formula (well-established). The non-trivial part is showing that ΔE ∝ 1/λ in the Crystal/Glass model. This requires:

1. Computing the barrier height explicitly in the Crystal/Glass energy landscape
2. Introducing the weight-decay-like parameter into the energy
3. Showing the scaling

**Approach**: In the Crystal/Glass model, weight decay maps to a modification of the energy:

E_WD(s) = E(s) + (λ/2) ||s||²

This adds a quadratic penalty favoring small ||s||. The memorization state has large ||s|| (all glass patterns active), while the crystal state has small ||s|| (concentrated in k ≪ p dimensions).

The barrier height is:
ΔE(λ) = E_WD(s_saddle) - E_WD(s_glass)

The glass minimum energy shifts as: E_glass → E_glass + (λ/2)||s_glass||²
The saddle energy shifts as: E_saddle → E_saddle + (λ/2)||s_saddle||²

So: ΔE(λ) = ΔE(0) + (λ/2)(||s_saddle||² - ||s_glass||²)

If ||s_glass|| > ||s_saddle|| (glass state has larger norm — which should be true since it uses p patterns while the saddle is a hybrid state), then the barrier DECREASES linearly with λ. This gives:

ln(t) = (ΔE_0 + c·λ) / D ← linear in λ, not 1/λ

**Problem**: This gives the wrong functional form! The linear barrier reduction gives ln(t) linear in λ, but the data shows ln(t) ∝ 1/λ.

### Resolution: WD as Effective Temperature

The Arrhenius form ln(t) = A/λ_WD is consistent with Kramers' theory if we identify:

**T_eff ∝ λ_WD** (weight decay acts as effective temperature)

This is physically reasonable: weight decay in SGD acts as a restoring force toward zero, which in the stochastic dynamics of SGD effectively INCREASES the exploration of the loss landscape. The combination of SGD noise + weight decay is more effective at exploring state space than SGD noise alone, and the effective temperature increases with λ_WD.

More precisely, in the SGD dynamics with weight decay:

W_{t+1} = (1 - η λ_WD) W_t - η ∇L(W_t) + noise

The term (1 - η λ_WD) W_t acts like a friction/restoring force. In the Langevin dynamics analogy, the noise-to-damping ratio determines the effective temperature. Weight decay increases the damping, and in the overdamped regime, the effective temperature is:

T_eff = T_SGD / (1 + c · λ_WD)

Wait, that gives T_eff DECREASING with λ_WD — the opposite of what we need.

**Alternative**: Weight decay narrows the basin of attraction of the memorization state. The effective barrier, measured relative to the typical fluctuation amplitude at the glass minimum, becomes:

ΔE_eff / T_SGD = (ΔE_0 · (1 - α λ_WD)) / T_SGD

For small λ_WD: if ΔE_0 / (α λ_WD) ≫ 1, this doesn't give Arrhenius either.

**Honest assessment**: Deriving the exact Arrhenius scaling from the Crystal/Glass model is harder than it initially appears. The 1/λ_WD form is not straightforward from Kramers + linear barrier modification. The most honest statement may be:

> "The Arrhenius form ln(t) = A/λ_WD is consistent with Kramers escape theory if weight decay acts as an effective temperature for barrier crossing. The exact mechanism by which weight decay provides effective thermal energy in the SGD dynamics is an open question at the intersection of stochastic optimization theory and statistical physics."

### Critique

This theorem is weaker than initially hoped. We can state the Kramers framework clearly and show it explains the functional form IF we accept that T_eff ∝ λ_WD. But deriving this proportionality from first principles in the SGD setting is a research problem in its own right.

**However**: Nobody else even attempts to explain the Arrhenius scaling. Even a conditional theorem (IF T_eff ∝ λ_WD THEN Arrhenius) is valuable because it:
1. Identifies the mechanism (barrier crossing, not critical slowing)
2. Predicts the functional form
3. Explains why WD=0 never groks (T_eff → 0, infinite escape time)
4. Makes a testable prediction: the slope A should change if you change the SGD noise level (learning rate, batch size)

**Testable prediction**: If the Kramers/temperature interpretation is correct, then:
- Increasing learning rate (more SGD noise) should DECREASE the slope A' = A/D
- The PRODUCT (learning_rate × slope) should be approximately constant across lr values
- This is testable with existing infrastructure!

---

## Theorem 3: Velocity Spike at Barrier Crossing

### The Physics

When the system crosses the energy barrier between glass and crystal, it passes through or near a saddle point. At the saddle, the energy surface is concave in the escape direction — the system accelerates. This produces a velocity spike.

### The Math

**Setup**: Consider the gradient descent dynamics on the energy landscape:

ds/dt = -∇E(s)

Near a saddle point s_saddle, expand E to second order:

E(s) ≈ E(s_saddle) + ½ (s - s_saddle)^T H (s - s_saddle)

where H = ∇²E|_{s_saddle} is the Hessian. At a saddle with one unstable direction, H has one negative eigenvalue -|μ| and (N-1) positive eigenvalues.

Along the unstable direction e_1 (eigenvector of -|μ|):

ds₁/dt = -∂E/∂s₁ = |μ| · s₁

This gives exponential acceleration: s₁(t) = s₁(0) · exp(|μ| · t)

The velocity along this direction is:

|ds₁/dt| = |μ| · |s₁(0)| · exp(|μ| · t)

### Statement

**Proposition 4 (Velocity Spike)**: For the dynamics ds/dt = -∇E(s), a trajectory that passes through a neighborhood of a saddle point s_saddle with Hessian eigenvalues {-|μ|, λ₂, ..., λ_N} (μ > 0, λ_i > 0) exhibits:

(a) A velocity spike with peak amplitude scaling as:

> Ψ_peak ∝ √(|μ|) · √(ΔE)

where ΔE is the energy difference between the initial state and the saddle.

(b) The spike duration (FWHM) scales as:

> T_spike ∝ 1 / √(|μ|)

(c) The velocity minimum BEFORE the spike (while trapped in the glass basin) scales as:

> Ψ_base ∝ noise_amplitude

(d) Therefore, the signal-to-noise ratio of the spike is:

> SNR ∝ √(|μ| · ΔE) / noise_amplitude

### Proof Sketch

Consider a 1D reduction along the unstable direction. The effective potential is:
V(x) = -½ |μ| x² (near the saddle, for small x)

With initial condition x(0) = ε (small perturbation from saddle):
x(t) = ε · exp(|μ| t)

Speed: |ẋ| = |μ| · ε · exp(|μ| t)

The trajectory leaves the saddle region when the quadratic approximation breaks down, at x ~ x_max where higher-order terms matter. At this point:
|ẋ|_max ~ |μ| · x_max

After crossing the saddle, the trajectory falls into the crystal basin and decelerates. The peak velocity occurs during the descent from saddle to crystal minimum.

For a trajectory starting at energy ΔE above the saddle (i.e., at the top of the glass basin wall):
½ |ẋ|² ≈ ΔE (energy conservation, neglecting damping in the fast-crossing regime)
|ẋ|_peak ≈ √(2 ΔE)

The spike duration is set by the time to cross the saddle region (width ~ 1/√|μ|):
T_spike ~ 1/√|μ|

### What This Adds

1. **Velocity spike is NECESSARY, not coincidental**: any barrier crossing through a saddle produces one.
2. **Spike amplitude is predictable** from barrier height and saddle curvature.
3. **Spike duration is predictable** from saddle curvature alone.
4. **The spike is localized** to a fraction of total dynamics — consistent with the empirical observation of <1% of training time.

### Empirical Connection

In grokking:
- The velocity spike spans ~40 epochs out of ~2000 (2% of training) — consistent with T_spike ≪ T_total
- The spike is large relative to baseline — consistent with high SNR prediction
- The spike occurs at the onset of generalization — consistent with saddle crossing

### Critique

This is largely textbook dynamical systems theory (saddle-point escape). The novelty is in:
1. Connecting it explicitly to the "aha moment" / insight phenomenology
2. Making quantitative predictions about spike amplitude and duration
3. Providing a mechanism that's **independent of the specific model** — any energy landscape with barrier crossing produces this signature

---

## Theorem 4: Architecture Depth Determines Transition Order

### The Big Question

Žunkovič & Ilievski (JMLR 2025) find **second-order** transitions in perceptrons.
Our EPT finds **first-order** transitions in deep MLPs.
Nareddy et al. (ICLR 2024) find first-order in two-layer networks.

Why does depth matter?

### The Key Insight

In a perceptron (single layer), there is ONE degree of freedom: the classifier direction w.

The transition from memorization to generalization is a **continuous rotation** of w from a data-fitting direction to the true discriminant direction. There's no barrier — just a smooth path. The transition is continuous (second-order).

In a deep network, there are TWO coupled degrees of freedom:
1. The hidden representation W_1 (features)
2. The classifier W_2 (mapping from features to output)

The transition requires BOTH to change simultaneously. But the intermediate state — new features with old classifier, or old features with new classifier — is **worse** than either pure state. This creates an **energy barrier**.

### Formal Setup

**Single-layer (perceptron)**:
- Parameters: w ∈ R^d
- Loss: L(w) = Σ_i ℓ(y_i, w^T x_i) + regularization
- The path from w_memo to w_gen is continuous in parameter space
- Along this path, the loss may increase locally but there's no topological barrier
- Critical exponent = 1 (Žunkovič: E(t) ∝ (t_ε - t), linear vanishing)

**Two-layer (deep)**:
- Parameters: (W_1, W_2) where W_1 ∈ R^{d×h}, W_2 ∈ R^{h×c}
- Output: f(x) = W_2 · σ(W_1 · x)
- The memorization solution: (W_1^memo, W_2^memo) with large ||W|| and unstructured features
- The generalization solution: (W_1^gen, W_2^gen) with small ||W|| and structured (e.g., Fourier) features

The key: the output is a PRODUCT of the two layers. The transition requires a coordinated change in both W_1 and W_2.

### The Barrier Argument

Consider interpolating between the two solutions:
(W_1(α), W_2(α)) = ((1-α) W_1^memo + α W_1^gen, (1-α) W_2^memo + α W_2^gen)

The loss along this path is:
L(α) = Σ_i ℓ(y_i, W_2(α) · σ(W_1(α) · x_i))

Due to the nonlinear interaction (σ and the product structure), L(α) is NOT a convex interpolation of L(0) and L(1). In fact:

At α = 0.5 (halfway):
- W_1(0.5) has NEITHER the memorization patterns NOR the generalization features
- W_2(0.5) is mismatched with both
- The output is garbled
- L(0.5) > max(L(0), L(1))

This is the **loss barrier**: the intermediate state is worse than either endpoint. This barrier is what makes the transition first-order.

### Statement

**Proposition 5 (Depth Creates Barriers)**: Consider a learning system parameterized by θ = (θ_features, θ_classifier).

(a) If the output is LINEAR in θ (single-layer): f(x; θ) = θ^T φ(x) for fixed features φ, then the loss is convex in θ and the transition from any minimum to any other minimum is barrier-free (second-order character).

(b) If the output involves a PRODUCT of parameters (deep network): f(x; θ) = θ_2 · g(θ_1, x), and the generalization solution requires a **different** θ_1 from the memorization solution, then the loss along any linear interpolation path has a barrier:

> max_{α ∈ [0,1]} L(α) > max(L(0), L(1))

whenever g(·, x) is nonlinear and the features θ_1^memo ≠ θ_1^gen.

(c) This barrier implies:
- The transition is discontinuous (must "jump" over the barrier)
- The transition exhibits hysteresis (barrier prevents reverse transition)
- The transition timing follows Kramers/Arrhenius kinetics (barrier crossing)
- These are the signatures of a **first-order** phase transition

**Corollary (Architecture determines order)**: Perceptrons (linear in parameters) exhibit second-order transitions. Deep networks (products of parameters with feature learning) exhibit first-order transitions. The critical ingredient is **whether the features must change during the transition**.

### Proof Sketch for (b)

Let f(x; α) = W_2(α) · σ(W_1(α) · x) where W_i(α) = (1-α) W_i^0 + α W_i^1.

Expand around α = 0.5:
f(x; 0.5) = ½(W_2^0 + W_2^1) · σ(½(W_1^0 + W_1^1) · x)

If σ is ReLU or tanh, then σ(½(a + b)) ≠ ½(σ(a) + σ(b)) in general (Jensen's inequality for concave/convex σ).

The output at α = 0.5 is NOT the average of the outputs at α = 0 and α = 1. The nonlinearity creates a "mismatch" between the halfway features and both endpoints' classifiers.

For the loss: if L is convex in the output (e.g., cross-entropy, MSE), then:
L(f(x; 0.5)) is determined by the mismatched output.

To show L(0.5) > max(L(0), L(1)), we need the mismatch to be severe enough. This holds when:
1. The memorization features are **orthogonal** to the generalization features (||W_1^0 - W_1^1|| is large)
2. The classifiers are adapted to their respective features (W_2^0 is optimal for W_1^0, etc.)
3. The nonlinearity σ is sufficiently nonlinear

Under these conditions, the halfway point garbles both the features and the classifier-feature alignment, producing high loss.

### What This Proves

This would be the first formal argument explaining why grokking in deep networks is first-order while in perceptrons it's second-order. The mechanism is clear: **parameter coupling through nonlinearity creates barriers**.

### What This Does NOT Prove

- The argument is about linear interpolation paths — the true transition path could avoid the barrier (geodesic through parameter space). However, if ALL linear paths have barriers, the minimum barrier over all paths is still positive.
- The proposition assumes the features must change. If a deep network can grok by only adjusting the classifier (no feature change), the transition could be second-order even in a deep network.
- The Riemannian geometry of the loss landscape matters — the "natural" metric for parameter space is not Euclidean.

### Critique

This is the most ambitious theorem and the least rigorous. The linear interpolation argument is suggestive but not definitive — the actual SGD trajectory could take a different path. The strongest version would show that ALL paths between memorization and generalization cross a barrier, but that requires understanding the full topology of the loss landscape.

**However**: the argument is physically compelling and explains a pattern in the literature that nobody else has addressed. Even as a "proposition" (not a full theorem), it provides theoretical grounding for the empirical observation.

---

## Summary: What to Add to the Manuscript

### Recommended additions (in order of strength)

| Theorem | Rigor | Impact | Recommendation |
|---------|-------|--------|----------------|
| T1: Hysteresis in Crystal/Glass | High — Hopfield math is standard | HIGH — directly supports crown jewel | **Include as Proposition 1 in Theory section** |
| T3: Velocity spike at saddle | High — textbook dynamical systems | Medium — formalizes intuition | **Include as Proposition 2** |
| T2: Kramers → Arrhenius | Medium — requires WD-as-temperature assumption | HIGH — explains R²=0.976 | **Include as Proposition 3 with stated assumption** |
| T4: Depth → transition order | Lower — interpolation argument, not full proof | VERY HIGH — explains JMLR contrast | **Include as Proposition 4 (conjecture) with supporting argument** |

### Testable predictions generated by the theorems

1. **From T1**: The critical seed strength s_crit = f(g_c, g_g) is computable. For grokking: there should be a minimum λ_WD below which grokking time diverges super-exponentially (not just Arrhenius). Testable with a fine WD sweep near the boundary.

2. **From T2**: If T_eff ∝ λ_WD, then changing the SGD learning rate (which changes D) should change the Arrhenius slope A' = A/D. Specifically: A' × lr should be approximately constant. **Testable with existing code**.

3. **From T3**: The velocity spike duration should scale as 1/√|μ| where μ is the saddle curvature. Measurable by comparing spike duration across different WD values (which change the saddle curvature).

4. **From T4**: A single-layer network (linear classifier on fixed features) should show second-order grokking (no hysteresis, no Arrhenius, continuous transition). **Directly testable**: freeze W_1 after memorization, let only W_2 train with weight decay.

Prediction 4 is particularly powerful because it's falsifiable and nobody has tested it.

---

## T4 Experiment: Results and Self-Critique

### Experiment run: 2026-03-16, 8.1 hours, 5 seeds

**Code**: `/storage/EPT/ept_definitive/test_t4_depth_order.py`
**Results**: `/storage/EPT/ept_definitive/results/t4_depth_order/`

### Raw Results

| Condition | Grok Rate | Mean t_grok | Sharpness (20%→80%) | Hysteresis (5/5 persist?) |
|-----------|-----------|-------------|---------------------|---------------------------|
| **FULL** (all params) | 5/5 | 37,120 | ~2,100 epochs | 4/5 |
| **FROZEN_FEATURES** (output only, memo features) | 0/5 | never (200k) | — | — |
| **RESET_OUTPUT** (output only, grokked features) | 5/5 | 100 | 0 | 5/5 |

Per-seed FULL grokking times: 28700, 39000, 41000, 28600, 47300

### Critical Self-Evaluation

**The RESET_OUTPUT "hysteresis" is vacuous and should NOT be cited as evidence.**

At the very first eval (epoch 100), RESET_OUTPUT already shows train=1.0, test=1.0. There is:
- No memorization phase
- No delayed generalization
- No grokking
- No transition of any kind

It's trivially fast convergence of a convex problem: a 128→97 linear layer on perfect Fourier features. The "hysteresis test" (remove WD, accuracy persists) is meaningless because:
1. Features are frozen by design — they cannot degrade
2. The output layer found the unique optimal linear mapping — there's no competing attractor
3. Removing WD from a converged convex solution does nothing

**Calling this "first-order" or "hysteretic" is an error.** It's like testing whether a solved jigsaw puzzle falls apart when you stop looking at it.

**The FROZEN_FEATURES result is uninformative about transition order.**

FROZEN_FEATURES ran for 200,000 epochs at train=1.0, test=0.03% throughout. The memorized features contain zero generalizable structure. This tells us the features ARE the bottleneck, but says nothing about what KIND of transition a learnable shallow model would show.

**The experiment does NOT test T4's actual prediction.**

T4 predicts: "a system with one learnable layer shows second-order transitions." The JMLR perceptrons are LEARNING — adjusting their weights to generalize. Our experiment tested:
- Fixed bad features + learnable classifier → can't generalize (uninformative)
- Fixed good features + learnable classifier → trivially solves (vacuous)

Neither replicates the JMLR setting of a shallow model learning from scratch.

### What We DID Learn (Genuinely Valuable)

**Finding: The phase transition barrier lives entirely in feature space.**

Evidence:
- Memorized features + 200k epochs of classifier training → 0% generalization
- Fourier features + 100 epochs of classifier training → 100% generalization
- Full network grokking takes 37,000 epochs — this delay is 100% feature reorganization
- The output layer adaptation is trivial (~100 epochs) once features are correct

This is a clean decomposition result: **grokking = slow feature transition + trivial classifier fit**. The 37,000-epoch delay, the velocity spike, the Arrhenius kinetics — these are all properties of the embedding/hidden-layer reorganization from memorization to Fourier structure. The output layer is a spectator.

### Revised Proposition 5

The original Proposition 5 (Depth Creates Barriers) survives in spirit but the experimental support must be reframed:

**Revised statement**: The first-order character of grokking in deep networks arises from the feature-space barrier between memorization and generalization representations. The output layer contributes no barrier and adapts trivially. In systems without feature learning (perceptrons), no such barrier exists, predicting second-order transitions — consistent with Žunkovič & Ilievski (JMLR 2025).

**Evidence**:
- (Indirect) FROZEN_FEATURES: memorized features are completely uninformative for generalization, confirming that the features must change entirely (large barrier)
- (Indirect) RESET_OUTPUT: Fourier features make the classifier problem trivial, confirming the barrier is in feature space, not classifier space
- (External) Žunkovič & Ilievski (2025): perceptrons show second-order transitions (no feature barrier)
- (Not yet tested) Direct comparison of 1-layer vs 2-layer grokking on the same task

### What a Proper T4 Test Would Look Like

**Option A**: Train a genuine single-layer model (no hidden layers, just embed_a + embed_b → output) on (a+b) mod 97. The embeddings can learn, but there's no hidden computation. Does it grok? If yes, measure transition sharpness and hysteresis.

**Option B**: Compare 1-hidden-layer vs 2-hidden-layer vs 4-hidden-layer on the same task. If T4 is correct, deeper models should show sharper transitions and stronger hysteresis.

**Option C**: Use the JMLR paper's exact setup (perceptron on Rule 30) and measure hysteresis directly. If their second-order claim is correct, there should be no hysteresis.

These remain as future work. The current experiment's main contribution is the feature-space localization finding.

---

## Open Questions

1. Can Theorem 1 be extended to the non-symmetric case (asymmetric W)? The dynamics are no longer gradient descent on an energy landscape, but the velocity spike argument (T3) applies via the Jacobian spectrum.

2. Can the barrier height in T4 be computed explicitly for the mod-97 MLP? This would give a quantitative prediction for the Arrhenius slope.

3. Is there a connection between our F_task (Rayleigh quotient) and the LLC (Local Learning Coefficient) from Singular Learning Theory? If so, the SLT paper's results could strengthen our framework.

4. The JMLR paper finds critical exponent = 1 for perceptrons. Does our deep network show a different exponent? Measuring the exponent (how fast test accuracy rises at the transition) would provide additional evidence for the first-order vs second-order distinction.

5. **NEW (from T4 experiment)**: Can the feature-space barrier height be estimated from the embedding distance ||E_memo - E_fourier||? If so, this predicts grokking time independently of the Arrhenius fit — a cross-validation of the barrier-crossing mechanism.

6. **NEW**: Seed 4's hysteresis dip (min_test=0.896 before recovery to 1.0) suggests the crystal basin depth varies across seeds. Does basin depth correlate with grokking time or Fourier concentration (IPR)?
