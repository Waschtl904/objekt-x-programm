"""Rational symmetric-pencil gate and explicit small-matrix relaxation witnesses.

The alternatives are NOT claimed to arise from the original full operator.
See EXTREMAL_GATE.md for the exact list of constraints and scope.
"""
from pathlib import Path
import argparse,hashlib,json,sys
from rational_tools import *
sys.set_int_max_str_digits(0)

def hull_order(lo,hi):
 out=scale(plus(lo,hi),F(1,2));delta=minus(hi,lo)
 assert all(delta[i][i][1]>=0 for i in range(2))
 for i in range(2):
  for j in range(2):
   radius=root(delta[i][i][1]*delta[j][j][1],True)/2
   out[i][j]=add(out[i][j],(-radius,radius))
 return out

def direct_pencil(r):
 g=matrix(r['canonical_basis_L2_Gram'])
 l=hull_order(matrix(r['energy_Loewner_lower_in_raw_basis']),matrix(r['energy_Loewner_upper_in_raw_basis']))
 positive2(l);b=plus(l,scale(g,17));positive2(b)
 z=hull_order(matrix(r['inverse_lower_family_in_raw_basis']),matrix(r['inverse_upper_family_in_raw_basis']))
 rr=plus(plus(l,scale(g,34)),scale(z,289))
 m=plus(plus(l,scale(g,34)),scale(mm(mm(g,inv2(l)),g),289))
 # det(M)=det(B)^2/det(L). This certifies the second Cholesky
 # pivot even if interval dependency spoils M22-M12^2/M11.
 dm=div(sq(det2(b)),det2(l));c=chol2(m,dm);ci=linv(c)
 k=mm(mm(ci,rr),tr(ci))
 # Intersect transpose entries: the exact congruence is symmetric.
 off=(max(k[0][1][0],k[1][0][0]),min(k[0][1][1],k[1][0][1]));assert off[0]<=off[1]
 delta=sub(k[0][0],k[1][1]);gap2=add(sq(delta),mul(pt(4),sq(off)))
 gap=(root(gap2[0]),root(gap2[1],True))
 return {'Cholesky_diagonal_intervals':[display(c[0][0]),display(c[1][1])],
         'K_diagonal_intervals':[display(k[0][0]),display(k[1][1])],
         'K12_interval':display(off),'K11_minus_K22_interval':display(delta),
         'eigenvalue_gap_interval':display(gap),'strict_gap_certified':gap[0]>0,
         'orientation_pair_contains_origin':delta[0]<=0<=delta[1] and off[0]<=0<=off[1]}

def point_input_factors(r):
 tl=symmetric_midpoint(r['trial_resolvent_lower']);th=symmetric_midpoint(r['trial_resolvent_upper'])
 inside(tl,r['trial_resolvent_lower'],'Tlo');inside(th,r['trial_resolvent_upper'],'Thi')
 interval_inside(tr(fine_chol(tl)),r['trial_resolvent_lower_factor'],'Tlo factor')
 interval_inside(tr(fine_chol(th)),r['trial_resolvent_upper_factor'],'Thi factor')
 ppositive(ps(th,tl))
 return tl,th

def candidate(r,source,key,parameters,kind):
 y=midpoint(r['annihilator_Y']);mc=midpoint(r['central_left'])
 for i in range(6):y[i][:6]=mc[i][:]
 for i in range(2):
  for j in range(2):
   cell=r['annihilator_Y'][4+i][6+j];radius=(F(cell[1])-F(cell[0]))/2
   y[4+i][6+j]+=radius*F(parameters[i][j])
 n=pc(pmm(pinv(mc),[row[6:] for row in y]),-1)+[[F(1),F(0)],[F(0),F(1)]]
 g=pmm(tr(n),n);sb=symmetric_midpoint(source['trials'][key.split('->')[1]]['physical_Ritz_matrix'])
 en=pmm(pmm(tr(n),sb),n)
 l=en
 tl,th=point_input_factors(r);z=pmm(pmm(tr(n),pc(pa(tl,th),F(1,2))),n)
 b=pa(l,pc(g,17));m=pmm(pmm(b,pinv(l)),b);rr=pa(pa(l,pc(g,34)),pc(z,289))
 if kind=='axis_one':
  target=m[0][1]*rr[0][0]/m[0][0]
  z[0][1]=z[1][0]=(target-l[0][1]-34*g[0][1])/289
 elif kind=='double':
  beta=rr[0][0]/m[0][0]
  z=pc(ps(ps(pc(m,beta),l),pc(g,34)),F(1,289))
 rr=pa(pa(l,pc(g,34)),pc(z,289))
 innerlo=pa(pc(tl,F(51,100)),pc(th,F(49,100)))
 innerhi=pa(pc(tl,F(49,100)),pc(th,F(51,100)))
 return {'Y':y,'N':n,'G':g,'EN':en,'L':l,'Z':z,'M':m,'R':rr,'innerlo':innerlo,'innerhi':innerhi}

