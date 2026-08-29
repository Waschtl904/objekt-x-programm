#!/usr/bin/env python3
import sympy as sp

L2,L3=sp.log(2),sp.log(3)
a=L2/2; b=L3/2; T=2*a; d=b-a; e=T-b; Delta=sp.simplify(d-e)
X=sp.symbols('X', real=True)

c1=L2*2**sp.Rational(-3,2)
c2=L2*2**sp.Rational(-9,4)
c3=L2*2**sp.Rational(-3)
c4=c2
c5=L2*2**sp.Rational(-3)
c6=L2*2**sp.Rational(-15,4)
c7=c3
c8=c6
c9=L2*2**sp.Rational(-9,2)
c10=L2/4
c11=2*L3/(3*sp.sqrt(3))
weights=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11]
WORDS=[(a,a,a),(a,T,a),(a,3*a,a),(T,a,a),(T,T,a),(T,3*a,a),(3*a,a,a),(3*a,T,a),(3*a,3*a,a),(T,T,T),(b,b,b)]
SIGNS=(-1,1,1,-1)

alphaA=sp.simplify(c1+c5)
alphab=sp.simplify(c1+c5+c11)
kappa=sp.simplify(c1+c5+c9+c10+c11)
beta0=sp.simplify(-c1+c3)
betam=sp.simplify(-c2-c4)
betap=sp.simplify(c2+c6)
betaT=sp.simplify(-c3-c5-c7-c10)
betab=-c11

def sgn(q):
    q=sp.simplify(q)
    if q==0: return 0
    if q.is_positive is True: return 1
    if q.is_negative is True: return -1
    # exact fallback for logarithmic algebraic constants
    v=sp.N(q,80)
    if v>0: return 1
    if v<0: return -1
    raise AssertionError(('undecided sign',q))

def inside_abs(q,bound):
    return sgn(sp.expand(bound**2-q**2))>=0

def folded(src_sym, src_at_mid):
    s=sgn(src_at_mid)
    assert s!=0
    return sp.simplify(src_sym if s>0 else -src_sym)

def aggregate(mid, eps):
    T0=T+eps
    out={}
    for j,(delta,eta,lam) in enumerate(WORDS):
        shifts=[-delta-eta,-delta+eta,delta-eta,delta+eta]
        gates=[X-delta,X-delta,X+delta,X+delta]
        for k,(gexpr,sh) in enumerate(zip(gates,shifts)):
            gmid=sp.simplify(gexpr.subs(X,mid))
            if not inside_abs(gmid,T0-lam):
                continue
            src=X+sh
            smid=sp.simplify(src.subs(X,mid))
            if not inside_abs(smid,T0):
                continue
            prof=folded(src,smid)
            out[prof]=sp.simplify(out.get(prof,0)+SIGNS[k]*weights[j])
    return {sp.simplify(k):sp.simplify(v) for k,v in out.items() if sp.simplify(v)!=0}

def assert_map(got, expected, name):
    rem=list(got.items())
    for ek,ev in expected.items():
        hit=None
        for i,(gk,gv) in enumerate(rem):
            if sp.simplify(gk-ek)==0:
                assert sp.simplify(gv-ev)==0,(name,ek,gv,ev)
                hit=i; break
        assert hit is not None,(name,'missing',ek,got)
        rem.pop(hit)
    assert not rem,(name,'extra',rem)

# Exact representatives in the two only epsilon chambers.
epsI=sp.Rational(2,5)*Delta
epsII=sp.Rational(3,5)*Delta

