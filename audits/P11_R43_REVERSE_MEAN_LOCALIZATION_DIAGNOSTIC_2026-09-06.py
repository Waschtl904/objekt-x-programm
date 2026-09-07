#!/usr/bin/env python3
"""
P11 / R43 — shifted-preimage localization diagnostic for the reverse mean channel.

DIAGNOSTIC SCOPE ONLY.

This script extends the exact PR #72 band-aggregated primitive-k=1 Galerkin
proxy.  It does NOT implement the actual reverse-normal vector

    x_rev = Q_{U,V} H_U^* E_{R,U} G_{R,cond}^{-1/2} epsilon_R.

Purpose:
- split the primitive local least-squares cost into weighted variance and
  coherent weighted-mean penalty;
- test whether spatial localization suppresses the mean channel;
- distinguish terminal-edge localization from localization per se.

For one new-strip node z with active old preimages x_i and weights w_i,

    W = sum_i w_i,
    xbar = (sum_i w_i x_i)/W,

and the exact primitive star minimum is

    variance + mean_penalty,

where

    variance = sum_i w_i |x_i-xbar|^2,
    mean_penalty = W/(1+W) |xbar|^2.

Weighted Cauchy gives the exact pointwise upper bound

    mean_penalty <= (1/(1+W)) sum_i w_i |x_i|^2.

Thus the coherent mean is controlled by mass on the PRIME-SHIFTED PREIMAGE
sets sampled by the new strip.  This is more precise than terminal-collar mass:
large prime shifts may sample deep bulk points, as already diagnosed in PR #69.

The present finite model uses the same U=30,V=40 and logarithmic prime bands
centered at 10,12,14 as PR #72.  It is not an asymptotic theorem.
"""

from math import exp, log, sqrt

U = 30
V = 40
CENTERS = (10, 12, 14)
HALF_WIDTH = 0.15


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


def prime_weight(p: int) -> float:
    return log(p) * (p - 1) * p ** (-1.5)


def band_weights():
    max_p = int(exp(max(CENTERS) + HALF_WIDTH)) + 16
    primes = sieve(max_p)
    out = []
    for t in CENTERS:
        band = [p for p in primes if t - HALF_WIDTH <= log(p) <= t + HALF_WIDTH]
        assert band
        out.append(sum(prime_weight(p) for p in band))
    return out


def old_graph_norm(profile, weights):
    old = set(range(-U, U + 1))
    l2 = sum(profile(z) ** 2 for z in old)
    residual = 0.0
    for shift, weight in zip(CENTERS, weights):
        for a in range(-U + shift, U + 1):
            b = a - shift
            residual += weight * (profile(a) - profile(b)) ** 2
    return l2 + residual


def star_split(profile, weights):
    old = set(range(-U, U + 1))
    new = [z for z in range(-V, V + 1) if z not in old]
    variance_total = 0.0
    mean_total = 0.0
    cauchy_total = 0.0

    for z in new:
        vals = []
        ws = []
        for shift, weight in zip(CENTERS, weights):
            for old_z in (z - shift, z + shift):
                if old_z in old:
                    vals.append(profile(old_z))
                    ws.append(weight)

        if not ws:
            continue

        W = sum(ws)
        xbar = sum(w * x for w, x in zip(ws, vals)) / W
        variance = sum(w * (x - xbar) ** 2 for w, x in zip(ws, vals))
        mean = (W / (1.0 + W)) * xbar * xbar
        cauchy_bound = sum(w * x * x for w, x in zip(ws, vals)) / (1.0 + W)

        assert mean <= cauchy_bound + 1e-12
        variance_total += variance
        mean_total += mean
        cauchy_total += cauchy_bound

    return variance_total, mean_total, cauchy_total


def report(name, profile, weights):
    graph = old_graph_norm(profile, weights)
    variance, mean, cauchy = star_split(profile, weights)
    result = {
        "variance": variance / graph,
        "mean": mean / graph,
        "total": (variance + mean) / graph,
        "mean_cauchy_bound": cauchy / graph,
    }
    print(
        f"{name:18s} mean={result['mean']:.12f}  "
        f"variance={result['variance']:.12f}  total={result['total']:.12f}  "
        f"mean-bound={result['mean_cauchy_bound']:.12f}"
    )
    return result


def main():
    weights = band_weights()
    target = log(U) / U
    print("R43 reverse-mean localization diagnostic")
    print("DIAGNOSTIC ONLY — not actual x_rev")
    print(f"weights={weights}")
    print(f"U={U}, V={V}, heuristic log(U)/U={target:.12f}")

    profiles = {
        "constant": lambda z: 1.0,
        "center-gauss12": lambda z: exp(-((z / 12.0) ** 2)),
        "edge-gauss-wide": lambda z: exp(-(((z - (U - 4)) / 6.0) ** 2)),
        "edge-gauss-narrow": lambda z: exp(-(((z - (U - 2)) / 3.0) ** 2)),
        "edge-gauss-symm": lambda z: exp(-(((abs(z) - (U - 2)) / 3.0) ** 2)),
    }

    results = {name: report(name, f, weights) for name, f in profiles.items()}

    # Reproducibility anchors.
    assert abs(results["constant"]["mean"] - 0.32720740013179683) < 1e-10
    assert abs(results["constant"]["variance"]) < 1e-14
    assert abs(results["center-gauss12"]["mean"] - 9.270339202597103e-06) < 1e-12
    assert abs(results["center-gauss12"]["variance"] - 0.00037344139986519425) < 1e-11
    assert abs(results["edge-gauss-wide"]["mean"] - 0.0014380903647534535) < 1e-11
    assert abs(results["edge-gauss-wide"]["variance"] - 0.02461316583115382) < 1e-10
    assert abs(results["edge-gauss-narrow"]["mean"] - 0.0005700301491714217) < 1e-11
    assert abs(results["edge-gauss-narrow"]["variance"] - 0.07614119345832104) < 1e-10

    # Localization strongly suppresses the coherent mean compared with the
    # constant common mode, but edge localization is not uniquely optimal.
    assert results["edge-gauss-wide"]["mean"] < 0.01 * results["constant"]["mean"]
    assert results["edge-gauss-narrow"]["mean"] < 0.01 * results["constant"]["mean"]
    assert results["center-gauss12"]["mean"] < results["edge-gauss-narrow"]["mean"]

    # In the narrow edge profile the variance, not the mean, dominates.
    assert results["edge-gauss-narrow"]["variance"] > 100.0 * results["edge-gauss-narrow"]["mean"]

    print("PASS")
    print("Conclusion:")
    print("- spatial localization can strongly suppress the coherent mean channel;")
    print("- terminal-edge localization is not the unique mechanism;")
    print("- the exact controlling object is occupancy of prime-shifted preimage sets;")
    print("- localization alone does not close the variance channel or actual rho_rev.")


if __name__ == "__main__":
    main()
