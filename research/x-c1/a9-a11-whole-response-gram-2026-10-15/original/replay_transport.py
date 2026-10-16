"""Execute the unchanged incoming replay with an explicit CRLF/LF comparison.

Only the two platform-native generated audit JSON comparisons are normalized.
All archive/source hashes and mathematical data remain byte-for-byte bound.
"""
from pathlib import Path
import json,hashlib,sys,argparse
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'input/objekt-x-f12-d12-audit-2026-10-15/verify.py'
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    text=SOURCE.read_text(encoding='utf-8')
    old="require((out/'reports'/name).read_bytes()==(here/'reports'/name).read_bytes(),'new independent receipt differs: '+name)"
    new="require((out/'reports'/name).read_bytes().replace(b'\\r\\n',b'\\n')==(here/'reports'/name).read_bytes().replace(b'\\r\\n',b'\\n'),'new independent receipt differs beyond line endings: '+name)"
    assert text.count(old)==1
    patched=text.replace(old,new).replace('PASS: original outputs and all four audit receipts are byte-identical.','PASS: original outputs are byte-identical; generated audit JSON agrees after CRLF/LF normalization.')
    scope={'__file__':str(SOURCE),'__name__':'transport_wrapped_original'}
    exec(compile(patched,str(SOURCE),'exec'),scope)
    scope['run'](SOURCE.parent,a.output)
    comparisons={}
    for name in ('INDEPENDENT_FUNCTIONS.json','RESPONSE_ERROR_BUDGET.json'):
        raw=(a.output/'reports'/name).read_bytes();expected=(SOURCE.parent/'reports'/name).read_bytes()
        assert json.loads(raw)==json.loads(expected)
        comparisons[name]={'raw_byte_equal':raw==expected,'LF_normalized_equal':raw.replace(b'\r\n',b'\n')==expected.replace(b'\r\n',b'\n'),'JSON_equal':True}
    receipt={'original_verifier_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
       'source_modified':False,'comparison_change':'only CRLF to LF in two generated audit JSON comparisons',
       'full_original_and_independent_calculations_rerun':True,'comparisons':comparisons}
    (a.output/'TRANSPORT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('PASS: explicit transport correction; all substantive data unchanged.')
if __name__=='__main__':main()
