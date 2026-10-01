"""Exact rational matrix algebra for explicit finite moment completions."""
from fractions import Fraction as F

def midpoint(box): return [[sum(map(F,x))/2 for x in row] for row in box]
def trans(a): return list(map(list,zip(*a)))
def mm(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def add(a,b): return [[x+y for x,y in zip(row,col)] for row,col in zip(a,b)]
def scale(a,t): return [[t*x for x in row] for row in a]
def sub(a,b): return add(a,scale(b,-1))
def symmetric(a): return scale(add(a,trans(a)),F(1,2))
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(a):
    n=len(a);m=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=m[j][j];assert pivot
        m[j]=[x/pivot for x in m[j]]
        for i in range(n):
            if i!=j:
                c=m[i][j];m[i]=[x-c*y for x,y in zip(m[i],m[j])]
    return [row[n:] for row in m]
def compressed(n,a): return mm(mm(trans(n),a),n)
def contain(a,box):
    assert len(a)==len(box) and all(len(x)==len(y) for x,y in zip(a,box))
    return all(F(v[0])<=x<=F(v[1]) for row,br in zip(a,box) for x,v in zip(row,br))
def annihilator(y): return scale(mm(inv([row[:6] for row in y]),[row[6:] for row in y]),-1)+eye(2)

def measure(r,trial):
    s=symmetric(midpoint(trial['physical_Ritz_matrix']))
    t=symmetric(scale(add(midpoint(r['trial_resolvent_lower']),midpoint(r['trial_resolvent_upper'])),F(1,2)))
    nu=F(trial['physical_complement_gap_lower_exact']);n=len(s)
    a=sub(scale(eye(n),nu),s)
    k=add(sub(scale(t,nu**2),scale(eye(n),2*nu)),s)
    lp=mm(mm(a,inv(k)),a)
    gp=scale(add(lp,a),1/nu);h=sub(eye(n),gp);zp=sub(t,scale(h,1/nu))
    assert all(x==trans(x) for x in [s,t,lp,gp,h,zp])
    assert zp==mm(mm(gp,inv(lp)),gp)
    assert s==add(lp,scale(h,nu)) and t==add(zp,scale(h,1/nu))
    return {'S':s,'T':t,'LP':lp,'GP':gp,'ZP':zp,'H':h,'nu':nu}

def pencil(y,model):
    n=annihilator(y)
    g=compressed(n,model['GP']);l=compressed(n,model['LP']);z=compressed(n,model['ZP'])
    h=mm(mm(g,inv(l)),g)
    m=add(add(l,scale(g,34)),scale(h,289));r=add(add(l,scale(g,34)),scale(z,289))
    return {'Y':y,'N':n,'G':g,'L':l,'Z':z,'M':m,'R':r,'W':sub(z,h)}

def positive_interval(v,a):
    """Certified LDL pivots for every symmetric matrix in this interval box."""
    m=v.symmetric(a);pivots=[]
    for j in range(len(m)):
        p=m[j][j];assert p[0]>0,('nonpositive LDL pivot',j,v.display(p))
        pivots.append(p)
        for i in range(j+1,len(m)):
            for k in range(i,len(m)):
                value=v.sub(m[i][k],v.div(v.mul(m[i][j],m[k][j]),p))
                m[i][k]=m[k][i]=value
    return pivots

def intervals(v,a): return [[v.rounded(v.point(x)) for x in row] for row in a]
