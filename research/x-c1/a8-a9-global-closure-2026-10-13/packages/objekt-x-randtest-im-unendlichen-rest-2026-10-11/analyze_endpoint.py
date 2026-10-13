from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'work/new-responses84-2026-10-11'))
from compute import af,box,mat,rat,eye,tr,sub,sym,norm,read,fixed,ldl,serial,arb,arb_mat,ctx
ctx.prec=1536
ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True);args=ap.parse_args()
g=read(args.input);p=0 if g['parity']=='even' else 1;label=g['parity'].upper()
rp=ROOT/f'work/new-responses84-2026-10-11/RESPONSES_{label}.json';d=read(rp)
np=ROOT/'work/direct-rest84-2026-10-11/REFINED_COMMON96.json';n=read(np)['cases'][p]
ip=ROOT/'work/direct-rest84-2026-10-11/REFINED_INPUT.json';inp=read(ip)['cases'][p]
K=rat(d['K12_new_rational']);Ki=K.inv();delta=af(d['delta']);rho=af(d['rho']);eta=af(d['eta']);beta=af(d['beta'])
X=rat(d['X84x203_rational']);D=arb_mat([[1-rho if i==j and i<191 else K[i-191,j-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
T=sym(beta*(D-rat(d['M_upper_rational'])));assert ldl(T)[2] is None
AC=rat([[str(F(int(v),int(n['inverse_congruence_denominator']))) for v in row] for row in n['inverse_congruence_integer_matrix']]);XI=AC*AC.transpose()/(1-rho)
HB=rat([[str(F(int(v),int(n['HB_denominator']))) for v in row] for row in n['HB_integer_matrix']])
old=inp['old_certificate'];pg=inp['galerkin']
lF=AC.transpose()*(mat(old['source_c_model'])-mat(old['source_Bh_model'])/delta)
lk=AC.transpose()*(mat(g['source_c_model'])-mat(g['source_Bh_model'])/delta)
UFK=mat(g['H_F_test_model'])/delta+lF.transpose()*lk/(1-rho)
CFK=mat(g['direct_F_test_model'])-UFK
AK=arb_mat([[lk[i,0] if i<191 else CFK[i-191,0]] for i in range(203)])
SJ=(1-eta)*mat(g['direct_J_test_model'])-mat(g['H_J_test_model'])/delta
R=AK.transpose()-SJ.transpose()*X
eF=tr(Ki*mat(n['finite_feature_error_gram']));tauF=tr(Ki*sub(mat(n['U96_model']),range(12),range(12)))
cn=[box(v) for v in g['moment_basis_coefficients']];Gm=eye(191)+arb_mat([[x*y for y in cn] for x in cn])
ef=box(g['source_error_norm']);eh=box(g['high_source_error_norm']);eb=box(g['old_coupling_error_norm']);hff=box(g['H_test_model'])
eK=eh**2/delta+3*(tr(XI*Gm)*ef**2+tr(XI*HB)*eh**2/delta**2+tr(XI)*eb**2*hff/delta**2)
tauk=hff/delta+(lk.transpose()*lk)[0,0]/(1-rho)
errC=eK.sqrt()+(eF*tauk).sqrt()+(tauF*eK).sqrt()+(eF*eK).sqrt()+(af(12)*tr(Ki)).sqrt()*af('1e-20')
ehJ=box(pg['high_source_error_norm']);hj=delta*tr(mat(n['H84_new_model']))
errH=(hj.sqrt()*eh+hff.sqrt()*ehJ+ehJ*eh)/delta
errS=(1-eta)*af(84).sqrt()*af('1e-20')+errH
errR=errC+errS*box(d['fixed_X_squared_HS_in_D_inverse_metric']).sqrt()+af('1e-50')
# The serialized rounding enclosure is <=1e-80. The full unprojected
# residual norm is <1e25; 1e-50 pays rounding and the whole moment change.
E=box(g['L_outside_exact_model']);sigma=af(d['sufficient_complete_QR_normalized_budget'])
aa=T.inv()*R.transpose();model=(R*aa)[0,0]/E
ratio_upper=(model.sqrt()+errR/(sigma*E).sqrt())**2
aa=aa/(aa.transpose()*D*aa)[0,0].sqrt();ar=fixed(aa,60);a=rat(ar)
an=(a.transpose()*D*a)[0,0];bt=(a.transpose()*T*a)[0,0]
rv=(R*a)[0,0];rl=abs(rv)-errR*an.sqrt();assert rl>0
qlo=rl**2/E
ratio_lower=qlo/bt
Mlower=(a.transpose()*mat(d['M203_model'])*a)[0,0]-box(d['M_error_relative_to_D203'])*an
stronggap=Mlower+(qlo-af('1e-250')*an)/beta-an
out={'status':'FINITE_BETA_RESIDUAL_CRITERION_REFUTED' if stronggap>0 else 'LOCALIZED_INFINITE_TAIL_TEST_EVALUATED',
 'parity':g['parity'],'cut_power':g['cut_power'],'bits':g['bits'],'residual_model':R,'AK_model':AK,'S_JK_model':SJ,
 'complete_residual_error_D_inverse_metric':errR,'L_outside_energy':E,'model_rank_one_gram_budget_ratio':model,
 'actual_rank_one_gram_budget_ratio_upper':ratio_upper,'rational_force_direction':ar,
 'direction_D_norm_squared':an,'direction_budget':bt,'direction_full_weighted_tail_lower':qlo,
 'direction_weighted_tail_to_budget_ratio_lower':ratio_lower,'direction_actual_M_lower':Mlower,
 'direction_beta_test_gap_lower':stronggap,'source_feature_error':eK,'force_error':errC,'S_cross_error':errS,
 'full_weighted_tail_upper_computed':False,'negative_actual_Schur_witness':False,'full_remainder_certified':False,
 'bindings':{x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in [args.input,rp,np,ip]}}
dest=HERE/f'ANALYSIS_{label}_{g["cut_power"]}_{g["bits"]}.json';dest.write_text(json.dumps(serial(out,80),indent=2)+'\n')
print(label,'outside mass',box(g['mass_outside']).str(12),'outside energy',E.str(12),flush=True)
print(label,'infinite-tail rank-one test / full budget:',ratio_lower.str(14),'to',ratio_upper.str(14),'strong gap',stronggap.str(14),flush=True)
