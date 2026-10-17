"""Stufe 5 (Teil 1): Mittelpunkt von L_{0,0} = <chi_p(k0), h>,  h = Pi_a (c_tilde - Dhat T z0),
fuer die exakt W-normierte konstante Schalenrichtung z0 auf (log3, log11/2).

Zerlegung wie Stufe 4 (HERLEITUNG (7.2) des Hochantwort-Pakets), mit D_j -> h und v -> p:
  <chi_p, h> = I0 - r_p,   I0 = <psi_p, h> - <c_p, Phi*h8>,
  r_p = (1/delta) <y_f - B*c, y_h>  (hoher Rest; |r_p| <= H_hi,p * ||y_h||; <y_f,y_h>/delta wird mit ausgegeben,
  ist aber nur ein Teil von r_p -- die Erstfassung dieses Skripts zog ihn faelschlich allein vom Mittelpunkt ab),
  h8 = Pi8 (h|(0,a8)).
Alle Werte sind Quadratur-Mittelpunkte (mpmath, 150 Stellen fuer Modellfunktionen); KEIN gerichtetes Intervall.
Eingaben: FUNCTIONS12.json (D-, F-Modelle), FROZEN_RESPONSE12.json (X), FINITE_ACTION.json (c_p, Phi*f_p),
PSI_DEFINITION.json (psi_p), MESH_{par}_lower_Pv.json (f_p auf Stufe-2-Netz), CP_Z0_SOURCE.json (Kontrolle c_tilde).
"""
import json, gzip, time, sys, os
from fractions import Fraction as Fr
from pathlib import Path
import mpmath as mp
import mpmath.calculus.quadrature as Qd

mp.mp.dps = 150
HERE = Path(__file__).resolve().parent
Z3 = next(Path('/home/user/workspace/zip3').glob('Objekt-X-Stufe3*'))
F12 = Path('/home/user/workspace/r227/inner/objekt-x-whole-functions12-2026-10-15/FUNCTIONS12.json')
FR12 = Path('/home/user/workspace/r227/Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15/inputs/FROZEN_RESPONSE12.json')
PSI = Path('/home/user/workspace/stufe1/PSI_DEFINITION.json')
MESH = Path('/home/user/workspace/stufe2')
CPZ0 = Path('/home/user/workspace/zip8/cp-z0-source/expected/CP_Z0_SOURCE.json')
Z5 = Path('/home/user/workspace/zip5/replay5/COMPLETE_HIGH_RESPONSE.json')

def Q2mp(s):
    q = Fr(s); return mp.mpf(q.numerator)/mp.mpf(q.denominator)
def mid(iv):
    return (Q2mp(iv[0])+Q2mp(iv[1]))/2
def legendre_all(s, N):
    P = [mp.mpf(1), s]
    for n in range(1, N-1):
        P.append(((2*n+1)*s*P[n] - n*P[n-1])/(n+1))
    return P[:N]
def gl_cells(edges, nodes):
    X, W = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        md, hf = (lo+hi)/2, (hi-lo)/2
        for s, w in nodes: X.append(md+hf*s); W.append(hf*w)
    return X, W

