#!/usr/bin/env python3
"""Exact rational implication for the native Feshbach d-exact firewall.

The five coarse moment inequalities are inputs established independently by
check_vor_iota_prime_m012_and_feshbach.py / the symbolic-position audit:
  m0(v+) > 163/100,  m1(v+) < 263/100,
  m0(v-) < 262/100,  m1(v-) > 441/100,  m2(v-) < 1033/100.

This script proves with fractions only that these bounds imply
<Sigma_1 a,b> > -17/100, while -log(2)/sqrt(2) < -44/100.
It intentionally does not claim to interval-certify the five moment inputs.
"""
from fractions import Fraction as F

m0p_lo = F(163, 100)
m1p_hi = F(263, 100)
m0m_hi = F(262, 100)
m1m_lo = F(441, 100)
m2m_hi = F(1033, 100)

# Q(v+) >= m0^2/(m0+m1); monotone increasing in m0 and decreasing in m1.
qplus_lo = m0p_lo * m0p_lo / (m0p_lo + m1p_hi)
assert qplus_lo == F(26569, 42600)

# Q(v-) <= m0 - m1^2/(m1+m2); increasing in m0,m2 and decreasing in m1.
qminus_hi = m0m_hi - m1m_lo * m1m_lo / (m1m_lo + m2m_hi)
assert qminus_hi == F(191707, 147400)

sigma_lo = (qplus_lo - qminus_hi) / 4
assert sigma_lo == F(-10626119, 62792400)
assert sigma_lo > F(-17, 100)
assert F(-17, 100) > F(-44, 100)
assert F(-44, 100) > F(-4, 9)

# Exact lower bound log(2)>2/3 from the even alternating-harmonic partial sum T20.
t20 = sum(((F(1, n) if n % 2 else -F(1, n)) for n in range(1, 21)), F(0))
assert t20 == F(155685007, 232792560)
assert t20 - F(2, 3) == F(489967, 232792560)
assert t20 > F(2, 3)  # even alternating partial sum lies below log(2)

# sqrt(2)<3/2 because 2<9/4.  Hence log(2)/sqrt(2) > (2/3)/(3/2)=4/9.
assert F(2, 1) < F(9, 4)

print("Exact rational implication certificate")
print(f"Q(v+)  > {qplus_lo}")
print(f"Q(v-)  < {qminus_hi}")
print(f"<Sigma_1 a,b> > {sigma_lo} > -17/100")
print("-17/100 > -44/100 > -4/9 > -log(2)/sqrt(2)")
print("(last comparison uses log(2)>T20>2/3 and sqrt(2)<3/2)")
print("PASS: native Feshbach d-exact target is separated, given the five moment inequalities.")
