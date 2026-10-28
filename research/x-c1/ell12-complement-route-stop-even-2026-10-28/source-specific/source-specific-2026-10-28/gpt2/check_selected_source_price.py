"""Independent exact data-only check of GPT1's ONE selected source price.
No integration, inverse answer construction, direction change or old replay.
The lower bound here is on a proposed UPPER PRICE, not on inverse energy.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,sys
if sys.flags.optimize:raise SystemExit('OPTIMIZED_PYTHON_REJECTED')
sys.set_int_max_str_digits(0)
R=Path(__file__).resolve().parents[2];H=Path(__file__).resolve().parent
paths={
 'old_U8_bound':R/'full-energy-execution-2026-10-27/ENERGY_BRIDGE_RATIONAL.json',
 'coupling_decision':R/'joint-energy-2026-10-28/gpt1-metric/COUPLING_ONLY_DECISION_RATIONAL.json',
 'inverse_data':R/'full-energy-execution-2026-10-27/inputs/INVERSE_DATA.json'}
j={k:json.loads(p.read_bytes())for k,p in paths.items()};checks=[]
def need(v,s):
 if not v:raise ValueError(s)
 checks.append(s)
u8=F(j['old_U8_bound']['exact']['U8_lower']);K=F(j['coupling_decision']['simplified_coupling_energy_lower']);theta=F(j['inverse_data']['theta_exact']);Dhi=F(j['coupling_decision']['direct_form_upper'])
X0=F(18,25);z0=F(20738,10000);theta_cap=F(1,400);cut=F(9,2);ecap=F(107,1000)
need(u8>X0,'Accepted U8 energy lower exceeds 18/25; X>=U8 by pure-core variational restriction')
need(K>z0*z0,'Accepted complete coupling energy gives norm strictly above 20738/10000')
need(0<=theta<theta_cap<1,'Inherited exact theta lies below 1/400')
need(theta_cap*cut==F(9,800),'For X<9/2, theta X<9/800')
need(F(9,800)<ecap*ecap,'107/1000 strictly majorizes the possible rest norm in the small-X case')
need(z0>ecap,'Reverse triangle lower is positive')
small=X0+(z0-ecap)**2
need(small==F(28676889,6250000),'Small-X source price lower equals 28676889/6250000')
need(small>cut,'Small-X case also exceeds 9/2')
need(cut>Dhi,'Every case yields source upper price above the direct upper bound')
# The denominator 1-theta is <=1, so omitting it in this LOWER bound
# for the selected upper price is conservative.
out={'status':'PASS_SELECTED_SOURCE_UPPER_PRICE_CANNOT_CERTIFY_POSITIVE_RESERVE',
 'selected_price':'A=X+(r12-eB)^T Cg_inverse (r12-eB)/(1-theta)',
 'source':'same Z ell12; g9=J*Z ell12, X=<g9,Qold(Knew)^-1 g9>',
 'assumptions_used':['X>=U8[g8] from restriction to pure-core variational tests','||eB||_Cg_inverse^2<=theta X from inherited v2 residual dual bound','A bounds actual inverse energy from above; a lower bound on A does NOT bound actual inverse energy from below'],
 'case_split_at_X':str(cut),'core_lower_used':str(X0),'coupling_norm_lower_used':str(z0),'theta_upper_used':str(theta_cap),'rest_norm_upper_if_small_X':str(ecap),
 'small_X_price_strict_lower':str(small),'universal_selected_price_lower':str(cut),'direct_form_upper':str(Dhi),'selected_price_gap_above_Dhi':str(cut-Dhi),
 'same_price_failure_only':True,'actual_inverse_energy_lower_claimed':False,'actual_Schur_sign_claimed':False,'new_quadrature':False,'new_inverse_response':False,'frozen_previous_result_changed':False,
 'checks_passed':checks,'input_hashes':{k:{'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for k,p in paths.items()}}
(H/'SELECTED_SOURCE_PRICE_RECHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status']);print('price >=',cut,'> Dhi; gap =',cut-Dhi,'~',float(cut-Dhi));print('checks',len(checks))
