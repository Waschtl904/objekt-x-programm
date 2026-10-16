"""Replay the one-line guard revision against the untouched original archive."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,hashlib,importlib.util,json,subprocess,sys,zipfile
HERE=Path(__file__).resolve().parent
NAME='Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15'
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();assert __debug__
    out=args.output.resolve();assert not out.exists() and not out.is_relative_to(HERE)
    manifest=json.loads((HERE/'MANIFEST.json').read_bytes())
    for name,want in manifest.items():
        p=(HERE/name).resolve();assert p.is_relative_to(HERE) and sha(p.read_bytes())==want,name
    binding=json.loads((HERE/'PATCH_BINDING.json').read_bytes())
    archive=HERE/'originals'/(NAME+'.zip')
    assert sha(archive.read_bytes())==binding['original_archive_sha256']
    out.mkdir(parents=True);rebuild=out/'rebuild';rebuild.mkdir()
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():assert (rebuild/info.filename).resolve().is_relative_to(rebuild.resolve())
        z.extractall(rebuild)
    root=rebuild/NAME
    oldmanifest=json.loads((root/'MANIFEST.json').read_bytes())
    for name,want in oldmanifest.items():
        p=(root/name).resolve();assert p.is_relative_to(root) and sha(p.read_bytes())==want,name
    old=(root/'response_norm.py').read_bytes();new=(HERE/'response_norm.py').read_bytes()
    assert sha(old)==binding['original_response_norm_sha256']
    assert sha(new)==binding['patched_response_norm_sha256']
    anchor=b"    need(0<s.low<s.high<Q(1,10),'whole shell radius')\n"
    assert old.count(anchor)==1
    assert new==old.replace(anchor,anchor+b"    need(h.high < Q(101,1000),'moment Taylor shell width')\n")
    # Patch only the fresh working copy, after checking the original manifest.
    (root/'response_norm.py').write_bytes(new)
    spec=importlib.util.spec_from_file_location('response_guard_review',root/'response_norm.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    h=mod.logq(Q(11))/2-mod.logq(Q(3))
    q=Q(1,10);terms=40
    lo=sum((q**(2*k+1)/(2*k+1) for k in range(terms)),Q(0))
    hi=lo+q**(2*terms+1)/((2*terms+1)*(1-q*q))
    assert lo<h.low<=h.high<hi<Q(101,1000)
    # An upper error bound needs an upper norm bound; a lower bound cannot replace it.
    error=Q(1,10**31);true_W_norm=Q(10**100);known_lower_norm=Q(62282)
    assert known_lower_norm<true_W_norm
    assert error**2*true_W_norm>error**2*known_lower_norm
    # Midpoints of inverse enclosures are only response candidates.
    assert Q(1,2)<=1<=2 and (Q(1,2)+2)/2!=1
    def run(name,argv):
        print('Running',name,flush=True)
        with (out/(name+'.log')).open('w',encoding='utf-8') as f:
            subprocess.run([sys.executable,'-u','-B','-X','utf8']+list(map(str,argv)),check=True,stdout=f,stderr=subprocess.STDOUT)
    run('response-with-explicit-width-check',[root/'response_norm.py','--output',out/'RESPONSE_ENERGY.json'])
    assert (out/'RESPONSE_ENERGY.json').read_bytes()==(root/'RESPONSE_ENERGY.json').read_bytes()
    run('independent-Gram-check',[root/'check_response_energy.py',out/'RESPONSE_ENERGY.json','--output',out/'RESPONSE_CHECK.json'])
    assert (out/'RESPONSE_CHECK.json').read_bytes()==(root/'RESPONSE_CHECK.json').read_bytes()
    oldcheck=json.loads((out/'RESPONSE_CHECK.json').read_bytes())
    receipt={'status':'PASS','addendum_manifest_bindings':len(manifest),
       'original_manifest_bindings_before_working_copy_patch':len(oldmanifest),
       'original_archive_unchanged':True,'only_one_precondition_line_added':True,
       'h_interval':[str(h.low),str(h.high)],'independent_atanh_bounds':[str(lo),str(hi)],
       'moment_width_precondition_certified':True,
       'RESPONSE_ENERGY_fresh_and_original_byte_equal':True,
       'RESPONSE_CHECK_fresh_and_original_byte_equal':True,
       'exact_Gram_entry_comparisons':oldcheck['exact_Gram_entry_comparisons'],
       'positive_pivots':oldcheck['positive_upper_Gram_pivots'],
       'lower_norm_substitution_rejected':True,'audit_S_not_asserted_to_be_inverse':True,
       'W9_norm_certified':False,'Q_D_certified':False,'whole_W9_residual_energy_certified':False,
       'A9_A11_closed':False,'historical_large_integrations_rerun':False}
    (out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('h_interval','independent_atanh_bounds')}),flush=True)
if __name__=='__main__':main()
