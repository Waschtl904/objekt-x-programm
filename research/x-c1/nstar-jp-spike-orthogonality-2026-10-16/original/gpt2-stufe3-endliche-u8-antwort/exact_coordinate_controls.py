"""Finite rational controls for projection factors and the scalar bypass identity.

These controls test algebra; they do not replace infinite-dimensional hypotheses.
"""
from fractions import Fraction as F


def dot(a, b): return sum((x*y for x, y in zip(a, b)), F(0))
def mv(a, x): return [dot(row, x) for row in a]
def tmv(a, x): return [dot(list(col), x) for col in zip(*a)]


def run():
    n, low = 7, 3
    m = list(map(F, [2, 1, -3, 4, 1, -2, 3]))
    delta, rho = F(9, 5), F(1, 100)
    c = [[F(2), F(1), F(-1)], [F(0), F(3), F(2)], [F(0), F(0), F(1)]]
    b = [[F(2), F(-1), F(1)], [F(3), F(2), F(0)], [F(-1), F(1), F(2)]]
    def project(x):
        d = dot(m, x)/dot(m, m)
        return [v-d*w for v, w in zip(x, m)]
    def mstar(x): return [v-w*x[0]/m[0] for v, w in zip(x, m)]
    def lift(x):
        out = list(x)
        assert out[0] == 0
        out[0] = -dot(m, out)/m[0]
        return out
    positive, wrong_rejected = 0, 0
    for seed in range(1, 5):
        f = project([F((i+seed)**2-3*i) for i in range(n)])
        h = project([F((-1)**i*(2*i+seed)) for i in range(n)])
        mf, mh = mstar(f), mstar(h)
        cf, ch = mf[1:low+1], mh[1:low+1]
        yf, yh = mf[low+1:], mh[low+1:]
        gamma = dot(m, m)/m[0]**2
        high_formula = dot(f, h)+gamma*f[0]*h[0]-dot(cf, ch)
        assert dot(yf, yh) == high_formula
        positive += 1
        if dot(f, h)-dot(cf, ch) != high_formula: wrong_rejected += 1
        vf = tmv(c, [x-y/delta for x, y in zip(cf, mv(b, yf))])
        vh = tmv(c, [x-y/delta for x, y in zip(ch, mv(b, yh))])
        cc = [x/(1-rho) for x in mv(c, vf)]
        full = lift([F(0)]+cc+[F(0)]*3)
        high = lift([F(0)]*4+[x-y for x, y in zip(yf, tmv(b, cc))])
        u = [x+y/delta for x, y in zip(full, high)]
        assert u[1:4] == cc and dot(m, u) == 0
        assert dot(u, h) == dot(yf, yh)/delta+dot(vf, vh)/(1-rho)
        assert dot(u, h) == high_formula/delta+dot(vf, vh)/(1-rho)
        positive += 4
        if dot(u, h) != dot(vf, vh)/(1-rho): wrong_rejected += 1
    assert wrong_rejected == 8
    return {'exact_coordinate_and_scalar_identities': positive,
            'omitted_moment_or_high_term_countercontrols_rejected': wrong_rejected}


if __name__ == '__main__': print(run())
