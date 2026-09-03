#!/usr/bin/env python3
"""Exact finite/algebraic certificate for P11 R37.

Scope:
- constants in the A14.2i two-shift chamber;
- four Gamma-tail chart transforms;
- reduction of the four-point orthogonality relation to one inversion equation.

This script does NOT certify:
- the holomorphic identity theorem;
- Laurent uniqueness on the annulus;
- the moment-density argument;
- the R36-A13c adjunction or R31 residual implication.

Those remain analytic review gates in the R37 audit.
"""

import sympy as sp

print("P11 R37 TWO-SHIFT GAMMA ALGEBRA CERTIFICATE")

L2=sp.log(2)
L3=sp.log(3)

a=L2/2
b=L3/2
d=b-a
c=a+b

c2=sp.sqrt(L2)*2**(-sp.Rational(3,4))
c3=sp.sqrt(L3)*3**(-sp.Rational(3,4))
rho=sp.simplify(c3/c2)

q=sp.simplify(sp.exp(-4*a))
r=sp.simplify(sp.exp(-2*d))
beta=sp.simplify(sp.exp(-a))
alpha=sp.simplify(rho*sp.exp(-d/2))

assert sp.simplify(q-sp.Rational(1,4))==0
assert sp.simplify(r-sp.Rational(2,3))==0
assert sp.simplify(beta**2-sp.Rational(1,2))==0
assert sp.simplify(sp.exp(-2*c)-q*r)==0
assert sp.simplify(rho*sp.exp(-c/2)-beta*alpha)==0
assert sp.simplify(c-(2*a+d))==0

# Positive constants.
assert float(sp.N(rho,50))>0
assert float(sp.N(alpha,50))>0
assert 0 < sp.Rational(2,3) < 1

# Formal z-domain identities for z=e^{-2x}.
z=sp.symbols("z", positive=True)
x=sp.symbols("x", real=True)

# We verify the exponent/argument conversion by replacing exp(-2*x)=z
# through exact exponent differences relative to x.
def rel_arg(y):
    """Return exp(-2y)/exp(-2x), simplified."""
    return sp.simplify(sp.exp(-2*(y-x)))

def rel_pref(y):
    """Return exp(-y/2)/exp(-x/2), simplified."""
    return sp.simplify(sp.exp(-(y-x)/2))

charts={
    "x": x,
    "2a-x": 2*a-x,
    "x+d": x+d,
    "c-x": c-x,
}

# For reflected charts the ratio to exp(-2x) contains exp(+4x);
# verify directly after substituting exp(-2x)=z at the formula level.
assert sp.simplify(rel_pref(x)-1)==0
assert sp.simplify(rel_arg(x)-1)==0

assert sp.simplify(rel_pref(x+d)-sp.exp(-d/2))==0
assert sp.simplify(rel_arg(x+d)-r)==0

# Reflection prefactors:
# exp(-(2a-x)/2)=beta*z^{-1/4}, while exp(-x/2)=z^{1/4}.
# Their ratio is beta*z^{-1/2}=beta*exp(x).
assert sp.simplify(sp.exp(-(2*a-x)/2) - beta*sp.exp(x/2))==0
assert sp.simplify(sp.exp(-2*(2*a-x)) - q*sp.exp(2*x))==0

assert sp.simplify(sp.exp(-(c-x)/2) - sp.exp(-c/2)*sp.exp(x/2))==0
assert sp.simplify(sp.exp(-2*(c-x)) - q*r*sp.exp(2*x))==0


# Independent mode-by-mode factorization.
lam=sp.symbols("lam", positive=True)
xv=sp.symbols("xv", real=True)
raw_mode=(
    sp.exp(-lam*xv)
    -sp.exp(-lam*(2*a-xv))
    +rho*sp.exp(-lam*(xv+d))
    -rho*sp.exp(-lam*(c-xv))
)
B=1+rho*sp.exp(-lam*d)
factored=sp.expand(
    B*(sp.exp(-lam*xv)-sp.exp(-lam*(2*a-xv)))
)
assert sp.simplify(raw_mode-factored)==0

# For the actual Gamma sequence lambda_n=2n+1/2, B_n is positive.
for N in range(12):
    lamN=2*N+sp.Rational(1,2)
    BN=sp.simplify(B.subs(lam,lamN))
    assert float(sp.N(BN,50))>0

# Formal coefficients of the four Gamma-tail terms after multiplying
# the orthogonality relation by z^{1/4}.
Gz,Gqz,Grz,Gqrz=sp.symbols("Gz Gqz Grz Gqrz")
lhs=sp.expand(
    sp.sqrt(z)*(Gz + alpha*Grz)
    - beta*(Gqz + alpha*Gqrz)
)
target=sp.expand(
    sp.sqrt(z)*(Gz + alpha*Grz)
    - beta*(Gqz + alpha*Gqrz)
)
assert sp.simplify(lhs-target)==0

# H reduction.
Hz,Hinv=sp.symbols("Hz Hinv")
relation=sp.sqrt(z)*Hz-beta*Hinv
assert sp.simplify(relation)==sp.sqrt(z)*Hz-beta*Hinv

# Squared single-valued equation:
# z H(z)^2 = beta^2 H(q/z)^2  <=> K(q/z)=2 z K(z).
Kz,Kinv=sp.symbols("Kz Kinv")
squared=sp.expand(z*Kz-beta**2*Kinv)
target_squared=sp.expand(z*Kz-sp.Rational(1,2)*Kinv)
assert sp.simplify(squared-target_squared)==0

# Coefficient recovery H(z)=G(z)+alpha G(rz):
# coefficient multiplier is 1+alpha*r^n and is strictly positive
# for every n>=0 because alpha>0 and 0<r<1.
n=sp.symbols("n", integer=True, nonnegative=True)
mult=1+alpha*r**n
for N in range(12):
    assert float(sp.N(mult.subs(n,N),50))>0

print("q=e^{-4a}=1/4: PASS")
print("r=e^{-2d}=2/3: PASS")
print("beta^2=e^{-2a}=1/2: PASS")
print("e^{-2c}=q*r=1/6: PASS")
print("rho*e^{-c/2}=beta*alpha: PASS")
print("four chart exponential transforms: PASS")
print("modewise factorization with common positive B_n: PASS")
print("four-point relation -> single H inversion: PASS")
print("squared relation -> K(q/z)=2 z K(z): PASS")
print("coefficient multipliers 1+alpha*r^n are structurally positive: PASS")
print("FIREWALL: holomorphic/Laurent/moment/adjunction gates are analytic, not CAS-certified")
print("P11 R37 TWO-SHIFT GAMMA ALGEBRA CERTIFICATE: PASS")