def certify_candidate(c,r,source,key,prior):
 y,n,g,en,l,z,m,rr=[c[name] for name in ['Y','N','G','EN','L','Z','M','R']]
 inside(y,r['annihilator_Y'],'Y');inside(n,r['canonical_N'],'N');inside(g,r['canonical_basis_L2_Gram'],'G')
 assert pmm(y,n)==[[0,0] for _ in range(6)]
 res=pmm(y,midpoint(r['central_N']))
 for i in range(6):
  for j in range(2):assert abs(res[i][j])<=F(r['residual_absolute_bound'][i][j][1]),('directionwise residual',i,j)
 inside(en,r['trial_energy_on_N'],'EN')
 for a in [g,l,z,m,rr]:ppositive(a)
 positive2(minus(pmat(l),matrix(r['energy_Loewner_lower_in_raw_basis'])))
 positive2(minus(matrix(r['energy_Loewner_upper_in_raw_basis']),pmat(l)))
 assert en==l
 tl,th=point_input_factors(r);nu=F(source['trials'][key.split('->')[1]]['physical_complement_gap_lower_exact'])
 ppositive(ps(c['innerlo'],tl));ppositive(ps(th,c['innerhi']))
 ppositive(ps(z,pmm(pmm(tr(n),c['innerlo']),n)))
 ppositive(ps(pmm(pmm(tr(n),c['innerhi']),n),z))
 zl=ps(pmm(pmm(tr(n),tl),n),pc(en,1/nu**2));zh=pmm(pmm(tr(n),th),n)
 inside(zl,r['inverse_lower_family_in_raw_basis'],'Zlower family');inside(zh,r['inverse_upper_family_in_raw_basis'],'Zupper family')
 ppositive(ps(z,zl));ppositive(ps(zh,z))
 ppositive(ps(z,pmm(pmm(g,pinv(l)),g)))
 sb=symmetric_midpoint(source['trials'][key.split('->')[1]]['physical_Ritz_matrix'])
 ppositive(ps(z,pmm(pmm(tr(n),pinv(sb)),n)))
 ppositive(ps(c['innerlo'],pinv(sb)))
 theta=F(r['physical_energy_uniform_upper_exact']);floor=F(r['physical_energy_uniform_lower_exact'])
 ppositive(ps(pc(g,theta),l));ppositive(ps(l,pc(g,floor)))
 ppositive(ps(z,pc(g,F(r['physical_inverse_energy_uniform_lower_exact']))))
 ppositive(ps(pc(g,F(r['physical_inverse_energy_uniform_upper_exact'])),z))
 # G=N*N is an allowed zero loss in the supplied Gram/projector bound.
 assert g==pmm(tr(n),n)
 o=tr(linv(chol2(pmat(g))))
 interval_inside(mm(mm(tr(o),pmat(l)),o),r['physical_energy_entries'],'physical L')
 zp=mm(mm(tr(o),pmat(z)),o)
 interval_inside(zp,r['physical_inverse_energy_entries'],'physical Z')
 for i in range(2):
  low,high=map(F,prior['physical_inverse_energy_diagonal_intervals'][i])
  assert low<=zp[i][i][0]<=zp[i][i][1]<=high
 # Same explicit dual-probe constraints used to form the old energy floor.
 w=midpoint(r['dual_probe_coefficients']);overlap=pmm(tr(w),n);probe=pmm(pmm(tr(w),th),w)
 inside(overlap,r['dual_overlap_enclosure'],'dual overlap')
 inside(probe,r['dual_probe_inverse_upper'],'dual inverse upper')
 ppositive(ps(l,pmm(pmm(tr(overlap),pinv(probe)),overlap)))
 return True

