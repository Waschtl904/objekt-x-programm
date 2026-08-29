#!/usr/bin/env python3
import sympy as sp

s, eps = sp.symbols("s eps", real=True)
L2,L3=sp.log(2),sp.log(3)
a=L2/2
b=L3/2
T=2*a
d=b-a
e=T-b
Delta=sp.simplify(d-e)
C=sp.simplify(a+e)
t=sp.simplify(Delta-s)
T0=T+eps

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
alphab=sp.simplify(c1+c5+c11)
betam=sp.simplify(-2*c2)
betab=-c11

WORDS=[(1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),(6,T,3*a,a),
       (7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),(10,T,T,T),(11,b,b,b)]
SIGNS=(-1,1,1,-1)

VK=[{s:0,eps:Delta},{s:Delta/2,eps:Delta/2},{s:Delta/2,eps:Delta}]

def vals(expr):
    return [sp.simplify(sp.expand(expr).subs(v)) for v in VK]
def nn(expr):
    return all(v.is_nonnegative is True for v in vals(expr))
def pos(expr):
    expr=sp.expand(expr)
    return expr!=0 and nn(expr)
def absclass(expr,bound):
    if nn(bound-expr) and nn(bound+expr): return "IN"
    if pos(expr-bound) or pos(-expr-bound): return "OUT"
    return "MIX"
def profile(expr):
    if pos(expr): return sp.simplify(expr)
    if pos(-expr): return sp.simplify(-expr)
    if sp.simplify(expr)==0: return sp.Integer(0)
    raise AssertionError(("profile sign switch",expr,vals(expr)))
def aggregate(x):
    out={}
    for j,delta,eta,lam in WORDS:
        gm=absclass(x-delta,T0-lam)
        gp=absclass(x+delta,T0-lam)
        assert gm!="MIX" and gp!="MIX",(x,j,gm,gp)
        gates=[gm,gm,gp,gp]
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        for k,(gate,q) in enumerate(zip(gates,src)):
            if gate=="OUT": continue
            hc=absclass(q,T0)
            assert hc!="MIX",(x,j,k+1,q)
            if hc=="IN":
                p=profile(q)
                out[p]=sp.simplify(out.get(p,0)+SIGNS[k]*weights[j-1])
    return {k:sp.simplify(v) for k,v in out.items() if sp.simplify(v)!=0}

assert sp.simplify(e+s-(d-t))==0
assert sp.simplify(d-s-(e+t))==0
assert sp.simplify(b-s-(C+t))==0
assert sp.simplify(C+s-(b-t))==0

X=[
 sp.simplify(e-s), sp.simplify(e+s), sp.simplify(d-s), sp.simplify(d+s),
 sp.simplify(b-s), sp.simplify(b+s), sp.simplify(C-s), sp.simplify(C+s),
 sp.simplify(e-t), sp.simplify(d+t), sp.simplify(b+t), sp.simplify(C-t),
]
for i in range(12):
    for j in range(i):
        assert sp.simplify(X[i]-X[j])!=0

lo=Delta-eps
hi=Delta/2
def image_interval(expr):
    slope=sp.simplify(sp.diff(expr,s))
    assert slope in (1,-1)
    if slope==1:
        return sp.simplify(expr.subs(s,lo)),sp.simplify(expr.subs(s,hi))
    return sp.simplify(expr.subs(s,hi)),sp.simplify(expr.subs(s,lo))
intervals=[image_interval(x) for x in X]
order=[8,0,1,2,3,9,11,6,7,4,5,10]
VE=[{eps:Delta/2},{eps:Delta}]
def eps_nn(expr):
    return all(sp.simplify(expr.subs(v)).is_nonnegative is True for v in VE)
for i,j in zip(order,order[1:]):
    assert eps_nn(sp.expand(intervals[j][0]-intervals[i][1]))

M=sp.zeros(12)
ext={}
for i,x in enumerate(X):
    M[i,i]+=1
    for q,coef in aggregate(x).items():
        hit=None
        for j,y in enumerate(X):
            if sp.simplify(q-y)==0:
                hit=j; break
        if hit is None:
            ext.setdefault(sp.simplify(q),[]).append((i,sp.simplify(coef)))
        else:
            M[i,hit]=sp.simplify(M[i,hit]+coef)

assert M==M.T
Qs=sp.simplify(b+Delta+s)
Qt=sp.simplify(b+Delta+t)
assert len(ext)==2
assert Qs in ext and Qt in ext
assert ext[Qs]==[(6,betab)]
assert ext[Qt]==[(11,betab)]

ME=sp.zeros(12)
def row(i,dct):
    for j,v in dct.items(): ME[i,j]=v
row(0,{0:1+c1,5:-c1,6:c2})
row(1,{1:1+c1,4:-c1,7:c2})
row(2,{2:1+c1,7:-c1,4:c2})
row(3,{3:1+c1,6:-c1,5:c2})
row(4,{4:1+alphab,1:-c1,7:betam,2:c2,5:betab})
row(5,{5:1+alphab,0:-c1,6:betam,3:c2,4:betab})
row(6,{6:1+alphab,3:-c1,5:betam,0:c2})
row(7,{7:1+alphab,2:-c1,4:betam,1:c2,10:betab})
row(8,{8:1+c1,10:-c1,11:c2})
row(9,{9:1+c1,11:-c1,10:c2})
row(10,{10:1+alphab,8:-c1,11:betam,9:c2,7:betab})
row(11,{11:1+alphab,9:-c1,10:betam,8:c2})
assert M==ME

pairs=[(0,8),(1,2),(3,9),(4,7),(5,10),(6,11)]
P=sp.zeros(12)
for i,j in pairs:
    P[i,j]=1
    P[j,i]=1
assert P*P==sp.eye(12)
assert P*M==M*P

def block(sig):
    B=sp.zeros(6)
    for r,(i,ip) in enumerate(pairs):
        for c,(j,jp) in enumerate(pairs):
            B[r,c]=sp.simplify(M[i,j]+sig*M[i,jp])
    return B
Bp=block(1)
Bm=block(-1)

def expected_block(sig):
    return sp.Matrix([
      [1+c1,0,0,0,-c1,c2],
      [0,1+c1,0,-c1+sig*c2,0,0],
      [0,0,1+c1,0,c2,-c1],
      [0,-c1+sig*c2,0,1+alphab-2*sig*c2,-c11,0],
      [-c1,0,c2,-c11,1+alphab,-2*c2],
      [c2,0,-c1,0,-2*c2,1+alphab],
    ])
assert all(sp.simplify(Bp[i,j]-expected_block(1)[i,j])==0 for i in range(6) for j in range(6))
assert all(sp.simplify(Bm[i,j]-expected_block(-1)[i,j])==0 for i in range(6) for j in range(6))
assert Bp.is_positive_definite is True
assert Bm.is_positive_definite is True
assert sp.simplify(sp.Rational(1,2)-c11).is_positive is True

print("SW1-DELTA-DESCENT STAGE-9 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("16 nominal profiles quotient to exactly 12 physical channels")
print("12 channel image intervals are disjoint up to endpoints on half-orbit K")
print("only external profiles are Q_s and Q_t, each with beta_b")
print("12x12 compression is symmetric and commutes with reflection")
print("both exact 6x6 reflection blocks are positive definite")
print("c11<1/2 certified; analytic proof gives nu_±>1/2 from B_±>=I")
