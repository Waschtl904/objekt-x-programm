"""Portable exact-rational cross audit. Python standard library only.
This checks exported enclosures and accounting, not the inherited analytic lemmas.
"""
if not __debug__:
 raise SystemExit('Verification requires assertions enabled; Python -O/-OO is rejected.')
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
from zipfile import ZipFile
import json,hashlib
HERE=Path(__file__).resolve().parent;DATA=HERE/'inputs'
def read(name):return json.loads((DATA/name).read_bytes())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def upper(pair):
 assert len(pair)==2 and Q(pair[0])<=Q(pair[1]);return Q(pair[1])
def sqrtup(value):
 value=Q(value);assert value>=0;grid=10**150
 target=value*grid*grid;n=isqrt(target.numerator//target.denominator)
 if n*n<target:n+=1
 result=Q(n,grid);assert result*result>=value;return result

# First bind the supplied archive and its contents; no archive instructions run.
archive=DATA/'GPT1-original.zip'
assert sha(archive)=='ead31d679ac0cf0af29ade85545581ced9e4a3cdd129aabeb8dd9c2afabc8ce1'
with ZipFile(archive) as z:
 manifest=json.loads(z.read('SHA256SUMS.json'))
 assert len(manifest)==24
 for name,want in manifest.items():assert hashlib.sha256(z.read(name)).hexdigest()==want,name
 prefix='connection-audit/fixed-source-investigation/'
 for original,copy in [('kernel-correction.json','GPT1-kernel-correction.json'),('corrected-low-source-check.json','GPT1-low-source-check.json'),('correction-outer-check.json','GPT1-outer-check.json'),('correction-function-exact.json.gz','GPT1-correction.json.gz')]:
  assert z.read(prefix+original)==(DATA/copy).read_bytes()
assert sha(DATA/'whole_function_probe.py')=='ed58da3caacd5ca39de1f910c77920e7079eec905a560b487600c71e97c8df64'
wr=read('WHOLE_RESULT.json')
for name in ['whole-error-ledger.json','analytic-caps.json','core-model-bridge.json','core-quadrature-control-128.json']:
 assert sha(DATA/name)==wr['input_receipts'][name]

theirs=read('GPT1-kernel-correction.json')['rows'];own=read('kernel-orientation-81.json')['rows']
assert len(theirs)==len(own)==84
gaps=[]
for t,o in zip(theirs,own):
 assert t['coordinate']==o['coordinate']
 a,b=map(Q,t['signed_corrected_minus_original_pairing']);c,d=map(Q,o['orientation_correction'])
 assert max(a,c)<=min(b,d)
 gaps.append(abs((a+b-c-d)/2))
assert max(gaps)==0
low=read('GPT1-low-source-check.json')['rows'];assert len(low)==191
assert all(Q(r['difference'][0])<=0<=Q(r['difference'][1])for r in low)

# Stronger coordinate acceptance: the entire arithmetic difference hull must
# fit inside the justified uncertainty, not merely overlap zero after padding.
local=read('localized-81.json')['rows'];core=read('core-tail.json')['rows']
assert len(local)==len(core)==84
margins=[];maxhull=Q(0)
for l,o,h in zip(local,own,core):
 assert l['coordinate']==o['coordinate']==h['coordinate']
 p0,p1=map(Q,l['partial_pairing']);n0,n1=map(Q,l['expanded_model'])
 d0,d1=map(Q,o['orientation_correction']);t0,t1=map(Q,h['signed_core_tail_correction'])
 lo=p0-n1+d0+t0;hi=p1-n0+d1+t1
 error=upper(l['integration_error'])+upper(h['remaining_core_error'])
 assert -error<=lo<=hi<=error
 margins.append(error-max(abs(lo),abs(hi)))
 f0,f1=map(Q,h['final_difference']);assert f0<=0<=f1
 maxhull=max(maxhull,abs(f0),abs(f1))
assert maxhull<Q('6.724e-14')

# Independently repeat final arithmetic from the new norm-square enclosure.
norm=json.loads((HERE/'independent-norm.json').read_bytes())
for key,name in [('original_model_cache','original-model.json.gz'),('own_correction_cache','own-correction.json.gz'),('GPT1_correction_cache','GPT1-correction.json.gz')]:
 assert norm['inputs'][key]==sha(DATA/name)
change=sqrtup(upper(norm['norm_squared_intermediate']))
change+=upper(norm['smooth_log_remainder_X'])+upper(norm['moment_Taylor_remainder_X'])
assert change<Q('3.653e-7')
assert upper(norm['whole_representation_difference_X_upper'])<Q('1e-300')

# Transfer check for the one model-function cap potentially affected by v.
controls=read('analytic-caps.json');val=read('orientation-validation.json')
du=sqrtup(upper(val['bounds']['du_X_norm_squared']))
corrected_u=upper(controls['values']['u_H8_bound'])+du
assert corrected_u<Q('1e20')
assert upper(controls['values']['raw_g_X_operator'])<100
assert Q(wr['core_bridge_X_error_upper'])==upper(read('core-model-bridge.json')['full_X_difference_bound'])
assert Q(wr['core_quadrature_X_error_upper'])==upper(read('core-quadrature-control-128.json')['total_outer_X_error_upper_expression'])

# p and low-feature errors are transported once, together, as in the frozen
# ledger. Rebuild the sum instead of accepting its previously reported total.
ledger=read('whole-error-ledger.json')['values'];sqrtL=sqrtup(Q(5,21))
operator_price=10*(upper(ledger['p_total'])+upper(ledger['low_feature_total']))+sqrtL*upper(ledger['raw_X_error'])
stored_operator_price=Q(wr['whole_operator_model_Ldual_error_upper'])
assert Q(ledger['proposed_Ldual_error'][0])<=operator_price<=stored_operator_price
# Keep the frozen upper endpoint, including its original outward rounding.
# The rational reconstruction confirms that it covers the ledger sum.
normup=sqrtL*(sqrtup(Q(wr['model_X_norm_squared_upper']))+change+Q(wr['core_bridge_X_error_upper'])+Q(wr['core_quadrature_X_error_upper']))+stored_operator_price
energy=normup*normup;assert energy<Q('4.632e-11')<Q('1e-9')
finite=read('FINITE_RESULT.json');beta=Q(finite['beta']);cc=Q(finite['c'])
assert beta>0 and 0<cc<1
fcap=Q(finite['F_upper_cap']);zcap=Q(finite['residual_P_norm_cap']);dcap=Q('1e-9')
assert upper(finite['F_interval'])<fcap and upper(finite['finite_bounds']['residual_P_norm'])<zcap
full=fcap+(dcap/beta+zcap*zcap+2*zcap*sqrtup(cc*dcap/beta))/(1-cc)
budget=Q(finite['budget_interval'][0]);assert full<budget
out={'status':'CROSS_CHECK_PASS_CONDITIONAL_ON_INHERITED_ANALYTIC_MODEL_AND_ERROR_LEMMAS',
 'archive_hashes_verified':24,'signed_corrections_matching':84,'maximum_exported_midpoint_gap':str(max(gaps)),
 'first_direction_source_interval_endpoints_rechecked':191,'first_direction_source_integrals_recomputed_in_this_review':False,
 'whole_arithmetic_hulls_inside_justified_error':84,'minimum_hull_coverage_margin':str(min(margins)),
 'maximum_final_coordinate_hull':str(maxhull),'correction_X_upper':str(change),
 'corrected_inner_model_norm_upper':str(corrected_u),'retained_inner_model_norm_cap':'1e20',
 'operator_price_rebuilt_with_p_once':str(operator_price),'retained_operator_price':str(stored_operator_price),
 'repaired_Ldual_energy_upper':str(energy),
 'conservative_energy_cap':str(dcap),'full_comparison_energy_upper':str(full),
 'budget_lower':str(budget),'comparison_margin':str(budget-full),
 'complete_model_identification_independently_accepted':False,'all_inherited_analytic_lemmas_reproved':False,
 'p_error_recharged':False,'inner_quadrature_tail_charged_twice':False,
 'inputs':{p.name:sha(p)for p in sorted(DATA.iterdir())if p.is_file()},
 'new_norm_result_sha256':sha(HERE/'independent-norm.json')}
(HERE/'cross-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for key in ['status','archive_hashes_verified','signed_corrections_matching','whole_arithmetic_hulls_inside_justified_error']:
 print(key,out[key])
for key in ['correction_X_upper','repaired_Ldual_energy_upper','maximum_final_coordinate_hull','comparison_margin']:
 print(key,float(Q(out[key])))
