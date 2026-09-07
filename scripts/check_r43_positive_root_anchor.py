#!/usr/bin/env python3
"""Algebraic regression only. This is not a numerical P11/C6 certificate."""
import json
import subprocess
from pathlib import Path

import numpy as np


BASE = "55a3a1617513cc5d82c47d0cfd606c6b0894c984"
ROOT = Path(__file__).resolve().parents[1]
CHECKS = []
REPAIRED = {
    "papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex":
        "6df7308cf269f09c6564ab162ed9b647cb3929da",
    "papers/P11_sections/P11_O3o_TC1_NearNull_Remainder_Collapse.tex":
        "741124dd8dbab29452b24ca9af5d4be5dd7a8f67",
    "papers/P11_sections/P11_O3p_Vanishing_NearNull_Core.tex":
        "1fb4217407e68ac3e2be3d2259ccd97ef450a40d",
}


def opnorm(matrix):
    return float(np.linalg.norm(matrix, 2))


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


def positive_root_and_column_polar(feature):
    # SVD avoids squaring the condition number in a formed Gram matrix.
    left, singular, right = np.linalg.svd(feature, full_matrices=False)
    root = (right.conj().T * singular) @ right
    polar = left @ right
    return root, polar


records = []
for complex_case in (False, True):
    for n in (8, 16, 32, 64):
        target_dim, source_dim = n + 3, n + 2
        dtype = complex if complex_case else float
        inclusion = np.zeros((target_dim, source_dim), dtype=dtype)
        retained = [0, 1, *range(3, target_dim)]
        inclusion[retained, np.arange(source_dim)] = 1
        nu_s = np.zeros(target_dim, dtype=dtype)
        nu_s[:3] = [1, 0.5j if complex_case else 0.5, 1 / 3]
        nu_r = inclusion.conj().T @ nu_s
        moving_nu_s = nu_s.copy()
        moving_nu_s[-1] += 1 / n
        moving_nu_r = inclusion.conj().T @ moving_nu_s
        tangent = np.zeros(target_dim, dtype=dtype)
        tangent[1] = 1
        tangent[0] = -np.conj(nu_s[1])
        spike = tangent / n**2
        spike[-1] += 1
        feature_s = np.vstack((
            moving_nu_s.conj()[None, :],
            n * spike.conj()[None, :],
            np.eye(target_dim, dtype=dtype) / n,
        ))
        feature_r = feature_s @ inclusion
        t_s, v_s = positive_root_and_column_polar(feature_s)
        t_r, v_r = positive_root_and_column_polar(feature_r)
        w = v_s.conj().T @ v_r
        f_r = np.zeros(source_dim, dtype=dtype)
        f_r[0] = 1
        f_s = inclusion @ f_r
        e_r, e_s = nu_r / np.linalg.norm(nu_r), nu_s / np.linalg.norm(nu_s)
        x_r, x_s = t_r @ f_r, t_s @ f_s
        suffix = f"{'complex' if complex_case else 'real'}_n{n}"
        check("exact_feature_pullback_" + suffix,
              opnorm(feature_r - feature_s @ inclusion) < 1e-12)
        check("full_transport_isometry_" + suffix,
              opnorm(w.conj().T @ w - np.eye(source_dim)) < 1e-9)
        check("exact_scaled_anchor_intertwining_" + suffix,
              np.linalg.norm(w @ x_r - x_s) < 1e-9)
        anchor_error = float(np.linalg.norm(x_r - e_r) + np.linalg.norm(x_s - e_s))
        normal_error = float(np.linalg.norm(w @ e_r - e_s))
        check("isometry_transfer_bound_" + suffix,
              normal_error <= anchor_error + 1e-9)

        explicit_error = 0.0
        root_lower_mins = []
        for label, feature, root, f, nu, moving_nu, e in (
            ("R", feature_r, t_r, f_r, nu_r, moving_nu_r, e_r),
            ("S", feature_s, t_s, f_s, nu_s, moving_nu_s, e_s),
        ):
            rho = float(np.linalg.norm(nu))
            rank_one_root = np.outer(moving_nu, moving_nu.conj()) / np.linalg.norm(moving_nu)
            difference = root - rank_one_root
            minimum = float(np.linalg.eigvalsh((difference + difference.conj().T) / 2)[0])
            root_lower_mins.append(minimum)
            check("global_root_order_" + label + "_" + suffix, minimum >= -1e-9)
            g = nu / rho**2
            tangent_test = f - g
            energy_g = float(np.linalg.norm(feature @ g)**2)
            energy_t = float(np.linalg.norm(feature @ tangent_test)**2)
            alpha_g = np.vdot(moving_nu, g)
            z = energy_g + 1 - 2 * rho * abs(alpha_g)**2 / np.linalg.norm(moving_nu)
            check("finite_source_distance_bound_" + label + "_" + suffix,
                  float(np.linalg.norm(root @ g - e)**2) <= z + 1e-9)
            explicit_error += np.sqrt(energy_t) + np.sqrt(max(0.0, float(z)))
            lhs = float(np.linalg.norm(feature @ tangent_test)**2)
            rhs = (float(np.linalg.norm(feature @ (g + tangent_test))**2)
                   + float(np.linalg.norm(feature @ (g - tangent_test))**2)) / 2 - energy_g
            check("m0_parallelogram_reduction_" + label + "_" + suffix,
                  abs(lhs - rhs) < 1e-10)
        check("four_fixed_source_bound_" + suffix,
              normal_error <= explicit_error + 1e-9)
        normal_remainder = w @ e_r - e_s * np.vdot(e_s, w @ e_r)
        check("full_tangential_remainder_bound_" + suffix,
              np.linalg.norm(normal_remainder) <= normal_error + 1e-10)
        records.append({
            "case": suffix,
            "normal_error": normal_error,
            "anchor_error_bound": anchor_error,
            "fixed_source_error_bound": float(explicit_error),
            "root_order_min_eigenvalues": root_lower_mins,
            "target_scaled_gram_norm": opnorm(feature_s)**2,
        })

