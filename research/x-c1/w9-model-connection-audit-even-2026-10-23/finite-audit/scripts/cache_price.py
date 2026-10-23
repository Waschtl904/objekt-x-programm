"""Rational transport of complete atom differences; no overlap-as-equality."""
import sys
if not __debug__:raise SystemExit('Optimized Python is rejected')
import argparse,json
from fractions import Fraction as F
from decimal import Decimal,localcontext
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--audit',type=Path,required=True);ap.add_argument('--rebuild',type=Path,required=True);ap.add_argument('--joint',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
j=json.loads(a.audit.read_bytes());rebuild=json.loads(a.rebuild.read_bytes());joint=json.loads(a.joint.read_bytes())
assert j['atoms']==5120 and all(rebuild['components_exact'].values())
g=F('1e-16');assert min(F(r['distance_to_outer_shell'][0]) for r in j['panels'])>g
D=F(j['max_node_difference'][1]);W=F(j['sum_weight_differences'][1])
def price(d,w):
 # sqrt(2(b-a))<1, delta>1, a>1, mu>1; TV<1.
 # |Gamma_model|<2, |d_y K_Gamma|<1e6;
 # Qm on each continued prime cell: |Qm|<1e9, |Qm'|<2e25.
 return (w/g+d/g**2)+(4*w+10**6*d)+200*w+2*(2*w+d+10**9*w+2*10**25*d)
P=price(D,W);assert P<F('1e-886')
total=F(joint['joint_raw_source_upper'])+F(18219,10000)*P/100
assert total<F('7.729e-239')<F('1e-150')
controls=[]
for name,d,w in [('node_displacement',F('1e-15'),W),('weight_displacement',D,F('1e-20'))]:
 assert not price(d,w)<F('1e-886');controls.append(name)
def dec(x):
 with localcontext()as c:c.prec=18;return str(Decimal(x.numerator)/Decimal(x.denominator))
out={'scope':'rounding of the finite 128/64 core measure only','complete_difference_X_upper':str(P),'complete_difference_X_display':dec(P),'new_joint_raw_equivalent_upper':str(total),'new_joint_raw_display':dec(total),'checked_gauss_atoms':5120,'five_cache_components_exact':True,'noncontainment_counts':{'nodes':5120-j['node_enclosures_contain_recomputation'],'weights':5120-j['weight_enclosures_contain_recomputation']},'negative_controls':controls,'reserve_1e150_respected':True,'analytic_contour_lemmas_reproved_by_this_arithmetic':False,'physical_source_error_reproved':False}
a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['complete_difference_X_display','new_joint_raw_display','noncontainment_counts','negative_controls']},indent=2))
