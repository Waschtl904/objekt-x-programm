#!/usr/bin/env python3
from fractions import Fraction
import sympy as sp

# P12 Round 29 candidate verifier.
# Backward/invariant step: the promoted M68 raw block is epsilon-invariant
# across both V-horizon walls on a fixed J-symmetric base box.
# Candidate only. No promotion. P11 FROZEN; R14 unchanged.


def ln_bounds_int(xint, N):
    z = Fraction(xint - 1, xint + 1)
    s = Fraction(0)
    for k in range(N + 1):
        s += z ** (2*k + 1) / Fraction(2*k + 1)
    lo = 2*s
    tail = 2*z ** (2*N + 3) / Fraction(2*N + 3) / (1-z*z)
    return lo, lo + tail

l2lo,l2hi = ln_bounds_int(2,120)
l3lo,l3hi = ln_bounds_int(3,180)
l5lo,l5hi = ln_bounds_int(5,500)
Hlo,Hhi = (8*l2lo-5*l3hi)/2, (8*l2hi-5*l3lo)/2
Clo,Chi = (7*l3lo-11*l2hi)/2, (7*l3hi-11*l2lo)/2
EElo,EEhi = l5lo/2-l2hi, l5hi/2-l2lo
assert Hlo > 0 and Clo > Hhi and EElo > Hhi + Chi

H,C,Y,R,SIG,EPS,EE = sp.symbols('H C Y R SIG EPS EE', real=True)
D = H + C
K = 2*H + C
X = D/2 + Y
TS = 14*H + 10*C
ES = 3*H + 2*C
RHO = EE-D

Rlo,Rhi = Fraction(19,2000), Fraction(21,2000)
Ylo,Yhi = Fraction(-1,5000), Fraction(1,5000)
Slo,Shi = Fraction(119,2000), Fraction(121,2000)
Eplo,Ephi = Fraction(139,2000), Fraction(11,100)

base_bounds = {
    H:(Hlo,Hhi), C:(Clo,Chi), Y:(Ylo,Yhi),
    R:(Rlo,Rhi), SIG:(Slo,Shi), EPS:(Eplo,Ephi), EE:(EElo,EEhi),
}

def qfrac(q0):
    q0 = sp.Rational(q0)
    return Fraction(int(q0.p), int(q0.q))

def affine_interval(expr, bounds=base_bounds):
    ex = sp.expand(expr)
    rem = ex
    lo = hi = Fraction(0)
    for z,(bl,bh) in bounds.items():
        a = ex.coeff(z)
        rem = sp.expand(rem-a*z)
        aa = qfrac(a)
        if aa >= 0:
            lo += aa*bl; hi += aa*bh
        else:
            lo += aa*bh; hi += aa*bl
    rem = sp.Rational(rem)
    cc = qfrac(rem)
    return lo+cc, hi+cc

def certify_positive(expr,label,bounds=base_bounds):
    lo,hi = affine_interval(expr,bounds)
    assert lo > 0, (label,float(lo),float(hi),sp.sstr(expr))
    return lo,hi

def certify_negative(expr,label,bounds=base_bounds):
    lo,hi = affine_interval(expr,bounds)
    assert hi < 0, (label,float(lo),float(hi),sp.sstr(expr))
    return lo,hi

ambient = [
    (R,'R>0'),
    (RHO-R,'R<rho'),
    (X-R,'R<x'),
    (SIG-R,'R<sigma'),
    (EPS-SIG,'sigma<epsilon'),
    (EE-EPS,'epsilon<epsmax'),
    (SIG+X-K,'Uminus live'),
    (SIG-X-H,'Uplus live'),
    (SIG-2*H,'sigma>2eta'),
]
for g,name in ambient:
    certify_positive(g,name)
print('R29_BRIDGE_AMBIENT = PASS')

HVminus = EPS + X - 2*D
HVplus  = EPS - X - D

low_bounds = dict(base_bounds)
low_bounds[EPS] = (Fraction(139,2000),Fraction(141,2000))
certify_negative(HVminus,'B28 low: Vminus illegal',low_bounds)
certify_negative(HVplus,'B28 low: Vplus illegal',low_bounds)
print('R29_LOW_SLICE_B28 = PASS')

minus_only = dict(base_bounds)
minus_only[Y] = (Fraction(1,10000),Fraction(1,5000))
minus_only[EPS] = (Fraction(883,10000),Fraction(221,2500))
certify_positive(HVminus,'single-V minus legal',minus_only)
certify_negative(HVplus,'single-V plus illegal',minus_only)

plus_only = dict(base_bounds)
plus_only[Y] = (Fraction(-1,5000),Fraction(-1,10000))
plus_only[EPS] = (Fraction(883,10000),Fraction(221,2500))
certify_negative(HVminus,'single-V minus illegal',plus_only)
certify_positive(HVplus,'single-V plus legal',plus_only)
print('R29_SINGLE_V_WITNESSES = PASS')

c44_bounds = dict(base_bounds)
c44_bounds[EPS] = (Fraction(181,2000),Fraction(1,10))
C44 = [
    R, RHO-R,
    X-R, D-R-X,
    X-(C-R), H+R-X,
    SIG-(K-X), SIG-(X+H),
    (2*D-X)-SIG, (X+D)-SIG,
    EPS-(2*D-X), EPS-(X+D),
    EPS-SIG, EE-EPS,
]
for i,g in enumerate(C44):
    certify_positive(g,f'C44[{i}]',c44_bounds)
print('R29_HIGH_SLAB_IN_C44 = PASS')

