from pathlib import Path
import json,hashlib,difflib
from fractions import Fraction as F
B=Path(__file__).resolve().parent;A=B.parent;R=B/'received';W=B/'work/pairing-refinement'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks={};names=list(range(32,40))+list(range(238,246))
exact=0
for i in names:
 x=json.loads((R/f'Abschnitte/{i:04}.json').read_bytes());y=json.loads((W/f'extra-panels/{i:04}.json').read_bytes())
 x.pop('seconds');y.pop('seconds');assert x==y,i;exact+=1
checks['extra_panel_numeric_records_exactly_reproduced']=exact
for file in ['core-tail.json','orientation-validation.json']:
 x=json.loads((R/'Pruefdaten'/file).read_bytes());y=json.loads((W/file).read_bytes());x.pop('seconds');y.pop('seconds');assert x==y,file
 checks[file+'_numeric_records_exactly_reproduced']=True
inputs=json.loads((A/'checked-inputs.json').read_bytes())
for r in inputs['files']:assert sha(A/'repo'/r['path'])==r['sha256'],r['path']
checks['selected_repository_files_still_unchanged']=len(inputs['files'])
checks['github_writes_performed']=False
(B/'final-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
original=(R/'Neuberechnung/pairing-refinement/core_tail.py').read_text()
needle='hh=tm.hjet(ns,xx);h0=hh.s[0]'
replacement='''# The tail Cauchy radius R is not 2. Bound every polynomial on the
# same normalized radius R before using the order-eight Cauchy remainder.
def peval_R(p,x):
 x=tm.jet(x);assert x.s.length()<=2
 co=p(arb_poly([x.s[0],x.s[1]]))
 bound=arb_poly([abs(v).upper()for v in co])(R).upper()
 return tm.Jet(arb_series(list(co)[:tm.Jet.N],prec=tm.Jet.N),acb(arb(0,bound),arb(0,bound)))
tm.peval=peval_R
hh=tm.hjet(ns,xx);h0=hh.s[0]'''
assert original.count(needle)==1
fixed=original.replace(needle,replacement)
(B/'core-tail-contour-fix.patch').write_text(''.join(difflib.unified_diff(original.splitlines(keepends=True),fixed.splitlines(keepends=True),fromfile='a/Neuberechnung/pairing-refinement/core_tail.py',tofile='b/Neuberechnung/pairing-refinement/core_tail.py')))
# Portable verification of the archive and all local result assertions.
print(json.dumps(checks,indent=2))
