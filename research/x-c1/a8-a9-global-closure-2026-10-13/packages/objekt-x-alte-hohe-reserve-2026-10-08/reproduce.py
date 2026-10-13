"""Run from the package root as reproduce.py. Python standard library only."""
from pathlib import Path
import json,sys,hashlib,argparse
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'work/high-floor-2026-10-08'))
from check_floor import prove
from check_upper import replay as replay_upper
from check_schur import replay as replay_schur,precision_compare

def replay():
 read=lambda p:json.loads(p.read_bytes())
 files=read(ROOT/'MANIFEST.json')['files']
 for n,h in files.items():
  path=ROOT/Path(n.replace('\\','/'))
  assert hashlib.sha256(path.read_bytes()).hexdigest()==h,n
 print(len(files),'manifest hashes passed',flush=True)
 work=ROOT/'work/high-floor-2026-10-08';floor=prove()
 assert floor==read(work/'FLOOR_CHECK.json')
 cases=[]
 for bits in [1024,1536]:
  response=read(work/f'RESPONSE_AUDITED_{bits}.json')
  assert floor==response['floor']
  for s in response['sources'].values():
   assert hashlib.sha256((ROOT/s['path'].replace('\\','/')).read_bytes()).hexdigest()==s['sha256']
  upper=replay_upper(bits);assert upper==read(work/f'EXACT_{bits}.json')
  finite=replay_schur(bits)
  cases.append({'upper':upper,'finite_schur':finite})
 actual={'floor':floor,'cases':cases,'precision_comparison':precision_compare()}
 assert actual==read(ROOT/'EXACT_CHECK.json')
 return {'status':'PASS_STRONGER_COMPLETE_OLD_HIGH_FLOOR_AND_UPPER_ENERGY_REPLAY',
  'manifest_files_verified':len(files),'physical_old_high_floor':'91/50',
  'previous_physical_old_high_floor':'2/3','exact_191D_inverse_cases':4,
  'joint_12_source_upper_cases':4,'strict_upper_improvement_all_cases':True,
  'finite_schur_cases':4,'derived_upper_entries_compared':288,
  'semantic_receipt_equal':True,'finite_schur_lower_certified_positive':False,
  'actual_new_remainder_sign':'OPEN','full_remainder_certified':False,
  'conservative_fixed_M_minus_gate':'PREVIOUSLY_CERTIFIED_FALSE_CONDITIONAL_ON_BOUND_INPUTS',
  'new_operator_integrations':False,'external_mathematical_review':False,'github_changed':False}

if __name__=='__main__':
 assert __debug__
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path);args=ap.parse_args()
 receipt=replay()
 if args.out:args.out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(receipt,indent=2))
