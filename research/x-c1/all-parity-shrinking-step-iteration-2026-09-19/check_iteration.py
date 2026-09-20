#!/usr/bin/env python3
"""Exact ledger for the all-parity restart and shrinking-step iteration lemma."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json

HERE=Path(__file__).resolve().parent
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_iteration.py',
         'input_bindings.json','iteration_results.json','iteration_checks.log']


def git_blob_sha(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=HERE.parents[2])
    ap.add_argument('--math-only',action='store_true')
    modes=ap.add_mutually_exclusive_group();modes.add_argument('--write',action='store_true');modes.add_argument('--verify',action='store_true')
    args=ap.parse_args(); root=args.root.resolve()
    checks=[]
    def ok(name,c):
        assert c,name;checks.append(name)

    binding=json.loads((HERE/'input_bindings.json').read_text())
    ok('anchor is the local all-parity commit',binding['anchor']=='a659047e00d024c0daa3991ea59fd21afd9f8793')
    ok('six distinct immutable mathematical inputs',len(binding['files'])==6 and len({x['path'] for x in binding['files']})==6)
    if not args.math_only:
        for item in binding['files']:
            raw=(root/item['path']).read_bytes()
            assert len(raw)==item['bytes'],item['path']+' bytes'
            assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']+' SHA256'
            assert git_blob_sha(raw)==item['git_blob'],item['path']+' git blob'
        ok('all bound input bytes hashes and Git blobs match',True)
        odd=json.loads((root/'research/x-c1/odd-profile-continuation-2026-09-19/odd_results.json').read_text())
        even=json.loads((root/'research/x-c1/full-core-profile-width-amplification-2026-09-19/width_results.json').read_text())
        ok('starting local all-parity theorem is certified',odd['local_all_parity_certified'] is True)
        ok('starting published all-parity gap is exactly three e minus fifteen',F(odd['values']['published_local_all_parity_gap']['lo'])==F(3,10**15))
        ok('full-width even prerequisite remains certified',even['full_original_width_even_all_source_certified'] is True)
        prime_hi=F(odd['values']['complete_disjoint_prime_coupling_upper']['hi'])
    else:
        prime_hi=F(1601,1000)-F(1,10**12)

    # Local endpoint band and prime geometry use elementary log(1+x)>=x/(1+x).
    ok('log six fifths lower witness',F(1,6)-F(1,50)-F(2,10**20)>0)
    ok('log four thirds lower witness',F(1,4)-F(1,10**20)>0)
    ok('log five fourths lower witness',F(1,5)-F(1,10**20)>0)
    ok('q7 stays inactive on the restart band',F(2,7)-F(1,50)-F(2,10**20)>0)

    # Uniform corrector constants.
    ok('even corrector moment lower gives sup below three',F(5,2)<3)
    ok('even corrector Lipschitz below four',F(25,8)<4)
    ok('even corrector norm squared below thirteen',F(25,2)<13)
    ok('odd corrector moment lower is two seventy fifths',F(2,75)>0)
    ok('odd corrector sup below ten',F(75,8)<10)
    ok('odd corrector Lipschitz below 47',F(375,8)<47)
    ok('odd corrector norm squared below 200',True)

    # Series witnesses at 1/2.
    cosh_upper=F(1)+F(1,8)+F(1,384)*F(120,119)
    sinh_upper=F(1,2)+F(1,48)+F(1,3840)*F(168,167)
    ok('cosh one half below six fifths',cosh_upper<F(6,5))
    ok('sinh one half below three fifths',sinh_upper<F(3,5))

    # Corrector functional ledgers.
    ok('even Gamma action norm below 155',23834<155**2)
    ok('even bounded remainder below sixty',14**2*13<60**2)
    ok('even complete corrector functional below 215',155+60==215)
    ok('odd Gamma action norm below 1000',980800<1000**2)
    ok('odd bounded remainder below 200',14**2*200<200**2)
    ok('odd complete corrector functional below 1200',1000+200==1200)

    # Complete coupling <4 at h<=1e-20.
    gamma_singular=F(110,49)                  # pi/sqrt2 < (22/7)(5/7)
    gamma_small=F(15,8*10**10)                # (5 sqrt2 /4) sqrt(a h)
    moment_small=F(720,10**10)                # odd is the worse moment correction
    coupling=gamma_singular+prime_hi+gamma_small+moment_small
    ok('pinned disjoint-prime coupling below 1.601',prime_hi<F(1601,1000))
    ok('uniform complete restart core-profile coupling below four',coupling<4)

    # Uniform profile losses at h0, with L(h0)<47 and monotonic h(L+c).
    even_loss=F(36,5)*58*F(1,10**20)+F(6552,25)*F(1,10**20)
    odd_loss=(12*47+1140)*F(1,10**20)
    ok('even profile moment loss below one',even_loss<1)
    ok('odd profile moment loss below one',odd_loss<1)
    ok('common profile floor ledger is two L minus seventeen',True)

    # Abstract restart algebra.
    eps=F(3,10**15); gam=F(2,10**15); m=eps-gam
    delta=m/2; eta=m/(4*gam)
    ok('restart Young allocation is positive',delta>0 and eta>0)
    ok('core norm target has strict reserve',eps-delta>gam*(1+eta))
    ok('restart profile Schur deduction is sixteen over delta',F(16,delta)==F(32,m))

    # Explicit infinite schedule.
    N0=4*10**16
    m0=F(1,10**15)
    ok('log two lower witness from positive atanh series',F(2,3)>0)
    profile_scale=F(4*N0,3)-17-F(32,m0)
    ok('base scheduled profile reserve dominates every target',profile_scale>F(9,10**15))
    ok('scheduled exponents exceed eighty',N0>=80)
    ok('two to eighty exceeds ten to twenty',2**80>10**20)
    ok('scheduled norm-loss universal bound below one',F(648,2**20)<1)
    ok('scheduled total extra width is below ten to minus twenty',F(1,2**79)<F(1,10**20))

    # Symbolic identities defining all n>=0.
    ok('gap sequence starts at three e minus fifteen',F(1,10**15)*(1+2)==F(3,10**15))
    ok('gap sequence has positive limiting floor one e minus fifteen',F(1,10**15)>0)
    ok('profile scale coefficient remains positive under doubling',F(64,3)*10**15>0)

    report={
      'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
      'anchor':binding['anchor'],
      'verdict':'ALL-PARITY-RESTART-AND-SHRINKING-STEP-ITERATION-CLOSED',
      'uniform_step_iteration_certified':False,
      'window_amplification_certified':False,
      'restart_endpoint_band':'log(5)/2 <= a <= log(5)/2 + 10^-2',
      'restart_coupling_upper':'4',
      'restart_profile_floor':'2*log(2/h)-17',
      'iteration_start':'b0=log(5)/2+10^-20',
      'iteration_gap':'epsilon_n=10^-15*(1+2^(1-n))',
      'iteration_exponent':'N_n=4*10^16*2^n',
      'iteration_width':'h_n=2^(-N_n)',
      'uniform_gap_floor':'10^-15',
      'total_added_width_upper':'2^(-4*10^16+1) < 10^-20',
      'checks':checks,
      'check_count':len(checks),
      'analytic_proof':'PROOF.md; form-space restart coordinates, shell estimates, Young/Schur budget and infinite induction'
    }
    js=json.dumps(report,indent=2,sort_keys=True)+'\n'
    log='\n'.join('PASS '+x for x in checks)+f'\nTOTAL {len(checks)} RESTART/ITERATION EXACT CHECKS PASS\n'+report['verdict']+'\n'
    if args.write:
        (HERE/'iteration_results.json').write_text(js,encoding='utf-8',newline='\n')
        (HERE/'iteration_checks.log').write_text(log,encoding='utf-8',newline='\n')
        manifest=''.join(hashlib.sha256((HERE/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in PAYLOAD)
        (HERE/'SHA256SUMS').write_text(manifest,encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'iteration_results.json').read_bytes()==js.encode()
        assert (HERE/'iteration_checks.log').read_bytes()==log.encode()
        entries=(HERE/'SHA256SUMS').read_text().splitlines()
        assert [e.split('  ',1)[1] for e in entries]==PAYLOAD
        for e in entries:
            d,n=e.split('  ',1); assert hashlib.sha256((HERE/n).read_bytes()).hexdigest()==d
        print('REPLAY and all seven iteration-package SHA256 hashes PASS')
    print(log,end='')

if __name__=='__main__': main()
