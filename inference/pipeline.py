"""
pipeline.py — unified transition detection pipeline

takes raw learning data (one or more channels) and runs the
full inference stack:
  1. Ψ computation
  2. changepoint detection
  3. model comparison
  4. learner classification
  5. persistence testing (if transfer data provided)
  6. convergence testing (if multiple channels provided)

returns a single structured result suitable for cross-domain comparison.
"""

import numpy as np
from .psi import compute_psi_smooth, psi_peak_stats
from .changepoint import detect_changepoints
from .model_compare import fit_and_compare
from .classify import classify_learner
from .persistence import test_persistence
from .convergence import detect_channel_changepoints, test_convergence_permutation


def detect_transitions(accuracy_series,
                       confidence_series=None,
                       rt_series=None,
                       transfer_series=None,
                       extra_channels=None,
                       chance_level=0.5,
                       min_improvement=0.15,
                       convergence_max_gap=5):
    """
    full transition detection pipeline for a single learner.

    args:
        accuracy_series: 1D array of accuracy/performance over trials (REQUIRED)
        confidence_series: 1D array of confidence ratings (optional)
        rt_series: 1D array of reaction times (optional)
        transfer_series: 1D array of transfer/test phase accuracy (optional)
        extra_channels: dict of {name: 1D_array} for additional channels
        chance_level: baseline performance
        min_improvement: threshold for "no learning" classification
        convergence_max_gap: max trials between channels for convergence

    returns:
        dict with:
            classification: learner type and confidence
            psi: velocity order parameter statistics
            changepoints: detected changepoints in accuracy
            model_comparison: continuous vs changepoint vs HMM
            persistence: transfer/hysteresis test results (if transfer data given)
            convergence: cross-channel alignment (if multiple channels given)
            summary: one-line human-readable summary
    """
    acc = np.asarray(accuracy_series, dtype=float)
    result = {}

    # 1. Ψ (velocity order parameter)
    psi = compute_psi_smooth(acc, sigma=3.0)
    result["psi"] = psi_peak_stats(psi)
    result["psi_series"] = psi.tolist()

    # 2. changepoints
    result["changepoints"] = detect_changepoints(acc, method="pelt")

    # 3. model comparison
    result["model_comparison"] = fit_and_compare(acc)

    # 4. classification
    result["classification"] = classify_learner(
        acc, min_improvement=min_improvement, chance_level=chance_level
    )

    # 5. persistence (if transfer data available)
    if transfer_series is not None:
        transfer = np.asarray(transfer_series, dtype=float)
        cp_idx = result["model_comparison"].get("changepoint_idx")
        result["persistence"] = test_persistence(
            acc, transfer, changepoint_idx=cp_idx, chance_level=chance_level
        )
    else:
        result["persistence"] = None

    # 6. convergence (if multiple channels available)
    channels = {"accuracy": acc}
    if confidence_series is not None:
        channels["confidence"] = np.asarray(confidence_series, dtype=float)
    if rt_series is not None:
        # for RT, we want NEGATIVE changes (faster = better) to align with
        # accuracy increases. use -RT so changepoints align.
        channels["neg_rt"] = -np.asarray(rt_series, dtype=float)
    if extra_channels:
        channels.update({k: np.asarray(v, dtype=float) for k, v in extra_channels.items()})

    if len(channels) >= 2:
        ch_cps = detect_channel_changepoints(channels)
        result["convergence"] = test_convergence_permutation(
            ch_cps, max_gap=convergence_max_gap, n_trials=len(acc)
        )
    else:
        result["convergence"] = None

    # summary
    label = result["classification"]["label"]
    mc_best = result["model_comparison"]["best_model"]
    mc_delta = result["model_comparison"]["delta_bic"]
    n_cp = result["changepoints"]["n_changes"]

    parts = [f"type={label}", f"model={mc_best}(ΔBIC={mc_delta:.1f})", f"changepoints={n_cp}"]
    if result["persistence"]:
        parts.append(f"persists={result['persistence']['persistence_strength']}")
    if result["convergence"]:
        parts.append(f"converge={result['convergence']['convergence_score']:.2f}")
    result["summary"] = " | ".join(parts)

    return result


def detect_transitions_cohort(participants, chance_level=0.5, **kwargs):
    """
    run full pipeline on a list of participants.

    args:
        participants: list of dicts, each with at least "accuracy" key
                      and optional "confidence", "rt", "transfer" keys
        **kwargs: passed to detect_transitions

    returns:
        dict with:
            individual: list of per-participant results
            cohort_summary: aggregate statistics
    """
    results = []
    for p in participants:
        r = detect_transitions(
            accuracy_series=p["accuracy"],
            confidence_series=p.get("confidence"),
            rt_series=p.get("rt"),
            transfer_series=p.get("transfer"),
            extra_channels=p.get("extra_channels"),
            chance_level=chance_level,
            **kwargs,
        )
        results.append(r)

    # aggregate
    labels = [r["classification"]["label"] for r in results]
    label_counts = {}
    for lbl in labels:
        label_counts[lbl] = label_counts.get(lbl, 0) + 1

    n = len(results)
    label_fractions = {k: v / n for k, v in label_counts.items()}

    # persistence summary
    persistence_results = [r["persistence"] for r in results if r["persistence"]]
    if persistence_results:
        n_persist = sum(1 for p in persistence_results if p.get("persists", False))
        persist_rate = n_persist / len(persistence_results)
    else:
        persist_rate = None

    # convergence summary
    conv_results = [r["convergence"] for r in results if r["convergence"]]
    if conv_results:
        mean_conv = np.mean([c["convergence_score"] for c in conv_results])
    else:
        mean_conv = None

    return {
        "individual": results,
        "cohort_summary": {
            "n": n,
            "label_counts": label_counts,
            "label_fractions": label_fractions,
            "abrupt_fraction": label_fractions.get("abrupt", 0),
            "persistence_rate": persist_rate,
            "mean_convergence_score": mean_conv,
        },
    }
