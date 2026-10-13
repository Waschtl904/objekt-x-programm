"""Portable quick audit and optional replay of this NEW computational stage."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile,shutil
ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--recompute-new',action='store_true');ap.add_argument('--destination',type=Path)
args=ap.parse_args();files=[]
for line in (ROOT/'SHA256SUMS').read_text().splitlines():
 digest,name=line.split('  ',1);p=(ROOT/name).resolve()
 assert ROOT in p.parents and p.is_file(),name
 assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
 files.append((p,name))
print(f'PASS: {len(files)} file hashes',flush=True)
code=ROOT/'work/signed-c-2026-10-07'
if not args.recompute_new:
 with tempfile.NamedTemporaryFile(suffix='.json',delete=False) as f:receipt=Path(f.name)
 subprocess.run([sys.executable,str(code/'check_signed.py'),'--directory',str(code),'--out',str(receipt)],check=True)
 result=json.loads(receipt.read_bytes());expected=json.loads((ROOT/'EXACT_CHECK.json').read_bytes())
 assert result==expected
 print('PASS: rational audit equals the packaged receipt; full remainder remains open.')
 print('Receipt: '+str(receipt))
else:
 assert args.destination is not None,'--recompute-new requires --destination'
 target=args.destination.resolve()
 assert target!=ROOT and ROOT not in target.parents
 assert not target.exists() or not any(target.iterdir()),'Destination must be empty'
 target.mkdir(parents=True,exist_ok=True)
 for p,name in files:
  rel=Path(name)
  if name.startswith('work/signed-c-2026-10-07/') and p.suffix=='.json' and p.name!='PROTOCOL.json':continue
  dst=(target/rel).resolve();assert target in dst.parents
  dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst)
 code=target/'work/signed-c-2026-10-07'
 subprocess.run([sys.executable,'-c',"import flint; assert flint.__version__=='0.9.0'"],check=True)
 for bits in [3072,4096]:
  for parity in ['even','odd']:
   subprocess.run([sys.executable,str(code/'compute_cross.py'),'--bits',str(bits),'--parity',parity,
     '--out',str(code/f'CROSS_{parity.upper()}_{bits}.json')],check=True,cwd=target)
  for script,prefix in [('enclose_response.py','RESPONSE'),('assemble_signed.py','U00_SIGNED')]:
   subprocess.run([sys.executable,str(code/script),'--bits',str(bits),'--out',str(code/f'{prefix}_{bits}.json')],check=True,cwd=target)
 subprocess.run([sys.executable,str(code/'diagnostics.py')],check=True,cwd=target)
 subprocess.run([sys.executable,str(code/'check_signed.py'),'--directory',str(code),'--out',str(target/'REPLAY_CHECK.json')],check=True,cwd=target)
 print('New computational stage replayed: '+str(target))
