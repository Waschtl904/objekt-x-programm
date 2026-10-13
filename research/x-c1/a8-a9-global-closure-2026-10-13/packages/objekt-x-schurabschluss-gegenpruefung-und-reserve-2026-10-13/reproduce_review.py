"""Verify this review and optionally repeat the complete sealed input chain."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
from independent_review import review,INPUT_SHA
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def main():
    if not __debug__:raise RuntimeError('Run without Python optimization flags.')
    ap=argparse.ArgumentParser();ap.add_argument('--input-zip',type=Path,required=True)
    ap.add_argument('--receipt',type=Path,required=True);ap.add_argument('--full-chain',action='store_true')
    a=ap.parse_args()
    for n,w in read(HERE/'MANIFEST.json')['files'].items():
        p=(HERE/n).resolve();assert p.is_relative_to(HERE) and sha(p)==w,n
    assert sha(a.input_zip)==INPUT_SHA
    result=review(a.input_zip);assert result==read(HERE/'INDEPENDENT_REVIEW.json')
    full=None
    if a.full_chain:
        with tempfile.TemporaryDirectory(prefix='objekt-x-schur-review-') as td:
            td=Path(td)
            with zipfile.ZipFile(a.input_zip) as z:
                for e in z.infolist():
                    assert (td/e.filename).resolve().is_relative_to(td.resolve())
                    assert ((e.external_attr>>16)&0o170000)!=0o120000
                z.extractall(td)
            p=td/'Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13'
            out=td/'FULL_CHAIN.json'
            subprocess.run([sys.executable,'-u','-B',str(p/'reproduce.py'),'--receipt',str(out)],check=True)
            full=read(out);assert full==read(HERE/'OUR_FULL_CHAIN_REPLAY.json')
    receipt={'status':'PASS_SCHUR_COUNTERREVIEW_PACKAGE','input_zip_sha256':INPUT_SHA,
        'independent_rational_review':result,'full_input_chain_repeated_this_run':a.full_chain,
        'full_input_chain_receipt':full,'large_global_integrations_repeated':False}
    a.receipt.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(receipt['status'],flush=True)
if __name__=='__main__':main()
