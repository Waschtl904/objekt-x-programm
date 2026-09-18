#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import json

# Exact source-level Rayleigh enclosure copied from the committed
# prime-power-segment-4 result at 6a16d90... .  The analytic monotonicity
# theorem is in PROOF.md; these checks bind its quantitative corollary.
LO=F('164814522840761248995619815807364924101674927763366358637886619578932704991870488192147930862884576446538346059244703233836651710700688259637808914350377221301870980636666555323964944665639/50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
HI=F('329629119641678396715614642284203289594975043263146221495670279121308617458008960690532639869911066782010656318170847272175058906709454996836111704365930258925302796110072550114443409839601/100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
PUBLISHED_ENDPOINT_GAP=F(1,10**13)
CEILING=F(33,10**13) # 3.3e-12

checks=[]
def ok(name,cond):
    if not cond: raise AssertionError(name)
    checks.append(name)

ok('explicit even source Rayleigh lower endpoint positive',LO>0)
ok('explicit even source Rayleigh interval ordered',LO<HI)
ok('explicit even source Rayleigh upper below 3.3e-12',HI<CEILING)
ok('published positive endpoint gap lies below explicit source Rayleigh',PUBLISHED_ENDPOINT_GAP<LO)
ok('zero-extension quantitative ceiling is nontrivial',CEILING< F(1,10**11))

res={
  'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
  'parent':'9d9c48de2d6e4d56556f38f45489d133c17bd181',
  'endpoint':'log(5)/2',
  'even_source_rayleigh_lower':str(LO),
  'even_source_rayleigh_upper':str(HI),
  'inherited_future_even_gap_ceiling':'33/10000000000000',
  'published_endpoint_lower_gap':'1/10000000000000',
  'checks':len(checks),
}
Path('window_gap_monotonicity_results.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
for c in checks: print('PASS',c)
print('TOTAL',len(checks))
