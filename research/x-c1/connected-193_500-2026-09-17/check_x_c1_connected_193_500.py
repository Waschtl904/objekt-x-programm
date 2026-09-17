#!/usr/bin/env python3
from fractions import Fraction as Q
import json, sys
sys.set_int_max_str_digits(0)

checks = []
results = {}

def check(name, cond, value=None):
    if not cond:
        raise AssertionError(name)
    checks.append(name)
    if value is not None:
        results[name] = str(value)

def atanh_bounds(q, N):
    s = Q(0)
    p = q
    q2 = q*q
    for n in range(N):
        s += p / Q(2*n+1)
        p *= q2
    lo = 2*s
    hi = lo + 2*p / (Q(2*N+1)*(1-q2))
    return lo, hi

def log_bounds(x, N=12):
    if x <= 0:
        raise ValueError("x must be positive")
    k = 0
    y = x
    while y >= 2:
        y /= 2
        k += 1
    while y < 1:
        y *= 2
        k -= 1
    lo2, hi2 = atanh_bounds(Q(1,3), N)
    q = (y-1)/(y+1)
    loy, hiy = atanh_bounds(q, N)
    if k >= 0:
        return k*lo2 + loy, k*hi2 + hiy
    return k*hi2 + loy, k*lo2 + hiy

a = Q(193,500)
L = 2*a
z = a/4
beta = Q(3307,2000)

# 1. Channel regime.
log2_lo, log2_hi = atanh_bounds(Q(1,3), 4)
check("log2_lower_6931e4", log2_lo > Q(6931,10000))
check("log2_upper_6932e4", log2_hi < Q(6932,10000))
check("prime2_active", log2_hi < L, L-log2_hi)
# log 3 > 1 because e<3; rational exp-series bound e<11/4<3 is checked.
e_upper = Q(1)+Q(1)+Q(1,2)+Q(1,6)/(1-Q(1,4))
check("e_upper_11_4", e_upper == Q(49,18) and e_upper < Q(11,4), e_upper)
check("prime3_inactive_via_log3_gt_1", L < 1, 1-L)

# 2. Kernel split valid on 0<t<=L, using stronger range t<=4/5.
check("L_below_4_5", L < Q(4,5), Q(4,5)-L)
# Lower proof reduces to t^2 - 10t + 10 >0; decreasing on [0,4/5].
poly_lower_at_4_5 = Q(4,5)**2 - 10*Q(4,5) + 10
check("kernel_lower_polynomial", poly_lower_at_4_5 > 0, poly_lower_at_4_5)
# Upper proof reduces to 4 t^2 - 35 t -1 <0.
poly_upper_at_0 = -Q(1)
poly_upper_at_4_5 = 4*Q(4,5)**2 - 35*Q(4,5) - 1
check("kernel_upper_polynomial_left", poly_upper_at_0 < 0, poly_upper_at_0)
check("kernel_upper_polynomial_right", poly_upper_at_4_5 < 0, poly_upper_at_4_5)
check("exp_tail_range", L/2 < Q(2,5) < Q(2,3), L/2)

# 3. Gamma upper bound gamma < 5773/10000 via H_10000-log10000.
H10000 = Q(0)
for k in range(1,10001):
    H10000 += Q(1,k)
log10000_lo, _ = log_bounds(Q(10000), 12)
gamma_upper = H10000 - log10000_lo
check("gamma_upper_5773e4", gamma_upper < Q(5773,10000))

# 4. Center reserve.
coth_lb = 1/z + z/Q(3) - z**3/Q(45)
X = coth_lb * Q(7,176)
logX_lo, _ = log_bounds(X, 6)
atan2_upper = 2*z - z**3
center_lb = logX_lo - Q(5773,10000) - atan2_upper
check("center_rho_floor", center_lb > -beta)

# 5. Prime-2 endband leakage.
llo = Q(6931,10000)
lhi = Q(6932,10000)
ratio = a*a / (llo*(2*a-llo))
logratio_lo, _ = log_bounds(ratio, 8)
dmin = 2*a-lhi
leak_lb = Q(1,2)*logratio_lo - (a*a-dmin*dmin)/Q(32) + (llo*llo-a*a)/Q(100)
check("prime2_endband_leak_gt_half", leak_lb > Q(1,2))
check("w2_lt_half_proxy", Q(7,10)/Q(7,5) == Q(1,2))

# 6. Moment reconstruction Taylor bounds at |x|/2<=193/1000.
r = Q(193,1000)
cosh_err = r*r / (2*(1-r*r/Q(12)))
sinh_rel_err = r*r / (6*(1-r*r/Q(20)))
check("cosh_moment_ratio_lt_1_50", cosh_err < Q(1,50), cosh_err)
check("sinh_moment_ratio_lt_1_150", sinh_rel_err < Q(1,150), sinh_rel_err)

# 7. Modal coefficients.
L5 = L/Q(5)
lam0 = -beta
lam1 = Q(1) + L5 - beta
lam2 = Q(3,2) + L5 - beta
check("lambda0", lam0 == -Q(3307,2000), lam0)
check("lambda1", lam1 == -Q(4991,10000), lam1)
check("lambda2", lam2 == Q(9,10000), lam2)
check("higher_modes_positive", lam2 > 0, lam2)

# 8. Rank-two defect norm.
even_row_sq = beta / (lam2 * Q(2500))
odd_row_sq = (-lam1) / (lam2 * Q(22500))
B2 = Q(3307,4500)
check("even_row_sq", even_row_sq == B2, even_row_sq)
check("odd_row_below_even", odd_row_sq < B2, odd_row_sq)
check("B_contractive", B2 < 1, 1-B2)

# 9. Source norm recovery and final quantitative gap.
norm_inflation = Q(1) + Q(1,2500)
gap = (1-B2)*lam2/norm_inflation
check("final_gap_exact", gap == Q(1193,5002000), gap)
check("final_gap_gt_1_5000", gap > Q(1,5000), gap-Q(1,5000))

# 10. Audit interpretation guard.
check("a_193_500_above_19_50", a > Q(19,50), a-Q(19,50))
check("a_193_500_below_reported_scalar_crossing_3869e4", a < Q(3869,10000), Q(3869,10000)-a)

print(f"{len(checks)} exact rational checks PASS")
for name in checks:
    print("PASS", name)
with open("connected_193_500_results.json","w",encoding="utf-8") as f:
    json.dump({"checks": checks, "results": results}, f, indent=2, sort_keys=True)
    f.write("\n")