def spectral_certificate(c,kind):
 r,m=c['R'],c['M'];mi=pinv(m)
 # Generalized characteristic polynomial; roots are real by positive congruence.
 t=sum(pmm(mi,r)[i][i] for i in range(2));d=(r[0][0]*r[1][1]-r[0][1]**2)/(m[0][0]*m[1][1]-m[0][1]**2)
 disc=t*t-4*d;assert disc>=0
 gaplo=root(disc);gaphi=root(disc,True);bp=((t+gaplo)/2,(t+gaphi)/2)
 out={'beta_plus':display(bp),'gap':display((gaplo,gaphi))}
 if kind=='double':
  beta=r[0][0]/m[0][0];assert r==pc(m,beta) and disc==0
  out.update({'double_eigenvalue_exact':True,'every_direction_maximizes':True})
  out['beta_exact']=str(beta)
 elif kind=='axis_one':
  beta=r[0][0]/m[0][0];assert r[1][0]==beta*m[1][0]
  other=t-beta;assert beta>other>0
  out.update({'unique_maximizer_ray':'(1,0)','double_eigenvalue_exact':False})
 else:
  # Set x2=1. The first row gives x1=(beta M12-R12)/(R11-beta M11).
  slope=div(sub(mul(bp,pt(m[0][1])),pt(r[0][1])),sub(pt(r[0][0]),mul(bp,pt(m[0][0]))))
  assert gaplo>0 and ab(slope)<F(1,50)
  out.update({'maximizer_x1_over_x2':display(slope),'absolute_slope_below_one_fiftieth':True})
 return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();base=Path(__file__).resolve().parent
 bindings=json.loads((base/'input_bindings.json').read_bytes());data={}
 for name,h in bindings['sha256'].items():
  raw=(base/'inputs'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==h;data[name]=json.loads(raw)
 pri,cross,source,mech,old=data['primary.json'],data['crosscheck.json'],data['outer_primary.json'],data['mechanism_verification.json'],data['resolvent_verification.json']
 assert pri['source_commit']==cross['source_commit']==mech['source_commit']==old['source_commit']==bindings['source_commit']
 assert pri['source_sha256']==cross['source_sha256']==old['source_sha256']
 assert pri['source_sha256']['research/x-c1/renewable-low-schur-spectral-2026-09-29/07-canonical-extension-outer-mass/primary.json']==bindings['sha256']['outer_primary.json']
 assert old['primary_sha256']==bindings['sha256']['primary.json'] and old['crosscheck_sha256']==bindings['sha256']['crosscheck.json']
 assert mech['input_sha256']['primary.json']==bindings['sha256']['primary.json'] and mech['input_sha256']['crosscheck.json']==bindings['sha256']['crosscheck.json']
 proposal=json.loads((base/'candidate_proposals.json').read_bytes())
 upper={'A8->A9-even':'1.996e-7','A8->A9-odd':'2.477e-5','A9->A11-even':'1.371e-12','A9->A11-odd':'8.005e-12'}
 cor={}
 for key,h in upper.items():
  beta=F(mech['results'][key]['beta_probe_lower']['exact']);rest=1/beta
  assert rest<F(h)
  cor[key]={'reciprocal_exact':str(rest),'strict_upper':h}
 results={}
 for key in ['A9->A11-even','A9->A11-odd']:
  print('checking',key,flush=True)
  result={'direct_symmetric_pencil':[direct_pencil(x['results'][key]) for x in [pri,cross]],'candidates':{}}
  cases=[('central',[['0','0'],['0','0']]),('axis_one',[['0','0'],['0',proposal[key]['last_right_radius_multiplier']]])]
  if 'double_parameters' in proposal[key]:cases.append(('double',proposal[key]['double_parameters']))
  for kind,parameters in cases:
   c=candidate(cross['results'][key],source,key,parameters,kind)
   for data_run in [pri,cross]:certify_candidate(c,data_run['results'][key],source,key,old['results'][key])
   result['candidates'][kind]=spectral_certificate(c,kind)
   beta_lo,beta_hi=map(F,result['candidates'][kind]['beta_plus'])
   survival_lo,survival_hi=map(F,old['results'][key]['display_outward'])
   assert beta_lo>1/survival_hi and beta_hi<1/survival_lo and beta_lo>1/F(upper[key])
   print(kind,{k:v for k,v in result['candidates'][kind].items() if k!='beta_exact'},flush=True)
  results[key]=result
 out={'status':'SYMMETRIC_PENCIL_GATE_AUDITED','research_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN',
      'source_commit':pri['source_commit'],'input_sha256':bindings['sha256'],'corollary':cor,'results':results,
      'true_maximizer_isolated':False,'true_eigenvalue_gap_decided':False,
      'scope':'Explicit alternatives inside the specified joint finite certificate relaxation. No claim that they are realizations of the original full operator.',
      'large_solves_rerun':False}
 a.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print('SYMMETRIC GATE AND RELAXATION WITNESSES PASS',flush=True)

if __name__=='__main__':main()
