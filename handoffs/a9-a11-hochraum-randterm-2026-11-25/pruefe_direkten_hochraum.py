"""Directed verification of the lifted direct row on the new odd shell."""
import json
from fractions import Fraction as F
from math import comb, factorial, isqrt

SOURCE = "9a21e089f65fe69367439819bd02b56fcb9c6508"
CASES = {
    "e": [
        "-0.59582177655562518",
        "0.64858020271278471",
        "-0.33069556952816787",
        "0.098350529204767598",
        "-0.017737011903709302",
        "0.0013347377068477922",
        "-0.00046429865739707539",
        "0.00055926124605209994",
        "0.00020939946182074647",
        "-0.00053072314306271855",
        "0.00033333826273553442",
        "-0.00010837339020799413"
    ],
    "s": [
        "-960",
        "-1786",
        "-1111",
        "735",
        "2564",
        "1686",
        "-2634",
        "-3352",
        "6471",
        "-4543",
        "1858",
        "-485"
    ]
}
SCALE = 10**75
N = 4096


def ceil_div(a, b):
    return -((-a) // b)


class Interval:
    """Endpoints are integers in units of 10^-75."""
    def __init__(self, lo, hi):
        assert lo <= hi
        self.lo, self.hi = lo, hi

    def __add__(self, value):
        other = box(value)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-box(other))

    def __rsub__(self, other):
        return box(other) + (-self)

    def __mul__(self, value):
        other = box(value)
        prod = [a*b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(min(prod)//SCALE, ceil_div(max(prod), SCALE))

    __rmul__ = __mul__

    def __truediv__(self, value):
        other = box(value)
        assert other.lo > 0
        return self * Interval(SCALE**2//other.hi, ceil_div(SCALE**2, other.lo))

    def sqrt(self):
        assert self.lo >= 0
        low, high = isqrt(self.lo*SCALE), isqrt(self.hi*SCALE)
        return Interval(low, high + (high*high < self.hi*SCALE))

    def absolute(self):
        return Interval(0 if self.lo <= 0 <= self.hi else min(abs(self.lo), abs(self.hi)),
                        max(abs(self.lo), abs(self.hi)))

    def display(self, digits=15):
        unit = SCALE//10**digits
        def fmt(i):
            a, r = divmod(abs(i), 10**digits)
            return ('-' if i<0 else '')+f'{a}.{r:0{digits}d}'
        return [fmt(self.lo//unit), fmt(ceil_div(self.hi,unit))]


def box(value):
    if isinstance(value, Interval):
        return value
    f = F(value)
    return Interval(f.numerator*SCALE//f.denominator, ceil_div(f.numerator*SCALE,f.denominator))


def symmetric(radius):
    return Interval(-radius.hi, radius.hi)


def atanh_rational(t, count=150):
    first_omitted = t**(2*count+1)/(2*count+1)
    partial = sum(t**(2*j+1)/(2*j+1) for j in range(count))
    return Interval(box(partial).lo, box(partial+first_omitted/(1-t*t)).hi)


def polynomial_at_endpoint(weights, right):
    # Coefficients of q(u) at u=0 or of q(1-v) at v=0.
    return [sum(w * ((-1)**(j-k + (j if right else 0))*comb(j,k)*comb(j+k,k))
                for j,w in enumerate(weights) if j>=k) for k in range(len(weights))]


def times_log_tail(poly, start):
    # The norm for k=0 is exactly 1/N. Ratios for k>=1 decrease with n>=N.
    ratio = F(1)
    total = box(0)
    for k, coefficient in enumerate(poly):
        if k:
            ratio *= F(k*k, (N-k)*(N+1+k))
        if k>=start:
            total += coefficient.absolute()*ratio
    return total / (2*N)


def compute(case):
    raw = [F(x) for x in CASES[case]]
    a = 2*atanh_rational(F(1,2))
    h = atanh_rational(F(1,10))
    mu = (box(F(4,3))-a)/2
    root3 = box(3).sqrt()
    weights = [box(2*j+1).sqrt()*x for j,x in enumerate(raw)]
    # Taylor polynomial of sinh((a+h*u)/2). Exact coefficients involve h and sqrt(3).
    m = []
    scale = box(1)
    for k in range(48):
        if k:
            scale = scale*h/(2*k)
        m.append(scale*(1 if k%2==0 else 2)/root3)
    raw_norm_squared = sum(c*c for c in raw)
    moment = box(0)
    for j,w in enumerate(weights):
        moment += w*sum(m[k]*F(factorial(k)**2, factorial(k-j)*factorial(k+j+1))
                        for k in range(j,len(m)))
    # Uniform Taylor error on 0<=u<=1, Cauchy-Schwarz in the unit interval.
    moment += symmetric(box(raw_norm_squared).sqrt()*F(2)*F(51,1000)**48/factorial(48))
    norm = (box(raw_norm_squared) + h*moment*moment/mu).sqrt()
    lift = -(h*moment/mu)/norm
    assert lift.absolute().hi < SCALE
    left = [x/norm for x in polynomial_at_endpoint(weights,False)]
    right = [x/norm for x in polynomial_at_endpoint(weights,True)]
    left += [box(0)]*(len(m)-len(left))
    jump = [x-lift*mk for x,mk in zip(left,m)]
    inner = jump[0].absolute()/(2*N)
    outer = right[0].absolute()/(2*N)
    varying = times_log_tail(jump,1)+times_log_tail(right,1)
    remainder = outer + varying + box('1e-30')
    upper = inner + remainder
    lower = inner - remainder
    return dict(norm=norm.display(), normalized_inner_jump=jump[0].display(),
                normalized_outer_value=right[0].display(),
                inner_constant_log_norm=inner.display(),
                outer_constant_log_norm=outer.display(),
                variable_log_upper=varying.display()[1],
                direct_after_inner_log_upper=remainder.display()[1],
                direct_tail_lower=lower.display()[0], direct_tail_upper=upper.display()[1])


def report():
    rows = {name: compute(name) for name in CASES}
    model_error = F('436586295261694305654338316329579061159459118426641817/20000000000000000000000000000000000000000000000000000000000000000000000000000000')
    assert model_error < F('2.183e-26')
    # Cauchy tails, smooth rational/log factors, Taylor remainder of the old lift.
    regular = 50*F(5)*F(24,25)**2049/(1-F(24,25))
    analytic = 100*F(51,1000)**65/(1-F(51,1000))
    old_lift = 400*6*F(11,10)**48/factorial(48)
    assert regular + analytic + old_lift < F('1e-30')
    old_residual = {'e': '0.00000000000667944674', 's': '0.00000053240166456875'}
    gate = {'e': '0.000033847', 's': '0.0054311'}
    budget = {'e': '3e-9', 's': '1e-4'}
    for name, row in rows.items():
        defect = (box('8.833') * F(old_residual[name])).sqrt()
        total = defect + F(gate[name]) + model_error + F(row['direct_after_inner_log_upper'])
        price = total*total/F('.58')
        assert price.hi < box(budget[name]).lo
        row['remaining_gate'] = gate[name]
        row['conditional_schur_price_upper'] = price.display(18)[1]
    return dict(commit=SOURCE, N=N, cases=rows,
                coupling_functionals_certified=False, point4_closed=False)


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))

