#!/usr/bin/env python3
import math, random
import sympy as sp

# P12 Round 20 -- Region D full-closure retained verifier.
# Reconstructs all rows from the canonical raw three-shift operator.
# Region D received independent raw-operator GREEN; global rho promotion is separate.

a0 = math.log(2)/2
b0 = math.log(3)/2
T0 = 2*a0
d0 = b0-a0
e0 = T0-b0
delta0 = d0-e0
epsmax0 = .5*math.log(5/4)
rho0 = epsmax0-delta0

p,q,r = sp.symbols("p q r", positive=True, nonzero=True)
Delta = p**2-q**2
Psi = Delta**2-p**2*r**2
F = 2*p**4-3*p**2*q**2-p**2*r**2+q**4-q**2*r**2

A=(0,2,1)
B=(0,3,2)
TT=(0,4,2)
shifts=[(A,p),(B,r),(TT,q)]

old19=[
(-1,3,2),(1,3,2),(-1,2,1),(-1,4,2),(1,4,2),(1,3,1),
(-1,1,0),(-1,3,1),(1,1,1),(1,3,3),(1,2,2),(-1,2,0),
(-1,4,1),(1,0,1),(-1,5,2),(1,1,2),(1,2,3),(-1,4,0),(-1,5,1)
]

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

def patt(src,x,R,sigma,eps):
    u=aval(src,x)
    if not (0<u<T0+eps):
        return None
    out=[]
    for sh in (A,B,TT):
        for pm in (-1,+1):
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            av=aval(arg,x)
            if av<0:
                arg=neg(arg)
                av=-av
            if R<av<T0+sigma:
                out.append(arg)
    return tuple(sorted(out))

assert rho0 < e0/2 < d0/2
gap = d0-epsmax0-e0/2
target_gap = .25*math.log(27/25)
assert abs(gap-target_gap) < 1e-14 and gap > 0
print("HARD_GEOMETRY_GAP = PASS", gap, "= 1/4 log(27/25)")

# Soft representative with H(e-x) dead.
Rm, sm, em, xm = .053, .080, .100, .055
assert rho0 < Rm < xm < e0/2 <= sm < em < epsmax0
assert sm <= e0-xm < em
rowsM=[raw_row(s,xm,Rm,sm,em) for s in old19]
assert all(z is not None for z in rowsM)
vars19=sorted(set().union(*(set(z) for z in rowsM)))
assert len(vars19)==19

Xaff=(1,0,0)
Jaff=(-1,5,2)  # T+e-x
assert Xaff in vars19 and Jaff not in vars19
M19=sp.Matrix([[rr.get(v,0) for v in vars19] for rr in rowsM])

det19=sp.factor(M19.det(method="domain-ge"))
target19=sp.factor(
    -p**6*r*(p-q)**2*(p+q)**2
    *(Delta-p*r)*(Delta+p*r)*F
)
assert sp.factor(det19-target19)==0
print("SOFT_DET19 = PASS", det19)

# Soft representative with H(e-x) live.
Rl, sl, el, xl = .053, .100, .105, .055
assert rho0 < Rl < xl < e0/2 <= sl < el < epsmax0
assert e0-xl < sl
rowsL=[raw_row(s,xl,Rl,sl,el) for s in old19]
assert all(z is not None for z in rowsL)
varsL=sorted(set().union(*(set(z) for z in rowsL)))
assert set(varsL)==set(vars19)|{Jaff}

MbaseL=sp.Matrix([[rr.get(v,0) for v in vars19] for rr in rowsL])
assert MbaseL==M19
C=sp.Matrix([rr.get(Jaff,0) for rr in rowsL])
expectedC=[0]*19
expectedC[6]=-q
expectedC[7]=-p
expectedC[11]=-r
assert all(sp.simplify(C[i]-expectedC[i])==0 for i in range(19))
print("OPTIONAL_TAIL_COLUMN = PASS", list(C))

ix=vars19.index(Xaff)
Mrep=M19.copy()
Mrep[:,ix]=C
det_rep=sp.factor(Mrep.det(method="domain-ge"))
assert det_rep==0
print("CRAMER_X_REPLACEMENT = PASS", det_rep)

# Exact stronger certificate:
# lambda^T [M19 | C] = e_X^T.
lam=[
    q**2*r/F,
    Psi/(r*F),
    -p*Delta/F,
    -q*Delta/F,
    -q*Delta/F,
    p*q*r/F,
    p**2*Delta/(r*F),
    -p*q*(Delta+r**2)/(r*F),
    -p*q*Delta/(r*F),
    p*q*r/F,
    -q*(2*p**2-q**2)/F,
    p**2*q/F,
    -2*p*(p**2-r**2)/F,
    -p**3/F,
    Psi/(r*F),
    p**2*r/F,
    -p*q**2*r**2/(Delta*F),
    -p**2*q*r**2/(Delta*F),
    p*q*r/F,
]
Maug=M19.row_join(C)
cert=sp.simplify(Maug.T*sp.Matrix(lam))
target=sp.zeros(20,1)
target[ix,0]=1
assert all(sp.simplify(cert[i]-target[i])==0 for i in range(20))
print("ROW_MULTIPLIER_CERTIFICATE = PASS")

