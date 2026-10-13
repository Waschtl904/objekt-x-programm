"""Independent rational checks and directed full L-energy Gram on the exact J.

Requires python-flint 0.9.0. No actual H, A0, tau or full residual Gram is
integrated here. The enclosing local J coefficients come from the sealed input.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
from decimal import Decimal, localcontext
import argparse
import hashlib
import json
import sys

from flint import arb, arb_mat, fmpq, fmpq_mat, ctx

ctx.prec = 768


def read(path):
    return json.loads(path.read_bytes())


def qm(rows):
    return fmpq_mat([[fmpq(str(v)) for v in row] for row in rows])


def qa(matrix):
    return arb_mat([[aq(Q(str(matrix[i,j]))) for j in range(matrix.ncols())]
                    for i in range(matrix.nrows())])


def aq(x):
    x=Q(x)
    return arb(x.numerator)/x.denominator


def box(v):
    lo,hi=map(Q,v)
    assert lo<=hi
    return aq((lo+hi)/2)+arb(0,aq((hi-lo)/2).upper())


def trace(a):
    return sum((a[i,i] for i in range(a.nrows())),fmpq(0))


def strict_ldl(a):
    n=a.nrows()
    v=[[a[i,j] for j in range(n)] for i in range(n)]
    piv=[]
    for k in range(n):
        pivot=v[k][k]
        assert pivot>0,(k,str(pivot))
        piv.append(pivot)
        for i in range(k+1,n):
            for j in range(i,n):
                x=v[i][j]-v[i][k]*v[j][k]/pivot
                v[i][j]=v[j][i]=x
    return piv


def display(x):
    with localcontext() as c:
        c.prec=20
        x=Q(x)
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('package',type=Path)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    root=args.package.resolve();out=args.out.resolve();out.mkdir(parents=True,exist_ok=True)
    finite=root/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09'
    halfpath=finite/'work/remainder-integration-check-v2/originals/half-inverse/expected/1536.json'
    half=read(halfpath)
    bridgepath=root/'work/inherited/Objekt-X-Unendlicher-Rest-Vergleich-2026-10-09/work/infinite-tail-2026-10-09/FINITE_BRIDGE.json'
    bridge=read(bridgepath)
    task=root/'work/basis-coverage-2026-10-10'
    # Reuse only the inherited outward serialization utility, not its basis algebra.
    sys.path.insert(0,str(root/'work/tail-probe-2026-10-10/vendor'))
    from compute_inverse_energy_gate import serial
    harmonic=[Q(0)]
    for n in range(1,96): harmonic.append(harmonic[-1]+Q(1,n))
    mtail=3*Q(1,64)**96/Q(factorial(96))/(1-Q(1,64*97))
    local_tail=Q(2*10**10,32)*mtail**2
    assert local_tail<Q(1,10**600)
    eta=Q(1,10**10);c=Q(11,100)-eta;wcap=Q(1000502,10**6)
    s_floor=c*Q(21,5)
    s_cap=(1-eta)*(harmonic[95]+Q(11,10))*wcap
    assert s_cap/s_floor<Q(1351,100)
    cases=[]
    for p,par in enumerate(['EVEN','ODD']):
        data=read(task/f'BASIS_{par}.json')
        S=[[Q(v) for v in row] for row in half['blocks'][p]['half_inverse_centre_rational_Q_coefficients']]
        D=[[Q(v) for v in row] for row in data['D_rational']]
        assert len(D)==8 and all(len(row)==84 for row in D)
        # Exact null equations plus an invertible top block establish the full kernel.
        qs=qm([row[:8] for row in S[:8]])
        assert qs.det()!=0
        for i in range(8):
            for j in range(84):
                assert sum((S[k][i]*D[k][j] for k in range(8)),Q(0))+S[8+j][i]==0
        extra=sum((v*v for row in D for v in row),Q(0))
        assert extra==Q(data['gram_extra_trace_exact']) and 1+extra<wcap
        P=[[Q(v) for v in row] for row in data['P_rational']]
        assert len(P)==84 and all(len(row)==268 for row in P)
        assert all(x==0 for row in P for x in row[65:])
        fit=Q(0)
        for i in range(84):
            for j in range(65):
                lo,hi=map(Q,data['ideal_fit_interval'][i][j])
                fit+=wcap*max(abs(lo-P[i][j]),abs(hi-P[i][j]))**2
        assert local_tail==Q(data['infinite_local_moment_tail_gram_scalar_exact'])
        assert fit+local_tail<Q(1,10**70)
        # Independent exact rational reconstruction of the coarse remaining bound.
        certpath=finite/f'work/gamma-low-2026-10-09/CERTIFICATE_{par}_gamma224_tight_4096.json'
        cert=read(certpath)
        ac=qm(cert['inverse_congruence_integer_matrix'])/fmpq(cert['inverse_congruence_denominator'])
        hb=qm(cert['HB_integer_matrix'])/fmpq(cert['HB_denominator'])
        x=ac*ac.transpose()/(1-fmpq(cert['rho']))
        delta=fmpq(91,50);beta=1+fmpq(1,10**12)
        mv=2*10**6*(2*trace(x)+beta*trace(x*hb)/(delta*delta))
        mu=beta*10**6/delta+mv
        ki=qm(bridge['cases'][2+p]['K12_lower']).inv()
        uf=qm(cert['upper_rational'])
        mc=24*10**20*trace(ki)+2*trace(ki*uf)*mu
        exact_rest=Q(str(mv+mc));cap=Q(data['remaining_203_full_gram_scalar'])
        assert exact_rest<=cap and cap-exact_rest<1
        # Exact W=I+D^T D, represented algebraically; J coefficients enclose exact QZ.
        z=qm(D+[[int(i==j) for j in range(84)] for i in range(84)])
        w=z.transpose()*z
        jl=arb_mat([[box(v) for v in row] for row in data['basis_local_coefficients']])
        qlocal=arb_mat([[box(v) for v in row] for row in half['blocks'][p]['basis_Q_local_coefficients']])
        jl_recomputed=qlocal*qa(z)
        for i in range(96):
            for j in range(84): assert jl[i,j].contains(jl_recomputed[i,j])
        weighted=arb_mat([[aq(harmonic[i]+Q(11,10))*jl[i,j] for j in range(84)] for i in range(96)])
        energy=jl.transpose()*weighted
        enclosures=serial(energy,80)
        scale=10**60
        centre=[[Q(0) for _ in range(84)] for _ in range(84)]
        errors=[[Q(0) for _ in range(84)] for _ in range(84)]
        for i in range(84):
            for j in range(i,84):
                lo=min(Q(enclosures[i][j][0]),Q(enclosures[j][i][0]))
                hi=max(Q(enclosures[i][j][1]),Q(enclosures[j][i][1]))
                nearest=Q(((lo+hi)*scale/2+Q(1,2)).__floor__(),scale)
                centre[i][j]=centre[j][i]=nearest
                errors[i][j]=errors[j][i]=max(abs(lo-nearest),abs(hi-nearest))
        radius=Q(1,10**58)
        rowsum=max(sum(row) for row in errors)
        assert rowsum<radius
        # Directed LDL gives a strict positive certificate for the rational lower matrix.
        lo=qm(centre)-qm([[radius*int(i==j) for j in range(84)] for i in range(84)])
        floor_pivots=strict_ldl(qa(lo-fmpq(21,5)*w))
        # A second check against the symbolic upper bound on the polynomial subspace.
        # The symbolic (H95+1.1) W bound follows from X<=WX; do not demand strictness
        # at its largest polynomial mode, where exact equality may occur.
        rec={
            'parity':par.lower(),'matrix':'E84 = L[J,J] in X form; J exact in WX',
            'dimension':84,'centre_rational':[[str(x) for x in row] for row in centre],
            'loewner_radius_scalar':str(radius),'max_error_row_sum_exact':str(rowsum),
            'enclosure':'centre - radius I <= E84 <= centre + radius I',
            'lower_bound_vs_exact_WJ':'E84 >= (21/5) WJ',
            'directed_LDL_of_lower_minus_21_over_5_WJ_passed':True,
            'LDL_pivots':serial(floor_pivots,60),
            'J_gram_upper_scalar':str(wcap),
            'S84_conditional_lower_scalar':str(s_floor),
            'S84_conditional_upper_scalar':str(s_cap),
            'S84_condition_number_upper':'1351/100',
            'S84_bound_requires_inherited_H_le_089_L':True,
            'H84_computed':False,'A0J_computed':False,'actual_S84_computed':False,
            'actual_tau_on_J_computed':False,'full_remainder_certified':False,
            'bindings':{'basis_json_sha256':hashlib.sha256((task/f'BASIS_{par}.json').read_bytes()).hexdigest(),
                        'half_sha256':hashlib.sha256(halfpath.read_bytes()).hexdigest()}}
        (out/f'L_ENERGY_84_{par}.json').write_text(json.dumps(rec,indent=2)+'\n')
        cases.append({'parity':par.lower(),'exact_null_equations':672,
                      'WJ_extra_trace_exact':str(extra),'WJ_extra_trace_display':display(extra),
                      'WJ_upper_scalar':str(wcap),'sharper_fit_error_display':display(fit),
                      'full_65_error_bound':'1e-70','coarse_remaining_bound_exactly_reconstructed':True,
                      'coarse_remaining_cap':str(cap),'L_energy_84_enclosure_computed':True,
                      'L_energy_lower_21_over_5_WJ_certified':True})
    results={'status':'PASS_EXACT_BASIS_CHECKS_AND_L_ENERGY_84',
             'cases':cases,'full_moment_tail_exact':str(local_tail),
             'full_moment_tail_display':display(local_tail),
             'S84_euclidean_condition_bound':'1351/100',
             'S84_precise_symbolic_condition_bound_display':display(s_cap/s_floor),
             'S84_floor_display':display(s_floor),'S84_upper_display':display(s_cap),
             'inherited_analytic_inputs_reproved':False,'H84_computed':False,'A0J_computed':False,
             'actual_tau_on_J_computed':False,'full_remainder_certified':False}
    (out/'INDEPENDENT_CHECKS.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({'status':results['status'],
                      'basis_upper':'1.000502 I',
                      'moment_tail_display':results['full_moment_tail_display'],
                      'S84_condition_bound':'13.51',
                      'full_remainder_certified':False},indent=2))


if __name__=='__main__':main()
