"""Exact rational rounding of the saved directed all-parity reserves."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json

here=Path(__file__).resolve().parent
raw=(here/'reserve_refined.json').read_bytes()
d=json.loads(raw)
assert d['both_parities_strictly_certified'] is True
assert d['full_high_physical_floor']=='2/3'
assert d['checker_sha256']==hashlib.sha256((here/'check_a8.py').read_bytes()).hexdigest()
assert d['model_sha256']==hashlib.sha256((here/'a8_model.json.gz').read_bytes()).hexdigest()
assert d['refined_tail_binding_sha256']==hashlib.sha256((here/'refined_tail.json').read_bytes()).hexdigest()
scale=10**d['scale_digits']
common=F(12,10**30)
eta=common/(common+F(23,2))
target=F(1,10**30)
out={}
for p,r in d['parities'].items():
    assert r['positive_directed_pivots']==191
    assert len(r['all_positive_pivot_intervals'])==191
    assert all(int(v[0])>0 and int(v[0])<=int(v[1]) for v in r['all_positive_pivot_intervals'])
    physical=F(int(r['full_physical_reserve'][0]),scale)
    defect=F(int(r['full_defect_reserve'][0]),scale)
    assert physical>common and defect>target
    out[p]={'all_191_saved_pivot_lower_endpoints_positive':True,
            'physical_lower_endpoint_exceeds_common_rational':True,
            'defect_lower_endpoint_exceeds_1e_minus_30':True}
assert eta==F(24,23*10**30+24) and eta>target
result={'status':'LOCAL_ALL_PARITY_RESERVE_ROUNDING_PASS',
        'physical_reserve_exact':str(common),'physical_reserve_decimal':'1.2e-29',
        'defect_reserve_from_common_physical_exact':str(eta),
        'defect_reserve_rounded_exact':str(target),'defect_reserve_decimal':'1e-30',
        'endpoint':'A8=log(8)/2','derived_chamber_scope':'1 <= A <= A8 via raw isometric compression',
        'proof_status':'AUTHOR_DERIVED_LOCAL / EXTERNAL_REVIEW_OPEN',
        'repository_status_promotion':False,
        'reserve_results_sha256':hashlib.sha256(raw).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'parities':out}
(here/'common_reserve.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
