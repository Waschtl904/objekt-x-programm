#!/usr/bin/env python3
"""SW1-A10-C1B2B exact chamber-representative / boundary-order ledger.

At the exact rational reference ratio r0=s*/chi=7/2:
- verify 64 rational interior representatives with 64 distinct sign patterns
  for the 18 genuine collision hyperplanes;
- by C1B2A, the total chamber count at r0 is exactly 64, hence the list is exhaustive;
- reconstruct the complete 92 C1B0 boundary signatures;
- sort all 92 circle boundaries exactly in every chamber representative;
- verify all 64 circular orders are distinct.

Firewall: reference-arrangement order ledger only. Transfer of these labeled
orders to the actual project ratio uses the separate no-degeneracy isotopy
step from C1B2A. No final physical fiber N or operator matrix claim.
"""
from fractions import Fraction as F
from itertools import combinations
import hashlib

r0=F(7,2)
E0=(r0+1)/2
# normalized by chi: Delta=1+2r, L=4+10r
D0=1+2*r0
L0=4+10*r0
assert (D0,L0,E0)==(F(8),F(39),F(9,4))

PLANES=[
((0,2,0),r0),((0,1,1),r0),((1,1,0),r0),((0,0,2),r0),((1,0,1),r0),((2,0,0),r0),
((0,-1,1),1),((1,0,0),1),((2,0,0),1),((-1,0,1),1),((0,0,1),1),((1,0,1),1),
((0,0,2),1),((-1,1,0),1),((0,1,0),1),((1,1,0),1),((0,1,1),1),((0,2,0),1)]

REPS=[
('------------------',('1/7','2/7','3/7')),
('------------+-----',('1/7','2/7','4/7')),
('------------+---+-',('1/7','3/7','5/7')),
('------------+---++',('1/7','4/7','5/7')),
('-----------++---+-',('2/7','3/7','6/7')),
('-----------++---++',('2/7','4/7','6/7')),
('-----------++--+++',('3/7','5/7','6/7')),
('----------+++---+-',('2/7','3/7','8/7')),
('----------+++---++',('2/7','4/7','8/7')),
('----------+++--+++',('2/5','4/5','6/5')),
('----------+++-++++',('3/7','8/7','9/7')),
('---------++++---+-',('1/7','3/7','9/7')),
('---------++++---++',('1/5','3/5','7/5')),
('---------++++--+++',('2/5','4/5','8/5')),
('---------++++-++++',('2/5','6/5','33/20')),
('---------+++++++++',('3/14','10/7','23/14')),
('--------+--++--+++',('4/7','5/7','6/7')),
('--------+-+++--+++',('3/5','4/5','6/5')),
('--------+-+++-++++',('3/4','5/4','3/2')),
('--------+++++--+++',('9/16','13/16','27/16')),
('--------+++++-++++',('9/16','9/8','27/16')),
('--------++++++++++',('13/24','13/8','41/24')),
('-------++-+++-++++',('17/14','10/7','23/14')),
('------+--++++---+-',('1/5','2/5','33/20')),
('------+--++++---++',('1/8','9/16','27/16')),
('------+--++++--+++',('11/24','5/8','41/24')),
('------+-+++++--+++',('13/24','5/8','41/24')),
('---+-----++++---++',('1/14','6/7','25/14')),
('---+-----++++--+++',('9/20','9/10','9/5')),
('---+-----++++-++++',('2/5','6/5','37/20')),
('---+-----+++++++++',('3/14','10/7','13/7')),
('---+----+-+++--+++',('6/7','13/14','25/14')),
('---+----+-+++-++++',('9/10','11/10','9/5')),
('---+----+++++--+++',('11/20','9/10','9/5')),
('---+----+++++-++++',('9/14','9/7','27/14')),
('---+----++++++++++',('13/24','13/8','43/24')),
('---+---++-+++-++++',('17/14','10/7','13/7')),
('---+---++++++-++++',('13/12','5/4','13/6')),
('---+--+--++++---+-',('1/5','2/5','37/20')),
('---+--+--++++---++',('1/5','3/5','37/20')),
('---+--+--++++--+++',('2/5','4/5','2/1')),
('---+--+--++++-++++',('11/24','13/12','13/6')),
('---+--+--+++++++++',('1/16','9/8','35/16')),
('---+--+-+++++--+++',('3/5','4/5','41/20')),
('---+--+-+++++-++++',('11/12','13/12','13/6')),
('---+--+++++++-++++',('17/16','9/8','35/16')),
('-+-+-----++++-++++',('13/28','39/28','61/28')),
('-+-+-----+++++++++',('2/5','33/20','41/20')),
('-+-+----+-+++-++++',('13/14','12/7','13/7')),
('-+-+----+++++-++++',('13/16','13/8','33/16')),
('-+-+----++++++++++',('9/16','27/16','17/8')),
('-+-+---++-+++-++++',('5/4','33/20','41/20')),
('-+-+---++++++-++++',('13/12','17/12','13/6')),
('-+-++--++-+++-++++',('43/28','47/28','59/28')),
('++-+-----+++++++++',('2/5','37/20','41/20')),
('++-+----+-+++-++++',('13/14','25/14','13/7')),
('++-+----+++++-++++',('9/10','9/5','2/1')),
('++-+----++++++++++',('3/5','37/20','41/20')),
('++-+---++-+++-++++',('5/4','37/20','41/20')),
('++-+---++++++-++++',('13/12','43/24','13/6')),
('++-+---+++++++++++',('17/16','17/8','35/16')),
('++-++--++-+++-++++',('43/28','51/28','59/28')),
('+++++--++-+++-++++',('47/28','55/28','59/28')),
('++++++-++-+++-++++',('51/28','55/28','59/28')),
 ]
