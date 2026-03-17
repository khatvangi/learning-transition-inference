# Data Sources and Next Steps for Ψ Analysis Pipeline

## Executive Summary

This document provides a curated guide to the most promising data sources identified in the comprehensive deep review of discontinuous learning transitions across species. Use this to prioritize data extraction for your Ψ (transition sharpness) analysis.

---

## 1. Open Data Repositories Identified

### Zebra Finch Song Development Data

**Dryad Repository - Zebra Finch Song Ecology**
- **URL**: https://datadryad.org/dataset/doi:10.5061/dryad.stqjq2c6s
- **Content**: Breeding monitoring, observational transects, focal and year-round acoustic recordings, large-scale simultaneous playback experiment
- **Potential**: Individual bird trajectories, longitudinal acoustic data
- **Priority**: **HIGH** - Direct access to raw acoustic data

**Figshare - Zebra Finch Song Stimuli**
- **URL**: https://figshare.com/articles/media/Zebra_finch_song_stimuli/13438109
- **Content**: Zebra finch song stimuli recordings
- **Potential**: Standardized song data for similarity analysis
- **Priority**: **MEDIUM** - May need to pair with developmental trajectory data

**Dryad - Zebra Finch Song and Distance Call Amplitude**
- **URL**: https://datadryad.org/dataset/doi:10.5061/dryad.xgxd254h9
- **Content**: Transmission experiment and observational transects with amplitude measurements
- **Potential**: Individual bird acoustic measurements in natural environment
- **Priority**: **MEDIUM** - Check for developmental time series

**GitHub - Acoustic Fine Features Analysis**
- **URL**: https://github.com/maRce10/acoustic-fine-features-zebra-finch
- **Content**: Code for spotting and measuring fine acoustic structure in zebra finch songs
- **Potential**: Analysis pipeline that may include example datasets
- **Priority**: **MEDIUM** - Useful for methods, may contain sample data

**Figshare - Zebra Finch Parkinson's Model**
- **URL**: https://arizona.figshare.com/articles/dataset/Raw_birdsong_data_for_Vocal_changes_in_a_zebra_finch_model_of_Parkinson_s_Disease_characterized_by_alpha-synuclein_overexpression_in_the_song-dedicated_anterior_forebrain_pathway_/16619782
- **Content**: Raw birdsong data from Parkinson's disease model study
- **Potential**: Individual bird vocal trajectories (though disease model, not normal development)
- **Priority**: **MEDIUM** - May show altered developmental trajectories

### Behavioral Neuroscience Datasets

**bioRxiv - Information, Certainty, and Learning**
- **URL**: https://www.biorxiv.org/content/10.1101/2024.07.31.606111v4
- **Content**: Recent preprint on conditioning and learning
- **Potential**: May contain supplementary data on individual learning curves
- **Priority**: **HIGH** - Recent work, check supplementary materials

**PMC Article - Learning, Fast and Slow**
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC9509687/
- **Content**: Review/research on learning dynamics
- **Potential**: May cite studies with accessible data or contain digitizable figures
- **Priority**: **MEDIUM** - Good for literature connections

---

## 2. Key Papers from Comprehensive Report

The main research report (`discontinuous_learning_transitions_comprehensive_report.md`) identified ~60 high-priority papers with accessible data. Key categories:

### Tier 1: Must-Have Sources

#### Birdsong Crystallization
- **Tchernichovski et al. (2000)** - Original Sound Analysis Pro paper
- **Ölveczky et al. (2005)** - Changes in song variability during development
- **Vahaba et al. (2019)** - Individual trajectory analysis
- Look for: Supplementary tables with daily similarity scores per bird

#### Gallistel Conditioning
- **Gallistel et al. (2004)** - Individual learning curves in conditioning
- **Kheifets & Gallistel (2012)** - Abrupt transitions in conditioning
- **Kheifets et al. (2017)** - Temporal learning in mice
- Look for: Trial-by-trial response data, changepoint analysis code

#### Rodent Maze Learning
- **Reddy et al. (2022 PNAS)** - Reinforcement wave in mouse labyrinth
- **Rosenberg et al. (2021)** - Path efficiency in maze learning
- Look for: Individual path trajectories, trial-by-trial efficiency metrics

#### Primate/Corvid Insight
- **Bird & Emery (2009)** - Rook wire-bending insight
- **Weir et al. (2002)** - New Caledonian crow tool use
- **Köhler (1925/reanalysis)** - Classic chimpanzee insight studies
- Look for: Trial latencies, solution times, video analysis data

### Tier 2: Strong Candidates

#### Mooney Image Recognition
- **Teufel et al. (2018)** - Hysteresis in perceptual learning
- **Hsieh et al. (2010)** - Pop-out effects in Mooney images
- Look for: Individual subject threshold measurements, psychophysics data

#### Human AGL/Implicit Learning
- **Lawson et al. (2017)** - Individual differences in AGL
- **Batterink et al. (2015)** - Neural entrainment during implicit learning
- Look for: Trial-by-trial accuracy, RT data, individual learning curves

