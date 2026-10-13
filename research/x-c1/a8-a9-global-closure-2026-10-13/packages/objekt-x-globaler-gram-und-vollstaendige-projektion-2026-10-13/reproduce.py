"""Portable rational replay; optional complete fresh Arb integration."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import sys,os,json,hashlib,tempfile,subprocess,argparse,zipfile
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def sqrtup(v):
 assert v>=0;scale=10**100
 return F(isqrt(v.numerator*scale*scale//v.denominator)+1,scale)
def compare_with_full_error(a,b,response):
 delta=F(a['complete_D_dual_L2_approximation_error'][1])+F(b['complete_D_dual_L2_approximation_error'][1])
 dd=[1-F(response['rho'])]*191+[F(response['K12_new_rational'][i][i]) for i in range(12)]
 sd=list(map(sqrtup,dd));count=0
 for key in ['model_Gram_203x203','low_projection_104x203','high_model_Gram_203x203']:
  if key!='low_projection_104x203':
   norms=[sqrtup(max(F(a[key][i][i][1]),F(b[key][i][i][1]),F(0))) for i in range(203)]
  for i,(r,s) in enumerate(zip(a[key],b[key])):
   for j,(x,y) in enumerate(zip(r,s)):
    price=delta*sd[j] if key=='low_projection_104x203' else delta*(sd[i]*norms[j]+sd[j]*norms[i])
    assert max(F(x[0])-F(y[1]),F(y[0])-F(x[1]))<=price+F(1,10**60),(key,i,j)
    count+=1
 return count
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--rebuild',action='store_true');ap.add_argument('--python',default=sys.executable);ap.add_argument('--deps',type=Path);ap.add_argument('--receipt',type=Path);args=ap.parse_args()
 assert __debug__
 for name,want in read(HERE/'MANIFEST.json')['files'].items():
  pp=(HERE/name).resolve();assert pp.is_relative_to(HERE.resolve()) and sha(pp)==want,name
 origins=read(HERE/'SNAPSHOT_ORIGINS.json')
 for name,item in origins.items():assert sha(HERE/'snapshot'/name)==item['snapshot_sha256']
 original_hashes={item['original_sha256'] for item in origins.values()}
 root=HERE/'snapshot';code=root/'work/global-gram-2026-10-13'
 inherited=next((HERE/'inputs').glob('*.zip'));assert sha(inherited)=='c323db96ea92b01ec887e83f4171b124150e3d81fa6bb61450bf66cccaf5cd8b'
 results=[];comparisons=0
 with tempfile.TemporaryDirectory(prefix='objekt-x-global-gram-') as tmp:
  tmp=Path(tmp)
  inherited_root=tmp/'physical-error';inherited_root.mkdir()
  with zipfile.ZipFile(inherited) as archive:
   for name in archive.namelist():assert (inherited_root/name).resolve().is_relative_to(inherited_root.resolve())
   archive.extractall(inherited_root)
  inherited_package=next(inherited_root.iterdir())
  inherited_receipt=tmp/'PHYSICAL_ERROR_REPLAY.json'
  subprocess.run([sys.executable,'-B',str(inherited_package/'reproduce.py'),'--receipt',str(inherited_receipt)],check=True)
  assert read(inherited_receipt)['status']=='PASS_COMPLETE_GLOBAL_MODEL_ERROR'
  physical_cases={item['parity']:item for item in read(inherited_package/'data/MODEL_ERROR.json')['cases']}
  for label in ['EVEN','ODD']:
   gram=read(HERE/f'data/GRAM_{label}_3072.json')
   assert gram['parity']==label.lower() and all(v in original_hashes for v in gram['bindings'].values())
   out=tmp/f'AUDIT_{label}.json'
   subprocess.run([sys.executable,'-B',str(code/'audit.py'),'--gram',str(HERE/f'data/GRAM_{label}_3072.json'),'--out',str(out)],check=True)
   fresh=read(out);expected=read(HERE/f'data/AUDIT_{label}_3072.json');assert fresh==expected
   assert F(fresh['model_Gram_relative_H_upper'])<F(3,10000)
   assert F(fresh['actual_regularized_Gram_relative_H_upper'])<F(3,10000)
   assert F(physical_cases[label.lower()]['simple_complete_model_error_cap'])<=F(fresh['physical_model_error_cap'])
   results.append(fresh)
  if args.rebuild:
   env=os.environ.copy()
   if args.deps:env['PYTHONPATH']=str(args.deps.resolve())+os.pathsep+env.get('PYTHONPATH','')
   subprocess.run([args.python,'-B',str(code/'test_primitives.py')],check=True,env=env)
   subprocess.run([args.python,'-B',str(code/'check_geometry.py')],check=True,env=env)
   subprocess.run([args.python,'-B',str(code/'check_log_groups.py')],check=True,env=env)
   subprocess.run([args.python,'-B',str(code/'test_radius_price.py')],check=True,env=env)
   for label in ['EVEN','ODD']:
    out=tmp/f'GRAM_{label}_4096.json'
    subprocess.run([args.python,'-u','-B',str(code/'background_run_grouped.py'),'--root',str(root),'--bits','4096','--parity',label.lower(),'--out',str(out)],text=True,env=env,check=True)
    subprocess.run([sys.executable,'-B',str(code/'audit.py'),'--gram',str(out),'--out',str(tmp/f'FRESH_AUDIT_{label}.json')],check=True)
    fresh=read(out);old=read(HERE/f'data/GRAM_{label}_3072.json')
    comparisons+=compare_with_full_error(fresh,old,read(root/f'work/new-responses84-2026-10-11/RESPONSES_{label}.json'))
 receipt={'status':'PASS_COMPLETE_GLOBAL_GRAM_RATIONAL_REPLAY','cases':results,'fresh_full_integration_rebuilt':args.rebuild,'fresh_matrix_entry_comparisons':comparisons,
          'complete_physical_error_v2_rationally_replayed':True,
          'A8_to_A9_final_assembly_performed':False,'tail_floor_1_over_20_final_assembly_performed':False}
 if args.receipt:args.receipt.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
 print(receipt['status'],flush=True)
if __name__=='__main__':main()
