import sys
sys.path.insert(0,'/home/user/workspace/stufe2')
import mpmath as mp
from a8_operator import *
import qnp_psi
g = setup(30); gq = qnp_psi.setup(30)
a8 = g['a8']
for n in [2, 3, 7]:
    coef = [mp.mpf(0)]*(n+1); coef[n] = mp.mpf(1); poly = LegPoly(coef)
    dh = [g['H'][k]*c for k, c in enumerate(coef)]
    psi = lambda y: poly(y/a8)   # Paritaet automatisch durch P_n
    for x in [mp.mpf('0.2'), mp.mpf('0.7'), mp.mpf('1.0')]:
        direct = qnp_psi.h_gamma(psi, x, gq) - gq['kappa']*psi(x)
        analytic = q_action(poly, x/a8, g, dh) + shift_action(poly, x/a8, g)   # ohne S: H_Gamma - kappa
        print('n=%d x=%s  direkt=%s  analytisch=%s  diff=%s' % (n, mp.nstr(x,3), mp.nstr(direct,15), mp.nstr(analytic,15), mp.nstr(direct-analytic,3)))
