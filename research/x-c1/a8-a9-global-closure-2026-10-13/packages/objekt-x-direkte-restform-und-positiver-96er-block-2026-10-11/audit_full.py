"""Independent rational rebuild of the new 96D positive comparison.

No numerical Python libraries, floating point decisions or sampled tails.
Inputs still assume the inherited analytic operator estimates.
"""
from pathlib import Path
from fractions import Fraction as F
import json,argparse
import rational_ldl as ld
from rational_helpers import mat,trans,dot,mv,q,inv,sup,point,isum,scale,im,iq,lin,orthogonal
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def ia(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def mul(a,b):
 vals=[x*y for x in a for y in b];return min(vals),max(vals)
def sq(a):return (F(0) if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2))
def div(a,b):
 assert b[0]>0;return mul(a,(1/b[1],1/b[0]))
def mm(a,b):return [[sum(x*y for x,y in zip(r,c) if x and y) for c in zip(*b)] for r in a]
def ints(a):return [[int(x) for x in r] for r in a]
def grid(a):return [[ld.interval(v) for v in r] for r in a]
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def upper_point(a,b):
 n=len(a)
 for i in range(n):
  room=a[i][i]-b[i][i][1]
  needed=sum(max(abs(a[i][j]-b[i][j][0]),abs(a[i][j]-b[i][j][1])) for j in range(n) if i!=j)
  assert room>=needed,(i,'Loewner diagonal dominance failed')
