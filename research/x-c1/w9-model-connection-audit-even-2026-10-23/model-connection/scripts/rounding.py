"""Price the canonical rational w -> frozen midpoint w0 exactly once.

Inherited common D/U source-error and whole-operator lemmas stay conditional.
No new numerical integration; no change to the test vector.
"""
import sys
if not __debug__:raise SystemExit('Assertions required; no -O/-OO.')
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction
from decimal import Decimal,localcontext
import json,hashlib
W=Path(__file__).resolve().parent
code=(W/'rebuild.py').read_text(encoding='utf-8').split("old=initialize(source);status('OLD_SOURCE_BUILT')")[0]
ns={'__file__':str(W/'rebuild.py'),'__name__':'canonical_rounding_audit'}
exec(compile(code,'bound_rebuild_initialization','exec'),ns)
arb=ns['arb'];ctx=ns['ctx'];ctx.prec=3072
base=ns['base'];c=base['c'];q=c.q;e=base['e'];env=base['env'];cached=ns['cached']
R=ns['ROOT'];PKG=R/'research/x-c1/w9-new-k-schur-underform-even-2026-10-20'
canonical=json.loads((PKG/'CANDIDATE.json').read_bytes())['raw_coefficients']
dw=[Fraction(v)-Fraction(str(cached['w'][i,0].fmpq()))for i,v in enumerate(canonical)]
dw2=sum((v*v for v in dw),Fraction(0))
assert dw2<Fraction('5e-309')**2
norm=q(str(dw2)).sqrt().upper()
root=lambda x:x.upper().sqrt()
tr=c.trace
Ki=e.w['Ki'];GF=e.w['GF'];GJ=e.w['GJ'];U=env['U']
UF=ns['arb_mat']([[U[i,j]for j in range(12)]for i in range(12)])
UJ=ns['arb_mat']([[U[i,j]for j in range(12,96)]for i in range(12,96)])
EF=base['EF'];EJ=base['EJ'];dd=e.bounds['direct_energy_relative_error_upper']
ea=(dd*root(tr(Ki*GF)*tr(GJ))+root(tr(Ki*UF)*EJ)
    +root(tr(Ki*EF)*tr(UJ))+root(tr(Ki*EF)*EJ))
weighted_a_norm=root(tr(e.w['a'].transpose()*Ki*e.w['a']))+ea
# True J has W_X norm <2. g and its X-density adjoint are <=100;
# the fixed D action has X-density norm <=2e5 using the bound finite Q
# action <=1e5 and Lambda's norm <=2. These are inherited conservative caps.
U8=e.bounds['U8_norm_upper']
assert U8.is_finite() and U8>0
eta=q('1e-10');density_direct_cap=(1+eta)*q('2e5')+q(20000)*U8
# ea_direction in the legacy probe is evaluated before its midpoint replacement.
# Rebase that directional source-error bound by ea*||dw|| as well; do not
# silently reuse an error bound evaluated at a different vector.
directional_rebase=q(10)*ea*norm
Lprice=(q('5/21').sqrt()*density_direct_cap+q(10)*weighted_a_norm)*norm+directional_rebase
# Express it in outer X-equivalent units before using the existing allowance.
Xequivalent=(Lprice/q('5/21').sqrt()).upper()
j=json.loads((W/'component-rebuild.json').read_bytes())
previous=q(j['bounds']['sum_projection_moment_and_rebuild_allowances'][1])
total=(previous+Xequivalent).upper()
assert total<q('1e-150')
def enc(v):return [str(v.lower().fmpq()),str(v.upper().fmpq())]
def dec(v):
    f=Fraction(str(v.upper().fmpq()))
    with localcontext()as d:
        d.prec=18
        return str(Decimal(f.numerator)/Decimal(f.denominator))
out={'status':'CANONICAL_W_ROUNDING_TRANSPORT_PASS_CONDITIONAL',
 'canonical_candidate_sha256':hashlib.sha256((PKG/'CANDIDATE.json').read_bytes()).hexdigest(),
 'nonzero_rounding_coordinates':sum(v!=0 for v in dw),'exact_w_difference_squared':str(dw2),
 'bounds':{k:enc(v)for k,v in dict(w_rounding_norm=norm,a_common_error_operator=ea,
   weighted_a_operator=weighted_a_norm,U8=U8,directional_rebase_Ldual=directional_rebase,rounding_Ldual_price=Lprice,
   rounding_X_equivalent=Xequivalent,total_allowance_X_equivalent=total).items()},
 'display':{'w_rounding_norm':dec(norm),'rounding_Ldual_price':dec(Lprice),
   'rounding_X_equivalent':dec(Xequivalent),'total_allowance_X_equivalent':dec(total)},
 'within_existing_raw_source_allowance_once':True,
 'conditional_caps':{'D_Xdensity_on_J':200000,'J_X_operator':2,'Lambda_adjoint_X_operator':2,
   'g_raw_and_adjoint_X':100,'force_D_to_Ldual':10},
 'common_source_error_lemmas_and_operator_caps_inherited':True,
 'external_acceptance':False}
(W/'rounding-result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'display':out['display']},indent=2))
