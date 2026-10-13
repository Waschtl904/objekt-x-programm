"""Verify hashes and the Fraction audit; optionally repeat algebra/integrals."""
from pathlib import Path
import argparse,json,hashlib,subprocess,sys,os,shutil
ap=argparse.ArgumentParser();ap.add_argument('--recompute-algebra',action='store_true');ap.add_argument('--recompute-integrals',action='store_true');ap.add_argument('--destination',type=Path)
args=ap.parse_args();ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'MANIFEST.json').read_bytes())
for name,digest in manifest['files'].items():
 p=(ROOT/name).resolve();assert ROOT in p.parents and hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
print('Manifest files verified:',len(manifest['files']),flush=True)
if args.recompute_algebra or args.recompute_integrals:
 assert args.destination is not None,'Provide a fresh --destination for recomputation'
 dest=args.destination.resolve();assert not dest.exists()
 shutil.copytree(ROOT,dest)
 stage=dest/'work/variational-high-2026-10-08'
 for bits in [3072,4096]:
  if args.recompute_integrals:
   for parity in ['even','odd']:
    target=stage/f'INTEGRALS_{parity.upper()}_{bits}.json';target.unlink()
    subprocess.run([sys.executable,str(stage/'compute_trial.py'),'--bits',str(bits),'--parity',parity,'--out',str(target)],cwd=dest,check=True)
  for name in [f'RESPONSE_NEW_{bits}.json',f'U00_NEW_{bits}.json']:(stage/name).unlink()
  subprocess.run([sys.executable,str(stage/'assemble_trial.py'),'--bits',str(bits),'--out',str(stage/f'RESPONSE_NEW_{bits}.json')],cwd=dest,check=True)
  subprocess.run([sys.executable,str(stage/'compute_u00.py'),'--response',str(stage/f'RESPONSE_NEW_{bits}.json'),'--arithmetic-bits',str(1024 if bits==3072 else 1536),'--out',str(stage/f'U00_NEW_{bits}.json')],cwd=dest,check=True)
else:dest=ROOT
stage=dest/'work/variational-high-2026-10-08';receipt=dest/'REPLAY_CHECK.json'
subprocess.run([sys.executable,str(stage/'check_variation.py'),'--out',str(receipt)],cwd=dest,check=True)
assert json.loads(receipt.read_bytes())==json.loads((ROOT/'EXACT_CHECK.json').read_bytes()),'Exact receipt changed'
print('PASS: exact audit semantically identical',flush=True)
