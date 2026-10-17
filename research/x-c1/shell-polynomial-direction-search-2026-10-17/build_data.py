"""Exploratory degree-11 residual maps, with all parities separate.

Uses only the bound repository inputs. Arb is used to retain cancellation;
Gauss integration in this candidate builder is NOT a directed certificate.
"""
import os,sys,json,gzip,time,math,hashlib
from pathlib import Path
from fractions import Fraction
from flint import arb,arb_poly,arb_series,arb_mat,ctx
ctx.prec=600
HERE=Path(__file__).resolve().parent
PACKAGE=HERE.parent/'nstar-jp-spike-orthogonality-2026-10-16'
INPUTS=Path(os.environ['OBJEKT_X_STAGE5_INPUTS'])
OUT=Path(os.environ.get('OBJEKT_X_SEARCH_OUTPUT',str(HERE/'data')));OUT.mkdir(exist_ok=True,parents=True)

def q(s):
 f=Fraction(s);return arb(f.numerator)/f.denominator
def box(v):return q(v[0]).union(q(v[1]))
def mid(v):return box(v).mid()
def dot(x,y):return sum((a*b for a,b in zip(x,y)),arb(0))
BOUND_INPUTS=None
def load(p):
 if BOUND_INPUTS is not None:assert p.resolve() in BOUND_INPUTS,'unbound input: '+str(p)
 return json.loads(p.read_bytes())
def poly(v):return arb_poly(v)
def legpolys(n):
 p=[poly([1]),poly([0,1])]
 for k in range(1,n-1):p.append(((2*k+1)*poly([0,1])*p[k]-k*p[k-1])*(arb(1)/(k+1)))
 return p[:n]
def pint(p,s):return sum((c*s**(k+1)/(k+1) for k,c in enumerate(p)),arb(0))
def plogint(p,s):return sum((c*s**(k+1)*(s.log()/(k+1)-arb(1)/(k+1)**2) for k,c in enumerate(p)),arb(0))
def af(v):return float(v.mid())
def vec(v):return [af(x) for x in v]
def mat(v):return [[af(v[i,j]) for j in range(v.ncols())]for i in range(v.nrows())]
def enc(v):return str(v.mid().fmpq())

