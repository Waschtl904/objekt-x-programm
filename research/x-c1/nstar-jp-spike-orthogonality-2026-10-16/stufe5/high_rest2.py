"""Hoher Rest r_v(h) = (1/delta)<y_f - B*c_v, y_h> fuer h = Pi_a(c_tilde - Dhat T z0) mit NEU ausgewerteter Funktion
A8(Phi c_v) auf einem an h angepassten Netz (alle Schnittstellen von c_tilde, Dhat und den a8-Verschiebungen; graded zu a8).
Die gespeicherte A8PHIC-Funktion (Teil 2) liegt auf einem Netz ohne die c_tilde-Schnittstellen und ist fuer h unbrauchbar.
Diagnose (Mittelpunkte); Vergleichswert: zertifizierter Faktor H_hi,v mal ||y_h||."""
import sys, json, gzip, glob, time
from fractions import Fraction as Fr
from pathlib import Path
import mpmath as mp
sys.path.insert(0, '/home/user/workspace/stufe4'); sys.path.insert(0, '/home/user/workspace/stufe5')
from a8_operator import setup, LegPoly, q_action, legendre_all
import mpmath.calculus.quadrature as Qd
HERE = Path('/home/user/workspace/stufe5')
Z3 = glob.glob('/home/user/workspace/zip3/Objekt-X-Stufe3*')[0]
Z5 = '/home/user/workspace/zip5/stage4-high-certificate-2026-10-16/inputs/a8_model.json.gz'
def toq(s): q = Fr(s); return mp.mpf(q.numerator)/mp.mpf(q.denominator)
def mid(iv): return (toq(iv[0])+toq(iv[1]))/2

