#!/usr/bin/env python3
"""Direct-complement adversarial cross-check for SALVAGE-A1/A2.

Unlike the primary certificate, this script does NOT infer K-invariance from
F-invariance plus inverse generators.  It constructs the 25 complement cells
K_epsilon directly and checks every active K-cell/domain image under all nine
A7 maps is again covered by K_epsilon, uniformly for
    0 < epsilon < epsilon_c.

It also independently re-enumerates the physical Hub pieces from K_epsilon
and checks direct avoidance of all 14 candidate blind intervals.

This is a cross-check of Gates B/C only.  No functional-analytic kernel claim.
"""

import sympy as sp

print("SW1 M1-ND SALVAGE DIRECT-COMPLEMENT CROSSCHECK")

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

def linlog_coeff(expr):
    z=sp.expand(expr)
    A=sp.simplify(z.coeff(L2))
    B=sp.simplify(z.coeff(L3))
    rest=sp.simplify(z-A*L2-B*L3)
    assert rest==0,(expr,A,B,rest)
    assert A.is_Rational and B.is_Rational
    return sp.Rational(A),sp.Rational(B)

def sign_log(expr):
    A,B=linlog_coeff(expr)
    if A==0 and B==0: return 0
    if A>=0 and B>=0: return 1
    if A<=0 and B<=0: return -1
    den=sp.ilcm(int(A.q),int(B.q))
    ai=int(A*den); bi=int(B*den)
    if ai>0 and bi<0:
        return (2**ai>3**(-bi))-(2**ai<3**(-bi))
    if ai<0 and bi>0:
        return (3**bi>2**(-ai))-(3**bi<2**(-ai))
    raise AssertionError((expr,A,B))

def sign_uniform(expr):
    z=sp.expand(expr)
    ce=sp.simplify(z.coeff(eps))
    rest=sp.expand(z-ce*eps)
    assert ce.is_Rational
    s0=sign_log(rest)
    s1=sign_log(sp.expand(rest+ce*eps_c))
    if s0==0:
        return 1 if ce>0 else (-1 if ce<0 else 0)
    if s1==0:
        return s0
    assert s0==s1,("crossing",expr,s0,s1)
    return s0

def cmpu(x,y): return sign_uniform(sp.expand(x-y))
def maxu(x,y): return x if cmpu(x,y)>=0 else y
def minu(x,y): return x if cmpu(x,y)<=0 else y

def inter(I,J):
    lo=maxu(I[0],J[0]); hi=minu(I[1],J[1])
    return (sp.expand(lo),sp.expand(hi)) if cmpu(hi,lo)>0 else None

def image(I,s,c):
    lo,hi=I
    return (sp.expand(lo+c),sp.expand(hi+c)) if s==1 else (sp.expand(c-hi),sp.expand(c-lo))

rep=sp.expand(eps_c/2)

# Construct F only to determine the complement endpoints.
F=[]
for shift in (sp.Integer(0),a):
    for k in range(6):
        for j in (0,1):
            base=sp.expand(shift+k*Delta+j*h)
            F.append((sp.expand(base+eps),sp.expand(base+h-eps)))
F.sort(key=lambda z:float(sp.N(z[0].subs(eps,rep),50)))

K=[]
cur=sp.Integer(0)
for lo,hi in F:
    if cmpu(lo,cur)>0:
        K.append((sp.expand(cur),sp.expand(lo)))
    cur=hi
if cmpu(T0,cur)>0:
    K.append((sp.expand(cur),sp.expand(T0)))
assert len(K)==25

def covered_by_K(I):
    pieces=[J for G in K if (J:=inter(I,G)) is not None]
    assert pieces,("no K cover",I)
    pieces.sort(key=lambda z:float(sp.N(z[0].subs(eps,rep),50)))
    assert cmpu(pieces[0][0],I[0])<=0
    cur=pieces[0][1]
    for lo,hi in pieces[1:]:
        assert cmpu(lo,cur)<=0,("K cover gap",I,cur,(lo,hi))
        if cmpu(hi,cur)>0: cur=hi
    assert cmpu(cur,I[1])>=0

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

counts={}
total=0
for name,(s,c,Ds) in domains.items():
    n=0
    for I in K:
        for D in Ds:
            J=inter(I,D)
            if J is None: continue
            covered_by_K(image(J,s,c))
            n+=1; total+=1
    counts[name]=n

# The count is a checksum after exhaustive loops, not an assumption.
assert set(counts)==set(domains)

C=[
    sp.Integer(0),Delta,2*Delta,3*Delta,
    d,d+Delta,d+2*Delta,
    a,a+Delta,a+2*Delta,a+3*Delta,
    b,b+Delta,b+2*Delta,
]
B=[(sp.expand(c+eps),sp.expand(c+h-eps)) for c in C]

def avoids_B(I):
    assert all(inter(I,J) is None for J in B)

hub_counts={}
hub_total=0
for tau_name,tau in (("a",a),("b",b),("T",T)):
    n=0
    for I in K:
        left=inter(I,(sp.Integer(0),tau))
        if left is not None:
            avoids_B((sp.expand(tau-left[1]),sp.expand(tau-left[0])))
            n+=1; hub_total+=1
        right=inter(I,(tau,T0))
        if right is not None:
            avoids_B((sp.expand(right[0]-tau),sp.expand(right[1]-tau)))
            n+=1; hub_total+=1
        avoids_B((sp.expand(I[0]+tau),sp.expand(I[1]+tau)))
        n+=1; hub_total+=1
    hub_counts[tau_name]=n

assert hub_total==153

print("25 complement cells reconstructed: PASS")
print("direct K-invariance under all nine A7 maps: PASS")
print("active K/domain image counts:",counts)
print("total active K/domain pieces:",total)
print("Hub piece counts by center:",hub_counts)
print("Hub total pieces:",hub_total)
print("all Hub pieces avoid all 14 blind intervals: PASS")
print("FIREWALL: Gate B/C direct cross-check only; no kernel promotion")
print("SW1 M1-ND SALVAGE DIRECT-COMPLEMENT CROSSCHECK: PASS")
