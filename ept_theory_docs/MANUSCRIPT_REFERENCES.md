# Complete Reference List and Field Positioning for EPT Manuscript

**Date**: 2026-03-16
**Purpose**: All references organized by section, with positioning commentary

---

## I. WHERE WE BELONG — Field Positioning

### The Landscape (as of March 2026)

The grokking literature has evolved through four phases:

**Phase 1 (2022): Discovery.** Power et al. (2022) reported grokking. Immediate response: mechanistic interpretability (Nanda et al., 2023; Gromov, 2023) reverse-engineered the Fourier circuits.

**Phase 2 (2023): Theoretical scramble.** Multiple frameworks competed: circuit competition (Merrill et al., 2023; Varma et al., 2023), lazy-to-rich transitions (Kumar et al., 2024), implicit bias dichotomy (Lyu et al., 2024), representation learning theory (Liu et al., 2022).

**Phase 3 (2024-2025): Phase transition claims.** Six+ groups independently claimed "grokking = phase transition" using different theoretical tools: mean-field theory (Rubin/Nareddy et al., ICLR 2024), Singular Learning Theory (Lau/Murfet et al., 2026), solvable models (Žunkovič & Ilievski, JMLR 2025), information theory (Clauw et al., 2024), rate-distortion complexity (DeMoss et al., 2025), multi-task geometry (Feb 2026).

**Phase 4 (2025-2026): Universality and applications.** Grokking beyond mod arith (Humayun "deep networks always grok" ICML 2024), LLM pretraining grokking (2025), anti-grokking (2026), ungrokking (2025).

### Where EPT Fits

**We are NOT in Phase 3** (yet another "grokking = phase transition" paper). That space is crowded with 6+ entrants.

**We are bridging Phases 3 and 4** with a unique position:

1. **The only empirical hysteresis test** in the grokking literature — the textbook first-order diagnostic that no other group performs
2. **The only Arrhenius kinetics measurement** — quantitative barrier-crossing evidence in SGD-trained networks
3. **A portable diagnostic framework (Ψ, F)** designed for cross-domain transfer — from grokking → dictionary learning → human cognition
4. **Novel depth-dependent results** — non-monotonic relationship between depth, transition sharpness, and hysteresis strength
5. **The bridge to human cognition** — Paper 3 (AGL experiment) applies the same framework to human learning

### Our Unique Contribution in One Sentence

> "We introduce a two-parameter diagnostic (Ψ, F) for detecting first-order phase transitions in learning systems, provide the first direct hysteresis test and Arrhenius kinetics measurement for grokking, and demonstrate that the phase transition barrier resides entirely in feature space with non-monotonic depth dependence."

### Papers We MUST Address (Potential Challenges)

**Zhang & Shang (2025) — "Is Grokking a Computational Glass Relaxation?" NeurIPS 2025 Spotlight.** arXiv:2505.11411.
- **Their claim**: No entropy barrier between memorization and generalization in Boltzmann landscape sampling. Grokking = glass relaxation (rapid cooling → non-equilibrium state → slow relaxation to stable config), NOT a first-order phase transition.
- **Why it matters**: If there's no barrier, our Kramers/Arrhenius picture is wrong.
- **Our counter-argument**: (1) Our hysteresis test directly demonstrates irreversibility — the crystal state persists at WD=0 while the glass state is the global minimum. Glass relaxation does NOT predict this asymmetry. (2) Their Boltzmann sampling operates at equilibrium; our SGD dynamics are non-equilibrium. The barrier may exist in the dynamics even if absent in the equilibrium landscape. (3) Glass transitions CAN show hysteresis, but our Arrhenius kinetics (R²=0.976) specifically matches barrier-crossing, not stretched-exponential relaxation typical of glasses. (4) Our depth sweep shows non-monotonic hysteresis strength — this is inconsistent with simple glass relaxation, which should be monotonic in system size.
- **Must cite and discuss explicitly in Discussion section.**

**Prieto et al. (2025) — "Using Physics-Inspired SLT to Understand Grokking." arXiv:2512.00686.**
- **Their claim**: Tests Arrhenius-style rate hypothesis using SLT on grokking models.
- **Why it matters**: If they already have Arrhenius fits, our T2 is not novel.
- **How to differentiate**: They use SLT (Bayesian framework). We use empirical SGD measurements + Kramers theory. Our hysteresis test is the distinguishing experiment.

**Xie et al. (2020/ICLR 2022) — "A Diffusion Theory for Deep Learning Dynamics."** arXiv:2002.03495.
- **Their claim**: SGD escape time ~ exp(C × batch_size / learning_rate). SGD favors flat minima exponentially.
- **Why it matters**: This is the closest existing Kramers-like escape rate for SGD. Our Arrhenius form should be compatible: if T_eff ~ lr/batch_size, then ln(t) = ΔE(λ_WD) / T_eff.

**Simsekli (2019) — "Tail-Index Analysis of SGD Noise."** arXiv:1901.06053.
- **Their claim**: SGD gradient noise is heavy-tailed (non-Gaussian), invalidating simple Kramers (which assumes Gaussian noise).
- **Why it matters**: Undermines direct application of classical Kramers formula.
- **Our response**: Acknowledge this caveat. Our Arrhenius fit is empirical — it's consistent with Kramers but we don't claim the classical formula applies directly. The heavy-tail extension (Lévy-driven metastability, Nguyen et al. 2019) also predicts exponential escape times.

### What We Should NOT Claim

- "First to show grokking is a phase transition" (6+ groups already claim this)
- "Proved grokking is first-order" (Nareddy et al. have the analytical theory)
- "Mechanistic understanding of grokking" (Nanda et al. did this for transformers)
- "Universality of grokking" (Humayun et al. already claimed this)
- "Derived Arrhenius from first principles" (we show consistency, not derivation)

