"""Replay this review and the unchanged endpoint input package."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, tempfile, zipfile
HERE=Path(__file__).resolve().parent
INPUT='Objekt-X-Randtest-im-unendlichen-Rest-2026-10-11'
RESP='Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11'
COMMON='Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11'
HASHES={INPUT:'a7126347b62078edf0025bba5450dbbef8b0af9c754a4c289b34eb4bca93b49a',
 RESP:'5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3',
 COMMON:'06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51'}
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def extract(p,target):
    with zipfile.ZipFile(p) as z:
        for e in z.infolist():
            assert (target/e.filename).resolve().is_relative_to(target.resolve())
            assert ((e.external_attr>>16)&0o170000)!=0o120000
        z.extractall(target)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--responses-zip',type=Path,required=True);ap.add_argument('--parent-zip',type=Path,required=True);args=ap.parse_args()
    assert __debug__
    manifest=json.loads((HERE/'MANIFEST.json').read_bytes())
    for name,want in manifest['files'].items():
        p=(HERE/name).resolve();assert p.is_relative_to(HERE);assert sha(p)==want,name
    print('REVIEW_MANIFEST_PASS',len(manifest['files']),flush=True)
    archive=HERE/'inputs'/f'{INPUT}.zip'
    for name,p in [(INPUT,archive),(RESP,args.responses_zip),(COMMON,args.parent_zip)]:assert sha(p)==HASHES[name],name
    with tempfile.TemporaryDirectory(prefix='objekt-x-boundary-review-') as d:
        temp=Path(d);extract(archive,temp);root=temp/INPUT
        out=temp/'INDEPENDENT_GEOMETRY.json'
        subprocess.run([sys.executable,'-B',str(HERE/'check_geometry.py'),'--input',str(root),'--out',str(out)],check=True)
        assert json.loads(out.read_bytes())==json.loads((HERE/'data/INDEPENDENT_GEOMETRY.json').read_bytes())
        subprocess.run([sys.executable,'-B',str(root/'reproduce.py'),'--responses-zip',str(args.responses_zip.resolve()),'--parent-zip',str(args.parent_zip.resolve())],check=True)
    print('PASS_BOUNDARY_REVIEW_AND_UNCHANGED_INPUT_REPLAY',flush=True)
    print('NEW_SOURCE_INTEGRATIONS_EXECUTED=false; FULL_TAIL_UPPER_COMPUTED=false; FULL_REMAINDER_CERTIFIED=false',flush=True)
if __name__=='__main__':main()
