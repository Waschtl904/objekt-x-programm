#!/usr/bin/env python3
"""Exact SALVAGE-A1/A2 certificate: an R-independent blind wedge.

Claimed geometric scope:
    0 < epsilon < epsilon_c := (T-10*Delta)/8,
    0 < R < epsilon,
    0 < sigma < R.

Define
    h = (T-10*Delta)/4 = d-3*Delta > 0.

Construct 24 open forbidden Horizon gaps F_epsilon.  Their complement
K_epsilon contains the maximal KNF sampling set U_epsilon^max.
The script proves, uniformly for the whole open epsilon interval:

1. the 24 gaps are positive, ordered, disjoint and lie in (0,T);
2. U_epsilon^max is disjoint from F_epsilon;
3. every one of the nine A7 graphing maps sends F_epsilon∩domain into
   F_epsilon; since inverse generators are present, K_epsilon is invariant;
4. the six physical Hub source maps from K_epsilon avoid 14 explicit
   positive-Annulus intervals B_epsilon;
5. the 14 intervals are disjoint, lie in (epsilon,T), and have total measure
       14(h-2 epsilon)
       = 7/2 (T-10 Delta-8 epsilon) > 0.

This script proves the new finite geometric premises.  The functional-analytic
kernel conclusion uses the already promoted IMG4 reducing/Hub/KNF mechanism
and is recorded separately in the candidate audit.
"""

import sympy as sp

print("SW1 M1-ND SALVAGE-A1/A2 UNIFORM BLIND WEDGE CERTIFICATE")

L2,L3=sp.log(2),sp.log(3)
a=L2/2
b=L3/2
T=L2
d=b-a
Delta=sp.expand(L3-sp.Rational(3,2)*L2)
h=sp.expand((T-10*Delta)/4)
eps_c=sp.expand(h/2)
eps=sp.symbols("eps", real=True)
T0=T+eps

# ---------- exact sign engine for affine-in-epsilon log forms ----------

def linlog_coeff(expr):
    z=sp.expand(expr)
    A=sp.simplify(z.coeff(L2))
    B=sp.simplify(z.coeff(L3))
    rest=sp.simplify(z-A*L2-B*L3)
    assert rest==0,(expr,A,B,rest)
    assert A.is_Rational and B.is_Rational,(expr,A,B)
    return sp.Rational(A),sp.Rational(B)

def sign_log(expr):
    A,B=linlog_coeff(sp.expand(expr))
    if A==0 and B==0:
        return 0
    if A>=0 and B>=0:
        return 1
    if A<=0 and B<=0:
        return -1
    den=sp.ilcm(int(A.q),int(B.q))
    ai=int(A*den)
    bi=int(B*den)
    if ai>0 and bi<0:
        lhs=2**ai
        rhs=3**(-bi)
        return (lhs>rhs)-(lhs<rhs)
    if ai<0 and bi>0:
        lhs=3**bi
        rhs=2**(-ai)
        return (lhs>rhs)-(lhs<rhs)
    raise AssertionError((expr,A,B))

def sign_uniform(expr):
    """Sign on the open interval 0<eps<eps_c for affine expr."""
    z=sp.expand(expr)
    c=sp.simplify(z.coeff(eps))
    rest=sp.expand(z-c*eps)
    assert sp.expand(z-rest-c*eps)==0
    assert c.is_Rational,(expr,c)
    s0=sign_log(rest)
    s1=sign_log(sp.expand(rest+c*eps_c))
    if s0==0:
        if c>0:
            return 1
        if c<0:
            return -1
        return 0
    if s1==0:
        return s0
    assert s0==s1,("epsilon crossing inside salvage wedge",expr,s0,s1)
    return s0

def cmpu(x,y):
    return sign_uniform(sp.expand(x-y))

def maxu(x,y):
    return x if cmpu(x,y)>=0 else y

def minu(x,y):
    return x if cmpu(x,y)<=0 else y

def inter(I,J):
    lo=maxu(I[0],J[0])
    hi=minu(I[1],J[1])
    s=cmpu(hi,lo)
    return (sp.expand(lo),sp.expand(hi)) if s==1 else None

def image(I,s,c):
    lo,hi=I
    if s==1:
        return (sp.expand(lo+c),sp.expand(hi+c))
    assert s==-1
    return (sp.expand(c-hi),sp.expand(c-lo))

