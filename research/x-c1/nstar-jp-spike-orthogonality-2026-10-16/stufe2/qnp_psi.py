"""Stufe 2: f_t = Pi8[ Q^np_{b9} psi_t ]|(0,a8) fuer die zusammengesetzte Quelle psi_t = Lambda(Jt) - F k_t.

Q^np_l u = H_Gamma u - kappa u - S_l u  (FUNKTIONSANSCHLUSS.txt §3), komprimiert auf (-l,l), l = b9:
  H_Gamma u(x) = int_0^oo k(r) [2u(x) - u(x+r) - u(x-r)] dr,  k(r) = e^{-r/2}/(1-e^{-2r}),
  kappa = log(8 pi) + EulerGamma + pi/2,
  S_l u = sum_{q<e^{2l}} w_q [u(.+log q) + u(.-log q)],  w_q = log(prime(q))/sqrt(q), q = 2,3,4,5,7,8.
  Pi8 f = f - m (int_0^a8 m f dx)/mu.
psi_t ist paritaetisch fortgesetzt und ausserhalb (-b9,b9) null. Die Sprungstellen von psi (+-a8, +-b9) und
alle durch Primverschiebungen in den Kern transportierten Sprungstellen werden als Integrations-Breakpoints
gefuehrt. Hochpraezise Gleitkomma-Diagnose (mpmath); KEIN Intervallzertifikat.
"""
import json, sys, time
from fractions import Fraction as Fr
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
PSI_PATH = Path('/home/user/workspace/stufe1/PSI_DEFINITION.json')

def setup(dps):
    mp.mp.dps = dps
    g = {}
    g['a8'] = 3*mp.log(2)/2; g['b9'] = mp.log(3); g['h'] = g['b9']-g['a8']; g['c'] = (g['a8']+g['b9'])/2
    g['kappa'] = mp.log(8*mp.pi) + mp.euler + mp.pi/2
    g['shifts'] = [(q, mp.log(pr)/mp.sqrt(q), mp.log(q)) for q, pr in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]]
    return g

def k_gamma(r):
    if r <= 0:
        return mp.inf
    return mp.exp(-r/2)/(-mp.expm1(-2*r))

def legendre_all(s, N):
    P = [mp.mpf(1), s]
    for n in range(1, N-1):
        P.append(((2*n+1)*s*P[n] - n*P[n-1])/(n+1))
    return P[:N]

class Psi:
    """psi_t aus PSI_DEFINITION.json (Mittelpunkte)."""
    def __init__(self, g, par, direction, lam_total_override=None):
        D = json.load(open(PSI_PATH))
        P = D[par]; d = P['directions'][direction]
        self.g = g; self.sigma = P['sigma']; self.eps = (-1)**self.sigma
        self.mu = mp.mpf(P['mu'])
        self.shell = [mp.mpf(x) for x in d['shell_coeff_mid']]
        self.N = len(self.shell)
        self.degs = P['core_z_degrees']
        self.ratios = [mp.mpf(x) for x in P['core_z_moment_ratios']]
        self.k = [mp.mpf(x) for x in d['core_k_mid']]
        self.lam_total = mp.mpf(d['lambda_total_mid']) if lam_total_override is None else lam_total_override
        self.sqrt_norm = [mp.sqrt(mp.mpf(2*n+1)/(2*g['h'])) for n in range(self.N)]
        self.eb_norm = {n: mp.sqrt(mp.mpf(2*n+1)/(2*g['b9'])) for n in self.degs+[self.sigma]}
    def m(self, x):
        return mp.cosh(x/2) if self.sigma == 0 else mp.sinh(x/2)
    def core(self, x):  # 0 <= x < a8
        g = self.g
        P = legendre_all(x/g['b9'], max(self.degs)+1)
        e = lambda n: self.eb_norm[n]*P[n]
        es = e(self.sigma)
        return -self.lam_total*self.m(x)/self.mu - sum(self.k[i]*(e(self.degs[i]) - es*self.ratios[i]) for i in range(4))
    def shell_val(self, x):  # a8 < x < b9
        g = self.g
        P = legendre_all(2*(x-g['c'])/g['h'], self.N)
        return sum(self.shell[n]*self.sqrt_norm[n]*P[n] for n in range(self.N))
    def __call__(self, y):
        g = self.g
        sgn = 1
        if y < 0:
            y = -y; sgn = self.eps
        if y >= g['b9']:
            return mp.mpf(0)
        if y < g['a8']:
            return sgn*self.core(y)
        return sgn*self.shell_val(y)

def h_gamma(psi, x, g):
    """H_Gamma psi (x) fuer 0 < x < a8, mit Breakpoints der Sprungstellen von psi."""
    a8, b9 = g['a8'], g['b9']
    px = psi(x)
    bps = sorted(set([a8-x, x, a8+x, b9-x, b9+x]))
    def f(r):
        if r <= 0:
            return mp.mpf(0)   # k ~ 1/(2r), Klammer O(r^2) im Kerninneren
        return k_gamma(r)*(2*px - psi(x+r) - psi(x-r))
    total = mp.quad(f, [0]+bps)
    # Rest r > b9+x: psi(x+-r) = 0
    total += 2*px*mp.quad(k_gamma, [b9+x, mp.inf])
    return total

def s_shift(psi, x, g):
    return sum(w*(psi(x+lq) + psi(x-lq)) for q, w, lq in g['shifts'])

def q_raw(psi, x, g):
    return h_gamma(psi, x, g) - g['kappa']*psi(x) - s_shift(psi, x, g)

def interior_breakpoints(g):
    """Sprungstellen von S psi im Kern: x +- log q trifft +-a8 oder +-b9."""
    a8, b9 = g['a8'], g['b9']
    pts = set()
    for q, w, lq in g['shifts']:
        for wall in [a8, b9]:
            for cand in [wall-lq, lq-wall, lq+wall, -wall-lq]:
                if 0 < cand < a8 and abs(cand-a8) > mp.mpf(10)**-20:
                    pts.add(cand)
    return sorted(pts)

def gauss_nodes(n):
    import mpmath.calculus.quadrature as Qd
    gl = Qd.GaussLegendre(mp.mp)
    # degree d -> 3*2^(d-1) nodes
    d = 1
    while 3*2**(d-1) < n: d += 1
    return gl.calc_nodes(d, mp.mp.prec)

def mesh(g, interior, n_per_cell=12, grade_levels=28):
    """Zellen zwischen Breakpoints; letzte Zelle zu a8 hin geometrisch verfeinert (log-Singularitaet)."""
    a8 = g['a8']
    pts = [mp.mpf(0)] + interior + [a8]
    cells = []
    for i in range(len(pts)-1):
        lo, hi = pts[i], pts[i+1]
        if i == len(pts)-2:
            # geometrische Verfeinerung Richtung a8
            L = hi-lo
            edges = [lo] + [hi - L*mp.mpf(2)**(-j) for j in range(1, grade_levels+1)]
            for j in range(len(edges)-1):
                cells.append((edges[j], edges[j+1]))
            cells.append((edges[-1], hi))
        else:
            cells.append((lo, hi))
    nodes = gauss_nodes(n_per_cell)
    out = []
    for lo, hi in cells:
        mid, half = (lo+hi)/2, (hi-lo)/2
        for s, w in nodes:
            out.append((mid+half*s, half*w))
    return out, cells
