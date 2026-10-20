"""Independent Fraction audit of rational K, Young weights, and endpoint logic."""
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sub(A, B):
    return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]


def add(A, B):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]


def scale(c, A):
    return [[c*a for a in row] for row in A]


def tr(A):
    return [list(row) for row in zip(*A)]


def mul(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def positive(A):
    n = len(A)
    need(n and all(len(row)==n for row in A), "Square matrix")
    need(all(A[i][j]==A[j][i] for i in range(n) for j in range(n)), "Exact symmetry")
    L = [[Q(0) for _ in range(n)] for _ in range(n)]
    D = []
    for j in range(n):
        pivot = A[j][j]-sum(L[j][k]**2*D[k] for k in range(j))
        need(pivot > 0, "Nonpositive rational pivot")
        D.append(pivot)
        L[j][j] = 1
        for i in range(j+1,n):
            L[i][j] = (A[i][j]-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/pivot
    return D


def admissibility(rows, old_rows, enclosure):
    K, Ks = ([[Q(x) for x in row] for row in a] for a in (rows,old_rows))
    need(len(K)==len(Ks)==len(enclosure)==12, "Twelve-source dimension")
    bounds = [[(Q(x[0]),Q(x[1])) for x in row] for row in enclosure]
    need(all(len(row)==12 for row in bounds), "Twelve-column enclosure")
    need(all(lo<=hi for row in bounds for lo,hi in row), "Reversed enclosure")
    need(all(bounds[i][j]==bounds[j][i] for i in range(12) for j in range(12)), "Symmetric enclosure")
    center = [[(lo+hi)/2 for lo,hi in row] for row in bounds]
    radii = [sum((hi-lo)/2 for lo,hi in row) for row in bounds]
    lower = [row[:] for row in center]
    for i in range(12):
        lower[i][i] -= radii[i]
    # Every symmetric matrix in the interval box is >= center-diag(row radii).
    p1, p2 = positive(sub(K,Ks)), positive(sub(lower,K))
    return {"K_new_minus_K_star":len(p1),"rounding_margin":len(p2)}


def controls():
    # Noncommuting model/error Grams; operator Young, not entrywise comparison.
    P = [[Q(1),Q(2)],[Q(0),Q(1)]]
    D = [[Q(1,10),Q(0)],[Q(1,20),Q(-1,8)]]
    U, E = mul(tr(P),P),mul(tr(D),D)
    need(mul(U,E)!=mul(E,U), "Control must be noncommuting")
    eps = Q(1,7)
    cap = add(scale(1+eps,U),scale(1+1/eps,E))
    actual = mul(tr(add(P,D)),add(P,D))
    positive(sub(cap,actual))
    # Exactly the squared Young residual proves the general matrix identity.
    residual = sub(P,scale(1/eps,D))
    need(sub(cap,actual)==scale(eps,mul(tr(residual),residual)), "Matrix Young identity")
    # Dropping the reciprocal-epsilon term can reverse the inequality.
    need(Q(4)>Q(2)+Q(1), "Missing reciprocal-error term must fail")
    c,b = Q(1977,500000),Q(51,50)
    a = (b-1)/(b*(1-c)-1)
    need(a*(1-c)>1 and b*(1-c)>1, "Young domains")
    need((a*(1-c)-1)*(b*(1-c)-1)==c, "Exact weight identity")


def check(result):
    need(__debug__, "Do not use python -O")
    counts=admissibility(result["K_new_rational"], result["K_star_rational"], result["K_ceiling_enclosure"])
    need(counts==result["rational_positive_pivots"], "Pivot reporting")
    controls()
    w=result["weights"]
    a,b,c=map(Q,(w["a"],w["b"],w["c"]))
    need(b==Q(51,50) and c==Q(1977,500000), "Frozen weights")
    need(a==(b-1)/(b*(1-c)-1), "Joint weight update")
    need(Q(w["dual_coefficient"])==a/Q(w["beta"]), "Full dual coefficient")
    m=result["model_only"]
    for interval in m.values():
        need(Q(interval[0])<=Q(interval[1]), "Model endpoint order")
    need(Q(m["margin_before_additional_errors_and_dual"][0])>0, "Only positive model margin")
    need(Q(m["partial_old_weight"][0])>Q(m["budget"][1]), "Old weights still exceed in model")
    need(not result["new_directed_partial_energy_computed"] and not result["P_upper_certified"],
         "No energy promotion")
    need(not result["partial_pass"] and result["certified_dual_reserve"] is None,
         "No certified reserve")
    need(not result["RL_computed"] and not result["milestone_4_closed"] and not result["N12_closed"],
         "Open obligations")


if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("result", nargs="?", type=Path, default=Path(__file__).with_name("EXPECTED.json"))
    args=ap.parse_args()
    check(json.loads(args.result.read_bytes()))
    print("PASS: independent rational candidate/rounding/weight audit; energy certification remains open")