def main(direction='lower_Pv', pars=('even', 'odd')):
    a8 = 3*mp.log(2)/2; a = mp.log(3); b = mp.log(11)/2; hsh = b-a; h89 = a-a8; cc = (a8+a)/2
    logs = {2: mp.log(2), 3: mp.log(3), 4: 2*mp.log(2), 5: mp.log(5), 7: mp.log(7), 8: 3*mp.log(2), 9: 2*mp.log(3)}
    CH = [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3)]
    wq = {q: mp.log(pr)/mp.sqrt(q) for q, pr in CH}
    common = json.loads(gzip.decompress(open(Z3/'inputs/REFINED_COMMON96.json.gz', 'rb').read()))
    FA = json.load(open(Z3/'expected/FINITE_ACTION.json'))
    f12 = json.load(open(F12)); fr12 = json.load(open(FR12)); psiD = json.load(open(PSI)); cpz = json.load(open(CPZ0))
    hi = json.load(open(Z5))
    gl = Qd.GaussLegendre(mp.mp)
    nodes = gl.calc_nodes(8, mp.mp.prec)   # 384 Knoten
    out = {}
    for par in pars:
        sigma = 0 if par == 'even' else 1
        t0 = time.time(); eps = (-1)**sigma
        co = common['cases'][sigma]
        delta = Q2mp(co['delta']); rho = Q2mp(co['rho'])
        m = (lambda x: mp.cosh(x/2)) if sigma == 0 else (lambda x: mp.sinh(x/2))
        mu8 = a8/2+mp.sinh(a8)/2 if sigma == 0 else -a8/2+mp.sinh(a8)/2          # int_0^a8 m^2
        mu = (mp.mpf(4)/3 + eps*a)/2                                               # int_0^a m^2  (exakt, K_P-Paket)
        # ---------- z0 (exakt W-normiert), Lift u
        ea, eb = mp.sqrt(3), mp.mpf(11)**mp.mpf('0.25')
        L = (eb - eps/eb) - (ea - eps/ea)                                          # int_a^b m
        B = 1/mp.sqrt(2*(hsh + L*L/mu)); Ac = -B*L/mu
        assert abs(2*B*B*(hsh+L*L/mu) - 1) < mp.mpf(10)**-140 and abs(Ac*mu + B*L) < mp.mpf(10)**-140
        def u_lift(y):
            if -a < y < a: return Ac*m(y)
            if a < y < b: return B
            if -b < y < -a: return eps*B
            return mp.mpf(0)
        # ---------- elementare Quelle c_tilde (993619be..., Formeln (2.1)-(4.1))
        def Theta(r): v = mp.exp(-r/2); return mp.atanh(v) + mp.atan(v)
        def Jp(R): return 3*mp.log(2)/2 + mp.pi/4 - R - mp.log(1-mp.exp(-2*R))/2
        def Jm(R): v = mp.exp(-R); return mp.log(2)/2 + mp.pi/4 - mp.log((1-v)/(1+v))/2
        def Msig(x):
            ep = mp.exp(x/2)
            return (ep*(Jp(a-x)+Jm(a+x)) + eps/ep*(Jm(a-x)+Jp(a+x)))/2
        def Tsig(x): return Theta(a-x) - Theta(b-x) + eps*(Theta(a+x) - Theta(b+x))
        def ctilde(x):
            return Ac*Msig(x) - B*Tsig(x) - sum(wq[q]*(u_lift(x+logs[q]) + u_lift(x-logs[q])) for q, _ in CH)
        # Kontrolle gegen 13 zertifizierte Zellmittelpunkte
        cp = cpz['parities'][par]
        devmax = mp.mpf(0)
        for cell in cp['cell_midpoints']:
            x = mid(cell['x']); ref = mid(cell['raw_source'] if 'raw_source' in cell else cell['value'])
            devmax = max(devmax, abs(ctilde(x) - ref))
        gA = mid(cp['log_coefficient_at_a']); gmine = (B - Ac*m(a))/2
        print(par, 'c_tilde Kontrolle: max|Abw.| an 13 Zellmittelpunkten =', mp.nstr(devmax, 3), ' g(a) Abw. =', mp.nstr(abs(gA-gmine), 3), flush=True)
        assert devmax < mp.mpf(10)**-60
        # ---------- F_hat z0 und T z0
        funcs = f12['parities'][par]['functions']
        Fspecs = [([Q2mp(c) for c in fj['F']['polynomial']][::-1], [Q2mp(c) for c in fj['F']['log_ratio_multiplier']][::-1],
                   Q2mp(fj['F']['raw_moment_multiplier'])) for fj in funcs]
        def fraw(j, y):
            pc, lc, mc = Fspecs[j]; v = y/a
            return (mp.polyval(pc, v) + mp.polyval(lc, v)*mp.log((v+1)/(v-1)) + mc*m(y))/mp.sqrt(2*a)
        sedgesF = [a] + [a + hsh*mp.mpf(2)**(-k) for k in range(30, 0, -1)] + [b]
        XF, WF = gl_cells(sedgesF, nodes)
        Fz0 = [2*B*sum(w*fraw(j, y) for w, y in zip(WF, XF)) for j in range(12)]
        X = [[Q2mp(x) for x in row] for row in fr12['parities'][par]['X']]
        Tz0 = [sum(X[i][j]*Fz0[j] for j in range(12)) for i in range(12)]
        print(par, 'F_hat z0 =', [mp.nstr(x, 8) for x in Fz0], flush=True)
        print(par, 'T z0 =', [mp.nstr(x, 8) for x in Tz0], ' |Tz0| =', mp.nstr(mp.sqrt(sum(x*x for x in Tz0)), 8), flush=True)
        # ---------- D-Modelle
        Dspecs = []
        for row in funcs:
            D = row['D']
            poly = [Q2mp(x) for x in D['polynomial']]; vm = [Q2mp(x) for x in D['V_multiplier']]; mm = Q2mp(D['moment_multiplier'])
            shifts = []
            for term in D['shift_terms']:
                q = int(term['channel']); sgn = int(term['translation_sign']); sh = logs[q]/a
                lo, hi_ = ((mp.mpf(0), 1-sh) if sgn == 1 else ((mp.mpf(0) if q in (2, 3) else sh-1), mp.mpf(1)))
                shifts.append((lo, hi_, [Q2mp(x) for x in term['polynomial']]))
            Dspecs.append((poly, vm, mm, shifts))
        def Dval(j, x):
            poly, vm, mm, shifts = Dspecs[j]; t = x/a
            v = mp.polyval(poly[::-1], t) + mp.polyval(vm[::-1], t)*(-mp.log(1-t*t)/2) + mm*m(x)
            for lo, hi_, pc in shifts:
                if lo < t < hi_: v += mp.polyval(pc[::-1], t)
            return v/mp.sqrt(2*a)
        def DTz0(x): return sum(Tz0[i]*Dval(i, x) for i in range(12))
        # ---------- Netze: Kern (0,a8) mit allen Schnittstellen, Schale (a8,a) geometrisch zu a
        cuts = [a-logs[2], b-logs[2], b-a] + [logs[q]-a for q in (4, 5, 7, 8)] + [logs[q]-b for q in (4, 5, 7, 8)] + [2*a-b]
        bps = sorted(set([mp.mpf(0)] + cuts + [a8]))
        assert all(0 < c_ < a8 for c_ in cuts)
        Xc, Wc = gl_cells(bps, nodes)
        sedges = [a8] + [a - h89*mp.mpf(2)**(-k) for k in range(1, 40)] + [a]
        Xs, Ws = gl_cells(sedges, nodes)
        print(par, 'Netze: Kern', len(Xc), 'Schale', len(Xs), flush=True)
        # r_tilde auf beiden Netzen
        t1 = time.time()
        Cc = [ctilde(x) for x in Xc]; Cs = [ctilde(x) for x in Xs]
        DTc = [DTz0(x) for x in Xc]; DTs = [DTz0(x) for x in Xs]
        print(par, 'Funktionsauswertung %.0fs' % (time.time()-t1), flush=True)
        Rc = [c_-d_ for c_, d_ in zip(Cc, DTc)]; Rs = [c_-d_ for c_, d_ in zip(Cs, DTs)]
        MC = [m(x) for x in Xc]; MS = [m(x) for x in Xs]
        mom_a = sum(w*mm_*r for w, mm_, r in zip(Wc, MC, Rc)) + sum(w*mm_*r for w, mm_, r in zip(Ws, MS, Rs))
        Hc = [r - mm_*mom_a/mu for r, mm_ in zip(Rc, MC)]; Hs = [r - mm_*mom_a/mu for r, mm_ in zip(Rs, MS)]
        norm_h = mp.sqrt(2*sum(w*x*x for w, x in zip(Wc, Hc)) + 2*sum(w*x*x for w, x in zip(Ws, Hs)))
        norm_c = mp.sqrt(2*sum(w*x*x for w, x in zip(Wc, Cc)) + 2*sum(w*x*x for w, x in zip(Ws, Cs)))
        norm_DT = mp.sqrt(2*sum(w*x*x for w, x in zip(Wc, DTc)) + 2*sum(w*x*x for w, x in zip(Ws, DTs)))
        # h8 = Pi8(h|(0,a8))
        mom8 = sum(w*mm_*x for w, mm_, x in zip(Wc, MC, Hc))
        H8 = [x - mm_*mom8/mu8 for x, mm_ in zip(Hc, MC)]
        norm_h8 = mp.sqrt(2*sum(w*x*x for w, x in zip(Wc, H8)))
        print(par, '||c_tilde|| =', mp.nstr(norm_c, 10), ' ||Dhat T z0|| =', mp.nstr(norm_DT, 10), ' ||h|| =', mp.nstr(norm_h, 10), ' ||h8|| =', mp.nstr(norm_h8, 10), ' Moment r_tilde =', mp.nstr(mom_a, 6), flush=True)
        # ---------- b_F = F*h  (zwoelf physische Quellen F = (z_{s+2},..,z_{s+8}, Lambda Y_1..Y_8)) und kohaerenter psi-k-Fehler
        import zipfile
        zz = zipfile.ZipFile(next(Path('/home/user/workspace/nstar').glob('*/inputs/*.zip')))
        hb = json.loads(zz.read([x for x in zz.namelist() if x.endswith('half-inverse/expected/1536.json')][0]))
        Dj = json.load(open(next(Path('/home/user/workspace/nstar').glob('*/expected/DIRECTIONS.json'))))[par]
        # Block-Paritaet ueber Jt = Q Z t (upper_v) identifizieren
        Zt = [Q2mp(x) for x in Dj['directions']['upper_v']['Zt_exact_rational']]
        assert len(Zt) == 92
        Jv_ref = [mid(x) for x in Dj['directions']['upper_v']['Jt_local_orthonormal_Legendre_coefficients_interval']]
        blk = None
        for cand in hb['blocks']:
            Qm = [[mid(x) for x in row] for row in cand['basis_Q_local_coefficients']]
            Jv = [sum(Qm[n][k]*Zt[k] for k in range(92)) for n in range(96)]
            dev = max(abs(x-y) for x, y in zip(Jv, Jv_ref))
            if dev < mp.mpf(10)**-20: blk = cand; print(par, 'Basisblock identifiziert, |QZt - Jt| <=', mp.nstr(dev, 3), flush=True)
        assert blk is not None
        Qm = [[mid(x) for x in row] for row in blk['basis_Q_local_coefficients']]
        Sm = [[Q2mp(x) for x in row] for row in blk['half_inverse_centre_rational_Q_coefficients']]
        Ycoef = [[sum(Qm[n][k]*Sm[k][j] for k in range(92)) for n in range(96)] for j in range(8)]   # Y_j = Q S, lokale Legendre-Koeffizienten
        def ell_shell(x, N=96):
            Pl = legendre_all(2*(x-cc)/h89, N); return [mp.sqrt(mp.mpf(2*n+1)/(2*h89))*Pl[n] for n in range(N)]
        ELs = [ell_shell(x) for x in Xs]
        Ys = [[sum(Ycoef[j][n]*E[n] for n in range(96)) for E in ELs] for j in range(8)]
        lamY = [sum(w*mm_*y for w, mm_, y in zip(Ws, MS, Ys[j])) for j in range(8)]            # lambda(Y_j) = int_a8^a m Y_j dx
        Pz = psiD[par]; zdeg = Pz['core_z_degrees']; ratios = [mp.mpf(x) for x in Pz['core_z_moment_ratios']]
        assert zdeg == [sigma+2, sigma+4, sigma+6, sigma+8]
        def zfun(i, x):
            Pb = legendre_all(x/a, max(zdeg)+1)
            e = lambda nn: mp.sqrt(mp.mpf(2*nn+1)/(2*a))*Pb[nn]
            return e(zdeg[i]) - e(sigma)*ratios[i]
        bF = []
        for i in range(4):
            bF.append(2*sum(w*zfun(i, x)*hh for w, x, hh in zip(Wc, Xc, Hc)) + 2*sum(w*zfun(i, x)*hh for w, x, hh in zip(Ws, Xs, Hs)))
        for j in range(8):
            bF.append(2*sum(w*y*hh for w, y, hh in zip(Ws, Ys[j], Hs)) - 2*(lamY[j]/mu8)*sum(w*mm_*hh for w, mm_, hh in zip(Wc, MC, Hc)))
        CT = json.load(open('/home/user/workspace/zip7/coherent-inputs/expected/COHERENT_TRANSPORT_INPUTS.json'))['parities'][par]
        coh = {}
        for key, dn in (('v', 'upper_v'), ('p', 'lower_Pv')):
            G = [[Q2mp(x) for x in row] for row in CT['directions'][key]['metric_G_equals_eta_squared_K_inverse']]
            k0 = [Q2mp(x) for x in CT['directions'][key]['fixed_k0_rational']]
            kpsi = [mp.mpf(x) for x in psiD[par]['directions'][dn]['core_k_mid']]
            coh[key] = {'sqrt(bF*G_t*bF)': mp.nstr(mp.sqrt(sum(bF[i]*G[i][j]*bF[j] for i in range(12) for j in range(12))), 10),
                        'eta': mp.nstr(Q2mp(CT['directions'][key]['eta_K_norm_upper']), 6),
                        'k0[0:4]_vs_PSI_core_k_mid_maxdiff': mp.nstr(max(abs(k0[i]-kpsi[i]) for i in range(4)), 3)}
        res_bF = {'b_F=F*h': [mp.nstr(x, 20) for x in bF], 'lambda_Y': [mp.nstr(x, 12) for x in lamY], 'coherent_psi_k_error': coh}
        print(par, res_bF, flush=True)
        # ---------- Mellin-Koordinaten Phi*h8 (191 Grade)
        degs = list(range(sigma+2, sigma+383, 2))
        m_s = lambda s: m(a8*s)
        me = {k: mp.quad(lambda s, k=k: m_s(s)*mp.sqrt(2*k+1)*mp.legendre(k, s), [-1, 1])/2 for k in degs+[sigma]}
        gamma_m = (mp.quad(lambda s: m_s(s)**2, [-1, 1])/2)/me[sigma]**2
        PHc = [legendre_all(x/a8, sigma+384) for x in Xc]
        raw = {k: mp.sqrt(2*mp.mpf(2*k+1)/a8)*sum(w*PH[k]*hh for w, PH, hh in zip(Wc, PHc, H8)) for k in degs+[sigma]}
        a_h = raw[sigma]
        phih = [raw[k] - me[k]*a_h/me[sigma] for k in degs]
        norm_phih = mp.sqrt(sum(p*p for p in phih))
        res = {'direction': direction, 'delta': mp.nstr(delta, 8), 'rho': mp.nstr(rho, 6), 'gamma_m': mp.nstr(gamma_m, 12),
               'z0': {'B': mp.nstr(B, 20), 'A_c': mp.nstr(Ac, 20), 'L': mp.nstr(L, 20), 'mu': mp.nstr(mu, 20)},
               'c_tilde_control_max_dev_13_points': mp.nstr(devmax, 3),
               'F_hat_z0': [mp.nstr(x, 30) for x in Fz0], 'T_z0': [mp.nstr(x, 30) for x in Tz0],
               'norm_c_tilde': mp.nstr(norm_c, 15), 'norm_Dhat_T_z0': mp.nstr(norm_DT, 15), 'norm_h': mp.nstr(norm_h, 15),
               'norm_h8': mp.nstr(norm_h8, 15), 'norm_Phi_star_h8': mp.nstr(norm_phih, 15), 'a_h': mp.nstr(a_h, 15),
               'moment_r_tilde': mp.nstr(mom_a, 10), 'Phi_star_h8': [mp.nstr(p, 25) for p in phih], **res_bF,
               'h_shell_samples': [[mp.nstr(x, 12), mp.nstr(v, 15)] for x, v in list(zip(Xs, Hs))[::384]],
               'h_core_samples': [[mp.nstr(x, 12), mp.nstr(v, 15)] for x, v in list(zip(Xc, Hc))[::384]]}
        json.dump({par: res}, open(HERE/f'L00_partial_{par}.json', 'w'), indent=1)
        # ---------- Richtungen: psi_t, c_t, f_t
        for dname in ([direction] + (['upper_v'] if direction != 'upper_v' else [])):
            dirn = FA[par]['directions'][dname]
            c = [mid(x) for x in dirn['c_model']]; phif = [mid(x) for x in dirn['Phi_star_f_model']]
            P = psiD[par]; d = P['directions'][dname]
            shell = [mp.mpf(x) for x in d['shell_coeff_mid']]; N = len(shell)
            kz = [mp.mpf(x) for x in d['core_k_mid']]; ratios = [mp.mpf(x) for x in P['core_z_moment_ratios']]
            zdeg = P['core_z_degrees']; lam_total = mp.mpf(d['lambda_total_mid'])
            def psi_core(x):
                Pb = legendre_all(x/a, max(zdeg)+1)
                e = lambda n: mp.sqrt(mp.mpf(2*n+1)/(2*a))*Pb[n]
                # Lambda lifts into (0,a8); its mass is mu8 (PSI_DEFINITION), not the a9 mass mu.
                return -lam_total*m(x)/mu8 - sum(kz[i]*(e(zdeg[i]) - e(sigma)*ratios[i]) for i in range(4))
            def psi_shell(x):
                Pl = legendre_all(2*(x-cc)/h89, N)
                return sum(shell[n]*mp.sqrt(mp.mpf(2*n+1)/(2*h89))*Pl[n] for n in range(N))
            PSc = [psi_core(x) for x in Xc]; PSs = [psi_shell(x) for x in Xs]
            psi_h = 2*sum(w*p*x for w, p, x in zip(Wc, PSc, Hc)) + 2*sum(w*p*x for w, p, x in zip(Ws, PSs, Hs))
            psi_h_shell = 2*sum(w*p*x for w, p, x in zip(Ws, PSs, Hs))
            c_phih = sum(ci*pi for ci, pi in zip(c, phih))
            phif_phih = sum(fi*pi for fi, pi in zip(phif, phih))
            mfh = MESH/f'MESHH_{par}_{dname}.json'          # f auf dem mit den h-Schnittstellen vereinigten Netz (Stufe 5)
            mf = mfh if mfh.exists() else MESH/f'MESH_{par}_{dname}.json'
            f_mesh_ok = mfh.exists()
            M2 = json.load(open(mf))
            Xf = [mp.mpf(n['x']) for n in M2['nodes']]; Wf = [mp.mpf(n['w']) for n in M2['nodes']]
            Qr = [mp.mpf(n['Q_raw']) for n in M2['nodes']]
            momf = sum(w*m(x)*q for w, x, q in zip(Wf, Xf, Qr))
            fv = [q - m(x)*momf/mu8 for q, x in zip(Qr, Xf)]
            a_f = mp.sqrt(2*mp.mpf(2*sigma+1)/a8)*sum(w*mp.legendre(sigma, x/a8)*f for w, x, f in zip(Wf, Xf, fv))
            # h8 auf dem Stufe-2-Netz (Funktionsauswertung erneut)
            Hf = [ctilde(x) - DTz0(x) - m(x)*mom_a/mu for x in Xf]
            H8f = [x - m(xx)*mom8/mu8 for x, xx in zip(Hf, Xf)]
            f_h8 = 2*sum(w*f*hh for w, f, hh in zip(Wf, fv, H8f))
            yf_yh_over_delta = (f_h8 + gamma_m*a_f*a_h - phif_phih)/delta   # = <y_f,y_h>/delta, Teil des hohen Restes
            I0 = psi_h - c_phih                                              # Mittelpunkt (7.1): I0 = <psi,h> - <c,Phi*h8>
            hd = hi[par]['directions'][dname]
            H_hi = Q2mp(hd['whole_physical_high_U8_part_norm_upper'][1]); e_psi = Q2mp(hd['whole_psi_model_error_upper'][1])
            fm = Q2mp(hd['finite_pairing_feature_error_multiplier'][1])
            row = {'f_mesh_contains_h_cuts': f_mesh_ok, '<psi,h>': mp.nstr(psi_h, 15), '<psi,h>_Schale': mp.nstr(psi_h_shell, 15), '<f,h8>': mp.nstr(f_h8, 15), 'a_f': mp.nstr(a_f, 12),
                   '<Phi*f,Phi*h8>': mp.nstr(phif_phih, 15), '<y_f,y_h>/delta (Teil des hohen Restes r=(1/delta)<y_f-B*c,y_h>, NICHT vom Mittelpunkt abzuziehen)': mp.nstr(yf_yh_over_delta, 15),
                   '<c,Phi*h8>': mp.nstr(c_phih, 15),
                   'psi_core_mass_horizon': 'a8', 'psi_core_mu': mp.nstr(mu8, 60),
                   'I0_midpoint=<psi,h>-<c,Phi*h8>': mp.nstr(I0, 15),
                   'hoher_Rest_Schranke_H_hi*norm_h8 (undirected, ||y_h||<=||h8||)': mp.nstr(H_hi*norm_h8, 8),
                   'Budgetdiagnose_e_psi*norm_h': mp.nstr(e_psi*norm_h, 8), 'Budgetdiagnose_featmult*norm_Phi_star_h8/sqrt(1-rho)': mp.nstr(fm*norm_phih/mp.sqrt(1-rho), 8),
                   'H_hi': mp.nstr(H_hi, 6), 'e_psi': mp.nstr(e_psi, 6), 'featmult': mp.nstr(fm, 6)}
            res['pairing_'+dname] = row
            print(par, dname, row, '%.0fs' % (time.time()-t0), flush=True)
        out[par] = res
        json.dump({par: res}, open(HERE/f'L00_{direction}_{par}.json', 'w'), indent=1)
    print('done')

if __name__ == '__main__':
    pars = tuple(sys.argv[1:]) or ('even', 'odd')
    main('lower_Pv', pars)
