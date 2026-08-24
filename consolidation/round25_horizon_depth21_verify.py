#!/usr/bin/env python3
import math
from fractions import Fraction
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import sympy as sp

# P12 Round 25 candidate: first finite horizon-wall circuit.
# Repo basis: main@38807dfe189a6cdc7386e78e0c40c17169317a8a
# Candidate only: no promotion, P11/R14 firewall unchanged.

# ---------- canonical constants / operator ----------
a0=.5*math.log(2); b0=.5*math.log(3); T0=2*a0
d0=b0-a0; e0=T0-b0; delta0=d0-e0
epsmax0=.5*math.log(5/4); rho0=epsmax0-delta0
eta0=e0-2*delta0; kappa0=e0-delta0
p,q,r=sp.symbols('p q r', nonzero=True)
A=(0,2,1); B=(0,3,2); TT=(0,4,2)
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
(1,5,0)]

# Fundamental depth-21 circuit found on the minus horizon side.
circuit_minus=[
(-1,1,-1),
(-1,2,-4),(-1,2,-3),(-1,2,-2),(-1,2,-1),
(-1,3,-5),(-1,3,-4),(-1,3,-3),(-1,3,-2),(-1,3,-1),
(-1,4,-5),(-1,4,-4),(-1,4,-3),(-1,4,-2),(-1,4,-1),
(-1,5,-5),(-1,5,-4),(-1,5,-3),(-1,5,-2),(-1,5,-1),(-1,5,0),
(-1,6,-4),(-1,6,-3),(-1,6,-2),(-1,7,-4),
(1,-2,5),(1,-2,6),
(1,-1,2),(1,-1,3),(1,-1,4),(1,-1,5),(1,-1,6),(1,-1,7),
(1,0,2),(1,0,3),(1,0,4),(1,0,5),(1,0,6),(1,0,7),(1,0,8),
(1,1,3),(1,1,4),(1,1,5),(1,1,6),(1,1,7),(1,1,8),
(1,2,4),(1,2,5),(1,2,6),(1,2,7),(1,3,4)]
assert len(circuit_minus)==51 and len(set(circuit_minus))==51

def add(u,v): return tuple(u[i]+v[i] for i in range(3))
def neg(u): return tuple(-z for z in u)
def J(u):
    s,m,n=u
    return (-s,m,n+s)
def aval(u,x): return u[0]*x+u[1]*e0+u[2]*delta0

def raw_row(src,x,R,sigma,eps):
    u=aval(src,x)
    if not (0<u<T0+eps): return None
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
    return {v:sp.factor(c) for v,c in row.items() if sp.simplify(c)!=0}

# ---------- reference minus-horizon chamber ----------
ref=(.020,.028,.040,.0555) # R,x,sigma,epsilon
R,x,sigma,eps=ref
rows42=[raw_row(s,x,R,sigma,eps) for s in sources42]
legal42=[i for i,rr in enumerate(rows42) if rr is not None]
assert len(legal42)==41
assert sources42.index((-1,5,1)) not in legal42
assert sources42.index((1,5,0)) in legal42
fixed_sources=[sources42[i] for i in legal42]
fixed_rows=[rows42[i] for i in legal42]
Vold=sorted(set().union(*(set(rr) for rr in fixed_rows)))
assert len(Vold)==42 and (1,0,0) in Vold and (-1,0,1) in Vold

crow={s:raw_row(s,x,R,sigma,eps) for s in circuit_minus}
assert all(rr is not None and rr for rr in crow.values())
Vnew=sorted(set().union(*(set(rr)-set(Vold) for rr in crow.values())))
assert len(Vnew)==50
cols=Vold+Vnew
M92=sp.Matrix(
    [[rr.get(v,0) for v in cols] for rr in fixed_rows]
    + [[crow[s].get(v,0) for v in cols] for s in circuit_minus]
)
assert M92.shape==(92,92)
print('R25_MINUS_BLOCK_SHAPE = PASS 92x92')

# New-variable subblock is 51x50: one forced circuit relation.
N51=sp.Matrix([[crow[s].get(v,0) for v in Vnew] for s in circuit_minus])
assert N51.shape==(51,50)
print('R25_CIRCUIT_SHAPE = PASS 51x50')

