"""Standard-library audit of canonical annihilators and small moment conclusions.

The large directed resolvent solves and Cholesky factor enclosures remain Arb
inputs. The analytic inequalities are proved in CANONICAL_RESOLVENT_MOMENTS.md.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json,shutil,subprocess

PIN='8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b'
def pt(x):return (F(x),F(x))
def iv(x):
 a,b=map(F,x);assert a<=b;return a,b
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 p=[a*b for a in x for b in y];return min(p),max(p)
def div(x,y):
 assert y[0]*y[1]>0
 return mul(x,(1/y[1],1/y[0]))
def ab(x):return max(abs(x[0]),abs(x[1]))
def sq(x):
 hi=ab(x)**2;lo=F(0) if x[0]<=0<=x[1] else min(abs(x[0]),abs(x[1]))**2
 return lo,hi
def total(xs):
 s=pt(0)
 for x in xs:s=add(s,x)
 return s
def rootup(x):
 assert x>=0;s=10**150;k=isqrt(x.numerator*s*s//x.denominator)
 if F(k*k,s*s)<x:k+=1
 assert F(k*k,s*s)>=x
 return F(k,s)
def rootdown(x):
 assert x>=0;s=10**150;k=isqrt(x.numerator*s*s//x.denominator)
 assert F(k*k,s*s)<=x
 return F(k,s)
def sqrtiv(x):
 assert x[0]>0
 return rootdown(x[0]),rootup(x[1])
def matrix(x):return [[iv(v) for v in row] for row in x]
def tr(a):return [list(row) for row in zip(*a)]
def mm(a,b):return [[total(mul(x,y) for x,y in zip(u,v)) for v in tr(b)] for u in a]
def ms(a,b):return [[sub(x,y) for x,y in zip(u,v)] for u,v in zip(a,b)]
def trace(a):return total(a[i][i] for i in range(len(a)))
def scale(c,a):return [[mul(pt(c),v) for v in row] for row in a]
def frob(a):return total(sq(v) for row in a for v in row)
def inverse_small(a):
 if len(a)==1:return [[div(pt(1),a[0][0])]]
 assert len(a)==2
 det=sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0]));assert det[0]>0
 return [[div(a[1][1],det),div(neg(a[0][1]),det)],
         [div(neg(a[1][0]),det),div(a[0][0],det)]]
def inverse_exact(a):
 n=len(a);rows=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
 for j in range(n):
  k=next(k for k in range(j,n) if rows[k][j]);rows[j],rows[k]=rows[k],rows[j]
  rows[j]=[v/rows[j][j] for v in rows[j]]
  for k in range(n):
   if k!=j:
    c=rows[k][j];rows[k]=[v-c*w for v,w in zip(rows[k],rows[j])]
 return [row[n:] for row in rows]
def point_matrix(a):
 assert all(v[0]==v[1] for row in a for v in row)
 return [[v[0] for v in row] for row in a]
def nonnegative_matrix_product(a,b):
 return [[sum(x*y for x,y in zip(u,v)) for v in zip(*b)] for u in a]
def positive(a):
 assert len(a) in (1,2) and a[0][0][0]>0
 if len(a)==2:assert sub(a[1][1],div(mul(a[1][0],a[0][1]),a[0][0]))[0]>0
def overlaps(a,b):
 assert len(a)==len(b)
 for u,v in zip(a,b):
  assert len(u)==len(v)
  for x,y in zip(u,v):assert max(F(x[0]),F(y[0]))<=min(F(x[1]),F(y[1]))
def rounded(x,up=False,digits=5):
 assert x>0;e=0;y=x
 while y<1:y*=10;e-=1
 while y>=10:y/=10;e+=1
 s=10**(digits-1);v=y*s;k=v.numerator//v.denominator
 if up and F(k)<v:k+=1
 r=F(k,s)*(F(10**e) if e>=0 else F(1,10**(-e)))
 assert r>=x if up else r<=x
 return f'{k/s:.{digits-1}f}e{e:+d}',str(r)

def annihilator(receipt,source,key):
 r=receipt;transition,parity=key.rsplit('-',1);old,new=transition.split('->')
 at,bt=source['trials'][old+'-'+parity],source['trials'][new+'-'+parity]
 sa,sb=matrix(at['physical_Ritz_matrix']),matrix(bt['physical_Ritz_matrix'])
 va,vb=F(at['physical_complement_gap_lower_exact']),F(bt['physical_complement_gap_lower_exact'])
 m=matrix(source['results'][key]['trial_overlap']);na,nb=len(m),len(m[0]);dim=nb-na
 qa=[sa[i][i][1] for i in range(na)];qb=[sb[j][j][1] for j in range(nb)]
 eta=[rootup(q/va) for q in qa]
 delta=[rootup(1-sum(sq(m[i][j])[0] for i in range(na))) for j in range(nb)]
 y=matrix(r['annihilator_Y'])
 for i in range(na):
  for j in range(nb):
   err=eta[i]*(sum(eta[k]*ab(m[k][j]) for k in range(na))+delta[j])+rootup(qa[i]*qb[j])*(1/vb+F(1,17))
   assert y[i][j][0]<=m[i][j][0]-err and y[i][j][1]>=m[i][j][1]+err
 w0=matrix(r['central_N']);mw=mm(m,w0);gram=mm(tr(w0),w0);energy=mm(mm(tr(w0),sb),w0)
 residual=[[F(0)]*dim for _ in range(na)]
 for i in range(na):
  for j in range(dim):
   de=rootup(gram[j][j][1]-sum(sq(mw[k][j])[0] for k in range(na)))
   residual[i][j]=ab(mw[i][j])+eta[i]*(sum(eta[k]*ab(mw[k][j]) for k in range(na))+de)+rootup(qa[i]*energy[j][j][1])*(1/vb+F(1,17))
 mc=point_matrix(matrix(r['central_left']));mi=inverse_exact(mc);ai=[[abs(x) for x in row] for row in mi]
 e=[[ab(sub(y[i][j],pt(mc[i][j]))) for j in range(na)] for i in range(na)]
 c=nonnegative_matrix_product(ai,e);assert max(map(sum,c))<1
 rhs=nonnegative_matrix_product(ai,residual);nn=matrix(r['canonical_N']);cent=point_matrix(w0)
 rad=[[min(nn[i][j][1]-cent[i][j],cent[i][j]-nn[i][j][0]) for j in range(dim)] for i in range(na)]
 cr=nonnegative_matrix_product(c,rad)
 for i in range(na):
  for j in range(dim):assert rad[i][j]-cr[i][j]>=rhs[i][j],('canonical radius',key,i,j)
 for i in range(na,nb):
  for j in range(dim):assert nn[i][j]==pt(int(i-na==j))
 return dim

def audit_case(r,source,key):
 dim=annihilator(r,source,key)
 n=matrix(r['canonical_N']);g=matrix(r['canonical_basis_L2_Gram']);positive(g);gi=inverse_small(g)
 lm=matrix(r['energy_Loewner_lower_in_raw_basis']);lp=matrix(r['energy_Loewner_upper_in_raw_basis']);positive(lm);positive(lp)
 flo=matrix(r['trial_resolvent_lower_factor']);fhi=matrix(r['trial_resolvent_upper_factor'])
 cl=matrix(r['energy_lower_factor']);ch=matrix(r['energy_upper_factor'])
 en=matrix(r['trial_energy_on_N']);newpar=key.split('->')[1]
 gap=F(source['trials'][newpar]['physical_complement_gap_lower_exact'])
 theta=F(source['trials'][newpar]['physical_trial_max_Rayleigh_upper_exact'])
 # This theta from primary is itself a directed valid bound (the old rational
 # verifier's hull theta differs only in the last saved digits).
 lo=frob(mm(mm(mm(flo,n),gi),cl))[0]-trace(mm(mm(mm(gi,lm),gi),en))[1]/gap**2
 hi=frob(mm(mm(mm(fhi,n),gi),ch))[1]
 assert 0<lo<=hi
 beta_lo=289*(lo/dim)/(17+theta)**2
 beta_hi=hi+(theta+34)*theta/289
 assert 1<beta_lo<=beta_hi
 low,high=1/beta_hi,1/beta_lo
 # Refine diagonal entries of the true inverse moment in the same physical
 # Cholesky-orthonormal basis; positive norm bounds avoid dependency losses.
 if dim==1:
  o=[[div(pt(1),sqrtiv(g[0][0]))]]
 else:
  a=sqrtiv(g[0][0]);b=div(g[1][0],a);c=sqrtiv(sub(g[1][1],mul(b,b)))
  o=[[div(pt(1),a),neg(div(b,mul(a,c)))],[pt(0),div(pt(1),c)]]
 fl=mm(mm(flo,n),o);fh=mm(mm(fhi,n),o);eh=mm(mm(tr(o),en),o)
 zdiag=[]
 for j in range(dim):
  zlow=max(F(1)/theta,total(sq(row[j]) for row in fl)[0]-eh[j][j][1]/gap**2)
  zhigh=total(sq(row[j]) for row in fh)[1]
  assert 0<zlow<=zhigh
  zdiag.append([str(zlow),str(zhigh)])
 return {'dimension':dim,'one_minus_kappa_lower_exact':str(low),'one_minus_kappa_upper_exact':str(high),
         'trace_lower_exact':str(lo),'trace_upper_exact':str(hi),
         'physical_inverse_energy_diagonal_intervals':zdiag}

def main():
 p=argparse.ArgumentParser()
 for name in ('repo','primary','crosscheck','out'):p.add_argument('--'+name,type=Path,required=True)
 a=p.parse_args();primary=json.loads(a.primary.read_bytes());cross=json.loads(a.crosscheck.read_bytes())
 assert primary['source_commit']==cross['source_commit']==PIN
 assert primary['source_sha256']==cross['source_sha256']
 assert primary['precision_bits']==1024 and cross['precision_bits']==1280
 assert len(primary['results'])==len(cross['results'])==4
 git=shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe'
 assert subprocess.check_output([git,'rev-parse','HEAD'],cwd=a.repo).decode().strip()==PIN
 for rel,h in primary['source_sha256'].items():
  raw=(a.repo/rel).read_bytes();assert hashlib.sha256(raw).hexdigest()==h
  assert raw==subprocess.check_output([git,'show',PIN+':'+rel],cwd=a.repo)
 rel='research/x-c1/renewable-low-schur-spectral-2026-09-29/07-canonical-extension-outer-mass/primary.json'
 source=json.loads((a.repo/rel).read_bytes());results={}
 for key,r in primary['results'].items():
  cr=cross['results'][key]
  for field in ('canonical_N','canonical_basis_L2_Gram','physical_energy_entries',
                'physical_inverse_energy_entries','trial_resolvent_lower','trial_resolvent_upper'):
   overlaps(r[field],cr[field])
  x,y=audit_case(r,source,key),audit_case(cr,source,key)
  # Keep the outward union; do not select whichever run looks better.
  lower=min(F(x['one_minus_kappa_lower_exact']),F(y['one_minus_kappa_lower_exact']))
  upper=max(F(x['one_minus_kappa_upper_exact']),F(y['one_minus_kappa_upper_exact']))
  dl,rl=rounded(lower);du,ru=rounded(upper,True)
  assert lower<=upper<1
  results[key]={'dimension':x['dimension'],'one_minus_kappa_lower_exact':str(lower),
     'one_minus_kappa_upper_exact':str(upper),'display_outward':[dl,du],
     'display_exact':[rl,ru],'primary_rational_recheck':x,'cross_rational_recheck':y,
     'annihilator_and_neumann_radius_verified':True,'global_inverse_floor_used':False,
     'physical_inverse_energy_diagonal_intervals':[[str(min(F(u[0]),F(v[0]))),str(max(F(u[1]),F(v[1])))]
         for u,v in zip(x['physical_inverse_energy_diagonal_intervals'],y['physical_inverse_energy_diagonal_intervals'])]}
  print(key,'CERTIFIED 1-kappa in',dl,du,flush=True)
 out={'status':'RATIONAL_CANONICAL_RESOLVENT_AUDIT_PASS','source_commit':PIN,
      'bound_file_count':len(primary['source_sha256']), 'source_sha256':primary['source_sha256'],
      'primary_sha256':hashlib.sha256(a.primary.read_bytes()).hexdigest(),
      'crosscheck_sha256':hashlib.sha256(a.crosscheck.read_bytes()).hexdigest(),
      'results':results,'large_Arb_solves_independently_recomputed':False,
      'scope':'Exact rational canonical-annihilator certificate and small weighted-trace conclusions; '
              'large directed resolvent solves/factors and analytic proof remain inputs.'}
 a.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print('ALL FOUR TRUE CANONICAL EXTENSIONS PASS',flush=True)

if __name__=='__main__':main()
