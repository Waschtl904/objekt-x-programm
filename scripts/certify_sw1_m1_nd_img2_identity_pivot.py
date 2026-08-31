#!/usr/bin/env python3
"""SW1 M1-ND IMG2 identity-pivot certificate.

Certifies that the P0-reduced IMG1 operator has a canonical safe local
multiplication pivot on the horizon channels:

    N_R(f,g) = D_R f + R_R f + H_R g,

where D_R is diagonal multiplication by the coefficient of the physical
identity term I in the unique active free row.  On every active horizon lift
this is the only contribution with the identity pullback theta -> theta, and
its coefficient is strictly > 1.

Consequently D_R is pointwise invertible on B_H^0 with ||D_R^{-1}|| <= 1,
and the kernel equation is equivalently

    f = -D_R^{-1}(R_R f + H_R g).

This is NOT inversion of an outer shift block and does not prove injectivity.

Scope: exact finite/reference-r atom bookkeeping + exact symbolic positivity
of the row multipliers.  No recurrence solvability or kernel-triviality claim.
"""

from fractions import Fraction as F
from collections import Counter
import sympy as sp

import certify_sw1_a10_c2_m1_full_b96 as m1

print("SW1 M1-ND IMG2 IDENTITY-PIVOT CERTIFICATE")

IDENTITY = (+1, F(0), 0)


def effective_map(gname, j):
    _, s, eta, kappa = m1.gdict[gname]
    return (s, F(eta, 2), s * j + kappa)


# ---------------------------------------------------------------------------
# 1. Source-level uniqueness of the identity pullback.
# ---------------------------------------------------------------------------

free_map = {}
for br in m1.FREE:
    gin, j, _, _ = m1.free_sr[(br[0], "P0")]
    free_map[br[0]] = effective_map(gin, j)

hub_map = {}
for ch in m1.HUB:
    gin, j, _, _ = m1.hub_sr[(ch[0], "P0")]
    hub_map[ch[0]] = effective_map(gin, j)

assert [name for name, amap in free_map.items() if amap == IDENTITY] == ["I"]
assert not [name for name, amap in hub_map.items() if amap == IDENTITY]

ginI, jI, mI, sI = m1.free_sr[("I", "P0")]
assert (ginI, jI, mI, sI) == ("P0", 0, 0, +1)

# ---------------------------------------------------------------------------
# 2. Exact symbolic row multipliers.
# ---------------------------------------------------------------------------

L2, L3 = sp.log(2), sp.log(3)
c1 = L2 * 2**sp.Rational(-3, 2)
c5 = L2 * 2**sp.Rational(-3)
c9 = L2 * 2**sp.Rational(-9, 2)
c10 = L2 / 4
c11 = 2 * L3 / (3 * sp.sqrt(3))

alphaA = sp.simplify(c1 + c5)
alphab = sp.simplify(c1 + c5 + c11)
kappa = sp.simplify(c1 + c5 + c9 + c10 + c11)

diag = {
    "R0": sp.simplify(1 + 2*c1),
    "R1": sp.simplify(1 + c1),
    "R2": sp.simplify(1 + alphaA),
    "R3": sp.simplify(1 + alphaA),
    "R4I": sp.simplify(1 + alphaA),
    "R4II": sp.simplify(1 + alphab),
    "R5": sp.simplify(1 + alphab),
    "R6": sp.simplify(1 + kappa),
    "R7": sp.simplify(1 + kappa),
}

for row, d in diag.items():
    assert sp.simplify(d - 1).is_positive is True, (row, d)

# In the C1B2A/M1 simplex one has eps < Emax=(r+1)/2 and
# Delta=1+2r, hence Emax < Delta/2 for r>0.  Therefore the historical
# upper-epsilon row R4II is structurally unreachable in the current M1 scope.
rr = sp.symbols("rr", positive=True)
assert sp.simplify((1 + 2*rr)/2 - (rr + 1)/2) == rr/2
ACTIVE_ROWS = set(diag) - {"R4II"}

# Cross-check symbolic names in the canonical M1 ledger.
row_I_coeff = {}
for row, (_, _, terms) in m1.ROWS.items():
    vals = [coeff for name, coeff in terms if name == "I"]
    assert len(vals) == 1
    row_I_coeff[row] = vals[0]

