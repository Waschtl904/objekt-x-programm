#!/usr/bin/env python3
import sympy as sp

L2,L3=sp.log(2),sp.log(3)
a=L2/2; b=L3/2; T=2*a; d=b-a; e=T-b
Delta=sp.simplify(d-e)
hB=sp.simplify(e-Delta)
kB=sp.simplify(hB-Delta)
g6=sp.simplify(6*Delta-a)

s=sp.symbols("s", real=True)
rD=sp.simplify(Delta-s)
rB=sp.simplify(hB-s)

assert sp.simplify(kB-(e-2*Delta))==0
assert kB.is_positive is True
assert sp.simplify((Delta-2*kB)-g6)==0
assert g6.is_positive is True
assert sp.simplify(3*kB-Delta).is_positive is True

assert sp.simplify(Delta-rB-(s-kB))==0
assert sp.simplify(hB-rD-(s+kB))==0

# Exact finite-orbit bound:
# each translation coset has spacing kB and interval length < Delta < 3*kB,
# hence at most 3 points. A dihedral orbit is the union of at most two cosets.
assert sp.simplify(Delta-3*kB).is_negative is True

print("SW1-DELTA-DESCENT STAGE-10B CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("r_Delta o r_B = translation by -k_B")
print("r_B o r_Delta = translation by +k_B")
print("2*k_B < Delta < 3*k_B")
print("each translation coset contributes at most 3 SW1 parameters")
print("combined reflection orbit contributes at most 6 parameters")
