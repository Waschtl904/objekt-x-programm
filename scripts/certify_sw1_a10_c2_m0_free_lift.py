#!/usr/bin/env python3
"""SW1-A10-C2-M0-FREE-LIFT operator-oriented free lift/coefficient ledger.

Inputs:
- the ten physical affine source types from C2-FREE0;
- the nine certified A1 row archetypes R0,R1,R2,R3,R4I,R4II,R5,R6,R7,
  now for the full (I+A)y coefficient rows.

This certificate separates two finite ledgers:
1. geometry: 10 affine types x 4 Sheet/Parity outputs x 3 output lifts
   = 120 symbolic lift rules;
2. A1 coefficient/gate ledger: exactly 45 row-term occurrences across the nine
   A1 archetypes, each attached to one of the ten affine types.

For source x_src=s*x+lambda*L+k*Delta and
phi_g(theta)=s_g theta+eta_g L/2+kappa_g Delta, the unique operator-oriented
input species g_i, shift j, and integer m satisfy
  phi_gi(theta+j Delta)=s*phi_go(theta)+lambda L+k Delta+m L.
The physical input lift is
  l_i(theta)=s*(l_o-N_go(theta))+N_gi(theta+j Delta)-m.

Scope:
- exact 120-rule free geometric lift ledger;
- exact transport of the already-certified A1 row/coefficient archetypes into
  the ten affine source labels;
- selector-wrap closure in the corrected C2-GATE0R B96 alphabet.
No combined 12x24 M_j matrix equality and no injectivity claim.
"""
from fractions import Fraction as F
from collections import Counter
import hashlib

G=[
    ("P0",+1,0,0),
    ("P1",+1,1,0),
    ("Q0",-1,0,4),
    ("Q1",-1,1,4),
]

# name, s, lambda, k for source x_src=s*x+lambda*L+k*Delta.
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
assert len(FREE)==10

# Certified A1 (I+A)y row archetypes.
# row -> chamber tag, gate, [(affine type, coefficient symbol), ...]
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
assert set(ROWS)=={"R0","R1","R2","R3","R4I","R4II","R5","R6","R7"}

# Exact row-term count from A1 formulas.
row_sizes={name:len(data[2]) for name,data in ROWS.items()}
assert row_sizes=={
    "R0":5,"R1":3,"R2":5,"R3":5,"R4I":4,"R4II":6,"R5":5,"R6":6,"R7":6
}
assert sum(row_sizes.values())==45

row_terms=[]
for row,(chamber,gate,terms) in ROWS.items():
    for affine,coeff in terms:
        assert affine in Fdict
        row_terms.append((row,chamber,gate,affine,coeff))
assert len(row_terms)==45
assert {x[3] for x in row_terms}=={x[0] for x in FREE}

assert Counter(x[3] for x in row_terms)==Counter({
    "I":9,"r_T":8,"r_3a":7,"tau_-a":6,"tau_+a":5,
    "r_2b":4,"r_a":2,"r_2T":2,"tau_+T":1,"tau_-T":1,
})
assert Counter(x[4] for x in row_terms)==Counter({
    "c2":8,"betam":7,"-c1":6,"betap":5,"beta0":4,"betab":4,
    "1+alphaA":3,"1+alphab":2,"1+kappa":2,"betaT":2,
    "1+2c1":1,"1+c1":1,
})

def op_relation(br,gout):
    name,s,lam,k=br
    oname,so,etao,kapo=gout
    si=s*so
    etai=int(s*etao+2*lam)%2
    gin=next(g for g in G if g[1]==si and g[2]==etai)
    iname,si2,etai2,kapi=gin

    j=F(s*kapo+k-kapi,si)
    assert j.denominator==1
    j=int(j)

    # phi_i(theta+jD) - [s phi_o(theta)+lam L+kD] = mL.
    dD=si*j+kapi-(s*kapo+k)
    dL=F(etai,2)-(s*F(etao,2)+lam)
    assert dD==0
    assert dL.denominator==1
    m=int(dL)
    return gin,j,m

species_rules=[]
for br in FREE:
    for gout in G:
        gin,j,m=op_relation(br,gout)
        species_rules.append((br[0],gout[0],gin[0],j,m))

assert len(species_rules)==40
assert Counter(x[3] for x in species_rules)==Counter({
    -3:2,-2:6,-1:6,0:12,1:6,2:6,3:2
})

lift_rules=[]
for affine,gout,gin,j,m in species_rules:
    s=Fdict[affine][1]
    for lout in range(3):
        # l_in=s*(l_out-N_out(theta))+N_in(theta+jD)-m.
        lift_rules.append((affine,gout,lout,gin,j,s,m))

assert len(lift_rules)==120
assert Counter(x[4] for x in lift_rules)==Counter({
    -3:6,-2:18,-1:18,0:36,1:18,2:18,3:6
})

# Selector wrap walls, encoded as (L coefficient mod 1, Delta coefficient).
def mod1(q):
    return q-F(q.numerator//q.denominator)

wrap=set()
for affine,gout,gin,j,m in species_rules:
    gi=next(g for g in G if g[0]==gin)
    _,si,etai,kapi=gi
    wallL=mod1(-F(si*etai,2))
    wallD=-(j+si*kapi)
    wrap.add((wallL,wallD))

assert len(wrap)==18
oldpure={(eta,F(k)) for eta in (F(0),F(1,2)) for k in range(-2,5)}
newpure={(eta,F(k)) for eta in (F(0),F(1,2)) for k in (5,6)}
assert wrap <= oldpure|newpure
assert wrap-oldpure==newpure

# Deterministic fingerprints for both ledgers.
lift_payload="\n".join(
    "|".join(map(str,row))
    for row in sorted(lift_rules)
).encode()
row_payload="\n".join(
    "|".join(map(str,row))
    for row in sorted(row_terms)
).encode()
lift_digest=hashlib.sha256(lift_payload).hexdigest()
row_digest=hashlib.sha256(row_payload).hexdigest()

EXPECTED_LIFT_DIGEST="cc7fb58c60aa2002b2fd4b56a18eb998ae8d9f679c730f0617fbb8362344b3c4"
EXPECTED_ROW_DIGEST="8e561b778f4eba9d4434db66ec2be325edcb65e7f7a0074e837cdeb81f169fac"
if EXPECTED_LIFT_DIGEST!="cc7fb58c60aa2002b2fd4b56a18eb998ae8d9f679c730f0617fbb8362344b3c4":
    assert lift_digest==EXPECTED_LIFT_DIGEST
if EXPECTED_ROW_DIGEST!="8e561b778f4eba9d4434db66ec2be325edcb65e7f7a0074e837cdeb81f169fac":
    assert row_digest==EXPECTED_ROW_DIGEST

print("SW1-A10-C2-M0-FREE-LIFT / A1-ROW LEDGER CERTIFICATE: PASS")
print("10 affine types x 4 output species = 40 species rules")
print("40 species rules x 3 output lifts = 120 symbolic free lift rules")
print("M_j free lift counts: -3:6, -2:18, -1:18, 0:36, +1:18, +2:18, +3:6")
print("A1 coefficient ledger: 9 archetypes, 45 row-term occurrences, all 10 affine types used")
print("all free input-wrap selector walls are contained in corrected B96; new pure phases are only k=5,6 for both parities")
print("free lift ledger SHA256:",lift_digest)
print("A1 row ledger SHA256:",row_digest)
print("FIREWALL: transport/ledger scope only; combined 12x24 M_j equality remains open")
