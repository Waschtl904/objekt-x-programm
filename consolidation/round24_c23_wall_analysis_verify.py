#!/usr/bin/env python3
import math, random
from fractions import Fraction
import sympy as sp

# P12 Round 24 candidate -- systematic C23 wall analysis.
# No theorem promotion is encoded here.  P11/R14 firewall unchanged.

# ---------- constants ----------
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
r42floor0=(chi0-eta0)/2

assert abs(eta0+chi0-delta0)<1e-15
assert abs(kappa0-delta0-eta0)<1e-15
assert abs(r42floor0-.25*math.log(531441/524288))<1e-14
assert r42floor0 < omega0 < eta0 < chi0 < rho0
print("CONSTANTS = PASS",{
    "r42_pattern_feasibility_floor":r42floor0,
    "omega":omega0,"eta":eta0,"chi":chi0,"rho":rho0
})

p,q,r=sp.symbols("p q r", positive=True, nonzero=True)
A=(0,2,1)
B=(0,3,2)
TT=(0,4,2)
shifts=[(A,p),(B,r),(TT,q)]

sources42=[
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
assert len(sources42)==42 and len(set(sources42))==42

def add(u,v): return tuple(u[i]+v[i] for i in range(3))
def neg(u): return tuple(-z for z in u)
def aval(u,x): return u[0]*x+u[1]*e0+u[2]*delta0
def J(u):
    s,m,n=u
    return (-s,m,n+s)

assert all(J(s) in sources42 for s in sources42)
print("J_SOURCE_PAIRING_42 = PASS")

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
    return {aa:sp.factor(c) for aa,c in row.items()
            if sp.simplify(c)!=0}

def make_matrix(sources,pt):
    R,x,sigma,eps=pt
    rows=[raw_row(s,x,R,sigma,eps) for s in sources]
    legal=[i for i,rr in enumerate(rows) if rr is not None]
    vars_=sorted(set().union(*(set(rows[i]) for i in legal)))
    M=sp.zeros(len(legal),len(vars_))
    for ii,i in enumerate(legal):
        for v,c in rows[i].items():
            M[ii,vars_.index(v)]=c
    return M,vars_,rows,legal

def pattern_fast(src,x,R,sigma,eps):
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

# ---------- committed Round-23 matrix ----------
ref=(.020,.030,.040,.060)
M42,V42,R42,L42=make_matrix(sources42,ref)
assert M42.shape==(42,42)
assert len(L42)==42
assert all(J(v) in V42 for v in V42)

# 21+21 block symmetry
negS=[s for s in sources42 if s[0]==-1]
posS=[J(s) for s in negS]
negV=[v for v in V42 if v[0]==-1]
posV=[J(v) for v in negV]
rowref={s:raw_row(s,ref[1],ref[0],ref[2],ref[3]) for s in sources42}
Mord=sp.Matrix([[rowref[s].get(v,0) for v in negV+posV] for s in negS+posS])
A21=Mord[:21,:21]; B21=Mord[:21,21:]
assert Mord[21:,:21]==B21
assert Mord[21:,21:]==A21
print("M42_J_BLOCK = PASS")

# ---------- exact wall atlas ----------
# event tuple = coefficients of (R,x,sigma,eps,e,delta) in event=0.
walls={
"X_EQ_ETA":(0,1,0,0,-1,2),
"X_EQ_CHI":(0,1,0,0,1,-3),
"R_PLUS_X_EQ_DELTA":(1,1,0,0,0,-1),
"SIGMA_PLUS_X_EQ_DELTA":(0,1,1,0,0,-1),
"SIGMA_PLUS_X_EQ_KAPPA":(0,1,1,0,-1,1),
"SIGMA_MINUS_X_EQ_ETA":(0,-1,1,0,-1,2),
"EPS_PLUS_X_EQ_KAPPA":(0,1,0,1,-1,1),
"EPS_EQ_X_PLUS_ETA":(0,-1,0,1,-1,2),
"X_EQ_R":(-1,1,0,0,0,0),
"SIGMA_EQ_X":(0,-1,1,0,0,0),
}

def same_wall(a,b):
    return a==b or tuple(-z for z in a)==b

events={k:[] for k in walls}
for src in sources42:
    s,m,n=src
    tests=[("source_lower",None,(0,s,0,0,m,n)),
           ("source_upper",None,(0,s,0,-1,m-4,n-2))]
    for shname,sh in [("a",A),("b",B),("T",TT)]:
        for pm in (-1,+1):
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            sa,ma,na=arg
            for sign in (+1,-1):
                tests.append(("support_lower",(shname,pm,sign),
                              (-1,sign*sa,0,0,sign*ma,sign*na)))
                tests.append(("support_upper",(shname,pm,sign),
                              (0,sign*sa,-1,0,sign*ma-4,sign*na-2)))
    for typ,slot,ev in tests:
        for name,w in walls.items():
            if same_wall(ev,w):
                events[name].append((src,typ,slot))

assert len(events["X_EQ_ETA"])==0
assert len(events["X_EQ_CHI"])==0
assert len(events["R_PLUS_X_EQ_DELTA"])==6
assert len(events["SIGMA_PLUS_X_EQ_DELTA"])==3
assert len(events["SIGMA_PLUS_X_EQ_KAPPA"])==1
assert len(events["SIGMA_MINUS_X_EQ_ETA"])==1
assert events["EPS_PLUS_X_EQ_KAPPA"]==[((-1,5,1),"source_upper",None)]
assert events["EPS_EQ_X_PLUS_ETA"]==[((1,5,0),"source_upper",None)]
assert len(events["X_EQ_R"])==6
assert len(events["SIGMA_EQ_X"])==3

assert aval((1,-1,2),eta0)==0
assert aval((-1,1,-2),eta0)==0
assert aval((1,1,-3),chi0)==0
assert aval((-1,-1,3),chi0)==0

print("WALL_EVENT_ATLAS = PASS",{
    k:len(v) for k,v in events.items()
})

# ---------- true fixed-42 pattern chamber ----------
def in_C42(pt):
    R,x,sigma,eps=pt
    return (
      0<R<rho0 and
      R<x<delta0-R and
      chi0-R<x<eta0+R and
      max(x,delta0-x)<sigma<min(kappa0-x,x+eta0) and
      max(kappa0-x,x+eta0)<eps<epsmax0
    )

deep=(.010,delta0/2,.040,.070)
assert in_C42(deep)
Mdeep,Vdeep,_,Ldeep=make_matrix(sources42,deep)
assert Vdeep==V42
assert Mdeep==M42
assert len(Ldeep)==42
assert deep[0] < omega0
print("TRUE_C42_DEEP_BELOW_OMEGA = PASS",deep)

refpat=[pattern_fast(s,ref[1],ref[0],ref[2],ref[3]) for s in sources42]
random.seed(240024)
count=0
for _ in range(30000):
    R=random.uniform(r42floor0+1e-8,delta0/2-1e-8)
    xlo=max(R,chi0-R)+1e-8
    xhi=min(delta0-R,eta0+R)-1e-8
    if xlo>=xhi: continue
    x=random.uniform(xlo,xhi)
    slo=max(x,delta0-x)+1e-8
    shi=min(kappa0-x,x+eta0)-1e-8
    if slo>=shi: continue
    sigma=random.uniform(slo,shi)
    elo=max(kappa0-x,x+eta0)+1e-8
    if elo>=epsmax0-1e-8: continue
    eps=random.uniform(elo,epsmax0-1e-8)
    pt=(R,x,sigma,eps)
    assert in_C42(pt)
    got=[pattern_fast(s,x,R,sigma,eps) for s in sources42]
    assert got==refpat
    count+=1
assert count>10000
print("TRUE_C42_PATTERN_STRESS = PASS",count)

assert omega0 > chi0-eta0
print("OMEGA_NOT_M42_EVENT = PASS")
print("ETA_CHI_NOT_M42_EVENTS = PASS")

# ---------- easy column-deletion walls ----------
pt_Rdelta=(.029,.030,.040,.070)
assert pt_Rdelta[0]+pt_Rdelta[1]>delta0 and pt_Rdelta[1]>pt_Rdelta[0]
MR,VR,_,LR=make_matrix(sources42,pt_Rdelta)
assert len(LR)==42 and MR.shape==(42,41)
assert set(VR)==set(V42)-{(-1,0,1)}

pt_Sdelta=(.020,.0265,.030,.070)
assert pt_Sdelta[2]+pt_Sdelta[1]<delta0 and pt_Sdelta[2]>pt_Sdelta[1]
MS,VS,_,LS=make_matrix(sources42,pt_Sdelta)
assert len(LS)==42 and MS.shape==(42,41)
assert set(VS)==set(V42)-{(-1,4,3)}

pt_Sx=(.020,.030,.029,.070)
MSx,VSx,_,LSx=make_matrix(sources42,pt_Sx)
assert len(LSx)==42 and MSx.shape==(42,41)
assert set(VSx)==set(V42)-{(1,4,2)}
print("COLUMN_DELETION_WALLS = PASS")

# ---------- genuine support-entry walls ----------
Uminus=(-1,5,1)
Uplus=(1,5,0)

pt_Uminus=(.020,.030,.0555,.070)
MUminus,VUminus,_,LUminus=make_matrix(sources42,pt_Uminus)
assert len(LUminus)==42 and MUminus.shape==(42,43)
assert set(VUminus)==set(V42)|{Uminus}

xmirror=delta0-.030
pt_Uplus=(.020,xmirror,.0555,.070)
MUplus,VUplus,_,LUplus=make_matrix(sources42,pt_Uplus)
assert len(LUplus)==42 and MUplus.shape==(42,43)
assert set(VUplus)==set(V42)|{Uplus}
print("SUPPORT_ENTRY_RANK_DEFECT = PASS 42x43, paired by J")

# ---------- genuine horizon-loss walls ----------
pt_Hminus=(.020,.028,.040,.0555)
MHminus,VHminus,_,LHminus=make_matrix(sources42,pt_Hminus)
assert MHminus.shape==(41,42)
assert (-1,5,1) not in [sources42[i] for i in LHminus]
assert (1,5,0) in [sources42[i] for i in LHminus]

pt_Hplus=(.020,.031,.040,.0555)
MHplus,VHplus,_,LHplus=make_matrix(sources42,pt_Hplus)
assert MHplus.shape==(41,42)
assert (1,5,0) not in [sources42[i] for i in LHplus]
assert (-1,5,1) in [sources42[i] for i in LHplus]
print("HORIZON_ROW_LOSS = PASS 41x42, paired by J")

# Exhaustive one-step replacement check
def one_step_candidates(vars_):
    C=set()
    for v in vars_:
        for vv in (v,neg(v)):
            for sh,_ in shifts:
                for pm in (-1,+1):
                    C.add(add(vv,(0,-pm*sh[1],-pm*sh[2])))
    return C

Cfinite=one_step_candidates(V42)-set(sources42)
assert len(Cfinite)==142

def no_old_var_replacement(pt):
    R,x,sigma,eps=pt
    hits=[]
    for src in Cfinite:
        rr=raw_row(src,x,R,sigma,eps)
        if rr is None or not rr: continue
        if set(rr)<=set(V42):
            hits.append((src,rr))
    return hits

assert no_old_var_replacement(pt_Hminus)==[]
assert no_old_var_replacement(pt_Hplus)==[]
print("HORIZON_NO_SINGLE_OLDVAR_REPLACEMENT = PASS 142 candidates each side")

# ---------- next-shell support-wall closure ----------
Vminus=(-1,4,4)
Vplus=(1,4,3)
assert J(Vminus)==Vplus

rrVm=raw_row(Vminus,pt_Uminus[1],pt_Uminus[0],pt_Uminus[2],.100)
rrVp=raw_row(Vplus,pt_Uplus[1],pt_Uplus[0],pt_Uplus[2],.100)
assert rrVm=={(-1,2,3):p,(-1,1,2):r,(-1,0,2):q}
assert rrVp=={(1,2,2):p,(1,1,1):r,(1,0,1):q}
assert set(rrVm)<=set(VUminus)
assert set(rrVp)<=set(VUplus)
print("SUPPORT_WALL_AUXILIARY_ROWS = PASS")

pt44=(.020,delta0/2,.070,.100)
sources44=sources42+[Vminus,Vplus]
M44,V44,R44,L44=make_matrix(sources44,pt44)
assert M44.shape==(44,44) and len(L44)==44
assert set(V44)==set(V42)|{Uminus,Uplus}
assert all(J(s) in sources44 for s in sources44)
assert all(J(v) in V44 for v in V44)

negS44=[s for s in sources44 if s[0]==-1]
posS44=[J(s) for s in negS44]
negV44=[v for v in V44 if v[0]==-1]
posV44=[J(v) for v in negV44]
row44={s:raw_row(s,pt44[1],pt44[0],pt44[2],pt44[3]) for s in sources44}
MO44=sp.Matrix([[row44[s].get(v,0) for v in negV44+posV44]
                 for s in negS44+posS44])
A22=MO44[:22,:22]; B22=MO44[:22,22:]
assert MO44[22:,:22]==B22
assert MO44[22:,22:]==A22
print("M44_J_BLOCK = PASS")

det44=sp.factor(M44.det(method="domain-ge"))
fl=sp.factor_list(det44)
deg9=[f for f,ex in fl[1] if sp.total_degree(f)==9]
assert len(deg9)==2
assert any(f==p-q for f,ex in fl[1])
assert any(f==p+q for f,ex in fl[1])

beta,v=sp.symbols("beta v", positive=True)
def normalize(F,deg):
    P=sp.Poly(sp.expand(F),p,q,r)
    out=0
    for (ep,eq,er),coef in P.terms():
        assert ep+eq+er==deg and er%2==0
        out += coef*beta**eq*v**(er//2)
    return sp.expand(out)

G1=normalize(deg9[0],9)
G2=normalize(deg9[1],9)
assert sp.expand(G2-G1.subs(beta,-beta))==0 or sp.expand(G1-G2.subs(beta,-beta))==0

def ln_bounds_int(xint,N):
    z=Fraction(xint-1,xint+1)
    s=Fraction(0)
    for k in range(N+1):
        s += z**(2*k+1)/Fraction(2*k+1)
    lo=2*s
    tail=2*z**(2*N+3)/Fraction(2*N+3)/(1-z*z)
    return lo,lo+tail

l2lo,l2hi=ln_bounds_int(2,40)
l3lo,l3hi=ln_bounds_int(3,60)
blo=Fraction("0.59460355750136053335")
bhi=Fraction("0.59460355750136053336")
assert blo**4 < Fraction(1,8) < bhi**4
slo=Fraction("0.54433105395181735515")
shi=Fraction("0.54433105395181735516")
assert slo*slo < Fraction(8,27) < shi*shi
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
            lo += coef*ml; hi += coef*mh
        else:
            lo += coef*mh; hi += coef*ml
    return lo,hi

I1=poly_interval(G1)
I2=poly_interval(G2)
assert I1[0]>0 and I2[0]>0
print("M44_PARITY_FACTOR_INTERVALS = PASS",
      (float(I1[0]),float(I1[1])),
      (float(I2[0]),float(I2[1])))
print("DET44_FACTOR = PASS",det44)

def in_C44(pt):
    R,x,sigma,eps=pt
    return (
      0<R<rho0 and
      R<x<delta0-R and
      chi0-R<x<eta0+R and
      max(kappa0-x,x+eta0)<sigma<min(2*delta0-x,x+delta0) and
      max(2*delta0-x,x+delta0)<eps<epsmax0
    )

refpat44=[pattern_fast(s,pt44[1],pt44[0],pt44[2],pt44[3]) for s in sources44]
random.seed(244044)
count44=0
for _ in range(25000):
    R=random.uniform(r42floor0+1e-8,delta0/2-1e-8)
    xlo=max(R,chi0-R)+1e-8
    xhi=min(delta0-R,eta0+R)-1e-8
    if xlo>=xhi: continue
    x=random.uniform(xlo,xhi)
    slo=max(kappa0-x,x+eta0)+1e-8
    shi=min(2*delta0-x,x+delta0)-1e-8
    if slo>=shi: continue
    sigma=random.uniform(slo,shi)
    elo=max(2*delta0-x,x+delta0)+1e-8
    if elo>=epsmax0-1e-8: continue
    eps=random.uniform(elo,epsmax0-1e-8)
    pt=(R,x,sigma,eps)
    assert in_C44(pt)
    got=[pattern_fast(s,x,R,sigma,eps) for s in sources44]
    assert got==refpat44
    count44+=1
assert count44>10000
print("C44_PATTERN_STRESS = PASS",count44)

print("ROUND24_C23_WALL_ANALYSIS_VERIFY = PASS")
