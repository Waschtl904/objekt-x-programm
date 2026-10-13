"""Exact endpoint formula for the inner squared logarithm; directed model.

The low-feature uncertainty is a separate coefficient error, never an H1 error.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/new-responses84-2026-10-11')]
from compute import arb,arb_mat,ctx,af,box,mat,rat,read,tr,norm,serial,ldl
ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=1536);args=ap.parse_args();ctx.prec=args.bits
parent=ROOT/'work/direct-rest84-2026-10-11'
nc=read(parent/'REFINED_COMMON96.json')['cases'];ni=read(parent/'REFINED_INPUT.json')['cases']
review=ROOT/'work/log-tail-review-input-2026-10-12/Objekt-X-Aussenresidualpruefung-und-Logarithmischer-Randtail-2026-10-11'
base=read(review/'data/ENDPOINT_BASIS_INPUT.json')['cases']
a=3*arb(2).log()/2;b=arb(3).log();h=b-a;mu=[(a.sinh()+a)/2,(a.sinh()-a)/2]
def mellin(n,t):
 z=t/2;lead=arb(1)
 for k in range(1,n+1):lead*=z/(2*k+1)
 v=t0=arb(1)
 for k in range(256):t0*=z*z/(2*(k+1)*(2*n+2*k+3));v+=t0
 ratio=z*z/(2*257*(2*n+515))
 return lead*(v+arb(0,(t0*ratio/(1-ratio)).upper()))
def blockright(row):return arb_mat([[arb(0)]*191+[row[0,j] for j in range(12)]])
rows=[]
for p,label in enumerate(['EVEN','ODD']):
 r=read(ROOT/f'work/new-responses84-2026-10-11/RESPONSES_{label}.json');n=nc[p];old=ni[p]['old_certificate']
 X=rat(r['X84x203_rational']);delta=af(r['delta']);rho=af(r['rho'])
 Q=mat(base[p]['Q']);D=rat(base[p]['D']);S=rat(base[p]['S'])
 Z=arb_mat([[D[i,j] if i<8 else int(i-8==j) for j in range(84)] for i in range(92)])
 J=Q*Z;Y=Q*S
 ea=arb_mat([[(-1)**k*((2*k+1)/(2*h)).sqrt() for k in range(96)]])
 lm=arb_mat([[(h*(2*k+1)/2).sqrt()*(((a+b)/4).cosh() if (k+p)%2==0 else ((a+b)/4).sinh())*mellin(k,h/2) for k in range(96)]])
 ma=(a/2).cosh() if p==0 else (a/2).sinh()
 jumpJ=(ea+lm*(ma/mu[p]))*J
 jumpY=(ea+lm*(ma/mu[p]))*Y
 jumpF=arb_mat([[arb(0)]*4+[jumpY[0,j] for j in range(8)]])
 phi=arb_mat([[((2*k+1)/(2*a)).sqrt()*(1-mellin(k,a)/mellin(p,a)) for k in range(p+2,384,2)]])
 AC=arb_mat([[af(F(int(v),int(n['inverse_congruence_denominator']))) for v in row] for row in n['inverse_congruence_integer_matrix']])
 lowF=AC.transpose()*(mat(old['source_c_model'])-mat(old['source_Bh_model'])/delta)
 pa=phi*AC
 paq=arb_mat([[pa[0,j] if j<191 else -(pa*lowF)[0,j-191]/(1-rho) for j in range(203)]])
 alog=(jumpJ*X-blockright(jumpF)+paq)/(2*delta)
 c2=alog/4
 K=rat(r['K12_new_rational']);Di=arb_mat([[1/(1-rho) if i==j and i<191 else K.inv()[i-191,j-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
 DM=Di.inv();TB=af(r['beta'])*(DM-rat(r['M_upper_rational']))
 lowerr=box(r['finite_feature_error_metric_trace']).sqrt()
 err=norm(pa)*lowerr/(8*delta*(1-rho))
 print(label,'norm(phi AC)',norm(pa).str(16),'c2 D-norm',(c2*Di*c2.transpose())[0,0].sqrt().str(16),'c2 coefficient error D',err.str(16),flush=True)
 print(label,'c2 log^2 isolated full weighted /T', (mat(read(review/'data/LOG_TAIL_104.json')['full_tail_Gram_intervals'])[1,1]/(sum((arb(1)/k for k in range(1,105)),arb('1.1')))*(c2*TB.inv()*c2.transpose())[0,0]).str(16),flush=True)
 rows.append({'parity':label.lower(),'basis84_inner_jump':jumpJ,'finite12_inner_jump':jumpF,'old_basis_physical_endpoint':phi,'old_endpoint_inverse_row':pa,'new_low_F_model':lowF,'A_log_model':alog,'C_left_log_squared_model':c2,'C_left_log_squared_D_metric_error_bound':err,'D_inverse_norm_squared_model':(c2*Di*c2.transpose())[0,0], 'T_inverse_norm_squared_model':(c2*TB.inv()*c2.transpose())[0,0], 'full_remainder_certified':False})
(HERE/f'INNER_LOG_{args.bits}.json').write_text(json.dumps(serial({'bits':args.bits,'a':a,'b':b,'cases':rows,'full_remainder_certified':False},80),indent=2)+'\n')
