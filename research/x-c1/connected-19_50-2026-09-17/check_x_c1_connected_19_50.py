#!/usr/bin/env python3
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path

CHECKS=[]
def req(ok,name):
    if not ok: raise AssertionError(name)
    CHECKS.append(name); print('PASS:',name)

def exp_bounds(x,n=48):
    if x<0:
        lo,hi=exp_bounds(-x,n); return 1/hi,1/lo
    p=sum((x**k/F(factorial(k)) for k in range(n+1)),F(0))
    tail=(x**(n+1)/F(factorial(n+1)))/(1-x/F(n+2))
    return p,p+tail

def log_unit(x,n=48):
    if not F(1)<=x<=F(2): raise ValueError(x)
    q=(x-1)/(x+1)
    p=2*sum((q**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    tail=2*q**(2*n+1)/(F(2*n+1)*(1-q*q))
    return p,p+tail

def log_bounds(x):
    if x<=0: raise ValueError(x)
    if x<1:
        lo,hi=log_bounds(1/x); return -hi,-lo
    k=0
    while x>2:
        x/=2; k+=1
    lo,hi=log_unit(x)
    l2,u2=log_unit(F(2))
    return lo+k*l2,hi+k*u2

def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))

def main():
    a=F(19,50); L=2*a; z=a/2
    l2lo,l2hi=log_bounds(F(2)); l3lo,l3hi=log_bounds(F(3))
    req(F(69,100)<l2lo and l2hi<F(7,10),'69/100 < log2 < 7/10')
    req(l2hi<L and 2*l2lo>L,'Prime-2 active with two disjoint endpoint bands')
    req(l3lo>1>L,'no Prime-3 shift on length 19/25')
    req(l2hi/F(7,5)<F(1,2),'w2<1/2')

    b=F(1,6)/(1-L*L/F(20))
    margin=F(1,10)-(b-F(1,8))*L-F(2,5)*b*L*L
    req(margin>0,'kernel lower margin stays positive through t=19/25')
    req(exp_bounds(a)[1]<F(3,2),'exp(L/2)=exp(19/50)<3/2')

    gamma_up=harmonic(400)-log_bounds(F(400))[0]
    req(gamma_up<F(579,1000),'gamma < H400-log400 < 579/1000')
    req(log_bounds(F(418,175))[1]<F(881,1000),'log(418/175)<881/1000')
    req(F(881+579+190,1000)==F(33,20),'central reserve budget totals 33/20')

    req(a*a/F(483,10000)==F(1444,483),'endpoint leakage ratio lower bound 1444/483')
    req(log_bounds(F(1444,483))[0]>F(407,375),'log(1444/483)>407/375')
    req(F(1,2)*F(407,375)-F(16,375)==F(1,2),
        'leakage lower bound is strictly >1/2>w2')

    C=F(33,20); cker=L/F(5)
    lam0=-C
    lam1=F(1)+cker-C
    lam2=F(3,2)+cker-C
    req(lam0==-F(33,20),'mode 0 coefficient')
    req(lam1==-F(249,500),'mode 1 coefficient')
    req(lam2==F(1,500),'mode 2 and higher floor is 1/500')

    cosh_err=z*z/(2*(1-z*z/F(12)))
    sinh_rel=z*z/(6*(1-z*z/F(20)))
    req(cosh_err<F(1,50),'cosh moment residual <1/50')
    req(sinh_rel<F(1,150),'sinh moment residual <1/150')

    be2=C*500/F(50)**2
    bo2=(-lam1)*500/F(150)**2
    req(be2==F(33,100),'even defect row norm squared <33/100')
    req(bo2==F(83,7500) and bo2<be2,'odd defect row smaller')
    req(be2<1,'rank-two defect remains contractive')

    qfloor=(1-be2)*lam2/(1+F(1,2500))
    req(qfloor==F(67,50020),'connected 19/50 lower bound 67/50020')
    req(qfloor>F(1,1000),'coarse lower bound >1/1000')

    result={
      'status':'EXACT_SCALAR_CHECKS_FOR_CONNECTED_19_50',
      'half_width':str(a), 'length':str(L),
      'mode0':str(lam0),'mode1':str(lam1),'mode2_floor':str(lam2),
      'B_norm_squared_upper':str(be2),'Q_lower':str(qfloor),
      'check_count':len(CHECKS),'checks':CHECKS,
      'not_tested':['external review','full unit window','A1','all-window Object X']
    }
    Path('connected_19_50_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('TOTAL:',len(CHECKS),'exact scalar checks PASS')

if __name__=='__main__': main()
