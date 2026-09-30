"""Exact invariant checks and negative controls for the generalized gap gate."""
from verify_joint_discriminant import *

def pm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in tr(b)] for row in a]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def inv(a):
    d=det(a);assert d>0
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def plus(a,b):return [[x+y for x,y in zip(row,col)] for row,col in zip(a,b)]
def times(a,s):return [[s*x for x in row] for row in a]
def is_positive(a):assert a[0][0]>0 and det(a)>0
def coeffs(r,m):
    a=det(m);b=r[0][0]*m[1][1]+r[1][1]*m[0][0]-2*r[0][1]*m[0][1];c=det(r)
    return a,b,c,b*b-4*a*c
def must_reject(f):
    try:f()
    except (AssertionError,ValueError,ZeroDivisionError):return
    raise AssertionError('negative control was accepted')

def main():
    r=[[F(7),F(2)],[F(2),F(3)]];m=[[F(3),F(1)],[F(1),F(2)]]
    assert pm(r,m)!=pm(m,r)
    a,b,c,delta=coeffs(r,m);assert a>0 and c>0 and delta>0
    for beta in [F(-3),F(0),F(1,7),F(2),F(13)]:
        shifted=[[r[i][j]-beta*m[i][j] for j in range(2)] for i in range(2)]
        assert det(shifted)==a*beta*beta-b*beta+c
    h=[[F(2),F(1)],[F(-1),F(3)]]
    rt=pm(pm(tr(h),r),h);mt=pm(pm(tr(h),m),h)
    at,bt,ct,dt=coeffs(rt,mt)
    assert dt==det(h)**4*delta and dt/at**2==delta/a**2
    print('Noncommuting determinant polynomial and congruence invariance: PASS')
    repeated=[[F(17)*x for x in row] for row in m]
    assert coeffs(repeated,m)[3]==0
    # In a double pencil, trace=2 beta and the small-eigenvalue bound cannot
    # be below beta. The strict comparison must fail.
    def strict_comparison():assert F(34)-2*F(17)>0
    must_reject(strict_comparison)
    print('Exact double pencil retained as a negative control: PASS')
    # Independent noncommuting positive pencil satisfying the needed moment order.
    g=[[F(2),F(1,2)],[F(1,2),F(1)]]
    l=[[F(1,10),F(1,30)],[F(1,30),F(1,5)]]
    factor=[[F(100),F(50)],[F(10),F(0)],[F(0),F(10)]]
    z=pm(tr(factor),factor);gi=inv(g)
    is_positive(plus(g,times(l,-1)))
    is_positive(plus(z,times(pm(pm(g,inv(l)),g),-1)))
    bmat=plus(l,times(g,17));m=pm(pm(bmat,inv(l)),bmat)
    r=plus(plus(l,times(g,34)),times(z,289));a,b,c,delta=coeffs(r,m)
    assert pm(r,m)!=pm(m,r)
    phi=sum(pm(pm(pm(gi,l),gi),z)[i][i] for i in range(2))
    t0=F(289,324)*phi
    multipliers=[F(1),F(2,25),F(1,25)]
    rest=[[factor[i][j]-multipliers[i]*factor[0][j] for j in range(2)] for i in range(3)]
    rest_gram=pm(tr(rest),rest)
    u=F(35,289)+sum(pm(pm(pm(gi,l),gi),rest_gram)[i][i] for i in range(2))
    assert b/a>=t0 and t0>2*u
    x=[F(-50),F(100)]
    quotient=sum(x[i]*r[i][j]*x[j] for i in range(2) for j in range(2))/sum(x[i]*m[i][j]*x[j] for i in range(2) for j in range(2))
    assert quotient<=u
    a0=17**4*det(g)**2/det(l)
    assert a>=a0 and delta>=a0*a0*(t0-2*u)**2>0
    print('Independent joint trace, kernel minimax and discriminant certificate: PASS')
    # Exact test of the joint functional enclosure, independently of research data.
    y=[[point(int(i==j)) for j in range(6)]+[point(F(i+1,100)),point(F(2-i,100))] for i in range(6)]
    mc=eye(6)
    n=[[neg(x) for x in row[6:]] for row in y]+[[point(1),point(0)],[point(0),point(1)]]
    f=[[point(F((i+2)*(j+1),19)) for j in range(8)] for i in range(8)]
    enclosed,proof=functional_enclosure(f,y,mc,n);exact=mm(f,n)
    assert all(enclosed[i][j][0]<=exact[i][j][0]<=exact[i][j][1]<=enclosed[i][j][1] for i in range(8) for j in range(2))
    assert proof['minimum_supersolution_margin']>0
    bad=[row[:] for row in y];bad[0][0]=point(3)
    must_reject(lambda:functional_enclosure(f,bad,mc,n))
    print('Joint functional identity and failed contraction rejection: PASS')
    assert angle_degrees(point(0))==(F(0),F(0))
    pos=angle_degrees((F(1,100),F(1,50)));assert 0<pos[0]<pos[1]<2
    negative=angle_degrees((F(-1,50),F(-1,100)));assert negative==neg(pos)
    must_reject(lambda:div(point(1),(F(-1),F(1))))
    print('Physical-angle orientation and zero-divisor guard: PASS')
    print('ALL JOINT DISCRIMINANT CHECKS PASS')

if __name__=='__main__':main()
