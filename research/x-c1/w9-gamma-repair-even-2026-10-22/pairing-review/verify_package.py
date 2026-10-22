"""Portable exact audit. Analytic prerequisites remain conditional."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,shutil,tempfile,subprocess,sys
if not __debug__:
 raise SystemExit('Verification requires assertions enabled; Python -O/-OO is rejected.')
B=Path(__file__).resolve().parent
seen=set()
for line in (B/'SHA256SUMS.txt').read_text().splitlines():
 h,rel=line.split('  ',1);p=B/rel
 assert not Path(rel).is_absolute() and p.resolve().is_relative_to(B.resolve())
 assert hashlib.sha256(p.read_bytes()).hexdigest()==h,rel
 seen.add(rel)
assert seen=={p.relative_to(B).as_posix()for p in B.rglob('*')if p.is_file()}-{'SHA256SUMS.txt'}
A=B/'connection-audit/repair-review'
d=json.loads((A/'reassembly-audit.json').read_bytes());assert len(d['rows'])==84
for i,r in enumerate(d['rows'],1):
 assert r['coordinate']==i
 lo,hi=map(F,r['raw_difference']);assert lo<=hi
 e=F(r['integration_error_upper'])+F(r['remaining_core_error_upper'])
 assert e==F(r['complete_error_envelope'])
 assert max(abs(lo),abs(hi))<=e
 assert e-max(abs(lo),abs(hi))==F(r['margin'])>0
assert min(F(r['margin'])for r in d['rows'])==F(d['minimum_margin'])
c=json.loads((A/'work/pairing-refinement/contour-review.json').read_bytes())
R=F(c['normalized_radius'][0]);M=F(c['corrected_contour_bound'][1])
assert R>1 and M*R**(-8)/(1-1/R)<F('2e-88')
assert len(list((B/'Replayed-panels').glob('*.json')))==16
with tempfile.TemporaryDirectory(prefix='objekt-x-rational-')as td:
 dest=Path(td)/'inputs';shutil.copytree(B/'Rationale-Pruefung',dest)
 received=json.loads((dest/'rational-audit.json').read_bytes())
 subprocess.run([sys.executable,str(dest/'rational_audit.py')],check=True,capture_output=True,text=True)
 assert json.loads((dest/'rational-audit.json').read_bytes())==received
print('PASS: own hashes, 84 full rational hulls, corrected contour tail < 2e-88, exact budget replay.')
print('CONDITIONAL on inherited analytic inputs; external acceptance remains OPEN.')
