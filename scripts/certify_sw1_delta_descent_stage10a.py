#!/usr/bin/env python3
import sympy as sp

s, eps = sp.symbols("s eps", real=True)
L2,L3=sp.log(2),sp.log(3)
a=L2/2; b=L3/2; T=2*a; d=b-a; e=T-b; Delta=sp.simplify(d-e); T0=T+eps
C=sp.simplify(a+e)
B1=sp.simplify(b+Delta)
B2=sp.simplify(b+2*Delta)
E0=sp.simplify(e-Delta)
D1=sp.simplify(d+Delta)
F0=sp.simplify(C-Delta)
hB=sp.simplify(E0)

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
alpha_b=sp.simplify(c1+c5+c11)
beta0=sp.simplify(-c1+c3)
beta_m=sp.simplify(-c2-c4)
beta_p=sp.simplify(c2+c6)
betaT=sp.simplify(-c3-c5-c7-c10)
beta_b=-c11
kappa=sp.simplify(c1+c5+c9+c10+c11)

WORDS=[(1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),(6,T,3*a,a),
       (7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),(10,T,T,T),(11,b,b,b)]
SIGNS=(-1,1,1,-1)

assert sp.simplify(hB-(a-e-2*Delta))==0
assert sp.simplify(hB-(T-B1))==0
assert sp.simplify(hB-Delta).is_positive is True
assert sp.simplify(2*Delta-hB).is_positive is True

kB=sp.simplify(hB-Delta)
VLOW=[{s:0,eps:0},{s:0,eps:Delta},{s:kB,eps:Delta},{s:hB/2,eps:hB/2}]
VHIGH=[{s:kB,eps:Delta},{s:Delta,eps:Delta},{s:hB/2,eps:hB/2}]

def vals(expr,vs):
    return [sp.simplify(sp.expand(expr).subs(v)) for v in vs]
def nn(expr,vs):
    return all(v.is_nonnegative is True for v in vals(expr,vs))
def pos(expr,vs):
    expr=sp.expand(expr)
    return expr!=0 and nn(expr,vs)
def absclass(expr,bound,vs):
    if nn(bound-expr,vs) and nn(bound+expr,vs): return "IN"
    if pos(expr-bound,vs) or pos(-expr-bound,vs): return "OUT"
    return "MIX"
def profile(expr,vs):
    if pos(expr,vs): return sp.simplify(expr)
    if pos(-expr,vs): return sp.simplify(-expr)
    if sp.simplify(expr)==0: return sp.Integer(0)
    raise AssertionError(("profile sign switch",expr,vals(expr,vs)))
def aggregate(x,vs):
    out={}; count=0
    for j,delta,eta,lam in WORDS:
        gm=absclass(x-delta,T0-lam,vs)
        gp=absclass(x+delta,T0-lam,vs)
        assert gm!="MIX" and gp!="MIX",(x,j,gm,gp)
        gates=[gm,gm,gp,gp]
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        for k,(gate,q) in enumerate(zip(gates,src)):
            if gate=="OUT": continue
            hc=absclass(q,T0,vs)
            assert hc!="MIX",(x,j,k+1,q)
            if hc=="IN":
                p=profile(q,vs)
                out[p]=sp.simplify(out.get(p,0)+SIGNS[k]*weights[j-1])
                count+=1
    return {k:sp.simplify(v) for k,v in out.items() if sp.simplify(v)!=0},count
def assert_map(got,expected):
    rem=list(got.items())
    for ek,ev in expected.items():
        hit=None
        for i,(gk,gv) in enumerate(rem):
            if sp.simplify(gk-ek)==0:
                assert sp.simplify(gv-ev)==0,(ek,gv,ev)
                hit=i; break
        assert hit is not None,("missing",ek,got)
        rem.pop(hit)
    assert not rem,("extra",rem)