# ---------- structural constants ----------

assert sp.simplify(h-(d-3*Delta))==0
assert sp.simplify(h-(a-(d+2*Delta)))==0
assert sp.simplify(h-(b-(a+3*Delta)))==0
assert sp.simplify(h-(T-(b+2*Delta)))==0
assert sp.simplify(h-(sp.simplify((a-Delta)/2)-2*Delta))==0

# h>0 is exactly 8 log2 > 5 log3, i.e. 2^8 > 3^5.
assert 2**8 > 3**5
assert sign_log(h)==1
assert sign_log(eps_c)==1

# The entire new wedge must remain inside the lower A7 chamber.
# eps_c < Delta/2 is equivalent to 11*log(2) < 7*log(3),
# hence to the exact integer inequality 2^11 < 3^7.
assert 2**11 < 3**7
assert sign_log(sp.expand(Delta/2-eps_c))==1

assert sign_uniform(eps)==1
assert sign_uniform(eps_c-eps)==1
assert sign_uniform(h-2*eps)==1
assert sign_uniform(Delta-2*eps)==1

# Maximal KNF centers remain inside the positive Horizon.
assert sign_uniform(a-eps)==1
assert sign_uniform(b-eps)==1

# ---------- 24 forbidden Horizon gaps ----------

F=[]
for shift in (sp.Integer(0),a):
    for k in range(6):
        base=sp.expand(shift+k*Delta)
        for j in (0,1):
            lo=sp.expand(base+j*h+eps)
            hi=sp.expand(base+(j+1)*h-eps)
            F.append((lo,hi,(shift,k,j)))

# Sort by one exact interior representative; all pairwise ordering checks below
# prove that the ordering is uniform on the full open epsilon wedge.
rep=sp.expand(eps_c/2)
F.sort(key=lambda z: float(sp.N(z[0].subs(eps,rep),50)))
assert len(F)==24

for i,(lo,hi,tag) in enumerate(F):
    assert sign_uniform(hi-lo)==1,("gap width",tag)
    assert sign_uniform(lo)==1,("gap lower",tag)
    assert sign_uniform(T-hi)==1,("gap upper",tag)
    if i+1<len(F):
        assert sign_uniform(F[i+1][0]-hi)==1,("gap order",tag,F[i+1][2])

Fints=[(lo,hi) for lo,hi,_ in F]

# Maximal KNF sampling set corresponding to the boundary majorant R=epsilon.
Umax=[
    (a-eps,a+eps),
    (b-eps,b+eps),
    (T-eps,T+eps),
]
for U in Umax:
    for G in Fints:
        assert inter(U,G) is None

# ---------- A7 graphing and F-invariance ----------

domains={
    "+a": ( 1, a, [(sp.Integer(0),a+eps)]),
    "-a": ( 1,-a, [(a,T0)]),
    "+T": ( 1, T, [(sp.Integer(0),eps)]),
    "-T": ( 1,-T, [(T,T0)]),
    "r_a":(-1, a, [(sp.Integer(0),eps),(a-eps,a)]),
    "r_T":(-1, T, [(sp.Integer(0),T)]),
    "r_3a":(-1,3*a,[(a-eps,T0)]),
    "r_4a":(-1,4*a,[(T-eps,T0)]),
    "r_2b":(-1,2*b,[(2*d-eps,T0)]),
}

def covered_by_F(I):
    pieces=[]
    for G in Fints:
        K=inter(I,G)
        if K is not None:
            pieces.append(K)
    assert pieces,("no F cover",I)
    pieces.sort(key=lambda z: float(sp.N(z[0].subs(eps,rep),50)))
    assert cmpu(pieces[0][0],I[0])<=0
    cur=pieces[0][1]
    for lo,hi in pieces[1:]:
        assert cmpu(lo,cur)<=0,("F cover gap",I,cur,(lo,hi))
        if cmpu(hi,cur)>0:
            cur=hi
    assert cmpu(cur,I[1])>=0
    return True

mapped_F_pieces=0
for name,(s,c,doms) in domains.items():
    for lo,hi,tag in F:
        for D in doms:
            K=inter((lo,hi),D)
            if K is None:
                continue
            covered_by_F(image(K,s,c))
            mapped_F_pieces += 1

