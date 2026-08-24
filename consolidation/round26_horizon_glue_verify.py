#!/usr/bin/env python3
import itertools, random, math
from fractions import Fraction
import sympy as sp

# P12 Round 26 candidate:
# exact enlargement and J-gluing of the promoted Round-25 92x92 horizon circuit.
# Repo basis: main@9b0982e40b60730c4936eb8910ef425c883ccfb4
# Candidate only; P11/R14 firewall unchanged.

def ln_bounds_int(xint,N):
    z=Fraction(xint-1,xint+1)
    s=Fraction(0)
    for k in range(N+1):
        s += z**(2*k+1)/Fraction(2*k+1)
    lo=2*s
    tail=2*z**(2*N+3)/Fraction(2*N+3)/(1-z*z)
    return lo,lo+tail

l2lo,l2hi=ln_bounds_int(2,120)
l3lo,l3hi=ln_bounds_int(3,180)
l5lo,l5hi=ln_bounds_int(5,500)
Hlo,Hhi=(8*l2lo-5*l3hi)/2,(8*l2hi-5*l3lo)/2
Clo,Chi=(7*l3lo-11*l2hi)/2,(7*l3hi-11*l2lo)/2
Elo,Ehi=l5lo/2-l2hi,l5hi/2-l2lo
assert Hlo>0 and Clo>Hhi and Elo>0
assert 2*Hhi+Chi < Elo
eta0=(float(Hlo)+float(Hhi))/2
chi0=(float(Clo)+float(Chi))/2
e0=3*eta0+2*chi0
delta0=eta0+chi0
T0=14*eta0+10*chi0
epsmax0=(float(Elo)+float(Ehi))/2
print('R26_CONSTANTS = PASS',{'eta':eta0,'chi':chi0,'epsmax':epsmax0,'delta':delta0,'T':T0})

p,q,r=sp.symbols('p q r', nonzero=True)
A=(0,2,1); B=(0,3,2); TT=(0,4,2)
shifts=[('a',A,p),('b',B,r),('T',TT,q)]

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
def aval(u,x):
    s,m,n=u
    return s*x+m*e0+n*delta0

def raw_row(src,x,R,sigma,eps):
    u=aval(src,x)
    if not (0<u<T0+eps): return None
    row={}
    for _,sh,k in shifts:
        for pm,sgn in [(-1,+1),(+1,-1)]:
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            coeff=sgn*k
            av=aval(arg,x)
            if av<0:
                arg=neg(arg); av=-av; coeff=-coeff
            if R<av<T0+sigma:
                row[arg]=sp.expand(row.get(arg,0)+coeff)
    return {v:sp.factor(c) for v,c in row.items() if sp.simplify(c)!=0}

ref=(.020,.028,.040,.0555)
Rref,xref,sref,eref=ref
rows42=[raw_row(s,xref,Rref,sref,eref) for s in sources42]
legal42=[i for i,rr in enumerate(rows42) if rr is not None]
assert len(legal42)==41
assert sources42.index((-1,5,1)) not in legal42
assert sources42.index((1,5,0)) in legal42
fixed_sources=[sources42[i] for i in legal42]
fixed_rows=[rows42[i] for i in legal42]
Vold=sorted(set().union(*(set(rr) for rr in fixed_rows)))
assert len(Vold)==42
crow={s:raw_row(s,xref,Rref,sref,eref) for s in circuit_minus}
assert all(rr is not None and rr for rr in crow.values())
Vnew=sorted(set().union(*(set(rr)-set(Vold) for rr in crow.values())))
assert len(Vnew)==50
cols=Vold+Vnew
M92=sp.Matrix([[rr.get(v,0) for v in cols] for rr in fixed_rows]+[[crow[s].get(v,0) for v in cols] for s in circuit_minus])
assert M92.shape==(92,92)
selected_sources=fixed_sources+circuit_minus
assert len(selected_sources)==92
print('R26_BASE_M92 = PASS 92x92')

