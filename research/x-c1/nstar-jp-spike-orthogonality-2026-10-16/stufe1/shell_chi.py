"""Stufe 1 (korrigierte Fassung v2, Vorzeichen von lambda_total): Schalenteil chi_t|(a8,b9) = r - sum_i F_i k_i  in der lokalen ON-Legendrebasis ell_n.

Hochpraezise Gleitkomma-Diagnose (mpmath, 60 Stellen) mit Transport der gelieferten
k-Intervallradien und Jt-/Q-Intervallradien. KEIN rationales Zertifikat.
Quellen: DIRECTIONS.json (N*Jp-Paket b48e3895...), 1536.json (Q, S) aus dem globalen Archiv
2ca3c682..., Funktionsdefinitionen FUNKTIONSANSCHLUSS.txt §§1-3, 6.
"""
import json, sys
from fractions import Fraction as Fr
from pathlib import Path
import mpmath as mp

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
PKG = Path('/home/user/workspace/nstar/Objekt-X-Nstar-Jp-Funktionsanschluss-und-Koeffizienten-2026-10-16')
HALF = PKG/'glob/Objekt-X-Globaler-Gram-und-vollstaendige-Projektion-2026-10-13/snapshot/work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/remainder-integration-check-v2/originals/half-inverse/expected/1536.json'

a8 = 3*mp.log(2)/2
b9 = mp.log(3)
h = b9 - a8
c = (a8 + b9)/2
N = 96

def mpf_of(q):
    q = Fr(q)
    return mp.mpf(q.numerator)/mp.mpf(q.denominator)

def ell(n, x):
    return mp.sqrt(mp.mpf(2*n+1)/(2*h))*mp.legendre(n, 2*(x-c)/h)

def eb(n, x):
    return mp.sqrt(mp.mpf(2*n+1)/(2*b9))*mp.legendre(n, x/b9)

def m_of(sigma):
    return (lambda x: mp.cosh(x/2)) if sigma == 0 else (lambda x: mp.sinh(x/2))

def quad(f, a, b):
    return mp.quad(f, [a, b])

