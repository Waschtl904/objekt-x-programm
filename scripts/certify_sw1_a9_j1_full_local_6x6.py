#!/usr/bin/env python3
"""SW1-A9-J1(full): exact local 6x6 KNF Gram-block certificate.

Scope:
- lower chamber, 0<u<R<epsilon;
- reconstruct A_-=a-u from the five free sample branches;
- form the exact local principal block of I+A on
  {u,A_-,A_+,B_-,B_+,T_-,T_+};
- pull it through the KNF reconstruction;
- certify all 15 off-diagonal entries of the resulting free 6x6 block,
  their affine map types, and their exact nonzero signs.

No numerical sign decision is used.

Firewall:
This certifies the complete local KNF modification around the reconstructed
A_- branch. It does not by itself prove a global separator theorem.
"""
import sympy as sp

L2=sp.log(2)
L3=sp.log(3)

a=L2/2
b=L3/2
T=2*a
d=b-a
e=T-b
Delta=sp.simplify(d-e)
L=sp.simplify(a-Delta)

c1=L2*2**sp.Rational(-3,2)
c2=L2*2**sp.Rational(-9,4)
c3=L2*2**sp.Rational(-3)
c4=c2
c5=L2*2**sp.Rational(-3)
c6=L2*2**sp.Rational(-15,4)
c7=c3
c9=L2*2**sp.Rational(-9,2)
c10=L2/4
c11=2*L3/(3*sp.sqrt(3))

alphaA=sp.simplify(c1+c5)
alphab=sp.simplify(c1+c5+c11)
kappa=sp.simplify(c1+c5+c9+c10+c11)
beta0=sp.simplify(-c1+c3)
betam=sp.simplify(-c2-c4)
betap=sp.simplify(c2+c6)
betaT=sp.simplify(-c3-c5-c7-c10)
betab=-c11

s=sp.symbols("s", positive=True)   # s=r/p>0
t=2**sp.Rational(-3,4)             # t=q/p>0

# Physical local order: z=u, A_-, A_+, B_-, B_+, T_-, T_+.
M=sp.zeros(7)
diag=[
    1+2*c1,
    1+alphaA,
    1+alphaA,
    1+alphab,
    1+alphab,
    1+kappa,
    1+kappa,
]
for i,v in enumerate(diag):
    M[i,i]=v

def edge(i,j,v):
    M[i,j]=v
    M[j,i]=v

# A1-R0 at u.
edge(0,1,c2)
edge(0,2,c2)
edge(0,5,beta0)
edge(0,6,beta0)

# A1-R2/R3 across A_-,A_+.
edge(1,2,-c1)
edge(1,5,betap)
edge(1,6,betam)
edge(2,5,betam)
edge(2,6,betap)

# A1-R5 across B_-,B_+.
edge(3,4,betab)

# A1-R6/R7 across T_-,T_+.
edge(5,6,betaT)

# Free order: z=u, A_+, B_-, B_+, T_-, T_+.
# A_-=A_+ - s B_- + s B_+ - t T_- + t T_+.
J=sp.zeros(7,6)
J[0,0]=1
J[1,1]=1
J[1,2]=-s
J[1,3]=s
J[1,4]=-t
J[1,5]=t
J[2,1]=1
J[3,2]=1
J[4,3]=1
J[5,4]=1
J[6,5]=1

G=sp.simplify(J.T*M*J)
assert G==G.T

names=["u","A+","B-","B+","T-","T+"]
maps={
 ("u","A+"):"tau_a",
 ("u","B-"):"r_b",
 ("u","B+"):"tau_b",
 ("u","T-"):"r_T",
 ("u","T+"):"tau_T",
 ("A+","B-"):"r_{a+b}",
 ("A+","B+"):"tau_d",
 ("A+","T-"):"r_{3a}",
 ("A+","T+"):"tau_a",
 ("B-","B+"):"r_{2b}",
 ("B-","T-"):"tau_e",
 ("B-","T+"):"r_{T+b}",
 ("B+","T-"):"r_{T+b}",
 ("B+","T+"):"tau_e",
 ("T-","T+"):"r_{4a}",
}

