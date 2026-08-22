import sympy as sp
from math import log, sqrt

# Symbolic core-both parity reduction
p, q, r = sp.symbols('p q r', positive=True, nonzero=True)
Delta = p**2 - q**2
A = Delta - r**2
c0 = 2*r/p

beta_plus = sp.factor(A - q**2*r/p)
beta_minus = sp.factor(A + q**2*r/p)
mu_plus = sp.factor((Delta - p*r)/p**2)
mu_minus = sp.factor((Delta + p*r)/p**2)
ell_plus_factor = sp.factor(-(1+c0)*mu_plus)
ell_minus_factor = sp.factor(-(1-c0)*mu_minus)
lambda_plus = sp.factor(-p**2*(p+r)/(p+2*r))
lambda_minus = sp.factor(-p**2*(p-r)/(p-2*r))

print('beta_+ =', beta_plus)
print('beta_- =', beta_minus)
print('mu_+ =', mu_plus)
print('mu_- =', mu_minus)
print('ell_+/h_+ =', ell_plus_factor)
print('ell_-/h_- =', ell_minus_factor)
print('lambda_+ =', lambda_plus)
print('lambda_- =', lambda_minus)
print('D_+ - lambda_+ l_+ =', sp.factor(beta_plus-lambda_plus*ell_plus_factor))
print('D_- - lambda_- l_- =', sp.factor(beta_minus-lambda_minus*ell_minus_factor))
print('P2_+ residual =', sp.factor((2+c0)*mu_plus - 2*beta_plus/p**2))
print('P2_- residual =', sp.factor((2-c0)*mu_minus - 2*beta_minus/p**2))

# Formal stress tests
print('q=r stress + =', sp.factor((beta_plus-lambda_plus*ell_plus_factor).subs(q,r)))
print('q=r stress - =', sp.factor((beta_minus-lambda_minus*ell_minus_factor).subs(q,r)))
print('r->0 lambda_+ =', sp.limit(lambda_plus,r,0))
print('r->0 lambda_- =', sp.limit(lambda_minus,r,0))
print('p=2r ell_-/h_- =', sp.factor(ell_minus_factor.subs(p,2*r)))
print('p=2r beta_- =', sp.factor(beta_minus.subs(p,2*r)))

# Actual P12 coefficient stress test near the J fixed point x=d/2
A0 = log(2)/2
B0 = log(3)/2
T0 = 2*A0
d = B0-A0
e = T0-B0
delta = d-e
p0 = sqrt(log(2))*2**(-3/4)
r0 = sqrt(log(3))*3**(-3/4)
q0 = sqrt(log(2))*2**(-3/2)
R = 0.08
sigma = 0.105
s = 1e-4
x = d/2+s
y = d/2-s
I_lo = max(R,d-sigma)
I_hi = min(sigma,d-R)
small = {'e-x':e-x,'e-y':e-y,'x-delta':x-delta,'y-delta':y-delta}
print('actual p,r,q,c0 =', p0,r0,q0,2*r0/p0)
print('I_both =', I_lo,I_hi)
print('x,y =', x,y)
print('small support args =', small)
assert I_lo < x < I_hi and I_lo < y < I_hi
assert all(0 < v < R for v in small.values())
assert 2*r0/p0 > 1
print('ACTUAL_P12_STRESS_A = PASS')
