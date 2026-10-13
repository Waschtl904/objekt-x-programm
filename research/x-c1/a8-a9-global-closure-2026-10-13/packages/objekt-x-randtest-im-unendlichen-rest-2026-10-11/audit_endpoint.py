"""Standard-library directed audit of a nonpolynomial infinite-tail test."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,argparse
import interval_helpers as h
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ip(a):return h.pts(h.rat(a))
def integer_matrix(a,den):return h.pts([[F(int(v),int(den)) for v in row] for row in a])
def scalar(a):return h.ld.interval(a)
def sqnorm(a):return sum(max(abs(h.lower(v)),abs(h.upper(v)))**2 for row in a for v in row)
def step_geometry(q=F(1,16384)):
 # Exact rational Legendre polynomials and projected squared coefficients.
 ps=[[F(1)],[F(0),F(1)]]
 for n in range(2,104):
  v=[F(0)]+[(2*n-1)*x/n for x in ps[-1]]
  for j,x in enumerate(ps[-2]):v[j]-=F(n-1,n)*x
  ps.append(v)
 cut=-1+2*q;cs=[];ss=[];low=F(0);harm=F(0)
 for n,poly in enumerate(ps):
  val=sum((v*(cut**(j+1)-(-1)**(j+1))/(j+1) for j,v in enumerate(poly)),F(0))
  squared=val*val*F(2*n+1,4)/q;cs.append((val,squared));ss.append(squared)
  if n:harm+=F(1,n)
  low+=(harm+F(11,10))*squared
 # log 2 = 2 atanh(1/3), positive remainder; -log(1-q) similarly.
 z=F(1,3);m=128;l2=2*sum((z**(2*k+1)/(2*k+1) for k in range(m)),F(0));e2=2*z**(2*m+1)/((2*m+1)*(1-z*z))
 ml=sum((q**k/k for k in range(1,65)),F(0));me=q**65/(65*(1-q))
 lo=F(11,10)+7*l2+(1-q)*ml/(2*q)-low
 hi=F(11,10)+7*(l2+e2)+(1-q)*(ml+me)/(2*q)-low
 assert F(371232,100000)<lo<hi<F(371233,100000) and 1-sum(ss)>F(1,2)
 return cs,1-sum(ss),(lo,hi)
def audit(new,common):
 assert __debug__
 ns=read(common/'REFINED_COMMON96.json')['cases'];inputs=read(common/'REFINED_INPUT.json')['cases'];prior=read(new/'AUDIT.json')['cases']
 cs,mass,energy=step_geometry();rows=[]
 for p,label in enumerate(['EVEN','ODD']):
  gp=HERE/f'ENDPOINT_{label}_14_3072.json';g=read(gp);high=read(HERE/f'ENDPOINT_{label}_14_4096.json')
  a=read(HERE/f'ANALYSIS_{label}_14_3072.json');d=read(new/f'RESPONSES_{label}.json');n=ns[p];inp=inputs[p]
  boundpaths=[gp,new/f'RESPONSES_{label}.json',common/'REFINED_COMMON96.json',common/'REFINED_INPUT.json']
  assert a['bindings']=={x.name:sha(x) for x in boundpaths}
  assert g['bindings']==high['bindings'] and g['cut_power']==high['cut_power']==14
  comparisons=0
  matrixfields=['source_c_model','source_Bh_model','H_J_test_model','H_F_test_model','direct_J_test_model','direct_F_test_model']
  for key in matrixfields:h.overlaps(h.im(g[key]),h.im(high[key]));comparisons+=sum(map(len,g[key]))
  for key in ['mass_outside','L_step_exact_model','L_outside_exact_model','H_test_model']:
   x,y=map(scalar,[g[key],high[key]]);assert max(x[0],y[0])<=min(x[1],y[1]);comparisons+=1
  assert F(g['mass_outside'][0])<=mass<=F(g['mass_outside'][1])
  assert max(energy[0],F(g['L_outside_exact_model'][0]))<=min(energy[1],F(g['L_outside_exact_model'][1]))
  for (v,ss),bounds in zip(cs,g['step_projection_coefficients']):
   rt=h.sqrtup(ss);lo=rt-F(1,10**100);interval=(lo,rt) if v>=0 else (-rt,-lo)
   assert max(interval[0],F(bounds[0]))<=min(interval[1],F(bounds[1]));comparisons+=1
  assert F(g['working_step_projection_rounding'][1])<=F(1,10**80)
  rho=F(d['rho']);delta=F(d['delta']);eta=F(d['eta']);beta=F(d['beta']);K=h.rat(d['K12_new_rational']);Ki=h.inv(K);kii=h.pts(Ki)
  X=ip(d['X84x203_rational']);AC=integer_matrix(n['inverse_congruence_integer_matrix'],n['inverse_congruence_denominator'])
  old=inp['old_certificate'];pg=inp['galerkin']
  lF=h.mmI(h.T(AC),h.add(h.im(old['source_c_model']),h.sc(h.im(old['source_Bh_model']),1/delta),-1))
  lk=h.mmI(h.T(AC),h.add(h.im(g['source_c_model']),h.sc(h.im(g['source_Bh_model']),1/delta),-1))
  UFK=h.add(h.sc(h.im(g['H_F_test_model']),1/delta),h.sc(h.mmI(h.T(lF),lk),1/(1-rho)))
  AK=lk+h.add(h.im(g['direct_F_test_model']),UFK,-1)
  SJ=h.add(h.sc(h.im(g['direct_J_test_model']),1-eta),h.sc(h.im(g['H_J_test_model']),1/delta),-1)
  R=h.add(h.T(AK),h.mmI(h.T(SJ),X),-1)
  h.overlaps(R,h.im(a['residual_model']));h.overlaps(AK,h.im(a['AK_model']));h.overlaps(SJ,h.im(a['S_JK_model']))
  # Complete high-source Cauchy bounds against the bound J and physical F
  # Grams are independent consistency checks of the new cross integrals.
  hfflo=F(g['H_test_model'][0]);assert hfflo>0
  for crosskey,oldgram,factor in [('H_J_test_model',n['H84_new_model'],delta),('H_F_test_model',old['source_h_gram_model'],F(1))]:
   for j,row in enumerate(g[crosskey]):
    maxcross=max(abs(F(v)) for v in row[0])
    assert maxcross**2 < hfflo*F(oldgram[j][j][0])*factor
  ci=[[int(v) for v in row] for row in n['inverse_congruence_integer_matrix']];cd=int(n['inverse_congruence_denominator'])
  assert all(ci[i][j]==0 for i in range(191) for j in range(i))
  xi=[[sum(ci[i][k]*ci[j][k] for k in range(max(i,j),191)) for j in range(191)] for i in range(191)]
  fac=F(1,cd**2)/(1-rho);tx=sum(xi[i][i] for i in range(191))*fac
  hb=[[int(v) for v in row] for row in n['HB_integer_matrix']];txh=F(sum(xi[i][j]*hb[j][i] for i in range(191) for j in range(191)),int(n['HB_denominator']))*fac
  acn=h.mmI(h.T(AC),[[scalar(v)] for v in g['moment_basis_coefficients']]);txgm=tx+sqnorm(acn)/(1-rho)
  ef=F(g['source_error_norm'][1]);eh=F(g['high_source_error_norm'][1]);eb=F(g['old_coupling_error_norm'][1]);hf=F(g['H_test_model'][1])
  eK=eh**2/delta+3*(txgm*ef**2+txh*eh**2/delta**2+tx*eb**2*hf/delta**2)
  eF=h.pair_upper(h.im(n['finite_feature_error_gram']),h.T(kii));tauF=h.pair_upper(h.block(h.im(n['U96_model']),range(12),range(12)),h.T(kii))
  tauk=hf/delta+sqnorm(lk)/(1-rho)
  errC=h.sqrtup(eK)+h.sqrtup(eF*tauk)+h.sqrtup(tauF*eK)+h.sqrtup(eF*eK)+h.sqrtup(12*h.tr(Ki))*F(1,10**20)
  ehJ=F(pg['high_source_error_norm'][1]);hj=delta*h.itr(h.im(n['H84_new_model']))
  errH=(h.sqrtup(hj)*eh+h.sqrtup(hf)*ehJ+ehJ*eh)/delta
  errS=(1-eta)*h.sqrtup(F(84))*F(1,10**20)+errH
  assert F(63,5)*F(prior[p]['full_coarse_QR_normalized_upper_audited'])<10**50
  errR=errC+errS*h.sqrtup(F(d['fixed_X_squared_HS_in_D_inverse_metric'][1]))+F(1,10**50)
  D=[[F(1-rho) if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
  MU=h.rat(d['M_upper_rational']);T=[[beta*(D[i][j]-MU[i][j]) for j in range(203)] for i in range(203)]
  modelcap=F(483,10**6) if p==0 else F(1333,10**6)
  gram=h.sc(h.mmI(h.T(R),R),1/energy[0])
  pivots=h.ld.positive(h.add(h.sc(h.pts(T),modelcap),gram,-1))
  sigma=F(d['sufficient_complete_QR_normalized_budget'])
  cap=(h.sqrtup(modelcap)+errR*h.sqrtup(1/(sigma*energy[0])))**2
  simplecap=F(484,10**6) if p==0 else F(1334,10**6);assert cap<simplecap
  ray=ip(a['rational_force_direction']);an=h.upper(h.mmI(h.T(ray),h.mmI(h.pts(D),ray))[0][0]);bt=h.upper(h.mmI(h.T(ray),h.mmI(h.pts(T),ray))[0][0])
  rv=h.lower(h.mmI(R,ray)[0][0]);rl=rv-errR*h.sqrtup(an);assert rl>0
  qlo=rl*rl/energy[1];ratio=qlo/bt
  simplelo=F(4828,10**7) if p==0 else F(13323,10**7);assert ratio>simplelo
  # The above bounds apply ONLY to the rank-one necessary test. It is a
  # lower contribution to the whole tail, not an upper enclosure of it.
  rows.append({'parity':g['parity'],'new_interval_and_projection_comparisons':comparisons,
   'outside_mass_exact':str(mass),'Eplus_lower':str(energy[0]),'Eplus_upper':str(energy[1]),
   'composed_residual_entries_rebuilt':203,'actual_residual_error_upper':str(errR),'model_rank_one_LDL':pivots,
   'rank_one_to_budget_lower_on_rational_ray':str(simplelo),'rank_one_to_budget_uniform_upper':str(simplecap),
   'full_weighted_tail_lower_on_rational_ray':str(qlo),'full_weighted_tail_upper_computed':False,'full_remainder_certified':False})
  print(label,'PASS 203 actual residual entries; rank-one budget ratio between',str(simplelo),'and',str(simplecap),flush=True)
 return {'status':'PASS_NONPOLYNOMIAL_ENDPOINT_NECESSARY_TEST_FULL_TAIL_UPPER_OPEN','cases':rows,
  'inherited_operator_hypotheses':True,'full_remainder_certified':False,'negative_actual_Schur_witness':False}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--new',type=Path,required=True);ap.add_argument('--common',type=Path,required=True);args=ap.parse_args()
 out=audit(args.new,args.common);(HERE/'AUDIT_ENDPOINT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
