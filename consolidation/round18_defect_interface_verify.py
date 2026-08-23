import math, random
import sympy as sp

# P12 Runde 18 -- low-radius defect-interface verifier.
# Reconstructs all rows from the canonical six raw slots.

a0=math.log(2)/2
b0=math.log(3)/2
T0=2*a0
d0=b0-a0
e0=T0-b0
delta0=d0-e0
epsmax0=.5*math.log(5/4)
rho0=epsmax0-delta0
eta0=e0-2*delta0
kappa0=e0-delta0

p,q,r=sp.symbols("p q r", positive=True, nonzero=True)
Delta=p**2-q**2
Psi=Delta**2-p**2*r**2
Fpoly=2*p**4-3*p**2*q**2-p**2*r**2+q**4-q**2*r**2

A=(0,2,1)
B=(0,3,2)
TT=(0,4,2)
shifts=[(A,p),(B,r),(TT,q)]

def add(u,v): return tuple(u[i]+v[i] for i in range(3))
def neg(u): return tuple(-z for z in u)
def aval(u,x): return u[0]*x+u[1]*e0+u[2]*delta0

old19=[
(-1,3,2),(1,3,2),(-1,2,1),(-1,4,2),(1,4,2),(1,3,1),
(-1,1,0),(-1,3,1),(1,1,1),(1,3,3),(1,2,2),(-1,2,0),
(-1,4,1),(1,0,1),(-1,5,2),(1,1,2),(1,2,3),(-1,4,0),(-1,5,1)
]
base18=old19[:14]+old19[15:]
u15=old19[14]

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
                arg=neg(arg); av=-av; coeff=-coeff
            if R<av<T0+sigma:
                row[arg]=sp.expand(row.get(arg,0)+coeff)
    return {a:sp.factor(c) for a,c in row.items() if sp.simplify(c)!=0}

def patt(src,x,R,sigma,eps):
    u=aval(src,x)
    if not (0<u<T0+eps): return None
    out=[]
    for sh in (A,B,TT):
        for pm in (-1,+1):
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            av=aval(arg,x)
            if av<0:
                arg=neg(arg); av=-av
            if R<av<T0+sigma:
                out.append(arg)
    return tuple(sorted(out))

# Representative soft-cell point.
R=.055
sigma=.065
eps=.100
x=.060
assert rho0<R<sigma<e0/2
assert sigma<eps<epsmax0
assert R<x<sigma
assert e0-x<eps
assert x<d0-sigma

rows18=[raw_row(s,x,R,sigma,eps) for s in base18]
assert all(z is not None for z in rows18)

# The stable 19 visibility variables.
vars19=sorted(set().union(*(set(z) for z in rows18)))
assert len(vars19)==19
Xaff=(1,0,0)
Zaff=(-1,1,0)
Naff=(-1,3,1)
Oaff=(-1,2,0)
assert all(v in vars19 for v in (Xaff,Zaff,Naff,Oaff))

M18=sp.Matrix([[rr.get(v,0) for v in vars19] for rr in rows18])
assert M18.shape==(18,19)

# Rank-18 minor: delete Z.
iz=vars19.index(Zaff)
cols=[j for j in range(19) if j!=iz]
minor=M18[:,cols]
det_minor=sp.factor(minor.det(method="domain-ge"))
# Sign is for this verifier's lexicographically sorted column order.
# The committed Runde-15H audit uses a different fixed column order and
# therefore records the opposite determinant sign.
target_minor=sp.factor(
    p**6*q*r*(p-q)**3*(p+q)**3
    *(Delta-p*r)*(Delta+p*r)
)
assert sp.factor(det_minor-target_minor)==0
print("RANK18_MINOR = PASS",det_minor)

# Solve unique mode with X=1.
vv=sp.symbols("v0:19")
ix=vars19.index(Xaff)
eqs=[sum(M18[i,j]*vv[j] for j in range(19)) for i in range(18)]
eqs.append(vv[ix]-1)
sol=sp.solve(eqs,vv,dict=True,simplify=False)
assert len(sol)==1
sol=sol[0]

def coord(aff):
    return sp.factor(sol[vv[vars19.index(aff)]])

Zexpr=coord(Zaff)
Nexpr=coord(Naff)
Oexpr=coord(Oaff)

targetZ=sp.factor(-q*r*Delta/Psi)
targetN=sp.factor(p*r*(2*p**2-2*q**2-r**2)/Psi)
targetO=sp.factor(-q**2*r**2/Psi)

