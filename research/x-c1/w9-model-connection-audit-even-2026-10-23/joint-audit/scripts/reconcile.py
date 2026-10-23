"""Compare independent fresh replays and reconcile identified tiny remainders.

Only the listed remainders are summed. Completeness of all inherited analytic
allowances is explicitly not inferred from this finite arithmetic audit.
"""
import sys
if not __debug__:raise SystemExit('Assertions required')
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import hashlib,json
W=Path(__file__).resolve().parent
A=W.parent/'binding-model-review-2026-10-23'
OURS=W.parent.parent/'outputs/Objekt-X-Modellanschluss-2026-10-22'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_bytes())
old_manifest=read(OURS/'MANIFEST.json')
for n,h in old_manifest.items():assert sha(OURS/n)==h,n
fresh={}
for d,n in [('fresh-sources','fixed-combination-source-check.json'),('fresh-identity','model-identity-audit.json'),('fresh-moment','core-moment-diagnostic.json')]:
    x=read(W/d/n);y=read(A/'Ergebnisse'/n)
    x.pop('seconds',None);y.pop('seconds',None);assert x==y,n
    fresh[n]={'mathematical_fields_exactly_reproduced':True,'received_sha256':sha(A/'Ergebnisse'/n),'fresh_sha256':sha(W/d/n)}
src=read(W/'fresh-sources/fixed-combination-source-check.json')
sumsq=F(0)
for row in src['rows']:
    a,b=map(F,row['actual_corrected_model']);c,d=map(F,row['bound_reference_model']);lo,hi=map(F,row['difference'])
    assert lo<=a-d and b-c<=hi
    sumsq+=max(abs(lo),abs(hi))**2
N=F(src['full_coordinate_difference_norm_upper'][1]);cap=F(src['inherited_low_source_error_cap'][0])
assert sumsq<=N*N and N<F('1.032e-30')<cap
diag=read(W/'fresh-moment/core-moment-diagnostic.json')
old=read(OURS/'evidence/component-rebuild.json');ownround=read(OURS/'evidence/rounding-result.json')
ownaudit=read(OURS/'evidence/audit-result.json')
upper=lambda pair:F(pair[1])
delta=F(18219,10000);inverse_density_conversion=F(21,10)
assert inverse_density_conversion**2>F(21,5)
# Two estimates for one cause are alternatives, not separate charges.
wL=max(upper(diag['conditional_whole_w_rounding_Ldual_upper']),upper(ownround['bounds']['rounding_Ldual_price']))
wX=inverse_density_conversion*wL
highX=max(inverse_density_conversion*upper(diag['conditional_raw_high_lift_Ldual_upper']),
          100*upper(old['bounds']['missing_post_M_core_cap_if_high_vector_norm_below_1e21']))
momentX=100*upper(old['bounds']['inherited_moment_series_bound_rebuilt'])
bridgeX=upper(old['bounds']['shared_whole_correction_identification_X'])
rows={'canonical_w_and_directional_rebase':wX,'exact_high_moment_lift':highX,
      'inherited_moment_derivative_envelope_other_stages':momentX,'whole_correction_source_bridge':bridgeX}
rawrows={k:delta*v/100 for k,v in rows.items()}
total=sum(rawrows.values(),F(0));allowance=F('1e-150')
assert total<allowance
def dec(x):
    with localcontext()as c:
        c.prec=18
        return str(Decimal(x.numerator)/Decimal(x.denominator))
normed={k:{'X_equivalent_upper':str(v),'raw_source_equivalent_upper':str(rawrows[k]),'raw_display':dec(rawrows[k])}for k,v in rows.items()}
res={'status':'REPLAYS_AND_LISTED_SMALL_REMAINDER_SUM_PASS_CONDITIONAL',
 'received_archive_sha256':'a2976b68b8693cf3bb5cda068eae16b8b8d34b3f87d4125d89dd9349a7f599e6',
 'our_previous_manifest_sha256':sha(OURS/'MANIFEST.json'),'fresh_replays':fresh,
 'full_191_coordinate_norm_upper':str(N),'inherited_low_source_cap_lower':str(cap),
 'coordinate_hull_to_cap_ratio_upper':str(N/cap),
 'alternatives_combined_by_max_not_sum':True,'raw_source_transport':'100/delta','delta':str(delta),
 'Ldual_to_X_conversion_rational_upper':'21/10','identified_remainder_rows':normed,
 'joint_raw_source_upper':str(total),'joint_raw_source_display':dec(total),
 'existing_raw_source_allowance':str(allowance),'listed_sum_inside_existing_allowance':True,
 'p_model_error_recharged':False,'quadrature_recharged':False,
 'all_small_remainders_completeness_proved':False,
 'inherited_moment_derivative_amplification_1e40_still_conditional':True,
 'full_analytic_acceptance':False,'external_review':'OPEN'}
(W/'reconciliation-result.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':res['status'],'three_fresh_replays_match':True,'191_norm_upper':dec(N),'norm_to_cap_ratio':dec(N/cap),'joint_raw_source_upper':dec(total),'completeness_remains_open':True},indent=2))
