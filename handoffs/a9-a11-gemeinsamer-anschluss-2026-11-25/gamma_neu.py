"""Rational degree-160 approximation on [0, 6/5], with a uniform error."""
from math import comb, factorial
from fractions import Fraction as F
from flint import fmpq, fmpq_poly
from functools import lru_cache

@lru_cache(None)
def coefficient_data(M=160):
    # Taylor coefficients of (sech(z) + csch(z) - 1/z)/4 at zero.
    J=640
    a=fmpq_poly([fmpq(1,factorial(k)) if not k%2 else 0 for k in range(J+2)])
    b=fmpq_poly([fmpq(1,factorial(k+1)) if not k%2 else 0 for k in range(J+2)])
    def reciprocal(v):
        coeff=[fmpq(0)]*(J+2)
        coeff[0]=1
        for k in range(2,J+2,2):
            coeff[k]=-sum((v[j]*coeff[k-j] for j in range(2,k+1,2)),fmpq(0))
        return coeff
    ac=reciprocal(a)
    bc=reciprocal(b)
    taylor=[(ac[k]+bc[k+1])/4 for k in range(J+1)]
    # On |z|=1.55 the distance from the cosh poles is >0.02.
    # |cosh(x+iy)|^2=sinh(x)^2+cos(y)^2>=cos(1.55)^2>0.02^2.
    # |sinh(z)|>0.3 there (split |Re z| >= 0.3 and its complement).
    # Cauchy's bound 16 is enough for the combined analytic kernel.
    ratio=fmpq(24,31)
    tail=16*ratio**(J+1)/(1-ratio)
    # Round individual shifted Chebyshev contributions to denominator 10^162.
    # This prevents denominators of the reciprocal series from accumulating.
    scale=10**162
    numerators=[0]*(M+1)
    round_loss=fmpq((M+1)*(J+1),scale)
    factor=fmpq(1)
    weights=[]
    for k,c in enumerate(taylor):
        v=c*factor
        for j in range(min(M,k)+1):
            term=v*((1 if j==0 else 2)*comb(2*k,k-j))*scale
            numerators[j]+=int(term.floor())
        if k>M:
            # Bound all coefficients above M, retaining their binomial decay.
            # Consecutive binomial terms have ratio <= (k-M-1)/(k+M+2).
            first=2*abs(v)*comb(2*k,k-M-1)
            high=first/(1-fmpq(k-M-1,k+M+2))
            weights.append(fmpq(int((high*scale).ceil()),scale))
        factor*=fmpq(3,10)
    tail+=sum(weights,fmpq(0))+round_loss
    # Clenshaw recurrence, t = 2 z/(6/5) - 1.
    linear=fmpq_poly([-1,fmpq(5,3)])
    later=fmpq_poly([])
    current=fmpq_poly([])
    for j in range(M,0,-1):
        later,current=current,2*linear*current-later+fmpq(numerators[j],scale)
    poly=linear*current-later+fmpq(numerators[0],scale)
    err=F(str(tail))
    assert err<F('1e-67')
    return list(poly),err
