"""Evaluate the new, cancellation-preserving residual on k96,...,k103.

The finite weighted sum is a contribution to a global formula, not the
uncomputed infinite residual tail. All source and cross errors are paid.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math,sys
import numpy as np
ap=argparse.ArgumentParser()
for name in ['root','responses','probe','cross','connection','out']:
 ap.add_argument('--'+name,type=Path,required=True)
args=ap.parse_args();ROOT=args.root.resolve()
sys.path[:0]=[str(ROOT/'work/tail-probe-2026-10-10/vendor'),str(ROOT/'work/galerkin84-2026-10-10')]
from flint import arb,arb_mat,ctx
from compute_inverse_energy_gate import af,box,ldl
from safe_serial import serial
ctx.prec=1024
def read(p):return json.loads(p.read_bytes())
def mat(a):return arb_mat([[box(v) for v in row] for row in a])
def rat(a):return arb_mat([[af(v) for v in row] for row in a])
def sub(a,rows,cols):return arb_mat([[a[i,j] for j in cols] for i in rows])
def tr(a):return sum((a[i,i] for i in range(a.nrows())),arb(0))
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def sym(a):return (a+a.transpose())/2
def floats(a):return np.array([[float(a[i,j].mid()) for j in range(a.ncols())] for i in range(a.nrows())])
g=read(args.probe);p=0 if g['parity']=='even' else 1;label=g['parity'].upper()
cp=read(args.cross);rpath=args.responses/f'RESPONSES_{label}.json';r=read(rpath)
refpath=ROOT/'work/direct-rest84-2026-10-11/REFINED_COMMON96.json'
inpath=ROOT/'work/direct-rest84-2026-10-11/REFINED_INPUT.json'
ref=read(refpath)['cases'][p];inp=read(inpath)['cases'][p]
conn=read(args.connection)['cases'][p]
assert cp['nprobe']==92 and cp['external_degrees']==list(range(96,104))
delta=af(r['delta']);rho=af(r['rho']);eta=af(r['eta']);beta=af(r['beta'])
ac=rat([[str(F(int(v),int(ref['inverse_congruence_denominator']))) for v in row] for row in ref['inverse_congruence_integer_matrix']])
XI=ac*ac.transpose()/(1-rho)
HB=rat([[str(F(int(v),int(ref['HB_denominator']))) for v in row] for row in ref['HB_integer_matrix']])
K=rat(r['K12_new_rational']);Ki=K.inv()
D=arb_mat([[1-rho if i==j and i<191 else K[i-191,j-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
T=beta*(D-rat(r['M_upper_rational']))
assert ldl(T)[2] is None
vF=mat(inp['old_certificate']['source_c_model'])-mat(inp['old_certificate']['source_Bh_model'])/delta
vK=sub(mat(g['source_c_model'])-mat(g['source_Bh_model'])/delta,range(191),range(1,9))
lF=ac.transpose()*vF;lK=ac.transpose()*vK
hFK=sub(mat(g['source_high_cross_model']),range(12),range(1,9))
hKK=sub(mat(g['Hgram']),range(1,9),range(1,9))
UFK=hFK/delta+lF.transpose()*lK/(1-rho)
UKK=hKK/delta+lK.transpose()*lK/(1-rho)
DFK=sub(mat(g['direct_F_cross_model']),range(12),range(1,9))
Cfin=DFK-UFK
CK=arb_mat([[lK[i,j] if i<191 else Cfin[i-191,j] for j in range(8)] for i in range(203)])
hJK=sub(mat(cp['Hgram']),range(84),range(84,92))
dJK=sub(mat(cp['direct_probe_model']),range(84),range(84,92))
SJK=(1-eta)*dJK-hJK/delta
X=rat(r['X84x203_rational'])
RK=CK.transpose()-SJK.transpose()*X
ds=[F(11,10)+sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(96,104)]
weighted=arb_mat([[RK[i,j]/af(ds[i]).sqrt() for j in range(203)] for i in range(8)])
small=sym(weighted*T.inv()*weighted.transpose())
eigen=float(np.linalg.eigvalsh(floats(small))[-1])
cap=F(math.ceil(eigen*10**8)+10,10**8)
assert ldl(af(cap)*eye(8)-small)[2] is None
# Independent existing-block calibration, including all 84 basis columns.
calibration=0
def compare(a,b):
 global calibration
 assert a.nrows()==b.nrows() and a.ncols()==b.ncols()
 for i in range(a.nrows()):
  for j in range(a.ncols()):
   # Different exact dyadic centres approximate the same exact J. The
   # explicit source/graph bounds pay these changes; this is a wide check.
   assert abs(a[i,j]-b[i,j])<af('1e-40'),('calibration',i,j)
   calibration+=1
compare(sub(mat(cp['Hgram']),range(84),range(84)),delta*mat(ref['H84_new_model']))
directpath=ROOT/f'work/direct-rest84-2026-10-11/DIRECT_REST_{label}_3072.json'
compare(sub(mat(cp['direct_probe_model']),range(84),range(84)),mat(read(directpath)['D84_direct_model']))
compare(sub(mat(cp['Hgram']),range(84,92),range(84,92)),hKK)
compare(sub(mat(cp['direct_probe_model']),range(84,92),range(84,92)),sub(mat(g['direct_probe_model']),range(1,9),range(1,9)))
compare(sub(mat(cp['source_c_model']),range(191),range(84,92)),sub(mat(g['source_c_model']),range(191),range(1,9)))
# Actual source feature error for K, with both finite and exterior errors.
cn=[box(v) for v in g['moment_basis_coefficients']]
Gm=arb_mat([[int(i==j)+cn[i]*cn[j] for j in range(191)] for i in range(191)])
ef=box(g['source_model_error_norm']);ehK=box(g['high_source_error_norm']);eb=box(g['old_coupling_error_norm'])
ek=ehK**2/delta+3*(tr(XI*Gm)*ef**2+tr(XI*HB)*ehK**2/delta**2+tr(XI)*eb**2*tr(mat(g['Hgram']))/delta**2)
eK=8*ek
EF=mat(ref['finite_feature_error_gram']);eF=tr(Ki*EF)
UFF=sub(mat(ref['U96_model']),range(12),range(12));tauF=tr(Ki*UFF);tauK=tr(UKK)
eD=af('1e-20')
eC=eK.sqrt()+(eF*tauK).sqrt()+(tauF*eK).sqrt()+(eF*eK).sqrt()+(af(12*8)*tr(Ki)).sqrt()*eD
# The NEW cross integration bounds the joint J/K source model error.
# A global bound also bounds either subblock, so no unproved per-column
# independence is assumed here.
ehcross=box(cp['high_source_error_norm'])
hJJ=sub(mat(cp['Hgram']),range(84),range(84))
hKKcross=sub(mat(cp['Hgram']),range(84,92),range(84,92))
eH=(tr(hJJ).sqrt()*ehcross+ehcross*tr(hKKcross).sqrt()+ehcross**2)/delta
eS=(1-eta)*af(84*8).sqrt()*eD+eH
x2=box(r['fixed_X_squared_HS_in_D_inverse_metric'])
eR=eC+eS*x2.sqrt()
# T>= scalar_budget D; hence the following full error is paid in T.
scalar=af(r['sufficient_complete_QR_normalized_budget'])
ew=eR/(af(ds[0])*scalar).sqrt()
charge=2*af(cap).sqrt()*ew+ew**2
actualcap=F(serial(af(cap)+charge,25)[1])
assert af(actualcap)>=af(cap)+charge
fprice=af(conn['full_finite_J_dual_Gram_D_normalized_upper'])/scalar
gprice=af('1e-250')/scalar
totalcap=F(serial(af(actualcap)+fprice+gprice,25)[1])
result={'status':'FINITE_EXTERIOR_RESIDUAL_CONTRIBUTION_ENCLOSED_GLOBAL_TAIL_OPEN',
 'parity':g['parity'],'external_degrees':list(range(96,104)),
 'new_R_on_K_model':RK,'weighted_residual_model':weighted,
 'T_normalized_small_Gram_model':small,'model_relative_to_directional_budget_upper':str(cap),
 'actual_exterior_C_D_metric_error':eC,'actual_SJK_error':eS,
 'actual_RK_D_metric_error':eR,'weighted_RK_T_metric_error':ew,
 'Gram_error_in_T_metric':charge,'true_eight_term_Gram_in_T_upper':str(actualcap),
 'true_finite_J_plus_eight_terms_and_geometry_in_T_upper':str(totalcap),
 'passes_directional_budget_on_computed_contributions':totalcap<1,
 'calibration_entries':calibration,'direct_entry_error':'1e-20',
 'remaining_required_inequality':'sum_{n>=104} R(k_n)^* R(k_n)/d_n <= T - Q_J_upper - Q96_103_upper - 1e-250 D',
 'full_weighted_residual_tail_computed':False,'full_remainder_certified':False,
 'bindings':{str(q.resolve()):hashlib.sha256(q.read_bytes()).hexdigest() for q in [args.probe,args.cross,rpath,refpath,inpath,args.connection]}}
args.out.write_text(json.dumps(serial(result,80),indent=2)+'\n')
print(label,'model eight-term budget ratio',eigen,'certified full price',float(totalcap),'calibrations',calibration,flush=True)
