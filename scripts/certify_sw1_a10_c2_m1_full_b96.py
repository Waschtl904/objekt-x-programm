#!/usr/bin/env python3
"""SW1-A10-C2-M1-FULL exhaustive B96-atom evaluation certificate.

Reference ratio r0=7/2. Uses the 64 exact chamber representatives and the
corrected 96-wall operator alphabet. For every open circle atom and every
physical output cover slot it compares:
  (a) direct physical FREE/HUB contributions, and
  (b) evaluated M1 raw-ledger contributions.
Comparison is as exact symbolic multisets, not only summed coefficients.

Scope: exact reference-arrangement atom evaluation and matrix-vs-physical
identity; actual project-r transfer remains separate (C1B2A isotopy gate).
No injectivity claim.
"""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
import hashlib

r0=F(7,2)
D=1+2*r0
L=4+10*r0
Emax=(r0+1)/2
assert (D,L,Emax)==(F(8),F(39),F(9,4))

REPS=[
('------------------',('1/7','2/7','3/7')),
('------------+-----',('1/7','2/7','4/7')),
('------------+---+-',('1/7','3/7','5/7')),
('------------+---++',('1/7','4/7','5/7')),
('-----------++---+-',('2/7','3/7','6/7')),
('-----------++---++',('2/7','4/7','6/7')),
('-----------++--+++',('3/7','5/7','6/7')),
('----------+++---+-',('2/7','3/7','8/7')),
('----------+++---++',('2/7','4/7','8/7')),
('----------+++--+++',('2/5','4/5','6/5')),
('----------+++-++++',('3/7','8/7','9/7')),
('---------++++---+-',('1/7','3/7','9/7')),
('---------++++---++',('1/5','3/5','7/5')),
('---------++++--+++',('2/5','4/5','8/5')),
('---------++++-++++',('2/5','6/5','33/20')),
('---------+++++++++',('3/14','10/7','23/14')),
('--------+--++--+++',('4/7','5/7','6/7')),
('--------+-+++--+++',('3/5','4/5','6/5')),
('--------+-+++-++++',('3/4','5/4','3/2')),
('--------+++++--+++',('9/16','13/16','27/16')),
('--------+++++-++++',('9/16','9/8','27/16')),
('--------++++++++++',('13/24','13/8','41/24')),
('-------++-+++-++++',('17/14','10/7','23/14')),
('------+--++++---+-',('1/5','2/5','33/20')),
('------+--++++---++',('1/8','9/16','27/16')),
('------+--++++--+++',('11/24','5/8','41/24')),
('------+-+++++--+++',('13/24','5/8','41/24')),
('---+-----++++---++',('1/14','6/7','25/14')),
('---+-----++++--+++',('9/20','9/10','9/5')),
('---+-----++++-++++',('2/5','6/5','37/20')),
('---+-----+++++++++',('3/14','10/7','13/7')),
('---+----+-+++--+++',('6/7','13/14','25/14')),
('---+----+-+++-++++',('9/10','11/10','9/5')),
('---+----+++++--+++',('11/20','9/10','9/5')),
('---+----+++++-++++',('9/14','9/7','27/14')),
('---+----++++++++++',('13/24','13/8','43/24')),
('---+---++-+++-++++',('17/14','10/7','13/7')),
('---+---++++++-++++',('13/12','5/4','13/6')),
('---+--+--++++---+-',('1/5','2/5','37/20')),
('---+--+--++++---++',('1/5','3/5','37/20')),
('---+--+--++++--+++',('2/5','4/5','2/1')),
('---+--+--++++-++++',('11/24','13/12','13/6')),
('---+--+--+++++++++',('1/16','9/8','35/16')),
('---+--+-+++++--+++',('3/5','4/5','41/20')),
('---+--+-+++++-++++',('11/12','13/12','13/6')),
('---+--+++++++-++++',('17/16','9/8','35/16')),
('-+-+-----++++-++++',('13/28','39/28','61/28')),
('-+-+-----+++++++++',('2/5','33/20','41/20')),
('-+-+----+-+++-++++',('13/14','12/7','13/7')),
('-+-+----+++++-++++',('13/16','13/8','33/16')),
('-+-+----++++++++++',('9/16','27/16','17/8')),
('-+-+---++-+++-++++',('5/4','33/20','41/20')),
('-+-+---++++++-++++',('13/12','17/12','13/6')),
('-+-++--++-+++-++++',('43/28','47/28','59/28')),
('++-+-----+++++++++',('2/5','37/20','41/20')),
('++-+----+-+++-++++',('13/14','25/14','13/7')),
('++-+----+++++-++++',('9/10','9/5','2/1')),
('++-+----++++++++++',('3/5','37/20','41/20')),
('++-+---++-+++-++++',('5/4','37/20','41/20')),
('++-+---++++++-++++',('13/12','43/24','13/6')),
('++-+---+++++++++++',('17/16','17/8','35/16')),
('++-++--++-+++-++++',('43/28','51/28','59/28')),
('+++++--++-+++-++++',('47/28','55/28','59/28')),
('++++++-++-+++-++++',('51/28','55/28','59/28')),
]
assert len(REPS)==64
reps=[tuple(F(v) for v in vals) for _,vals in REPS]
assert all(F(0)<s<R<eps<Emax for s,R,eps in reps)

