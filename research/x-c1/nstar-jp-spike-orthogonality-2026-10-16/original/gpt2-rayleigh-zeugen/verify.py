"""Two fixed rational Rayleigh witnesses; directed stdlib verification.

The PR quadratures are not replayed and are not used as error bounds.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,io,json,sys,zipfile
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'vendor'))
import source_core as sc
import rational_bounds as rb
sc.DIGITS=180;sc.S=10**180
I=sc.I
HIGH='1ccb6be11c6a8b4e325338b80f2136990b464b4a70e724a02ca7addbe7ba99b0'
RESPONSE='b8677c0bb085f40052e52953ec39112894fbaa0f9f5d9997df8ae546238f41ee'
def need(ok,msg):
 if not ok:raise AssertionError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def member(z,suffix):
 names=[n for n in z.namelist() if n==suffix or n.endswith('/'+suffix)]
 need(len(names)==1,('unique member',suffix,names));return z.read(names[0])
def box(v,scale=1):
 a,b=map(F,v);need(a<=b,'ordered interval')
 return I.raw(I(a/scale).lo,I(b/scale).hi)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),I(0))
def encode(x):
 if isinstance(x,I):return x.frac()
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 if isinstance(x,list):return [encode(v) for v in x]
 return x
def dump(p,x):p.write_bytes((json.dumps(encode(x),indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--high-archive',type=Path,required=True)
 ap.add_argument('--response-archive',type=Path,required=True)
 ap.add_argument('--output',type=Path,required=True)
 args=ap.parse_args();out=args.output.resolve()
 need(not out.exists() and not out.is_relative_to(HERE),'new output outside package')
 if (HERE/'MANIFEST.json').exists():
  for p,h in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
   path=(HERE/p).resolve();need(path.is_relative_to(HERE) and sha(path.read_bytes())==h,('manifest',p))
 hb=args.high_archive.read_bytes();need(sha(hb)==HIGH,'high archive hash')
 rr=args.response_archive.read_bytes();need(sha(rr)==RESPONSE,'response archive hash')
 with zipfile.ZipFile(io.BytesIO(hb)) as z:
  modelraw=member(z,'inputs/a8_model.json.gz')
  need(sha(member(z,'vendor/source_core.py'))==sha((HERE/'vendor/source_core.py').read_bytes()),'bound interval arithmetic')
  gen=member(z,'sources/generate_a8.py')
  highreceipt=json.loads(member(z,'expected/RECEIPT.json'))
 model=json.loads(gzip.decompress(modelraw))
 need(sha(modelraw)==highreceipt['source_hashes']['a8_model.json.gz'],'original Gram binding')
 need(sha(gen)==model['generator_sha256'],'source model generator')
 need(sha((HERE/'vendor/rational_bounds.py').read_bytes())==model['bounds_source_sha256'],'original rational Gamma proof code')
 with zipfile.ZipFile(io.BytesIO(rr)) as z:
  a12raw=member(z,'inputs/FRESH_A12.json');a12=json.loads(a12raw)
  er=json.loads(member(z,'RESPONSE_ENERGY.json'))
  need(sha(a12raw)==er['source_bindings']['inputs/FRESH_A12.json'],'A12 source binding')
 need(model['endpoint']=='3*log(2)/2' and model['scale_digits']==100,'source geometry')
 need(model['cutoff']==383 and model['Gamma_degree']==160,'source degrees')
 a=3*sc.log_point(2)/2
 need(a.hi<I(F(21,20)).lo,'full kernel radius')
 eps=rb.gamma_bound(160,F(21,20))
 need(eps==F(model['Gamma_kernel_error_exact']),'full exact rational Gamma error recomputed')
 scale=10**model['scale_digits']
 epsbox=box(model['Gamma_kernel_error'],scale)
 need(F(epsbox.lo,sc.S)<=eps<=F(epsbox.hi,sc.S),'stored error encloses exact bound')
 z0=F(21,40)
 need(1+(rb.cosh_upper(z0)-1)**2<4,'full even M norm below 2')
 need(1+(z0*z0/(3*(1-z0*z0/20)))**2<4,'full odd M norm below 2')
 lowerr=F(42,5)*eps
 vectors=json.loads((HERE/'inputs/SOFT_WITNESSES.json').read_bytes())
 moms=[box(v,scale) for v in model['raw_low_moments']]
 result={'status':'AUTHOR_DERIVED_CONDITIONAL_RAYLEIGH_CERTIFICATE_EXTERNAL_REVIEW_OPEN',
  'high_archive_sha256':HIGH,'response_archive_sha256':RESPONSE,
  'source_model_sha256':sha(modelraw),'Gamma_kernel_error_exact':eps,
  'whole_coordinate_form_model_error_upper':lowerr,'parities':{}}
 for sigma,p in enumerate(['even','odd']):
  uq=list(map(F,vectors[p]['exact_rational_coordinates']));u=list(map(I,uq));n2=sum((x*x for x in uq),F(0))
  need(len(u)==191 and n2>0,'nonzero fixed rational witness')
  degrees=list(range(sigma+2,sigma+383,2))
  need(degrees==vectors[p]['degrees'],'physical low basis')
  A=[[box(v,scale) for v in row] for row in model['parities'][p]['A']]
  qmodel=dot(u,[dot(row,u) for row in A])
  beta=[I(F(2*k+1,2*sigma+1)).sqrt()*moms[k]/moms[sigma] for k in degrees]
  normphi=I(n2)+dot(beta,u)**2
  error=I(lowerr*n2)
  qactual=qmodel.inflate(F(error.hi,sc.S));normalized=qactual/normphi
  need(qactual.lo>0 and normalized.lo>0,'positive entire witness energy interval')
  inverse=1/normalized;claimed=F('7.4e25' if sigma==0 else '1.17e23')
  need(inverse.lo>I(claimed).hi,'stated strict inverse norm lower bound')
  dA12=F(a12['parities'][p]['whole_Loewner_radius'])
  cs=[(I(F(normalized.hi,sc.S))*(I(F(row[j]))+dA12)).sqrt() for j,row in enumerate(a12['parities'][p]['midpoint'])]
  result['parities'][p]={'coordinate_norm_squared':n2,'physical_norm_squared':normphi,
    'model_form_interval':qmodel,'complete_Gamma_form_error_upper':error,
    'true_form_interval':qactual,'true_Rayleigh_interval':normalized,
    'A9_inverse_norm_lower_bound':F(inverse.lo,sc.S),'safe_strict_A9_inverse_norm_lower':claimed,
    'CS_upper_bounds_for_new_physical_unit_witness':cs,
    'old_PR_softmode_pairing_ratios_certified':False}
  print(p,'actual Rayleigh interval',normalized.display(),'inverse norm >',claimed,flush=True)
 out.mkdir(parents=True)
 dump(out/'RAYLEIGH_CERTIFICATE.json',result)
 receipt={'status':'PASS_UNDER_BOUND_OPERATOR_DOMAIN_AND_FULL_MODEL_INTEGRATION_HYPOTHESES',
  'high_archive_sha256':HIGH,'response_archive_sha256':RESPONSE,
  'exact_Gamma_error_recomputed':True,'fixed_rational_witnesses_checked':2,
  'whole_physical_moment_norm_paid':True,'CS_bounds_for_new_witnesses':24,
  'actual_A9_inverse_norm_lower_certified_conditionally':True,
  'old_PR_pairing_ratios_certified':False,'D12_error_budget_certified':False,
  'high_pairing_quadratures_replayed':False,'new_large_integrations':False,
  'new_historical_pivot_replay':False,'N12_excluded':False,'A9_A11_closed':False,
  'Objekt_X_constructed':False,'RH_proved':False,'external_review_open':True,'github_changed':False}
 dump(out/'RECEIPT.json',receipt)
 if (HERE/'expected').exists():
  for name in ['RAYLEIGH_CERTIFICATE.json','RECEIPT.json']:
   need((out/name).read_bytes()==(HERE/'expected'/name).read_bytes(),('byte-identical replay',name))
 print('PASS: two fixed rational physical witnesses, complete Gamma errors, 24 conditional CS bounds',flush=True)
if __name__=='__main__':main()
