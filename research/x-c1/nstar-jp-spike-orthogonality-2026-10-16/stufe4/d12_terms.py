"""Stufe 4 (Teil): alle Terme von HERLEITUNG (7.2) fuer h = D_j, die ohne B T_h h8 berechenbar sind.

<chi_v, D_j> = <psi_v, D_j> - [<f_v,h8_j> + gamma_m a_f a_h - <Phi*f_v, Phi*h8_j>]/delta - <c, Phi*h8_j> + <c, B T_h h8_j>/delta
mit h8_j = Pi8 (D_j|core), <Vf,Vh8>/(1-rho) = <c, d_h>, d_h = Phi*h8 - B T_h h8/delta.
Der letzte Term (B-Kopplung) wird NICHT berechnet und als offener Rest ausgewiesen.
Diagnose (mpmath, 150 Stellen fuer D_j-Auswertung); kein Zertifikat.
"""
import json, gzip, time
from fractions import Fraction as Fr
from pathlib import Path
import mpmath as mp
import mpmath.calculus.quadrature as Qd

mp.mp.dps = 150
HERE = Path(__file__).resolve().parent
Z3 = next(Path('/home/user/workspace/zip3').glob('Objekt-X-Stufe3*'))
F12 = Path('/home/user/workspace/r227/inner/objekt-x-whole-functions12-2026-10-15/FUNCTIONS12.json')
PSI = Path('/home/user/workspace/stufe1/PSI_DEFINITION.json')
MESH = Path('/home/user/workspace/stufe2')

def Q2mp(s):
    q = Fr(s); return mp.mpf(q.numerator)/mp.mpf(q.denominator)
def mid(iv):
    return (Q2mp(iv[0])+Q2mp(iv[1]))/2
def legendre_all(s, N):
    P = [mp.mpf(1), s]
    for n in range(1, N-1):
        P.append(((2*n+1)*s*P[n] - n*P[n-1])/(n+1))
    return P[:N]

