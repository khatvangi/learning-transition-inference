# transition signatures in human learning

a domain-agnostic framework for detecting abrupt transitions in learning curves,
with an Artificial Grammar Learning experiment as the first human instantiation.

part of the Epistemic Phase Transition (EPT) research program, which finds
common transition signatures across neural networks (grokking), animal learning,
and human cognition.

## core idea

the `inference/` module takes ANY time-series of learning performance and
answers: did this learner transition abruptly or gradually? did the transition
persist? do multiple measurement channels agree on timing?

the same code runs on grokking accuracy curves, zebra finch song trajectories,
rodent maze learning, and human AGL data. that's what makes the cross-domain
claim defensible.

## quick start

```bash
pip install -r requirements.txt

# validate the inference module on synthetic learners
python simulation/validate_inference.py

# run the AGL experiment analysis (once data is collected)
python analysis/analyze_ept_human.py data/
```

## directory structure

```
inference/                  — THE CORE: domain-agnostic transition detection
  psi.py                    — Ψ(t) velocity order parameter
  changepoint.py            — PELT + Bayesian online changepoint detection
  model_compare.py          — continuous vs changepoint vs HMM (BIC comparison)
  classify.py               — learner type classification (abrupt/gradual/unstable/non-learner)
  persistence.py            — post-transition stability tests (hysteresis analog)
  convergence.py            — cross-channel alignment with permutation test
  pipeline.py               — unified detect_transitions() interface

simulation/                 — synthetic validation
  synthetic_learners.py     — 5 learner types with known ground truth
  validate_inference.py     — recovery test (proves inference isn't circular)

tasks/agl/                  — (TODO) human AGL experiment
  web/                      — web experiment code (grammars.js, experiment.js)
  analysis/                 — AGL-specific analysis using inference/

ept_theory_docs/            — EPT theoretical framework
  FORMAL_PROPOSITIONS.md    — Ψ, F definitions, 4 transition signatures
  THEOREM_DEVELOPMENT.md    — mathematical formalism
  KRAMERS_CONNECTION.md     — barrier-crossing kinetics
  EVIDENCE_SCORECARD.md     — cross-domain evidence inventory
  ...

docs/                       — experiment design and literature
  EXPERIMENT_DESIGN.md      — AGL experiment protocol
  LITERATURE_REVIEW.md      — cross-domain literature review

scispace_data/              — literature search data (230 files, bibliographic)
recruitment/                — consent form, flyer, Prolific description
```

## inference module

the inference module detects transition signatures in any 1D learning curve:

```python
from inference import detect_transitions

result = detect_transitions(
    accuracy_series=acc,          # required: performance over trials
    confidence_series=conf,       # optional: metacognitive ratings
    rt_series=rt,                 # optional: reaction times
    transfer_series=transfer,     # optional: post-learning test data
)

print(result["classification"]["label"])  # "abrupt", "gradual", "non_learner", etc.
print(result["model_comparison"])         # continuous vs changepoint vs HMM
print(result["persistence"])              # did the transition hold?
print(result["convergence"])              # do channels agree on timing?
```

### what it does

1. **Ψ (velocity)**: computes |d(performance)/dt| — the instantaneous learning rate
2. **changepoints**: PELT or Bayesian online detection of mean-shift transitions
3. **model comparison**: fits sigmoid (gradual), step-function (abrupt), and 2-state HMM (unstable), selects by BIC
4. **classification**: combines evidence from sigmoid steepness, changepoint count, Ψ spike, and jump magnitude
5. **persistence**: tests whether post-transition performance holds after perturbation
6. **convergence**: tests whether accuracy, confidence, and RT changepoints align temporally (permutation test)

### validation

synthetic learner recovery (n=75, 15 per type):

| type | recovery rate |
|------|--------------|
| abrupt | ~87% |
| gradual | ~87% |
| non_learner | ~93% |
| unstable | ~13% (inherently ambiguous at low switch rates) |
| **overall** | **~73%** |

false-aha detection via convergence: 0.29 (false) vs 0.58 (true abrupt).

## transition signatures tested

| # | signature | operational definition | inference method |
|---|-----------|----------------------|-----------------|
| S1 | abruptness | Ψ spike + changepoint model wins + large jump | model_compare + psi |
| S2 | persistence | transfer accuracy > pre-transition baseline, controlling for learning ability | persistence (controlled) |
| S3 | convergence | accuracy, confidence, RT changepoints within ±5 trials | convergence (permutation) |
| S4 | dose-response | transition rate varies with task difficulty | cohort-level analysis |

note: these are "transition signatures," not "phase transition proof." the inference
layer measures behavioral signatures. the EPT interpretation maps them to phase-transition
physics. the two are deliberately separated.

## what's done vs TODO

done:
- [x] inference module (6 files, ~800 lines)
- [x] synthetic learner generators (5 types)
- [x] validation script (73% recovery, false-aha detection works)
- [x] experiment design document
- [x] grammar engine + trial engine
- [x] recruitment materials
- [x] EPT theory documents

TODO:
- [ ] cross-domain reanalysis (apply inference/ to grokking, animal, vocab data)
- [ ] web UI for AGL experiment
- [ ] backend API for data submission
- [ ] IRB protocol
- [ ] OSF pre-registration
- [ ] pilot test
- [ ] data dictionary

## license

MIT
