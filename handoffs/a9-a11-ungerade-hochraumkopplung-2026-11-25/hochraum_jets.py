from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json,sys,hashlib
from flint import fmpq, fmpq_mat
N=4096
def output_log_jets(fn, frozen):
    assert hashlib.sha256(fn.read_bytes()).hexdigest()=='7c13f08ad85084379249c4a08b7c8bda0813eaea72939ba385cb3756b2801b3c'
    assert hashlib.sha256(frozen.read_bytes()).hexdigest()=='132959da5d34c0c89471ee15f7c34d8b4a42ad48c641b6c4db5181113d11426a'
    F=json.loads(fn.read_bytes())['parities']['odd']['functions']
    X=json.loads(frozen.read_bytes())['parities']['odd']['X']
    assert max(len(col['F']['polynomial']) for col in F)<N
    return cardinal([col['F']['log_ratio_multiplier'] for col in F], X)

def cardinal(rows, X):
    assert fmpq_mat([[fmpq(v) for v in line] for line in X]).det()!=0
    polys=[[fmpq(v) for v in col] for col in rows]
    assert len(polys)==12 and max(map(len,polys))==26
    M=fmpq_mat([[sum((q*comb(j,k) for j,q in enumerate(p) if j>=k),fmpq(0)) for p in polys] for k in range(26)])
    low=fmpq_mat([[M[k,j] for j in range(12)] for k in range(12)])
    B=M*low.inv()
    assert all(B[i,j]==int(i==j) for i in range(12) for j in range(12))
    return [[Q(str(B[r,k])) for k in range(12)] for r in range(26)]

def upper_tail(log_bounds):
    ratio=Q(1)
    total=Q(0)
    for k,A in enumerate(log_bounds):
        if k: ratio*=Q(k*k,(N-k)*(N+k+1))
        total+=A*ratio/N
    return total

def projected_log(B, coeff):
    # Only k<=11 need to be matched. 0<h/a<1/10.
    high=[Q(0)]*max(len(coeff),26)
    polynorm=Q(0)
    for k,A in enumerate(coeff):
        if k>=12:
            high[k]+=A
            continue
        polynorm+=A
        for r in range(12,26):
            term=A*abs(B[r][k])*Q(1,10)**(r-k)
            high[r]+=term
            polynorm+=term
    return upper_tail(high) + polynorm*Q(1,19)**4000

def log_bounds(B):
    g_ratio=Q(12,7) # h/g < 12/7
    coeff=[3000*comb(95,k)*comb(95+k,k)*g_ratio**k for k in range(96)]
    bound=projected_log(B,coeff)
    return bound,projected_log(B,[Q(1)]),sum(coeff)

if __name__=='__main__':
    d=Path(sys.argv[1])
    B=output_log_jets(d/'FUNCTIONS12.json',d/'FROZEN_RESPONSE12.json')
    for v in log_bounds(B): print(float(v))
