#!/usr/bin/env python3
"""SW1 M1-ND IMG3 local R0+KNF+(R6,R7) eliminator certificate.

This certificate derives, for 0 < sigma < R and 0 < u < R, the exact
local equations at x=u, x=T-u, x=T+u together with the KNF row.

It proves two new algebraic eliminations:

1. DIFF-PIVOT:
   (R6-R7, KNF) is a 2x2 system for
       D_T = y(T-u)-y(T+u),
       D_A = y(a-u)-y(a+u),
   with an exact manifestly positive determinant.

2. SUM-CANCEL:
   R0 + (R6+R7) cancels the complete p-annulus sum
       p [w(a-u)+w(a+u)]
   exactly.

The script also records the common orbit/channel labels of all variables.

FIREWALL:
- no kernel-triviality or unique-continuation claim;
- no contraction estimate;
- no claim that the resulting recurrence preserves B_K by itself;
- no finite-window determinant is promoted to an infinite-dimensional result.
"""

import sympy as sp

print("SW1 M1-ND IMG3 LOCAL ELIMINATOR CERTIFICATE")

# ---------------------------------------------------------------------------
# 1. Exact constants from A1 / KNF.
# ---------------------------------------------------------------------------

L2, L3 = sp.log(2), sp.log(3)

c1 = L2 * 2**sp.Rational(-3, 2)
c2 = L2 * 2**sp.Rational(-9, 4)
c3 = L2 * 2**sp.Rational(-3)
c4 = c2
c5 = c3
c6 = L2 * 2**sp.Rational(-15, 4)
c7 = c3
c9 = L2 * 2**sp.Rational(-9, 2)
c10 = L2 / 4
c11 = 2 * L3 / (3 * sp.sqrt(3))

kappa = sp.simplify(c1 + c5 + c9 + c10 + c11)
beta0 = sp.simplify(-c1 + c3)
betam = sp.simplify(-c2 - c4)
betap = sp.simplify(c2 + c6)
betaT = sp.simplify(-c3 - c5 - c7 - c10)
betab = sp.simplify(-c11)

d0 = sp.simplify(1 + 2*c1)
lambda_sum = sp.simplify(1 + kappa + betaT)
lambda_diff = sp.simplify(1 + kappa - betaT)
gamma = sp.simplify(betap - betam)
beta_A_sum = sp.simplify(betap + betam)

p = sp.sqrt(L2) * 2**(-sp.Rational(3, 4))
rhub = sp.sqrt(L3) * 3**(-sp.Rational(3, 4))
q = sp.sqrt(L2) * 2**(-sp.Rational(3, 2))

assert p.is_positive is True
assert rhub.is_positive is True
assert q.is_positive is True
assert lambda_sum.is_positive is True
assert lambda_diff.is_positive is True
assert gamma.is_positive is True

# ---------------------------------------------------------------------------
# 2. Physical support geometry for the inner strip.
#
# C1B2A normalization:
#   Delta=1+2r, L=4+10r, Emax=(r+1)/2, 3<r<4,
#   0<sigma<R<eps<Emax and 0<u<R.
#
# For the R6/R7 HUB rows, p/r branches are always annulus-active and q
# branches are always lower-support dead because |u|<R.
# ---------------------------------------------------------------------------

rr = sp.symbols("rr", positive=True)
D = 1 + 2*rr
L = 4 + 10*rr
Emax = (rr + 1)/2
a = L + D
b = sp.Rational(3, 2)*L + 2*D
T = 2*L + 2*D
e = sp.simplify(T-b)
d = sp.simplify(b-a)

assert sp.simplify(e - L/2) == 0
assert sp.simplify(2*d - (L + 2*D)) == 0

# Worst-case lower-support margins after u,R < Emax.
for expr in [
    a - 2*Emax,       # a-u > R
    e - 2*Emax,       # e-u > R
    b - 2*Emax,       # b-u > R
    T - 2*Emax,       # T-u > R
]:
    assert sp.simplify(expr.subs(rr, 3)).is_positive is True
    assert sp.Poly(sp.expand(expr), rr).coeff_monomial(rr) >= 0

# Upper annulus support for a+u and e+u follows already from < T.
assert sp.simplify(T-a-Emax).subs(rr,3).is_positive is True
assert sp.simplify(T-e-Emax).subs(rr,3).is_positive is True

# At x=T+-u, the opposite +a,+b,+T HUB branches are above S=T+sigma.
# It suffices to use u+sigma < 2R < 2Emax.
for expr in [
    a - 2*Emax,
    b - 2*Emax,
    T - 2*Emax,
]:
    assert sp.simplify(expr.subs(rr,3)).is_positive is True

