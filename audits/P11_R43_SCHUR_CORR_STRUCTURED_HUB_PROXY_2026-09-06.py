#!/usr/bin/env python3
"""
P11 / R43 — structured hub-to-Schur correlation proxy diagnostic.

DIAGNOSTIC SCOPE ONLY.

This script is a fifth finite-dimensional diagnostic in the PR #70/#72/#76/#78
series.  It is deliberately narrower than an implementation of the canonical

    x_rev = Q_{U,V} H_U^* E_{R,U} f_rev.

It keeps the exact PR #72 primitive k=1 band graph and replaces the hand-picked
constant/Gaussian/cosine profiles by a structure-derived source:

1. choose a smooth compactly supported ODD source f_X;
2. apply the band-aggregated k=1 hub
       H^* f ~ - sum_p sqrt(log p) p^(-3/4) D_{log p} f,
   with the exact PR #70 prime bands centered at log p = 10,12,14;
3. obtain an EVEN raw hub vector v, as required by PR #81;
4. apply either endpoint resolvent proxy
       B_U v
   or
       (iota^* B_V iota) v.
   These are the two positive operators whose geometric mean is the true Q in
   the analytic theory.  Neither endpoint is called x_rev.
5. measure the exact finite-graph Schur forcing
       r(x) = S^* M x  in the NEW-STRIP space N,
   and compare it with the response r(1) of the old constant mode.

Important type correction:
S^* M maps the old-window space into N.  It is therefore NOT an old-window
double-shift operator.  The natural unsaturated common-mode diagnostic is the
correlation of r(x)=S^*Mx with r(1)=S^*M1 in N, together with the exact local
weighted mean/variance split from PR #70/#76.

The script uses X in {4,6,8} to avoid a single cherry-picked source width.
It tests whether the qualitative conclusion is robust across that compact
source family.

This proxy does NOT:
- compute G_{R,cond}^{-1/2} epsilon_R;
- compute the geometric mean Q itself;
- prove any estimate for the actual canonical x_rev;
- prove reverse-normal stretch decay, FD23-UNIF, FLAGDYN/TIGHT,
  Strong Terminal/C6, Object X, or RH.
"""

from math import exp, log, sqrt

U = 30
V = 40
CENTERS = (10, 12, 14)
HALF_WIDTH = 0.15
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


def prime_graph_weight(p: int) -> float:
    return log(p) * (p - 1) * p ** (-1.5)


def prime_hub_amplitude(p: int) -> float:
    return sqrt(log(p)) * p ** (-0.75)


def band_data():
    max_p = int(exp(max(CENTERS) + HALF_WIDTH)) + 16
    primes = sieve(max_p)
    out = []
    for t in CENTERS:
        band = [p for p in primes if t - HALF_WIDTH <= log(p) <= t + HALF_WIDTH]
        assert band
        graph_weight = sum(prime_graph_weight(p) for p in band)
        hub_amp = sum(prime_hub_amplitude(p) for p in band)
        out.append((t, len(band), graph_weight, hub_amp, band[0], band[-1]))
    return out


def odd_bump(t: float, radius: float) -> float:
    """C-infinity odd compact bump on (-radius,radius)."""
    if abs(t) >= radius:
        return 0.0
    r = t / radius
    return t * exp(-1.0 / (1.0 - r * r))


def raw_hub_values(radius, hub_amps):
    """
    Band-aggregated k=1 hub proxy.

    D_s = U_{s/2} - U_{-s/2}; the band centers are even integers, so the
    half-shifts 5,6,7 land on the integer grid exactly.
    """
    vals = {}
    for u in range(-U, U + 1):
        total = 0.0
        for center, amp in zip(CENTERS, hub_amps):
            a = center // 2
            total += amp * (odd_bump(u - a, radius) - odd_bump(u + a, radius))
        vals[u] = -total
    return vals


