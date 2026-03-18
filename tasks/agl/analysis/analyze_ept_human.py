#!/usr/bin/env python3
"""
EPT Human Experiment — Primary Analysis Script

implements the pre-registered analysis plan for Paper 3.
reads JSON data from data/ directory, runs all 5 primary analyses.
"""

import json
import glob
import numpy as np
from scipy import stats
from pathlib import Path


def load_all_participants(data_dir="data"):
    """load all participant JSON files"""
    files = sorted(glob.glob(f"{data_dir}/*.json"))
    participants = []
    for f in files:
        with open(f) as fh:
            participants.append(json.load(fh))
    return participants


def compute_velocity(accuracy_seq, window=5):
    """rolling accuracy change velocity — bounded, non-circular"""
    arr = np.array(accuracy_seq, dtype=float)
    rolling = np.convolve(arr, np.ones(window) / window, mode="same")
    vel = np.abs(np.diff(rolling, prepend=rolling[0]))
    return vel


def get_aha_trial(participant):
    """get first aha button press trial, or None"""
    if participant["aha_events"]:
        return participant["aha_events"][0]["trial_num"]
    return None


def get_learning_trials(participant):
    """extract learning phase trials in order"""
    return [t for t in participant["trials"] if t["phase"] == "learning"]


def get_transfer_trials(participant):
    return [t for t in participant["trials"] if t["phase"] == "transfer"]


# ─────────────────────────────────────────────
# P1: velocity spike at insight onset
# ─────────────────────────────────────────────

def test_p1_velocity_spike(participants):
    """
    test whether behavioral velocity peaks at self-reported aha trial.
    uses permutation test to avoid circularity.
    """
    print("\n" + "=" * 60)
    print("P1: VELOCITY SPIKE AT AHA ONSET")
    print("=" * 60)

    z_scores = []
    for p in participants:
        aha = get_aha_trial(p)
        if aha is None:
            continue

        learning = get_learning_trials(p)
        if len(learning) < 20:
            continue

        accuracy_seq = [t["correct"] for t in learning]
        vel = compute_velocity(accuracy_seq)

        # find aha position in learning sequence
        learning_trial_nums = [t["trial_num"] for t in learning]
        if aha not in learning_trial_nums:
            continue
        aha_idx = learning_trial_nums.index(aha)

        # baseline: trials far from aha
        baseline_mask = np.ones(len(vel), dtype=bool)
        baseline_mask[max(0, aha_idx - 5):min(len(vel), aha_idx + 6)] = False
        if baseline_mask.sum() < 10:
            continue

        bl_mean = vel[baseline_mask].mean()
        bl_std = vel[baseline_mask].std()
        if bl_std < 1e-10:
            continue

        # peak in [-2, +2] around aha
        pk_start = max(0, aha_idx - 2)
        pk_end = min(len(vel), aha_idx + 3)
        peak = vel[pk_start:pk_end].max()

        z = (peak - bl_mean) / bl_std
        z_scores.append(z)

    if len(z_scores) < 5:
        print(f"  insufficient aha participants: {len(z_scores)}")
        return None

    z_arr = np.array(z_scores)
    t_stat, p_val = stats.ttest_1samp(z_arr, 0)
    d = z_arr.mean() / (z_arr.std() + 1e-10)

    # permutation test
    n_perm = 5000
    null_means = []
    for _ in range(n_perm):
        perm_z = np.random.choice(z_arr, size=len(z_arr), replace=True)
        # shift each z by random offset
        null_means.append(np.random.normal(0, z_arr.std(), len(z_arr)).mean())
    perm_p = np.mean([nm >= z_arr.mean() for nm in null_means])

    print(f"  n aha participants: {len(z_scores)}")
    print(f"  mean z: {z_arr.mean():.3f} +/- {z_arr.std():.3f}")
    print(f"  t-test: t={t_stat:.3f}, p={p_val:.4f}")
    print(f"  permutation p: {perm_p:.4f}")
    print(f"  cohen's d: {d:.3f}")

    return {"n": len(z_scores), "mean_z": float(z_arr.mean()),
            "t": float(t_stat), "p": float(p_val), "d": float(d),
            "perm_p": float(perm_p)}


# ─────────────────────────────────────────────
# P2: dose-response (grammar difficulty)
# ─────────────────────────────────────────────

