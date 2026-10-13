"""Package root entry point. Standard-library bounded independent replay."""
from pathlib import Path
import json,sys,hashlib,argparse,importlib.util
ROOT=Path(__file__).resolve().parent;WORK=ROOT/'work/gamma-low-2026-10-09'
def module(name,file):
 spec=importlib.util.spec_from_file_location(name,WORK/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
inputs=module('gamma_input_audit','audit_inputs.py')
upper=module('gamma_upper_audit','check_upper.py')
schur=module('gamma_schur_audit','audit_schur.py')

def replay():
 read=lambda p:json.loads(p.read_bytes())
 files=read(ROOT/'MANIFEST.json')['files']
 for n,h in files.items():assert hashlib.sha256((ROOT/n.replace('\\','/')).read_bytes()).hexdigest()==h,n
 print(len(files),'manifest hashes passed',flush=True)
 assert upper.prove()==read(ROOT/'work/high-floor-2026-10-08/FLOOR_CHECK.json')
 for bits in [3072,4096]:
  for prefix in ['', 'TIGHT_']:
   for s in read(WORK/f'RESPONSE_{prefix}{bits}.json')['sources'].values():
    assert hashlib.sha256((ROOT/s['path'].replace('\\','/')).read_bytes()).hexdigest()==s['sha256']
 inp=inputs.replay();assert inp==read(WORK/'INPUT_EXACT.json')
 uc=[]
 for bits in [3072,4096]:
  for tight in [False,True]:
   result=upper.replay(bits,tight);prefix='TIGHT_' if tight else ''
   assert result==read(WORK/f'EXACT_{prefix}{bits}.json')
   uc.append({'tight_coupling':tight,'result':result})
 sc=[schur.replay(bits,stage) for bits in [3072,4096] for stage in ['gamma','shell','tight']]
 assert sc==read(WORK/'SCHUR_EXACT.json')['cases']
 actual={'input_audit':inp,'upper_audits':uc,'schur_audits':sc}
 assert actual==read(ROOT/'EXACT_CHECK.json')
 return {'status':'PASS_CONDITIONAL_FINITE_4_PLUS_8_SCHUR_CERTIFICATE',
  'manifest_files_verified':len(files),'old_high_floor':'91/50',
  'exact_191D_inverse_cases':8,'exact_schur_reconstructions':12,
  'positive_final_schur_cases':4,'schur_reserve_relative_WY':'1/25000',
  'reserve_scope':'Eight-source Schur block after eliminating the full old space and the four-source block, both parities.',
  'low_Gamma_precision_comparisons':72962,'shell_Gamma_precision_comparisons':384,
  'derived_upper_entries_compared':576,'independent_Fraction_Gamma_samples':10,
  'semantic_receipt_equal':True,'new_Gamma_matrix_integrations_rerun_by_quick_replay':False,
  'full_remainder_certified':False,'object_X_constructed':False,
  'conservative_fixed_M_minus_gate':'PREVIOUSLY_CERTIFIED_FALSE_CONDITIONAL_ON_BOUND_INPUTS',
  'external_mathematical_review':False,'github_changed':False}

if __name__=='__main__':
 assert __debug__
 ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path);args=ap.parse_args();receipt=replay()
 if args.out:args.out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(receipt,indent=2))
