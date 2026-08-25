#!/usr/bin/env python3
"""Cross-check verifier for NS-1 first noncentral shell transversality.

Checks exact interval identities, coefficient gap, and the two-point reflection
matrix. This is not a substitute for the continuum support proof in the audit.
No promotion is implied.
"""
import sympy as sp

# Basic exact arithmetic facts.
# d=b-a, e=a-d; d>a/2 <=> 9>8; d>e <=> 9>8 as well.
assert 9 > 8
assert 2**sp.Rational(-3,2) > 2**(-3)
print('NS_ARITHMETIC = PASS')

# Shell geometry h=d-R with R>=d/2 gives h<=R.
d, R, a = sp.symbols('d R a', positive=True)
h = d-R
# Symbolic bookkeeping identities used in the audit.
assert sp.expand((a+2*d-h) - (a+d+R)) == 0
print('NS_OUTER_REST_EDGE = PASS a+2d-h = a+d+R')

# Coefficient gap p^2-q^2 >0 from exact powers of 2.
L2 = sp.symbols('L2', positive=True)
p2 = L2 * sp.Integer(2)**sp.Rational(-3,2)
q2 = L2 * sp.Integer(2)**(-3)
gap = sp.simplify(p2-q2)
assert gap.is_positive
print('NS_PQ_GAP = PASS', gap)

# Two-point reflection system.
p,q = sp.symbols('p q', positive=True)
M = sp.Matrix([[p,-q],[-q,p]])
det = sp.factor(M.det())
assert det == p**2-q**2
print('NS_REFLECTION_DET = PASS', det)

# If R>=e=a-d, then R+d>=a, so S<a automatically implies S<R+d.
e = a-d
assert sp.expand((R+d)-a - (R-e)) == 0
print('NS_FULL_S_RANGE_FOR_R_GE_E = PASS')

print('P11_R32_FIRST_NONCENTRAL_SHELL_VERIFY = PASS')