---

## II. REFERENCES BY MANUSCRIPT SECTION

### Introduction / Anomalies

**The Linearity Illusion and its exceptions:**

| Ref | Citation | Role in manuscript |
|-----|----------|-------------------|
| Rumelhart1986 | Rumelhart, D.E., Hinton, G.E. & Williams, R.J. (1986). Learning representations by back-propagating errors. *Nature*, 323, 533-536. | Gradient descent as the foundation of learning theory |
| Kohler1925 | Köhler, W. (1925). *The Mentality of Apes*. Routledge & Kegan Paul. | Original insight observations in chimpanzees |
| Metcalfe1986 | Metcalfe, J. & Wiebe, D. (1987). Intuition in insight and noninsight problem solving. *Memory & Cognition*, 15(3), 238-246. | "Warmth" ratings flat then spike — incompatible with gradual progress |

**The Aha! moment — neural signatures:**

| Ref | Citation | Role |
|-----|----------|------|
| JungBeeman2004 | Jung-Beeman, M. et al. (2004). Neural activity when people solve verbal problems with insight. *PLoS Biology*, 2(4), e97. DOI:10.1371/journal.pbio.0020097 | Gamma burst in right aSTG, 300ms before insight report |
| Kounios2014 | Kounios, J. & Beeman, M. (2014). The cognitive neuroscience of insight. *Annual Review of Psychology*, 65, 71-93. DOI:10.1146/annurev-psych-010213-115154 | Comprehensive review: pre-insight alpha, reward circuit activation |

**The irreversible pop-out:**

| Ref | Citation | Role |
|-----|----------|------|
| Ludmer2011 | Ludmer, R., Dudai, Y. & Rubin, N. (2011). Uncovering camouflage: Amygdala activation predicts long-term memory of induced perceptual insight. *Neuron*, 69(5), 1002-1014. DOI:10.1016/j.neuron.2011.02.013 | Mooney image pop-out is irreversible — once seen, cannot unsee |

**Grokking:**

| Ref | Citation | Role |
|-----|----------|------|
| Power2022 | Power, A. et al. (2022). Grokking: Generalization beyond overfitting on small algorithmic datasets. arXiv:2201.02177. | Original grokking observation |
| Nanda2023 | Nanda, N. et al. (2023). Progress measures for grokking via mechanistic interpretability. *ICLR 2023*. arXiv:2301.05217. | Reverse-engineered Fourier circuits in transformers |

**Emergent abilities:**

| Ref | Citation | Role |
|-----|----------|------|
| Wei2022 | Wei, J. et al. (2022). Emergent abilities of large language models. arXiv:2206.07682. | Abilities appear suddenly at critical parameter counts |
| Schaeffer2023 | Schaeffer, R., Miranda, B. & Koyejo, S. (2024). Are emergent abilities of large language models a mirage? *NeurIPS 2023*. | Some emergence is metric-choice artifact — our central point |

---

### Theory Section (Crystal/Glass Model, Propositions)

**Hopfield networks and attractor dynamics:**

| Ref | Citation | Role |
|-----|----------|------|
| Hopfield1982 | Hopfield, J.J. (1982). Neural networks and physical systems with emergent collective computational abilities. *PNAS*, 79(8), 2554-2558. | Foundation for Crystal/Glass model |
| Amit1985 | Amit, D.J., Gutfreund, H. & Sompolinsky, H. (1985). Storing infinite numbers of patterns in a spin-glass model of neural networks. *Physical Review Letters*, 55(14), 1530. | Storage capacity, spin-glass phase |
| Kaszas2025 | Kaszás, B. et al. (2025). Memorisation and forgetting in a learning Hopfield neural network: bifurcation mechanisms. arXiv:2508.10765. | **KEY**: attractor creation/destruction via distinct bifurcation pathways = formal mechanism for hysteresis (Prop 1) |
| Ramsauer2020 | Ramsauer, H. et al. (2021). Hopfield networks is all you need. *ICLR 2021*. arXiv:2008.02217. | Modern Hopfield networks; connection to transformers/attention |

**Kramers escape theory (Proposition 3):**

| Ref | Citation | Role |
|-----|----------|------|
| Kramers1940 | Kramers, H.A. (1940). Brownian motion in a field of force and the diffusion model of chemical reactions. *Physica*, 7(4), 284-304. | Foundation for Arrhenius derivation |
| Hanggi1990 | Hänggi, P., Talkner, P. & Borkovec, M. (1990). Reaction-rate theory: fifty years after Kramers. *Reviews of Modern Physics*, 62(2), 251-341. DOI:10.1103/RevModPhys.62.251 | Comprehensive review of Kramers theory extensions |
| Pollak2023 | Pollak, E. (2023). Recent developments in Kramers' theory of reaction rates. *ChemPhysChem*, e202300272. DOI:10.1002/cphc.202300272 | Latest developments in barrier-crossing theory |
| Ly2025 | Ly, A. & Gong, P. (2025). Optimization on multifractal loss landscapes explains a diverse range of geometrical and dynamical properties of deep learning. *Nature Communications*, 16, 3252. DOI:10.1038/s41467-025-58532-9 | **KEY**: Kramers escape in NN loss landscapes; noise intensity σ = η²β; learning rate squared as effective temperature |

**Saddle point escape (Proposition 2):**

| Ref | Citation | Role |
|-----|----------|------|
| Jin2017 | Jin, C. et al. (2017). How to escape saddle points efficiently. *ICML 2017*, 1724-1732. | Foundation: perturbed GD escapes strict saddles in poly time |
| Bornstein2025 | Bornstein, M. et al. (2025). Escaping saddle points via curvature-calibrated perturbations. arXiv:2508.16540. | **KEY**: explicit escape time T = O(ℓ/√(ρε)·log(d)); exponential growth of escape direction at rate γ = √(ρε) |
| Cheridito2024 | Cheridito, P. et al. (2024). Gradient descent provably escapes saddle points in shallow ReLU networks. *JMLR 2024*. PMC11628594. | GD almost surely avoids saddles without perturbation |

