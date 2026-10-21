"""Algebraic precomputation for the exploratory whole residual evaluator."""
from flint import arb,arb_poly

def install(ns):
    c=ns['c'];roots=ns['roots'];logseq=ns['logseq']
    static=ns['outerstatic'];upp=ns['upp'];cells=ns['cells']
    def quotient_integral(p,mom):
        return arb_poly([sum((p[k]*mom[k-1-j]for k in range(j+1,len(p))),arb(0))for j in range(len(p)-1)])
    corr=arb_poly([])
    for tag,p in static.items():
        mom=[arb(1)/(k+1)for k in range(len(p))]if tag is None else logseq[tag]
        corr+=quotient_integral(p,mom)
    for p,(lo,hi)in zip(upp,cells):
        ll,hh=roots[lo],roots[hi]
        corr+=quotient_integral(p,[(hh**(k+1)-ll**(k+1))/(k+1)for k in range(len(p))])
    def fast(s):
        total=-corr(s)
        for tag,p in static.items():
            total+=p(s)*(abs(s/(s-1)).log()if tag is None else ns['ilog'](s,ns['rootvalues'][tag]))
        for p,(lo,hi)in zip(upp,cells):
            total+=p(s)*abs((s-roots[lo])/(s-roots[hi])).log()
        return total
    ns['cauchy_static']=fast
    a,b,spx=ns['a'],ns['b'],ns['spx']
    sc=quotient_integral(spx,[(b**(k+1)-a**(k+1))/(k+1)for k in range(len(spx))])
    ns['shell_cauchy']=lambda x:sc(-x)+spx(-x)*((x+b)/(x+a)).log()
    res=ns['res'];original=res.cell;cc=ns['cc'];q=ns['q']
    ell=sum((res.ell[j].p*cc[j]for j in range(12)),arb_poly([]))
    quot=sum((res.quot[j].p*cc[j]for j in range(12)),arb_poly([]))
    gamma=sum((res.gamma[j].p*cc[j]for j in range(12)),arb_poly([]))
    dv=sum((res.Dv[j].p*cc[j]for j in range(12)),arb_poly([]))
    dm=sum((res.Dm[j]*cc[j]for j in range(12)),arb(0))
    ac=sum((res.Ac[j]*cc[j]for j in range(12)),arb(0))
    dp0=sum((res.Dpoly[j]*cc[j]for j in range(12)),arb_poly([]))
    tc=[sum((res.T[i,j]*cc[j]for j in range(12)),arb(0))for i in range(12)]
    bounds=[arb(0),res.a,res.b]
    for n,prime in res.channels:
        sh=res.logs[n]
        for endpoint in (-res.a,-res.b,res.a,res.b):
            bounds.extend([endpoint-sh,endpoint+sh])
    bounds.sort(key=float)
    cache={}
    records={}
    def scalar_cell(lo,hi):
        mid=(lo+hi)/2;a,b=res.a,res.b;dp=arb_poly(dp0);terms=[]
        for i,fj in enumerate(res.funcs):
            for term in fj['D']['shift_terms']:
                sh=res.logs[int(term['channel'])]/a
                dl,dh=(arb(0),1-sh)if int(term['translation_sign'])==1 else(max(arb(0),sh-1),arb(1))
                if dl<mid/a<dh:dp+=arb_poly(list(map(q,term['polynomial'])))*tc[i]
        for n,prime in res.channels:
            for sign in (-1,1):
                shift=sign*res.logs[n];y=mid+shift;weight=arb(prime).log()/arb(n).sqrt()
                if -a<y<a:terms.append((weight,shift,'core'))
                elif a<y<b:terms.append((weight,shift,'plus'))
                elif -b<y<-a:terms.append((weight,shift,'minus'))
        def scalar(x):
            ep=(x/2).exp()
            ms=(ep*(res.jp(a-x)+res.jm(a+x))+res.eps/ep*(res.jm(a-x)+res.jp(a+x)))/2
            logm=(b-x).log()-(a-x).log();logp=(b+x).log()-(a+x).log()
            vlog=-((a-x).log()+(a+x).log()-2*a.log())/2
            shell=(ell(x)*logm+quot(x)+res.eps*(ell(-x)*logp+quot(-x)))/2+gamma(x)
            prime=sum((wt*(ac*res.m(x+sh)if kind=='core'else ell(x+sh)if kind=='plus'else res.eps*ell(-x-sh))for wt,sh,kind in terms),arb(0))
            return ac*ms-shell-prime-(dp(x/a)+dv(x/a)*vlog+dm*res.m(x))/(2*a).sqrt()
        records[scalar]={'dp':dp,'terms':terms}
        return scalar
    def cell(lo,hi):
        mid=(lo+hi)/2
        key=sum(1 for cut in bounds if mid>cut)
        if key not in cache:cache[key]=scalar_cell(lo,hi)
        return cache[key]
    res.cell=cell
    ns['hfun']=lambda fun,x:fun(x)
    ns['_scalar_model']={'ell':ell,'quot':quot,'gamma':gamma,'dv':dv,'dm':dm,'ac':ac,'records':records}
    return {'cauchy_correction':corr,'shell_cauchy_correction':sc,'cell_cache':cache}
