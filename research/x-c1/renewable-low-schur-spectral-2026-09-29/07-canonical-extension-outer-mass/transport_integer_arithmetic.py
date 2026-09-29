"""Outward integer intervals on the grid 10^-200; standard library only."""
from fractions import Fraction as Q

SCALE=10**200
ZERO=(0,0)
ONE=(SCALE,SCALE)
def ceildiv(a,b):return -((-a)//b)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    v=[x*y for x in a for y in b]
    return min(v)//SCALE,ceildiv(max(v),SCALE)
def div(a,b):
    assert b[0]*b[1]>0
    return min(x*SCALE//y for x in a for y in b),max(ceildiv(x*SCALE,y) for x in a for y in b)
def isum(values):
    out=ZERO
    for v in values:out=add(out,v)
    return out
def irat(value):
    x=Q(value)*SCALE
    return x.numerator//x.denominator,ceildiv(x.numerator,x.denominator)
def decode(pair):
    lo,hi=map(int,pair);assert lo<=hi
    return lo*10**100,hi*10**100
def positive_pivots(a):
    n=len(a);L=[[ZERO]*n for _ in range(n)];d=[]
    for i in range(n):
        pivot=sub(a[i][i],isum(mul(mul(L[i][k],L[i][k]),d[k]) for k in range(i)))
        assert pivot[0]>0,(i,'uncertified pivot')
        d.append(pivot);L[i][i]=ONE
        for j in range(i+1,n):
            L[j][i]=div(sub(a[j][i],isum(mul(mul(L[j][k],L[i][k]),d[k]) for k in range(i))),pivot)
    return [str(Q(x[0],SCALE)) for x in d]
