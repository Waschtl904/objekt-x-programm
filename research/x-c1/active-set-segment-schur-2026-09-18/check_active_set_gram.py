#!/usr/bin/env python3
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path


def padd(p,q):
    n=max(len(p),len(q)); return [(p[i] if i<len(p) else F(0))+(q[i] if i<len(q) else F(0)) for i in range(n)]

def pmul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return r

def pshift(p,c):
    # p(x+c)
    from math import comb
    r=[F(0)]*len(p)
    for n,a in enumerate(p):
        for k in range(n+1): r[k]+=a*F(comb(n,k))*c**(n-k)
    return r

def pint(p,lo,hi):
    return sum((a*(hi**(k+1)-lo**(k+1))/F(k+1) for k,a in enumerate(p)),F(0))

def leg(n):
    if n==0:return [F(1)]
    if n==1:return [F(0),F(1)]
    a=[F(0)]+[F(2*n-1,n)*x for x in leg(n-1)]
    b=[-F(n-1,n)*x for x in leg(n-2)]
    return padd(a,b)

def band(sign,d):
    return (F(-1),F(1)-d) if sign==1 else (F(-1)+d,F(1))

def intersect(a,b):
    lo=max(a[0],b[0]); hi=min(a[1],b[1]); return None if lo>=hi else (lo,hi)

def shift_entry(i,j,d):
    out=F(0)
    for s in (1,-1):
        lo,hi=band(s,d)
        out += pint(pmul(leg(i),pshift(leg(j),s*d)),lo,hi)/2
    return out

def cross_entry(i,j,d,e):
    out=F(0)
    for s in (1,-1):
        for t in (1,-1):
            iv=intersect(band(s,d),band(t,e))
            if iv is None: continue
            out += pint(pmul(pshift(leg(i),s*d),pshift(leg(j),t*e)),iv[0],iv[1])/2
    return out

def tpoly(i,j):
    # historical one-shift formula, valid for all 0<d<2 with u=2-d
    r=[F(0)]*(i+j+2)
    for k in range(i+1):
        ai=F((-1)**(i+k)*factorial(i+k),2**k*factorial(k)**2*factorial(i-k))
        for l in range(j+1):
            aj=F((-1)**(j+l)*factorial(j+l),2**l*factorial(l)**2*factorial(j-l))
            r[k+l+1]+=(-1)**j*ai*aj*F(factorial(k)*factorial(l),factorial(k+l+1))
    return r

def peval(p,x):
    v=F(0)
    for a in reversed(p):v=v*x+a
    return v

checks=[]
def ok(name,c):
    if not c: raise AssertionError(name)
    checks.append(name)

# Cover overlapping and disjoint-band regimes.
for d in (F(1,3),F(4,5),F(6,5),F(9,5)):
    for parity in (0,1):
        inds=list(range(parity,8,2))
        for i in inds:
            for j in inds:
                ok(f'shift generic=tpoly d={d} parity={parity} i={i} j={j}', shift_entry(i,j,d)==peval(tpoly(i,j),2-d))

# Self-adjointness and mixed-Gram symmetry for arbitrary shift pairs.
for d,e in ((F(1,3),F(7,5)),(F(4,5),F(6,5)),(F(9,10),F(17,10))):
    for i in range(6):
        for j in range(6):
            ok(f'shift selfadj d={d} {i},{j}',shift_entry(i,j,d)==shift_entry(j,i,d))
            ok(f'cross symmetry d={d} e={e} {i},{j}',cross_entry(i,j,d,e)==cross_entry(j,i,e,d))

# Exact parity-block d=0 limit: T_0=2I.
for parity in (0,1):
    inds=list(range(parity,8,2))
    for i in inds:
        for j in inds:
            expected=F(2,2*i+1) if i==j else F(0)
            ok(f'd0 limit parity={parity} {i},{j}', peval(tpoly(i,j),F(2))==expected)

# Positive semidefiniteness of a nontrivial two-shift Gram on a finite test family.
# Gram_ij=<S P_i,S P_j> with S=T_d+2T_e; exact rational band integrals.
d,e=F(4,5),F(7,5)
G=[[cross_entry(i,j,d,d)+2*cross_entry(i,j,d,e)+2*cross_entry(i,j,e,d)+4*cross_entry(i,j,e,e) for j in range(5)] for i in range(5)]
# exact LDL semidefinite/definite check on this independent polynomial family
L=[[F(0) for _ in range(5)] for _ in range(5)]; D=[]
for i in range(5):
    L[i][i]=1
    piv=G[i][i]-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
    ok(f'test Gram pivot {i} positive',piv>0); D.append(piv)
    for j in range(i+1,5):
        L[j][i]=(G[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/piv

res={'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN','checks':len(checks),'tested_shift_regimes':['d<1 overlapping','d>1 disjoint'],'test_gram_pivots':[str(x) for x in D]}
Path('active_set_gram_results.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print('PASS 128 same-parity generic shift identities across d<1 and d>1')
print('PASS 216 self-adjointness and mixed-shift Gram symmetry identities')
print('PASS 32 exact parity-block d=0 limits')
print('PASS 5 exact positive LDL pivots for nontrivial two-shift Gram')
print('TOTAL',len(checks))