**SGD as Langevin dynamics:**

| Ref | Citation | Role |
|-----|----------|------|
| Mandt2017 | Mandt, S., Hoffman, M.D. & Blei, D.M. (2017). Stochastic gradient descent as approximate Bayesian inference. *JMLR*, 18(1), 4873-4907. | SGD ≈ Langevin dynamics with lr as temperature |
| Jastrzkebski2017 | Jastrzębski, S. et al. (2017). Three factors influencing minima in SGD. arXiv:1711.04623. | lr/batch_size ratio controls effective temperature |
| Smith2018 | Smith, S.L. & Le, Q.V. (2018). A Bayesian perspective on generalization and stochastic gradient descent. *ICLR 2018*. | lr/batch_size as noise-to-signal ratio |

---

### Grokking Results Section

**Competing "grokking = phase transition" papers (must cite all):**

| Ref | Citation | Their claim | Our response |
|-----|----------|-------------|-------------|
| Rubin2024 | Rubin, N., Seroussi, I. & Ringel, Z. (2024). Grokking as a first order phase transition in two layer networks. *ICLR 2024*. arXiv:2310.03789. | Analytical mean-field theory; mixed-phase Gaussian structure | We confirm empirically in SGD regime; add hysteresis test they lack |
| Lau2026 | Lau, J., Estan-Ruiz, S. et al. (2026). Grokking as a phase transition between competing basins: SLT approach. arXiv:2603.01192. | LLC closed-form for quadratic nets; basin competition | Different theoretical framework; we test predictions they derive |
| Zunkovic2025 | Žunkovič, B. & Ilievski, E. (2025). Grokking phase transitions in learning local rules with gradient descent. *JMLR*, 25(199), 1-52. | **Second-order** transitions in perceptrons; exact critical exponents | Crucial contrast — we find first-order in deep nets; depth matters |
| Clauw2024 | Clauw, K. et al. (2024). Information-theoretic progress measures reveal grokking is an emergent phase transition. arXiv:2408.08944. | O-Information (synergy) as order parameter | Complementary — they track neuron interactions, we track representation geometry |
| DeMoss2025 | DeMoss, B. et al. (2025). The complexity dynamics of grokking. *Physica D*, 482, 134859. arXiv:2412.09810. | Kolmogorov complexity rise-and-fall | Different observable; no phase transition classification |
| MultiTask2026 | [Authors] (2026). The geometry of multi-task grokking. arXiv:2602.18523. | WD phase structure; defect-mediated transitions; WD=0 doesn't grok | Independently confirms our WD=0 finding; no hysteresis test |

**Mechanistic interpretability (context for Fourier results):**

| Ref | Citation | Role |
|-----|----------|------|
| Nanda2023 | (see above) | Fourier circuits in transformers |
| Gromov2023 | Gromov, A. (2023). Grokking modular arithmetic. arXiv:2301.02679. | Analytical solutions: trig feature maps |
| Chughtai2023 | Chughtai, B., Chan, L. & Nanda, N. (2023). A toy model of universality. arXiv:2302.03025. | Group representation theory for grokking |
| Liu2022_NeurIPS | Liu, Z. et al. (2022). Towards understanding grokking: an effective theory of representation learning. *NeurIPS 2022*. arXiv:2205.10343. | Four learning phases; Goldilocks zone; physics-inspired phase diagrams |

**Weight decay and regularization:**

| Ref | Citation | Role |
|-----|----------|------|
| Lyu2024 | Lyu, K. et al. (2024). Dichotomy of early and late phase implicit biases. *ICLR 2024*. arXiv:2311.18817. | Large init + small WD provably induces grokking |
| Thilak2022 | Thilak, V. et al. (2022). The slingshot mechanism. arXiv:2206.04817. | Grokking via adaptive optimizer oscillations without explicit WD |

**Grokking universality:**

| Ref | Citation | Role |
|-----|----------|------|
| Liu2022_Omnigrok | Liu, Z., Michaud, E.J. & Tegmark, M. (2023). Omnigrok. *ICLR 2023*. arXiv:2210.01117. | Grokking on images, language, molecules |
| Humayun2024 | Humayun, A.I. et al. (2024). Deep networks always grok. *ICML 2024*. arXiv:2402.15555. | Grokking is universal in practical settings |
| Barak2022 | Barak, B. et al. (2022). Hidden progress in deep learning. *NeurIPS 2022*. arXiv:2207.08799. | Invisible progress in Fourier gap |

---

### Discussion Section

**Phase transitions in cognition (for the bridge to Paper 3):**

| Ref | Citation | Role |
|-----|----------|------|
| Spivey2009 | Spivey, M.J., Anderson, S.E. & Dale, R. (2009). The phase transition in human cognition. *New Mathematics and Natural Computation*, 5(1), 197-220. | Cognition as self-organizing process with phase transitions |
| Stephen2009 | Stephen, D.G. et al. (2009). The dynamics of insight: mathematical discovery as a phase transition. *Memory & Cognition*, 37(8), 1132-1149. DOI:10.3758/MC.37.8.1132 | Insight predicted by entropy changes and power-law behavior |
| Viteri2022 | Viteri, S. & DeDeo, S. (2022). Epistemic phase transitions in mathematical proofs. *Cognition*, 225, 105120. DOI:10.1016/j.cognition.2022.105120 | Belief in proofs undergoes phase transition via bidirectional inference |
| Durstewitz2010 | Durstewitz, D. et al. (2010). Abrupt transitions between prefrontal neural ensemble states accompany behavioral transitions during rule learning. *Neuron*, 66(3), 438-448. DOI:10.1016/j.neuron.2010.03.029 | **KEY**: Direct neural evidence for abrupt state transitions during rule learning |
| Reddy2022 | Reddy, G. (2022). A reinforcement-based mechanism for discontinuous learning. *PNAS*, 119(49), e2215352119. DOI:10.1073/pnas.2215352119 | **KEY**: RL with reinforcement waves produces discontinuous learning; bridges RL and sudden insight |

