"""Independent series controls for the complete Cauchy primitives."""
from pathlib import Path
import argparse,json,sys
from fractions import Fraction as F
HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=HERE.parents[1]);ap.add_argument('--out',type=Path,required=True);x=ap.parse_args()
sys.path[:0]=[str(x.root/'work/compute-deps'),str(x.root/'work/tail-probe-2026-10-10/vendor'),str(x.root/'work/galerkin84-2026-10-10')]
from flint import arb,acb,ctx
from cauchy_transform import cauchy_moments,integer_powers
from safe_serial import serial
ctx.prec=1024
count=0;worst=arb(0)
harm=[F(0)]
for j in range(1,802):harm.append(harm[-1]+F(1,j))
for s in [arb(2),arb(-2),arb(3)/2,arb(-3)/2]:
    for root in [None,arb(0),arb(1)]:
        seq=cauchy_moments(s,arb(0),arb(1),32,root)
        for n in [0,1,2,9,17,32]:
            # Uniformly convergent geometric kernel expansion. Its omitted
            # part is bounded using |integral t^k log(t or 1-t)|<=1.
            exact=F(0);sp=F(2 if s>0 else -2) if s in [arb(2),arb(-2)] else (F(3,2) if s>0 else F(-3,2))
            for k in range(768):
                degree=n+k
                moment=F(1,degree+1) if root is None else -F(1,(degree+1)**2) if root==arb(0) else -harm[degree+1]/ (degree+1)
                exact+=moment/sp**(k+1)
            remainder=abs(sp)**(-769)/(1-1/abs(sp))
            ref=arb(exact.numerator)/exact.denominator+arb(0,(arb(remainder.numerator)/remainder.denominator).upper())
            assert seq[n].overlaps(ref),(s,root,n,seq[n],ref)
            diff=abs(seq[n]-ref).upper();worst=max(worst,diff);count+=1
zero=cauchy_moments(arb(2),arb(0),arb(1),0,arb(0))[0]
assert (zero+acb(arb(1)/2).polylog(2).real).contains(0)
right=cauchy_moments(arb(2),arb(0),arb(1),0,arb(1))[0]
assert (right+arb.pi()**2/12).contains(0)
# Cell additivity checks exterior roots and endpoints beyond [-1,1].
for s in [arb(2),arb(-2)]:
    for root in [None,arb(-1),arb(1),arb(3)]:
        whole=cauchy_moments(s,arb(0),arb(1),32,root)
        left=cauchy_moments(s,arb(0),arb(1)/3,32,root)
        right=cauchy_moments(s,arb(1)/3,arb(1),32,root)
        for i in range(33):assert (whole[i]-left[i]-right[i]).contains(0);count+=1
# An intentionally reversed primitive sign must be rejected by a reference.
assert not (-zero+acb(arb(1)/2).polylog(2).real).contains(0)
for s in [arb(2).sqrt(),-arb(2).sqrt()]:
    for root in [arb(0),arb(1)]:
        value=cauchy_moments(s,arb(0),arb(1),0,root)[0]
        want=-acb(1/s).polylog(2).real if root==arb(0) else acb(-1/(s-1)).polylog(2).real
        assert value.is_finite() and (value-want).contains(0)
        count+=1
for v in integer_powers(arb(0,arb('1e-100')),32):
    assert v.is_finite()
    count+=1
out={'status':'PASS_COMPLETE_CAUCHY_PRIMITIVES','independent_series_checks':72,'total_checks':count+3,
 'series_reference_maximum_width_or_difference':worst,'deliberate_sign_error_rejected':True,
 'global_model_Gram_computed':False,'global_model_error_certified':False}
x.out.write_text(json.dumps(serial(out,80),indent=2)+'\n')
print('PASS',count+3,'complete-Cauchy controls, including rejected sign error')
