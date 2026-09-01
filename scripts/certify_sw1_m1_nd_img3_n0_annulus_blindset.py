#!/usr/bin/env python3
"""SW1 M1-ND IMG3 exact N=0 annulus Neumann term / blind-set certificate.

For
    A0 = C_K D_R^{-1} H_A
this script derives the exact local formula on 0<u<R and proves that it sees
only the four annulus windows centered at e,d,a,T.  Hence A0 has an
infinite-dimensional kernel on every SW1 parameter point.

This is a genuine no-go only for the zeroth Neumann truncation.  It says
nothing negative about the full infinite Neumann operator.
"""

import sympy as sp

print("SW1 M1-ND IMG3 N=0 ANNULUS BLIND-SET CERTIFICATE")

# Physical constants.
L2,L3=sp.log(2),sp.log(3)
a=L2/2
b=L3/2
T=2*a
d=sp.simplify(b-a)
e=sp.simplify(T-b)
Delta=sp.simplify(d-e)

# Canonical coefficients.
c1=L2*2**sp.Rational(-3,2)
c3=L2*2**sp.Rational(-3)
c5=c3
c9=L2*2**sp.Rational(-9,2)
c10=L2/4
c11=2*L3/(3*sp.sqrt(3))
alphaA=sp.simplify(c1+c5)
alphab=sp.simplify(c1+c5+c11)
kappa=sp.simplify(c1+c5+c9+c10+c11)

p=sp.sqrt(L2)*2**(-sp.Rational(3,4))
r=sp.sqrt(L3)*3**(-sp.Rational(3,4))
q=sp.sqrt(L2)*2**(-sp.Rational(3,2))

dA=sp.simplify(1+alphaA)   # rows R2/R3 at a+-u
dB=sp.simplify(1+alphab)   # row R5 at b+-u
dT=sp.simplify(1+kappa)    # rows R6/R7 at T+-u

for z in [p,r,q,dA,dB,dT]:
    assert z.is_positive is True

# Symbolic annulus samples.
wdm,wdp,wam,wap,wem,wep,wTm,wTp=sp.symbols(
    "wdm wdp wam wap wem wep wTm wTp"
)
chi=sp.symbols("chi") # 1_{u<sigma}

# Exact H-values on the six KNF sample branches, after odd folding and support.
Ha_m=sp.expand(-p*wTm-r*wdp-q*wap)
Ha_p=sp.expand(-r*wdm-q*wam-chi*p*wTp)
Hb_m=sp.expand(p*wdm-q*wep)
Hb_p=sp.expand(p*wdp-q*wem)
HT_m=sp.expand(p*wam+r*wem)
HT_p=sp.expand(p*wap+r*wep)

A0=sp.expand(
    p*(Ha_m/dA-Ha_p/dA)
    +r*(Hb_m/dB-Hb_p/dB)
    +q*(HT_m/dT-HT_p/dT)
)

Cd=sp.simplify(p*r*(1/dA+1/dB))
Ca=sp.simplify(p*q*(1/dA+1/dT))
Ce=sp.simplify(r*q*(1/dB+1/dT))
CT=sp.simplify(p**2/dA)

expected=sp.expand(
    Cd*(wdm-wdp)
    +Ca*(wam-wap)
    +Ce*(wem-wep)
    -CT*(wTm-chi*wTp)
)
assert sp.simplify(A0-expected)==0

for z in [Cd,Ca,Ce,CT]:
    assert z.is_positive is True

# Structural constant ordering used by the SW1 support proof.
assert sp.simplify(d-e-Delta)==0
assert sp.simplify(a-d-e)==0
assert sp.simplify(T-2*a)==0
assert sp.simplify(e-2*Delta).is_positive is True

# Under SW1: 0<sigma<R<eps and R+eps<Delta.
# Hence 2R < Delta and e>2Delta>2R.  The four visible windows are
#   (e-R,e+R), (d-R,d+R), (a-R,a+R), (T-R,T+sigma).
# The following four blind gaps have strictly positive lengths, with
# conservative lower bounds obtained from 2R<Delta.
#
# gap0: (R,e-R), length e-2R > e-Delta > 0
# gap1: (e+R,d-R), length Delta-2R > 0
# gap2: (d+R,a-R), length e-2R > 0
# gap3: (a+R,T-R), length a-2R > 0
assert sp.simplify(e-Delta).is_positive is True
assert Delta.is_positive is True
assert sp.simplify(a-Delta).is_positive is True

print("A0 exact formula:")
print(sp.factor(expected))
print("positive coefficients Cd,Ca,Ce,CT: PASS")
print("visible windows: I_e, I_d, I_a, and left/full-right-truncated I_T")
print("blind gaps: (R,e-R), (e+R,d-R), (d+R,a-R), (a+R,T-R)")
print("all four blind gaps are nonempty on SW1: PASS")
print("CONCLUSION: ker(A0) contains L2 of the blind set, hence is infinite-dimensional")
print("FIREWALL: N=0 truncation only; no claim about the full Neumann operator")
print("SW1 M1-ND IMG3 N=0 ANNULUS BLIND-SET CERTIFICATE: PASS")