assert len(REPS)==64

def parse(q): return F(q)
patterns=[]; reps=[]
for pat,vals in REPS:
    x=tuple(parse(v) for v in vals)
    s,R,e=x
    assert 0<s<R<e<E0
    signs=[]
    for a,c in PLANES:
        z=sum(F(ai)*xi for ai,xi in zip(a,x))-F(c)
        assert z!=0
        signs.append('+' if z>0 else '-')
    assert ''.join(signs)==pat
    patterns.append(pat); reps.append(x)
assert len(set(patterns))==64

# Rebuild the exact C1B0 boundary signature set.
def V(L=0,D=0,R=0,E=0,S=0): return (F(L),F(D),F(R),F(E),F(S))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
zero=V(); ee=V(F(1,2),0); d=V(F(1,2),1); a=V(1,1); b=V(F(3,2),2); T=V(2,2); twod=V(1,2)
Bf={zero,V(E=1),sub(a,V(E=1)),add(a,V(E=1)),sub(twod,V(E=1)),sub(T,V(E=1)),V(S=1),add(ee,V(S=1)),add(a,V(S=1)),sub(a,V(R=1)),add(a,V(R=1)),sub(b,V(R=1)),add(b,V(R=1)),sub(T,V(R=1)),add(T,V(R=1)),a,b,T,add(T,V(E=1))}
Bw={V(R=1),V(E=1),add(ee,V(E=1)),d,add(d,V(R=1)),a,add(a,V(R=1)),add(a,V(E=1)),b,sub(T,V(R=1)),T,add(T,V(S=1))}
C=[[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1),(1,3,2),(1,4,2)],[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1),(1,3,2)],[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1)],[(-1,2,1),(-1,4,2),(-1,4,3),(-1,5,3),(1,1,0),(1,2,1),(1,3,1)],[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1)],[(-1,3,2),(-1,5,3),(-1,6,3),(1,-2,-1),(1,0,0),(1,1,1),(1,2,1)],[(-1,3,2),(-1,4,2),(1,-2,-1),(1,2,1)],[(-1,3,2),(-1,4,2),(1,-2,-1)],[(-1,4,2),(1,-3,-2),(1,-2,-1)],[(-1,4,2),(-1,6,3),(-1,7,4),(-1,8,4),(1,-3,-2),(1,-1,0),(1,0,0)],[(1,-4,-2),(1,-3,-2),(1,-2,-1)]]
sig=set(q for cell in C for q in cell)
def rel(x,y):
    s,l,k=x; t,m,j=y
    if s==t:
        lam=F(m-l,2); dk=j-k
        if lam<0 or (lam==0 and dk<0): lam=-lam; dk=-dk
        return ('T',lam,dk)
    return ('R',F(l+m,2),k+j)
master={rel(x,y) for cell in C for x,y in combinations(cell,2)}
def cv(lam,k): return V(L=lam,D=k)
Braw=set(Bf|Bw)
for typ,lam,k in master:
    cc0=cv(lam,k)
    if typ=='T':
        for dr in (-1,1):
            cc=tuple(dr*z for z in cc0)
            for wall in Bf: Braw.add(sub(wall,cc))
    else:
        for wall in Bf: Braw.add(sub(cc0,wall))
for orient,twolam,k in sig:
    cc=cv(F(twolam,2),k)
    for wall in Bf:
        z=sub(wall,cc)
        if orient==-1: z=neg(z)
        Braw.add(z)
def floorf(q): return q.numerator//q.denominator
def modL(x):
    n=F(floorf(x[0])); return (x[0]-n,)+x[1:]
Bmod=sorted({modL(x) for x in Braw})
assert len(Bmod)==92

def value(sig,rep):
    l,k,rho,mu,nu=sig; s,R,e=rep
    z=l*L0+k*D0+rho*R+mu*e+nu*s
    n=z//L0
    return z-n*L0

orders=[]
for rep in reps:
    vals=[value(sig,rep) for sig in Bmod]
    assert len(set(vals))==92
    order=tuple(sorted(range(92),key=lambda i:vals[i]))
    orders.append(order)
assert len(set(orders))==64

payload='\n'.join(patterns[i]+':' + ','.join(map(str,orders[i])) for i in range(64)).encode()
digest=hashlib.sha256(payload).hexdigest()
assert digest=='d1a9767f147b405980d8f9989752a5b90f1fa0bc78ef0a73de2878248d928ba2'

print('SW1-A10-C1B2B CHAMBER-ORDER LEDGER CERTIFICATE: PASS')
print('64 exact rational representatives; 64 distinct 18-plane sign patterns')
print('C1B2A total count=64 therefore representative list is exhaustive at r0=7/2')
print('92 exact boundary values are pairwise distinct in every representative')
print('64 distinct complete circular boundary orders')
print('order-ledger SHA256:',digest)
print('FIREWALL: exact reference-order ledger only; actual-r transfer uses C1B2A no-degeneracy isotopy')
