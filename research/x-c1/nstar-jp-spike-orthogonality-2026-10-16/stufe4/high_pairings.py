"""r_{v,j} = (1/delta) <y_f - B*c, y_{h,j}>  ueber die ganze Funktion A8(Phi c) am Horizont a8.

<B*c, y_h> = <T_h A8Phic, T_h h8> = <A8Phic, h8> + gamma_m a_{A8Phic} a_h - (A c).(Phi* h8)   (7.1)
A8(Phi c) = [Q^np_{a8} P_c(x/a8) - kappa_c m(x)]/sqrt(2 a8),  P_c = sum_i c_i (e_{n_i} - beta_i e_sigma).
Kontrollen: ||B*c||^2 = ||A8Phic||^2 + gamma_m a^2 - sum (Ac)_k^2  vs  c^T G0 c;
            <B*c, y_f> = <A8Phic, f> + gamma_m a a_f - (Ac).Phi*f  vs Archiv <c, B T_h f>;
            (Ac)_k aus a8_model-A vs Quadratur.
Diagnose (mpmath 50 Stellen Operator, 150 Stellen D_j-Auswertung); kein Zertifikat.
"""
import sys, json, gzip, glob, time
from fractions import Fraction as Fr
from pathlib import Path
import mpmath as mp
sys.path.insert(0, '/home/user/workspace/stufe4')
from a8_operator import setup, LegPoly, q_action, legendre_all

HERE = Path('/home/user/workspace/stufe4')
Z3 = glob.glob('/home/user/workspace/zip3/Objekt-X-Stufe3*')[0]
Z5 = '/home/user/workspace/zip5/stage4-high-certificate-2026-10-16/inputs/a8_model.json.gz'
F12 = '/home/user/workspace/r227/inner/objekt-x-whole-functions12-2026-10-15/FUNCTIONS12.json'

def toq(s):
    q = Fr(s); return mp.mpf(q.numerator)/mp.mpf(q.denominator)
def mid(iv): return (toq(iv[0])+toq(iv[1]))/2

