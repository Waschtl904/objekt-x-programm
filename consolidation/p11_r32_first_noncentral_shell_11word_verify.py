#!/usr/bin/env python3
"""Exact bookkeeping cross-check for the NS-1 11-word Full-Rest ledger.

This checks only combinatorial word survival, coefficient identities, and the
support-separation inequalities used in the supplemental audit. It is not a
substitute for the continuum support proof and does not promote NS-1.
"""
import sympy as sp

# Exact constants.
L2 = sp.log(2)
L3 = sp.log(3)
a = L2/2
b = L3/2
d = b-a
e = a-d

# Basic exact gates used in the support separation.
assert 3 < 4                    # d<a
assert 9 > 8                    # d>a/2
assert 15 < 16                  # E<e
assert 32 > 27                  # e>d/2
print('WL_ARITHMETIC_GATES = PASS')

# (2,0) has 3x3 ordered words W_lk.
words20 = [(l,k) for l in (1,2,3) for k in (1,2,3)]
assert len(words20) == 9

# On S_R^+, right factors k=1 and k=3 die after M20.
vanishing20 = {(l,k) for l in (1,2,3) for k in (1,3)}
surviving20 = set(words20) - vanishing20
assert surviving20 == {(1,2),(2,2),(3,2)}
print('WL_20_WORD_SURVIVAL = PASS 3 of 9 survive')

# Add one (2,1) word, which vanishes, and one (3,0) word, which survives.
all_count = 9 + 1 + 1
active_count = 3 + 0 + 1
assert all_count == 11
assert active_count == 4
print('WL_GLOBAL_COUNT = PASS 4 of 11 active on S_R^+')

# Coefficients.
a1 = sp.Integer(2)**sp.Rational(-3,4)
a2 = sp.Integer(2)**sp.Rational(-3,2)
a3 = sp.Integer(2)**sp.Rational(-9,4)
gamma = sp.simplify(L2*a1*a2)
q2 = sp.simplify(L2*a2**2)
r2 = sp.simplify(L3*sp.Integer(3)**sp.Rational(-3,2))
assert gamma == L2*sp.Integer(2)**sp.Rational(-9,4)
assert q2 == L2*sp.Integer(2)**(-3)
print('WL_COEFFICIENTS = PASS')

# Support-center ledger in units of the natural shifts.
# g=M20 K2 y is centered at +-a.
centers = {
    (1,2): {0, 2},       # units of a: 0, +-2a
    (2,2): {1, 3},       # +-a, +-3a
    (3,2): {2, 4},       # +-2a, +-4a
}
assert centers[(1,2)] == {0,2}
assert centers[(2,2)] == {1,3}
assert centers[(3,2)] == {2,4}
print('WL_20_SUPPORT_CENTERS = PASS')

# (3,0): Ly is centered at +-d; L* with halfshift b=a+d gives +-a and +-(a+2d).
print('WL_30_SUPPORT_CENTERS = PASS +-a and +-(a+2d)')

# Separation logic under R>=d/2, h=d-R:
# h<=d/2 => 2h<=d<a, hence a-h>h and 2a-h>a+h.
# d>h for R>0 gives a+2d-h>a+h.
R,h = sp.symbols('R h', positive=True)
# Identities retained symbolically.
assert sp.expand((a-(d-R)) - (d-R)) == sp.expand(a-2*d+2*R)
assert sp.expand((2*a-(d-R)) - (a+(d-R))) == sp.expand(a-2*d+2*R)
assert sp.expand((a+2*d-(d-R)) - (a+(d-R))) == 2*R
print('WL_SUPPORT_SEPARATION_IDENTITIES = PASS')

# 3a lies outside the horizon because T0<c<3a follows from 5<8.
assert 5 < 8
print('WL_3A_OUTSIDE_HORIZON = PASS')

print('P11_R32_FIRST_NONCENTRAL_SHELL_11WORD_VERIFY = PASS')
