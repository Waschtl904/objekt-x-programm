"""Fresh sealed-archive replay and the new exact global Schur assembly."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, tempfile, zipfile
from assemble import assemble

HERE=Path(__file__).resolve().parent
NAMES={
 'gram':'Objekt-X-Globaler-Gram-und-vollstaendige-Projektion-2026-10-13',
 'logreview':'Objekt-X-Logrest-Gegenpruefung-und-groesseres-Ableitungsbudget-2026-10-12',
 'responses':'Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11',
 'common':'Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11',
 'innerlogs':'Objekt-X-Innere-Randterme-und-Gemeinsamer-Logrest-2026-10-12',
 'outerlog':'Objekt-X-Aussenresidualpruefung-und-Logarithmischer-Randtail-2026-10-11',
 'exterior':'Objekt-X-Zusammengesetzte-Aussenresiduen-und-Momentanschluss-2026-10-11'}
def read(p):return json.loads(p.read_bytes())
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def extract(p,target):
    with zipfile.ZipFile(p) as z:
        for e in z.infolist():
            assert (target/e.filename).resolve().is_relative_to(target.resolve())
            assert ((e.external_attr>>16)&0o170000)!=0o120000
        z.extractall(target)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--receipt',type=Path,required=True)
    ap.add_argument('--inputs',type=Path,default=HERE/'inputs')
    ap.add_argument('--assembly-only',action='store_true')
    args=ap.parse_args();assert __debug__
    if (HERE/'MANIFEST.json').exists():
        for name,want in read(HERE/'MANIFEST.json')['files'].items():
            p=(HERE/name).resolve();assert p.is_relative_to(HERE) and sha(p)==want,name
    bindings=read(HERE/'INPUT_BINDINGS.json'); passed=[]
    logdir=args.receipt.resolve().parent/(args.receipt.stem+'-logs');logdir.mkdir(exist_ok=True)
    def run(tag,script,argv,marker):
        print('RUN',tag,flush=True)
        with (logdir/(tag+'.log')).open('w',encoding='utf-8') as f:
            subprocess.run([sys.executable,'-u','-B',str(script),*map(str,argv)],check=True,stdout=f,stderr=subprocess.STDOUT)
        assert marker in (logdir/(tag+'.log')).read_text(),(tag,'missing completion marker')
        passed.append(tag); print('PASS',tag,flush=True)
    with tempfile.TemporaryDirectory(prefix='objekt-x-final-schur-') as td:
        td=Path(td); roots={}; zips={}
        for key in ['gram','logreview','responses','common']:
            path=(args.inputs/(NAMES[key]+'.zip')).resolve()
            assert sha(path)==bindings[key]['sha256'],key
            extract(path,td); roots[key]=td/NAMES[key];zips[key]=path
        for key,parent in [('innerlogs','logreview'),('outerlog','innerlogs'),('exterior','outerlog')]:
            extract(roots[parent]/'inputs'/(NAMES[key]+'.zip'),td);roots[key]=td/NAMES[key]
        if not args.assembly_only:
            run('GLOBAL_GRAM',roots['gram']/'reproduce.py',['--receipt',td/'GLOBAL.json'],
                'PASS_COMPLETE_GLOBAL_GRAM_RATIONAL_REPLAY')
            run('RESPONSES_AND_COMMON',HERE/'replay_responses_portably.py',
                [roots['responses'],'--input-zip',zips['common'],'--full-input-replay'],
                'PASS_RESPONSE_REPLAY_WITH_ONLY_CRLF_LF_COMPARISON_PORTABILITY_FIX')
            run('EXTERIOR_GEOMETRY',roots['exterior']/'reproduce.py',
                ['--responses-zip',zips['responses'],'--common-zip',zips['common']],
                'PASS_COMPOSED_RESIDUAL_PACKAGE_FRESH_REPLAY')
            run('LOGS_AND_TARGET',roots['logreview']/'reproduce_review.py',
                ['--responses-zip',zips['responses'],'--common-zip',zips['common']],
                'PASS_COMMON_LOG_REVIEW_AND_ENLARGED_DERIVATIVE_TARGETS')
        output=td/'ASSEMBLY.json'
        result=assemble(**{k:roots[k] for k in ['gram','responses','logreview','innerlogs','exterior','common']},out=output)
        if (HERE/'ASSEMBLY_AUDIT.json').exists(): assert result==read(HERE/'ASSEMBLY_AUDIT.json')
    receipt={'status':'PASS_FRESH_FINAL_SCHUR_ASSEMBLY','full_bound_input_replays_performed':not args.assembly_only,
        'completed_replays':passed,'assembly':result,'fresh_full_integrations_repeated':False,
        'scope':'Conditional on the bound analytic operator, form-domain and complete-space-decomposition hypotheses; no tail 1/20 or all-horizons claim.'}
    args.receipt.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(receipt['status'],flush=True)
if __name__=='__main__':main()
