# Quick Screening Guide for Individual Learning Trajectory Papers

## Purpose
Use this checklist to rapidly screen papers for usability in the Ψ (transition sharpness) analysis. Print this and keep it handy when reviewing papers.

---

## ✅ INCLUSION CRITERIA (Must have ALL)

### 1. Individual-Level Data
- [ ] Shows data from **individual subjects** (not just group means)
- [ ] Can distinguish between different individuals in figures/tables
- [ ] Reports individual variability (not just error bars on group means)

**RED FLAGS**: 
- ❌ "Mean ± SEM" without individual data points
- ❌ "Group average performance over sessions"
- ❌ "Pooled data from N subjects"

---

### 2. Longitudinal/Sequential Measurements
- [ ] **≥20 measurement points** per individual (minimum for Ψ estimation)
- [ ] Measurements are **ordered in time** (trials, days, sessions)
- [ ] **Same individuals** measured repeatedly (not cross-sectional)

**RED FLAGS**:
- ❌ "Pre-test vs. Post-test only" (2 time points insufficient)
- ❌ "Different groups tested at different ages" (cross-sectional)
- ❌ "Averaged across 10-trial blocks" (reduces temporal resolution)

---

### 3. Clear Performance Metric
- [ ] **Quantitative measure** that can be tracked over time
- [ ] Metric is clearly defined and consistently measured
- [ ] Metric shows clear learning trajectory (not just binary success/fail)

**GOOD METRICS**:
- ✅ Song similarity score (0-100)
- ✅ Accuracy (% correct)
- ✅ Latency (seconds to solution)
- ✅ Path efficiency (optimal path length / actual path length)
- ✅ Recognition threshold (contrast %)

**RED FLAGS**:
- ❌ "Qualitative assessment of learning"
- ❌ "Pass/fail criterion" (binary, not continuous)
- ❌ Metric definition changes mid-study

---

### 4. Data Accessibility
At least ONE of the following:
- [ ] **Supplementary data files** (Excel, CSV, text)
- [ ] **Open data repository** (Dryad, Figshare, OSF, GitHub)
- [ ] **High-quality digitizable figures** (individual trajectories clearly visible)
- [ ] **"Data available on request"** statement (for recent papers)

**PRIORITY RANKING**:
1. 🥇 **Open repository** with raw data files → **HIGHEST PRIORITY**
2. 🥈 **Supplementary tables** with individual data → **HIGH PRIORITY**
3. 🥉 **Clear figures** with individual trajectories → **MEDIUM PRIORITY**
4. 📧 **Data on request** (recent papers, <5 years) → **MEDIUM PRIORITY**
5. 📧 **Data on request** (older papers, >5 years) → **LOW PRIORITY**
6. ❌ **No data statement** → **EXCLUDE** (unless classic/foundational)

---

## 🎯 BONUS FEATURES (Not required, but highly valuable)

### Statistical Sophistication
- [ ] Uses **changepoint detection** or **state-space models**
- [ ] Reports **individual transition times** or **onset points**
- [ ] Discusses **abrupt vs. gradual** learning explicitly
- [ ] Compares **individual variability** in learning trajectories

**KEYWORDS TO LOOK FOR**:
- "Changepoint analysis"
- "Hidden Markov model"
- "State-space model"
- "Transition point"
- "Sudden improvement"
- "Step function"
- "Abrupt onset"

---

### Sample Size
- [ ] **N ≥ 10 individuals** (robust statistics)
- [ ] **N ≥ 5 individuals** (minimum acceptable)
- [ ] **N < 5 individuals** (only if very detailed data or classic study)

---

### Temporal Resolution
- [ ] **≥50 time points** per individual (excellent)
- [ ] **20-49 time points** per individual (good)
- [ ] **10-19 time points** per individual (marginal, only if other features strong)
- [ ] **<10 time points** per individual (insufficient)

---

## 📋 DOMAIN-SPECIFIC TIPS

### Birdsong Crystallization
**Look for**: 
- Daily recordings over 30-90 days
- Similarity scores to tutor song (SAP software)
- Individual bird IDs in supplementary materials

**Classic papers**: Tchernichovski, Ölveczky, Brainard, Nottebohm
**Keywords**: "song development", "crystallization", "similarity score", "juvenile"

---

### Gallistel Conditioning
**Look for**:
- Trial-by-trial response rates
- Individual cumulative records
- Changepoint analysis
- "Backward learning curves"

**Classic papers**: Gallistel, Kheifets, Bhatt, Balsam
**Keywords**: "individual learning curve", "step function", "abrupt transition", "conditioning"

---

### Rodent Maze Learning
**Look for**:
- Individual path trajectories (video tracking)
- Trial-by-trial latency or path length
- Sudden drops in errors or time

**Classic papers**: Tolman, Reddy, Rosenberg
**Keywords**: "maze learning", "path efficiency", "latency", "spatial learning", "navigation"

---

### Primate/Corvid Insight
**Look for**:
- Trial-by-trial solution times
- Video analysis data
- Individual subject performance

**Classic papers**: Köhler, Bird & Emery, Weir, Taylor
**Keywords**: "tool use", "insight", "problem solving", "latency", "spontaneous"

---

### Mooney Image Recognition
**Look for**:
- Individual psychophysics thresholds
- Forward/backward contrast sequences
- Hysteresis measurements

**Classic papers**: Teufel, Hsieh, Moore
**Keywords**: "Mooney", "bistable", "hysteresis", "pop-out", "perceptual learning"

---

### Human AGL / Implicit Learning
**Look for**:
- Trial-by-trial accuracy or RT
- Individual learning curves
- Awareness assessments