# ---------- exact whole-box pattern stability ----------
def ln_bounds_int(xint,N):
    z=Fraction(xint-1,xint+1)
    ss=Fraction(0)
    for k in range(N+1):
        ss += z**(2*k+1)/Fraction(2*k+1)
    lo=2*ss
    tail=2*z**(2*N+3)/Fraction(2*N+3)/(1-z*z)
    return lo,lo+tail

l2lo,l2hi=ln_bounds_int(2,120)
l3lo,l3hi=ln_bounds_int(3,180)
Tlo,Thi=l2lo,l2hi
elo,ehi=l2lo-l3hi/2, l2hi-l3lo/2
dlo,dhi=l3lo-3*l2hi/2, l3hi-3*l2lo/2
etalo,etahi=elo-2*dhi, ehi-2*dlo
klo,khi=elo-dhi, ehi-dlo

# Open rational box B25^-.
Rlo,Rhi=Fraction('0.0195'),Fraction('0.0205')
xlo,xhi=Fraction('0.0275'),Fraction('0.0285')
slo,shi=Fraction('0.0395'),Fraction('0.0405')
eplo,ephi=Fraction('0.0550'),Fraction('0.0559')

assert 0<Rlo<Rhi<xlo<xhi<slo<shi<eplo<ephi<Fraction('0.111')+Fraction('0.001')
# Explicit horizon-wall orientation: U_- lost, U_+ retained.
assert klo-xhi > ephi
assert xhi+etahi < eplo
assert Rhi < slo


def mul_int_interval(c,lo,hi):
    return (c*lo,c*hi) if c>=0 else (c*hi,c*lo)

def affine_interval(u):
    s,m,n=u
    xa,xb=mul_int_interval(s,xlo,xhi)
    ea,eb=mul_int_interval(m,elo,ehi)
    da,db=mul_int_interval(n,dlo,dhi)
    return xa+ea+da, xb+eb+db

def certify_source_pattern(src, rr_ref):
    ulo,uhi=affine_interval(src)
    assert ulo>0 and uhi<Tlo+eplo
    for sh,k in shifts:
        for pm,sgn in [(-1,+1),(+1,-1)]:
            arg0=add(src,(0,pm*sh[1],pm*sh[2]))
            lo,hi=affine_interval(arg0)
            aref=aval(arg0,x)
            if aref<0:
                assert hi<0
                arg=neg(arg0); alo,ahi=-hi,-lo
            else:
                assert lo>0
                arg=arg0; alo,ahi=lo,hi
            live=arg in rr_ref
            if live:
                assert alo>Rhi and ahi<Tlo+slo
            else:
                # every dead slot must remain strictly on the same side
                if abs(aref)<R:
                    assert ahi<Rlo
                else:
                    assert abs(aref)>T0+sigma
                    assert alo>Thi+shi

for s,rr in zip(fixed_sources,fixed_rows): certify_source_pattern(s,rr)
for s in circuit_minus: certify_source_pattern(s,crow[s])
# Lost source remains above horizon throughout the box.
umlo,umhi=affine_interval((-1,5,1))
assert umlo>Thi+ephi
# Mirror source remains legal throughout the box.
uplo,uphi=affine_interval((1,5,0))
assert uplo>0 and uphi<Tlo+eplo
print('R25_MINUS_BOX_PATTERN = PASS')

# ---------- J-mirror chamber ----------
# At x^+=delta-x^- the J-map preserves source values and raw coefficients.
xmirror=delta0-x
mirror_ref=(R,xmirror,sigma,eps)
mirror_sources=[J(s) for s in fixed_sources+circuit_minus]
mirror_rows=[raw_row(s,xmirror,R,sigma,eps) for s in mirror_sources]
assert all(rr is not None for rr in mirror_rows)
mirror_cols=[J(v) for v in cols]
Mmir=sp.Matrix([[rr.get(v,0) for v in mirror_cols] for rr in mirror_rows])
assert Mmir==M92
assert J((-1,5,1))==(1,5,0)
print('R25_J_MIRROR_MATRIX = PASS')

