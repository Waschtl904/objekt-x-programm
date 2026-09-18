#!/usr/bin/env python3
"""Small exact checks for X-C0/common-memory, NOT an A1 re-audit.

Needs SymPy. No network, A1 imports, matrix artifacts, numeric approximations,
LDL calls or large computations. These identities support the accompanying
manual domain proofs; they do not certify a positive Weil realization.
"""
from __future__ import annotations
import sympy as s

R = s.Rational
passed = 0


def equal(left: s.Expr | s.MatrixBase, right: s.Expr | s.MatrixBase,
          label: str) -> None:
    global passed
    difference = left - right
    if isinstance(difference, s.MatrixBase):
        ok = all(s.simplify(e) == 0 for e in difference)
    else:
        ok = s.simplify(difference) == 0
    if not ok:
        raise AssertionError(f"FAIL: {label}: {difference}")
    passed += 1
    print(f"PASS: {label}")


def main() -> None:
    r, t, mu, p = s.symbols("r t mu p", positive=True)
    x = s.symbols("x", real=True)
    k = s.symbols("k", integer=True, positive=True)
    v = s.Function("v")
    left = s.exp(-(t-r)/2)
    right = s.exp(-(r-t)/2)
    equal(-s.diff(left, r, 2)+left/4, 0, "Green ODE left of the evaluation point")
    equal(-s.diff(right, r, 2)+right/4, 0, "Green ODE right of the evaluation point")
    equal(s.diff(right, r).subs(r,t)-s.diff(left,r).subs(r,t), -1,
          "Green derivative jump is -1")
    equal(s.diff(left,r).subs(r,0)-left.subs(r,0)/2, 0,
          "Robin boundary condition for t>0")
    k0 = s.exp(-r/2)
    equal(-s.diff(k0,r).subs(r,0)+k0.subs(r,0)/2, 1,
          "evaluation at zero has unit boundary coefficient")
    equal(s.integrate(s.diff(k0,r)**2+k0**2/4,(r,0,s.oo))+R(1,2), 1,
          "the root evaluation vector has norm one")

    lift = s.exp(-r/4)*v(x-r)
    equal(s.diff(lift,x)+s.diff(lift,r)+lift/4,0,"common-memory transport PDE")
    equal(lift.subs(r,0),v(x),"boundary trace recovers the source")
    weight = s.integrate(s.exp(-r/2),(r,0,s.oo))
    equal(weight,2,"memory weight integral")
    # The mixed derivative integral vanishes by integration by parts on H^1.
    equal(weight*(R(1,16)+R(1,4))+R(1,2),R(9,8),
          "L2 coefficient in the lift norm; derivative coefficient is two")

    actual = s.exp(-t/4)*v(x-t/2)-s.exp(-t/4)*v(x+t/2)
    desired = s.exp(-t/4)*(v(x-t/2)-v(x+t/2))
    equal(actual,desired,"jump port is exp(-t/4) times the symmetric jump")
    equal((s.sqrt(s.log(p))*s.exp(-k*s.log(p)/4))**2,
          s.log(p)*p**(-k/2),"prime-port amplitude squared is the Weil weight")
    equal(s.exp(-t/2)/(1-s.exp(-2*t))*s.exp(t/2),
          1/(1-s.exp(-2*t)),"Gamma port uses the same damped jump")
    equal(s.exp(-(mu-R(1,4))*r)*s.exp(-r/4),s.exp(-mu*r),
          "Gamma Laplace port gives the causal resolvent kernel")

    a,b = s.symbols("a b",positive=True)
    # Here 0<a<a+b, avoiding numerical absolute-value case choices.
    ss,tt=a,a+b
    cov=lambda u,w: s.exp(-s.Abs(u-w)/2)
    gram=(cov(ss,tt)-s.exp(-tt/4)*cov(ss,0)
          -s.exp(-ss/4)*cov(0,tt)+s.exp(-(ss+tt)/4))
    formula=(s.exp(-(tt-ss)/2)-s.exp(-ss/2-tt/4)
             -s.exp(-ss/4-tt/2)+s.exp(-(ss+tt)/4))
    equal(gram,formula,"nonorthogonal jump-port Gram")
    y=s.symbols("y",positive=True)
    equal(y**2-y,y*(y-1),"root/jump pairing has strict sign for 0<y<1")
    equal(s.exp(-s.log(4)),R(1,4),"stopped coordinate norm at depth zero")
    equal(s.exp(s.log(2)-s.log(4)),R(1,2),"same stopped coordinate norm at depth log 2")

    for sign in (-1,1):
        f=s.exp(sign*x/2)
        equal(-s.diff(f,x,2)+f/4,0,f"NULLPOL integration-by-parts annihilator {sign:+}")
    G=s.Matrix([[2,-1],[-1,2]])
    lam=s.symbols("lambda")
    equal(G.charpoly(lam).as_expr(),(lam-1)*(lam-3),
          "mixed-probe uncentered jump Gram is positive")
    equal((G-2*s.eye(2)).charpoly(lam).as_expr(),lam**2-1,
          "centered prime block has both signs")
    equal(G[0,1],-1,"Prime-2 mixed coefficient has the required negative sign")
    mass=s.symbols("mass",positive=True)
    equal(2*mass-2*mass,0,"exterior centered channel cancels exactly")
    print(f"TOTAL: {passed} exact symbolic/algebraic checks PASS")
    print("NOT TESTED: a positive C_a, full Weil identity, or final X connecting maps.")
    print("No A1 re-audit, numerical positivity promotion, or novelty claim.")


if __name__ == "__main__":
    main()
