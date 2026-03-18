"""
persistence.py — test whether transitions persist after perturbation

the operational definition of "irreversibility" (hysteresis analog):

    a transition is PERSISTENT if post-transition performance remains
    in the new regime after removal or alteration of the inducing
    conditions, controlling for ordinary retention.

this module tests persistence by comparing:
  - post-transition performance to pre-transition baseline
  - transfer/perturbation performance to learning-phase performance
  - decay rate after feedback removal

domain-agnostic: takes learning-phase and transfer-phase time-series.
"""

import numpy as np
from scipy import stats


def test_persistence(learning_series, transfer_series,
                     changepoint_idx=None, chance_level=0.5):
    """
    test whether learning persists into transfer/perturbation phase.

    args:
        learning_series: 1D array of learning-phase performance
        transfer_series: 1D array of transfer/perturbation performance
        changepoint_idx: if known, the transition point in learning_series.
                         if None, uses the midpoint.
        chance_level: baseline/chance performance

    returns:
        dict with:
            persists: bool — does post-transition performance hold?
            transfer_mean: mean transfer performance
            pre_transition_mean: mean performance before transition
            post_transition_mean: mean performance after transition
            transfer_vs_chance: one-sample t-test vs chance
            transfer_vs_pre: comparison to pre-transition baseline
            decay_rate: slope of transfer performance over trials (negative = decay)
            persistence_strength: "strong", "moderate", "weak", "none"
    """
    learn = np.asarray(learning_series, dtype=float)
    transfer = np.asarray(transfer_series, dtype=float)

    if len(learn) < 10 or len(transfer) < 5:
        return {"persists": False, "persistence_strength": "insufficient_data"}

    # determine pre/post split
    if changepoint_idx is None:
        changepoint_idx = len(learn) // 2
    cp = int(min(max(3, changepoint_idx), len(learn) - 3))

    pre = learn[:cp]
    post = learn[cp:]

    pre_mean = float(pre.mean())
    post_mean = float(post.mean())
    transfer_mean = float(transfer.mean())

    # test 1: transfer above chance?
    t_vs_chance, p_vs_chance = stats.ttest_1samp(transfer, chance_level)

    # test 2: transfer vs pre-transition (should be better)
    # use mann-whitney since samples may not be normal
    if len(pre) >= 3 and len(transfer) >= 3:
        u_stat, p_vs_pre = stats.mannwhitneyu(
            transfer, pre, alternative="greater"
        )
    else:
        u_stat, p_vs_pre = np.nan, 1.0

    # test 3: decay rate in transfer phase
    if len(transfer) >= 5:
        t_idx = np.arange(len(transfer), dtype=float)
        slope, intercept, r, p_slope, se = stats.linregress(t_idx, transfer)
        decay_rate = float(slope)
    else:
        decay_rate = 0.0
        p_slope = 1.0

    # classify persistence strength
    above_chance = p_vs_chance < 0.05 and transfer_mean > chance_level
    above_baseline = p_vs_pre < 0.05
    not_decaying = decay_rate > -0.01 or p_slope > 0.05

    if above_chance and above_baseline and not_decaying:
        strength = "strong"
    elif above_chance and (above_baseline or not_decaying):
        strength = "moderate"
    elif above_chance:
        strength = "weak"
    else:
        strength = "none"

    return {
        "persists": strength in ("strong", "moderate"),
        "persistence_strength": strength,
        "pre_transition_mean": pre_mean,
        "post_transition_mean": post_mean,
        "transfer_mean": transfer_mean,
        "transfer_vs_chance_p": float(p_vs_chance),
        "transfer_vs_pre_p": float(p_vs_pre),
        "decay_rate": decay_rate,
        "decay_p": float(p_slope),
    }


def test_persistence_controlled(transfer_series, learning_performance,
                                 chance_level=0.5):
    """
    test persistence while controlling for general learning ability.

    this addresses the key confound: "better learners transfer better"
    is not the same as "transitions are persistent."

    returns residual persistence: transfer accuracy after regressing out
    learning-phase performance.

    args:
        transfer_series: list of (transfer_accuracy, had_transition) tuples per participant
        learning_performance: list of final learning accuracy per participant

    returns:
        dict with logistic regression results showing whether transition
        predicts transfer BEYOND what learning performance predicts.
    """
    if len(transfer_series) < 10:
        return {"sufficient_data": False}

    transfer_acc = np.array([t[0] for t in transfer_series])
    had_transition = np.array([t[1] for t in transfer_series], dtype=float)
    learn_perf = np.asarray(learning_performance, dtype=float)

    # partial correlation: does transition predict transfer beyond learning?
    # regress transfer on learning performance, then check residuals vs transition
    slope_l, intercept_l, _, _, _ = stats.linregress(learn_perf, transfer_acc)
    residuals = transfer_acc - (slope_l * learn_perf + intercept_l)

    # test: do residuals differ by transition status?
    trans_resid = residuals[had_transition == 1]
    no_trans_resid = residuals[had_transition == 0]

    if len(trans_resid) < 3 or len(no_trans_resid) < 3:
        return {"sufficient_data": False}

    u_stat, p_val = stats.mannwhitneyu(trans_resid, no_trans_resid, alternative="greater")
    effect_size = (trans_resid.mean() - no_trans_resid.mean()) / (
        np.sqrt((trans_resid.var() + no_trans_resid.var()) / 2) + 1e-10
    )

    return {
        "sufficient_data": True,
        "residual_transfer_effect": float(trans_resid.mean() - no_trans_resid.mean()),
        "effect_size_d": float(effect_size),
        "p_value": float(p_val),
        "n_transition": int(had_transition.sum()),
        "n_no_transition": int((1 - had_transition).sum()),
        "learning_transfer_r": float(np.corrcoef(learn_perf, transfer_acc)[0, 1]),
        "interpretation": (
            "transition predicts transfer beyond learning ability"
            if p_val < 0.05 else
            "no residual effect of transition after controlling for learning"
        ),
    }
