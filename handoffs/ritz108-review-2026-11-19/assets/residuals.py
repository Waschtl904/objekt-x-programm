"""Twelve common analytic residual models; every prime cell is explicit."""
from math import factorial
from flint import arb, arb_poly, arb_series, arb_mat, ctx
from common import q, pad, legs, Poly, mellin, pint, need


def plogint(p, s):
    return sum((c*s**(k+1)*(s.log()/(k+1)-arb(1)/(k+1)**2)
                for k, c in enumerate(p)), arb(0))


class Residuals:
    def __init__(self, inputs, parity, degree=360):
        self.parity = parity
        self.sigma = p = int(parity == 'odd')
        self.eps = eps = (-1)**p
        self.a8 = a8 = 3*arb(2).log()/2
        self.a = a = arb(3).log()
        self.b = b = arb(11).log()/2
        self.hs = a-a8
        self.h = h = b-a
        self.mu8 = (a8*eps+a8.sinh())/2
        self.mu = mu = (a*eps+arb(4)/3)/2
        self.legs = leg = legs(545)
        ell = [leg[j](arb_poly([-1-2*a/h, 2/h]))*(arb(2*j+1)/(2*h)).sqrt()
               for j in range(12)]
        self.ell = [Poly(f) for f in ell]
        # Exact moment series, including its geometric tail.
        center = (a+b)/2
        lam = [(h*(2*j+1)/2).sqrt()*mellin(j,h/2)*
               ((center/2).cosh() if (j+p)%2 == 0 else (center/2).sinh())
               for j in range(12)]
        self.lam = lam
        self.GW = arb_mat([[int(i==j)+2*lam[i]*lam[j]/mu for j in range(12)] for i in range(12)])
        self.Ac = [-v/mu for v in lam]
        funcs = inputs.json('functions')['parities'][parity]['functions']
        self.funcs = funcs
        frozen = inputs.json('frozen_response')['parities'][parity]
        self.X = X = arb_mat([[q(v) for v in row] for row in frozen['X']])
        order = 120
        s = b/a-1
        lp = arb_poly([0]+[arb((-1)**(j+1))/(j*2**j) for j in range(1,order+1)])
        M = arb_poly([((a/2).cosh() if (p+j)%2==0 else (a/2).sinh())*(a/2)**j/factorial(j)
                      for j in range(order+1)])
        elog=(s/2)**(order+1)/((order+1)*(1-s/2))
        em=(b/2).exp()*(a*s/2)**(order+1)/factorial(order+1)
        def pn(f):
            return sum((abs(v).upper()*s**k for k,v in enumerate(f)),arb(0))
        W=[en(arb_poly([a,a]))+M*(lam[j]/mu) for j,en in enumerate(ell)]
        F=[]
        for fj in funcs:
            sp=fj['F']
            P=arb_poly(list(map(q,sp['polynomial'])))(arb_poly([1,1]))
            Q=arb_poly(list(map(q,sp['log_ratio_multiplier'])))(arb_poly([1,1]))
            cm=q(sp['physical_W_moment_multiplier'])
            pp=P+Q*(arb_poly([arb(2).log()])+lp)+cm*M
            er=pn(Q)*elog+abs(cm).upper()*em
            row=[]
            for j,ww in enumerate(W):
                ew=abs(lam[j]/mu).upper()*em
                error=s*er*(pn(ww)+ew)+ew*s*(pn(pp)+pn(Q)*(1-s.log()))
                row.append(2*a/(2*a).sqrt()*pad(pint(pp*ww,arb(0),s)-plogint(Q*ww,s),error))
            F.append(row)
        self.Fhat=arb_mat(F)
        self.T_enclosure=X*self.Fhat
        # Freeze the common coefficients before monomial moment accumulation.
        # Their directed enclosure is retained for a separate function error;
        # otherwise repeated interval copies destroy exact linear dependence.
        self.T=T=arb_mat([[q(self.T_enclosure[i,j].mid().fmpq()) for j in range(12)] for i in range(12)])
        self.Dpoly=[sum((T[i,j]*arb_poly(list(map(q,fj['D']['polynomial']))) for i,fj in enumerate(funcs)),arb_poly([])) for j in range(12)]
        self.Dv=[Poly(sum((T[i,j]*arb_poly(list(map(q,fj['D']['V_multiplier']))) for i,fj in enumerate(funcs)),arb_poly([]))) for j in range(12)]
        self.Dm=[sum((T[i,j]*q(fj['D']['moment_multiplier']) for i,fj in enumerate(funcs)),arb(0)) for j in range(12)]
        # Regular Gamma source: integrate the polynomial kernel in the shell
        # variable BEFORE evaluating the core variable. This preserves cancellation.
        ctx.cap=degree+2
        fac=[arb(factorial(j)) for j in range(degree+15)]
        sh=arb_series([1/fac[j+1] if j%2==0 else arb(0) for j in range(degree+2)],prec=degree+2)
        ex=arb_series([1/(2**j*fac[j]) for j in range(degree+2)],prec=degree+2)
        reg=(ex/sh)/2
        need(reg.prec>=degree+2,'Gamma series precision')
        g=[reg[j+1] for j in range(degree+1)]
        A=arb_poly([g[j]*fac[j] for j in range(degree,-1,-1)])
        moments=[(b**(j+1)-a**(j+1))/(j+1) for j in range(degree+12)]
        self.gamma=[];self.quot=[]
        for en in ell:
            muvec=[sum((c*moments[j+k] for k,c in enumerate(en)),arb(0)) for j in range(degree+1)]
            conv=A*arb_poly([v/fac[j] for j,v in enumerate(muvec)])
            self.gamma.append(Poly([conv[degree-k]/fac[k]*((-1)**k+eps) for k in range(degree+1)]))
            self.quot.append(Poly([sum((en[j]*moments[j-k-1] for j in range(k+1,len(en))),arb(0)) for k in range(len(en)-1)]))
        self.logs={n:arb(n).log() for n in (2,3,4,5,7,8,9)}
        self.channels=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
        cuts=[a-self.logs[2],b-self.logs[2],b-a]+[self.logs[k]-a for k in (4,5,7,8)]+[self.logs[k]-b for k in (4,5,7,8)]+[2*a-b]
        self.cuts=sorted(cuts,key=float)
        self.gamma_degree=degree

    def m(self,x):
        return (x/2).cosh() if self.sigma==0 else (x/2).sinh()

    @staticmethod
    def jp(r):
        return 3*arb(2).log()/2+arb.pi()/4-r-(1-(-2*r).exp()).log()/2

    @staticmethod
    def jm(r):
        v=(-r).exp()
        return arb(2).log()/2+arb.pi()/4-((1-v).log()-(1+v).log())/2

    def cell(self,lo,hi):
        a,b=self.a,self.b
        mid=(lo+hi)/2
        dp=[arb_poly(p) for p in self.Dpoly]
        terms=[]
        for i,fj in enumerate(self.funcs):
            for term in fj['D']['shift_terms']:
                sh=self.logs[int(term['channel'])]/a
                dl,dh=(arb(0),1-sh) if int(term['translation_sign'])==1 else (max(arb(0),sh-1),arb(1))
                if dl<mid/a<dh:
                    pp=arb_poly(list(map(q,term['polynomial'])))
                    for j in range(12): dp[j]+=self.T[i,j]*pp
        for n,prime in self.channels:
            for sign in (-1,1):
                shift=sign*self.logs[n];y=mid+shift;weight=arb(prime).log()/arb(n).sqrt()
                if -a<y<a:terms.append((weight,shift,'core'))
                elif a<y<b:terms.append((weight,shift,'plus'))
                elif -b<y<-a:terms.append((weight,shift,'minus'))
        dp=list(map(Poly,dp))
        def value(x):
            ep=(x/2).exp()
            ms=(ep*(self.jp(a-x)+self.jm(a+x))+self.eps/ep*(self.jm(a-x)+self.jp(a+x)))/2
            # All factors lie in the right half-plane on each accepted
            # ellipse. Separate analytic logarithms retain their dependence;
            # boxing a quotient first can spuriously enclose the origin.
            logm=(b-x).log()-(a-x).log();logp=(b+x).log()-(a+x).log()
            vlog=-((a-x).log()+(a+x).log()-2*a.log())/2;mx=self.m(x)
            out=[]
            for j in range(12):
                shell=(self.ell[j](x)*logm+self.quot[j](x)+self.eps*(self.ell[j](-x)*logp+self.quot[j](-x)))/2+self.gamma[j](x)
                prime=sum((w*(self.Ac[j]*self.m(x+sh) if kind=='core' else self.ell[j](x+sh) if kind=='plus' else self.eps*self.ell[j](-x-sh)) for w,sh,kind in terms),arb(0))
                out.append(self.Ac[j]*ms-shell-prime-(dp[j](x/a)+self.Dv[j](x/a)*vlog+self.Dm[j]*mx)/(2*a).sqrt())
            return out
        return value
