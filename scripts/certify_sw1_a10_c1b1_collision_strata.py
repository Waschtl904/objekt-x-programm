#!/usr/bin/env python3
"""SW1-A10-C1B1 exact collision-hyperplane classification.

Small lower H3 chamber:
  0 < sigma <= R < epsilon < epsilon_*,
  epsilon_*=(6 Delta-L)/4.

Starting from the complete 92 C1B0 circle-boundary signatures, enumerate all
pairwise collision equations modulo L. No irrationality shortcut k'=0 is used:
R,epsilon,sigma are free real parameters and can compensate nonzero Delta terms.

The certificate proves:
- 4186 unordered boundary pairs -> 463 distinct raw difference signatures;
- a uniform size bound excludes all wrap coefficients |q|>=2;
- 1087 unique canonical collision equations remain;
- 18 meet the strict chamber interior;
- 18 meet only the closure;
- among closure-only equations, exactly sigma=R is allowed by SW1;
- the other 17 lie on excluded boundaries (zero/strict-order/epsilon_* walls).

The 18 genuine interior hyperplanes split into two exact families:
  s_* = L/2-2Delta equals one of
      2R, R+epsilon, R+sigma, 2epsilon, epsilon+sigma, 2sigma;
  chi = 5Delta-L equals one of
      epsilon-R, sigma, 2sigma, epsilon-sigma, epsilon,
      epsilon+sigma, 2epsilon, R-sigma, R, R+sigma,
      R+epsilon, 2R.

Firewall: collision-strata classification only. No atom ordering, final fiber N,
matrix cocycle, or injectivity claim.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

L2,L3=sp.log(2),sp.log(3)
Delta=sp.simplify(L3-sp.Rational(3,2)*L2)
L=sp.simplify(2*L2-L3)
eps_star=sp.simplify((6*Delta-L)/4)

assert Delta.is_positive is True
assert L.is_positive is True
assert eps_star.is_positive is True
assert sp.simplify(5*Delta-L).is_positive is True
assert sp.simplify(L/2-2*Delta).is_positive is True
assert sp.simplify(7*L-34*Delta).is_positive is True

def V(Lc=0,D=0,R=0,E=0,S=0):
    return (F(Lc),F(D),F(R),F(E),F(S))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)

zero=V()
e=V(F(1,2),0)
d=V(F(1,2),1)
a=V(1,1)
b=V(F(3,2),2)
T=V(2,2)
twod=V(1,2)

Bf={
 zero,V(E=1),sub(a,V(E=1)),add(a,V(E=1)),sub(twod,V(E=1)),sub(T,V(E=1)),
 V(S=1),add(e,V(S=1)),add(a,V(S=1)),
 sub(a,V(R=1)),add(a,V(R=1)),sub(b,V(R=1)),add(b,V(R=1)),
 sub(T,V(R=1)),add(T,V(R=1)),a,b,T,add(T,V(E=1)),
}
Bw={
 V(R=1),V(E=1),add(e,V(E=1)),d,add(d,V(R=1)),
 a,add(a,V(R=1)),add(a,V(E=1)),b,sub(T,V(R=1)),T,add(T,V(S=1)),
}
assert len(Bf)==19 and len(Bw)==12 and len(Bf|Bw)==24

C=[
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1),(1,3,2),(1,4,2)],
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1),(1,3,2)],
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1)],
[(-1,2,1),(-1,4,2),(-1,4,3),(-1,5,3),(1,1,0),(1,2,1),(1,3,1)],
[(-1,2,1),(-1,3,2),(-1,4,2),(1,2,1)],
[(-1,3,2),(-1,5,3),(-1,6,3),(1,-2,-1),(1,0,0),(1,1,1),(1,2,1)],
[(-1,3,2),(-1,4,2),(1,-2,-1),(1,2,1)],
[(-1,3,2),(-1,4,2),(1,-2,-1)],
[(-1,4,2),(1,-3,-2),(1,-2,-1)],
[(-1,4,2),(-1,6,3),(-1,7,4),(-1,8,4),(1,-3,-2),(1,-1,0),(1,0,0)],
[(1,-4,-2),(1,-3,-2),(1,-2,-1)]]
sig=set(q for cell in C for q in cell)
assert len(sig)==19

def rel(x,y):
    s,l,k=x; t,m,j=y
    if s==t:
        lam=F(m-l,2); dk=j-k
        if lam<0 or (lam==0 and dk<0):
            lam=-lam; dk=-dk
        return ("T",lam,dk)
    return ("R",F(l+m,2),k+j)

master={rel(x,y) for cell in C for x,y in combinations(cell,2)}
assert len(master)==22

def cv(lam,k): return V(Lc=lam,D=k)

Braw=set(Bf|Bw)
generated=24
nT=sum(1 for x in master if x[0]=="T")
nR=sum(1 for x in master if x[0]=="R")
assert (nT,nR)==(8,14)

for typ,lam,k in master:
    cc0=cv(lam,k)
    if typ=="T":
        for direction in (-1,1):
            cc=tuple(direction*z for z in cc0)
            for wall in Bf:
                generated+=1
                Braw.add(sub(wall,cc))
    else:
        for wall in Bf:
            generated+=1
            Braw.add(sub(cc0,wall))

for s,twolam,k in sig:
    cc=cv(F(twolam,2),k)
    for wall in Bf:
        generated+=1
        z=sub(wall,cc)
        if s==-1:
            z=neg(z)
        Braw.add(z)

assert generated==24+8*2*19+14*19+19*19==955
assert len(Braw)==195

def floor_fraction(q):
    return q.numerator//q.denominator
def modL(x):
    n=F(floor_fraction(x[0]))
    return (x[0]-n,)+x[1:]

Bmod={modL(x) for x in Braw}
assert len(Bmod)==92
assert {x[0] for x in Bmod}=={F(0),F(1,2)}

pairs=list(combinations(sorted(Bmod),2))
assert len(pairs)==92*91//2==4186
rawdiff={sub(x,y) for x,y in pairs}
assert len(rawdiff)==463

assert sp.simplify(2*L-(8*Delta+6*eps_star)-(7*L-34*Delta)/2)==0
assert sp.simplify(2*L-(8*Delta+6*eps_star)).is_positive is True

def canon(eq):
    for z in eq:
        if z:
            if z<0:
                return tuple(-x for x in eq)
            break
    return eq

equations=set()
for dL,dD,dR,dE,dS in rawdiff:
    for n in range(-3,4):
        q=dL-F(n)
        if abs(q)>=2:
            continue
        equations.add(canon((q,dD,dR,dE,dS)))
assert len(equations)==1087

def Q(x):
    return sp.Rational(x.numerator,x.denominator)

def sgn(z):
    z=sp.simplify(z)
    if z==0: return 0
    if z.is_positive is True: return 1
    if z.is_negative is True: return -1
    raise AssertionError(("undecided exact sign",z))

strict=set()
closure_boundary=set()
outside=set()

for eq in equations:
    q,k,rho,mu,nu=eq
    target=sp.simplify(-(Q(q)*L+Q(k)*Delta))
    coeffs=[F(0),mu,rho+mu,rho+mu+nu]
    lo=Q(min(coeffs))*eps_star
    hi=Q(max(coeffs))*eps_star
    slo=sgn(target-lo)
    shi=sgn(hi-target)
    if slo>0 and shi>0:
        strict.add(eq)
    elif slo>=0 and shi>=0:
        closure_boundary.add(eq)
    else:
        outside.add(eq)

assert len(strict)==18
assert len(closure_boundary)==18
assert len(outside)==1051
assert len(strict|closure_boundary|outside)==1087

A={
 (F(1,2),F(-2),F(-2),F(0),F(0)),
 (F(1,2),F(-2),F(-1),F(-1),F(0)),
 (F(1,2),F(-2),F(-1),F(0),F(-1)),
 (F(1,2),F(-2),F(0),F(-2),F(0)),
 (F(1,2),F(-2),F(0),F(-1),F(-1)),
 (F(1,2),F(-2),F(0),F(0),F(-2)),
}
B={
 (F(1),F(-5),F(-1),F(1),F(0)),
 (F(1),F(-5),F(0),F(0),F(1)),
 (F(1),F(-5),F(0),F(0),F(2)),
 (F(1),F(-5),F(0),F(1),F(-1)),
 (F(1),F(-5),F(0),F(1),F(0)),
 (F(1),F(-5),F(0),F(1),F(1)),
 (F(1),F(-5),F(0),F(2),F(0)),
 (F(1),F(-5),F(1),F(0),F(-1)),
 (F(1),F(-5),F(1),F(0),F(0)),
 (F(1),F(-5),F(1),F(0),F(1)),
 (F(1),F(-5),F(1),F(1),F(0)),
 (F(1),F(-5),F(2),F(0),F(0)),
}
assert strict==A|B

allowed_face={(F(0),F(0),F(1),F(0),F(-1))}
assert allowed_face <= closure_boundary
excluded_boundary=closure_boundary-allowed_face
assert len(excluded_boundary)==17

upperwall={eq for eq in excluded_boundary if eq[0]==F(1,2)}
assert len(upperwall)==6
assert all(eq[1]==-3 for eq in upperwall)
assert sp.simplify(3*Delta-L/2-2*eps_star)==0

zerowall=excluded_boundary-upperwall
assert len(zerowall)==11
assert all(eq[0]==0 and eq[1]==0 for eq in zerowall)

sstar=sp.simplify(L/2-2*Delta)
chi=sp.simplify(5*Delta-L)
assert sstar.is_positive is True
assert chi.is_positive is True

print("SW1-A10-C1B1 COLLISION-STRATIFICATION CERTIFICATE: PASS")
print("C1B0 generation ledger: 955 exhaustive generated occurrences -> 195 symbolic forms -> 92 mod-L signatures")
print("92 choose 2 = 4186 boundary pairs -> 463 distinct raw difference signatures")
print("uniform exact bound excludes every circle-wrap coefficient |q|>=2")
print("1087 unique canonical collision equations remain")
print("1051 do not meet even the closed small-lower parameter simplex")
print("18 meet the strict chamber interior; 18 meet only its closure")
print("of the 18 closure-only equations, exactly R=sigma is allowed by SW1; 17 are excluded strict-boundary cases")
print("genuine family A (6): s*=L/2-2Delta equals 2R,R+eps,R+sigma,2eps,eps+sigma,2sigma")
print("genuine family B (12): chi=5Delta-L equals eps-R,sigma,2sigma,eps-sigma,eps,eps+sigma,2eps,R-sigma,R,R+sigma,R+eps,2R")
print("IMPORTANT: nonzero Delta coefficients occur in both genuine families; irrationality does NOT force k'=0")
print("FIREWALL: collision hyperplanes only; atom ordering, final N, matrices and injectivity remain open")
