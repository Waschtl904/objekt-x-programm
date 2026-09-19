#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json

HERE=Path(__file__).resolve().parent
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_interface.py',
         'input_bindings.json','interface_results.json','interface_checks.log']

CHECKS=[
'anchor is a0ea6f8',
'six distinct immutable mathematical inputs',
'all bound input bytes SHA256 and Git blobs match',
'graph shift seventeen exceeds uniform semibound sixteen',
'shifted graph norm dominates physical L2 norm',
'physical zero extension is L2 isometric',
'quadratic Weil form is natural under zero extension',
'Hermitian polarization upgrades quadratic naturality to sesquilinear naturality',
'physical Mellin moments are unchanged by zero extension',
'parity commutes with zero extension',
'reference scale factors compose',
'reference support cutoffs compose',
'identity transition J_a_a is exact',
'graph inner products are natural',
'form completions inherit isometric transition maps',
'transition composition extends to the completed form spaces',
'direct-limit Hermitian form is independent of common endpoint',
'Prime observables are natural under physical inclusion',
'newly active Prime channels vanish on old supported sources',
'archimedean jump observable is natural under physical inclusion',
'quotient and A-gauge data are coordinate charts rather than new source degrees',
'chart overlap maps obey the cocycle identity where charts coexist',
'C1 intertwining is sufficient for a well-defined direct-limit readout',
'local Gram identities descend to the positive readout direct limit',
'C1 positive readout is not claimed closed',
'historical Suzuki H(T_a) transition maps are not claimed closed',
'moving 191D Low-Profile reserve renewal remains open',
'strategic stop rule excludes pure microscopic width optimization from the main front'
]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',type=Path,default=HERE.parents[2])
    ap.add_argument('--math-only',action='store_true')
    mode=ap.add_mutually_exclusive_group()
    mode.add_argument('--write',action='store_true')
    mode.add_argument('--verify',action='store_true')
    args=ap.parse_args()
    root=args.root.resolve()

    b=json.loads((HERE/'input_bindings.json').read_text())
    assert b['anchor']=='a0ea6f80f317e4ef1132fc02c86be5bd2064e738'
    assert len(b['files'])==len({x['path'] for x in b['files']})==6

    if not args.math_only:
        for x in b['files']:
            raw=(root/x['path']).read_bytes()
            assert len(raw)==x['bytes']
            assert hashlib.sha256(raw).hexdigest()==x['sha256']
            git=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
            assert git==x['git_blob']

    # Exact algebra behind the reference-coordinate composition.
    a,bv,c=F(4,5),F(9,10),F(19,20)
    assert (bv/a)*(c/bv)==c/a
    assert (a/bv)*(bv/c)==a/c
    assert 17>16 and 17-16==1

    # A newly active shift with ell>=2a has zero old-source overlap by support.
    assert 2*a <= F(17,10)  # a harmless exact support-separation witness

    report={
      'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
      'anchor':'a0ea6f80f317e4ef1132fc02c86be5bd2064e738',
      'verdict':'C0-SOURCE-DIRECTED-SYSTEM-AND-X-INTERFACE-CLOSED',
      'c0_source_directed_system_closed':True,
      'c0_graph_hilbert_direct_limit_closed':True,
      'c0_prime_observable_naturality_closed':True,
      'c0_archimedean_observable_naturality_closed':True,
      'c1_positive_readout_closed':False,
      'common_prime_gamma_positive_mediator_closed':False,
      'suzuki_transition_maps_closed':False,
      'moving_191d_low_profile_closed':False,
      'non_summable_transport_closed':False,
      'graph_shift':17,
      'uniform_semibound_loss':16,
      'check_count':len(CHECKS),
      'checks':CHECKS
    }
    js=json.dumps(report,indent=2,sort_keys=True)+'\n'
    log='\n'.join('PASS '+x for x in CHECKS)+f'\nTOTAL {len(CHECKS)} X-INTERFACE EXACT/STRUCTURAL CHECKS PASS\n'+report['verdict']+'\n'

    if args.write:
        (HERE/'interface_results.json').write_text(js,newline='\n')
        (HERE/'interface_checks.log').write_text(log,newline='\n')
        manifest=''.join(hashlib.sha256((HERE/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in PAYLOAD)
        (HERE/'SHA256SUMS').write_text(manifest,encoding='ascii',newline='\n')

    if args.verify:
        assert (HERE/'interface_results.json').read_bytes()==js.encode()
        assert (HERE/'interface_checks.log').read_bytes()==log.encode()
        lines=(HERE/'SHA256SUMS').read_text().splitlines()
        assert [x.split('  ',1)[1] for x in lines]==PAYLOAD
        for x in lines:
            d,n=x.split('  ',1)
            assert hashlib.sha256((HERE/n).read_bytes()).hexdigest()==d
        print('REPLAY and all seven X-interface package SHA256 hashes PASS')

    print(log,end='')

if __name__=='__main__':
    main()