**Classic papers**: Reber, Cleeremans, Batterink, Lawson
**Keywords**: "artificial grammar", "implicit learning", "SRT", "serial reaction time", "awareness"

---

### Honeybee Concept Learning
**Look for**:
- Individual bee choice data
- Trial-by-trial accuracy
- Transfer tests

**Classic papers**: Giurfa, Avargues-Weber, Finke
**Keywords**: "honeybee", "concept learning", "same-different", "transfer", "abstract rule"

---

### Vocabulary Explosion
**Look for**:
- Longitudinal CDI data
- Individual child word counts
- Daily/weekly measurements

**Classic papers**: Ganger & Brent, Mayor & Plunkett, McMurray
**Keywords**: "vocabulary spurt", "naming explosion", "word learning", "CDI", "longitudinal"

---

### Neural State Transitions
**Look for**:
- Trial-by-trial neural ensemble data
- State-space analysis
- Individual recording sessions

**Classic papers**: Durstewitz, Maggi, Kuchibhotla, Mante
**Keywords**: "neural ensemble", "state transition", "prefrontal", "trial-by-trial", "dynamics"

---

## 🚀 RAPID SCREENING WORKFLOW

### Step 1: Abstract Scan (30 seconds)
- Does it mention **individual subjects/animals/participants**?
- Does it mention **longitudinal/repeated measurements**?
- Does it mention **learning trajectories/curves**?

**If NO to any** → Skip to next paper
**If YES to all** → Proceed to Step 2

---

### Step 2: Methods Scan (2 minutes)
- Check **Sample Size** (N individuals)
- Check **Number of measurements** per individual
- Check **Performance metric** used
- Check **Data availability** statement

**If fails inclusion criteria** → Mark as EXCLUDED
**If meets criteria** → Proceed to Step 3

---

### Step 3: Results/Figures Scan (3 minutes)
- Look for **individual trajectory figures**
- Check if **individual data points** are visible
- Assess **figure quality** for digitization
- Check for **supplementary materials** mention

**Rate as**:
- 🥇 **HIGH PRIORITY** (open data or excellent figures)
- 🥈 **MEDIUM PRIORITY** (good figures or data on request)
- 🥉 **LOW PRIORITY** (marginal data quality or accessibility)

---

### Step 4: Data Access Check (2 minutes)
- Search for **supplementary materials** link
- Check journal website for **data supplements**
- Look for **repository DOI** in paper
- Note **author contact** for data requests

**Document**:
- Data location (if found)
- Repository URL (if available)
- Contact email (if data on request)

---

## 📊 TRACKING TEMPLATE

For each screened paper, record:

```
Paper ID: [First author + Year]
Domain: [Birdsong/Conditioning/Maze/etc.]
✅ Individual data: YES / NO
✅ ≥20 time points: YES / NO
✅ Clear metric: YES / NO
✅ Data accessible: YES / NO
Priority: HIGH / MEDIUM / LOW / EXCLUDE
Data location: [Repository URL / Supplementary / Figures / Request]
Notes: [Any special considerations]
```

---

## 🎯 EFFICIENCY TIPS

### Time-Saving Strategies
1. **Start with recent papers** (2015-2025) - more likely to have open data
2. **Check supplementary materials FIRST** - often overlooked treasure trove
3. **Use Ctrl+F** to search PDFs for keywords: "individual", "trajectory", "supplementary", "repository"
4. **Batch similar papers** - screen all birdsong papers together, etc.
5. **Set time limits** - 5 min max per paper for initial screening

### Red Flags for Quick Exclusion
- ❌ "Group-level analysis only"
- ❌ "Aggregated across subjects"
- ❌ "Mean performance shown"
- ❌ Review paper with no original data
- ❌ Theoretical/computational model with no empirical data

### Green Flags for Quick Inclusion
- ✅ "Individual learning curves shown in Figure X"
- ✅ "Data available at [repository URL]"
- ✅ "See supplementary materials for individual data"
- ✅ Figure caption: "Each line represents one subject"
- ✅ "Trial-by-trial analysis"

---

## 🎓 CLASSIC PAPERS EXCEPTION RULE

Some classic foundational papers should be included **even if** they don't meet modern data accessibility standards:

**Include if**:
- Widely cited (>500 citations) **AND**
- Foundational to the field **AND**
- Contains digitizable figures with individual data

**Examples**:
- Köhler (1925) - Chimpanzee insight
- Tolman (1948) - Latent learning
- Tchernichovski et al. (2000) - Birdsong SAP
- Gallistel et al. (2004) - Conditioning step functions

**Rationale**: Historical importance + potential for figure digitization

---

## ✍️ NOTES SECTION

Use this space for domain-specific observations:

**Birdsong**:
- Most papers use SAP similarity scores (standardized metric ✅)
- Supplementary materials often have daily scores per bird
- Look for "individual bird data" in figure legends

**Conditioning**:
- Gallistel lab papers almost always have individual curves
- Look for "cumulative record" figures
- Trial-by-trial data often in supplementary Excel files

**Maze**:
- Video tracking data increasingly available
- Look for "path analysis" or "trajectory analysis"
- Latency data more common than path efficiency

**Insight**:
- Often small N (3-8 subjects) but very detailed
- Solution times are key metric
- Video data may be in supplementary materials

**Human**:
- AGL studies often have trial-by-trial RT and accuracy
- Psychophysics studies have individual threshold data
- Check OSF for preregistered studies (often have open data)

---

**Last Updated**: 2026-03-17

**Version**: 1.0

**For**: Ψ Analysis Pipeline - Discontinuous Learning Transitions Project

---

*Print this guide and keep it next to you when screening papers. Aim for 5-10 minutes per paper maximum.*
