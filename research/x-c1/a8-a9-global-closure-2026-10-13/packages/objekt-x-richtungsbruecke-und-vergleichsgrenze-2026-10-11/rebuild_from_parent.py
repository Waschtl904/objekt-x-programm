"""Optional fresh integration and matrix rebuild inside a bound extracted parent.

Run with the Python interpreter containing python-flint, numpy and scipy.
The parent reproduce.py must previously have unpacked its bound predecessors.
Only a new work/directional-bridge-2026-10-11 directory is written.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys
HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);args=ap.parse_args()
root=args.root.resolve();dest=root/'work/directional-bridge-2026-10-11'
assert dest.resolve().is_relative_to(root) and not dest.exists(),'Use a fresh extracted parent with no directional output.'
data=json.loads((HERE/'AUDIT_INPUT.json').read_bytes())
for key,item in data['sources'].items():
 if key=='review':continue
 p=(root/item['path']).resolve();assert p.is_relative_to(root)
 assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],key
dest.mkdir(parents=True);(dest/'review-rebuild').mkdir()
for name in ['compute_direct_y.py','directional_gate.py','optimistic_test.py','build_audit_input.py','audit_directional.py','rational_ldl.py']:
 shutil.copy2(HERE/name,dest/name)
shutil.copy2(HERE/'review-rebuild/BRIDGE_OBSTRUCTION_INPUT.json',dest/'review-rebuild/BRIDGE_OBSTRUCTION_INPUT.json')
for bits in [3072,4096]:
 for parity in ['even','odd']:
  subprocess.run([sys.executable,'-B',str(dest/'compute_direct_y.py'),'--bits',str(bits),'--parity',parity,'--out',str(dest/f'DIRECT_Y_{parity.upper()}_{bits}.json')],check=True)
for name in ['directional_gate.py','optimistic_test.py','build_audit_input.py','audit_directional.py']:
 subprocess.run([sys.executable,'-B',str(dest/name)],check=True)
assert json.loads((dest/'AUDIT.json').read_bytes())==json.loads((HERE/'AUDIT.json').read_bytes())
for label in ['EVEN','ODD']:
 for bits in [3072,4096]:
  a=json.loads((dest/f'DIRECT_Y_{label}_{bits}.json').read_bytes());b=json.loads((HERE/f'DIRECT_Y_{label}_{bits}.json').read_bytes())
  a.pop('seconds');b.pop('seconds');assert a==b
print('PASS fresh direct integrations, matrix rebuilds and exact rational audit')
