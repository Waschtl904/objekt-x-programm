"""Directed actual K_P for the two fixed candidates: full autocorrelation energy.

No direction selection. Inherited F/A/T and scalar enclosures are explicit inputs.
"""
import hashlib,io,json,os,sys,zipfile
from pathlib import Path
from fractions import Fraction
from flint import arb,acb,arb_poly,acb_poly,arb_mat,ctx
ctx.prec=800
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
OUT=Path(os.environ.get('OBJEKT_X_SHARP_K_OUTPUT',str(HERE/'expected')))
OUT.mkdir(parents=True,exist_ok=True)
def q(v):
 f=Fraction(v);return arb(f.numerator)/f.denominator
def box(v):return q(v[0]).union(q(v[1]))
def ub(x):return abs(x).upper()
def enc(x):return [str(x.lower().fmpq()),str(x.upper().fmpq())]
def pad(x,e):return x+arb(0,ub(e))
def pint(p,s):return sum((c*s**(j+1)/(j+1)for j,c in enumerate(p)),arb(0))
def abs_poly(p,s):return sum((ub(c)*s**j for j,c in enumerate(p)),arb(0))
def load_bound(rel,bindings):
 assert rel in bindings['repository_files'],rel
 return json.loads((ROOT/rel).read_bytes())
def member(z,suffix):
 roots={n.split('/')[0]for n in z.namelist()if '/' in n};assert len(roots)==1
 return z.read(next(iter(roots))+'/'+suffix)
def positive_pivots(S):
 a=[[S[i,j]for j in range(12)]for i in range(12)];p=[]
 for k in range(12):
  d=a[k][k];assert d>0,('positive S0 pivot',k,d);p.append(d)
  for i in range(k+1,12):
   for j in range(i,12):
    a[i][j]-=a[i][k]*a[k][j]/d;a[j][i]=a[i][j]
 return p
