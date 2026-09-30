"""Full-space inverse moments on true canonical extension spaces.

Polynomial trial spaces define coordinates, not substitutes for spectral spaces.
Directionwise projection bounds certify the exact canonical annihilator.
No global terminal-floor inverse bound is used.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json,shutil,subprocess,time
import flint
from flint import arb,arb_mat,fmpq,ctx

PIN='8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b'
FAMILY='research/x-c1/renewable-low-schur-spectral-2026-09-29/'
DEN=10**100
def rat(x):
 f=F(x);return arb(fmpq(f.numerator,f.denominator))
def ball(x,den=None):
 l,h=map(F,x)
 if den:l,h=l/den,h/den
 assert l<=h
 return rat((l+h)/2)+arb(0,rat((h-l)/2))
def mat(x,den=None):return arb_mat([[ball(v,den) for v in row] for row in x])
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def pointup(x):return x.upper()
def absupper(x):return abs(x).upper()
def exact(x,lower=True):
 v=x.lower() if lower else x.upper();m,e=map(int,v.man_exp())
 return str(F(m*2**e) if e>=0 else F(m,2**(-e)))
def iv(x):return [exact(x),exact(x,False)]
def mi(x):return [[iv(x[i,j]) for j in range(x.ncols())] for i in range(x.nrows())]
def dotcol(m,j):
 out=sum((m[i,j]*m[i,j] for i in range(m.nrows())),arb(0))
 assert out.is_finite()
 return out
def nonnegative_upper(x):
 assert x.is_finite(),('nonfinite bound',x)
 assert x.upper()>=0,('negative upper bound for nonnegative quantity',x)
 return x.upper()
def gupper(x):
 assert all(v.is_finite() for v in x.entries())
 return max(x[i,i].upper()+sum((absupper(x[i,j]) for j in range(x.ncols()) if j!=i),arb(0)) for i in range(x.nrows()))
def glower(x):
 assert all(v.is_finite() for v in x.entries())
 return min(x[i,i].lower()-sum((absupper(x[i,j]) for j in range(x.ncols()) if j!=i),arb(0)) for i in range(x.nrows()))
def fixed_bound(x,upper):
 assert all(v.is_finite() for v in x.entries())
 ds=[abs(x[i,i]).upper().sqrt().mid() for i in range(x.nrows())]
 assert all(z>0 for z in ds)
 xn=arb_mat([[x[i,j]/(ds[i]*ds[j]) for j in range(x.ncols())] for i in range(x.nrows())])
 c=((xn+xn.transpose())/2).mid()
 err=max(sum((absupper(xn[i,j]-c[i,j]) for j in range(x.ncols())),arb(0)) for i in range(x.nrows())).upper()
 c=c+(eye(x.nrows())*err if upper else -eye(x.nrows())*err)
 return arb_mat([[c[i,j]*ds[i]*ds[j] for j in range(x.ncols())] for i in range(x.nrows())])
def chol(g):
 n=g.nrows();l=arb_mat(n,n)
 for i in range(n):
  v=g[i,i]-sum((l[i,k]*l[i,k] for k in range(i)),arb(0));assert v>0,('Gram pivot',i,v)
  l[i,i]=v.sqrt()
  for j in range(i+1,n):l[j,i]=(g[j,i]-sum((l[j,k]*l[i,k] for k in range(i)),arb(0)))/l[i,i]
 return l
def ortho(g):return chol(g).transpose().inv()
def square_bounds(x):
 assert x.is_finite()
 lo,hi=x.lower(),x.upper();top=max(abs(lo),abs(hi))
 bottom=arb(0) if x.contains(0) else min(abs(lo),abs(hi))
 return bottom*bottom,top*top
def frob_bounds(x):
 pairs=[square_bounds(v) for v in x.entries()]
 return sum((p[0] for p in pairs),arb(0)),sum((p[1] for p in pairs),arb(0))
def gram_enclosure(x):
 g=x.transpose()*x
 for j in range(x.ncols()):
  lo,hi=frob_bounds(arb_mat([[x[i,j]] for i in range(x.nrows())]))
  g[j,j]=(lo+hi)/2+arb(0,((hi-lo)/2).upper())
 return g
def entry_hull_from_order(lo,hi):
 assert all(v.is_finite() for v in lo.entries()+hi.entries())
 n=lo.nrows();out=arb_mat(n,n);delta=hi-lo
 ds=[nonnegative_upper(delta[i,i]) for i in range(n)]
 for i in range(n):
  for j in range(n):out[i,j]=(lo[i,j]+hi[i,j])/2+arb(0,(ds[i]*ds[j]).sqrt().upper()/2)
 return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
 p.add_argument('--out',type=Path,required=True);p.add_argument('--bits',type=int,default=1024)
 a=p.parse_args();ctx.prec=a.bits;assert flint.__version__=='0.9.0'
 git=shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe'
 assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==PIN
 sources={}
 def read(rel,zipped=False):
  raw=(a.repo/rel).read_bytes()
  assert raw==subprocess.check_output([git,'show',PIN+':'+rel],cwd=a.repo),rel
  sources[rel]=hashlib.sha256(raw).hexdigest()
  return json.loads(gzip.decompress(raw) if zipped else raw) if (rel.endswith('.json') or zipped) else raw
 outer=FAMILY+'07-canonical-extension-outer-mass/'
 data=read(outer+'primary.json');cross=read(outer+'crosscheck.json');receipt=read(outer+'verification.json')
 assert sources[outer+'primary.json']==receipt['primary_sha256']
 assert sources[outer+'crosscheck.json']==receipt['crosscheck_sha256']
 for rel,h in receipt['source_sha256'].items():
  read(rel,rel.endswith('.gz'));assert sources[rel]==h
 for rel in (FAMILY+'06-critical-spectral-transport/PROOF.md',FAMILY+'05-canonical-spectral-ranks/verification.json',outer+'PROOF.md'):
  read(rel)
 vectors=read(FAMILY+'05-canonical-spectral-ranks/fixed_vectors.json')
 assert sources[FAMILY+'05-canonical-spectral-ranks/fixed_vectors.json']==data['vectors_sha256']
 results={};rescache={}
 for key,old_result in data['results'].items():
  started=time.time();trans,par=key.rsplit('-',1);old,new=trans.split('->')
  at,bt=data['trials'][old+'-'+par],data['trials'][new+'-'+par]
  sa,sb=mat(at['physical_Ritz_matrix']),mat(bt['physical_Ritz_matrix'])
  va,vb=rat(at['physical_complement_gap_lower_exact']),rat(bt['physical_complement_gap_lower_exact'])
  m=mat(old_result['trial_overlap']);na,nb=m.nrows(),m.ncols();dim=nb-na
  qa=[sa[i,i].upper() for i in range(na)];qb=[sb[j,j].upper() for j in range(nb)]
  eta=[(q/va).sqrt().upper() for q in qa]
  assert gupper(sa)<va and gupper(sb)<vb
  rem=[nonnegative_upper(1-dotcol(m,j)).sqrt().upper() for j in range(nb)]
  # Exact Y = b(J P_A U_A, P_B U_B)/17. Radius pays BOTH projections.
  y=arb_mat(na,nb)
  for i in range(na):
   for j in range(nb):
    err=eta[i]*(sum((eta[k]*absupper(m[k,j]) for k in range(na)),arb(0))+rem[j])
    err+=(qa[i]*qb[j]).sqrt()*(1/vb+arb(1)/17)
    y[i,j]=m[i,j]+arb(0,err.upper())
  mc=arb_mat([[m[i,j].mid() for j in range(na)] for i in range(na)])
  rc=arb_mat([[m[i,j].mid() for j in range(na,nb)] for i in range(na)])
  n0=(-mc.inv()*rc).mid()
  w0=arb_mat([[n0[i,j] if i<na else arb(int(i-na==j)) for j in range(dim)] for i in range(nb)])
  residual=m*w0;gram0=w0.transpose()*w0;energy0=w0.transpose()*sb*w0
  errs=arb_mat(na,dim)
  for i in range(na):
   for j in range(dim):
    de=nonnegative_upper(gram0[j,j]-dotcol(residual,j)).sqrt().upper()
    er=eta[i]*(sum((eta[k]*absupper(residual[k,j]) for k in range(na)),arb(0))+de)
    er+=(qa[i]*energy0[j,j].upper()).sqrt()*(1/vb+arb(1)/17)
    errs[i,j]=(abs(residual[i,j])+er).upper()
  inv=mc.inv();ai=arb_mat([[absupper(inv[i,j]) for j in range(na)] for i in range(na)])
  el=arb_mat([[absupper(y[i,j]-mc[i,j]) for j in range(na)] for i in range(na)])
  cm=ai*el;cm=arb_mat([[cm[i,j].upper() for j in range(na)] for i in range(na)])
  contraction=max(sum((cm[i,j] for j in range(na)),arb(0)) for i in range(na)).upper()
  assert contraction<1
  radius=(eye(na)-cm).inv()*(ai*errs)
  assert all(x>0 for x in radius.entries())
  radius=arb_mat([[radius[i,j].upper()*rat('1.000000000000000000000000000001') for j in range(dim)] for i in range(na)])
  n=arb_mat([[n0[i,j]+arb(0,radius[i,j].upper()) if i<na else arb(int(i-na==j)) for j in range(dim)] for i in range(nb)])
  print(key,'canonical annihilator certified; building full resolvent moments',flush=True)
  # Physical U_B=M V, using exactly the L2 trial basis from the outer package.
  folder=f'research/x-c1/chambers-through-a11-2026-09-28/{new.lower()}/'
  model=read(folder+new.lower()+'_model.json.gz',True)
  res=read(folder+'reserve_results.json');low=read(folder+'reserve_results_lower_matrices.json.gz',True)
  pi=int(par=='odd');ds=list(range(pi+2,model['cutoff']+1,2));nn=len(ds)
  coef=arb_mat([[rat(vectors[new+'-'+par+'-'+str(j+1)]['coefficients'][i]) for j in range(nb)] for i in range(nn)])
  coef=coef*mat(bt['orthogonalizer'])
  ep=ball(model['endpoint_interval'],DEN)
  me=arb(2*pi+1).sqrt()*ball(model['raw_low_moments'][pi],DEN)
  tl=arb_mat([[arb(2*d+1).sqrt()*ball(model['raw_low_moments'][d],DEN)/me] for d in ds])
  carrier=-tl.transpose()*coef
  rho=((ep.sinh()/ep+(1 if pi==0 else -1))/2)/(me*me)
  tail2=nonnegative_upper(rho-1-(tl.transpose()*tl)[0,0])
  dual=coef-tl*carrier
  hgram=(carrier.transpose()*carrier)*tail2
  ff=mat(low['parities'][par]['lower_matrix'],DEN)
  ll=mat(model['parities'][par]['A'],DEN)+eye(nn)*rat(res['low_form_error_exact'])
  eb=rat(res['parities'][par]['coupling_operator_error_exact'])
  hup=mat(model['parities'][par]['complete_model_raw_high_Gram'],DEN)*rat('1001/1000')+eye(nn)*(1001*eb*eb)
  delta=rat(res['full_high_physical_floor'])
  # Solve only the selected trial right sides; solve against Hup for a trace.
  vlo=ll.solve(dual,algorithm='precond');vhi=ff.solve(dual,algorithm='precond')
  gamma=ff.solve(hup,algorithm='precond').trace().upper();assert gamma>0
  young=rat('1e-20')
  tlo=dual.transpose()*vlo
  thi=(1+young)*(dual.transpose()*vhi)+hgram*((1+1/young)*gamma/(delta*delta)+1/delta)
  assert all(x.is_finite() for x in thi.entries())
  # True basis V0=P_B U_B N; the last d coefficients of N are exactly I.
  en=n.transpose()*sb*n;gn=n.transpose()*n
  g=arb_mat(dim,dim)
  for i in range(dim):
   for j in range(dim):
    err=(en[i,i].upper()*en[j,j].upper()).sqrt()/vb
    g[i,j]=gn[i,j]+arb(0,err.upper())
  assert glower(g)>0
  flo,fhi=chol(tlo).transpose(),chol(thi).transpose()
  zlo=gram_enclosure(flo*n)-en/(vb*vb)
  zhi=gram_enclosure(fhi*n)
  # A variational lower bound for the true projected energy, without a tiny
  # global floor. Polynomial dual probes W optimize the already bounded inverse.
  w=thi.mid().solve(n.mid(),algorithm='precond').mid()
  ew=w.transpose()*sb*w;test_hi=w.transpose()*thi*w
  overlap=w.transpose()*n
  for i in range(dim):
   for j in range(dim):
    er=(ew[i,i].upper()*en[j,j].upper()).sqrt()/vb
    overlap[i,j]+=arb(0,er.upper())
  lower_family=overlap.transpose()*test_hi.inv()*overlap
  lminus=fixed_bound(lower_family,False);lplus=fixed_bound(en,True)
  clow,chi=chol(lminus),chol(lplus)
  # All traces are evaluated on the SAME exact canonical coefficient basis.
  gi=g.inv()
  trlo=frob_bounds(flo*n*gi*clow)[0]-(gi*lminus*gi*en).trace().upper()/(vb*vb)
  trhi=frob_bounds(fhi*n*gi*chi)[1]
  assert trlo>0 and trhi>0,(key,trlo,trhi)
  phi_lo=trlo.lower()/dim;phi_hi=trhi.upper()
  theta=rat(receipt['trials'][new+'-'+par]['theta_upper_exact'])
  # In physical orthonormal coordinates: f(L)=L/(L+17I)^2.
  beta_lo=289*phi_lo/(17+theta)**2
  beta_hi=phi_hi+(theta+34)*theta/289
  assert beta_lo>1
  survival_lo=1/beta_hi;survival_hi=1/beta_lo
  # Actual entry intervals, not entrywise Loewner bounds: order-to-entry hull.
  l_entries=entry_hull_from_order(lminus,en)
  z_entries=entry_hull_from_order(zlo,zhi)
  o=ortho(g)
  lphys=o.transpose()*l_entries*o;zphys=o.transpose()*z_entries*o
  l_floor=1/(lminus.inv().trace().upper()*gupper(g))
  z_floor=1/theta
  z_ceiling=gupper(fixed_bound(zhi,True))/glower(g)
  results[key]={'dimension':dim,'canonical_N':mi(n),'annihilator_Y':mi(y),
   'central_left':mi(mc),'inverse_central_left':mi(inv),
   'central_N':mi(w0),'residual_absolute_bound':mi(errs),'contraction_matrix':mi(cm),
   'contraction_max_row_sum_upper_exact':exact(contraction,False),
   'coordinate_radii':mi(radius),'trial_resolvent_lower':mi(tlo),'trial_resolvent_upper':mi(thi),
   'dual_probe_coefficients':mi(w),'dual_overlap_enclosure':mi(overlap),
   'dual_probe_inverse_upper':mi(test_hi),
   'trial_resolvent_lower_factor':mi(flo),'trial_resolvent_upper_factor':mi(fhi),
   'energy_lower_factor':mi(clow),'energy_upper_factor':mi(chi),
   'high_dual_tail_squared_upper_exact':exact(tail2,False),'relative_high_trace_upper_exact':exact(gamma,False),
   'canonical_basis_L2_Gram':mi(g),'energy_Loewner_lower_in_raw_basis':mi(lminus),
   'trial_energy_on_N':mi(en),
   'energy_Loewner_upper_in_raw_basis':mi(lplus),
   'inverse_lower_family_in_raw_basis':mi(zlo),'inverse_upper_family_in_raw_basis':mi(zhi),
   'physical_energy_entries':mi(lphys),'physical_inverse_energy_entries':mi(zphys),
   'physical_energy_uniform_lower_exact':exact(l_floor),
   'physical_energy_uniform_upper_exact':str(F(receipt['trials'][new+'-'+par]['theta_upper_exact'])),
   'physical_inverse_energy_uniform_lower_exact':exact(z_floor),
   'physical_inverse_energy_uniform_upper_exact':exact(z_ceiling,False),
   'weighted_trace_lower_exact':exact(trlo),'weighted_trace_upper_exact':exact(trhi,False),
   'one_minus_kappa_lower_exact':exact(survival_lo),'one_minus_kappa_upper_exact':exact(survival_hi,False),
   'one_minus_kappa_display':[float(survival_lo.lower()),float(survival_hi.upper())],
   'true_E_used':True,'whole_high_response_included':True,'global_floor_inverse_used':False,
   'seconds':time.time()-started}
  print(key,'1-kappa in',results[key]['one_minus_kappa_display'],flush=True)
  output={'status':'CANONICAL_EXTENSION_RESOLVENT_MOMENTS_CERTIFIED',
   'source_commit':PIN,'precision_bits':a.bits,'source_sha256':sources,
   'canonical_basis':'V0=P_B U_B N, N=[-Y_left^-1 Y_right;I]; V=V0 chol(V0*V0)^-T',
   'results':results,'uses_existing_terminal_positivity':True,
   'forward_renewal_proved':False,'global_terminal_floor_inverse_used':False}
  a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
 print('ALL FOUR CANONICAL RESOLVENT MOMENTS COMPLETE',flush=True)

if __name__=='__main__':main()
