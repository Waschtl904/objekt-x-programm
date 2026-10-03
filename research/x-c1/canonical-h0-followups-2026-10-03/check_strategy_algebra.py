"""Exact finite checks accompanying a strategy note, not an operator certificate."""
from fractions import Fraction as F
import json

def mat(a):
    return [[F(x) for x in row] for row in a]
def tr(a):
    return list(map(list, zip(*a)))
def mul(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def add(a,b,k=1):
    return [[x+k*b[i][j] for j,x in enumerate(row)] for i,row in enumerate(a)]
def inv(a):
    n=len(a)
    a=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j])
        a[j],a[p]=a[p],a[j]
        v=a[j][j]
        a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j]
                a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return [row[n:] for row in a]
def block(a,c,d):
    return [r+s for r,s in zip(a,c)]+[r+s for r,s in zip(tr(c),d)]
def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]
def pd(a):
    a=[row[:] for row in a]
    for k in range(len(a)):
        p=a[k][k]
        if p<=0:
            return False
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                a[i][j]-=a[i][k]*a[k][j]/p
    return True

checks=[]
A=mat([[3,1],[1,2]])
C=mat([[F(1,3),F(2,5)],[F(-1,7),F(4,9)]])
assert pd(A)
Ai=inv(A)
for t in (F(1,10),F(-1,10)):
    S=mat([[t,0],[0,F(2,3)]])
    D=add(mul(tr(C),mul(Ai,C)),S)
    for P in (mat([[0,0],[0,0]]),mat([[F(1,8),F(2,11)],[F(-1,6),F(1,5)]]),mul(Ai,C)):
        E=add(C,mul(A,P),-1)
        K=add(add(add(D,mul(tr(C),P),-1),mul(tr(P),C),-1),mul(tr(P),mul(A,P)))
        recovered=add(K,mul(tr(E),mul(Ai,E)),-1)
        assert recovered==S
        R=eye(4)
        for i in range(2):
            for j in range(2):
                R[i][j+2]=-P[i][j]
        assert mul(tr(R),mul(block(A,C,D),R))==block(A,E,K)
        assert pd(block(A,C,D))==(t>0)
        checks.append({'residual_identity':True,'congruence_identity':True,'positive_schur':t>0})

# Same old form, same cross block, same positive high block; opposite new sign.
for t in (F(1,10),F(-1,10)):
    Q=mat([[1,2,0],[2,4+t,0],[0,0,2]])
    assert Q[0][0]==1 and Q[0][1]==2 and Q[2][2]==2
    assert pd(Q)==(t>0)

# A common spectral measure gives a block Gram identity, including mixed terms.
lam=[F(1,100),F(2,3),F(7,2)]
V=mat([[1,F(1,2)],[F(2,3),F(-1,5)],[F(1,7),1]])
M=mul(tr(V),V)
energy=mul(tr(V),[[lam[i]*x for x in row] for i,row in enumerate(V)])
inverse_energy=mul(tr(V),[[x/lam[i] for x in row] for i,row in enumerate(V)])
gram=block(energy,M,inverse_energy)
features=[[lam[i]*x for x in V[i]]+V[i] for i in range(3)]
weighted=[[x/lam[i] for x in row] for i,row in enumerate(features)]
assert gram==mul(tr(features),weighted)

# The secant of reciprocal energy supplies the required upper bound.
a,b=F(1,100),F(7,2)
weights=[]
for l in lam:
    gap=(a+b-l)/(a*b)-1/l
    assert gap==(l-a)*(b-l)/(a*b*l)>=0
    weights.append(gap)
upper=[[((a+b)*M[i][j]-energy[i][j])/(a*b) for j in range(2)] for i in range(2)]
gap_matrix=add(upper,inverse_energy,-1)
assert gap_matrix==mul(tr(V),[[weights[i]*x for x in row] for i,row in enumerate(V)])
assert gap_matrix[0][0]>=0 and gap_matrix[1][1]>=0
assert gap_matrix[0][0]*gap_matrix[1][1]-gap_matrix[0][1]**2>=0
coarse=[[x/a for x in row] for row in M]
improvement=add(coarse,upper,-1)
assert improvement==[[x/(a*b) for x in row] for row in add(energy,[[a*x for x in row] for row in M],-1)]

# Reducing the residual alone cannot increase the exact Schur reserve.
assert all(row['residual_identity'] for row in checks)

print(json.dumps({'status':'PASS','scope':'Finite rational checks of the displayed standard algebra; no new Root, renewal, or operator certificate.', 'residual_cases':len(checks),'old_high_positivity_counterexamples':2,'matrix_moment_gram_identity':True,'band_upper_bound':True,'band_upper_bound_improves_coarse_bound':True,'schur_reserve_independent_of_P':True},ensure_ascii=False,indent=2))
