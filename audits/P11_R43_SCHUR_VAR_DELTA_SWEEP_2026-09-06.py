#!/usr/bin/env python3
"""
P11 / R43 — SCHUR-VAR fixed-mass delta-sweep diagnostic.

DIAGNOSTIC / PROXY SCOPE ONLY.

PR #83 showed that, in a structured odd-source -> even-hub -> resolvent proxy,
the primitive Schur-star weighted variance dominates the coherent mean.  This
sixth diagnostic asks whether that variance is merely a small-bandwidth
regularity effect or whether a robust cross-channel component remains.

A naive sweep of PR #83's HALF_WIDTH is confounded because (i) #83 aggregates
every prime band to one center shift, so the true within-band log(q/p)
difference set is absent, and (ii) shrinking the band also shrinks its total
prime mass.  We therefore use a fixed-mass, prime-resolved microgeometry:

  U=30, V=40; centers log p=10,12,14; baseline delta_0=0.15;
  source radii X in {4,6,8}.

For every smaller delta, individual graph weights and hub amplitudes inside
one band are renormalized to the corresponding delta_0 total mass.  Delta thus
changes the spread of log-primes around the fixed band center, not the total
channel strength.

Prime-resolved pieces:
- raw k=1 hub uses individual half-shifts (1/2)log p;
- Schur-star sampling uses individual old preimages z +/- log p, with linear
  interpolation on the integer old grid;
- weighted variance is decomposed exactly by the law of total variance:

      V_total = V_intra + V_inter,

  where V_intra is variance inside each fixed log-prime band and V_inter is
  variance of the three band means.

Firewall: finite resolvent matrices remain the frozen PR #83 band-center
Galerkin operators with BASELINE aggregate graph weights.  Thus this is a
hybrid off-grid diagnostic, not the full P11 residual operator.

This script does NOT compute G_{R,cond}^{-1/2}epsilon_R, the geometric mean Q,
or canonical x_rev, and proves no reverse-normal decay, FD23-UNIF,
FLAGDYN/TIGHT, Strong Terminal/C6, Object X, or RH.
"""

from math import ceil, exp, floor, log, sqrt

U = 30
V = 40
CENTERS = (10, 12, 14)
BASE_DELTA = 0.15
DELTAS = (0.15, 0.10, 0.075, 0.05, 0.03, 0.02, 0.01, 0.005)
SOURCE_RADII = (4, 6, 8)