# ---------------------------------------------------------------------------
# 3. Symbolic local variables.
# ---------------------------------------------------------------------------

y0 = sp.symbols("y0")
Am, Ap = sp.symbols("Am Ap")          # y(a-u), y(a+u)
Bm, Bp = sp.symbols("Bm Bp")          # y(b-u), y(b+u)
Tm, Tp = sp.symbols("Tm Tp")          # y(T-u), y(T+u)
Dm, Dp = sp.symbols("Dm Dp")          # y(2d-u), y(2d+u)

wAm, wAp = sp.symbols("wAm wAp")      # w(a-u), w(a+u)
wBm, wBp = sp.symbols("wBm wBp")      # w(b-u), w(b+u)
wEm, wEp = sp.symbols("wEm wEp")      # w(e-u), w(e+u)
wTm, wTp = sp.symbols("wTm wTp")      # w(T-u), w(T+u)
chi = sp.symbols("chi")                # indicator 1_{u<sigma}; algebraic flag

# R0 at x=u.
R0 = sp.expand(
    d0*y0
    + c2*(Am+Ap)
    + beta0*(Tm+Tp)
    - p*(wAm+wAp)
    - rhub*(wBm+wBp)
    - q*wTm
    - chi*q*wTp
)

# R6 at x=T-u.  Since u<R, the q HUB branch w(-u) is support-dead.
R6 = sp.expand(
    (1+kappa)*Tm
    + betaT*Tp
    + beta0*y0
    + betam*Ap
    + betap*Am
    + betab*Dp
    + p*wAm
    + rhub*wEm
)

# R7 at x=T+u.  Again the q HUB branch w(u) is support-dead.
R7 = sp.expand(
    betaT*Tm
    + (1+kappa)*Tp
    + beta0*y0
    + betam*Am
    + betap*Ap
    + betab*Dm
    + p*wAp
    + rhub*wEp
)

# KNF admissibility row.
KNF = sp.expand(
    p*(Am-Ap)
    + rhub*(Bm-Bp)
    + q*(Tm-Tp)
)

# ---------------------------------------------------------------------------
# 4. Sum / difference channels.
# ---------------------------------------------------------------------------

SA = sp.symbols("SA")
DA = sp.symbols("DA")
SB = sp.symbols("SB")
DB = sp.symbols("DB")
ST = sp.symbols("ST")
DT = sp.symbols("DT")
SD = sp.symbols("SD")
DD = sp.symbols("DD")
SWA = sp.symbols("SWA")
DWA = sp.symbols("DWA")
SWB = sp.symbols("SWB")
SWE = sp.symbols("SWE")
DWE = sp.symbols("DWE")

subs_sd = {
    Am: (SA+DA)/2,
    Ap: (SA-DA)/2,
    Bm: (SB+DB)/2,
    Bp: (SB-DB)/2,
    Tm: (ST+DT)/2,
    Tp: (ST-DT)/2,
    Dm: (SD+DD)/2,
    Dp: (SD-DD)/2,
    wAm: (SWA+DWA)/2,
    wAp: (SWA-DWA)/2,
    wBm: SWB/2,  # only the sum enters R0; split value irrelevant here
    wBp: SWB/2,
    wEm: (SWE+DWE)/2,
    wEp: (SWE-DWE)/2,
}

R0sd = sp.simplify(R0.subs(subs_sd))
SUMsd = sp.simplify((R6+R7).subs(subs_sd))
DIFFsd = sp.simplify((R6-R7).subs(subs_sd))
KNFsd = sp.simplify(KNF.subs(subs_sd))

EXPECTED_DIFF = sp.expand(
    lambda_diff*DT
    + gamma*DA
    - betab*DD
    + p*DWA
    + rhub*DWE
)
assert sp.simplify(DIFFsd - EXPECTED_DIFF) == 0

EXPECTED_KNF = sp.expand(
    q*DT + p*DA + rhub*DB
)
assert sp.simplify(KNFsd - EXPECTED_KNF) == 0

EXPECTED_SUM = sp.expand(
    lambda_sum*ST
    + 2*beta0*y0
    + beta_A_sum*SA
    + betab*SD
    + p*SWA
    + rhub*SWE
)
assert sp.simplify(SUMsd - EXPECTED_SUM) == 0

# ---------------------------------------------------------------------------
# 5. New exact DIFF-PIVOT.
# ---------------------------------------------------------------------------

