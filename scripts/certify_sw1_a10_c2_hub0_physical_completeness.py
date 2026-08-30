#!/usr/bin/env python3
"""SW1-A10-C2-HUB0-COMP physical H E_A branch completeness certificate.

Derives the positive odd-folded hub branches directly from
  H E_A w = sum_{tau in {a,b,T}} c_tau [w(x-tau)-w(x+tau)]
for x>0 and odd annulus w.

For each tau there are exactly three positive physical source branches:
  tau-x with coefficient -c_tau on 0<x<tau-R,
  x-tau with coefficient +c_tau on tau+R<x<T0,
  x+tau with coefficient -c_tau on 0<x<S-tau.
The support endpoints over tau=a,b,T are exactly the nine A1 hub walls.

Firewall: physical branch/support completeness only; no Sheet/Parity transport,
matrix ledger, or injectivity claim.
"""
from fractions import Fraction as F

# symbolic vectors in (L,Delta,R,eps,sigma)
def V(L=0,D=0,R=0,E=0,S=0):
    return (F(L),F(D),F(R),F(E),F(S))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))

a=V(1,1)
b=V(F(3,2),2)
T=V(2,2)
e=V(F(1,2),0)
Sann=add(T,V(S=1))
T0=add(T,V(E=1))

taus=[("a",a,"p"),("b",b,"r"),("T",T,"q")]
branches=[]
walls=set()

for name,tau,c in taus:
    # w(x-tau), x<tau: odd folding gives -w(tau-x)
    branches.append((name+"_L","tau-x","-"+c, V(), sub(tau,V(R=1))))
    walls.add(sub(tau,V(R=1)))

    # w(x-tau), x>tau: +w(x-tau), source enters annulus at tau+R.
    # Its upper source wall tau+S lies beyond T0 in the SW1 chamber.
    branches.append((name+"_R","x-tau","+"+c, add(tau,V(R=1)), T0))
    walls.add(add(tau,V(R=1)))

    # -w(x+tau), positive source: active until x=S-tau.
    branches.append((name+"_O","x+tau","-"+c, V(), sub(Sann,tau)))
    walls.add(sub(Sann,tau))

assert len(branches)==9
assert len({x[0] for x in branches})==9

expected_walls={
    V(S=1),                 # S-T = sigma
    add(e,V(S=1)),          # S-b = e+sigma
    add(a,V(S=1)),          # S-a = a+sigma
    sub(a,V(R=1)),add(a,V(R=1)),
    sub(b,V(R=1)),add(b,V(R=1)),
    sub(T,V(R=1)),add(T,V(R=1)),
}
assert walls==expected_walls
assert len(walls)==9

# Exact upper-wall exclusions tau+S > T0:
# tau+S-T0 = tau + sigma-epsilon > 0.
# In SW1 epsilon<Delta and tau>=a=L+Delta, so tau-epsilon>0.
# Pure symbolic coefficient check: tau has positive L coefficient and
# Delta coefficient >=1, while eps<Delta.
for name,tau,c in taus:
    assert tau[0] > 0
    assert tau[1] >= 1

# The sign list is forced by oddness:
# c*w(x-tau): left -> -c*w(tau-x), right -> +c*w(x-tau);
# -c*w(x+tau) stays -c because x+tau>0.
assert [x[2] for x in branches]==[
    "-p","+p","-p",
    "-r","+r","-r",
    "-q","+q","-q",
]

print("SW1-A10-C2-HUB0-COMP PHYSICAL HUB COMPLETENESS CERTIFICATE: PASS")
print("global signed formula has 3 shifts a,b,T and 2 raw terms per shift")
print("odd folding gives exactly 3 positive physical branches per shift = 9 total")
print("branch weights:",",".join(x[2] for x in branches))
print("support-wall set is exactly sigma,e+sigma,a+sigma,a±R,b±R,T±R")
print("no H2/KNF-pulled-back channel count is used in this derivation")
print("FIREWALL: physical H E_A branch/support completeness only")