G=[
    ("P0",+1,0,0),
    ("P1",+1,1,0),
    ("Q0",-1,0,4),
    ("Q1",-1,1,4),
]
gidx={g[0]:i for i,g in enumerate(G)}
gdict={g[0]:g for g in G}

FREE=[
    ("I",+1,F(0),0),
    ("r_a",-1,F(1),1),
    ("tau_+a",+1,F(1),1),
    ("r_T",-1,F(2),2),
    ("tau_+T",+1,F(2),2),
    ("r_3a",-1,F(3),3),
    ("tau_-a",+1,F(-1),-1),
    ("r_2b",-1,F(3),4),
    ("r_2T",-1,F(4),4),
    ("tau_-T",+1,F(-2),-2),
]
Fdict={x[0]:x for x in FREE}

ROWS={
"R0":("BOTH","0<x<eps",[("I","1+2c1"),("r_a","c2"),("tau_+a","c2"),("r_T","beta0"),("tau_+T","beta0")]),
"R1":("BOTH","eps<x<a-eps",[("I","1+c1"),("r_T","-c1"),("tau_+a","c2")]),
"R2":("BOTH","a-eps<x<a",[("I","1+alphaA"),("r_T","-c1"),("r_3a","betam"),("tau_+a","betap"),("r_a","c2")]),
"R3":("BOTH","a<x<min(a+eps,2d-eps)",[("I","1+alphaA"),("r_T","-c1"),("r_3a","betam"),("tau_+a","betap"),("tau_-a","c2")]),
"R4I":("I","a+eps<x<2d-eps",[("I","1+alphaA"),("r_T","-c1"),("r_3a","betam"),("tau_-a","c2")]),
"R4II":("II","2d-eps<x<a+eps",[("I","1+alphab"),("r_T","-c1"),("r_3a","betam"),("tau_+a","betap"),("tau_-a","c2"),("r_2b","betab")]),
"R5":("BOTH","max(a+eps,2d-eps)<x<T-eps",[("I","1+alphab"),("r_T","-c1"),("r_3a","betam"),("tau_-a","c2"),("r_2b","betab")]),
"R6":("BOTH","T-eps<x<T",[("I","1+kappa"),("r_T","beta0"),("r_3a","betam"),("r_2T","betaT"),("tau_-a","betap"),("r_2b","betab")]),
"R7":("BOTH","T<x<T+eps",[("I","1+kappa"),("tau_-T","beta0"),("r_3a","betam"),("r_2T","betaT"),("tau_-a","betap"),("r_2b","betab")]),
}
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
    name,s,lam,k,coeff=ch
    lamsrc=-s*lam; ksrc=-s*k
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

def V(LL=0,DD=0,RR=0,EE=0,SS=0): return (F(LL),F(DD),F(RR),F(EE),F(SS))
def addv(x,y): return tuple(a+b for a,b in zip(x,y))
def subv(x,y): return tuple(a-b for a,b in zip(x,y))
def negv(x): return tuple(-a for a in x)
def modLsig(x):
    n=x[0].numerator//x[0].denominator
    return (x[0]-F(n),)+x[1:]

