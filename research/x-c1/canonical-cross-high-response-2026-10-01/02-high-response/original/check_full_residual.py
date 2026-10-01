"""Compare complete response integrals with the independently assembled old Gram."""
from pathlib import Path
import argparse,sys
from flint import arb,acb,acb_mat,ctx
from high_common import *
from full_residual import norm_certificates
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);args=p.parse_args()
engine=args.repo/'research/x-c1/chambers-through-a11-2026-09-28/a11'
sys.path.insert(0,str(engine));import generate_a11 as reference
ctx.prec=512;model=reference.compute(N=15,M=16,precision=512)
a=arb(11).log()/2;w=acb_mat(16,1);w[3,0]=arb(7).sqrt();w[1,0]=-arb(7).sqrt()*moment(a,3)/moment(a,1)
q=finite_action(w,model['Gamma_polynomial_coefficients'],a,'A11',list(range(1,16,2)))
r=norm_certificates(w,acb_mat(16,1),[acb(0)],model['Gamma_polynomial_coefficients'],a,'A11',subtract_normal=False)[0]
raw=ball(r['raw_model_residual_norm_squared']);tail=raw-normsq(q,0)
expected=mat(model['parities']['odd']['complete_model_raw_high_Gram'],10**100)[0,0]
assert tail.overlaps(expected),(tail,expected)
assert tail>0
projected=norm_certificates(w,acb_mat(16,1),[acb(0)],model['Gamma_polynomial_coefficients'],a,'A11')[0]
assert projected['all_high_modes_included']
# A finite-only check would incorrectly omit this strictly positive tail.
print('PASS: complete function integration minus finite coefficients matches full Parseval Gram')
ctx.prec=3072
a=arb(11).log()/2;z=a/2
assert moment(a,1).overlaps((z*z.cosh()-z.sinh())/(z*z))
assert moment(a,1).rad()<rat('1e-850')
print('PASS: full-integral Mellin normalization has a paid Taylor remainder below arithmetic needs')
