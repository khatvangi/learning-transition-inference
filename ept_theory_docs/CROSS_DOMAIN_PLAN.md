# Cross-Domain Universality — From Analogy to Evidence

**Date**: 2026-03-17
**Goal**: Move from "these systems look similar" to "we measured the same signatures" — the step that makes this a Nature paper.

---

## 1. The Strategy

We can't run new animal experiments. But we CAN reanalyze published data with our Ψ metric. The key insight: **many published papers contain quantitative learning trajectories that have never been analyzed for phase-transition signatures.**

What we need to compute for each system:
- **Ψ(t)** = |d(performance)/dt| — velocity of the performance measure at each time point
- **Spike ratio** = max(Ψ) / median(Ψ) — how localized is the transition?
- **Transition sharpness** = time from 20% to 80% of final performance
- **CV of transition timing** = across individuals/seeds
- **Hysteresis evidence** = does performance persist when the driving condition is removed?

If these metrics show the SAME quantitative pattern across grokking, birdsong, and rodent learning, that's cross-domain evidence — not analogy.

---

## 2. Available Data Sources

### 2.1 Birdsong Crystallization

**Source**: Tchernichovski, O., Mitra, P.P., Lints, T. & Nottebohm, F. (2001). Dynamics of the vocal imitation process. Science, 291, 2564-2569.

**What they measured**: Daily similarity scores between pupil song and tutor song for individual zebra finches, from subsong through crystallization. The paper includes Figure 3 showing similarity trajectories for individual birds.

**Data availability**:
- Figures contain individual bird trajectories — can be digitized with WebPlotDigitizer or similar
- Sound Analysis Pro (SAP) software is open source — Tchernichovski's lab at CUNY
- The Brainard lab (UCSF) and Fee lab (MIT) have extensive developmental birdsong datasets
- Zebrafinch.org may have shared datasets

**What we'd compute**:
- Ψ(day) = |Δ(similarity_score)| per day
- Spike ratio at crystallization vs baseline
- Sharpness: days from 20% to 80% similarity
- Compare across individual birds (CV of crystallization timing)

**The prediction**: Ψ should spike sharply at crystallization (localized to a small fraction of total development), just as weight velocity spikes at grokking.

### 2.2 Individual Conditioning Curves (Gallistel)

**Source**: Gallistel, C.R., Fairhurst, S. & Balsam, P. (2004). The learning curve. PNAS, 101, 13124-13131.

**What they measured**: Trial-by-trial performance for individual animals across 6 paradigms:
1. Pigeon autoshaping
2. Rabbit delay eye-blink
3. Rabbit trace eye-blink
4. Rat autoshaped hopper entry
5. Rat plus maze
6. Mouse water maze

**Data availability**:
- Figures show individual animal learning curves — can be digitized
- Gallistel's lab may have the raw data (he's at Rutgers)
- The specific datasets were from published studies by other labs

**What we'd compute**:
- Ψ(trial) = |Δ(performance)| per trial block
- Spike ratio — how sudden is the step?
- Sharpness: trials from 20% to 80% performance
- Compare EPT prediction: conditioning should show Ψ spike (discontinuous output) but may differ from grokking in the velocity profile shape

### 2.3 Mouse Maze Learning (Reddy 2022)

**Source**: Reddy, G. (2022). A reinforcement-based mechanism for discontinuous learning. PNAS, 119, e2215352119.

**What they measured**: Trial-by-trial path efficiency in mice navigating a labyrinth. Individual mouse trajectories showing the "reinforcement wave" and the sudden discovery of direct paths.

**Data availability**:
- PNAS papers usually have supplementary data
- The paper explicitly discusses discontinuous learning — the data may be available
- Rosenberg (co-author) is at Harvard

**What we'd compute**:
- Ψ(trial) = |Δ(path_efficiency)| per trial
- Spike at the "sudden insight" moment
- Compare with the reinforcement wave prediction

### 2.4 Mooney Image Pop-Out

**Source**: Ludmer, R., Dudai, Y. & Rubin, N. (2011). Uncovering camouflage. Neuron, 69, 1002-1014.

**What they measured**: Recognition accuracy for Mooney images before and after learning the hidden figure. The key data: contrast threshold for recognition.

**What we'd compute**: Hysteresis gap — the forward threshold (first recognition) vs reverse threshold (image degradation at which percept is lost). This IS our Prediction 2.

**Challenge**: We'd need to run our own psychophysics experiment for the contrast threshold hysteresis. Can't easily get this from published data.

### 2.5 Prefrontal Neural Ensemble Transitions (Durstewitz 2010)

**Source**: Durstewitz, D. et al. (2010). Abrupt transitions between prefrontal neural ensemble states. Neuron, 66, 438-448.

**What they measured**: Trial-by-trial neural ensemble states in rat PFC during rule-learning task. They explicitly showed "abrupt transitions" in neural states.

