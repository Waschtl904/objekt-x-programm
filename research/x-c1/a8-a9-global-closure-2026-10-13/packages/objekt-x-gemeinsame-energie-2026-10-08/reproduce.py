from pathlib import Path
import sys,json,hashlib,subprocess,tempfile,argparse,shutil
ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--recompute-algebra',action='store_true');ap.add_argument('--destination',type=Path)
args=ap.parse_args();files=[]
for line in (ROOT/'SHA256SUMS').read_text().splitlines():
 digest,name=line.split('  ',1);p=(ROOT/name.replace('\\','/')).resolve()
 assert ROOT in p.parents and hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
 files.append((p,name))
print(f'PASS: {len(files)} file hashes',flush=True)
code=ROOT/'work/185d-gate-2026-10-08'
if not args.recompute_algebra:
 with tempfile.NamedTemporaryFile(suffix='.json',delete=False) as f:out=Path(f.name)
 subprocess.run([sys.executable,str(code/'check_stage.py'),'--directory',str(code),'--out',str(out)],check=True)
 assert json.loads(out.read_bytes())==json.loads((ROOT/'EXACT_CHECK.json').read_bytes())
 print('PASS: exact bounded audit equals the packaged receipt.')
else:
 assert args.destination is not None
 target=args.destination.resolve();assert target!=ROOT and ROOT not in target.parents
 assert not target.exists() or not any(target.iterdir());target.mkdir(parents=True,exist_ok=True)
 outputs={'FEASIBILITY.json','COMPLETION_PROBE.json','JOINT_1024.json','JOINT_1536.json','EXACT_CHECK.json'}
 for p,name in files:
  if name.startswith('work/185d-gate-2026-10-08/') and p.name in outputs:continue
  dst=(target/name).resolve();assert target in dst.parents;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst)
 code=target/'work/185d-gate-2026-10-08'
 subprocess.run([sys.executable,'-c',"import flint; assert flint.__version__=='0.9.0'"],check=True)
 for script in ['feasibility.py','completion_probe.py']:
  subprocess.run([sys.executable,str(code/script)],check=True,cwd=target)
 for bits in [1024,1536]:
  subprocess.run([sys.executable,str(code/'joint_candidate.py'),'--arithmetic-bits',str(bits),'--out',str(code/f'JOINT_{bits}.json')],check=True,cwd=target)
 subprocess.run([sys.executable,str(code/'check_stage.py'),'--directory',str(code),'--out',str(target/'REPLAY_CHECK.json')],check=True)
 print('Algebraic replay completed; no operator integration was run.')
