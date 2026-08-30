#!/usr/bin/env python3
"""SW1-A10-C2-M1-RAW additive raw matrix assembly certificate.

Purpose:
Construct the final operator-oriented matrix ledger from the already certified
M0-HUB-LIFT and M0-FREE-LIFT/A1-ROW data WITHOUT overwriting collisions.

The matrix convention is
  (C F)(theta)=sum_{j=-3}^3 M_j(theta) F(theta+j Delta).

There are:
- 45 A1 free row terms x 4 output species x 3 output lifts = 540 free raw contributions;
- 9 hub branches x 4 output species x 3 output lifts = 108 hub raw contributions;
- 648 raw contributions total.

Each raw contribution is expanded to the three possible input lifts using a
selector indicator SEL(l_in(theta)=ell). This gives 1944 matrix atoms.
Matrix cells are built only by additive list aggregation keyed by
  (j, output_coordinate, input_coordinate).
No assignment/overwrite operation is used.

The resulting matrix entry is the formal finite sum of all its stored atoms,
each atom carrying its coefficient, physical output gate/chamber tag, and lift
selector. This proves additive assembly; later simplification/evaluation of
piecewise indicators is a separate M1 step.

Firewall:
- raw/additive matrix assembly only;
- no claim yet that all indicator sums have been simplified on every B96 atom;
- no injectivity claim.
"""
from fractions import Fraction as F
from collections import Counter, defaultdict
import hashlib

G=[
    ("P0",+1,0,0),
    ("P1",+1,1,0),
    ("Q0",-1,0,4),
    ("Q1",-1,1,4),
]
gidx={g[0]:i for i,g in enumerate(G)}

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
Fdict={x[0]:x for x in FREE}

ROWS={
"R0":("BOTH","0<x<eps",[
    ("I","1+2c1"),("r_a","c2"),("tau_+a","c2"),("r_T","beta0"),("tau_+T","beta0"),
]),
"R1":("BOTH","eps<x<a-eps",[
    ("I","1+c1"),("r_T","-c1"),("tau_+a","c2"),
]),
"R2":("BOTH","a-eps<x<a",[
    ("I","1+alphaA"),("r_T","-c1"),("r_3a","betam"),("tau_+a","betap"),("r_a","c2"),
]),
"R3":("BOTH","a<x<min(a+eps,2d-eps)",[
    ("I","1+alphaA"),("r_T","-c1"),("r_3a","betam"),("tau_+a","betap"),("tau_-a","c2"),
]),
"R4I":("I","a+eps<x<2d-eps",[
    ("I","1+alphaA"),("r_T","-c1"),("r_3a","betam"),("tau_-a","c2"),
]),
"R4II":("II","2d-eps<x<a+eps",[
    ("I","1+alphab"),("r_T","-c1"),("r_3a","betam"),("tau_+a","betap"),("tau_-a","c2"),("r_2b","betab"),
]),
"R5":("BOTH","max(a+eps,2d-eps)<x<T-eps",[
    ("I","1+alphab"),("r_T","-c1"),("r_3a","betam"),("tau_-a","c2"),("r_2b","betab"),
]),
"R6":("BOTH","T-eps<x<T",[
    ("I","1+kappa"),("r_T","beta0"),("r_3a","betam"),("r_2T","betaT"),("tau_-a","betap"),("r_2b","betab"),
]),
"R7":("BOTH","T<x<T+eps",[
    ("I","1+kappa"),("tau_-T","beta0"),("r_3a","betam"),("r_2T","betaT"),("tau_-a","betap"),("r_2b","betab"),
]),
}

HUB=[
    ("A_L",-1,F(1),1,"-p","0<x<a-R"),
    ("A_R",+1,F(1),1,"+p","a+R<x<T0"),
    ("A_O",+1,F(-1),-1,"-p","0<x<S-a"),
    ("B_L",-1,F(3,2),2,"-r","0<x<b-R"),
    ("B_R",+1,F(3,2),2,"+r","b+R<x<T0"),
    ("B_O",+1,F(-3,2),-2,"-r","0<x<S-b"),
    ("T_L",-1,F(2),2,"-q","0<x<T-R"),
    ("T_R",+1,F(2),2,"+q","T+R<x<T0"),
    ("T_O",+1,F(-2),-2,"-q","0<x<S-T"),
]

assert sum(len(v[2]) for v in ROWS.values())==45
assert len(HUB)==9

def free_op(br,gout):
    name,s,lam,k=br
    _,so,etao,kapo=gout
    si=s*so
    etai=int(s*etao+2*lam)%2
    gin=next(g for g in G if g[1]==si and g[2]==etai)
    _,_,_,kapi=gin
    j=F(s*kapo+k-kapi,si)
    assert j.denominator==1
    j=int(j)
    dD=si*j+kapi-(s*kapo+k)
    dL=F(etai,2)-(s*F(etao,2)+lam)
    assert dD==0 and dL.denominator==1
    return gin,j,int(dL)

def hub_op(ch,gout):
    name,s,lam,k,coeff,gate=ch
    lamsrc=-s*lam
    ksrc=-s*k
    _,so,etao,kapo=gout
    si=s*so
    etai=int(s*etao+2*lamsrc)%2
    gin=next(g for g in G if g[1]==si and g[2]==etai)
    _,_,_,kapi=gin
    j=F(s*kapo+ksrc-kapi,si)
    assert j.denominator==1
    j=int(j)
    dD=si*j+kapi-(s*kapo+ksrc)
    dL=F(etai,2)-(s*F(etao,2)+lamsrc)
    assert dD==0 and dL.denominator==1
    return gin,j,int(dL)