def test_p2_dose_response(participants):
    print("\n" + "=" * 60)
    print("P2: DOSE-RESPONSE (GRAMMAR DIFFICULTY)")
    print("=" * 60)

    by_condition = {}
    for p in participants:
        cond = p["condition"]
        if cond not in by_condition:
            by_condition[cond] = []

        learning = get_learning_trials(p)
        if len(learning) < 20:
            continue

        last20_acc = np.mean([t["correct"] for t in learning[-20:]])
        reached_criterion = last20_acc >= 0.75
        aha = get_aha_trial(p) is not None

        by_condition[cond].append({
            "criterion": reached_criterion,
            "aha": aha,
            "last20_acc": last20_acc,
        })

    for cond in sorted(by_condition.keys()):
        runs = by_condition[cond]
        crit_rate = np.mean([r["criterion"] for r in runs])
        aha_rate = np.mean([r["aha"] for r in runs])
        acc = np.mean([r["last20_acc"] for r in runs])
        print(f"  {cond:8s}: n={len(runs)}, criterion={crit_rate:.0%}, "
              f"aha={aha_rate:.0%}, last20_acc={acc:.3f}")

    # chi-squared on criterion rates
    if len(by_condition) >= 2:
        observed = []
        for cond in sorted(by_condition.keys()):
            runs = by_condition[cond]
            n_crit = sum(r["criterion"] for r in runs)
            n_not = len(runs) - n_crit
            observed.append([n_crit, n_not])
        chi2, p_val, dof, expected = stats.chi2_contingency(observed)
        print(f"\n  chi-squared: chi2={chi2:.3f}, p={p_val:.4f}, dof={dof}")

    return by_condition


# ─────────────────────────────────────────────
# P3: hysteresis (transfer test)
# ─────────────────────────────────────────────

def test_p3_hysteresis(participants):
    print("\n" + "=" * 60)
    print("P3: HYSTERESIS (TRANSFER ACCURACY)")
    print("=" * 60)

    aha_transfer = []
    noaha_transfer = []

    for p in participants:
        transfer = get_transfer_trials(p)
        if len(transfer) < 10:
            continue

        transfer_acc = np.mean([t["correct"] for t in transfer])
        has_aha = get_aha_trial(p) is not None

        if has_aha:
            aha_transfer.append(transfer_acc)
        else:
            noaha_transfer.append(transfer_acc)

    if len(aha_transfer) < 5 or len(noaha_transfer) < 5:
        print(f"  insufficient: aha={len(aha_transfer)}, no-aha={len(noaha_transfer)}")
        return None

    aha_arr = np.array(aha_transfer)
    noaha_arr = np.array(noaha_transfer)

    u_stat, p_val = stats.mannwhitneyu(aha_arr, noaha_arr, alternative="greater")
    pooled_std = np.sqrt((aha_arr.std() ** 2 + noaha_arr.std() ** 2) / 2)
    d = (aha_arr.mean() - noaha_arr.mean()) / (pooled_std + 1e-10)

    print(f"  aha group: n={len(aha_arr)}, transfer_acc={aha_arr.mean():.3f} +/- {aha_arr.std():.3f}")
    print(f"  no-aha group: n={len(noaha_arr)}, transfer_acc={noaha_arr.mean():.3f} +/- {noaha_arr.std():.3f}")
    print(f"  mann-whitney: U={u_stat:.0f}, p={p_val:.4f}")
    print(f"  cohen's d: {d:.3f}")

    return {"n_aha": len(aha_arr), "n_noaha": len(noaha_arr),
            "aha_mean": float(aha_arr.mean()), "noaha_mean": float(noaha_arr.mean()),
            "U": float(u_stat), "p": float(p_val), "d": float(d)}


# ─────────────────────────────────────────────
# P4: marker convergence
# ─────────────────────────────────────────────

