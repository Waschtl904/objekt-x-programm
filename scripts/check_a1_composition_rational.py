#!/usr/bin/env python3
"""Independent exact-rational scalar audit for the frozen A1 composition.

Standard library only. No author modules, Arb, matrices, floats or network
enter any acceptance predicate. This checks scalar majorants, scaling and
coverage. It does NOT replay the finite SPD or node-evaluation certificates.
Source model: ac164bbbd2c46623aa64e567d21f813f41f164b0.
See the companion composition audit for the analytic input identities.
"""
from fractions import Fraction as F
from math import factorial, isqrt, prod


def require(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError("FAIL: " + label)
    print("PASS: " + label)


def atan_partial(inv: int, terms: int) -> F:
    return sum((F((-1)**k, (2*k+1)*inv**(2*k+1)) for k in range(terms)), F(0))


def log_upper(x: int, terms: int = 100) -> F:
    """Positive atanh expansion, with a geometric upper bound for its tail."""
    if x < 1 or terms < 1:
        raise ValueError("invalid logarithm parameters")
    y = F(x-1, x+1)
    partial = 2*sum((y**(2*k+1)/(2*k+1) for k in range(terms)), F(0))
    return partial + 2*y**(2*terms+1)/((2*terms+1)*(1-y*y))


def exp_lower(x: F, terms: int) -> F:
    if x < 0 or terms < 1:
        raise ValueError("positive exponential series required")
    return sum((x**k/factorial(k) for k in range(terms)), F(0))


def cosh_upper(x: F, terms: int = 20) -> F:
    if x < 0 or terms < 1:
        raise ValueError("invalid hyperbolic cosine parameters")
    partial = sum((x**(2*k)/factorial(2*k) for k in range(terms)), F(0))
    first_tail = x**(2*terms)/factorial(2*terms)
    ratio = x*x/((2*terms+1)*(2*terms+2))
    if not ratio < 1:
        raise ValueError("tail ratio is not below one")
    return partial + first_tail/(1-ratio)


def main() -> None:
    pi_lo = 16*atan_partial(5, 6)-4*atan_partial(239, 3)
    pi_hi = 16*atan_partial(5, 7)-4*atan_partial(239, 2)
    require(F(157, 50) < pi_lo < pi_hi < F(22, 7), "Machin rational enclosures for pi")

    # Every q=40 Bernstein ellipse: h<=1/5, rho=2+sqrt(5),
    # semiaxes sqrt(5),2. Real overhang <1/4; imaginary part <=2/5.
    require(F(9, 4)**2 > 5, "sqrt(5)<9/4, so endpoint overhang<1/4")
    require(F(409, 20)**2+F(6205, 8)**2 < 776**2,
            "endpoint-extended digamma argument still has |u|<776")
    require(exp_lower(F(7), 20) > 776, "log(776)<7")
    require(exp_lower(F(6, 5), 12) > F(22, 7), "log(pi)<6/5")
    psi_cap = F(7)+F(11, 7)+1/(2*F(401, 20))+1/(12*F(401, 20)**2)
    psi_cap += sum((1/(F(k)+F(1, 20)) for k in range(20)), F(0))
    prime_cap = F(0)
    for n, p in ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7)):
        sqrt_lo = F(isqrt(n*10**12), 10**6)
        require(0 < sqrt_lo and sqrt_lo*sqrt_lo <= n, f"rational sqrt({n}) lower bound")
        prime_cap += 2*log_upper(p)/sqrt_lo*cosh_upper(F(2, 5)*log_upper(n))
    r_cap = psi_cap+F(6, 5)+F(1, 10)+prime_cap
    require(r_cap < 42, "analytic multiplier |r_an|<42 on every endpoint ellipse")
    # exp(4/5) has a positive series. Bound the tail after terms 0..19.
    x, terms = F(4, 5), 20
    exp_cap = exp_lower(x, terms)+x**terms/factorial(terms)/(1-x/(terms+1))
    entry_cap = 42*2*(2*2150-1)/pi_lo*exp_cap
    require(entry_cap < 260000, "every parity integrand entry is below 260000")
    rho_lo = F(1059, 250)
    require(rho_lo > 1 and (rho_lo-2)**2 < 5, "rho=2+sqrt(5)>4.236")
    # Degree-79 Chebyshev truncation and positive Gauss weights give
    # panel error <=8*h*M_f*rho^(-79)/(rho-1), h<=1/5.
    quad = F(8, 5)*260000*rho_lo**(-79)/(rho_lo-1)*3878*1075
    require(quad < F(16, 10**39), "independent quadrature operator bound <1.6e-38")
    require(quad < F(4, 10**38), "unchanged booked quadrature budget <4e-38 is valid")

    M, omega = 2150, 1551
    df = prod(range(1, 2*M+2, 2))
    ratio = F(omega**2, (2*M+3)**2)
    require(ratio < 1, "Legendre tail geometric ratio<1")
    eta = (2/pi_lo)*F(omega**(2*M+1), df*df)/(1-ratio)
    eta_cap = F(4672, 10**45)
    require(eta < eta_cap, "Legendre eta_2150<4.672e-42")
    u = F(1, 4*(2*M+3))
    moment_ratio = F(1, 4*(2*M+1)*(2*M+3))
    sigma2 = F(2*(2*M+1), 2**(2*M)*df*df)/(1-u)/(1-moment_ratio)
    require(sigma2 < F(1, 10**15054), "one-row moment tail squared<1e-15054")
    # E norm squared <6; EP_T norm squared <=2 sigma^2; weighted Young.
    theta = F(1, 1000)
    b2 = (1+theta)*144*eta_cap+(1+1/theta)*12*F(1, 10**1000)
    tau = F(1, 10)-12*eta_cap
    require(tau > F(99, 1000), "Legendre tail floor>0.099")
    require(b2/tau < F(7, 10**39), "complete Legendre Schur penalty<7e-39")
    mu, delta = F(1, 10**35), F(9, 10**36)
    require(delta < tau and (mu-delta)*(tau-delta) > b2,
            "shifted Schur test at delta=9e-36")

    # A midpoint need not inherit the exact scalar bound. The all-shard
    # scalar budget is sum(e_alpha)*(Bmax+2E)^2<1e-39. Its factor>1/2,
    # hence sum(e_alpha)<2e-39 and sum(abs(alpha_mid))<18613.
    require(2/pi_hi > F(1, 2), "scalar-error conversion factor>1/2")
    require(12*1551+F(2, 10**39) < 18613, "safe alpha midpoint mass<18613")
    E, Bmid = F(1, 10**43), F(4, 5)+F(1, 10**43)
    require(2/pi_lo < F(4, 5)**2, "Bmax=sqrt(2/pi)<4/5")
    vector = 18613*(2*Bmid*E+E*E)
    require(vector < F(3, 10**39), "repaired midpoint-mass vector budget<3e-39")
    require(vector+F(1, 10**39) < F(4, 10**39), "repaired total evaluation budget<4e-39")
    q, qvec = F(1, 2**161), F(33, 2**161)
    require(1075 < 33**2, "dyadic vector radius<33 half-ulps")
    # Both parity moment vectors have norm<2. Moment target-ball rounding
    # is guarded directly by the unchanged builders' half-ulp test.
    quant = 155120*q*(Bmid+qvec)**2+18613*(2*Bmid*qvec+qvec*qvec)
    quant += 2*(4*qvec+qvec*qvec)
    require(quant < F(4, 10**43), "independent both-parity dyadic budget<4e-43")

    ledger = F(4, 10**38)+F(4, 10**39)+F(4, 10**43)
    require(ledger == F(440004, 10**43) < F(45, 10**39), "finite ledger sum=4.40004e-38<4.5e-38")
    shift, scale = F(1005, 10**38), 10**38*2**480
    require((F(1, 10)-shift)*scale == (10**37-1005)*2**480, "exact diagonal integer scaling")
    require(F(2, 2**320)*scale == 10**38*2**161, "exact rank-one moment scaling")
    require(F(1, 2**480)*scale == 10**38, "exact signed-Gram scaling")
    require(shift-F(45, 10**39) == F(10005, 10**39) > mu, "finite shift minus ledger>1e-35")
    panels = [p for shard in range(32) for p in range(shard, 3878, 32)]
    require(len(panels) == len(set(panels)) == 3878 and set(panels) == set(range(3878)),
            "32-shard panel coverage is exact and disjoint")
    require(len(panels)*40 == 155120, "all-node count=155120")
    print("CONDITIONAL: the correctly matched imported finite certificates imply L_1>=9e-36 I.")
    print("NOT REPLAYED: matrix artifacts, LDL, all-node evaluation or the real-frequency grid.")
    print("NO all-window, Object-X or RH conclusion.")


if __name__ == "__main__":
    main()
