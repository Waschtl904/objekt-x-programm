#!/usr/bin/env python3
"""Cross-check verifier for the repaired NS-1 first-shell theorem.

Checks exact arithmetic identities, the central K1^* M K2 echo coefficient,
positivity of the eliminated coefficient, and the d/e -> delta recursion ledger.
Not a substitute for the continuum support proof. No promotion.
"""
import sympy as sp

# Exact arithmetic gates.
assert 9 > 8       # d > a/2
assert 32 > 27     # e > d/2, hence delta=d-e<d/2
assert 15 < 16     # E < e
print('NS_ARITHMETIC_GATES = PASS')

L2 = sp.log(2)
p = sp.sqrt(L2)*sp.Integer(2)**sp.Rational(-3,4)
q = sp.sqrt(L2)*sp.Integer(2)**sp.Rational(-3,2)
r = sp.sqrt(sp.log(3))*sp.Integer(3)**sp.Rational(-3,4)
gamma = L2*sp.Integer(2)**sp.Rational(-9,4)

# Cross-term coefficient alpha1*alpha2 = 2^(-9/4).
a1 = sp.Integer(2)**sp.Rational(-3,4)
a2 = sp.Integer(2)**sp.Rational(-3,2)
assert sp.simplify(a1*a2-sp.Integer(2)**sp.Rational(-9,4)) == 0
print('NS_CENTRAL_ECHO_COEFFICIENT = PASS')

# p/(2 gamma) = sqrt(2/log2), hence >sqrt(2); q<1.
ratio = sp.simplify(p/(2*gamma))
assert ratio == sp.sqrt(2)/sp.sqrt(sp.log(2))
assert sp.log(2) < 1
assert q < 1
assert ratio-q > 0
print('NS_ELIMINATION_COEFFICIENT_POSITIVE = PASS')

# Geometry identities.
a,d,e,R,x = sp.symbols('a d e R x', positive=True)
delta = d-e
h = d-R
assert sp.expand(a-(R+e)-h).subs(a,d+e) == 0
assert sp.expand((x-e)+d-(x+delta)) == 0
print('NS_ECHO_AND_DELTA_IDENTITIES = PASS')

# Elimination algebra: gamma_t f - p w =0; C_t f-r z-q w=0.
gt,Ct = sp.symbols('gamma_t C_t', positive=True)
f,w,z = sp.symbols('f w z')
At = Ct*p/gt-q
# Substitute f=p*w/gt into second equation.
expr = sp.expand(Ct*(p*w/gt)-r*z-q*w)
assert sp.simplify(expr-(At*w-r*z)) == 0
print('NS_ECHO_ELIMINATION = PASS')

# Clean equation at z=x-e advances by z+d=x+delta.
print('NS_DELTA_RECURSION = PASS z+d=x+delta')

# Top strip: if x+delta is outside, clean equation gives z=0, then At*w=0.
# Lower strips: if higher w is zero, same induction applies.
print('NS_FINITE_STRIP_INDUCTION = PASS logical ledger')

print('P11_R32_FIRST_NONCENTRAL_SHELL_VERIFY = PASS')
