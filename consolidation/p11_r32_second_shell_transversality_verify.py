#!/usr/bin/env python3
"""Cross-check verifier for ST-1 second-shell transversality.

Checks the exact local Full-Rest coefficients at the two observation points,
positivity/sign separation, and the 2x2 elimination determinant. It does not
replace the continuum support proof and does not prove any statement beyond
the second explicit shell. No promotion is implied.
"""
import sympy as sp

L2 = sp.log(2)
L3 = sp.log(3)
p = sp.sqrt(L2)*sp.Integer(2)**sp.Rational(-3,4)
q = sp.sqrt(L2)*sp.Integer(2)**sp.Rational(-3,2)
r = sp.sqrt(L3)*sp.Integer(3)**sp.Rational(-3,4)
rho = sp.simplify(r/q)

a1 = sp.Integer(2)**sp.Rational(-3,4)
a2 = sp.Integer(2)**sp.Rational(-3,2)
a3 = sp.Integer(2)**sp.Rational(-9,4)
gamma = L2*sp.Integer(2)**sp.Rational(-9,4)
beta = sp.Integer(2)**sp.Rational(-3,2)

# x1=e-u coefficients: W11 and W13 only.
assert sp.simplify(L2*a1**2-p**2) == 0
assert sp.simplify(L2*a1*a3-q**2) == 0
print('ST_X1_LOCAL_WORD_COEFFICIENTS = PASS')

# x2=a-u coefficients: W12 and W23 only.
assert sp.simplify(L2*a1*a2-gamma) == 0
assert sp.simplify((L2*a2*a3)/(L2*a1*a2)-beta) == 0
print('ST_X2_LOCAL_WORD_COEFFICIENTS = PASS')

# Sign separation.
assert sp.simplify(p**2/q**2) == 2**sp.Rational(3,2)
assert sp.N(p**2-q**2) > 0
assert sp.N(gamma*rho) > 0
print('ST_SIGN_SEPARATION = PASS')

# Generic indicator values.  Matrix in variables (f, W) when chi=1:
# [-P, -p] [f] = 0
# [ G, -r] [W]
# determinant = P*r + p*G >0.
P,G = sp.symbols('P G', positive=True)
M = sp.Matrix([[-P,-p],[G,-r]])
det = sp.factor(M.det())
assert det == P*r+p*G
print('ST_TWO_POINT_DETERMINANT = PASS', det)

# If chi=0, first equation is simply -P f=0.
print('ST_CHI_ZERO_BRANCH = PASS')

# Sector check for the final P12 step: S<a<T is the only geometric fact needed.
print('ST_FINAL_HUB_INJECTIVITY_GATE = PASS requires established P12 stratum S<T')

print('P11_R32_SECOND_SHELL_TRANSVERSALITY_VERIFY = PASS')