zero=V(); ee=V(F(1,2),0); dd=V(F(1,2),1); aa=V(1,1); bb=V(F(3,2),2); TT=V(2,2); twod=V(1,2)
Bf={zero,V(EE=1),subv(aa,V(EE=1)),addv(aa,V(EE=1)),subv(twod,V(EE=1)),subv(TT,V(EE=1)),V(SS=1),addv(ee,V(SS=1)),addv(aa,V(SS=1)),subv(aa,V(RR=1)),addv(aa,V(RR=1)),subv(bb,V(RR=1)),addv(bb,V(RR=1)),subv(TT,V(RR=1)),addv(TT,V(RR=1)),aa,bb,TT,addv(TT,V(EE=1))}
Bw={V(RR=1),V(EE=1),addv(ee,V(EE=1)),dd,addv(dd,V(RR=1)),aa,addv(aa,V(RR=1)),addv(aa,V(EE=1)),bb,subv(TT,V(RR=1)),TT,addv(TT,V(SS=1))}
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
        return ("T",lam,dk)
    return ("R",F(l+m,2),k+j)
master={rel(x,y) for cell in C for x,y in combinations(cell,2)}
def cv(lam,k): return V(lam,k)
Braw=set(Bf|Bw)
for typ,lam,k in master:
    cc0=cv(lam,k)
    if typ=="T":
        for dr in (-1,1):
            cc=tuple(dr*z for z in cc0)
            for wall in Bf: Braw.add(subv(wall,cc))
    else:
        for wall in Bf: Braw.add(subv(cc0,wall))
for orient,twolam,k in sig:
    cc=cv(F(twolam,2),k)
    for wall in Bf:
        z=subv(wall,cc)
        if orient==-1: z=negv(z)
        Braw.add(z)
B92={modLsig(x) for x in Braw}
assert len(B92)==92
NEW={V(DD=5),V(LL=F(1,2),DD=5),V(DD=6),V(LL=F(1,2),DD=6)}
B96=sorted(B92|NEW)
assert len(B96)==96

def bvalue(sig,rep):
    l,k,rho,mu,nu=sig
    sigma,R,eps=rep
    z=l*L+k*D+rho*R+mu*eps+nu*sigma
    n=z//L
    return z-n*L

def phi(gname,theta):
    _,s,eta,kappa=gdict[gname]
    return s*theta+F(eta,2)*L+kappa*D
def Nwrap(gname,theta):
    z=phi(gname,theta)
    return z//L
