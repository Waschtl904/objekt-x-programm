#!/usr/bin/env python3
"""SW1 M1-ND IMG3 exact horizon contraction coefficient certificate.

Finite/exact premises for the analytic theorem

    || D_R^{-1} R_R ||_{L2(B_H^0)} < 693/700 < 1,

where D_R is the IMG2 identity multiplication pivot and R_R is the
Horizon-Horizon off-diagonal FREE remainder.

This script certifies only:
- exact signs of all A1 coefficients;
- exact absolute off-diagonal row sums for the eight active M1 row types;
- the exact maximal diagonal-dominance ratio q_* (attained at R6/R7);
- q_* < 96/125 using elementary rational bounds for logs/radicals;
- d_min = 1+c1, d_max = 1+kappa and sqrt(d_max/d_min) < 251/200;
- therefore (96/125)*(251/200)=3012/3125<1.

The infinite-dimensional step using selfadjointness, symmetric atomic-kernel
quadratic forms, and the unitary positive-half/lift model is NOT machine-proved
here; it belongs to the separate IMG3 audit.
"""

from fractions import Fraction as F
import sympy as sp

print("SW1 M1-ND IMG3 HORIZON CONTRACTION COEFFICIENT CERTIFICATE")

# ---------------------------------------------------------------------------
# 1. Exact A1 coefficients.
# ---------------------------------------------------------------------------

L2, L3 = sp.log(2), sp.log(3)

c1 = L2 * 2**sp.Rational(-3,2)
c2 = L2 * 2**sp.Rational(-9,4)
c3 = L2 * 2**sp.Rational(-3)
c4 = c2
c5 = c3
c6 = L2 * 2**sp.Rational(-15,4)
c7 = c3
c9 = L2 * 2**sp.Rational(-9,2)
c10 = L2/4
c11 = 2*L3/(3*sp.sqrt(3))

alphaA = sp.simplify(c1+c5)
alphab = sp.simplify(c1+c5+c11)
kappa = sp.simplify(c1+c5+c9+c10+c11)

beta0 = sp.simplify(-c1+c3)
betam = sp.simplify(-c2-c4)
betap = sp.simplify(c2+c6)
betaT = sp.simplify(-c3-c5-c7-c10)
betab = sp.simplify(-c11)

for x in [c1,c2,c3,c5,c6,c9,c10,c11,alphaA,alphab,kappa,betap]:
    assert x.is_positive is True, x
for x in [beta0,betam,betaT,betab]:
    assert x.is_negative is True, x

ab0 = -beta0
abm = -betam
abT = -betaT
abb = -betab

# ---------------------------------------------------------------------------
# 2. Eight active row types and exact row absolute sums.
# ---------------------------------------------------------------------------

rows = {
    "R0": (
        sp.simplify(1+2*c1),
        sp.simplify(2*c2+2*ab0),
    ),
    "R1": (
        sp.simplify(1+c1),
        sp.simplify(c1+c2),
    ),
    "R2": (
        sp.simplify(1+alphaA),
        sp.simplify(c1+abm+betap+c2),
    ),
    "R3": (
        sp.simplify(1+alphaA),
        sp.simplify(c1+abm+betap+c2),
    ),
    "R4I": (
        sp.simplify(1+alphaA),
        sp.simplify(c1+abm+c2),
    ),
    "R5": (
        sp.simplify(1+alphab),
        sp.simplify(c1+abm+c2+abb),
    ),
    "R6": (
        sp.simplify(1+kappa),
        sp.simplify(ab0+abm+abT+betap+abb),
    ),
    "R7": (
        sp.simplify(1+kappa),
        sp.simplify(ab0+abm+abT+betap+abb),
    ),
}

assert len(rows)==8
ratios={name:sp.simplify(off/diag) for name,(diag,off) in rows.items()}
qstar=ratios["R6"]
assert sp.simplify(ratios["R7"]-qstar)==0

for name,ratio in ratios.items():
    assert sp.simplify(qstar-ratio).is_nonnegative is True, (name,ratio)

# Exact d_min and d_max.
dmin=sp.simplify(1+c1)
dmax=sp.simplify(1+kappa)
for name,(diag,_) in rows.items():
    assert sp.simplify(diag-dmin).is_nonnegative is True, (name,diag)
    assert sp.simplify(dmax-diag).is_nonnegative is True, (name,diag)

# ---------------------------------------------------------------------------
# 3. Elementary rational log bounds via atanh series.
#
# log x = 2 sum_{n>=0} z^(2n+1)/(2n+1), z=(x-1)/(x+1).
# After N, positive tail <=
#   2 z^(2N+3) / ((2N+3)(1-z^2)).
# ---------------------------------------------------------------------------