**Representational change theory:**

| Ref | Citation | Role |
|-----|----------|------|
| Ohlsson1992 | Ohlsson, S. (1992). Information-processing explanations of insight and related phenomena. In *Advances in the Psychology of Thinking* (vol. 1, pp. 1-44). | Insight via constraint relaxation, chunk decomposition |
| Knoblich1999 | Knoblich, G. et al. (1999). Constraint relaxation and chunk decomposition in insight problem solving. *Journal of Experimental Psychology: LMC*, 25(6), 1534-1555. | Difficulty depends on which type of representational change is required |
| Chi2005 | Chi, M.T.H. (2005). Commonsense conceptions of emergent processes. *Journal of the Learning Sciences*, 14(2), 161-199. | Misconceptions as stable, resistant-to-change beliefs = Glass phase analog |
| diSessa1988 | diSessa, A.A. (1988). Knowledge in pieces. In *Constructivism in the Computer Age* (pp. 49-70). | Knowledge-in-pieces framework = Glass phase |

**AGL (for Paper 3 connection):**

| Ref | Citation | Role |
|-----|----------|------|
| Reber1967 | Reber, A.S. (1967). Implicit learning of artificial grammars. *JVLVB*, 6, 855-863. | Original AGL paradigm |
| Pothos2007 | Pothos, E.M. (2007). Theories of artificial grammar learning. *Psychological Bulletin*, 133(2), 227-244. DOI:10.1037/0033-2909.133.2.227 | Comprehensive AGL theory review |
| Chen2024 | Chen, T.-Y. (2024). ENIGMA: A web application for running online AGL experiments. *J Psycholinguistic Research*, 53(3), 38. DOI:10.1007/s10936-024-10078-5 | Web-based AGL platform; validates our approach |

---

### Loss Landscape and Optimization Theory

| Ref | Citation | Role |
|-----|----------|------|
| Draxler2018 | Draxler, F. et al. (2018). Essentially no barriers in neural network energy landscape. *ICML 2018*. arXiv:1803.00885. | Mode connectivity — BUT only between same-loss minima; our barrier is between DIFFERENT loss regimes (memo vs gen) |
| Fort2019 | Fort, S. et al. (2020). Deep learning versus kernel learning: an empirical study of loss landscape geometry. *NeurIPS 2020*. | Loss landscape structure depends on overparameterization |
| Keskar2017 | Keskar, N.S. et al. (2017). On large-batch training for deep learning. *ICLR 2017*. arXiv:1609.04836. | Sharp vs flat minima; batch size affects generalization |

---

## III. MASTER BIBTEX

