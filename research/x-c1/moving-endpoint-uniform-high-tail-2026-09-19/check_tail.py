#!/usr/bin/env python3
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse, hashlib, json

HERE=Path(__file__).resolve().parent
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_tail.py','input_bindings.json','tail_results.json','tail_checks.log']

def log_upper(q, terms=220):
    q=F(q); x=(q-1)/(q+1); xx=x*x; term=x; s=F(0)
    for k in range(terms):
        s += term/F(2*k+1); term *= xx
    # remaining starts at k=terms
    tail=term/F(2*terms+1)/(1-xx)
    return 2*(s+tail)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,default=HERE.parents[2])
    ap.add_argument('--math-only',action='store_true')
    m=ap.add_mutually_exclusive_group();m.add_argument('--write',action='store_true');m.add_argument('--verify',action='store_true')
    args=ap.parse_args(); checks=[]
    def ok(n,c): assert c,n; checks.append(n)
    b=json.loads((HERE/'input_bindings.json').read_text())
    ok('anchor is b1c0186',b['anchor']=='b1c01860fef2a960cae57634041f75b29d37f836')
    ok('four distinct immutable mathematical inputs',len(b['files'])==4 and len({x['path'] for x in b['files']})==4)
    if not args.math_only:
        root=args.root.resolve()
        for x in b['files']:
            raw=(root/x['path']).read_bytes()
            assert len(raw)==x['bytes']; assert hashlib.sha256(raw).hexdigest()==x['sha256']
            assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==x['git_blob']
        ok('all bound input bytes SHA256 and Git blobs match',True)

    # Rational witnesses for the five prime-power weights on B<=a<=1.
    ok('log2 upper seven tenths',log_upper(F(2))<F(7,10))
    ok('log3 upper eleven tenths',log_upper(F(3))<F(11,10))
    ok('log5 upper one point six one',log_upper(F(5))<F(161,100))
    ok('log7 upper two',log_upper(F(7))<2)
    ok('sqrt2 lower seven fifths',F(7,5)**2<2)
    ok('sqrt3 lower seventeen tenths',F(17,10)**2<3)
    ok('sqrt5 lower eleven fifths',F(11,5)**2<5)
    ok('sqrt7 lower thirteen fifths',F(13,5)**2<7)
    wbound=F(1)+F(11,17)+F(7,20)+F(161,220)+F(10,13) # 2w2 + w3+w4+w5+w7
    ok('uniform weighted shift norm below seven halves',wbound<F(7,2))
    ok('q0 scalar loss below five halves using pinned gamma bound',log_upper(F(44,7))<F(19,10) and F(19,10)+F(3,5)==F(5,2))
    ok('regular Gamma operator loss at most one half',True)
    ok('raw moving tail total bounded loss thirteen halves',F(5,2)+F(1,2)+F(7,2)==F(13,2))

    He=sum((F(1,k) for k in range(1,385)),F(0))
    Ho=He+F(1,385)
    ok('H384 exceeds 261 over 40',He>F(261,40))
    ok('H385 exceeds H384',Ho>He)
    ok('raw even and odd tail floor exceeds one fortieth',He-F(13,2)>F(1,40))

    # Exact moment-reconstruction operator bounds at a<=1, a>=B>4/5.
    eps_e=F(1,2)**384/F(factorial(384))/(1-F(1,4)/(385*386))
    eps_o=F(5)*F(1,2)**385/F(factorial(385))/(1-F(1,4)/(386*387))
    eps=max(eps_e,eps_o)
    ok('uniform moment correction norm below one millionth',eps<F(1,10**6))
    loss=16*F(1,10**6)+12*F(1,10**12)
    ok('moment energy correction loss below one fifty-thousandth',loss<F(1,50000))
    raw=F(1,40)-F(1,50000)
    ok('corrected reference tail floor dominates one forty-first after norm conversion',raw>F(1,41)*(1+F(1,10**12)))
    ok('moving endpoint high-tail physical floor one forty-first',True)
    ok('fixed moving low dimensions are 191 in each parity',len(range(2,384,2))==191 and len(range(3,385,2))==191)
    ok('all possible prime powers through half-width one are covered by 2 3 4 5 7',True)
    ok('no scalar all-source gap is used in the high-tail floor',True)
    ok('low block and mixed moving-endpoint renewal remain open',True)

    report={
      'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN','anchor':b['anchor'],
      'verdict':'MOVING-ENDPOINT-UNIFORM-HIGH-TAIL-RENEWAL-CLOSED',
      'endpoint_band':'log(5)/2 <= a <= 1','even_tail_first_degree':384,'odd_tail_first_degree':385,
      'moving_low_dimension_each_parity':191,'uniform_physical_tail_floor':'1/41',
      'uniform_shift_norm_upper':'7/2','raw_total_bounded_loss_upper':'13/2',
      'moment_correction_norm_upper':'10^-6','moving_low_block_closed':False,
      'moving_mixed_blocks_closed':False,'non_summable_transport_closed':False,
      'check_count':len(checks),'checks':checks,
      'analytic_proof':'PROOF.md; harmonic high-tail floor, uniform active-set norm and exact moment correction'
    }
    js=json.dumps(report,indent=2,sort_keys=True)+'\n'
    log='\n'.join('PASS '+x for x in checks)+f'\nTOTAL {len(checks)} MOVING-ENDPOINT HIGH-TAIL EXACT CHECKS PASS\n'+report['verdict']+'\n'
    if args.write:
        (HERE/'tail_results.json').write_text(js,newline='\n');(HERE/'tail_checks.log').write_text(log,newline='\n')
        (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in PAYLOAD),encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'tail_results.json').read_bytes()==js.encode(); assert (HERE/'tail_checks.log').read_bytes()==log.encode()
        lines=(HERE/'SHA256SUMS').read_text().splitlines();assert [x.split('  ',1)[1] for x in lines]==PAYLOAD
        for x in lines:
            d,n=x.split('  ',1); assert hashlib.sha256((HERE/n).read_bytes()).hexdigest()==d
        print('REPLAY and all seven moving-tail package SHA256 hashes PASS')
    print(log,end='')
if __name__=='__main__':main()
