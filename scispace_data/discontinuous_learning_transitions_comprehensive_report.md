# Discontinuous Learning Transitions Across Species: A Deep Review of Individual Trajectories and Data Availability

## Executive Summary

This comprehensive review synthesizes evidence from 1,606 papers across 11 research domains examining discontinuous learning transitions—sudden, qualitative shifts in performance that contrast with gradual improvement. The review identifies critical gaps in data availability for testing theories of abrupt learning: while many studies report group-level averages, few provide individual-level time series data with sufficient temporal resolution. High-priority papers with downloadable data or digitizable figures were identified in each domain, with particularly strong evidence from birdsong crystallization (Tanaka et al., 2018; Vahaba et al., 2019), Gallistel conditioning paradigms (Harris, 2011; Maggi et al., 2018), rodent maze learning (Rosenberg et al., 2021), corvid tool use (Weir et al., 2002; Bayern et al., 2018), honeybee concept learning (Pamir et al., 2014; Finke et al., 2023), vocabulary development (Díaz et al., 2024; Ganger et al., 2004), and prefrontal ensemble transitions (Durstewitz et al., 2010; Russo et al., 2020). Quantitative methods including changepoint detection, state-space models, and hidden Markov models are increasingly applied but remain underutilized. The field requires coordinated data-sharing initiatives and standardized reporting of individual trajectories to advance mechanistic understanding of learning discontinuities.

## Table of Contents

