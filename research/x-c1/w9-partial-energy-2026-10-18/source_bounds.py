"""Analytic source bounds before reflected-polynomial cancellation is lost."""
from flint import arb,arb_poly
from common import Poly,q,ratmat,need
from old_fields import gamma_coefficients


class SourceBounds:
    def __init__(self,old,inp):
        self.old=old;a=old.a;b=old.res.a;hs=b-a
        Y=ratmat(inp.json('frozen_Y_'+old.res.parity)['Y_local_rational_midpoints'])
        J=ratmat(inp.json('frozen_J_'+old.res.parity)['working_basis_midpoints_rational'])
        self.sup=[]
        for A in (Y,J):
            for j in range(A.ncols()):
                self.sup.append(sum((abs(A[k,j]).upper()*(arb(2*k+1)/(2*hs)).sqrt()
                                     for k in range(96)),arb(0)))
        self.qm={tag:Poly(f(arb_poly([1,1])))for tag,f in old.qm.items()}
        radius=q('11/10')
        self.regular=sum((abs(v).upper()*radius**k for k,v in enumerate(gamma_coefficients(224))),arb(0))

    def ellipse(self,xx,prime_bounds):
        old=self.old;a=old.a;b=old.res.a;hs=b-a;tt=xx/a;u=tt-1
        need(xx.real<a and xx.real>-a,'Old shell source ellipse crosses the core boundary')
        need((b+abs(xx).upper())/2<q('11/10'),'Old regular-kernel disk')
        right=xx.real.upper();left=xx.real.lower()
        cauchy=(((b-right)/(a-right)).log()+((b+left)/(a+left)).log())/2
        qm=self.qm[None](u)+self.qm['one'](u)*(1-tt).log()+self.qm['minus_one'](u)*(1+tt).log()
        qm=abs(qm).upper()
        return [n*(cauchy+2*hs*self.regular)+abs(old.lam[j]/old.res.mu8).upper()*qm+prime_bounds[j]
                for j,n in enumerate(self.sup)]

    def tail_integrals(self,d,prime_bounds):
        old=self.old;a=old.a;b=old.res.a;hs=b-a
        need(0<d<hs and hs+d<1,'Old shell source tail range')
        tt=arb(1-d/(2*a),(d/a).upper()/2);u=tt-1
        qm_A=abs(self.qm['one'](u)).upper()
        qm_B=abs(self.qm[None](u)-self.qm['one'](u)*a.log()+self.qm['minus_one'](u)*(1+tt).log()).upper()
        regular_B=abs(hs.log()).upper()/2+hs/(2*(2*a-d))+2*hs*self.regular
        out=[]
        for j,n in enumerate(self.sup):
            factor=abs(old.lam[j]/old.res.mu8).upper()
            A=n/2+factor*qm_A
            B=n*regular_B+factor*qm_B+prime_bounds[j]
            out.append(d*(A*(1-d.log())+B))
        return out
