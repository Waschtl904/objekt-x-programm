"""Portable replay of the complete global function-error certificate."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from concurrent.futures import ThreadPoolExecutor
import json,hashlib,os,subprocess,sys,tempfile,zipfile,argparse
HERE=Path(__file__).resolve().parent
from audit_exterior import audit,up
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def normalize(d):
 d=json.loads(json.dumps(d))
 for row in d['cases']:
  for key in list(row):
   if key.endswith('_sha256'):row.pop(key)
 return d
def parameters():
 d=read(HERE/'data/PARAMETERS.json');assert d['status']=='PASS_FULL_FUNCTION_ERROR_PARAMETERS'
 eg=up(d['Gamma224_error']);es=up(d['shell_self_error']);assert eg<F(1,10**34) and es<F(1,10**50)
 # e>8/3 by its first five nonnegative Taylor terms; a>1.
 mirror=F(16,15)*F(3,8)**129;assert mirror<F(1,10**50)
 a2=F(21,40);h4=F(3,200)
 rem=[2*a2**161/factorial(161)/(1-a2/162),a2**160/factorial(160)/(1-a2/161),2*h4**161/factorial(161)/(1-h4/162)]
 assert all(v<F(1,10**300) for v in rem)
 assert 1000*eg+F(1,10**40)+100*es+100*mirror<F(1,10**28)
 for row in d['cases']:
  assert F(row['local_J_rounding_upper'])<F(1,10**60) and F(row['local_Y_rounding_upper'])<F(1,10**60)
  assert F(row['old_A_interval_width'])<F(1,10**69)
 return True
def compare_shared(a,b):
 aa={(v['kind'],v['u_lo'],v['u_hi']):v for v in a['panels']};bb={(v['kind'],v['u_lo'],v['u_hi']):v for v in b['panels']};checks=0
 for key in aa.keys()&bb.keys():
  for field in aa[key].keys()&bb[key].keys():
   va,vb=aa[key][field],bb[key][field]
   if isinstance(va,list):
    assert max(F(va[0]),F(vb[0]))<=min(F(va[1]),F(vb[1])),(key,field)
    checks+=1
 assert checks>20
 return checks
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--rebuild',action='store_true');ap.add_argument('--python',default=sys.executable);ap.add_argument('--deps',type=Path);ap.add_argument('--receipt',type=Path);x=ap.parse_args();assert __debug__
 for fn,want in read(HERE/'MANIFEST.json')['files'].items():
  p=(HERE/fn).resolve();assert p.is_relative_to(HERE.resolve()) and sha(p)==want,fn
 for fn,item in read(HERE/'SNAPSHOT_ORIGINS.json').items():assert sha(HERE/'snapshot'/fn)==item['snapshot_sha256']
 fresh_binding=HERE/'data/FRESH_KERNEL_REBUILD.json'
 inherited_fresh=False
 if fresh_binding.exists():
  binding=read(fresh_binding)
  assert binding['status']=='PASS_UNCHANGED_COMPLETE_KERNEL_REBUILD_BOUND_TO_V2'
  assert binding['freshly_rebuilt_interval_checks']>200
  for fn,want in binding['identical_builder_input_and_output_bindings'].items():assert sha(HERE/fn)==want
  inherited_fresh=True
 prior=next((HERE/'inputs').glob('*.zip'));assert sha(prior)=='86e510b6d68f5b70345f7ce710491fd09e7d8818cff3be6565fd8254d16581e3'
 with zipfile.ZipFile(prior) as z:
  manifest=next(n for n in z.namelist() if n.endswith('/MANIFEST.json'));base=manifest.rsplit('/',1)[0]+'/'
  for fn,want in json.loads(z.read(manifest))['files'].items():assert hashlib.sha256(z.read(base+fn)).hexdigest()==want
 assert parameters();print('PASS manifests and complete analytic error parameters',flush=True)
 results=[];overlaps=0
 for P in ['EVEN','ODD']:
  d=read(HERE/f'data/EXTERIOR_{P}_3072.json');d2=read(HERE/f'data/EXTERIOR_{P}_4096.json')
  results.append({'parity':P.lower(),'first':audit(d),'second_partition':audit(d2)})
  overlaps+=compare_shared(d,d2)
  assert len(d2['independent_Legendre_Q_controls'])==3
  assert all(up(c['complete_singular_row_difference'])<F(1,10**70) for c in d2['independent_Legendre_Q_controls'])
 with tempfile.TemporaryDirectory(prefix='objekt-x-full-model-error-') as tmp:
  tmp=Path(tmp)
  for P in ['EVEN','ODD']:
   subprocess.run([sys.executable,'-B',str(HERE/'audit_exterior.py'),'--input',str(HERE/f'data/EXTERIOR_{P}_3072.json'),'--out',str(tmp/f'EXT_{P}.json')],check=True)
  output=tmp/'ERROR.json'
  subprocess.run([sys.executable,'-B',str(HERE/'audit_model_error.py'),'--root',str(HERE/'snapshot'),'--exterior',str(HERE/'data'),'--out',str(output)],check=True)
  assert normalize(read(output))==normalize(read(HERE/'data/MODEL_ERROR.json'))
  subprocess.run([sys.executable,'-B',str(HERE/'audit_model_error.py'),'--root',str(HERE/'snapshot'),'--exterior',str(HERE/'data'),'--exterior-bits','4096','--out',str(tmp/'SECOND_ERROR.json')],check=True)
  if x.rebuild:
   env=os.environ.copy()
   if x.deps:env['PYTHONPATH']=str(x.deps.resolve())+os.pathsep+env.get('PYTHONPATH','')
   par=tmp/'PARAM.json'
   subprocess.run([x.python,'-B',str(HERE/'check_parameters.py'),'--root',str(HERE/'snapshot'),'--out',str(par)],env=env,check=True)
   assert read(par)==read(HERE/'data/PARAMETERS.json')
   def run(P):
    output=tmp/f'EXTERIOR_{P}_4096.json'
    subprocess.run([x.python,'-B',str(HERE/'bound_exterior_phi.py'),'--root',str(HERE/'snapshot'),'--parity',P.lower(),'--bits','4096','--panels','32','--out',str(output)],env=env,check=True)
    fresh=read(output);audit(fresh);return compare_shared(fresh,read(HERE/f'data/EXTERIOR_{P}_4096.json'))
   with ThreadPoolExecutor(max_workers=2) as pool:freshchecks=sum(pool.map(run,['EVEN','ODD']))
   subprocess.run([sys.executable,'-B',str(HERE/'audit_model_error.py'),'--root',str(HERE/'snapshot'),'--exterior',str(tmp),'--exterior-bits','4096','--out',str(tmp/'FRESH_ERROR.json')],check=True)
  else:freshchecks=0
 receipt={'status':'PASS_COMPLETE_GLOBAL_MODEL_ERROR','complete_global_model_error_certified':True,
  'rational_complete_exterior_checks':results,'cross_precision_shared_interval_checks':overlaps,
  'independent_Legendre_Q_row_checks':6,'missing_interval_counterchecks':4,
  'fresh_full_function_bound_rebuilt':x.rebuild,'fresh_interval_checks':freshchecks,
  'verified_fresh_kernel_rebuild_matches_current_builder_and_inputs':inherited_fresh,
  'rounded_log_error_in_joint_budget':True,'global_model_Gram_computed':False,
  'tail_floor_1_over_20_certified':False,'full_remainder_certified':False}
 if x.receipt:x.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps({k:v for k,v in receipt.items() if k!='rational_complete_exterior_checks'}),flush=True)
if __name__=='__main__':main()
