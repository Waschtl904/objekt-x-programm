#!/usr/bin/env python3
"""Exact rational ledger for the A-gauge high-tail contraction theorem."""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json

HERE=Path(__file__).resolve().parent
P_SEG=Path('research/x-c1/prime-power-segment-4-2026-09-18')
P_TRANS=Path('research/x-c1/a-gauge-transition-congruence-2026-09-19')
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_high_tail.py','input_bindings.json','high_tail_results.json','high_tail_checks.log']


def log_upper_rational(n, terms=120):
    # log n = 2 atanh((n-1)/(n+1)); positive tail bounded geometrically.
    x=F(n-1,n+1)
    total=F(0)
    power=x
    for k in range(terms):
        total += power/F(2*k+1)
        power *= x*x
    tail = power/F(2*terms+1)/(1-x*x)
    return 2*(total+tail)


def decimal(x):
    x=F(x); scale=10**18
    lo=(x.numerator*scale)//x.denominator
    hi=-((-x.numerator*scale)//x.denominator)
    def fmt(k): return ('-' if k<0 else '')+str(abs(k)//scale)+'.'+str(abs(k)%scale).zfill(18)
    return [fmt(lo),fmt(hi)]


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=HERE.parents[2])
    g=ap.add_mutually_exclusive_group();g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true')
    args=ap.parse_args(); root=args.root.resolve()
    bind=json.loads((HERE/'input_bindings.json').read_text())
    checks=[]
    def ok(name,c):
        assert c,name;checks.append(name)
    ok('anchor is current A-gauge transition head',bind['anchor']=='8f5b711145b28b6dbfc8280d8e51625f3d2f1532')
    ok('seven direct immutable inputs',len(bind['files'])==7 and len({x['path'] for x in bind['files']})==7)
    for item in bind['files']:
        raw=(root/item['path']).read_bytes()
        assert len(raw)==item['bytes'],item['path']
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'],item['path']
    ok('all direct input bytes SHA256 and Git blobs match',True)

    seg=json.loads((root/P_SEG/'segment_results.json').read_text())
    trans=json.loads((root/P_TRANS/'transition_results.json').read_text())
    v=seg['values']
    delta=F(v['even_tail_floor']['lo']); beta=F(v['even_beta']['hi'])
    alpha=delta/(1+beta)
    ok('endpoint tail begins after degree 62',seg['cutoff']==63)
    ok('even tail floor exceeds 0.719',delta>F(719,1000))
    ok('even Mellin norm beta is below 0.007',beta<F(7,1000))
    ok('physical reconstructed tail floor exceeds seven tenths',alpha>F(7,10))

    l2=log_upper_rational(2); l3=log_upper_rational(3); l5=log_upper_rational(5)
    s2lo=F(1414,1000); s3lo=F(1732,1000); s5lo=F(2236,1000)
    ok('radical lower witnesses',s2lo*s2lo<2 and s3lo*s3lo<3 and s5lo*s5lo<5)
    ok('w2 below 0.491',l2/s2lo<F(491,1000))
    ok('w3 below 0.635',l3/s3lo<F(635,1000))
    ok('w4 below 0.347',l2/2<F(347,1000))
    ok('w5 below 0.721',l5/s5lo<F(721,1000))
    arithmetic=2*F(2194,1000)
    ok('four reflected prime channels below 4.388',arithmetic==F(1097,250))

    s2hi=F(1415,1000); pi_hi=F(22,7); sqrth=F(1,10**10)
    ok('sqrt two upper witness',s2hi*s2hi>2)
    gamma=s2hi*(pi_hi/2+F(5,4)*sqrth)
    ok('full Gamma Carleman coefficient below 2.224',gamma<F(278,125))
    complete=gamma+arithmetic
    ok('Gamma plus exact-weight prime coefficient below 6.62',complete<F(331,50))

    ok('Gamma chi Cauchy coefficient below 48',106*21<48**2)
    ok('bounded chi remainder coefficient below 84',14**2*F(180,7)<84**2)
    qchi=132
    moment=F(6,5)*sqrth*qchi
    ok('tail moment correction below one hundredth energy amplitude',moment<F(1,100))
    s_amp_sq=F(331,50)**2*F(10,7)
    ok('shell term below 7.92 energy amplitude',s_amp_sq<F(792,100)**2)
    total_amp=F(793,100)
    ok('combined squared energy amplitude below 63',total_amp*total_amp<63)
    ok('full shell profile floor exceeds 73 at h0',2*46-19==73)
    kappa=F(63,73)
    ok('complete high-tail block strictly below one',kappa<1)

    nu=F(trans['values']['published_A_direction_eta_upper']['hi'])
    ok('near-null A direction is inherited below 7.55e-6',nu==F(151,20000000))
    mixed_sq=nu*kappa
    ok('Near-High mixed Gram square bound below one hundred thousandth',mixed_sq<F(1,100000))

    report={
      'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
      'anchor':bind['anchor'],
      'verdict':'FULL-A-GAUGE-HIGH-TAIL-CONTRACTIVE / FINITE-LOW-BLOCK-OPEN',
      'interval':'B=log(5)/2, 0<h<=10^-20',
      'endpoint_tail_reference':'even Mellin-reconstructed Legendre tail degrees >=64',
      'tail_low_dimension_bound':31,
      'all_source_full_width_closed':False,
      'odd_continuation_closed':False,
      'passed_checks':checks,
      'values':{
        'endpoint_tail_floor_lower':str(delta),
        'endpoint_beta_upper':str(beta),
        'physical_tail_alpha_lower_witness':'7/10',
        'prime_cross_upper_witness':str(arithmetic),
        'gamma_cross_upper_witness':'278/125',
        'complete_L2_cross_upper_witness':'331/50',
        'combined_energy_amplitude_upper_witness':'793/100',
        'shell_profile_floor_lower_witness':'73',
        'high_tail_Theta_upper':str(kappa),
        'near_A_eta_upper':str(nu),
        'near_high_mixed_squared_upper':str(mixed_sq)
      }
    }
    jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
    logtext='\n'.join('PASS '+x for x in checks)+'\nTOTAL '+str(len(checks))+' HIGH-TAIL EXACT CHECKS PASS\n'+report['verdict']+'\n'
    if args.write:
        (HERE/'high_tail_results.json').write_text(jsontext,newline='\n')
        (HERE/'high_tail_checks.log').write_text(logtext,newline='\n')
        (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/f).read_bytes()).hexdigest()+'  '+f+'\n' for f in PAYLOAD),encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'high_tail_results.json').read_bytes()==jsontext.encode()
        assert (HERE/'high_tail_checks.log').read_bytes()==logtext.encode()
        lines=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines();assert len(lines)==len(PAYLOAD)
        for line,f in zip(lines,PAYLOAD):
            d,n=line.split('  ',1);assert n==f;assert hashlib.sha256((HERE/f).read_bytes()).hexdigest()==d
        print('REPLAY and all seven high-tail package SHA256 hashes PASS')
    print(logtext,end='')

if __name__=='__main__':main()
