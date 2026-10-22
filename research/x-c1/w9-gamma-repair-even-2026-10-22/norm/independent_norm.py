"""Independent full norm: local polynomial coefficients and elementary log moments.
No imported log-product integrator and no residual quadrature.
"""
if not __debug__:
 raise SystemExit('Verification requires assertions enabled; Python -O/-OO is rejected.')
from pathlib import Path
import sys,json,gzip,hashlib,time,argparse
from fractions import Fraction
from decimal import Decimal,localcontext
HERE=Path(__file__).resolve().parent;WORK=HERE.parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--inputs',type=Path,default=HERE/'inputs')
parser.add_argument('--flint-path',type=Path,default=WORK/'pairing-check/deps')
args=parser.parse_args();DATA=args.inputs
sys.path.insert(0,str(args.flint_path))
from flint import arb,arb_poly,ctx,fmpq
ctx.prec=3072;tick=time.monotonic()
sys.path.insert(0,str(DATA));import model_cache
def q(s):
 value=Fraction(str(s))
 return arb(fmpq(value.numerator,value.denominator))
enc=lambda v:[str(v.lower().fmpq()),str(v.upper().fmpq())]
def load(path):
 raw=path.read_bytes();body=json.loads(gzip.decompress(raw))
 values,inputs=model_cache.load(path,body['source_sha256'])
 return values,hashlib.sha256(raw).hexdigest()
orig,cachehash=load(DATA/'original-model.json.gz')
assert cachehash=='040436a000b91c136d9b6977b859d739773a37fb228dfca076bb953dd80bcfcc'
own,ownhash=load(DATA/'own-correction.json.gz')
other,otherhash=load(DATA/'GPT1-correction.json.gz')
a,b,hs,mu=(orig[k]for k in ['a','b','hs','mu']);x=arb_poly([a,hs]);du=own['du']
assert (own['dR']/mu).overlaps(other['moment_coefficient'])
P=arb_poly(own['plain'])
for n,(sh,wt)in zip([2,3,4,5,7,8],orig['channels']):
 if n==2:
  assert a-sh>0 and b-sh<a;aff=(x-sh)*(1/a)
 else:
  assert sh-a<a or n==8
  assert b-sh<0 or n==3
  if n==8:assert (sh-2*a).contains(0)
  if n==3:assert (sh-b).contains(0)
  aff=(sh-x)*(1/a)
 P-=du(aff)*wt
logs=own['log_terms']
# Cross-check the entire coefficient representation with GPT 1 after the
# affine coordinate substitution x=a+hs*z, including constant log(hs) terms.
parts=other['outer_correction'];otherP=parts[None](x)
otherlogs=[(arb(0),parts['left'](x)),(-2*a/hs,parts['minus_left'](x)),(-a/hs,parts['zero'](x))]
otherP+=sum((p for r,p in otherlogs),arb_poly([]))*hs.log()
sup=lambda p:sum((abs(v).upper()for v in p),arb(0)).upper()
representation_error=sup(P-otherP)*(2*hs).sqrt()
for (root,pol),(root2,pol2)in zip(logs,otherlogs):
 assert root.overlaps(root2)
 if root==0:representation_error+=sup(pol-pol2)*(4*hs).sqrt()
 else:representation_error+=sup(pol-pol2)*(2*hs).sqrt()*max(abs((-root).log()).upper(),abs((1-root).log()).upper())
assert representation_error<q('1e-100')
# Smooth logs log(z+c) have a uniformly convergent Taylor series on [0,1].
# The only endpoint singularity, A(z) log(z), is integrated exactly below.
N=160;T=arb_poly(P);A=arb_poly([]);uniform=arb(0)
for root,pol in logs:
 if root==0:A+=pol;continue
 cc=-root;assert cc>1
 series=arb_poly([cc.log()]+[(-1)**(k+1)/(k*cc**k)for k in range(1,N+1)])
 T+=pol*series
 error=cc**(-N-1)/((N+1)*(1-1/cc));uniform+=sup(pol)*error
def integral_poly(pol):return sum((v/(k+1)for k,v in enumerate(pol)),arb(0))
def integral_log(pol):return -sum((v/(k+1)**2 for k,v in enumerate(pol)),arb(0))
def integral_log_squared(pol):return sum((2*v/(k+1)**3 for k,v in enumerate(pol)),arb(0))
norm2=2*hs*(integral_poly(T*T)+2*integral_log(T*A)+integral_log_squared(A*A))
assert norm2>0
logrest=(2*hs).sqrt()*uniform
mtail=(b/2).exp()*(b/2)**162/arb.fac_ui(162)
momentrest=(2*hs).sqrt()*mtail*abs(own['dR']/mu).upper()
norm_upper=(norm2.upper().sqrt()+logrest+momentrest).upper()
norm_lower=(norm2.lower().sqrt()-logrest-momentrest).lower()
assert norm_upper<q('3.653e-7')
their=json.loads((DATA/'GPT1-outer-check.json').read_bytes())['bounds']
assert norm_upper<q(their['correction_X_norm_upper'][1])+q('1e-70')
wr=json.loads((DATA/'WHOLE_RESULT.json').read_bytes())
newnorm=q('5/21').sqrt()*(q(wr['model_X_norm_squared_upper']).sqrt()+norm_upper+q(wr['core_quadrature_X_error_upper'])+q(wr['core_bridge_X_error_upper']))+q(wr['whole_operator_model_Ldual_error_upper'])
energy=(newnorm**2).upper();assert energy<q('4.632e-11')
out={'status':'INDEPENDENT_LOCAL_LOG_SERIES_NORM_CHECK_PASS_CONDITIONAL_ON_FROZEN_MODEL_IDENTIFICATION',
 'method':'Own correction coefficients; local z in [0,1]; smooth logs Taylor N=160 with geometric remainder; exact polynomial/log/log^2 moments; same Arb library, no external log-product library.',
 'norm_squared_intermediate':enc(norm2),'smooth_log_remainder_X':enc(logrest),'moment_Taylor_remainder_X':enc(momentrest),
 'correction_X_norm_interval':[str(norm_lower.fmpq()),str(norm_upper.fmpq())],
 'whole_representation_difference_X_upper':enc(representation_error),
 'conditional_repaired_Ldual_norm_upper':enc(newnorm.upper()),'conditional_repaired_Ldual_energy_upper':enc(energy),
 'inputs':{'original_model_cache':cachehash,'own_correction_cache':ownhash,'GPT1_correction_cache':otherhash},'seconds':time.monotonic()-tick}
(HERE/'independent-norm.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for k in ['norm_squared_intermediate','smooth_log_remainder_X','moment_Taylor_remainder_X','correction_X_norm_interval','whole_representation_difference_X_upper','conditional_repaired_Ldual_energy_upper']:
 with localcontext() as dc:
  dc.prec=20
  print(k,[format(Decimal(Fraction(v).numerator)/Decimal(Fraction(v).denominator),'.16E')for v in out[k]],flush=True)
print('SECONDS',out['seconds'],flush=True)
