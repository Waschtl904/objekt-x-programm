#!/usr/bin/env python3
"""SW1-A10-C2-M0-HUB-LIFT exact symbolic lift-selector ledger.

For the operator convention
  (C F)(theta)=sum_j M_j(theta)F(theta+j Delta),
this certificate expands the 36 operator-oriented physical hub Sheet/Parity
relations over the three output horizon lifts, producing 108 symbolic rules.

For a branch x=s*t+lambda L+k Delta, solve
  t=s*x-s*lambda L-s*k Delta.
Let phi_g(theta)=s_g theta+eta_g L/2+kappa_g Delta and
N_g(theta)=(phi_g(theta)-rho_g(theta))/L in Z.
For each output species/lift (g_o,l_o), the unique input species g_i, shift j,
and constant integer m satisfy
  phi_gi(theta+j Delta)
   = s*phi_go(theta)-s*lambda L-s*k Delta + m L.
Then the physical input lift is exactly
  l_i(theta)
   = s*(l_o-N_go(theta))+N_gi(theta+j Delta)-m.

Scope:
- exact 108-rule symbolic lift ledger;
- exact affine identities and operator shift orientation;
- selector-wrap boundaries agree with the already certified operator-oriented C2-GATE0R selector set.
No claim yet about the free (I+A) block or the combined 12x24 matrices.
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

# branch: name, s in x=s*t+lam L+kD, lam, k, coefficient, output gate label
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

def op_relation(ch,gout):
    name,s,lam,k,coeff,gate=ch
    oname,so,etao,kapo=gout

    # source map t=s*x+lamsrc L+ksrc D
    lamsrc=-s*lam
    ksrc=-s*k

    si=s*so
    parity_twice=s*etao+2*lamsrc
    assert parity_twice.denominator==1
    etai=int(parity_twice)%2
    gin=next(g for g in G if g[1]==si and g[2]==etai)
    iname,si2,etai2,kapi=gin

    j=F(s*kapo+ksrc-kapi,si)
    assert j.denominator==1
    j=int(j)

    # phi_i(theta+jD) - [s phi_o(theta)+lamsrc L+ksrc D] = m L
    dD=si*j+kapi-(s*kapo+ksrc)
    dL=F(etai,2)-(s*F(etao,2)+lamsrc)
    assert dD==0
    assert dL.denominator==1
    m=int(dL)

    return gin,j,m

species_rules=[]
for ch in HUB:
    for gout in G:
        gin,j,m=op_relation(ch,gout)
        species_rules.append((ch[0],gout[0],gin[0],j,m,ch[4],ch[5]))

assert len(species_rules)==36
assert Counter(x[3] for x in species_rules)==Counter({
    -3:2,-2:12,-1:4,1:4,2:12,3:2
})

lift_rules=[]
for name,gout,gin,j,m,coeff,gate in species_rules:
    s=next(ch[1] for ch in HUB if ch[0]==name)
    for lout in range(3):
        # The input lift is the symbolic integer
        # s*(lout-N_out(theta))+N_in(theta+jD)-m.
        lift_rules.append((name,gout,lout,gin,j,s,m,coeff,gate))

assert len(lift_rules)==108
assert Counter(x[4] for x in lift_rules)==Counter({
    -3:6,-2:36,-1:12,1:12,2:36,3:6
})

# Selector-wrap boundaries N_gin(theta+jD) change exactly at
# phi_gin(theta+jD)=0 mod L. Encode mod-L wall as (eta/2, kD).
def mod1(q):
    return q-F(q.numerator//q.denominator)

wrap=set()
for name,gout,gin,j,m,coeff,gate in species_rules:
    gi=next(g for g in G if g[0]==gin)
    _,si,etai,kapi=gi
    # si*(theta+jD)+eta_i L/2+kappa_i D = 0 mod L
    # solve for theta; after multiplying by si (±1), wall is
    # L coeff -si*eta_i/2 mod 1, D coeff -(j+si*kappa_i).
    wallL=mod1(-F(si*etai,2))
    wallD=-(j+si*kapi)
    wrap.add((wallL,wallD))

assert len(wrap)==14

# GATE0R old pure phases contain eta=0,1/2 and k=-2..4;
# the only new ones in the operator convention are eta=0,1/2 and k=5,6.
oldpure={(eta,F(k)) for eta in (F(0),F(1,2)) for k in range(-2,5)}
newpure={(eta,F(k)) for eta in (F(0),F(1,2)) for k in (5,6)}
assert wrap <= oldpure|newpure
assert wrap-oldpure==newpure

# Deterministic ledger fingerprint.
payload="\n".join(
    "|".join(map(str,row))
    for row in sorted(lift_rules)
).encode()
digest=hashlib.sha256(payload).hexdigest()
assert digest=="a6000b315c22a4464dd9ed5105be2bcd7ea0fd1ff44e32c5a1646ab1c6fc1508"

print("SW1-A10-C2-M0-HUB-LIFT SYMBOLIC LIFT LEDGER CERTIFICATE: PASS")
print("36 operator-oriented species rules x 3 output lifts = 108 symbolic hub lift rules")
print("M_j hub rule counts: -3:6, -2:36, -1:12, +1:12, +2:36, +3:6")
print("input lift formula: l_in=s*(l_out-N_out(theta))+N_in(theta+jDelta)-m")
print("all input-wrap selector walls are exactly contained in the C2-GATE0R 96-wall alphabet")
print("ledger SHA256:",digest)
print("FIREWALL: symbolic hub lift matrix only; free block and combined M_j remain open")
