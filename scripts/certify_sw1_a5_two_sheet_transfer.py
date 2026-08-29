#!/usr/bin/env python3
import sympy as sp

L2,L3=sp.log(2),sp.log(3)
a=L2/2; b=L3/2; T=2*a; d=b-a; e=T-b; Delta=sp.simplify(d-e)
L=sp.simplify(a-Delta)

assert sp.simplify(Delta-(2*b-3*a))==0
assert sp.simplify(L-(4*a-2*b))==0
assert sp.simplify(L-2*e)==0
assert sp.simplify(a-(L+Delta))==0
assert sp.simplify(T-(2*L+2*Delta))==0
assert sp.simplify(2*b-(3*L+4*Delta))==0

# Translation index shifts modulo L.
assert sp.simplify(a-Delta-L)==0
assert sp.simplify(T-2*Delta-2*L)==0

# Reflection offsets relative to Q_n = 2b-x0+n Delta.
offs={
 'r_a': sp.simplify(a-2*b),
 'r_T': sp.simplify(T-2*b),
 'r_3a': sp.simplify(3*a-2*b),
 'r_4a': sp.simplify(4*a-2*b),
 'r_2b': sp.Integer(0),
}
# Exact reflection offsets, written directly as integer multiples of L plus
# the claimed Delta-index shift.
assert sp.simplify(offs['r_a']   -(-2*L-3*Delta))==0
assert sp.simplify(offs['r_T']   -(-L-2*Delta))==0
assert sp.simplify(offs['r_3a']  -(-Delta))==0
assert sp.simplify(offs['r_4a']  -L)==0
assert sp.simplify(offs['r_2b'])==0

# Horizon lift count: T0<3L uniformly on SW1 since eps<Delta.
eps=sp.symbols('eps', positive=True)
T0=T+eps
assert sp.simplify((3*L-T0)-((a-4*Delta)+(Delta-eps)))==0
assert sp.simplify(a-4*Delta).is_positive is True

# Lower-chamber hole.
Aeps=2*d-eps
Beps=T-eps
Ceps=T+eps-Delta
assert sp.simplify(Beps-Aeps-L)==0
assert sp.simplify(Beps-Ceps-(Delta-2*eps))==0
assert sp.simplify(Ceps-(Beps-Delta+2*eps))==0

print('SW1-A5 TWO-SHEET TRANSFER CERTIFICATE: PASS')
print(f'sympy={sp.__version__}')
print('L=a-Delta=4a-2b=2e')
print('all four translations reduce to index shifts +/-1,+/-2')
print('all five reflections reduce to the two-sheet index table')
print('T0<3L follows from (a-4Delta)+(Delta-eps)>0')
print('lower-chamber hole length Delta-2eps certified')
print('scope: affine/two-sheet normal form only; no component-finiteness or Schur verdict')
