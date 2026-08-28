#!/usr/bin/env python3
"""
Exact algebraic certificate for Objekt-X SW1-AWI.

Scope:
- fixed identities 2d=a+Delta and the A-wall reflection law;
- exact A-wall coefficient signs;
- 2x2 reflection-block diagonalization and invertibility.

Requires: sympy
"""
import sympy as sp

a = sp.log(2) / 2
b = sp.log(3) / 2
T = 2 * a
d = b - a
e = T - b
Delta = d - e

assert sp.simplify(2*d - a - Delta) == 0

s = sp.symbols("s", real=True)
j = sp.simplify(Delta - s)

# Physical collision identity:
assert sp.simplify((a+s) - (2*d-j)) == 0
assert sp.simplify(Delta-j-s) == 0  # J_Delta^2(s)=s

beta_plus = sp.log(2) * (
    2**sp.Rational(-9,4) + 2**sp.Rational(-15,4)
)
c11 = 2*sp.log(3) / (3*sp.sqrt(3))
beta_b = -c11

assert beta_plus.is_positive is True
assert beta_b.is_negative is True
assert sp.simplify(sp.Rational(3,8)-beta_plus).is_positive is True
assert sp.simplify(c11-sp.Rational(3,8)).is_positive is True
assert sp.simplify(c11-beta_plus).is_positive is True

mu_sym = sp.simplify(beta_plus + beta_b)
mu_asym = sp.simplify(beta_plus - beta_b)

assert mu_sym.is_negative is True
assert mu_asym.is_positive is True

Rmat = sp.Matrix([[0,1],[1,0]])
I2 = sp.eye(2)
C = sp.simplify(beta_plus*I2 + beta_b*Rmat)

vs = sp.Matrix([1,1])
va = sp.Matrix([1,-1])

assert sp.simplify(C*vs - mu_sym*vs) == sp.zeros(2,1)
assert sp.simplify(C*va - mu_asym*va) == sp.zeros(2,1)
assert sp.simplify(C.det() - (beta_plus**2-beta_b**2)) == 0
assert C.det().is_nonzero is True

Cinv = sp.simplify((beta_plus*I2-beta_b*Rmat)/(beta_plus**2-beta_b**2))
assert sp.simplify(C*Cinv-I2) == sp.zeros(2)

print("SW1-AWI CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("2d=a+Delta: certified")
print("collision law a+s = 2d-(Delta-s): certified")
print("reflection involution: certified")
print("beta_plus < 3/8 < c11=-beta_b: certified")
print("symmetric eigenvalue beta_plus+beta_b < 0")
print("antisymmetric eigenvalue beta_plus-beta_b > 0")
print("A-wall reflection block invertible")
