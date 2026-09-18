#!/usr/bin/env python3
"""Gamma-plus-Node envelope: rational derivatives and exhaustive interval covers.

All proof decisions and displayed enclosures use integer/Fraction arithmetic.
The analytic domain and the meaning of the interval covers are in PROOF.md.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

SCALE = 10**25


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
    # Convex trapezoid error: 0 < E < (1/8) integral_N^infty f''
    # for f(x)=1/x. Thus gamma=H_N-log(N)-1/(2N)+E.
    n = 10000
    harmonic = I(0)
    for k in range(1, n+1):
        harmonic = harmonic+I(F(1, k))
    v = harmonic-log(I(n))-F(1, 2*n)
    return I(v.lo, v.hi+F(1, 8*n*n))


def H(s):
    q = 1/exp_pos(I.of(s)/2)
    r = (1-q)/(1+q)
    return log((1+q)/(1-q))/2 + PI/4 - atan(r)


def h(t):
    t = I.of(t)
    return (1/exp_pos(t/2))/(1-1/exp_pos(2*t))


def g(t):
    return h(t)-1/(2*I.of(t))


class J:
    """Second-order interval jets in two real variables."""
    def __init__(self, v, d=None, hess=None):
        self.v = I.of(v)
        self.d = [I(0), I(0)] if d is None else d
        self.hess = [[I(0), I(0)], [I(0), I(0)]] if hess is None else hess

    @staticmethod
    def of(x):
        return x if isinstance(x, J) else J(x)

    @staticmethod
    def var(v, index):
        r = J(v)
        r.d[index] = I(1)
        return r

    def __add__(self, other):
        o = J.of(other)
        return J(self.v+o.v, [self.d[i]+o.d[i] for i in range(2)],
                 [[self.hess[i][j]+o.hess[i][j] for j in range(2)] for i in range(2)])

    __radd__ = __add__

    def __neg__(self):
        return J(-self.v, [-v for v in self.d], [[-v for v in row] for row in self.hess])

    def __sub__(self, other):
        return self+-J.of(other)

    def __rsub__(self, other):
        return J.of(other)+-self

    def __mul__(self, other):
        o = J.of(other)
        return J(self.v*o.v, [self.d[i]*o.v+self.v*o.d[i] for i in range(2)],
                 [[self.hess[i][j]*o.v+self.d[i]*o.d[j]+self.d[j]*o.d[i]+self.v*o.hess[i][j]
                   for j in range(2)] for i in range(2)])

    __rmul__ = __mul__

    def compose(self, val, first, second):
        return J(val, [first*v for v in self.d],
                 [[first*self.hess[i][j]+second*self.d[i]*self.d[j] for j in range(2)] for i in range(2)])

    def reciprocal(self):
        return self.compose(1/self.v, -1/(self.v**2), 2/(self.v**3))

    def __truediv__(self, other):
        return self*J.of(other).reciprocal()

    def __rtruediv__(self, other):
        return J.of(other)*self.reciprocal()

    def __pow__(self, n):
        r = J(1)
        for _ in range(n):
            r = r*self
        return r


def regular_g(t):
    # Cancellation-free g(t)=1/4[1/cosh(x)-x B(x)/(1+x^2 B(x))], x=t/2.
    # B(x)=sum_{k>=0} x^(2k)/(2k+3)!, including all derivative tails.
    from math import factorial
    x = I.of(t)/2
    assert 0 <= x.lo <= x.hi <= F(3, 5)
    jets = []
    for shift in (0, 3):
        vals = []
        for derivative in range(3):
            total = I(0)
            for k in range(17):
                power = 2*k
                if power < derivative:
                    continue
                coeff = F(factorial(power), factorial(power-derivative)*factorial(power+shift))
                total += coeff*x**(power-derivative)
            power = 34
            coeff = F(factorial(power), factorial(power-derivative)*factorial(power+shift))
            tail = coeff*I(x.hi)**(power-derivative)/(1-I(x.hi)**2)
            vals.append(total+I(0, tail.hi))
        jets.append(J(vals[0], [vals[1], I(0)], [[vals[2], I(0)], [I(0), I(0)]]))
    coshx, B = jets
    X = J.var(x, 0)
    result = (1/coshx-X*B/(1+X*X*B))/4
    return result.v, result.d[0]/2, result.hess[0][0]/4


def phi(z):
    z = I.of(z)
    return z**3*(20+z*(-45+z*(36-10*z)))


def q_jet(a, z):
    L = 2*I.of(a)
    z = I.of(z)
    val, first, second = regular_g(L*z)
    diff = val-regular_g(L)[0]
    P = phi(z)
    P1 = 60*z*z*(1-z)**3
    P2 = 60*z*(1-z)**2*(2-5*z)
    return (L*P*diff, L*(P1*diff+L*P*first),
            L*(P2*diff+2*L*P1*first+L*L*P*second))


KAPPA = log(8*PI)+gamma()+PI/2
SQ2 = I(F(1414213562373095048801688724209698, 10**33), F(1414213562373095048801688724209699, 10**33))


def constants(a):
    # Active-endband analytic branch; run_certificate verifies that it equals
    # the true global node floor throughout the whole crossing interval.
    a = I.of(a)
    L = 2*a
    ell = LOG2
    Hd, Hl = H(L-ell), H(ell)
    C = KAPPA+ell/SQ2-Hd-Hl
    m = H(a+ell/2)+H(a-ell/2)-Hd-Hl
    z0 = ell/L
    p = 1-F(9, 4)*z0**5+F(5, 2)*z0**3-F(5, 4)*z0
    lam = 1+L*h(L)-C
    be = ((a/2)**2/(2*(1-(a/2)**2/12)))**2
    bo = ((a/2)**2/(6*(1-(a/2)**2/20)))**2
    return dict(a=a, C=C, m=m, p=p, lam=lam, delta=lam+F(7, 12),
                be=be, bo=bo, M=2*L*(F(1, 4)-regular_g(L)[0]))


def gap(c, q, s, theta, jets=False):
    if jets:
        s, theta = J.var(s, 0), J.var(theta, 1)
        c = {k:J(v) for k,v in c.items()}
        q = J(q)
    elif not isinstance(s, J):
        s, theta = I.of(s), I.of(theta)
    d = c['delta']-s/(1-s)*c['M']
    mu = theta*c['m']
    sigma = c['lam']+s*q+mu*c['p']*(1-mu/d)
    eta = sigma/(1+mu/d)**2
    K = c['C']+theta/(1-theta)*c['m']
    return (eta-c['be']*K)/(1+c['be'])


def mid(v):
    return (v.lo+v.hi)/2


def z_bracket(a, bits=28):
    lo, hi = F(2, 5), F(1)
    for _ in range(bits):
        z = (lo+hi)/2
        derivative = q_jet(a, z)[1]
        if derivative.lo > 0:
            lo = z
        elif derivative.hi < 0:
            hi = z
        else:
            break
    return I(lo, hi)


def dec(v):
    v = I.of(v)
    # Integers only, diagnostic truncation to 10 digits, not proof endpoints.
    q = mid(v)
    n = abs(q.numerator)*10**10//q.denominator
    return ('-' if q < 0 else '')+str(n//10**10)+'.'+str(n%10**10).zfill(10)


def q_max(a):
    zb = z_bracket(a)
    zm = mid(zb)
    q, qp, _ = q_jet(a, zm)
    radius = (zb.hi-zb.lo)/2
    # The tangent line of a concave function bounds its maximum from above.
    return zb, I(q.lo, q.hi+max(abs(qp.lo), abs(qp.hi))*radius)


LEVEL = -F(1, 10000)
SBOX = (F(328025,10**6), F(328825,10**6))
TBOX = (F(759267,10**6), F(759667,10**6))


def boundary_s_zero(c, q):
    pending = [(F(3,10), F(199,200))]
    leaves = 0
    length = F(0)
    while pending:
        lo, hi = pending.pop()
        val = gap(c, q, 0, I(lo,hi))
        if val.hi < LEVEL:
            leaves += 1
            length += hi-lo
            continue
        assert hi-lo > F(1, 10**8), 's=0 boundary exclusion failed'
        m = (lo+hi)/2
        pending += [(lo,m), (m,hi)]
    assert length == F(199,200)-F(3,10)
    return leaves


def stationary_cover(c, q):
    pending = [(F(0),F(3,4),F(3,10),F(199,200))]
    counts = dict(visited=0,value=0,ds=0,dtheta=0,inside=0)
    area = F(0)
    while pending:
        sl, sh, tl, th = pending.pop()
        counts['visited'] += 1
        assert counts['visited'] < 50000, 'stationary cover limit'
        if SBOX[0] <= sl and sh <= SBOX[1] and TBOX[0] <= tl and th <= TBOX[1]:
            counts['inside'] += 1
            area += (sh-sl)*(th-tl)
            continue
        j = gap(c, q, I(sl,sh), I(tl,th), True)
        if j.v.hi < LEVEL:
            counts['value'] += 1
            area += (sh-sl)*(th-tl)
        elif j.d[0].lo > 0 or j.d[0].hi < 0:
            counts['ds'] += 1
            area += (sh-sl)*(th-tl)
        elif j.d[1].lo > 0 or j.d[1].hi < 0:
            counts['dtheta'] += 1
            area += (sh-sl)*(th-tl)
        else:
            if sh-sl >= th-tl:
                sm = (sl+sh)/2
                pending += [(sl,sm,tl,th),(sm,sh,tl,th)]
            else:
                tm = (tl+th)/2
                pending += [(sl,sh,tl,tm),(sl,sh,tm,th)]
    assert area == F(3,4)*(F(199,200)-F(3,10))
    assert counts['visited'] == 2*sum(counts[k] for k in ['value','ds','dtheta','inside'])-1
    return counts


def a_derivative(c, z, s, theta):
    a = c['a']
    L = 2*a
    ell = LOG2
    Cp = 2*h(L-ell)
    mp = -h(a+ell/2)-h(a-ell/2)+2*h(L-ell)
    z0 = ell/L
    pp = F(5,4)*(3*z0*z0-1)**2*z0/a
    em = 1/exp_pos(2*L)
    hp = h(L)*(-F(1,2)-2*em/(1-em))
    lp = 2*h(L)+2*L*hp-Cp
    Mp = 4*(F(1,4)-regular_g(L)[0])-4*L*regular_g(L)[1]
    av = J.var(a,0)
    betaj = ((av/2)**2/(2*(1-(av/2)**2/12)))**2
    derivatives = dict(a=I(1), C=Cp,m=mp,p=pp,lam=lp,delta=lp,be=betaj.d[0],bo=I(0),M=Mp)
    cj = {k:J(v,[derivatives[k],I(0)]) for k,v in c.items()}
    qval = q_jet(a,z)[0]
    P = phi(z)
    qp = 2*P*(regular_g(L*z)[0]-regular_g(L)[0])+2*L*P*(z*regular_g(L*z)[1]-regular_g(L)[1])
    qj = J(qval,[qp,I(0)])
    return gap(cj,qj,J(s),J(theta)).d[0]


def run_certificate():
    checks = []
    values = {}

    def ok(name, condition):
        assert condition, name
        checks.append(name)

    def keep(name, val):
        values[name] = encode(val)
        return val

    al, au = F(3931224,10**7), F(3931226,10**7)
    arange = I(al,au)
    c = constants(arange)
    ok('sqrt2 enclosed algebraically', SQ2.lo**2 < 2 < SQ2.hi**2)
    ok('window strictly inside Prime-2-only domain', LOG2.hi < 2*al < 2*au < log(I(3)).lo)
    center_minus_end = 2*H(arange)-H(2*arange-LOG2)-H(LOG2)+LOG2/SQ2
    keep('center_minus_end',center_minus_end)
    ok('active-endband node floor is the global floor on the crossing interval', center_minus_end.lo > 0)
    half = F(1,2)
    ok('exact Gamma primitive at half and full length',
       20*half**3-45*half**4+36*half**5-10*half**6 == F(21,32) and 20-45+36-10 == 1)
    # This finite analytic interval cover proves g''<0 on [0,4/5].
    gsecond = []
    for k in range(8):
        v = regular_g(I(F(k,10),F(k+1,10)))[2]
        assert v.hi < 0
        gsecond.append(encode(v))
    ok('eight derivative intervals certify g second derivative negative on [0,4/5]', len(gsecond)==8)
    zb, q = q_max(arange)
    keep('z_optimizer',zb)
    keep('q_maximum',q)
    qleft, qright = q_jet(arange,zb.lo)[1], q_jet(arange,zb.hi)[1]
    keep('q_z_left',qleft)
    keep('q_z_right',qright)
    ok('Gamma optimizer isolated by derivative signs', qleft.lo > 0 and qright.hi < 0 and 2*arange.hi < F(4,5))
    ok('positive coefficients and negative lambda2 plus maximal Gamma diagonal',
       all(c[k].lo>0 for k in ['C','m','p','delta','be','bo','M']) and q.lo>0 and c['lam'].hi+q.hi < 0)
    base_negative = -c['be']*c['C']/(1+c['be'])
    keep('nonpositive_pivot_gap_upper',base_negative)
    ok('nonpositive pivots lie below comparison level', base_negative.hi < LEVEL)
    slowtheta_sigma = c['lam']+q+F(3,10)*c['m']*c['p']
    shigh_sigma = c['lam']+q+c['p']*(c['delta']-3*c['M'])/4
    keep('small_theta_sigma_upper',slowtheta_sigma)
    keep('large_s_sigma_upper',shigh_sigma)
    ok('small theta and large s are excluded globally', slowtheta_sigma.hi < 0 and shigh_sigma.hi < 0)
    sigma_max = c['lam']+q+c['p']*c['delta']/4
    top_theta = (I(max(F(0),sigma_max.hi))-c['be']*(c['C']+199*c['m']))/(1+c['be'])
    keep('large_theta_gap_upper',top_theta)
    ok('theta approaching one excluded globally', top_theta.hi < LEVEL)
    keep('compact_tail_floor',c['delta']-3*c['M'])
    ok('closed search rectangle has positive tail and inactive min branch',
       (c['delta']-3*c['M']).lo > 0 and
       (c['lam']+q+c['m']*c['p']).hi < (c['delta']-3*c['M']).lo)
    center = (F(328425,10**6),F(759467,10**6))
    keep('uniform_interior_witness',gap(c,q,*center))
    ok('uniform interior witness exceeds exclusion level', gap(c,q,*center).lo > LEVEL)
    boundary = boundary_s_zero(c,q)
    ok('entire s=0 boundary excluded by complete interval cover', boundary>0)
    counts = stationary_cover(c,q)
    ok('exhaustive adaptive derivative cover isolates all possible maximizers', counts['inside']>0)
    bjet = gap(c,q,I(*SBOX),I(*TBOX),True)
    hh = bjet.hess
    determinant = hh[0][0]*hh[1][1]-hh[0][1]*hh[1][0]
    keep('Hessian_ss',hh[0][0])
    keep('Hessian_s_theta',hh[0][1])
    keep('Hessian_theta_theta',hh[1][1])
    keep('Hessian_determinant',determinant)
    ok('negative definite Hessian gives unique maximizer', hh[0][0].hi < 0 and determinant.lo > 0)
    ga = a_derivative(c,zb,I(*SBOX),I(*TBOX))
    keep('envelope_a_derivative',ga)
    ok('optimized envelope decreases strictly across crossing interval', ga.hi < -5)
    endpoints = []
    for a in (al,au):
        cc = constants(a)
        zz, qq = q_max(a)
        j = gap(cc,qq,*center,True)
        radii = [max(abs(center[0]-v) for v in SBOX), max(abs(center[1]-v) for v in TBOX)]
        tangent_upper = j.v.hi+sum(max(abs(j.d[i].lo),abs(j.d[i].hi))*radii[i] for i in range(2))
        witness = gap(cc,q_jet(a,mid(zz))[0],*center)
        label = 'lower_endpoint' if a == al else 'upper_endpoint'
        keep(label+'_witness',witness)
        keep(label+'_global_tangent_upper',tangent_upper)
        keep(label+'_z_optimizer',zz)
        endpoints.append((witness.lo,tangent_upper))
    ok('positive certified envelope at lower rational endpoint', endpoints[0][0]>0)
    ok('negative global upper bound at upper rational endpoint', endpoints[1][1]<0)
    odd = keep('odd_gap_lower_bound',(c['lam']+F(1,3)-(F(1,2)-c['lam'])*c['bo'])/(1+c['bo']))
    ok('odd sector stays above 1/4 throughout crossing interval', odd.lo>F(1,4))
    return dict(status='AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
                arithmetic='Fraction, outward grid 10^-25, no binary floats',
                a_bracket=[str(al),str(au)],
                optimizer_box={'s':list(map(str,SBOX)),'theta':list(map(str,TBOX)),
                               'z':[str(zb.lo),str(zb.hi)]},
                search_rectangle_closure={'s':['0','3/4'],'theta':['3/10','199/200'],
                                'comparison_level':str(LEVEL)},
                rational_witness=list(map(str,center)),
                stationary_cover=counts, s_zero_boundary_leaves=boundary,
                g_second_derivative_cover=gsecond,
                checks=checks,values=values)


def outer_decimal(q, places=12, upper=False):
    scale = 10**places
    n = -((-q.numerator*scale)//q.denominator) if upper else q.numerator*scale//q.denominator
    sign = '-' if n < 0 else ''
    n = abs(n)
    return f'{sign}{n//scale}.{n%scale:0{places}d}'


def encode(v):
    v = I.of(v)
    return {'lower':str(v.lo),'upper':str(v.hi),
            'decimal_outer':[outer_decimal(v.lo),outer_decimal(v.hi,upper=True)]}


def artifacts(result):
    log_text = '\n'.join('PASS '+c for c in result['checks'])
    log_text += f"\nTOTAL {len(result['checks'])}\n"
    log_text += 'STATIONARY_COVER '+json.dumps(result['stationary_cover'],sort_keys=True)+'\n'
    log_text += 'S_ZERO_BOUNDARY_LEAVES '+str(result['s_zero_boundary_leaves'])+'\n'
    return {'gamma_node_results.json':(json.dumps(result,indent=2)+'\n').encode('utf-8'),
            'gamma_node_checks.log':log_text.encode('utf-8')}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--verify',action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    result = run_certificate()
    generated = artifacts(result)
    if args.write:
        for name,data in generated.items():
            (root/name).write_bytes(data)
    if args.verify:
        for name,data in generated.items():
            assert (root/name).read_bytes()==data, 'stale '+name
        names = []
        for line in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
            digest,name = line.split('  ',1)
            assert name not in names and '/' not in name and '\\' not in name
            names.append(name)
            assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
        assert set(names)=={'README.md','PROOF.md','check_gamma_node_waxing.py',*generated}
        print('PASS deterministic artifacts and all five SHA256 entries')
    print(generated['gamma_node_checks.log'].decode('utf-8'),end='')
    for key in ['lower_endpoint_witness','upper_endpoint_global_tangent_upper','envelope_a_derivative']:
        print(key,result['values'][key]['decimal_outer'])


if __name__ == '__main__':
    main()
