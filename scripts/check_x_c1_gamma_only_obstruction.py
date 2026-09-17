#!/usr/bin/env python3
"""Exact supporting algebra for X-C1-GAMMA-ONLY-OBSTRUCTION.

Requires Python 3 and SymPy. No quadrature, collocation, optimization,
A1/C0 replay, or large matrix. The proof's convergence and domain steps
are analytic and are NOT certified by these finite checks.
"""
from __future__ import annotations
from math import factorial
import sympy as s

checks: list[str] = []

def zero(name: str, expression: s.Expr) -> None:
    value = s.simplify(s.expand_log(s.expand(expression), force=True))
    if value != 0:
        raise AssertionError(f'{name}: residual {value}')
    checks.append(name)

def positive(name: str, expression: s.Expr) -> None:
    value = s.simplify(expression)
    if value.is_positive is not True:
        raise AssertionError(f'{name}: positivity not established for {value}')
    checks.append(name)

def exp_lower(x: s.Rational, degree: int) -> s.Expr:
    return sum((x**k/s.Integer(factorial(k)) for k in range(degree+1)),s.Integer(0))

R=s.Rational
r,t=s.symbols('r t',real=True)
z=s.symbols('z',positive=True)
# z=exp(a/4), so r=2cosh(a/4)-1=z+1/z-1.
shalf=(z-z**-1)/2
swhole=(z**2-z**-2)/2
zero('exact even step-source Mellin annihilation', swhole-(z+1/z)*shalf)
positive('r bound 33/31 < 16/15',R(16,15)-R(33,31))
positive('r bound is below 3',3-R(16,15))

# Translation energy of the four jumps, computed without correlation quadrature.
positions=[R(-1),R(-1,2),R(1,2),R(1)]
jumps=[s.Integer(1),-1-r,1+r,s.Integer(-1)]
breaks=[R(0),R(1,2),R(1),R(3,2),R(2)]
expected=[(2*r*r+4*r+4)*t,
          2*r*r*t+2*r+2,
          2*r*r-4*r*t+6*r-2*t+4,
          2*r*r+2*t-2]
short=s.Integer(0)
for k,(lo,hi) in enumerate(zip(breaks,breaks[1:])):
    mid=(lo+hi)/2
    actual=sum(j*j*t for j in jumps)
    actual+=2*sum(jumps[i]*jumps[j]*(t-(positions[j]-positions[i]))
                  for j in range(4) for i in range(j)
                  if positions[j]-positions[i] < mid)
    zero(f'translation-energy interval {k+1}',actual-expected[k])
    short+=s.integrate(expected[k]*(1/(2*t)+R(1,4)),(t,lo,hi))
for k in range(3):
    zero(f'translation-energy continuity {k+1}',
         (expected[k]-expected[k+1]).subs(t,breaks[k+1]))
zero('translation tail is twice the norm',expected[3].subs(t,2)-2*(1+r*r))
phi=R(7,4)*r*r+r/2+R(7,4)+(r*r-2*r-3)*s.log(2)+(3*r+3)*s.log(3)
zero('exact integrated short-energy formula',short-phi)
majorant=R(29,12)*r*r+R(37,15)*r+R(61,20)
zero('rational majorant after log bounds',
     phi.subs({s.log(2):R(2,3),s.log(3):R(11,10)})-majorant)
zero('positive polynomial energy margin',
     4*(1+r*r)-majorant-(R(19,12)*(r-1)**2+R(7,10)*(r-1)+R(1,15)))

# All scalar comparisons use exact finite positive exponential series.
positive('log 2 < 7/10',exp_lower(R(7,10),3)-2)
positive('log 3 < 11/10',exp_lower(R(11,10),5)-3)
positive('log 7 < 39/20',exp_lower(R(39,20),6)-7)
zero('gamma > 1/2 from H6-log7',sum(R(1,k) for k in range(1,7))-R(39,20)-R(1,2))
positive('e^3 < 24 via e<11/4',24-R(11,4)**3)
positive('e>8/3',exp_lower(R(1),4)-R(8,3))
positive('e^4>32 via e>8/3',R(8,3)**4-32)
positive('sqrt 2 < 3/2',R(3,2)**2-2)
positive('sqrt 3 < 7/4',R(7,4)**2-3)
positive('e^2<8 via e<11/4',8-R(11,4)**2)

# H(2a) < 3/4: q=exp(-a) < 16/43; H=2 sum q^(4j+1)/(4j+1).
a=R(99,100)
positive('exp(99/100)>43/16',exp_lower(a,5)-R(43,16))
q=R(16,43)
tail_bound=2*q+2*q**5/(5*(1-q**4))
positive('H(198/100)<3/4',R(3,4)-tail_bound)

norm_upper=a*(1+R(16,15)**2)
degree_lower=2*(R(4,9)*(a+R(3,10))+R(4,7)*(a-R(1,10)))
zero('two-prime degree lower bound',degree_lower-R(1136,525))
zero('step-source norm upper bound',norm_upper-R(5291,2500))
positive('prime degree exceeds the norm',degree_lower-norm_upper)
zero('exact degree surplus',degree_lower-norm_upper-R(2489,52500))
positive('norm upper bound is below 3',3-norm_upper)
zero('unmollified negative budget',R(11,2)-5-1+R(1,2))

# Mollification: contraction of Gamma energy + a bounded-potential L2 budget.
epsilon=R(1,10**6)
jump_upper=2+2*(1+R(16,15))**2
positive('small-translation jump bound below 11',11-jump_upper)
positive('smoothing support stays inside (-1,1)',1-a-epsilon)
positive('jump strips are disjoint at the smoothing scale',a/2-epsilon)
positive('sqrt(33 epsilon)<6/1000',R(6,1000)**2-33*epsilon)
zero('mollification potential loss bound',40*R(6,1000)-R(6,25))
zero('smooth witness bound equals -3/4',-a+R(6,25)+R(3,4))
positive('potential bound 7+10<20',20-(7+10))
zero('restricted scalar prime-allocation threshold',-R(3,4)+R(1,80)*60)

# Exact finite-dimensional analogue of P_M A P_M=0 => rank<=4.
# It verifies the general block formulas, not a sampled spectrum.
E=s.zeros(5,2); E[0,0]=1; E[1,1]=1
P=E*E.T
names=s.symbols('a0:25',real=True)
A=s.zeros(5)
for i in range(5):
    for j in range(i,5):
        if i<2 or j<2:
            A[i,j]=A[j,i]=names[5*i+j]
Q=s.eye(5)-P
B=A*E-R(1,2)*E*(E.T*A*E)
zero('orthogonal-projection compression block',sum(x*x for x in Q*A*Q))
zero('all cross-kernel blocks reconstructed',sum(x*x for x in A-(E*B.T+B*E.T)))
zero('projection decomposition',sum(x*x for x in A-(P*A+A*P-P*A*P)))

if __name__=='__main__':
    print(f'SymPy {s.__version__}')
    for name in checks:
        print('PASS  '+name)
    print(f'TOTAL: {len(checks)} exact supporting checks PASS')
    print('Analytic conclusion in note: a fixed smooth v in W_1 has F_I[v] < -3/4.')
    print('F_I is Q_W minus the positive INTERNAL prime-edge energy, NOT Q_W.')
    print('No external certification, full-window positivity, or RH claim.')