```bibtex
% === GROKKING: ORIGINAL + MECHANISTIC ===

@article{power2022grokking,
  title={Grokking: Generalization beyond overfitting on small algorithmic datasets},
  author={Power, Alethea and Burda, Yuri and Edwards, Harri and Babuschkin, Igor and Misra, Vedant},
  journal={arXiv preprint arXiv:2201.02177},
  year={2022}
}

@inproceedings{nanda2023progress,
  title={Progress measures for grokking via mechanistic interpretability},
  author={Nanda, Neel and Chan, Lawrence and Lieberum, Tom and Smith, Jess and Steinhardt, Jacob},
  booktitle={ICLR 2023},
  year={2023}
}

@article{gromov2023grokking,
  title={Grokking modular arithmetic},
  author={Gromov, Andrey},
  journal={arXiv preprint arXiv:2301.02679},
  year={2023}
}

@article{chughtai2023toy,
  title={A toy model of universality: Reverse engineering how networks learn group operations},
  author={Chughtai, Bilal and Chan, Lawrence and Nanda, Neel},
  journal={arXiv preprint arXiv:2302.03025},
  year={2023}
}

@inproceedings{liu2022towards,
  title={Towards understanding grokking: An effective theory of representation learning},
  author={Liu, Ziming and Kitouni, Ouail and Nolte, Niklas and Michaud, Eric and Tegmark, Max and Williams, Mike},
  booktitle={NeurIPS 2022},
  year={2022}
}

% === GROKKING: PHASE TRANSITION CLAIMS ===

@inproceedings{rubin2024grokking,
  title={Grokking as a first order phase transition in two layer networks},
  author={Rubin, Noa and Seroussi, Inbar and Ringel, Zohar},
  booktitle={ICLR 2024},
  year={2024}
}

@article{zunkovic2025grokking,
  title={Grokking phase transitions in learning local rules with gradient descent},
  author={\v{Z}unkovi\v{c}, Bojan and Ilievski, Enej},
  journal={Journal of Machine Learning Research},
  volume={25},
  number={199},
  pages={1--52},
  year={2025}
}

@article{clauw2024information,
  title={Information-theoretic progress measures reveal grokking is an emergent phase transition},
  author={Clauw, Kenzo and Stramaglia, Sebastiano and Marinazzo, Daniele},
  journal={arXiv preprint arXiv:2408.08944},
  year={2024}
}

@article{lau2026slt,
  title={Grokking as a phase transition between competing basins: a {S}ingular {L}earning {T}heory approach},
  author={Lau, Jesse and Estan-Ruiz, S. and Danait, R. and Li, J.},
  journal={arXiv preprint arXiv:2603.01192},
  year={2026}
}

@article{demoss2025complexity,
  title={The complexity dynamics of grokking},
  author={DeMoss, Broden and Bordelon, Blake and Foerster, Jakob and Hawes, Nick and Posner, Ingmar},
  journal={Physica D: Nonlinear Phenomena},
  volume={482},
  pages={134859},
  year={2025}
}

@article{multitask2026geometry,
  title={The geometry of multi-task grokking},
  author={[Authors]},
  journal={arXiv preprint arXiv:2602.18523},
  year={2026}
}

% === GROKKING: WEIGHT DECAY + UNIVERSALITY ===

@inproceedings{lyu2024dichotomy,
  title={Dichotomy of early and late phase implicit biases can provably induce grokking},
  author={Lyu, Kaifeng and Jin, Jikai and Li, Zhiyuan and Du, Simon and Lee, Jason and Hu, Wei},
  booktitle={ICLR 2024},
  year={2024}
}

@article{thilak2022slingshot,
  title={The slingshot mechanism: An empirical study of adaptive optimizers and the grokking phenomenon},
  author={Thilak, Vimal and Littwin, Etai and others},
  journal={arXiv preprint arXiv:2206.04817},
  year={2022}
}

@inproceedings{liu2023omnigrok,
  title={Omnigrok: Grokking beyond algorithmic data},
  author={Liu, Ziming and Michaud, Eric J and Tegmark, Max},
  booktitle={ICLR 2023},
  year={2023}
}

@inproceedings{humayun2024always,
  title={Deep networks always grok and here is why},
  author={Humayun, Ahmed Imtiaz and Balestriero, Randall and Baraniuk, Richard},
  booktitle={ICML 2024},
  year={2024}
}

@inproceedings{barak2022hidden,
  title={Hidden progress in deep learning: {SGD} learns parities near the computational limit},
  author={Barak, Boaz and Edelman, Benjamin and Goel, Surbhi and Kakade, Sham and Malach, Eran and Zhang, Cyril},
  booktitle={NeurIPS 2022},
  year={2022}
}

@article{merrill2023tale,
  title={A tale of two circuits: Grokking as competition of sparse and dense subnetworks},
  author={Merrill, William and Tsilivis, Nikolaos and Shukla, Aman},
  journal={arXiv preprint arXiv:2303.11873},
  year={2023}
}

@article{varma2023circuit,
  title={Explaining grokking through circuit efficiency},
  author={Varma, Vikrant and Shah, Rohin and Kenton, Zachary and Kram\'ar, J\'anos and Kumar, Ramana},
  journal={arXiv preprint arXiv:2309.02390},
  year={2023}
}

@inproceedings{kumar2024grokking,
  title={Grokking as the transition from lazy to rich training dynamics},
  author={Kumar, Tanishq and Bordelon, Blake and Gershman, Samuel and Pehlevan, Cengiz},
  booktitle={ICLR 2024},
  year={2024}
}

@article{davies2023unifying,
  title={Unifying grokking and double descent},
  author={Davies, Xander and Langosco, Lauro and Krueger, David},
  journal={arXiv preprint arXiv:2303.06173},
  year={2023}
}

% === HOPFIELD + ATTRACTOR DYNAMICS ===

@article{hopfield1982neural,
  title={Neural networks and physical systems with emergent collective computational abilities},
  author={Hopfield, John J},
  journal={Proceedings of the National Academy of Sciences},
  volume={79},
  number={8},
  pages={2554--2558},
  year={1982}
}

@article{amit1985storing,
  title={Storing infinite numbers of patterns in a spin-glass model of neural networks},
  author={Amit, Daniel J and Gutfreund, Hanoch and Sompolinsky, Haim},
  journal={Physical Review Letters},
  volume={55},
  number={14},
  pages={1530},
  year={1985}
}

@article{kaszas2025bifurcation,
  title={Memorisation and forgetting in a learning {H}opfield neural network: bifurcation mechanisms, attractors and basins},
  author={Kasz\'as, B\'alint and others},
  journal={arXiv preprint arXiv:2508.10765},
  year={2025}
}

@inproceedings{ramsauer2021hopfield,
  title={Hopfield networks is all you need},
  author={Ramsauer, Hubert and others},
  booktitle={ICLR 2021},
  year={2021}
}

% === KRAMERS + BARRIER CROSSING + SGD DYNAMICS ===

@article{kramers1940brownian,
  title={Brownian motion in a field of force and the diffusion model of chemical reactions},
  author={Kramers, Hendrik A},
  journal={Physica},
  volume={7},
  number={4},
  pages={284--304},
  year={1940}
}

@article{hanggi1990reaction,
  title={Reaction-rate theory: fifty years after {K}ramers},
  author={H\"anggi, Peter and Talkner, Peter and Borkovec, Michal},
  journal={Reviews of Modern Physics},
  volume={62},
  number={2},
  pages={251--341},
  year={1990}
}

@article{pollak2023kramers,
  title={Recent developments in {K}ramers' theory of reaction rates},
  author={Pollak, Eli},
  journal={ChemPhysChem},
  pages={e202300272},
  year={2023},
  doi={10.1002/cphc.202300272}
}

@article{ly2025multifractal,
  title={Optimization on multifractal loss landscapes explains a diverse range of geometrical and dynamical properties of deep learning},
  author={Ly, Alexander and Gong, Pulin},
  journal={Nature Communications},
  volume={16},
  pages={3252},
  year={2025},
  doi={10.1038/s41467-025-58532-9}
}

@article{mandt2017sgd,
  title={Stochastic gradient descent as approximate {B}ayesian inference},
  author={Mandt, Stephan and Hoffman, Matthew D and Blei, David M},
  journal={Journal of Machine Learning Research},
  volume={18},
  number={1},
  pages={4873--4907},
  year={2017}
}

@article{jastrzebski2017three,
  title={Three factors influencing minima in {SGD}},
  author={Jastrz\k{e}bski, Stanis\l{}aw and others},
  journal={arXiv preprint arXiv:1711.04623},
  year={2017}
}

% === SADDLE POINT ESCAPE ===

@inproceedings{jin2017escape,
  title={How to escape saddle points efficiently},
  author={Jin, Chi and Ge, Rong and Netrapalli, Praneeth and Kakade, Sham M and Jordan, Michael I},
  booktitle={ICML 2017},
  pages={1724--1732},
  year={2017}
}

@article{bornstein2025curvature,
  title={Escaping saddle points via curvature-calibrated perturbations},
  author={Bornstein, Max and others},
  journal={arXiv preprint arXiv:2508.16540},
  year={2025}
}

@article{cheridito2024gradient,
  title={Gradient descent provably escapes saddle points in the training of shallow {ReLU} networks},
  author={Cheridito, Patrick and others},
  journal={Journal of Machine Learning Research},
  year={2024}
}

% === PHASE TRANSITIONS IN COGNITION ===

@article{spivey2009phase,
  title={The phase transition in human cognition},
  author={Spivey, Michael J and Anderson, Sarah E and Dale, Rick},
  journal={New Mathematics and Natural Computation},
  volume={5},
  number={1},
  pages={197--220},
  year={2009}
}

@article{stephen2009dynamics,
  title={The dynamics of insight: Mathematical discovery as a phase transition},
  author={Stephen, Damian G and Boncoddo, Rebecca A and Magnuson, James S and Dixon, James A},
  journal={Memory \& Cognition},
  volume={37},
  number={8},
  pages={1132--1149},
  year={2009}
}

@article{viteri2022epistemic,
  title={Epistemic phase transitions in mathematical proofs},
  author={Viteri, Scott and DeDeo, Simon},
  journal={Cognition},
  volume={225},
  pages={105120},
  year={2022}
}

@article{durstewitz2010abrupt,
  title={Abrupt transitions between prefrontal neural ensemble states accompany behavioral transitions during rule learning},
  author={Durstewitz, Daniel and Vittoz, Nicole M and Floresco, Stan B and Seamans, Jeremy K},
  journal={Neuron},
  volume={66},
  number={3},
  pages={438--448},
  year={2010}
}

@article{reddy2022reinforcement,
  title={A reinforcement-based mechanism for discontinuous learning},
  author={Reddy, Gautam},
  journal={Proceedings of the National Academy of Sciences},
  volume={119},
  number={49},
  pages={e2215352119},
  year={2022}
}

% === INSIGHT + AHA MOMENTS ===

@article{jungbeeman2004neural,
  title={Neural activity when people solve verbal problems with insight},
  author={Jung-Beeman, Mark and Bowden, Edward M and Haberman, Jason and Frymiare, Jennifer L and Arambel-Liu, Stella and Greenblatt, Richard and Reber, Paul J and Kounios, John},
  journal={PLoS Biology},
  volume={2},
  number={4},
  pages={e97},
  year={2004}
}

@article{kounios2014cognitive,
  title={The cognitive neuroscience of insight},
  author={Kounios, John and Beeman, Mark},
  journal={Annual Review of Psychology},
  volume={65},
  pages={71--93},
  year={2014}
}

@article{ludmer2011uncovering,
  title={Uncovering camouflage: Amygdala activation predicts long-term memory of induced perceptual insight},
  author={Ludmer, Ravit and Dudai, Yadin and Rubin, Nava},
  journal={Neuron},
  volume={69},
  number={5},
  pages={1002--1014},
  year={2011}
}

% === REPRESENTATIONAL CHANGE ===

@incollection{ohlsson1992information,
  title={Information-processing explanations of insight and related phenomena},
  author={Ohlsson, Stellan},
  booktitle={Advances in the Psychology of Thinking},
  volume={1},
  pages={1--44},
  year={1992},
  publisher={Harvester Wheatsheaf}
}

@article{knoblich1999constraint,
  title={Constraint relaxation and chunk decomposition in insight problem solving},
  author={Knoblich, G\"unther and Ohlsson, Stellan and Haider, Hilde and Rhenius, Dirk},
  journal={Journal of Experimental Psychology: Learning, Memory, and Cognition},
  volume={25},
  number={6},
  pages={1534--1555},
  year={1999}
}

@article{chi2005commonsense,
  title={Commonsense conceptions of emergent processes: Why some misconceptions are robust},
  author={Chi, Michelene TH},
  journal={Journal of the Learning Sciences},
  volume={14},
  number={2},
  pages={161--199},
  year={2005}
}

@incollection{disessa1988knowledge,
  title={Knowledge in pieces},
  author={diSessa, Andrea A},
  booktitle={Constructivism in the Computer Age},
  pages={49--70},
  year={1988},
  publisher={Lawrence Erlbaum}
}

% === AGL ===

@article{reber1967implicit,
  title={Implicit learning of artificial grammars},
  author={Reber, Arthur S},
  journal={Journal of Verbal Learning and Verbal Behavior},
  volume={6},
  pages={855--863},
  year={1967}
}

@article{pothos2007theories,
  title={Theories of artificial grammar learning},
  author={Pothos, Emmanuel M},
  journal={Psychological Bulletin},
  volume={133},
  number={2},
  pages={227--244},
  year={2007}
}

@article{chen2024enigma,
  title={{ENIGMA}: A web application for running online artificial grammar learning experiments},
  author={Chen, Tsung-Ying},
  journal={Journal of Psycholinguistic Research},
  volume={53},
  number={3},
  pages={38},
  year={2024}
}

% === MUST-ADDRESS PAPERS ===

@article{zhang2025glass,
  title={Is grokking a computational glass relaxation?},
  author={Zhang, Xiaotian and Shang, Yue and Yang, Entao and Zhang, Ge},
  journal={NeurIPS 2025 (Spotlight)},
  year={2025},
  note={arXiv:2505.11411}
}

@article{prieto2025slt,
  title={Using physics-inspired singular learning theory to understand grokking},
  author={Prieto, Lucas and Barsbey, Melih and Mediano, Pedro and Birdal, Tolga},
  journal={arXiv preprint arXiv:2512.00686},
  year={2025}
}

@article{xie2022diffusion,
  title={A diffusion theory for deep learning dynamics: Stochastic gradient descent exponentially favors flat minima},
  author={Xie, Zeke and Sato, Issei and Sugiyama, Masashi},
  journal={ICLR 2022},
  year={2022},
  note={arXiv:2002.03495}
}

@article{simsekli2019tail,
  title={A tail-index analysis of stochastic gradient noise in deep neural networks},
  author={Simsekli, Umut},
  journal={ICML 2019},
  year={2019},
  note={arXiv:1901.06053}
}

@article{nguyen2019first,
  title={First exit time analysis of stochastic gradient descent under heavy-tailed gradient noise},
  author={Nguyen, Thanh Huy and Simsekli, Umut and Gurbuzbalaban, Mert and Richard, Gael},
  journal={NeurIPS 2019},
  year={2019},
  note={arXiv:1906.09069}
}

@article{sadrtdinov2025thermodynamic,
  title={{SGD} as free energy minimization: A thermodynamic view on neural network training},
  author={Sadrtdinov, Ildus and Klimov, Ivan and Lobacheva, Ekaterina and Vetrov, Dmitry},
  journal={arXiv preprint arXiv:2505.23489},
  year={2025}
}

@article{zhu2018anisotropic,
  title={The anisotropic noise in stochastic gradient descent: Its behavior of escaping from sharp minima and regularization effects},
  author={Zhu, Zhanxing and Wu, Jingfeng and Yu, Bing and Wu, Lei and Ma, Jinwen},
  journal={arXiv preprint arXiv:1803.00195},
  year={2018}
}

% === LOSS LANDSCAPE ===

@inproceedings{draxler2018essentially,
  title={Essentially no barriers in neural network energy landscape},
  author={Draxler, Felix and Veschgini, Kambis and Salmhofer, Manfred and Hamprecht, Fred A},
  booktitle={ICML 2018},
  year={2018}
}

% === DEPTH + LEARNING DYNAMICS ===

@article{fan2024deep,
  title={Deep Grokking: Would Deep Neural Networks Generalize Better?},
  author={Fan, Simin and Pascanu, Razvan and Jaggi, Martin},
  journal={arXiv preprint arXiv:2405.19454},
  year={2024}
}

@article{saxe2014exact,
  title={Exact solutions to the nonlinear dynamics of learning in deep linear neural networks},
  author={Saxe, Andrew M and McClelland, James L and Ganguli, Surya},
  journal={ICLR 2014},
  year={2014},
  note={arXiv:1312.6120}
}

@article{lewkowycz2020catapult,
  title={The large learning rate phase of deep learning: the catapult mechanism},
  author={Lewkowycz, Aitor and Gur-Ari, Guy},
  journal={arXiv preprint arXiv:2003.02218},
  year={2020}
}

% === SADDLE POINTS ===

@inproceedings{dauphin2014identifying,
  title={Identifying and attacking the saddle point problem in high-dimensional non-convex optimization},
  author={Dauphin, Yann N and Pascanu, Razvan and Gulcehre, Caglar and Cho, Kyunghyun and Ganguli, Surya and Bengio, Yoshua},
  booktitle={NeurIPS 2014},
  year={2014}
}

@article{jin2021nonconvex,
  title={On nonconvex optimization for machine learning: Gradients, stochasticity, and saddle points},
  author={Jin, Chi and Netrapalli, Praneeth and Ge, Rong and Kakade, Sham M and Jordan, Michael I},
  journal={Journal of the ACM},
  volume={68},
  number={2},
  year={2021}
}

% === MODERN HOPFIELD ===

@inproceedings{krotov2016dense,
  title={Dense associative memory for pattern recognition},
  author={Krotov, Dmitry and Hopfield, John J},
  booktitle={NeurIPS 2016},
  year={2016}
}

% === DISCONTINUOUS LEARNING ===

@article{gallistel2004learning,
  title={The learning curve: implications of a quantitative analysis},
  author={Gallistel, C Randy and Fairhurst, Stephen and Balsam, Peter},
  journal={Proceedings of the National Academy of Sciences},
  volume={101},
  number={36},
  pages={13124--13131},
  year={2004}
}

% === LATENT LEARNING ===

@article{tolman1948cognitive,
  title={Cognitive maps in rats and men},
  author={Tolman, Edward C},
  journal={Psychological Review},
  volume={55},
  number={4},
  pages={189--208},
  year={1948}
}

% === HONEYBEE CONCEPTS ===

@article{giurfa2001sameness,
  title={The concepts of `sameness' and `difference' in an insect},
  author={Giurfa, Martin and Zhang, Shaowu and Jenett, Arnim and Menzel, Randolf and Srinivasan, Mandyam V},
  journal={Nature},
  volume={410},
  pages={930--933},
  year={2001}
}

