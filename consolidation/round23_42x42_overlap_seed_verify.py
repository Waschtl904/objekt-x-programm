#!/usr/bin/env python3
import math, random
from fractions import Fraction
import sympy as sp

# P12 Round 23 -- exact 42x42 overlap-seed verifier.
# Reconstructs all rows from the canonical six raw slots.

a0=.5*math.log(2)
b0=.5*math.log(3)
T0=2*a0
d0=b0-a0
e0=T0-b0
delta0=d0-e0
epsmax0=.5*math.log(5/4)
rho0=epsmax0-delta0
omega0=e0/2-rho0
eta0=e0-2*delta0
chi0=3*delta0-e0
kappa0=e0-delta0

p,q,r=sp.symbols("p q r", positive=True, nonzero=True)
Ashift=(0,2,1)
Bshift=(0,3,2)
Tshift=(0,4,2)
shifts=[(Ashift,p),(Bshift,r),(Tshift,q)]

sources=[
(-1,0,1),(-1,0,2),
(-1,1,0),(-1,1,1),(-1,1,2),(-1,1,3),
(-1,2,0),(-1,2,1),(-1,2,2),(-1,2,3),(-1,2,4),
(-1,3,0),(-1,3,1),(-1,3,2),(-1,3,3),(-1,3,4),
(-1,4,0),(-1,4,1),(-1,4,2),(-1,4,3),
(-1,5,1),
(1,0,0),(1,0,1),
(1,1,-1),(1,1,0),(1,1,1),(1,1,2),
(1,2,-1),(1,2,0),(1,2,1),(1,2,2),(1,2,3),
(1,3,-1),(1,3,0),(1,3,1),(1,3,2),(1,3,3),
(1,4,-1),(1,4,0),(1,4,1),(1,4,2),
(1,5,0)
]
assert len(sources)==42 and len(set(sources))==42

def add(u,v): return tuple(u[i]+v[i] for i in range(3))
def neg(u): return tuple(-z for z in u)
def aval(u,x): return u[0]*x+u[1]*e0+u[2]*delta0

def raw_row(src,x,R,sigma,eps):
    u=aval(src,x)
    if not (0<u<T0+eps):
        return None
    row={}
    for sh,k in shifts:
        for pm,sgn in [(-1,+1),(+1,-1)]:
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            coeff=sgn*k
            av=aval(arg,x)
            if av<0:
                arg=neg(arg)
                av=-av
                coeff=-coeff
            if R<av<T0+sigma:
                row[arg]=sp.expand(row.get(arg,0)+coeff)
    return {aa:sp.factor(c) for aa,c in row.items()
            if sp.simplify(c)!=0}

def pattern(src,x,R,sigma,eps):
    rr=raw_row(src,x,R,sigma,eps)
    if rr is None: return None
    return tuple(sorted(rr.keys()))

def pattern_fast(src,x,R,sigma,eps):
    u=aval(src,x)
    if not (0<u<T0+eps):
        return None
    out=[]
    for sh in (Ashift,Bshift,Tshift):
        for pm in (-1,+1):
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            av=aval(arg,x)
            if av<0:
                arg=neg(arg)
                av=-av
            if R<av<T0+sigma:
                out.append(arg)
    return tuple(sorted(out))

# Exact constant identities used to name the new walls.
assert abs(omega0-.25*math.log(27/25))<1e-14
assert abs(eta0-.5*math.log(256/243))<1e-14
assert abs(chi0-.5*math.log(2187/2048))<1e-14
assert abs(kappa0-.5*math.log(32/27))<1e-14
assert omega0<eta0<chi0<rho0
print("CONSTANTS = PASS",{
    "omega":omega0,"eta":eta0,"chi":chi0,"rho":rho0
})

# Interior reference point.
R=.020
x=.030
sigma=.040
eps=.060
assert omega0<R<x<sigma<eps<epsmax0
assert eta0<x<chi0
assert R+x<delta0<sigma+x<kappa0
assert sigma-x<eta0
assert kappa0<eps+x
assert x+eta0<eps

rows=[raw_row(s,x,R,sigma,eps) for s in sources]
assert all(rr is not None for rr in rows)
variables=sorted(set().union(*(set(rr) for rr in rows)))
assert len(variables)==42
M=sp.Matrix([[rr.get(v,0) for v in variables] for rr in rows])
assert M.shape==(42,42)

detM=sp.factor(M.det(method="domain-ge"))
fac=sp.factor_list(detM)
assert fac[0]==-1
# Remove the obvious p^14 r^4 and normalize the two degree-12 factors.
rest=sp.factor(detM/(-p**14*r**4))
rest_factors=sp.factor_list(rest)[1]
assert len(rest_factors)==2 and all(exp==1 for _,exp in rest_factors)
F1,F2=[f for f,exp in rest_factors]

beta,v=sp.symbols("beta v", positive=True)

