"""Exact symbolic identity and noncommuting rational controls (stdlib only)."""
from fractions import Fraction as F
from pathlib import Path
from verify_schur_defect import checked_archive, ARCHIVE


# Sparse polynomials in six formal variables a,b,c,p,q,r over Q.
def add(x,y):
    z = dict(x)
    for k,v in y.items():
        z[k] = z.get(k,F(0))+v
    return {k:v for k,v in z.items() if v}
def scale(x,t): return {k:v*t for k,v in x.items() if v*t}
def sub(x,y): return add(x,scale(y,-1))
def mul(x,y):
    z = {}
    for k,v in x.items():
        for l,w in y.items():
            m = tuple(a+b for a,b in zip(k,l))
            z[m] = z.get(m,F(0))+v*w
    return {k:v for k,v in z.items() if v}
def sq(x): return mul(x,x)


def determinant(x): return x[0][0]*x[1][1]-x[0][1]*x[1][0]
def mm(x,y): return [[sum(a*b for a,b in zip(row,col)) for col in zip(*y)] for row in x]
def plus(x,y): return [[a+b for a,b in zip(row,col)] for row,col in zip(x,y)]
def times(x,t): return [[a*t for a in row] for row in x]
def inverse(x):
    d = determinant(x)
    return times([[x[1][1],-x[0][1]],[-x[1][0],x[0][0]]],1/d)
def mat(x): return [list(map(F,row)) for row in x]
def positive(x): return x[0][0]>0 and determinant(x)>0
def defects(m,w):
    a,b,c=m[0][0],m[0][1],m[1][1]
    p,q,r=w[0][0],w[0][1],w[1][1]
    return a*q-b*p,a*r-c*p


def main():
    a,b,c,p,q,r = [{tuple(int(i==j) for j in range(6)):F(1)} for i in range(6)]
    d=sub(mul(a,c),sq(b)); f1=sub(mul(a,q),mul(b,p)); f2=sub(mul(a,r),mul(c,p))
    coeff=sub(add(mul(p,c),mul(r,a)),scale(mul(q,b),2))
    delta=sub(sq(coeff),scale(mul(d,sub(mul(p,r),sq(q))),4))
    psi=add(sq(add(scale(mul(a,f2),-1),scale(mul(b,f1),2))),scale(mul(d,sq(f1)),4))
    assert mul(sq(a),delta)==psi

    l=mat([[3,1],[1,2]]); g=mat([[2,F(1,3)],[F(1,3),1]])
    w=mat([[2,F(1,2)],[F(1,2),3]])
    assert all(positive(x) for x in [l,g,w]) and mm(l,g)!=mm(g,l)
    h=mm(mm(g,inverse(l)),g); z=plus(h,w); b0=plus(l,times(g,17))
    m=mm(mm(b0,inverse(l)),b0); rr=plus(plus(l,times(g,34)),times(z,289))
    assert rr==plus(m,times(w,289))
    f1,f2=defects(m,w); assert (f1,f2)!=(0,0)
    gamma=F(7,13); assert defects(m,times(m,gamma))==(0,0)
    # F1=0 alone is not a double-root test, even for SPD data.
    m=mat([[2,0],[0,3]]); w=mat([[1,0],[0,4]])
    assert defects(m,w)==(0,5)
    assert (w[1][1]/m[1][1]-w[0][0]/m[0][0])**2==F(25,36)

    raw=(Path(__file__).resolve().parent/'inputs'/ARCHIVE).read_bytes()
    checked_archive(raw)
    try: checked_archive(raw+b' ')
    except AssertionError as exc: assert 'hash mismatch' in str(exc)
    else: raise AssertionError('tampered archive accepted')
    print('Exact polynomial identity, noncommuting Schur algebra, proportional zero, F1-only control, archive tampering rejection: PASS')


if __name__=='__main__': main()
