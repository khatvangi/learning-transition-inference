# TODO — transition-inference framework

ordered by priority. do not drift.

## phase 1: fix what's broken (before anything else)

- [ ] **1a. delete old AGL analysis, replace with inference adapter**
  the old `tasks/agl/analysis/analyze_ept_human.py` has broken P1 (fake
  permutation), confounded P3/P5. do not patch. write a new thin adapter
  that loads AGL JSON data and calls `inference.detect_transitions()`.
  ~2 hours.

- [ ] **1b. rewrite claim language in EXPERIMENT_DESIGN.md**
  replace "first-order phase transition" with "transition signatures."
  replace "human validation of EPT" with "human tests of transition-signature
  predictions." replace "hysteresis" with "persistence under perturbation."
  ~30 min.

- [ ] **1c. hierarchical classification**
  restructure classify.py: stage 1 (learner vs non-learner) → stage 2
  (abrupt vs non-abrupt) → stage 3 (gradual vs unstable/mixed).
  moves the weakest distinction to the last branch. re-run validation.
  ~2 hours.

## phase 2: strengthen cross-domain evidence

- [ ] **2a. get zebra finch data** (Dryad API failed)
  try alternate download: direct Dryad file stream URLs, Zenodo mirror,
  or the GitHub acoustic-features repo. need individual bird song
  similarity trajectories over development days.

- [ ] **2b. get one gradual-learning dataset**
  need an empirical exemplar of GRADUAL learning to fill the topology map.
  candidates: human category learning (Shepard et al. style),
  motor skill acquisition, or second-language vocabulary.
  check OSF/Dryad for trial-level data.

- [ ] **2c. grokking with multiple seeds**
  current analysis uses 1 seed. run 5-10 seeds of mod-97 grokking
  (30 min on GPU) to get Ψ statistics with error bars.

## phase 3: documentation and framing

- [ ] **3a. update README to match new framing**
  core claim: domain-agnostic transition-topology inference.
  secondary claims: synthetic validation, cross-domain topology map,
  human experiment pipeline. README already partially reflects this
  but needs the "topology not proof" language.

- [ ] **3b. write a SCHEMA.md**
  document the canonical input/output contract of detect_transitions().
  this already exists in the code docstrings but should be a standalone
  reference for users/reviewers.

## phase 4: AGL experiment completion (only after 1-3)

- [ ] 4a. web UI (index.html, CSS)
- [ ] 4b. backend API endpoint for data submission
- [ ] 4c. IRB protocol
- [ ] 4d. OSF preregistration
- [ ] 4e. data dictionary
- [ ] 4f. pilot test (5-10 participants)

## explicitly NOT doing now

- directory restructuring (current layout is fine)
- formal "benchmark suite" (only 2 domains, premature)
- report generator (analysis scripts already produce comparable output)
- chasing more animal domains beyond zebra finch
- overselling Kramers kinetics
