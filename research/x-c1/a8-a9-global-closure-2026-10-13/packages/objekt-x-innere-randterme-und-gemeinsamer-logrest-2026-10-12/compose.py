"""Compose all three endpoint rows before testing the full log-model Gram."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,gzip,sys,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/new-responses84-2026-10-11')]
from compute import arb,arb_mat,ctx,af,box,mat,rat,read,tr,norm,serial,ldl,sub
ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=3072);ap.add_argument('--parity',choices=['even','odd'],required=True);args=ap.parse_args();ctx.prec=1536
p=['even','odd'].index(args.parity);label=args.parity.upper()
parent=ROOT/'work/direct-rest84-2026-10-11';n=read(parent/'REFINED_COMMON96.json')['cases'][p];inp=read(parent/'REFINED_INPUT.json')['cases'][p];oc=inp['old_certificate'];gj=inp['galerkin']
r=read(ROOT/f'work/new-responses84-2026-10-11/RESPONSES_{label}.json');ep=read(HERE/f'TRACES_{label}_{args.bits}.json');inner=read(HERE/'INNER_LOG_1536.json')['cases'][p]
review=ROOT/'work/log-tail-review-input-2026-10-12/Objekt-X-Aussenresidualpruefung-und-Logarithmischer-Randtail-2026-10-11'
outer=read(review/'data/OUTER_ENDPOINT.json')['cases'][p];gram=read(review/'data/LOG_TAIL_104.json')
oldpath=ROOT/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/remainder-integration-check-v2/originals/weighted-response/inputs/a8_model.json.gz'
old=json.loads(gzip.decompress(oldpath.read_bytes()))
aa=old['parities'][args.parity]['A'];A=arb_mat([[box([str(F(int(v),10**100)) for v in item]) for item in row] for row in aa])
a=3*arb(2).log()/2;b=arb(3).log();h=b-a;sqa=(2*a).sqrt();delta=af(r['delta']);rho=af(r['rho']);eta=af(r['eta'])
AC=arb_mat([[af(F(int(v),int(n['inverse_congruence_denominator']))) for v in row] for row in n['inverse_congruence_integer_matrix']]);X=rat(r['X84x203_rational'])
lowF=mat(inner['new_low_F_model']);phi=mat(inner['old_basis_physical_endpoint'])
wc=box(ep['old_endpoint_carrier_weight']);ww=arb_mat([[box(v) for v in ep['old_endpoint_raw_low_weights']]])
def row(v):return arb_mat([[box(x) for x in v]])
def extend(v):return arb_mat([[arb(0)]*191+[v[0,i] for i in range(12)]])
def project_trace(fin,car,cc):return (row(fin)-ww*cc-row(car)*wc)/sqa
hJ=project_trace([v[1] for v in ep['source_JY_endpoint_log_and_finite'][:84]],ep['source_JY_carrier'][:84],mat(gj['old_low_c_model']))
hF=project_trace([v[1] for v in ep['source_Z_endpoint_log_and_finite']]+[v[1] for v in ep['source_JY_endpoint_log_and_finite'][84:]],ep['source_Z_carrier']+ep['source_JY_carrier'][84:],mat(oc['source_c_model']))
hP=project_trace([v[1] for v in ep['old_Qphi_endpoint_log_and_finite']],ep['old_Qphi_carrier'],A)
k=phi-hP/delta;ka=k*AC
kt=arb_mat([[ka[0,j] if j<191 else -(ka*lowF)[0,j-191]/(1-rho) for j in range(203)]])
afin=kt+(hJ*X-extend(hF))/delta
alog=mat(inner['A_log_model']);jump=extend(mat(inner['finite12_inner_jump']))-(1-eta)*mat(inner['basis84_inner_jump'])*X
c1=-jump/2+afin/2-((-1)**p)*arb(2).log()/arb(8).sqrt()*alog
c2=alog/4;c3=mat(outer['outer_log_coefficient_1x203'])
C=arb_mat([[c[0,j] for j in range(203)] for c in [c1,c2,c3]])
K=rat(r['K12_new_rational']);Ki=K.inv();DM=arb_mat([[1-rho if i==j and i<191 else K[i-191,j-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
Di=DM.inv();TB=af(r['beta'])*(DM-rat(r['M_upper_rational']));G=rat(gram['full_tail_Gram_rational_upper']);d104=sum((arb(1)/i for i in range(1,105)),arb('1.1'))
AG=C*TB.inv()*C.transpose();lognorm=tr(G*AG)/d104

# Analytic error inputs. Smooth Gamma errors have endpoint and L2 bounds;
# finite-rank projection evaluation has norm <= 273 in normalized units.
Gm=arb_mat([[int(i==j)+box(ep['old_moment_coefficients_cn'][i])*box(ep['old_moment_coefficients_cn'][j]) for j in range(191)] for i in range(191)])
acl=AC*lowF
q=arb_mat([[AC[i,j] if j<191 else -acl[i,j-191]/(1-rho) for j in range(203)] for i in range(191)])
qnorm=tr(Gm*q*Di*q.transpose()).sqrt()
gammaold=af(old['Gamma_kernel_error_exact'])
e_qphi=af(600)*gammaold*qnorm # physical high-projected endpoint error
kaerror=af(600)*gammaold*tr(Gm*AC*AC.transpose()).sqrt()/delta
e_low=(norm(ka)+kaerror)*box(r['finite_feature_error_metric_trace']).sqrt()/(1-rho)
# Complete source errors before the old low projection; trace projection
# costs at most 273. The physical endpoint error is separately <=1e-28
# per source (see PROOF.txt; all gamma, moment and basis errors included).
ecF=mat(oc['joint_low_source_error_gram']);emF=tr(Ki*ecF).sqrt()
sourceJ=box(gj['source_model_error_norm'])
e_directJ=(af('1e-28')*arb(84).sqrt()+af(400)*sourceJ)*box(r['fixed_X_squared_HS_in_D_inverse_metric']).sqrt()
e_directF=af('1e-28')*(12*tr(Ki)).sqrt()+af(400)*emF
e_afin=e_low+(e_qphi+e_directJ+e_directF)/delta+af('1e-100')
e_c2=box(inner['C_left_log_squared_D_metric_error_bound'])+af('1e-100')
e_c1=e_afin/2+4*arb(2).log()/arb(8).sqrt()*e_c2+af('1e-100')
e_c3=af('1e-60')
e_log=G[0,0].sqrt()*e_c1+G[1,1].sqrt()*e_c2+G[2,2].sqrt()*e_c3
print(label,'full THREE-log model weighted trace /T',lognorm.str(18),'A_fin error /D',e_afin.str(18),'model X-log error /D',e_log.str(18),flush=True)
import numpy as np
from scipy.linalg import eigvals
z=np.linalg.eigvals(np.array([[float((G*AG)[i,j].mid()) for j in range(3)] for i in range(3)]));print(label,'exploratory log eigs /d104:',sorted(z/d104.mid().__float__()),flush=True)
out={'parity':args.parity,'bits':args.bits,'high_J84_finite_part_model':hJ,'high_F12_finite_part_model':hF,'high_Qphi191_finite_part_model':hP,
 'core_finite_low_inverse_row':ka,'A_fin_model':afin,'A_log_model':alog,'G_inner_jump':jump,'C_three_log_rows_model':C,
 'full_log_model_weighted_T_trace':lognorm,'old_q_polynomial_D_HS_norm':qnorm,'error_inputs':{'gamma160':gammaold,'old_q_action_endpoint':e_qphi,'core_finite_row_inverse_error':kaerror,'low_feature_coefficient':e_low,'J_source_trace':e_directJ,'F_source_trace':e_directF},
 'A_fin_D_metric_error_upper':e_afin,'C1_D_metric_error_upper':e_c1,'C2_D_metric_error_upper':e_c2,'C3_D_metric_error_upper':e_c3,'log_model_X_error_D_norm_upper':e_log,
 'full_remainder_certified':False,'endpoint_raw_projection_correction_charged':True}
(HERE/f'COMPOSED_{label}_{args.bits}.json').write_text(json.dumps(serial(out,80),indent=2)+'\n')
