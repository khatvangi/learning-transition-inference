"""
psi.py — velocity order parameter Ψ(t) = |d(performance)/dt|

computes the instantaneous rate of change in a learning curve.
this is the primary observable for detecting transition sharpness.

domain-agnostic: works on any 1D performance time-series.
"""

import numpy as np
from scipy.ndimage import gaussian_filter1d


def compute_psi(series, window=5):
    """
    raw velocity: rolling-average smoothed, then absolute first difference.

    args:
        series: 1D array of performance values (accuracy, score, etc.)
        window: smoothing window for rolling average

    returns:
        psi: array same length as series, Ψ(t) = |d(smoothed)/dt|
    """
    arr = np.asarray(series, dtype=float)
    if len(arr) < window:
        return np.abs(np.diff(arr, prepend=arr[0]))

    # rolling mean for smoothing
    kernel = np.ones(window) / window
    smoothed = np.convolve(arr, kernel, mode="same")

    # absolute first difference
    psi = np.abs(np.diff(smoothed, prepend=smoothed[0]))
    return psi


def compute_psi_smooth(series, sigma=3.0):
    """
    gaussian-smoothed velocity. better for noisy behavioral data
    than rectangular window.

    args:
        series: 1D array of performance values
        sigma: gaussian kernel width in samples

    returns:
        psi: array same length as series
    """
    arr = np.asarray(series, dtype=float)
    smoothed = gaussian_filter1d(arr, sigma=sigma)
    psi = np.abs(np.gradient(smoothed))
    return psi


def psi_peak_stats(psi):
    """
    characterize the Ψ peak: location, amplitude, duration, localization.

    returns dict with:
        peak_idx: index of maximum Ψ
        peak_value: Ψ at peak
        baseline_mean: mean Ψ outside peak region
        baseline_std: std of Ψ outside peak region
        z_score: (peak - baseline_mean) / baseline_std
        spike_ratio: peak / baseline_mean (analog of 10^6 ratio in grokking)
        duration: number of consecutive samples where Ψ > 2*baseline_std
        localization: duration / total_length (fraction of time in spike)
    """
    psi = np.asarray(psi, dtype=float)
    if len(psi) < 10:
        return None

    peak_idx = int(np.argmax(psi))
    peak_value = float(psi[peak_idx])

    # baseline: everything outside ±5 of peak
    mask = np.ones(len(psi), dtype=bool)
    lo = max(0, peak_idx - 5)
    hi = min(len(psi), peak_idx + 6)
    mask[lo:hi] = False

    if mask.sum() < 5:
        # too short to compute baseline
        return {"peak_idx": peak_idx, "peak_value": peak_value}

    bl_mean = float(psi[mask].mean())
    bl_std = float(psi[mask].std())

    z = (peak_value - bl_mean) / (bl_std + 1e-12)
    spike_ratio = peak_value / (bl_mean + 1e-12)

    # spike duration: contiguous region above 2*baseline_std
    threshold = bl_mean + 2 * bl_std
    above = psi > threshold
    # find contiguous block containing peak
    duration = 0
    for i in range(peak_idx, len(psi)):
        if above[i]:
            duration += 1
        else:
            break
    for i in range(peak_idx - 1, -1, -1):
        if above[i]:
            duration += 1
        else:
            break

    localization = duration / len(psi)

    return {
        "peak_idx": peak_idx,
        "peak_value": peak_value,
        "baseline_mean": bl_mean,
        "baseline_std": bl_std,
        "z_score": z,
        "spike_ratio": spike_ratio,
        "duration": duration,
        "localization": localization,
    }
