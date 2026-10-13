"""Portable audit of the model-error replay and rational scalar Gram gate."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def extract(zpath,dest):
 with zipfile.ZipFile(zpath) as z:
  for n in z.namelist():assert (dest/n).resolve().is_relative_to(dest.resolve()),n
  z.extractall(dest)
 return next(p for p in dest.iterdir() if p.is_dir())
def main():
 assert __debug__
 ap=argparse.ArgumentParser();ap.add_argument('--receipt',type=Path);a=ap.parse_args()
 for n,digest in read(HERE/'MANIFEST.json')['files'].items():assert sha(HERE/n)==digest,n
 z=HERE/'inputs/Objekt-X-Vollstaendiger-Globaler-Modellfehler-2026-10-12-v2.zip'
 assert sha(z)=='c323db96ea92b01ec887e83f4171b124150e3d81fa6bb61450bf66cccaf5cd8b'
 with tempfile.TemporaryDirectory(prefix='objekt-x-scalar-gate-') as tmp:
  tmp=Path(tmp);incoming=extract(z,tmp/'incoming')
  source_origins=read(incoming/'SNAPSHOT_ORIGINS.json');finite=read(HERE/'data/FINITE_TARGET_INPUT.json')
  for idx,P in enumerate(['EVEN','ODD']):
   path=HERE/f'inputs/RESPONSES_{P}.json';response=read(path)
   wanted=source_origins[f'work/new-responses84-2026-10-11/RESPONSES_{P}.json']['original_sha256']
   assert sha(path)==wanted==finite['cases'][idx]['source_response_sha256']
   for key in ['rho','beta','K12_new_rational','M_upper_rational']:assert response[key]==finite['cases'][idx][key]
  prior=extract(next((incoming/'inputs').glob('*.zip')),tmp/'prior')
  assert read(prior/'data/DIRECTIONAL_DERIVATIVE_TARGET.json')==read(HERE/'data/DIRECTIONAL_DERIVATIVE_TARGET.json')
  subprocess.run([sys.executable,'-B',str(incoming/'reproduce.py'),'--receipt',str(tmp/'INPUT.json')],check=True)
  subprocess.run([sys.executable,'-B',str(HERE/'audit_scalar_gate.py'),
   '--helpers',str(HERE/'helpers'), '--inputs',str(HERE/'data/FINITE_TARGET_INPUT.json'),
   '--direction',str(HERE/'data/DIRECTIONAL_DERIVATIVE_TARGET.json'),
   '--weights',str(HERE/'data/SCALAR_GATE.json'),'--error',str(incoming/'data/MODEL_ERROR.json'),
   '--out',str(tmp/'SCALAR.json')],check=True)
  scalar=read(tmp/'SCALAR.json');assert scalar==read(HERE/'data/SCALAR_GATE_AUDIT.json')
  receipt={'status':'PASS_MODEL_ERROR_REPLAY_AND_RATIONAL_SCALAR_METRIC',
   'input_replay':read(tmp/'INPUT.json'),'scalar_gate':scalar,
   'full_original_response_bindings_checked':True,'unchanged_directional_target_checked':True,
   'new_full_exterior_integrations_executed':False,'full_scalar_integral_upper_computed':False,
   'full_global_residual_Gram_certified':False,'tail_floor_1_over_20_certified':False,'full_remainder_certified':False}
 if a.receipt:a.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
 print(receipt['status'],flush=True)
if __name__=='__main__':main()