Aexpr=(
3*beta**12-beta**10*v-18*beta**10-7*beta**8*v+45*beta**8
-beta**6*v**3-3*beta**6*v**2+38*beta**6*v-60*beta**6
-beta**4*v**3+21*beta**4*v**2-62*beta**4*v+45*beta**4
+8*beta**2*v**3-33*beta**2*v**2+43*beta**2*v-18*beta**2
+2*v**4-9*v**3+15*v**2-11*v+3
)
Cexpr=2*beta**3*v**2*(beta**2-1)*(2*beta**2+v-2)

def normalize_F(F):
    P=sp.Poly(sp.expand(F),p,q,r)
    out=0
    for (ep,eq,er),coef in P.terms():
        assert ep+eq+er==12
        assert er%2==0
        out += coef*beta**eq*v**(er//2)
    return sp.expand(out)

N1=normalize_F(F1)
N2=normalize_F(F2)
assert (
    (sp.simplify(N1-(Aexpr-Cexpr))==0 and sp.simplify(N2-(Aexpr+Cexpr))==0)
    or
    (sp.simplify(N2-(Aexpr-Cexpr))==0 and sp.simplify(N1-(Aexpr+Cexpr))==0)
)
print("DET42_FACTOR = PASS")
print("det(M42) =",detM)

# ---------- exact rational interval arithmetic ----------

def ln_bounds_int(xint,N):
    # ln x = 2 sum z^(2k+1)/(2k+1), z=(x-1)/(x+1), all terms positive.
    z=Fraction(xint-1,xint+1)
    s=Fraction(0)
    for k in range(N+1):
        s += z**(2*k+1)/Fraction(2*k+1)
    lo=2*s
    tail=2*z**(2*N+3)/Fraction(2*N+3)/(1-z*z)
    return lo,lo+tail

l2lo,l2hi=ln_bounds_int(2,40)
l3lo,l3hi=ln_bounds_int(3,60)

# beta=2^(-3/4), so beta^4=1/8.
blo=Fraction("0.59460355750136053335")
bhi=Fraction("0.59460355750136053336")
assert blo**4 < Fraction(1,8) < bhi**4

# sqrt(8/27)
slo=Fraction("0.54433105395181735515")
shi=Fraction("0.54433105395181735516")
assert slo*slo < Fraction(8,27) < shi*shi

# v=(ln3/ln2)*sqrt(8/27)
vlo=(l3lo/l2hi)*slo
vhi=(l3hi/l2lo)*shi

def poly_interval(expr):
    P=sp.Poly(sp.expand(expr),beta,v)
    lo=Fraction(0); hi=Fraction(0)
    for (eb,ev),coef in P.terms():
        coef=int(coef)
        ml=(blo**eb)*(vlo**ev)
        mh=(bhi**eb)*(vhi**ev)
        if coef>=0:
            lo += coef*ml
            hi += coef*mh
        else:
            lo += coef*mh
            hi += coef*ml
    return lo,hi

im=poly_interval(Aexpr-Cexpr)
ip=poly_interval(Aexpr+Cexpr)
assert im[1] < 0
assert ip[1] < 0
print("EXACT_INTERVAL_A_MINUS_C = PASS",float(im[0]),float(im[1]))
print("EXACT_INTERVAL_A_PLUS_C  = PASS",float(ip[0]),float(ip[1]))

# ---------- whole-cell pattern stress ----------

ref=[pattern_fast(s,x,R,sigma,eps) for s in sources]

def in_cell(R,sigma,eps,x):
    return (
        omega0<R<x<sigma<eps<epsmax0
        and eta0<x<chi0
        and R+x<delta0
        and delta0<sigma+x<kappa0
        and sigma-x<eta0
        and kappa0<eps+x
        and x+eta0<eps
    )

random.seed(230023)
n=0
attempts=0
while n<50000 and attempts<1200000:
    attempts+=1
    RR=random.uniform(omega0+1e-9,chi0-1e-9)
    xxlo=max(RR,eta0)+1e-9
    xxhi=chi0-1e-9
    if xxlo>=xxhi: continue
    xx=random.uniform(xxlo,xxhi)

    sslo=max(xx,delta0-xx)+1e-9
    sshi=min(kappa0-xx,xx+eta0,epsmax0-2e-9)
    if sslo>=sshi: continue
    ss=random.uniform(sslo,sshi)

    eelo=max(ss,kappa0-xx,xx+eta0)+1e-9
    eehi=epsmax0-1e-9
    if eelo>=eehi: continue
    ee=random.uniform(eelo,eehi)

    if not in_cell(RR,ss,ee,xx): continue
    got=[pattern_fast(s,xx,RR,ss,ee) for s in sources]
    assert got==ref,(RR,ss,ee,xx)
    n+=1

assert n==50000
print("WHOLE_CELL_PATTERN_STRESS = PASS",n)
print("ROUND23_42X42_OVERLAP_SEED_VERIFY = PASS")
