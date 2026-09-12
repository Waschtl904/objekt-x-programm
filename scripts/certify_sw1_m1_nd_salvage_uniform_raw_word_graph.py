#!/usr/bin/env python3
"""Uniform raw-word cross-check for the SALVAGE lower-epsilon wedge.

This closes the upstream question left by the older A1 representative-point
certificate.  It works symbolically for the full open interval

    0 < epsilon < epsilon_c = (T-10*Delta)/8

and derives the A7 graph directly from the eleven raw four-echo A1 words.

Certified:
1. all positive internal gate/source-horizon walls are exactly
      epsilon, a-epsilon, a+epsilon, 2d-epsilon, T-epsilon;
2. all positive internal source-folding zeros are exactly a,T;
3. therefore the eight open lower-chamber row cells are exhaustive;
4. direct raw-word evaluation on those cells produces exactly the nine A7
   nonidentity maps, no tenth map;
5. the mapwise unions equal A7.1--A7.9 uniformly in epsilon.

No reducing-subspace or kernel claim.
"""

import sympy as sp
import certify_sw1_a1_raw_archetypes as a1

print("SW1 M1-ND SALVAGE UNIFORM RAW-WORD GRAPH CROSSCHECK")

X=a1.X
L2,L3=sp.log(2),sp.log(3)
a,b,T,d,Delta=a1.a,a1.b,a1.T,a1.d,a1.Delta
eps=sp.symbols("eps", real=True)
eps_c=sp.expand((T-10*Delta)/8)
T0=T+eps

# ---------- exact signs on 0<eps<eps_c ----------

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
    assert ce.is_Rational,(expr,ce)
    s0=sign_log(rest)
    s1=sign_log(sp.expand(rest+ce*eps_c))
    if s0==0:
        return 1 if ce>0 else (-1 if ce<0 else 0)
    if s1==0:
        return s0
    assert s0==s1,("epsilon crossing",expr,s0,s1)
    return s0

assert sign_log(sp.expand(Delta/2-eps_c))>0
assert sign_uniform(eps)>0
assert sign_uniform(eps_c-eps)>0

# ---------- exhaustive wall reconstruction ----------

walls=set()
foldzeros=set()

for delta,eta,lam in a1.WORDS:
    # Horizon gate equations |x +/- delta| = T0-lambda.
    B=sp.expand(T0-lam)
    for shift in (-delta,delta):
        for s in (-1,1):
            x=sp.expand(s*B-shift)
            if sign_uniform(x)>0 and sign_uniform(T0-x)>0:
                walls.add(sp.simplify(x))

    # Source horizon equations |x+shift|=T0 and folding zeros x+shift=0.
    shifts=(-delta-eta,-delta+eta,delta-eta,delta+eta)
    for shift in shifts:
        for s in (-1,1):
            x=sp.expand(s*T0-shift)
            if sign_uniform(x)>0 and sign_uniform(T0-x)>0:
                walls.add(sp.simplify(x))
        x0=sp.expand(-shift)
        if sign_uniform(x0)>0 and sign_uniform(T0-x0)>0:
            foldzeros.add(sp.simplify(x0))

expected_walls={
    sp.simplify(eps),
    sp.simplify(a-eps),
    sp.simplify(a+eps),
    sp.simplify(2*d-eps),
    sp.simplify(T-eps),
}
assert walls==expected_walls,(walls,expected_walls)
assert foldzeros=={sp.simplify(a),sp.simplify(T)},foldzeros

# ---------- direct raw-word evaluation on exhaustive open cells ----------

def inside_abs_uniform(q,bound):
    return sign_uniform(sp.expand(bound-q))>=0 and sign_uniform(sp.expand(bound+q))>=0

def folded(src_sym,src_mid):
    s=sign_uniform(src_mid)
    assert s!=0,("fold zero at row midpoint",src_mid)
    return sp.expand(src_sym if s>0 else -src_sym)

def aggregate_direct(mid):
    out={}
    for j,(delta,eta,lam) in enumerate(a1.WORDS):
        shifts=(-delta-eta,-delta+eta,delta-eta,delta+eta)
        gates=(X-delta,X-delta,X+delta,X+delta)
        for k,(gexpr,sh) in enumerate(zip(gates,shifts)):
            gmid=sp.expand(gexpr.subs(X,mid))
            if not inside_abs_uniform(gmid,T0-lam):
                continue
            src=X+sh
            smid=sp.expand(src.subs(X,mid))
            if not inside_abs_uniform(smid,T0):
                continue
            prof=folded(src,smid)
            out[prof]=sp.simplify(out.get(prof,0)+a1.SIGNS[k]*a1.weights[j])
    return {sp.expand(k):sp.simplify(v) for k,v in out.items() if sp.simplify(v)!=0}

