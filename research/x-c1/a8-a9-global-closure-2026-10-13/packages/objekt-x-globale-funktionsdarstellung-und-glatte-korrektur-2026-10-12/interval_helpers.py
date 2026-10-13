"""Independent standard-library rational audit of the new response step.

All large new products are recomputed with outward fixed-grid intervals.
Inherited source and analytic error matrices remain bound inputs.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json
import rational_ldl as ld
ld.SCALE=10**100;ld.ONE=(ld.SCALE,ld.SCALE)
S=ld.SCALE
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def tr(a):return sum((a[i][i] for i in range(len(a))),F(0))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def T(a):return list(map(list,zip(*a)))
def mm(a,b):return [[dot(row,col) for col in zip(*b)] for row in a]
def inv(a):
 n=len(a);w=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
 for j in range(n):
  v=w[j][j];assert v;w[j]=[x/v for x in w[j]]
  for i in range(n):
   if i!=j:
    v=w[i][j];w[i]=[x-v*y for x,y in zip(w[i],w[j])]
 out=[row[n:] for row in w]
 assert mm(a,out)==[[F(i==j) for j in range(n)] for i in range(n)]
 return out
def sqrtup(x):
 assert x>=0;den=10**100;z=F(isqrt(x.numerator*den**2//x.denominator)+1,den);assert z*z>=x;return z
def rat(a):return [[F(v) for v in row] for row in a]
def pts(a):return [[ld.point(v) for v in row] for row in a]
def im(a):return [[ld.interval(v) for v in row] for row in a]
def block(a,ii,jj):return [[a[i][j] for j in jj] for i in ii]
def add(a,b,sign=1):return [[ld.add(x,y) if sign==1 else ld.sub(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(a,v):return [[ld.mul(x,ld.point(v)) for x in row] for row in a]
def mmI(a,b):
 # Integer centre/radius products: every rounding error is included.
 ac=[[(lo+hi)//2 for lo,hi in row] for row in a];ar=[[max(c-lo,hi-c) for (lo,hi),c in zip(row,cr)] for row,cr in zip(a,ac)]
 bc=[[(lo+hi)//2 for lo,hi in row] for row in b];br=[[max(c-lo,hi-c) for (lo,hi),c in zip(row,cr)] for row,cr in zip(b,bc)]
 out=[]
 for x,xr in zip(ac,ar):
  row=[]
  for y,yr in zip(zip(*bc),zip(*br)):
   z=sum(u*v for u,v in zip(x,y));rad=sum(abs(u)*vr+ur*abs(v)+ur*vr for u,ur,v,vr in zip(x,xr,y,yr))
   row.append(((z-rad)//S,ld.ceildiv(z+rad,S)))
  out.append(row)
 return out
def upper(x):return F(x[1],S)
def lower(x):return F(x[0],S)
def itr(a):return sum((upper(a[i][i]) for i in range(len(a))),F(0))
def pair_upper(a,b):
 val=ld.ZERO
 for r,s in zip(a,b):
  for x,y in zip(r,s):val=ld.add(val,ld.mul(x,y))
 return upper(val)
def overlaps(a,b):
 assert len(a)==len(b) and all(len(x)==len(y) for x,y in zip(a,b))
 for r,s in zip(a,b):
  for x,y in zip(r,s):assert max(x[0],y[0])<=min(x[1],y[1])
def diagonal(a,v):return [[ld.add(x,ld.point(v if i==j else 0)) for j,x in enumerate(row)] for i,row in enumerate(a)]
def lower_point(k,a):
 for i,row in enumerate(a):
  room=lower(row[i])-k[i][i]
  need=sum(max(abs(lower(v)-k[i][j]),abs(upper(v)-k[i][j])) for j,v in enumerate(row) if j!=i)
  assert room>=need,('lower enclosure',i)
def audit(parent):
 ndata=read(parent/'REFINED_COMMON96.json')['cases'];source=read(parent/'REFINED_INPUT.json')['cases'];prior=read(parent/'AUDIT.json')['cases'];rows=[]
 for p,label in enumerate(['EVEN','ODD']):
  d=read(HERE/f'RESPONSES_{label}.json');n=ndata[p];g=source[p]['galerkin'];direct=read(parent/f'DIRECT_REST_{label}_3072.json')
  for name,want in d['bindings'].items():assert hashlib.sha256((parent/name).read_bytes()).hexdigest()==want,name
  eta=F(d['eta']);delta=F(d['delta']);rho=F(d['rho']);beta=F(d['beta'])
  assert eta==F(1,10**10) and delta==F(18219,10000) and beta==1-eta-F(16198,18219)
  assert rho==F(n['rho'])<1
  K=rat(d['K12_new_rational']);Ki=inv(K);kii=pts(Ki)
  gamma=F(prior[p]['new_energy_relative_error_upper']);G=pts(rat(n['G96_rational']));U=im(n['U96_model'])
  kraw=block(add(add(im(n['D96_lower_model']),U,-1),sc(G,gamma),-1),range(12),range(12))
  lower_point(K,kraw);kproof=ld.positive(pts(K))
  C=im(n['low_feature_J84_model'])+im(n['finite_cross_C84_new_model']);overlaps(C,im(d['C203x84_model']))
  H=im(n['H84_new_model']);B=add(sc(im(direct['D84_direct_model']),1-eta),H,-1);overlaps(B,im(d['B84_model']))
  eh=F(g['high_source_error_norm'][1]);htrace=delta*itr(H);Herr=(2*sqrtup(htrace)*eh+eh**2)/delta
  Berr=(1-eta)*F(direct['D84_operator_error'])+Herr
  eF=pair_upper(im(n['finite_feature_error_gram']),T(kii));eJ=84*F(n['tail_feature_error_scalar'][1])
  tauF=pair_upper(block(U,range(12),range(12)),T(kii));tauJ=itr(block(U,range(12,96),range(12,96)))
  cerr=sqrtup(eJ)+sqrtup(eF*tauJ)+sqrtup(tauF*eJ)+sqrtup(eF*eJ)+sqrtup(12*84*tr(Ki))*F(1,10**25)
  low=C[:191];fin=C[191:]
  R=add(sc(mmI(T(low),low),1/(1-rho)),mmI(T(fin),mmI(kii,fin)))
  overlaps(R,im(d['R84_model']))
  ell=F(d['model_loss_generalized_eigenvalue_upper']);eigproof=ld.positive(add(sc(B,ell),R,-1))
  bproof=ld.positive(diagonal(B,-F(d['B84_lower_scalar'])-Berr))
  bhiproof=ld.positive(diagonal(sc(B,-1),F(d['B84_upper_scalar'])-Berr))
  print(label,'K12, B84 and new joint loss bound rationally verified',flush=True)
  Xrat=rat(d['X84x203_rational']);assert len(Xrat)==84 and all(len(row)==203 for row in Xrat)
  assert all((v*10**60).denominator==1 for row in Xrat for v in row)
  X=pts(Xrat);xl=block(X,range(84),range(191));xf=block(X,range(84),range(191,203))
  V=add(sc(mmI(xl,T(xl)),1/(1-rho)),mmI(xf,mmI(kii,T(xf))));x2=itr(V)
  em=2*sqrtup(x2)*cerr+x2*Berr;um=F(d['M_actual_normalized_upper_scalar'])
  assert ell+em<=um<1
  budget=beta*(1-um);assert budget==F(d['sufficient_complete_QR_normalized_budget'])>0
  CX=mmI(C,X);M=add(add(CX,T(CX)),mmI(T(X),mmI(B,X)),-1)
  overlaps(M,im(d['M203_model']))
  mup=rat(d['M_upper_rational']);emcap=F(d['M_error_coefficient_rational']);assert em<=emcap
  D=[[F(1-rho) if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
  # Exact diagonal-dominance proof of the fixed directional upper matrix.
  for i in range(203):
   room=mup[i][i]-emcap*D[i][i]-upper(M[i][i])
   need=sum(max(abs(mup[i][j]-emcap*D[i][j]-lower(M[i][j])),abs(mup[i][j]-emcap*D[i][j]-upper(M[i][j]))) for j in range(203) if j!=i)
   assert room>=need,('M upper',i)
  # The complete directional budget itself is positive, after every error.
  mproof=ld.positive(pts([[um*D[i][j]-mup[i][j] for j in range(203)] for i in range(203)]))
  # M computed from the new data, not inferred from a small finite residual.
  gres=add(T(C),mmI(B,X),-1)
  gresnorm=sqrtup(sum(max(abs(lower(v)),abs(upper(v)))**2 for row in gres for v in row))
  assert gresnorm<F(1,10**50)
  print(label,'all 41209 M entries and 17052 response entries checked',flush=True)
  # Rationally rebuild the traces entering the COMPLETE coarse bound.
  ci=[[int(v) for v in row] for row in n['inverse_congruence_integer_matrix']];cd=int(n['inverse_congruence_denominator'])
  # Upper triangular C: calculate its symmetric Gram with integer arithmetic.
  xi=[[sum(ci[i][k]*ci[j][k] for k in range(max(i,j),191)) for j in range(191)] for i in range(191)]
  factor=F(1,cd**2)/(1-rho);tx=sum(xi[i][i] for i in range(191))*factor
  hi=[[int(v) for v in row] for row in n['HB_integer_matrix']]
  txh=F(sum(xi[i][j]*hi[j][i] for i in range(191) for j in range(191)),int(n['HB_denominator']))*factor
  mv=2*10**6*(2*tx+(1+F(1,10**12))*txh/delta**2);mh=(1+F(1,10**12))*10**6/delta;mu=mh+mv
  taua=(sqrtup(tauF)+sqrtup(eF))**2;A2=mv+96*10**20*tr(Ki)+2*taua*mu
  sj=(1-eta)*10**10+2*mh;coarse=(sqrtup(A2)+sj*sqrtup(x2))**2/F(21,5)
  cap=F(d['complete_coarse_QR_normalized_upper'])
  # Stored exact integer ceiling is allowed one rounding unit of audit slack;
  # if needed, use the independently recomputed ceiling as the valid cap.
  auditedcap=F(-((-coarse.numerator)//coarse.denominator))
  assert cap<=auditedcap<=cap+1
  # The concrete majorant cannot pass the sufficient matrix comparison.
  assert lower(M[0][0])+auditedcap/beta*(1-rho)>(1-rho)
  rows.append({'parity':label.lower(),'K12_positive':kproof,'B84_lower':bproof,'B84_upper':bhiproof,
   'joint_model_loss_bound':eigproof,'directional_M_upper_below_scalar_D':mproof,
   'new_response_entries':84*203,'M_entries_rebuilt':203**2,
   'M_actual_normalized_upper':str(um),'full_QR_sufficient_budget':str(budget),
   'finite_model_residual_norm_upper':str(gresnorm),'full_coarse_QR_normalized_upper_audited':str(auditedcap),
   'full_coarse_bound_fails_sufficient_matrix_test':True,'failure_is_not_a_negative_actual_Schur_witness':True,'full_remainder_certified':False})
  print(label,'PASS new finite budget; complete coarse upper is insufficient',flush=True)
 # A false finite-only completion must be rejected.
 try:ld.positive([[ld.point(1),ld.point(2)],[ld.point(2),ld.point(1)]])
 except AssertionError:pass
 else:raise AssertionError('indefinite matrix accepted')
 # Full residual identity on R^2, with a nonorthonormal J and invisible e2.
 sm=[[F(2),F(0)],[F(0),F(3)]];am=[[F(1),F(1)]];jm=[[F(2)],[F(0)]]
 bm=mm(T(jm),mm(sm,jm));cm=mm(am,jm);xm=mm(inv(bm),T(cm));zm=mm(jm,xm)
 residual=[[x-y for x,y in zip(r,s)] for r,s in zip(T(am),mm(sm,zm))]
 assert xm==[[F(1,4)]] and mm(T(jm),residual)==[[F(0)]]
 model=2*mm(am,zm)[0][0]-mm(T(zm),mm(sm,zm))[0][0]
 full=mm(am,mm(inv(sm),T(am)))[0][0]
 assert full==model+mm(T(residual),mm(inv(sm),residual))[0][0]==F(5,6)
 assert model<F(3,4)<full
 try:assert mm(T(residual),residual)[0][0]<=0
 except AssertionError:pass
 else:raise AssertionError('omitted outside residual accepted')
 return {'status':'PASS_NEW_RESPONSES_AND_RATIONAL_BUDGET_FULL_COARSE_BOUND_INCONCLUSIVE','rational_grid_digits':100,'cases':rows,
  'countercontrols':['indefinite matrix rejected','omitted outside residual rejected','nonorthonormal J uses correct Gram'],
  'inherited_operator_hypotheses':True,'sharp_full_Gram_computed':False,'full_remainder_certified':False}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--parent',type=Path,required=True);args=ap.parse_args()
 assert __debug__,'Do not run with -O'
 out=audit(args.parent);(HERE/'AUDIT.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