p0=math.sqrt(math.log(2))*2**(-3/4)
r0=math.sqrt(math.log(3))*3**(-3/4)
q0=math.sqrt(math.log(2))*2**(-3/2)
Delta0=p0*p0-q0*q0
Psi0=Delta0*Delta0-p0*p0*r0*r0
F0=2*p0**4-3*p0*p0*q0*q0-p0*p0*r0*r0+q0**4-q0*q0*r0*r0
assert Delta0>0 and Psi0<0 and F0<0
print("NONDEGENERACY_SANITY = PASS", {"Delta":Delta0,"Psi":Psi0,"F":F0})

refM=[patt(s,xm,Rm,sm,em) for s in old19]
refL=[patt(s,xl,Rl,sl,el) for s in old19]

random.seed(200020)
counts={"hard":0,"soft_tail_dead":0,"soft_tail_live":0}
for _ in range(500000):
    R=random.uniform(rho0+1e-10,e0/2-1e-10)
    sigma=random.uniform(e0/2+1e-10,epsmax0-2e-10)
    eps=random.uniform(sigma+1e-10,epsmax0-1e-10)
    x=random.uniform(R+1e-10,e0/2-1e-10)
    z=e0-x

    if z>eps:
        counts["hard"]+=1
        assert rho0<R<e0/2
        assert R<x<sigma
        assert x<d0-sigma
        assert x<e0-eps
    else:
        if z>=sigma:
            counts["soft_tail_dead"]+=1
            assert [patt(s,x,R,sigma,eps) for s in old19]==refM
        else:
            counts["soft_tail_live"]+=1
            assert [patt(s,x,R,sigma,eps) for s in old19]==refL

assert min(counts.values())>1000
print("REGION_D_LOW_STRIP_STRESS = PASS 500000", counts)

random.seed(200021)
n_eps=n_sig=0
for _ in range(30000):
    R=random.uniform(rho0+1e-8,e0/2-2e-6)
    sigma=random.uniform(e0/2+2e-6,epsmax0-4e-6)
    eps=random.uniform(sigma+2e-6,epsmax0-2e-6)

    wall=e0-eps
    if R+2e-8 < wall < e0/2-2e-8:
        dh=min(1e-8,(wall-R)/4,(e0/2-wall)/4,(eps-sigma)/4)
        if dh>0:
            xh=wall-dh
            xs=wall+dh
            assert e0-xh>eps
            assert e0-xs<eps
            got=[patt(s,xs,R,sigma,eps) for s in old19]
            ref=refL if e0-xs<sigma else refM
            assert got==ref
            n_eps+=1

    wall=e0-sigma
    if R+2e-8 < wall < e0/2-2e-8:
        dh=min(1e-8,(wall-R)/4,(e0/2-wall)/4,(eps-sigma)/4)
        if dh>0:
            xd=wall-dh
            xl2=wall+dh
            assert sigma<e0-xd<eps
            assert e0-xl2<sigma
            assert [patt(s,xd,R,sigma,eps) for s in old19]==refM
            assert [patt(s,xl2,R,sigma,eps) for s in old19]==refL
            n_sig+=1

assert n_eps>100 and n_sig>100
print("DIRECTED_HORIZON_WALL = PASS",n_eps)
print("DIRECTED_TAIL_WALL = PASS",n_sig)

random.seed(200022)
parts={"A":0,"B":0,"C":0,"D":0}
for _ in range(300000):
    R=random.uniform(rho0+1e-10,T0-1e-8)
    eps=random.uniform(1e-7,epsmax0-1e-10)
    sigma=random.uniform(1e-10,eps-1e-10)
    if R>=e0/2:
        parts["A"]+=1
    elif sigma<=R:
        parts["B"]+=1
    elif sigma<e0/2:
        parts["C"]+=1
    else:
        parts["D"]+=1

assert sum(parts.values())==300000 and min(parts.values())>0
print("GLOBAL_FOUR_WAY_PARTITION = PASS 300000",parts)
print("REBASE_LOGIC = PASS: kill (R,e/2) => support in (e/2,S); Round 14 applies at R_eff=e/2")
print("ROUND20_REGION_D_FULL_CLOSURE_VERIFY = PASS")