def main(par):
    sigma = 0 if par == 'even' else 1
    g = setup(50); a8 = g['a8']; a = mp.log(3)
    FA = json.load(open(Z3+'/expected/FINITE_ACTION.json'))
    common = json.loads(gzip.decompress(open(Z3+'/inputs/REFINED_COMMON96.json.gz', 'rb').read()))
    a8m = json.loads(gzip.decompress(open(Z5, 'rb').read())); SC = mp.mpf(10)**a8m['scale_digits']
    T = json.load(open(HERE/'D12_TERMS.json'))[par]
    co = common['cases'][sigma]; delta = toq(co['delta'])
    d = FA[par]['directions']['upper_v']
    c = [mid(x) for x in d['c_model']]; phif = [mid(x) for x in d['Phi_star_f_model']]
    n = 191; degs = list(range(sigma+2, sigma+383, 2))
    m = (lambda x: mp.cosh(x/2)) if sigma == 0 else (lambda x: mp.sinh(x/2))
    mu = a8/2+mp.sinh(a8)/2 if sigma == 0 else -a8/2+mp.sinh(a8)/2
    m_s = lambda s: m(a8*s)
    me = {k: mp.quad(lambda s, k=k: m_s(s)*mp.sqrt(2*k+1)*mp.legendre(k, s), [-1, 1])/2 for k in degs+[sigma]}
    gamma_m = (mp.quad(lambda s: m_s(s)**2, [-1, 1])/2)/me[sigma]**2
    beta = {k: me[k]/me[sigma] for k in degs}
    # P_c
    coef = [mp.mpf(0)]*(sigma+384)
    for i, k in enumerate(degs): coef[k] += c[i]*mp.sqrt(2*k+1)
    coef[sigma] += -mp.sqrt(2*sigma+1)*sum(c[i]*beta[k] for i, k in enumerate(degs))
    poly = LegPoly(coef); dh = [g['H'][k]*cc for k, cc in enumerate(coef)]
    # A c aus Modellgram
    A = a8m['parities'][par]['A']
    Amid = [[(mp.mpf(int(A[i][j][0]))+mp.mpf(int(A[i][j][1])))/2/SC for j in range(n)] for i in range(n)]
    Ac = [sum(Amid[i][j]*c[j] for j in range(n)) for i in range(n)]
    G0 = a8m['parities'][par]['complete_model_raw_high_Gram']
    cG0c = sum(c[i]*c[j]*(mp.mpf(int(G0[i][j][0]))+mp.mpf(int(G0[i][j][1])))/2/SC for i in range(n) for j in range(n))
    # Netz: a8-Shift-Spruenge, b9-Spruenge (h8_j), graded zu a8
    L = {q: mp.log(q) for q in [2, 3, 4, 5, 7, 8]}
    bps = sorted(set([L[3]-a8, a8-L[2], L[5]-a8, L[7]-a8, L[4]-a, a-L[2], L[5]-a, L[7]-a, L[8]-a]))
    edges = [mp.mpf(0)] + bps
    last = bps[-1]; h = a8-last
    edges += [a8 - h*mp.mpf(2)**(-k) for k in range(1, 25)] + [a8]
    import mpmath.calculus.quadrature as Qd
    gl = Qd.GaussLegendre(mp.mp).calc_nodes(4, mp.mp.prec)  # 24 Knoten
    X, W = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        md, hf = (lo+hi)/2, (hi-lo)/2
        for s, w in gl: X.append(md+hf*s); W.append(hf*w)
    # f-Netz
    M2 = json.load(open(f'/home/user/workspace/stufe2/MESH_{par}_upper_v.json'))
    Xf = [mp.mpf(nd['x']) for nd in M2['nodes']]; Wf = [mp.mpf(nd['w']) for nd in M2['nodes']]; Qr = [mp.mpf(nd['Q_raw']) for nd in M2['nodes']]
    momf = sum(w*m(x)*q for w, x, q in zip(Wf, Xf, Qr)); fv = [q - m(x)*momf/mu for q, x in zip(Qr, Xf)]
    t0 = time.time()
    QP = []
    for i, x in enumerate(X):
        QP.append(q_action(poly, x/a8, g, dh))
        if i % 100 == 0: print(par, 'Knoten', i, len(X), '%.0fs' % (time.time()-t0), flush=True)
    QPf = [q_action(poly, x/a8, g, dh) for x in Xf]
    print(par, 'Operator fertig %.0fs' % (time.time()-t0), flush=True)
    kappa_c = sum(w*m(x)*q for w, x, q in zip(W, X, QP))/mu
    A8c = [(q - kappa_c*m(x))/mp.sqrt(2*a8) for q, x in zip(QP, X)]
    A8cf = [(q - kappa_c*m(x))/mp.sqrt(2*a8) for q, x in zip(QPf, Xf)]
    norm2 = 2*sum(w*v*v for w, v in zip(W, A8c))
    Pn = [legendre_all(x/a8, sigma+384) for x in X]
    coordsU = {k: mp.sqrt(2*mp.mpf(2*k+1)/a8)*sum(w*P[k]*v for w, P, v in zip(W, Pn, A8c)) for k in degs+[sigma]}
    a_c = coordsU[sigma]
    Ac_quad = [coordsU[k] - beta[k]*a_c for k in degs]
    Bc2 = norm2 + gamma_m*a_c**2 - sum(v*v for v in Ac)
    a_f = mp.sqrt(2*mp.mpf(2*sigma+1)/a8)*sum(w*mp.legendre(sigma, x/a8)*f for w, x, f in zip(Wf, Xf, fv))
    Bc_yf = 2*sum(w*v*f for w, v, f in zip(Wf, A8cf, fv)) + gamma_m*a_c*a_f - sum(x*y for x, y in zip(Ac, phif))
    json.dump({'X':[mp.nstr(x,45) for x in X],'W':[mp.nstr(w,45) for w in W],'A8c':[mp.nstr(v,40) for v in A8c],'Xf':[mp.nstr(x,45) for x in Xf],'A8cf':[mp.nstr(v,40) for v in A8cf],'kappa_c':mp.nstr(kappa_c,40)}, open(HERE/f'A8PHIC_{par}.json','w'))
    lowk = [k for k in degs if k <= 30]
    res = {'check_Ac_matrix_vs_quadrature_k<=30_maxreldiff': mp.nstr(max(abs(Ac[degs.index(k)]-Ac_quad[degs.index(k)])/abs(Ac[degs.index(k)]) for k in lowk), 4),
           'kappa_c': mp.nstr(kappa_c, 15), 'norm_A8Phic': mp.nstr(mp.sqrt(norm2), 15), 'a_A8Phic': mp.nstr(a_c, 15), 'gamma_m': mp.nstr(gamma_m, 15),
           'check_Ac_matrix_vs_quadrature_maxdiff': mp.nstr(max(abs(x-y) for x, y in zip(Ac, Ac_quad)), 4), 'Ac_norm': mp.nstr(mp.sqrt(sum(v*v for v in Ac)), 12),
           'check_||B*c||^2_from_function': mp.nstr(Bc2, 15), 'check_cT_G0_c': mp.nstr(cG0c, 15),
           'check_<B*c,y_f>_from_function': mp.nstr(Bc_yf, 15), 'archive_<c,B_Th_f>': mp.nstr(sum(x*y for x, y in zip(c, [mid(v) for v in d['B_Th_f_model']])), 15),
           'rows': []}
    print(par, {k: v for k, v in res.items() if k != 'rows'}, flush=True)
    # D_j
    mp.mp.dps = 150
    f12 = json.load(open(F12)); funcs = f12['parities'][par]['functions']
    LA = {q: mp.log(q)/a for q in [2, 3, 4, 5, 7, 8]}
    for j, row in enumerate(funcs):
        D = row['D']; polyD = [toq(x) for x in D['polynomial']]; vm = [toq(x) for x in D['V_multiplier']]; mmul = toq(D['moment_multiplier'])
        shifts = []
        for term in D['shift_terms']:
            q = int(term['channel']); sgn = int(term['translation_sign']); sh = LA[q]
            lo, hi = ((mp.mpf(0), 1-sh) if sgn == 1 else ((mp.mpf(0) if q in (2, 3) else sh-1), mp.mpf(1)))
            shifts.append((lo, hi, [toq(x) for x in term['polynomial']]))
        def Dval(x):
            t = x/a
            v = mp.polyval(polyD[::-1], t) + mp.polyval(vm[::-1], t)*(-mp.log(1-t*t)/2) + mmul*m(x)
            for lo, hi, pc in shifts:
                if lo < t < hi: v += mp.polyval(pc[::-1], t)
            return v/mp.sqrt(2*a)
        DC = [Dval(x) for x in X]
        momD = sum(w*m(x)*dd for w, x, dd in zip(W, X, DC)); h8 = [dd - m(x)*momD/mu for dd, x in zip(DC, X)]
        with mp.workdps(50):
            a_h = mp.mpf(T['rows'][j]['a_h']); phih = [mp.mpf(q) for q in T['rows'][j]['Phi_star_h8_j']]   # 384-Knoten-Werte, 150 Stellen
            momD_ref = None
            A8c_h8 = 2*sum(w*v*hh for w, v, hh in zip(W, A8c, h8))
            Bc_yh = A8c_h8 + gamma_m*a_c*a_h - sum(x*y for x, y in zip(Ac, phih))
            bracket = mp.mpf(T['rows'][j]['bracket/delta'])   # <y_f,y_h>/delta
            r = bracket - Bc_yh/delta
            core = mp.mpf(T['rows'][j]['<psi_v,D_j>']) - mp.mpf(T['rows'][j]['<c,Phi*h8_j>'])
            ell = core - r
            yh2 = 2*sum(w*hh*hh for w, hh in zip(W, h8)) + gamma_m*a_h**2 - sum(p*p for p in phih)
            rr = {'j': j, 'degree': row['degree'], '<y_f,y_h>/delta': mp.nstr(bracket, 12), '<B*c,y_h>/delta': mp.nstr(Bc_yh/delta, 12),
                  'r_vj': mp.nstr(r, 10), 'Klammer <psi,D>-<c,Phi*h8>': mp.nstr(core, 10), 'ell_v(D_j) Mittelpunkt': mp.nstr(ell, 10),
                  'norm_y_h': mp.nstr(mp.sqrt(abs(yh2)), 8), 'norm_h8 vs D12_TERMS reldiff': mp.nstr(abs(mp.sqrt(2*sum(w*hh*hh for w, hh in zip(W, h8)))-mp.mpf(T['rows'][j]['norm_h8_j']))/mp.mpf(T['rows'][j]['norm_h8_j']), 3), 'cert_bound_|r|<=0.0159*gamma^-1/2*norm_y_h': mp.nstr((mp.mpf('0.0159163') if sigma==0 else mp.mpf('0.00244487'))*mp.sqrt(abs(yh2)), 4)}
        res['rows'].append(rr); print(par, rr, flush=True)
        json.dump(res, open(HERE/f'HIGH_PAIRINGS_{par}.json', 'w'), indent=1)
    print(par, 'done %.0fs' % (time.time()-t0))

if __name__ == '__main__':
    main(sys.argv[1])
