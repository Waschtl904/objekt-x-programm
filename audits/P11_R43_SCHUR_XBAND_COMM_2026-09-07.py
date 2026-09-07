#!/usr/bin/env python3
"""R43-SCHUR-XBAND-COMM: finite matrix/proxy diagnostic, NOT canonical x_rev.

Parent: PR #84, 3e4e5a73679db9f88624869587c4bd3bc3fec266.
Requires NumPy and SciPy; both unchanged parent scripts must be alongside this file.
Run: OPENBLAS_NUM_THREADS=1 python <this-file> --output results.json
Optional --parents also reruns the full original #83/#84 assertion suites.

The exact center-shift experiment is #83's finite graph. The additional #84
prime-resolved band-mean experiment explicitly retains its averaging remainder;
finite-width band means are NOT identified with point evaluations at centers.
No canonical source, analytic Q, reverse-normal decay, Strong Terminal/C6,
Object X, or RH is computed or certified. Floating-point assertions are not
interval certificates or independent review. No theorem-registry promotion.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import platform
from itertools import combinations
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigh, solve_sylvester

HERE = Path(__file__).resolve().parent
PARENTS = {
    "p83": ("P11_R43_SCHUR_CORR_STRUCTURED_HUB_PROXY_2026-09-06.py",
            "237bf3406debcc3d2ec757ce547d3759c55a1fc2"),
    "p84": ("P11_R43_SCHUR_VAR_DELTA_SWEEP_2026-09-06.py",
            "bb0ccb9e788bb0949ab1ea01b80ad6f6ce5fef4d"),
}
ERRORS: dict[str, float] = {}
TOL = 5e-11  # Every asserted normalized identity is strictly below 1e-10.


def load_parent(name):
    filename, expected = PARENTS[name]
    path = HERE / filename
    data = path.read_bytes()
    actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if actual != expected:
        raise RuntimeError(f"Parent blob mismatch: {filename}: {actual}")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sym(a):
    return (a + a.T) / 2


def norm(a):
    return float(np.linalg.norm(a))


def check(name, a, b):
    a, b = np.asarray(a), np.asarray(b)
    error = norm(a - b) / max(norm(a), norm(b), 1e-300)
    ERRORS[name] = error
    if not error < TOL:
        raise AssertionError((name, error))
    return error


def zero(name, a):
    error = norm(a)
    ERRORS[name] = error
    if not error < TOL:
        raise AssertionError((name, error))


def power(a, exponent):
    check("power_symmetry", a, a.T)
    d, v = np.linalg.eigh(sym(a))
    if d[0] <= 0:
        raise ArithmeticError(f"Non-SPD matrix: lambda_min={d[0]}")
    return sym((v * d**exponent) @ v.T)


def shift(nodes, h):
    """T_h x(u) = x(u-h), zero outside the indicated finite grid."""
    return (nodes[None, :] == nodes[:, None] - h).astype(float)


def spectrum(a):
    e = np.linalg.eigvalsh(sym(a))
    return [float(e[0]), float(e[-1]), float(e[-1] / e[0])]


def dot(a, b):
    return float(np.vdot(a, b).real)


def run(rerun_parents=False):
    ERRORS.clear()
    p83, p84 = load_parent("p83"), load_parent("p84")
    if rerun_parents:
        p83.main()
        p84.main()
    bands = p83.band_data()
    weights = np.array([r[2] for r in bands])
    amps = [r[3] for r in bands]
    centers = p83.CENTERS
    U, V = p83.U, p83.V
    nodes, big = np.arange(-U, U + 1), np.arange(-V, V + 1)
    n, nb = len(nodes), len(big)
    I = np.eye(n)
    E = (big[:, None] == nodes[None, :]).astype(float)
    PN = np.eye(nb) - E @ E.T
    new = np.flatnonzero(np.abs(big) > U)
    AU = np.array(p83.build_resolvent_matrix(U, weights)[1])
    AV = np.array(p83.build_resolvent_matrix(V, weights)[1])
    BU, BV = sym(np.linalg.solve(AU, I)), sym(np.linalg.solve(AV, np.eye(nb)))
    BT = sym(E.T @ BV @ E)
    AO, ON, NN = E.T @ AV @ E, E.T @ AV[:, new], AV[np.ix_(new, new)]
    F = sym(AO - ON @ np.linalg.solve(NN, ON.T))
    check("compressed_inverse_Schur", BT @ F, I)
    zero("strip_strip_offdiagonal", NN - np.diag(np.diag(NN)))
    rows, stars = [], []
    K, VAR, MEAN = np.zeros_like(AU), np.zeros_like(AU), np.zeros_like(AU)
    for z in big[new]:
        sign = int(np.sign(z))
        active = [(i, int(z - sign * t)) for i, t in enumerate(centers)
                  if -U <= z - sign * t <= U]
        W = sum(weights[i] for i, _ in active)  # ALL active channels, never a pair sum.
        g, diag = np.zeros(n), np.zeros(n)
        for i, pos in active:
            g[pos + U] += weights[i]
            diag[pos + U] += weights[i]
        K += np.diag(diag) - np.outer(g, g) / (1 + W)
        VAR += np.diag(diag) - np.outer(g, g) / W
        MEAN += np.outer(g, g) / (W * (1 + W))
        stars.append((int(z), active, W))
        for (i, pos), (j, target) in combinations(active, 2):
            h = sign * (centers[j] - centers[i])
            rows.append((int(z), i, j, pos + U, target + U, h,
                         float(weights[i] * weights[j] / W)))
    check("K_Schur_equals_stars", F - AU, K)
    check("K_variance_plus_mean", K, VAR + MEAN)
    incidence = np.zeros((len(rows), n))
    for k, (_, i, j, pos, target, h, w) in enumerate(rows):
        incidence[k, target], incidence[k, pos] = np.sqrt(w), -np.sqrt(w)
    check("pair_Gram_ANOVA", incidence.T @ incidence, VAR)
    rng = np.random.default_rng(20260907)
    test_x = rng.normal(size=n)
    correct = norm(incidence @ test_x)**2
    wrong = sum(weights[i] * weights[j] / (weights[i] + weights[j])
                * (test_x[t] - test_x[p])**2 for _, i, j, p, t, _, _ in rows)
    assert abs(wrong / correct - 1) > .1  # Reject the pair-only denominator.

    Ah, Ai = power(AU, .5), power(AU, -.5)
    Kbar = sym(Ai @ K @ Ai)
    H = power(I + Kbar, -.5)
    Q = sym(Ai @ H @ Ai)
    Bh, Bi = power(BU, .5), power(BU, -.5)
    Qgeneric = sym(Bh @ power(Bi @ BT @ Bi, .5) @ Bh)
    check("Q_two_constructions", Q, Qgeneric)
    riccati = check("Q_Riccati", Q @ AU @ Q, BT)
    check("H_whitening", Ah @ Q @ Ah, H)
    check("Q_inverse_Riccati", Q @ F @ Q, BU)
    assert np.linalg.eigvalsh(Kbar)[0] > -TOL
    J = np.fliplr(I)
    for name, B in (("BU", BU), ("BT", BT), ("Q", Q)):
        check(f"reflection_{name}", J @ B, B @ J)
    # Center shifts are all even: two lattice components, not an arithmetic theorem.
    for parity in (0, 1):
        c = (nodes % 2 == parity).astype(float)
        check(f"lattice_component_{parity}", AU @ c, c)

    # Exact finite shift-compression counterexamples, including smooth boundary data.
    padded = np.arange(-U - 20, U + 21)
    Ep = (padded[:, None] == nodes[None, :]).astype(float)
    lost = np.eye(len(padded)) - Ep @ Ep.T
    for h, k in ((2, 4), (-2, -4), (-2, 2), (4, -2)):
        lhs = shift(nodes, h) @ shift(nodes, k) - shift(nodes, h + k)
        rhs = -Ep.T @ shift(padded, h) @ lost @ shift(padded, k) @ Ep
        assert np.array_equal(lhs, rhs)
        if h * k > 0:
            assert not np.any(lhs)
    defect = shift(nodes, -2) @ shift(nodes, 2) - I
    expected = np.zeros_like(I)
    expected[-2, -2] = expected[-1, -1] = -1
    assert np.array_equal(defect, expected)
    impulse = I[:, -1]
    bump = np.array([np.exp(-1 / (1 - ((u - 29.5) / 3)**2))
                     if abs(u - 29.5) < 3 else 0 for u in nodes])
    controls = {"right_impulse_loss": norm(defect @ impulse),
                "smooth_boundary_loss_fraction": norm(defect @ bump) / norm(bump),
                "same_sign_defect_operator_norm": 0.0}
    assert controls["right_impulse_loss"] == 1
    assert controls["smooth_boundary_loss_fraction"] > 0

    # Infinite-graph compression and the lost-degree diagonal.
    L0 = 2 * sum(weights) * I
    for t, w in zip(centers, weights):
        L0 -= w * (shift(nodes, t) + shift(nodes, -t))
    Dlost = np.diag(np.diag(L0 - (AU - I)))
    check("graph_lost_degree", AU, I + L0 - Dlost)
    matrix_tests, transfer = [], []
    hmin = np.linalg.eigvalsh(H)[0]
    sylvester_inverse = float(1 / (2 * hmin))
    check("Sylvester_inverse_Schur_formula", sylvester_inverse,
          .5 * np.sqrt(1 + np.linalg.eigvalsh(Kbar)[-1]))
    for h in (2, 4, 10, 12, 14):
        T, TV = shift(nodes, h), shift(big, h)
        AB = AU @ T - T @ AU
        check(f"boundary_split_{h}", AB,
              (L0 @ T - T @ L0) - (Dlost @ T - T @ Dlost))
        mask = U - np.abs(nodes) < max(centers) + h
        zero(f"boundary_rows_{h}", AB[~mask, :])
        zero(f"boundary_cols_{h}", AB[:, ~mask])
        for term_name, term in (("infinite_compression", L0 @ T - T @ L0),
                                ("lost_degree", Dlost @ T - T @ Dlost)):
            zero(f"{term_name}_rows_{h}", term[~mask, :])
            zero(f"{term_name}_cols_{h}", term[:, ~mask])
        e1 = check(f"BU_comm_{h}", T @ BU - BU @ T, BU @ AB @ BU)
        AF = F @ T - T @ F
        zero(f"Schur_boundary_rows_{h}", AF[~mask, :])
        zero(f"Schur_boundary_cols_{h}", AF[:, ~mask])
        e2 = check(f"BT_comm_Schur_{h}", T @ BT - BT @ T, BT @ AF @ BT)
        compressed = (E.T @ (TV @ BV - BV @ TV) @ E
                      - E.T @ TV @ PN @ BV @ E + E.T @ BV @ PN @ TV @ E)
        e3 = check(f"BT_comm_excursions_{h}", T @ BT - BT @ T, compressed)
        Dq = T @ Q - Q @ T
        forcing = (T @ BT - BT @ T) - Q @ (T @ AU - AU @ T) @ Q
        e4 = check(f"Q_Sylvester_{h}", Q @ AU @ Dq + Dq @ AU @ Q, forcing)
        d_hat, f_hat = Ah @ Dq @ Ah, Ah @ forcing @ Ah
        e5 = check(f"Q_Sylvester_solve_{h}", solve_sylvester(H, H, f_hat), d_hat)
        assert norm(d_hat) <= sylvester_inverse * norm(f_hat) * (1 + TOL)
        matrix_tests.append([h, e1, e2, e3, e4, e5])
        if h in (2, 4):
            relevant = [r for r in rows if r[5] == h]
            R = np.zeros((len(relevant), n))
            for k, r in enumerate(relevant):
                R[k, r[3]] = np.sqrt(r[6])
            for name, B in (("BU", BU), ("BT", BT)):
                beta = float(np.linalg.norm(R @ B[:, mask], 2))
                lower = max(np.sqrt(r[6]) / (1 + 2 * sum(weights)) for r in relevant
                            if mask[r[3]])
                assert beta >= lower
                transfer.append([h, name, beta, float(lower),
                                 int(sum(mask[r[3]] for r in relevant))])

    # Weighted source-specific decompositions. Each denominator is G=(Bv)^* AU Bv.
    transports = (("BU", BU), ("BT", BT), ("Q", Q))
    cases, pair_rows, large_controls, globals_, boundary_sources = [], [], [], [], []
    for radius in (4, 6, 8):
        v = np.array(list(p83.raw_hub_values(radius, amps).values()))
        zero(f"bulk_compression_{radius}", defect @ v)
        for name, B in transports:
            x = B @ v
            G = dot(x, AU @ x)
            cache = {}
            for h in (-14, -12, -10, -4, -2, 2, 4, 10, 12, 14):
                T = shift(nodes, h)
                a = B @ ((T - I) @ v)
                c = (T @ B - B @ T) @ v
                d = (T - I) @ x
                check(f"vector_{radius}_{name}_{h}", d, a + c)
                check(f"global_square_{radius}_{name}_{h}", dot(d, d),
                      dot(a, a) + dot(c, c) + 2 * dot(a, c))
                cache[h] = (a, c, d)
                if h > 0:
                    globals_.append([radius, name, h, dot(a, a) / G, dot(c, c) / G,
                                     2 * dot(a, c) / G, dot(d, d) / G])

            def measure(selected, control_h=None):
                aa, cc, xx = [], [], []
                for z, i, j, pos, target, h, w in selected:
                    if control_h is not None:
                        h = int(np.sign(h)) * control_h
                    a, c, d = cache[h]
                    s = np.sqrt(w / G)
                    aa.append(s * a[pos]); cc.append(s * c[pos]); xx.append(s * d[pos])
                    if control_h is None:
                        check(f"orientation_{radius}_{name}_{z}_{i}_{j}",
                              d[pos], x[target] - x[pos])
                aa, cc, xx = np.array(aa), np.array(cc), np.array(xx)
                values = [dot(aa, aa), dot(cc, cc), 2 * dot(aa, cc), dot(xx, xx)]
                check(f"relative_square_{radius}_{name}_{len(selected)}_{control_h}",
                      values[3], sum(values[:3]))
                return values

            if name in ("BU", "BT"):
                Fused = AU if name == "BU" else F
                for h in (2, 4):
                    T = shift(nodes, h)
                    mask = U - np.abs(nodes) < max(centers) + h
                    force = (Fused @ T - T @ Fused) @ x
                    zero(f"source_boundary_support_{radius}_{name}_{h}", force[~mask])
                    selected = [r for r in rows if r[5] == h]
                    R = np.zeros((len(selected), n))
                    for k, r in enumerate(selected):
                        R[k, r[3]] = np.sqrt(r[6])
                    observed = norm(R @ B @ force) / np.sqrt(G)
                    check(f"boundary_source_identity_{radius}_{name}_{h}",
                          R @ B @ force, R @ cache[h][1])
                    beta = float(np.linalg.norm(R @ B[:, mask], 2))
                    majorant = beta * norm(force) / np.sqrt(G)
                    assert observed <= majorant * (1 + TOL)
                    boundary_sources.append([radius, name, h, norm(force)/np.sqrt(G),
                                             observed, majorant])
            total = measure(rows)
            check(f"ANOVA_source_{radius}_{name}", total[3],
                  p83.star_split(dict(zip(nodes, x)), weights)[0] / G)
            epsilon = float(np.sqrt(total[1] / total[0]))
            assert epsilon < 1
            assert total[3] >= (1 - epsilon)**2 * total[0] * (1 - TOL)
            cases.append([radius, name, G, *total, epsilon, total[3] / total[0]])
            for i, j in combinations(range(3), 2):
                selected = [r for r in rows if (r[1], r[2]) == (i, j)]
                pair_rows.append([radius, name, centers[i], centers[j], *measure(selected)])
            for h in (10, 12, 14):
                large_controls.append([radius, name, h, *measure(rows, h)])

    # All discrete odd source directions, not just the three smooth bumps.
    # Generalized eigenvalues are numerical diagnostics, not interval certificates.
    subspace = []
    Hfull = -sum(amp * (shift(nodes, t//2) - shift(nodes, -t//2))
                 for t, amp in zip(centers, amps))
    for radius in (4, 6, 8):
        hub = np.zeros((n, radius - 1))
        for j, k in enumerate(range(1, radius)):
            def f(u):
                return float(u == k) - float(u == -k)
            for row, u in enumerate(nodes):
                hub[row, j] = -sum(amp * (f(u - t//2) - f(u + t//2))
                                  for t, amp in zip(centers, amps))
        source_basis = np.array([[float(u == k) - float(u == -k)
                                  for k in range(1, radius)] for u in nodes])
        check(f"hub_basis_{radius}", hub, Hfull @ source_basis)
        for h in (-4, -2, 2, 4):
            T = shift(nodes, h)
            zero(f"bulk_hub_commutation_{radius}_{h}",
                 (T @ Hfull - Hfull @ T) @ source_basis)
        for name, B in transports:
            RA, RC = [], []
            for z, i, j, pos, target, h, w in rows:
                T = shift(nodes, h)
                RA.append(np.sqrt(w) * (B @ (T - I) @ hub)[pos])
                RC.append(np.sqrt(w) * ((T @ B - B @ T) @ hub)[pos])
            RA, RC = np.array(RA), np.array(RC)
            RD = incidence @ B @ hub
            check(f"subspace_amplitude_{radius}_{name}", RD, RA + RC)
            GA, GC, GD = sym(RA.T @ RA), sym(RC.T @ RC), sym(RD.T @ RD)
            GG = sym(hub.T @ B @ AU @ B @ hub)
            assert np.linalg.eigvalsh(GA)[0] > 0
            ec, vc = eigh(GC, GA)
            ed, vd = eigh(GD, GA)
            eg, vg = eigh(GD, GG)
            check(f"subspace_eigen_C_{radius}_{name}", GC @ vc, (GA @ vc) * ec)
            check(f"subspace_eigen_D_{radius}_{name}", GD @ vd, (GA @ vd) * ed)
            check(f"subspace_eigen_G_{radius}_{name}", GD @ vg, (GG @ vg) * eg)
            assert np.sqrt(ec[-1]) < .22
            if name == "Q":
                assert np.sqrt(ec[-1]) < .12
                assert ed[0] > .82
            subspace.append([radius, name, radius-1, float(np.sqrt(ec[-1])),
                             float(ed[0]), float(ed[-1]), float(eg[0]), float(eg[-1]),
                             float(np.linalg.cond(GA))])

    # Prime-resolved ANOVA and explicit band-mean/center-shift bridge (#84 hybrid).
    offgrid = []
    for delta in (.15, .005):
        pbands, gs, hs = p84.normalized_band_data(delta)
        geometry = []
        for z, active, Wcenter in stars:
            groups = []
            for i, band in enumerate(pbands):
                lp = np.log(np.array(band, dtype=float))
                w = np.array([p84.prime_graph_weight(p) * gs[i] for p in band])
                positions = z - np.sign(z) * lp
                ok = (positions >= -U) & (positions <= U)
                positions, w = positions[ok], w[ok]
                lo = np.floor(positions).astype(int)
                alpha = positions - lo
                hi = np.minimum(lo + 1, U)
                assert len(w) > 0
                groups.append((lo + U, hi + U, alpha, w))
            geometry.append((z, groups))
        for radius in (4, 6, 8):
            v = np.array(list(p84.raw_hub_values(radius, pbands, hs).values()))
            for name, B in transports:
                x = B @ v
                G = dot(x, AU @ x)
                intra = inter = allvar = pair = center = rem = cross = 0.0
                for z, groups in geometry:
                    wgroup, means, rawitems = [], [], []
                    for lo, hi, alpha, w in groups:
                        values = (1 - alpha) * x[lo] + alpha * x[hi]
                        Wj = float(sum(w))
                        mu = dot(w, values) / Wj
                        wgroup.append(Wj); means.append(mu); rawitems.append((w, values))
                        intra += dot(w, (values - mu)**2)
                    W = sum(wgroup)
                    mu = dot(wgroup, means) / W
                    inter += dot(wgroup, (np.array(means) - mu)**2)
                    allvar += sum(dot(w, (values - mu)**2) for w, values in rawitems)
                    for i, j in combinations(range(3), 2):
                        rho = wgroup[i] * wgroup[j] / W
                        p = int(z - np.sign(z) * centers[i]) + U
                        t = int(z - np.sign(z) * centers[j]) + U
                        d = x[t] - x[p]
                        e = means[j] - means[i] - d
                        pair += rho * (means[j] - means[i])**2
                        center += rho * d*d
                        rem += rho * e*e
                        cross += 2 * rho * d*e
                check(f"offgrid_ANOVA_{delta}_{radius}_{name}", allvar, intra + inter)
                check(f"offgrid_pair_{delta}_{radius}_{name}", inter, pair)
                check(f"offgrid_bridge_{delta}_{radius}_{name}", inter, center + rem + cross)
                reference = p84.variance_decomposition(dict(zip(nodes, x)), pbands, gs)
                check(f"offgrid_parent_{delta}_{radius}_{name}", [intra, inter, allvar], reference)
                offgrid.append([delta, radius, name, intra/G, inter/G,
                                center/G, rem/G, cross/G])

    # Exact logical negative control: B=I commutes but arbitrary data can have variance.
    # This is NOT a counterexample within the restricted compact-hub source family.
    e = I[:, 17 + U]
    assert np.array_equal(shift(nodes, 2) @ I - I @ shift(nodes, 2), np.zeros_like(I))
    arbitrary_source_variance = norm(incidence @ e)**2
    assert arbitrary_source_variance > 0
    result = {
        "scope": "finite proxy only; not canonical x_rev; no independent certification",
        "parent_head": "3e4e5a73679db9f88624869587c4bd3bc3fec266",
        "parent_blobs": {k: v[1] for k, v in PARENTS.items()},
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "scipy": scipy.__version__},
        "weights": weights.tolist(), "hub_amplitudes": amps,
        "spectra_min_max_condition": {name: spectrum(a) for name, a in
                                      (("AU", AU), ("BU", BU), ("BT", BT), ("Q", Q), ("H", H))},
        "Kbar_lambda_max": float(np.linalg.eigvalsh(Kbar)[-1]),
        "Q_Riccati_relative_residual": riccati,
        "Sylvester_inverse_Frobenius_energy": sylvester_inverse,
        "Sylvester_unweighted_upper_bound": sylvester_inverse * spectrum(AU)[2],
        "compression_controls": controls,
        "wrong_pair_denominator_ratio": wrong/correct,
        "boundary_transfer_columns": ["h", "B", "operator_norm", "uniform_positive_lower_bound", "overlap_rows"],
        "boundary_transfer": transfer,
        "matrix_test_columns": ["h", "BU_identity", "BT_Schur", "BT_excursions", "Q_Sylvester", "Q_solved"],
        "matrix_tests": matrix_tests,
        "boundary_source_columns": ["X", "B", "h", "force_norm/sqrtG", "observed_comm/sqrtG", "operator_majorant/sqrtG"],
        "boundary_sources": boundary_sources,
        "odd_source_subspace_columns": ["X", "B", "dimension", "epsilon_sup", "variance/A2_min", "variance/A2_max", "variance/G_min", "variance/G_max", "condition_GA"],
        "odd_source_subspace_NUMERICAL_NOT_INTERVAL_CERTIFIED": subspace,
        "case_columns": ["X", "B", "G", "A2/G", "C2/G", "2AC/G", "variance/G", "epsilon", "variance/A2"],
        "cases": cases,
        "pair_columns": ["X", "B", "ti", "tj", "A2/G", "C2/G", "2AC/G", "pair_variance/G"],
        "pairs": pair_rows,
        "control_columns": ["X", "B", "h", "A2/G", "C2/G", "2AC/G", "difference2/G"],
        "large_shift_same_sampler_NOT_ANOVA": large_controls,
        "global_L2_by_G_NOT_relative_geometry": globals_,
        "offgrid_columns": ["delta", "X", "B", "intra/G", "inter/G", "center_difference/G", "averaging_remainder/G", "2center_remainder/G"],
        "offgrid_bridge": offgrid,
        "arbitrary_source_identity_transport_variance": arbitrary_source_variance,
        "checked_identity_count": len(ERRORS),
        "max_recorded_error": max(ERRORS.values()),
        "worst_error_label": max(ERRORS, key=ERRORS.get),
        "assertion_tolerance": TOL,
        "status": "PASS_PROXY_NOT_THEOREM",
    }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parents", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.parents)
    text = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(f"PASS: {result['checked_identity_count']} recorded identities; "
              f"max error={result['max_recorded_error']:.3e}")
        print("X B  A2/G  C2/G  interference/G  variance/G  epsilon  variance/A2")
        for row in result["cases"]:
            print(row[0], row[1], *(f"{x:.12g}" for x in row[3:]))
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
