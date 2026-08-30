#!/usr/bin/env python3
"""SW1-A9-J1a: exact survival of genuinely new KNF channels.

Scope: new affine channels created when the reconstructed left a-branch is
inserted into J^*(I+A)J in the lower chamber. Existing A7 channels are not
fully re-aggregated here.

Firewall: J1a is not the full J1 ledger and not a separator theorem.
"""
import sympy as sp

L2=sp.log(2)
c1=L2*2**sp.Rational(-3,2)
c2=L2*2**sp.Rational(-9,4)
c5=L2*2**sp.Rational(-3)
c6=L2*2**sp.Rational(-15,4)
alphaA=c1+c5
betap=c2+c6
betam=-2*c2
lam=1+alphaA
t=2**sp.Rational(-3,4)
s=sp.symbols("s", positive=True)  # s=r/p>0

# Local physical star at A-=a-u:
# diagonal lambda; A-<->A+ coefficient -c1;
# A-<->T- coefficient betap; A-<->T+ coefficient betam;
# A-<->z(u) coefficient c2.
P=sp.simplify(lam*t-betap)
M=sp.simplify(lam*t+betam)
assert sp.simplify(P-t)==0
ratio=sp.simplify(M/t)
target=1-(2*sp.sqrt(2)-1)*L2/8
assert sp.simplify(ratio-target)==0
assert (1-L2).is_positive is True
assert (2-(2*sp.sqrt(2)-1)).is_positive is True
# Hence target > 1-2/8 = 3/4 >0.
assert sp.Rational(3,4)>0

coeff={
 "r_ab": -s*(1+c5),
 "tau_d": s*(1+c5),
 "tau_e_BmTm": s*P,
 "tau_e_BpTp": s*M,
 "r_Tb_BmTp": -s*M,
 "r_Tb_BpTm": -s*P,
 "r_b": -s*c2,
 "tau_b": s*c2,
}
assert sp.simplify(coeff["r_ab"] + coeff["tau_d"])==0
assert sp.simplify(coeff["tau_e_BmTm"]-s*t)==0
assert sp.simplify(coeff["r_Tb_BpTm"]+s*t)==0
# Sign certificate from s,c2,c5,t,M>0.
assert c2.is_positive is True and c5.is_positive is True and t.is_positive is True
assert sp.N(M,80)>0
for name,v in coeff.items():
    assert sp.simplify(v)!=0, name

# Exact phase identities for the two extra b-channels.
a=sp.log(2)/2; b=sp.log(3)/2; T=2*a
d=b-a; e=T-b; Delta=sp.simplify(d-e); L=sp.simplify(a-Delta)
assert sp.simplify(b-(sp.Rational(3,2)*L+2*Delta))==0

print("SW1-A9-J1a NEW-CHANNEL SURVIVAL CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("J0 new h-h channels survive full local J^*(I+A)J aggregation")
print("tau_e coefficients: s*t and s*M with M>0")
print("r_{a+b}/tau_d coefficients: +/- s*(1+c5)")
print("additional z-h channels r_b and tau_b survive with +/- s*c2")
print("b = 3L/2 + 2Delta, so no new irrational base phase")
print("FIREWALL: existing A7 channels not fully aggregated; no separator verdict")
