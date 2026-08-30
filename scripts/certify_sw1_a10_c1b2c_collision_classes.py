#!/usr/bin/env python3
"""SW1-A10-C1B2C exact higher-degeneracy / boundary-collision strata certificate.

Reference arrangement r0=s*/chi=7/2, with exact rational arithmetic.

Scope:
1. Retrospective completeness check for C1B2A critical ratios:
   enumerate dependent subsets of sizes 2,3,4 among the 18 collision planes
   plus 4 simplex facets. In R^3 every minimal affine consistency/incidence
   witness has at most 4 equations, so this exhausts higher degeneracies.
2. Reconstruct all 92 C1B0 boundary signatures and map each of the 18 genuine
   collision planes to the exact label pairs that collide there.
3. Enumerate every nonempty codim-2/codim-3 intersection stratum in the open
   reference simplex and compute transitive boundary-label collision classes.
4. Treat the allowed SW1 boundary face sigma=R separately, including all
   face-line and face-point strata.

Firewall: exact reference-strata / label-collision ledger only. Transfer to the
actual project ratio r in (3,4) uses the separate no-critical-r isotopy step.
No final fiber dimension N, operator matrix, or injectivity claim.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict, Counter
import sympy as sp

# ---------------------------------------------------------------------------
# A. Higher-degeneracy completeness for the 22-plane clipped arrangement
# ---------------------------------------------------------------------------
r=sp.symbols('r')
H=[]
def hp(name,a,b0=0,b1=0):
    H.append((name,sp.Matrix([sp.Rational(x) for x in a]),sp.Rational(b0)+sp.Rational(b1)*r))
for name,a,b0,b1 in [
('A_2R',[0,2,0],0,1),('A_R+e',[0,1,1],0,1),('A_R+s',[1,1,0],0,1),
('A_2e',[0,0,2],0,1),('A_e+s',[1,0,1],0,1),('A_2s',[2,0,0],0,1),
('B_e-R',[0,-1,1],1,0),('B_s',[1,0,0],1,0),('B_2s',[2,0,0],1,0),
('B_e-s',[-1,0,1],1,0),('B_e',[0,0,1],1,0),('B_e+s',[1,0,1],1,0),
('B_2e',[0,0,2],1,0),('B_R-s',[-1,1,0],1,0),('B_R',[0,1,0],1,0),
('B_R+s',[1,1,0],1,0),('B_R+e',[0,1,1],1,0),('B_2R',[0,2,0],1,0),
('D_s0',[1,0,0],0,0),('D_R=s',[-1,1,0],0,0),('D_e=R',[0,-1,1],0,0),
('D_e=E',[0,0,1],sp.Rational(1,2),sp.Rational(1,2))]:
    hp(name,a,b0,b1)
assert len(H)==22

critical_by_size={2:set(),3:set(),4:set()}
witness_count={2:0,3:0,4:0}
for ksize in (2,3,4):
    for inds in combinations(range(22),ksize):
        A=sp.Matrix.vstack(*[H[i][1].T for i in inds])
        b=sp.Matrix([H[i][2] for i in inds])
        left=A.T.nullspace()
        if not left:
            continue
        conds=[sp.expand((v.T*b)[0]) for v in left]
        if all(c==0 for c in conds):
            continue
        roots=None; possible=True
        for c in conds:
            if c==0:
                continue
            p=sp.Poly(c,r)
            if p.degree()==0:
                possible=False; break
            vals=set(sp.solve(sp.Eq(c,0),r))
            roots=vals if roots is None else roots & vals
        if possible and roots:
            witness_count[ksize]+=1
            critical_by_size[ksize] |= {x for x in roots if x.is_Rational}

assert witness_count=={2:12,3:359,4:3841}
assert critical_by_size[2]=={sp.Rational(0),sp.Rational(1),sp.Rational(2)}
assert critical_by_size[3]=={
    sp.Rational(-1),sp.Rational(0),sp.Rational(1,2),sp.Rational(1),
    sp.Rational(3,2),sp.Rational(2),sp.Rational(3),sp.Rational(4)}
expected={sp.Rational(x) for x in [-3,-2,-1,0,1,2,3,4,5,6]}
expected|={sp.Rational(-1,2),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(2,3),
           sp.Rational(4,3),sp.Rational(3,2),sp.Rational(5,2)}
assert critical_by_size[2]|critical_by_size[3]|critical_by_size[4]==expected
assert critical_by_size[4]-(critical_by_size[2]|critical_by_size[3])=={
    sp.Rational(-3),sp.Rational(-2),sp.Rational(-1,2),sp.Rational(1,3),
    sp.Rational(2,3),sp.Rational(4,3),sp.Rational(5,2),sp.Rational(5),sp.Rational(6)}
assert not any(sp.Rational(3)<x<sp.Rational(4) for x in expected)

# ---------------------------------------------------------------------------
# B. Reconstruct the complete 92 boundary signatures and collision-pair maps
# ---------------------------------------------------------------------------
def V(L=0,D=0,R=0,E=0,S=0): return (F(L),F(D),F(R),F(E),F(S))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
zero=V(); ee=V(F(1,2),0); d=V(F(1,2),1); a=V(1,1); b=V(F(3,2),2); T=V(2,2); twod=V(1,2)
Bf={zero,V(E=1),sub(a,V(E=1)),add(a,V(E=1)),sub(twod,V(E=1)),sub(T,V(E=1)),
    V(S=1),add(ee,V(S=1)),add(a,V(S=1)),sub(a,V(R=1)),add(a,V(R=1)),
    sub(b,V(R=1)),add(b,V(R=1)),sub(T,V(R=1)),add(T,V(R=1)),a,b,T,add(T,V(E=1))}
Bw={V(R=1),V(E=1),add(ee,V(E=1)),d,add(d,V(R=1)),a,add(a,V(R=1)),add(a,V(E=1)),
    b,sub(T,V(R=1)),T,add(T,V(S=1))}
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
sig={q for cell in C for q in cell}
def rel(x,y):
    s,l,k=x; t,m,j=y
    if s==t:
        lam=F(m-l,2); dk=j-k
        if lam<0 or (lam==0 and dk<0): lam=-lam; dk=-dk
        return ('T',lam,dk)
    return ('R',F(l+m,2),k+j)
master={rel(x,y) for cell in C for x,y in combinations(cell,2)}
def cv(lam,k): return V(L=lam,D=k)
Braw=set(Bf|Bw)
for typ,lam,k in master:
    cc0=cv(lam,k)
    if typ=='T':
        for dr in (-1,1):
            cc=tuple(dr*z for z in cc0)
            for wall in Bf: Braw.add(sub(wall,cc))
    else:
        for wall in Bf: Braw.add(sub(cc0,wall))
for orient,twolam,k in sig:
    cc=cv(F(twolam,2),k)
    for wall in Bf:
        z=sub(wall,cc)
        if orient==-1: z=neg(z)
        Braw.add(z)
def floorf(q): return q.numerator//q.denominator
def modL(x):
    n=F(floorf(x[0])); return (x[0]-n,)+x[1:]
Bmod=sorted({modL(x) for x in Braw})
assert len(Bmod)==92

Aeq=[
(F(1,2),-2,-2,0,0),(F(1,2),-2,-1,-1,0),(F(1,2),-2,-1,0,-1),
(F(1,2),-2,0,-2,0),(F(1,2),-2,0,-1,-1),(F(1,2),-2,0,0,-2)]
Beq=[
(1,-5,-1,1,0),(1,-5,0,0,1),(1,-5,0,0,2),(1,-5,0,1,-1),
(1,-5,0,1,0),(1,-5,0,1,1),(1,-5,0,2,0),(1,-5,1,0,-1),
(1,-5,1,0,0),(1,-5,1,0,1),(1,-5,1,1,0),(1,-5,2,0,0)]
eqs=[tuple(F(x) for x in z) for z in Aeq+Beq]
faceeq=(F(0),F(0),F(1),F(0),F(-1)) # R-sigma=0
all_eq=eqs+[faceeq]
def canon(eq):
    for z in eq:
        if z:
            return tuple(-x for x in eq) if z<0 else eq
    return eq
emap={e:[] for e in all_eq}
for i,j in combinations(range(92),2):
    dd=sub(Bmod[i],Bmod[j])
    for n in range(-3,4):
        eq=canon((dd[0]-F(n),dd[1],dd[2],dd[3],dd[4]))
        if eq in emap:
            emap[eq].append((i,j))

pair_count=[len(emap[e]) for e in eqs]
assert pair_count==[10,19,15,9,14,5,8,8,4,3,8,8,4,3,8,8,8,4]
assert len(emap[faceeq])==23

def components(edges):
    g=defaultdict(set)
    for i,j in edges:
        g[i].add(j); g[j].add(i)
    seen=set(); out=[]
    for v in sorted(g):
        if v in seen: continue
        stack=[v]; seen.add(v); cc=[]
        while stack:
            u=stack.pop(); cc.append(u)
            for w in g[u]:
                if w not in seen:
                    seen.add(w); stack.append(w)
        out.append(tuple(sorted(cc)))
    return sorted(out,key=lambda z:(-len(z),z))

for e in eqs:
    assert max(map(len,components(emap[e])))==2
assert max(map(len,components(emap[faceeq])))==2

# ---------------------------------------------------------------------------
# C. Exact reference-strata lattice at r0=7/2
# ---------------------------------------------------------------------------
r0=sp.Rational(7,2); D0=1+2*r0; L0=4+10*r0; E0=(r0+1)/2
P=[]
for idx,e in enumerate(eqs):
    q,k,rho,mu,nu=e
    const=-(sp.Rational(q.numerator,q.denominator)*L0+sp.Rational(k.numerator,k.denominator)*D0)
    P.append((idx,sp.Matrix([sp.Rational(nu),sp.Rational(rho),sp.Rational(mu)]),const))
Dfac=[
('s0',sp.Matrix([1,0,0]),sp.Rational(0)),
('R=s',sp.Matrix([-1,1,0]),sp.Rational(0)),
('e=R',sp.Matrix([0,-1,1]),sp.Rational(0)),
('e=E',sp.Matrix([0,0,1]),sp.Rational(E0))]

def solve3(pls):
    A=sp.Matrix.vstack(*[p[1].T for p in pls]); b=sp.Matrix([p[2] for p in pls])
    if A.rank()!=3 or A.row_join(b).rank()!=3: return None
    return A.inv()*b

def closure(z):
    s,R,e=z; return bool(0<=s<=R<=e<=E0)
def interior(z):
    s,R,e=z; return bool(0<s<R<e<E0)

def line_key(i,j):
    A=sp.Matrix.vstack(P[i][1].T,P[j][1].T); b=sp.Matrix([P[i][2],P[j][2]])
    if A.rank()!=2 or A.row_join(b).rank()!=2: return None
    rr=A.row_join(b).rref()[0]
    return tuple(tuple(rr[x,y] for y in range(4)) for x in range(rr.rows))

def line_active(i,j):
    pts=[]
    for d in Dfac:
        z=solve3([P[i],P[j],d])
        if z is not None and closure(z): pts.append(z)
    uniq=[]
    for z in pts:
        if not any(z==u for u in uniq): uniq.append(z)
    if len(uniq)<2: return False
    avg=sum(uniq,sp.zeros(3,1))/len(uniq)
    return interior(avg)

lines={}
for i,j in combinations(range(18),2):
    key=line_key(i,j)
    if key is None or not line_active(i,j): continue
    A=sp.Matrix.vstack(P[i][1].T,P[j][1].T); b=sp.Matrix([P[i][2],P[j][2]])
    active=[]
    for k,p in enumerate(P):
        AA=sp.Matrix.vstack(A,p[1].T); bb=sp.Matrix.vstack(b,sp.Matrix([p[2]]))
        if AA.rank()==2 and AA.row_join(bb).rank()==2: active.append(k)
    lines[key]=tuple(active)
assert len(lines)==35
assert Counter(len(x) for x in lines.values())==Counter({2:35})

points={}
for ids in combinations(range(18),3):
    z=solve3([P[i] for i in ids])
    if z is None or not interior(z): continue
    active=tuple(i for i,p in enumerate(P) if p[1].dot(z)==p[2])
    points[tuple(z)]=active
assert len(points)==10
assert Counter(len(x) for x in points.values())==Counter({3:10})

# Boundary-label classes remain pairwise even on all open-interior intersections.
for active in lines.values():
    edges=[]
    for i in active: edges += emap[eqs[i]]
    assert max(map(len,components(edges)))==2
for active in points.values():
    edges=[]
    for i in active: edges += emap[eqs[i]]
    assert max(map(len,components(edges)))==2

# ---------------------------------------------------------------------------
# D. Allowed SW1 face sigma=R
# ---------------------------------------------------------------------------
Fface=('R=s',sp.Matrix([-1,1,0]),sp.Rational(0))
face_facets=[
('s0',sp.Matrix([1,0,0]),sp.Rational(0)),
('e=R',sp.Matrix([0,-1,1]),sp.Rational(0)),
('e=E',sp.Matrix([0,0,1]),sp.Rational(E0))]

face_lines=[]
for i,p in enumerate(P):
    pts=[]
    for d in face_facets:
        z=solve3([Fface,p,d])
        if z is not None:
            s,R,e=z
            if 0<=s and s==R and R<=e<=E0: pts.append(z)
    uniq=[]
    for z in pts:
        if not any(z==u for u in uniq): uniq.append(z)
    if len(uniq)<2: continue
    avg=sum(uniq,sp.zeros(3,1))/len(uniq)
    s,R,e=avg
    if not (0<s and s==R and R<e<E0): continue
    edges=list(emap[faceeq])+list(emap[eqs[i]])
    cls=components(edges)
    face_lines.append((i,max(map(len,cls))))

assert len(face_lines)==17
assert [i for i,_ in face_lines]==[0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17]
assert [m for _,m in face_lines]==[4,3,4,2,3,4,3,3,4,3,2,3,2,3,4,3,4]
assert Counter(m for _,m in face_lines)==Counter({3:8,4:6,2:3})

face_points={}
for i,j in combinations(range(18),2):
    z=solve3([Fface,P[i],P[j]])
    if z is None: continue
    s,R,e=z
    if not (0<s and s==R and R<e<E0): continue
    active=tuple(k for k,p in enumerate(P) if p[1].dot(z)==p[2])
    face_points[tuple(z)]=active
assert len(face_points)==6
assert Counter(len(x) for x in face_points.values())==Counter({4:3,3:2,5:1})

point_max=[]
for z,active in sorted(face_points.items()):
    edges=list(emap[faceeq])
    for i in active: edges += emap[eqs[i]]
    point_max.append(max(map(len,components(edges))))
assert point_max==[4,4,4,3,3,3]

# Deterministic face-point coordinate ledger.
assert sorted(face_points)==[
    (sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1)),
    (sp.Rational(1,2),sp.Rational(1,2),sp.Rational(3,2)),
    (sp.Rational(1,2),sp.Rational(1,2),sp.Rational(7,4)),
    (sp.Rational(3,4),sp.Rational(3,4),sp.Rational(7,4)),
    (sp.Rational(1),sp.Rational(1),sp.Rational(7,4)),
    (sp.Rational(1),sp.Rational(1),sp.Rational(2))]

print('SW1-A10-C1B2C HIGHER-DEGENERACY / COLLISION-STRATA CERTIFICATE: PASS')
print('higher-degeneracy witnesses searched exhaustively at subset sizes 2,3,4 among 18 planes + 4 simplex facets')
print('critical roots by subset size: |R2|=3, |R3|=8, |R4|=17; union is exactly the C1B2A 17-value critical set')
print('size-4 subsets contribute 9 critical values not visible from sizes 2 or 3')
print('18 generic interior collision planes map to label-pair counts:',','.join(map(str,pair_count)))
print('generic interior plane collision classes are all size 2')
print('reference open simplex: 35 codim-2 lines, each on exactly 2 planes; 10 codim-3 points, each on exactly 3 planes')
print('all label-collision classes on those open-interior lines/points remain size 2')
print('allowed face sigma=R: 23 generic pair collisions; 17 face-lines with max class sizes',','.join(str(m) for _,m in face_lines))
print('allowed face has 6 interior intersection points; active-plane multiplicities 3/4/5 and max label-class sizes 4,4,4,3,3,3')
print('FIREWALL: exact reference-strata ledger only; no actual-r transfer, final fiber N, matrices or injectivity claim')
