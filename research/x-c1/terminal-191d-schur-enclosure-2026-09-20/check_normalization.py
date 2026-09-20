"""Independent elementary identities for terminal matrix normalization."""
import sys
from pathlib import Path
import generate_terminal_matrices as t
from flint import arb,fmpq,fmpq_poly,arb_poly,ctx
from math import factorial
ctx.prec=512
checks=[]
def check(label,truth):
    if not truth:raise RuntimeError(label)
    checks.append(label)
polys=t.leg_polynomials(12);log2=arb(2).log()
harm=[arb(0)]
for k in range(1,26):harm.append(harm[-1]+arb(1)/k)
lm=[];odd=arb(0)
for r in range(13):
    odd+=arb(1)/(2*r+1);lm.append((odd-log2)/(2*r+1))
for i in range(9):
    for j in range(i,9):
        if (i+j)%2:continue
        product=polys[i]*polys[j]
        direct=sum((arb(product[k])*lm[k//2] for k in range(0,i+j+1,2)),arb(0))
        formula=(arb(1)/(2*i+1)+2*(harm[2*i]-harm[i])-log2)/(2*i+1) if i==j else arb(1)/((j-i)*(i+j+1))
        check('V moment '+str((i,j)),direct.overlaps(formula))
nodes=[arb.legendre_p_root(16,k,weight=True) for k in range(16)]
check('Gauss weights positive',all(w>0 for _,w in nodes))
check('Gauss roots strictly interior',all(x>-1 and x<1 for x,_ in nodes))
check('Gauss rule includes total length',sum((w for _,w in nodes),arb(0)).contains(2))
def tpoly(i,j):
    out=[fmpq(0)]*(i+j+2)
    for k in range(i+1):
        ai=fmpq((-1)**(i+k)*factorial(i+k),2**k*factorial(k)**2*factorial(i-k))
        for l in range(j+1):
            aj=fmpq((-1)**(j+l)*factorial(j+l),2**l*factorial(l)**2*factorial(j-l))
            out[k+l+1]+=(-1)**j*ai*aj*fmpq(factorial(k)*factorial(l),factorial(k+l+1))
    return arb_poly(out)
for q in (2,3,4,5,7):
    d=arb(q).log();length=2-d
    for i,j in [(0,0),(0,2),(1,1),(1,5),(4,6),(7,9)]:
        direct=tpoly(i,j)(length)
        rule=sum((w*arb_poly(polys[i])(-1+length*(x+1)/2)*arb_poly(polys[j])(-1+length*(x+1)/2+d)*length/2 for x,w in nodes),arb(0))
        check('Prime normalization '+str((q,i,j)),direct.overlaps(rule))
pg,eps=t.gamma_polynomial(32)
columns=t.gamma_columns(10,32,pg)
# Integrate correlation against the Gamma polynomial directly in monomials.
kernel=arb_poly([arb(pg[k])/2**k for k in range(33)])
for i,j in [(0,0),(0,2),(1,1),(1,5),(4,6),(7,9)]:
    corr=tpoly(i,j)(arb_poly([2,-1]))
    integrand=kernel*corr
    direct=2*sum((integrand[k]*2**k/(k+1) for k in range(len(integrand))),arb(0))
    entry=arb(columns[i].get(j,fmpq(0)))/(2*j+1)
    check('Gamma normalization '+str((i,j)),direct.overlaps(entry))
for k,label in enumerate(checks,1):print('PASS',k,label)
print('TOTAL',len(checks),'normalization checks PASS')
