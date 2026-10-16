"""Rebuild the new whole response Grams; optional fresh incoming full replay."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,zipfile
HERE=Path(__file__).resolve().parent
AUDIT=HERE/'input/objekt-x-f12-d12-audit-2026-10-15'
FUNCTIONS_ARCHIVE=AUDIT/'originals/Objekt-X-A9-A11-Ganze-Kraftfunktionen-und-D12-2026-10-15.zip'
FUNCTIONS_SHA='0a7bda3d2d896801f757c3b658d9ad559529409c64dd489283e656b95710d3d3'
FIXED_SHA='132959da5d34c0c89471ee15f7c34d8b4a42ad48c641b6c4db5181113d11426a'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--full-input',action='store_true');a=ap.parse_args()
    assert __debug__,'Do not disable checks with -O'
    out=a.output.resolve();assert not out.exists() and not out.is_relative_to(HERE),'new output outside package required'
    bindings=json.loads((HERE/'MANIFEST.json').read_bytes())
    for name,want in bindings.items():
        p=(HERE/name).resolve();assert p.is_relative_to(HERE) and sha(p)==want,name
    for name,want in json.loads((AUDIT/'MANIFEST.json').read_bytes()).items():
        p=(AUDIT/name).resolve();assert p.is_relative_to(AUDIT) and sha(p)==want,name
    assert sha(FUNCTIONS_ARCHIVE)==FUNCTIONS_SHA
    assert sha(HERE/'inputs/FROZEN_RESPONSE12.json')==FIXED_SHA
    with zipfile.ZipFile(FUNCTIONS_ARCHIVE) as z:
        for name,member in [('FUNCTIONS12.json','FUNCTIONS12.json'),('FRESH_A12.json','FRESH_A12.json'),('OLD_A9_N12.json','inputs/OLD_A9_N12.json')]:
            assert z.read('objekt-x-whole-functions12-2026-10-15/'+member)==(HERE/'inputs'/name).read_bytes()
    out.mkdir(parents=True)
    def run(args,name):
        print('Running',name,flush=True)
        with (out/(name+'.log')).open('w',encoding='utf-8') as f:
            subprocess.run([sys.executable,'-u','-B','-X','utf8']+list(map(str,args)),check=True,stdout=f,stderr=subprocess.STDOUT)
    run([HERE/'response_norm.py','--output',out/'RESPONSE_ENERGY.json'],'whole-response-Grams')
    assert (out/'RESPONSE_ENERGY.json').read_bytes()==(HERE/'RESPONSE_ENERGY.json').read_bytes()
    run([HERE/'check_response_energy.py',out/'RESPONSE_ENERGY.json','--output',out/'RESPONSE_CHECK.json'],'separate-exact-check')
    assert (out/'RESPONSE_CHECK.json').read_bytes()==(HERE/'RESPONSE_CHECK.json').read_bytes()
    if a.full_input:run([HERE/'replay_transport.py','--output',out/'incoming-full-replay'],'incoming-full-replay')
    receipt={'status':'PASS','manifest_bindings':len(bindings),'original_function_members_byte_equal':3,
       'fixed_response_unchanged':True,'new_energy_JSON_fresh_and_byte_equal':True,
       'new_separate_check_fresh_and_byte_equal':True,'exact_Gram_entry_comparisons':576,
       'positive_upper_Gram_pivots':48,'incoming_full_replay_rerun_in_this_invocation':a.full_input,
       'incoming_previous_fresh_replay_receipt_bound':True,'exact_D_projection_required':True,
       'complete_response_Gram_certified_under_inherited_hypotheses':True,
       'direct_K_model_error_certified_under_inherited_hypotheses':True,
       'W9_norm_certified':False,'Q_D_certified':False,'whole_W9_residual_energy_certified':False,
       'new_A9_A11_certificate_closed':False,'external_review_open':True}
    (out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
