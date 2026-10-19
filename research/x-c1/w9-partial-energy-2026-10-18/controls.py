"""Independent analytic controls for the newly used Gamma function models."""
import json
from fractions import Fraction
from math import factorial
from flint import arb,arb_poly,fmpq_mat,ctx
from common import Inputs,q,need,encode,HERE
from residuals import Residuals
from old_fields import kernel,gamma_coefficients
from weights import gamma_error


def run():
    ctx.prec=800;inp=Inputs();report={}
    theta=lambda v:(-v/2).exp().atanh()+(-v/2).exp().atan()
    for par in ('even','odd'):
        p=int(par=='odd')
        sq=inp.json('half')['blocks'][p]['half_inverse_centre_rational_Q_coefficients']
        dq=inp.json('basis_'+par)['D_rational']
        S=fmpq_mat(sq);Z=fmpq_mat([[dq[i][j]if i<8 else int(i-8==j)for j in range(84)]for i in range(92)])
        exact_constraints=S.transpose()*Z
        need(all(exact_constraints[i,j]==0 for i in range(8)for j in range(84)),
             'Exact rational old T constraints')
        r=Residuals(inp,par);eps=gamma_error(360,q('6/5'));differences=[]
        for t in (r.a/7,r.a/2,6*r.a/7):
            e=r.ell[0].p[0]
            g=(e*((r.b-t)/(r.a-t)).log()+r.eps*e*((r.b+t)/(r.a+t)).log())/2+r.gamma[0](t)
            exact=e*(theta(r.a-t)-theta(r.b-t)+r.eps*(theta(r.a+t)-theta(r.b+t)))
            difference=g-exact
            need(abs(difference)<2*(r.b-r.a)*abs(e)*eps,'Constant shell Gamma primitive')
            differences.append(difference)
        report[par]={'exact_rational_T_constraint_zeros':672,
                     'constant_shell_primitive_differences':differences}
    a=3*arb(2).log()/2
    saved=list(map(q,inp.json('a8_model')['Gamma_polynomial_coefficients']))
    reference=gamma_coefficients(160)
    need(len(saved)==161 and all(x.overlaps(y)for x,y in zip(saved,reference)),'Old Taylor coefficient identity')
    inverse_cosh=[Fraction(1)];inverse_sinhc=[Fraction(1)]
    for n in range(1,162):
        inverse_cosh.append(-sum((inverse_cosh[n-j]/factorial(j)for j in range(2,n+1,2)),Fraction(0)))
        inverse_sinhc.append(-sum((inverse_sinhc[n-j]/factorial(j+1)for j in range(2,n+1,2)),Fraction(0)))
    exact=[(inverse_cosh[k]+inverse_sinhc[k+1])/4 for k in range(161)]
    need([Fraction(v)for v in inp.json('a8_model')['Gamma_polynomial_coefficients']]==exact,
         'Exact rational old Taylor coefficients')
    f=arb_poly([1]);k=kernel(f,[arb(1)],a,reference,0);err=gamma_error(160,q('21/20'))
    differences=[]
    for t in (arb(0),q('1/3'),q('9/10')):
        exact=2*(arb(2).log()+arb.pi()/4)-theta(a*(1-t))-theta(a*(1+t))-((a*(1-t))*(a*(1+t))).log()/2
        need(abs(k(t)-exact)<2*a*err,'Constant complete core Gamma primitive')
        differences.append(k(t)-exact)
    report['old_core']={'constant_core_primitive_differences':differences,'old_coefficient_identities':161,
                        'old_coefficient_exact_rational_identities':161}
    return report


if __name__=='__main__':
    (HERE/'CONTROLS.json').write_text(json.dumps(encode(run()),indent=2)+'\n')
    print('PASS: six new-shell and three complete-core analytic primitive controls; 161 old coefficients')
