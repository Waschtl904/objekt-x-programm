"""Optional complete numerical rebuild from the bound large original package."""
from pathlib import Path
import json,hashlib,shutil,tempfile,subprocess,sys,argparse
from reproduce import unpack_previous
HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);args=ap.parse_args()
root=args.root.resolve();dest=root/'work/direct-rest84-2026-10-11';prior=root/'work/directional-bridge-2026-10-11'
assert dest.resolve().is_relative_to(root) and prior.resolve().is_relative_to(root)
assert not dest.exists(),'Use a fresh extracted original without this output directory.'
data=json.loads((HERE/'REFINED_INPUT.json').read_bytes())
for item in data['sources'].values():
 p=(root/item['path']).resolve();assert p.is_relative_to(root)
 assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],item['path']
with tempfile.TemporaryDirectory(prefix='objekt-x-direct96-input-') as tmp:
 parent=unpack_previous(Path(tmp));dest.mkdir(parents=True);prior.mkdir(parents=True,exist_ok=True)
 for name in ['DIRECT_Y_EVEN_3072.json','DIRECT_Y_ODD_3072.json','review-rebuild/BRIDGE_OBSTRUCTION_INPUT.json']:
  target=prior/name;target.parent.mkdir(parents=True,exist_ok=True)
  if target.exists():assert target.read_bytes()==(parent/name).read_bytes()
  else:shutil.copy2(parent/name,target)
 for name in ['compute_direct_rest.py','test_full_direct.py','refine_old_majorant.py','build_audit_input.py','audit_full.py','rational_helpers.py','rational_ldl.py','inherited_floor.py']:
  shutil.copy2(HERE/name,dest/name)
 for bits in [3072,4096]:
  for parity in ['even','odd']:
   subprocess.run([sys.executable,'-B',str(dest/'compute_direct_rest.py'),'--bits',str(bits),'--parity',parity,'--out',str(dest/f'DIRECT_REST_{parity.upper()}_{bits}.json')],check=True)
 for name in ['test_full_direct.py','refine_old_majorant.py','build_audit_input.py']:
  subprocess.run([sys.executable,'-B',str(dest/name)],check=True)
 subprocess.run([sys.executable,'-B',str(dest/'audit_full.py'),'--parent',str(parent)],check=True)
 actual=json.loads((dest/'AUDIT.json').read_bytes());assert actual['status']=='PASS_FULL_DIRECT_REST_AND_REFINED_COMMON96'
 assert all(c['new_common96_positive'] for c in actual['cases'])
 print('PASS complete new integrations, response rebuild, integer inverse and rational common96 positivity')
