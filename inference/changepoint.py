"""
changepoint.py — detect abrupt transitions in learning curves

two methods:
  1. PELT (Pruned Exact Linear Time) — offline, exact, fast
  2. BOCPD (Bayesian Online Changepoint Detection) — online, probabilistic

both are domain-agnostic: they take a 1D time-series and return
changepoint locations + confidence.
"""

import numpy as np
import ruptures


def pelt(series, model="l2", pen=None, min_size=10):
    """
    PELT changepoint detection via ruptures library.

    uses "l2" cost (mean-shift model) by default, which detects changes
    in signal mean — appropriate for learning curves.

    args:
        series: 1D array of performance values
        model: cost model — "l2" (mean shift, default), "rbf" (kernel), "normal" (mean+var)
        pen: penalty for adding changepoints. if None, auto-calibrated
             conservatively to avoid over-segmenting noisy data.
        min_size: minimum segment length (default 10 to avoid micro-segments)

    returns:
        dict with:
            changepoints: list of changepoint indices (excluding final index)
            n_changes: number of detected changepoints
            segments: list of (start, end) tuples for each segment
            segment_means: mean performance in each segment
    """
    arr = np.asarray(series, dtype=float).reshape(-1, 1)
    n = len(arr)

    if n < 2 * min_size:
        return {"changepoints": [], "n_changes": 0,
                "segments": [(0, n)], "segment_means": [float(arr.mean())]}

    algo = ruptures.Pelt(model=model, min_size=min_size, jump=1)
    algo.fit(arr)

    if pen is None:
        pen = _auto_penalty(algo, arr, min_size)

    bkps = algo.predict(pen=pen)

    # bkps includes final index — remove it
    changepoints = [b for b in bkps if b < n]

    # compute segments
    boundaries = [0] + changepoints + [n]
    segments = [(boundaries[i], boundaries[i + 1]) for i in range(len(boundaries) - 1)]
    segment_means = [float(arr[s:e].mean()) for s, e in segments]

    return {
        "changepoints": changepoints,
        "n_changes": len(changepoints),
        "segments": segments,
        "segment_means": segment_means,
    }


def _auto_penalty(algo, arr, min_size):
    """
    conservative penalty: finds only major mean-shifts, not noise.

    design choice: caps at 2 changepoints. most learning curves have
    0–2 real transitions (pre-learning, transition, post-learning).
    detecting 3+ changepoints in noisy behavioral data usually means
    over-segmentation. if you need to detect multi-regime switching,
    use the HMM model in model_compare.py instead.

    method: sweep BIC-scaled penalties, find smallest where n_cp <= 2.
    """
    n = len(arr)
    signal_range = float(arr.max() - arr.min())

    # penalty proportional to signal variance * log(n)
    # this is the BIC penalty for gaussian mean-shift
    sigma2 = float(np.var(arr))
    pen_bic = sigma2 * np.log(n)

    # also try a range and find the elbow
    pens = np.linspace(pen_bic * 0.1, pen_bic * 5, 30)
    n_cps = []
    for p in pens:
        bkps = algo.predict(pen=p)
        n_cps.append(len([b for b in bkps if b < n]))

    n_cps = np.array(n_cps)

    # find smallest penalty where n_changepoints <= 2
    for i, nc in enumerate(n_cps):
        if nc <= 2:
            # use this penalty (conservative)
            return float(pens[i])

    # fallback: high penalty, allowing at most 1 changepoint
    return float(pen_bic * 3)


def bocpd(series, hazard_rate=1 / 50, mu0=0.5, kappa0=1.0, alpha0=1.0, beta0=0.1):
    """
    bayesian online changepoint detection (Adams & MacKay 2007).

    returns run-length posterior at each time step, plus
    MAP changepoint locations.

    args:
        series: 1D array
        hazard_rate: prior probability of changepoint at each step (1/expected_run_length)
        mu0, kappa0, alpha0, beta0: normal-inverse-gamma prior parameters

    returns:
        dict with:
            changepoints: MAP changepoint indices
            run_length_posterior: (T, T) matrix of P(run_length | data_1:t)
            growth_probs: P(changepoint at t) for each t
    """
    arr = np.asarray(series, dtype=float)
    T = len(arr)

    # run length posterior: R[t, r] = P(run_length = r at time t)
    R = np.zeros((T + 1, T + 1))
    R[0, 0] = 1.0

    # sufficient statistics for each run length
    mu = np.full(T + 1, mu0)
    kappa = np.full(T + 1, kappa0)
    alpha = np.full(T + 1, alpha0)
    beta = np.full(T + 1, beta0)

    growth_probs = np.zeros(T)

    for t in range(T):
        x = arr[t]

        # predictive probability under each run length
        pred_var = beta * (kappa + 1) / (alpha * kappa)
        pred_var = np.maximum(pred_var, 1e-12)
        # student-t pdf approximated by normal for speed
        pred_prob = np.exp(-0.5 * (x - mu) ** 2 / pred_var) / np.sqrt(2 * np.pi * pred_var)

        # growth probabilities
        growth = R[t, :T + 1] * pred_prob[:T + 1] * (1 - hazard_rate)

        # changepoint probability
        cp = np.sum(R[t, :T + 1] * pred_prob[:T + 1] * hazard_rate)

        # update run length posterior
        R[t + 1, 1:T + 2] = growth[:T + 1]
        R[t + 1, 0] = cp

        # normalize
        evidence = R[t + 1, :].sum()
        if evidence > 0:
            R[t + 1, :] /= evidence

        growth_probs[t] = cp / (evidence + 1e-12) if evidence > 0 else 0

        # update sufficient statistics
        mu_new = (kappa * mu + x) / (kappa + 1)
        kappa_new = kappa + 1
        alpha_new = alpha + 0.5
        beta_new = beta + kappa * (x - mu) ** 2 / (2 * (kappa + 1))

        # shift for new run length
        mu[1:] = mu_new[:-1]
        kappa[1:] = kappa_new[:-1]
        alpha[1:] = alpha_new[:-1]
        beta[1:] = beta_new[:-1]
        # reset for run_length = 0
        mu[0] = mu0
        kappa[0] = kappa0
        alpha[0] = alpha0
        beta[0] = beta0

    # extract MAP changepoints: peaks in growth_probs
    changepoints = _extract_peaks(growth_probs, min_height=0.3, min_distance=5)

    return {
        "changepoints": changepoints,
        "growth_probs": growth_probs,
    }


def _extract_peaks(signal, min_height=0.3, min_distance=5):
    """simple peak detection: local maxima above threshold, separated by min_distance."""
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > min_height and signal[i] > signal[i - 1] and signal[i] >= signal[i + 1]:
            if not peaks or (i - peaks[-1]) >= min_distance:
                peaks.append(i)
    return peaks


def detect_changepoints(series, method="pelt", **kwargs):
    """
    unified interface: detect changepoints in a learning curve.

    args:
        series: 1D array of performance values
        method: "pelt" (offline, recommended) or "bocpd" (online/probabilistic)
        **kwargs: passed to the chosen method

    returns:
        dict with at minimum: changepoints (list of indices), n_changes (int)
    """
    if method == "pelt":
        return pelt(series, **kwargs)
    elif method == "bocpd":
        return bocpd(series, **kwargs)
    else:
        raise ValueError(f"unknown method: {method}. use 'pelt' or 'bocpd'.")
