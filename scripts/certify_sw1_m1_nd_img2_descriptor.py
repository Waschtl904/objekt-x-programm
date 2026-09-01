#!/usr/bin/env python3
"""SW1 M1-ND IMG2 descriptor / BK-cocycle certificate.

Purpose
-------
Certify the finite affine bookkeeping behind the next M1-ND step:

1. The 12 IMG1 pullbacks act on a two-sheet, half-period-parity orbit model
   over the single Delta-rotation with local index range at most 3.
2. The KNF admissibility row defining B_K uses no new affine phase.
3. On the full SW1 parameter scope, the six KNF samples have fixed horizon
   lift channels:
       a-u,a+u,b-u,b+u -> f_1
       T-u,T+u         -> f_2.
   Hence B_K becomes an additional range-3 descriptor relation in exactly
   the same orbit algebra.

Scope firewall
--------------
Finite/algebraic affine/lift bookkeeping only. No injectivity, no recurrence
solvability, no outer-block inversion, no all-r numerical operator identity.
"""

from fractions import Fraction as F
import sympy as sp

import certify_sw1_a10_c2_m1_full_b96 as m1

print("SW1 M1-ND IMG2 DESCRIPTOR / BK-COCYCLE CERTIFICATE")

# ---------------------------------------------------------------------------
# 1. Re-derive the exact IMG1 affine alphabet from canonical M1 data.
#    alpha=(s,h,k) acts by theta -> s*theta + h*L + k*Delta (mod L).
# ---------------------------------------------------------------------------

def effective_map(gname, j):
    _, s, eta, kappa = m1.gdict[gname]
    return (s, F(eta, 2), s * j + kappa)

img1_types = set()
for br in m1.FREE:
    gin, j, _, _ = m1.free_sr[(br[0], "P0")]
    img1_types.add(effective_map(gin, j))
for ch in m1.HUB:
    gin, j, _, _ = m1.hub_sr[(ch[0], "P0")]
    img1_types.add(effective_map(gin, j))

EXPECTED_TYPES = {
    (+1, F(0), -2),
    (+1, F(0), -1),
    (+1, F(0), 0),
    (+1, F(0), 1),
    (+1, F(0), 2),
    (-1, F(0), 1),
    (-1, F(0), 2),
    (-1, F(0), 3),
    (-1, F(0), 4),
    (-1, F(1, 2), 2),
    (+1, F(1, 2), -2),
    (+1, F(1, 2), 2),
}
assert img1_types == EXPECTED_TYPES

# ---------------------------------------------------------------------------
# 2. Exact two-sheet/parity orbit coordinates.
#
# For a generic base phase t, write formally
#   P_{n,e} = +t + n*D + e/2*L,
#   Q_{n,e} = -t + (4-n)*D + e/2*L,
# with e in Z/2.
#
# These formulas are affine identities; no numerical irrationality is used.
# ---------------------------------------------------------------------------

def orbit_tuple(sheet, n, e):
    assert sheet in {"P", "Q"}
    assert e in {0, 1}
    if sheet == "P":
        return (+1, F(e, 2), n)
    return (-1, F(e, 2), 4 - n)


