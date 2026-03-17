# EPT Human Experiment: Artificial Grammar Learning with Phase-Transition Diagnostics

**Paper 3 — Human validation of Epistemic Phase Transitions**

## Background & Rationale

The EPT framework predicts that genuine insight (the "aha moment") is a first-order phase
transition: discontinuous, irreversible (hysteretic), and parameter-dependent. Papers 1-2
validate this in neural networks (grokking) and dictionary learning. This experiment tests
whether the same (Ψ, F) signatures appear in human learning.

**Why AGL?** Artificial Grammar Learning is the ideal paradigm because:
- The "correct structure" (grammar) is known a priori → F_task is computable
- Some subjects learn suddenly, others gradually → natural variation
- Trial-by-trial behavioral data (RT, accuracy) is standard
- Well-established methodology with 40+ years of literature
- Domain-agnostic: no prior knowledge advantage
- Web-deployable: works for all recruitment channels

**Key prior work:**
- Reber (1967): Original AGL paradigm
- ENIGMA tool (Chen et al., 2024): Web-based AGL platform
- Reinforcement waves (Rosenberg et al., PNAS 2022): Discontinuous learning with
  quantitative theory — showed "aha" moments in maze learning follow from RL dynamics

## Design Overview

### Participants
- **Target N**: 120 total (40 per grammar difficulty condition)
- **Recruitment**: 4 channels
  - (a) Students in instructor's class (extra credit)
  - (b) Students from other classes (recruitment flyer)
  - (c) General university students
  - (d) Online via Prolific
- **Inclusion**: Age 18+, fluent English, normal/corrected vision
- **Exclusion**: Prior participation in AGL studies, linguistics majors
- **Compensation**: Extra credit (a), $10 gift card (b,c), $8 Prolific payment (d)

### Task: Artificial Grammar Learning with Adaptive Difficulty

Participants view letter strings and classify them as "grammatical" or "ungrammatical."
Feedback is provided during the learning phase and removed during the transfer/hysteresis test.

**Grammars**: Three finite-state automata (FSA) of increasing complexity:
- **Easy** (3-state): ~70% of participants expected to reach criterion
- **Medium** (5-state): ~40-50% expected to reach criterion (sweet spot)
- **Hard** (7-state): ~15-20% expected to reach criterion

**Between-subjects design**: Each participant is assigned ONE grammar difficulty.
This is the "dose" — analogous to weight decay strength in grokking.

**Within-subjects phases** (30-40 minutes total):

| Phase | Duration | Trials | Feedback | Purpose |
|-------|----------|--------|----------|---------|
| 1. Familiarization | 3 min | 20 | YES (correct/incorrect) | Calibrate baseline, learn interface |
| 2. Main learning | 15 min | ~100 | YES | Primary learning phase — where aha may occur |
| 3. Transfer test | 5 min | 40 | NO | Novel strings, same grammar — tests genuine rule learning |
| 4. Old-string test | 3 min | 20 | NO | Previously seen strings — tests memorization vs understanding |
| 5. Debrief survey | 5 min | — | — | Self-report, demographics, strategy questions |

### Measurements (All Three Independent Channels)

**1. Self-report aha button (always available)**
- A dedicated "I think I understand the pattern!" button visible throughout
- Participant can press it at any time, multiple times
- Records: trial number, timestamp, number of presses
- This is the PRIMARY independent variable for "insight onset"

**2. Confidence rating (every 10 trials)**
- "How well do you understand the pattern?" (1-10 slider)
- Brief, 3-second interruption every 10 trials
- Generates a confidence trajectory — sharp jump = potential aha

**3. Reaction time (every trial, implicit)**
- Time from string presentation to grammaticality judgment
- Fast RT + correct = confident decision
- |ΔRT| between consecutive trials = behavioral velocity proxy

**Additional per-trial data:**
- Accuracy (correct/incorrect)
- String presented
- String properties (length, similarity to training strings, violation type)
- Response (grammatical/ungrammatical)

### Hysteresis Protocol

The transfer test (Phase 3) IS the hysteresis test, following established AGL methodology:

1. **Feedback removal**: The "seed" (feedback) is silently removed
2. **Novel strings**: New strings from the SAME grammar (never seen before)
3. **Persistence measure**: F_task = accuracy on transfer strings
   - High F_task (>70%) = genuine rule learning (Crystal) — structure persists without seed
   - Low F_task (~50%) = memorization (Glass) — no transfer, no genuine insight

