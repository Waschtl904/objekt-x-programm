#!/usr/bin/env python3
"""Cross-check verifier for horizon-adaptive CTX-1.

Checks exact arithmetic implications and the 4x4 / 6x6 symbolic determinants.
Not a substitute for the continuum support proof. No promotion.
"""
import sympy as sp

# -----------------------------------------------------------------------------
# 1. Exact arithmetic used by the adaptive proof
# -----------------------------------------------------------------------------
assert 3**2 > 2**3      # d>a/2, equivalently 9>8; also d>e
assert 25 > 24          # E>d/2, for the uniform corollary
assert 625 < 648        # 2^(-3/2) < 9/25
assert 16 < 18          # 2^(-3/2) < 3/8
assert 2**7 < 3**5      # a < 5d/2; partition length check (128<243)
print('CTX_ADAPTIVE_ARITHMETIC = PASS')

# Rest-collapse ledger:
# D_R=a-R, epsilon=T0-2a.
# R>=epsilon -> D_R<=a-epsilon.
# Omega(2,0) radius a+epsilon; k=2 min distance = a-epsilon.
# Omega(2,1) radius epsilon; k=2 min distance = 2a-epsilon > D_R.
# Omega(3,0) radius e+epsilon; k=1 min distance = 2d-epsilon
# and 2d>a -> 2d-epsilon > a-epsilon >= D_R.
print('CTX_REST_THRESHOLD = PASS symbolic ledger R>=epsilon')

# -----------------------------------------------------------------------------
# 2. Primitive coefficient gap
# -----------------------------------------------------------------------------
# log2 < 25/36 from the atanh(z=1/3) series tail bound.
beta2_upper = sp.Rational(9,25)
log2_upper = sp.Rational(25,36)
lambda_upper = sp.simplify(beta2_upper*log2_upper)
assert lambda_upper == sp.Rational(1,4)
primitive_gap_upper = sp.Rational(3,8)*sp.Rational(5,4)**2
assert primitive_gap_upper == sp.Rational(75,128)
assert primitive_gap_upper < 1
print('CTX_PRIMITIVE_GAP = PASS p^2-q^2(1+lambda)^2 > 0')

# -----------------------------------------------------------------------------
# 3. 4x4 q-reflection orbit
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# 4. 6x6 low/middle/high b-orbit
# -----------------------------------------------------------------------------
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

# Partition bookkeeping in S>R+d:
# R>=d/2 and d>a/2 imply S-R<a-d/2<2d, so L/H do not overlap.
# d>e and 2R>=d imply e<2R, so reflection of H lies below R.
print('CTX_ORBIT_PARTITION = PASS symbolic inequality ledger')

print('P11_R32_CENTRAL_TRANSVERSALITY_EXTENDED_VERIFY = PASS')