regions=[
    ("R0",sp.Integer(0),eps),
    ("R1",eps,a-eps),
    ("R2",a-eps,a),
    ("R3",a,a+eps),
    ("R4I",a+eps,2*d-eps),
    ("R5",2*d-eps,T-eps),
    ("R6",T-eps,T),
    ("R7",T,T+eps),
]
for row,lo,hi in regions:
    assert sign_uniform(hi-lo)>0,(row,lo,hi)

map_exprs={
    "+a":X+a,
    "-a":X-a,
    "+T":X+T,
    "-T":X-T,
    "r_a":a-X,
    "r_T":T-X,
    "r_3a":3*a-X,
    "r_4a":4*a-X,
    "r_2b":2*b-X,
}

def classify(expr):
    if sp.simplify(expr-X)==0:
        return "I"
    for name,ref in map_exprs.items():
        if sp.simplify(expr-ref)==0:
            return name
    raise AssertionError(("unexpected map",expr))

by_map={}
row_maps={}
for row,lo,hi in regions:
    mid=sp.expand((lo+hi)/2)
    got=aggregate_direct(mid)
    names=[]
    for expr,coeff in got.items():
        name=classify(expr)
        if name=="I":
            continue
        names.append(name)
        by_map.setdefault(name,[]).append((lo,hi))
    row_maps[row]=names

assert set(by_map)==set(map_exprs),(set(by_map),set(map_exprs))
assert set(row_maps["R6"])=={"r_T","r_3a","r_4a","-a","r_2b"}
assert set(row_maps["R7"])=={"-T","r_3a","r_4a","-a","r_2b"}

# ---------- symbolic interval-union reconstruction ----------

rep=sp.expand(eps_c/2)

def merge(intervals):
    xs=sorted(intervals,key=lambda I:float(sp.N(I[0].subs(eps,rep),50)))
    out=[]
    for lo,hi in xs:
        if not out:
            out.append([lo,hi]); continue
        gap=sign_uniform(sp.expand(lo-out[-1][1]))
        if gap<=0:
            if sign_uniform(sp.expand(hi-out[-1][1]))>0:
                out[-1][1]=hi
        else:
            out.append([lo,hi])
    return [(sp.expand(lo),sp.expand(hi)) for lo,hi in out]

got_domains={name:merge(iv) for name,iv in by_map.items()}
expected={
    "+a":[(sp.Integer(0),a+eps)],
    "-a":[(a,T0)],
    "+T":[(sp.Integer(0),eps)],
    "-T":[(T,T0)],
    "r_a":[(sp.Integer(0),eps),(a-eps,a)],
    "r_T":[(sp.Integer(0),T)],
    "r_3a":[(a-eps,T0)],
    "r_4a":[(T-eps,T0)],
    "r_2b":[(2*d-eps,T0)],
}

assert set(got_domains)==set(expected)
for name in expected:
    assert len(got_domains[name])==len(expected[name]),(name,got_domains[name],expected[name])
    for (glo,ghi),(elo,ehi) in zip(got_domains[name],expected[name]):
        assert sp.simplify(glo-elo)==0,(name,"lo",glo,elo)
        assert sp.simplify(ghi-ehi)==0,(name,"hi",ghi,ehi)

print("eleven raw A1 words evaluated symbolically: PASS")
print("all positive internal horizon walls =",sorted(map(str,walls)))
print("all positive source-folding zeros =",sorted(map(str,foldzeros)))
print("eight lower-wedge row cells exhaustive: PASS")
print("derived nonidentity alphabet =",sorted(by_map))
print("no tenth nonidentity map: PASS")
print("derived domains == A7.1--A7.9 uniformly in epsilon: PASS")
print("R6/R7 five-arm support uniform in epsilon: PASS")
print("FIREWALL: raw graph support only; no reducing/kernel verdict")
print("SW1 M1-ND SALVAGE UNIFORM RAW-WORD GRAPH CROSSCHECK: PASS")
