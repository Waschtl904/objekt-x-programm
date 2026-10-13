"""Pure rational reconstruction and complete three-log tail comparison.

Endpoint primitives are directed analytic integrations, bound inputs;
their independent precision comparison is not a substitute for the kernel lemma.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt,factorial
import argparse,json,gzip,hashlib,zipfile
import interval_helpers as h
HERE=Path(__file__).resolve().parent;ld=h.ld;S=ld.SCALE
pt=ld.point
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sq(v):return ld.mul(v,v)
def sm(a,v):return [[ld.mul(x,v) for x in r] for r in a]
def divm(a,v):return [[ld.div(x,v) for x in r] for r in a]
def row(v):return [[ld.interval(x) for x in v]]
def ext(v):return [[pt(0)]*191+v[0]]
def norm2(a):return sum(max(abs(h.lower(v)),abs(h.upper(v)))**2 for r in a for v in r)
def sqrtiv(x):
 assert x[0]>=0
 lo=isqrt(x[0]*S);hi=isqrt(x[1]*S)
 return lo,hi+(hi*hi<x[1]*S)
def logiv(n,k=240):
 z=F(n-1,n+1);v=2*sum((z**(2*j+1)/F(2*j+1) for j in range(k)),F(0))
 return ld.interval((v,v+2*z**(2*k+1)/F(2*k+1)/(1-z*z)))
def mellin(n,t):
 z=ld.div(t,pt(2));lead=pt(1)
 for k in range(1,n+1):lead=ld.mul(lead,ld.div(z,pt(2*k+1)))
 val=term=pt(1)
 for k in range(96):
  term=ld.mul(term,ld.div(sq(z),pt(2*(k+1)*(2*n+2*k+3))));val=ld.add(val,term)
 ratio=ld.div(sq(z),pt(2*97*(2*n+195)));err=ld.div(ld.mul(term,ratio),ld.sub(pt(1),ratio))
 return ld.mul(lead,ld.add(val,(0,err[1])))
def hyper(t,p):
 term=t if p else pt(1);val=term
 for j in range(100):
  k=2*j+p;term=ld.mul(term,ld.div(sq(t),pt((k+1)*(k+2))));val=ld.add(val,term)
 ratio=ld.div(sq(t),pt((202+p)*(201+p)));err=ld.div(ld.mul(term,ratio),ld.sub(pt(1),ratio))
 return ld.add(val,(0,err[1]))
def compare(x,y):
 if isinstance(x,list) and len(x)==2 and all(isinstance(v,str) for v in x):
  assert max(F(x[0]),F(y[0]))<=min(F(x[1]),F(y[1]));return 1
 assert len(x)==len(y);return sum(compare(v,w) for v,w in zip(x,y))
def main(responses,common,review,oldpath,out):
 assert __debug__
 nn=read(common/'REFINED_COMMON96.json')['cases'];ii=read(common/'REFINED_INPUT.json')['cases']
 old=json.loads(gzip.decompress(oldpath.read_bytes()));basis=read(review/'data/ENDPOINT_BASIS_INPUT.json')['cases']
 gate_name='Objekt-X-Zusammengesetzte-Aussenresiduen-und-Momentanschluss-2026-10-11'
 with zipfile.ZipFile(review/'inputs'/(gate_name+'.zip')) as zz:gate= json.loads(zz.read(gate_name+'/ATTACHMENT_GATES.json'))['cases']
 outer=read(review/'data/OUTER_ENDPOINT.json')['cases'];gram=read(review/'data/LOG_TAIL_104.json');G=h.rat(gram['full_tail_Gram_rational_upper']);Gi=h.inv(G)
 ln2=logiv(2);a=ld.mul(pt(F(3,2)),ln2);b=logiv(3);width=ld.sub(b,a);sqa=sqrtiv(ld.mul(pt(2),a));c=ld.div(ld.add(a,b),pt(2));d104=F(11,10)+sum((F(1,i) for i in range(1,105)),F(0));rows=[]
 # Analytic moment remainder: even the factorial majorant is <1e-800.
 mt=4*385*F(21,40)**384/F(factorial(384))/(1-F(21,40)/385)
 assert mt<F(1,10**800)
 for p,label in enumerate(['EVEN','ODD']):
  r=read(responses/f'RESPONSES_{label}.json');n=nn[p];inp=ii[p];oc=inp['old_certificate'];gj=inp['galerkin']
  ep=read(HERE/f'TRACES_{label}_3072.json');ep2=read(HERE/f'TRACES_{label}_4096.json');inner=read(HERE/'INNER_LOG_1536.json')['cases'][p];saved=read(HERE/f'COMPOSED_{label}_3072.json')
  assert sha(oldpath)==ep['bindings']['old']==ep2['bindings']['old']
  precision=sum(compare(ep[k],ep2[k]) for k in ['source_JY_endpoint_log_and_finite','source_JY_carrier','source_Z_endpoint_log_and_finite','source_Z_carrier','old_Qphi_endpoint_log_and_finite','old_Qphi_carrier','old_moment_coefficients_cn','old_endpoint_raw_low_weights','old_endpoint_carrier_weight'])
  assert precision==1244
  for e in [ep,ep2]:
   assert F(e['gamma224_error'][1])<F(1,10**34) and F(e['J_rounding'][1])<F(1,10**60) and F(e['Y_rounding'][1])<F(1,10**60)
   for check in e['independent_action_checks']:
    lo,hi=map(F,check['difference']);assert lo<=0<=hi and max(abs(lo),abs(hi))<F(1,10**60)
  rho=F(r['rho']);delta=F(r['delta']);eta=F(r['eta']);beta=F(r['beta']);X=h.pts(h.rat(r['X84x203_rational']))
  aci=[[int(v) for v in rr] for rr in n['inverse_congruence_integer_matrix']];acd=int(n['inverse_congruence_denominator']);AC=h.pts([[F(v,acd) for v in rr] for rr in aci])
  lowF=h.mmI(h.T(AC),h.add(h.im(oc['source_c_model']),h.sc(h.im(oc['source_Bh_model']),1/delta),-1));h.overlaps(lowF,h.im(inner['new_low_F_model']))
  # Independent reconstruction of exact inner jumps and physical old traces.
  Q=h.im(basis[p]['Q']);DD=h.pts(h.rat(basis[p]['D']));SS=h.pts(h.rat(basis[p]['S']))
  eleft=[[ld.mul(pt((-1)**k),sqrtiv(ld.div(pt(2*k+1),ld.mul(pt(2),width)))) for k in range(96)]]
  lc=[[ld.mul(ld.mul(sqrtiv(ld.mul(width,pt(F(2*k+1,2)))),hyper(ld.div(c,pt(2)),(k+p)%2)),mellin(k,ld.div(width,pt(2)))) for k in range(96)]]
  mu=ld.div(ld.add(hyper(a,1),ld.mul(pt((-1)**p),a)),pt(2));ma=hyper(ld.div(a,pt(2)),p)
  eq=h.mmI(h.add(eleft,sm(lc,ld.div(ma,mu))),Q)
  jj=h.add([eq[0][8:]],h.mmI([eq[0][:8]],DD));jy=h.mmI(eq,SS);jf=[[pt(0)]*4+jy[0]]
  h.overlaps(jj,h.im(inner['basis84_inner_jump']));h.overlaps(jf,h.im(inner['finite12_inner_jump']))
  phi=[[ld.div(ld.sub(sqrtiv(pt(2*k+1)),ld.mul(sqrtiv(pt(2*p+1)),ld.interval(ep['old_moment_coefficients_cn'][j]))),sqa) for j,k in enumerate(range(p+2,384,2))]]
  h.overlaps(phi,h.im(inner['old_basis_physical_endpoint']));pa=h.mmI(phi,AC)
  pal=h.mmI(pa,lowF);paq=[pa[0]+h.sc(pal,-1/(1-rho))[0]]
  alog=h.sc(h.add(h.add(h.mmI(jj,X),ext(jf),-1),paq),1/(2*delta));h.overlaps(alog,h.im(inner['A_log_model']))
  # Raw source endpoint logs are a separate normalization check.
  h.overlaps(divm(row([v[0] for v in ep['source_JY_endpoint_log_and_finite'][:84]]),sqa),h.sc(jj,F(1,2)))
  h.overlaps(divm(row([v[0] for v in ep['old_Qphi_endpoint_log_and_finite']]),sqa),h.sc(phi,F(-1,2)))
  # Exact raw-low projection identity, including the carrier ell_p.
  ww=row(ep['old_endpoint_raw_low_weights']);wc=ld.interval(ep['old_endpoint_carrier_weight'])
  def ht(fin,car,cc):return divm(h.add(h.add(row(fin),h.mmI(ww,cc),-1),sm(row(car),wc),-1),sqa)
  hj=ht([v[1] for v in ep['source_JY_endpoint_log_and_finite'][:84]],ep['source_JY_carrier'][:84],h.im(gj['old_low_c_model']))
  hf=ht([v[1] for v in ep['source_Z_endpoint_log_and_finite']]+[v[1] for v in ep['source_JY_endpoint_log_and_finite'][84:]],ep['source_Z_carrier']+ep['source_JY_carrier'][84:],h.im(oc['source_c_model']))
  amat=[[ld.interval([F(int(v),10**100) for v in vv]) for vv in rr] for rr in old['parities'][label.lower()]['A']]
  hp=ht([v[1] for v in ep['old_Qphi_endpoint_log_and_finite']],ep['old_Qphi_carrier'],amat)
  for value,key in [(hj,'high_J84_finite_part_model'),(hf,'high_F12_finite_part_model'),(hp,'high_Qphi191_finite_part_model')]:h.overlaps(value,h.im(saved[key]))
  ka=h.mmI(h.add(phi,h.sc(hp,1/delta),-1),AC);kal=h.mmI(ka,lowF);kt=[ka[0]+h.sc(kal,-1/(1-rho))[0]]
  afin=h.add(kt,h.sc(h.add(h.mmI(hj,X),ext(hf),-1),1/delta));h.overlaps(afin,h.im(saved['A_fin_model']))
  jump=h.add(ext(jf),h.sc(h.mmI(jj,X),1-eta),-1)
  prime8=ld.div(ld.mul(pt((-1)**p),ln2),sqrtiv(pt(8)))
  c1=h.add(h.sc(h.add(afin,jump,-1),F(1,2)),sm(alog,prime8),-1)
  c2=h.sc(alog,F(1,4));c3=h.im(outer[p]['outer_log_coefficient_1x203']);C=c1+c2+c3;h.overlaps(C,h.im(saved['C_three_log_rows_model']))
  # Bound all coefficient errors in D^{-1}. The coarse caps below are
  # deliberately wider than the Arb estimates, then paid in X, not H1.
  K=h.rat(r['K12_new_rational']);Ki=h.inv(K);g0=F(old['Gamma_kernel_error_exact']);traceAC=F(sum(v*v for rr in aci for v in rr),acd*acd)
  assert norm2(row(ep['old_moment_coefficients_cn']))<1
  normPhiAC=h.sqrtup(2*traceAC)
  acl=h.mmI(AC,lowF);aclgram=h.mmI(h.T(acl),acl)
  qbound=h.sqrtup(2*(traceAC/(1-rho)+h.pair_upper(aclgram,h.T(h.pts(Ki)))/(1-rho)**2))
  assert qbound<10**20 and h.sqrtup(norm2(ww))<273 and h.upper(wc)<3
  lowerr=h.sqrtup(F(r['finite_feature_error_metric_trace'][1]))
  eqlow=(h.sqrtup(norm2(ka))+600*g0*normPhiAC/delta)*lowerr/(1-rho)
  ecF=h.sqrtup(h.pair_upper(h.im(oc['joint_low_source_error_gram']),h.T(h.pts(Ki))))
  ej=(F(1,10**28)*h.sqrtup(F(84))+400*F(gj['source_model_error_norm'][1]))*h.sqrtup(F(r['fixed_X_squared_HS_in_D_inverse_metric'][1]))
  ef=F(1,10**28)*h.sqrtup(12*h.tr(Ki))+400*ecF
  eafin=eqlow+(600*g0*qbound+ej+ef)/delta+F(1,10**100)
  ec2=h.sqrtup(norm2(pa))*lowerr/(8*delta*(1-rho))+F(1,10**100)
  ec1=eafin/2+4*h.upper(ld.div(ln2,sqrtiv(pt(8))))*ec2+F(1,10**100)
  print(label,'directed coefficient errors',float(ec1),float(ec2),'qbound',float(qbound),'low trace',float(eqlow),flush=True)
  assert ec1<F(1,10**8) and ec2<F(1,10**10)
  elog=h.sqrtup(G[0][0])*F(1,10**8)+h.sqrtup(G[1][1])*F(1,10**10)+h.sqrtup(G[2][2])*F(1,10**60)
  theta=F(1,10**6);cap=F(1,500) if p==0 else F(1,250)
  DM=[[1-rho if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
  M=h.rat(r['M_upper_rational']);T=[[beta*(DM[i][j]-M[i][j]) for j in range(203)] for i in range(203)]
  # Young pays model/coefficient discrepancy, including all cross terms.
  top=[[(cap*d104*T[i][j]-(1+1/theta)*elog*elog*DM[i][j])/(1+theta) for j in range(203)] for i in range(203)]
  block=[[pt(top[i][j]) if i<203 and j<203 else C[j-203][i] if i<203 else C[i-203][j] if j<203 else pt(Gi[i-203][j-203]) for j in range(206)] for i in range(206)]
  proof=ld.positive(block)
  # Countercontrols: carrier and prime-8 contributions must be nonzero.
  carrier_effect=sm(row(ep['old_Qphi_carrier']),wc)
  assert max(max(abs(h.lower(v)),abs(h.upper(v))) for v in carrier_effect[0])>F(1,10)
  assert any(v[1]<0 or v[0]>0 for v in sm(alog,prime8)[0])
  wrong_c1=h.add(c1,sm(alog,prime8))
  try:h.overlaps(wrong_c1,c1)
  except AssertionError:pass
  else:raise AssertionError('omitted prime-8 term not detected')
  wrong_ka=h.mmI(h.add(phi,h.sc(h.add(hp,divm(carrier_effect,sqa)),1/delta),-1),AC)
  try:h.overlaps(wrong_ka,ka)
  except AssertionError:pass
  else:raise AssertionError('omitted raw carrier not detected')
  c8=F(1,5000) if p==0 else F(13,20000);jprice=F(gate[p]['basis84_dual_contribution_relative_to_D_upper'])
  reserve=1-c8-2*cap
  scalar=F(10920,2)*d104*(reserve*F(r['sufficient_complete_QR_normalized_budget'])-jprice-F(1,10**300))
  scalar_floor=F((scalar*10**12).numerator//(scalar*10**12).denominator,10**12);assert 0<scalar_floor<=scalar
  rows.append({'parity':label.lower(),'primitive_precision_overlaps':precision,'composed_log_coefficients_rebuilt':609,'core_finite_part_D_error_upper':str(eafin),'inner_log_coefficient_D_error_upper':str(ec1),'inner_squared_log_coefficient_D_error_upper':str(ec2),'three_log_full_weighted_tail_relative_to_T_upper':str(cap),'rational_joint_tail_proof':proof,'coefficient_errors_paid_in_X':True,'prime8_and_carrier_retained':True,'remaining_derivative_target_T_factor':str(reserve),'sufficient_E_g_tail_scalar_relative_to_D':str(scalar_floor),'regularized_derivative_Gram_computed':False,'full_remainder_certified':False})
  print(label,'PASS all three endpoint rows and full weighted log tail <',float(cap)*100,'% of T; 206 rational pivots',flush=True)
 powers=[2,3,4,5,7,8]
 assert all(q*z<=8 or q*z>=9 for q in powers for z in powers)
 assert all(q<=z or F(q*q,z*z)>=F(64,49)>F(9,8) for q in powers for z in powers)
 result={'status':'PASS_COMPLETE_THREE_LOG_COMPONENT_TAIL','cases':rows,'countercontrols':['omitted prime-8 term rejected','omitted raw carrier rejected'],'no_open_shell_prime_composition_cut':True,'analytic_operator_hypotheses_inherited':True,'full_remainder_certified':False,'tail_floor_1_over_20_certified':False}
 out.write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':
 ap=argparse.ArgumentParser()
 for k in ['responses','common','review','old','out']:ap.add_argument('--'+k,type=Path,required=True)
 x=ap.parse_args();main(x.responses,x.common,x.review,x.old,x.out)
