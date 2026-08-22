"""
Round 14 full b2d-core-both verifier.

Independent layers:
1. symbolic triangular closing residual;
2. polynomial row-multiplier certificate;
3. 20,000-point horizon/support-pattern stress over sharp cases B/C;
4. independent reconstruction of all 13 reduced rows directly from the
   six raw slots u±a,u±b,u±T, including anti-reflection.

This is verification support for P12_A15_1b2d_CoreBothClosure.tex.
"""

import math
import random
import sympy as sp

a0 = math.log(2)/2
b0 = math.log(3)/2
T0 = 2*a0
d0 = b0-a0
e0 = T0-b0
delta0 = d0-e0
epsmax = 0.5*math.log(5/4)

p0 = math.sqrt(math.log(2))*2**(-3/4)
r0 = math.sqrt(math.log(3))*3**(-3/4)
q0 = math.sqrt(math.log(2))*2**(-3/2)

def add(t1,t2):
    return tuple(u+v for u,v in zip(t1,t2))

def neg(t):
    return tuple(-u for u in t)

def aval(t,x):
    return t[0]*x+t[1]*e0+t[2]*delta0

A=(0,2,1)
B=(0,3,2)
TT=(0,4,2)

p,q,r=sp.symbols("p q r", positive=True, nonzero=True)
Delta=p**2-q**2

names=[
    "y","yD","amx","twoDmx","bmx","Tdelmx","Tpy",
    "x","xkap","epx","twoepx","apx","lY","H_x",
]
V=sp.symbols(" ".join(names))
(y,yD,amx,twoDmx,bmx,Tdelmx,Tpy,
 x,xkap,epx,twoepx,apx,lY,Hx)=V
Hy=Tpy

Qrows=[
    -p*epx-p*bmx-r*apx-r*Tdelmx-q*lY-q*Hy,
    -p*Tdelmx-r*epx-q*twoepx,
    p*y-p*Hy-r*x-q*epx,
    p*yD-q*xkap,
    p*amx-q*x,
    p*twoDmx+r*y,
    p*bmx+r*amx+q*y,
    -p*y-p*lY-r*twoDmx-r*Hx-q*bmx,
    p*x-p*Hx-r*y-q*amx,
    p*xkap-q*yD,
    p*epx-q*y,
    p*twoepx+r*xkap,
    p*apx+r*epx+q*x,
]

subs={
    yD:0,
    xkap:0,
    twoepx:0,
    epx:q/p*y,
    Tdelmx:-r*q/p**2*y,
    twoDmx:-r/p*y,
    amx:q/p*x,
    apx:-q/p*x-r*q/p**2*y,
    bmx:-r*q/p**2*x-q/p*y,
    Hy:Delta/p**2*y-r/p*x,
    Hx:Delta/p**2*x-r/p*y,
    lY:-r*(p**2-2*q**2)/p**3*x-(Delta-2*r**2)/p**2*y,
}

closing=sp.factor(Qrows[0].subs(subs))
target_closing=2*q*r*(2*p**2-q**2)/p**3*x
print("TRIANGULAR_Q1_CLOSING =",closing)
assert sp.simplify(closing-target_closing)==0

C=[
    p**3*Delta,
    -p**2*r*Delta,
    -p**2*q*Delta,
    p*q**2*r**2,
    -r*Delta*(p**2-2*q**2),
    -p*q*r*Delta,
    p*Delta**2,
    -p**2*q*Delta,
    p*q*r*Delta,
    p**2*q*r**2,
    p*Delta*(Delta-2*r**2),
    -p*q*r*Delta,
    p**2*r*Delta,
]
cert=sp.factor(sum(c*row for c,row in zip(C,Qrows)))
target_cert=2*q*r*Delta*(2*p**2-q**2)*x
print("ROW_CERTIFICATE_MINUS_TARGET =",sp.factor(cert-target_cert))
assert sp.simplify(cert-target_cert)==0

shifts_num=[(A,p0),(B,r0),(TT,q0)]
sources=[
    (-1,1,1), (-1,2,2), (-1,3,2), (-1,3,3),
    (-1,4,2), (-1,4,3), (-1,5,3),
    (1,1,0), (1,2,1), (1,3,0), (1,3,1),
    (1,4,1), (1,4,2),
]

def numeric_pattern(src,xnum,R,sigma,eps):
    u=aval(src,xnum)
    assert 0<u<T0+eps
    live=[]
    for sh,k in shifts_num:
        for sign in (-1,+1):
            arg=add(src,(0,sign*sh[1],sign*sh[2]))
            av=aval(arg,xnum)
            if av<0:
                arg=neg(arg)
                av=-av
            if R<av<T0+sigma:
                live.append(arg)
    return frozenset(live)

