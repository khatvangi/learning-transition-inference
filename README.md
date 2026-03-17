# EPT Human Experiment — Paper 3

Artificial Grammar Learning experiment testing whether human "aha moments"
exhibit phase-transition signatures (velocity spikes, hysteresis, dose-response).

## Quick Start

1. Read: `docs/EXPERIMENT_DESIGN.md` — full experimental design
2. Deploy: `web/` directory to thebeaker.com/study
3. Recruit: materials in `recruitment/`
4. Analyze: `python analysis/analyze_ept_human.py data/`

## Directory Structure

```
docs/
  EXPERIMENT_DESIGN.md     — full experiment design + pre-registered analysis plan
  IRB_PROTOCOL.md          — (TODO) ethics protocol for IRB submission
  PREREGISTRATION.md       — (TODO) OSF pre-registration document

web/
  index.html               — (TODO) main experiment page
  grammars.js              — FSA grammar definitions + string generation
  experiment.js            — trial engine, timing, data collection
  style.css                — (TODO) UI styling

analysis/
  analyze_ept_human.py     — primary analysis (5 pre-registered tests)
  plot_results.py          — (TODO) figure generation

recruitment/
  consent_form.md          — informed consent text
  flyer.md                 — recruitment flyer
  prolific_description.md  — Prolific study listing

data/                      — collected data (one JSON per participant)
```

## What's Done vs TODO

Done:
- [x] Experiment design document
- [x] Grammar engine (3 grammars, string generation, violation generation)
- [x] Trial engine (phase management, timing, aha button, data collection)
- [x] Analysis script (5 pre-registered EPT tests)
- [x] Recruitment materials (consent, flyer, Prolific)

TODO (next session):
- [ ] index.html — the actual web interface (UI, screens, styling)
- [ ] style.css — thebeaker.com aesthetic
- [ ] Backend API endpoint for data submission
- [ ] IRB protocol document
- [ ] OSF pre-registration
- [ ] Pilot test (5-10 participants)
- [ ] Deploy to thebeaker.com

## EPT Predictions Tested

| # | Prediction | Measure | Test |
|---|-----------|---------|------|
| P1 | Velocity spike at aha | |Δ(accuracy)| at self-report | Permutation test |
| P2 | Dose-response | Grammar difficulty vs criterion rate | Chi-squared |
| P3 | Hysteresis | Transfer accuracy: aha vs non-aha | Mann-Whitney U |
| P4 | Marker convergence | Spread between aha, confidence, RT peak | Descriptive |
| P5 | RT consistency | CV of RT: aha vs non-aha | Mann-Whitney U |
