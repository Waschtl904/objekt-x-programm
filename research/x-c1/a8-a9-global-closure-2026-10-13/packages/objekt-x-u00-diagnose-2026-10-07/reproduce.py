"""Portable manifest check, exact audit, and optional full numerical replay."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile,shutil
ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--full',action='store_true');ap.add_argument('--destination',type=Path)
args=ap.parse_args()
files=[]
for line in (ROOT/'SHA256SUMS').read_text().splitlines():
    digest,name=line.split('  ',1);p=(ROOT/name).resolve()
    assert ROOT in p.parents and p.is_file(),name
    assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
    files.append((p,name))
print(f'PASS: {len(files)} package file hashes',flush=True)
code=ROOT/'work/u00-2026-10-07'
if not args.full:
    with tempfile.NamedTemporaryFile(suffix='.json',delete=False) as f:receipt=Path(f.name)
    subprocess.run([sys.executable,str(code/'check_u00.py'),'--directory',str(code),'--out',str(receipt)],check=True)
    result=json.loads(receipt.read_bytes());expected=json.loads((ROOT/'EXACT_CHECK.json').read_bytes())
    assert result==expected
    print('PASS: exact audit equals the supplied receipt; full remainder remains uncertified.')
    print('Audit receipt: '+str(receipt))
else:
    assert args.destination is not None,'--full requires --destination'
    target=args.destination.resolve()
    assert target!=ROOT and ROOT not in target.parents,'Use a separate output directory'
    assert not target.exists() or not any(target.iterdir()),'Destination must be empty'
    target.mkdir(parents=True,exist_ok=True)
    for p,name in files:
        rel=Path(name)
        if name.startswith('work/u00-2026-10-07/'):
            if 'history-before-global-rounding' in rel.parts:continue
            if p.suffix=='.json' and p.name!='PROTOCOL.json':continue
        dst=(target/rel).resolve();assert target in dst.parents
        dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst)
    code=target/'work/u00-2026-10-07'
    subprocess.run([sys.executable,'-c',"import flint; assert flint.__version__=='0.9.0'"],check=True)
    for bits in [3072,4096]:
        for parity in ['even','odd']:
            for script,prefix in [('compute_centres.py','CENTRES'),('compute_duals.py','DUALS')]:
                out=code/f'{prefix}_{parity.upper()}_{bits}.json'
                subprocess.run([sys.executable,str(code/script),'--bits',str(bits),'--parity',parity,'--out',str(out)],check=True,cwd=target)
        subprocess.run([sys.executable,str(code/'assemble.py'),'--bits',str(bits),'--out',str(code/f'U00_FINAL_{bits}.json')],check=True,cwd=target)
    subprocess.run([sys.executable,str(code/'check_integrals.py')],check=True,cwd=target)
    subprocess.run([sys.executable,str(code/'check_u00.py'),'--directory',str(code),'--out',str(target/'REPLAY_CHECK.json')],check=True,cwd=target)
    print('Full replay completed: '+str(target))