def log_rational_bounds(x, N):
    x=F(x)
    z=(x-1)/(x+1)
    lower=sum(
        F(2)*z**(2*n+1)/F(2*n+1)
        for n in range(N+1)
    )
    tail=F(2)*z**(2*N+3)/F(2*N+3)/(1-z*z)
    return lower, lower+tail

log2_lo,log2_hi=log_rational_bounds(2,1)
log3_lo,log3_hi=log_rational_bounds(3,2)

assert log2_lo == F(56,81)
assert log2_hi == F(1123,1620)
assert log3_lo == F(263,240)
assert log3_hi == F(923,840)

# Tighter radical rational bounds, certified by integer powers.
sqrt2_lo=F(7,5)
sqrt2_hi=F(577,408)
root4_2_hi=F(11893,10000)
sqrt3_hi=F(1351,780)
root34_2_hi=F(8409,5000)

assert sqrt2_lo**2 < 2
assert sqrt2_hi**2 > 2
assert root4_2_hi**4 > 2
assert sqrt3_hi**2 > 3
assert root34_2_hi**4 > 8

# ---------------------------------------------------------------------------
# 4. Human-checkable rational proof q_* < 96/125.
#
# SymPy simplifies
#   96*dmax - 125*off_R6
# to (13824 - QNUM)/144 where
#   QNUM =
#     612 sqrt(2) log2
#   + 1125 2^(1/4) log2
#   + 928 sqrt(3) log3
#   + 3816 log2
#   + 6750 2^(3/4) log2.
#
# We upper-bound QNUM entirely by the rational log/radical bounds above.
# ---------------------------------------------------------------------------

offmax=rows["R6"][1]
q_margin=sp.factor(sp.simplify(96*dmax-125*offmax))
QNUM=(
    612*sp.sqrt(2)*L2
    +1125*2**sp.Rational(1,4)*L2
    +928*sp.sqrt(3)*L3
    +3816*L2
    +6750*2**sp.Rational(3,4)*L2
)
assert sp.simplify(q_margin-(sp.Integer(13824)-QNUM)/144)==0

QNUM_upper=(
    612*sqrt2_hi*log2_hi
    +1125*root4_2_hi*log2_hi
    +928*sqrt3_hi*log3_hi
    +3816*log2_hi
    +6750*root34_2_hi*log2_hi
)
assert QNUM_upper < 13824
assert sp.simplify(sp.Rational(96,125)-qstar).is_positive is True

# ---------------------------------------------------------------------------
# 5. Human-checkable rational proof sqrt(dmax/dmin) < 251/200.
#
# Equivalent to 40000*dmax < 63001*dmin.
# SymPy simplifies the positive margin to
#   (828036 - 320000 sqrt(3)log3 - 540000 log2
#            + 162009 sqrt(2)log2)/36.
#
# Negative terms use upper bounds; the positive term uses lower bounds.
# ---------------------------------------------------------------------------

cond_margin=sp.factor(sp.simplify(251**2*dmin-200**2*dmax))
CNUM=(
    828036
    -320000*sp.sqrt(3)*L3
    -540000*L2
    +162009*sp.sqrt(2)*L2
)
assert sp.simplify(cond_margin-CNUM/36)==0

CNUM_lower=(
    F(828036)
    -320000*sqrt3_hi*log3_hi
    -540000*log2_hi
    +162009*sqrt2_lo*log2_lo
)
assert CNUM_lower > 0
assert sp.simplify(251**2*dmin-200**2*dmax).is_positive is True

# Final rational envelope.
q_envelope=F(96,125)
condition_envelope=F(251,200)
standard_envelope=q_envelope*condition_envelope
assert standard_envelope==F(3012,3125)
assert standard_envelope<1

print("active row types:", ",".join(rows))
for name in rows:
    print(name, "ratio=", sp.N(ratios[name], 16))
print("q_* attained at R6/R7 =",sp.N(qstar,18))
print("exact rational envelope q_* < 96/125: PASS")
print("d_min =",sp.N(dmin,18))
print("d_max =",sp.N(dmax,18))
print("exact rational envelope sqrt(d_max/d_min) < 251/200: PASS")
print("finite coefficient envelope: (96/125)*(251/200) = 3012/3125 < 1")
print("FIREWALL: analytic selfadjoint L2 contraction step is separate")
print("SW1 M1-ND IMG3 HORIZON CONTRACTION COEFFICIENT CERTIFICATE: PASS")
