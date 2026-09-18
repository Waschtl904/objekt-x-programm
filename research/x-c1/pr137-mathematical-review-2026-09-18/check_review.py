from pathlib import Path
import importlib.util,json,time,argparse,hashlib
from functools import lru_cache
from fractions import Fraction as F
from math import factorial,comb
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description='Separate exact identity checks supporting the critical author review')
parser.add_argument('--root',type=Path,default=HERE.parents[2])
mode=parser.add_mutually_exclusive_group();mode.add_argument('--write',action='store_true');mode.add_argument('--verify',action='store_true')
args=parser.parse_args();ROOT=args.root.resolve()
SOURCE=ROOT/'research/x-c1/prime-power-segment-4-2026-09-18/check_segment.py'
for item in json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))['files']:
 raw=(ROOT/item['path']).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']
LOG=[]
def note(s):LOG.append(s);print(s,flush=True)

spec=importlib.util.spec_from_file_location('endpoint',SOURCE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.progress=note
checks=[]
def ok(name,cond):
 if not cond:raise AssertionError(name)
 checks.append(name)
def trim(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def add(p,q):
 r=[F(0)]*max(len(p),len(q))
 for i,x in enumerate(p):r[i]+=x
 for i,x in enumerate(q):r[i]+=x
 return trim(r)
def mul(p,q):
 r=[F(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):r[i+j]+=x*y
 return trim(r)
def power_shift(p,c):
 r=[F(0)]*len(p)
 for n,v in enumerate(p):
  for k in range(n+1):r[k]+=v*comb(n,k)*c**(n-k)
 return trim(r)
def integ(p,l,h):return sum((v*(h**(n+1)-l**(n+1))/(n+1) for n,v in enumerate(p)),F(0))
@lru_cache(None)
def rod(n):
 p=[F(0)]*(n+1)
 for k in range(n//2+1):p[n-2*k]=F((-1)**k*factorial(2*n-2*k),2**n*factorial(k)*factorial(n-k)*factorial(n-2*k))
 return p
@lru_cache(None)
def unit(n):return [F((-1)**(n+r)*factorial(n+r),factorial(r)**2*factorial(n-r)) for r in range(n+1)]
def singular(p):
 out=[F(0)]*len(p)
 for n,v in enumerate(p):
  out[n]+=v*sum((F(1,k) for k in range(1,n+1)),F(0))
  for r in range(1,n,2):out[n-1-r]-=v/F(r+1)
 return out
note('Rodrigues and exact singular operator')
for n in range(129):
 p=rod(n);ok('Rodrigues Legendre '+str(n),p==m.leg(n))
 H=sum((F(1,k) for k in range(1,n+1)),F(0));ok('singular operator eigenpair '+str(n),singular(p)==[H*v for v in p])
note('Gamma image: separate two-triangle monomial integration')
def direct_image(j,k):
 out=[F(0)]*(j+k+2)
 for r,v in enumerate(unit(j)):
  out[r+k+1]+=2**k*v*F(factorial(r)*factorial(k),factorial(r+k+1))
  for h in range(r+1):
   c=2**k*v*F(comb(r,h),k+h+1)
   for e in range(k+h+2):out[r-h+e]+=c*comb(k+h+1,e)*(-1)**e
 return trim(out)
for j in [0,1,2,3,4,8,15,16,30,31,62,63]:
 cols=m.kernel_columns(j,64)
 for k in [0,1,2,3,16,32,64]:
  out=[F(0)]
  for n,v in enumerate(cols[k]):
   if v:out=add(out,[v*c for c in unit(n)])
  ok('Gamma full image j='+str(j)+' k='+str(k),trim(out)==direct_image(j,k))
note('Logarithmic off-diagonal identity')
for i,j in [(i,i+2) for i in range(0,64)]+[(i,128-i%2) for i in [0,1,2,3,16,17,30,31,62,63]]:
 p=mul(rod(i),rod(j));rational=sum((v*sum((F(1,2*r+1) for r in range(k//2+1)),F(0))/F(k+1) for k,v in enumerate(p) if k%2==0),F(0))
 logcoeff=-sum((v/F(k+1) for k,v in enumerate(p) if k%2==0),F(0))
 ok('V offdiag '+str(i)+','+str(j),logcoeff==0 and rational==F(1,(j-i)*(j+i+1)))
note('Rational signed-band integrals and independent logarithmic antiderivatives')
def band(s,d):return (F(-1),F(1)-d) if s==1 else (F(-1)+d,F(1))
def shift_entry(i,j,d):
 return sum((integ(mul(rod(i),power_shift(rod(j),s*d)),*band(s,d))/2 for s in [-1,1]),F(0))
def cross(i,j,d,e):
 total=F(0)
 for s in [-1,1]:
  for t in [-1,1]:
   aa,bb=band(s,d);cc,dd=band(t,e);l=max(aa,cc);h=min(bb,dd)
   if l<h:total+=integ(mul(power_shift(rod(i),s*d),power_shift(rod(j),t*e)),l,h)/2
 return total
@lru_cache(None)
def logpower(k,z):
 if z==0:return m.I(0)
 return m.I(z**(k+1)/F(k+1))*(m.log(m.I(z))-F(1,k+1))
@lru_cache(None)
def vmoment(n,l,h):
 minus=sum(((-1)**k*comb(n,k)*(logpower(k,1-l)-logpower(k,1-h)) for k in range(n+1)),m.I(0))
 plus=sum(((-1)**(n-k)*comb(n,k)*(logpower(k,1+h)-logpower(k,1+l)) for k in range(n+1)),m.I(0))
 return -(minus+plus)/2
def vs_entry(i,j,d):
 value=m.I(0)
 for s in [-1,1]:
  l,h=band(s,d);p=mul(rod(i),power_shift(rod(j),s*d))
  value+=sum((c*vmoment(n,l,h) for n,c in enumerate(p)),m.I(0))/2
 return value
DS=[F(4,5),F(13,10),F(8,5)];WS=[F(2,7),F(3,11),F(5,13)]
ch=[{'ell':m.I(d),'weight':m.I(w)} for d,w in zip(DS,WS)]
sq,vs,b=m.shift_grams(ch,m.I(1),8)
for i in range(9):
 for j in range(i%2,9,2):
  for d in DS:
   val=shift_entry(i,j,d);z=m.polyval(m.tpoly(i,j),m.I(2-d));ok('beta shift '+str((i,j,d)),z.lo<=val<=z.hi)
  val=sum((w*v*cross(i,j,d,e) for d,w in zip(DS,WS) for e,v in zip(DS,WS)),F(0));ok('all ordered mixed shifts '+str((i,j)),sq[i][j].lo<=val<=sq[i][j].hi)
  z=sum((w*vs_entry(i,j,d) for d,w in zip(DS,WS)),m.I(0));other=vs[i][j];ok('independent V-S primitive '+str((i,j)),max(z.lo,other.lo)<=min(z.hi,other.hi))
note('Coincident-breakpoint limitation of endpoint band engine')
try:
 m.shift_grams([{'ell':m.I(F(4,5)),'weight':m.I(1)},{'ell':m.I(F(6,5)),'weight':m.I(1)}],m.I(1),2)
except AssertionError:ok('engine explicitly rejects coincident breakpoints',True)
else:raise AssertionError('Expected frozen engine rejection not reproduced')
note('Directed interval sign and reciprocal edge cases')
intervals=[(F(-7,3),F(-1,7)),(F(-1,3),F(2,7)),(F(1,11),F(7,3)),(F(-1,10**220),F(1,10**220))]
for al,ah in intervals:
 for bl,bh in intervals:
  A=m.I(al,ah);B=m.I(bl,bh)
  for op,name in [(lambda x,y:x+y,'add'),(lambda x,y:x-y,'subtract'),(lambda x,y:x*y,'multiply')]+([(lambda x,y:x/y,'divide')] if bl>0 or bh<0 else []):
   enclosure=op(A,B);vals=[op(x,y) for x in [al,(al+ah)/2,ah] for y in [bl,(bl+bh)/2,bh]]
   ok('directed '+name+' '+str((al,ah,bl,bh)),enclosure.lo<=min(vals)<=max(vals)<=enclosure.hi)
report={'status':'AUTHOR-REVIEW / EXTERNAL-REVIEW-OPEN','target':'8074d14508873e09068222b9703b1f34e8607fc6','endpoint_source':'6a16d90b551588572c87e622c21c2df7f7b1adc2','counts':{'singular_eigenpairs':129,'Rodrigues_basis':129,'Gamma_images':84,'V_offdiagonal':74,'mixed_shift_pairs':41,'V_shift_pairs':41,'shift_beta_entries':123,'directed_sign_cases':56,'coincident_breakpoint_rejection':1},'check_count':len(checks),'checks':checks,'scope':'exact implementation regressions supplement analytic review, not a finite enumeration proof of infinite-dimensional theorems'}
assert report['check_count']==sum(report['counts'].values())
note('TOTAL '+str(len(checks))+' exact/rational-interval regressions PASS')
jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n';logtext='\n'.join(LOG)+'\n'
if args.write:
 (HERE/'review_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
 (HERE/'review_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
if args.verify:
 assert (HERE/'review_results.json').read_bytes()==jsontext.encode('utf-8')
 assert (HERE/'review_checks.log').read_bytes()==logtext.encode('utf-8')
 for line in (HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines():
  digest,name=line.split('  ',1)
  assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
 print('REPLAY and review package SHA256 hashes PASS')
