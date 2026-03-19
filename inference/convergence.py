"""
convergence.py — test whether multiple measurement channels agree on transition timing

if a transition is real, independent observables should show
coordinated changes at approximately the same time:
  - accuracy changepoint
  - confidence jump
  - RT reorganization
  - self-report (aha)
  - any other channel

this module tests temporal alignment across channels WITHOUT
using arbitrary thresholds (like "confidence >= 7").
instead, it detects changepoints in EACH channel independently,
then measures inter-channel agreement.
"""

import numpy as np
from .changepoint import detect_changepoints
from scipy import stats


def detect_channel_changepoints(channels, method="pelt", **kwargs):
    """
    detect changepoints independently in each measurement channel.

    args:
        channels: dict of {channel_name: 1D_array}
                  e.g. {"accuracy": [...], "confidence": [...], "rt": [...]}
        method: changepoint detection method
        **kwargs: passed to detect_changepoints

    returns:
        dict mapping channel_name -> list of changepoint indices
    """
    results = {}
    for name, series in channels.items():
        arr = np.asarray(series, dtype=float)
        if len(arr) < 10:
            results[name] = []
            continue

        cp = detect_changepoints(arr, method=method, **kwargs)
        results[name] = cp["changepoints"]

    return results


def test_convergence(channel_changepoints, max_gap=5):
    """
    test whether changepoints across channels are temporally aligned.

    args:
        channel_changepoints: dict of {channel_name: [changepoint_indices]}
                              (output from detect_channel_changepoints)
        max_gap: maximum distance (in trials) between changepoints
                 for them to count as "converged"

    returns:
        dict with:
            n_channels: number of channels with at least one changepoint
            n_converged: number of channel pairs within max_gap
            convergence_score: fraction of valid pairs that converge
            mean_spread: mean distance between closest changepoints across channels
            median_spread: median distance
            converged: bool — majority of channels agree within max_gap
            channel_timing: dict of channel -> earliest changepoint
            cluster: the consensus transition region [earliest, latest]
    """
    # extract the first (primary) changepoint from each channel
    timing = {}
    for name, cps in channel_changepoints.items():
        if cps:
            timing[name] = cps[0]  # first changepoint only

    n_channels = len(timing)

    if n_channels < 2:
        return {
            "n_channels": n_channels,
            "converged": False,
            "convergence_score": 0.0,
            "reasoning": f"only {n_channels} channel(s) with detected changepoints",
        }

    # compute pairwise distances
    names = list(timing.keys())
    values = [timing[n] for n in names]

    pairs_total = 0
    pairs_converged = 0
    distances = []

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            d = abs(values[i] - values[j])
            distances.append(d)
            pairs_total += 1
            if d <= max_gap:
                pairs_converged += 1

    spread = np.array(distances)
    convergence_score = pairs_converged / pairs_total if pairs_total > 0 else 0

    return {
        "n_channels": n_channels,
        "n_converged_pairs": pairs_converged,
        "n_total_pairs": pairs_total,
        "convergence_score": convergence_score,
        "mean_spread": float(spread.mean()),
        "median_spread": float(np.median(spread)),
        "max_spread": float(spread.max()),
        "converged": convergence_score >= 0.5,
        "channel_timing": timing,
        "cluster": [int(min(values)), int(max(values))],
    }


def test_convergence_permutation(channel_changepoints, max_gap=5, n_perm=5000,
                                  n_trials=None):
    """
    permutation test: is the observed convergence better than expected
    by chance?

    randomly places each channel's changepoint uniformly within the
    trial range, recomputes convergence score, and estimates a p-value.

    args:
        channel_changepoints: dict of {channel_name: [changepoint_indices]}
        max_gap: max distance for convergence
        n_perm: number of permutations
        n_trials: total number of trials in the experiment. if None,
                  estimated as max(all_changepoints) + 20. providing the
                  actual trial count avoids bias from data-dependent range.
    """
    result = test_convergence(channel_changepoints, max_gap=max_gap)

    if result["n_channels"] < 2:
        result["perm_p"] = 1.0
        return result

    observed_score = result["convergence_score"]

    # null range: use actual trial count if provided (avoids bias)
    timing = result["channel_timing"]
    all_cps = list(timing.values())
    if n_trials is not None:
        trial_range = n_trials
    else:
        # fallback: estimate from data (add buffer to avoid tight range)
        trial_range = max(all_cps) + 20 if all_cps else 100

    null_scores = []
    n_channels = len(timing)
    names = list(timing.keys())

    rng = np.random.default_rng(42)

    for _ in range(n_perm):
        # random changepoint for each channel
        fake_cps = rng.integers(0, max(trial_range, 10), size=n_channels)

        # count converged pairs
        pairs_conv = 0
        pairs_total = 0
        for i in range(n_channels):
            for j in range(i + 1, n_channels):
                pairs_total += 1
                if abs(fake_cps[i] - fake_cps[j]) <= max_gap:
                    pairs_conv += 1

        null_scores.append(pairs_conv / pairs_total if pairs_total > 0 else 0)

    perm_p = np.mean([ns >= observed_score for ns in null_scores])

    result["perm_p"] = float(perm_p)
    result["null_mean"] = float(np.mean(null_scores))
    result["null_std"] = float(np.std(null_scores))

    return result