def main():
    a8 = 3*mp.log(2)/2; a = mp.log(3); h = a-a8; cc = (a8+a)/2
    logs = {2: mp.log(2), 3: mp.log(3), 4: 2*mp.log(2), 5: mp.log(5), 7: mp.log(7), 8: 3*mp.log(2)}
    common = json.loads(gzip.decompress(open(Z3/'inputs/REFINED_COMMON96.json.gz', 'rb').read()))
    FA = json.load(open(Z3/'expected/FINITE_ACTION.json'))
    f12 = json.load(open(F12)); psiD = json.load(open(PSI))
    gl = Qd.GaussLegendre(mp.mp)
    nodes = gl.calc_nodes(8, mp.mp.prec)   # 384 Knoten
    out = {}
    for sigma, par in enumerate(['even', 'odd']):
        t0 = time.time()
        co = common['cases'][sigma]
        delta = Q2mp(co['delta']); rho = Q2mp(co['rho'])
        dirn = FA[par]['directions']['upper_v']
        c = [mid(x) for x in dirn['c_model']]; phif = [mid(x) for x in dirn['Phi_star_f_model']]
        m = (lambda x: mp.cosh(x/2)) if sigma == 0 else (lambda x: mp.sinh(x/2))
        mu = a8/2+mp.sinh(a8)/2 if sigma == 0 else -a8/2+mp.sinh(a8)/2
        degs = list(range(sigma+2, sigma+383, 2))
        # Mellin-Koordinaten in der skalierten Basis
        m_s = lambda s: m(a8*s)
        me = {k: mp.quad(lambda s, k=k: m_s(s)*mp.sqrt(2*k+1)*mp.legendre(k, s), [-1, 1])/2 for k in degs+[sigma]}
        gamma_m = (mp.quad(lambda s: m_s(s)**2, [-1, 1])/2)/me[sigma]**2
        # psi_v
        P = psiD[par]; d = P['directions']['upper_v']
        shell = [mp.mpf(x) for x in d['shell_coeff_mid']]; N = len(shell)
        kz = [mp.mpf(x) for x in d['core_k_mid']]; ratios = [mp.mpf(x) for x in P['core_z_moment_ratios']]
        zdeg = P['core_z_degrees']; lam_total = mp.mpf(d['lambda_total_mid'])
        def psi_core(x):
            Pb = legendre_all(x/a, max(zdeg)+1)
            e = lambda n: mp.sqrt(mp.mpf(2*n+1)/(2*a))*Pb[n]
            return -lam_total*m(x)/mu - sum(kz[i]*(e(zdeg[i]) - e(sigma)*ratios[i]) for i in range(4))
        def psi_shell(x):
            Pl = legendre_all(2*(x-cc)/h, N)
            return sum(shell[n]*mp.sqrt(mp.mpf(2*n+1)/(2*h))*Pl[n] for n in range(N))
        # D_j Modelle
        funcs = f12['parities'][par]['functions']
        Dspecs = []
        for row in funcs:
            D = row['D']
            poly = [Q2mp(x) for x in D['polynomial']]; vm = [Q2mp(x) for x in D['V_multiplier']]; mm = Q2mp(D['moment_multiplier'])
            shifts = []
            for term in D['shift_terms']:
                q = int(term['channel']); sgn = int(term['translation_sign']); sh = logs[q]/a
                lo, hi = ((mp.mpf(0), 1-sh) if sgn == 1 else ((mp.mpf(0) if q in (2, 3) else sh-1), mp.mpf(1)))
                shifts.append((lo, hi, [Q2mp(x) for x in term['polynomial']]))
            Dspecs.append((poly, vm, mm, shifts))
        def Dval(j, x):
            poly, vm, mm, shifts = Dspecs[j]; t = x/a
            v = mp.polyval(poly[::-1], t) + mp.polyval(vm[::-1], t)*(-mp.log(1-t*t)/2) + mm*m(x)
            for lo, hi, pc in shifts:
                if lo < t < hi: v += mp.polyval(pc[::-1], t)
            return v/mp.sqrt(2*a)
        # Kernnetz (0,a8) mit D-Sprungstellen
        bps = sorted([logs[4]-a, a-logs[2], logs[5]-a, logs[7]-a, logs[8]-a])
        edges = [mp.mpf(0)] + bps + [a8]
        Xc, Wc = [], []
        for lo, hi in zip(edges[:-1], edges[1:]):
            md, hf = (lo+hi)/2, (hi-lo)/2
            for s, w in nodes: Xc.append(md+hf*s); Wc.append(hf*w)
        # Schalennetz (a8,a), geometrisch zu a verfeinert (V-Log von D_j)
        Xs, Ws = [], []
        sedges = [a8] + [a - h*mp.mpf(2)**(-k) for k in range(1, 40)] + [a]
        for lo, hi in zip(sedges[:-1], sedges[1:]):
            md, hf = (lo+hi)/2, (hi-lo)/2
            for s, w in nodes: Xs.append(md+hf*s); Ws.append(hf*w)
        print(par, 'Netze:', len(Xc), len(Xs), flush=True)
        PHc = [legendre_all(x/a8, sigma+384) for x in Xc]          # Legendre in skalierter Kernkoordinate
        MC = [m(x) for x in Xc]
        PSc = [psi_core(x) for x in Xc]; PSs = [psi_shell(x) for x in Xs]
        # f_v auf Stufe-2-Netz
        M2 = json.load(open(MESH/f'MESH_{par}_upper_v.json'))
        Xf = [mp.mpf(n['x']) for n in M2['nodes']]; Wf = [mp.mpf(n['w']) for n in M2['nodes']]
        Qr = [mp.mpf(n['Q_raw']) for n in M2['nodes']]
        momf = sum(w*m(x)*q for w, x, q in zip(Wf, Xf, Qr))
        fv = [q - m(x)*momf/mu for q, x in zip(Qr, Xf)]
        a_f = mp.sqrt(2*mp.mpf(2*sigma+1)/a8)*sum(w*mp.legendre(sigma, x/a8)*f for w, x, f in zip(Wf, Xf, fv))
        res = {'delta': mp.nstr(delta, 8), 'gamma_m': mp.nstr(gamma_m, 12), 'a_f': mp.nstr(a_f, 12), 'rows': []}
        for j in range(12):
            DC = [Dval(j, x) for x in Xc]
            momD = sum(w*mm_*dd for w, mm_, dd in zip(Wc, MC, DC))
            h8 = [dd - mm_*momD/mu for dd, mm_ in zip(DC, MC)]          # Pi8 (D_j|core)
            # Phi*h8: <Phi_i,h8> = <e_i, M* U h8> = <e_i,Uh8> - <e_i,m_s> a_h/m_e ; <e_k,Uh8> = sqrt(2/a8)*sqrt(2k+1) int P_k(x/a8) h8 dx
            raw = {k: mp.sqrt(2*mp.mpf(2*k+1)/a8)*sum(w*PH[k]*hh for w, PH, hh in zip(Wc, PHc, h8)) for k in degs+[sigma]}
            a_h = raw[sigma]
            phih = [raw[k] - me[k]*a_h/me[sigma] for k in degs]
            c_phih = sum(ci*pi for ci, pi in zip(c, phih))
            phif_phih = sum(fi*pi for fi, pi in zip(phif, phih))
            # <psi, D_j> ueber (0,a): Kern + Schale
            DS = [Dval(j, x) for x in Xs]
            psiD_ = 2*sum(w*p*dd for w, p, dd in zip(Wc, PSc, DC)) + 2*sum(w*p*dd for w, p, dd in zip(Ws, PSs, DS))
            # <f_v, h8_j> auf Stufe-2-Netz
            Df = [Dval(j, x) for x in Xf]
            h8f = [dd - m(x)*momD/mu for dd, x in zip(Df, Xf)]
            f_h8 = 2*sum(w*f*hh for w, f, hh in zip(Wf, fv, h8f))
            bracket = (f_h8 + gamma_m*a_f*a_h - phif_phih)/delta
            partial = psiD_ - bracket - c_phih
            # Modenzerlegung von <c,Phi*h8>: Anteil der weichsten Mode separat (u1 aus SOFTMODE-Lauf nicht geladen; hier nur Gesamtwert)
            row = {'j': j, 'degree': funcs[j]['degree'], '<psi_v,D_j>': mp.nstr(psiD_, 12), '<f_v,h8_j>': mp.nstr(f_h8, 12), 'a_h': mp.nstr(a_h, 12),
                   '<Phi*f,Phi*h8>': mp.nstr(phif_phih, 12), 'bracket/delta': mp.nstr(bracket, 12), '<c,Phi*h8_j>': mp.nstr(c_phih, 12),
                   'ell_v(D_j) ohne B-Term': mp.nstr(partial, 12), 'offen': '+ <c, B T_h h8_j>/delta',
                   'norm_h8_j': mp.nstr(mp.sqrt(2*sum(w*hh*hh for w, hh in zip(Wc, h8))), 10), 'norm_Phi*h8_j': mp.nstr(mp.sqrt(sum(p*p for p in phih)), 10),
                   'Phi_star_h8_j': [mp.nstr(p, 25) for p in phih]}
            res['rows'].append(row)
            print(par, j, {k: v for k, v in row.items() if k not in ('Phi_star_h8_j',)}, '%.0fs' % (time.time()-t0), flush=True)
        out[par] = res
        json.dump(out, open(HERE/'D12_TERMS.json', 'w'), indent=1)
    print('done')

if __name__ == '__main__':
    main()
