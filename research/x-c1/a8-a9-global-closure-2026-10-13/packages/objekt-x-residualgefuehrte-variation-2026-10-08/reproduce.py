"""Portable bounded replay; preserve frozen selection and all original inputs."""
from pathlib import Path
import argparse,json,hashlib,subprocess,sys,shutil
ap=argparse.ArgumentParser();ap.add_argument('--recompute-algebra',action='store_true');ap.add_argument('--recompute-integrals',action='store_true');ap.add_argument('--destination',type=Path)
args=ap.parse_args();ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'MANIFEST.json').read_bytes())
for name,digest in manifest['files'].items():
 p=(ROOT/name).resolve();assert ROOT in p.parents and hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
print('Manifest files verified:',len(manifest['files']),flush=True)
if args.recompute_algebra or args.recompute_integrals:
 assert args.destination is not None,'Provide a fresh --destination'
 dest=args.destination.resolve();assert not dest.exists();shutil.copytree(ROOT,dest)
else:dest=ROOT
stage=dest/'work/residual-guided-2026-10-08'
def run(script,*arguments):subprocess.run([sys.executable,str(stage/script),*map(str,arguments)],cwd=dest,check=True)
if args.recompute_integrals:
 for bits in [4096,6144]:
  for parity in ['even','odd']:
   for engine,kind in [('scan_residual.py','SCAN'),('compute_form.py','INTEGRALS')]:
    original=stage/f'{kind}_{parity.upper()}_{bits}.json';new=stage/f'REPLAY_{kind}_{parity.upper()}_{bits}.json'
    run(engine,'--bits',bits,'--parity',parity,'--out',new)
    a=json.loads(original.read_bytes());b=json.loads(new.read_bytes());a.pop('seconds');b.pop('seconds')
    assert a==b,(kind,parity,bits,'recomputed integral data differ')
if args.recompute_integrals or args.recompute_algebra:
 for bits in [4096,6144]:
  for name in [f'RESPONSE_NEW_{bits}.json',f'U00_NEW_{bits}.json']:(stage/name).unlink()
  run('assemble_trial.py','--bits',bits,'--out',stage/f'RESPONSE_NEW_{bits}.json')
  run('compute_u00.py','--response',stage/f'RESPONSE_NEW_{bits}.json','--arithmetic-bits',1536 if bits==4096 else 2048,'--out',stage/f'U00_NEW_{bits}.json')
receipt=dest/'REPLAY_CHECK.json';run('check_residual.py','--out',receipt)
assert json.loads(receipt.read_bytes())==json.loads((ROOT/'EXACT_CHECK.json').read_bytes()),'Exact receipt changed'
print('PASS: exact audit semantically identical',flush=True)