def build_resolvent_matrix(T, weights):
    nodes = list(range(-T, T + 1))
    idx = {z: i for i, z in enumerate(nodes)}
    n = len(nodes)
    A = [[0.0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = 1.0

    for shift, weight in zip(CENTERS, weights):
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


def apply_B_U(vals, nodes_U, chol_U):
    rhs = [vals[z] for z in nodes_U]
    sol = chol_solve(chol_U, rhs)
    return {z: sol[i] for i, z in enumerate(nodes_U)}


def apply_compressed_B_V(vals, nodes_V, chol_V):
    idx_V = {z: i for i, z in enumerate(nodes_V)}
    rhs = [vals.get(z, 0.0) for z in nodes_V]
    sol = chol_solve(chol_V, rhs)
    return {z: sol[idx_V[z]] for z in range(-U, U + 1)}


def old_graph_norm(vals, weights):
    old = set(range(-U, U + 1))
    l2 = sum(vals[z] ** 2 for z in old)
    residual = 0.0
    for shift, weight in zip(CENTERS, weights):
        for a in range(-U + shift, U + 1):
            b = a - shift
            residual += weight * (vals[a] - vals[b]) ** 2
    return l2 + residual


def schur_forcing(vals, weights):
    """
    Exact cross-boundary normal-equation forcing r=S^*Mx in the PR #72 graph.

    The output is indexed by NEW-STRIP nodes, as required by the operator type.
    Overall sign depends on whether the variational correction is written as
    iota x-y or iota x+y; all correlation magnitudes below are sign-insensitive.
    """
    old = set(range(-U, U + 1))
    new = [z for z in range(-V, V + 1) if z not in old]
    out = {z: 0.0 for z in new}

    for shift, weight in zip(CENTERS, weights):
        for a in range(-V + shift, V + 1):
            b = a - shift
            if a in out and b in old:
                out[a] += weight * vals[b]
            elif b in out and a in old:
                out[b] += weight * vals[a]
    return out


def cosine_abs(a, b):
    keys = list(a)
    dot = sum(a[k] * b[k] for k in keys)
    na = sqrt(sum(a[k] * a[k] for k in keys))
    nb = sqrt(sum(b[k] * b[k] for k in keys))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return abs(dot) / (na * nb)


def star_split(vals, weights):
    """Exact PR #70/#76 primitive local variance + coherent mean split."""
    old = set(range(-U, U + 1))
    new = [z for z in range(-V, V + 1) if z not in old]
    variance_total = 0.0
    mean_total = 0.0

    for z in new:
        xs = []
        ws = []
        for shift, weight in zip(CENTERS, weights):
            for old_z in (z - shift, z + shift):
                if old_z in old:
                    xs.append(vals[old_z])
                    ws.append(weight)

        if not ws:
            continue

        W = sum(ws)
        xbar = sum(w * x for w, x in zip(ws, xs)) / W
        variance_total += sum(w * (x - xbar) ** 2 for w, x in zip(ws, xs))
        mean_total += W / (1.0 + W) * xbar * xbar

    return variance_total, mean_total


def parity_error(vals):
    return max(abs(vals[u] - vals[-u]) for u in range(0, U + 1))


def diagnostics(name, vals, weights, constant_response):
    graph = old_graph_norm(vals, weights)
    forcing = schur_forcing(vals, weights)
    variance, mean = star_split(vals, weights)
    forcing_norm = sqrt(sum(v * v for v in forcing.values()))
    corr = cosine_abs(forcing, constant_response)
    result = {
        "graph": graph,
        "forcing_norm": forcing_norm,
        "common_corr": corr,
        "mean": mean / graph,
        "variance": variance / graph,
    }
    print(
        f"  {name:12s} "
        f"|S*Mx|={result['forcing_norm']:.9f}  "
        f"corr_const={result['common_corr']:.9f}  "
        f"mean/G={result['mean']:.12f}  "
        f"var/G={result['variance']:.12f}"
    )
    return result


def main():
    bands = band_data()
    weights = [row[2] for row in bands]
    hub_amps = [row[3] for row in bands]

    print("R43 structured hub-to-Schur correlation proxy")
    print("DIAGNOSTIC ONLY — not actual x_rev")
    print("bands:")
    for t, count, weight, amp, p0, p1 in bands:
        print(
            f"  logp~{t:2d}: primes={count:5d}, "
            f"graph-W={weight:.12f}, hub-A={amp:.12f}, "
            f"p-range=[{p0},{p1}]"
        )

    nodes_U, A_U = build_resolvent_matrix(U, weights)
    nodes_V, A_V = build_resolvent_matrix(V, weights)
    chol_U = cholesky(A_U)
    chol_V = cholesky(A_V)

    constant = {z: 1.0 for z in range(-U, U + 1)}
    constant_response = schur_forcing(constant, weights)

    all_results = {}
    for radius in SOURCE_RADII:
        print(f"source radius X={radius}")
        raw = raw_hub_values(radius, hub_amps)
        assert parity_error(raw) < 1e-12

        raw_force = schur_forcing(raw, weights)
        raw_force_norm = sqrt(sum(v * v for v in raw_force.values()))
        print(
            f"  {'raw H*':12s} "
            f"|S*Mx|={raw_force_norm:.9f}  "
            f"parity_err={parity_error(raw):.3e}"
        )

        b_u = apply_B_U(raw, nodes_U, chol_U)
        b_v = apply_compressed_B_V(raw, nodes_V, chol_V)
        assert parity_error(b_u) < 1e-10
        assert parity_error(b_v) < 1e-10

        ru = diagnostics("B_U H*", b_u, weights, constant_response)
        rv = diagnostics("B~_V H*", b_v, weights, constant_response)
        all_results[radius] = (raw_force_norm, ru, rv)

    # Reproducibility anchors for the exact standard-library computation.
    assert abs(weights[0] - 44.59817706246725) < 1e-9
    assert abs(weights[1] - 120.89687763600345) < 1e-9
    assert abs(weights[2] - 329.1851915820806) < 1e-9
    assert abs(hub_amps[0] - 1.1572520185069353) < 1e-12
    assert abs(hub_amps[1] - 1.7361325665411198) < 1e-12
    assert abs(hub_amps[2] - 2.6546513413534485) < 1e-12

    # For X<=8 the raw compact hub does not reach the PR #72 new-strip
    # cross-boundary forcing in these three bands.  The resolvent proxies do.
    for radius in SOURCE_RADII:
        raw_norm, ru, rv = all_results[radius]
        assert raw_norm < 1e-12
        assert ru["forcing_norm"] > 0.0
        assert rv["forcing_norm"] > 0.0

        # In both endpoint resolvent proxies, the coherent mean contribution is
        # small compared with the variance contribution.  This is the main
        # diagnostic observation, not a theorem for Q or x_rev.
        assert ru["mean"] < 0.01 * ru["variance"]
        assert rv["mean"] < 0.01 * rv["variance"]

    # Representative X=8 anchors.
    _, ru8, rv8 = all_results[8]
    assert abs(ru8["common_corr"] - 0.6642405605283507) < 1e-10
    assert abs(ru8["mean"] - 0.0003226361579182181) < 1e-12
    assert abs(ru8["variance"] - 0.07774575130993219) < 1e-10
    assert abs(rv8["common_corr"] - 0.6139952961098145) < 1e-10
    assert abs(rv8["mean"] - 0.00015509941834763424) < 1e-12
    assert abs(rv8["variance"] - 0.04037469561856026) < 1e-10

    print("PASS")
    print("Diagnostic conclusion:")
    print("- the PR #81 parity chain is reproduced: odd source -> even hub target;")
    print("- S^*Mx lives in the new-strip space N, so the old-window double-sum picture is type-wrong;")
    print("- raw compact hub support alone gives zero coupling here, but either resolvent endpoint spreads it into the Schur forcing;")
    print("- the forcing can have moderate correlation with the constant-mode response while the coherent mean cost stays tiny;")
    print("- across X=4,6,8 the weighted variance term dominates the mean term by >100x in both endpoint proxies;")
    print("- therefore common-mode coefficient control alone is unlikely to close the structured proxy: the variance/cross-prime channel remains the sharper next target.")
    print("- no statement about the true geometric mean Q or canonical x_rev is made.")


if __name__ == "__main__":
    main()
