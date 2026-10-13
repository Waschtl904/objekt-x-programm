"""Complete real Cauchy transforms of polynomial/logarithm functions.

The pole must lie strictly outside the integration interval. There is no
quadrature and no truncation of the logarithmic coefficient sequence.
"""
from flint import arb, acb, ctx

_ordinary_cache={}

def integer_powers(x,n):
    result=[arb(1)]
    for k in range(n):result.append(result[-1]*x)
    return result


def cauchy_moments(s, lo, hi, n, log_root=None):
    assert lo < hi and (s < lo or s > hi)
    if log_root is None:
        value = (abs(s-lo)/abs(s-hi)).log()
        lp,hp=integer_powers(lo,n),integer_powers(hi,n)
        ordinary = [(hp[k+1]-lp[k+1])/(k+1) for k in range(n)]
    else:
        r = log_root
        assert not (s-r).contains(0)
        def primitive(t):
            if t is r or (t-r).is_zero():
                # The argument of Li_2 is EXACTLY one. Dividing two
                # enclosures would straddle its branch point and give NaN.
                return -abs(s-r).log()**2 + arb.pi()**2/6
            return -abs(s-r).log()*abs(s-t).log() + acb((s-t)/(s-r)).polylog(2).real
        value = primitive(hi)-primitive(lo)
        # These complete ordinary moments do not depend on the pole.
        at_lo=lo is r or bool((lo-r).is_zero())
        at_hi=hi is r or bool((hi-r).is_zero())
        key=(ctx.prec,str(lo),str(hi),str(r),n,at_lo,at_hi)
        if key not in _ordinary_cache:
            from log_integrals import primitive_log
            left=primitive_log(r,lo,n-1,at_lo) if n else []
            right=primitive_log(r,hi,n-1,at_hi) if n else []
            if len(_ordinary_cache)>512:_ordinary_cache.clear()
            _ordinary_cache[key]=[b-a for a,b in zip(left,right)]
        ordinary=_ordinary_cache[key]
    result = [value]
    for k in range(n):
        result.append(s*result[-1]-ordinary[k])
    return result


def row_pair(moments, coefficients, arb_mat):
    return arb_mat([moments[:coefficients.nrows()]])*coefficients