def ceil_display(x,digits=12):
 s=10**digits;return str(F(-((-x.numerator*s)//x.denominator),s))
def old_common_upper(c,d,ob):
 g=c['galerkin'];cert=c['certificate'];rv=c['review'];br=c['bridge'];K=mat(br['K12_lower']);Ki=inv(K);P=mat(br['P'])
 U0=im(cert['model_upper_energy']);EE=im(cert['energy_model_error_gram'])
 ef=lin(EE,trans(Ki))[1];tau=lin(U0,trans(Ki))[1];gamma=2*sup(ef*tau)+ef
 w=[F(x[0]) for x in ob['w_rational']];t=[F(x[0]) for x in ob['t_rational']];u=[F(x[0]) for x in ob['u_rational']]
 orthogonal(c,w);wn=dot(w,w);tk=q(K,t);x,y=t[:4],t[4:];rho=F(cert['rho'])
 U=mat(rv['old_energy_upper']);B=[[F(rv['C_U_centre'][i][j])+U[i][j+4] for j in range(8)] for i in range(4)]
 eps=F(rv['C_error_norm_upper']);M=mat(rv['C_error_metric'])
 # Use the newly integrated YY block, paying the complete 8-column error.
 DY=[[tuple(map(F,d['D92_model'][i+84][j+84])) for j in range(8)] for i in range(8)]
 fupper=q(mat(rv['D_z_upper']),x)+2*dot(x,mv(B,y))+iq(DY,y)[1]+F(8,10**25)*dot(y,y)+eps*(q(M,x)+dot(y,y))-iq(U0,t)[0]+gamma*tk
 weights=u+[a+b for a,b in zip(x,mv(P,y))]+y;C=im(g['C84_model'])
 cross=isum(scale(v,2*weights[i]*w[j]) for i,row in enumerate(C) for j,v in enumerate(row))[1]
 bmodel=iq(im(d['D84_direct_model']),w)[1]-iq(im(g['H84_model']),w)[0]
 charge=2*F(g['C84_D0_inverse_metric_error_norm'][1])*sup(wn*((1-rho)*dot(u,u)+tk))+(F(d['D84_operator_error'])+F(g['H84_operator_error_scalar'][1]))*wn
 hupper=iq(im(g['H84_model']),w)[1]+F(g['H84_operator_error_scalar'][1])*wn
 cl=[isum(scale(v,w[j]) for j,v in enumerate(row)) for row in C[:191]]
 low=sum(max(abs(x),abs(y))**2 for x,y in cl)/(1-rho)
 utail=hupper+(sup(low)+sup(F(g['weighted_low_error_squared'][1])*wn))**2
 result=fupper+cross+(1-rho)*dot(u,u)+bmodel+charge+2*sup(ef*utail*tk)
 assert result<0
 return result
def audit(parent):
 data=read(HERE/'REFINED_INPUT.json');new=read(HERE/'REFINED_COMMON96.json')['cases'];old=read(parent/'AUDIT_INPUT.json')['cases'];obs=read(HERE/'FULL_DIRECT_TEST.json')['cases']
 floor=read(HERE/'REFINED_HIGH_FLOOR.json');delta=F(floor['new_physical_high_floor']);od=F(91,50)
 from inherited_floor import prove
 assert floor['inherited']==prove()
 raw=F(floor['inherited']['raw_high_floor']);margin=raw-16*F(1,10**6)-12*F(1,10**12)-delta*(1+F(1,10**12))
 assert margin==F(floor['exact_positive_margin'])>0 and delta==F(18219,10000)>od
 rows=[]
 for p,label in enumerate(['EVEN','ODD']):
  inp=data['cases'][p];n=new[p];c=inp['old_certificate'];g=inp['galerkin'];prev=old[p];br=prev['bridge'];rv=prev['review']
  d=read(HERE/f'DIRECT_REST_{label}_3072.json');repeat=read(HERE/f'DIRECT_REST_{label}_4096.json');checks=0
  assert d['bindings']==repeat['bindings'] and F(d['coefficient_rounding_norm'][1])<F(1,10**60)
  assert F(d['gamma_error'][1])<F(1,10**34) and F(d['D92_operator_error'])==92*F(d['entry_error'])==F(92,10**25)
  keys=['mass_model','shell_diagonal_model','shell_potential_model','shell_self_kernel_model','shell_mirror_unsigned_model','shell_signed_kernel_model','moment_correction_model','D92_model','D84_direct_model']
  for key in keys:
   for r,s in zip(d[key],repeat[key]):
    for a,b in zip(r,s):assert overlap(tuple(map(F,a)),tuple(map(F,b)));checks+=1
  lam=[tuple(map(F,x)) for x in d['lambda_model']];ms=[tuple(map(F,x)) for x in d['M_source_model']];mu=tuple(map(F,d['mu']));qmm=tuple(map(F,d['Q_mm_model']))
  for i in range(92):
   for j in range(92):
    mc=neg(ia(div(ia(mul(lam[i],ms[j]),mul(ms[i],lam[j])),mu),div(mul(mul(lam[i],lam[j]),qmm),sq(mu))))
    assert overlap(mc,tuple(map(F,d['moment_correction_model'][i][j])))
    kg=ia(tuple(map(F,d['shell_self_kernel_model'][i][j])),scale(tuple(map(F,d['shell_mirror_unsigned_model'][i][j])),(-1)**p))
    assert overlap(kg,tuple(map(F,d['shell_signed_kernel_model'][i][j])))
    total=isum([tuple(map(F,d['shell_diagonal_model'][i][j])),tuple(map(F,d['shell_potential_model'][i][j])),neg(kg),mc])
    assert overlap(total,tuple(map(F,d['D92_model'][i][j])))
  for i in range(8):
   for j in range(84):
    diff=ia(tuple(map(F,d['D92_model'][i+84][j])),neg(tuple(map(F,g['direct_cross_model'][i+4][j]))))
    assert max(abs(x) for x in diff)<F(2,10**25)
  oldray=old_common_upper(prev,d,obs[p]);print(label,'old majorant full-direct upper <=',ceil_display(oldray),flush=True)
  # Full rational input inequalities and inverse congruence for the NEW majorant.
  Fi=ints(n['F_integer_matrix']);Hi=ints(n['HB_integer_matrix']);Ci=ints(n['inverse_congruence_integer_matrix']);fd=int(n['F_denominator']);hd=int(n['HB_denominator']);cd=int(n['inverse_congruence_denominator'])
  assert Fi==trans(Fi) and Hi==trans(Hi)
  assert all(Ci[i][i]>0 and all(Ci[i][j]==0 for j in range(i)) for i in range(191))
  H=[[F(x,hd) for x in r] for r in Hi];FM=[[F(x,fd) for x in r] for r in Fi]
  padding=F(n['coupling_padding']);assert padding==F(1,10**10)
  eb=F(c['old_coupling_error_norm'][1]);rawG=[[(F(int(a),10**100),F(int(b),10**100)) for a,b in r] for r in inp['old_raw_coupling_gram']]
  HBinput=[[ia(scale(rawG[i][j],1+padding),point((1+1/padding)*eb**2 if i==j else 0)) for j in range(191)] for i in range(191)]
  upper_point(H,HBinput)
  Finput=[[F(c['F_integer_matrix'][i][j])/F(c['F_denominator'])+F(c['HB_integer_matrix'][i][j])/F(c['HB_denominator'])/od-H[i][j]/delta for j in range(191)] for i in range(191)]
  upper_point([[-x for x in r] for r in FM],[[point(-x) for x in r] for r in Finput])
  product=mm(trans(Ci),mm(Fi,Ci));den=fd*cd**2
  err=max(sum(abs(product[i][j]-(den if i==j else 0)) for j in range(191)) for i in range(191));rho=F(err,den)
  assert err==int(n['congruence_error_numerator']) and den==int(n['congruence_error_denominator']) and rho==F(n['rho'])<F(1,10**40)
  print(label,'new 191D integer inverse congruence passed',flush=True)
  # Rebuild all 96 source responses, with common integer denominators.
  cc=[a+b for a,b in zip(c['source_c_model'],g['old_low_c_model'])];bb=[a+b for a,b in zip(c['source_Bh_model'],g['old_low_Bh_model'])]
  v=[];vd=delta.numerator*10**100
  for i in range(191):
   row=[]
   for j in range(96):
    a=tuple(map(F,cc[i][j]));b=tuple(map(F,bb[i][j]));z=(a[0]*delta.numerator-b[1]*delta.denominator,a[1]*delta.numerator-b[0]*delta.denominator)
    assert all((x*10**100).denominator==1 for x in z);row.append(tuple(int(x*10**100) for x in z))
   v.append(row)
  transformed=[]
  for i in range(191):
   rr=[]
   for j in range(96):
    lo=hi=0
    for k in range(i+1):
     z=Ci[k][i];lo+=z*v[k][j][0 if z>=0 else 1];hi+=z*v[k][j][1 if z>=0 else 0]
    rr.append((lo,hi))
   transformed.append(rr)
  gramden=F((cd*vd)**2)*(1-rho);HGf=im(c['source_h_gram_model']);HGj=[[scale(x,od) for x in r] for r in im(g['H84_model'])];HGcross=im(g['complete_source_high_cross_model'])
  HG=[[HGf[i][j] if i<12 and j<12 else HGcross[i][j-12] if i<12 else HGcross[j][i-12] if j<12 else HGj[i-12][j-12] for j in range(96)] for i in range(96)]
  U=[[None]*96 for _ in range(96)]
  for i in range(96):
   for j in range(i,96):
    lo=hi=0
    for r in transformed:
     a=r[i];b=r[j]
     if i==j:pair=(0 if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2))
     else:
      prod=[x*y for x in a for y in b];pair=min(prod),max(prod)
     lo+=pair[0];hi+=pair[1]
    U[i][j]=U[j][i]=ia(scale(HG[i][j],1/delta),(lo/gramden,hi/gramden))
    assert overlap(U[i][j],tuple(map(F,n['U96_model'][i][j])))
  print(label,'all 9216 new common-energy entries rebuilt rationally',flush=True)
  XI=mm(Ci,trans(Ci));xf=1/(F(cd**2)*(1-rho));tx=sum(XI[i][i] for i in range(191))*xf;txh=F(sum(XI[i][j]*Hi[j][i] for i in range(191) for j in range(191)),hd)*xf
  Ec=im(c['joint_low_source_error_gram']);Eh=im(c['joint_high_source_error_gram']);HGu=mat(c['source_h_gram_upper_rational'])
  EF=[[isum([scale(Eh[i][j],1/delta+3*txh/delta**2),scale(Ec[i][j],3*tx),point(3*HGu[i][j]*tx*eb**2/delta**2)]) for j in range(12)] for i in range(12)]
  # A conservative rational moment-basis bound replaces irrational square roots.
  rm=data['old_raw_moments'];denmom=F(int(rm[p][0]),10**100);assert denmom>0
  cn2=sum(F(2*k+1,2*p+1)*(F(int(rm[k][1]),10**100)/denmom)**2 for k in range(p+2,384,2))
  ef=F(g['source_model_error_norm'][1]);eh=F(g['high_source_error_norm'][1]);ebj=F(g['old_coupling_error_norm'][1]);htrace=sum(HGj[i][i][1] for i in range(84))
  EJ=eh**2/delta+3*(tx*(1+cn2)*ef**2+txh*eh**2/delta**2+tx*ebj**2*htrace/delta**2)
  K=mat(br['K12_lower']);Ki=inv(K);e2=2*(lin(EF,trans(Ki))[1]+84*EJ);tau=lin([r[:12] for r in U[:12]],trans(Ki))[1]+sum(U[i][i][1] for i in range(12,96));gamma=2*sup(e2*tau)+e2
  assert e2>0 and tau>0
  # Rebuild the actual direct lower block with its complete cross/error prices.
  OU=mat(rv['old_energy_upper']);Dz=[[F(br['N'][i][j])+OU[i][j] for j in range(4)] for i in range(4)];Bc=[[F(rv['C_U_centre'][i][j])+OU[i][j+4] for j in range(8)] for i in range(4)]
  DC=im(g['direct_cross_model']);DD=im(d['D92_model']);idx=list(range(84,92))+list(range(84));eps=F(rv['C_error_norm_upper']);M=mat(rv['C_error_metric'])
  G=[[K[i][j] if i<12 and j<12 else F(i==j) if i>=12 and j>=12 else F(0) for j in range(96)] for i in range(96)]
  assert G==mat(n['G96_rational']);lower=[]
  for i in range(96):
   row=[]
   for j in range(96):
    z=point(Dz[i][j]) if i<4 and j<4 else point(Bc[i][j-4]) if i<4 and j<12 else DC[i][j-12] if i<4 else point(Bc[j][i-4]) if j<4 and i<12 else DC[j][i-12] if j<4 else DD[idx[i-4]][idx[j-4]]
    charge=eps*M[i][j] if i<4 and j<4 else eps if 4<=i<12 and i==j else F(0)
    z=ia(z,point(-charge-(F(96,10**25) if i==j else 0)))
    row.append(ia(ia(z,neg(U[i][j])),point(-gamma*G[i][j])))
   lower.append(row)
  reserve=F(n['common96_positive_reserve_relative_to_G']);assert reserve>0
  proof=ld.positive([[ld.sub(ld.interval(lower[i][j]),ld.point(reserve*G[i][j])) for j in range(96)] for i in range(96)])
  rows.append({'parity':label.lower(),'precision_interval_comparisons':checks,'moment_formula_checks':92**2,'YJ_analytic_consistency_checks':8*84,
   'old_majorant_full_direct_upper_display':ceil_display(oldray),'new_inverse_congruence_rho':str(rho),'new_common_energy_entries_rebuilt':96**2,
   'new_feature_error_metric_trace_upper':str(e2),'new_energy_relative_error_upper':str(gamma),'common96_reserve_relative_to_diag_Kold_I84':str(reserve),
   'positive_block_check':proof,'new_common96_positive':True,'full_remainder_certified':False,'negative_actual_schur_witness':False})
  print(label,'PASS positive common96 reserve',reserve,flush=True)
 # Countercontrol for the final rational LDL.
 try:ld.positive([[ld.point(1),ld.point(2)],[ld.point(2),ld.point(1)]])
 except AssertionError:pass
 else:raise AssertionError('indefinite countercontrol accepted')
 return {'status':'PASS_FULL_DIRECT_REST_AND_REFINED_COMMON96','cases':rows,'operator_hypotheses_inherited':True,'external_review_open':True,'full_remainder_certified':False}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--parent',type=Path,required=True);args=ap.parse_args()
 out=audit(args.parent);(HERE/'AUDIT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