def main(par, nodes_per_cell=24):
    sigma = 0 if par == 'even' else 1; eps = (-1)**sigma
    g = setup(50); a8 = g['a8']; a = mp.log(3); b = mp.log(11)/2
    FA = json.load(open(Z3+'/expected/FINITE_ACTION.json'))
    common = json.loads(gzip.decompress(open(Z3+'/inputs/REFINED_COMMON96.json.gz', 'rb').read()))
    a8m = json.loads(gzip.decompress(open(Z5, 'rb').read())); SC = mp.mpf(10)**a8m['scale_digits']
    co = common['cases'][sigma]; delta = toq(co['delta'])
    d = FA[par]['directions']['upper_v']; c = [mid(x) for x in d['c_model']]
    n = 191; degs = list(range(sigma+2, sigma+383, 2))
    m = (lambda x: mp.cosh(x/2)) if sigma == 0 else (lambda x: mp.sinh(x/2))
    mu8 = a8/2+mp.sinh(a8)/2 if sigma == 0 else -a8/2+mp.sinh(a8)/2
    mu = (mp.mpf(4)/3 + eps*a)/2
    m_s = lambda s: m(a8*s)
    me = {k: mp.quad(lambda s, k=k: m_s(s)*mp.sqrt(2*k+1)*mp.legendre(k, s), [-1, 1])/2 for k in degs+[sigma]}
    gamma_m = (mp.quad(lambda s: m_s(s)**2, [-1, 1])/2)/me[sigma]**2
    beta = {k: me[k]/me[sigma] for k in degs}
    coef = [mp.mpf(0)]*(sigma+384)
    for i, k in enumerate(degs): coef[k] += c[i]*mp.sqrt(2*k+1)
    coef[sigma] += -mp.sqrt(2*sigma+1)*sum(c[i]*beta[k] for i, k in enumerate(degs))
    poly = LegPoly(coef); dh = [g['H'][k]*cc for k, cc in enumerate(coef)]
    A = a8m['parities'][par]['A']
    Amid = [[(mp.mpf(int(A[i][j][0]))+mp.mpf(int(A[i][j][1])))/2/SC for j in range(n)] for i in range(n)]
    Ac = [sum(Amid[i][j]*c[j] for j in range(n)) for i in range(n)]
    # Netz: a8-Verschiebungen, Dhat-Schnitte, c_tilde-Schnitte; graded zu a8
    L = {q: mp.log(q) for q in [2, 3, 4, 5, 7, 8]}
    cuts_c = [a-L[2], b-L[2], b-a] + [L[q]-a for q in (4, 5, 7, 8)] + [L[q]-b for q in (4, 5, 7, 8)] + [2*a-b]
    bps = sorted(set([L[3]-a8, a8-L[2], L[5]-a8, L[7]-a8, L[4]-a, a-L[2], L[5]-a, L[7]-a, L[8]-a] + cuts_c))
    bps = [x for x in bps if 0 < x < a8]
    edges = [mp.mpf(0)] + bps
    last = bps[-1]; hh_ = a8-last
    edges += [a8 - hh_*mp.mpf(2)**(-k) for k in range(1, 25)] + [a8]
    gl = Qd.GaussLegendre(mp.mp).calc_nodes({24: 4, 48: 5, 96: 6}[nodes_per_cell], mp.mp.prec)
    X, W = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        md, hf = (lo+hi)/2, (hi-lo)/2
        for s, w in gl: X.append(md+hf*s); W.append(hf*w)
    print(par, 'Netz', len(edges)-1, 'Zellen', len(X), 'Knoten', flush=True)
    t0 = time.time(); QP = []
    for i, x in enumerate(X):
        QP.append(q_action(poly, x/a8, g, dh))
        if i % 100 == 0: print(par, 'Knoten', i, len(X), '%.0fs' % (time.time()-t0), flush=True)
    kappa_c = sum(w*m(x)*q for w, x, q in zip(W, X, QP))/mu8
    A8c = [(q - kappa_c*m(x))/mp.sqrt(2*a8) for q, x in zip(QP, X)]
    a_c = mp.sqrt(2*mp.mpf(2*sigma+1)/a8)*sum(w*mp.legendre(sigma, x/a8)*v for w, x, v in zip(W, X, A8c))
    json.dump({'X': [mp.nstr(x, 45) for x in X], 'W': [mp.nstr(w, 45) for w in W], 'A8c': [mp.nstr(v, 40) for v in A8c], 'kappa_c': mp.nstr(kappa_c, 40),
               'note': 'A8(Phi c_v) auf h-angepasstem Netz (Stufe 5); Mittelpunkte'}, open(HERE/f'A8PHIC_hmesh_{par}.json', 'w'))
    print(par, 'Operator fertig %.0fs' % (time.time()-t0), ' kappa_c', mp.nstr(kappa_c, 12), ' (Teil 2:', json.load(open(f'/home/user/workspace/stufe4/A8PHIC_{par}.json'))['kappa_c'][:14], ')', flush=True)
    # h auf diesem Netz (150 Stellen)
    mp.mp.dps = 150
    P = json.load(open(HERE/'L00_lower_Pv_ERSTFASSUNG.json'))[par]
    Tz0 = [mp.mpf(x) for x in P['T_z0']]
    import l00
    f12 = json.load(open(l00.F12)); funcs = f12['parities'][par]['functions']
    logs = {2: mp.log(2), 3: mp.log(3), 4: 2*mp.log(2), 5: mp.log(5), 7: mp.log(7), 8: 3*mp.log(2), 9: 2*mp.log(3)}
    CH = [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3)]
    wq = {q: mp.log(pr)/mp.sqrt(q) for q, pr in CH}
    B = mp.mpf(P['z0']['B']); Ac_ = mp.mpf(P['z0']['A_c'])
    def u_lift(y):
        if -a < y < a: return Ac_*m(y)
        if a < y < b: return B
        if -b < y < -a: return eps*B
        return mp.mpf(0)
    def Theta(r): v = mp.exp(-r/2); return mp.atanh(v) + mp.atan(v)
    def Jp(R): return 3*mp.log(2)/2 + mp.pi/4 - R - mp.log(1-mp.exp(-2*R))/2
    def Jm(R): v = mp.exp(-R); return mp.log(2)/2 + mp.pi/4 - mp.log((1-v)/(1+v))/2
    def Msig(x): ep = mp.exp(x/2); return (ep*(Jp(a-x)+Jm(a+x)) + eps/ep*(Jm(a-x)+Jp(a+x)))/2
    def Tsig(x): return Theta(a-x) - Theta(b-x) + eps*(Theta(a+x) - Theta(b+x))
    def ctilde(x): return Ac_*Msig(x) - B*Tsig(x) - sum(wq[q]*(u_lift(x+logs[q]) + u_lift(x-logs[q])) for q, _ in CH)
    Dspecs = []
    for row in funcs:
        D = row['D']
        polyD = [toq(x) for x in D['polynomial']]; vm = [toq(x) for x in D['V_multiplier']]; mm = toq(D['moment_multiplier'])
        shifts = []
        for term in D['shift_terms']:
            q = int(term['channel']); sgn = int(term['translation_sign']); sh = logs[q]/a
            lo, hi_ = ((mp.mpf(0), 1-sh) if sgn == 1 else ((mp.mpf(0) if q in (2, 3) else sh-1), mp.mpf(1)))
            shifts.append((lo, hi_, [toq(x) for x in term['polynomial']]))
        Dspecs.append((polyD, vm, mm, shifts))
    def Dval(j, x):
        polyD, vm, mm, shifts = Dspecs[j]; t = x/a
        v = mp.polyval(polyD[::-1], t) + mp.polyval(vm[::-1], t)*(-mp.log(1-t*t)/2) + mm*m(x)
        for lo, hi_, pc in shifts:
            if lo < t < hi_: v += mp.polyval(pc[::-1], t)
        return v/mp.sqrt(2*a)
    mom_a = mp.mpf(P['moment_r_tilde'])
    Xh = [mp.mpf(x) for x in [mp.nstr(x, 45) for x in X]]
    H = [ctilde(x) - sum(Tz0[i]*Dval(i, x) for i in range(12)) - m(x)*mom_a/mu for x in Xh]
    mom8 = sum(w*m(x)*hh for w, x, hh in zip(W, Xh, H))
    H8 = [hh - m(x)*mom8/mu8 for hh, x in zip(H, Xh)]
    norm_h8 = mp.sqrt(2*sum(w*x*x for w, x in zip(W, H8)))
    phih = [mp.mpf(x) for x in P['Phi_star_h8']]; a_h = mp.mpf(P['a_h'])
    # Kontrolle: a_h und einige Phi*h8-Koordinaten (k<=30) aus diesem Netz
    Pn = [legendre_all(x/a8, 32) for x in Xh]
    a_h_here = mp.sqrt(2*mp.mpf(2*sigma+1)/a8)*sum(w*P_[sigma]*v for w, P_, v in zip(W, Pn, H8))
    lowk = [k for k in degs if k <= 30]
    coords_here = {k: mp.sqrt(2*mp.mpf(2*k+1)/a8)*sum(w*P_[k]*v for w, P_, v in zip(W, Pn, H8)) - beta[k]*a_h_here for k in lowk}
    maxrel = max(abs(coords_here[k]-phih[degs.index(k)])/abs(phih[degs.index(k)]) for k in lowk)
    yh2 = norm_h8**2 + gamma_m*a_h**2 - sum(p*p for p in phih)
    assert yh2 > 0
    norm_yh = mp.sqrt(yh2)
    A8c_h8 = 2*sum(w*v*hh for w, v, hh in zip(W, A8c, H8))
    Bc_yh = A8c_h8 + gamma_m*a_c*a_h - sum(x*y for x, y in zip(Ac, phih))
    yf_yh = mp.mpf(P['pairing_upper_v']['bracket/delta'])*delta
    r = (yf_yh - Bc_yh)/delta
    hi = json.load(open(l00.Z5))[par]['directions']
    Hhi = toq(hi['upper_v']['whole_physical_high_U8_part_norm_upper'][1]); Hhie = toq(hi['orthogonal_difference']['whole_physical_high_U8_part_norm_upper'][1])
    Hhip = toq(hi['lower_Pv']['whole_physical_high_U8_part_norm_upper'][1])
    D_ = json.load(open(glob.glob('/home/user/workspace/nstar/*/expected/DIRECTIONS.json')[0]))[par]['directions']
    v_ = [toq(x) for x in D_['upper_v']['t_exact_rational']]; p_ = [toq(x) for x in D_['lower_Pv']['t_exact_rational']]
    alpha = sum(x*y for x, y in zip(p_, v_))/sum(x*x for x in v_)
    I0 = mp.mpf(P['pairing_lower_Pv']['<psi,h>']) - mp.mpf(P['pairing_lower_Pv']['<c,Phi*h8>'])
    res = {'mesh_cells': len(edges)-1, 'nodes_per_cell': nodes_per_cell, 'norm_h8_this_mesh': mp.nstr(norm_h8, 12), 'norm_h8_L00_mesh': P['norm_h8'],
           'a_h_this_mesh_vs_L00_reldiff': mp.nstr(abs(a_h_here-a_h)/abs(a_h), 3), 'Phi_star_h8_k<=30_maxreldiff': mp.nstr(maxrel, 3),
           'norm_y_h': mp.nstr(norm_yh, 12), 'kappa_c': mp.nstr(kappa_c, 15), 'a_A8Phic': mp.nstr(a_c, 15),
           '<y_f,y_h>/delta': mp.nstr(yf_yh/delta, 15), '<B*c_v,y_h>/delta': mp.nstr(Bc_yh/delta, 15), 'r_v(h)': mp.nstr(r, 10),
           'Vergleichswert_H_hi,v*||y_h||': mp.nstr(Hhi*norm_yh, 6),
           'alpha': mp.nstr(alpha, 15), 'alpha*r_v(h)': mp.nstr(alpha*r, 10), '|r_e|<=H_hi,e*||y_h||': mp.nstr(Hhie*norm_yh, 4),
           'Vergleichswert_H_hi,p*||y_h||': mp.nstr(Hhip*norm_yh, 6),
           'I0=<psi_p,h>-<c_p,Phi*h8>': mp.nstr(I0, 12), 'L00_midpoint=I0-alpha*r_v(h)-r_e(midpoint 0)': mp.nstr(I0-alpha*r, 12)}
    print(par, res, flush=True)
    json.dump(res, open(HERE/f'HIGH_REST_{par}.json', 'w'), indent=1)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 24)
