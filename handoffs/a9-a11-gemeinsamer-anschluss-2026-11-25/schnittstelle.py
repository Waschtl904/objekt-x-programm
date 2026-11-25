"""Directed physical U11 energy for sources supplied with certified L2 errors.

The inputs are orthonormal physical coordinates. The moment constraints on the
exact sources are part of the caller's source contract. The two error radii
cover the entire omitted Hilbert vectors, including tails, in this metric.
"""
from fractions import Fraction as Q
from math import isqrt


def sqrt_upper(x, digits=65):
    x=Q(x)
    scale=10**digits
    root=isqrt((x.numerator*scale**2)//x.denominator)
    return Q(root if root**2*x.denominator==x.numerator*scale**2 else root+1,scale)


def mutual_energy(left, right, error_left=0, error_right=0):
    """Enclose the real mutual energy; for complex sources apply to real/imaginary parts."""
    a=list(map(Q,left))
    b=list(map(Q,right))
    ea,eb=Q(error_left),Q(error_right)
    if ea<0 or eb<0:
        raise ValueError("Negative L2 error")
    norm_a=sqrt_upper(sum(x*x for x in a))
    norm_b=sqrt_upper(sum(x*x for x in b))
    pairing=sum(x*y for x,y in zip(a,b))
    loss=ea*norm_b+eb*norm_a+ea*eb
    return 10**44*(pairing-loss),10**44*(pairing+loss)


def regression():
    # The last coordinate of the first approximation is absent from the second.
    a=[Q(2,3),Q(-1,5),Q(1,7)]
    b=[Q(-1,3),Q(1,11)]
    da,db=Q(2,17),Q(1,13)
    lo,hi=mutual_energy(a,b,da,db)
    assert lo<=10**44*(a[0]*(b[0]-db)+(a[1]+da)*b[1])<=hi
    assert mutual_energy([1],[1])==(10**44,10**44)
    assert mutual_energy([],[],0,0)==(0,0)


if __name__=="__main__":
    regression()
    print("Physical energy and error transport OK")
