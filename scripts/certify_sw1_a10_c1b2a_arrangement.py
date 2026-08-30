#!/usr/bin/env python3
from itertools import combinations
import sympy as sp

r=sp.symbols('r')
# planes: a dot (sigma,R,eps) = b0+b1*r
H=[]
def hp(name,a,b0=0,b1=0): H.append((name,sp.Matrix([sp.Rational(x) for x in a]),sp.Rational(b0)+sp.Rational(b1)*r))
# A family (=r)
hp('A_2R',[0,2,0],0,1); hp('A_R+e',[0,1,1],0,1); hp('A_R+s',[1,1,0],0,1)
hp('A_2e',[0,0,2],0,1); hp('A_e+s',[1,0,1],0,1); hp('A_2s',[2,0,0],0,1)
# B family (=1)
hp('B_e-R',[0,-1,1],1,0); hp('B_s',[1,0,0],1,0); hp('B_2s',[2,0,0],1,0)
hp('B_e-s',[-1,0,1],1,0); hp('B_e',[0,0,1],1,0); hp('B_e+s',[1,0,1],1,0)
hp('B_2e',[0,0,2],1,0); hp('B_R-s',[-1,1,0],1,0); hp('B_R',[0,1,0],1,0)
hp('B_R+s',[1,1,0],1,0); hp('B_R+e',[0,1,1],1,0); hp('B_2R',[0,2,0],1,0)
# simplex facets: sigma=0, R=sigma, eps=R, eps=(r+1)/2
hp('D_s0',[1,0,0],0,0); hp('D_R=s',[-1,1,0],0,0); hp('D_e=R',[0,-1,1],0,0); hp('D_e=E',[0,0,1],sp.Rational(1,2),sp.Rational(1,2))
assert len(H)==22

# all r values where a dependent subset (2..4 planes) becomes consistent;
# these are all possible incidence/tangency/concurrency changes of the clipped arrangement.
critical=set()
for ksize in (2,3,4):
    for inds in combinations(range(len(H)),ksize):
        A=sp.Matrix.vstack(*[H[i][1].T for i in inds])
        b=sp.Matrix([H[i][2] for i in inds])
        left=A.T.nullspace()
        if not left: continue
        conds=[sp.expand((v.T*b)[0]) for v in left]
        if all(c==0 for c in conds): continue
        roots=None; possible=True
        for c in conds:
            if c==0: continue
            p=sp.Poly(c,r)
            if p.degree()==0:
                possible=False; break
            vals=set(sp.solve(sp.Eq(c,0),r))
            roots=vals if roots is None else roots & vals
        if possible and roots:
            for val in roots:
                if val.is_Rational: critical.add(val)
expected={sp.Rational(x) for x in [-3,-2,-1,0,1,2,3,4,5,6]}
expected|={sp.Rational(-1,2),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(2,3),sp.Rational(4,3),sp.Rational(3,2),sp.Rational(5,2)}
assert critical==expected
assert not any(sp.Rational(3)<x<sp.Rational(4) for x in critical)

# exact project ratio: s*=L/2-2D, chi=5D-L.
# s*>3chi iff 2^65>3^41; s*<4chi iff 3^53>2^84.
assert 2**65 > 3**41
assert 3**53 > 2**84

# exact rational sample r0=7/2
r0=sp.Rational(7,2); E0=(r0+1)/2
P=[]
def pp(name,a,c): P.append((name,sp.Matrix([sp.Rational(x) for x in a]),sp.Rational(c)))
for name,a,b in [
('A_2R',[0,2,0],r0),('A_R+e',[0,1,1],r0),('A_R+s',[1,1,0],r0),
('A_2e',[0,0,2],r0),('A_e+s',[1,0,1],r0),('A_2s',[2,0,0],r0),
('B_e-R',[0,-1,1],1),('B_s',[1,0,0],1),('B_2s',[2,0,0],1),
('B_e-s',[-1,0,1],1),('B_e',[0,0,1],1),('B_e+s',[1,0,1],1),
('B_2e',[0,0,2],1),('B_R-s',[-1,1,0],1),('B_R',[0,1,0],1),
('B_R+s',[1,1,0],1),('B_R+e',[0,1,1],1),('B_2R',[0,2,0],1)]: pp(name,a,b)
D=[]
def dd(name,a,c): D.append((name,sp.Matrix([sp.Rational(x) for x in a]),sp.Rational(c)))
dd('s=0',[1,0,0],0); dd('R=s',[-1,1,0],0); dd('e=R',[0,-1,1],0); dd('e=E',[0,0,1],E0)

def solve3(pls):
    A=sp.Matrix.vstack(*[p[1].T for p in pls]); b=sp.Matrix([p[2] for p in pls])
    if A.rank()!=3: return None
    v=A.inv()*b
    return tuple(sp.factor(x) for x in v)

def closure(x):
    s,R,e=x; return s>=0 and R-s>=0 and e-R>=0 and E0-e>=0

def interior(x):
    s,R,e=x; return s>0 and R-s>0 and e-R>0 and E0-e>0

def lkey(pi,pj):
    A=sp.Matrix.vstack(pi[1].T,pj[1].T); b=sp.Matrix([pi[2],pj[2]])
    if A.rank()<2: return None
    aug=A.row_join(b)
    if aug.rank()!=2: return None
    rr,_=aug.rref()
    return tuple(tuple(rr[i,j] for j in range(4)) for i in range(rr.rows))

def line_active(pi,pj):
    pts=set()
    for d in D:
        z=solve3([pi,pj,d])
        if z is not None and closure(z): pts.add(z)
    if len(pts)<2: return False
    avg=tuple(sp.factor(sum(z[k] for z in pts)/len(pts)) for k in range(3))
    return interior(avg)

def crosspoint(pi,pj,pk):
    z=solve3([pi,pj,pk])
    return z if z is not None and interior(z) else None

total=1; profile=[]
for i,pi in enumerate(P):
    lines={}
    for j in range(i):
        key=lkey(pi,P[j])
        if key is not None and line_active(pi,P[j]) and key not in lines: lines[key]=j
    items=sorted(lines.items(),key=lambda kv:kv[1])
    reg2=1; prev=[]
    for key,j in items:
        pts=set()
        for key2,k in prev:
            z=crosspoint(pi,P[j],P[k])
            if z is not None: pts.add(z)
        reg2 += 1+len(pts)
        prev.append((key,j))
    total += reg2
    profile.append((pi[0],len(items),reg2))
assert total==64
assert [x[2] for x in profile]==[1,1,1,1,2,1,2,5,6,8,2,1,1,9,9,6,1,6]

print('SW1-A10-C1B2A HYPERPLANE-ARRANGEMENT CERTIFICATE: PASS')
print('exact normalized ratio r=s*/chi satisfies 3<r<4')
print('all critical incidence ratios:', ','.join(str(x) for x in sorted(critical)))
print('no critical incidence/tangency ratio lies in the open interval (3,4)')
print('exact rational reference r0=7/2 has 64 open chambers in 0<sigma<R<epsilon<(r0+1)/2')
print('2D slice-region profile:', ','.join(str(x[2]) for x in profile))
print('FIREWALL: certificate proves critical-ratio set and rational-sample chamber count; transfer to actual r uses the standard no-degeneracy isotopy lemma')