def sieve(n: int):
    mark = bytearray(b"\x01") * (n + 1)
    mark[0:2] = b"\x00\x00"
    p = 2
    while p * p <= n:
        if mark[p]:
            start = p * p
            mark[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return [k for k in range(2, n + 1) if mark[k]]


MAX_P = int(exp(max(CENTERS) + BASE_DELTA)) + 16
PRIMES = sieve(MAX_P)


def prime_graph_weight(p: int) -> float:
    return log(p) * (p - 1) * p ** (-1.5)


def prime_hub_amplitude(p: int) -> float:
    return sqrt(log(p)) * p ** (-0.75)


def primes_in_band(center: float, delta: float):
    return [p for p in PRIMES if center - delta <= log(p) <= center + delta]


def band_family(delta: float):
    return [primes_in_band(t, delta) for t in CENTERS]


BASE_BANDS = band_family(BASE_DELTA)
BASE_GRAPH_MASS = [
    sum(prime_graph_weight(p) for p in band) for band in BASE_BANDS
]
BASE_HUB_MASS = [
    sum(prime_hub_amplitude(p) for p in band) for band in BASE_BANDS
]


def normalized_band_data(delta: float):
    bands = band_family(delta)
    for band in bands:
        assert band

    graph_mass = [sum(prime_graph_weight(p) for p in band) for band in bands]
    hub_mass = [sum(prime_hub_amplitude(p) for p in band) for band in bands]

    graph_scales = [
        base / current for base, current in zip(BASE_GRAPH_MASS, graph_mass)
    ]
    hub_scales = [
        base / current for base, current in zip(BASE_HUB_MASS, hub_mass)
    ]

    for j, band in enumerate(bands):
        graph_check = sum(
            graph_scales[j] * prime_graph_weight(p) for p in band
        )
        hub_check = sum(
            hub_scales[j] * prime_hub_amplitude(p) for p in band
        )
        assert abs(graph_check - BASE_GRAPH_MASS[j]) < 1e-9
        assert abs(hub_check - BASE_HUB_MASS[j]) < 1e-10

    return bands, graph_scales, hub_scales


def odd_bump(t: float, radius: float) -> float:
    if abs(t) >= radius:
        return 0.0
    r = t / radius
    return t * exp(-1.0 / (1.0 - r * r))


def raw_hub_values(radius, bands, hub_scales):
    prime_rows = []
    for band, scale in zip(bands, hub_scales):
        prime_rows.append([
            (0.5 * log(p), scale * prime_hub_amplitude(p)) for p in band
        ])

    vals = {}
    for u in range(-U, U + 1):
        total = 0.0
        for rows in prime_rows:
            for half_shift, amp in rows:
                total += amp * (
                    odd_bump(u - half_shift, radius)
                    - odd_bump(u + half_shift, radius)
                )
        vals[u] = -total
    return vals


def build_resolvent_matrix(T):
    nodes = list(range(-T, T + 1))
    idx = {z: i for i, z in enumerate(nodes)}
    n = len(nodes)
    A = [[0.0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = 1.0

    for shift, weight in zip(CENTERS, BASE_GRAPH_MASS):
        for a in range(-T + shift, T + 1):
            b = a - shift
            ia, ib = idx[a], idx[b]
            A[ia][ia] += weight
            A[ib][ib] += weight
            A[ia][ib] -= weight
            A[ib][ia] -= weight
    return nodes, A


def cholesky(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                value = A[i][i] - s
                assert value > 0.0
                L[i][j] = sqrt(value)
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    return L


def chol_solve(L, b):
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        y[i] = (b[i] - sum(L[i][k] * y[k] for k in range(i))) / L[i][i]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (
            y[i] - sum(L[k][i] * x[k] for k in range(i + 1, n))
        ) / L[i][i]
    return x


NODES_U, A_U = build_resolvent_matrix(U)
NODES_V, A_V = build_resolvent_matrix(V)
CHOL_U = cholesky(A_U)
CHOL_V = cholesky(A_V)


def apply_B_U(vals):
    rhs = [vals[z] for z in NODES_U]
    sol = chol_solve(CHOL_U, rhs)
    return {z: sol[i] for i, z in enumerate(NODES_U)}


def apply_compressed_B_V(vals):
    idx_v = {z: i for i, z in enumerate(NODES_V)}
    rhs = [vals.get(z, 0.0) for z in NODES_V]
    sol = chol_solve(CHOL_V, rhs)
    return {z: sol[idx_v[z]] for z in range(-U, U + 1)}


def parity_error(vals):
    return max(abs(vals[u] - vals[-u]) for u in range(0, U + 1))


def interpolate(vals, t: float):
    assert -U <= t <= U
    lo = floor(t)
    hi = ceil(t)
    if lo == hi:
        return vals[int(lo)]
    alpha = t - lo
    return (1.0 - alpha) * vals[lo] + alpha * vals[hi]


def old_graph_norm(vals):
    l2 = sum(vals[z] ** 2 for z in range(-U, U + 1))
    residual = 0.0
    for shift, weight in zip(CENTERS, BASE_GRAPH_MASS):
        for a in range(-U + shift, U + 1):
            b = a - shift
            residual += weight * (vals[a] - vals[b]) ** 2
    return l2 + residual


def variance_decomposition(vals, bands, graph_scales):
    intra_total = 0.0
    inter_total = 0.0
    total_total = 0.0
    new_nodes = list(range(-V, -U)) + list(range(U + 1, V + 1))

    for z in new_nodes:
        grouped = []
        all_items = []

        for band, scale in zip(bands, graph_scales):
            items = []
            for p in band:
                lp = log(p)
                w = scale * prime_graph_weight(p)
                for old_t in (z - lp, z + lp):
                    if -U <= old_t <= U:
                        value = interpolate(vals, old_t)
                        items.append((w, value))
                        all_items.append((w, value))
            grouped.append(items)

        if not all_items:
            continue

        W = sum(w for w, _ in all_items)
        mu = sum(w * x for w, x in all_items) / W
        local_total = sum(w * (x - mu) ** 2 for w, x in all_items)

        local_intra = 0.0
        local_inter = 0.0
        for items in grouped:
            if not items:
                continue
            Wj = sum(w for w, _ in items)
            muj = sum(w * x for w, x in items) / Wj
            local_intra += sum(w * (x - muj) ** 2 for w, x in items)
            local_inter += Wj * (muj - mu) ** 2

        assert abs(local_total - local_intra - local_inter) <= (
            1e-10 * max(1.0, abs(local_total))
        )
        intra_total += local_intra
        inter_total += local_inter
        total_total += local_total

    assert abs(total_total - intra_total - inter_total) <= (
        1e-10 * max(1.0, abs(total_total))
    )
    return intra_total, inter_total, total_total


def loglog_slope(xs, ys):
    lx = [log(x) for x in xs]
    ly = [log(y) for y in ys]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    num = sum((x - mx) * (y - my) for x, y in zip(lx, ly))
    den = sum((x - mx) ** 2 for x in lx)
    return num / den


def run_one(radius, delta):
    bands, graph_scales, hub_scales = normalized_band_data(delta)
    raw = raw_hub_values(radius, bands, hub_scales)
    assert parity_error(raw) < 1e-10

    bu = apply_B_U(raw)
    bv = apply_compressed_B_V(raw)
    assert parity_error(bu) < 1e-9
    assert parity_error(bv) < 1e-9

    out = {}
    for name, vals in (("B_U H*", bu), ("B~_V H*", bv)):
        graph = old_graph_norm(vals)
        intra, inter, total = variance_decomposition(vals, bands, graph_scales)
        out[name] = {
            "intra": intra / graph,
            "inter": inter / graph,
            "total": total / graph,
        }
    return out


def main():
    print("R43-SCHUR-VAR fixed-mass delta sweep")
    print("DIAGNOSTIC ONLY — not actual x_rev")
    print(f"baseline graph masses = {BASE_GRAPH_MASS}")
    print(f"baseline hub masses   = {BASE_HUB_MASS}")
    print()

    all_results = {}
    for radius in SOURCE_RADII:
        print(f"source radius X={radius}")
        rows = {}
        for delta in DELTAS:
            result = run_one(radius, delta)
            rows[delta] = result
            print(
                f"  delta={delta:0.3f}  "
                f"BU[intra={result['B_U H*']['intra']:.12g}, "
                f"inter={result['B_U H*']['inter']:.12g}, "
                f"total={result['B_U H*']['total']:.12g}]  "
                f"BV[intra={result['B~_V H*']['intra']:.12g}, "
                f"inter={result['B~_V H*']['inter']:.12g}, "
                f"total={result['B~_V H*']['total']:.12g}]"
            )

        all_results[radius] = rows
        for name in ("B_U H*", "B~_V H*"):
            intra_vals = [rows[d][name]["intra"] for d in DELTAS]
            inter_vals = [rows[d][name]["inter"] for d in DELTAS]
            slope = loglog_slope(DELTAS, intra_vals)
            inter_spread = max(inter_vals) / min(inter_vals)
            print(
                f"  {name}: log-log intra slope={slope:.9f}, "
                f"inter max/min={inter_spread:.9f}"
            )
            assert 1.95 < slope < 2.05
            assert inter_spread < 1.05
            narrow = rows[DELTAS[-1]][name]
            assert narrow["intra"] < 1e-4 * narrow["inter"]
        print()

    assert abs(BASE_GRAPH_MASS[0] - 44.59817706246725) < 1e-9
    assert abs(BASE_GRAPH_MASS[1] - 120.89687763600345) < 1e-9
    assert abs(BASE_GRAPH_MASS[2] - 329.1851915820806) < 1e-9
    assert abs(BASE_HUB_MASS[0] - 1.1572520185069353) < 1e-12
    assert abs(BASE_HUB_MASS[1] - 1.7361325665411198) < 1e-12
    assert abs(BASE_HUB_MASS[2] - 2.6546513413534485) < 1e-12

    r8_015 = all_results[8][0.15]
    r8_005 = all_results[8][0.005]
    assert abs(r8_015["B_U H*"]["intra"] - 0.00038831543026571983) < 1e-12
    assert abs(r8_015["B_U H*"]["inter"] - 0.07612965713965107) < 1e-10
    assert abs(r8_015["B~_V H*"]["intra"] - 0.00020747116328667683) < 1e-12
    assert abs(r8_015["B~_V H*"]["inter"] - 0.03964722090973499) < 1e-10
    assert abs(r8_005["B_U H*"]["intra"] - 4.227493739527122e-07) < 1e-13
    assert abs(r8_005["B_U H*"]["inter"] - 0.07760182009854069) < 1e-10
    assert abs(r8_005["B~_V H*"]["intra"] - 2.2547431633110823e-07) < 1e-13
    assert abs(r8_005["B~_V H*"]["inter"] - 0.040236080523582685) < 1e-10

    print("PASS")
    print("Diagnostic conclusion:")
    print("- fixed-mass within-band variance scales approximately as delta^2;")
    print("- inter-band variance remains at an O(1) relative scale as delta narrows;")
    print("- local band-scale regularity can kill only the intra-band component;")
    print("- the dominant surviving variance is cross-band/cross-channel in this proxy;")
    print("- pure Route-A narrow-band smoothness cannot by itself close the full")
    print("  PR #83 variance channel; Route-B-type structured correlation remains necessary.")


if __name__ == "__main__":
    main()
