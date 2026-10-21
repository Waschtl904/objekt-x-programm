"""Complete polynomial/logarithm moments, including endpoint singularities.

All primitive formulas follow by integration by parts and polynomial division.
Intervals may end at a logarithmic root but may not cross one internally.
The real dilogarithm is used only in a scalar primitive; no quadrature or
truncation of logarithmic high modes is used.
"""
from flint import arb, acb, arb_poly


def powers(x, n):
    out = [arb(1)]
    for _ in range(n):
        out.append(out[-1] * x)
    return out


def primitive_log(a, x, n, at_root=False):
    ap, xp = powers(a, n+1), powers(x, n+1)
    lg = arb(0) if at_root else abs(x-a).log()
    return [((xp[j+1]-ap[j+1])*lg - sum(
        (ap[k]*xp[j-k+1]/(j-k+1) for k in range(j+1)), arb(0))) / (j+1)
        for j in range(n+1)]


def primitive_log2(a, x, n, at_root=False):
    ap, xp = powers(a, n+1), powers(x, n+1)
    lm = primitive_log(a, x, n, at_root)
    lg2 = arb(0) if at_root else abs(x-a).log()**2
    return [((xp[j+1]-ap[j+1])*lg2 - 2*sum(
        (ap[k]*lm[j-k] for k in range(j+1)), arb(0))) / (j+1)
        for j in range(n+1)]


def primitive_loglog(a, b, x, n, at_a=False, at_b=False):
    assert not (a-b).contains(0)
    ap, bp, xp = powers(a, n+1), powers(b, n+1), powers(x, n+1)
    la = primitive_log(a, x, n, at_a)
    lb = primitive_log(b, x, n, at_b)
    ld = abs(a-b).log()
    if at_a:
        boundary = [bp[j+1]*(arb.pi()**2/6-ld**2) for j in range(n+1)]
    elif at_b:
        boundary = [ap[j+1]*(arb.pi()**2/6-ld**2) for j in range(n+1)]
    else:
        al, bl = abs(x-a).log(), abs(x-b).log()
        da = acb((x-a)/(b-a)).polylog(2).real
        db = acb((x-b)/(a-b)).polylog(2).real
        boundary = [xp[j+1]*al*bl-ld*(ap[j+1]*al+bp[j+1]*bl)
                    +ap[j+1]*da+bp[j+1]*db for j in range(n+1)]
    return [(boundary[j]-sum((ap[k]*lb[j-k]+bp[k]*la[j-k]
                              for k in range(j+1)), arb(0)))/(j+1)
            for j in range(n+1)]


class Moments:
    """Named endpoints avoid guessing equality from overlapping intervals."""
    def __init__(self, roots, n):
        self.roots, self.n, self.cache = roots, n, {}

    def primitive(self, endpoint, logarithms=()):
        logarithms = tuple(sorted(logarithms))
        key = (endpoint, logarithms)
        if key in self.cache:
            return self.cache[key]
        x = self.roots[endpoint]
        if not logarithms:
            pp = powers(x, self.n+1)
            result = [pp[j+1]/(j+1) for j in range(self.n+1)]
        elif len(logarithms) == 1:
            a = logarithms[0]
            result = primitive_log(self.roots[a], x, self.n, a == endpoint)
        else:
            assert len(logarithms) == 2
            a, b = logarithms
            if a == b:
                result = primitive_log2(self.roots[a], x, self.n, a == endpoint)
            else:
                result = primitive_loglog(self.roots[a], self.roots[b], x,
                                          self.n, a == endpoint, b == endpoint)
        self.cache[key] = result
        return result

    def sequence(self, lo, hi, logarithms=()):
        aa, bb = self.primitive(lo, logarithms), self.primitive(hi, logarithms)
        return [b-a for a, b in zip(aa, bb)]

    def integral(self, poly, lo, hi, logarithms=()):
        assert len(poly) <= self.n+1
        m = self.sequence(lo, hi, logarithms)
        return sum((poly[k]*m[k] for k in range(len(poly))), arb(0))

    def polynomial_moments(self, poly, lo, hi, n, logarithms=()):
        if not len(poly):
            return [arb(0)]*(n+1)
        d = len(poly)-1
        assert d+n <= self.n
        seq = self.sequence(lo, hi, logarithms)[:d+n+1]
        conv = arb_poly(list(reversed(poly.coeffs())))*arb_poly(seq)
        return [conv[d+k] for k in range(n+1)]


def function_moments(parts, moments, lo, hi, n, extra_log=()):
    result = [arb(0)]*(n+1)
    for root, poly in parts.items():
        logarithms = (() if root is None else (root,))+extra_log
        vals = moments.polynomial_moments(poly, lo, hi, n, logarithms)
        result = [a+b for a, b in zip(result, vals)]
    return result


def function_product(a, b, moments, lo, hi):
    result = arb(0)
    for ra, pa in a.items():
        for rb, pb in b.items():
            logs = (() if ra is None else (ra,))+(() if rb is None else (rb,))
            result += moments.integral(pa*pb, lo, hi, logs)
    return result


def add_function(a, b, scale=1):
    result = dict(a)
    for r, p in b.items():
        result[r] = result.get(r, arb_poly([]))+p*scale
    return result
