"""Assemble ALL new residual rows on eight exterior functions before squaring.

These are exact test-function evaluations of the full residual, not a
truncation of any old high source. A finite obstruction is checked before
attempting an upper bound on the as-yet uncomputed infinite exterior tail.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys,hashlib,math
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'work/new-responses84-2026-10-11'))
from compute import af,box,mat,rat,eye,tr,sub,sym,norm,read,floats,fixed,ldl,serial,arb,arb_mat,ctx
import numpy as np
ctx.prec=1024
ap=argparse.ArgumentParser();ap.add_argument('--parity',choices=['even','odd'],required=True);ap.add_argument('--bits',type=int,default=3072);args=ap.parse_args()
label=args.parity.upper();p=0 if args.parity=='even' else 1
responsepath=ROOT/f'work/new-responses84-2026-10-11/RESPONSES_{label}.json';resp=read(responsepath)
refpath=ROOT/'work/direct-rest84-2026-10-11/REFINED_COMMON96.json';n=read(refpath)['cases'][p]
inputpath=ROOT/'work/direct-rest84-2026-10-11/REFINED_INPUT.json';inp=read(inputpath)['cases'][p]
probepath=ROOT/f'work/infinite-dual-review-input-2026-10-11/Objekt-X-Unendlicher-Dualrest-und-Aussenrichtungen-2026-10-11/data/PROBE_{label}_3072.json';probe=read(probepath)
crosspath=HERE/f'CROSS_{label}_{args.bits}.json';cross=read(crosspath)
gatespath=HERE/'ATTACHMENT_GATES.json';gates=read(gatespath)['cases'][p]
K=rat(resp['K12_new_rational']);Ki=K.inv();delta=af(resp['delta']);rho=af(resp['rho']);eta=af(resp['eta']);beta=af(resp['beta'])
D=arb_mat([[1-rho if i==j and i<191 else K[i-191,j-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
MU=rat(resp['M_upper_rational']);slack=sym(beta*(D-MU));assert ldl(slack)[2] is None
SI=slack.inv();X=rat(resp['X84x203_rational'])
AC=rat([[str(F(int(v),int(n['inverse_congruence_denominator']))) for v in row] for row in n['inverse_congruence_integer_matrix']])
XI=AC*AC.transpose()/(1-rho)
HB=rat([[str(F(int(v),int(n['HB_denominator']))) for v in row] for row in n['HB_integer_matrix']])
c=inp['old_certificate'];pg=inp['galerkin']
lF=AC.transpose()*(mat(c['source_c_model'])-mat(c['source_Bh_model'])/delta)
lK=AC.transpose()*(sub(mat(probe['source_c_model']),range(191),range(1,9))-sub(mat(probe['source_Bh_model']),range(191),range(1,9))/delta)
HFK=sub(mat(probe['source_high_cross_model']),range(12),range(1,9));HKK=sub(mat(probe['Hgram']),range(1,9),range(1,9))
UFK=HFK/delta+lF.transpose()*lK/(1-rho)
UKK=HKK/delta+lK.transpose()*lK/(1-rho)
CFK=sub(mat(probe['direct_F_cross_model']),range(12),range(1,9))-UFK
AK=arb_mat([[lK[i,j] if i<191 else CFK[i-191,j] for j in range(8)] for i in range(203)])
SJK=(1-eta)*mat(cross['direct_cross_model'])-mat(cross['full_high_cross_model'])/delta
RK=AK.transpose()-SJK.transpose()*X
# Full analytic error bounds for all 203 residual evaluations at once.
EF=mat(n['finite_feature_error_gram']);eF=tr(Ki*EF)
cn=[box(v) for v in probe['moment_basis_coefficients']]
Gm=eye(191)+arb_mat([[x*y for y in cn] for x in cn])
ef=box(probe['source_model_error_norm']);eh=box(probe['high_source_error_norm']);eb=box(probe['old_coupling_error_norm'])
Ebase=eh**2/delta+3*(tr(XI*Gm)*ef**2+tr(XI*HB)*eh**2/delta**2+tr(XI)*eb**2*tr(HKK)/delta**2)
eK=8*Ebase
UF= sub(mat(n['U96_model']),range(12),range(12));tauF=tr(Ki*UF);tauK=tr(UKK)
errC=eK.sqrt()+(eF*tauK).sqrt()+(tauF*eK).sqrt()+(eF*eK).sqrt()+(af(12*8)*tr(Ki)).sqrt()*af('1e-20')
ehJ=box(pg['high_source_error_norm']);hJtrace=tr(mat(n['H84_new_model']))*delta
errH=(hJtrace.sqrt()*eh+tr(HKK).sqrt()*ehJ+eh*ehJ)/delta
errS=(1-eta)*af(84*8).sqrt()*af('1e-20')+errH
x2=box(resp['fixed_X_squared_HS_in_D_inverse_metric'])
errR=errC+errS*x2.sqrt()
# ell_n differs from k_n only by a fully bounded rank-one moment correction.
mr=af(gates['full_canonical_X_residual_squared_norm_upper'])
ellprice=20*af('1e-352')*mr.sqrt();assert ellprice<af('1e-300')
errEll=errR+af('1e-300')
weights=[sum((F(1,k) for k in range(1,j+1)),F(11,10)) for j in range(96,104)]
DL=arb_mat([[af(weights[i]) if i==j else 0 for j in range(8)] for i in range(8)])
WH=arb_mat([[1/af(weights[i]).sqrt() if i==j else 0 for j in range(8)] for i in range(8)])
small=sym(WH*RK*SI*RK.transpose()*WH)
evals,evecs=np.linalg.eigh(floats(small));suggest=float(evals[-1]);ell=F(math.ceil(suggest*10**10)+2,10**10)
assert ldl(eye(8)*af(ell)-small)[2] is None
sigma=af(resp['sufficient_complete_QR_normalized_budget'])
upper_factor=(af(ell).sqrt()+errEll/(af(6)*sigma).sqrt())**2
# Fix one exact rational test direction in the NEW 203 coordinates.
w=arb_mat([[af(str(x))] for x in evecs[:,-1]])
aa=SI*RK.transpose()*WH*w;aa=aa/((aa.transpose()*D*aa)[0,0]).sqrt()
ar=fixed(aa,50);a=rat(ar);an=(a.transpose()*D*a)[0,0]
LKK=mat(cross['L_external_model']);Lprice=af('1e-50');Lup=LKK+eye(8)*Lprice
assert ldl(LKK-eye(8)*af(6))[2] is None
rv=RK*a;qk=(rv.transpose()*Lup.inv()*rv)[0,0]
# A fixed rational exterior test function gives a variational lower bound
# without trusting a numerical inverse or a finite-tail equality.
trational=fixed(Lup.inv()*rv,50);tt=rat(trational);tn=(tt.transpose()*tt)[0,0]
q_lower=2*(tt.transpose()*rv)[0,0]-(tt.transpose()*LKK*tt)[0,0]-Lprice*tn-2*errR*(an*tn).sqrt()
assert q_lower>0
mlo=(a.transpose()*mat(resp['M203_model'])*a)[0,0]-box(resp['M_error_relative_to_D203'])*an
strong_gap=mlo+q_lower/beta-an
fixed_upper_gap=q_lower-(a.transpose()*slack*a)[0,0]
print(label,'first-eight residual / directional budget: exploratory',suggest,'upper',upper_factor.str(15),flush=True)
print(label,'rational ray: complete dual lower',q_lower.str(15),'D norm',an.str(12),'strong beta-test gap',strong_gap.str(15),flush=True)
out={'status':'FIXED_BETA_RESIDUAL_TEST_REFUTED' if strong_gap>0 else 'CHOSEN_MUPPER_RESIDUAL_TEST_REFUTED' if fixed_upper_gap>0 else 'FIRST_EIGHT_COMPOSED_RESIDUAL_ROWS_COMPUTED',
 'parity':args.parity,'cross_bits':args.bits,'force_order':resp['force_order'],'external_degrees':list(range(96,104)),
 'AK_model':AK,'S_JK_model':SJK,'RK_8x203_model':RK,'RK_inverse_D_metric_error':errR,
 'R_ell_inverse_D_metric_error':errEll,'external_source_feature_error':eK,'external_force_error':errC,'S_JK_error':errS,
 'L_external_operator_error':'1e-50','model_eight_gram_over_directional_budget_upper':str(ell),
 'actual_first_eight_weighted_gram_over_directional_budget_upper':upper_factor,
 'rational_test_direction':ar,'rational_exterior_test_coefficients':trational,'direction_D_norm_squared':an,'direction_full_dual_lower_from_subspace':q_lower,
 'direction_actual_M_lower':mlo,'direction_exact_beta_residual_test_gap_lower':strong_gap,
 'direction_chosen_Mupper_test_gap_lower':fixed_upper_gap,
 'matrix_slack_definition':'beta*(D203-M_upper)',
 'first_eight_gram_fits_directional_budget':bool(upper_factor<1),
 'fixed_beta_residual_sufficient_test_refuted':bool(strong_gap>0),
 'full_exterior_tail_upper_computed':False,'negative_actual_Schur_witness':False,'full_remainder_certified':False,
 'bindings':{path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in [responsepath,refpath,inputpath,probepath,crosspath,gatespath]}}
(HERE/f'EXTERIOR_{label}_{args.bits}.json').write_text(json.dumps(serial(out,80),indent=2)+'\n')
