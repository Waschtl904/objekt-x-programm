"""Replay optimized target audit and the new rational consolidation."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
HERE=Path(__file__).resolve().parent
CURRENT='Objekt-X-Globaler-Anschluss-und-Optimiertes-Restbudget-2026-10-12'
PRIOR='Objekt-X-Logrest-Gegenpruefung-und-groesseres-Ableitungsbudget-2026-10-12'
LOG='Objekt-X-Innere-Randterme-und-Gemeinsamer-Logrest-2026-10-12'
RESP='Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11'
HASHES={CURRENT:'7a51fbebb8587ed2c61af9c933c8f3ae86f1412c94edb09eb17ce64f533a8a4f',
 PRIOR:'6febe3404fc9fe040e925653a545b7b516554305cd1f148be19b79bb3d46f273',
 LOG:'96b8367c5f49ab8b99f63aade251942221a3fcad50ba09c6acb3a662e0dd8016',
 RESP:'5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3'}
def read(p):return json.loads(p.read_bytes())
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def manifest(root):
    for name,want in read(root/'MANIFEST.json')['files'].items():
        p=(root/name).resolve();assert p.is_relative_to(root.resolve());assert sha(p)==want,name
def extract(p,dest):
    with zipfile.ZipFile(p) as z:
        for e in z.infolist():
            assert (dest/e.filename).resolve().is_relative_to(dest.resolve())
            assert ((e.external_attr>>16)&0o170000)!=0o120000
        z.extractall(dest)
def run(*a):subprocess.run([sys.executable,'-B',*map(str,a)],check=True)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--responses-zip',type=Path,required=True);ap.add_argument('--boundary-review-zip',type=Path,required=True);x=ap.parse_args();assert __debug__
    manifest(HERE);print('REVIEW_MANIFEST_PASS',flush=True)
    assert sha(x.responses_zip)==HASHES[RESP]
    assert sha(x.boundary_review_zip)=='869a8b518825ed73a440cc82f0dfaba7f8f70c330931c2f4571ee6e880d684a0'
    with tempfile.TemporaryDirectory(prefix='objekt-x-target-consolidation-') as td:
        td=Path(td)
        for name in [CURRENT,PRIOR]:
            z=HERE/'inputs'/(name+'.zip');assert sha(z)==HASHES[name];extract(z,td);manifest(td/name)
        logzip=td/PRIOR/'inputs'/(LOG+'.zip');assert sha(logzip)==HASHES[LOG]
        run(td/CURRENT/'reproduce.py','--responses-zip',x.responses_zip.resolve(),'--log-zip',logzip,'--review-zip',x.boundary_review_zip.resolve())
        extract(x.responses_zip,td);out=td/'CONSOLIDATION_AUDIT.json'
        run(HERE/'audit_consolidation.py','--current',td/CURRENT,'--prior',td/PRIOR,'--responses',td/RESP,'--out',out)
        assert read(out)==read(HERE/'data/CONSOLIDATION_AUDIT.json')
    print('PASS_OPTIMIZED_BUDGET_REVIEW_AND_DIRECTIONAL_CONSOLIDATION',flush=True)
    print('GLOBAL_MODEL_GRAM_COMPUTED=false; GLOBAL_MODEL_ERROR_CERTIFIED=false; FULL_REMAINDER_CERTIFIED=false',flush=True)
if __name__=='__main__':main()
