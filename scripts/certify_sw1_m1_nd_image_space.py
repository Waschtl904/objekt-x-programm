#!/usr/bin/env python3
"""SW1 M1-ND IMG0 image-space reduction certificate.

Finite algebraic/mechanical scope:
- exact Klein-four sheet/parity maps;
- exact P0-range covariance skeleton for four species x three lifts;
- exact two-sided extension/restriction on a deterministic finite model;
- exact P0-output reduction of the already certified FREE/HUB species rules;
- exact 12-type effective affine alphabet after species elimination.

This does not certify the infinite-dimensional L2 change-of-variables,
closed-image theorem, or the KNF kernel row as an analytic statement.
"""
from fractions import Fraction as F

print("SW1 M1-ND IMG0 IMAGE-SPACE CERTIFICATE")

# ---------------------------------------------------------------------------
# 1. Exact sheet/parity affine maps modulo L.
# map = (slope, L_coeff mod 1, Delta_coeff)
# ---------------------------------------------------------------------------
P0=(+1,F(0),F(0))
P1=(+1,F(1,2),F(0))
Q0=(-1,F(0),F(4))
Q1=(-1,F(1,2),F(4))
G=(P0,P1,Q0,Q1)
GN=("P0","P1","Q0","Q1")

def mod1(q):
    return q-F(q.numerator//q.denominator)

def norm(m):
    s,l,d=m
    return (s,mod1(l),d)

def compose(f,g):
    sf,lf,df=f
    sg,lg,dg=g
    return norm((sf*sg, sf*lg+lf, sf*dg+df))

assert compose(P1,P1)==P0
assert compose(Q0,Q0)==P0
assert compose(P1,Q0)==Q1
assert compose(Q0,P1)==Q1
assert compose(Q1,Q1)==P0
assert set(G)=={P0,P1,Q0,Q1}

# ---------------------------------------------------------------------------
# 2. Finite exact covariance/reconstruction toy model.
#    The group action is mirrored on a 14-point circle; masks are arbitrary
#    P0 masks pulled back by the species permutations.
# ---------------------------------------------------------------------------
N=14
half=N//2
reflection_offset=4

def rho(name,t):
    if name=="P0":
        return t%N
    if name=="P1":
        return (t+half)%N
    if name=="Q0":
        return (reflection_offset-t)%N
    if name=="Q1":
        return (reflection_offset-t+half)%N
    raise KeyError(name)

# Three lift base functions and deliberately nontrivial support masks.
base={(k,t): 100*k+t+1 for k in range(3) for t in range(N)}
mask0={(k,t): int(((t+2*k)%5)!=0) for k in range(3) for t in range(N)}
base_masked={(k,t):mask0[(k,t)]*base[(k,t)] for k in range(3) for t in range(N)}

# Species extension E: F[g,k](theta)=base_k(rho_g(theta)).
ext={}
for g in GN:
    for k in range(3):
        for t in range(N):
            ext[(g,k,t)]=base_masked[(k,rho(g,t))]

# P0 restriction R and right/left inverse checks.
recovered={(k,t):ext[("P0",k,t)] for k in range(3) for t in range(N)}
assert recovered==base_masked

reextended={}
for g in GN:
    for k in range(3):
        for t in range(N):
            reextended[(g,k,t)]=recovered[(k,rho(g,t))]
assert reextended==ext

# Explicit covariance for all species/lifts/base points.
for g in GN:
    for k in range(3):
        for t in range(N):
            assert ext[(g,k,t)]==ext[("P0",k,rho(g,t))]

# ---------------------------------------------------------------------------
# 3. Output-side P0 injectivity on the true symmetric horizon image.
# ---------------------------------------------------------------------------
# Build a second, nontrivial valid horizon-output sample independently of the
# input sample above. It satisfies the same species covariance because the
# physical output is again covered by U_H.
out_base={(k,t): (k+1)*(t+3) for k in range(3) for t in range(N)}
out_mask={(k,t): int(((2*t+k)%7)!=1) for k in range(3) for t in range(N)}
out_p0={(k,t):out_mask[(k,t)]*out_base[(k,t)] for k in range(3) for t in range(N)}

out_full={}
for g in GN:
    for k in range(3):
        for t in range(N):
            out_full[(g,k,t)]=out_p0[(k,rho(g,t))]

# Restrict to P0 and reconstruct the complete valid output.
out_restricted={(k,t):out_full[("P0",k,t)] for k in range(3) for t in range(N)}
assert out_restricted==out_p0

out_reconstructed={}
for g in GN:
    for k in range(3):
        for t in range(N):
            out_reconstructed[(g,k,t)]=out_restricted[(k,rho(g,t))]
assert out_reconstructed==out_full

# Explicit injectivity of P0 restriction on the valid output image:
# if all P0 output components vanish, covariance forces every species to vanish.
zero_p0={(k,t):0 for k in range(3) for t in range(N)}
zero_full={}
for g in GN:
    for k in range(3):
        for t in range(N):
            zero_full[(g,k,t)]=zero_p0[(k,rho(g,t))]
assert all(v==0 for v in zero_full.values())

# Conversely, the full zero output trivially restricts to P0 zero.
full_zero={key:0 for key in out_full}
restricted_full_zero={(k,t):full_zero[("P0",k,t)] for k in range(3) for t in range(N)}
assert all(v==0 for v in restricted_full_zero.values())

# Therefore on the valid symmetric horizon image:
#     R_P0(F)=0  <=>  F=0.
assert any(v!=0 for v in out_full.values())
assert any(v!=0 for v in out_restricted.values())

# ---------------------------------------------------------------------------
# 4. Exact P0-output elimination for FREE and HUB species rules.
# ---------------------------------------------------------------------------
FREE=[
    ("I",       +1,F(0), 0),
    ("r_a",     -1,F(1), 1),
    ("tau_+a",  +1,F(1), 1),
    ("r_T",     -1,F(2), 2),
    ("tau_+T",  +1,F(2), 2),
    ("r_3a",    -1,F(3), 3),
    ("tau_-a",  +1,F(-1),-1),
    ("r_2b",    -1,F(3), 4),
    ("r_2T",    -1,F(4), 4),
    ("tau_-T",  +1,F(-2),-2),
]

HUB=[
    ("A_L",-1,F(1),1,"-p"),
    ("A_R",+1,F(1),1,"+p"),
    ("A_O",+1,F(-1),-1,"-p"),
    ("B_L",-1,F(3,2),2,"-r"),
    ("B_R",+1,F(3,2),2,"+r"),
    ("B_O",+1,F(-3,2),-2,"-r"),
    ("T_L",-1,F(2),2,"-q"),
    ("T_R",+1,F(2),2,"+q"),
    ("T_O",+1,F(-2),-2,"-q"),
]

GDATA=[
    ("P0",+1,0,0),
    ("P1",+1,1,0),
    ("Q0",-1,0,4),
    ("Q1",-1,1,4),
]
P0DATA=GDATA[0]

def free_op_relation(br,gout):
    name,s,lam,k=br
    oname,so,etao,kapo=gout
    si=s*so
    etai=int(s*etao+2*lam)%2
    gin=next(g for g in GDATA if g[1]==si and g[2]==etai)
    _,si2,etai2,kapi=gin
    j=F(s*kapo+k-kapi,si)
    assert j.denominator==1
    return gin,int(j)

def hub_op_relation(ch,gout):
    name,s,lam,k,coeff=ch
    oname,so,etao,kapo=gout
    lamsrc=-s*lam
    ksrc=-s*k
    si=s*so
    parity_twice=s*etao+2*lamsrc
    assert parity_twice.denominator==1
    etai=int(parity_twice)%2
    gin=next(g for g in GDATA if g[1]==si and g[2]==etai)
    _,si2,etai2,kapi=gin
    j=F(s*kapo+ksrc-kapi,si)
    assert j.denominator==1
    return gin,int(j)

def effective_base_map(gin,j):
    # rho_g(theta+j Delta)
    name,s,eta,kappa=gin
    return (s,F(eta,2),s*j+kappa)

free_rows=[]
for br in FREE:
    gin,j=free_op_relation(br,P0DATA)
    free_rows.append((br[0],gin[0],j,effective_base_map(gin,j)))

hub_rows=[]
for ch in HUB:
    gin,j=hub_op_relation(ch,P0DATA)
    hub_rows.append((ch[0],gin[0],j,effective_base_map(gin,j),ch[4]))

free_types={row[3] for row in free_rows}
hub_types={row[3] for row in hub_rows}
all_types=free_types|hub_types

expected_free={
    (+1,F(0),-2),
    (+1,F(0),-1),
    (+1,F(0),0),
    (+1,F(0),1),
    (+1,F(0),2),
    (-1,F(0),1),
    (-1,F(0),2),
    (-1,F(0),3),
    (-1,F(0),4),
}
assert free_types==expected_free
assert len(free_types)==9

expected_half={
    (-1,F(1,2),2),
    (+1,F(1,2),-2),
    (+1,F(1,2),2),
}
assert {x for x in hub_types if x[1]==F(1,2)}==expected_half
assert len(hub_types)==9

expected_all=expected_free|expected_half
assert all_types==expected_all
assert len(all_types)==12

# The free effective maps contain no half-period pullback.
assert all(x[1]==0 for x in free_types)

# Only the B hub branches generate the half-period maps.
half_hub_names={row[0] for row in hub_rows if row[3][1]==F(1,2)}
assert half_hub_names=={"B_L","B_R","B_O"}

# ---------------------------------------------------------------------------
# 5. Structural slot-count firewall.
# ---------------------------------------------------------------------------
formal_species=4
lifts=3
formal_H=formal_species*lifts
formal_W=formal_species*lifts
assert formal_H+formal_W==24

independent_base_H=lifts
independent_base_W=lifts
assert independent_base_H+independent_base_W==6

print("Klein-four sheet/parity algebra: PASS")
print("P0 covariance and two-sided input-range reconstruction: PASS")\nprint("P0 output restriction is injective on valid symmetric horizon image: PASS")
print("formal input cover: 12_H + 12_W = 24 slots")
print("valid symmetric-cover data determined by 3_H + 3_W base-lift functions")
print("P0-output FREE effective affine types: 9")
print("P0-output HUB effective affine types: 9")
print("union effective affine types after species elimination: 12")
print("only B hub branches introduce L/2 pullbacks: PASS")
print("FIREWALL: 24->6 is a function-channel reduction, not finite dimension")
print("SW1 M1-ND IMG0 IMAGE-SPACE CERTIFICATE: PASS")
