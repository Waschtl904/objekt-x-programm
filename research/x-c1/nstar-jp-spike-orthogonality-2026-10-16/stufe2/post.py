import json, sys
import mpmath as mp
from qnp_psi import *
g=setup(22); a8=g['a8']
res={}
for par in ['even','odd']:
    M=json.load(open(f'MESH_{par}_upper_v.json'))
    assert len(M['nodes'])==468, len(M['nodes'])
    psi=Psi(g,par,'upper_v'); sigma=psi.sigma; mu=psi.mu
    X=[mp.mpf(n['x']) for n in M['nodes']]; W=[mp.mpf(n['w']) for n in M['nodes']]
    Qr=[mp.mpf(n['Q_raw']) for n in M['nodes']]; PS=[mp.mpf(n['psi']) for n in M['nodes']]
    HG=[mp.mpf(n['H_gamma_psi']) for n in M['nodes']]; SP=[mp.mpf(n['S_psi']) for n in M['nodes']]
    mm=[psi.m(x) for x in X]
    # Quadraturkontrollen
    q_mpsi=sum(w*m*p for w,m,p in zip(W,mm,PS))
    lam_s=mp.mpf({'even':'196.271485','odd':'105.6955761'}[par])  # aus Stufe-1-Check (-lambda(s_t) = int_core m psi)
    q_log=sum(w*mp.log(a8-x) for w,x in zip(W,X)); ex_log=a8*(mp.log(a8)-1)
    q_mu=sum(w*m*m for w,m in zip(W,mm))
    # Pi8
    mom=sum(w*m*q for w,m,q in zip(W,mm,Qr))
    f=[q-m*mom/mu for q,m in zip(Qr,mm)]
    mom_after=sum(w*m*v for w,m,v in zip(W,mm,f))
    norm2=2*sum(w*v*v for w,v in zip(W,f))
    norm2_raw=2*sum(w*v*v for w,v in zip(W,Qr))
    norm2_HG=2*sum(w*v*v for w,v in zip(W,HG)); norm2_S=2*sum(w*v*v for w,v in zip(W,SP)); norm2_kpsi=2*sum(w*(g['kappa']*v)**2 for w,v in zip(W,PS))
    # skalierte Legendre-Koeffizienten <e_n, U f>, e_n = sqrt(2n+1) P_n, n = sigma mod 2
    coeffs={}
    Pn=[legendre_all(x/a8,62) for x in X]
    for n in range(sigma,62,2):
        coeffs[n]=mp.sqrt(2*mp.mpf(2*n+1)/a8)*sum(w*Pn[i][n]*f[i] for i,w in enumerate(W))
    low=sum(c*c for c in coeffs.values())
    # Profil
    prof=[]
    for frac in ['0','0.1','0.25','0.5','0.75','0.9','0.99','0.999']:
        x=a8*mp.mpf(frac); 
        pass
    res[par]={'mesh_nodes':len(X),'quadrature_checks':{
        'int_0^a8 m psi (Netz)':mp.nstr(q_mpsi,12),'-lambda(s_t) exakt (Stufe 1)':mp.nstr(lam_s,12),'Differenz':mp.nstr(q_mpsi-lam_s,3),
        'int log(a8-x) mesh - exact':mp.nstr(q_log-ex_log,3),'int m^2 mesh - mu':mp.nstr(q_mu-mu,3)},
        'moment_before_Pi8_int_m_Qraw':mp.nstr(mom,15),'moment_after_Pi8':mp.nstr(mom_after,3),
        'norm_H8_f_t':mp.nstr(mp.sqrt(norm2),12),'norm_H8_Qraw':mp.nstr(mp.sqrt(norm2_raw),12),
        'norm_H8_H_gamma_psi':mp.nstr(mp.sqrt(norm2_HG),10),'norm_H8_S_psi':mp.nstr(mp.sqrt(norm2_S),10),'norm_H8_kappa_psi':mp.nstr(mp.sqrt(norm2_kpsi),10),
        'moment_term_norm_|mom|sqrt(2mu)/mu':mp.nstr(abs(mom)*mp.sqrt(2*mu)/mu,10),
        'scaled_legendre_coeffs_<e_n,Uf>':{str(n):mp.nstr(c,12) for n,c in coeffs.items()},
        'sum_sq_coeffs_n<=61':mp.nstr(low,12),'norm2_f':mp.nstr(norm2,12),'high_part_norm2_n>61':mp.nstr(norm2-low,10),
        'f_values':[(mp.nstr(x,8),mp.nstr(v,10)) for x,v in zip(X,f)][::13]}
    print(par, json.dumps({k:v for k,v in res[par].items() if k not in ('scaled_legendre_coeffs_<e_n,Uf>','f_values')},indent=1))
    print('  coeffs:',[(n,mp.nstr(c,6)) for n,c in list(coeffs.items())[:12]])
json.dump(res,open('STUFE2_RESULTS.json','w'),indent=1)