p,q,r = sp.symbols('p q r', positive=True, nonzero=True)
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
(1,5,0),
]
extra26=[
(-1,-1,3),(-1,0,3),(-1,0,4),(-1,1,-1),(-1,1,4),
(-1,2,-2),(-1,2,-1),(-1,2,5),(-1,3,-1),(-1,3,5),
(-1,3,6),(-1,4,-1),(-1,5,0),
(1,-1,2),(1,0,2),(1,0,3),(1,1,-2),(1,1,3),
(1,2,-3),(1,2,-2),(1,2,4),(1,3,-2),(1,3,4),
(1,3,5),(1,4,-2),(1,5,-1),
]
selected68=sources42+extra26
Vminus=(-1,4,4); Vplus=(1,4,3)
assert len(selected68)==68 and len(set(selected68))==68
assert Vminus not in selected68 and Vplus not in selected68

def add(u,v): return tuple(u[i]+v[i] for i in range(3))
def neg(u): return tuple(-z for z in u)
def J(u):
    s,m,n=u
    return (-s,m,n+s)
assert all(J(s) in selected68 for s in selected68)

h0=(float(Hlo)+float(Hhi))/2
c0=(float(Clo)+float(Chi))/2
d0=h0+c0
e0=3*h0+2*c0
t0=14*h0+10*c0
ref=(0.010,d0/2,0.060,0.070)

def aval(u,x0):
    s,m,n=u
    return s*x0+m*e0+n*d0

def raw_row(src,x0,R0,sigma0,eps0):
    u=aval(src,x0)
    if not (0<u<t0+eps0): return None
    row={}
    for _,sh,k in shifts:
        for pm,sgn in [(-1,+1),(+1,-1)]:
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            coeff=sgn*k
            av=aval(arg,x0)
            if av<0:
                arg=neg(arg); av=-av; coeff=-coeff
            if R0<av<t0+sigma0:
                row[arg]=sp.expand(row.get(arg,0)+coeff)
    return {v:sp.factor(c) for v,c in row.items() if sp.simplify(c)!=0}

def make_matrix(sources,pt):
    R0,x0,sigma0,eps0=pt
    rows=[raw_row(s,x0,R0,sigma0,eps0) for s in sources]
    legal=[i for i,rr in enumerate(rows) if rr is not None]
    vars_=sorted(set().union(*(set(rows[i]) for i in legal)))
    M=sp.zeros(len(legal),len(vars_))
    for ii,i in enumerate(legal):
        for v,c in rows[i].items():
            M[ii,vars_.index(v)] = c
    return M,vars_,rows,legal

M68,V68,rows68,L68=make_matrix(selected68,ref)
assert M68.shape==(68,68) and len(L68)==68 and len(V68)==68
assert all(J(v) in V68 for v in V68)
print('R29_PROMOTED_M68_REFERENCE = PASS 68x68')

def aff_sym(u):
    s,m,n=u
    return sp.expand(s*X + m*ES + n*D)

raw_conditions=[]
Rref,xref,sref,eref=ref
for src in selected68:
    u=aff_sym(src)
    raw_conditions.append((u,('source_lower',src)))
    raw_conditions.append((TS+EPS-u,('source_upper',src)))
    for shname,sh,_ in shifts:
        for pm in (-1,+1):
            arg0=add(src,(0,pm*sh[1],pm*sh[2]))
            vv=aff_sym(arg0)
            vref=aval(arg0,xref)
            sign=1 if vref>0 else -1
            w=sp.expand(sign*vv)
            raw_conditions.append((w,('slot_sign',src,shname,pm,arg0,sign)))
            avref=abs(vref)
            if Rref<avref<t0+sref:
                raw_conditions.append((w-R,('live_lower',src,shname,pm,arg0,sign)))
                raw_conditions.append((TS+SIG-w,('live_upper',src,shname,pm,arg0,sign)))
            elif avref<Rref:
                raw_conditions.append((R-w,('dead_lower',src,shname,pm,arg0,sign)))
            else:
                raw_conditions.append((w-TS-SIG,('dead_upper',src,shname,pm,arg0,sign)))

assert len(raw_conditions)==1204
eps_dependent=[(g,label) for g,label in raw_conditions if sp.expand(g).coeff(EPS)!=0]
assert len(eps_dependent)==68
assert all(sp.expand(g).coeff(EPS)==1 and label[0]=='source_upper' for g,label in eps_dependent)
assert all(sp.expand(g-HVminus)!=0 and sp.expand(g-HVplus)!=0 for g,label in raw_conditions)
print('R29_HORIZON_WALL_INVARIANT = PASS Vminus/Vplus walls absent from M68 raw events')

min_margin=None; min_label=None
for g,label in raw_conditions:
    lo,hi=certify_positive(g,label)
    if min_margin is None or lo<min_margin:
        min_margin=lo; min_label=label
print('R29_BRIDGE_PATTERN_CERTIFICATE = PASS',len(raw_conditions),
      'raw inequalities; min margin >',float(min_margin),min_label)

rep_points=[
    ('both_illegal',(0.010,d0/2,0.060,0.070)),
    ('minus_only',(0.010,d0/2+0.00015,0.060,0.08835)),
    ('plus_only',(0.010,d0/2-0.00015,0.060,0.08835)),
    ('both_legal',(0.010,d0/2,0.060,0.095)),
]
for name,pt in rep_points:
    MM,VV,rr,ll=make_matrix(selected68,pt)
    assert MM==M68 and VV==V68 and len(ll)==68
print('R29_ALL_HORIZON_ORIENTATIONS_SAME_M68 = PASS')

print('R29_EPSILON_BRIDGE = PASS B28 -> single-V cells -> C44 high slab')
print('ROUND29_EPSILON_BRIDGE_VERIFY = PASS')