assert mapped_F_pieces==70

# Inverse-domain facts needed to pass from F-invariance to K=F^c invariance.
def eq_int(I,J):
    return sp.simplify(I[0]-J[0])==0 and sp.simplify(I[1]-J[1])==0

def image_full(s,c,I):
    return image(I,s,c)

assert eq_int(image_full(1,a,domains["+a"][2][0]),domains["-a"][2][0])
assert eq_int(image_full(1,-a,domains["-a"][2][0]),domains["+a"][2][0])
assert eq_int(image_full(1,T,domains["+T"][2][0]),domains["-T"][2][0])
assert eq_int(image_full(1,-T,domains["-T"][2][0]),domains["+T"][2][0])
for name in ("r_T","r_3a","r_4a","r_2b"):
    s,c,Ds=domains[name]
    assert eq_int(image_full(s,c,Ds[0]),Ds[0])
ra0,ra1=domains["r_a"][2]
assert eq_int(image_full(-1,a,ra0),ra1)
assert eq_int(image_full(-1,a,ra1),ra0)

# ---------- complement K and 14 blind Annulus gaps ----------

K=[]
cur=sp.Integer(0)
for lo,hi,_ in F:
    if sign_uniform(lo-cur)==1:
        K.append((sp.expand(cur),sp.expand(lo)))
    cur=hi
if sign_uniform(T0-cur)==1:
    K.append((sp.expand(cur),sp.expand(T0)))
assert len(K)==25

C=[
    sp.Integer(0),Delta,2*Delta,3*Delta,
    d,d+Delta,d+2*Delta,
    a,a+Delta,a+2*Delta,a+3*Delta,
    b,b+Delta,b+2*Delta,
]
assert len(C)==14

B=[(sp.expand(c+eps),sp.expand(c+h-eps)) for c in C]
for i,(lo,hi) in enumerate(B):
    assert sign_uniform(hi-lo)==1
    assert cmpu(lo,eps)>=0
    assert cmpu(T,hi)>=0
    if i+1<len(B):
        assert sign_uniform(B[i+1][0]-hi)==1

def avoids_B(I):
    for J in B:
        assert inter(I,J) is None

hub_pieces=0
for tau in (a,b,T):
    for I in K:
        left=inter(I,(sp.Integer(0),tau))
        if left is not None:
            avoids_B((sp.expand(tau-left[1]),sp.expand(tau-left[0])))
            hub_pieces += 1
        right=inter(I,(tau,T0))
        if right is not None:
            avoids_B((sp.expand(right[0]-tau),sp.expand(right[1]-tau)))
            hub_pieces += 1
        avoids_B((sp.expand(I[0]+tau),sp.expand(I[1]+tau)))
        hub_pieces += 1

assert hub_pieces==153

# Total blind measure.
blind_measure=sp.expand(sum(hi-lo for lo,hi in B))
expected=sp.expand(14*(h-2*eps))
assert sp.simplify(blind_measure-expected)==0
assert sp.simplify(expected-sp.Rational(7,2)*(T-10*Delta-8*eps))==0
assert sign_uniform(expected)==1

print("h=(T-10 Delta)/4=d-3 Delta > 0: PASS")
print("epsilon_c=(T-10 Delta)/8 and epsilon_c<Delta/2: PASS")
print("24 forbidden Horizon gaps: ordered/disjoint/uniform PASS")
print("maximal KNF sampling set U_epsilon^max avoids F_epsilon: PASS")
print("70 active forbidden-gap FREE images remain in F_epsilon: PASS")
print("all nine A7 inverse-domain/involution relations: PASS")
print("therefore K_epsilon=F_epsilon^c is graph-invariant: ANALYTIC CONSEQUENCE")
print("25 K_epsilon cells assembled: PASS")
print("14 candidate Annulus blind gaps: ordered/disjoint/in (epsilon,T): PASS")
print("153 Hub image pieces from K_epsilon avoid all 14 blind gaps: PASS")
print("blind measure = 14(h-2 epsilon) = 7/2(T-10Delta-8epsilon) > 0: PASS")
print("FIREWALL: kernel conclusion imports promoted IMG4 reducing/Hub/KNF mechanism")
print("SW1 M1-ND SALVAGE-A1/A2 UNIFORM BLIND WEDGE CERTIFICATE: PASS")
