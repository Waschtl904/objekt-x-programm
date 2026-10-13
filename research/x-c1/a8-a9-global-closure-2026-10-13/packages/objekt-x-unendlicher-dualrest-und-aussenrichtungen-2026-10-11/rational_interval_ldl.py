"""Directed rational LDL primitives from the bound input auditor."""
from fractions import Fraction as F
SCALE=10**45

def ceildiv(a,b):return -((-a)//b)
def point(q):
    q=F(q);v=q.numerator*SCALE
    return (v//q.denominator,ceildiv(v,q.denominator))
def interval(v):return (point(v[0])[0],point(v[1])[1])
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    z=[a*b for a in x for b in y]
    return (min(z)//SCALE,ceildiv(max(z),SCALE))
def div(x,y):
    assert y[0]>0
    z=[(a*SCALE,b) for a in x for b in y]
    return (min(a//b for a,b in z),max(ceildiv(a,b) for a,b in z))
ZERO=(0,0);ONE=(SCALE,SCALE)

def positive(A):
    n=len(A);L=[[ZERO]*n for _ in range(n)];D=[]
    for j in range(n):
        d=A[j][j]
        for k in range(j):d=sub(d,mul(mul(L[j][k],D[k]),L[j][k]))
        assert d[0]>0,('unproved positive pivot',j,d)
        D.append(d);L[j][j]=ONE
        for i in range(j+1,n):
            q=A[i][j]
            for k in range(j):q=sub(q,mul(mul(L[i][k],D[k]),L[j][k]))
            L[i][j]=div(q,d)
    return {'positive_pivots':n,'smallest_pivot_lower':str(F(min(d[0] for d in D),SCALE))}

