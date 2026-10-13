"""New physical 203-row Galerkin responses and a complete coarse residual bound.

All matrices refer to the new common inverse majorant. No old responses or
P-residualized rows are reused. Analytic hypotheses are listed in PROOF.txt.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,math,sys
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/compute-deps')]
from flint import arb,arb_mat,fmpq,ctx
from safe_serial import serial
import numpy as np
from scipy.linalg import eigh

def ldl(a):
 n=a.nrows();l=[[arb(0) for _ in range(n)] for _ in range(n)];ds=[]
 for i in range(n):
  d=a[i,i]-sum((l[i][k]**2*ds[k] for k in range(i)),arb(0))
  if not d>0:return None,ds,d
  ds.append(d);l[i][i]=arb(1)
  for j in range(i+1,n):l[j][i]=(a[j,i]-sum((l[j][k]*l[i][k]*ds[k] for k in range(i)),arb(0)))/d
 return l,ds,None

def af(v):
 q=F(v);return arb(fmpq(q.numerator,q.denominator))
def box(v):return af(v[0]).union(af(v[1]))
def mat(a):return arb_mat([[box(v) for v in row] for row in a])
def rat(a):return arb_mat([[af(v) for v in row] for row in a])
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def tr(a):return sum((a[i,i] for i in range(a.nrows())),arb(0))
def sub(a,ii,jj):return arb_mat([[a[i,j] for j in jj] for i in ii])
def sym(a):return (a+a.transpose())/2
def norm(a):return sum((abs(a[i,j]).upper()**2 for i in range(a.nrows()) for j in range(a.ncols())),arb(0)).sqrt()
def read(p):return json.loads(p.read_bytes())
def floats(a):return np.array([[float(a[i,j].mid()) for j in range(a.ncols())] for i in range(a.nrows())])
def fixed(a,digits=60):
 den=10**digits
 return [[str(F(int((a[i,j].mid()*den).floor().unique_fmpz()),den)) for j in range(a.ncols())] for i in range(a.nrows())]
def lower(a,digits=60):
 vals=serial(sym(a),digits);n=len(vals);den=10**digits
 mid=[[sum(map(F,v))/2 for v in row] for row in vals]
 out=[[F(round(mid[i][j]*den),den) for j in range(n)] for i in range(n)]
 for i in range(n):
  radius=sum(max(abs(F(vals[i][j][0])-out[i][j]),abs(F(vals[i][j][1])-out[i][j])) for j in range(n))
  out[i][i]-=F(math.ceil(radius*den),den)
 return [[str(v) for v in row] for row in out]
def ceilgrid(x,digits=12):
 z=F(serial(x,digits+10)[1]);den=10**digits
 return F(math.ceil(z*den),den)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--parent',type=Path,default=ROOT/'work/direct-rest84-2026-10-11');ap.add_argument('--bits',type=int,default=768);ap.add_argument('--suffix',default='');args=ap.parse_args()
 ctx.prec=args.bits;parent=args.parent
 paths={name:parent/name for name in ['REFINED_COMMON96.json','REFINED_INPUT.json','AUDIT.json']}
 ndata=read(paths['REFINED_COMMON96.json']);source=read(paths['REFINED_INPUT.json']);audit=read(paths['AUDIT.json'])
 delta=F(18219,10000);eta=F(1,10**10);beta=F(20209999981781,182190000000000)
 summaries=[]
 for p,label in enumerate(['EVEN','ODD']):
  print(label,'constructing sharp finite metric and new responses',flush=True)
  n=ndata['cases'][p];g=source['cases'][p]['galerkin'];dp=parent/f'DIRECT_REST_{label}_3072.json';d=read(dp)
  rho=F(n['rho']);G=rat(n['G96_rational']);Kold=sub(G,range(12),range(12));U=mat(n['U96_model'])
  # Use the independent rational auditor's (slightly larger) full error price.
  gamma=F(audit['cases'][p]['new_energy_relative_error_upper'])
  Kraw=sub(mat(n['D96_lower_model'])-U-af(gamma)*G,range(12),range(12))
  Krat=lower(Kraw);K=rat(Krat);Ki=K.inv();assert ldl(K)[2] is None
  D203=arb_mat([[af(1-rho) if i==j and i<191 else K[i-191,j-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
  Di=arb_mat([[1/af(1-rho) if i==j and i<191 else Ki[i-191,j-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
  low=mat(n['low_feature_J84_model']);cross=mat(n['finite_cross_C84_new_model'])
  C=arb_mat([[low[i,j] if i<191 else cross[i-191,j] for j in range(84)] for i in range(203)])
  H=mat(n['H84_new_model']);B=sym((1-af(eta))*mat(d['D84_direct_model'])-H)
  eh=box(g['high_source_error_norm']);htrace=tr(H)*af(delta)
  Herr=(2*htrace.sqrt()*eh+eh**2)/af(delta)
  Berr=(1-af(eta))*af(d['D84_operator_error'])+Herr
  # Complete 96-source energy feature error, split into F and J blocks.
  # EJ is deliberately used 84 times, matching the certified blockwise bound.
  EF=mat(n['finite_feature_error_gram']);eF=tr(Ki*EF);eJ=84*box(n['tail_feature_error_scalar'])
  tauF=tr(Ki*sub(U,range(12),range(12)));tauJ=tr(sub(U,range(12,96),range(12,96)))
  errcross=(eF*tauJ).sqrt()+(tauF*eJ).sqrt()+(eF*eJ).sqrt()
  directerr=(af(12*84)*tr(Ki)).sqrt()*af('1e-25')
  Cerr=eJ.sqrt()+errcross+directerr
  R=sym(C.transpose()*Di*C)
  vals=eigh(floats(R),floats(B),eigvals_only=True)
  ell=F(math.ceil(float(vals[-1])*10**12)+2,10**12)
  assert ldl(af(ell)*B-R)[2] is None
  be=np.linalg.eigvalsh(floats(B));blo=F(math.floor(be[0]*10**8)-2,10**8);bhi=F(math.ceil(be[-1]*10**8)+2,10**8)
  assert ldl(B-eye(84)*(af(blo)+Berr))[2] is None
  assert ldl(eye(84)*(af(bhi)-Berr)-B)[2] is None
  Xrat=fixed(B.inv()*C.transpose());X=rat(Xrat);V=sym(X*Di*X.transpose());x2=tr(V)
  M=sym(C*X+X.transpose()*C.transpose()-X.transpose()*B*X)
  eM=2*x2.sqrt()*Cerr+x2*Berr
  # Fixed rational upper matrix: preserve directions for a sharper next test.
  Mrup=[[-F(v) for v in row] for row in lower(-M,75)]
  for i in range(203):Mrup[i][i]+=F(1,10**55)
  emcap=F(serial(eM,40)[1]);Dup=[[F(1-rho) if i==j and i<191 else F(Krat[i-191][j-191]) if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
  Mupper=[[str(Mrup[i][j]+emcap*Dup[i][j]) for j in range(203)] for i in range(203)]
  roundingprice=norm(rat(Mrup)-M)*tr(Di)
  upper=ceilgrid(af(ell)+af(emcap)+roundingprice);budget=beta*(1-upper)
  assert upper<1 and budget>0
  gres=norm(C.transpose()-B*X)
  # Coarse FULL formdual estimate, including every outside-basis component.
  # The graph-norm bound ||q J|| <= 10^10 is proved in PROOF.txt.
  Ac=arb_mat([[af(F(int(v),int(n['inverse_congruence_denominator']))) for v in row] for row in n['inverse_congruence_integer_matrix']])
  XI=Ac*Ac.transpose()/af(1-rho);HB=arb_mat([[af(F(int(v),int(n['HB_denominator']))) for v in row] for row in n['HB_integer_matrix']])
  tx=tr(XI);txh=tr(XI*HB);tiny=af('1e-12')
  MV=2*10**6*(2*tx+(1+tiny)*txh/af(delta**2));MH=(1+tiny)*10**6/af(delta);MU=MH+MV
  tauActual=(tauF.sqrt()+eF.sqrt())**2
  A2=MV+af('96e20')*tr(Ki)+2*tauActual*MU
  # ||J||_{ell2 -> WX}<sqrt(2); H norm <= MH, qJ graph bound 1e10.
  SJ=(1-af(eta))*af(10**10)+2*MH
  coarse=(A2.sqrt()+SJ*x2.sqrt())**2/af('4.2')
  coarsecap=ceilgrid(coarse,0)
  assert af(coarsecap)>=coarse and coarsecap>beta
  # Riesz representers are defined exactly in PROOF.txt; no sampled tail is used.
  record={'status':'NEW_RESPONSES_AND_FINITE_BUDGET_COARSE_FULL_RESIDUAL_INCONCLUSIVE','parity':label.lower(),'bits':args.bits,
   'delta':str(delta),'eta':str(eta),'beta':str(beta),'rho':str(rho),'old_Young_parameter_documentation_correction':'1e-8 -> 1e-10',
   'K12_new_rational':Krat,'K12_lower_source':'top-left block of D96_lower-U96-gamma_audit G, rounded down',
   'new_common_energy_error_gamma':str(gamma),'D203_definition':'diag((1-rho) I191,K12_new)',
   'force_order':'191 new low features followed by 12 physical cross rows; no P residualization',
   'C203x84_model':C,'C_inverse_D_metric_error':Cerr,'finite_feature_error_metric_trace':eF,'tail_feature_error_trace_bound':eJ,
   'finite_model_feature_metric_trace':tauF,'tail_model_feature_trace':tauJ,'direct_cross_metric_error':directerr,
   'B84_model':B,'B84_operator_error':Berr,'H84_operator_error':Herr,
   'B84_lower_scalar':str(blo),'B84_upper_scalar':str(bhi),'B84_condition_number_upper':str(bhi/blo),
   'R84_model':R,'model_loss_generalized_eigenvalue_upper':str(ell),
   'X84x203_rational':Xrat,'M203_model':M,'M_error_relative_to_D203':eM,
   'fixed_X_squared_HS_in_D_inverse_metric':x2,'finite_Galerkin_residual_model_Frobenius':gres,
   'M_upper_rational':Mupper,'M_upper_definition':'outward rational model upper + upper(eM) D203',
   'M_error_coefficient_rational':str(emcap),
   'M_upper_rounding_relative_to_D203':roundingprice,
   'directional_QR_budget_definition':'beta * (D203 - M_upper_rational), positive definite; preferable to its scalar lower bound',
   'M_actual_normalized_upper_scalar':str(upper),'sufficient_complete_QR_normalized_budget':str(budget),
   'full_coarse_inputs':{'inverse_trace':tx,'inverse_HB_trace':txh,'low_feature_HS_squared_WX':MV,'high_response_norm_squared_WX':MH,
    'total_response_norm_squared_WX':MU,'actual_finite_response_metric_trace':tauActual,'A_HS_squared_WX_dual':A2,
    'qJ_operator_WX_dual_bound':'10000000000','SJ_operator_WX_dual_bound':SJ},
   'complete_coarse_QR_normalized_upper':str(coarsecap),'complete_coarse_QR_definition':'Q_R = scalar * D203; R* R_L R <= Q_R on exact T',
   'complete_coarse_bound_includes_outside_basis':True,'complete_coarse_bound_passes':False,
   'sharp_full_formdual_Gram_computed':False,'negative_actual_Schur_witness':False,'tail_floor_1_over_20_certified':False,'full_remainder_certified':False,
   'bindings':{name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in {**paths,dp.name:dp}.items()}}
  dest=HERE/f'RESPONSES_{label}{args.suffix}.json';dest.write_text(json.dumps(serial(record,75),indent=2)+'\n')
  summary={k:record[k] for k in ['parity','M_actual_normalized_upper_scalar','sufficient_complete_QR_normalized_budget','complete_coarse_QR_normalized_upper','model_loss_generalized_eigenvalue_upper','B84_condition_number_upper']}
  summaries.append(summary)
  print(label,'M/D <=',float(upper),'required QR/D <=',float(budget),'full coarse upper',float(coarsecap),flush=True)
 (HERE/f'SUMMARY{args.suffix}.json').write_text(json.dumps({'cases':summaries,'full_remainder_certified':False},indent=2)+'\n')
if __name__=='__main__':main()