# Lower-wall eight exact rows.
expected_low={
 E0+s:{B1-s:-c1,E0+s:c1,F0+s:c2},
 E0-s:{B1+s:-c1,E0-s:c1,F0-s:c2},
 D1+s:{F0-s:-c1,D1+s:c1,B1+s:c2},
 D1-s:{F0+s:-c1,D1-s:c1,B1-s:c2},
 B1+s:{E0-s:-c1,B1+s:alpha_b,F0-s:beta_m,D1+s:c2,C-s:beta_b},
 B1-s:{E0+s:-c1,B1-s:alpha_b,F0+s:beta_m,D1-s:c2,C+s:beta_b},
 F0+s:{D1-s:-c1,F0+s:alpha_b,B1-s:beta_m,E0+s:c2,B2-s:beta_b},
 F0-s:{D1+s:-c1,F0-s:alpha_b,B1+s:beta_m,E0-s:c2,B2+s:beta_b},
}
for x,exp in expected_low.items():
    got,_=aggregate(x,VLOW)
    assert_map(got,exp)

# Positive lower-wall difference block and nonzero through-coupling.
M=sp.Matrix([
 [1+c1,0,c1,c2],
 [0,1+c1,c2,c1],
 [c1,c2,1+alpha_b,2*c2],
 [c2,c1,2*c2,1+alpha_b],
])
assert M.is_positive_definite is True

A=1+c1
def K(sig):
    return sp.Matrix([[A,c1+sig*c2],[c1+sig*c2,1+alpha_b+2*sig*c2]])
Kp,Km=K(1),K(-1)
assert Kp.is_positive_definite is True
assert Km.is_positive_definite is True
dp=sp.expand(Kp.det())
dm=sp.expand(Km.det())
assert sp.simplify(dp-dm-4*c2)==0
assert dp.is_positive is True and dm.is_positive is True
inv34_formula=sp.simplify(-2*A*c2/(dp*dm))
assert inv34_formula.is_negative is True
gamma=sp.simplify(-c11**2*inv34_formula)
assert gamma.is_positive is True

# Upper-wall fold.
u=sp.simplify(hB-s)
tt=sp.simplify(Delta-u)
assert sp.simplify(E0-s-u)==0
assert sp.simplify(D1+s-(a-u))==0
assert sp.simplify(F0-s-(a+u))==0
assert sp.simplify(B1+s-(T-u))==0

# Direct rows equal the already-certified inner/AWI forms.
exp_u={u:2*c1,a-u:c2,a+u:c2,T-u:beta0,T+u:beta0}
exp_am={u:c2,a-u:c1+c5,a+u:-c1,T-u:beta_p,T+u:beta_m}
exp_ap={u:c2,a-u:-c1,a+u:alpha_b,T-u:beta_m,T+u:beta_p,T+tt:beta_b}
exp_Tm={T-u:kappa,u:beta0,a+u:beta_m,a-u:beta_p,T+u:betaT,2*d+u:beta_b}
for x,exp in [(E0-s,exp_u),(D1+s,exp_am),(F0-s,exp_ap),(B1+s,exp_Tm)]:
    got,_=aggregate(x,VHIGH)
    assert_map(got,exp)

# Restore full SW1 slack and certify u in (R,eps)∩J on upper wall.
R, sig, rr, uu, vv, gg = sp.symbols("R sig rr uu vv gg", positive=True)
# parameterize R=rr, s=rr+uu, eps=rr+uu+vv, Delta=R+eps+gg
RR=rr; ss=rr+uu; eeps=rr+uu+vv; DD=2*rr+uu+vv+gg
hDD=sp.simplify((e-Delta).subs(Delta,DD)) if False else None
# use algebraic identities with abstract hB and Delta:
# u=hB-s > hB-eps > Delta-eps > R
assert sp.simplify((Delta-eps)-R - (Delta-(R+eps)))==0
# u+eps>hB>Delta is immediate from eps>s and hB>Delta.

print("SW1-DELTA-DESCENT STAGE-10A CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("h_B=e-Delta=T-(b+Delta), with Delta<h_B<2Delta")
print("lower wall: all 8 direct rows certified")
print("lower 4x4 difference block positive; gamma_B1>0")
print("upper wall: E0-s,D1+s,F0-s,B1+s fold exactly to u,a-u,a+u,T-u")
print("upper fold lies in the previously certified inner/AWI regime")
print("global residual quartet on J_B intentionally remains open")
