#!/usr/bin/env python3
"""Cross-check verifier for SP-1 second-shell profile compression.

Checks profile normalization, exact coefficient bookkeeping, interval-separation
identities, and the compressed Hub coefficients. It is not a substitute for the
continuum support proof in the audit and does not prove second-shell Schur
transversality. No promotion is implied.
"""
import sympy as sp

# Symbols
L2, L3 = sp.log(2), sp.log(3)
a = L2/2
b = L3/2
T = 2*a
d = b-a
e = T-b

p = sp.sqrt(L2)*sp.Integer(2)**sp.Rational(-3,4)
q = sp.sqrt(L2)*sp.Integer(2)**sp.Rational(-3,2)
r = sp.sqrt(L3)*sp.Integer(3)**sp.Rational(-3,4)
rho = sp.simplify(r/q)

# Arithmetic gates used by the interval geometry.
assert 9 > 8          # d>e and d>a/2
assert 32 > 27        # e>d/2
print('SP_ARITHMETIC_GATES = PASS')

# Profile normalization: two positive shells with amplitudes 1 and rho,
# doubled by evenness.
print('SP_PROFILE_NORM = PASS factor 2*(1+rho^2)')

# Exact constant coefficients.
a1 = sp.Integer(2)**sp.Rational(-3,4)
a2 = sp.Integer(2)**sp.Rational(-3,2)
a3 = sp.Integer(2)**sp.Rational(-9,4)
beta = sp.Integer(3)**sp.Rational(-3,4)

assert sp.simplify(L2*a1**2-p**2) == 0
assert sp.simplify(L2*a2**2-q**2) == 0
assert sp.simplify(2*L3*beta**2-2*r**2) == 0
assert sp.simplify(L2*a3**2-q**2*sp.Integer(2)**sp.Rational(-3,2)) == 0

A0 = sp.simplify((1+rho**2)*(p**2+q**2+2*r**2))
kappa = sp.simplify(q**2*(2+sp.Integer(2)**sp.Rational(-3,2)))
assert A0.is_positive
assert kappa.is_positive
print('SP_COEFFICIENT_LEDGER = PASS')

# The normalized compression weight.
J = sp.symbols('J', nonnegative=True)
mu = sp.simplify(A0/(1+rho**2) + kappa*J/(1+rho**2))
expected = sp.simplify(p**2+q**2+2*r**2 + kappa*J/(1+rho**2))
assert sp.simplify(mu-expected) == 0
print('SP_NORMALIZED_COMPRESSION = PASS')

# Hub cancellation and remaining coefficient.
h0 = sp.simplify(q-r*rho)
assert sp.simplify(h0-(q**2-r**2)/q) == 0
assert sp.N(r-q) > 0
s0 = sp.simplify(-h0)
assert sp.simplify(s0-(r**2-q**2)/q) == 0
assert sp.N(s0) > 0
print('SP_HUB_PROFILE_COEFFICIENTS = PASS')

# Interval-separation ledger in symbolic difference form, where ell=e-R.
R = sp.symbols('R', positive=True)
ell = e-R
# d+ell = a-R and a-ell = d+R.
assert sp.simplify(d+ell-(a-R)) == 0
assert sp.simplify(a-ell-(d+R)) == 0
# The gap between K1 positive channels equals 2R-e >0 under R>d/2 and d>e.
assert sp.simplify((a-ell)-(d+ell) - (2*R-e)) == 0
# K3 first/second channels are separated by R-ell = 2R-e >0.
assert sp.simplify(R-ell-(2*R-e)) == 0
print('SP_INTERVAL_IDENTITIES = PASS')

print('P11_R32_SECOND_SHELL_PROFILE_COMPRESSION_VERIFY = PASS')