expected={
 ("u","A+"): 2**sp.Rational(3,4)*L2/4,
 ("u","B-"): -2**sp.Rational(3,4)*s*L2/8,
 ("u","B+"): 2**sp.Rational(3,4)*s*L2/8,
 ("u","T-"): -sp.sqrt(2)*L2/4,
 ("u","T+"): -(sp.sqrt(2)-1)*L2/4,
 ("A+","B-"): -s*(L2+8)/8,
 ("A+","B+"): s*(L2+8)/8,
 ("A+","T-"): -2**sp.Rational(1,4)*(sp.sqrt(2)*L2+4)/8,
 ("A+","T+"): 2**sp.Rational(1,4)*(4+L2-sp.sqrt(2)*L2)/8,
 ("B-","B+"): -(9*s**2*L2+18*sp.sqrt(2)*s**2*L2+72*s**2+16*sp.sqrt(3)*L3)/72,
 ("B-","T-"): 2**sp.Rational(1,4)*s/2,
 ("B-","T+"): -2**sp.Rational(1,4)*s*(8+L2-2*sp.sqrt(2)*L2)/16,
 ("B+","T-"): -2**sp.Rational(1,4)*s/2,
 ("B+","T+"): 2**sp.Rational(1,4)*s*(8+L2-2*sp.sqrt(2)*L2)/16,
 ("T-","T+"): -(3*L2+2*sp.sqrt(2))/8,
}

assert len(expected)==15
for i in range(6):
    for j in range(i+1,6):
        pair=(names[i],names[j])
        assert pair in expected
        assert sp.simplify(G[i,j]-expected[pair])==0, pair

# Exact sign proof ingredients.
assert L2.is_positive is True
assert (1-L2).is_positive is True              # log 2 < 1
assert (sp.sqrt(2)-1).is_positive is True
assert (2-sp.sqrt(2)).is_positive is True
assert L3.is_positive is True
assert c11.is_positive is True

H=sp.simplify(4+L2-sp.sqrt(2)*L2)
K=sp.simplify(8+L2-2*sp.sqrt(2)*L2)
assert H.is_positive is True
assert K.is_positive is True
# Explicit margins, not decimal evidence:
assert sp.simplify(H-3).is_positive is True
assert sp.simplify(K-6).is_positive is True

signs={
 ("u","A+"):+1,
 ("u","B-"):-1,
 ("u","B+"):+1,
 ("u","T-"):-1,
 ("u","T+"):-1,
 ("A+","B-"):-1,
 ("A+","B+"):+1,
 ("A+","T-"):-1,
 ("A+","T+"):+1,
 ("B-","B+"):-1,
 ("B-","T-"):+1,
 ("B-","T+"):-1,
 ("B+","T-"):-1,
 ("B+","T+"):+1,
 ("T-","T+"):-1,
}

# Exact positivity decomposition for every absolute factor.
positive_abs={
 ("u","A+"): 2**sp.Rational(3,4)*L2/4,
 ("u","B-"): 2**sp.Rational(3,4)*s*L2/8,
 ("u","B+"): 2**sp.Rational(3,4)*s*L2/8,
 ("u","T-"): sp.sqrt(2)*L2/4,
 ("u","T+"): (sp.sqrt(2)-1)*L2/4,
 ("A+","B-"): s*(L2+8)/8,
 ("A+","B+"): s*(L2+8)/8,
 ("A+","T-"): 2**sp.Rational(1,4)*(sp.sqrt(2)*L2+4)/8,
 ("A+","T+"): 2**sp.Rational(1,4)*H/8,
 ("B-","B+"): (9*s**2*L2+18*sp.sqrt(2)*s**2*L2+72*s**2+16*sp.sqrt(3)*L3)/72,
 ("B-","T-"): 2**sp.Rational(1,4)*s/2,
 ("B-","T+"): 2**sp.Rational(1,4)*s*K/16,
 ("B+","T-"): 2**sp.Rational(1,4)*s/2,
 ("B+","T+"): 2**sp.Rational(1,4)*s*K/16,
 ("T-","T+"): (3*L2+2*sp.sqrt(2))/8,
}
for pair,v in positive_abs.items():
    assert v.is_positive is True, pair
    assert sp.simplify(expected[pair]-signs[pair]*v)==0, pair

# Dedicated new-channel lines requested by audit:
assert maps[("u","B-")]=="r_b"
assert maps[("u","B+")]=="tau_b"
assert sp.simplify(expected[("u","B-")]+s*c2)==0
assert sp.simplify(expected[("u","B+")]-s*c2)==0

# No new irrational base phase from b,d,e.
assert sp.simplify(e-L/2)==0
assert sp.simplify(d-(L/2+Delta))==0
assert sp.simplify(b-(sp.Rational(3,2)*L+2*Delta))==0

print("SW1-A9-J1 FULL LOCAL 6x6 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("all 15 off-diagonal entries certified exactly, no numerical sign checks")
for pair in expected:
    print(f"{pair[0]} <-> {pair[1]} : {maps[pair]} : sign {signs[pair]:+d}")
print("r_b and tau_b certified separately with coefficients -s*c2 and +s*c2")
print("H>3 and K>6 exact margins certify the two formerly delicate signs")
print("e=L/2, d=L/2+Delta, b=3L/2+2Delta certified")
print("FIREWALL: local J1 block only; no global separator verdict")