# ---------- rigorous weight certificate for det(M92) ----------
# Scale p out of every row.  beta=q/p=2^(-3/4), alpha=r/p.
beta_lo_s='0.59460355750136053335874998528023795764648604623190870650950111235973333411345857'
beta_hi_s='0.59460355750136053335874998528023795764648604623190870650950111235973333411345859'
blo,bhi=Fraction(beta_lo_s),Fraction(beta_hi_s)
assert blo**4 < Fraction(1,8) < bhi**4

sqrt_lo=Fraction('0.54433105395181735515495201660130919821465499570148225076282057050021341721273667')
sqrt_hi=Fraction('0.54433105395181735515495201660130919821465499570148225076282057050021341721273668')
assert sqrt_lo*sqrt_lo < Fraction(8,27) < sqrt_hi*sqrt_hi
vlo=(l3lo/l2hi)*sqrt_lo
vhi=(l3hi/l2lo)*sqrt_hi
alpha_lo_s='0.92884030300781792630950321450028482769105581365568391416740928015650424187658192'
alpha_hi_s='0.92884030300781792630950321450028482769105581365568391416740928015650424187658195'
alo,ahi=Fraction(alpha_lo_s),Fraction(alpha_hi_s)
assert alo*alo < vlo and ahi*ahi > vhi

PREC=120
class DI:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=lo if isinstance(lo,Decimal) else Decimal(lo)
        self.hi=self.lo if hi is None else (hi if isinstance(hi,Decimal) else Decimal(hi))
    def add(self,o):
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_FLOOR; lo=self.lo+o.lo
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_CEILING; hi=self.hi+o.hi
        return DI(lo,hi)
    def neg(self): return DI(-self.hi,-self.lo)
    def sub(self,o): return self.add(o.neg())
    def mul(self,o):
        lows=[]; highs=[]
        for aa in (self.lo,self.hi):
            for bb in (o.lo,o.hi):
                with localcontext() as c:
                    c.prec=PREC; c.rounding=ROUND_FLOOR; lows.append(aa*bb)
                with localcontext() as c:
                    c.prec=PREC; c.rounding=ROUND_CEILING; highs.append(aa*bb)
        return DI(min(lows),max(highs))
    def div(self,o):
        assert not (o.lo<=0<=o.hi)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_FLOOR
            a=Decimal(1)/o.lo; b=Decimal(1)/o.hi; rlo=min(a,b)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_CEILING
            a=Decimal(1)/o.lo; b=Decimal(1)/o.hi; rhi=max(a,b)
        return self.mul(DI(rlo,rhi))
    def contains0(self): return self.lo<=0<=self.hi
    def minabs(self):
        if self.contains0(): return Decimal(0)
        return min(abs(self.lo),abs(self.hi))

betaI=DI(Decimal(beta_lo_s),Decimal(beta_hi_s))
alphaI=DI(Decimal(alpha_lo_s),Decimal(alpha_hi_s))
AI=[]
for i in range(92):
    rowi=[]
    for j in range(92):
        P=sp.Poly(sp.expand(M92[i,j]),p,q,r)
        cp=int(P.coeff_monomial(p)); cq=int(P.coeff_monomial(q)); cr=int(P.coeff_monomial(r))
        z=DI(cp)
        if cq: z=z.add(DI(cq).mul(betaI))
        if cr: z=z.add(DI(cr).mul(alphaI))
        rowi.append(z)
    AI.append(rowi)

sgn=1; detI=DI(1)
for k in range(92):
    _,pr=max((AI[i][k].minabs(),i) for i in range(k,92))
    assert not AI[pr][k].contains0()
    if pr!=k:
        AI[k],AI[pr]=AI[pr],AI[k]; sgn*=-1
    piv=AI[k][k]
    detI=detI.mul(piv)
    for i in range(k+1,92):
        if AI[i][k].lo==0 and AI[i][k].hi==0: continue
        fac=AI[i][k].div(piv)
        AI[i][k]=DI(0)
        for j in range(k+1,92):
            AI[i][j]=AI[i][j].sub(fac.mul(AI[k][j]))
if sgn<0: detI=detI.neg()
assert detI.lo>0
print('R25_DET92_INTERVAL = PASS',detI.lo,detI.hi)

# Since p>0, det(M92)=p^92*det(scaled matrix) is nonzero.
print('ROUND25_HORIZON_DEPTH21_VERIFY = PASS')