def rho(gname,theta):
    z=phi(gname,theta)
    return z-(z//L)*L

a=L+D
d=F(1,2)*L+D
b=F(3,2)*L+2*D
T=2*L+2*D
assert a==F(47) and d==F(55,2) and b==F(149,2) and T==F(94)

def active_rows(x,eps):
    ch="I" if 2*eps<D else "II"
    out=[]
    tests={
        "R0":0<x<eps,
        "R1":eps<x<a-eps,
        "R2":a-eps<x<a,
        "R3":a<x<min(a+eps,2*d-eps),
        "R4I":ch=="I" and a+eps<x<2*d-eps,
        "R4II":ch=="II" and 2*d-eps<x<a+eps,
        "R5":max(a+eps,2*d-eps)<x<T-eps,
        "R6":T-eps<x<T,
        "R7":T<x<T+eps,
    }
    return [name for name,v in tests.items() if v]

def hub_active(name,x,sigma,R,eps):
    T0=T+eps; S=T+sigma
    return {"A_L":0<x<a-R,"A_R":a+R<x<T0,"A_O":0<x<S-a,"B_L":0<x<b-R,"B_R":b+R<x<T0,"B_O":0<x<S-b,"T_L":0<x<T-R,"T_R":T+R<x<T0,"T_O":0<x<S-T}[name]

row_terms_by_name={r:ROWS[r][2] for r in ROWS}
state_hasher=hashlib.sha256()
nonzero_hist=Counter()
total_active=0
max_cell_mult=0
atom_count=0
unique_state_digests=set()

for ci,rep in enumerate(reps):
    sigma,R,eps=rep
    assert eps<Emax<D/2
    vals=[bvalue(sig,rep) for sig in B96]
    assert len(set(vals))==96
    vals=sorted(vals)
    thetas=[(vals[i]+vals[i+1])/2 for i in range(95)]
    thetas.append(((vals[-1]+vals[0]+L)/2)%L)
    assert len(thetas)==96

    for ai,theta in enumerate(thetas):
        atom_count+=1
        physical=[]
        ledger=[]
        for gout in G:
            goutn=gout[0]
            for lout in range(3):
                outidx=gidx[goutn]*3+lout
                xout=rho(goutn,theta)+lout*L
                T0=T+eps
                if not (0<xout<T0):
                    continue
                rows=active_rows(xout,eps)
                assert len(rows)==1
                row=rows[0]

                for affine,coeff in row_terms_by_name[row]:
                    _,s,lam,k=Fdict[affine]
                    xsrc=s*xout+lam*L+k*D
                    assert 0<xsrc<T0
                    gin,j,m,s2=free_sr[(affine,goutn)]
                    assert s2==s
                    rin=rho(gin,theta+j*D)
                    q=(xsrc-rin)/L
                    assert q.denominator==1
                    lin=int(q)
                    assert 0<=lin<3
                    inidx=gidx[gin]*3+lin
                    physical.append((j,outidx,inidx,"H",coeff,row,affine))

                for name,s,lam,k,coeff in HUB:
                    if not hub_active(name,xout,sigma,R,eps):
                        continue
                    t=s*xout-s*lam*L-s*k*D
                    assert R<t<T+sigma
                    gin,j,m,s2=hub_sr[(name,goutn)]
                    assert s2==s
                    rin=rho(gin,theta+j*D)
                    q=(t-rin)/L
                    assert q.denominator==1
                    lin=int(q)
                    assert 0<=lin<3
                    inidx=12+gidx[gin]*3+lin
                    physical.append((j,outidx,inidx,"W",coeff,name,name))

                for affine,coeff in row_terms_by_name[row]:
                    gin,j,m,s=free_sr[(affine,goutn)]
                    lin=s*(lout-Nwrap(goutn,theta))+Nwrap(gin,theta+j*D)-m
                    if 0<=lin<3:
                        xsrc=s*xout+Fdict[affine][2]*L+Fdict[affine][3]*D
                        assert xsrc==rho(gin,theta+j*D)+lin*L
                        inidx=gidx[gin]*3+lin
                        ledger.append((j,outidx,inidx,"H",coeff,row,affine))

                for name,s,lam,k,coeff in HUB:
                    if not hub_active(name,xout,sigma,R,eps):
                        continue
                    gin,j,m,s2=hub_sr[(name,goutn)]
                    assert s2==s
                    lin=s*(lout-Nwrap(goutn,theta))+Nwrap(gin,theta+j*D)-m
                    if 0<=lin<3:
                        t=s*xout-s*lam*L-s*k*D
                        assert t==rho(gin,theta+j*D)+lin*L
                        inidx=12+gidx[gin]*3+lin
                        ledger.append((j,outidx,inidx,"W",coeff,name,name))

        physical=sorted(physical,key=str)
        ledger=sorted(ledger,key=str)
        assert physical==ledger
        cells=Counter((z[0],z[1],z[2]) for z in ledger)
        if cells:
            mm=max(cells.values())
            max_cell_mult=max(max_cell_mult,mm)
            assert mm==1
        nz=len(cells)
        nonzero_hist[nz]+=1
        total_active+=len(ledger)
        payload=(str(ci)+"|"+str(ai)+"|"+str(theta)+"|"+repr(tuple(ledger))).encode()
        state_hasher.update(payload+b"\n")
        unique_state_digests.add(hashlib.sha256(repr(tuple(ledger)).encode()).hexdigest())

assert atom_count==64*96==6144
assert max_cell_mult==1
assert total_active==468081
assert nonzero_hist==Counter({69:878,76:1712,77:1529,78:1133,79:80,80:812})
assert len(unique_state_digests)==82
state_digest=state_hasher.hexdigest()
EXPECTED_STATE_DIGEST="de2ab5b32478509feb380804a20705fa5a63e16897e46b05f8d696343cea8a4b"
assert state_digest==EXPECTED_STATE_DIGEST

print("SW1-A10-C2-M1-FULL EXHAUSTIVE B96-ATOM MATRIX CERTIFICATE: PASS")
print("reference ratio r0=7/2; exact open atoms checked: 64*96=6144")
print("physical contribution multiset == evaluated M1 ledger on every atom/output slot")
print("all active sources have unique input lift in {0,1,2}")
print("pointwise active summands per (j,out,input) cell: max = 1")
print("total active matrix entries across all atoms:",total_active)
print("nonzero-cell histogram:",sorted(nonzero_hist.items()))
print("distinct evaluated matrix states:",len(unique_state_digests))
print("state ledger SHA256:",state_digest)
print("FIREWALL: reference-r M1-FULL only; actual-r isotopy transfer and injectivity remain separate")
