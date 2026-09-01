#!/usr/bin/env python3
"""Exploratory full-FREE saturation probe for the M1-ND salvage phase diagram.

This is deliberately NOT a certificate.  It numerically saturates the maximal
KNF sampling set R=epsilon under all nine lower-chamber A7 maps, then computes
the exact physical six-branch Hub visibility on the positive annulus.

The probe tests the candidate
    h = (T-10 Delta)/4 = d-3 Delta,
    epsilon_c = h/2,
and the 14 candidate blind gaps
    (c+epsilon, c+h-epsilon)
for c in
    0,D,2D,3D,
    d,d+D,d+2D,
    a,a+D,a+2D,a+3D,
    b,b+D,b+2D.

Numerical agreement is discovery evidence only.  SALVAGE-A1/A2 must replace
this probe by symbolic interval-cell and Hub-exclusion proofs before promotion.
"""

from mpmath import mp

mp.dps=80

L2=mp.log(2)
L3=mp.log(3)
a=L2/2
b=L3/2
T=L2
d=b-a
Delta=L3-mp.mpf(3)/2*L2
h=(T-10*Delta)/4
epscrit=h/2

TOL=mp.mpf("1e-60")

def merge(intervals):
    xs=sorted((l,r) for l,r in intervals if r-l>TOL)
    out=[]
    for l,r in xs:
        if not out or l>out[-1][1]+TOL:
            out.append([l,r])
        elif r>out[-1][1]:
            out[-1][1]=r
    return [(l,r) for l,r in out]

def inter(I,J):
    l=max(I[0],J[0])
    r=min(I[1],J[1])
    return (l,r) if r-l>TOL else None

def image(I,s,c):
    l,r=I
    return (l+c,r+c) if s==1 else (c-r,c-l)

def saturation(eps,maxit=4000):
    T0=T+eps
    domains=[
        ( 1, a, [(0,a+eps)]),
        ( 1,-a, [(a,T0)]),
        ( 1, T, [(0,eps)]),
        ( 1,-T, [(T,T0)]),
        (-1, a, [(0,eps),(a-eps,a)]),
        (-1, T, [(0,T)]),
        (-1,3*a, [(a-eps,T0)]),
        (-1,4*a, [(T-eps,T0)]),
        (-1,2*b, [(2*d-eps,T0)]),
    ]
    V=merge([
        (a-eps,a+eps),
        (b-eps,b+eps),
        (T-eps,T+eps),
    ])
    for it in range(1,maxit+1):
        new=list(V)
        for I in V:
            for s,c,doms in domains:
                for D in doms:
                    K=inter(I,D)
                    if K is None:
                        continue
                    J=inter(image(K,s,c),(mp.mpf("0"),T0))
                    if J is not None:
                        new.append(J)
        V2=merge(new)
        if len(V2)==len(V) and all(
            abs(x-u)<TOL and abs(y-v)<TOL
            for (x,y),(u,v) in zip(V2,V)
        ):
            return V2,it
        V=V2
    raise RuntimeError("saturation did not stabilize")

def hub_visibility(V,eps):
    # Boundary-majorant geometry R=eps; choose sigma=eps/2.
    R=eps
    S=T+eps/2
    ann=(R,S)
    images=[]
    for l,r in V:
        for tau in (a,b,T):
            # |x-tau|, split at tau.
            if l<tau:
                K=(l,min(r,tau))
                if K[1]-K[0]>TOL:
                    Q=inter((tau-K[1],tau-K[0]),ann)
                    if Q is not None:
                        images.append(Q)
            if r>tau:
                K=(max(l,tau),r)
                if K[1]-K[0]>TOL:
                    Q=inter((K[0]-tau,K[1]-tau),ann)
                    if Q is not None:
                        images.append(Q)
            # x+tau.
            Q=inter((l+tau,r+tau),ann)
            if Q is not None:
                images.append(Q)
    return merge(images),ann

def blind_measure(W,ann):
    cur=ann[0]
    total=mp.mpf("0")
    gaps=[]
    for l,r in W:
        if l>cur+TOL:
            gaps.append((cur,l))
            total += l-cur
        cur=max(cur,r)
    if cur<ann[1]-TOL:
        gaps.append((cur,ann[1]))
        total += ann[1]-cur
    return total,gaps

C=[
    0,Delta,2*Delta,3*Delta,
    d,d+Delta,d+2*Delta,
    a,a+Delta,a+2*Delta,a+3*Delta,
    b,b+Delta,b+2*Delta,
]
assert len(C)==14

# Exact constant identities, checked numerically at 80 digits.
assert abs(h-(d-3*Delta)) < TOL
assert abs(h-(a-(d+2*Delta))) < TOL
assert abs(h-(b-(a+3*Delta))) < TOL
assert abs(h-(T-(b+2*Delta))) < TOL

print("SW1 M1-ND SALVAGE PHASE-DIAGRAM PROBE")
print("Delta =",mp.nstr(Delta,30))
print("h =",mp.nstr(h,30))
print("epsilon_c/Delta =",mp.nstr(epscrit/Delta,30))

for frac in ("0.05","0.10","0.15","0.18","0.20","0.22"):
    eps=mp.mpf(frac)*Delta
    assert eps<epscrit
    V,it=saturation(eps)
    W,ann=hub_visibility(V,eps)
    beta,gaps=blind_measure(W,ann)

    g=h-2*eps
    assert g>0
    cand=[(c+eps,c+h-eps) for c in C]

    # Candidate gaps must lie in (eps,T) and be pairwise separated.
    for l,r in cand:
        assert l>=eps-TOL and r<=T+TOL and r-l>0

    # Numerical disjointness from actual visible union.
    for B in cand:
        for J in W:
            assert inter(B,J) is None

    lower=14*g
    assert beta+mp.mpf("1e-50") >= lower

    print(
        "eps/Delta=",frac,
        "iters=",it,
        "Vcells=",len(V),
        "Wcells=",len(W),
        "beta=",mp.nstr(beta,18),
        "14g=",mp.nstr(lower,18),
    )

# Just above the candidate threshold the majorant scan reaches full support.
eps=mp.mpf("0.23")*Delta
assert eps>epscrit
V,it=saturation(eps)
W,ann=hub_visibility(V,eps)
beta,_=blind_measure(W,ann)
print("eps/Delta=0.23 exploratory beta =",mp.nstr(beta,18))
assert abs(beta) < mp.mpf("1e-50")

print("DISCOVERY: 14-gap candidate survives every tested epsilon<epsilon_c")
print("DISCOVERY: boundary-majorant visibility is full at epsilon=0.23 Delta")
print("FIREWALL: numerical probe only; no SALVAGE-A1/A2 theorem")
