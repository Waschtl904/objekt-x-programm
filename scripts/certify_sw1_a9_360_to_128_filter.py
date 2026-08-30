#!/usr/bin/env python3
"""A9 exact 360->128 staggered cross-filter certificate. Filter ledger only."""
from fractions import Fraction as F
from collections import Counter
def V(c=0,g=0,s=0):return(F(c),F(g),F(s))
def A(x,y):return tuple(a+b for a,b in zip(x,y))
def D(x,y):return tuple(a-b for a,b in zip(x,y))
def M(q,x):return tuple(F(q)*a for a in x)
G=V(g=1);S=V(s=1);L=A(V(c=4),M(2,G))
N=lambda e:0 if e==0 else-2
Z={0:[("P",0),("P",1),("P",2),("Q",0),("Q",1)],1:[("P",0),("P",1),("P",2),("Q",0),("Q",1)],2:[("P",0),("P",1),("Q",0),("Q",1),("Q",2)],3:[("P",0),("P",1),("Q",0),("Q",1),("Q",2)]}
Lft={0:{("P",1),("P",2),("Q",0),("Q",1)},1:{("P",2),("Q",0),("Q",1)},2:{("Q",0),("Q",1)},3:{("Q",0)}}
Rgt={0:{("P",0)},1:{("P",0),("P",1)},2:{("P",0),("P",1),("Q",2)},3:{("P",0),("P",1),("Q",1),("Q",2)}}
def side(n,e,h,k):
 j=n-N(e)
 if j<=-1:return"L"
 if j>=4:return"R"
 return"L" if(h,k)in Lft[j]else"R"
def phy(n,e,h,k):
 j=n-N(e);b=S if e==0 else A(S,G)
 r=A(b,V(c=j))if h=="P"else D(V(c=4-j),b)
 return A(r,M(k,L))
Q=[]
for e in(0,1):
 for j in range(4):
  n=N(e)+j
  for h,k in Z[j]:Q.append((e,n,h,k,phy(n,e,h,k),side(n,e,h,k)))
assert len(Q)==40
J={"+e":{"P":("P",0),"Q":("Q",0)},"-e":{"P":("P",0),"Q":("Q",0)},"+d":{"P":("P",1),"Q":("Q",-1)},"-d":{"P":("P",-1),"Q":("Q",1)},"+b":{"P":("P",2),"Q":("Q",-2)},"-b":{"P":("P",-2),"Q":("Q",2)},"ab":{"P":("Q",1),"Q":("P",-1)},"Tb":{"P":("Q",0),"Q":("P",0)},"b":{"P":("Q",2),"Q":("P",-2)}}
e=M(F(1,2),L);d=A(e,V(c=1));b=A(M(F(3,2),L),V(c=2));a=A(L,V(c=1));T=A(M(2,L),V(c=2))
def f(n,x):
 return{"+e":A(x,e),"-e":D(x,e),"+d":A(x,d),"-d":D(x,d),"+b":A(x,b),"-b":D(x,b),"ab":D(A(a,b),x),"Tb":D(A(T,b),x),"b":D(b,x)}[n]
C=Counter()
for eta,n,h,k,x,s in Q:
 for name in J:
  C["raw"]+=1;hh,j=J[name][h];m=n+j;ee=1-eta;y=f(name,x);q=m-N(ee)
  if q<=-1 or q>=4:
   C["outside"]+=1;t="L"if q<=-1 else"R";C["out_cross"if t!=s else"out_same"]+=1
  else:
   C["middle"]+=1;z=[(u,v)for u,v in Z[q]if u==hh and phy(m,ee,u,v)==y]
   if not z:C["unmatched"]+=1
   else:
    assert len(z)==1;C["matched"]+=1;t=side(m,ee,*z[0]);C["mid_cross"if t!=s else"mid_same"]+=1
assert C==Counter(raw=360,outside=180,middle=180,out_same=118,out_cross=62,matched=102,unmatched=78,mid_cross=66,mid_same=36)
assert C["out_cross"]+C["mid_cross"]==128
print("SW1-A9 360-TO-128 FILTER CERTIFICATE: PASS")
print("360 raw = 180 outside-target + 180 middle-target")
print("outside: 62 cross + 118 same-side")
print("middle: 102 matched = 66 cross + 36 same-side; 78 unmatched")
print("complete directed cross ledger: 62+66=128")
