"""Replay the original basis calculation and this review from its sealed ZIP."""
from pathlib import Path
from zipfile import ZipFile
import argparse
import hashlib
import json
import os
import subprocess
import sys

ROOT=Path(__file__).resolve().parent


def read(path):return json.loads(path.read_bytes())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('original_zip',type=Path)
    ap.add_argument('--work',type=Path,required=True)
    ap.add_argument('--deps',type=Path)
    args=ap.parse_args()
    bind=read(ROOT/'SOURCE_BINDINGS.json')
    assert sha(args.original_zip)==bind['original_zip']['sha256']
    files=read(ROOT/'MANIFEST.json')['files']
    for name,digest in files.items():
        p=(ROOT/name).resolve()
        assert p.is_relative_to(ROOT) and sha(p)==digest,name
    work=args.work.resolve()
    assert not work.exists(),'Choose a fresh work directory'
    work.mkdir(parents=True)
    with ZipFile(args.original_zip) as z:
        for name in z.namelist():assert (work/name).resolve().is_relative_to(work)
        z.extractall(work)
    package=work/bind['original_zip']['root_directory']
    env=os.environ.copy()
    if args.deps:env['PYTHONPATH']=str(args.deps.resolve())+os.pathsep+env.get('PYTHONPATH','')
    def run(script,*opts):
        subprocess.run([sys.executable,str(script),*map(str,opts)],env=env,check=True)
    run(package/'reproduce.py','--compute')
    with ZipFile(args.original_zip) as z:
        for name in ['BASIS_EVEN.json','BASIS_ODD.json','GATE_EVEN.json','GATE_ODD.json','RESULT.json','AUDIT.json']:
            rel='work/basis-coverage-2026-10-10/'+name
            old=z.read(package.name+'/'+rel)
            new=(package/rel).read_bytes()
            assert old.replace(b'\r\n',b'\n')==new,name
    calc=work/'calculated'
    run(ROOT/'check_basis_and_build_L.py',package,'--out',calc)
    for name in ['INDEPENDENT_CHECKS.json','L_ENERGY_84_EVEN.json','L_ENERGY_84_ODD.json']:
        assert read(calc/name)==read(ROOT/'expected'/name),name
    result={'status':'PASS_BASIS84_REVIEW_AND_L_ENERGY_REPLAY',
            'original_six_outputs_reproduced_modulo_line_endings':True,
            'independent_check_output_reproduced':True,
            'two_L_energy_84_enclosures_reproduced':True,
            'review_manifest_files':len(files),
            'new_H_or_A0_operator_integrations':False,
            'full_remainder_certified':False}
    (work/'REVIEW_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
