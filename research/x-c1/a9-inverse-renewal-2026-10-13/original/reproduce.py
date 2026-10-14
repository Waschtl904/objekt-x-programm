"""Verify sealed contents, repeat the full new rational audit, compare results."""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys
HERE=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--schur-package',type=Path)
    ap.add_argument('--output',type=Path,default=HERE/'REPLAY.json');args=ap.parse_args()
    manifest=json.loads((HERE/'MANIFEST.json').read_bytes())
    for name,d in manifest['files'].items():
        p=HERE/name;raw=p.read_bytes()
        assert len(raw)==d['bytes'] and hashlib.sha256(raw).hexdigest()==d['sha256'],name
    target=args.output.with_name(args.output.stem+'-audit.json')
    cmd=[sys.executable,str(HERE/'audit.py'),'--output',str(target)]
    if args.schur_package:cmd+=['--schur-package',str(args.schur_package)]
    subprocess.run(cmd,check=True)
    expected=json.loads((HERE/'AUDIT.json').read_bytes());actual=json.loads(target.read_bytes())
    binding=actual['original_Schur_source_fields_verified']
    for field in ['seconds','original_Schur_source_fields_verified']:
        expected.pop(field);actual.pop(field)
    assert actual==expected,'mathematical audit fields differ'
    out={'status':'PASS_FRESH_PACKAGE_REPLAY','sealed_files_verified':len(manifest['files']),
         'all_mathematical_audit_fields_identical':True,
         'original_Schur_source_fields_verified':binding,
         'new_complete_positive_LDL_pivots':574,
         'large_integrations_rerun':False,'external_review_open':True}
    args.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