Rref=0.08
sigref=0.105
xref=d0/2+0.001
epsref=0.11
reference=[numeric_pattern(s,xref,Rref,sigref,epsref) for s in sources]

random.seed(20260822)
nB=nC=0
for _ in range(20000):
    R=random.uniform(e0/2+1e-8,d0/2-1e-8)
    sigma=random.uniform(d0/2+1e-8,epsmax-1e-8)
    lo=max(R,d0-sigma)
    hi=min(sigma,d0-R)
    if hi<=lo+1e-10:
        continue
    xnum=random.uniform(lo+1e-10,hi-1e-10)
    eps=random.uniform(sigma+1e-9,epsmax-1e-9)
    pats=[numeric_pattern(s,xnum,R,sigma,eps) for s in sources]
    assert pats==reference
    if sigma<=d0-R:
        nB+=1
    else:
        nC+=1
print("RANDOM_PATTERN_STRESS = PASS",nB,nC)

pS,qS,rS=sp.symbols("p q r", nonzero=True)
shifts=[(A,pS,"a"),(B,rS,"b"),(TT,qS,"T")]

varmap={
    (-1,1,1): "h(y)",
    (-1,1,2): "h(y+delta)",
    (-1,2,1): "h(a-x)",
    (-1,2,2): "h(2d-x)",
    (-1,3,2): "h(b-x)",
    (-1,4,3): "h(T+delta-x)",
    (-1,5,3): "H(y)",
    (1,0,0): "h(x)",
    (1,1,-1): "h(x+kappa)",
    (1,1,0): "h(e+x)",
    (1,2,0): "h(2e+x)",
    (1,2,1): "h(a+x)",
    (1,3,1): "l(y)",
    (1,4,2): "H(x)",
}

R=0.08
sigma=0.105
epsilon=0.11
x0=d0/2+1e-3
S=T0+sigma
horizon=T0+epsilon

def raw_reduce(src):
    u=aval(src,x0)
    assert 0<u<horizon
    sparse={}
    for sh,k,sname in shifts:
        for pm,coeff_sign in [(-1,+1),(+1,-1)]:
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            coeff=coeff_sign*k
            numeric=aval(arg,x0)
            if numeric<0:
                arg=neg(arg)
                numeric=-numeric
                coeff=-coeff
            if R<numeric<S:
                sparse[arg]=sp.expand(sparse.get(arg,0)+coeff)
    return {
        arg:sp.simplify(c)
        for arg,c in sparse.items()
        if sp.simplify(c)!=0
    }

def E(**kwargs):
    reverse={v:k for k,v in varmap.items()}
    return {
        reverse[name]:sp.sympify(c,locals={"p":pS,"q":qS,"r":rS})
        for name,c in kwargs.items()
    }

expected=[
    E(**{"h(e+x)":"-p","h(b-x)":"-p","h(a+x)":"-r",
         "h(T+delta-x)":"-r","l(y)":"-q","H(y)":"-q"}),
    E(**{"h(T+delta-x)":"-p","h(e+x)":"-r","h(2e+x)":"-q"}),
    E(**{"h(y)":"p","H(y)":"-p","h(x)":"-r","h(e+x)":"-q"}),
    E(**{"h(y+delta)":"p","h(x+kappa)":"-q"}),
    E(**{"h(a-x)":"p","h(x)":"-q"}),
    E(**{"h(2d-x)":"p","h(y)":"r"}),
    E(**{"h(b-x)":"p","h(a-x)":"r","h(y)":"q"}),
    E(**{"h(y)":"-p","l(y)":"-p","h(2d-x)":"-r",
         "H(x)":"-r","h(b-x)":"-q"}),
    E(**{"h(x)":"p","H(x)":"-p","h(y)":"-r","h(a-x)":"-q"}),
    E(**{"h(x+kappa)":"p","h(y+delta)":"-q"}),
    E(**{"h(e+x)":"p","h(y)":"-q"}),
    E(**{"h(2e+x)":"p","h(x+kappa)":"r"}),
    E(**{"h(a+x)":"p","h(e+x)":"r","h(x)":"q"}),
]

generated=[raw_reduce(src) for src in sources]
for j,(g,e) in enumerate(zip(generated,expected),1):
    keys=set(g)|set(e)
    diff={k:sp.simplify(g.get(k,0)-e.get(k,0)) for k in keys}
    diff={k:v for k,v in diff.items() if v!=0}
    assert not diff,(j,diff)
    print(f"EXACT_ROW_MATCH Q{j}: PASS")

print("ALL_13_RAW_OPERATOR_ROWS_MATCH_EXACTLY = PASS")
print("2p^2-q^2 =",2*p0*p0-q0*q0)
assert 2*p0*p0-q0*q0>0
print("ROUND14_FULL_VERIFY = PASS")
