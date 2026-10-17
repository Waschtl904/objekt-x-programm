"""<y_f,y_h>/delta mit f_v auf dem h-angepassten Netz (MESHH) und Vergleich mit <B*c_v,y_h>/delta aus HIGH_REST (A8(Phi c_v) auf h-Netz)."""
import sys, json, glob
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 150
sys.path.insert(0, '/home/user/workspace/stufe5'); import l00
Z3 = glob.glob('/home/user/workspace/zip3/Objekt-X-Stufe3*')[0]
def toq(s): q = Fr(s); return mp.mpf(q.numerator)/mp.mpf(q.denominator)
def mid(iv): return (toq(iv[0])+toq(iv[1]))/2
for par in sys.argv[1:] or ['even', 'odd']:
    sigma = 0 if par == 'even' else 1; eps = (-1)**sigma
    a8 = 3*mp.log(2)/2; a = mp.log(3); b = mp.log(11)/2
    m = (lambda x: mp.cosh(x/2)) if sigma == 0 else (lambda x: mp.sinh(x/2))
    mu8 = a8/2+mp.sinh(a8)/2 if sigma == 0 else -a8/2+mp.sinh(a8)/2; mu = (mp.mpf(4)/3 + eps*a)/2
    P = json.load(open(f'/home/user/workspace/stufe5/L00_lower_Pv_ERSTFASSUNG.json'))[par]; HR = json.load(open(f'/home/user/workspace/stufe5/HIGH_REST_{par}.json'))
    FA = json.load(open(Z3+'/expected/FINITE_ACTION.json')); d = FA[par]['directions']['upper_v']; phif = [mid(x) for x in d['Phi_star_f_model']]
    import gzip; common = json.loads(gzip.decompress(open(Z3+'/inputs/REFINED_COMMON96.json.gz', 'rb').read())); delta = toq(common['cases'][sigma]['delta'])
    M2 = json.load(open(f'/home/user/workspace/stufe2/MESHH_{par}_upper_v.json'))
    Xf = [mp.mpf(n['x']) for n in M2['nodes']]; Wf = [mp.mpf(n['w']) for n in M2['nodes']]; Qr = [mp.mpf(n['Q_raw']) for n in M2['nodes']]
    momf = sum(w*m(x)*q for w, x, q in zip(Wf, Xf, Qr)); fv = [q - m(x)*momf/mu8 for q, x in zip(Qr, Xf)]
    a_f = mp.sqrt(2*mp.mpf(2*sigma+1)/a8)*sum(w*mp.legendre(sigma, x/a8)*f for w, x, f in zip(Wf, Xf, fv))
    norm_f = mp.sqrt(2*sum(w*f*f for w, f in zip(Wf, fv)))
    # h8 auf dem f-Netz
    Tz0 = [mp.mpf(x) for x in P['T_z0']]; B = mp.mpf(P['z0']['B']); Ac_ = mp.mpf(P['z0']['A_c'])
    logs = {2: mp.log(2), 3: mp.log(3), 4: 2*mp.log(2), 5: mp.log(5), 7: mp.log(7), 8: 3*mp.log(2), 9: 2*mp.log(3)}
    CH = [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7), (8, 2), (9, 3)]; wq = {q: mp.log(pr)/mp.sqrt(q) for q, pr in CH}
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
    funcs = json.load(open(l00.F12))['parities'][par]['functions']; Dspecs = []
    for row in funcs:
        D = row['D']; poly = [toq(x) for x in D['polynomial']]; vm = [toq(x) for x in D['V_multiplier']]; mm = toq(D['moment_multiplier']); shifts = []
        for term in D['shift_terms']:
            q = int(term['channel']); sgn = int(term['translation_sign']); sh = logs[q]/a
            lo, hi_ = ((mp.mpf(0), 1-sh) if sgn == 1 else ((mp.mpf(0) if q in (2, 3) else sh-1), mp.mpf(1)))
            shifts.append((lo, hi_, [toq(x) for x in term['polynomial']]))
        Dspecs.append((poly, vm, mm, shifts))
    def Dval(j, x):
        poly, vm, mm, shifts = Dspecs[j]; t = x/a
        v = mp.polyval(poly[::-1], t) + mp.polyval(vm[::-1], t)*(-mp.log(1-t*t)/2) + mm*m(x)
        for lo, hi_, pc in shifts:
            if lo < t < hi_: v += mp.polyval(pc[::-1], t)
        return v/mp.sqrt(2*a)
    mom_a = mp.mpf(P['moment_r_tilde'])
    H = [ctilde(x) - sum(Tz0[i]*Dval(i, x) for i in range(12)) - m(x)*mom_a/mu for x in Xf]
    mom8 = sum(w*m(x)*hh for w, x, hh in zip(Wf, Xf, H)); H8 = [hh - m(x)*mom8/mu8 for hh, x in zip(H, Xf)]
    norm_h8 = mp.sqrt(2*sum(w*x*x for w, x in zip(Wf, H8)))
    phih = [mp.mpf(x) for x in P['Phi_star_h8']]; a_h = mp.mpf(P['a_h']); gamma_m = mp.mpf(P['gamma_m'])
    f_h8 = 2*sum(w*f*hh for w, f, hh in zip(Wf, fv, H8)); phif_phih = sum(x*y for x, y in zip(phif, phih))
    yf_yh = f_h8 + gamma_m*a_f*a_h - phif_phih
    yf2 = norm_f**2 + gamma_m*a_f**2 - sum(x*x for x in phif)
    Bc_yh = mp.mpf(HR['<B*c_v,y_h>/delta'])*delta
    r = (yf_yh - Bc_yh)/delta
    res = {'f_mesh': 'MESHH (h-Schnittstellen enthalten)', 'cells': len(M2['cells']), 'norm_f': mp.nstr(norm_f, 12), 'norm_y_f_from_mesh': mp.nstr(mp.sqrt(yf2), 10),
           'norm_h8_on_f_mesh': mp.nstr(norm_h8, 12), 'norm_h8_L00': P['norm_h8'], '<f,h8>': mp.nstr(f_h8, 15), 'gamma_m*a_f*a_h': mp.nstr(gamma_m*a_f*a_h, 15),
           '<Phi*f,Phi*h8>': mp.nstr(phif_phih, 15), '<y_f,y_h>/delta': mp.nstr(yf_yh/delta, 12), '<B*c_v,y_h>/delta': HR['<B*c_v,y_h>/delta'],
           'r_v(h)': mp.nstr(r, 8), 'Vergleichswert_H_hi,v*||y_h||': HR['Vergleichswert_H_hi,v*||y_h||'],
           'alpha*r_v(h)': mp.nstr(mp.mpf(HR['alpha'])*r, 8), 'Vergleichswert_H_hi,p*||y_h||': HR['Vergleichswert_H_hi,p*||y_h||'],
           'old_f_mesh_<y_f,y_h>/delta (unbrauchbar)': P['pairing_upper_v']['bracket/delta']}
    print(par, res, flush=True)
    HR['yf_yh_corrected'] = res; json.dump(HR, open(f'/home/user/workspace/stufe5/HIGH_REST_{par}.json', 'w'), indent=1)