# Exact two-coordinate slices of the infinite escaping counterfamily.
counter_records = []
for n in (4, 16, 64):
    t = np.array([[1 / n, 1], [1, n]], dtype=float) + np.eye(2) / n**2
    m = t @ t
    normal_projector = np.diag([1.0, 0.0])
    check(f"escaping_counterfamily_positive_n{n}", np.linalg.eigvalsh(t)[0] > 0)
    check(f"escaping_counterfamily_missing_lower_order_n{n}",
          np.linalg.eigvalsh(m - normal_projector)[0] < 0)
    check(f"escaping_counterfamily_exact_column_n{n}",
          np.allclose(t[:, 0], [1 / n + 1 / n**2, 1], rtol=0, atol=1e-14))
    counter_records.append({
        "n": n, "fixed_normal_energy": float(m[0, 0]),
        "normal_root_coefficient": float(t[0, 0]),
        "escaped_root_coefficient": float(t[1, 0]),
    })

source_paths = [
    "papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex",
    "papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex",
    "papers/P11_sections/P11_Direct_Terminal_Bridge.tex",
    "papers/P11_sections/P11_O3o_TC1_NearNull_Remainder_Collapse.tex",
    "papers/P11_sections/P11_O3p_Vanishing_NearNull_Core.tex",
    "audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md",
    "audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md",
]
source_blobs = {}
for path in source_paths:
    blob = subprocess.check_output(
        ["git", "-C", str(ROOT), "rev-parse", f"{BASE}:{path}"], text=True
    ).strip()
    current = subprocess.check_output(
        ["git", "-C", str(ROOT), "hash-object", path], text=True
    ).strip()
    if path in REPAIRED:
        check("reviewed_source_repair_exact_blob_" + path, REPAIRED[path] == current)
    else:
        check("canonical_source_unchanged_" + path, blob == current)
    source_blobs[path] = blob

print(json.dumps({
    "status": "PASS_ALGEBRAIC_REGRESSION_NOT_P11_CERTIFICATE",
    "checks_passed": len(CHECKS),
    "base_commit": BASE,
    "scope": "Finite algebraic identities and counterfamily only; no numerical infinite-horizon or P11 proof.",
    "source_blobs": source_blobs,
    "repaired_source_blobs": REPAIRED,
    "anchor_models": records,
    "escaping_counterfamily": counter_records,
    "checks": CHECKS,
}, ensure_ascii=False, indent=2))
