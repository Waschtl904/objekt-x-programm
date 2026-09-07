#!/usr/bin/env python3
"""
P11 / R43 — primitive-band Galerkin graph proxy for reverse extension.

DIAGNOSTIC SCOPE ONLY.

This script is NOT an implementation of the actual reverse-normal vector

    x_rev = Q_{U,V} H_U^* E_{R,U} G_{R,cond}^{-1/2} epsilon_R.

The current Draft stack contains analytic definitions and local diagnostic
scripts, but no executable end-to-end implementation of all four source /
whitening / hub / geometric-mean components.  Calling the present proxy
"x_rev" would therefore be incorrect.

Instead the script asks a logically weaker, but useful adversarial question:

    Does old primitive k=1 residual graph normalization BY ITSELF force
    cheap spatial extension at the O(log U / U) scale?

We build a finite integer-grid graph model of the level-0 primitive k=1
translation differences used in PR #64.  The three logarithmic prime bands
are exactly the PR #70 toy bands, centered at log p = 10, 12, 14 with
half-width 0.15.  The actual prime weights

    w_p = (log p)(p-1)p^(-3/2)

are summed inside each band, while each band is represented by its integer
center shift.  Thus this is a BAND-AGGREGATED GALERKIN PROXY, not the exact
P11 operator.

For old data x on [-U,U], the full proxy residual energy on [-V,V] is the
weighted graph energy over the three shift families.  New-strip values are
chosen by the exact finite least-squares problem

    min_n  E_V([x,n]) + ||n||^2.

We compare the resulting extra extension cost with the old graph norm

    ||x||^2 + E_U(x).

If graph normalization alone implied the desired reverse-extension theorem,
one would expect robust O(log U/U) control for every normalized proxy vector.
The test instead finds a clear separation: smooth localized data extend very
cheaply, while other perfectly graph-normalized data retain O(1) extension
cost.  Hence the special Q H^* E f_rev structure (or an equivalent additional
coherence theorem) is genuinely needed.

The U=30,V=40 comparison to log(U)/U is diagnostic only.  It is NOT an
application of PR #64's asymptotic r=8 log U collar theorem; at U=30 the
large-U collar admissibility regime is not satisfied.
"""

from math import cos, exp, log, sqrt


def sieve(n: int):
    mark = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        mark[0] = 0
    if n >= 1:
        mark[1] = 0
    p = 2
    while p * p <= n:
        if mark[p]:
            start = p * p
            mark[start:n + 1:p] = b"\x00" * (((n - start) // p) + 1)
        p += 1
    return [k for k in range(2, n + 1) if mark[k]]


def prime_weight(p: int) -> float:
    return log(p) * (p - 1) * p ** (-1.5)


def band_weights(centers, half_width):
    max_p = int(exp(max(centers) + half_width)) + 16
    primes = sieve(max_p)
    data = []
    for t in centers:
        band = [p for p in primes if t - half_width <= log(p) <= t + half_width]
        W = sum(prime_weight(p) for p in band)
        assert band
        data.append((t, len(band), W, band[0], band[-1]))
    return data


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


def extension_ratio(U, V, shifts, weights, profile):
    old = list(range(-U, U + 1))
    old_set = set(old)
    new = [z for z in range(-V, V + 1) if z not in old_set]
    new_index = {z: i for i, z in enumerate(new)}

    # A n = rhs is the exact Euler-Lagrange equation for minimizing
    # full weighted graph energy + ||n||^2 with old values fixed.
    m = len(new)
    A = [[0.0] * m for _ in range(m)]
    for i in range(m):
        A[i][i] = 1.0
    rhs = [0.0] * m
    edges = []

    for shift, weight in zip(shifts, weights):
        for a in range(-V + shift, V + 1):
            b = a - shift
            edges.append((a, b, weight))
            a_new = a in new_index
            b_new = b in new_index

            if a_new and b_new:
                ia, ib = new_index[a], new_index[b]
                A[ia][ia] += weight
                A[ib][ib] += weight
                A[ia][ib] -= weight
                A[ib][ia] -= weight
            elif a_new and b in old_set:
                ia = new_index[a]
                A[ia][ia] += weight
                rhs[ia] += weight * profile(b)
            elif b_new and a in old_set:
                ib = new_index[b]
                A[ib][ib] += weight
                rhs[ib] += weight * profile(a)

    nvals = chol_solve(cholesky(A), rhs)
    full_values = {z: profile(z) for z in old}
    full_values.update({z: nvals[i] for z, i in new_index.items()})

    full_residual = sum(
        weight * (full_values[a] - full_values[b]) ** 2
        for a, b, weight in edges
    )
    new_penalty = sum(v * v for v in nvals)
    old_residual = sum(
        weight * (profile(a) - profile(b)) ** 2
        for a, b, weight in edges
        if a in old_set and b in old_set
    )
    old_l2 = sum(profile(z) ** 2 for z in old)
    graph_norm = old_l2 + old_residual

    increment = full_residual + new_penalty - old_residual
    return increment / graph_norm


def main():
    centers = [10, 12, 14]
    half_width = 0.15
    bands = band_weights(centers, half_width)
    weights = [entry[2] for entry in bands]

    print("R43 primitive-band Galerkin graph proxy")
    print("DIAGNOSTIC ONLY — not actual x_rev")
    print("bands:")
    for t, count, W, p0, p1 in bands:
        print(
            f"  t={t:2d}: primes={count:5d}, W={W:.12f}, "
            f"p-range=[{p0},{p1}]"
        )

    U, V = 30, 40
    target = log(U) / U

    profiles = {
        "constant": lambda z: 1.0,
        "linear": lambda z: z / U,
        "gaussian": lambda z: exp(-((z / (0.4 * U)) ** 2)),
        "cos-low": lambda z: cos(3.0 * z / U),
        "cos-mid": lambda z: cos(0.5 * z),
        "cos-high": lambda z: cos(2.0 * z),
    }

    print(f"U={U}, V={V}, heuristic log(U)/U={target:.12f}")
    print("normalized proxy extension increments:")

    results = {}
    for name, profile in profiles.items():
        ratio = extension_ratio(U, V, centers, weights, profile)
        results[name] = ratio
        print(f"  {name:9s}: {ratio:.12f}")

    # Reproducibility anchors from the exact standard-library computation.
    assert abs(weights[0] - 44.59817706246725) < 1e-9
    assert abs(weights[1] - 120.89687763600345) < 1e-9
    assert abs(weights[2] - 329.1851915820806) < 1e-9
    assert abs(results["constant"] - 0.3272074001318) < 1e-9
    assert abs(results["linear"] - 0.00651991335977) < 1e-9
    assert abs(results["gaussian"] - 0.000382711739067) < 1e-10
    assert abs(results["cos-low"] - 0.00451807774223) < 1e-9
    assert abs(results["cos-mid"] - 0.267353927272) < 1e-9
    assert abs(results["cos-high"] - 0.107141920815) < 1e-9

    assert results["constant"] > 2.0 * target
    assert results["gaussian"] < 0.01 * target

    print("PASS")
    print(
        "Conclusion: primitive old-graph normalization alone does not force "
        "O(log U/U) cheap extension in this band-aggregated Galerkin model."
    )
    print(
        "Smooth/localized data can extend far more cheaply, so special "
        "Q H^* E f_rev structure or a proved coherence theorem remains viable."
    )


if __name__ == "__main__":
    main()