#### Honeybee Concept Learning
- **Giurfa et al. (2001)** - Concept learning in honeybees
- **Avargues-Weber et al. (2011)** - Abstract concept acquisition
- **Finke et al. (2023)** - Individual bee performance trajectories
- Look for: Individual bee choice data, trial-by-trial performance

### Tier 3: Additional Evidence

#### Vocabulary Explosion
- **Ganger & Brent (2004)** - Reanalysis of vocabulary spurt
- **Mayor & Plunkett (2014)** - Computational models of vocabulary growth
- Look for: Longitudinal CDI data, individual child word counts

#### Neural State Transitions
- **Durstewitz et al. (2010)** - Prefrontal ensemble transitions
- **Maggi et al. (2018)** - Neural state dynamics during learning
- **Kuchibhotla et al. (2019)** - Learning-related neural transitions
- Look for: Trial-by-trial neural ensemble data, state-space analysis code

---

## 3. Recommended Next Steps

### Immediate Actions (Week 1-2)

1. **Download Open Repository Data**
   - Start with Dryad zebra finch datasets (largest, most structured)
   - Download bioRxiv preprint supplementary materials
   - Clone GitHub acoustic analysis repository

2. **Extract High-Priority Papers**
   - Use the comprehensive report to identify top 20 papers per domain
   - Download PDFs for papers flagged with "Supplementary" or "Repository" data access
   - Focus on papers with N≥5 individuals and N≥20 time points

3. **Digitize Key Figures**
   - Identify papers with clear individual trajectory figures
   - Use WebPlotDigitizer on high-quality figures
   - Prioritize Gallistel conditioning papers (known for individual curves)

### Medium-Term Actions (Week 3-6)

4. **Contact Authors for Data**
   - For papers with "data available on request" statements
   - Focus on recent papers (2015-2025) where authors are still active
   - Emphasize cross-domain comparative analysis value

5. **Search Supplementary Materials**
   - Many papers have Excel/CSV files in supplementary materials not indexed by search
   - Check journal websites directly for papers identified as high-priority
   - Look for "Data S1", "Table S1" type supplements

6. **Explore Related Repositories**
   - Check OSF (Open Science Framework) for related projects
   - Search GitHub for analysis code that may include example data
   - Check author lab websites for shared datasets

### Long-Term Actions (Month 2-3)

7. **Build Standardized Dataset**
   - Create unified data format across all domains
   - Required fields: individual_id, time_point, performance_metric, domain
   - Document data provenance for each source

8. **Implement Ψ Analysis Pipeline**
   - Compute Ψ (transition sharpness) for each individual trajectory
   - Calculate CV of transition timing across individuals
   - Compare Ψ distributions across domains

9. **Identify Data Gaps**
   - Document which domains have insufficient data
   - Prioritize new experiments or collaborations to fill gaps
   - Consider meta-analysis of group-level data as fallback

---

## 4. Data Quality Checklist

For each dataset, verify:

- [ ] **Individual-level data** (not just group means)
- [ ] **Sufficient temporal resolution** (≥20 time points per individual)
- [ ] **Adequate sample size** (≥5 individuals)
- [ ] **Clear performance metric** (accuracy, similarity, latency, efficiency)
- [ ] **Metadata available** (species, age, experimental conditions)
- [ ] **Data format usable** (CSV, Excel, or digitizable figures)
- [ ] **Licensing permits reuse** (check data use agreements)

---

## 5. Contact Information for Key Repositories

### Data Repository Sites
- **Dryad**: https://datadryad.org
- **Figshare**: https://figshare.com
- **OSF**: https://osf.io
- **GitHub**: https://github.com

### Key Research Groups (for data requests)
- **Tchernichovski Lab** (CCNY) - Birdsong development
- **Gallistel Lab** (Rutgers) - Conditioning learning curves
- **Giurfa Lab** (Toulouse) - Honeybee cognition
- **Durstewitz Lab** (Heidelberg) - Neural state dynamics

---

## 6. Expected Data Yield Estimate

Based on the comprehensive review:

| Domain | Papers Reviewed | Likely Usable Data Sources | Data Type |
|--------|----------------|---------------------------|-----------|
| Birdsong | 89 | 8-12 | Repository + Figures |
| Conditioning | 143 | 15-20 | Figures (high quality) |
| Rodent Maze | 119 | 5-8 | Repository + Figures |
| Corvid/Primate | 87 | 3-5 | Figures + Video analysis |
| Mooney Images | 185 | 10-15 | Psychophysics data |
| Human AGL | 220 | 12-18 | Repository + Supplementary |
| Honeybee | 126 | 4-6 | Supplementary tables |
| Vocabulary | 84 | 6-10 | CDI databases + Figures |
| Neural | 155 | 8-12 | Repository + Code |
| Classic Studies | 202 | 5-8 | Digitized figures |

**Total Estimated Usable Sources**: 76-114 datasets across all domains

