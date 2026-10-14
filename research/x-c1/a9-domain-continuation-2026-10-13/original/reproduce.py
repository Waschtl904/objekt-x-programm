"""Verify the sealed files and replay all NEW finite checks without Arb."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys, tempfile
HERE=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--schur-package',type=Path)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    manifest=json.loads((HERE/'MANIFEST.json').read_bytes())
    for name,want in manifest['files'].items():
        path=HERE/name
        assert path.resolve().is_relative_to(HERE.resolve())
        assert hashlib.sha256(path.read_bytes()).hexdigest()==want,name
    with tempfile.TemporaryDirectory(prefix='objekt-x-domain-replay-') as temp:
        out=Path(temp)/'check.json'
        command=[sys.executable,str(HERE/'check.py'),'--output',str(out)]
        if args.schur_package: command+=['--schur-package',str(args.schur_package.resolve())]
        run=subprocess.run(command,capture_output=True,text=True,encoding='utf-8')
        if run.returncode:
            print(run.stdout);print(run.stderr);raise SystemExit(run.returncode)
        actual=json.loads(out.read_bytes());expected=json.loads((HERE/'CHECK.json').read_bytes())
        for k in expected:
            if k!='source_verifications_this_run': assert actual[k]==expected[k],k
    result={'status':'PASS_FRESH_DOMAIN_FLOOR_EXTENSION_REPLAY',
            'manifest_files_verified':len(manifest['files']),
            'all_new_exact_check_fields_match':True,
            'source_verifications_this_run':actual['source_verifications_this_run'],
            'large_predecessor_integrations_repeated':False,
            'analytic_proof_machine_verified':False,
            'external_mathematical_review_open':True}
    if args.output: args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