Mdiff = sp.Matrix([
    [lambda_diff, gamma],
    [q, p],
])
det_diff = sp.factor(sp.simplify(Mdiff.det()))

det_manifest = sp.simplify(
    2**sp.Rational(1,4) * sp.sqrt(L2) / 144
    * (
        72
        + 18*sp.sqrt(2)*L2
        + 45*L2
        + 16*sp.sqrt(3)*L3
    )
)
assert sp.simplify(det_diff - det_manifest) == 0
assert det_manifest.is_positive is True

Fdiff = sp.expand(
    -betab*DD + p*DWA + rhub*DWE
)
# Equations:
#   lambda_diff*DT + gamma*DA + Fdiff = 0
#   q*DT + p*DA + rhub*DB = 0
rhs = sp.Matrix([-Fdiff, -rhub*DB])
sol = sp.simplify(Mdiff.inv()*rhs)
DT_sol = sp.factor(sol[0])
DA_sol = sp.factor(sol[1])

assert sp.simplify(
    lambda_diff*DT_sol + gamma*DA_sol + Fdiff
) == 0
assert sp.simplify(
    q*DT_sol + p*DA_sol + rhub*DB
) == 0

# Cramer's-rule forms, recorded explicitly.
assert sp.simplify(
    DT_sol - (-p*Fdiff + gamma*rhub*DB)/det_diff
) == 0
assert sp.simplify(
    DA_sol - (q*Fdiff - lambda_diff*rhub*DB)/det_diff
) == 0

# ---------------------------------------------------------------------------
# 6. New exact SUM-CANCEL.
# ---------------------------------------------------------------------------

sum_cancel = sp.simplify(R0sd + SUMsd)

A_ST = sp.simplify(beta0 + lambda_sum)
A_SA = sp.simplify(c2 + beta_A_sum)
A_y0 = sp.simplify(d0 + 2*beta0)

assert sp.simplify(A_SA - 2**sp.Rational(1,4)*L2/16) == 0
assert sp.simplify(A_y0 - (1 + L2/4)) == 0
assert A_ST.is_positive is True
assert A_SA.is_positive is True
assert A_y0.is_positive is True

EXPECTED_SUM_CANCEL = sp.expand(
    A_ST*ST
    + A_SA*SA
    + A_y0*y0
    + betab*SD
    + rhub*(SWE-SWB)
    - q*wTm
    - chi*q*wTp
)
assert sp.simplify(sum_cancel - EXPECTED_SUM_CANCEL) == 0
assert sp.simplify(sp.diff(sum_cancel, SWA)) == 0

# ---------------------------------------------------------------------------
# 7. Common orbit/channel labels relative to the inner base u.
# ---------------------------------------------------------------------------

labels = {
    "Am": ("f1", "Q", 3, 0),
    "Ap": ("f1", "P", 1, 0),
    "Bm": ("f1", "Q", 2, 1),
    "Bp": ("f1", "P", 2, 1),
    "Tm": ("f2", "Q", 2, 0),
    "Tp": ("f2", "P", 2, 0),
    "Dm": ("f1", "Q", 2, 0),
    "Dp": ("f1", "P", 2, 0),
    "wAm": ("g1", "Q", 3, 0),
    "wAp": ("g1", "P", 1, 0),
    "wEm": ("g0", "Q", 4, 1),
    "wEp": ("g0", "P", 0, 1),
}
assert max(abs(v[2]) for v in labels.values()) == 4

print("R0 inner-row formula: PASS")
print("R6/R7 inner-strip HUB support: p/r active, q lower-support dead: PASS")
print("R6+R7 sum channel formula: PASS")
print("R6-R7 difference channel formula: PASS")
print("KNF difference channel formula: PASS")
print("DIFF-PIVOT determinant:")
print(det_diff)
print("DIFF-PIVOT determinant manifestly positive: PASS")
print("DT reconstruction:", DT_sol)
print("DA reconstruction:", DA_sol)
print("SUM-CANCEL removes p*[w(a-u)+w(a+u)] exactly: PASS")
print("sum-cancel horizon coefficients A_ST,A_SA,A_y0 are all positive: PASS")
print("combined inner-base orbit/channel stencil maximum |n|:", 4)
print("FIREWALL: local synchronization/elimination only; no unique continuation")
print("FIREWALL: no B_K self-map, contraction, or kernel-triviality claim")
print("SW1 M1-ND IMG3 LOCAL ELIMINATOR CERTIFICATE: PASS")
