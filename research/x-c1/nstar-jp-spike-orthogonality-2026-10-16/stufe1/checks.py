import json
from fractions import Fraction as Fr
import mpmath as mp
from shell_chi import *
mp.mp.dps = 40
dirs = json.load(open(PKG/'expected/DIRECTIONS.json'))
half = json.load(open(HALF))
# (a) p vs v: exakter Winkel
for par in ['even','odd']:
    v=[Fr(x) for x in dirs[par]['directions']['upper_v']['t_exact_rational']]
    p=[Fr(x) for x in dirs[par]['directions']['lower_Pv']['t_exact_rational']]
    vv=sum(x*x for x in v); pp=sum(x*x for x in p); vp=sum(x*y for x,y in zip(v,p))
    cos2 = vp*vp/(vv*pp)
    q=Fr(dirs[par]['q'])
    print(par,'1-cos^2(v,p)=%.3e'%float(1-cos2),' q=%.6f'%float(q),' |p|=%.6f'%mp.sqrt(mpf_of(pp)), ' ||p - q v||/||p|| = %.3e'%float(mp.sqrt(mpf_of(sum((pi-q*vi)**2 for pi,vi in zip(p,v))/pp))))
# (b) Q-Isometrie in W_X mit meinen lambda-Integralen: ||q_i||_X^2 + 2 lambda(q_i)^2/mu == 1 ?
for idx,par in enumerate(['even','odd']):
    sigma=idx; m=m_of(sigma)
    mu=(a8/2+mp.sinh(a8)/2) if sigma==0 else (-a8/2+mp.sinh(a8)/2)
    lam_ell=[mp.quad(lambda x,n=n: m(x)*ell(n,x),[a8,b9]) for n in range(N)]
    # zweite Methode: Gauss-Legendre
    lam_ell2=[mp.quad(lambda x,n=n: m(x)*ell(n,x),[a8,c,b9],method='gauss-legendre') for n in range(N)]
    print(par,'max |lam_ell tanh-sinh - gauss-legendre| =', mp.nstr(max(abs(a-b) for a,b in zip(lam_ell,lam_ell2)),3))
    qbox=half['blocks'][idx]['basis_Q_local_coefficients']
    Qmid=[[mpf_of((Fr(a)+Fr(b))/2) for a,b in row] for row in qbox]
    worst=0; worst_off=0
    cols=[[Qmid[n][i] for n in range(N)] for i in range(92)]
    lamq=[sum(cols[i][n]*lam_ell[n] for n in range(N)) for i in range(92)]
    for i in range(92):
        wx=sum(x*x for x in cols[i])+2*lamq[i]**2/mu
        worst=max(worst,abs(wx-1))
    for i in range(0,92,7):
        for j in range(i+1,92,11):
            off=sum(x*y for x,y in zip(cols[i],cols[j]))+2*lamq[i]*lamq[j]/mu
            worst_off=max(worst_off,abs(off))
    print(par,'Q*W_X Q - I: max diag dev =',mp.nstr(worst,3),' sampled offdiag max =',mp.nstr(worst_off,3))
    # (c) z_n Schalenkoeffizienten: zweite Methode ueber Polynomalgebra (Legendre-Rekursion in s-Variable, exakte Gauss-Quadratur 12 Knoten)
    degs=[sigma+2,sigma+4,sigma+6,sigma+8]
    def mom(n): return mp.quad(lambda x: m(x)*eb(n,x),[0,b9])
    def mom2(n): return mp.quad(lambda x: m(x)*eb(n,x),[0,b9/2,b9],method='gauss-legendre')
    print(par,'moment check max dev:', mp.nstr(max(abs(mom(n)-mom2(n)) for n in degs+[sigma]),3))
    # Gauss-Legendre 12 Knoten exakt fuer Grad<=23 in s
    import mpmath.calculus.quadrature as Qd
    gl=Qd.GaussLegendre(mp.mp)
    nodes=gl.calc_nodes(3, mp.mp.prec)  # degree 3 -> 3*2^(3-1)=12 Knoten auf [-1,1]
    for n in degs:
        ratio=mom(n)/mom(sigma)
        for k in range(10):
            s1=2*mp.quad(lambda x: (eb(n,x)-eb(sigma,x)*ratio)*ell(k,x),[a8,b9])
            s2=2*(h/2)*sum(w*((eb(n,c+h*s/2)-eb(sigma,c+h*s/2)*ratio)*ell(k,c+h*s/2)) for s,w in nodes)
            assert abs(s1-s2)<mp.mpf(10)**-30,(n,k,s1,s2)
    print(par,'z_n shell coefficients: quad vs 12-node Gauss agree to 1e-30')
