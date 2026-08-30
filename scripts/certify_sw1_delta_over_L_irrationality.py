#!/usr/bin/env python3
"""Exact algebraic certificate for Delta/L irrationality.

Mathematical lemma:
  Delta = log 3 - (3/2) log 2,
  L     = 2 log 2 - log 3.
If Delta/L = m/n with integers m,n and n != 0, then
  2(n+m) log 3 = (3n+4m) log 2.
By unique prime valuations in Q^x, A log 3 = B log 2 with integers A,B
forces A=B=0. The resulting integer system has determinant 2, hence m=n=0,
contradicting n != 0.

The script certifies the exact coefficient reduction and integer linear system.
The prime-valuation step is the written mathematical input, not a CAS claim.
"""
from fractions import Fraction as F

# coefficient pairs in basis (log 2, log 3)
Delta=(F(-3,2),F(1))
L=(F(2),F(-1))

# n*Delta = m*L gives, after moving terms and multiplying by 2:
# 2(n+m) log3 = (3n+4m) log2.
# Coefficient matrix for the equations 2n+2m=0, 3n+4m=0:
M=((2,2),(3,4))
det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
assert det==2

# Cramer's/elementary elimination: only integer/rational solution is n=m=0.
# 2n+2m=0 => m=-n; substitute into 3n+4m=0 => -n=0.
for n in range(-20,21):
    for m in range(-20,21):
        if 2*n+2*m==0 and 3*n+4*m==0:
            assert (n,m)==(0,0)

# Exact identities for the constants used by SW1.
# a=(1/2,0), b=(0,1/2), d=b-a, e=2a-b.
a=(F(1,2),F(0)); b=(F(0),F(1,2))
d=(b[0]-a[0],b[1]-a[1])
e=(2*a[0]-b[0],2*a[1]-b[1])
D=(d[0]-e[0],d[1]-e[1])
LL=(a[0]-D[0],a[1]-D[1])
assert D==Delta
assert LL==L

print("SW1 DELTA-OVER-L IRRATIONALITY ALGEBRA CERTIFICATE: PASS")
print("Delta = log3 - 3/2 log2; L = 2 log2 - log3")
print("rationality assumption reduces to 2(n+m)log3=(3n+4m)log2")
print("prime-valuation lemma forces 2(n+m)=0 and 3n+4m=0")
print("integer coefficient determinant = 2; hence n=m=0, contradicting n!=0")
print("FIREWALL: algebraic reduction certified; prime-valuation lemma is written mathematics")
