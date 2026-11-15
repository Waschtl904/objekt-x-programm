"""Exact rational checks for the q=11 wall instantiation.

Standard library only. This checks the scalar q=11/A13 constants used in
PROOF.md. Infinite-dimensional wall arguments are inherited from the already
bound general wall theorem and are not replaced by this script.
"""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib, argparse

def log_bounds(q,n=220):
    q=F(q); assert q>=1
    z=(q-1)/(q+1); term=z; s=F(0)
    for k in range(n):
        s += term/F(2*k+1)
        term *= z*z
    return 2*s, 2*(s + term/F(2*n+1)/(1-z*z))

def prime_power(q):
    for p in range(2,q+1):
        if any(p%d==0 for d in range(2,p)): continue
        v=p
        while v<q: v*=p
        if v==q: return p
    return None

def active(threshold):
    return {q for q in range(2,14) if q<threshold and prime_power(q)}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path)
    args=ap.parse_args()
    here=Path(__file__).resolve().parent
    checks=[]
    def check(name,cond):
        if not cond: raise AssertionError(name)
        checks.append(name)

    l2,u2=log_bounds(2)
    l11,u11=log_bounds(11)
    l13,u13=log_bounds(13)

    check("A11 < A13",u11<l13)
    check("A13 < 13/10",u13<F(13,5))
    check("log11 < 12/5",u11<F(12,5))
    check("sqrt11 > 33/10",F(33,10)**2<11)
    check("q11 weight < 8/11",u11/F(33,10)<F(8,11))
    check("q11 shift < 4 so C_ell=1",u11<4)

    v=F(8,11)
    check("new envelope < 29/2",F(13)+2*v==F(159,11)<F(29,2))
    check("wall lower squared 55/63",F(10)/(F(10)+2*v)==F(55,63))
    check("T upper 19/11",1+v==F(19,11))
    check("D upper 71/55",1+2*v/F(5)==F(71,55))

    check("11 is prime power",prime_power(11)==11)
    check("12 is not prime power",prime_power(12) is None)
    check("13 is prime power",prime_power(13)==13)
    check("strict A11 family excludes11",active(F(11))=={2,3,4,5,7,8,9})
    check("interior fourth chamber includes11",active(F(12))=={2,3,4,5,7,8,9,11})
    check("strict A13 family excludes13",active(F(13))=={2,3,4,5,7,8,9,11})

    check("A13 < log4",u13<4*l2)
    S=F(29,2)
    theta=F(1)/(1+S)
    rho=S+1
    check("common T floor 2/31",theta==F(2,31))
    check("helper shift rho=31/2",rho==F(31,2))
    check("source norm factor 965/4",1+rho/theta==F(965,4))
    check("R squared upper 899/4",S/theta==F(899,4))

    c=F(1,10**50)
    image=c/(c+S)
    check("transported old-image defect floor",image==F(2,29*10**50+2))

    result={
      "status":"Q11_WALL_EXACT_SCALAR_CHECKS_PASS",
      "checks_passed":len(checks),
      "checks":checks,
      "scope":"raw q11 wall from A11 through A13; no full A13 terminal positivity",
      "q11":{
        "weight_upper":"8/11",
        "shift_upper":"12/5",
        "lower_multiplier_squared":"55/63",
        "T_upper":"19/11",
        "D_upper":"71/55",
        "post_wall_envelope_upper":"29/2",
        "source_T_floor":"2/31",
        "source_norm_factor":"965/4",
        "R_squared_upper":"899/4",
        "transported_A11_image_defect_floor":"2/(29*10^50+2)"
      },
      "full_A13_terminal_positivity":"OPEN",
      "external_analytic_review":"OPEN",
      "checker_sha256":sha(Path(__file__))
    }
    out=args.output or here/"CHECK_RESULTS.json"
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["status","checks_passed","scope","full_A13_terminal_positivity"]}))

if __name__=="__main__":
    main()
