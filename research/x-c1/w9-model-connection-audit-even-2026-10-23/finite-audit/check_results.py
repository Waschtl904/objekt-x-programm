"""Check package bytes, exact caps, bookkeeping and declared scope."""
import sys
if not __debug__:raise SystemExit('Python -O/-OO is rejected')
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
H=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((H/'MANIFEST.json').read_bytes())
actual={p.relative_to(H).as_posix()for p in H.rglob('*')if p.is_file()}
assert actual==set(manifest)|{'MANIFEST.json'}
for name,want in manifest.items():assert sha(H/name)==want,name
read=lambda n:json.loads((H/'evidence'/n).read_bytes())
s=read('source-caps.json')['values'];upper=lambda p:F(p[1])
assert upper(s['continuous_corrected_u_norm'])<F('3.240e17')<F('1e20')
assert upper(s['continuous_alpha_cap'])<F('1e18')
assert upper(s['explicit_moment_chain_X'])<F('8.570e-257')
assert upper(s['n128_atom_total_variation'])<1
f=read('finite-RESULT.json')['whole_force_transport']['values']
assert upper(f['full_force_operator_upper'])<F('6.051')<10
g=read('raw-operator-result.json')['bounds_with_half'];assert upper(g['raw_g_and_density_adjoint'])<F('11.439')<100
c=read('cache-price.json');assert F(c['complete_difference_X_upper'])<F('5.989e-888')
assert F(c['new_joint_raw_equivalent_upper'])<F('7.729e-239')<F('1e-150')
assert all(read('cache-rebuild.json')['components_exact'].values())
r=read('rational-cross-audit.json');assert F(r['repaired_Ldual_energy_upper'])<F('4.632e-11')
assert r['whole_arithmetic_hulls_inside_justified_error']==84
assert r['p_error_recharged']is False and r['inner_quadrature_tail_charged_twice']is False
p=json.loads((H/'PFLICHTEN.json').read_bytes());assert p['next_single_obligation']=='H-SOURCE'
assert p['overall']=='CONDITIONAL_INTERNAL_ANALYTIC_REVIEW_NOT_FINISHED'
print('PASS: package bindings, exact caps and bounded bookkeeping; H-SOURCE remains open.')
