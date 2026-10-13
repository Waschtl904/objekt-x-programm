"""Standard-library rational audit; no floating point decisions."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt,factorial
import json
import rational_ldl as ld
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def mat(a):return [[F(x) for x in r] for r in a]
def trans(a):return list(map(list,zip(*a)))
def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
def mv(a,x):return [dot(r,x) for r in a]
def q(a,x):return dot(x,mv(a,x))
def add(a,b,s=1):return [[x+s*y for x,y in zip(r,t)] for r,t in zip(a,b)]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(a):
 n=len(a);w=[r[:]+e for r,e in zip(a,eye(n))]
 for j in range(n):
  assert w[j][j];v=w[j][j];w[j]=[x/v for x in w[j]]
  for i in range(n):
   if i!=j:
    v=w[i][j];w[i]=[x-v*y for x,y in zip(w[i],w[j])]
 out=[r[n:] for r in w]
 assert [[dot(r,c) for c in zip(*out)] for r in a]==eye(n)
 return out
def sup(x):
 assert x>=0;den=10**60;n=isqrt(x.numerator*den**2//x.denominator)+1
 z=F(n,den);assert z*z>x;return z
def point(x):return F(x),F(x)
def isum(v):
 v=list(v);return sum((x[0] for x in v),F(0)),sum((x[1] for x in v),F(0))
def scale(v,s):return (v[0]*s,v[1]*s) if s>=0 else (v[1]*s,v[0]*s)
def im(a):return [[tuple(map(F,x)) for x in r] for r in a]
def iq(a,x):return isum(scale(a[i][j],x[i]*x[j]) for i in range(len(x)) for j in range(len(x)))
def lin(a,coeff):return isum(scale(a[i][j],coeff[i][j]) for i in range(len(a)) for j in range(len(a[0])))
def mid(a):return [[(v[0]+v[1])/2 for v in r] for r in a]
def rr(a):return max(sum((v[1]-v[0])/2 for v in r) for r in a)
def lower(a,e):
 m=mid(a);n=len(a);out=[[(m[i][j]+m[j][i])/2 for j in range(n)] for i in range(n)]
 for i in range(n):out[i][i]-=e+sum((a[i][j][1]-a[i][j][0])/2+abs(m[i][j]-m[j][i])/2 for j in range(n))
 return out
def positive(a):return ld.positive([[ld.point(x) for x in r] for r in a])
def orthogonal(c,w):
 zw=mv(mat(c['D']),w)+w
 assert mv(trans(mat(c['S'])),zw)==[0]*8
 return 8
def floatsafeceil(x,digits=9):
 s=10**digits;return F(-((-x.numerator*s)//x.denominator),s)
def audit():
 assert isum((v for v in [(F(-2),F(3)),(F(4),F(8))]))==(F(2),F(11))
 assert scale((F(-2),F(3)),F(-2))==(F(-6),F(4))
 data=read(HERE/'AUDIT_INPUT.json');gates=read(HERE/'DIRECTIONAL_GATE.json')['cases'];obs=read(HERE/'OPTIMISTIC_OBSTRUCTION.json')['cases'];rows=[]
 # Inherited domain argument: generous direct-entry budget covers all analytic errors.
 for n in [160,161]:assert 2*F(21,40)**n/factorial(n)/(1-F(21,40)/F(n+1))<F(1,10**320)
 assert F(1,10**48)+36*F(1,10**34)+10*F(1,10**50)+F(1,10**300)<F(1,10**25)
 for p,label in enumerate(['EVEN','ODD']):
  c=data['cases'][p];gate=gates[p];ob=obs[p];br=c['bridge'];sc=c['schur'];rv=c['review'];g=c['galerkin'];cert=c['certificate']
  new=read(HERE/f'DIRECT_Y_{label}_3072.json');repeat=read(HERE/f'DIRECT_Y_{label}_4096.json')
  count=0
  for key in ['shell_diagonal_model','shell_potential_model','shell_kernel_inherited','moment_correction_model','D_Y_model']:
   for r,t in zip(new[key],repeat[key]):
    for x,y in zip(r,t):assert max(F(x[0]),F(y[0]))<=min(F(x[1]),F(y[1]));count+=1
  assert new['bindings']==repeat['bindings']
  assert F(new['gamma_error'][1])<F(1,10**34) and F(new['mu'][0])>F(9,100)
  assert F(new['coefficient_rounding_norm'][1])<F(1,10**60)
  assert F(new['operator_error'])==8*F(new['entry_error'])==F(8,10**25)
  for i in range(8):
   for j in range(8):
    terms=[tuple(map(F,new[key][i][j])) for key in ['shell_diagonal_model','shell_potential_model','moment_correction_model']]
    kernel=tuple(map(F,new['shell_kernel_inherited'][i][j]));terms.append(scale(kernel,-1))
    summed=isum(terms);out=tuple(map(F,new['D_Y_model'][i][j]))
    assert max(summed[0],out[0])<=min(summed[1],out[1])
  DY=lower(im(new['D_Y_model']),F(new['operator_error']));assert DY==mat(gate['D_Y_lower_new'])
  change=add(DY,mat(sc['D_Y_lower']),-1);assert change==mat(gate['D_Y_lower_improvement']);positive(change)
  upper_new=[[-v for v in r] for r in lower([[(-F(v[1]),-F(v[0])) for v in row] for row in new['D_Y_model']],F(new['operator_error']))]
  positive(add(mat(sc['D_Y_upper']),upper_new,-1))
  Q=add(mat(br['Q8']),change);assert Q==mat(gate['Qhat8']);positive(Q)
  full=gate['retained_four_block'];theta=F(full['theta']);assert F(1,2)<theta<1
  Qf=[[F(sc['K_lower'][i][j])+change[i][j]-F(sc['Gamma_R_upper'][i][j])/(1-theta) for j in range(8)] for i in range(8)]
  assert Qf==mat(full['Qhat8']);positive(add(Qf,mat(br['Q8']),-1))
  # Both supplied actual-Schur upper witnesses must be respected.
  y=list(map(F,rv['y']));x=[-z for z in mv(mat(br['P']),y)];z=x+y
  U=mat(rv['old_energy_upper']);L=mat(rv['old_energy_lower']);P=mat(br['P'])
  Bc=add(mat(rv['C_U_centre']),[r[4:] for r in U[:4]])
  eps=F(rv['C_error_norm_upper']);M=mat(rv['C_error_metric'])
  actual_upper=q(mat(rv['D_z_upper']),x)+2*dot(x,mv(Bc,y))+q(mat(rv['D_Y_upper']),y)-q(L,z)+2*eps*sup(q(M,x)*dot(y,y))
  assert q(Q,y)<actual_upper and q(Qf,y)<actual_upper
  # Rational fixed-grid LDL for the two new generalized-eigenvalue upper bounds.
  bb=ld.imat(g['B84_model']);vv=ld.imat(c['potential']['potential84_model']);oneeta=ld.point(F(9999999999,10**10))
  bp=[[ld.add(bb[i][j],ld.mul(oneeta,vv[i][j])) for j in range(84)] for i in range(84)]
  eb=ld.interval(c['potential']['Bplus_operator_error_scalar']);er=ld.interval(g['R84_operator_error_scalar'])
  checks=[]
  for record,rkey in [(gate,'R84_new_model'),(full,'R84_model')]:
   ell=ld.point(record['finite_generalized_eigenvalue_upper'])
   checks.append(ld.positive(ld.test_matrix(bp,ld.imat(record[rkey]),ell,ld.add(ld.mul(ell,eb),er))))
   w=list(map(F,record['rational_witness']));orthogonal(c,w)
   # Enclosed full model matrix plus its inherited analytic operator error.
   rlo=iq(im(record[rkey]),w)[0]-F(g['R84_operator_error_scalar'][1])*dot(w,w)
   bup=iq(im(g['B84_model']),w)[1]+F(9999999999,10**10)*iq(im(c['potential']['potential84_model']),w)[1]+F(c['potential']['Bplus_operator_error_scalar'][1])*dot(w,w)
   assert rlo>F(record['finite_generalized_eigenvalue_lower'])*bup and bup>0
  # Independent rational evaluation of the optimistic common-form witness.
  K=mat(br['K12_lower']);Ki=inv(K);Um=im(cert['model_upper_energy']);Eg=im(cert['energy_model_error_gram'])
  tau=lin(Um,trans(Ki))[1];eF=lin(Eg,trans(Ki))[1];assert 0<eF<F(3,10**25)
  gamma=2*sup(tau*eF)+eF
  w=[F(x[0]) for x in ob['w_rational']];t=[F(x[0]) for x in ob['t_rational']];u=[F(x[0]) for x in ob['u_rational']]
  orthogonal(c,w);wn=dot(w,w);tk=q(K,t);rho=F(cert['rho']);assert tk>0
  x,y=t[:4],t[4:];transx=[a+b for a,b in zip(x,mv(P,y))]
  weights=u+transx+y;C=im(g['C84_model'])
  cross=isum(scale(v,2*weights[i]*w[j]) for i,row in enumerate(C) for j,v in enumerate(row))[1]
  directupper=q(mat(rv['D_z_upper']),x)+2*dot(x,mv(Bc,y))+iq(im(new['D_Y_model']),y)[1]+F(new['operator_error'])*dot(y,y)+eps*(q(M,x)+dot(y,y))
  fupper=directupper-iq(Um,t)[0]+gamma*tk
  bupper=iq(im(g['B84_model']),w)[1]+F(9999999999,10**10)*iq(im(c['potential']['potential84_model']),w)[1]
  raw=fupper+cross+(1-rho)*dot(u,u)+bupper
  charge=2*F(g['C84_D0_inverse_metric_error_norm'][1])*sup(wn*((1-rho)*dot(u,u)+tk))+F(c['potential']['Bplus_operator_error_scalar'][1])*wn
  # Upper U[r] from the exact tail feature errors; interval centres of c_l paid before squaring.
  lowrows=[isum(scale(v,w[j]) for j,v in enumerate(row)) for row in C[:191]]
  lowmodel=sum(max(abs(lo),abs(hi))**2 for lo,hi in lowrows)/(1-rho)
  Utail=iq(im(g['H84_model']),w)[1]+F(g['H84_operator_error_scalar'][1])*wn+(sup(lowmodel)+sup(F(g['weighted_low_error_squared'][1])*wn))**2
  sourcecharge=2*sup(eF*Utail*tk);final=raw+charge+sourcecharge;assert final<0
  rows.append({'parity':label.lower(),'precision_interval_comparisons':count,
   'D_Y_improvement_positive':True,'compatible_bridge_lower_bounds_certified':True,
   'existing_actual_Schur_upper_witnesses_respected':True,'finite_eigenvalue_upper_checks':checks,
   'moment_only_eigenvalue_lower':gate['finite_generalized_eigenvalue_lower'],'moment_only_eigenvalue_upper':gate['finite_generalized_eigenvalue_upper'],
   'retained_four_eigenvalue_lower':full['finite_generalized_eigenvalue_lower'],'retained_four_eigenvalue_upper':full['finite_generalized_eigenvalue_upper'],
   'optimistic_common_form_ray_upper':str(final),'optimistic_common_form_ray_upper_display':str(floatsafeceil(final)),
   'fixed_Uop_and_Lplus_cannot_be_rescued_by_finite_bridge_alone':True,
   'negative_actual_schur_witness':False,'full_remainder_certified':False})
  print(label,'rational common-comparison upper <=',floatsafeceil(final),flush=True)
 # Meaningful negative control: an indefinite matrix must fail the positive checker.
 try:positive([[F(1),F(2)],[F(2),F(1)]])
 except AssertionError:pass
 else:raise AssertionError('indefinite control incorrectly accepted')
 return {'status':'PASS_RATIONAL_DIRECTIONAL_BRIDGE_AND_COMMON_OBSTRUCTION','cases':rows,'inherited_operator_bounds_assumed':True,'independent_external_review':False,'full_remainder_certified':False}
if __name__=='__main__':
 out=audit();(HERE/'AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out['status'])
