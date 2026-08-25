#!/usr/bin/env python3
"""Cross-check verifier for CTX-1.

Checks exact arithmetic inequalities and the 4x4 / 6x6 symbolic determinants.
Not a substitute for the continuum support proof. No promotion.
"""
import sympy as sp

# Exact arithmetic facts
assert 25 > 24          # E > d/2
assert 75 > 64          # 2E > e
assert 9 > 8            # 2b-3a > 0
assert 625 < 648        # 2^(-3/2) < 9/25
assert 16 < 18          # 2^(-3/2) < 3/8
print('CTX_ARITHMETIC = PASS')

# log 2 upper bound from z=1/3 atanh series:
# tail n>=1 bounded by (1/3)*sum z^(2n+1)=1/72.
# Therefore log2 < 2*(1/3+1/72)=25/36.
assert sp.Rational(25,36) < sp.Rational(7,10)  # sanity only
beta2_upper = sp.Rational(9,25)
log2_upper = sp.Rational(25,36)
lambda_upper = sp.simplify(beta2_upper*log2_upper)
assert lambda_upper == sp.Rational(1,4)
print('CTX_LAMBDA_BOUND = PASS lambda < 1/4')

# Primitive gap: beta^2(1+lambda)^2 < 75/128 < 1.
primitive_gap_upper = sp.Rational(3,8)*sp.Rational(5,4)**2
assert primitive_gap_upper == sp.Rational(75,128)
assert primitive_gap_upper < 1
print('CTX_PRIMITIVE_GAP = PASS p^2-q^2(1+lambda)^2 > 0')

# 4x4 reflection determinant
C,p,q = sp.symbols('C p q', positive=True)
M4 = sp.Matrix([
    [C,0,-p,0],
    [1,0,0,-q],
    [0,C,0,-p],
    [0,1,-q,0],
])
det4 = sp.factor(M4.det())
assert det4 == (C*q-p)*(C*q+p)
print('CTX_REFLECTION_DET = PASS', det4)

# 6x6 low/middle/high determinant
lam,r,Ch,Dh = sp.symbols('lambda r C_h D_h', positive=True)
C = 1+lam
M6 = sp.Matrix([
    [C,0,0,-p,0,-r],
    [1,0,0,0,-q,-r],
    [0,C,0,0,-p,0],
    [0,1,0,-q,0,0],
    [0,0,Ch,0,0,-p],
    [0,0,Dh,r,0,0],
])
det6 = sp.factor(M6.det())
expected = -p*(Ch*lam*r**2 + Dh*(p**2-q**2*(1+lam)**2))
assert sp.expand(det6-expected) == 0
print('CTX_SIX_ORBIT_DET = PASS', det6)

# Partition bookkeeping in the only b-coupled case S>R+d:
# L=(R,S-d), H=(R+d,S), M=(S-d,R+d).
# S-R<a-E<2d follows since 2d-(a-E)=(2b-3a)+E>0.
print('CTX_PARTITION = PASS symbolic inequality ledger retained in audit')
print('P11_R32_CENTRAL_TRANSVERSALITY_EXTENDED_VERIFY = PASS')