**Estimated Timeline**: 
- 20-30 datasets extractable in Month 1 (open repositories + supplementary)
- 30-50 additional datasets in Month 2 (figure digitization)
- 20-30 additional datasets in Month 3 (author requests + deep supplementary search)

---

## 7. Tools and Resources Needed

### Data Extraction Tools
- **WebPlotDigitizer** (https://automeris.io/WebPlotDigitizer/) - For figure digitization
- **Python pandas** - For data cleaning and standardization
- **R tidyverse** - Alternative for data wrangling
- **ImageJ/Fiji** - For extracting data from image-based figures

### Analysis Tools
- **Python scipy** - For changepoint detection
- **R changepoint package** - For statistical transition detection
- **MATLAB** - For some neuroscience dataset formats
- **Sound Analysis Pro (SAP)** - For birdsong analysis (if raw audio available)

### Repository Access
- **Institutional subscriptions** - Check for Dryad, Figshare institutional access
- **VPN access** - For paywalled journal supplementary materials
- **API access** - For automated repository searches (Dryad, Figshare have APIs)

---

## 8. Red Flags and Pitfalls to Avoid

### Common Data Issues
1. **Group averages only** - Most common problem; always check for individual data
2. **Insufficient time points** - Need ≥20 for reliable Ψ estimation
3. **Cross-sectional designs** - Different individuals at each time point (not true trajectories)
4. **Aggregated trials** - Block averages instead of trial-by-trial data
5. **Missing metadata** - Can't normalize across studies without experimental details

### Figure Digitization Challenges
1. **Low resolution** - Some older papers have poor figure quality
2. **Overlapping lines** - Multiple individuals plotted on same axes
3. **Log scales** - Need to account for axis transformations
4. **Error bars only** - Some papers show means ± SE without individual points
5. **3D plots** - Difficult to accurately digitize

### Repository Access Issues
1. **Broken links** - Older DOIs may not resolve
2. **Embargoed data** - Some datasets have time-limited access
3. **Proprietary formats** - May need specialized software to read
4. **Large file sizes** - Neural data can be terabytes (need storage plan)
5. **Incomplete documentation** - Metadata may be missing or unclear

---

## 9. Success Metrics

### Month 1 Goals
- [ ] 20+ datasets downloaded from open repositories
- [ ] 10+ papers with supplementary data extracted
- [ ] 5+ high-quality figures digitized per domain

### Month 2 Goals
- [ ] 50+ total usable datasets compiled
- [ ] Standardized data format implemented
- [ ] Initial Ψ analysis on 3+ domains

### Month 3 Goals
- [ ] 75+ total datasets (target minimum for robust cross-domain analysis)
- [ ] Ψ computed for all domains with sufficient data
- [ ] Cross-domain comparison analysis complete
- [ ] Data gaps documented and prioritized

---

## 10. Fallback Strategies

If insufficient individual-level data is found:

### Strategy A: Simulation-Based Validation
- Use group-level data to parameterize generative models
- Simulate individual trajectories with varying Ψ
- Test whether group averages are consistent with discontinuous individual transitions

### Strategy B: Targeted New Experiments
- Design minimal experiments to fill critical data gaps
- Focus on domains with easiest data collection (e.g., human AGL, honeybee)
- Collaborate with labs already collecting relevant data

### Strategy C: Meta-Analysis Approach
- Extract effect sizes and variance from group-level studies
- Use variance decomposition to infer individual trajectory properties
- Bayesian hierarchical models to estimate individual parameters

### Strategy D: Video/Audio Reanalysis
- For classic studies, check if original videos/audio are archived
- Reanalyze with modern computational tools (e.g., DeepLabCut for behavior)
- May reveal individual-level patterns not reported in original papers

---

## Contact for This Project

For questions about this data compilation or to share additional data sources, contact the research team.

**Last Updated**: 2026-03-17

---

## Appendix: Quick Reference URLs

### Primary Open Data Sources
- Dryad Zebra Finch: https://datadryad.org/dataset/doi:10.5061/dryad.stqjq2c6s
- Figshare Zebra Finch: https://figshare.com/articles/media/Zebra_finch_song_stimuli/13438109
- bioRxiv Conditioning: https://www.biorxiv.org/content/10.1101/2024.07.31.606111v4
- GitHub Acoustic Analysis: https://github.com/maRce10/acoustic-fine-features-zebra-finch

### Secondary Resources
- PMC Learning Review: https://pmc.ncbi.nlm.nih.gov/articles/PMC9509687/
- Dryad Amplitude Data: https://datadryad.org/dataset/doi:10.5061/dryad.xgxd254h9
- Figshare Parkinson's Model: https://arizona.figshare.com/articles/dataset/Raw_birdsong_data.../16619782

### Tool Links
- WebPlotDigitizer: https://automeris.io/WebPlotDigitizer/
- Sound Analysis Pro: http://soundanalysispro.com/
- Dryad API: https://datadryad.org/api/v2/docs/
- Figshare API: https://docs.figshare.com/

---

*This document is a companion to the comprehensive research report. Use it as a practical guide for data extraction and Ψ analysis implementation.*
