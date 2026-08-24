#!/usr/bin/env python3
import math
from fractions import Fraction
import sympy as sp

# P12 Round 28 candidate verifier.
# Central next-shell double-horizon gap: exact J-symmetric 68x68 circuit.
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

Rlo,Rhi = Fraction(19,2000), Fraction(21,2000)
Ylo,Yhi = Fraction(-1,5000), Fraction(1,5000)
Slo,Shi = Fraction(119,2000), Fraction(121,2000)
Eplo,Ephi = Fraction(139,2000), Fraction(141,2000)

bounds = {
    H:(Hlo,Hhi), C:(Clo,Chi), Y:(Ylo,Yhi),
    R:(Rlo,Rhi), SIG:(Slo,Shi), EPS:(Eplo,Ephi), EE:(EElo,EEhi),
}

def qfrac(q0):
    q0 = sp.Rational(q0)
    return Fraction(int(q0.p), int(q0.q))

def affine_interval(expr):
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

def certify_positive(expr, label):
    lo,hi = affine_interval(expr)
    assert lo > 0, (label, float(lo), float(hi), sp.sstr(expr))
    return lo,hi

ambient_gap = [
    (R, 'R>0'),
    (EE-D-R, 'R<rho'),
    (X-R, 'R<x'),
    (SIG-R, 'R<sigma'),
    (EPS-SIG, 'sigma<epsilon'),
    (EE-EPS, 'epsilon<epsmax'),
    (SIG+X-K, 'Uminus_live: sigma+x>kappa'),
    (SIG-X-H, 'Uplus_live: sigma-x>eta'),
    (2*D-EPS-X, 'Vminus_horizon_illegal: epsilon+x<2delta'),
    (D+X-EPS, 'Vplus_horizon_illegal: epsilon-x<delta'),
    (SIG-2*H, 'separate_from_C26: sigma>2eta'),
]
for g,name in ambient_gap:
    certify_positive(g,name)
print('R28_DOUBLE_HORIZON_GAP_BOX = PASS')

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
selected68 = sources42 + extra26
assert len(selected68)==68 and len(set(selected68))==68

Vminus=(-1,4,4); Vplus=(1,4,3)
Uminus=(-1,5,1); Uplus=(1,5,0)
assert Vminus not in selected68 and Vplus not in selected68

def add(u,v): return tuple(u[i]+v[i] for i in range(3))
def neg(u): return tuple(-z for z in u)
def J(u):
    s,m,n=u
    return (-s,m,n+s)

assert all(J(s) in selected68 for s in selected68)
assert all(J(s) in sources42 for s in sources42)

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
    if not (0<u<t0+eps0):
        return None
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

Mbase,Vbase,_,Lbase = make_matrix(sources42,ref)
assert Mbase.shape==(42,44) and len(Lbase)==42
assert Uminus in Vbase and Uplus in Vbase
assert raw_row(Vminus,ref[1],ref[0],ref[2],ref[3]) is None
assert raw_row(Vplus,ref[1],ref[0],ref[2],ref[3]) is None
print('R28_BASE_DEFECT = PASS 42x44 with both U variables live and both V rows horizon-illegal')

M68,V68,rows68,L68 = make_matrix(selected68,ref)
assert M68.shape==(68,68) and len(L68)==68
assert len(V68)==68
assert (1,0,0) in V68 and (-1,0,1) in V68
assert all(J(v) in V68 for v in V68)
print('R28_M68_RAW_SHAPE = PASS 68x68')

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
min_margin=None; min_label=None
for g,label in raw_conditions:
    lo,hi=certify_positive(g,label)
    if min_margin is None or lo<min_margin:
        min_margin=lo; min_label=label
print('R28_BOX_PATTERN_CERTIFICATE = PASS',len(raw_conditions),
      'raw inequalities; min margin >',float(min_margin),min_label)

negS=[s for s in selected68 if s[0]==-1]
posS=[J(s) for s in negS]
negV=[v for v in V68 if v[0]==-1]
posV=[J(v) for v in negV]
assert len(negS)==len(posS)==len(negV)==len(posV)==34
rowmap={s:raw_row(s,xref,Rref,sref,eref) for s in selected68}
MJ=sp.Matrix([[rowmap[s].get(v,0) for v in negV+posV] for s in negS+posS])
A34=MJ[:34,:34]; B34=MJ[:34,34:]
assert MJ[34:,:34]==B34 and MJ[34:,34:]==A34
print('R28_M68_J_BLOCK = PASS 34+34')

I34=sp.eye(34)
Q=I34.row_join(I34).col_join(I34.row_join(-I34))
Qinv=sp.Rational(1,2)*Q
BD=sp.diag(A34+B34,A34-B34)
assert Qinv*MJ*Q == BD

Dp=sp.factor((A34+B34).det(method='domain-ge'))
Dm=sp.factor((A34-B34).det(method='domain-ge'))
Fp=sp.cancel(-Dp/(p**12*q*r**8))
Fm=sp.cancel(Dm/(p**12*q*r**8))
assert sp.denom(Fp)==1 and sp.denom(Fm)==1
assert sp.expand(Fm-Fp.subs(q,-q))==0
Pp=sp.Poly(sp.expand(Fp),p,q,r)
Pm=sp.Poly(sp.expand(Fm),p,q,r)
assert {sum(mon) for mon,coef in Pp.terms()}=={13}
assert {sum(mon) for mon,coef in Pm.terms()}=={13}

beta,v=sp.symbols('beta v', positive=True)
def normalize_inner(F):
    P=sp.Poly(sp.expand(F),p,q,r)
    out=0
    for (ep,eq,er),coef in P.terms():
        assert er%2==0
        out += coef*beta**eq*v**(er//2)
    return sp.expand(out)

Gp=normalize_inner(Fp)
Gm=normalize_inner(Fm)
assert sp.expand(Gm-Gp.subs(beta,-beta))==0
assert len(sp.Poly(Gp,beta,v).terms())==40

blo=Fraction('0.59460355750136053335')
bhi=Fraction('0.59460355750136053336')
assert blo**4 < Fraction(1,8) < bhi**4
sqrlo=Fraction('0.54433105395181735515')
sqrhi=Fraction('0.54433105395181735516')
assert sqrlo*sqrlo < Fraction(8,27) < sqrhi*sqrhi
l2lo2,l2hi2=ln_bounds_int(2,40)
l3lo2,l3hi2=ln_bounds_int(3,60)
vlo=(l3lo2/l2hi2)*sqrlo
vhi=(l3hi2/l2lo2)*sqrhi

def poly_interval(expr):
    P=sp.Poly(sp.expand(expr),beta,v)
    lo=Fraction(0); hi=Fraction(0)
    for (eb,ev),coef in P.terms():
        coef=int(coef)
        ml=blo**eb * vlo**ev
        mh=bhi**eb * vhi**ev
        if coef>=0:
            lo += coef*ml; hi += coef*mh
        else:
            lo += coef*mh; hi += coef*ml
    return lo,hi

Ip=poly_interval(Gp); Im=poly_interval(Gm)
assert Ip[0]>0 and Im[0]>0
print('R28_GPLUS_INTERVAL = PASS',(float(Ip[0]),float(Ip[1])))
print('R28_GMINUS_INTERVAL = PASS',(float(Im[0]),float(Im[1])))
print('R28_DET68_FACTOR = PASS det(M68)=-p^68*beta^2*v^8*Gplus(beta,v)*Gminus(beta,v) != 0')
print('ROUND28_NEXT_SHELL_HORIZON_VERIFY = PASS')