def apply_affine_tuple(alpha, z):
    s, h, k = alpha
    st, ht, kt = z
    # Since e/2 is only 0 or 1/2, multiplication by s leaves the parity
    # class unchanged modulo integers; reduce the L coefficient mod 1.
    hnew = s * ht + h
    hnew = hnew - (hnew.numerator // hnew.denominator)
    assert hnew in {F(0), F(1, 2)}
    return (s * st, hnew, s * kt + k)


def tuple_to_orbit(z):
    st, h, k = z
    e = int(2 * h) % 2
    if st == +1:
        return ("P", k, e)
    assert st == -1
    return ("Q", 4 - k, e)


def transition(alpha, sheet, n, e):
    return tuple_to_orbit(apply_affine_tuple(alpha, orbit_tuple(sheet, n, e)))


# Closed-form transition laws.
for alpha in sorted(EXPECTED_TYPES, key=str):
    s, h, k = alpha
    flip = int(2 * h) % 2
    for n in range(-7, 8):
        for e in (0, 1):
            gotP = transition(alpha, "P", n, e)
            gotQ = transition(alpha, "Q", n, e)
            if s == +1:
                expP = ("P", n + k, e ^ flip)
                expQ = ("Q", n - k, e ^ flip)
            else:
                expP = ("Q", n + 4 - k, e ^ flip)
                expQ = ("P", n + k - 4, e ^ flip)
            assert gotP == expP
            assert gotQ == expQ

# Local index range relative to the input index n.
jumps = {}
for alpha in sorted(EXPECTED_TYPES, key=str):
    p = transition(alpha, "P", 0, 0)
    q = transition(alpha, "Q", 0, 0)
    jp = p[1]
    jq = q[1]
    jumps[alpha] = (jp, jq)
assert max(abs(j) for pair in jumps.values() for j in pair) == 3

# Exactly the half-period IMG1 maps flip parity.
for alpha, (jp, jq) in jumps.items():
    p = transition(alpha, "P", 0, 0)
    q = transition(alpha, "Q", 0, 0)
    expect_flip = alpha[1] == F(1, 2)
    assert (p[2] == 1) == expect_flip
    assert (q[2] == 1) == expect_flip

# ---------------------------------------------------------------------------
# 3. KNF row maps in the same affine alphabet.
#
# Modulo L:
#   a-u = -u + D
#   a+u = +u + D
#   b-u = -u + L/2 + 2D
#   b+u = +u + L/2 + 2D
#   T-u = -u + 2D
#   T+u = +u + 2D.
# ---------------------------------------------------------------------------

BK_TYPES = {
    "A-": (-1, F(0), 1),
    "A+": (+1, F(0), 1),
    "B-": (-1, F(1, 2), 2),
    "B+": (+1, F(1, 2), 2),
    "T-": (-1, F(0), 2),
    "T+": (+1, F(0), 2),
}
assert set(BK_TYPES.values()) <= EXPECTED_TYPES

# Formal P-sheet version of the BK descriptor row.
# p*(A- - A+) + r*(B- - B+) + q*(T- - T+)=0
BK_P_TRANSITIONS = {
    name: transition(alpha, "P", 0, 0)
    for name, alpha in BK_TYPES.items()
}
assert BK_P_TRANSITIONS == {
    "A-": ("Q", 3, 0),
    "A+": ("P", 1, 0),
    "B-": ("Q", 2, 1),
    "B+": ("P", 2, 1),
    "T-": ("Q", 2, 0),
    "T+": ("P", 2, 0),
}

# ---------------------------------------------------------------------------
# 4. Analytic SW1 lift-channel inequalities, encoded symbolically.
#
# Use the C1B2A normalized variables valid on 3<r<4:
#   D=1+2r, L=4+10r, Emax=(r+1)/2,
# with 0<u<R<eps<Emax.
#
# We prove positive slack lower bounds after replacing u by the larger Emax.
# ---------------------------------------------------------------------------

rr = sp.symbols("rr", real=True)
D = 1 + 2 * rr
L = 4 + 10 * rr
Emax = (rr + 1) / 2
a = L + D
b = sp.Rational(3, 2) * L + 2 * D
T = 2 * L + 2 * D

# Structural identities.
assert sp.expand(L - 4 * D - 2 * rr) == 0
assert sp.expand((2 * L - b) - rr) == 0

# The following slacks are positive for rr>3, hence certainly on 3<rr<4.
slacks = {
    "a-u above L": sp.expand((a - L) - Emax),
    "a+u below 2L": sp.expand((2 * L - a) - Emax),
    "b-u above L": sp.expand((b - L) - Emax),
    "b+u below 2L": sp.expand((2 * L - b) - Emax),
    "T-u above 2L": sp.expand((T - 2 * L) - Emax),
    "T+u below 3L": sp.expand((3 * L - T) - Emax),
}

# Verify each affine slack has positive value already at rr=3 and
# nonnegative slope; strict rr>3 then gives strict positivity.
for name, expr in slacks.items():
    poly = sp.Poly(expr, rr)
    assert poly.degree() <= 1
    slope = poly.coeff_monomial(rr)
    at3 = sp.simplify(expr.subs(rr, 3))
    assert slope >= 0
    assert at3 > 0, (name, expr, at3)

# In particular:
#   L < a-u < a+u < 2L,
#   L < b-u < b+u < 2L,
#   2L < T-u < T+u < 3L.
# Thus the base-lift channels are fixed throughout SW1.
BK_CHANNELS = {
    "A-": 1,
    "A+": 1,
    "B-": 1,
    "B+": 1,
    "T-": 2,
    "T+": 2,
}
assert BK_CHANNELS["A-"] == BK_CHANNELS["A+"] == 1
assert BK_CHANNELS["B-"] == BK_CHANNELS["B+"] == 1
assert BK_CHANNELS["T-"] == BK_CHANNELS["T+"] == 2

# ---------------------------------------------------------------------------
# 5. Exact physical-coordinate spot checks on every reference chamber.
#    These are supplementary to the symbolic slack proof above.
# ---------------------------------------------------------------------------

spot_checks = 0
for sigma, R, eps in m1.reps:
    for u in (R / 5, R / 2, 4 * R / 5):
        pts = {
            "A-": m1.a - u,
            "A+": m1.a + u,
            "B-": m1.b - u,
            "B+": m1.b + u,
            "T-": m1.T - u,
            "T+": m1.T + u,
        }
        for name, x in pts.items():
            ell = int(x // m1.L)
            assert ell == BK_CHANNELS[name]
            theta = x - ell * m1.L
            s, h, k = BK_TYPES[name]
            expected_theta = (s * u + h * m1.L + k * m1.D) % m1.L
            assert theta == expected_theta
            spot_checks += 1

assert spot_checks == 64 * 3 * 6

print("IMG1 affine pullback types:", len(EXPECTED_TYPES))
print("two-sheet/parity transition law: PASS")
print("maximum local orbit-index range:", max(abs(j) for pair in jumps.values() for j in pair))
print("half-period parity flips only: PASS")
print("BK affine maps are a subset of IMG1 alphabet: PASS")
print("BK fixed channels: A+/A-/B+/B- -> f1; T+/T- -> f2")
print("BK P-sheet descriptor:", BK_P_TRANSITIONS)
print("reference-chamber physical lift/map spot checks:", spot_checks)
print("FIREWALL: descriptor/admissibility bookkeeping only; no injectivity claim")
print("SW1 M1-ND IMG2 DESCRIPTOR / BK-COCYCLE CERTIFICATE: PASS")
