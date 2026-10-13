"""Portable rational replay of the unchanged input and new derivative budgets."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
HERE=Path(__file__).resolve().parent
INPUT='Objekt-X-Innere-Randterme-und-Gemeinsamer-Logrest-2026-10-12'
REVIEW='Objekt-X-Aussenresidualpruefung-und-Logarithmischer-Randtail-2026-10-11'
RESP='Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11'
COMMON='Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11'
HASHES={INPUT:'96b8367c5f49ab8b99f63aade251942221a3fcad50ba09c6acb3a662e0dd8016',
 REVIEW:'d4394c74d224cda1fcab44bc7e945a608f2228ff3cc91fcbe75da59de3572e3e',
 RESP:'5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3',
 COMMON:'06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51'}
def read(p):return json.loads(p.read_bytes())
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def extract(p,d):
    with zipfile.ZipFile(p) as z:
        for e in z.infolist():
            assert (d/e.filename).resolve().is_relative_to(d.resolve())
            assert ((e.external_attr>>16)&0o170000)!=0o120000
        z.extractall(d)
def run(*a):subprocess.run([sys.executable,'-B',*map(str,a)],check=True)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--responses-zip',type=Path,required=True);ap.add_argument('--common-zip',type=Path,required=True);x=ap.parse_args();assert __debug__
    mf=read(HERE/'MANIFEST.json')['files']
    for name,want in mf.items():
        p=(HERE/name).resolve();assert p.is_relative_to(HERE);assert sha(p)==want,name
    print('REVIEW_MANIFEST_PASS',len(mf),flush=True)
    source=HERE/'inputs'/(INPUT+'.zip')
    for name,p in [(INPUT,source),(RESP,x.responses_zip),(COMMON,x.common_zip)]:assert sha(p)==HASHES[name],name
    with tempfile.TemporaryDirectory(prefix='objekt-x-logrest-budget-review-') as td:
        td=Path(td);extract(source,td);root=td/INPUT
        run(root/'reproduce.py','--responses-zip',x.responses_zip.resolve(),'--common-zip',x.common_zip.resolve())
        extract(x.responses_zip,td)
        prev=root/'inputs'/(REVIEW+'.zip');assert sha(prev)==HASHES[REVIEW];extract(prev,td)
        for script,result in [('audit_young_budget.py','YOUNG_BUDGET_AUDIT.json'),('audit_directional_target.py','DIRECTIONAL_DERIVATIVE_TARGET.json')]:
            output=td/result
            run(HERE/script,'--input',root,'--responses',td/RESP,'--review',td/REVIEW,'--out',output)
            assert read(output)==read(HERE/'data'/result),result
    print('PASS_COMMON_LOG_REVIEW_AND_ENLARGED_DERIVATIVE_TARGETS',flush=True)
    print('ACTUAL_REGULARIZED_DERIVATIVE_GRAM_COMPUTED=false; FULL_REMAINDER_CERTIFIED=false; TAIL_FLOOR_CERTIFIED=false',flush=True)
if __name__=='__main__':main()
