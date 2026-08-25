#!/usr/bin/env python3
"""Arithmetic/algebra cross-check for P11/R32 FG-TR1.

This script checks:
- a=d+e and a<2d (hence one-step B_- feedback only);
- exact first- and second-layer row solves;
- the explicit right-inverse formulas;
- deterministic numerical spot checks across R<d and R>d and several horizons.

It does NOT prove the continuum L2 bounded-isomorphism statement; that proof is
in audits/P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md.
"""

import math
import sympy as sp

# Exact geometry.
L2 = sp.log(2)
L3 = sp.log(3)
a = L2 / 2
b = L3 / 2
T = 2 * a
d = b - a
e = T - b

assert sp.simplify(a - (d + e)) == 0
assert sp.simplify((2 * d - a) - (d - e)) == 0
# d-e = 1/2 log(9/8) > 0, equivalently 9>8.
assert sp.simplify((d - e) - sp.log(sp.Rational(9, 8)) / 2) == 0
assert 9 > 8
print("FG_TR1_GEOMETRY = PASS a=d+e, e<d, a<2d")

# Exact first-layer solve.
p, r, q = sp.symbols("p r q", nonzero=True)
f = sp.symbols("f")
Ap, Bm, Bp, Cm, Cp = sp.symbols("Ap Bm Bp Cm Cp")
x0 = Ap - (r / p) * (Bm - Bp) - (q / p) * (Cm - Cp) + f / p
row0 = p * (x0 - Ap) + r * (Bm - Bp) + q * (Cm - Cp)
assert sp.simplify(row0 - f) == 0
print("FG_TR1_FIRST_LAYER_SOLVE = PASS")

# Exact second-layer solve, where B_-(u)=x0(u-d).
xprev = sp.symbols("xprev")
x1 = Ap - (r / p) * (xprev - Bp) - (q / p) * (Cm - Cp) + f / p
row1 = p * (x1 - Ap) + r * (xprev - Bp) + q * (Cm - Cp)
assert sp.simplify(row1 - f) == 0
print("FG_TR1_SECOND_LAYER_SOLVE = PASS")

# Explicit right inverse Q_R with right-side free datum h=0.
f0, f1 = sp.symbols("f0 f1")
q0 = f0 / p
q1 = f1 / p - r * f0 / p**2
assert sp.simplify(p * q0 - f0) == 0
assert sp.simplify(p * q1 + r * q0 - f1) == 0
print("FG_TR1_RIGHT_INVERSE_ALGEBRA = PASS")

# Deterministic numerical spot checks, including horizon truncations.
af = 0.5 * math.log(2.0)
bf = 0.5 * math.log(3.0)
Tf = 2.0 * af
df = bf - af


def in_u(t, R, eps):
    T0 = Tf + eps
    return 0.0 < t < T0 and any(abs(t - c) < R for c in (af, bf, Tf))


def max_residual(R, eps, p0=1.7, r0=-0.9, q0=0.6):
    """Check the reconstruction against a nontrivial smooth f/h pair."""
    T0 = Tf + eps

    def ff(u):
        return math.sin(7.0 * u) + 0.3 * math.cos(11.0 * u)

    def hh(t):
        return math.cos(5.0 * t) - 0.2 * math.sin(13.0 * t)

    def ht(t):
        return hh(t) if af < t < T0 and in_u(t, R, eps) else 0.0

    def first(u):
        return (
            ht(af + u)
            - (r0 / p0) * (ht(bf - u) - ht(bf + u))
            - (q0 / p0) * (ht(Tf - u) - ht(Tf + u))
            + ff(u) / p0
        )

    def left(u):
        if u < df:
            return first(u)
        return (
            ht(af + u)
            - (r0 / p0) * (first(u - df) - ht(bf + u))
            - (q0 / p0) * (ht(Tf - u) - ht(Tf + u))
            + ff(u) / p0
        )

    def gg(t):
        if af - R < t < af:
            return left(af - t)
        return ht(t)

    def row(u):
        return (
            p0 * (gg(af - u) - gg(af + u))
            + r0 * (gg(bf - u) - gg(bf + u))
            + q0 * (gg(Tf - u) - gg(Tf + u))
        )

    err = 0.0
    n = 800
    for j in range(1, n):
        u = R * j / n
        if abs(u - df) < 1e-12:
            continue
        err = max(err, abs(row(u) - ff(u)))
    return err


# Both sides of R=d and several admissible epsilon values.
for eps in (0.03, 0.08, 0.105):
    for R in (0.05, 0.19, 0.25, 0.34):
        assert R < af
        err = max_residual(R, eps)
        assert err < 1e-11, (eps, R, err)

print("FG_TR1_NUMERICAL_RECONSTRUCTION = PASS")
print("P11_R32_TRIANGULAR_ROW_SPLITTING_VERIFY = PASS")
