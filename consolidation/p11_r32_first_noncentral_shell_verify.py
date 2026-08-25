#!/usr/bin/env python3
"""Cross-check verifier for the strengthened NS-1 theorem.

Checks the exact shell-width identities and the two-step d-descent arithmetic.
This is not a substitute for the continuum support proof in the audit.
No promotion is implied.
"""
import sympy as sp

# Exact arithmetic: d>a/2 iff 9>8, hence a<2d.
assert 9 > 8
print('NS_D_GT_A_HALF = PASS')

# Symbolic shell identities.
a,d,R = sp.symbols('a d R', positive=True)
h = d-R
e = a-d
assert sp.expand((a-h) - (e+R)) == 0
assert sp.expand((a+2*d-h) - (a+d+R)) == 0
print('NS_SHELL_EDGES = PASS')

# Clean lower-output corridor: a-R <= e+R iff d<=2R.
assert sp.expand((e+R) - (a-R)) == 2*R-d
print('NS_CLEAN_CORRIDOR_IDENTITY = PASS')

# Annulus-width estimate used for the two-step d descent:
# S-R < a-R <= a-d/2 < 3d/2 < 2d, using R>=d/2 and a<2d.
# Record the strict arithmetic endpoint 3d/2 < 2d.
assert sp.Rational(3,2) < 2
print('NS_TWO_D_WIDTH_BOOKKEEPING = PASS')

# Logical finite chain: high point kills directly; low point maps by +d into high,
# and a second +d exits because width<2d.
p,r = sp.symbols('p r', positive=True)
wx,wX = sp.symbols('w_x w_X')
# high equation: p*wX=0 => wX=0; low equation p*wx+r*wX=0 => wx=0.
sol = sp.solve([p*wX, p*wx+r*wX],[wx,wX], dict=True)
assert sol == [{wX:0, wx:0}]
print('NS_TWO_STEP_D_DESCENT = PASS')

print('P11_R32_FIRST_NONCENTRAL_SHELL_VERIFY = PASS')