H,C,E=sp.symbols('H C E', real=True)
RR,X,SIG,EPS=sp.symbols('RR X SIG EPS', real=True)
vars4=(RR,X,SIG,EPS)
Tsym=14*H+10*C

def aff_sym(u):
    s,m,n=u
    return s*X+m*(3*H+2*C)+n*(H+C)

chamber=[
    X-H,
    C-X,
    RR+X-C,
    2*H-RR-X,
    H-X+RR,
    SIG-X-(C-H),
    3*H-SIG-X,
    EPS-X-H,
    E-EPS
]

raw_conditions=[]
for src in selected_sources:
    u=aff_sym(src)
    raw_conditions.append((u,('source_lower',src)))
    raw_conditions.append((Tsym+EPS-u,('source_upper',src)))
    for shname,sh,_ in shifts:
        for pm in (-1,+1):
            arg0=add(src,(0,pm*sh[1],pm*sh[2]))
            vv=aff_sym(arg0)
            vref=aval(arg0,xref)
            sign=1 if vref>0 else -1
            w=sp.expand(sign*vv)
            raw_conditions.append((w,('slot_sign',src,shname,pm,arg0,sign)))
            avref=abs(vref)
            if Rref<avref<T0+sref:
                raw_conditions.append((w-RR,('live_lower',src,shname,pm,arg0,sign)))
                raw_conditions.append((Tsym+SIG-w,('live_upper',src,shname,pm,arg0,sign)))
            elif avref<Rref:
                raw_conditions.append((RR-w,('dead_lower',src,shname,pm,arg0,sign)))
            else:
                raw_conditions.append((w-Tsym-SIG,('dead_upper',src,shname,pm,arg0,sign)))
assert len(raw_conditions)==1628

facet_names=['x=eta','x=chi','R+x=chi','R+x=2eta','x-R=eta','sigma-x=chi-eta','sigma+x=3eta','eps=x+eta']
facet_hits=[]
for f in chamber[:8]:
    n=sum(1 for g,_ in raw_conditions if sp.expand(g-f)==0)
    facet_hits.append(n)
assert all(n>0 for n in facet_hits)
print('R26_EIGHT_RAW_FACETS = PASS',dict(zip(facet_names,facet_hits)))

def qfrac(q0):
    q0=sp.Rational(q0)
    return Fraction(int(q0.p),int(q0.q))

def coeff3(expr):
    ex=sp.expand(expr)
    ch=ex.coeff(H); cc=ex.coeff(C); ce=ex.coeff(E)
    const=sp.expand(ex-ch*H-cc*C-ce*E)
    assert not const.free_symbols
    return qfrac(ch),qfrac(cc),qfrac(ce),qfrac(const)

def interval3(cf):
    ah,ac,ae,c0=cf
    lo=hi=c0
    for aa,(bl,bh) in zip((ah,ac,ae),((Hlo,Hhi),(Clo,Chi),(Elo,Ehi))):
        if aa>=0:
            lo+=aa*bl; hi+=aa*bh
        else:
            lo+=aa*bh; hi+=aa*bl
    return lo,hi

vertices=[]
for combo in itertools.combinations(range(len(chamber)),4):
    sol=sp.solve([chamber[i] for i in combo],vars4,dict=True,simplify=False)
    if len(sol)!=1 or not all(v in sol[0] for v in vars4):
        continue
    vv=tuple(sp.expand(sol[0][v]) for v in vars4)
    sub=dict(zip(vars4,vv))
    feasible=True
    for gg in chamber:
        ex=sp.expand(gg.subs(sub))
        lo,hi=interval3(coeff3(ex))
        if hi<0:
            feasible=False
            break
        assert not (lo<0<hi),('uncertain vertex sign',combo,ex,float(lo),float(hi))
    if feasible:
        vertices.append((combo,vv))
assert len(vertices)==20

def coeff8(expr):
    ex=sp.expand(expr)
    syms=(RR,X,SIG,EPS,H,C,E)
    co=[ex.coeff(s) for s in syms]
    const=sp.expand(ex-sum(a*s for a,s in zip(co,syms)))
    assert not const.free_symbols
    return tuple(qfrac(a) for a in (*co,const))

