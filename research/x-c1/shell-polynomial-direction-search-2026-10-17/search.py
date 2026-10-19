"""Reproducible, explicitly undirected multistart search on the W-unit sphere."""
import os,json,sys,hashlib
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import minimize,minimize_scalar
from scipy.linalg import solve_triangular
HERE=Path(__file__).resolve().parent
DATA=Path(os.environ.get('OBJEKT_X_SEARCH_OUTPUT',str(HERE/'data')))

def number(x):return float(Fraction(x))
def psd(a,name):
 a=np.asarray(a);a=(a+a.T)/2;v,u=np.linalg.eigh(a);scale=max(1,np.max(abs(v)))
 if v[0]<-1e-12*scale:raise ValueError((name,'non-PSD diagnostic matrix',v[0]))
 return (u*np.maximum(v,0))@u.T,{'min_eigenvalue':float(v[0]),'max_eigenvalue':float(v[-1]),'roundoff_negative_eigenvalues_clipped':int(np.sum(v<0))}

def run(par):
 src=DATA/f'MAPS_{par}_384.json';d=json.loads(src.read_text())
 G=np.array(d['G_W']);L=np.linalg.cholesky(G);W=solve_triangular(L.T,np.eye(12),lower=False)
 assert np.linalg.norm(W.T@G@W-np.eye(12),ord=2)<1e-13
 ell=np.array(d['I0_row'])@W
 mats={};diagnostics={}
 for name in ('H8_gram','psi_k_gram','derivative_gram','jump_gram'):
  mats[name],diagnostics[name]=psd(W.T@np.array(d[name])@W,name)
 feat=np.array(d['feature_factor'])@W;feature=feat.T@feat
 high=d['high_multiplier'];featmul=d['feature_multiplier'];q=number(d['q']);eps=number(d['D_model_scalar_error_upper']);ek=number(d['K_model_error_upper']);whole=number(d['K_whole_W_unit_upper'])
 alpha=10*q/11
 def qform(A,y):return max(0,float(y@A@y))
 def ngrad(A,y):
  v=np.sqrt(qform(A,y));return v,(A@y/v if v>1e-24 else np.zeros(12))
 def budget(a,j,t):
  return a*(t**3/3+t*t/4)+2*np.sqrt(a*j)*(2*t**2.5/5+t**1.5/3)+j*(t*t/2+t/2)+4*(1-t+np.log(1/t)/2+35/24)+3
 def calc(y):
  yn=np.linalg.norm(y);u=y/yn
  nh,gh=ngrad(mats['H8_gram'],u);nf,gf=ngrad(feature,u);nk,gk=ngrad(mats['psi_k_gram'],u)
  radius=high*nh+featmul*nf+nk
  a=qform(mats['derivative_gram'],u);j=qform(mats['jump_gram'],u)
  opt=minimize_scalar(lambda v:budget(a,j,np.exp(v)),bounds=(np.log(1e-9),np.log(.1)),method='bounded',options={'xatol':1e-12})
  t=min(.1,np.exp(opt.x));raw=budget(a,j,t)+ek
  if budget(a,j,.1)+ek<raw:t=.1;raw=budget(a,j,t)+ek
  B=min(whole,raw);tau=np.sqrt(alpha*B)+eps
  dtau=np.zeros(12)
  if raw<whole:
   aa=t**3/3+t*t/4;cc=2*t**2.5/5+t**1.5/3;jj=t*t/2+t/2
   dB=2*aa*(mats['derivative_gram']@u)+2*jj*(mats['jump_gram']@u)
   if a>1e-24 and j>1e-24:dB+=2*cc*(np.sqrt(j/a)*(mats['derivative_gram']@u)+np.sqrt(a/j)*(mats['jump_gram']@u))
   dtau=np.sqrt(alpha)/(2*np.sqrt(B))*dB
  center=float(ell@u);score=center-radius-tau
  grad=ell-high*gh-featmul*gf-gk-dtau;grad=(grad-u*(u@grad))/yn
  return score,grad,dict(I0_midpoint=center,coarse_radius=radius,high_error=high*nh,finite_response_error=featmul*nf,psi_k_error=nk,K_upper_diagnostic=B,tau_diagnostic=tau,margin_diagnostic=score,translation_cutoff=t,piecewise_derivative_square=a,jump_square_sum=j)
 z0=np.zeros(12);z0[0]=d['z0_coefficient'];y0=L.T@z0
 if ell@y0<0:y0=-y0
 rng=np.random.default_rng(20261017+(0 if par=='even' else 1));starts=[y0,ell/np.linalg.norm(ell)]
 _,hh=np.linalg.eigh(mats['H8_gram']);starts.extend(hh[:,j]for j in range(12));starts.extend(np.eye(12));starts.extend(rng.normal(size=(32,12)))
 results=[]
 for idx,y in enumerate(starts):
  y=np.array(y);y/=np.linalg.norm(y)
  if ell@y<0:y=-y
  op=minimize(lambda v:(-calc(v)[0],-calc(v)[1]),y,jac=True,method='SLSQP',constraints=[{'type':'eq','fun':lambda v:float(v@v-1),'jac':lambda v:2*v}],options={'ftol':1e-10,'maxiter':350})
  yy=op.x/np.linalg.norm(op.x)
  if ell@yy<0:yy=-yy
  score,grad,row=calc(yy);coef=W@yy
  row.update(start=idx,optimizer_success=bool(op.success),optimizer_message=str(op.message),iterations=int(op.nit),projected_gradient_norm=float(np.linalg.norm(grad)),coefficients=coef.tolist(),whitened=yy.tolist(),physical_norm_squared=float(coef@G@coef),coefficient_euclidean_norm=float(np.linalg.norm(coef)))
  results.append(row)
  if idx%10==0:print(par,'start',idx,'margin',score,flush=True)
 results.sort(key=lambda r:r['margin_diagnostic'],reverse=True)
 unique=[]
 for r in results:
  if all(abs(np.dot(r['whitened'],x['whitened']))<1-1e-8 for x in unique):unique.append(r)
  if len(unique)>=8:break
 baseline=calc(y0)[2];best=results[0]
 # A diagnostic ceiling for this chosen budget: all nonnegative A,J terms are dropped.
 floorB=4*(1-.1+np.log(10)/2+35/24)+3
 ceiling=float(np.linalg.norm(ell)-np.sqrt(alpha*min(whole,floorB)))
 out={'status':'EXPLORATORY_NOT_DIRECTED_NO_N12_CLAIM','parity':par,'map_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'seed':20261017+(0 if par=='even' else 1),'starts':len(starts),'G_condition_number':float(np.linalg.cond(G)),'whitening_residual':float(np.linalg.norm(W.T@G@W-np.eye(12),ord=2)),'matrix_diagnostics':diagnostics,'I0_dual_W_norm':float(np.linalg.norm(ell)),'chosen_budget_global_margin_ceiling_diagnostic':ceiling,'z0_with_same_direction_budget':baseline,'best':best,'distinct_ranked_candidates':unique,'all_starts':results,
  'scope':'I0 midpoint, not a high-pairing-shifted center; coarse norms and thresholds remain undirected in this search. The scalar certificate must include all integration/model errors afresh.'}
 (DATA/f'SEARCH_{par}.json').write_text(json.dumps(out,indent=2)+'\n')
 frozen={'status':'FROZEN_CANDIDATE_NOT_CERTIFIED','parity':par,'selection_file_sha256':hashlib.sha256((DATA/f'SEARCH_{par}.json').read_bytes()).hexdigest(),'basis':d['basis'],'raw_exact_rational_coefficients':[str(Fraction(format(x,'.25g')))for x in best['coefficients']], 'normalization':'z = sum_j raw_j ell_j / sqrt(raw^T G_W raw); normalization is part of the exact fixed direction','selection_margin_diagnostic':best['margin_diagnostic'],'requires_separate_directed_run':True}
 frozen['translation_cutoff_exact_rational']=str(Fraction(format(best['translation_cutoff'],'.25g')))
 (DATA/f'FROZEN_{par}.json').write_text(json.dumps(frozen,indent=2)+'\n')
 print(par,'best',best['margin_diagnostic'],'z0',baseline['margin_diagnostic'],'I0 dual',np.linalg.norm(ell),'ceiling',ceiling,flush=True)

if __name__=='__main__':
 for p in sys.argv[1:]or('even','odd'):run(p)
