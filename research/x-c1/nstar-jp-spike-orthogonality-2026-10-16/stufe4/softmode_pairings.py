"""Stufe-4-Gegentest: Energie-Cauchy-Schwarz fuer die weichste A8-Mode.

I_j := <Phi u1, D_j>_{H8} = 2 int_0^{a8} (Phi u1)(x) D_j(x) dx,  D_j = A9 Phi_j (FUNCTIONS12.json, #227),
Phi u1 = U^{-1} M E u1 mit u1 = Top-Links-Singulaervektor der Kongruenzmatrix C (Common96).
Vorhersage (Pullback-Vertraeglichkeit + Cauchy-Schwarz in der positiven Form):
   |I_j| = |a9[J Phi u1, Phi_j]| <= sqrt(u1^T G_head u1) * sqrt(A12_jj),   G_head = (C C^T)^{-1}.
Gleitkomma-Diagnose (mpmath 150 Stellen, Gauss-Legendre 768 Knoten je Zelle); kein Zertifikat.
"""
import json, sys, gzip, time
from fractions import Fraction as Fr
from pathlib import Path
import mpmath as mp
import mpmath.calculus.quadrature as Qd

mp.mp.dps = 150
HERE = Path(__file__).resolve().parent
Z3 = next(Path('/home/user/workspace/zip3').glob('Objekt-X-Stufe3*'))
F12 = Path('/home/user/workspace/r227/inner/objekt-x-whole-functions12-2026-10-15/FUNCTIONS12.json')
A12 = Path('/home/user/workspace/r227/inner/objekt-x-whole-functions12-2026-10-15/FRESH_A12.json')

def Q2mp(s):
    q = Fr(s); return mp.mpf(q.numerator)/mp.mpf(q.denominator)

def legendre_all(s, N):
    P = [mp.mpf(1), s]
    for n in range(1, N-1):
        P.append(((2*n+1)*s*P[n] - n*P[n-1])/(n+1))
    return P[:N]

