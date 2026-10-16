"""Sealed-package checks and fresh exact directional reconstruction."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--full-pr226',action='store_true');args=ap.parse_args()
    assert __debug__;out=args.output.resolve()
    assert not out.exists() and not out.is_relative_to(HERE)
    manifest=json.loads((HERE/'MANIFEST.json').read_bytes())
    for name,want in manifest.items():
        p=(HERE/name).resolve();assert p.is_relative_to(HERE) and sha(p.read_bytes())==want,name
    bound=json.loads((HERE/'PR_BINDINGS.json').read_bytes())
    for name,record in bound['files'].items():
        b=(HERE/'pr226'/name).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==record['git_blob_sha'],name
    out.mkdir(parents=True)
    def run(name,argv):
        print('Running',name,flush=True)
        with (out/(name+'.log')).open('w',encoding='utf-8') as f:
            subprocess.run([sys.executable,'-u','-B','-X','utf8']+list(map(str,argv)),stdout=f,stderr=subprocess.STDOUT,check=True)
    run('directions',[HERE/'check_budget_direction.py','--inputs',HERE/'inputs','--output',out/'BUDGET_CERTIFICATE.json'])
    assert (out/'BUDGET_CERTIFICATE.json').read_bytes()==(HERE/'BUDGET_CERTIFICATE.json').read_bytes()
    run('separate-integer-check',[HERE/'independent_direction_check.py','--inputs',HERE/'inputs','--result',out/'BUDGET_CERTIFICATE.json','--output',out/'INDEPENDENT_CHECK.json'])
    assert (out/'INDEPENDENT_CHECK.json').read_bytes()==(HERE/'INDEPENDENT_CHECK.json').read_bytes()
    if args.full_pr226:
        run('original-pr226',[HERE/'replay_pr226.py','--inputs',HERE/'inputs','--output',out/'PR226_REPLAY.json'])
    result={'status':'PASS','manifest_bindings':len(manifest),'exact_Git_blob_bindings':len(bound['files']),
            'new_directional_result_fresh_and_byte_equal':True,'separate_check_fresh_and_byte_equal':True,
            'original_pr226_replay_executed_this_invocation':args.full_pr226,
            'previous_fresh_original_pr226_replay_bound':True,
            'full_A9_inverse_claim':False,'A9_A11_closed':False,'external_review_open':True}
    (out/'RECEIPT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result),flush=True)
if __name__=='__main__':main()
