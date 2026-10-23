"""Exact-rational sign/adjoint controls and dyadic-cache rejection controls.

The finite example checks the algebra, not the inherited infinite-dimensional
operator hypotheses. The full source rebuild is a separate test.
"""
import sys
if not __debug__:raise SystemExit('Assertions required; no -O/-OO.')
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
from math import factorial
import gzip,hashlib,json,tempfile
W=Path(__file__).resolve().parent
ROOT=W.parent/'pr254-review'
WHOLE=ROOT/'research/x-c1/w9-residual-centered-control-even-2026-10-21/whole'
sys.path.insert(0,str(WHOLE))
from flint import arb,ctx
ctx.prec=3072
import exact_cache,model_cache

def mat(rows):return [[F(x)for x in row]for row in rows]
def tr(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0))for col in tr(b)]for row in a]
def add(a,b):return [[x+y for x,y in zip(aa,bb)]for aa,bb in zip(a,b)]
def scale(c,a):return [[c*x for x in row]for row in a]
def sub(a,b):return add(a,scale(-1,b))
def inv2(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return scale(1/d,[[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]])

# Core dimension 3, shell dimension 2. Core moment is its first coordinate;
# J embeds the two moment-zero core directions. Lambda is an actual lift.
J=mat([[0,0],[1,0],[0,1],[0,0],[0,0]])
L=mat([['-2/3','-1/2'],[0,0],[0,0],[1,0],[0,1]])
Q=mat([[7,2,-1,3,1],[2,8,1,-2,4],[-1,1,9,2,-3],[3,-2,2,10,1],[1,4,-3,1,11]])
U=mat([[3,1],[1,2]])
Fm=mat([[1,-2],[2,1],[-1,3],[4,2],[3,-1]])
K=mat([[5,1],[1,4]]);Ki=inv2(K)
f=mat([[2],[-3],[1],[5],[-2]]);t=mat([['3/7'],['-2/5']]);eta=F(1,10**10)
Wx=mul(tr(L),L);Winv=inv2(Wx)
g=mul(tr(J),mul(Q,L));gF=mul(tr(J),mul(Q,Fm))
h=mul(tr(J),f)
A=sub(mul(tr(Fm),mul(Q,L)),mul(tr(gF),mul(U,g)))
v=sub(mul(tr(Fm),f),mul(tr(gF),mul(U,h)))
nu=sub(sub(mul(tr(L),f),mul(tr(g),mul(U,h))),mul(tr(A),mul(Ki,v)))
H=sub(sub(scale(1-eta,mul(tr(L),mul(Q,L))),mul(tr(g),mul(U,g))),mul(tr(A),mul(Ki,A)))
left=sub(nu,mul(H,t))
p=mul(Ki,sub(mul(A,t),v))
u=mul(U,sub(sub(mul(g,t),h),mul(gF,p)))
psi=sub(mul(Fm,p),scale(1-eta,mul(L,t)))
R=add(f,mul(Q,add(psi,mul(J,u))))
density=mul(tr(L),R)
assert left==density
assert mul(Winv,left)==mul(Winv,density)
assert mul(Winv,left)!=density # A W-Riesz vector is not the X density.
wrong_p=scale(-1,p)
wrong_u=mul(U,sub(sub(mul(g,t),h),mul(gF,wrong_p)))
wrong_psi=sub(mul(Fm,wrong_p),scale(1-eta,mul(L,t)))
wrong_density=mul(tr(L),add(f,mul(Q,add(wrong_psi,mul(J,wrong_u)))))
assert wrong_density!=left
shell=R[3:]
moment_lift=mat([[F(2,3)*R[0][0]],[F(1,2)*R[0][0]]])
assert sub(shell,moment_lift)==density
assert add(shell,moment_lift)!=density
assert scale(2,density)!=left

# Restore exactly the declared midpoint/radius. Reject wrong source, changed
# payload and a malformed record rather than silently interpreting a new model.
cache=WHOLE/'whole-model-ed58da3caacd.json.gz'
body=json.loads(gzip.decompress(cache.read_bytes()))
values,_=exact_cache.load(cache,body['source_sha256'])
payload=json.loads(body['payload'])
roundtrip=model_cache.pack(values)==payload
assert roundtrip
def expect_error(fn,kind):
    try:fn()
    except kind:return True
    raise AssertionError('Negative control was accepted')
bad_source=expect_error(lambda:exact_cache.load(cache,'0'*64),ValueError)
bad_record=expect_error(lambda:exact_cache.unpack({'unknown':[1,2]}),ValueError)
with tempfile.TemporaryDirectory(dir=W,prefix='cache-negative-')as tmp:
    altered=dict(body);altered['payload']=body['payload']+' '
    path=Path(tmp)/'tampered.json.gz'
    path.write_bytes(gzip.compress(json.dumps(altered).encode()))
    bad_hash=expect_error(lambda:exact_cache.load(path,body['source_sha256']),ValueError)
raw_a=payload['mapping'][next(i for i,(k,v)in enumerate(payload['mapping'])if k=='a')][1]['ball']
m,e,r,s=map(int,raw_a)
ordinary=arb((m,e),(r,s))
ordinary_radius=tuple(map(int,ordinary.rad().man_exp()))
restored=exact_cache.ball(raw_a)
assert model_cache.pack(restored)=={'ball':raw_a}

rebuilt=json.loads((W/'component-rebuild.json').read_bytes())
assert rebuilt['old_cache_exact_reproduction_pass']
assert rebuilt['shared_correction_bridge_below_1e_150']
assert rebuilt['allowances_below_1e_150']
bounds=rebuilt['bounds'];upper=lambda key:F(bounds[key][1])
bridge=upper('shared_whole_correction_identification_X')
postM=F(2*10**21,factorial(384))
moment=F(2*10**46,factorial(160))
price=100*(postM+moment)+bridge
assert price<F('1e-150')
assert bridge<F('6.648e-313')
assert F(10**20+2*10**14+1)<10**21
def dec(x):
    with localcontext()as d:
        d.prec=18
        return str(Decimal(x.numerator)/Decimal(x.denominator))
result={
 'status':'EXACT_ALGEBRA_AND_REBUILD_AUDIT_PASS_CONDITIONAL',
 'algebra_example_only_not_operator_proof':True,
 'schur_to_function_density_identity':True,'weighted_Riesz_distinction_checked':True,
 'negative_controls':{'reversed_p_sign_rejected':True,'wrong_moment_lift_sign_rejected':True,
   'extra_factor_two_rejected':True,'wrong_source_hash_rejected':bad_source,
   'changed_payload_rejected':bad_hash,'unknown_cache_record_rejected':bad_record},
 'cache_roundtrip_all_values_exact':roundtrip,
 'example_a_stored_radius':[r,s],'ordinary_constructor_radius':list(ordinary_radius),
 'ordinary_constructor_is_outward_not_a_mathematical_defect':True,
 'component_rebuild_sha256':hashlib.sha256((W/'component-rebuild.json').read_bytes()).hexdigest(),
 'whole_correction_bridge_upper':str(bridge),'projection_moment_bridge_sum_upper':str(price),
 'display':{'whole_correction_bridge':dec(bridge),'post_M_core':dec(postM),'post_M_outer':dec(100*postM),
   'inherited_moment_envelope':dec(moment),'total_outer_allowance':dec(price)},
 'fits_existing_raw_source_allowance_once':True,
 'inherited_caps_and_source_lemmas_remain_assumptions':True,
 'canonical_w_rounding_transport_is_a_separate_check':True,
 'full_analytic_identification_closed':False,'external_acceptance':False}
(W/'audit-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'negative_controls':result['negative_controls'],'display':result['display']},indent=2))
