"""Test the entire common finite block against a directed upper envelope.

Floating point proposes a ray only. All final ray values are directed balls.
This tests a specified comparison, not the actual Schur form.
"""
from pathlib import Path
from fractions import Fraction as F
import json,sys,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/compute-deps'),str(ROOT/'work/galerkin84-2026-10-10')]
from flint import arb,arb_mat,fmpq,ctx
from safe_serial import serial
import numpy as np
from scipy.linalg import eigh
ctx.prec=768
def af(x):
 q=F(x);return arb(fmpq(q.numerator,q.denominator))
def box(x):return af(x[0]).union(af(x[1]))
def mat(a):return arb_mat([[box(x) for x in r] for r in a])
def rat(a):return arb_mat([[af(x) for x in r] for r in a])
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def sym(a):return (a+a.transpose())/2
def sub(a,rows,cols):return arb_mat([[a[i,j] for j in cols] for i in rows])
def trace(a):return sum((a[i,i] for i in range(a.nrows())),arb(0))
def form(a,w):return (w.transpose()*a*w)[0,0]
def floats(a):return np.array([[float(a[i,j].mid()) for j in range(a.ncols())] for i in range(a.nrows())])
def freeze(a):return [[F(int((a[i,j].mid()*10**30).floor().unique_fmpz()),10**30) for j in range(a.ncols())] for i in range(a.nrows())]
def read(p):return json.loads(p.read_bytes())
review=HERE/'review-rebuild/BRIDGE_OBSTRUCTION_INPUT.json';inp=read(review)
bp=ROOT/'work/inherited/Objekt-X-Unendlicher-Rest-Vergleich-2026-10-09/work/infinite-tail-2026-10-09/FINITE_BRIDGE.json'
brs=read(bp)['cases'];rows=[]
for p,label in enumerate(['EVEN','ODD']):
 c=inp['cases'][p];br=brs[p+2]
 gp=ROOT/f'work/galerkin84-2026-10-10/GALERKIN_{label}_3072.json';g=read(gp)
 cp=ROOT/f'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/gamma-low-2026-10-09/CERTIFICATE_{label}_gamma224_tight_4096.json';cert=read(cp)
 dp=HERE/f'DIRECT_Y_{label}_3072.json';new=read(dp)
 K=rat(br['K12_lower']);Ki=K.inv();Um=mat(cert['model_upper_energy']);Eg=mat(cert['energy_model_error_gram'])
 epsF2=trace(Ki*Eg);tau=trace(Ki*Um);assert epsF2>0 and epsF2<af('3e-25')
 gamma=2*(epsF2*tau).sqrt()+epsF2
 U=rat(c['old_energy_upper']);cross=rat(c['C_U_centre'])+sub(U,range(4),range(4,12))
 Dz=rat(c['D_z_upper']);Dy=mat(new['D_Y_model'])+eye(8)*af(new['operator_error'])
 # Weighted Young bound for the inherited direct cross uncertainty.
 eps=af(c['C_error_norm_upper']);M=rat(c['C_error_metric'])
 Dup=arb_mat([[Dz[i,j]+eps*M[i,j] if i<4 and j<4 else
  cross[i,j-4] if i<4 else cross[j,i-4] if j<4 else
  Dy[i-4,j-4]+(eps if i==j else 0) for j in range(12)] for i in range(12)])
 Fu=sym(Dup-Um+gamma*K)
 C=mat(g['C84_model']);cl=sub(C,range(191),range(84));cz=sub(C,range(191,195),range(84));ce=sub(C,range(195,203),range(84))
 cy=ce+rat(br['P']).transpose()*cz
 Cf=arb_mat([[cz[i,j] if i<4 else cy[i-4,j] for j in range(84)] for i in range(12)])
 rho=af(cert['rho']);B=mat(g['B84_model'])+af('9999999999/10000000000')*mat(g['optional_positive_potential_comparison']['potential84_model'])
 R=sym(cl.transpose()*cl/(1-rho)+Cf.transpose()*Fu.inv()*Cf)
 ev,v=eigh(floats(R),floats(B));w=v[:,-1];w/=np.linalg.norm(w)
 wr=[[F(round(float(x)*10**12),10**12)] for x in w];wa=rat(wr)
 tr=freeze(-Fu.inv()*Cf*wa);ur=freeze(-cl*wa/(1-rho));t=rat(tr);u=rat(ur)
 q=form(Fu,t)+2*(t.transpose()*Cf*wa)[0,0]+(1-rho)*form(eye(191),u)+2*(u.transpose()*cl*wa)[0,0]+form(B,wa)
 w2=form(eye(84),wa);tk=form(K,t);dn=(1-rho)*form(eye(191),u)+tk
 errC=box(g['C84_D0_inverse_metric_error_norm']);errB=box(g['optional_positive_potential_comparison']['Bplus_operator_error_scalar'])
 charge=2*errC*(w2*dn).sqrt()+errB*w2
 # Additionally pay the finite-source change C0 -> C_common on this ray.
 H=form(mat(g['H84_model']),wa)+box(g['H84_operator_error_scalar'])*w2
 low=(form(cl.transpose()*cl,wa)/(1-rho)).sqrt()+box(g['weighted_low_error_squared']).sqrt()*w2.sqrt()
 Utail=H+low**2
 sourcecharge=2*(epsF2*Utail*tk).sqrt()
 qmax=q+charge+sourcecharge
 assert qmax<0,(label,str(qmax))
 print(label,'optimistic eigenvalue',ev[-1],'certified joint upper',qmax.str(18),'feature error relative',gamma.str(10),flush=True)
 rows.append({'parity':label.lower(),'w_rational':wr,'t_rational':tr,'u_rational':ur,
  'finite_source_error_squared_in_K_metric':epsF2,'model_feature_trace_in_K_metric':tau,
  'finite_energy_relative_error':gamma,'F12_upper_model':Fu,
  'optimistic_R84_model':R,'joint_ray_model':q,'joint_ray_error_charge':charge,
  'finite_source_cross_charge':sourcecharge,'joint_ray_upper':qmax,
  'fixed_comparison_impossible_by_finite_block_refinement_alone':True,
  'negative_actual_schur_witness':False,'full_remainder_certified':False,
  'bindings':{str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [review,bp,gp,cp,dp]}})
(HERE/'OPTIMISTIC_OBSTRUCTION.json').write_text(json.dumps(serial({'status':'PASS_COMMON_COMPARISON_UPPER_OBSTRUCTION','cases':rows,'full_remainder_certified':False},80),indent=2)+'\n')
