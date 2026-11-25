"""Full admissible replay. Python 3.13 / python-flint 0.9.0."""
import gzip
import hashlib
import json
import sys
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

import flint
from flint import arb, arb_mat, ctx, fmpq

from gamma_neu import coefficient_data
from kongruenz import positivity
from primgewicht import row_bound
from rohstichprobe import compare
from schnittstelle import regression

MATH_SHA256="b4f76b9e9a4e290484962f8677d5761bd38438d1f6dd46a9a8a2f879e9857ad2"
FIELDS=["endpoint","cutoff","Gamma_degree","Gamma_kernel_error_exact","Gamma_polynomial_coefficients",
        "active_prime_powers","positive_half_cells","raw_low_moments","scale_digits","parities"]


def ball(pair,scale):
    lo,hi=map(int,pair)
    assert lo<=hi
    return arb(fmpq(lo+hi,2*scale))+arb(0,arb(fmpq(hi-lo,2*scale)))


def exact(q):
    return arb(fmpq(q.numerator,q.denominator))


def verify(path):
    assert flint.__version__=="0.9.0"
    X=json.loads(Path(__file__).with_name("ANTWORT.json").read_bytes())
    assert set(X)=={"even","odd"}
    for rows in X.values():
        assert len(rows)==12 and all(len(row)==12 for row in rows)
        assert all(Q(rows[i][j])==Q(rows[j][i]) for i in range(12) for j in range(12))
        assert max(sum(abs(Q(v)) for v in row) for row in rows)<5*10**13
    assert 20*(5*10**13)*(150*20+1)<10**19
    ctx.prec=1024
    data=json.loads(gzip.decompress(path.read_bytes()))
    raw=json.dumps({key:data[key] for key in FIELDS},sort_keys=True,separators=(",",":")).encode()
    assert hashlib.sha256(raw).hexdigest()==MATH_SHA256
    assert data["endpoint"]=="log(11)/2" and data["active_prime_powers"]==[2,3,4,5,7,8,9]
    N=data["cutoff"]+1
    assert N==384 and data["Gamma_degree"]==160
    # Independent low entries by polynomial autocorrelation, including K, V and S.
    tests=compare(data)
    ctx.prec=1024
    b=arb(11).log()/2
    harmonic=sum((arb(1)/j for j in range(1,N+1)),arb(0))
    q0=-(2*arb.pi()*b).log()-arb.const_euler()
    assert (arb(6)/5).cosh()<2
    gamma_tail=2*b*b*exact(Q(3,8))*(arb(2)/(3*N*(N+1))).sqrt()
    prime_cap=row_bound()
    assert gamma_tail<exact(Q(".0024")) and prime_cap<exact(Q("2.319"))
    assert harmonic+q0-prime_cap-gamma_tail>exact(Q("1.611"))
    assert exact(Q("1.55")).cos()>exact(Q(".02")) and exact(Q(".3")).sinh()>exact(Q(".3"))
    assert exact(Q("1.5")).sin()>exact(Q(".9")) and arb.pi()/2>exact(Q("1.55"))
    poly,epsilon_kernel=coefficient_data()
    assert list(map(str,poly))==data["Gamma_polynomial_coefficients"]
    assert epsilon_kernel==Q(data["Gamma_kernel_error_exact"]) and epsilon_kernel<Q("4.01e-70")
    err=Q(12,5)*epsilon_kernel
    moment=4*Q(3,5)**N/factorial(N)/(1-Q(1,4))
    assert moment<Q("1e-800")
    penalty=Q("1e-211")
    assert 8*Q("1e-250")*(1+10**19)**2 < penalty
    assert Q("1.611")-200*moment-100*moment**2-penalty>Q("1.61")
    high=exact(Q("1.61"))
    p=Q("1e-12")
    coupling_error=2*err+200*moment
    correction=exact(4*err+penalty+(1+1/p)*coupling_error**2/Q("1.61"))
    scale=10**data["scale_digits"]
    results={}
    for parity,row in data["parities"].items():
        n=row["dimension"]
        assert n==191
        L=arb_mat([[ball(x,scale) for x in values] for values in row["A"]])
        G=arb_mat([[ball(x,scale) for x in values] for values in row["complete_model_raw_high_Gram"]])
        lower=L-exact(1+p)*G/high
        for j in range(n):
            lower[j,j]-=correction
        trace=exact(1+p)*G.trace()+exact(n*(1+1/p)*coupling_error**2)
        result=positivity(lower,high,trace)
        assert result["positive"]
        assert Q(result["exact_physical_lower"])>Q("1e-44")
        results[parity]=result
    assert set(results)=={"even","odd"}
    regression()
    return dict(status="AUTHOR_DERIVED_CONDITIONAL_FULL_A9_TO_A11_SHIFTED_OLD_COMPARISON",
                proof_scope="both parities, complete physical Hilbert spaces and form domains",
                input_math_sha256=MATH_SHA256,old_shift="1e-250",initial_shell_floor="1e-250",
                compare_low_entries=tests,gamma_uniform_error_upper="4.01e-70",parities=results,
                full_residual_comparison_floor="1e-44",comparison_inverse_upper="1e44 I_W",
                physical_U11="1e44 I_phys",known_terminal_positivity_used=False,
                fixed_Qstar_full_quotient_certified=False,external_review="OPEN")


if __name__=="__main__":
    print(json.dumps(verify(Path(sys.argv[1])),indent=2))
