#!/usr/bin/env python3
"""Rational, outward-rounded certificate; Python standard library only."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

SCALE = 10**35


def down(x):
    x = F(x)
    return F((x.numerator * SCALE) // x.denominator, SCALE)


def up(x):
    return -down(-F(x))


class I:
    def __init__(self, lo, hi=None):
        self.lo = down(lo)
        self.hi = up(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def of(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        o = I.of(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-I.of(other))

    def __rsub__(self, other):
        return I.of(other) + (-self)

    def __mul__(self, other):
        o = I.of(other)
        v = [self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi]
        return I(min(v), max(v))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = I.of(other)
        assert o.lo > 0 or o.hi < 0
        return self * I(1/o.hi, 1/o.lo)

    def __rtruediv__(self, other):
        return I.of(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        v = I(1)
        for _ in range(n):
            v = v*self
        return v


def exp_pos(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= 4
    term = total = I(1)
    for k in range(1, 65):
        term = term*x/k
        total = total+term
    following = term*x/65
    tail = following/(1-x/66)
    return total + I(0, tail.hi)


def atanh(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= F(1, 2)
    term = x
    total = I(0)
    for k in range(64):
        total = total + term/(2*k+1)
        term = term*x*x
    tail = term/(129*(1-x*x))
    return total + I(0, tail.hi)


LOG2 = 2*atanh(I(F(1, 3)))


def log_point(x):
    assert x > 0
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1
    return 2*atanh(I((x-1)/(x+1))) + k*LOG2


def log(x):
    x = I.of(x)
    return I(log_point(x.lo).lo, log_point(x.hi).hi)


def atan(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= F(1, 2)
    term = x
    total = I(0)
    for k in range(64):
        total = total + ((-1)**k)*term/(2*k+1)
        term = term*x*x
    # 64 terms end negative; the next positive term bounds the remainder.
    return total + I(0, (term/129).hi)


PI = 16*atan(I(F(1, 5))) - 4*atan(I(F(1, 239)))


def gamma():
    # Elementary harmonic/integral bounds, no decimal gamma import or EM rule.
    n = 10000
    harmonic = I(0)
    for k in range(1, n+1):
        harmonic = harmonic+I(F(1, k))
    v = harmonic-log(I(n))
    return I(v.lo-F(1, n), v.hi)


def H(s):
    q = 1/exp_pos(I.of(s)/2)
    r = (1-q)/(1+q)
    return log((1+q)/(1-q))/2 + PI/4 - atan(r)


def h(t):
    t = I.of(t)
    return (1/exp_pos(t/2))/(1-1/exp_pos(2*t))


def g(t):
    return h(t)-1/(2*I.of(t))


def outer_decimal(q, places, upper=False):
    scale = 10**places
    n = -((-q.numerator*scale)//q.denominator) if upper else (q.numerator*scale)//q.denominator
    sign = '-' if n < 0 else ''
    n = abs(n)
    return f'{sign}{n//scale}.{n%scale:0{places}d}'


def encode(v):
    v = I.of(v)
    return {'lower': str(v.lo), 'upper': str(v.hi),
            'decimal_outer': [outer_decimal(v.lo, 12), outer_decimal(v.hi, 12, True)]}


def certificate():
    checks = []
    values = {}

    def keep(name, v):
        values[name] = encode(v)
        return v

    def ok(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    a = F(19651, 50000)
    L = 2*a
    ell = LOG2
    sqlo = F(1414213562373095048801688724209698, 10**33)
    sqhi = sqlo+F(1, 10**33)
    ok('algebraic sqrt(2) enclosure', sqlo**2 < 2 < sqhi**2)
    w = keep('w', ell/I(sqlo, sqhi))
    ok('only prime 2 active and its endpoint bands disjoint', a < ell.lo and ell.hi < L < log(I(3)).lo)
    ok('Gamma monotonicity rational coefficient', F(1240, 3249) < F(1, 2) and L < 2)
    kap = keep('kappa', log(8*PI)+gamma()+PI/2)
    Hd = H(L-ell)
    Hl = H(ell)
    C = keep('C', kap+w-Hd-Hl)
    center = keep('center_minus_end', 2*H(a)-Hd-Hl+w)
    ok('endband node floor is global', C.lo > 0 and center.lo > 0)
    m = keep('m', H(a+ell/2)+H(a-ell/2)-Hd-Hl)
    ok('positive outer node reserve', m.lo > F(3, 10))
    z = ell/L
    p = keep('p', 1-F(9, 4)*z**5+F(5, 2)*z**3-F(5, 4)*z)
    b0sq = keep('constant_projection_squared', F(5, 4)*(z-z**3)**2)
    v = keep('node_tail_mass', p-p*p-b0sq)
    ok('exact projected node tail mass positive', 0 < v.lo < v.hi < p.lo)
    lam = keep('lambda2', 1+L*h(L)-C)
    delta = keep('delta', lam+F(7, 12))
    ok('negative scalar mode 2 and positive full infinite tail', lam.hi < 0 and delta.lo > F(53, 100))
    rmax = keep('gamma_kernel_upper', F(1, 4)-g(L))
    qg = keep('gamma_e2_bounds', I((F(21, 32)*L*(g(L/2)-g(L))).lo, (L*rmax).hi))
    Mg = keep('gamma_operator_norm_bound', 2*L*rmax)
    q2 = keep('prime2_e2', w*60*ell**2*(L-ell)**3/L**5)
    M2 = keep('prime2_operator_norm_bound', 2*w)
    ok('Gamma and Prime-2 both contribute strictly positive mode-2 energy', qg.lo > F(1, 100) and q2.lo > F(3, 100))
    ok('bounded Gamma and Prime-2 tails', 0 < Mg.hi < F(27, 500) and M2.hi < 1)
    # Retain their exact sum T in the actual full block. The following is a
    # conservative comparison bound for that block, not a finite truncation.
    s = F(1, 10)
    theta = F(3, 4)
    mu = keep('mu', theta*m)
    dt = keep('comparison_tail', delta-s/(1-s)*(Mg+M2))
    ok('joint residual comparison tail positive', dt.lo > F(2, 5))
    sigma = keep('full_pivot_lower_bound', lam+s*(qg+q2)+mu*p-mu**2*v/dt)
    ok('full infinite-dimensional Schur pivot greater than 1/50', sigma.lo > F(1, 50))
    # The exact full A is enclosed; D_full >= delta I. From positivity and
    # sigma_full >= sigma.lo: ||D_full^-1 b_full||^2 <= (A-sigma.lo)/delta.
    A = keep('full_A22', lam+mu*p+qg+q2)
    ksq = keep('full_shear_squared_upper_bound', (A-I(sigma.lo))/delta)
    ok('actual full inverse shear norm less than 3/2', ksq.hi < F(1, 4))
    eta = keep('pre_moment_gap_lower_bound', I(min(sigma.lo, delta.lo))/F(9, 4))
    ok('full back-transformed gap greater than 2/225', eta.lo > F(2, 225))
    t = a/2
    be = (t*t/(2*(1-t*t/12)))**2
    bo = (t*t/(6*(1-t*t/20)))**2
    keep('beta_even', be)
    keep('beta_odd', bo)
    K = keep('K', C+theta/(1-theta)*m)
    penalty = keep('moment_penalty', be*K)
    numerator = keep('post_moment_numerator', eta-penalty)
    ok('positive moment-subtracted numerator', numerator.lo > F(7, 1000))
    G = keep('full_even_gap_lower_bound', numerator/(1+be))
    ok('final division by 1+beta_even gives gap greater than 1/150', G.lo > F(1, 150))
    odd = keep('odd_gap_lower_bound', (lam+F(1, 3)-(F(1, 2)-lam)*bo)/(1+bo))
    ok('odd gap greater than 1/4', odd.lo > F(1, 4))
    return {'status': 'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
            'a': str(a), 'mathematical_anchor': '9aa5cb1edac72fc683c5c9aba5a1f0639fbbf8bb',
            'arithmetic': 'Fraction with outward rounding on 10^-35 grid; no floats',
            'node_theta': str(theta), 'joint_difference_split': str(s),
            'published_gap': '1/150', 'checks': checks, 'values': values}


def artifacts(result):
    log_text = '\n'.join('PASS '+c for c in result['checks'])
    log_text += f"\nTOTAL {len(result['checks'])}\n"
    return {'full_residual_results.json': (json.dumps(result, indent=2)+'\n').encode('utf-8'),
            'full_residual_checks.log': log_text.encode('utf-8')}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true', help='write deterministic JSON and log')
    parser.add_argument('--verify', action='store_true', help='compare JSON/log and all manifest bytes')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    result = certificate()
    generated = artifacts(result)
    if args.write:
        for name, data in generated.items():
            (root/name).write_bytes(data)
    if args.verify:
        for name, data in generated.items():
            assert (root/name).read_bytes() == data, f'stale generated artifact: {name}'
        manifest_names = []
        for line in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
            digest, name = line.split('  ', 1)
            assert name not in manifest_names and '/' not in name and '\\' not in name
            manifest_names.append(name)
            assert hashlib.sha256((root/name).read_bytes()).hexdigest() == digest, name
        assert set(manifest_names) == {'README.md', 'PROOF.md', 'check_full_residual.py', *generated}
        print('PASS deterministic artifacts and all 5 SHA256 entries')
    print(generated['full_residual_checks.log'].decode('utf-8'), end='')
    for key in ['full_pivot_lower_bound', 'full_shear_squared_upper_bound', 'pre_moment_gap_lower_bound', 'moment_penalty', 'full_even_gap_lower_bound']:
        print(key, result['values'][key]['decimal_outer'])


if __name__ == '__main__':
    main()