def main():
    dirs = json.load(open(PKG/'expected/DIRECTIONS.json'))
    half = json.load(open(HALF))
    out = {}
    for idx, par in enumerate(['even', 'odd']):
        sigma = idx
        m = m_of(sigma)
        mu = quad(lambda x: m(x)**2, 0, a8)
        mu_exact = (a8/2 + mp.sinh(a8)/2) if sigma == 0 else (-a8/2 + mp.sinh(a8)/2)
        assert abs(mu - mu_exact) < mp.mpf(10)**-50
        # Momente int_a8^b9 m ell_n dx  (dx, nicht 2dx; FUNKTIONSANSCHLUSS §1)
        lam_ell = [quad(lambda x, n=n: m(x)*ell(n, x), a8, b9) for n in range(N)]
        # z_n: physische Funktionen auf (-b9,b9); Moment int_0^b9 m e_n^b dx
        mom_e = {}
        def mom(n):
            if n not in mom_e:
                mom_e[n] = quad(lambda x: m(x)*eb(n, x), 0, b9)
            return mom_e[n]
        degs = [sigma+2, sigma+4, sigma+6, sigma+8]
        # Schalenkoeffizienten der z_n: (z_n|shell, ell_k)_X = 2 int_a8^b9 z_n ell_k dx, k<=9 exakt (Polynome)
        z_shell = []
        z_core_norm2 = []
        z_full_norm2 = []
        for n in degs:
            ratio = mom(n)/mom(sigma)
            zf = lambda x, n=n, ratio=ratio: eb(n, x) - eb(sigma, x)*ratio
            coef = [2*quad(lambda x, k=k: zf(x)*ell(k, x), a8, b9) for k in range(10)] + [mp.mpf(0)]*(N-10)
            # Kontrolle: Projektion vollstaendig (Grad<=9): Norm^2 auf Schale == sum coef^2
            n2_shell = 2*quad(lambda x: zf(x)**2, a8, b9)
            assert abs(n2_shell - sum(cc**2 for cc in coef)) < mp.mpf(10)**-45, (n, n2_shell - sum(cc**2 for cc in coef))
            z_shell.append(coef)
            z_core_norm2.append(2*quad(lambda x: zf(x)**2, 0, a8))
            z_full_norm2.append(n2_shell + z_core_norm2[-1])
            # Momentnull-Kontrolle
            assert abs(quad(zf, 0, b9) if False else quad(lambda x: m(x)*zf(x), 0, b9)) < mp.mpf(10)**-45
        # Y_j = Q S_j (Mittelpunkte der Q-Intervalle; Radien ~1e-60 separat gezaehlt)
        hb = half['blocks'][idx]
        qbox = hb['basis_Q_local_coefficients']
        S = [[Fr(x) for x in row] for row in hb['half_inverse_centre_rational_Q_coefficients']]
        Qmid = [[(Fr(a)+Fr(b))/2 for a, b in row] for row in qbox]
        Qrad_max = max(abs(Fr(b)-Fr(a))/2 for row in qbox for a, b in row)
        Y = []
        for j in range(8):
            col = []
            for n in range(N):
                col.append(mpf_of(sum(Qmid[n][i]*S[i][j] for i in range(92))))
            Y.append(col)
        lam_Y = [sum(Y[j][n]*lam_ell[n] for n in range(N)) for j in range(8)]
        # Funktionsnormen der F_i auf der Schale (X-Norm)
        F_shell = z_shell + Y
        F_shell_norm = [mp.sqrt(sum(cc**2 for cc in col)) for col in F_shell]
        F_full_norm = [mp.sqrt(v) for v in z_full_norm2] + [mp.sqrt(sum(cc**2 for cc in Y[j]) + 2*lam_Y[j]**2/mu) for j in range(8)]
        res_par = {'mu': str(mu), 'lambda_Y_j': [str(v) for v in lam_Y],
                   'F_shell_X_norm': [str(v) for v in F_shell_norm],
                   'F_full_H9_norm': [str(v) for v in F_full_norm],
                   'Q_interval_radius_max': float(Qrad_max), 'directions': {}}
        for dn in ['upper_v', 'lower_Pv']:
            D = dirs[par]['directions'][dn]
            Jt = [((Fr(a)+Fr(b))/2, (Fr(b)-Fr(a))/2) for a, b in D['Jt_local_orthonormal_Legendre_coefficients_interval']]
            r = [mpf_of(x[0]) for x in Jt]
            r_rad = sum(mpf_of(x[1]) for x in Jt)  # grobe l1-Summe der Radien
            k = [((Fr(a)+Fr(b))/2, (Fr(b)-Fr(a))/2) for a, b in D['actual_k_component_intervals']]
            kmid = [mpf_of(x[0]) for x in k]
            krad = [mpf_of(x[1]) for x in k]
            lam_r = sum(r[n]*lam_ell[n] for n in range(N))
            r_norm2 = sum(x**2 for x in r)
            WX_r = r_norm2 + 2*lam_r**2/mu
            t2 = sum(mpf_of(x)**2 for x in D['t_exact_rational'])
            # Schalenteil
            Fk = [sum(kmid[i]*F_shell[i][n] for i in range(12)) for n in range(N)]
            Fk_z = [sum(kmid[i]*F_shell[i][n] for i in range(4)) for n in range(N)]
            Fk_Y = [sum(kmid[i]*F_shell[i][n] for i in range(4, 12)) for n in range(N)]
            chi_shell = [r[n] - Fk[n] for n in range(N)]
            nrm = lambda v: mp.sqrt(sum(x**2 for x in v))
            # Fehlertransport aus k-Radien: sum_i rad_i ||F_i|shell||  (Dreiecksungleichung)
            err_k = sum(krad[i]*F_shell_norm[i] for i in range(12))
            err_k_z = sum(krad[i]*F_shell_norm[i] for i in range(4))
            # Kern-Momentanteil von chi auf (0,a8) ohne u: Koeffizient von -m/mu
            # KORRIGIERT 2026-10-16: (Lambda Y_j)|Kern = -(lambda(Y_j)/mu) m, daher MINUS (vorher faelschlich Plus)
            lam_total = lam_r - sum(kmid[4+j]*lam_Y[j] for j in range(8))
            lam_total_rad = sum(krad[4+j]*abs(lam_Y[j]) for j in range(8))
            # Kernpolynomteil sum_{i<=4} k_i z_i auf (0,a8): Norm (2dx)
            core_poly_norm2 = 2*quad(lambda x: (sum(kmid[i]*(eb(degs[i], x) - eb(sigma, x)*mom(degs[i])/mom(sigma)) for i in range(4)))**2, 0, a8)
            core_mom_norm = abs(lam_total)*mp.sqrt(mu)/mu  # ||lam_total m/mu||_{L2(2dx)} = |lam_total| sqrt(2mu)/mu ... siehe unten
            core_mom_norm = abs(lam_total)*mp.sqrt(2*mu)/mu
            sum_abs = sum(abs(kmid[i])*F_shell_norm[i] for i in range(12))
            sum_abs_z = sum(abs(kmid[i])*F_shell_norm[i] for i in range(4))
            res = {
                't_norm2': str(t2), 'r_X_norm2': str(r_norm2), 'lambda_r': str(lam_r), 'W_X[r]': str(WX_r),
                'W_X[r]/t_norm2': str(WX_r/t2), 'Jt_radius_l1': str(r_rad),
                'k_mid': [str(x) for x in kmid], 'k_rad': [str(x) for x in krad],
                'shell_chi_X_norm': str(nrm(chi_shell)),
                'shell_Fk_X_norm': str(nrm(Fk)), 'shell_Fk_z_part_X_norm': str(nrm(Fk_z)), 'shell_Fk_Y_part_X_norm': str(nrm(Fk_Y)),
                'shell_sum_abs_k_i_normF_i': str(sum_abs), 'shell_sum_abs_z_part': str(sum_abs_z),
                'cancellation_factor_sumabs_over_result': str(sum_abs/nrm(chi_shell)),
                'shell_error_radius_from_k_intervals': str(err_k), 'shell_error_radius_from_k_intervals_z_part': str(err_k_z),
                'shell_relative_error_from_k': str(err_k/nrm(chi_shell)),
                'core_moment_coefficient_lambda_total': str(lam_total), 'core_moment_coefficient_radius': str(lam_total_rad),
                'core_moment_term_norm_||lam_total m/mu||': str(core_mom_norm),
                'core_poly_part_norm_||sum_{i<=4} k_i z_i on (0,a8)||': str(mp.sqrt(core_poly_norm2)),
                'chi_shell_coefficients_mid': [str(x) for x in chi_shell],
                'chi_shell_coefficients_lowdeg_0_9': [mp.nstr(x, 12) for x in chi_shell[:10]],
                'chi_shell_coefficients_tail_abs_max_n>=10': str(max(abs(x) for x in chi_shell[10:])),
                'r_coefficients_lowdeg_0_9': [mp.nstr(x, 12) for x in r[:10]],
            }
            res_par['directions'][dn] = res
            print(par, dn)
            for key in ['W_X[r]/t_norm2', 'shell_chi_X_norm', 'shell_Fk_X_norm', 'shell_Fk_z_part_X_norm', 'shell_Fk_Y_part_X_norm',
                        'shell_sum_abs_k_i_normF_i', 'cancellation_factor_sumabs_over_result',
                        'shell_error_radius_from_k_intervals', 'shell_relative_error_from_k',
                        'core_moment_coefficient_lambda_total', 'core_moment_coefficient_radius',
                        'core_moment_term_norm_||lam_total m/mu||', 'core_poly_part_norm_||sum_{i<=4} k_i z_i on (0,a8)||',
                        'chi_shell_coefficients_tail_abs_max_n>=10']:
                print('  ', key, '=', mp.nstr(mp.mpf(res[key]), 10))
            print('   chi_shell low coeffs:', res['chi_shell_coefficients_lowdeg_0_9'])
            print('   r low coeffs       :', res['r_coefficients_lowdeg_0_9'])
            sys.stdout.flush()
        out[par] = res_par
    json.dump(out, open(HERE/'STUFE1_SHELL_RESULTS.json', 'w'), indent=1)

if __name__ == '__main__':
    main()
