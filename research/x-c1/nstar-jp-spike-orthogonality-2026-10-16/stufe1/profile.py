import json
import mpmath as mp
from shell_chi import *
mp.mp.dps = 30
R=json.load(open('STUFE1_SHELL_RESULTS.json'))
dirs = json.load(open(PKG/'expected/DIRECTIONS.json'))
for idx,par in enumerate(['even','odd']):
    sigma=idx; m=m_of(sigma)
    D=R[par]['directions']['upper_v']
    co=[mp.mpf(x) for x in D['chi_shell_coefficients_mid']]
    f=lambda x: sum(co[n]*ell(n,x) for n in range(N))
    print(par,'upper_v  Schalenfunktion chi_v|(a8,b9):')
    for frac in [0,0.01,0.05,0.1,0.25,0.5,0.75,0.9,0.95,0.99,1.0]:
        x=a8+frac*h; print('   x=a8+%.2f h: chi=%s'%(frac, mp.nstr(f(x),8)))
    # Kernpolynomteil -sum k_i z_i auf (0,a8) pointwise
    kmid=[mp.mpf(x) for x in D['k_mid']]
    degs=[sigma+2,sigma+4,sigma+6,sigma+8]
    def mom(n): return mp.quad(lambda x: m(x)*eb(n,x),[0,b9])
    ratios=[mom(n)/mom(sigma) for n in degs]
    P=lambda x: -sum(kmid[i]*(eb(degs[i],x)-eb(sigma,x)*ratios[i]) for i in range(4))
    print('   Kernpolynomteil -sum_{i<=4} k_i z_i (ohne u) auf (0,a8):')
    for frac in [0,0.25,0.5,0.75,0.9,1.0]:
        x=frac*a8; print('   x=%.2f a8: %s'%(frac, mp.nstr(P(x),8)))
    print('   an der Wand: -sum k_i z_i(a8) =',mp.nstr(P(a8),8),'  Schalenwert chi(a8+) =',mp.nstr(f(a8),8), ' r(a8+)=',mp.nstr(sum(mp.mpf(dirs[par]['directions']['upper_v']['Jt_local_orthonormal_Legendre_coefficients_interval'][n][0].split('/')[0])/mp.mpf(dirs[par]['directions']['upper_v']['Jt_local_orthonormal_Legendre_coefficients_interval'][n][0].split('/')[1])*ell(n,a8) for n in range(N)),6))
    # Anteil der Y-Kombination auf der Schale
    print('   ||Fk_z||=%s ||Fk_Y||=%s ||chi_shell||=%s'%(mp.nstr(mp.mpf(D['shell_Fk_z_part_X_norm']),8),mp.nstr(mp.mpf(D['shell_Fk_Y_part_X_norm']),8),mp.nstr(mp.mpf(D['shell_chi_X_norm']),8)))