@article{avargues2012simultaneous,
  title={Simultaneous mastering of two abstract concepts by the miniature brain of bees},
  author={Avargues-Weber, Aurore and Dyer, Adrian G and Combe, Maud and Giurfa, Martin},
  journal={Proceedings of the National Academy of Sciences},
  volume={109},
  number={19},
  pages={7481--7486},
  year={2012}
}

% === PIGEON INSIGHT ===

@article{epstein1984insight,
  title={``Insight'' in the pigeon: Antecedents and determinants of an intelligent performance},
  author={Epstein, Robert and Kirshnit, Carolyn E and Lanza, Robert P and Rubin, L C},
  journal={Nature},
  volume={308},
  pages={61--62},
  year={1984}
}

% === VOCABULARY EXPLOSION ===

@article{mcmurray2007defusing,
  title={Defusing the childhood vocabulary explosion},
  author={McMurray, Bob},
  journal={Science},
  volume={317},
  number={5838},
  pages={631},
  year={2007}
}

% === REANALYSIS OF LEARNING CURVES ===

@article{kheifets2022slow,
  title={Slow or sudden: Re-interpreting the learning curve for modern systems neuroscience},
  author={Kheifets, Arkady and Bhatt, Ramesh S},
  journal={European Journal of Neuroscience},
  volume={55},
  number={11--12},
  pages={2828--2840},
  year={2022}
}

