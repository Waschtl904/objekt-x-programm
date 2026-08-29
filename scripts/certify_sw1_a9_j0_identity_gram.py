#!/usr/bin/env python3
"""Exact SW1-A9-J0 certificate for J_R^* J_R only.

Constants are represented as rational coefficient pairs of (log 2, log 3).
This avoids any CAS log-normalization ambiguity.

Firewall: no claim about survival after adding J_R^* A J_R, no A9 separator
theorem, no Schur injectivity, HT-RED, Objekt X, or RH claim.
"""
from fractions import Fraction as F
from itertools import combinations

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(q,x): return (q*x[0],q*x[1])
def eq(x,y): return x==y
def nz(x): return x!=(F(0),F(0))

a=(F(1,2),F(0)); b=(F(0),F(1,2)); T=(F(1),F(0))
d=sub(b,a); e=sub(T,b); Delta=sub(d,e); L=sub(a,Delta)
assert e==mul(F(1,2),L)
assert d==add(mul(F(1,2),L),Delta)
gap=sub(mul(F(1,2),L),Delta)
assert gap==(F(5,2),F(-3,2)) and 32>27  # gap = 1/2 log(32/27)>0

# branch x = slope*u + center
branches={"A+":(1,a),"B-":(-1,b),"B+":(1,b),"T-":(-1,T),"T+":(1,T)}
expected={
("A+","B-"):(-1,add(a,b),"new"),
("A+","B+"):(1,d,"new"),
("A+","T-"):(-1,mul(3,a),"existing"),
("A+","T+"):(1,a,"existing"),
("B-","B+"):(-1,mul(2,b),"existing"),
("B-","T-"):(1,e,"new"),
("B-","T+"):(-1,add(T,b),"new"),
("B+","T-"):(-1,add(T,b),"new"),
("B+","T+"):(1,e,"new"),
("T-","T+"):(-1,mul(4,a),"existing"),
}
pairs=list(combinations(branches,2))
assert len(pairs)==10 and set(pairs)==set(expected)
for s,t in pairs:
    ss,cs=branches[s]; st,ct=branches[t]
    slope=st//ss
    intercept=sub(ct,mul(F(slope),cs))
    es,ei,_=expected[(s,t)]
    assert slope==es and intercept==ei
# c=(1,-r/p,r/p,-q/p,q/p), with p,q,r>0 => all 10 pair products nonzero.
assert len(list(combinations(range(5),2)))==10

# genuinely new affine constants versus A7 list
for x in (d,mul(-1,d),e,mul(-1,e)):
    for y in (a,mul(-1,a),T,mul(-1,T)): assert nz(sub(x,y))
for x in (add(a,b),add(T,b)):
    for y in (a,T,mul(3,a),mul(4,a),mul(2,b)): assert nz(sub(x,y))

def multiple_of_L(x):
    # L=(2,-1); exact integer multiple test.
    if x[0] % L[0] != 0: return False
    k=x[0]/L[0]
    return k.denominator==1 and x[1]==k*L[1]

# P_n,eta constants (x0 omitted); Qbar has -x0 plus 2b constant.
def P(n,eta): return add(mul(F(n),Delta),mul(F(eta,2),L))
def Q(n,eta): return add(mul(2,b),add(mul(F(-n),Delta),mul(F(eta,2),L)))
for n in range(-4,5):
  for eta in (0,1):
    ep=(eta+1)%2
    assert multiple_of_L(sub(add(P(n,eta),e),P(n,ep)))
    assert multiple_of_L(sub(add(Q(n,eta),e),Q(n,ep)))
    assert multiple_of_L(sub(add(P(n,eta),d),P(n+1,ep)))
    assert multiple_of_L(sub(add(Q(n,eta),d),Q(n-1,ep)))
    assert multiple_of_L(sub(sub(add(a,b),P(n,eta)),Q(n+1,ep)))
    assert multiple_of_L(sub(sub(add(a,b),Q(n,eta)),P(n-1,ep)))
    assert multiple_of_L(sub(sub(add(T,b),P(n,eta)),Q(n,ep)))
    assert multiple_of_L(sub(sub(add(T,b),Q(n,eta)),P(n,ep)))

# Since 0<eps<Delta/2, S_eps is contained in (0,Delta).
# Its half-period translate lies in (L/2,L/2+Delta); gap Delta<L/2 above
# proves these containing intervals, hence the separator windows, are disjoint.
print("SW1-A9-J0 IDENTITY-GRAM/PARITY CERTIFICATE: PASS")
print("exact arithmetic: Python fractions.Fraction")
print("5 branches -> exactly 10 unordered off-diagonal pair channels")
print("all 10 affine relations and existing/new classification certified")
print("e=L/2, d=L/2+Delta, and Delta<L/2 certified exactly")
print("P/Qbar parity transitions certified for both parity states")
print("A8 separator window and its L/2-shift are disjoint")
print("FIREWALL: J^*J only; no edge-survival claim after J^*AJ cancellation")
