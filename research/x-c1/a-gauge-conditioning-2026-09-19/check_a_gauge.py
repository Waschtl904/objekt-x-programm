#!/usr/bin/env python3
"""Arithmetic replay for the A-gauge conditioning package.

This checker verifies pinned inputs, replays the parent directional certificate,
and checks only the finite rational arithmetic used in the displayed conditioning
constants. The analytic L2-functional and form-domain proofs are in PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, subprocess, sys

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--root',type=Path,default=HERE.parents[2])
g=parser.add_mutually_exclusive_group();g.add_argument('--write',action='store_true');g.add_argument('--verify',action='store_true')
args=parser.parse_args();REPO=args.root.resolve();ROOT=REPO/'research/x-c1'
BIND=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
for item in BIND['files']:
    raw=(REPO/item['path']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'],item['path']

parent=ROOT/'near-null-reduced-schur-direction-2026-09-19'
replay=subprocess.run([sys.executable,str(parent/'check_direction.py'),'--verify','--root',str(REPO)],capture_output=True,text=True,check=True)
assert not replay.stderr
assert 'TOTAL 31 NEW EXACT CHECKS PASS' in replay.stdout
assert 'REPLAY and all seven direction-package SHA256 hashes PASS' in replay.stdout
D=json.loads((parent/'direction_results.json').read_text(encoding='utf-8'))
qpsi_lo=F(D['values']['q_psi_psi']['lo'])

checks=[]
def ok(name,cond):
    assert cond,name;checks.append(name)

ok('parent trace energy exceeds 0.14',qpsi_lo>F(14,100))
ok('Gamma representative square bound',2*(124**2+2*124*8+8**2*2)==34976<188**2)
ok('non-Gamma plus Gamma functional bound',188+14*6==272)
ok('A-gauge coefficient bound',F(272,1)/F(14,100)<1943)
K=(1+6*1943)**2+1943**2
ok('core inverse conditioning integer',K==139707530<140000000)
h0=F(1,10**20)
mu2=F(648,25)*h0
mu=F(6,10**10)
ok('shell moment correction below chosen mu',mu2<mu*mu)
ok('core coefficient remains below 140m',F(K)*(1+mu)<140000000)
ok('shell coefficient is harmless',1+F(K)*mu*(1+mu)<2)
ok('forward coordinate constant unchanged',1+8**2==65)

report={
 'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
 'anchor':BIND['anchor'],
 'interval':'b = log(5)/2 + h, 0 < h <= 10^-20',
 'q_psi_psi_lower_import':str(qpsi_lo),
 'L2_functional_bound':272,
 'ell_A_L2_bound':1943,
 'core_inverse_factor':K,
 'full_inverse_factor':140000000,
 'forward_factor':65,
 'pure_trace_cross_exactly_zero':'analytic identity in PROOF.md',
 'new_exact_checks':len(checks),
 'passed_checks':checks,
 'all_core_schur_closed':False,
 'odd_continuation_closed':False,
}
jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
logtext='\n'.join('PASS '+x for x in checks)+'\nTOTAL '+str(len(checks))+' A-GAUGE ARITHMETIC CHECKS PASS\n'
if args.write:
    (HERE/'a_gauge_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
    (HERE/'a_gauge_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
    payload=['PROOF.md','README.md','STATUS_DE.md','check_a_gauge.py','input_bindings.json','a_gauge_results.json','a_gauge_checks.log']
    (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/f).read_bytes()).hexdigest()+'  '+f+'\n' for f in payload),encoding='ascii',newline='\n')
if args.verify:
    assert (HERE/'a_gauge_results.json').read_bytes()==jsontext.encode()
    assert (HERE/'a_gauge_checks.log').read_bytes()==logtext.encode()
    lines=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines();assert len(lines)==7
    for line in lines:
        digest,name=line.split('  ',1)
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
    print('REPLAY and all seven A-gauge package SHA256 hashes PASS')
print(logtext,end='')