**Data availability**: Neural data may be available through the original authors or data sharing repositories.

**What we'd compute**:
- Ψ on the neural state trajectory (they already computed something similar)
- Compare the transition sharpness and timing with our grokking data

---

## 3. What's Feasible RIGHT NOW

### Tier 1: Digitize published figures (1-2 days work)

1. **Gallistel (2004)** — Digitize the individual learning curves from their Figures 2-7. Apply Ψ metric. Compare spike ratio and sharpness with grokking.

2. **Tchernichovski (2001)** — Digitize the similarity trajectories from their Figure 3. Apply Ψ metric. Look for velocity spike at crystallization.

3. **Reddy (2022)** — Digitize the individual mouse learning curves from their figures. Apply Ψ metric.

Tools: WebPlotDigitizer (web-based, free), or Python with matplotlib's ginput for manual digitization.

### Tier 2: Request data from authors (1-2 weeks)

4. Email Tchernichovski (CUNY) for raw song similarity data
5. Email Reddy (NTT Research / Harvard) for raw maze data
6. Email Gallistel (Rutgers) for raw trial-by-trial data

### Tier 3: Run our own experiments (months)

7. Mooney image hysteresis (Prediction 2) — needs psychophysics setup
8. Human AGL (Paper 3) — experiment designed, needs web interface + IRB

---

## 4. The Analysis Pipeline

For each dataset (grokking + each biological system):

```python
def compute_ept_signatures(time_points, performance):
    """compute EPT diagnostic from any learning trajectory"""

    # 1. velocity Ψ(t)
    psi = np.abs(np.diff(performance) / np.diff(time_points))

    # 2. spike ratio
    baseline = np.median(psi[:len(psi)//4])  # first quarter as baseline
    spike_ratio = np.max(psi) / (baseline + 1e-8)

    # 3. transition sharpness (time from 20% to 80% of final)
    final = performance[-1]
    t_20 = time_points[np.argmax(performance >= 0.2 * final)]
    t_80 = time_points[np.argmax(performance >= 0.8 * final)]
    sharpness = t_80 - t_20

    # 4. fraction of total time in transition
    total_time = time_points[-1] - time_points[0]
    transition_fraction = sharpness / total_time

    return {
        'spike_ratio': spike_ratio,
        'sharpness': sharpness,
        'transition_fraction': transition_fraction,
        'psi_max': np.max(psi),
        'psi_median': np.median(psi),
    }
```

### The Cross-Domain Comparison Table

If we compute these for grokking, birdsong, and Gallistel conditioning, we get:

| Metric | Grokking (ours) | Birdsong (digitized) | Conditioning (digitized) |
|--------|-----------------|---------------------|-------------------------|
| Spike ratio | >100 | predicted: >10 | predicted: >5 |
| Transition fraction | <2% | predicted: <10% | predicted: <5% |
| CV of timing | 0.14-0.21 | to be measured | to be measured |
| Hysteresis | YES (0.999) | YES (deafening lit.) | PARTIAL (extinction) |

If the numbers match in order of magnitude, that's quantitative cross-domain evidence.

---

## 5. What This Adds to the Paper

### Without cross-domain data (current state):
> "We propose that these signatures are universal" (Discussion speculation)

### With digitized cross-domain data:
> "We computed the velocity diagnostic Ψ on published learning trajectories from three independent domains (Table X). In all systems where the task requires representational reorganization — neural network grokking, zebra finch song crystallization, and rodent maze learning — the velocity spike ratio exceeds 10 and the transition occupies less than 5% of total learning time. Conditioning paradigms show smaller spike ratios, consistent with the EPT prediction that threshold crossing (parameter adjustment) produces weaker velocity signatures than representational reorganization."

This is the difference between a Discussion paragraph and a Results figure.

---

## 6. The Figure

**Figure X: Cross-domain EPT signatures**

Panel A: Grokking — test accuracy trajectory with Ψ overlay showing spike
Panel B: Birdsong — similarity trajectory with Ψ overlay showing spike at crystallization
Panel C: Mouse maze — path efficiency with Ψ overlay showing spike at "insight"
Panel D: Conditioning — response rate with Ψ overlay (smaller spike, different shape)
Panel E: Cross-domain comparison — spike ratio, transition fraction, CV on same axes for all systems

This one figure could be the most impactful in the paper.

---

## 7. Immediate Next Steps

1. **Download/digitize** Gallistel (2004) Figure 2 (pigeon autoshaping individual curves) — I can help write the digitization code
2. **Download/digitize** Tchernichovski (2001) Figure 3 (song similarity trajectories)
3. **Download/digitize** Reddy (2022) individual mouse learning curves
4. **Write the analysis pipeline** (compute_ept_signatures function)
5. **Generate the cross-domain comparison table and figure**

Shall I start with the analysis pipeline code and the digitization approach? We can work with even rough digitized data to see if the pattern holds before seeking raw data from authors.
