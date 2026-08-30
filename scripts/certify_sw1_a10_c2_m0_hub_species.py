#!/usr/bin/env python3
"""SW1-A10-C2-M0-HUB-SPEC operator-oriented hub species certificate.

The earlier C2-HUB0 table was encoded as an input->output displacement:
  output_base = input_base + j_disp*Delta.
For the final operator convention
  (C F)(theta) = sum_j M_j(theta) F(theta+j*Delta),
we need the inverse orientation:
  input_base = output_base + j_op*Delta.

This certificate derives the operator-oriented table directly from the nine
physical relations x=s*t+lambda*L+k*Delta and verifies it is exactly the inverse
of the committed HUB0 relation, with j_op=-j_disp after swapping input/output.

Scope: Sheet/Parity species blocks only. Lift selectors and physical gates
remain for M0-HUB-LIFT.
"""
from fractions import Fraction as F
from collections import Counter

G=[
    ("P0",+1,0,0),
    ("P1",+1,1,0),
    ("Q0",-1,0,4),
    ("Q1",-1,1,4),
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

def hub0_input_to_output(ch,gin):
    name,s,lam,k,coeff=ch
    iname,si,etai,kapi=gin
    so=s*si
    parity_twice=s*etai+2*lam
    assert parity_twice.denominator==1
    etaout=int(parity_twice)%2
    gout=next(g for g in G if g[1]==so and g[2]==etaout)
    oname,so2,etao,kapo=gout
    jdisp=F(s*kapi+k-kapo,so)
    assert jdisp.denominator==1
    return oname,int(jdisp)

def operator_output_to_input(ch,gout):
    name,s,lam,k,coeff=ch
    # Solve the physical branch for the source:
    # t = s*x - s*lam*L - s*k*Delta.
    ss=s
    lamsrc=-s*lam
    ksrc=-s*k

    oname,so,etao,kapo=gout
    si=ss*so
    parity_twice=ss*etao+2*lamsrc
    assert parity_twice.denominator==1
    etain=int(parity_twice)%2
    gin=next(g for g in G if g[1]==si and g[2]==etain)
    iname,si2,etai,kapi=gin
    jop=F(ss*kapo+ksrc-kapi,si)
    assert jop.denominator==1
    return iname,int(jop)

old=[]
for ch in HUB:
    for gin in G:
        gout,jdisp=hub0_input_to_output(ch,gin)
        old.append((ch[0],gin[0],gout,jdisp,ch[4]))

op=[]
for ch in HUB:
    seen_inputs=set()
    for gout in G:
        gin,jop=operator_output_to_input(ch,gout)
        op.append((ch[0],gout[0],gin,jop,ch[4]))
        seen_inputs.add(gin)
    assert seen_inputs=={g[0] for g in G}

assert len(old)==len(op)==36

# Exact inverse-relation identity.
old_inverse={(name,gout,gin,-j,c) for name,gin,gout,j,c in old}
assert set(op)==old_inverse

counts=Counter(j for _,_,_,j,_ in op)
assert counts==Counter({-3:2,-2:12,-1:4,1:4,2:12,3:2})
assert set(counts)=={-3,-2,-1,1,2,3}

# Each branch gives exactly one input species for each output species.
for ch in HUB:
    rows=[x for x in op if x[0]==ch[0]]
    assert len(rows)==4
    assert {x[1] for x in rows}=={g[0] for g in G}
    assert len({(x[1],x[2]) for x in rows})==4

print("SW1-A10-C2-M0-HUB-SPEC OPERATOR-ORIENTATION CERTIFICATE: PASS")
print("36 physical hub Sheet/Parity transitions rederived in output<-input convention")
print("operator shifts j counts: -3:2, -2:12, -1:4, +1:4, +2:12, +3:2")
print("operator-oriented table is exactly the inverse of HUB0 input->output table")
print("therefore HUB0 radius |j|<=3 remains correct, but M_j uses the operator-oriented signs")
print("FIREWALL: species blocks only; lift selectors/gates remain for M0-HUB-LIFT")
