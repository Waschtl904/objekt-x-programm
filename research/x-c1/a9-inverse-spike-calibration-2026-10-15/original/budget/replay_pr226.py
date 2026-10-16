from pathlib import Path
import importlib.util,json,argparse
HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--inputs',type=Path,default=HERE.parents[1]/'outputs')
ap.add_argument('--output',type=Path,default=HERE/'PR226_REPLAY.json');args=ap.parse_args()
assert not args.output.exists()
spec=importlib.util.spec_from_file_location('pr226_verifier',HERE/'pr226/verify.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
mod.ARCHIVE=args.inputs/'Objekt-X-A9-Inverserneuerung-und-Hoher-Schurrest-2026-10-13.zip'
arch=mod.load_archive();wit=json.loads(mod.WITNESSES.read_bytes())
assert wit['source_archive_sha256']==mod.ARCHIVE_SHA
out={'status':'PASS','source_archive_sha256':mod.ARCHIVE_SHA,'override':'archive path only; original mathematical checks unchanged','parities':{}}
for par in ('even','odd'):
    print('Checking original',par,'84 by 84 exact LDL',flush=True)
    out['parities'][par]=mod.check_parity(par,arch[par],wit['parities'][par])
    print('PASS',par,flush=True)
args.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(out['status'],flush=True)