free_sr={}
for br in FREE:
    for gout in G:
        gin,j,m=free_op(br,gout)
        free_sr[(br[0],gout[0])]=(gin[0],j,m,br[1])

hub_sr={}
for ch in HUB:
    for gout in G:
        gin,j,m=hub_op(ch,gout)
        hub_sr[(ch[0],gout[0])]=(gin[0],j,m,ch[1])

raw=[]

# 540 free raw contributions.
for row,(chamber,gate,terms) in ROWS.items():
    for affine,coeff in terms:
        for gout in G:
            gin,j,m,s=free_sr[(affine,gout[0])]
            for lout in range(3):
                outidx=gidx[gout[0]]*3+lout
                raw.append((
                    "H",j,outidx,gout[0],lout,gin,s,m,
                    coeff,gate,chamber,row,affine
                ))

# 108 hub raw contributions.
for ch in HUB:
    name,s,lam,k,coeff,gate=ch
    for gout in G:
        gin,j,m,s2=hub_sr[(name,gout[0])]
        assert s2==s
        for lout in range(3):
            outidx=gidx[gout[0]]*3+lout
            raw.append((
                "W",j,outidx,gout[0],lout,gin,s,m,
                coeff,gate,"BOTH",name,name
            ))

assert len(raw)==648
assert Counter(x[0] for x in raw)==Counter({"H":540,"W":108})
assert Counter(x[1] for x in raw)==Counter({
    -3:18,-2:96,-1:120,0:180,1:120,2:96,3:18
})

# Expand every raw contribution to the three actual input matrix columns.
# Exactly one selector is active when the physical source lies in its
# three-lift cover; retaining all three indicator atoms makes the matrix
# expression explicit without choosing a sample theta.
atoms=[]
for block,j,outidx,gout,lout,gin,s,m,coeff,gate,chamber,source,affine in raw:
    for lin in range(3):
        inidx=(0 if block=="H" else 12)+gidx[gin]*3+lin
        selector=("SEL",s,lout,gout,gin,j,m,lin)
        atoms.append((
            j,outidx,inidx,
            block,coeff,gate,chamber,selector,source,affine
        ))

assert len(atoms)==1944

# CRITICAL FIREWALL: additive aggregation only.
# Each key stores a LIST of every contribution. There is no overwrite.
matrix=defaultdict(list)
for atom in atoms:
    key=atom[:3]  # (j,output,input)
    matrix[key].append(atom[3:])

# Conservation proves no atom was silently discarded/overwritten.
assert sum(len(v) for v in matrix.values())==len(atoms)==1944
assert len(matrix)==648

# Structural nonzero-cell counts by shift.
assert Counter(key[0] for key in matrix)==Counter({
    -3:36,-2:162,-1:90,0:72,1:90,2:162,3:36
})

# Exact additive multiplicity histogram of the 648 structurally nonempty cells.
mult=Counter(len(v) for v in matrix.values())
assert mult==Counter({
    1:396,
    2:36,
    5:36,
    6:72,
    7:36,
    8:36,
    9:36,
})
assert sum(mult.values())==648
assert sum(m*n for m,n in mult.items())==1944

# There are no duplicate FULL atoms (same cell + same gate/chamber/selector).
# Hence every stored atom is a genuinely distinct summand in the formal entry.
full_atom_keys=Counter(
    (a[0],a[1],a[2],a[5],a[6],a[7])
    for a in atoms
)
assert max(full_atom_keys.values())==1

# Free and hub input columns are disjoint in the 24-column ambient input.
assert all((a[3]=="H")==(a[2]<12) for a in atoms)
assert all(0<=a[1]<12 and 0<=a[2]<24 for a in atoms)

# Deterministic fingerprints.
raw_payload="\n".join(
    "|".join(map(str,row))
    for row in sorted(raw,key=str)
).encode()
atom_payload="\n".join(
    "|".join(map(str,row))
    for row in sorted(atoms,key=str)
).encode()
matrix_payload="\n".join(
    f"{key}|{tuple(sorted(matrix[key],key=str))}"
    for key in sorted(matrix)
).encode()

raw_digest=hashlib.sha256(raw_payload).hexdigest()
atom_digest=hashlib.sha256(atom_payload).hexdigest()
matrix_digest=hashlib.sha256(matrix_payload).hexdigest()

assert raw_digest=="fc9e2aed972c2f9ffa441d1dc0528aa9c75400d645bbf828b18ff78f4ce5de76"
assert atom_digest=="03d0a75b43dcfa6fc46a940fbc9aa0affe830c5281c35ea1eb13f72db40061ea"
assert matrix_digest=="513fc6b78c7b2bc770ef7ebca5612f817d2a47b3b60bda69bcac46ca76e22616"

print("SW1-A10-C2-M1-RAW ADDITIVE MATRIX ASSEMBLY CERTIFICATE: PASS")
print("raw contributions: 540 free + 108 hub = 648")
print("raw j counts: -3:18, -2:96, -1:120, 0:180, +1:120, +2:96, +3:18")
print("three input-lift selector atoms per raw contribution: 1944 total")
print("additive structural matrix cells: 648")
print("cell counts by j: -3:36, -2:162, -1:90, 0:72, +1:90, +2:162, +3:36")
print("cell multiplicity histogram: 396x1, 36x2, 36x5, 72x6, 36x7, 36x8, 36x9")
print("NO OVERWRITE: sum of stored cell-list lengths is exactly 1944")
print("raw ledger SHA256:",raw_digest)
print("matrix atom SHA256:",atom_digest)
print("additive matrix SHA256:",matrix_digest)
print("FIREWALL: raw additive M_j representation only; B96-atom simplification/operator equality remains for M1-FULL")
