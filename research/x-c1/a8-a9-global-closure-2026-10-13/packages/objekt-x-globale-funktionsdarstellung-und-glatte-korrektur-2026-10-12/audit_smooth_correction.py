"""Full >=104 error from the moment adjoint and canonical T projection.

Conditional on the inherited domain, g, V and whole-shell residual bounds.
No Gamma/model error and no global Gram is certified here.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,json,sys,hashlib
HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=HERE.parents[1]);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
sys.path.insert(0,str(HERE));import interval_helpers as h
def read(p):return json.loads(p.read_bytes())
def up(v):return F(v[1])
def tr(v):return sum((v[i][i] for i in range(len(v))),F(0))
epsilon=F(4,64**104*factorial(104))
assert epsilon<F(1,10**353)
rows=[]
for label in ['EVEN','ODD']:
    path=a.root/f'work/new-responses84-2026-10-11/RESPONSES_{label}.json'
    r=read(path);c=r['full_coarse_inputs'];delta=F(r['delta'])
    Ki=h.inv(h.rat(r['K12_new_rational']));k=tr(Ki)
    tau=up(c['actual_finite_response_metric_trace']);mv=up(c['low_feature_HS_squared_WX'])
    xd=h.sqrtup(up(r['fixed_X_squared_HS_in_D_inverse_metric']))
    # ||T_h||<2, ||g||<1000, ||J||_WX<sqrt(2).
    W=h.sqrtup(mv)/1000*(1+h.sqrtup(tau))+F(2,1)/delta*(2000*h.sqrtup(F(2))*xd+h.sqrtup(delta*tau))
    # Physical complete Q_b F_i norm <2e10 and Q_b Lambda J norm <1e10.
    qG=2*10**10*h.sqrtup(12*k)+10**10*xd
    # mu>9/100, sqrt(2mu)<2; the domain lemma gives ||Q_a m||<1e4.
    chi=12*qG+F(500000,9)*W
    assert chi<10**30
    # Already verified on the whole shell, before the final T projection.
    Rcap=F(10**25)
    coarse=F(r['complete_coarse_QR_normalized_upper'])+1
    assert F(63,5)*coarse<Rcap**2
    omitted=epsilon*(chi+3*Rcap)
    assert omitted<F(1,10**300)
    rows.append({'parity':label.lower(),'core_W_D_dual_norm_upper':str(W),
     'moment_adjoint_coefficient_D_dual_norm_upper':str(chi),
     'whole_shell_residual_D_dual_norm_cap':str(Rcap),
     'joint_moment_adjoint_and_T_projection_high_error_upper':str(omitted),
     'joint_error_simplified_cap':'1e-300',
     'response_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    print(label,'PASS complete smooth correction above degree 103 <1e-300',flush=True)
out={'status':'PASS_COMPLETE_SMOOTH_CORRECTION_BOUND_CONDITIONAL_ON_INHERITED_OPERATORS',
 'moment_high_norm_upper':str(epsilon),'moment_high_norm_simple_cap':'1e-353','cases':rows,
 'global_model_Gram_computed':False,'remaining_global_model_error_certified':False,'full_remainder_certified':False}
a.out.write_text(json.dumps(out,indent=2)+'\n')