% === FOUNDATIONS ===

@article{rumelhart1986learning,
  title={Learning representations by back-propagating errors},
  author={Rumelhart, David E and Hinton, Geoffrey E and Williams, Ronald J},
  journal={Nature},
  volume={323},
  pages={533--536},
  year={1986}
}

@book{kohler1925mentality,
  title={The Mentality of Apes},
  author={K\"ohler, Wolfgang},
  year={1925},
  publisher={Routledge \& Kegan Paul}
}

@article{metcalfe1987intuition,
  title={Intuition in insight and noninsight problem solving},
  author={Metcalfe, Janet and Wiebe, David},
  journal={Memory \& Cognition},
  volume={15},
  number={3},
  pages={238--246},
  year={1987}
}

@article{wei2022emergent,
  title={Emergent abilities of large language models},
  author={Wei, Jason and Tay, Yi and others},
  journal={arXiv preprint arXiv:2206.07682},
  year={2022}
}

@article{schaeffer2024mirage,
  title={Are emergent abilities of large language models a mirage?},
  author={Schaeffer, Rylan and Miranda, Brando and Koyejo, Sanmi},
  booktitle={NeurIPS 2023},
  year={2024}
}
```

---

## IV. REFERENCE COUNT BY SECTION

| Section | Count | Key refs |
|---------|-------|----------|
| Introduction (anomalies) | 8 | Köhler, Metcalfe, Jung-Beeman, Kounios, Ludmer, Power, Wei, Schaeffer |
| Theory (Crystal/Glass, Props) | 12 | Hopfield, Amit, Kaszás, Kramers, Hänggi, Pollak, Ly, Jin, Bornstein, Mandt, Jastrzębski, Ramsauer |
| Grokking results | 14 | Rubin, Žunkovič, Clauw, Lau, DeMoss, MultiTask, Nanda, Gromov, Liu(×2), Lyu, Thilak, Humayun, Barak |
| Must-address | 7 | Zhang (glass), Prieto (SLT Arrhenius), Xie (diffusion), Simsekli (heavy tails), Nguyen (MFPT), Sadrtdinov (thermo), Zhu (anisotropic) |
| Discussion (cognition) | 16 | Spivey, Stephen, Viteri, Durstewitz, Reddy, Gallistel, Ohlsson(×2), Knoblich, Chi(×2), diSessa, Reber, Pothos, Chen, Tuller |
| Dynamic systems | 4 | Thelen, Smith, Case, Friedman (neural inertia) |
| Supporting (circuit theory) | 4 | Merrill, Varma, Kumar, Davies |
| **Total unique** | **~65** | |

At ~65 references this is on the higher end for NHB but justified by the cross-domain scope. Can trim to ~55 by moving supporting refs to supplementary.

---

## V. KEY PAPER TO ADDRESS: The Glass Relaxation Challenge

**Zhang & Shang (2025) — "Is Grokking a Computational Glass Relaxation?" NeurIPS 2025 Spotlight. arXiv:2505.11411.**

This is our most serious intellectual opponent. They claim grokking is NOT a first-order phase transition but a glass relaxation. Our response:

1. **Empirical (hysteresis)**: Our hysteresis test shows the crystal state persists at WD=0 while memorization is the global minimum. Glass relaxation predicts the system should relax BACK to the glass state — it doesn't.

2. **Kinetic (Arrhenius vs VFT)**: Glass relaxation follows Vogel-Fulcher-Tammann kinetics: t ~ exp[(T₀/T)^β] with β < 1 (stretched exponential). Our data fits Arrhenius (β = 1, R² = 0.976). This is testable: fit both models.

3. **Structural (depth non-monotonicity)**: Hysteresis strength is non-monotonic with depth (L2 > L1 > L4). Glass relaxation rate should be monotonic in system size.

4. **Honest concession**: Glass transitions and first-order transitions share features (hysteresis, slow dynamics). The memorization phase may have glassy character while the transition to Fourier order exhibits first-order signatures.

**Manuscript paragraph for Discussion:**

> "Zhang and Shang (2025) propose that grokking is a computational glass relaxation rather than a first-order phase transition, noting the absence of an entropy barrier in Boltzmann landscape sampling. Three observations favor the first-order interpretation for our system. First, the Arrhenius functional form ln(t) = A/λ_WD + B (R² = 0.976) is characteristic of barrier crossing, while glass relaxation typically follows Vogel-Fulcher-Tammann kinetics with a stretched exponential. Second, the hysteresis test demonstrates that the ordered state is self-sustaining at zero weight decay — a local minimum inaccessible from random initialization — which is the defining signature of first-order coexistence rather than gradual relaxation. Third, hysteresis strength varies non-monotonically with depth, inconsistent with the uniform relaxation expected in glass-like dynamics. We note that the glass and first-order frameworks are not mutually exclusive: the disordered (memorization) phase may itself have glassy character, while the transition to the ordered (Fourier) phase exhibits first-order signatures."
