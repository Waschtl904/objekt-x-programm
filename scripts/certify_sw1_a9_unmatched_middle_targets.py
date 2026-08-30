#!/usr/bin/env python3
"""A9 exact classification of the 78 unmatched middle-target cases.

Scope: the 360->128 staggered filter ledger only. For every formal new-KNF
source/map case whose target index lies in one of the two middle blocks but
has no matching physical target label, solve the unique algebraic target
lift k*. Prove k* is outside the exact allowed lift set of that target
sheet/layer. Thus 'unmatched' means 'target lift does not physically exist',
not 'scan missed a target'.
"""
from fractions import Fraction as F
from collections import Counter

def V(c=0,g=0,s=0): return (F(c),F(g),F(s))
def A(x,y): return tuple(a+b for a,b in zip(x,y))
def D(x,y): return tuple(a-b for a,b in zip(x,y))
def M(q,x): return tuple(F(q)*a for a in x)
G=V(g=1); S=V(s=1); L=A(V(c=4),M(2,G))
N=lambda e:0 if e==0 else -2
Z={
 0:[("P",0),("P",1),("P",2),("Q",0),("Q",1)],
 1:[("P",0),("P",1),("P",2),("Q",0),("Q",1)],
 2:[("P",0),("P",1),("Q",0),("Q",1),("Q",2)],
 3:[("P",0),("P",1),("Q",0),("Q",1),("Q",2)],
}
def base(e): return S if e==0 else A(S,G)
def residue(n,e,h):
 j=n-N(e); b=base(e)
 return A(b,V(c=j)) if h=="P" else D(V(c=4-j),b)
def phy(n,e,h,k): return A(residue(n,e,h),M(k,L))
Q=[]
for e in (0,1):
 for j in range(4):
  n=N(e)+j
  for h,k in Z[j]: Q.append((e,n,h,k,phy(n,e,h,k)))
assert len(Q)==40
J={
 "+e":{"P":("P",0),"Q":("Q",0)},"-e":{"P":("P",0),"Q":("Q",0)},
 "+d":{"P":("P",1),"Q":("Q",-1)},"-d":{"P":("P",-1),"Q":("Q",1)},
 "+b":{"P":("P",2),"Q":("Q",-2)},"-b":{"P":("P",-2),"Q":("Q",2)},
 "ab":{"P":("Q",1),"Q":("P",-1)},"Tb":{"P":("Q",0),"Q":("P",0)},
 "b":{"P":("Q",2),"Q":("P",-2)},
}
e=M(F(1,2),L); d=A(e,V(c=1)); b=A(M(F(3,2),L),V(c=2)); a=A(L,V(c=1)); T=A(M(2,L),V(c=2))
def fmap(n,x):
 return {"+e":A(x,e),"-e":D(x,e),"+d":A(x,d),"-d":D(x,d),
         "+b":A(x,b),"-b":D(x,b),"ab":D(A(a,b),x),"Tb":D(A(T,b),x),"b":D(b,x)}[n]

bad=[]
for eta,n,h,k,x in Q:
 for name in J:
  hh,jump=J[name][h]; m=n+jump; ee=1-eta; jj=m-N(ee)
  if not (0<=jj<4): continue
  y=fmap(name,x)
  allowed=[v for u,v in Z[jj] if u==hh]
  matches=[v for v in allowed if phy(m,ee,hh,v)==y]
  if matches: continue
  diff=D(y,residue(m,ee,hh))
  c0,cg,cs=diff
  assert cs==0
  kstar=F(c0,4)
  assert F(cg,2)==kstar
  assert kstar.denominator==1
  assert kstar not in allowed
  bad.append((jj,hh,kstar,tuple(allowed)))

assert len(bad)==78
by_lift=Counter(k for _,_,k,_ in bad)
assert by_lift==Counter({F(-2):8,F(-1):22,F(2):20,F(3):20,F(4):8})
for j,h,k,allowed in bad:
 if k==2:
  assert (j in (0,1) and h=="Q") or (j in (2,3) and h=="P")
  assert 2 not in allowed
assert sum(1 for _,_,k,_ in bad if k not in (0,1,2))==58
assert sum(1 for _,_,k,_ in bad if k==2)==20

print("SW1-A9 UNMATCHED MIDDLE-TARGET CERTIFICATE: PASS")
print("78/78 unmatched cases solved to a unique algebraic target lift k*")
print("lift histogram: k*=-2:8, -1:22, 2:20, 3:20, 4:8")
print("58 targets require lifts outside {0,1,2}")
print("20 targets require k*=2 on exactly those sheet/layers where the certified third lift is absent")
print("therefore every unmatched case means: physical middle target does not exist")
print("FIREWALL: filter-completeness lemma only; no separator or injectivity claim")