def main(par,nodes_count=128):
 assert par in ('even','odd');eps=1 if par=='even' else -1
 bind=json.loads((HERE/'INPUT_BINDINGS.json').read_bytes())
 for rel,digest in bind['repository_files'].items():assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest,rel
 archive=ROOT/bind['response_archive']['path'];raw=archive.read_bytes();assert hashlib.sha256(raw).hexdigest()==bind['response_archive']['sha256']
 z=zipfile.ZipFile(io.BytesIO(raw));man=json.loads(member(z,'MANIFEST.json'))
 for rel,digest in man.items():assert hashlib.sha256(member(z,rel)).hexdigest()==digest,rel
 fresh=json.loads(member(z,'inputs/FRESH_A12.json'));fixed=json.loads(member(z,'inputs/FROZEN_RESPONSE12.json'));energy=json.loads(member(z,'RESPONSE_ENERGY.json'));funcs=json.loads(member(z,'inputs/FUNCTIONS12.json'))
 assert fixed['rule_id']=='A9_A11_N12_MIDPOINT_INVERSE_60_V1'
 for rel,digest in energy['source_bindings'].items():assert hashlib.sha256(member(z,rel)).hexdigest()==digest,rel
 candidate_rel=f'research/x-c1/shell-polynomial-direction-search-2026-10-17/data/FROZEN_{par}.json'
 cert_rel=f'research/x-c1/frozen-shell-direction-certificates-2026-10-17/expected/FROZEN_CERTIFICATE_{par}.json'
 frozen=load_bound(candidate_rel,bind);previous=load_bound(cert_rel,bind)
 assert previous['candidate_sha256']==bind['repository_files'][candidate_rel]
 assert frozen['parity']==previous['parity']==par
 assert len(frozen['raw_exact_rational_coefficients'])==12
 inherited=load_bound('research/x-c1/frozen-shell-direction-certificates-2026-10-17/INPUT_BINDINGS.json',bind)
 for name in ('FROZEN_RESPONSE12.json','FUNCTIONS12.json'):
  assert hashlib.sha256(member(z,'inputs/'+name)).hexdigest()==inherited['prepared_inputs'][name],name
 a=arb(3).log();b=arb(11).log()/2;h=b-a;mu=(eps*a+a.sinh())/2
 assert a>1 and h>q('0.1')
 leg=[arb_poly([1]),arb_poly([0,1])]
 for n in range(1,11):leg.append(((2*n+1)*arb_poly([0,1])*leg[n]-n*leg[n-1])*(arb(1)/(n+1)))
 coeff=list(map(q,frozen['raw_exact_rational_coefficients']))
 rawpoly=sum((coeff[j]*(arb(2*j+1)/(2*h)).sqrt()*leg[j](arb_poly([-1-2*a/h,2/h]))for j in range(12)),arb_poly([]))
 s=b/a-1;order=120
 m=lambda x:(x/2).cosh()if eps==1 else(x/2).sinh()
 M=arb_poly([((a/2).cosh()if ((eps==1)==(j%2==0))else(a/2).sinh())*(a/2)**j/arb.fac_ui(j)for j in range(order+1)])
 em=(b/2).exp()*(a*s/2)**(order+1)/arb.fac_ui(order+1)
 pu=rawpoly(arb_poly([a,a]));lamraw=a*pad(pint(pu*M,s),s*abs_poly(pu,s)*em)
 norm=(sum((c*c for c in coeff),arb(0))+2*lamraw**2/mu).sqrt();P=rawpoly*(1/norm);lam=lamraw/norm;Ac=-lam/mu
 assert norm.overlaps(box(previous['exact_candidate_normalization']))
 Pd=P.derivative();A=2*(pint(Pd*Pd,b)-pint(Pd*Pd,a))+2*Ac**2*(-eps*a+a.sinh())/8
 J=2*((P(a)-Ac*m(a))**2+P(b)**2)
 assert A>0 and J>0
 assert A.overlaps(box(previous['piecewise_derivative_square'])) and J.overlaps(box(previous['jump_square_sum']))
 # Three physical pieces on R; the central hyperbolic function already has parity eps.
 ends=[(-b,-a),(-a,a),(a,b)];polys=[P(arb_poly([0,-1]))*eps,None,P]
 def exponential_primitive(p,sign):
  ans=p*(arb(2)*sign);der=p
  for k in range(1,len(p)):
   der=der.derivative();ans+=der*((-1)**k*(arb(2)*sign)**(k+1))
  return ans
 def correlation_formula(selector):
  pairs=[]
  for i,(ai,bi)in enumerate(ends):
   for j,(aj,bj)in enumerate(ends):
    lower_difference=aj-selector-ai;upper_difference=bj-selector-bi
    assert lower_difference>0 or lower_difference<0,('ambiguous lower branch',i,j,selector)
    assert upper_difference>0 or upper_difference<0,('ambiguous upper branch',i,j,selector)
    lo_from_j=lower_difference>0
    hi_from_j=upper_difference<0
    lo=aj-selector if lo_from_j else ai;hi=bj-selector if hi_from_j else bi
    assert hi>lo or hi<lo,('ambiguous overlap',i,j,selector)
    if hi>lo:pairs.append((i,j,lo_from_j,hi_from_j))
  def value(r):
   complex_value=isinstance(r,acb);Poly=acb_poly if complex_value else arb_poly;total=acb(0)if complex_value else arb(0)
   for i,j,lo_j,hi_j in pairs:
    lo=ends[j][0]-r if lo_j else ends[i][0];hi=ends[j][1]-r if hi_j else ends[i][1]
    if i==j==1:
     total+=Ac**2*((hi+r/2).sinh()-(lo+r/2).sinh()+eps*(hi-lo)*(r/2).cosh())/2
    elif i!=1 and j!=1:
     p=Poly(polys[i])*Poly(polys[j])(Poly([r,1]));Q=p.integral();total+=Q(hi)-Q(lo)
    else:
     p=Poly(polys[j])(Poly([r,1]))if i==1 else Poly(polys[i])
     shift=arb(0)if i==1 else r
     for sign in (1,-1):
      Q=exponential_primitive(p,sign)
      v=(hi*sign/2).exp()*Q(hi)-(lo*sign/2).exp()*Q(lo)
      total+=Ac/2*(1 if sign==1 else eps)*(shift*sign/2).exp()*v
   return total
  return value
 # Point controls are used only by the separate numerical audit.
 if os.environ.get('OBJEKT_X_CORRELATION_PROBE'):
  points=[h/4,h/2,(h+2*a)/2,(2*a+a+b)/2,(a+b+2*b)/2]
  points+=[arb(n).log()for n in (2,3,4,5,7,8)]+[2*a]
  report=[{'r':enc(r),'C':enc(correlation_formula(r+q('1e-10'))(r))}for r in points]
  (OUT/f'CORRELATION_PROBE_{par}.json').write_text(json.dumps(report,indent=2)+'\n')
  return
 C0=correlation_formula(h/2)(arb(0));assert C0.contains(1),C0
 print(par,'unit autocorrelation control',C0,flush=True)
 kernel=lambda r:(-r/2).exp()/(1-(-2*r).exp())
 theta=lambda r:(-r/2).exp().atanh()+(-r/2).exp().atan()
 # All correlation breakpoints: 0,h,2a,a+b,2b. Stop before zero with a proved local bound.
 depth=48;cut=h*arb(2)**(-depth)
 near=A*(cut**3/3+cut**2/4)+2*(A*J).sqrt()*(2*cut**2*cut.sqrt()/5+cut*cut.sqrt()/3)+J*(cut**2/2+cut/2)
 panels=[(h*arb(2)**(-k),h*arb(2)**(-k+1))for k in range(depth,0,-1)]
 for left,right in ((h,2*a),(2*a,a+b),(a+b,2*b)):
  lo=left
  while 2*lo<right:panels.append((lo,2*lo));lo=2*lo
  panels.append((lo,right))
 nodes=[arb.legendre_p_root(nodes_count,k,weight=True)for k in range(nodes_count)]
 integrated=arb(0);quad_error=arb(0)
 for idx,(lo,hi)in enumerate(panels):
  mid=(lo+hi)/2;half=(hi-lo)/2;corr=correlation_formula(mid)
  value=sum((half*w*2*kernel(mid+half*x)*(1-corr(mid+half*x))for x,w in nodes),arb(0))
  zz=acb(arb(mid,ub(half)*5/4),arb(0,ub(half)*3/4));assert zz.real>0
  M=ub(2*kernel(zz)*(1-corr(zz)));error=8*half*M*arb(2)**(-2*nodes_count)/(1-arb(1)/2)
  assert value.is_finite() and error.is_finite(),idx
  integrated+=pad(value,error);quad_error+=ub(error)
  if idx%12==0:print(par,'autocorrelation cells',idx,'radius',float(integrated.rad()),flush=True)
 tail=2*theta(2*b);E=integrated+arb(0).union(ub(near))+tail
 channels=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3));prime=arb(0);prime_values={}
 for n,p in channels:
  r=2*a if n==9 else arb(n).log()
  # The autocorrelation is continuous at the breakpoint 2a; choose its right-hand formula there.
  value=correlation_formula(r+q('1e-10'))(r);prime_values[str(n)]=enc(value);prime+=2*arb(p).log()/arb(n).sqrt()*value
 kappa=(8*arb.pi()).log()+arb.const_euler()+arb.pi()/2
 direct=E-kappa-prime
 # Exact rational S0, independently recomputed from the bound A12 model and X_fix.
 AQ=[[Fraction(v)for v in row]for row in fresh['parities'][par]['midpoint']];XQ=[[Fraction(v)for v in row]for row in fixed['parities'][par]['X']]
 assert AQ==list(map(list,zip(*AQ)))and XQ==list(map(list,zip(*XQ)))
 SQ=[[XQ[i][j]+XQ[j][i]-sum((XQ[k][i]*AQ[k][l]*XQ[l][j]for k in range(12)for l in range(12)),Fraction(0))for j in range(12)]for i in range(12)]
 S0=arb_mat([[q(v)for v in row]for row in SQ]);pivots=positive_pivots(S0)
 F=arb_mat([[box(v)]for v in previous['Fhat_z']]);correction=(F.transpose()*S0*F)[0,0];assert correction>0
 fixed_energy=energy['parities'][par]['fixed_X'];EK=q(fixed_energy['direct_K_error_upper'])
 rhs=2*q(funcs['parities'][par]['whole_F12_operator_error_upper'])*q(fixed_energy['T_norm_upper'])+q(fresh['parities'][par]['whole_Loewner_radius'])*q(fixed_energy['T_norm_squared_upper'])
 assert EK>=rhs
 KP=pad(direct-correction,EK)
 budget=load_bound('research/x-c1/nstar-jp-spike-orthogonality-2026-10-16/original/gpt2-kp-budgets/expected/BUDGET_BOUNDS.json',bind)['parities'][par]
 assert EK.contains(q(budget['two_sided_K_model_error_upper']))
 old=box(previous['K_upper_majorant']);coarse_corrected=old-correction
 L=box(previous['L00']);alpha=q('10/11')*q(budget['q']);epsD=q(budget['D_model_scalar_error_upper'])
 if KP.upper()<0:threshold=None;outcome='DIRECT_K_UPPER_NEGATIVE'
 else:
  threshold=(alpha*KP.upper()).sqrt()+epsD
  if L>threshold or L< -threshold:outcome='EXCLUDES_FOR_DIRECTION'
  elif ub(L)<=threshold.lower():outcome='DOES_NOT_EXCLUDE_FOR_DIRECTION'
  else:outcome='INCONCLUSIVE_FOR_DIRECTION'
 out={'status':'AUTHOR_DERIVED_CONDITIONAL_DIRECTED_K_P_EXTERNAL_REVIEW_OPEN','parity':par,'candidate_sha256':bind['repository_files'][candidate_rel],
  'inherited_scalar_sha256':bind['repository_files'][cert_rel],'normalization':enc(norm),'C_zero':enc(C0),
  'piecewise_derivative_square':enc(A),'jump_square_sum':enc(J),'near_zero_cutoff':enc(cut),'near_zero_energy_upper':enc(near),
  'outer_energy_integral':enc(integrated),'quadrature_remainder_sum_upper':enc(quad_error),'whole_large_r_energy':enc(tail),
  'translation_energy':enc(E),'prime_correlations':prime_values,'whole_prime_term':enc(prime),'kappa':enc(kappa),'direct_form':enc(direct),
  'S0_positive_pivots':[enc(v)for v in pivots],'subtracted_F_S0_F':enc(correction),'K_model_error':enc(EK),
  'old_K_majorant':enc(old),'old_majorant_minus_correction':enc(coarse_corrected),'actual_K_P_interval':enc(KP),
  'K_P_upper_rational':str(KP.upper().fmpq()),'threshold':enc(threshold)if threshold is not None else None,
  'inherited_L_interval':enc(L),'outcome':outcome,'gauss_nodes':nodes_count,'near_zero_dyadic_depth':depth,'cells':len(panels),'precision_bits':ctx.prec,
  'response_input_member_sha256':{name:hashlib.sha256(member(z,name)).hexdigest()for name in ('inputs/FRESH_A12.json','inputs/FROZEN_RESPONSE12.json','inputs/FUNCTIONS12.json','RESPONSE_ENERGY.json')}}
 assert KP.rad()<q('1e-8'),KP
 (OUT/f'SHARP_K_{par}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(par,'E',E,'prime',prime,'d',direct,'correction',correction,'K_P',KP,'threshold',threshold,'outcome',outcome,flush=True)
if __name__=='__main__':main(sys.argv[1],int(sys.argv[2])if len(sys.argv)>2 else 128)