This follows Reber's original transfer paradigm and subsequent work on
abstract vs. chunk-based learning in AGL.

### EPT Predictions (Pre-registered, Falsifiable)

**P1: Velocity spike at insight onset**
- |ΔRT| or |Δ(rolling accuracy)| should peak within ±3 trials of self-reported aha
- Test: paired comparison of velocity at aha-trial vs. velocity at random matched trials
- Correction: permutation test with circular shift (avoids v2 circularity)

**P2: Dose-response (grammar difficulty)**
- Easy grammar → more participants reach criterion, faster
- Hard grammar → fewer reach criterion, slower
- The TIMING of transition should follow Arrhenius-like scaling with difficulty

**P3: Hysteresis (transfer test)**
- Participants who reported aha should show HIGHER transfer accuracy than
  participants who didn't, even though feedback is removed for both
- This is the human analog of: grokked networks maintain accuracy at WD=0

**P4: Convergent markers**
- Self-report aha, confidence jump, and RT velocity spike should co-occur
  (within ±3 trials of each other) in genuine insight episodes
- Divergence = pseudo-insight or non-insight

**P5: IPR analog**
- Participants who "grokked" should show LOWER RT variability (more consistent
  responding) after the transition — analogous to IPR dropping from 48 to 3
- Crystal state = consistent strategy. Glass state = variable guessing.

### What Would Falsify EPT

- If velocity spikes don't co-occur with self-reported aha → timing prediction fails
- If transfer accuracy is equal for aha vs. non-aha participants → no hysteresis
- If difficulty has no effect on transition rate → no dose-response
- If all three markers (aha, confidence, RT) diverge systematically → EPT is wrong
  about unified transition signatures

## Grammar Specifications

### Easy Grammar (3-state FSA)
```
States: S0 (start), S1, S2 (accept)
Alphabet: {M, V, X, R}
Transitions:
  S0 → S1: M, V
  S1 → S1: X
  S1 → S2: R
  S0 → S2: R
```
Generates: MR, MXR, MXXR, VR, VXR, R, etc.
Rule in words: "start with M or V (optional), any number of X's, end with R"

### Medium Grammar (5-state FSA)
```
States: S0 (start), S1, S2, S3, S4 (accept)
Alphabet: {M, V, X, R, T}
Transitions:
  S0 → S1: M
  S0 → S2: V
  S1 → S3: X, R
  S2 → S3: X, T
  S3 → S3: V
  S3 → S4: R
  S1 → S4: T
```
Generates: MXR, MXVR, MXVVR, MRR, MT, VXVR, VTR, VTVVR, etc.

### Hard Grammar (7-state FSA)
```
States: S0-S6, S6 is accept
Alphabet: {M, V, X, R, T, S}
Transitions:
  S0 → S1: M
  S0 → S2: V
  S1 → S3: X, S
  S2 → S3: T, X
  S3 → S4: V, R
  S4 → S5: M, X
  S4 → S3: T (loop)
  S5 → S6: R, S
  S3 → S6: S
```

### Ungrammatical String Generation
For each grammatical string, create an ungrammatical variant by:
1. Single letter substitution (change one letter to create illegal transition)
2. Letter insertion (add letter that violates transition rules)
3. Letter deletion (remove letter needed for valid path)
Equal mix of violation types. Matched for string length.

## Web Interface (thebeaker.com)

### Technical Requirements
- Single-page web application (HTML/CSS/JS)
- No server-side processing during experiment (all logic client-side)
- Data submitted to backend API at end of session
- Works on desktop and mobile (responsive)
- Minimum 60fps for accurate RT measurement
- Uses `performance.now()` for sub-millisecond timing

### Screens
1. **Welcome / Consent** — informed consent, demographics
2. **Instructions** — explain task, practice trial
3. **Main experiment** — string display, response buttons, aha button, confidence slider
4. **Transfer test** — same interface, no feedback
5. **Debrief** — strategy questions, aha self-report, open-ended feedback
6. **Thank you** — completion code (for Prolific), redirect