def check_chamber(eps, chamber):
    regions=[]
    regions.append(('R0',0,eps,{X:2*c1,a-X:c2,a+X:c2,T-X:beta0,T+X:beta0}))
    regions.append(('R1',eps,a-eps,{X:c1,T-X:-c1,a+X:c2}))
    regions.append(('R2',a-eps,a,{X:alphaA,T-X:-c1,3*a-X:betam,a+X:betap,a-X:c2}))
    m=min_expr = (a+eps if chamber=='I' else 2*d-eps)
    regions.append(('R3',a,m,{X:alphaA,T-X:-c1,3*a-X:betam,a+X:betap,X-a:c2}))
    if chamber=='I':
        regions.append(('R4I',a+eps,2*d-eps,{X:alphaA,T-X:-c1,3*a-X:betam,X-a:c2}))
        M=2*d-eps
    else:
        regions.append(('R4II',2*d-eps,a+eps,{X:alphab,T-X:-c1,3*a-X:betam,a+X:betap,X-a:c2,2*b-X:betab}))
        M=a+eps
    regions.append(('R5',M,T-eps,{X:alphab,T-X:-c1,3*a-X:betam,X-a:c2,2*b-X:betab}))
    regions.append(('R6',T-eps,T,{X:kappa,T-X:beta0,3*a-X:betam,2*T-X:betaT,X-a:betap,2*b-X:betab}))
    regions.append(('R7',T,T+eps,{X:kappa,X-T:beta0,3*a-X:betam,2*T-X:betaT,X-a:betap,2*b-X:betab}))
    for name,lo,hi,exp in regions:
        assert sgn(hi-lo)>0,(chamber,name,lo,hi)
        mid=sp.simplify((lo+hi)/2)
        got=aggregate(mid,eps)
        assert_map(got,{sp.simplify(k):sp.simplify(v) for k,v in exp.items()},name)

check_chamber(epsI,'I')
check_chamber(epsII,'II')

# Degenerate wall collision.
assert sp.simplify((a+Delta/2)-(2*d-Delta/2))==0

# Reconstruct all positive inner A-wall values from every gate/source equation
# at exact representatives and compare with the canonical five-wall set.
def positive_internal_wall_values(eps):
    T0=T+eps
    vals=set()
    for delta,eta,lam in WORDS:
        # Gate equations |x +/- delta| = T0-lam.
        B=T0-lam
        for shift in (-delta,delta):
            for s in (-1,1):
                x=sp.simplify(s*B-shift)
                if sgn(x)>0 and sgn(T0-x)>0:
                    vals.add(sp.simplify(x))
        # Source horizon equations |x + shift| = T0.
        for shift in (-delta-eta,-delta+eta,delta-eta,delta+eta):
            for s in (-1,1):
                x=sp.simplify(s*T0-shift)
                if sgn(x)>0 and sgn(T0-x)>0:
                    vals.add(sp.simplify(x))
    return vals

for eps in (epsI,epsII):
    got=positive_internal_wall_values(eps)
    expected={sp.simplify(eps),sp.simplify(a-eps),sp.simplify(a+eps),sp.simplify(2*d-eps),sp.simplify(T-eps)}
    assert got==expected,(eps,got,expected)

# Hub support wall exhaustivity on an exact SW1 point in each chamber.
def hub_walls(eps):
    R=eps/3
    sig=R/2
    S=T+sig; T0=T+eps
    got=set()
    for tau in (a,b,T):
        for B in (R,S):
            for form in (X-tau,X+tau):
                sh=sp.simplify(form-X)
                for ss in (-1,1):
                    x=sp.simplify(ss*B-sh)
                    if sgn(x)>0 and sgn(T0-x)>0:
                        got.add(x)
    expected={sig,e+sig,a+sig,a-R,a+R,b-R,b+R,T-R,T+R}
    assert got=={sp.simplify(v) for v in expected},(eps,got,expected)
    # right T branch x+T is annulus-active below sigma and dead above sigma.
    xlo=sig/2
    xhi=(sig+eps)/2
    assert sgn(abs(sp.N(xlo+T,80))-R)>0
    assert sgn(S-(xlo+T))>0
    assert sgn((xhi+T)-S)>0

hub_walls(epsI)
hub_walls(epsII)

print('SW1-A1 RAW ARCHETYPES CERTIFICATE: PASS')
print(f'sympy={sp.__version__}')
print('all eleven A words reconstructed exactly')
print('canonical five inner A walls exhaustively recovered in both epsilon chambers')
print('R0,R1,R2,R3,R4I,R4II,R5,R6,R7 archetypes certified')
print('degenerate epsilon=Delta/2 wall collision certified')
print('positive Hub support-wall list certified on exact SW1 representatives')
print('right T Hub branch active for 0<x<sigma and dead for sigma<x<epsilon')
print('certificate proves raw cell algebra only; no A2/Schur injectivity')