assert sp.factor(Zexpr-targetZ)==0
assert sp.factor(Nexpr-targetN)==0
assert sp.factor(Oexpr-targetO)==0
print("UNIQUE_MODE_COORDS = PASS")
print("Z/X =",Zexpr)
print("N/X =",Nexpr)
print("O/X =",Oexpr)

# u15 is legal in the soft cell and its row adds no new coordinate.
row15=raw_row(u15,x,R,sigma,eps)
assert row15 is not None
expected15={Naff:p,Oaff:r,Zaff:q}
keys=set(row15)|set(expected15)
assert all(sp.simplify(row15.get(k,0)-expected15.get(k,0))==0 for k in keys)
print("U15_RAW_ROW = PASS",row15)

closure=sp.factor(p*Nexpr+r*Oexpr+q*Zexpr)
target_closure=sp.factor(r*Fpoly/Psi)
assert sp.factor(closure-target_closure)==0
print("MODE_CLOSURE = PASS",closure)

# Full 19x19 determinant cross-check.
rows19=[raw_row(s,x,R,sigma,eps) for s in old19]
vars19b=sorted(set().union(*(set(z) for z in rows19)))
assert vars19b==vars19
M19=sp.Matrix([[rr.get(v,0) for v in vars19] for rr in rows19])
det19=sp.factor(M19.det(method="domain-ge"))
target19=sp.factor(
    -p**6*r*(p-q)**2*(p+q)**2
    *(Delta-p*r)*(Delta+p*r)*Fpoly
)
assert sp.factor(det19-target19)==0
print("DET19 = PASS",det19)

# Arithmetic sanity / previously established inequalities.
assert rho0<delta0<e0/2
assert eta0<rho0
assert kappa0<2*rho0
assert e0/2<d0/2
# e/2 - eta < rho, exact integer form
assert 9**6*12 < 8**6*25
print("ARITHMETIC = PASS")

# Combined whole-overlap stress. The base18 pattern is checked everywhere;
# in the soft cell the newly legal u15 row and the full old19 pattern are
# checked as well.
ref18=[patt(s,x,R,sigma,eps) for s in base18]
ref19=[patt(s,x,R,sigma,eps) for s in old19]
random.seed(180018)
nall=0
hard=0
soft=0
nearwall=0
for _ in range(150000):
    RR=random.uniform(rho0+1e-10,e0/2-1e-10)
    ss=random.uniform(RR+1e-10,e0/2-1e-10)
    ee=random.uniform(ss+1e-10,epsmax0-1e-10)
    xx=random.uniform(RR+1e-10,ss-1e-10)
    assert xx<d0-ss

    got18=[patt(s,xx,RR,ss,ee) for s in base18]
    assert all(z is not None for z in got18)
    assert got18==ref18,(RR,ss,ee,xx,"base18")
    nall+=1

    if xx<e0-ee:
        hard+=1
    elif xx>e0-ee:
        soft+=1
        got19=[patt(s,xx,RR,ss,ee) for s in old19]
        assert all(z is not None for z in got19)
        assert got19==ref19,(RR,ss,ee,xx,"soft19")
        if xx-(e0-ee)<1e-5:
            nearwall+=1

assert hard>1000 and soft>1000 and nearwall>10
print("WHOLE_OVERLAP_STRESS = PASS",nall,
      {"hard":hard,"soft":soft,"soft_nearwall":nearwall})

# Directed legal-side stress arbitrarily close to x=e-eps.
random.seed(180020)
nb=0
for _ in range(10000):
    RR=random.uniform(rho0+1e-8,e0/2-1e-6)
    ss=random.uniform(RR+1e-7,e0/2-1e-7)
    elo=max(ss+1e-7,e0-ss+1e-7)
    ehi=min(epsmax0-1e-7,e0-RR-1e-7)
    if elo>=ehi: continue
    ee=random.uniform(elo,ehi)
    wall=e0-ee
    room=ss-wall
    if room<=2e-9: continue
    xx=wall+min(room/2,1e-8)
    got=[patt(s,xx,RR,ss,ee) for s in old19]
    assert all(z is not None for z in got)
    assert got==ref19,(RR,ss,ee,xx,wall)
    nb+=1
assert nb>500
print("SOFT19_NEAR_HORIZON_WALL = PASS",nb)

print("ROUND18_DEFECT_INTERFACE_VERIFY = PASS")
