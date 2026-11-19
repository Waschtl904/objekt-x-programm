"""Complete old core sources, with exact logarithms and every prime shift.

Order: 191 Q8 Phi columns, four Q9 z, eight Q9 Lambda Y, 84 Q9 Lambda J.
Functions are physical (unscaled) and not yet projected against the moment.
"""
from math import factorial, comb
from fractions import Fraction
from flint import arb, arb_poly, arb_series, arb_mat, ctx
from common import q, box, mat, ratmat, need, mellin, pint, Poly, columns, dot, norm


def mirror(p):
    return arb_poly([(-1)**k*v for k,v in enumerate(p)])


def gamma_coefficients(n):
    ctx.cap=n+2
    co=arb_series([arb(1)/factorial(j) if j%2==0 else arb(0) for j in range(n+2)],prec=n+2)
    sh=arb_series([arb(1)/factorial(j+1) if j%2==0 else arb(0) for j in range(n+2)],prec=n+2)
    pc=1/co;ps=1/sh
    return [(pc[k]+ps[k+1])/4 for k in range(n+1)]


def kernel(poly, ls, a, cs, parity):
    moments=[sum((ls[n]*q((-1)**n*2**(k+1)*factorial(k)**2)/
                        (factorial(k-n)*factorial(k+n+1))
                        for n in range(parity,min(k,len(ls)-1)+1,2)),arb(0))
             for k in range(len(cs))]
    previous=[];out=arb_poly([]);power=arb(1)
    for k,w in enumerate(cs):
        if k==0:
            ak=arb_poly([moments[0]])
        else:
            rhs=poly*2 if k==1 else previous[k-2]*(k*(k-1))
            arr=[arb(0),arb(0)]+[rhs[j]/((j+1)*(j+2)) for j in range(len(rhs))]
            if parity==0:arr[0]=moments[k]-sum(arr,arb(0))
            else:arr[1]=k*moments[k-1]-sum((j*arr[j] for j in range(len(arr))),arb(0))
            for j in range(1-parity,len(arr),2):
                need(arr[j].contains(0),'Gamma action parity')
                arr[j]=arb(0)
            ak=arb_poly(arr)
        previous.append(ak)
        out+=ak*(a*w*power)
        power*=a/2
    return out


def log_moments(root, n):
    """Exact integral of t^k log|t-root| on [0,1]."""
    if root == 1:
        H=arb(0);out=[]
        for k in range(n):
            H+=arb(1)/(k+1);out.append(-H/(k+1))
        return out
    powers=[root**k for k in range(n+1)]
    L=abs(1-root).log();D=L-abs(root).log()
    return [(L-sum((powers[j]/(k-j+1) for j in range(k+1)),arb(0))-powers[k+1]*D)/(k+1)
            for k in range(n)]