def test_p4_convergence(participants):
    print("\n" + "=" * 60)
    print("P4: MARKER CONVERGENCE")
    print("=" * 60)

    distances = []
    for p in participants:
        aha = get_aha_trial(p)
        if aha is None:
            continue

        # confidence jump: first trial where confidence >= 7
        conf_jump = None
        for c in p["confidence_trajectory"]:
            if c["rating"] >= 7:
                conf_jump = c["after_trial"]
                break

        # RT velocity peak
        learning = get_learning_trials(p)
        if len(learning) < 20:
            continue
        rts = [t["rt_ms"] for t in learning]
        rt_vel = np.abs(np.diff(rts))
        if len(rt_vel) > 0:
            rt_peak_idx = np.argmax(rt_vel)
            rt_peak_trial = learning[rt_peak_idx + 1]["trial_num"]
        else:
            rt_peak_trial = None

        # compute distances between markers
        markers = {"aha": aha}
        if conf_jump is not None:
            markers["confidence"] = conf_jump
        if rt_peak_trial is not None:
            markers["rt_peak"] = rt_peak_trial

        if len(markers) >= 2:
            vals = list(markers.values())
            max_dist = max(vals) - min(vals)
            distances.append(max_dist)
            within3 = max_dist <= 3

            marker_str = ", ".join(f"{k}={v}" for k, v in markers.items())
            print(f"  {p['participant_id'][:12]}: {marker_str} | "
                  f"spread={max_dist} {'CONVERGE' if within3 else ''}")

    if distances:
        dist_arr = np.array(distances)
        n_converge = sum(d <= 3 for d in distances)
        print(f"\n  mean marker spread: {dist_arr.mean():.1f} trials")
        print(f"  converged (within 3): {n_converge}/{len(distances)} "
              f"({n_converge / len(distances):.0%})")

    return {"distances": distances}


# ─────────────────────────────────────────────
# P5: RT variability (IPR analog)
# ─────────────────────────────────────────────

def test_p5_rt_variability(participants):
    print("\n" + "=" * 60)
    print("P5: RT VARIABILITY (IPR ANALOG)")
    print("=" * 60)

    aha_cvs = []
    noaha_cvs = []

    for p in participants:
        learning = get_learning_trials(p)
        if len(learning) < 30:
            continue

        # CV of RT in last 20 trials
        last20_rts = [t["rt_ms"] for t in learning[-20:]]
        cv = np.std(last20_rts) / (np.mean(last20_rts) + 1e-10)

        has_aha = get_aha_trial(p) is not None
        if has_aha:
            aha_cvs.append(cv)
        else:
            noaha_cvs.append(cv)

    if len(aha_cvs) < 5 or len(noaha_cvs) < 5:
        print(f"  insufficient: aha={len(aha_cvs)}, no-aha={len(noaha_cvs)}")
        return None

    aha_arr = np.array(aha_cvs)
    noaha_arr = np.array(noaha_cvs)

    # aha group should have LOWER CV (more consistent = crystal)
    u_stat, p_val = stats.mannwhitneyu(aha_arr, noaha_arr, alternative="less")
    pooled_std = np.sqrt((aha_arr.std() ** 2 + noaha_arr.std() ** 2) / 2)
    d = (noaha_arr.mean() - aha_arr.mean()) / (pooled_std + 1e-10)

    print(f"  aha group: n={len(aha_arr)}, RT_CV={aha_arr.mean():.3f} +/- {aha_arr.std():.3f}")
    print(f"  no-aha group: n={len(noaha_arr)}, RT_CV={noaha_arr.mean():.3f} +/- {noaha_arr.std():.3f}")
    print(f"  mann-whitney (aha < noaha): U={u_stat:.0f}, p={p_val:.4f}")
    print(f"  cohen's d (noaha-aha): {d:.3f}")

    return {"aha_cv": float(aha_arr.mean()), "noaha_cv": float(noaha_arr.mean()),
            "U": float(u_stat), "p": float(p_val), "d": float(d)}


# ─────────────────────────────────────────────
# main
# ─────────────────────────────────────────────

def main():
    import sys
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "data"

    participants = load_all_participants(data_dir)
    print(f"loaded {len(participants)} participants")

    if len(participants) == 0:
        print("no data found. collect data first.")
        return

    # bonferroni correction: alpha = 0.01 per test (5 tests, family alpha = 0.05)
    alpha = 0.01

    results = {}
    results["P1"] = test_p1_velocity_spike(participants)
    results["P2"] = test_p2_dose_response(participants)
    results["P3"] = test_p3_hysteresis(participants)
    results["P4"] = test_p4_convergence(participants)
    results["P5"] = test_p5_rt_variability(participants)

    # summary
    print("\n" + "=" * 60)
    print("SUMMARY (Bonferroni-corrected α = 0.01)")
    print("=" * 60)

    for name, r in results.items():
        if r is None:
            print(f"  {name}: INSUFFICIENT DATA")
        elif "p" in r:
            sig = "***" if r["p"] < 0.001 else "**" if r["p"] < alpha else "*" if r["p"] < 0.05 else "ns"
            print(f"  {name}: p={r['p']:.4f} {sig}, d={r.get('d', 'N/A')}")

    # save results
    out_path = f"{data_dir}/../analysis/results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nresults saved: {out_path}")


if __name__ == "__main__":
    main()
