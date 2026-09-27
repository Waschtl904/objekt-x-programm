"""Exact constants for a sharper complete physical tail floor at A <= A8."""
from fractions import Fraction as F
from math import factorial,isqrt
from pathlib import Path
import json,hashlib
from rational_bounds import log_bounds,cosh_upper,decimal_display


def main():
    checks=[]
    def check(name,truth):
        if not truth:raise AssertionError(name)
        checks.append(name)
    r=F(26,25)
    check('A8 < 26/25',log_bounds(8)[1]/2<r)
    # S(z)=sinh(z)/z; (S(z)-1)/z^2 has nonnegative coefficients.
    n=20
    b=sum((r**(2*k)/factorial(2*k+3) for k in range(n+1)),F(0))
    tail=r**(2*n+2)/factorial(2*n+5)/(1-r*r/((2*n+6)*(2*n+7)))
    b+=tail
    lower=(1/cosh_upper(r)-r*b/(1+r*r/6))/4
    check('z/(1+z^2/6) increasing through radius',r*r<6)
    check('regular Gamma kernel >= 59/500',lower>F(59,500))
    h8192=sum((F(1,k) for k in range(1,8193)),F(0))
    check('Euler gamma < 5773/10000',h8192-13*log_bounds(2)[0]<F(5773,10000))
    check('new q0 loss < 491/200',log_bounds(2*F(22,7)*r)[1]+F(5773,10000)<F(491,200))
    def sqrt_lower(q):
        grid=10**10
        return F(isqrt(q*grid*grid),grid)
    shift=log_bounds(2)[1]
    for q,p in [(3,3),(4,2),(5,5),(7,7)]:
        shift+=log_bounds(p)[1]/sqrt_lower(q)
    check('new full shift bound < 313/100',shift<F(313,100))
    H384=sum((F(1,k) for k in range(1,385)),F(0))
    check('H384 > 6529/1000',H384>F(6529,1000))
    gamma_loss=2*r*(F(1,4)-F(59,500))
    raw=F(6529,1000)-F(491,200)-gamma_loss-F(313,100)
    ep=F(1,10**6)
    check('moment-corrected whole high floor > 2/3',raw-16*ep-12*ep*ep>F(2,3)*(1+ep*ep))
    # Original mixed and moment-carrier bounds 8 and 12 remain valid.
    check('mixed factor still < 8',4+r/2+F(313,100)<8)
    check('carrier factor still < 12',1+4+F(491,200)+r/2+F(313,100)<12)
    check('new high T reserve 4/73',F(2,3)/(F(2,3)+F(23,2))==F(4,73))
    result={'status':'EXACT_CONSTANTS_PASS_ANALYTIC_REVIEW_OPEN','scope':'1 <= A <= A8',
            'high_physical_floor':'2/3','high_T_defect_floor':'4/73','radius':'26/25',
            'regular_kernel_floor':'59/500','q0_loss_upper':'491/200','shift_norm_upper':'313/100',
            'raw_high_floor':str(raw),'raw_high_floor_display':decimal_display(raw),
            'Gamma_high_loss':str(gamma_loss),'moment_error_bound_used':'1/1000000',
            'checks':checks,'check_count':len(checks),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (Path(__file__).parent/'refined_tail.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
