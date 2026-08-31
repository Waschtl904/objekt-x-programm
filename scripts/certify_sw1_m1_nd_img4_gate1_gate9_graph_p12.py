#!/usr/bin/env python3
"""SW1 M1-ND IMG4 Gate-1/Gate-9 exact cross-check.

Gate 1:
Reconstruct the complete off-diagonal map alphabet and activity-domain unions
of the physical positive-half A1 Horizon operator in the lower chamber
epsilon0=Delta/4, directly from the A1-R0..R7 row archetypes.  Compare them
exactly with the nine A7/A8 graphing maps/domains.

This proves the mechanical premise needed by IMG4:
    Graph_off(T_B) is contained in (in fact equals, before possible
    coefficient cancellations) the A7/A8 raw FREE graph.
The five R6/R7 off-diagonal arms are checked explicitly.

Gate 9:
At the explicit IMG4 point
    epsilon0=Delta/4, R0=T/100000, sigma0=R0/2,
check the exact P12 all-radius restricted-tail hypotheses, including
T0 < c=(log 5)/2 by the integer inequality 2^5*3^2 < 5^4.

Analytic unitary transport T_B=V^*(I+A)V and the reducing-subspace theorem are
not machine-proved here; they are separate Hilbert-space steps.
"""

import sympy as sp
from fractions import Fraction as F

print("SW1 M1-ND IMG4 GATE1/GATE9 GRAPH/P12 CROSS-CHECK")

L2,L3=sp.log(2),sp.log(3)
a=L2/2
b=L3/2
T=2*a
d=b-a
e=T-b
Delta=sp.simplify(d-e)
eps=sp.simplify(Delta/4)
T0=sp.simplify(T+eps)

# Exact A1 coefficients.
c1=L2*2**sp.Rational(-3,2)
c2=L2*2**sp.Rational(-9,4)
c3=L2*2**sp.Rational(-3)
c4=L2*2**sp.Rational(-11,4)
c5=L2*2**sp.Rational(-7,2)
c6=L2*2**sp.Rational(-13,4)
c7=L2*2**sp.Rational(-4)
c9=L2*2**sp.Rational(-9,2)
c10=L2/4
c11=2*L3/(3*sp.sqrt(3))
alphaA=sp.simplify(c1+c5)
alphab=sp.simplify(c1+c5+c11)
kappa=sp.simplify(c1+c5+c9+c10+c11)
beta0=sp.simplify(-c1+c3)
betam=sp.simplify(-c2-c4)
betap=sp.simplify(c2+c6)
betaT=sp.simplify(-c3-c5-c7-c10)
betab=sp.simplify(-c11)

for z in [c1,c2,alphaA,alphab,kappa,betap]:
    assert z.is_positive is True
for z in [beta0,betam,betaT,betab]:
    assert z.is_negative is True

# Lower chamber ordering at eps=Delta/4.
bounds=[
    sp.Integer(0),eps,a-eps,a,a+eps,2*d-eps,T-eps,T,T+eps
]
for lo,hi in zip(bounds,bounds[1:]):
    assert sp.simplify(hi-lo).is_positive is True,(lo,hi)

# Each row entry is (map_name, nonzero coefficient).
rows={
 "R0": [
   ("r_a",c2),("+a",c2),("r_T",beta0),("+T",beta0),
 ],
 "R1": [
   ("r_T",-c1),("+a",c2),
 ],
 "R2": [
   ("r_T",-c1),("r_3a",betam),("+a",betap),("r_a",c2),
 ],
 "R3": [
   ("r_T",-c1),("r_3a",betam),("+a",betap),("-a",c2),
 ],
 "R4I": [
   ("r_T",-c1),("r_3a",betam),("-a",c2),
 ],
 "R5": [
   ("r_T",-c1),("r_3a",betam),("-a",c2),("r_2b",betab),
 ],
 "R6": [
   ("r_T",beta0),("r_3a",betam),("r_4a",betaT),
   ("-a",betap),("r_2b",betab),
 ],
 "R7": [
   ("-T",beta0),("r_3a",betam),("r_4a",betaT),
   ("-a",betap),("r_2b",betab),
 ],
}
row_intervals={
 "R0":(0,eps),
 "R1":(eps,a-eps),
 "R2":(a-eps,a),
 "R3":(a,a+eps),
 "R4I":(a+eps,2*d-eps),
 "R5":(2*d-eps,T-eps),
 "R6":(T-eps,T),
 "R7":(T,T+eps),
}