### Data Format (JSON per participant)
```json
{
  "participant_id": "uuid",
  "condition": "medium",
  "demographics": {"age": 21, "gender": "F", "education": "undergrad"},
  "consent_timestamp": "2026-04-01T10:00:00Z",
  "trials": [
    {
      "trial_num": 1,
      "phase": "learning",
      "string": "MXVR",
      "grammatical": true,
      "response": "grammatical",
      "correct": true,
      "rt_ms": 1234,
      "feedback_shown": true,
      "confidence": null,
      "aha_pressed": false,
      "timestamp": "2026-04-01T10:01:23Z"
    }
  ],
  "aha_events": [
    {"trial_num": 47, "timestamp": "..."}
  ],
  "confidence_trajectory": [
    {"after_trial": 10, "rating": 3},
    {"after_trial": 20, "rating": 4},
    {"after_trial": 30, "rating": 8}
  ],
  "debrief": {
    "reported_aha": true,
    "aha_trial_estimate": 45,
    "strategy_description": "I noticed all valid strings end with R...",
    "difficulty_rating": 6
  },
  "completion_code": "EPT-A3X9"
}
```

## Analysis Plan (Pre-registered)

### Primary Analyses

1. **Velocity spike at aha** (P1)
   - Compute |Δ(rolling accuracy, window=5)| per participant
   - For each aha participant: z-score of velocity at aha-trial vs baseline
   - Group test: one-sample t-test of z-scores vs 0
   - Permutation test: circularly shift trial labels, recompute z (5000 permutations)
   - Non-circular: aha button is INDEPENDENT of accuracy (pressed at any time)

2. **Dose-response** (P2)
   - Proportion reaching criterion (>75% accuracy in last 20 learning trials) by condition
   - Chi-squared test across Easy/Medium/Hard
   - Among those who reach criterion: Kruskal-Wallis on trial-of-criterion

3. **Hysteresis** (P3)
   - Transfer accuracy: aha-group vs non-aha-group
   - Mann-Whitney U test
   - Effect size: Cohen's d

4. **Marker convergence** (P4)
   - For each aha participant: compute distance (in trials) between:
     - Self-report aha trial
     - Confidence jump trial (first trial where confidence >= 7)
     - RT velocity peak trial
   - Report: mean |distance| and proportion within ±3 trials

5. **RT variability** (P5)
   - CV of RT in last 20 trials: aha-group vs non-aha-group
   - Lower CV in aha-group = more consistent (Crystal)

### Corrections
- Bonferroni correction for 5 primary tests (α = 0.01 per test)
- All secondary/exploratory analyses clearly labeled

### Power Analysis
- For P3 (hysteresis, primary test): medium effect d=0.5, α=0.01, power=0.80
  → N=38 per group (aha vs non-aha within each condition)
- With 40 per condition and ~50% expected aha rate: ~20 aha per condition
  → borderline power. Solution: pool across conditions for primary test,
    condition-specific tests are secondary.

## Timeline

| Week | Task |
|------|------|
| 1 | Build web interface, deploy to thebeaker.com |
| 2 | Pilot with 5-10 participants, iterate on UX and timing |
| 3 | IRB submission (or exemption request) |
| 4-5 | Data collection (recruitment channels a-d) |
| 6 | Analysis, write up results |

## Files in This Directory

```
ept_human_experiment/
├── docs/
│   ├── EXPERIMENT_DESIGN.md     ← this file
│   ├── IRB_PROTOCOL.md          ← ethics protocol
│   └── PREREGISTRATION.md       ← analysis pre-registration (for OSF)
├── web/
│   ├── index.html               ← main experiment page
│   ├── grammars.js              ← FSA definitions + string generation
│   ├── experiment.js            ← trial logic, timing, data collection
│   └── style.css                ← UI styling
├── analysis/
│   ├── analyze_ept_human.py     ← primary analysis script
│   └── plot_results.py          ← figure generation
├── recruitment/
│   ├── flyer.md                 ← recruitment flyer text
│   ├── consent_form.md          ← informed consent
│   └── prolific_description.md  ← Prolific study description
└── data/                        ← collected data (gitignored)
```

## References

- Reber, A.S. (1967). Implicit learning of artificial grammars. JVLVB, 6, 855-863.
- Chen et al. (2024). ENIGMA: A Web Application for Running Online AGL Experiments. J Psycholinguistic Res.
- Rosenberg et al. (2022). A reinforcement-based mechanism for discontinuous learning. PNAS.
- Pothos, E.M. (2007). Theories of Artificial Grammar Learning. Psychological Bulletin.
- Reber, A.S. & Lewis, S. (1977). Implicit learning: an analysis of the form and structure of a body of tacit knowledge. Cognition.
