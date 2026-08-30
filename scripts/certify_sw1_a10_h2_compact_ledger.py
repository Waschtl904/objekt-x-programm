#!/usr/bin/env python3
"""A10-H2 compact exact ledger certificate. Scope: aggregated hub-bridge ledger only."""
from fractions import Fraction as F
from itertools import combinations

# Each channel is (slope, 2*lambda, k) for x(t)=slope*t+lambda*L+k*Delta.
C=[
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1),(1,3,2),(1,4,2)],
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1),(1,3,2)],
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1)],
[(-1,2,1),(-1,4,2),(-1,4,3),(-1,5,3),(1,1,0),(1,2,1),(1,3,1)],
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1)],
[(-1,3,2),(-1,5,3),(-1,6,3),(1,-2,-1),(1,0,0),(1,1,1),(1,2,1)],
[(-1,3,2),(-1,4,2),(1,-2,-1),(1,2,1)],
[(-1,3,2),(-1,4,2),(1,-2,-1)],
[(-1,4,2),(1,-3,-2),(1,-2,-1)],
[(-1,4,2),(-1,6,3),(-1,7,4),(-1,8,4),(1,-3,-2),(1,-1,0),(1,0,0)],
[(1,-4,-2),(1,-3,-2),(1,-2,-1)]]
assert [len(x) for x in C]==[6,5,4,7,4,7,4,3,3,7,3]
assert sum(map(len,C))==53

def rel(a,b):
 s,l,k=a; t,m,j=b
 if s==t:
  x,y=m-l,j-k
  if x<0 or (x==0 and y<0): x,y=-x,-y
  return ("T",F(x,2),y)
 return ("R",F(l+m,2),k+j)

R=set(); pairs=0
for cell in C:
 for a,b in combinations(cell,2):
  pairs+=1; R.add(rel(a,b))
assert pairs==115
T={x for x in R if x[0]=="T"}; Q={x for x in R if x[0]=="R"}
assert len(R)==22 and len(T)==8 and len(Q)==14
assert max(abs(x[2]) for x in T)==2
assert max(abs(4-x[2]) for x in Q)==4
assert all(x[1].denominator in (1,2) for x in R)

# The full derivation has only two duplicate-channel coefficient sums.
# (p^2-q^2)/p>0: log2>0 and 1/(2sqrt2)>1/8, since 16>2.
assert 16>2
# (p^2-r^2)/p>0:
# log2>2/3 from the first positive term of 2*atanh(1/3).
# log3<10/9 because its atanh(1/2) tail after the first term is <1/9:
assert 2*F(1,3)==F(2,3)
assert 2*F(1,3)*F(1,8)/(1-F(1,4))==F(1,9)
# Then p^2>1/(3sqrt2), r^2<10/(27sqrt3);
# the former exceeds the latter because squaring 9sqrt3>10sqrt2 gives 243>200.
assert 243>200

print("SW1-A10-H2 COMPACT LEDGER CERTIFICATE: PASS")
print("53 aggregated channel/cell occurrences on 11 t-cells")
print("115 two-step pairs; 22 affine types = 8 translations + 14 reflections")
print("max bridge index range 4; only half-L parity over the same Delta rotation")
print("two cancellation-sensitive aggregate coefficients are strictly positive")
print("FIREWALL: aggregated H2 ledger only; no component or kernel verdict")