assert row_I_coeff == {
    "R0": "1+2c1",
    "R1": "1+c1",
    "R2": "1+alphaA",
    "R3": "1+alphaA",
    "R4I": "1+alphaA",
    "R4II": "1+alphab",
    "R5": "1+alphab",
    "R6": "1+kappa",
    "R7": "1+kappa",
}

# ---------------------------------------------------------------------------
# 3. Exhaustive reference-r atom check.
# ---------------------------------------------------------------------------

atoms = 0
active_output_slots = 0
identity_terms = 0
row_hist = Counter()
lift_hist = Counter()

for rep in m1.reps:
    sigma, R, eps = rep
    vals = sorted(m1.bvalue(sig, rep) for sig in m1.B96)
    assert len(set(vals)) == 96
    thetas = [(vals[i] + vals[i+1]) / 2 for i in range(95)]
    thetas.append(((vals[-1] + vals[0] + m1.L) / 2) % m1.L)

    for theta in thetas:
        atoms += 1
        for lout in range(3):
            xout = theta + lout*m1.L
            T0 = m1.T + eps
            if not (0 < xout < T0):
                continue

            active_output_slots += 1
            rows = m1.active_rows(xout, eps)
            assert len(rows) == 1
            row = rows[0]
            row_hist[row] += 1
            lift_hist[lout] += 1

            # Assemble every identity-pullback term in this P0 output equation.
            got = []

            for affine, coeff in m1.row_terms_by_name[row]:
                gin, j, m, s = m1.free_sr[(affine, "P0")]
                amap = effective_map(gin, j)
                lin = (
                    s * (lout - m1.Nwrap("P0", theta))
                    + m1.Nwrap(gin, theta + j*m1.D)
                    - m
                )
                if 0 <= lin < 3 and amap == IDENTITY:
                    got.append(("H", lin, affine, coeff, gin, j))

            for name, s, lam, k, coeff in m1.HUB:
                if not m1.hub_active(name, xout, sigma, R, eps):
                    continue
                gin, j, m, s2 = m1.hub_sr[(name, "P0")]
                assert s2 == s
                amap = effective_map(gin, j)
                lin = (
                    s * (lout - m1.Nwrap("P0", theta))
                    + m1.Nwrap(gin, theta + j*m1.D)
                    - m
                )
                if 0 <= lin < 3 and amap == IDENTITY:
                    got.append(("W", lin, name, coeff, gin, j))

            # Exactly one identity term: H input on the same lift, source I.
            assert got == [
                ("H", lout, "I", row_I_coeff[row], "P0", 0)
            ], (rep, theta, lout, row, got)
            identity_terms += 1

assert atoms == 64*96 == 6144
assert identity_terms == active_output_slots
assert set(row_hist) == ACTIVE_ROWS
assert row_hist["R4II"] == 0
assert lift_hist[0] == 64*96
assert lift_hist[1] > 0
assert lift_hist[2] > 0

# D_R^{-1} is a multiplication inverse on active support only.
# Since every active multiplier d_row > 1, sup |1/d_row| < 1 <= 1.
max_inverse_numeric = max(float(sp.N(1/diag[row], 30)) for row in ACTIVE_ROWS)
assert max_inverse_numeric < 1.0

print("source-level identity map unique to FREE source I: PASS")
print("HUB identity-pullback terms: 0")
print("reference atoms:", atoms)
print("active P0 horizon output slots:", active_output_slots)
print("identity pivot terms:", identity_terms)
print("active lift histogram:", sorted(lift_hist.items()))
print("active row histogram:", sorted(row_hist.items()))
print("R4II structurally inactive in M1 simplex eps<Emax<Delta/2: PASS")
print("all eight active row multipliers strictly > 1: PASS")
print("max numerical reciprocal of row multiplier:", format(max_inverse_numeric, ".16f"))
print("canonical decomposition: N_R = D_R f + R_R f + H_R g")
print("kernel relation: f = -D_R^{-1}(R_R f + H_R g)")
print("FIREWALL: only diagonal multiplication D_R is inverted; no shift/outer block")
print("FIREWALL: no contraction, recurrence solvability, or injectivity claim")
print("SW1 M1-ND IMG2 IDENTITY-PIVOT CERTIFICATE: PASS")