# Explicitly certify the five-arm tail rows that motivated the adversarial check.
assert [name for name,_ in rows["R6"]]==["r_T","r_3a","r_4a","-a","r_2b"]
assert [name for name,_ in rows["R7"]]==["-T","r_3a","r_4a","-a","r_2b"]
assert all(sp.simplify(c)!=0 for r in rows.values() for _,c in r)

# Collect row intervals by map.
by_map={}
for r,entries in rows.items():
    lo,hi=row_intervals[r]
    for name,c in entries:
        by_map.setdefault(name,[]).append((sp.simplify(lo),sp.simplify(hi)))

def merge(intervals):
    # The canonical rows are already linearly ordered; merge touching pieces.
    ints=sorted(intervals,key=lambda q:float(sp.N(q[0],40)))
    out=[]
    for lo,hi in ints:
        if not out:
            out.append([lo,hi])
            continue
        gap=sp.simplify(lo-out[-1][1])
        assert gap.is_nonnegative is True
        if gap==0:
            out[-1][1]=hi
        else:
            out.append([lo,hi])
    return [(sp.simplify(lo),sp.simplify(hi)) for lo,hi in out]

got={k:merge(v) for k,v in by_map.items()}
expected={
 "+a":[(0,a+eps)],
 "-a":[(a,T0)],
 "+T":[(0,eps)],
 "-T":[(T,T0)],
 "r_a":[(0,eps),(a-eps,a)],
 "r_T":[(0,T)],
 "r_3a":[(a-eps,T0)],
 "r_4a":[(T-eps,T0)],
 "r_2b":[(2*d-eps,T0)],
}
assert set(got)==set(expected)
for name in expected:
    assert len(got[name])==len(expected[name]),(name,got[name],expected[name])
    for (glo,ghi),(elo,ehi) in zip(got[name],expected[name]):
        assert sp.simplify(glo-elo)==0,(name,glo,elo)
        assert sp.simplify(ghi-ehi)==0,(name,ghi,ehi)

# Map formula identities used by A7/A8.
x=sp.symbols("x", real=True)
maps={
 "+a":x+a,
 "-a":x-a,
 "+T":x+T,
 "-T":x-T,
 "r_a":a-x,
 "r_T":T-x,
 "r_3a":3*a-x,
 "r_4a":4*a-x,
 "r_2b":2*b-x,
}
assert set(maps)==set(expected)

# Gate 9: exact P12 restricted-tail hypotheses.
R0=sp.simplify(T/100000)
sigma0=sp.simplify(R0/2)
c=sp.log(5)/2
epsmax=sp.simplify(c-T)

assert R0.is_positive is True
assert sp.simplify(T-R0).is_positive is True
assert sigma0.is_positive is True
assert sp.simplify(R0-sigma0).is_positive is True
assert sp.simplify(eps-sigma0).is_positive is True

# T0<c exactly:
# 4*(2*T0 < log5) is 5 log2 + 2 log3 < 4 log5
# i.e. 2^5 * 3^2 < 5^4.
assert 2**5 * 3**2 < 5**4
# epsilon<epsilon_max is exactly the same T+epsilon<c comparison.
assert sp.simplify((epsmax-eps)-(c-T0))==0

print("A1 off-diagonal map alphabet:",sorted(got))
print("A1 domain unions == A7/A8 nine graphing domains: PASS")
print("R6 five-arm row:",[name for name,_ in rows["R6"]])
print("R7 five-arm row:",[name for name,_ in rows["R7"]])
print("all tail coefficients nonzero: PASS")
print("P12 exact integer horizon test: 2^5*3^2 =",2**5*3**2,"<",5**4,"= 5^4")
print("P12 restricted-tail inequalities sigma0<R0<T and sigma0<epsilon0<epsilon_max: PASS")
print("FIREWALL: reducing-subspace/Mass-Transport are analytic gates")
print("SW1 M1-ND IMG4 GATE1/GATE9 GRAPH/P12 CROSS-CHECK: PASS")