def main(par,ncore=384):
 global BOUND_INPUTS
 bindings=load(HERE/'INPUT_BINDINGS.json')
 BOUND_INPUTS={(HERE.parents[2]/rel).resolve() for rel in bindings['repository_files']}|{(INPUTS/rel).resolve() for rel in bindings['prepared_inputs']}
 for rel,digest in bindings['repository_files'].items():assert hashlib.sha256((HERE.parents[2]/rel).read_bytes()).hexdigest()==digest,rel
 for rel,digest in bindings['prepared_inputs'].items():assert hashlib.sha256((INPUTS/rel).read_bytes()).hexdigest()==digest,rel
 sigma=int(par=='odd');eps=(-1)**sigma
 a8=3*arb(2).log()/2;a=arb(3).log();b=arb(11).log()/2;hs=a-a8;h=b-a
 mu8=(a8*eps+a8.sinh())/2;mu=(a*eps+arb(4)/3)/2
 m=lambda x:(x/2).cosh() if sigma==0 else (x/2).sinh()
 legs=legpolys(384);ell=[legs[j](poly([-1-2*a/h,2/h]))*(arb(2*j+1)/(2*h)).sqrt() for j in range(12)]
 nshell=128;nr=360;ctx.cap=nr+2
 # Regular Gamma kernel: exp(r/2)/(2sinh r)-1/(2r), analytic for |r|<pi.
 fac=[arb(1)]
 for j in range(1,nr+15):fac.append(fac[-1]*j)
 sh=arb_series([1/fac[j+1] if j%2==0 else arb(0) for j in range(nr+2)],prec=nr+2)
 ex=arb_series([1/(2**j*fac[j]) for j in range(nr+2)],prec=nr+2)
 reg=(ex/sh)/2;assert reg.prec>=nr+2
 g=[reg[j+1] for j in range(nr+1)]
 A=poly([g[j]*fac[j] for j in range(nr,-1,-1)])
 powers_a=[a**j for j in range(nr+14)];powers_b=[b**j for j in range(nr+14)]
 moments=[(powers_b[j+1]-powers_a[j+1])/(j+1) for j in range(nr+12)]
 gamma=[];quot=[]
 for en in ell:
  muvec=[sum((c*moments[j+k] for k,c in enumerate(en)),arb(0)) for j in range(nr+1)]
  conv=A*poly([v/fac[j] for j,v in enumerate(muvec)])
  gamma.append(poly([conv[nr-k]/fac[k]*((-1)**k+eps) for k in range(nr+1)]))
  quot.append(poly([sum((en[j]*moments[j-k-1] for j in range(k+1,len(en))),arb(0))for k in range(len(en)-1)]))
 # Moment function on the new shell and W Gram.
 gn=[arb.legendre_p_root(64,k,weight=True) for k in range(64)]
 lam=[sum((h/2*w*m((a+b)/2+h*z/2)*en((a+b)/2+h*z/2)for z,w in gn),arb(0)) for en in ell]
 G=arb_mat([[arb(int(i==j))+2*lam[i]*lam[j]/mu for j in range(12)]for i in range(12)])
 Ac=[-v/mu for v in lam]
 funcs=load(INPUTS/'FUNCTIONS12.json')['parities'][par]['functions'];fr=load(INPUTS/'FROZEN_RESPONSE12.json')['parities'][par]
 X=arb_mat([[q(x)for x in row]for row in fr['X']])
 # Frozen physical Fhat; exact log moments, smooth expansions through degree 120.
 s=b/a-1;order=120
 lp=poly([arb(0)]+[arb((-1)**(j+1))/(j*2**j)for j in range(1,order+1)])
 M=poly([((a/2).cosh() if (sigma+j)%2==0 else (a/2).sinh())*(a/2)**j/fac[j] for j in range(order+1)])
 W=[en(poly([a,a]))+lam[j]/mu*M for j,en in enumerate(ell)]
 F=[]
 for fj in funcs:
  sp=fj['F'];P=poly(list(map(q,sp['polynomial'])))(poly([1,1]));Q=poly(list(map(q,sp['log_ratio_multiplier'])))(poly([1,1]));cm=q(sp['physical_W_moment_multiplier'])
  pp=P+Q*(poly([arb(2).log()])+lp)+cm*M
  F.append([2*a/(2*a).sqrt()*(pint(pp*ww,s)-plogint(Q*ww,s))for ww in W])
 F=arb_mat(F);T=X*F
 logs={n:arb(n).log()for n in(2,3,4,5,7,8,9)};channels=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
 Dpoly=[sum((T[i,j]*poly(list(map(q,fj['D']['polynomial'])))for i,fj in enumerate(funcs)),poly([]))for j in range(12)]
 Dv=[sum((T[i,j]*poly(list(map(q,fj['D']['V_multiplier'])))for i,fj in enumerate(funcs)),poly([]))for j in range(12)]
 Dm=[sum((T[i,j]*q(fj['D']['moment_multiplier'])for i,fj in enumerate(funcs)),arb(0))for j in range(12)]
 def theta(r):v=(-r/2).exp();return v.atanh()+v.atan()
 def jp(r):return 3*arb(2).log()/2+arb.pi()/4-r-(1-(-2*r).exp()).log()/2
 def jm(r):v=(-r).exp();return arb(2).log()/2+arb.pi()/4-((1-v)/(1+v)).log()/2
 def cell(lo,hi):
  midx=(lo+hi)/2;dp=[poly(p)for p in Dpoly];terms=[]
  for i,fj in enumerate(funcs):
   for term in fj['D']['shift_terms']:
    sh=logs[int(term['channel'])]/a
    dl,dh=(arb(0),1-sh)if int(term['translation_sign'])==1 else(max(arb(0),sh-1),arb(1))
    if dl<midx/a<dh:
     pp=poly(list(map(q,term['polynomial'])))
     for j in range(12):dp[j]+=T[i,j]*pp
  for n,prime in channels:
   for sign in(-1,1):
    shift=sign*logs[n];y=midx+shift;weight=arb(prime).log()/arb(n).sqrt()
    if -a<y<a:terms.append((weight,shift,'core'))
    elif a<y<b:terms.append((weight,shift,'plus'))
    elif -b<y<-a:terms.append((weight,shift,'minus'))
  def value(x):
   ep=(x/2).exp();ms=(ep*(jp(a-x)+jm(a+x))+eps/ep*(jm(a-x)+jp(a+x)))/2
   logm=((b-x)/(a-x)).log();logp=((b+x)/(a+x)).log();vlog=-(1-(x/a)**2).log()/2;mx=m(x)
   out=[]
   for j in range(12):
    shell=(ell[j](x)*logm+quot[j](x)+eps*(ell[j](-x)*logp+quot[j](-x)))/2+gamma[j](x)
    prime=sum((ww*(Ac[j]*m(x+sh)if kind=='core' else ell[j](x+sh)if kind=='plus' else eps*ell[j](-x-sh))for ww,sh,kind in terms),arb(0))
    out.append(Ac[j]*ms-shell-prime-(dp[j](x/a)+Dv[j](x/a)*vlog+Dm[j]*mx)/(2*a).sqrt())
   return out
  return value
 # Entire source-kernel control against the exact constant-shell primitive.
 for xx in (a/7,a/2,6*a/7):
  new=(ell[0](xx)*((b-xx)/(a-xx)).log()+eps*ell[0](-xx)*((b+xx)/(a+xx)).log())/2+gamma[0](xx)
  old=ell[0][0]*(theta(a-xx)-theta(b-xx)+eps*(theta(a+xx)-theta(b+xx)))
  assert abs(new-old)<arb('1e-38'),str(new-old)
 print(par,'constant-shell Gamma control PASS; series precision',reg.prec,flush=True)
 cuts=sorted([a-logs[2],b-logs[2],b-a]+[logs[k]-a for k in(4,5,7,8)]+[logs[k]-b for k in(4,5,7,8)]+[2*a-b],key=af)
 edges=[arb(0)]+cuts+[a8]
 psi=load(PACKAGE/'original/gpt1-stufe1-zertifikat/expected/PSI_CORRECTED.json')['data'][par]['directions']['lower_Pv']
 psiP=poly([mid(v)for v in psi['core_polynomial_scaled_x_over_a8_interval']]);psiM=mid(psi['core_m_multiplier_model_interval'])
 psiS=sum((mid(v)*(arb(2*n+1)/(2*hs)).sqrt()*legs[n]for n,v in enumerate(psi['shell_model_coefficients_interval'])),poly([]))
 fa=load(PACKAGE/'original/gpt2-stufe3-endliche-u8-antwort/expected/FINITE_ACTION.json')[par]['directions']['lower_Pv'];c=arb_mat([[mid(v) for v in fa['c_model']]])
 def moment(n,endpoint):
  z=endpoint/2;t=z**n*2**n*arb.fac_ui(n)/arb.fac_ui(2*n+1);v=t
  for k in range(1,160):t*=z*z/(2*k*(2*n+2*k+1));v+=t
  return v*arb(2*n+1).sqrt()
 degs=list(range(sigma+2,sigma+383,2));base=moment(sigma,a8);beta=[moment(n,a8)/base for n in degs]
 Z=[(arb(2*n+1)/(2*a)).sqrt()*legs[n]-(moment(n,a)/moment(sigma,a))*(arb(2*sigma+1)/(2*a)).sqrt()*legs[sigma]for n in range(sigma+2,sigma+10,2)]
 hb=load(INPUTS/'HALF_INVERSE_1536.json');dirs=load(INPUTS/'DIRECTIONS.json')[par]['directions']['upper_v'];zt=list(map(q,dirs['Zt_exact_rational']));jr=[box(v)for v in dirs['Jt_local_orthonormal_Legendre_coefficients_interval']]
 valid=[]
 for cand in hb['blocks']:
  qm=[[box(v)for v in row]for row in cand['basis_Q_local_coefficients']]
  if all(dot(row,zt).overlaps(v)for row,v in zip(qm,jr)):valid.append((cand,qm))
 assert len(valid)==1
 blk,qm=valid[0];sm=[[q(v)for v in row]for row in blk['half_inverse_centre_rational_Q_coefficients']]
 Y=[sum((dot(qm[n],[sm[k][j]for k in range(92)])*(arb(2*n+1)/(2*hs)).sqrt()*legs[n]for n in range(96)),poly([]))for j in range(8)]
 mr=arb_mat(1,12);mc=arb_mat(1,12);pr=arb_mat(1,12);pm=arb(0);RR=arb_mat(12,12);RC=arb_mat(12,12);Phi=arb_mat(191,12);Bf=arb_mat(12,12);lamY=[arb(0)]*8
 nodes={n:[arb.legendre_p_root(n,k,weight=True)for k in range(n)]for n in(ncore,nshell)}
 for region,panels,n in [('core',list(zip(edges[:-1],edges[1:])),ncore),('shell',[(a-hs*arb(2)**(-k),a-hs*arb(2)**(-k-1))for k in range(60)],nshell)]:
  for ix,(lo,hi) in enumerate(panels):
   rv=cell(lo,hi);rows=[];weighted=[];mweights=[];pweights=[];phivals=[];zvals=[];yv=[]
   for z,w in nodes[n]:
    xx=(lo+hi)/2+(hi-lo)*z/2;ww=(hi-lo)*w/2;mm=m(xx);rr=rv(xx);pp=psiP(xx/a8)+psiM*mm if region=='core' else psiS((2*xx-a8-a)/hs)
    rows.append(rr);weighted.append([ww*v for v in rr]);mweights.append(ww*mm);pweights.append(ww*pp);pm+=ww*pp*mm
    zvals.append([zz(xx/a)for zz in Z])
    if region=='core':
     ps=[arb(1),xx/a8]
     for k in range(1,383):ps.append(((2*k+1)*(xx/a8)*ps[k]-k*ps[k-1])/(k+1))
     phivals.append([(arb(2*k+1)/(2*a8)).sqrt()*ps[k]-bb*(arb(2*sigma+1)/(2*a8)).sqrt()*ps[sigma]for k,bb in zip(degs,beta)])
    else:
     yy=[y((2*xx-a8-a)/hs)for y in Y];yv.append(yy)
     for j,y in enumerate(yy):lamY[j]+=ww*y*mm
   R=arb_mat(rows);WR=arb_mat(weighted);mom=arb_mat([mweights])*R;mr+=mom;pr+=arb_mat([pweights])*R;rrg=R.transpose()*WR;RR+=rrg
   zpair=arb_mat(zvals).transpose()*WR
   for i in range(4):
    for j in range(12):Bf[i,j]+=2*zpair[i,j]
   if region=='core':mc+=mom;RC+=rrg;Phi+=2*arb_mat(phivals).transpose()*WR
   else:
    yy=2*arb_mat(yv).transpose()*WR
    for i in range(8):
     for j in range(12):Bf[i+4,j]+=yy[i,j]
   if ix%20==0:print(par,region,ix,flush=True)
 for i in range(8):
  for j in range(12):Bf[i+4,j]-=2*lamY[i]*mc[0,j]/mu8
 H=2*(RR-mr.transpose()*mr*(1/mu));H8=2*(RC-mc.transpose()*mc*(1/mu8))
 I0=2*(pr-mr*(pm/mu))-c*Phi
 common=json.loads(gzip.decompress((INPUTS/'stage3/inputs/REFINED_COMMON96.json.gz').read_bytes()))['cases'][sigma]
 C=arb_mat([[arb(int(v))/int(common['inverse_congruence_denominator'])for v in row]for row in common['inverse_congruence_integer_matrix']]);CP=C.transpose()*Phi
 coh=load(PACKAGE/'original/gpt2-kp-und-kohaerenter-transport/expected/COHERENT_TRANSPORT_INPUTS.json')['parities'][par]['directions']['p'];metric=arb_mat([[q(v)for v in row]for row in coh['metric_G_equals_eta_squared_K_inverse']])
 assert psi['k_model_exact']==coh['fixed_k0_rational']
 high=load(PACKAGE/'original/gpt2-stufe4-hochantwort/expected/COMPLETE_HIGH_RESPONSE.json')[par]['directions']['lower_Pv']
 kp=load(PACKAGE/'original/gpt2-kp-budgets/expected/BUDGET_BOUNDS.json')['parities'][par]
 # Derivative norm and jump maps for direction-dependent translation budgets.
 deriv=[en.derivative()for en in ell]
 def ipoly(p):return pint(p,b)-pint(p,a)
 muprime=((a*(-eps)+a.sinh())/2)/4
 DA=arb_mat([[2*ipoly(deriv[i]*deriv[j])+2*Ac[i]*Ac[j]*muprime for j in range(12)]for i in range(12)])
 jumps=arb_mat([[en(a)-Ac[j]*m(a)for j,en in enumerate(ell)],[en(b)for en in ell]])
 JG=2*jumps.transpose()*jumps
 coefz0=1/G[0,0].sqrt()
 ref=load(HERE.parent/'l00-z0-directed-interval-2026-10-17/expected'/f'L00_CERTIFICATE_{par}.json')
 dev=abs(I0[0,0]*coefz0-mid(ref['I0']))
 print(par,'I0 z0',I0[0,0]*coefz0,'deviation',dev,flush=True)
 assert dev<arb('1e-8'),str(dev)
 out={'status':'EXPLORATORY_NOT_DIRECTED','parity':par,'basis':'ell_n=sqrt((2n+1)/(2h))*P_n(2(x-a)/h-1), n=0..11',
  'G_W':mat(G),'I0_row':mat(I0)[0],'H_gram':mat(H),'H8_gram':mat(H8),'feature_factor':mat(CP),'psi_k_gram':mat(Bf.transpose()*metric*Bf),
  'b_F':mat(Bf),'Fhat':mat(F),'T':mat(T),'derivative_gram':mat(DA),'jump_gram':mat(JG),
  'high_multiplier':af(q(high['whole_physical_high_U8_part_norm_upper'][1])),
  'feature_multiplier':af(q(high['finite_pairing_feature_error_multiplier'][1])/(1-q(common['rho'])).sqrt()),
  'q':kp['q'],'D_model_scalar_error_upper':kp['D_model_scalar_error_upper'],
  'K_whole_W_unit_upper':kp['all_degree_at_most_11_K_P_upper_per_W_norm_squared'],
  'K_model_error_upper':kp['two_sided_K_model_error_upper'],
  'z0_coefficient':af(coefz0),'z0_I0_control_difference':af(dev),'gamma_regular_degree':nr,'precision_bits':ctx.prec,'core_gauss_nodes':ncore,'shell_gauss_nodes':nshell,'shell_panels':60,
  'exact_midpoint_I0_row':[enc(I0[0,j])for j in range(12)]}
 (OUT/f'MAPS_{par}_{ncore}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(par,'I0 row',out['I0_row'],flush=True)

if __name__=='__main__':main(sys.argv[1],int(sys.argv[2])if len(sys.argv)>2 else 384)