def raw_at_vertex(cf,coord):
    ar,ax,asig,aeps,ah,ac,aE,c0=cf
    h,c,e_,ct=ah,ac,aE,c0
    for aa,vexpr in zip((ar,ax,asig,aeps),coord):
        vh,vc,vE,v0=coeff3(vexpr)
        h+=aa*vh; c+=aa*vc; e_+=aa*vE; ct+=aa*v0
    return h,c,e_,ct

for expr,label in raw_conditions:
    cf=coeff8(expr)
    for combo,vv in vertices:
        lo,hi=interval3(raw_at_vertex(cf,vv))
        assert hi>=0,(label,combo,float(lo),float(hi))
        assert not (lo<0<hi),(label,combo,'uncertain',float(lo),float(hi))
print('R26_POLYHEDRAL_PATTERN_CERTIFICATE = PASS',len(vertices),'vertices',len(raw_conditions),'raw inequalities')

Rlo,Rhi=Fraction('0.0195'),Fraction('0.0205')
xlo,xhi=Fraction('0.0275'),Fraction('0.0285')
slo,shi=Fraction('0.0395'),Fraction('0.0405')
eplo,ephi=Fraction('0.0550'),Fraction('0.0559')
assert xlo>Hhi and xhi<Clo
assert Rlo+xlo>Chi and Rhi+xhi<2*Hlo
assert xhi-Rlo<Hlo
assert slo-xhi>Chi-Hlo
assert shi+xhi<3*Hlo
assert eplo>xhi+Hhi
assert ephi<Elo
print('R26_B25_STRICT_SUBSET = PASS')

plus_chamber=[
    X-H,
    C-X,
    RR+X-C,
    X-RR-(C-H),
    H-X+RR,
    SIG+X-2*C,
    2*H-C-SIG+X,
    EPS+X-(2*H+C),
    E-EPS
]
Y=H+C-X
minus_mirrored=[sp.expand(g.subs(X,Y, simultaneous=True)) for g in chamber]
assert sorted(map(str,map(sp.expand,minus_mirrored)))==sorted(map(str,map(sp.expand,plus_chamber)))
print('R26_J_CHAMBER_MAP = PASS')

xmir=delta0-xref
mirror_sources=[J(s) for s in selected_sources]
mirror_rows=[raw_row(s,xmir,Rref,sref,eref) for s in mirror_sources]
mirror_cols=[J(v) for v in cols]
assert all(rr is not None for rr in mirror_rows)
Mmir=sp.Matrix([[rr.get(v,0) for v in mirror_cols] for rr in mirror_rows])
assert Mmir==M92
print('R26_J_MATRIX_IDENTITY = PASS')

ORlo,ORhi=Fraction('0.014'),Fraction('0.016')
OXlo,OXhi=Fraction('0.0293'),Fraction('0.0296')
OSlo,OShi=Fraction('0.041'),Fraction('0.043')
OElo,OEhi=Fraction('0.065'),Fraction('0.075')
overlap_checks=[
    OXlo-Hhi,
    Clo-OXhi,
    ORlo+OXlo-Chi,
    2*Hlo-ORhi-OXhi,
    Hlo-OXhi+ORlo,
    OSlo-OXhi-(Chi-Hlo),
    3*Hlo-OShi-OXhi,
    OElo-OXhi-Hhi,
    OXlo-ORhi-(Chi-Hlo),
    2*Hlo-Chi-OShi+OXlo,
    OSlo+OXlo-2*Chi,
    OElo+OXlo-(2*Hhi+Chi),
    Elo-OEhi
]
assert all(z>0 for z in overlap_checks)
print('R26_OPEN_OVERLAP_BOX = PASS',{'R':(float(ORlo),float(ORhi)),'x':(float(OXlo),float(OXhi)),'sigma':(float(OSlo),float(OShi)),'eps':(float(OElo),float(OEhi))})
print('ROUND26_HORIZON_GLUE_VERIFY = PASS')