#!/usr/bin/env python3
import sympy as sp

# Fixed constants / weights
log2, log3 = sp.log(2), sp.log(3)
a = log2/2
b = log3/2
T = 2*a
d = b-a
e = T-b
Delta = sp.simplify(d-e)

c1 = log2*2**sp.Rational(-3,2)
c2 = log2*2**sp.Rational(-9,4)
c5 = log2/8
c6 = log2*2**sp.Rational(-15,4)
c9 = log2*2**sp.Rational(-9,2)
c10 = log2/4
c11 = 2*log3/(3*sp.sqrt(3))

kappa = sp.simplify(c1+c5+c9+c10+c11)
tau = sp.simplify(1+kappa)
theta = sp.simplify(-sp.Rational(5,8)*log2)
DT = sp.simplify(tau**2-theta**2)

beta0 = sp.simplify(-c1+log2/8)
betam = sp.simplify(-2*c2)
betap = sp.simplify(c2+c6)
betab = sp.simplify(-c11)
alphab = sp.simplify(c1+c5+c11)
P = sp.simplify(1+alphab)

assert DT.is_positive is True
assert sp.simplify(tau+theta-sp.Rational(3,8)).is_positive is True
assert sp.simplify(tau-theta-1).is_positive is True

# Exact c11 < 1/2 is certified directly by SymPy and also has a hand proof in the audit.
assert sp.simplify(sp.Rational(1,2)-c11).is_positive is True

KD = sp.simplify(P-tau*betab**2/DT)
LD = sp.simplify(theta*betab**2/DT)
muS = sp.simplify(KD+LD)
muD = sp.simplify(KD-LD)

assert sp.simplify(muS - (P-betab**2/(tau+theta))) == 0
assert sp.simplify(muD - (P-betab**2/(tau-theta))) == 0
assert muS.is_positive is True
assert muD.is_positive is True
assert sp.N(muS) > sp.Rational(1,3)
assert sp.N(muD) > sp.Rational(3,4)

# Symbolic verification of the Schur substitution.
Dp,Dm,Yp,Ym,Fp,Fm,Gp,Gm = sp.symbols("Dp Dm Yp Ym Fp Fm Gp Gm")
Yp_expr = sp.simplify(-(tau*(Fp+betab*Dm)-theta*(Fm+betab*Dp))/DT)
Ym_expr = sp.simplify((theta*(Fp+betab*Dm)-tau*(Fm+betab*Dp))/DT)

eqp = sp.expand(P*Dp + betab*Ym_expr + Gp)
eqm = sp.expand(P*Dm + betab*Yp_expr + Gm)

Gphat = sp.simplify(Gp + betab*(theta*Fp-tau*Fm)/DT)
Gmhat = sp.simplify(Gm + betab*(-tau*Fp+theta*Fm)/DT)

assert sp.simplify(eqp-(KD*Dp+LD*Dm+Gphat)) == 0
assert sp.simplify(eqm-(LD*Dp+KD*Dm+Gmhat)) == 0

# On-J extra 2TP tail at t=Delta-s: coefficient of D_+(t)
extra_coeff = sp.simplify(betap*theta*betab/DT)
assert extra_coeff.is_zero is False
assert extra_coeff.is_positive is True

# Fixed inequalities needed for the KNF blind placement.
assert sp.simplify(e-2*Delta).is_positive is True
assert sp.simplify(a-2*Delta).is_positive is True

# SW1 slack parametrization:
# R=r, s=r+u, eps=r+u+v, Delta=R+eps+g=2r+u+v+g.
r,u,v,g = sp.symbols("r u v g", positive=True)
R = r
ss = r+u
eps = r+u+v
DD = 2*r+u+v+g
umin = sp.simplify(DD-ss)
uplus = sp.simplify(DD+ss)

assert sp.simplify(umin-R-(v+g)) == 0
assert sp.simplify((DD-(R+eps))-g) == 0

# u_plus + R < 2 Delta and u_minus > R.
assert sp.simplify(2*DD-(uplus+R)-(v+g)) == 0
assert sp.simplify(umin-R-(v+g)) == 0

# T-u_plus > b+R follows from e-2Delta>0 plus strict slack:
# (T-uplus)-(b+R) = e-Delta-s-R
# and Delta-(s+R)=v+g.
lhs_high_plus = sp.expand(e - DD - ss - R)
assert sp.simplify(lhs_high_plus - ((e-2*DD)+(v+g))) == 0

# T-u_minus > b+R:
lhs_high_minus = sp.expand(e - umin - R)
assert sp.simplify(lhs_high_minus - ((e-DD)+u)) == 0

# Physical affine identities for companion profiles.
s0 = sp.symbols("s0", real=True)
up = sp.simplify(Delta+s0)
um = sp.simplify(Delta-s0)
assert sp.simplify(a-up-(2*e-s0)) == 0
assert sp.simplify(a-um-(2*e+s0)) == 0
assert sp.simplify(T-up-(T-Delta-s0)) == 0
assert sp.simplify(T-um-(T-Delta+s0)) == 0

# Nonzero coefficients of the three companion y-profiles.
assert betam.is_zero is False
assert c2.is_positive is True
assert c1.is_positive is True

print("SW1-DELTA-DESCENT STAGE-3 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("effective D± Schur block derived exactly")
print("mu_Sigma > 1/3 and mu_Delta > 3/4")
print("on J: extra 2TP tail creates nonzero D_+(Delta-s) channel")
print("u=Delta±s companion profiles lie in KNF blind sectors")
print("companion coefficients beta_-, c2, -c1 are nonzero")
print("verdict: 2TP + AWI + 2d±s rows do not close Delta-descent by themselves")
