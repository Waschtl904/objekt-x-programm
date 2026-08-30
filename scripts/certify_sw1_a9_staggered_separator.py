#!/usr/bin/env python3
"""SW1-A9 staggered KNF separator certificate.

Normalized by Delta=1. Let
    g = s_*/Delta = L/(2 Delta) - 2,
so the exact fixed inequalities 0<g<1/2 follow from
L-4Delta>0 and 5Delta-L>0.

For epsilon/Delta < (1-g)/2, choose a phase
    epsilon < s < 1-epsilon-g.
Then parity 0 has the A8 separator at index n, while parity 1 has the
staggered A8 separator at index n-2, with phase s+g.

This certificate proves:
- the complete new-edge cross ledger has 128 directed formal candidates,
  not the exploratory count 84;
- these represent 95 generic undirected edge classes (33 reciprocal duplicates);
- all 128 directed candidates are inactive on the whole staggered phase domain;
- opposite-side physical label collisions form only a finite exceptional
  phase set, so a nonempty open quotient-regular separator set remains.

Together with the already-certified A8 blocking of all parity-preserving A7
edges, this gives a genuine staggered separator for the full KNF Gram graph.

Firewall: lower chamber and epsilon<(6Delta-L)/4 only. No statement for the
complementary lower chamber, upper chamber, Schur injectivity, HT-RED,
Objekt X, or RH.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter, defaultdict

def V(c=0,g=0,eps=0,R=0,s=0):
    return tuple(F(x) for x in (c,g,eps,R,s))
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def mul(q,x):
    q=F(q); return tuple(q*a for a in x)
ZERO=V(); ONE=V(c=1); G=V(g=1); EPS=V(eps=1); RR=V(R=1); SS=V(s=1)

L=add(V(c=4),mul(2,G))
a=add(L,ONE)
b=add(mul(F(3,2),L),V(c=2))
T=add(mul(2,L),V(c=2))
e=mul(F(1,2),L)
d=add(e,ONE)

states={
 0:[("P",0),("P",1),("P",2),("Q",0),("Q",1)],
 1:[("P",0),("P",1),("P",2),("Q",0),("Q",1)],
 2:[("P",0),("P",1),("Q",0),("Q",1),("Q",2)],
 3:[("P",0),("P",1),("Q",0),("Q",1),("Q",2)],
}
left={
 0:{("P",1),("P",2),("Q",0),("Q",1)},
 1:{("P",2),("Q",0),("Q",1)},
 2:{("Q",0),("Q",1)},
 3:{("Q",0)},
}
right={
 0:{("P",0)},
 1:{("P",0),("P",1)},
 2:{("P",0),("P",1),("Q",2)},
 3:{("P",0),("P",1),("Q",1),("Q",2)},
}

def n0(eta): return 0 if eta==0 else -2
def side(m,eta,sheet,k):
    j=m-n0(eta)
    if j<=-1: return "L"
    if j>=4: return "R"
    pair=(sheet,k)
    if pair in left[j]: return "L"
    if pair in right[j]: return "R"
    return None

def base(eta): return SS if eta==0 else add(SS,G)
def residue(m,eta,sheet):
    j=m-n0(eta)
    if sheet=="P":
        return add(base(eta),V(c=j))
    return sub(V(c=4-j),base(eta))
def physical(m,eta,sheet,k):
    return add(residue(m,eta,sheet),mul(k,L))

middle=[]
for eta in (0,1):
    for j in range(4):
        m=n0(eta)+j
        for sheet,k in states[j]:
            middle.append((eta,m,j,sheet,k,physical(m,eta,sheet,k),side(m,eta,sheet,k)))
assert len(middle)==40

trans={
 "+e":{"P":("P",0),"Q":("Q",0)},
 "-e":{"P":("P",0),"Q":("Q",0)},
 "+d":{"P":("P",1),"Q":("Q",-1)},
 "-d":{"P":("P",-1),"Q":("Q",1)},
 "+b":{"P":("P",2),"Q":("Q",-2)},
 "-b":{"P":("P",-2),"Q":("Q",2)},
 "r_ab":{"P":("Q",1),"Q":("P",-1)},
 "r_Tb":{"P":("Q",0),"Q":("P",0)},
 "r_b":{"P":("Q",2),"Q":("P",-2)},
}
assert len(trans)==9
assert max(abs(j) for M in trans.values() for _,j in M.values())==2

def amap(name,x):
    if name=="+e": return add(x,e)
    if name=="-e": return sub(x,e)
    if name=="+d": return add(x,d)
    if name=="-d": return sub(x,d)
    if name=="+b": return add(x,b)
    if name=="-b": return sub(x,b)
    if name=="r_ab": return sub(add(a,b),x)
    if name=="r_Tb": return sub(add(T,b),x)
    if name=="r_b": return sub(b,x)
    raise KeyError(name)

cross=[]
unmatched=[]
filter_counts=Counter()
for eta,m,j,sheet,k,x,src_side in middle:
    for name in trans:
        filter_counts["raw"]+=1
        target_sheet,jump=trans[name][sheet]
        mm=m+jump
        eta2=1-eta
        y=amap(name,x)
        jj=mm-n0(eta2)
        if jj<=-1 or jj>=4:
            filter_counts["target_outside_middle"]+=1
            tgt_side="L" if jj<=-1 else "R"
            if tgt_side!=src_side:
                filter_counts["outside_cross"]+=1
                cross.append((eta,m,j,sheet,k,name,eta2,mm,target_sheet,None,x,y,src_side,tgt_side))
            else:
                filter_counts["outside_same_side"]+=1
        else:
            filter_counts["target_middle_index"]+=1
            matches=[]
            for sh2,k2 in states[jj]:
                if sh2==target_sheet and physical(mm,eta2,sh2,k2)==y:
                    matches.append((sh2,k2))
            if len(matches)==1:
                filter_counts["matched_middle"]+=1
                tgt_side=side(mm,eta2,*matches[0])
                if tgt_side!=src_side:
                    filter_counts["middle_cross"]+=1
                    cross.append((eta,m,j,sheet,k,name,eta2,mm,target_sheet,matches[0][1],x,y,src_side,tgt_side))
                else:
                    filter_counts["middle_same_side"]+=1
            elif len(matches)==0:
                filter_counts["unmatched_middle"]+=1
                unmatched.append((eta,m,j,sheet,k,name,eta2,mm,target_sheet,x,y))
            else:
                raise AssertionError(("multiple target labels",matches))

assert filter_counts==Counter({
    "raw":360,
    "target_outside_middle":180,
    "target_middle_index":180,
    "outside_same_side":118,
    "outside_cross":62,
    "matched_middle":102,
    "unmatched_middle":78,
    "middle_same_side":36,
    "middle_cross":66,
})
assert len(cross)==filter_counts["outside_cross"]+filter_counts["middle_cross"]==128
assert Counter(c[0] for c in cross)==Counter({0:64,1:64})

def affine_key(x):
    assert x[2]==0 and x[3]==0
    return (x[0],x[1],x[4])
classes=defaultdict(list)
for c in cross:
    kx,ky=affine_key(c[10]),affine_key(c[11])
    key=tuple(sorted((kx,ky)))
    classes[key].append(c)
assert len(classes)==95
assert Counter(len(v) for v in classes.values())==Counter({1:62,2:33})

domains={
 "+e":[(sub(b,RR),b),(b,add(b,RR))],
 "-e":[(sub(T,RR),T),(T,add(T,RR))],
 "+d":[(a,add(a,RR))],
 "-d":[(b,add(b,RR))],
 "+b":[(ZERO,RR)],
 "-b":[(b,add(b,RR))],
 "r_ab":[(a,add(a,RR)),(sub(b,RR),b)],
 "r_Tb":[(sub(b,RR),b),(b,add(b,RR)),(sub(T,RR),T),(T,add(T,RR))],
 "r_b":[(ZERO,RR),(sub(b,RR),b)],
}

sample=(F(1),F(2,5),F(1,10),F(1,20),F(1,5))
def value(x): return sum(a*v for a,v in zip(x,sample))
def choose_margin(x,lo,hi):
    xv,lv,hv=value(x),value(lo),value(hi)
    if xv<=lv: return sub(lo,x)
    if xv>=hv: return sub(x,hi)
    raise AssertionError(("sample unexpectedly inside new KNF domain",x,lo,hi))

slacks=[
 G,
 sub(V(c=F(1,2)),G),
 RR,
 sub(EPS,RR),
 sub(SS,EPS),
 sub(sub(sub(ONE,EPS),G),SS),
]

def positive_decomposition(m):
    C,cg,ce,cR,cs=m
    for n in range(0,101):
        t=F(n,2)
        c5=t
        c1=2*(C-t)
        c4=cs+t
        c3=ce+cs+2*t
        c2=cR+c3
        c0=cg+2*C-t
        coeff=[c0,c1,c2,c3,c4,c5]
        if all(q>=0 for q in coeff) and any(q>0 for q in coeff):
            rec=ZERO
            for q,sl in zip(coeff,slacks):
                rec=add(rec,mul(q,sl))
            if rec==m:
                return coeff
    raise AssertionError(("no exact positive-slack decomposition",m))

margins=[]
for c in cross:
    x=c[10]
    for lo,hi in domains[c[5]]:
        margin=choose_margin(x,lo,hi)
        positive_decomposition(margin)
        margins.append(margin)
assert len(margins)==218
assert len(set(margins))==42

bad_phase_forms=set()
for i,j in combinations(range(len(middle)),2):
    A=middle[i]; B=middle[j]
    if A[6]==B[6]:
        continue
    diff=sub(A[5],B[5])
    assert diff[2]==0 and diff[3]==0
    C,cg,_,_,cs=diff
    if cs==0:
        assert not (C==0 and cg==0)
        continue
    bad_phase_forms.add((-C/cs,-cg/cs))
assert len(bad_phase_forms)==53

print("SW1-A9 STAGGERED KNF SEPARATOR CERTIFICATE: PASS")
print("exact arithmetic: Python fractions.Fraction")
print("two A8 middle blocks: 20+20 = 40 formal labels")
print("new KNF directed map list: 9; new-map range <=2")
print("filter ledger: 360 raw = 180 outside-target + 180 middle-target")\nprint("outside-target: 62 cross + 118 same-side")\nprint("middle-target: 102 matched = 66 cross + 36 same-side; 78 unmatched")\nprint("complete side-cross ledger: 62+66 = 128 directed candidates (NOT 84)")
print("generic undirected classes: 95 = 62 single + 33 reciprocal-double")
print("218 exact interval-exclusion inequalities; 42 distinct margins")
print("all margins have exact nonnegative positive-slack decompositions")
print("active new KNF cross edges on staggered phase domain: 0")
print("opposite-side physical collisions: finite exceptional set <=53 affine phase forms")
print("quotient-regular open separator phases therefore remain")
print("threshold: epsilon/Delta < (1-g)/2 = (6Delta-L)/(4Delta)")
print("with A8 old-edge blocking: full KNF staggered separator certified")
print("FIREWALL: small-epsilon lower subchamber only; no Schur/HT/Objekt-X/RH claim")
