#!/usr/bin/env python3
"""Cross-check for ST-1 local 11-word and hub ledger.

This verifies exact arithmetic/position identities and coefficient signs used by
P11_R32_SECOND_SHELL_TRANSVERSALITY_LOCAL_LEDGER_AUDIT.md. It is not a
substitute for the continuum support proof and implies no promotion.
"""
import sympy as sp

L2, L3 = sp.log(2), sp.log(3)
a = L2/2
b = L3/2
T = 2*a
d = b-a
e = T-b

p = sp.sqrt(L2)*sp.Integer(2)**sp.Rational(-3,4)
q = sp.sqrt(L2)*sp.Integer(2)**sp.Rational(-3,2)
r = sp.sqrt(L3)*sp.Integer(3)**sp.Rational(-3,4)
gamma = L2*sp.Integer(2)**sp.Rational(-9,4)
beta = sp.Integer(2)**sp.Rational(-3,2)

# Exact structural arithmetic.
assert sp.simplify(a-e-d) == 0
assert sp.simplify(b-e-2*d) == 0
assert sp.simplify(T-e-b) == 0
assert sp.simplify(3*a-e-(a+b)) == 0
assert 9 > 8       # d>a/2 and d>e
assert 32 > 27     # e>d/2
print('ST_LOCAL_ARITHMETIC = PASS')

# Coefficients of the four locally surviving (2,0) words.
a1 = sp.Integer(2)**sp.Rational(-3,4)
a2 = sp.Integer(2)**sp.Rational(-3,2)
a3 = sp.Integer(2)**sp.Rational(-9,4)
assert sp.simplify(L2*a1*a1-p**2) == 0           # W11
assert sp.simplify(L2*a1*a3-q**2) == 0           # W13
assert sp.simplify(L2*a1*a2-gamma) == 0          # W12
assert sp.simplify(L2*a2*a3-gamma*beta) == 0     # W23
print('ST_LOCAL_WORD_COEFFICIENTS = PASS')

# Symbolic point identities used by the two observations.
u = sp.symbols('u', positive=True)
x1 = e-u
x2 = a-u
assert sp.simplify(x1-a + (d+u)) == 0
assert sp.simplify(x1+a - (a+e-u)) == 0
assert sp.simplify(x1-T + (b+u)) == 0
assert sp.simplify(x1-b + (2*d+u)) == 0
assert sp.simplify(x1+b - (T-u)) == 0

assert sp.simplify(x2-a + u) == 0
assert sp.simplify(x2+a - (T-u)) == 0
assert sp.simplify(x2-T + (a+u)) == 0
assert sp.simplify(x2-b + (d+u)) == 0
print('ST_LOCAL_POINT_IDENTITIES = PASS')

# Positive determinant of the sign-locked 2x2 system.
Pu, Gu = sp.symbols('P_u G_u', positive=True)
M = sp.Matrix([[-Pu, -p], [Gu, -r]])
det = sp.factor(M.det())
assert sp.simplify(det-(Pu*r+p*Gu)) == 0
assert det.is_positive
print('ST_LOCAL_SIGN_LOCK_DET = PASS', det)

# P_u positivity is uniform because p^2>q^2.
assert sp.simplify(p**2-q**2) > 0
print('ST_LOCAL_PU_GAP = PASS')

print('P11_R32_SECOND_SHELL_TRANSVERSALITY_LOCAL_LEDGER_VERIFY = PASS')
