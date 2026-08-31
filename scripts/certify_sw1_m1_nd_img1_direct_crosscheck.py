#!/usr/bin/env python3
"""Independent-path direct physical cross-check for M1-ND IMG1.

This script intentionally does NOT import the IMG1 effective-ledger script and
does NOT use M1-FULL's free_sr, hub_sr or Nwrap tables.

It re-derives source species and shifts directly from the physical affine
relations, computes source lifts from the physical source coordinate itself,
and builds the reduced P0 operator state from that route alone.

Shared inputs are limited to the already certified M1-FULL geometry fixture:
the 64 chamber representatives, B96 wall alphabet, physical FREE/HUB rows and
constant geometric parameters at r0=7/2.

The resulting reduced statistics and SHA256 fingerprint must match IMG1.
"""

from fractions import Fraction as F
from collections import defaultdict, Counter
import hashlib

import certify_sw1_a10_c2_m1_full_b96 as m1

print("SW1 M1-ND IMG1 DIRECT PHYSICAL CROSS-CHECK")

G = m1.G
GDICT = m1.gdict


def phi(gname, theta):
    _, s, eta, kappa = GDICT[gname]
    return s * theta + F(eta, 2) * m1.L + kappa * m1.D


def rho(gname, theta):
    z = phi(gname, theta)
    return z - (z // m1.L) * m1.L


def bvalue(sig, rep):
    l, k, rr, mu, nu = sig
    sigma, R, eps = rep
    z = l * m1.L + k * m1.D + rr * R + mu * eps + nu * sigma
    return z - (z // m1.L) * m1.L


def active_rows(x, eps):
    chamber = "I" if 2 * eps < m1.D else "II"
    tests = {
        "R0": 0 < x < eps,
        "R1": eps < x < m1.a - eps,
        "R2": m1.a - eps < x < m1.a,
        "R3": m1.a < x < min(m1.a + eps, 2 * m1.d - eps),
        "R4I": chamber == "I" and m1.a + eps < x < 2 * m1.d - eps,
        "R4II": chamber == "II" and 2 * m1.d - eps < x < m1.a + eps,
        "R5": max(m1.a + eps, 2 * m1.d - eps) < x < m1.T - eps,
        "R6": m1.T - eps < x < m1.T,
        "R7": m1.T < x < m1.T + eps,
    }
    return [name for name, ok in tests.items() if ok]


def hub_active(name, x, sigma, R, eps):
    T0 = m1.T + eps
    S = m1.T + sigma
    return {
        "A_L": 0 < x < m1.a - R,
        "A_R": m1.a + R < x < T0,
        "A_O": 0 < x < S - m1.a,
        "B_L": 0 < x < m1.b - R,
        "B_R": m1.b + R < x < T0,
        "B_O": 0 < x < S - m1.b,
        "T_L": 0 < x < m1.T - R,
        "T_R": m1.T + R < x < T0,
        "T_O": 0 < x < S - m1.T,
    }[name]


def derive_source(s, lam_src, k_src, gout_name):
    _, so, etao, kapo = GDICT[gout_name]
    si = s * so
    cL = s * F(etao, 2) + lam_src
    etai = int(2 * cL) % 2
    gin = next(g for g in G if g[1] == si and g[2] == etai)
    _, _, _, kapi = gin
    cD = s * kapo + k_src
    j = F(cD - kapi, si)
    assert j.denominator == 1
    return gin[0], int(j)


def effective_map(gname, j):
    _, s, eta, kappa = GDICT[gname]
    return (s, F(eta, 2), s * j + kappa)


def reduced_term(lout, block, lin, amap, coeff, gate, source, gin, j):
    col = lin if block == "H" else 3 + lin
    return (lout, col, block, lin, amap, coeff, gate, source, gin, j)


def aggregate_signature(terms):
    groups = defaultdict(list)
    for t in terms:
        lout, col, block, lin, amap, coeff, gate, source, gin, j = t
        groups[(lout, col, amap)].append(
            (coeff, block, lin, gate, source, gin, j)
        )
    return tuple(
        (key, tuple(sorted(vals, key=str)))
        for key, vals in sorted(groups.items(), key=lambda kv: str(kv[0]))
    )


EXPECTED_TOTAL = 117546
EXPECTED_STATES = 22
EXPECTED_DIGEST = "1cffd33529534a15c941b67086217f8f8c47b0cc302cb2cf740b0e08c2ff4474"
EXPECTED_AGG = Counter({1: 117546})

atom_count = 0
total_terms = 0
state_hasher = hashlib.sha256()
unique_states = set()
agg_hist = Counter()

for ci, rep in enumerate(m1.reps):
    sigma, R, eps = rep
    vals = sorted(bvalue(sig, rep) for sig in m1.B96)
    assert len(vals) == len(set(vals)) == 96
    thetas = [(vals[i] + vals[i + 1]) / 2 for i in range(95)]
    thetas.append(((vals[-1] + vals[0] + m1.L) / 2) % m1.L)

    for ai, theta in enumerate(thetas):
        atom_count += 1
        terms = []

        for lout in range(3):
            xout = theta + lout * m1.L
            T0 = m1.T + eps
            if not (0 < xout < T0):
                continue

            rows = active_rows(xout, eps)
            assert len(rows) == 1
            row = rows[0]

            # FREE: direct physical source coordinate only.
            for affine, coeff in m1.row_terms_by_name[row]:
                _, s, lam, k = m1.Fdict[affine]
                xsrc = s * xout + lam * m1.L + k * m1.D
                assert 0 < xsrc < T0

                gin, j = derive_source(s, lam, k, "P0")
                rin = rho(gin, theta + j * m1.D)
                q = (xsrc - rin) / m1.L
                assert q.denominator == 1
                lin = int(q)
                assert 0 <= lin < 3

                terms.append(
                    reduced_term(
                        lout, "H", lin, effective_map(gin, j),
                        coeff, row, affine, gin, j
                    )
                )

            # HUB: solve physical branch directly for the annulus variable.
            for name, s, lam, k, coeff in m1.HUB:
                if not hub_active(name, xout, sigma, R, eps):
                    continue

                t = s * xout - s * lam * m1.L - s * k * m1.D
                assert R < t < m1.T + sigma

                gin, j = derive_source(s, -s * lam, -s * k, "P0")
                rin = rho(gin, theta + j * m1.D)
                q = (t - rin) / m1.L
                assert q.denominator == 1
                lin = int(q)
                assert 0 <= lin < 3

                terms.append(
                    reduced_term(
                        lout, "W", lin, effective_map(gin, j),
                        coeff, name, name, gin, j
                    )
                )

        terms = sorted(terms, key=str)
        sig = aggregate_signature(terms)

        for _, vals in sig:
            agg_hist[len(vals)] += 1

        total_terms += len(terms)
        payload = (
            str(ci) + "|" + str(ai) + "|" + str(theta) + "|" + repr(sig)
        ).encode()
        state_hasher.update(payload + b"\n")
        unique_states.add(hashlib.sha256(repr(sig).encode()).hexdigest())

assert atom_count == 6144
assert total_terms == EXPECTED_TOTAL
assert len(unique_states) == EXPECTED_STATES
assert agg_hist == EXPECTED_AGG

digest = state_hasher.hexdigest()
assert digest == EXPECTED_DIGEST

print("atoms checked:", atom_count)
print("direct physical reduced terms:", total_terms)
print("aggregation multiplicity histogram:", sorted(agg_hist.items()))
print("distinct direct physical reduced states:", len(unique_states))
print("direct physical reduced SHA256:", digest)
print("No IMG1 helper/free_sr/hub_sr/Nwrap used: PASS")
print("FIREWALL: second implementation of reference-r0 reduction only")
print("SW1 M1-ND IMG1 DIRECT PHYSICAL CROSS-CHECK: PASS")