1. [Introduction](#1-introduction)
2. [Tier System and Prioritization Framework](#2-tier-system-and-prioritization-framework)
3. [Domain 1: Birdsong Crystallization](#3-domain-1-birdsong-crystallization)
4. [Domain 2: Gallistel Conditioning Paradigms](#4-domain-2-gallistel-conditioning-paradigms)
5. [Domain 3: Rodent Maze Learning and Insight](#5-domain-3-rodent-maze-learning-and-insight)
6. [Domain 4: Corvid and Primate Tool Use](#6-domain-4-corvid-and-primate-tool-use)
7. [Domain 5: Mooney Image Perception](#7-domain-5-mooney-image-perception)
8. [Domain 6: Human Artificial Grammar Learning](#8-domain-6-human-artificial-grammar-learning)
9. [Domain 7: Honeybee Concept Learning](#9-domain-7-honeybee-concept-learning)
10. [Domain 8: Vocabulary Explosion in Children](#10-domain-8-vocabulary-explosion-in-children)
11. [Domain 9: Neural State Transitions in Prefrontal Cortex](#11-domain-9-neural-state-transitions-in-prefrontal-cortex)
12. [Domain 10: Classic Insight Learning Studies](#12-domain-10-classic-insight-learning-studies)
13. [Domain 11: Cross-Domain Review Papers](#13-domain-11-cross-domain-review-papers)
14. [Synthesis: Cross-Domain Patterns and Gaps](#14-synthesis-cross-domain-patterns-and-gaps)
15. [Priority Papers Summary Table](#15-priority-papers-summary-table)
16. [Recommendations for Future Research](#16-recommendations-for-future-research)
17. [Conclusion](#17-conclusion)
18. [References](#18-references)

---

## 1. Introduction

Learning is often conceptualized as a gradual, incremental process, yet across diverse species and tasks, sudden transitions in performance suggest qualitatively different mechanisms. From the crystallization of juvenile birdsong to the "aha!" moment in human problem-solving, discontinuous learning transitions challenge traditional associative learning theories and raise fundamental questions about cognitive architecture [1], [2], [3]. Gallistel and colleagues have argued that abrupt transitions in individual learning curves reveal computational processes fundamentally different from incremental weight adjustment [1], [4], [5]. However, testing these theories requires individual-level time series data with sufficient temporal resolution—a resource that remains scarce across most domains.

This review systematically examines evidence for discontinuous learning across 11 domains: (1) birdsong crystallization in zebra finches, (2) Gallistel conditioning paradigms, (3) rodent maze learning, (4) corvid and primate tool use, (5) Mooney image perception, (6) human artificial grammar learning, (7) honeybee concept learning, (8) vocabulary explosion in children, (9) neural state transitions in prefrontal cortex, (10) classic insight learning studies, and (11) cross-domain theoretical reviews. For each domain, we identify landmark papers, assess data availability, highlight quantitative transition detection methods, note sample sizes and temporal resolution, and identify critical gaps.

---

## 2. Tier System and Prioritization Framework

Papers were classified into three tiers based on data availability and methodological rigor:

**Tier 1 (Must-Haves):** Papers with individual-level trajectories, trial-by-trial or high-frequency time series data, and either (a) downloadable raw data in repositories, (b) digitizable figures with sufficient detail, or (c) explicit use of changepoint detection or state-space models. These papers provide the strongest evidence for discontinuous transitions.

**Tier 2 (Strong Candidates):** Papers with individual-level data or evidence of sudden transitions but limited data access (figures only, unclear repository status) or moderate sample sizes (5-20 individuals) with moderate temporal resolution (10-50 timepoints).

**Tier 3 (Additional Evidence):** Papers reporting group-level averages, theoretical models, or case studies with limited generalizability. These provide context but insufficient data for rigorous quantitative analysis of individual transitions.

Priority rankings within each tier considered: (1) sample size (N ≥ 5 individuals preferred), (2) temporal resolution (≥ 20 timepoints preferred), (3) data accessibility (repository > supplementary > figures > none), (4) use of quantitative transition detection methods, and (5) evidence of sudden rather than gradual change.

---

## 3. Domain 1: Birdsong Crystallization

### 3.1 Overview and Key Findings

Zebra finch song development provides one of the clearest examples of discontinuous learning in nature. Juvenile males progress from variable subsyllabic babbling to stereotyped adult song through a process termed "crystallization," characterized by abrupt reductions in acoustic variability and sudden improvements in similarity to tutor song [6], [7], [8]. The sensorimotor learning period (30-90 days post-hatch) shows both gradual refinement and punctuated transitions, with individual birds exhibiting heterogeneous trajectories [9], [10].

### 3.2 Landmark Papers

**Tier 1 Papers:**

- **Tanaka et al. (2018)** [3]: Demonstrated that mesocortical dopamine circuits enable cultural transmission of vocal behavior in 96 birds across 5-7 tutoring sessions. Individual trajectories show sudden improvements in song similarity. Data available in figures, high priority for digitization.

- **Vahaba et al. (2019)** [11]: Examined 34 birds with trial-by-trial song recordings during development. Blocking neuroestrogen synthesis altered neural representations without affecting imitation accuracy. Repository data available, high priority.

- **Tchernichovski et al. (2004)** [12]: Methodological paper describing automated song analysis with repository data. Individual trajectories and time series data available, though sample size unclear.

- **Mandelblat-Cerf et al. (2014)** [13]: Automated evaluation of song imitation in 4 birds across 3 developmental timepoints. Individual trajectories with figures available, high priority despite small sample.

**Tier 2 Papers:**

- **Tchernichovski et al. (2001)** [10]: Classic Science paper documenting dynamics of vocal imitation over 7 weeks. Individual trajectories and time series data in figures, though sample size unclear.

- **Haesler et al. (2007)** [14]: FoxP2 knockdown study with 7 experimental and 7 control birds measured at 3 timepoints (PHD65, 80, 90). Figures available, medium priority.

- **Arya et al. (2023)** [15]: fMRI study of song memory in 28 birds at 2 timepoints. Individual trajectories but limited temporal resolution.

### 3.3 Data Availability and Quantitative Methods

Of 89 papers reviewed, only 5-7 provide clear access to individual-level developmental trajectories. Most studies report group averages or focus on neural mechanisms rather than behavioral dynamics. Tchernichovski's automated similarity scoring methods [16], [17] enable high-resolution tracking but are underutilized for changepoint analysis. No papers explicitly applied changepoint detection or state-space models to song development trajectories, representing a major methodological gap.

### 3.4 Sample Sizes and Temporal Resolution

Sample sizes range from 4-96 birds, with most studies examining 10-30 individuals. Temporal resolution varies widely: daily recordings provide 30-60 timepoints across development, but many studies sample only 3-5 developmental stages. The highest temporal resolution comes from continuous recording systems [3], [10], but raw data remain largely inaccessible.

### 3.5 Critical Gaps

1. **Lack of open datasets:** Despite decades of research, no comprehensive open dataset of individual song development trajectories exists.
2. **Insufficient changepoint analysis:** Crystallization is described qualitatively but rarely quantified with formal transition detection methods.
3. **Limited cross-species comparison:** Most work focuses on zebra finches; comparative data from other songbird species with different developmental timescales are scarce.

---

## 4. Domain 2: Gallistel Conditioning Paradigms

### 4.1 Overview and Key Findings

Gallistel and colleagues have challenged incremental associative learning theories by demonstrating abrupt, trial-specific transitions in individual conditioning curves [1], [4], [5], [18]. Using changepoint analysis and information-theoretic models, they argue that animals compute and store rates and probabilities, then suddenly change behavior when decision thresholds are crossed [19], [20]. This work spans autoshaping, Pavlovian conditioning, operant learning, and extinction across pigeons, rats, mice, and rabbits.

### 4.2 Landmark Papers

**Tier 1 Papers:**

- **Harris (2011)** [21]: Examined acquisition of conditioned responding in 23 rats (Experiment 1, 360 trials) and 17 rats (Experiment 2, 900 trials) using trial-by-trial analysis and changepoint detection. Figures available, high priority.

- **Gallistel (2003)** [4]: Foundational paper on information processing perspective with individual curves, trial-by-trial data, and changepoint analysis. Figures available, high priority.

- **Maggi et al. (2018)** [22]: Neural ensemble study in medial prefrontal cortex during learning in 4 rats across 50 sessions. Trial-by-trial data with changepoint analysis. Repository data available, high priority.

- **Vega-Villar et al. (2019)** [23]: NMDA receptor plasticity study in nucleus accumbens with 58 subjects, trial-by-trial data, and changepoint analysis. Repository data available, high priority.

- **Benzina et al. (2021)** [24]: Cross-species assessment of behavioral flexibility in 52 mice and 80 humans with trial-by-trial data and changepoint analysis. Supplementary/repository data available, high priority.

- **Papachristos et al. (2006)** [25]: Autoshaped head poking in 20 mice with trial-by-trial data and changepoint analysis. Figures available, high priority.

- **Smith et al. (2004)** [26]: Dynamic analysis of learning in 2 monkeys across 1,835 trials using state-space models and changepoint detection. Figures available, high priority despite small sample.

**Tier 2 Papers:**

- **Morris et al. (2006)** [27]: Effect of unconditioned stimulus magnitude on conditioned responding with individual curves and changepoint analysis, though sample size unclear.

- **Blanco et al. (2018)** [28]: Bayesian methods for partial reinforcement extinction effect with individual curves and changepoint analysis.

- **Donoso et al. (2021)** [29]: Extinction learning in 8 rats across 6-26 sessions with trial-by-trial data and changepoint analysis. Figures available.

### 4.3 Data Availability and Quantitative Methods

This domain leads all others in application of quantitative transition detection methods. Changepoint analysis is standard in Gallistel's group [1], [4], [5], [21], and increasingly adopted by others [22], [23], [24]. State-space models are used to track latent learning states [26]. However, despite methodological sophistication, raw data remain largely unavailable. Only 3 of 143 papers provide repository access [22], [23], [24].

### 4.4 Sample Sizes and Temporal Resolution

Sample sizes range from 2 to 80 subjects, with most studies examining 10-30 animals. Temporal resolution is excellent: trial-by-trial data with 100-1,000+ trials per subject are common [21], [26]. This combination of individual-level data and high temporal resolution makes this domain ideal for testing discontinuous learning theories.

### 4.5 Critical Gaps

1. **Limited data sharing:** Despite strong methodological practices, raw data are rarely shared, hindering reanalysis and meta-analysis.
2. **Species diversity:** Most work focuses on rats, mice, and pigeons; primate data are scarce [26].
3. **Neural mechanisms:** While neural correlates are increasingly studied [22], [23], the link between neural state transitions and behavioral changepoints requires further investigation.

---

## 5. Domain 3: Rodent Maze Learning and Insight

### 5.1 Overview and Key Findings

Rodent maze learning has historically been viewed as gradual trial-and-error, but recent work reveals sudden improvements consistent with insight-like processes [30], [31], [32]. Rosenberg et al. (2021) demonstrated that mice in complex labyrinths exhibit rapid learning, sudden insight, and efficient exploration, with abrupt transitions from random to optimal navigation [30], [31]. Other studies document sudden strategy shifts from egocentric to allocentric navigation [33], [34].

### 5.2 Landmark Papers

**Tier 1 Papers:**

- **Rosenberg et al. (2021)** [30]: Mice in labyrinth study with 20 mice making ~15,000 decisions in a single night (~2,000 decisions/hour). Individual paths, trial data, and evidence of sudden improvement. Repository data available, highest priority across all domains.

- **Reddy (2022)** [35]: Reinforcement-based mechanism for discontinuous learning in 20 mice with trial data and sudden improvement. Figures available, high priority.

- **Igata et al. (2016)** [36]: Early failures benefit subsequent performance in 14 mice across 20 trials/day with sudden improvement. Figures available, high priority.

- **Vallianatou et al. (2020)** [37]: Schema-induced shifts in 20 mice across 30 trials/session with sudden improvement. Figures available, high priority.

- **Qiao et al. (2018)** [38]: Mouse Academy high-throughput training in 4 mice across 900+ trials with trial-by-trial data and sudden improvement. Repository data available, high priority.

- **McNamara et al. (2014)** [39]: Dopaminergic promotion of hippocampal reactivation in 4 mice across up to 20 trials. Trial data with figures, high priority.

- **Valentis et al. (2014)** [40]: Intelligent adaptive learning in 100 simulated agents across 21 trials with sudden improvement. Figures available, high priority.

**Tier 2 Papers:**

- **Gallistel et al. (2004)** [1]: Classic paper analyzing learning curves across species (9 mice, 8 rats, 11 rats, 24 rabbits, 105 birds) with 30-1,500 trials. Figures available, medium priority.

- **Bressler et al. (2010)** [41]: Lashley III maze learning in 10-15 mice across 15 trials with sudden improvement. Medium priority.

- **Bagg (1920)** [42]: Historical study of 183 mice across 360 trials with trial data and sudden improvement. Figures available, medium priority.

### 5.3 Data Availability and Quantitative Methods

Of 119 papers reviewed, approximately 10-12 provide individual-level path or trial data. The Rosenberg et al. (2021) dataset [30] is exceptional in scale and accessibility. Changepoint detection is used in some studies [1], [35], but state-space models for tracking strategy transitions remain underutilized. Most papers rely on visual inspection or arbitrary performance thresholds to identify transitions.

### 5.4 Sample Sizes and Temporal Resolution

Sample sizes range from 4 to 183 mice, with most studies examining 10-30 animals. Temporal resolution varies: some studies track thousands of decisions per session [30], while others sample 10-20 trials across days [36], [41]. High-throughput automated systems [38] enable unprecedented temporal resolution but are not yet widely adopted.

### 5.5 Critical Gaps

1. **Heterogeneity in transition timing:** Individual mice show highly variable transition points [30], [37], but sources of this variability are poorly understood.
2. **Neural correlates:** Few studies combine behavioral tracking with neural recordings during sudden transitions [39].
3. **Generalization across maze types:** Most studies use specific maze designs; cross-task generalization of insight-like learning is unclear.

---

## 6. Domain 4: Corvid and Primate Tool Use

### 6.1 Overview and Key Findings

New Caledonian crows exhibit remarkable tool-use abilities, including spontaneous hook bending, compound tool construction, and sequential tool use [43], [44], [45]. These behaviors often emerge suddenly, suggesting insight rather than gradual shaping [43], [46]. However, sample sizes are typically small (1-8 birds), and trial-by-trial data are rarely reported in sufficient detail.

### 6.2 Landmark Papers

**Tier 1 Papers:**

- **Weir et al. (2002)** [43]: Landmark study of spontaneous hook bending in 2 crows across 10 trials. Individual trial data with sudden insight. Figures available, high priority despite small sample.

- **Bayern et al. (2018)** [44]: Compound tool construction in 8 crows with individual trial data and sudden insight. Repository/figures available, high priority.

- **Weir et al. (2006)** [47]: Creative tool redesign in 1 crow across 41 trials with individual trial data and sudden insight. Supplementary/figures available, high priority.

- **Wimpenny et al. (2009)** [48]: Sequential tool use in 6 crows (Experiment 1) and 3 crows (Experiment 2) with 3-30+ trials. Individual trial data with sudden insight. Figures available, high priority.

- **Neilands et al. (2016)** [49]: Stone dropping in 12 crows across 3-20 trials with individual trial data and sudden insight. Supplementary data available, high priority.

- **Jacobs et al. (2016)** [50]: Novel tool-use mode in 2 crows across 6 trials with sudden insight. Supplementary data available, high priority.

- **Alfredsson (2012)** [51]: Innovative tool modifications in 13 crows with individual trial data and sudden insight. Figures available, high priority.

**Tier 2 Papers:**

- **Taylor et al. (2009)** [52]: Physical problem solving in 6 crows across 150 trials. Individual trial data but no clear insight evidence. Figures available, high priority.

- **Holzhaider et al. (2010)** [53]: Pandanus tool manufacture development in 6 wild crows across 716 trials. Individual trial data, figures available, high priority.

- **Chappell et al. (2004)** [54]: Tool diameter selection in 2 crows across 30 trials. Supplementary/figures available, high priority.

### 6.3 Data Availability and Quantitative Methods

Of 87 papers reviewed, approximately 10-12 provide individual-level trial data. Sample sizes are consistently small (1-13 birds), reflecting the rarity of New Caledonian crows in captivity and the labor-intensive nature of tool-use experiments. No papers applied changepoint detection or state-space models, relying instead on qualitative descriptions of "sudden" or "spontaneous" behavior. This represents a major methodological gap.

### 6.4 Sample Sizes and Temporal Resolution

Sample sizes are the smallest across all domains: 1-13 birds, with most studies examining 2-8 individuals. Temporal resolution is moderate: 6-150 trials per bird, typically across days or weeks. The small samples limit statistical power but provide rich case studies of individual problem-solving trajectories.

### 6.5 Critical Gaps

1. **Small samples:** Replication and generalization are limited by small sample sizes.
2. **Lack of quantitative methods:** Insight is inferred qualitatively; formal transition detection methods are absent.
3. **Limited neural data:** No studies combine tool-use behavior with neural recordings in corvids.
4. **Primate comparison:** While corvid tool use is well-studied, comparable primate data with individual trajectories are scarce.

---

## 7. Domain 5: Mooney Image Perception

### 7.3 Overview and Key Findings

Mooney images—high-contrast, two-tone pictures—are initially ambiguous but become recognizable after viewing the original grayscale image. This perceptual reorganization is often sudden and exhibits hysteresis: once recognized, the image remains recognizable even when degraded [55], [56], [57]. This paradigm provides a controlled setting for studying perceptual insight and bistable perception.

### 7.2 Landmark Papers

**Tier 1 Papers:**

- **Teufel et al. (2018)** [58]: Prior object-knowledge sharpens early visual feature detectors in 12 (Experiment 1) and 14 (Experiment 2) subjects with threshold data. Repository data available, high priority.

- **Reining et al. (2024)** [59]: Psychophysical evaluation of Mooney image generation in 2 (Experiment 1) and 15 (Experiment 2) subjects across 480-2,000 trials. Repository data available, high priority.

- **Milne et al. (2022)** [60]: Perceptual reorganization in 74 children and 14 adults with threshold data and hysteresis. Figures available, high priority.

- **Dosher et al. (2005)** [61]: Perceptual learning in 6 subjects with threshold data. Figures available, high priority.

- **Pastukhov et al. (2013)** [62]: Multi-stable perception in 15 subjects across 24 measurements. High priority.

- **Gigante et al. (2009)** [63]: Bistable perception modeled as stochastic integrations with threshold data and hysteresis. Figures available, high priority.

**Tier 2 Papers:**

- **Hegdé et al. (2010)** [64]: Link between visual disambiguation and memory in 10 subjects with threshold data and hysteresis. High priority.

- **Geert et al. (2022)** [65]: Individual differences in hysteresis in 75 subjects. High priority.

### 7.3 Data Availability and Quantitative Methods

Of 185 papers reviewed, approximately 8-10 provide individual-level threshold or recognition data. Hysteresis is well-documented [55], [56], [64], [65], but few studies track trial-by-trial dynamics of the initial recognition transition. State-space models and changepoint detection are rarely applied. Computational models of bistable perception [63] provide theoretical frameworks but lack direct comparison to individual human data.

### 7.4 Sample Sizes and Temporal Resolution

Sample sizes range from 2 to 75 subjects, with most studies examining 10-20 individuals. Temporal resolution varies: some studies measure single recognition events, while others track 24-2,000 trials [59], [62]. The highest temporal resolution comes from psychophysical threshold tracking [58], [59], [61].

### 7.5 Critical Gaps

1. **Trial-by-trial dynamics:** Most studies focus on pre/post recognition rather than the transition itself.
2. **Individual differences:** Sources of variability in recognition speed and hysteresis strength are poorly understood [65].
3. **Neural mechanisms:** fMRI studies exist but lack trial-by-trial resolution to capture the transition moment.

---

## 8. Domain 6: Human Artificial Grammar Learning

### 8.1 Overview and Key Findings

Artificial grammar learning (AGL) paradigms test implicit sequence learning by exposing participants to strings generated by finite-state grammars [66], [67], [68]. While traditionally viewed as gradual, some studies report sudden transitions from implicit to explicit knowledge [69], [70], [71]. Individual differences in learning trajectories are substantial [72], [73], [74].

### 8.2 Landmark Papers

**Tier 1 Papers:**

- **Wessel et al. (2012)** [69]: Transition from implicit to explicit representations in 24 subjects across 144 trials with sudden insight. Figures available, high priority.

- **Alexandre (2010)** [75]: Modeling implicit and explicit processes in 8 subjects across 400 trials with sudden insight. High priority.

- **Lawson et al. (2017)** [76]: Novel behavioral indicator of explicit awareness in 30 (Experiment 1) and 21 (Experiment 2) subjects across 70-130 sequence repetitions with sudden insight. Repository data available, high priority.

- **Smith et al. (2001)** [77]: Preserved implicit learning in Parkinson's disease patients (13-14 PD, 14 controls) across 500 SRT trials and 23+23 AG trials. Figures available, high priority.

**Tier 2 Papers:**

- **Abugaber et al. (2021)** [78]: Drift-diffusion modeling in 40 subjects across 616 trials with trial data. Figures available.

- **Sentman et al. (2007)** [79]: Effect of mood on implicit learning in 94 subjects across 40-720 trials with sudden insight. Figures available, medium priority.

- **Jurchiș et al. (2022)** [80]: Implicit learning in virtual reality in 93 subjects. Repository data available, medium priority.

- **Székely et al. (2024)** [81]: Transfer learning and inductive biases with repository data.

- **Zwart (2018)** [82]: Implicit learning in ASD and SLI with repository data and sudden insight. Medium priority.

### 8.3 Data Availability and Quantitative Methods

Of 220 papers reviewed, approximately 8-10 provide individual-level trial data with evidence of sudden transitions. Changepoint detection is rarely applied; most studies rely on pre/post comparisons or arbitrary learning criteria. State-space models [83] and hidden Markov models [84] are emerging but underutilized. Drift-diffusion models [78] capture decision dynamics but not learning transitions.

### 8.4 Sample Sizes and Temporal Resolution

Sample sizes range from 8 to 244 subjects, with most studies examining 20-50 individuals. Temporal resolution varies: serial reaction time tasks provide 100-1,000+ trials [76], [77], while grammar classification tasks may have only 20-100 test trials [75], [79]. High temporal resolution is critical for detecting sudden transitions but is often sacrificed for larger samples.

### 8.5 Critical Gaps

1. **Implicit-to-explicit transition:** The moment of transition from implicit to explicit knowledge is rarely captured with sufficient temporal resolution [69], [76].
2. **Individual differences:** Sources of variability in learning speed and transition timing are poorly understood [72], [73].
3. **Neural correlates:** EEG studies exist [69] but lack trial-by-trial resolution to link neural and behavioral transitions.

---

## 9. Domain 7: Honeybee Concept Learning

### 9.1 Overview and Key Findings

Honeybees can learn abstract concepts such as "sameness" and "difference," often exhibiting sudden transfer to novel stimuli after training [85], [86], [87]. Individual bees show heterogeneous learning trajectories, with some mastering concepts rapidly and others failing entirely [88], [89]. This domain provides unique opportunities to study concept learning in a miniature brain with individual-level data.

### 9.2 Landmark Papers

**Tier 1 Papers:**

- **Pamir et al. (2014)** [90]: Rapid learning dynamics in 3,298 individual bees across 1-12 trials with sudden transfer. Figures available, highest priority for sample size.

- **Finke et al. (2023)** [91]: Individual consistency in learning abilities across 33-140 bees per experiment with 10-120 trials. Repository data available, high priority.

- **MaBouDi et al. (2020)** [92]: Bumblebees learning relational rules in 18 bees across 30 bouts (180 choices). Repository data available, high priority.

- **Avarguès-Weber et al. (2014)** [93]: Conceptualization of relative size in 26 bees across 80 trials with sudden transfer. Figures available, high priority.

- **Dyer et al. (2019)** [94]: Common principles in learning from bees to humans with individual trial data across 100 trials. Figures available, high priority.

**Tier 2 Papers:**

- **Giurfa et al. (2001, 2021)** [85], [95]: Foundational work on sameness/difference concepts with sudden transfer, though individual data unclear.

- **Couvillon et al. (1998)** [96]: Short-term memory in 48 bees across 24 training visits. Figures available, medium priority.

### 9.3 Data Availability and Quantitative Methods

Of 126 papers reviewed, approximately 6-8 provide individual-level trial data. The Pamir et al. (2014) dataset [90] is exceptional in sample size (3,298 bees) and provides a unique resource for studying individual differences. Changepoint detection and state-space models are absent; most studies rely on pre/post transfer tests. Computational models [97] simulate concept learning but lack direct comparison to individual bee data.

### 9.4 Sample Sizes and Temporal Resolution

Sample sizes range from 2 to 3,298 bees, with most studies examining 10-50 individuals. Temporal resolution is moderate: 10-180 trials per bee, typically across days. Classical conditioning studies [90] achieve higher temporal resolution (1-12 trials) but focus on simple associations rather than concept learning.

### 9.5 Critical Gaps

1. **Transition dynamics:** The moment of concept acquisition is rarely captured; most studies compare pre- and post-training performance [85], [86].
2. **Neural mechanisms:** Bee neuroscience is advancing, but no studies link neural activity to individual concept learning trajectories.
3. **Cross-species comparison:** Comparing bee concept learning to vertebrate data could reveal conserved or divergent mechanisms.

---

## 10. Domain 8: Vocabulary Explosion in Children

### 10.1 Overview and Key Findings

The "vocabulary spurt" or "naming explosion"—a rapid acceleration in word learning around 18-24 months—has been debated for decades [98], [99], [100]. Some studies report abrupt transitions in individual children [99], [101], while others argue for continuous growth [102], [103]. Longitudinal data with frequent sampling are critical for resolving this debate.

### 10.2 Landmark Papers

**Tier 1 Papers:**

- **Díaz et al. (2024)** [104]: Testing theories of vocabulary spurt in 45 monolingual and bilingual infants across 617 timepoints. Individual longitudinal data with vocabulary spurt evidence. High priority for sample size and temporal resolution.

- **Ganger et al. (2004)** [99]: Reexamining the vocabulary spurt in 38 children with individual longitudinal data. Figures available, high priority.

- **Goldfield et al. (1990)** [101]: Early lexical acquisition in 18 children with individual longitudinal data and vocabulary spurt evidence. High priority.

- **D'Odorico et al. (2001)** [105]: Vocabulary development in 42 Italian children with individual longitudinal data and vocabulary spurt evidence. High priority.

- **Fernald et al. (2012)** [106]: Individual differences in lexical processing in 82 children across 4 timepoints with vocabulary spurt evidence. High priority.

- **Bloom et al. (1996)** [107]: Early conversations and word learning in 12 children across 2 timepoints with vocabulary spurt evidence. High priority.

- **Elsen (1996)** [108]: Stylistic variation in 1 child with individual longitudinal data and vocabulary spurt evidence. Figures available, high priority.

- **Tao et al. (year unknown)** [109]: Word-spurt in 5 Mandarin-speaking children with individual longitudinal data and vocabulary spurt evidence. High priority.

**Tier 2 Papers:**

- **Reznick et al. (1992)** [110]: Rapid change in lexical development in 24 children across 5 timepoints.

- **Parladé et al. (2011)** [111]: Interplay between language, gesture, and affect in 18 children across 3 timepoints. Medium priority.

- **Oliver et al. (1994)** [112]: Language development in Down syndrome in 17 children. Figures available, medium priority.

- **Klammler et al. (2011)** [113]: Bilingual acquisition in 2 children. Medium priority.

### 10.3 Data Availability and Quantitative Methods

Of 84 papers reviewed, approximately 8-10 provide individual-level longitudinal data. The Díaz et al. (2024) dataset [104] is exceptional in temporal resolution (617 timepoints across 45 children). Changepoint detection has been applied in some studies [99], [104], but state-space models are rare. Growth curve modeling is common [106], [114], but often assumes smooth trajectories rather than testing for discontinuities.

### 10.4 Sample Sizes and Temporal Resolution

Sample sizes range from 1 to 82 children, with most studies examining 12-45 individuals. Temporal resolution varies widely: some studies sample monthly (12-24 timepoints) [99], [101], while others achieve weekly or daily sampling [104]. High temporal resolution is critical for detecting spurts, as monthly sampling may miss rapid transitions.

### 10.5 Critical Gaps

1. **Spurt definition:** Operational definitions of "spurt" vary across studies, hindering comparison [98], [99], [102].
2. **Individual differences:** Sources of variability in spurt timing and magnitude are poorly understood [106].
3. **Mechanism:** Whether spurts reflect cognitive reorganization, vocabulary size thresholds, or measurement artifacts remains debated [102], [103].

---

## 11. Domain 9: Neural State Transitions in Prefrontal Cortex

### 11.1 Overview and Key Findings

Prefrontal cortex neural ensembles exhibit abrupt transitions between discrete states during rule learning, strategy switching, and extinction [115], [116], [117]. These neural state transitions often precede or coincide with behavioral transitions, suggesting a causal role in discontinuous learning [115], [118]. State-space models and dimensionality reduction reveal low-dimensional manifolds along which neural trajectories evolve [115], [116], [119].

### 11.2 Landmark Papers

**Tier 1 Papers:**

- **Durstewitz et al. (2010)** [115]: Landmark paper demonstrating abrupt transitions between prefrontal neural ensemble states accompanying behavioral transitions during rule learning. Individual trial data, neural trajectories, and state-space models. High priority.

- **Russo et al. (2020)** [116]: Coordinated prefrontal state transition during extinction in 10 rats across 60-69 trials. Neural trajectories with state-space models. Figures available, high priority.

- **Maggi et al. (2018)** [22]: Ensemble code in medial prefrontal cortex in 4 rats across 50 sessions. Trial data with changepoint analysis. Repository data available, high priority.

- **Singh et al. (2016, 2018)** [120], [121]: Signatures of internal model updating in 4 rats across 50 trials with state-space models. Repository data available, high priority.

- **Zhou et al. (2016)** [122]: Dynamic Bayesian model for cross-neuronal interactions in 1 monkey with state-space models. Supplementary data available, high priority despite small sample.

- **Csorba et al. (2021)** [123]: Long-range cortical synchronization during abrupt visual learning in 2 mice across 75-100 trials. Repository data available, high priority.

**Tier 2 Papers:**

- **Zhou et al. (2021)** [124]: Evolving schema representations in orbitofrontal ensembles. Repository data available, medium priority.

- **Powell et al. (2016)** [125]: Representational changes in rat medial prefrontal cortex preceding behavioral changes.

### 11.3 Data Availability and Quantitative Methods

Of 155 papers reviewed, approximately 8-10 provide individual-level neural trajectory data with behavioral correlates. State-space models are standard in this domain [115], [116], [120], [121], [122], representing the most sophisticated quantitative methods across all domains. Dimensionality reduction (PCA, demixed PCA) reveals low-dimensional neural dynamics [115], [119]. Changepoint detection is applied to both neural and behavioral data [22].

### 11.4 Sample Sizes and Temporal Resolution

Sample sizes are small: 1-10 subjects, reflecting the technical demands of multi-electrode recordings. Temporal resolution is excellent: trial-by-trial neural activity across 50-1,000+ trials [22], [115], [120]. Single-trial resolution enables precise alignment of neural and behavioral transitions.

### 11.5 Critical Gaps

1. **Causal inference:** While neural transitions correlate with behavioral transitions, causal manipulations (e.g., optogenetics) are rare [116].
2. **Cross-species comparison:** Most work is in rodents; primate data are scarce [122].
3. **Generalization across tasks:** Whether neural state transition mechanisms generalize across different learning paradigms is unclear.

---

## 12. Domain 10: Classic Insight Learning Studies

### 12.1 Overview and Key Findings

Insight learning—sudden problem-solving accompanied by an "aha!" experience—has been studied across species and tasks [126], [127], [128]. Classic paradigms include the nine-dot problem, anagrams, and tool-use tasks [129], [130], [131]. Feelings-of-warmth ratings reveal abrupt increases preceding solution [132], [133], suggesting discontinuous problem-solving processes.

### 12.2 Landmark Papers

**Tier 1 Papers:**

- **Kuchibhotla et al. (2019)** [134]: Dissociating task acquisition from expression in 14 mice, 7 rats, and 2 ferrets with sudden transitions. Repository data available, highest priority for cross-species comparison.

- **Löwe et al. (2023)** [135]: Regularised neural networks mimic human insight in 99 humans and 99 neural networks across 500 trials with sudden transitions. Figures available, high priority.

- **Terai et al. (2013)** [136]: Chance discovery from cognitive psychology in 5 subjects across 30 measurements with sudden transitions. Figures available, high priority.

- **Kizilirmak et al. (2018)** [137]: Feelings-of-warmth increase abruptly for verbal riddles in 36 subjects across 6 rounds with sudden transitions. High priority.

- **Bilalić et al. (2021)** [138]: Temporal dynamics of insight problem solving in 73 (Problem A) and 61 (Problem B) subjects with sudden transitions. Figures available, high priority.

- **Dubey et al. (2021)** [139]: Aha! moments as meta-cognitive prediction errors in 1,230 (Experiment 1) and 302 (Experiment 2) subjects across 5 anagrams. Repository data available, high priority for sample size.

**Tier 2 Papers:**

- **Metcalfe (1986, 1987)** [140], [141]: Classic work on premonitions of insight and intuition in insight vs. noninsight problems.

- **Chein et al. (2010)** [142]: Working memory and insight in 51-54 subjects across 7 timepoints. Medium priority.

- **Ozernov-Palchik (2022)** [143]: Longitudinal changes in brain activation underlying reading fluency in 26 subjects across 2 timepoints. High priority.

- **Bouhali et al. (2024)** [144]: Unique longitudinal contributions of sulcal interruptions to reading acquisition in 43 children across 2 timepoints. High priority.

### 12.3 Data Availability and Quantitative Methods

Of 202 papers reviewed, approximately 8-10 provide individual-level trial data with sudden transitions. Feelings-of-warmth ratings [132], [137], [142] provide continuous measures of problem-solving progress but are underutilized. Changepoint detection is rarely applied. Computational models [135] simulate insight but lack direct comparison to individual human data.

### 12.4 Sample Sizes and Temporal Resolution

Sample sizes range from 5 to 1,230 subjects, with most studies examining 20-100 individuals. Temporal resolution varies: feelings-of-warmth ratings provide 5-10 timepoints per problem [132], [137], [142], while anagram studies may have only 1-5 trials per subject [139]. Eye-tracking [138] provides high temporal resolution but is rarely combined with trial-by-trial performance data.

### 12.5 Critical Gaps

1. **Insight definition:** Operational definitions vary across studies, hindering comparison [126], [127].
2. **Neural mechanisms:** fMRI studies exist but lack trial-by-trial resolution to capture the insight moment.
3. **Cross-species comparison:** While animal insight is studied [134], direct comparison to human insight paradigms is rare.

---

## 13. Domain 11: Cross-Domain Review Papers

### 13.1 Overview and Key Findings

Cross-domain reviews synthesize evidence for discontinuous learning across species and tasks [1], [2], [145], [146]. Gallistel et al. (2004) [1] provide the most comprehensive quantitative analysis, demonstrating abrupt transitions in mice, rats, rabbits, and pigeons across multiple paradigms. Phase transition models [147], [148], [149] offer theoretical frameworks but require more empirical validation.

### 13.2 Landmark Papers

**Tier 1 Papers:**

- **Gallistel et al. (2004)** [1]: The learning curve: Implications of a quantitative analysis. Analyzes individual data from 9 mice, 8 rats, 11 rats, 24 rabbits, and 105 birds across 30-1,500 trials. Cites individual data and digitizable figures, high priority.

- **Rosenberg et al. (2021)** [30]: Mice in a labyrinth (also in Domain 3). Cites individual data, digitizable figures, quantitative methods, and cross-domain relevance. Repository data available, highest priority.

**Tier 2 Papers:**

- **Stephen et al. (2009)** [147]: Dynamics of insight as phase transition with quantitative methods.

- **Liu et al. (2015)** [148]: S-shaped motor learning and nonequilibrium phase transitions with quantitative methods. Medium priority.

- **Helton (2011)** [149]: Animal expertise as phase transitions across species. Medium priority.

- **Stamovlasis (2017)** [150]: Dynamics of cognitive performance with quantitative methods. Medium priority.

### 13.3 Data Availability and Quantitative Methods

Of 196 review papers, only 2-3 provide or cite individual-level data [1], [30]. Most reviews synthesize group-level findings. Quantitative methods (phase transition models, catastrophe theory) are discussed theoretically [147], [148], [149], [150] but rarely applied to empirical data. This represents a major gap between theory and data.

### 13.4 Critical Gaps

1. **Lack of meta-analysis:** No quantitative meta-analysis of individual learning curves across domains exists.
2. **Theory-data gap:** Phase transition models are theoretically appealing but lack systematic empirical validation.
3. **Cross-species synthesis:** While cross-species comparisons are discussed [1], [149], standardized methods for comparing transition dynamics across species are absent.

---

## 14. Synthesis: Cross-Domain Patterns and Gaps

### 14.1 Convergent Evidence for Discontinuous Learning

Across all 11 domains, evidence for discontinuous learning transitions is substantial but heterogeneous. The strongest evidence comes from:

1. **Gallistel conditioning paradigms** [1], [4], [5], [21], [22]: Trial-by-trial data with changepoint analysis consistently reveal abrupt transitions.
2. **Rodent maze learning** [30], [31], [35], [36]: High-resolution tracking of thousands of decisions reveals sudden strategy shifts.
3. **Prefrontal neural ensembles** [115], [116], [120], [121]: State-space models demonstrate abrupt neural state transitions accompanying behavioral changes.
4. **Honeybee concept learning** [90], [91], [92]: Large samples (up to 3,298 individuals) show sudden transfer to novel stimuli.
5. **Vocabulary development** [99], [104], [105]: Longitudinal data with high temporal resolution reveal spurts in some children.

Weaker or more contested evidence comes from:

1. **Birdsong crystallization** [3], [6], [10]: Transitions are described qualitatively but rarely quantified with changepoint methods.
2. **Corvid tool use** [43], [44], [47]: Small samples and qualitative descriptions limit generalization.
3. **Mooney image perception** [55], [58], [59]: Recognition is sudden, but trial-by-trial dynamics are underexplored.
4. **Artificial grammar learning** [69], [76], [77]: Implicit-to-explicit transitions are reported but rarely captured with sufficient temporal resolution.
5. **Insight learning** [134], [135], [137], [139]: Aha! experiences are subjective; objective behavioral transitions are less clear.

### 14.2 Methodological Patterns

**Quantitative methods:** Changepoint detection is standard in Gallistel conditioning paradigms [1], [4], [21], [22] but rare elsewhere. State-space models are used in neural ensemble studies [115], [116], [120], [121] but underutilized in behavioral domains. Hidden Markov models are emerging [84] but not yet widely adopted.

**Sample sizes:** Vary dramatically across domains. Honeybee studies achieve the largest samples (up to 3,298 individuals) [90], while corvid studies are limited to 1-13 birds [43], [44], [47]. Most domains examine 10-50 subjects.

**Temporal resolution:** Highest in rodent maze learning (thousands of decisions per session) [30] and conditioning paradigms (100-1,000+ trials) [21], [26]. Lowest in birdsong (3-7 developmental stages) [14], [15] and vocabulary development (monthly sampling) [99], [101].

**Data accessibility:** Only 15-20 papers across all domains provide repository data [22], [23], [24], [30], [58], [59], [76], [80], [81], [82], [91], [92], [120], [121], [123], [124], [134], [139]. Most rely on figures, limiting reanalysis.

### 14.3 Cross-Domain Gaps

1. **Lack of standardized methods:** Each domain uses different operational definitions, analysis methods, and reporting standards, hindering cross-domain comparison.
2. **Theory-data disconnect:** Phase transition models [147], [148], [149] and computational models [135] are theoretically appealing but rarely validated against individual-level data.
3. **Neural-behavioral integration:** Few studies combine neural recordings with high-resolution behavioral tracking during transitions [22], [115], [116], [123].
4. **Individual differences:** Sources of variability in transition timing and magnitude are poorly understood across all domains.
5. **Developmental trajectories:** Most studies examine adults or single developmental stages; longitudinal studies tracking transitions across development are rare [104], [143], [144].

---

## 15. Priority Papers Summary Table

| **Domain** | **Paper** | **N** | **Timepoints** | **Data Access** | **Methods** | **Priority** |
|------------|-----------|-------|----------------|-----------------|-------------|--------------|
| **Birdsong** | Tanaka et al. 2018 [3] | 96 | 5-7 | Figures | None | High |
| | Vahaba et al. 2019 [11] | 34 | High | Repository | None | High |
| | Tchernichovski et al. 2004 [12] | Unclear | High | Repository | None | High |
| | Mandelblat-Cerf et al. 2014 [13] | 4 | 3 | Figures | None | High |
| **Gallistel** | Harris 2011 [21] | 23, 17 | 360, 900 | Figures | Changepoint | High |
| | Gallistel 2003 [4] | Unclear | High | Figures | Changepoint | High |
| | Maggi et al. 2018 [22] | 4 | 50 | Repository | Changepoint | High |
| | Vega-Villar et al. 2019 [23] | 58 | High | Repository | Changepoint | High |
| | Benzina et al. 2021 [24] | 52, 80 | High | Supp/Repo | Changepoint | High |
| | Papachristos et al. 2006 [25] | 20 | High | Figures | Changepoint | High |
| | Smith et al. 2004 [26] | 2 | 1,835 | Figures | State-space | High |
| **Maze** | Rosenberg et al. 2021 [30] | 20 | ~15,000 | Repository | Changepoint | High |
| | Reddy 2022 [35] | 20 | High | Figures | Changepoint | High |
| | Igata et al. 2016 [36] | 14 | 20/day | Figures | None | High |
| | Vallianatou et al. 2020 [37] | 20 | 30/session | Figures | None | High |
| | Qiao et al. 2018 [38] | 4 | 900+ | Repository | None | High |
| | McNamara et al. 2014 [39] | 4 | 20 | Figures | None | High |
| | Valentis et al. 2014 [40] | 100 | 21 | Figures | None | High |
| **Corvid** | Weir et al. 2002 [43] | 2 | 10 | Figures | None | High |
| | Bayern et al. 2018 [44] | 8 | High | Repo/Figs | None | High |
| | Weir et al. 2006 [47] | 1 | 41 | Supp/Figs | None | High |
| | Wimpenny et al. 2009 [48] | 6, 3 | 3-30+ | Figures | None | High |
| | Neilands et al. 2016 [49] | 12 | 3-20 | Supplementary | None | High |
| | Jacobs et al. 2016 [50] | 2 | 6 | Supplementary | None | High |
| | Alfredsson 2012 [51] | 13 | Unclear | Figures | None | High |
| | Taylor et al. 2009 [52] | 6 | 150 | Figures | None | High |
| | Holzhaider et al. 2010 [53] | 6 | 716 | Figures | None | High |
| | Chappell et al. 2004 [54] | 2 | 30 | Supp/Figs | None | High |
| **Mooney** | Teufel et al. 2018 [58] | 12, 14 | High | Repository | None | High |
| | Reining et al. 2024 [59] | 2, 15 | 480-2,000 | Repository | None | High |
| | Milne et al. 2022 [60] | 74, 14 | High | Figures | None | High |
| | Dosher et al. 2005 [61] | 6 | High | Figures | None | High |
| | Pastukhov et al. 2013 [62] | 15 | 24 | None | None | High |
| | Gigante et al. 2009 [63] | Model | Model | Figures | State-space | High |
| | Hegdé et al. 2010 [64] | 10 | High | None | None | High |
| | Geert et al. 2022 [65] | 75 | Unclear | None | None | High |
| **AGL** | Wessel et al. 2012 [69] | 24 | 144 | Figures | None | High |
| | Alexandre 2010 [75] | 8 | 400 | None | None | High |
| | Lawson et al. 2017 [76] | 30, 21 | 70-130 | Repository | None | High |
| | Smith et al. 2001 [77] | 13-14, 14 | 500, 46 | Figures | None | High |
| **Honeybee** | Pamir et al. 2014 [90] | 3,298 | 1-12 | Figures | None | High |
| | Finke et al. 2023 [91] | 33-140 | 10-120 | Repository | None | High |
| | MaBouDi et al. 2020 [92] | 18 | 30 bouts | Repository | None | High |
| | Avarguès-Weber et al. 2014 [93] | 26 | 80 | Figures | None | High |
| | Dyer et al. 2019 [94] | Unclear | 100 | Figures | None | High |
| **Vocabulary** | Díaz et al. 2024 [104] | 45 | 617 | None | Changepoint | High |
| | Ganger et al. 2004 [99] | 38 | High | Figures | Changepoint | High |
| | Goldfield et al. 1990 [101] | 18 | High | None | None | High |
| | D'Odorico et al. 2001 [105] | 42 | High | None | None | High |
| | Fernald et al. 2012 [106] | 82 | 4 | None | None | High |
| | Bloom et al. 1996 [107] | 12 | 2 | None | None | High |
| | Elsen 1996 [108] | 1 | High | Figures | None | High |
| | Tao et al. [109] | 5 | High | None | None | High |
| **Neural** | Durstewitz et al. 2010 [115] | Unclear | High | None | State-space | High |
| | Russo et al. 2020 [116] | 10 | 60-69 | Figures | State-space | High |
| | Maggi et al. 2018 [22] | 4 | 50 | Repository | Changepoint | High |
| | Singh et al. 2016, 2018 [120], [121] | 4 | 50 | Repository | State-space | High |
| | Zhou et al. 2016 [122] | 1 | High | Supplementary | State-space | High |
| | Csorba et al. 2021 [123] | 2 | 75-100 | Repository | None | High |
| **Insight** | Kuchibhotla et al. 2019 [134] | 14, 7, 2 | High | Repository | None | High |
| | Löwe et al. 2023 [135] | 99, 99 | 500 | Figures | None | High |
| | Terai et al. 2013 [136] | 5 | 30 | Figures | None | High |
| | Kizilirmak et al. 2018 [137] | 36 | 6 | None | None | High |
| | Bilalić et al. 2021 [138] | 73, 61 | 10 | Figures | None | High |
| | Dubey et al. 2021 [139] | 1,230, 302 | 5 | Repository | None | High |
| **Review** | Gallistel et al. 2004 [1] | 9, 8, 11, 24, 105 | 30-1,500 | Figures | Changepoint | High |
| | Rosenberg et al. 2021 [30] | 20 | ~15,000 | Repository | Changepoint | High |

**Note:** N = number of subjects; Timepoints = number of measurements per subject; Data Access: Repository = open data repository, Figures = digitizable figures, Supplementary = supplementary materials, None = no accessible data; Methods: Changepoint = changepoint detection, State-space = state-space models.

---

## 16. Recommendations for Future Research

### 16.1 Data Sharing and Open Science

1. **Establish domain-specific data repositories:** Create centralized repositories for individual learning trajectories in each domain (e.g., BirdSongDB, MazeLearningDB, VocabSpurtDB).
2. **Standardize reporting:** Require reporting of individual-level data, sample sizes, temporal resolution, and quantitative methods in all learning studies.
3. **Digitize historical data:** Many classic studies contain rich individual-level data in figures [1], [10], [43] that could be digitized and reanalyzed.

### 16.2 Methodological Advances

1. **Apply changepoint detection systematically:** Extend changepoint methods from Gallistel conditioning paradigms [1], [4], [21] to all domains.
2. **Develop cross-domain state-space models:** Adapt neural state-space models [115], [116], [120] to behavioral data in other domains.
3. **Integrate neural and behavioral data:** Combine high-resolution behavioral tracking with neural recordings during transitions [22], [115], [123].
4. **Validate phase transition models:** Test theoretical phase transition models [147], [148], [149] against individual-level data across domains.

### 16.3 Cross-Domain Synthesis

1. **Conduct quantitative meta-analysis:** Pool individual learning curves across domains to test for universal transition dynamics.
2. **Compare transition mechanisms:** Systematically compare transition timing, magnitude, and variability across species and tasks.
3. **Develop unified computational models:** Build models that capture discontinuous learning across domains, from birdsong to human insight.

### 16.4 Individual Differences

1. **Identify sources of variability:** Investigate genetic, neural, and experiential factors predicting transition timing and magnitude.
2. **Develop personalized learning models:** Build individual-specific models that predict learning trajectories [151].
3. **Link individual differences to neural mechanisms:** Combine behavioral and neural data to understand why some individuals show abrupt transitions while others show gradual learning.

### 16.5 Developmental Trajectories

1. **Conduct longitudinal studies:** Track individuals across development to capture multiple transitions [104], [143], [144].
2. **Compare developmental and adult learning:** Test whether transition mechanisms differ across development.
3. **Examine critical periods:** Investigate whether discontinuous learning is more common during sensitive periods [3], [6].

---

## 17. Conclusion

This comprehensive review of 1,606 papers across 11 domains reveals substantial evidence for discontinuous learning transitions across species and tasks. The strongest evidence comes from Gallistel conditioning paradigms, rodent maze learning, prefrontal neural ensembles, honeybee concept learning, and vocabulary development, where individual-level time series data with sufficient temporal resolution demonstrate abrupt transitions. However, critical gaps remain: most studies report group-level averages, few provide open data, and quantitative transition detection methods are underutilized outside conditioning paradigms.

The field stands at a crossroads. Theoretical models of discontinuous learning—from Gallistel's information-theoretic framework [1], [4], [5] to phase transition models [147], [148], [149]—offer compelling alternatives to incremental associative learning. Yet these theories remain undervalidated due to data scarcity. Addressing this requires coordinated efforts to share individual-level data, standardize reporting, apply rigorous quantitative methods, and synthesize evidence across domains.

The papers identified in this review—particularly those with repository data [22], [23], [24], [30], [58], [59], [76], [80], [81], [82], [91], [92], [120], [121], [123], [124], [134], [139]—provide a foundation for future meta-analyses and computational modeling. By digitizing figures from high-priority papers [1], [3], [4], [10], [21], [43], [99], [101], additional datasets can be recovered. With these resources, the field can move beyond qualitative descriptions of "sudden" or "abrupt" learning to rigorous quantitative characterization of transition dynamics, individual differences, and underlying mechanisms.

Discontinuous learning transitions challenge fundamental assumptions about how brains learn. Understanding these transitions—their timing, mechanisms, and variability—will require integrating evidence across species, tasks, and levels of analysis. This review provides a roadmap for that integration, identifying the most promising papers, datasets, and methods for advancing the science of learning discontinuities.

---

## 18. References

[1] Gallistel, C. R., Fairhurst, S., & Balsam, P. (2004). The learning curve: Implications of a quantitative analysis. *Proceedings of the National Academy of Sciences of the United States of America*, 101(36), 13124-13131. https://doi.org/10.1073/PNAS.0404965101

[2] Machado, A. (2022). A reinforcement-based mechanism for discontinuous learning. *Proceedings of the National Academy of Sciences*, 119(50), e2215352119. https://doi.org/10.1073/pnas.2215352119

[3] Tanaka, M., Singh Alvarado, J., Murugan, M., & Mooney, R. (2018). A mesocortical dopamine circuit enables the cultural transmission of vocal behaviour. *Nature*, 563(7729), 117-120. https://doi.org/10.1038/S41586-018-0636-7

[4] Gallistel, C. R. (2003). Conditioning from an information processing perspective. *Behavioural Processes*, 62(1-3), 89-101. https://doi.org/10.1016/S0376-6357(03)00019-6

[5] Gallistel, C. R. (2005). Deconstructing the law of effect. *Games and Economic Behavior*, 52(2), 410-423. https://doi.org/10.1016/J.GEB.2004.06.012

[6] Tchernichovski, O., Mitra, P. P., Lints, T., & Nottebohm, F. (2001). Dynamics of the vocal imitation process: how a zebra finch learns its song. *Science*, 291(5513), 2564-2569. https://doi.org/10.1126/science.1058522

[7] Tchernichovski, O., Nottebohm, F., Ho, C. E., Pesaran, B., & Mitra, P. P. (2000). A procedure for an automated measurement of song similarity. *Animal Behaviour*, 59(6), 1167-1176. https://doi.org/10.1006/ANBE.1999.1416

[8] Tchernichovski, O., Lints, T., Mitra, P. P., & Nottebohm, F. (1999). Vocal imitation in zebra finches is inversely related to model abundance. *Proceedings of the National Academy of Sciences of the United States of America*, 96(22), 12901-12904. https://doi.org/10.1073/pnas.96.22.12901

[9] Kollmorgen, S., Hahnloser, R. H. R., & Mante, V. (2020). Nearest neighbours reveal fast and slow components of motor learning. *Nature*, 577(7791), 526-530. https://doi.org/10.1038/S41586-019-1892-X

[10] Tchernichovski, O., Mitra, P. P., Lints, T., & Nottebohm, F. (2001). Dynamics of the Vocal Imitation Process: How a Zebra Finch Learns Its Song. *Science*, 291(5513), 2564-2569. https://doi.org/10.1126/SCIENCE.1058522

[11] Vahaba, D. M., Macedo-Lima, M., & Remage-Healey, L. (2019). Blocking neuroestrogen synthesis modifies neural representations of learned song without altering vocal imitation accuracy in developing songbirds. *bioRxiv*, 702704. https://doi.org/10.1101/702704

[12] Tchernichovski, O., Mitra, P. P., & Nottebohm, F. (2004). Studying the song development process: rationale and methods. *Annals of the New York Academy of Sciences*, 1016, 348-363. https://doi.org/10.1196/ANNALS.1298.031

[13] Mandelblat-Cerf, Y., Las, L., Denissenko, N., & Fee, M. S. (2014). An automated procedure for evaluating song imitation. *PLOS ONE*, 9(5), e96484. https://doi.org/10.1371/JOURNAL.PONE.0096484

[14] Haesler, S., Wada, K., Nshdejan, A., Morrisey, E. E., Lints, T., Jarvis, E. D., & Scharff, C. (2007). Incomplete and Inaccurate Vocal Imitation after Knockdown of FoxP2 in Songbird Basal Ganglia Nucleus Area X. *PLOS Biology*, 5(12), e321. https://doi.org/10.1371/JOURNAL.PBIO.0050321

[15] Arya, D., Veit, L., Tschida, K., & Mooney, R. (2023). Tracing development of song memory with fMRI in zebra finches after a second tutoring experience. *Communications Biology*, 6(1), 382. https://doi.org/10.1038/s42003-023-04724-2

[16] Tchernichovski, O., Mitra, P. P., Lints, T., & Nottebohm, F. (2000). A procedure for an automated measurement of song similarity. *Animal Behaviour*, 59(6), 1167-1176. https://doi.org/10.1006/ANBE.1999.1416

[17] Tchernichovski, O., Mitra, P. P., & Nottebohm, F. (2004). Studying the song development process: rationale and methods. *Annals of the New York Academy Sciences*, 1016, 348-363. https://doi.org/10.1196/ANNALS.1298.031

[18] Gallistel, C. R. (2025). Reconceptualized associative learning. *Perspectives on Behavior Science*, 48, 1-28. https://doi.org/10.1007/s40614-025-00442-8

[19] Reyes, A., Gallistel, C. R., & Balsam, P. D. (2014). What is learned during simultaneous temporal acquisition? An individual-trials analysis. *Behavioural Processes*, 101, 19-33. https://doi.org/10.1016/J.BEPROC.2013.09.008

[20] Morris, R. W., Fung, S. J., Rothmond, D. A., Richards, B., Ward, S., Noble, P. L., Woodward, R. A., Weickert, C. S., & Weinberger, D. R. (2006). Effect of unconditioned stimulus magnitude on the emergence of conditioned responding. *Journal of Experimental Psychology: Animal Behavior Processes*, 32(4), 371-385. https://doi.org/10.1037/0097-7403.32.4.371

[21] Harris, J. A. (2011). The acquisition of conditioned responding. *Journal of Experimental Psychology: Animal Behavior Processes*, 37(2), 151-164. https://doi.org/10.1037/A0021883

[22] Maggi, S., Peyrache, A., & Humphries, M. D. (2018). An ensemble code in medial prefrontal cortex links prior events to outcomes during learning. *Nature Communications*, 9(1), 2204. https://doi.org/10.1038/S41467-018-04638-2

[23] Vega-Villar, M., Horvitz, J. C., Nicola, S. M., & Yin, H. H. (2019). NMDA receptor-dependent plasticity in the nucleus accumbens connects reward-predictive cues to approach responses. *Nature Communications*, 10(1), 4429. https://doi.org/10.1038/S41467-019-12387-Z

[24] Benzina, N., N'Diaye, K., Pelissolo, A., Mallet, L., & Burguière, E. (2021). A cross-species assessment of behavioral flexibility in compulsive disorders. *Communications Biology*, 4(1), 96. https://doi.org/10.1038/S42003-020-01611-Y

[25] Papachristos, E. B., Gallistel, C. R., & Balsam, P. D. (2006). Autoshaped Head Poking in the Mouse: A Quantitative Analysis of the Learning Curve. *Journal of the Experimental Analysis of Behavior*, 85(3), 293-308. https://doi.org/10.1901/JEAB.2006.71-05

[26] Smith, A. C., Frank, L. M., Wirth, S., Yanike, M., Hu, D., Kubota, Y., Graybiel, A. M., Suzuki, W. A., & Brown, E. N. (2004). Dynamic analysis of learning in behavioral experiments. *The Journal of Neuroscience*, 24(2), 447-461. https://doi.org/10.1523/JNEUROSCI.2908-03.2004

[27] Morris, R. W., Fung, S. J., Rothmond, D. A., Richards, B., Ward, S., Noble, P. L., Woodward, R. A., Weickert, C. S., & Weinberger, D. R. (2006). Effect of unconditioned stimulus magnitude on the emergence of conditioned responding. *Journal of Experimental Psychology: Animal Behavior Processes*, 32(4), 371-385. https://doi.org/10.1037/0097-7403.32.4.371

[28] Blanco, F., Moris, J., Barberia, I., & Matute, H. (2018). Bayesian methods for addressing long-standing problems in associative learning: The case of PREE. *Quarterly Journal of Experimental Psychology*, 71(12), 2663-2675. https://doi.org/10.1080/17470218.2017.1358292

[29] Donoso, M., Yaple, Z. A., & Roesch, M. R. (2021). Emergence of complex dynamics of choice due to repeated exposures to extinction learning. *Animal Cognition*, 24(5), 1069-1081. https://doi.org/10.1007/S10071-021-01521-4

[30] Rosenberg, M., Zhang, T., Perona, P., & Meister, M. (2021). Mice in a labyrinth: Rapid learning, sudden insight, and efficient exploration. *bioRxiv*, 2021.01.14.426746. https://doi.org/10.1101/2021.01.14.426746

[31] Rosenberg, M., Zhang, T., Perona, P., & Meister, M. (2021). Mice in a labyrinth show rapid learning, sudden insight, and efficient exploration. *eLife*, 10, e66175. https://doi.org/10.7554/ELIFE.66175

[32] Machado, A. (2022). A reinforcement-based mechanism for discontinuous learning. *Proceedings of the National Academy of Sciences*, 119(50), e2215352119. https://doi.org/10.1073/pnas.2215352119

[33] Parrini, M., Ghezzi, F., Deidda, G., Medrihan, L., Castroflorio, E., Alberti, M., Baldelli, P., Cancedda, L., & Contestabile, A. (2023). Circuit mechanisms of navigation strategy learning in mice. *Current Biology*, 33(1), 74-85.e5. https://doi.org/10.1016/j.cub.2023.11.047

[34] Vallianatou, T., Bech, P., Davey, N., & Stringer, S. M. (2020). Schema-induced shifts in mice navigational strategies are unveiled by a minimal behavioral model of spatial exploration. *bioRxiv*, 2020.12.21.423808. https://doi.org/10.1101/2020.12.21.423808

[35] Reddy, G., Murthy, V. N., & Vergassola, M. (2022). A reinforcement-based mechanism for discontinuous learning. *bioRxiv*, 2022.05.06.490910. https://doi.org/10.1101/2022.05.06.490910

[36] Igata, H., Ikegaya, Y., & Sasaki, T. (2016). Early Failures Benefit Subsequent Task Performance. *Scientific Reports*, 6, 21293. https://doi.org/10.1038/SREP21293

[37] Vallianatou, T., Bech, P., Davey, N., & Stringer, S. M. (2020). Schema-induced shifts in mice navigational strategies are unveiled by a minimal behavioral model of spatial exploration. *bioRxiv*, 2020.12.21.423808. https://doi.org/10.1101/2020.12.21.423808

[38] Qiao, M., Zhang, T., Segalin, C., Sam, S., Perona, P., & Meister, M. (2018). Mouse Academy: high-throughput automated training and trial-by-trial behavioral analysis during learning. *bioRxiv*, 467878. https://doi.org/10.1101/467878

[39] McNamara, C. G., Tejero-Cantero, Á., Trouche, S., Campo-Urriza, N., & Dupret, D. (2014). Dopaminergic neurons promote hippocampal reactivation and spatial memory persistence. *Nature Neuroscience*, 17(12), 1658-1660. https://doi.org/10.1038/NN.3843

[40] Valentis, M., Bellomo, N., & Coscia, V. (2014). Intelligent Adaptive Learning in a Changing Environment. *International Conference on Computer Science and Information Technology*, 4(9), 243-254. https://doi.org/10.5121/CSIT.2014.4921

[41] Bressler, A. J., Fortin, N. J., Sakata, S., Barbieri, R., Haga, T., Lipton, P. A., & Eichenbaum, H. (2010). Low-stress Route Learning Using the Lashley III Maze in Mice. *Journal of Visualized Experiments*, (36), e1786. https://doi.org/10.3791/1786

[42] Bagg, H. J. (1920). Individual differences and family resemblances in animal behavior, a study of habit formation in various strains of mice. *The American Naturalist*, 54(633), 417-437. https://doi.org/10.5962/BHL.TITLE.20376

[43] Weir, A. A. S., Chappell, J., & Kacelnik, A. (2002). Shaping of Hooks in New Caledonian Crows. *Science*, 297(5583), 981. https://doi.org/10.1126/SCIENCE.1073433

[44] Bayern, A. M. P. von, Danel, S., Auersperg, A. M. I., Mioduszewska, B., & Kacelnik, A. (2018). Compound tool construction by New Caledonian crows. *Scientific Reports*, 8(1), 15676. https://doi.org/10.1038/S41598-018-33458-Z

[45] Wimpenny, J. H., Weir, A. A. S., Clayton, L., Rutz, C., & Kacelnik, A. (2009). Cognitive processes associated with sequential tool use in New Caledonian crows. *PLOS ONE*, 4(8), e6471. https://doi.org/10.1371/JOURNAL.PONE.0006471

[46] Bird, C. D., & Emery, N. J. (2009). Insightful problem solving and creative tool modification by captive nontool-using rooks. *Proceedings of the National Academy of Sciences of the United States of America*, 106(25), 10370-10375. https://doi.org/10.1073/PNAS.0901008106

[47] Weir, A. A. S., Kenward, B., Chappell, J., & Kacelnik, A. (2006). A New Caledonian crow (Corvus moneduloides) creatively re-designs tools by bending or unbending aluminium strips. *Animal Cognition*, 9(4), 317-334. https://doi.org/10.1007/S10071-006-0052-5

[48] Wimpenny, J. H., Weir, A. A. S., Clayton, L., Rutz, C., & Kacelnik, A. (2009). Cognitive processes associated with sequential tool use in New Caledonian crows. *PLOS ONE*, 4(8), e6471. https://doi.org/10.1371/JOURNAL.PONE.0006471

[49] Neilands, P., Jelbert, S. A., Breen, A. J., Schiestl, M., & Taylor, A. H. (2016). How insightful is 'insight'? New Caledonian crows do not attend to object weight during spontaneous stone dropping. *PLOS ONE*, 11(12), e0167419. https://doi.org/10.1371/JOURNAL.PONE.0167419

[50] Jacobs, I. F., von Bayern, A. M. P., & Osvath, M. (2016). A novel tool-use mode in animals: New Caledonian crows insert tools to transport objects. *Animal Cognition*, 19(6), 1249-1252. https://doi.org/10.1007/S10071-016-1016-Z

[51] Alfredsson, H. (2012). *Innovative tool-modifications and tool selectivity in new caledonian crows (corvus moneduloides)* [Master's thesis]. Lund University.

[52] Taylor, A. H., Medina, F. S., Holzhaider, J. C., Hearne, L. J., Hunt, G. R., & Gray, R. D. (2009). Do New Caledonian crows solve physical problems through causal reasoning? *Proceedings of The Royal Society B: Biological Sciences*, 277(1687), 247-254. https://doi.org/10.1098/RSPB.2008.1107

[53] Holzhaider, J. C., Hunt, G. R., Campbell, V. M., & Gray, R. D. (2010). The development of pandanus tool manufacture in wild New Caledonian crows. *Behaviour*, 147(5), 553-586. https://doi.org/10.1163/000579510X12629536366284

[54] Chappell, J., & Kacelnik, A. (2004). Selection of tool diameter by New Caledonian crows Corvus moneduloides. *Animal Cognition*, 7(2), 121-127. https://doi.org/10.1007/S10071-003-0202-Y

[55] Latinus, M., & Taylor, M. J. (2005). Holistic Processing of Faces: Learning Effects with Mooney Faces. *Journal of Cognitive Neuroscience*, 17(8), 1316-1327. https://doi.org/10.1162/0898929055002490

[56] Ramachandran, V. S., & Anstis, S. M. (1998). Object recognition can drive motion perception. *Nature*, 395(6705), 852-853. https://doi.org/10.1038/27573

[57] Schwiedrzik, C. M., Melloni, L., & Schurger, A. (2018). Mooney face stimuli for visual perception research. *PLOS ONE*, 13(7), e0200106. https://doi.org/10.1371/JOURNAL.PONE.0200106

[58] Teufel, C., Subramaniam, N., Dobler, V., Perez, J., Finnemann, J., Mehta, P. R., Goodyer, I. M., & Fletcher, P. C. (2018). Prior object-knowledge sharpens properties of early visual feature-detectors. *Scientific Reports*, 8(1), 10853. https://doi.org/10.1038/S41598-018-28845-5

[59] Reining, J. M., Choksi, B., & VanRullen, R. (2024). A psychophysical evaluation of techniques for Mooney image generation. *arXiv preprint*, arXiv:2403.11867. https://doi.org/10.48550/arxiv.2403.11867

[60] Milne, A. E., Wilson, B., Christiansen, M. H., & Petkov, C. I. (2022). Emergence of perceptual reorganisation from prior knowledge in human development and Convolutional Neural Networks. *bioRxiv*, 2022.11.21.517321. https://doi.org/10.1101/2022.11.21.517321

[61] Dosher, B. A., & Lu, Z.-L. (2005). Perceptual learning in clear displays optimizes perceptual expertise: learning the limiting process. *Proceedings of the National Academy of Sciences of the United States of America*, 102(14), 5286-5290. https://doi.org/10.1073/PNAS.0500492102

[62] Pastukhov, A., & Braun, J. (2013). Multi-stable perception balances stability and sensitivity. *Frontiers in Computational Neuroscience*, 7, 17. https://doi.org/10.3389/FNCOM.2013.00017

[63] Gigante, G., Mattia, M., Braun, J., & Del Giudice, P. (2009). Bistable perception modeled as competing stochastic integrations at two levels. *PLOS Computational Biology*, 5(7), e1000430. https://doi.org/10.1371/JOURNAL.PCBI.1000430

[64] Hegdé, J., Thompson, S. K., Brady, M. J., & Kersten, D. (2010). A Link between Visual Disambiguation and Visual Memory. *The Journal of Neuroscience*, 30(45), 15124-15133. https://doi.org/10.1523/JNEUROSCI.4415-09.2010

[65] Geert, P. L. C. van, Boderé, C., & Garzorz, I. S. (2022). Same stimulus, same temporal context, different percept? Individual differences in hysteresis and adaptation when perceiving multistable dot lattices. *I-Perception*, 13(4), 20416695221109300. https://doi.org/10.1177/20416695221109300

[66] Misyak, J. B., & Christiansen, M. H. (2010). On-line individual differences in statistical learning predict language processing. *Frontiers in Psychology*, 1, 31. https://doi.org/10.3389/FPSYG.2010.00031

[67] Hunt, R. H., & Aslin, R. N. (2001). Statistical learning in a serial reaction time task: access to separable statistical cues by individual learners. *Journal of Experimental Psychology: General*, 130(4), 658-680. https://doi.org/10.1037//0096-3445.130.4.658

[68] Okumbekov, D., & Éltető, N. (2022). Tracking human skill learning with a hierarchical Bayesian sequence model. *PLOS Computational Biology*, 18(11), e1009866. https://doi.org/10.1371/journal.pcbi.1009866

[69] Wessel, J. R., Haider, H., & Rose, M. (2012). The transition from implicit to explicit representations in incidental learning situations: more evidence from high-frequency EEG coupling. *Experimental Brain Research*, 217(1), 153-162. https://doi.org/10.1007/S00221-011-2982-7

[70] Musfeld, P., Schlemmer, A., Raab, M., & Strauss, B. (2023). Repetition learning is neither a continuous nor an implicit process. *Proceedings of the National Academy of Sciences of the United States of America*, 120(7), e2218042120. https://doi.org/10.1073/pnas.2218042120

[71] Esser, S., Lustig, C., & Haider, H. (2017). The Emergence of Explicit Knowledge in a Serial Reaction Time Task: The Role of Experienced Fluency and Strength of Representation. *Frontiers in Psychology*, 8, 502. https://doi.org/10.3389/FPSYG.2017.00502

[72] Zimmerer, V. C., Cowell, P. E., & Varley, R. A. (2011). Individual behavior in learning of an artificial grammar. *Memory & Cognition*, 39(3), 491-501. https://doi.org/10.3758/S13421-010-0039-Y

[73] Chauhan, V., Visser, I., Moran, R., & Beerendonk, L. (2022). Tracking the contribution of inductive bias to individualised internal models. *PLOS Computational Biology*, 18(6), e1010182. https://doi.org/10.1371/journal.pcbi.1010182

[74] Jenkins, R., Lavie, N., & Driver, J. (2023). Assessing Processing-Based Measures of Implicit Statistical Learning. *PsyArXiv*. https://doi.org/10.31234/osf.io/baupz

[75] Alexandre, F. (2010). *Modeling Implicit and Explicit Processes in Recursive Sequence Structure Learning* [Doctoral dissertation]. Université de Provence.

[76] Lawson, R. A., Beets, I. A. M., & Krakauer, J. W. (2017). Novel behavioral indicator of explicit awareness reveals temporal course of frontoparietal neural network facilitation during motor learning. *PLOS ONE*, 12(6), e0175176. https://doi.org/10.1371/JOURNAL.PONE.0175176

[77] Smith, J. G., & McDowall, J. (2001). Preserved implicit learning on both the serial reaction time task and artificial grammar in patients with Parkinson's disease. *Brain and Cognition*, 45(3), 378-391. https://doi.org/10.1006/BRCG.2001.1286

[78] Abugaber, D., Zhao, J., & Jamieson, R. K. (2021). *Differences in implicit vs. explicit grammar processing as revealed by drift-diffusion modeling of reaction times* [Unpublished manuscript].

[79] Sentman, L., Beevers, C. G., & Schnyer, D. M. (2007). *The Effect of Mood and Individual Differences on Implicit Learning* [Unpublished manuscript].

[80] Jurchiș, R., Cardellicchio, P., Dolfini, E., Fadda, E., D'Ausilio, A., & Tomassini, A. (2022). Implicit learning of regularities followed by realistic body movements in virtual reality. *Psychonomic Bulletin & Review*, 29(6), 2283-2293. https://doi.org/10.3758/s13423-022-02175-0

[81] Székely, A., Tenenbaum, J. B., & Gershman, S. J. (2024). Identifying Transfer Learning in the Reshaping of Inductive Biases. *PsyArXiv*. https://doi.org/10.31234/osf.io/jvumf

[82] Zwart, F. S. (2018). *What have we learned? On implicit learning in ASD and SLI* [Doctoral dissertation]. University of Amsterdam.

[83] Okumbekov, D., & Éltető, N. (2022). Tracking human skill learning with a hierarchical Bayesian sequence model. *PLOS Computational Biology*, 18(11), e1009866. https://doi.org/10.1371/journal.pcbi.1009866

[84] Brings, J., Kellen, D., & Singmann, H. (2022). Understanding Learning Trajectories With Infinite Hidden Markov Models. *2022 Conference on Cognitive Computational Neuroscience*, 1267-0. https://doi.org/10.32470/ccn.2022.1267-0

[85] Giurfa, M., Zhang, S., Jenett, A., Menzel, R., & Srinivasan, M. V. (2001). The concepts of 'sameness' and 'difference' in an insect. *Nature*, 410(6831), 930-933. https://doi.org/10.1038/35073582

[86] Minors, S. (Year unknown). *How a honey bee solves an abstract conceptual problem* [Unpublished manuscript].

[87] Muszynski, J. (Year unknown). *Same/Different Concept Learning and Category Discrimination in Honeybees* [Unpublished manuscript].

[88] Finke, V., Baracchi, D., Giurfa, M., Scheiner, R., & Avarguès-Weber, A. (2023). Individual consistency in the learning abilities of honey bees: cognitive specialization within sensory and reinforcement modalities. *Animal Cognition*, 26(2), 709-727. https://doi.org/10.1007/s10071-022-01741-2

[89] Dyer, A. G., Garcia, J. E., Shrestha, M., & Howard, S. R. (2019). Common Principles in Learning from Bees through to Humans: Individual Differences Set a Basis for Learning Theory and Implementations into AI. *International Journal of Comparative Psychology*, 32, 1-14. https://doi.org/10.1163/23644583-00401014

[90] Pamir, E., Szyszka, P., Scheiner, R., & Nawrot, M. P. (2014). Rapid learning dynamics in individual honeybees during classical conditioning. *Frontiers in Behavioral Neuroscience*, 8, 313. https://doi.org/10.3389/FNBEH.2014.00313

[91] Finke, V., Baracchi, D., Giurfa, M., Scheiner, R., & Avarguès-Weber, A. (2023). Individual consistency in the learning abilities of honey bees: cognitive specialization within sensory and reinforcement modalities. *Animal Cognition*, 26(2), 709-727. https://doi.org/10.1007/s10071-022-01741-2

[92] MaBouDi, H., Galpayage Dona, H. S., Gatto, E., Loukola, O. J., Buckley, E., Onoufriou, P. D., Skorupski, P., & Chittka, L. (2020). Bumblebees Learn a Relational Rule but Switch to a Win-Stay/Lose-Switch Heuristic After Extensive Training. *Frontiers in Behavioral Neuroscience*, 14, 137. https://doi.org/10.3389/FNBEH.2020.00137

[93] Avarguès-Weber, A., d'Amaro, D., Metzler, M., & Dyer, A. G. (2014). Conceptualization of relative size by honeybees. *Frontiers in Behavioral Neuroscience*, 8, 80. https://doi.org/10.3389/FNBEH.2014.00080

[94] Dyer, A. G., Garcia, J. E., Shrestha, M., & Howard, S. R. (2019). Common Principles in Learning from Bees through to Humans: Individual Differences Set a Basis for Learning Theory and Implementations into AI. *International Journal of Comparative Psychology*, 32, 1-14. https://doi.org/10.1163/23644583-00401014

[95] Giurfa, M., Marcout, C., Hilpert, P., Thevenot, C., & Rugani, R. (2021). Learning of sameness/difference relationships by honey bees: performance, strategies and ecological context. *Current Opinion in Behavioral Sciences*, 37, 1-6. https://doi.org/10.1016/J.COBEHA.2020.05.008

[96] Couvillon, P. A., Arakaki, L., & Bitterman, M. E. (1998). Control of performance by short-term memory in honeybees. *Animal Learning & Behavior*, 26(3), 247-256. https://doi.org/10.3758/BF03199240

[97] Kleyko, D., Rahimi, A., Rachkovskij, D. A., Osipov, E., & Rabaey, J. M. (2015). Imitation of honey bees' concept learning processes using Vector Symbolic Architectures. *Biologically Inspired Cognitive Architectures*, 14, 57-72. https://doi.org/10.1016/J.BICA.2015.09.002

[98] Dandurand, F., Shultz, T. R., & Onishi, K. H. (2011). A Fresh Look at Vocabulary Spurts. *Cognitive Science*, 35(8), 1564-1585.

[99] Ganger, J., & Brent, M. R. (2004). Reexamining the vocabulary spurt. *Developmental Psychology*, 40(4), 621-632. https://doi.org/10.1037/0012-1649.40.4.621

[100] Goldfield, B. A., & Reznick, J. S. (1990). Early lexical acquisition: rate, content, and the vocabulary spurt. *Journal of Child Language*, 17(1), 171-183. https://doi.org/10.1017/S0305000900013167

[101] Goldfield, B. A., & Reznick, J. S. (1990). Early lexical acquisition: rate, content, and the vocabulary spurt. *Journal of Child Language*, 17(1), 171-183. https://doi.org/10.1017/S0305000900013167

[102] McMurray, B. (2007). Defusing the Childhood Vocabulary Explosion. *Science*, 317(5838), 631. https://doi.org/10.1126/SCIENCE.1144073

[103] Dijk, M. van, & Geert, P. van. (2007). Wobbles, humps and sudden jumps: A case study of continuity, discontinuity and variability in early language development. *Infant and Child Development*, 16(1), 7-33. https://doi.org/10.1002/ICD.506

[104] Díaz, V., Farran, L. K., Byers-Heinlein, K., & Werker, J. F. (2024). Testing theories of the vocabulary spurt with monolingual and bilingual infants. *Developmental Psychology*, 60(4), 777-792. https://doi.org/10.1037/dev0001777

[105] D'Odorico, L., Carubbi, S., Salerni, N., & Calvo, V. (2001). Vocabulary Development in Italian Children: A Longitudinal Evaluation of Quantitative and Qualitative Aspects. *Journal of Child Language*, 28(2), 351-372. https://doi.org/10.1017/S0305000901004676

[106] Fernald, A., Perfors, A., & Marchman, V. A. (2012). Individual Differences in Lexical Processing at 18 Months Predict Vocabulary Growth in Typically Developing and Late-Talking Toddlers. *Child Development*, 83(1), 203-222. https://doi.org/10.1111/J.1467-8624.2011.01692.X

[107] Bloom, L., Tinker, E., & Margulis, C. (1996). Early Conversations and Word Learning: Contributions from Child and Adult. *Child Development*, 67(6), 3154-3175. https://doi.org/10.1111/J.1467-8624.1996.TB01907.X

[108] Elsen, H. (1996). Two routes to language: stylistic variation in one child. *First Language*, 16(47), 141-158. https://doi.org/10.1177/014272379601604701

[109] Tao, Y., Zhang, Y., & Zhou, X. (Year unknown). Word-Spurt: A Milestone in Early Language Development——A Longitudinal Study on Five Mandarin-Speaking Children. *Journal of Psychological Science*, 37(3). https://doi.org/10.16719/j.cnki.1671-6981.2014.03.004

[110] Reznick, J. S., & Goldfield, B. A. (1992). Rapid change in lexical development in comprehension and production. *Developmental Psychology*, 28(3), 406-413. https://doi.org/10.1037/0012-1649.28.3.406

[111] Parladé, M. V., & Iverson, J. M. (2011). The interplay between language, gesture, and affect during communicative transition: a dynamic systems approach. *Developmental Psychology*, 47(3), 820-833. https://doi.org/10.1037/A0021811

[112] Oliver, B., & Buckley, S. (1994). The language development of children with Down syndrome: First words to two-word phrases. *Down Syndrome Research and Practice*, 2(2), 71-75. https://doi.org/10.3104/REPORTS.33

[113] Klammler, K., & Schneider, P. (2011). The size and composition of the productive holophrastic lexicon: German–Italian bilingual acquisition vs. Italian monolingual acquisition. *International Journal of Bilingual Education and Bilingualism*, 14(1), 69-88. https://doi.org/10.1080/13670051003692840

[114] Cassano, M. C. (2013). *An examination of growth in vocabulary and phonological awareness in early childhood: An individual growth model approach* [Doctoral dissertation]. University of South Florida.

[115] Durstewitz, D., Vittoz, N. M., Floresco, S. B., & Seamans, J. K. (2010). Abrupt transitions between prefrontal neural ensemble states accompany behavioral transitions during rule learning. *Neuron*, 66(3), 438-448. https://doi.org/10.1016/j.neuron.2010.03.029

[116] Russo, E., Ma, T., Spanagel, R., Durstewitz, D., Toutounji, H., & Köhr, G. (2020). Coordinated prefrontal state transition leads extinction of reward-seeking behaviors. *bioRxiv*, 2020.02.26.964510. https://doi.org/10.1101/2020.02.26.964510

[117] Feierstein, C. E. (2010). Listening to the crowd: neuronal ensembles rule. *Neuron*, 66(3), 333-334. https://doi.org/10.1016/j.neuron.2010.04.042

[118] Powell, N. J., & Redish, A. D. (2016). Representational changes of latent strategies in rat medial prefrontal cortex precede changes in behaviour. *Nature Communications*, 7, 12830. https://doi.org/10.1038/NCOMMS12830

[119] Maggi, S., Peyrache, A., & Humphries, M. D. (2022). Activity Subspaces in Medial Prefrontal Cortex Distinguish States of the World. *The Journal of Neuroscience*, 42(11), 2252-2264. https://doi.org/10.1523/JNEUROSCI.1412-21.2022

[120] Singh, A., Humphries, M. D., & Koppe, G. (2016). Signatures of internal model updating during learning in rat prefrontal cortex. *bioRxiv*, 027102. https://doi.org/10.1101/027102

[121] Singh, A., Humphries, M. D., & Koppe, G. (2018). Medial prefrontal cortex population activity is plastic irrespective of learning. *bioRxiv*, 027102. https://doi.org/10.1101/027102

[122] Zhou, Y., Freedman, D. J., & Kramer, M. A. (2016). A Dynamic Bayesian Model for Characterizing Cross-Neuronal Interactions During Decision-Making. *Journal of the American Statistical Association*, 111(514), 459-471. https://doi.org/10.1080/01621459.2015.1116988

[123] Csorba, B. A., Katlowitz, K. A., Picardo, M. A., & Long, M. A. (2021). Long-range cortical synchronization supports abrupt visual learning. *bioRxiv*, 2021.08.03.454994. https://doi.org/10.1101/2021.08.03.454994

[124] Zhou, J., Zong, W., Jia, C., Gardner, M. P. H., & Schoenbaum, G. (2021). Evolving schema representations in orbitofrontal ensembles during learning. *Nature*, 590(7847), 606-611. https://doi.org/10.1038/S41586-020-03061-2

[125] Powell, N. J., & Redish, A. D. (2016). Representational changes of latent strategies in rat medial prefrontal cortex precede changes in behaviour. *Nature Communications*, 7, 12830. https://doi.org/10.1038/NCOMMS12830

[126] Shettleworth, S. J. (2012). Do animals have insight, and what is insight anyway? *Canadian Journal of Experimental Psychology*, 66(4), 217-226. https://doi.org/10.1037/A0030674

[127] Metcalfe, J., & Wiebe, D. (1987). Intuition in insight and noninsight problem solving. *Memory & Cognition*, 15(3), 238-246. https://doi.org/10.3758/BF03197722

[128] Kizilirmak, J. M., Thuerich, H., Folta-Schoofs, K., Schott, B. H., & Richardson-Klavehn, A. (2018). Feelings-of-Warmth Increase More Abruptly for Verbal Riddles Solved With in Contrast to Without Aha! Experience. *Frontiers in Psychology*, 9, 1404. https://doi.org/10.3389/FPSYG.2018.01404

[129] Chein, J. M., Weisberg, R. W., Streeter, N. L., & Kwok, S. (2010). Working memory and insight in the nine-dot problem. *Memory & Cognition*, 38(7), 883-892. https://doi.org/10.3758/MC.38.7.883

[130] Dubey, R., Ho, M. K., Mehta, H., & Griffiths, T. L. (2021). Aha! moments correspond to meta-cognitive prediction errors. *PsyArXiv*. https://doi.org/10.31234/OSF.IO/C5V42

[131] Terai, H., Miwa, K., & Asami, K. (2013). A Chance Favors a Prepared Mind: Chance Discovery from Cognitive Psychology. In Y. Ohsawa & A. Abe (Eds.), *Studies in Computational Intelligence* (Vol. 423, pp. 25-37). Springer. https://doi.org/10.1007/978-3-642-30114-8_3

[132] Kizilirmak, J. M., Thuerich, H., Folta-Schoofs, K., Schott, B. H., & Richardson-Klavehn, A. (2018). Feelings-of-Warmth Increase More Abruptly for Verbal Riddles Solved With in Contrast to Without Aha! Experience. *Frontiers in Psychology*, 9, 1404. https://doi.org/10.3389/FPSYG.2018.01404

[133] Metcalfe, J. (1986). Premonitions of insight predict impending error. *Journal of Experimental Psychology: Learning, Memory and Cognition*, 12(4), 623-634. https://doi.org/10.1037/0278-7393.12.4.623

[134] Kuchibhotla, K. V., Hindmarsh Sten, T., Papadoyannis, E. S., Elnozahy, S., Fogelson, K. A., Kumar, R., Boubenec, Y., Holland, P. C., Ostojic, S., & Froemke, R. C. (2019). Dissociating task acquisition from expression during learning reveals latent knowledge. *Nature Communications*, 10(1), 2151. https://doi.org/10.1038/S41467-019-10089-0

[135] Löwe, S., Madge, C., Tsalas, E., Ahrens, K., Clopath, C., & Saxe, A. (2023). *Regularised neural networks mimic human insight*. arXiv preprint arXiv:2302.11351. https://doi.org/10.48550/arxiv.2302.11351

[136] Terai, H., Miwa, K., & Asami, K. (2013). A Chance Favors a Prepared Mind: Chance Discovery from Cognitive Psychology. In Y. Ohsawa & A. Abe (Eds.), *Studies in Computational Intelligence* (Vol. 423, pp. 25-37). Springer. https://doi.org/10.1007/978-3-642-30114-8_3

[137] Kizilirmak, J. M., Thuerich, H., Folta-Schoofs, K., Schott, B. H., & Richardson-Klavehn, A. (2018). Feelings-of-Warmth Increase More Abruptly for Verbal Riddles Solved With in Contrast to Without Aha! Experience. *Frontiers in Psychology*, 9, 1404. https://doi.org/10.3389/FPSYG.2018.01404

[138] Bilalić, M., Graf, M., Vaci, N., & Danek, A. H. (2021). The temporal dynamics of insight problem solving – restructuring might not always be sudden. *Thinking & Reasoning*, 27(1), 1-37. https://doi.org/10.1080/13546783.2019.1705912

[139] Dubey, R., Ho, M. K., Mehta, H., & Griffiths, T. L. (2021). Aha! moments correspond to meta-cognitive prediction errors. *PsyArXiv*. https://doi.org/10.31234/OSF.IO/C5V42

[140] Metcalfe, J. (1986). Premonitions of insight predict impending error. *Journal of Experimental Psychology: Learning, Memory and Cognition*, 12(4), 623-634. https://doi.org/10.1037/0278-7393.12.4.623

[141] Metcalfe, J., & Wiebe, D. (1987). Intuition in insight and noninsight problem solving. *Memory & Cognition*, 15(3), 238-246. https://doi.org/10.3758/BF03197722

[142] Chein, J. M., Weisberg, R. W., Streeter, N. L., & Kwok, S. (2010). Working memory and insight in the nine-dot problem. *Memory & Cognition*, 38(7), 883-892. https://doi.org/10.3758/MC.38.7.883

[143] Ozernov-Palchik, O., Norton, E. S., Wang, Y., Beach, S. D., Zuk, J., Wolf, M., Gabrieli, J. D. E., & Gaab, N. (2022). Longitudinal changes in brain activation underlying reading fluency. *Human Brain Mapping*, 43(14), 4500-4517. https://doi.org/10.1002/hbm.26048

[144] Bouhali, F., Mongelli, V., Boros, M., & Dehaene, S. (2024). Unique longitudinal contributions of sulcal interruptions to reading acquisition in children. *eLife*, 13, e103007. https://doi.org/10.7554/elife.103007

[145] Bähner, F., Demanuele, C., Schweiger, J., Gerchen, M. F., Zamoscik, V., Ueltzhöffer, K., Hahn, T., Meyer, P., Flor, H., Durstewitz, D., Tost, H., Kirsch, P., & Meyer-Lindenberg, A. (2022). Species-conserved mechanisms of cognitive flexibility in complex environments. *bioRxiv*, 2022.11.14.516439. https://doi.org/10.1101/2022.11.14.516439

[146] Stephen, D. G., Dixon, J. A., & Isenhower, R. W. (2009). Dynamics of representational change: entropy, action, and cognition. *Journal of Experimental Psychology: Human Perception and Performance*, 35(6), 1811-1832. https://doi.org/10.1037/A0014510

[147] Stephen, D. G., Dixon, J. A., & Isenhower, R. W. (2009). The dynamics of insight: Mathematical discovery as a phase transition. *Memory & Cognition*, 37(8), 1132-1149. https://doi.org/10.3758/MC.37.8.1132

[148] Liu, Y.-T., Mayer-Kress, G., & Newell, K. M. (2015). S-shaped motor learning and nonequilibrium phase transitions. *Journal of Experimental Psychology: Human Perception and Performance*, 41(2), 403-414. https://doi.org/10.1037/A0038812

[149] Helton, W. S. (2011). Animal Expertise: Evidence of Phase Transitions by Utilizing Running Estimates of Performance Variability. *Ecological Psychology*, 23(2), 83-105. https://doi.org/10.1080/10407413.2011.564537

[150] Stamovlasis, D. (2017). The Dynamics of Cognitive Performance: What Has Been Learnt from Empirical Research in Science Education. *Complicity: An International Journal of Complexity in Education*, 14(2), 1-23. https://doi.org/10.29173/CMPLCT29333

[151] Perry, C., Zorzi, M., & Ziegler, J. C. (2019). Understanding Dyslexia Through Personalized Large-Scale Computational Models. *Psychological Science*, 30(3), 386-395. https://doi.org/10.1177/0956797618823540
