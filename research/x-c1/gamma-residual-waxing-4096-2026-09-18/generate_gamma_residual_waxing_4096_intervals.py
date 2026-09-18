#!/usr/bin/env python3
"""Supporting 70-decimal interval enclosure generator.

This script is not the gate checker. Its printed outer intervals are copied into
the Fraction-only checker, where all PASS decisions are exact rational ones.
"""
import mpmath as mp
mp.iv.dps=70
N=4096

def h(t): return mp.iv.exp(-t/2)/(1-mp.iv.exp(-2*t))
def g(t): return h(t)-1/(2*t)
def H(t):
    q=mp.iv.exp(-t/2)
    return mp.iv.log((1+q)/(1-q))/2 + mp.iv.pi/4 - mp.iv.atan2((1-q)/(1+q),1)
def J(t):
    q=mp.iv.exp(-t/2)
    th=(1-q)/(1+q)
    sh=(1/q-q)/2
    return (mp.iv.log(4*th/t)+mp.iv.atan2(sh,1))/2

def W(x): return 20*x**3-45*x**4+36*x**5-10*x**6

def allv(num):
    a=mp.iv.mpf([mp.mpf(num)/10_000_000,mp.mpf(num)/10_000_000])
    ell=mp.iv.log(2); L=2*a
    kap=mp.iv.log(8*mp.iv.pi)+mp.iv.euler+mp.iv.pi/2
    C=kap+ell/mp.iv.sqrt(2)-H(2*a-ell)-H(ell)
    m=H(a+ell/2)+H(a-ell/2)-H(2*a-ell)-H(ell)
    z=ell/L
    p=1-mp.iv.mpf(9)/4*z**5+mp.iv.mpf(5)/2*z**3-mp.iv.mpf(5)/4*z
    lam=1+L*h(L)-C
    d=lam+mp.iv.mpf(7)/12
    be=((a/2)**2/(2*(1-(a/2)**2/12)))**2
    bo=((a/2)**2/(6*(1-(a/2)**2/20)))**2
    gl=g(L)
    qminus=mp.iv.mpf([0,0]); qplus=mp.iv.mpf([0,0])
    prevW=mp.iv.mpf([0,0]); prev_r=mp.iv.mpf([mp.mpf('0.25'),mp.mpf('0.25')])-gl
    for j in range(1,N+1):
        x=mp.iv.mpf([mp.mpf(j)/N,mp.mpf(j)/N])
        Wj=W(x); wt=Wj-prevW
        r=g(L*x)-gl
        qminus += wt*r
        qplus += wt*prev_r
        prevW=Wj; prev_r=r
    qminus*=L; qplus*=L
    M=4*(J(a)-a*gl)
    return dict(C=C,m=m,p=p,lam=lam,d=d,be=be,bo=bo,qminus=qminus,qplus=qplus,M=M)
a_bracket=mp.iv.mpf([mp.mpf(3934355)/10_000_000,mp.mpf(3934360)/10_000_000])
ell_bracket=mp.iv.log(2)
floor_margin=2*H(a_bracket)-H(2*a_bracket-ell_bracket)-H(ell_bracket)+ell_bracket/mp.iv.sqrt(2)
print('BRACKET C2-C0',floor_margin)

for label,num in [('LOW',3934355),('UP',3934360)]:
    print(label)
    vals=allv(num)
    for k,v in vals.items(): print(k, v)