def main():
    a8 = 3*mp.log(2)/2; a = mp.log(3)
    logs = {2: mp.log(2), 3: mp.log(3), 4: 2*mp.log(2), 5: mp.log(5), 7: mp.log(7), 8: 3*mp.log(2)}
    common = json.loads(gzip.decompress(open(Z3/'inputs/REFINED_COMMON96.json.gz', 'rb').read()))
    f12 = json.load(open(F12)); a12 = json.load(open(A12))
    gl = Qd.GaussLegendre(mp.mp)
    nodes = gl.calc_nodes(9, mp.mp.prec)   # 768 Knoten
    out = {}
    for sigma, par in enumerate(['even', 'odd']):
        t0 = time.time()
        co = common['cases'][sigma]; den = int(co['inverse_congruence_denominator'])
        C = mp.matrix([[mp.mpf(int(v))/den for v in row] for row in co['inverse_congruence_integer_matrix']])
        n = C.rows
        # u1: Potenziteration auf C C^T
        with mp.workdps(50):
            CCt = C*C.T
            u = mp.matrix([1]*n); u = u/mp.norm(u)
            for it in range(40):
                u = CCt*u; lam = mp.norm(u); u = u/lam
            s1 = mp.sqrt(lam)
            # Rayleigh-Quotient bzgl. G_head = (C C^T)^{-1}:  u^T G u = ||C^{-1} u||^2
            x = mp.lu_solve(C, u)
            rq = mp.norm(x)**2
        u1 = [mp.mpf(u[i]) for i in range(n)]
        degs = list(range(sigma+2, sigma+383, 2))
        m_s = (lambda s: mp.cosh(a8*s/2)) if sigma == 0 else (lambda s: mp.sinh(a8*s/2))
        # <m_s, e_k> = int_-1^1 m_s e_k ds / 2
        me = {k: mp.quad(lambda s, k=k: m_s(s)*mp.sqrt(2*k+1)*mp.legendre(k, s), [-1, 1])/2 for k in degs+[sigma]}
        mom_coef = sum(u1[i]*me[degs[i]] for i in range(n))/me[sigma]
        def phi_u1(x):
            s = x/a8; P = legendre_all(s, sigma+384)
            val = sum(u1[i]*mp.sqrt(2*degs[i]+1)*P[degs[i]] for i in range(n)) - mom_coef*mp.sqrt(2*sigma+1)*P[sigma]
            return val/mp.sqrt(2*a8)
        # Zellen in x auf (0,a8): Sprungstellen der D-Verschiebungsterme
        bps = sorted([logs[4]-a, a-logs[2], logs[5]-a, logs[7]-a, logs[8]-a])
        edges = [mp.mpf(0)] + bps + [a8]
        cells = list(zip(edges[:-1], edges[1:]))
        X = []; W = []
        for lo, hi in cells:
            mid, half = (lo+hi)/2, (hi-lo)/2
            for s, w in nodes:
                X.append(mid+half*s); W.append(half*w)
        PH = [phi_u1(x) for x in X]
        norm_phi2 = 2*sum(w*p*p for w, p in zip(W, PH))
        mom_phi = sum(w*(mp.cosh(x/2) if sigma == 0 else mp.sinh(x/2))*p for w, x, p in zip(W, X, PH))
        res = {'s1': mp.nstr(s1, 15), 'lambda_min_approx_1/s1^2': mp.nstr(1/s1**2, 10), 'rayleigh_u1_G_head': mp.nstr(rq, 15),
               'norm_phi_u1_H8': mp.nstr(mp.sqrt(norm_phi2), 15), 'moment_phi_u1 (soll 0)': mp.nstr(mom_phi, 3),
               'u1_top_degrees': [(degs[i], mp.nstr(u1[i], 8)) for i in sorted(range(n), key=lambda i: -abs(u1[i]))[:8]], 'pairings': []}
        funcs = f12['parities'][par]['functions']
        A = a12['parities'][par]['midpoint']
        for j, row in enumerate(funcs):
            D = row['D']
            poly = [Q2mp(c) for c in D['polynomial']]; vm = [Q2mp(c) for c in D['V_multiplier']]; mm = Q2mp(D['moment_multiplier'])
            shifts = []
            for term in D['shift_terms']:
                q = int(term['channel']); sgn = int(term['translation_sign']); sh = logs[q]/a
                if sgn == 1: lo, hi = mp.mpf(0), 1-sh
                else: lo, hi = (mp.mpf(0) if q in (2, 3) else sh-1), mp.mpf(1)
                shifts.append((lo, hi, [Q2mp(c) for c in term['polynomial']]))
            def Dval(x):
                t = x/a
                v = mp.polyval(poly[::-1], t) + mp.polyval(vm[::-1], t)*(-mp.log(1-t*t)/2) + mm*(mp.cosh(x/2) if sigma == 0 else mp.sinh(x/2))
                for lo, hi, pc in shifts:
                    if lo < t < hi: v += mp.polyval(pc[::-1], t)
                return v/mp.sqrt(2*a)
            DV = [Dval(x) for x in X]
            I = 2*sum(w*p*d for w, p, d in zip(W, PH, DV))
            normD2 = 2*sum(w*d*d for w, d in zip(W, DV))
            Ajj = Q2mp(A[j][j])
            bound = mp.sqrt(rq)*mp.sqrt(Ajj)
            # naive Erwartung ohne Energieargument: ||Phi u1|| * ||D_j|core||
            naive = mp.sqrt(norm_phi2)*mp.sqrt(normD2)
            res['pairings'].append({'j': j, 'degree': row['degree'], 'I_j': mp.nstr(I, 12), 'bound_CS': mp.nstr(bound, 6),
                                    'ratio_|I|/bound': mp.nstr(abs(I)/bound, 6), 'norm_Dj_core': mp.nstr(mp.sqrt(normD2), 8),
                                    'naive_scale': mp.nstr(naive, 6), 'A12_jj': mp.nstr(Ajj, 10), 'c_times_I (1.345e13*I)': mp.nstr(I*(mp.mpf('1.345361e13') if sigma == 0 else mp.mpf('1.022029e12')), 8)})
            print(par, j, 'deg', row['degree'], 'I_j =', mp.nstr(I, 10), ' CS-Schranke', mp.nstr(bound, 4), ' Verhaeltnis', mp.nstr(abs(I)/bound, 4), ' naiv', mp.nstr(naive, 4), ' %.0fs' % (time.time()-t0), flush=True)
        out[par] = res
        json.dump(out, open(HERE/'SOFTMODE_PAIRINGS.json', 'w'), indent=1)
    print('done')

if __name__ == '__main__':
    main()