class OldFields:
    def __init__(self,inputs,res):
        p=res.sigma;eps=res.eps;a=res.a8;b=res.a;hs=b-a
        self.res=res;self.a=a;self.r=b/a
        leg=res.legs;self.degree=544
        self.roots={None:None,'one':arb(1),'minus_one':arb(-1),'outer':b/a,'minus_outer':-b/a}
        common=inputs.json('common')['cases'][p]
        raw=inputs.json('old_sources')['cases'][p]
        old=inputs.json('a8_model')
        oldcs=list(map(q,old['Gamma_polynomial_coefficients']))
        newcs=gamma_coefficients(224)
        self.phi=[];self.beta=[]
        base=mellin(p,a)*arb(2*p+1).sqrt()
        self.global_fields=[];self.prime_builders=[]
        for j,n in enumerate(range(p+2,384,2)):
            beta=arb(2*n+1).sqrt()*mellin(n,a)/base
            self.beta.append(beta)
            ls=[arb(0)]*(n+1);ls[n]=(arb(2*n+1)/(2*a)).sqrt();ls[p]=-beta*(arb(2*p+1)/(2*a)).sqrt()
            f=leg[n]*ls[n]+leg[p]*ls[p]
            self.phi.append(f)
            hn=sum((arb(1)/k for k in range(1,n+1)),arb(0))
            hp=arb(0) if p==0 else arb(1)
            smooth=leg[n]*(ls[n]*hn)+leg[p]*(ls[p]*hp)+f*(-(2*arb.pi()*a).log()-arb.const_euler())-kernel(f,ls,a,oldcs,p)
            self.global_fields.append({None:smooth,'one':f*(-arb(1)/2),'minus_one':f*(-arb(1)/2)})
            self.prime_builders.append(('inner',f))
            if j%48==0:print(res.parity,'old QPhi',j,flush=True)
        # Four complete old physical z sources, with the a9 boundary logs intact.
        self.z=[]
        for n in range(p+2,p+10,2):
            beta=arb(2*n+1).sqrt()*mellin(n,b)/(arb(2*p+1).sqrt()*mellin(p,b))
            ls=[arb(0)]*(n+1);ls[n]=(arb(2*n+1)/(2*b)).sqrt();ls[p]=-beta*(arb(2*p+1)/(2*b)).sqrt()
            f=leg[n]*ls[n]+leg[p]*ls[p];self.z.append(f)
            dh=sum((leg[k]*(ls[k]*sum((arb(1)/j for j in range(1,k+1)),arb(0))) for k in range(n+1)),arb_poly([]))
            smooth=dh+f*(-(2*arb.pi()*b).log()-arb.const_euler())-kernel(f,ls,b,newcs,p)
            f=f(arb_poly([0,a/b]));smooth=smooth(arb_poly([0,a/b]))
            self.global_fields.append({None:smooth+f*(b/a).log(),'outer':f*(-arb(1)/2),'minus_outer':f*(-arb(1)/2)})
            self.prime_builders.append(('outer',f))
        # The old Y and J bases use their physical W_X geometry.
        hb=inputs.json('half')['blocks'][p]
        Q=mat(hb['basis_Q_local_coefficients'])
        S=ratmat(hb['half_inverse_centre_rational_Q_coefficients'])
        D=ratmat(inputs.json('basis_'+res.parity)['D_rational'])
        Z=arb_mat([[D[i,j] if i<8 else int(i-8==j) for j in range(84)] for i in range(92)])
        check=S.transpose()*Z
        need(all(check[i,j].contains(0) for i in range(8) for j in range(84)), 'Exact T constraints')
        actual_Y=Q*S;actual_J=Q*Z
        frozen_Y=ratmat(inputs.json('frozen_Y_'+res.parity)['Y_local_rational_midpoints'])
        frozen_J=ratmat(inputs.json('frozen_J_'+res.parity)['working_basis_midpoints_rational'])
        self.round_Y=norm(actual_Y-frozen_Y);self.round_J=norm(actual_J-frozen_J)
        need(self.round_Y<q('1e-60') and self.round_J<q('1e-60'),'Bound old coordinate rounding')
        # Freeze in the well-conditioned local orthonormal coordinates. Keeping
        # independent interval copies through monomial composition loses their
        # common dependence and produces useless 10^160-sized interval radii.
        YJ=arb_mat([[frozen_Y[i,j] if j<8 else frozen_J[i,j-8] for j in range(92)]for i in range(96)])
        self.local=[];self.shell=[];self.lam=[]
        c=(a+b)/2;d=hs/2
        for j in range(92):
            f=sum((leg[k]*(YJ[k,j]*(arb(2*k+1)/(2*hs)).sqrt()) for k in range(96)),arb_poly([]))
            self.local.append(f);self.shell.append(f(arb_poly([-c/d,1/d])))
            self.lam.append(sum((YJ[k,j]*(hs*(2*k+1)/2).sqrt()*mellin(k,hs/2)*
                                 ((c/2).cosh() if (k+p)%2==0 else (c/2).sinh()) for k in range(96)),arb(0)))
        # Q8 m: Taylor error is charged separately; no endpoint log is truncated.
        self.mcore=mc=arb_poly([(a/2)**k/factorial(k) if k%2==p else arb(0) for k in range(161)])
        mls=[arb(0)]*161;mdh=arb_poly([])
        for n in range(p,161,2):
            mls[n]=(2*n+1)*pint(mc*leg[n])
            mdh+=leg[n]*(mls[n]*sum((arb(1)/k for k in range(1,n+1)),arb(0)))
        qm={None:mdh+mc*(-(2*arb.pi()*a).log()-arb.const_euler())-kernel(mc,mls,a,newcs,p),
            'one':mc*(-arb(1)/2),'minus_one':mc*(-arb(1)/2)}
        self.qm=qm
        fac=[arb(factorial(k)) for k in range(321)]
        convolution=arb_poly([newcs[k]/2**k*fac[k] for k in range(224,-1,-1)])
        for j,f in enumerate(self.shell):
            yc=f(arb_poly([0,a]))
            div=arb_poly([sum((f[k]*(b**(k-l)-a**(k-l))/(k-l) for k in range(l+1,len(f))),arb(0)) for l in range(len(f)-1)])(arb_poly([0,a]))
            ym=[pint(f*arb_poly([0]*k+[1]),a,b) for k in range(225)]
            conv=convolution*arb_poly([ym[k]/fac[k] for k in range(225)])
            regular=arb_poly([conv[224-l]/fac[l]*((-1)**l+eps)*a**l for l in range(225)])
            glob={None:(div+mirror(div)*eps)*(-arb(1)/2)-regular,
                  'outer':yc*(-arb(1)/2),'one':yc*(arb(1)/2),
                  'minus_outer':mirror(yc)*(-eps*arb(1)/2),'minus_one':mirror(yc)*(eps*arb(1)/2)}
            for tag,v in qm.items():glob[tag]=glob.get(tag,arb_poly([]))-v*(self.lam[j]/res.mu8)
            self.global_fields.append(glob)
            self.prime_builders.append(('shell',j))
            if j%24==0:print(res.parity,'old shell source',j,flush=True)
        need(len(self.global_fields)==287,'Source count')
        # Old finite models; their inherited source/coupling errors remain explicit.
        A=old['parities'][res.parity]['A']
        Am=arb_mat([[q(v[0]).union(q(v[1]))/10**100 for v in row] for row in A])
        cf=mat(raw['old_certificate']['source_c_model']);cj=mat(raw['galerkin']['old_low_c_model'])
        self.low=arb_mat([[Am[i,j] if j<191 else cf[i,j-191] if j<203 else cj[i,j-203]
                          for j in range(287)] for i in range(191)])
        self.C=arb_mat([[arb(int(v))/int(common['inverse_congruence_denominator']) for v in row] for row in common['inverse_congruence_integer_matrix']])
        self.delta=q(common['delta']);self.rho=q(common['rho'])
        # Every old and new prime discontinuity enters the common positive-core grid.
        # Deduplication is SYMBOLIC in the independent prime logarithms.
        # Numeric overlap alone is not a proof that two jump locations agree.
        lv={2:(1,0,0,0,0),3:(0,1,0,0,0),4:(2,0,0,0,0),
            5:(0,0,1,0,0),7:(0,0,0,1,0),8:(3,0,0,0,0),9:(0,2,0,0,0)}
        av=(Fraction(3,2),0,0,0,0);bv=lv[3];cv=(0,0,0,0,Fraction(1,2))
        subvec=lambda x,y:tuple(Fraction(u)-Fraction(v) for u,v in zip(x,y))
        candidates={subvec(bv,lv[2]),subvec(cv,lv[2]),subvec(cv,bv),
                    subvec(tuple(2*v for v in bv),cv)}
        for n in (4,5,7,8):
            candidates.add(subvec(lv[n],bv));candidates.add(subvec(lv[n],cv))
        for n,_ in res.channels:
            for edge in (av,bv):
                candidates.add(subvec(lv[n],edge));candidates.add(subvec(edge,lv[n]))
        logs=[arb(n).log() for n in (2,3,5,7,11)]
        cuts=[]
        for v in candidates:
            if not any(v) or v==av:continue
            at=dot(list(map(q,v)),logs)
            need(at>0 or at<0,'Unresolved nonzero jump root')
            need(at<a or at>a,'Unresolved non-endpoint jump root')
            if at>0 and at<a:cuts.append(at)
        cuts.sort(key=float)
        self.edges=[arb(0)]+cuts+[a]
        need(all(lo<hi for lo,hi in zip(self.edges[:-1],self.edges[1:])), 'Common jump order')
        self.global_matrices={tag:columns([f.get(tag,arb_poly([])) for f in self.global_fields]) for tag in self.roots}

    def prime_polys(self,lo,hi):
        a=self.a;b=self.res.a;p=self.res.sigma;eps=self.res.eps
        t=(lo+hi)/(2*a)
        def shifts(f,outer):
            out=arb_poly([])
            for n,prime in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2)):
                s=arb(n).log()/a;w=arb(prime).log()/arb(n).sqrt()
                for sign in (-1,1):
                    if abs(t+sign*s)<outer:out-=f(arb_poly([sign*s,1]))*w
            return out
        qmshift=shifts(self.mcore,arb(1));out=[]
        for kind,data in self.prime_builders:
            if kind in ('inner','outer'):
                out.append(shifts(data,arb(1) if kind=='inner' else b/a))
            else:
                j=data;f=self.shell[j];part=arb_poly([])
                for n,prime in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2)):
                    s=arb(n).log();w=arb(prime).log()/arb(n).sqrt()
                    for sign in (-1,1):
                        y=a*t+sign*s
                        if a<y<b:part-=f(arb_poly([sign*s,a]))*w
                        elif -b<y<-a:part-=f(arb_poly([-sign*s,-a]))*w*eps
                out.append(part-qmshift*(self.lam[j]/self.res.mu8))
        return out
