"""Q^np_{a8} auf Polynome P(x/a8) mit Traeger (-a8,a8): analytische Zerlegung
   Q P (t) = D_H P + q0 P + V(t) P - Gamma P - S P,  t = x/a8,
   D_H P_n = H_n P_n, q0 = -log(2 pi a8) - gamma, V = -1/2 log(1-t^2),
   Gamma P(t) = a8 int_{-1}^{1} k_reg(a8|t-u|) P(u) du, k_reg(r) = k(r) - 1/(2r),
   S P(t) = sum_{q<8} w_q [P(t+log q/a8) + P(t-log q/a8)] (Indikator des Traegers).
"""
import mpmath as mp
import mpmath.calculus.quadrature as Qd

def setup(dps):
    mp.mp.dps = dps
    g = {}
    g['a8'] = 3*mp.log(2)/2
    g['q0'] = -mp.log(2*mp.pi*g['a8']) - mp.euler
    g['kappa'] = mp.log(8*mp.pi) + mp.euler + mp.pi/2
    g['shifts'] = [(q, mp.log(pr)/mp.sqrt(q), mp.log(q)/g['a8']) for q, pr in [(2,2),(3,3),(4,2),(5,5),(7,7)]]
    gl = Qd.GaussLegendre(mp.mp)
    g['gl'] = gl.calc_nodes(7, mp.mp.prec)   # 192 Knoten (exakt bis Grad 383)
    g['H'] = [mp.mpf(0)]
    for n in range(1, 600): g['H'].append(g['H'][-1] + mp.mpf(1)/n)
    return g

def k_reg(r):
    if r == 0: return mp.mpf(1)/4
    return mp.exp(-r/2)/(-mp.expm1(-2*r)) - 1/(2*r)

def legendre_all(s, N):
    P = [mp.mpf(1), s]
    for n in range(1, N-1):
        P.append(((2*n+1)*s*P[n] - n*P[n-1])/(n+1))
    return P[:N]

class LegPoly:
    """P(t) = sum_n coef[n] P_n(t)"""
    def __init__(self, coef): self.coef = coef; self.N = len(coef)
    def __call__(self, t):
        if abs(t) >= 1: return mp.mpf(0)
        P = legendre_all(t, self.N); return sum(c*p for c, p in zip(self.coef, P))
    def inside(self, t):
        P = legendre_all(t, self.N); return sum(c*p for c, p in zip(self.coef, P))

def gamma_action(poly, t, g):
    a8 = g['a8']; tot = mp.mpf(0)
    for lo, hi in [(-1, t), (t, 1)]:
        mid, half = (lo+hi)/2, (hi-lo)/2
        if half <= 0: continue
        for s, w in g['gl']:
            u = mid + half*s
            tot += half*w*k_reg(a8*abs(t-u))*poly.inside(u)
    return a8*tot

def shift_action(poly, t, g):
    return sum(w*(poly(t+lq) + poly(t-lq)) for q, w, lq in g['shifts'])

def q_action(poly, t, g, dh_coef):
    """dh_coef: Koeffizienten von D_H P (H_n * coef[n])"""
    P = legendre_all(t, poly.N)
    val = sum(c*p for c, p in zip(poly.coef, P))
    dh = sum(c*p for c, p in zip(dh_coef, P))
    V = -mp.log(1-t*t)/2
    return dh + g['q0']*val + V*val - gamma_action(poly, t, g) - shift_action(poly, t, g)
