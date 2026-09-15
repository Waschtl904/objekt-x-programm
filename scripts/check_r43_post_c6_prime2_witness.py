#!/usr/bin/env python3
"""Finite checks of the post-C6 prime-2 separation witness.

NOT a P11, C6, operator-limit, positivity, or RH certificate.
Uses the actual smooth compactly supported probe, not a grid proxy.
"""
from __future__ import annotations
import argparse, json, math, platform
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import quad


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional path for the JSON result")
    args = parser.parse_args()
    checks: dict[str, float] = {}
    def exact(name: str, condition: bool) -> None:
        if not bool(condition):
            raise AssertionError(name)
        checks[name] = 0.0
    def close(name: str, actual: float, expected: float, tol: float = 1e-10) -> None:
        err = abs(actual - expected)
        if not math.isfinite(err) or err > tol:
            raise AssertionError(f'{name}: {actual} != {expected}; error={err}')
        checks[name] = err

    z, lam = sp.symbols('z lam', real=True)
    d = sp.Rational(1, 100)
    p = -lam**3 + lam/4  # Integral of e^(lam x) D(D^2-1/4) phi.
    for r in [sp.Integer(0), sp.Rational(1,2), -sp.Rational(1,2)]:
        exact(f'moment_polynomial_at_{r}', p.subs(lam,r)==0)
    # Log(1+x)>x/(1+x), checked by its nonnegative derivative.
    x=sp.symbols('x', positive=True)
    exact('log_lower_bound_derivative', sp.simplify(sp.diff(sp.log(1+x)-x/(1+x),x)-x/(1+x)**2)==0)
    exact('lower_lobe_stays_positive', d < sp.Rational(1,10))
    exact('sum_shift_avoids_log2', 2*d < sp.Rational(1,5))
    exact('sum_shift_avoids_log3', 2*d < sp.Rational(1,6))
    exact('difference_shift_avoids_zero', 2*d < sp.Rational(1,2))
    exact('difference_shift_avoids_log3', 2*d < sp.Rational(1,3))
    # log 2 < .7 since this partial exponential sum already exceeds 2.
    exact('log2_upper_bound', sum(sp.Rational(7,10)**k/sp.factorial(k) for k in range(4)) > 2)
    exact('all_sources_fit_radius_one', sp.Rational(1,8)+sp.Rational(7,10)+d < 1)
    exact('prime2_factor_evenisation', sp.simplify(-2*sp.log(2)/sp.sqrt(2)*sp.Rational(1,2)+sp.log(2)/sp.sqrt(2))==0)
    psi=sp.exp(-1/(1-z*z))
    q=sp.diff(psi,z,3)-d*d/4*sp.diff(psi,z)
    qraw=sp.lambdify(z,q,modules='numpy',cse=True)
    def qfun(s: float) -> float:
        if abs(s)>=1.0:
            return 0.0
        with np.errstate(over='ignore',under='ignore',invalid='raise'):
            return float(qraw(s))
    def integrate(fun):
        value,error=quad(fun,-1,1,epsabs=1e-10,epsrel=2e-12,limit=250)
        return value,error
    n2,nerr=integrate(lambda s:qfun(s)**2)
    exact('probe_norm_nonzero', n2>0)
    norm=math.sqrt(n2)
    delta=float(d); y=.5*math.log(5/4); ell=math.log(2)
    def h(t:float)->float:
        return qfun((t-y)/delta)/(math.sqrt(delta)*norm)
    def a(t:float)->float:
        return (h(t-ell)-h(-t-ell))/math.sqrt(2)
    def b(t:float)->float:
        return (h(t)-h(-t))/math.sqrt(2)
    def correlation(u:float)->float:
        # Integrate only the two actual b support intervals.
        result=0.0
        for center in [y,-y]:
            val,_=integrate(lambda s:delta*a(center+delta*s+u)*b(center+delta*s))
            result+=val
        return result
    hm={}
    for r in [0.0,.5,-.5]:
        value,_=integrate(lambda s:qfun(s)*math.exp(r*delta*s))
        value*=math.sqrt(delta)*math.exp(r*y)/norm
        hm[r]=value
        close(f'smooth_h_exponential_moment_{r}',value,0.0)
    close('h_L2_normalization', n2/norm**2,1.0)
    close('beta_b',2*math.sqrt(2)*(hm[0.0]-hm[-.5]),0.0)
    close('beta_a',2*math.sqrt(2)*(hm[0.0]-math.exp(-ell/2)*hm[-.5]),0.0)
    for r in [.5,-.5]:
        close(f'pole_moment_b_{r}',(hm[r]-hm[-r])/math.sqrt(2),0.0)
        close(f'pole_moment_a_{r}',(math.exp(r*ell)*hm[r]-math.exp(-r*ell)*hm[-r])/math.sqrt(2),0.0)
    close('disjoint_L2_pairing',correlation(0),0.0)
    close('correlation_plus_log2',correlation(ell),.5)
    close('correlation_minus_log2',correlation(-ell),.5)
    for n in range(3,10):
        close(f'correlation_plus_log{n}',correlation(math.log(n)),0.0)
        close(f'correlation_minus_log{n}',correlation(-math.log(n)),0.0)
    g2=.5*(correlation(ell)+correlation(-ell))
    finite=-2*math.log(2)/math.sqrt(2)*g2
    close('finite_prime_block',finite,-math.log(2)/math.sqrt(2))
    result={
        'scope':'FINITE_ALGEBRA_AND_SMOOTH_PROBE_NOT_P11_CERTIFICATE',
        'python':platform.python_version(),
        'checks':checks,'number_of_checks':len(checks),
        'max_absolute_residual':max(checks.values()),
        'probe':{'delta':delta,'y':y,'ell':ell,'sum_shift':2*y+ell,
                 'unscaled_norm_squared':n2,'norm_quadrature_error_estimate':nerr,
                 'finite_block':finite,'exact_difference':'-log(2)/sqrt(2)'},
        'nonclaims':['no negative diagonal of Weil form','no C6 verification by numerics',
                    'no universal Object-X no-go','no registry promotion']}
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
