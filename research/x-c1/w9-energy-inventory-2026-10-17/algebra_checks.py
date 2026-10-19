"""Exact finite counterchecks of feature/Young algebra, not arithmetic evidence."""
from fractions import Fraction as Q


def mat(rows): return [[Q(x) for x in row] for row in rows]
def tr(a): return list(map(list,zip(*a)))
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def neg(a): return [[-x for x in r] for r in a]
def scale(a,t): return [[t*x for x in r] for r in a]
def mul(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def gram(a,w): return mul(tr(a),mul(w,a))
def inv2(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return scale([[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]],1/d)
def need(ok):
    if not ok: raise RuntimeError('Exact algebra countercheck failed')


def run():
    ident=mat([[1,0],[0,1]])
    jold=mat([[1,0],[0,1],[0,0],[0,0]])
    lam=mat([[1,0],[0,1],[1,1],[0,1]])
    f=mat([[1,2],[0,1],[1,0],[2,-1]])
    gf=mat([[1,2],[3,1]]);g=mat([[2,1],[0,3]])
    afin=mat([[3,1],[-1,2]])
    k=mat([[2,1],[1,3]]);ki=inv2(k)
    p=mat([[4,1],[1,2]]);jl=mat([[1,1],[0,2]])
    rl=mat([[Q(1,3),Q(1,7)],[Q(1,7),Q(1,2)]])
    th=mat([[1,2],[0,1]]);vf=mat([[2,0],[1,1]])
    delta=Q(7,3);rho=Q(1,10);beta=Q(2,5)
    u=add(scale(gram(th,ident),1/delta),scale(gram(vf,ident),1/(1-rho)))
    v=add(tr(f),neg(mul(tr(gf),mul(u,tr(jold)))))
    n=add(add(tr(lam),neg(mul(tr(g),mul(u,tr(jold))))),neg(mul(tr(afin),mul(ki,v))))
    spike=scale(gram(mul(tr(jl),n),p),Q(11,10))
    w=add(add(gram(tr(jold),u),gram(v,ki)),add(scale(gram(n,rl),Q(11,10)/beta),spike))
    need(mul(k,p)!=mul(p,k))
    count=0
    for seed in range(1,7):
        e=mat([[seed,1],[2,-1],[1,3],[0,2]])
        t=mat([[1,seed,-2],[0,1,1]])
        rh=mat([[1,2,0],[0,1,3],[2,1,seed],[1,-1,2]])
        et=mul(e,t);r=add(rh,neg(et))
        qd=gram(e,w)
        e8=mul(tr(jold),e)
        blocks=add(add(scale(gram(mul(th,e8),ident),1/delta),scale(gram(mul(vf,e8),ident),1/(1-rho))),
                   add(gram(mul(v,e),ki),add(scale(gram(mul(n,e),rl),Q(11,10)/beta),scale(gram(mul(tr(jl),mul(n,e)),p),Q(11,10)))))
        need(qd==blocks)
        err=gram(t,qd);h=gram(rh,w);actual=gram(r,w)
        for theta in (Q(1,3),Q(2,3)):
            upper=add(scale(h,1+theta),scale(err,1+1/theta))
            lower=add(scale(h,1-theta),scale(err,1-1/theta))
            need(add(upper,neg(actual))==scale(gram(add(scale(rh,theta),et),w),1/theta))
            need(add(actual,neg(lower))==scale(gram(add(scale(rh,theta),neg(et)),w),1/theta))
            count+=2
        need(actual!=add(h,err))  # dropping shared cross terms changes energy
    # A lower norm bound cannot price an upper weighted error.
    huge=mat([[10000,0],[0,1]]);e=mat([[Q(1,100)],[0]])
    need(gram(e,huge)[0][0]>Q(1,10000))
    # Phi*h and ||h|| do not determine B*T_h h: same low part/norm, opposite high sign.
    hplus=mat([[1],[1]]);hminus=mat([[1],[-1]])
    vplus=hplus[0][0]-hplus[1][0];vminus=hminus[0][0]-hminus[1][0]
    need(gram(hplus,ident)==gram(hminus,ident) and vplus*vplus!=vminus*vminus)
    return {'feature_Gram_identities':6,'Young_matrix_identities':count,
            'cross_terms_required':True,'lower_norm_as_upper_rejected':True,
            'stored_low_map_and_norm_are_insufficient':True,
            'noncommuting_weights_used':True,'arithmetic_operator_evidence':False}


if __name__=='__main__': print(run())
