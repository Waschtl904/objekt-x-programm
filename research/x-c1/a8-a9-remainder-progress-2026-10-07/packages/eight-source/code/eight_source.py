"""Fixed eight-source experiment. Directed arithmetic; no target positivity.

The old analytic form identities and two original operator models are inputs.
This program extends the previously published mixed-source / inverse-energy rule.
"""
from pathlib import Path
import sys, json, gzip, hashlib, argparse, time
from fractions import Fraction as F
from math import factorial

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
sys.path[:0]=[str(ROOT/'work/inverse-energy-deps'), str(ROOT/'work')]
from compute_inverse_energy_gate import af, box, serial, loewner_bounds, ldl, inverse_traces
from compute_source_mixed import legendre, polynomial_moments, moment_sequence, pair
from flint import arb, arb_mat, arb_poly, ctx
import flint
ORIGINAL=ROOT/'work/inverse-energy-repo-replay/original'
sys.path.insert(0,str(ORIGINAL/'vendor'))
import source_core as sc

NC=4
def say(x): print(time.strftime('%H:%M:%S')+' '+x,flush=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
    b=p.read_bytes()
    return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)
def eye(n): return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def mat(a): return arb_mat([[box(x) for x in row] for row in a])
def sym(a): return (a+a.transpose())/2
def upper(a): return loewner_bounds(sym(a))[1]
def lower(a): return loewner_bounds(sym(a))[0]
def coeff(p): return [p[k] for k in range(len(p))]
def ipoly(a): return arb_poly([box(x.frac()) for x in a])
def pint(poly,l=arb(0),h=arb(1),weight=0):
    return polynomial_moments(coeff(poly),l,h,0,weight)[0] if len(poly) else arb(0)
def positive(a): return ldl(a)[2] is None
def sub(a,n): return arb_mat([[a[i,j] for j in range(n)] for i in range(n)])
def mid_decimal(v,digits=100):
    s=10**digits
    return af(F(int((v.mid()*s).floor().unique_fmpz()),s))

def kernel(poly,ls,t,cs,p):
    """Complete polynomial regular Gamma action, with exact endpoint moments."""
    moments=[]
    for k in range(len(cs)):
        moments.append(sum((ls[n]*af(F((-1)**n*2**(k+1)*factorial(k)**2,
                         factorial(k-n)*factorial(k+n+1)))
                         for n in range(p,min(k,len(ls)-1)+1,2)),arb(0)))
    previous=[];out=arb_poly([]);power=arb(1)
    for k,w in enumerate(cs):
        if k==0: ak=arb_poly([moments[0]])
        else:
            rhs=poly*2 if k==1 else previous[k-2]*(k*(k-1))
            arr=[arb(0),arb(0)]+[rhs[j]/((j+1)*(j+2)) for j in range(len(rhs))]
            if p==0: arr[0]=moments[k]-sum(arr,arb(0))
            else: arr[1]=k*moments[k-1]-sum((j*arr[j] for j in range(len(arr))),arb(0))
            for j in range(1-p,len(arr),2):
                assert arr[j].contains(0);arr[j]=arb(0)
            ak=arb_poly(arr)
            if p==0: assert (ak.derivative()(arb(1))-k*moments[k-1]).contains(0)
            else: assert (ak(arb(1))-moments[k]).contains(0)
        previous.append(ak)
        if w:out+=ak*(t*af(w)*power)
        power*=t/2
    return out

def scale_arg(poly,r): return arb_poly([poly[k]*r**k for k in range(len(poly))])
def shifted(poly,t): return poly(arb_poly([t,1]))

def make_sources(p,cells,pol):
    ai=3*sc.log2()/2;bi=sc.log_point(3)
    a=box(ai.frac());b=box(bi.frac());r=a/b;sr=r.sqrt()
    newcs,eps=sc.gamma_polynomial(128)
    vp=[arb(0)]*1281
    for k in range(1,641):vp[2*k]=r**(2*k)/(2*k)
    tail=r**1282/(1282*(1-r*r))
    base=[];profiles=[];cn=[];cellsh=[[] for _ in cells]
    for m in range(p+2,p+10,2):
        pr=sc.profile(m,bi);f=ipoly(pr['f']);dh=ipoly(pr['dh'])
        c=arb(2*m+1).sqrt()/arb(2*p+1).sqrt()*box((sc.mellin(m,bi)/sc.mellin(p,bi)).frac())
        cn.append(c);profiles.append(f)
        ls=[arb(0)]*(m+1);ls[m]=arb(2*m+1).sqrt();ls[p]=-c*arb(2*p+1).sqrt()
        smooth=dh+f*(-(2*arb.pi()*b).log()-arb.const_euler())-kernel(f,ls,b,newcs,p)
        base.append(scale_arg(smooth,r)*sr+scale_arg(f,r)*sr*arb_poly(vp))
        for ci,(l,h) in enumerate(cells):
            mid=(l+h)/2;v=arb_poly([])
            for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
                d=arb(1) if q==3 else arb(q).log()/b
                w=arb(prime).log()/arb(q).sqrt()
                for sign in (-1,1):
                    loc=r*mid+sign*d
                    if loc>-1 and loc<1:
                        v-=scale_arg(shifted(f,sign*d),r)*sr*w
            cellsh[ci].append(v)
    W=arb_mat([[int(i==j)+cn[i]*cn[j] for j in range(NC)] for i in range(NC)])
    assert positive(lower(W))
    return base,cellsh,profiles,W,tail,af(eps)

def poly_gram(base,cellsh,cells):
    ans=arb_mat(NC,NC)
    for i in range(NC):
        for j in range(i,NC):
            v=pint(base[i]*base[j])
            for (l,h),sh in zip(cells,cellsh):
                v+=pint(base[i]*sh[j]+sh[i]*base[j]+sh[i]*sh[j],l,h)
            ans[i,j]=ans[j,i]=v
    return ans

def complete_mixed(p,pol,base,cellsh,cells,gm,cn,old):
    hp=[]
    for j in range(NC):
        projection=sum((pol[n]*(gm[j][n]*arb(2*n+1).sqrt()) for n in range(p,384,2)),arb_poly([]))
        hp.append(base[j]-projection)
    vf=[]
    for j in range(NC):
        mm=polynomial_moments(coeff(hp[j]),arb(0),arb(1),383,1)
        for (l,h),sh in zip(cells,cellsh):
            sm=polynomial_moments(coeff(sh[j]),l,h,383,1)
            mm=[v+w for v,w in zip(mm,sm)]
        vf.append([pair(pol[n],mm,n) if n%2==p else arb(0) for n in range(384)])
    say(('even' if p==0 else 'odd')+': complete logarithmic pairings')
    a=3*arb(2).log()/2;spec=[]
    for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
        d=af(F(2 if q==2 else 4,3)) if q in (2,4) else arb(q).log()/a
        w=arb(prime).log()/arb(q).sqrt()
        for sign in (-1,1):spec.append((sign*d,w,legendre(383,sign*d)))
    shifts=[[arb(0)]*384 for _ in range(NC)]
    for (l,h),sh in zip(cells,cellsh):
        mm=[polynomial_moments(coeff(hp[j]+sh[j]),l,h,383) for j in range(NC)]
        for t,w,pols in spec:
            if (l+h)/2+t>-1 and (l+h)/2+t<1:
                assert l+t>-1 or (l+t).contains(-1)
                assert h+t<1 or (h+t).contains(1)
                for n in range(p,384,2):
                    for j in range(NC):shifts[j][n]+=w*pair(pols[n],mm[j],n)
    up=[1/(arb(2*n+1)*arb(2*n+3)).sqrt() for n in range(550)]
    cs=list(map(F,old['Gamma_polynomial_coefficients']))
    weights={k:2*a*af(cs[k])*(a/2)**k*factorial(k) for k in range(1,161,2)}
    km=arb_mat(191,NC);first=384+p
    for row,n in enumerate(range(p+2,384,2)):
        if n+160<first:continue
        power={n:arb(1)}
        for order in range(1,161):
            nxt={}
            for k,v in power.items():
                nxt[k+1]=nxt.get(k+1,arb(0))+v*up[k]
                nxt[k-1]=nxt.get(k-1,arb(0))-v*up[k-1]
            power=nxt
            if order%2==0:
                for j in range(NC):km[row,j]+=weights[order-1]*sum((v*gm[j][k] for k,v in power.items() if k>=first),arb(0))
    mixed=arb_mat([[vf[j][n]-cn[row]*vf[j][p]-shifts[j][n]+cn[row]*shifts[j][p]-km[row,j]
                   for j in range(NC)] for row,n in enumerate(range(p+2,384,2))])
    assert all(2*mixed[i,j].rad()<af('1e-40') for i in range(191) for j in range(NC))
    say(('even' if p==0 else 'odd')+': all 764 mixed B0 h0 entries enclosed')
    return mixed

def full_residual(p,pol,base,cellsh,cells,P,old,cn,Craw,mixed,sourcegram,epsnew,tail,W):
    a=3*arb(2).log()/2;b=arb(3).log();qa=-(2*arb.pi()*a).log()-arb.const_euler()
    # Building high-degree action polynomials requires the analytic carrier,
    # not the much shorter 100-digit matrix-input moment boxes.
    ai=3*sc.log2()/2;den=sc.mellin(p,ai)
    cn_function=[af(F(2*n+1,2*p+1)).sqrt()*box((sc.mellin(n,ai)/den).frac()) for n in range(p+2,384,2)]
    assert all(v.overlaps(w) for v,w in zip(cn_function,cn))
    pp=[];oq=[];norm=[];oldsh=[[] for _ in cells]
    harmonics=[af(sc.H(n)) for n in range(384)]
    for j in range(NC):
        ls=[arb(0)]*384
        for row,n in enumerate(range(p+2,384,2)):ls[n]=P[row,j]*arb(2*n+1).sqrt()
        ls[p]=-sum((cn_function[row]*P[row,j] for row in range(191)),arb(0))*arb(2*p+1).sqrt()
        poly=sum((pol[n]*ls[n] for n in range(p,384,2)),arb_poly([]))
        dh=sum((pol[n]*(ls[n]*harmonics[n]) for n in range(p,384,2)),arb_poly([]))
        pp.append(poly);oq.append(dh+poly*qa-kernel(poly,ls,a,list(map(F,old['Gamma_polynomial_coefficients'])),p))
        norm.append((sum((P[i,j]**2 for i in range(191)),arb(0))+ls[p]**2/(2*p+1)).sqrt())
        shspec=[]
        for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
            d=af(F(2 if q==2 else 4,3)) if q in (2,4) else arb(q).log()/a
            w=arb(prime).log()/arb(q).sqrt()
            for sign in (-1,1):shspec.append((sign*d,shifted(poly,sign*d)*(-w)))
        for idx,(l,h) in enumerate(cells):
            v=arb_poly([])
            for t,sp in shspec:
                if (l+h)/2+t>-1 and (l+h)/2+t<1:v+=sp
            oldsh[idx].append(v)
        say(('even' if p==0 else 'odd')+': complete old action '+str(j+1)+'/4')
    rb=[base[j]-oq[j] for j in range(NC)]
    rsh=[[s[j]-o[j] for j in range(NC)] for s,o in zip(cellsh,oldsh)]
    v2=[];odd=arb(0);odd2=arb(0)
    for k in range(767):
        if k%2==0:
            odd+=arb(1)/(k+1);odd2+=arb(1)/(k+1)**2
            v2.append(((odd-arb(2).log())**2+odd2-arb.pi()**2/12)/(k+1))
        else:v2.append(arb(0))
    def log2int(poly):return sum((poly[k]*v2[k] for k in range(len(poly))),arb(0))
    raw=arb_mat(NC,NC);oldgram=arb_mat(NC,NC);newold=arb_mat(NC,NC)
    for i in range(NC):
        for j in range(i,NC):
            v=pint(rb[i]*rb[j])-pint(rb[i]*pp[j]+pp[i]*rb[j],weight=1)+log2int(pp[i]*pp[j])
            o=pint(oq[i]*oq[j])+pint(oq[i]*pp[j]+pp[i]*oq[j],weight=1)+log2int(pp[i]*pp[j])
            for (l,h),sh,osh in zip(cells,rsh,oldsh):
                v+=pint(rb[i]*sh[j]+sh[i]*rb[j]+sh[i]*sh[j],l,h)-pint(pp[i]*sh[j]+sh[i]*pp[j],l,h,1)
                o+=pint(oq[i]*osh[j]+osh[i]*oq[j]+osh[i]*osh[j],l,h)+pint(pp[i]*osh[j]+osh[i]*pp[j],l,h,1)
            raw[i,j]=raw[j,i]=v;oldgram[i,j]=oldgram[j,i]=o
        for j in range(NC):
            v=pint(base[i]*oq[j])+pint(base[i]*pp[j],weight=1)
            for (l,h),sh,osh in zip(cells,cellsh,oldsh):
                v+=pint(base[i]*osh[j]+sh[i]*oq[j]+sh[i]*osh[j],l,h)+pint(sh[i]*pp[j],l,h,1)
            newold[i,j]=v
    alternate=sourcegram+oldgram-newold-newold.transpose()
    assert all(raw[i,j].overlaps(alternate[i,j]) for i in range(NC) for j in range(NC))
    mu_poly=arb_poly([(a/2)**k/factorial(k) if k%2==p else arb(0) for k in range(201)])
    mtail=(a/2)**201/factorial(201)/(1-a/(2*202))
    mu0=pint(mu_poly*mu_poly);mu=mu0+arb(0,(2*mu0.upper().sqrt()*mtail+mtail**2).upper())
    bp=[];car=[]
    for j in range(NC):
        v=pint(rb[j]*mu_poly)-pint(pp[j]*mu_poly,weight=1)
        co=pint(oq[j]*pol[p])*arb(2*p+1).sqrt()+pint(pp[j]*pol[p],weight=1)*arb(2*p+1).sqrt()
        for (l,h),sh,osh in zip(cells,rsh,oldsh):
            v+=pint(sh[j]*mu_poly,l,h)
            co+=pint(osh[j]*pol[p],l,h)*arb(2*p+1).sqrt()
        bp.append(v+arb(0,(raw[j,j].upper().sqrt()*mtail).upper()));car.append(co)
    projected=arb_mat([[raw[i,j]-bp[i]*bp[j]/mu for j in range(NC)] for i in range(NC)])
    err=[2*a*af(old['Gamma_kernel_error_exact'])*norm[j]+(2*b*epsnew+tail)*W[j,j].sqrt() for j in range(NC)]
    true=arb_mat([[projected[i,j]+arb(0,(projected[i,i].upper().sqrt()*err[j]+projected[j,j].upper().sqrt()*err[i]+err[i]*err[j]).upper()) for j in range(NC)] for i in range(NC)])
    assert all(raw[j,j]>0 and projected[j,j]>0 for j in range(NC))
    assert all(2*raw[i,j].rad()<af('1e-25') for i in range(NC) for j in range(NC)), 'Uninformative full-function Gram enclosure'
    # Independent complete Gram contraction of the newly integrated B0 h0.
    Am=arb_mat([[box(v,10**100) for v in row] for row in old['parities']['even' if p==0 else 'odd']['A']])
    lowold=Am*P
    for k in range(191):
        for j in range(NC):lowold[k,j]+=cn[k]*car[j]
    target=arb_mat([[newold[j,i]-car[i]*Craw[j][p]-sum((lowold[k,i]*Craw[j][p+2+2*k] for k in range(191)),arb(0)) for j in range(NC)] for i in range(NC)])
    got=P.transpose()*mixed
    assert all(got[i,j].overlaps(target[i,j]) for i in range(NC) for j in range(NC))
    assert all(2*got[i,j].rad()<af('1e-25') for i in range(NC) for j in range(NC))
    assert all(2*target[i,j].rad()<af('1e-25') for i in range(NC) for j in range(NC))
    say(('even' if p==0 else 'odd')+': full 4x4 residual Gram and 16 independent contractions checked')
    return {'complete_true_residual_gram':true,'unprojected_model_gram':raw,'projected_model_gram':projected,
            'mellin_projection_pairings':bp,'mellin_function_norm_squared':mu,'function_error_norms':err,
            'old_source_norms':norm,'new_restricted_model_action_gram':sourcegram,'old_model_action_gram':oldgram,
            'new_old_mixed_model_gram':newold,'independent_contractions':target,'mixed_contractions':got,
            'complete_gram_alternate_route_overlap':True,'independent_contractions_checked':16}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=3072);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();assert __debug__ and flint.__version__=='0.9.0' and not args.out.exists()
    ctx.prec=args.bits;args.out.mkdir(parents=True)
    inp=ORIGINAL/'inputs'
    paths={k:inp/v for k,v in {'a8':'a8_model.json.gz','a9':'a9_model.json.gz','solutions':'SOLUTIONS.json','functions':'FUNCTIONS.json','rhs':'RHS_ERROR_BUDGET.json','prior_gram':'FULL_GRAM.json'}.items()}
    data={k:read(v) for k,v in paths.items()};bindings={k:sha(v) for k,v in paths.items()}
    assert bindings['a8']=='5f8935d53f8518540ef25e6f2d511955bad688cf5905cb63e8d89f03aae2474b'
    assert bindings['a9']=='a1cb251d5563cffb01eec3fbbf11c891851b677bd4f4ec7f5fba37164d14ab72'
    old=data['a8'];new=data['a9'];pol=legendre(544);a=3*arb(2).log()/2;b=arb(3).log()
    gammaa=af(F(21,10)*F(old['Gamma_kernel_error_exact']));gammab=af(F(11,5)*F(new['Gamma_kernel_error_exact']))
    oldmixed=read(ORIGINAL/'expected/SOURCE_MIXED_3072.json')
    blocks=[]
    for p,label in enumerate(['even','odd']):
        start=time.time();say(label+': fixed eight-source run begins')
        cells=[(box(c['lo']),box(c['hi'])) for c in data['functions']['blocks'][p]['positive_cells']]
        base,cellsh,profiles,W,vtail,epsnew=make_sources(p,cells,pol)
        gm=[]
        for j in range(NC):
            mm=polynomial_moments(coeff(base[j]),arb(0),arb(1),544)
            for (l,h),sh in zip(cells,cellsh):mm=[v+w for v,w in zip(mm,polynomial_moments(coeff(sh[j]),l,h,544))]
            gm.append([pair(pol[n],mm,n) if n%2==p else arb(0) for n in range(545)])
        moments=old['raw_low_moments']
        cn=[af(F(2*n+1,2*p+1)).sqrt()*box(moments[n],10**100)/box(moments[p],10**100) for n in range(p+2,384,2)]
        gold=1+sum((v*v for v in cn),arb(0));assert gold<af('1.002')
        Cmod=arb_mat([[gm[j][n]-cn[row]*gm[j][p] for j in range(NC)] for row,n in enumerate(range(p+2,384,2))])
        C=arb_mat([[mid_decimal(Cmod[i,j]) for j in range(NC)] for i in range(191)])
        priorcs={(v['n'],v['m']):af(v['value']) for v in data['rhs']['blocks'][p]['rational_model_midpoints']}
        assert all(abs(Cmod[row,j]-priorcs[n,p+2+2*j])<af('2e-33') for row,n in enumerate(range(p+2,384,2)) for j in range(2))
        delta_source=2*b*epsnew+vtail;Wlo=lower(W);Whi=upper(W)
        midpoint_error=sum((abs(Cmod[i,j]-C[i,j])**2 for i in range(191) for j in range(NC)),arb(0)).upper()
        young=af('1e-20')
        BC=upper(Whi*((1+young)*gold.upper()*delta_source**2)+eye(NC)*((1+1/young)*midpoint_error))
        A=arb_mat([[box(v,10**100) for v in row] for row in old['parities'][label]['A']])
        A0=arb_mat([[af(sum(map(F,old['parities'][label]['A'][i][j]))/(2*10**100)) for j in range(191)] for i in range(191)])
        Praw=A0.solve(C)
        P=arb_mat([[af(data['solutions']['blocks'][p]['proposal'][i][j]) if j<2 else mid_decimal(Praw[i,j]) for j in range(NC)] for i in range(191)])
        GP=P.transpose()*P;E0=C-A0*P
        arad=max(sum((abs(A[i,j]-A0[i,j]) for j in range(191)),arb(0)).upper() for i in range(191))
        alpha=arad+gammaa*gold.upper()
        finite_error=upper((E0.transpose()*E0+BC+GP*alpha**2)*3)
        sourcegram=poly_gram(base,cellsh,cells)
        highgram=arb_mat([[sourcegram[i,j]-sum((gm[i][n]*gm[j][n] for n in range(p,384,2)),arb(0)) for j in range(NC)] for i in range(NC)])
        mixed=complete_mixed(p,pol,base,cellsh,cells,gm,cn,old)
        prev=mat(oldmixed['blocks'][p]['B0_raw_high_new_model_pairings'])
        assert all(mixed[i,j].overlaps(prev[i,j]) for i in range(191) for j in range(2))
        residual=full_residual(p,pol,base,cellsh,cells,P,old,cn,gm,mixed,sourcegram,epsnew,vtail,W)
        priorgram=mat(data['prior_gram']['blocks'][p]['complete_true_residual_gram'])
        assert all(residual['complete_true_residual_gram'][i,j].overlaps(priorgram[i,j]) for i in range(2) for j in range(2))
        D=arb_mat([[box(new['parities'][label]['A'][i][j],10**100) for j in range(NC)] for i in range(NC)])
        Dlo=lower(D-eye(NC)*4*gammab);Dhi=upper(D+eye(NC)*4*gammab)
        K0=D-sym(C.transpose()*P)-sym(P.transpose()*E0)
        tau=af('1e-32' if p==0 else '1e-31')
        KE=GP*(alpha+tau)+BC/tau+eye(NC)*4*gammab
        Klo=lower(K0-KE);Khi=upper(K0+KE)
        em=af(F(21,40)**(384+p)/factorial(384+p)/(1-F(21,40)**2/((385+p)*(386+p)))*(4 if p else 1))
        eb=2*gammaa+24*em;delta=af(F(2,3))
        HB=arb_mat([[box(v,10**100) for v in row] for row in old['parities'][label]['complete_model_raw_high_Gram']])*af(F(1001,1000))+eye(191)*1001*eb**2
        FF=A-eye(191)*4*gammaa-HB/delta
        _,piv,fail=ldl(FF);assert fail is None and len(piv)==191
        t,beta,ji,ie,invreceipt=inverse_traces(FF,HB)
        herr=[delta_source*W[j,j].sqrt()+em*(sourcegram[j,j].upper().sqrt()+delta_source*W[j,j].sqrt()) for j in range(NC)]
        assert all(x<af('7e-21') for x in herr)
        eh=eye(NC)*NC*af('7e-21')**2
        hh=upper(upper(highgram)*(1+af('1e-16'))+eh*(1+af('1e16')))
        v=C-mixed/delta
        V=upper(v.transpose()*ji*v+(v.transpose()*v)*ie)
        er=upper((BC*t.upper()+eh*(beta.upper()/delta**2)+hh*(t.upper()*eb**2/delta**2))*3)
        epsilon=af('1e-7')
        T=upper(hh/delta+V*(1+epsilon)+er*(1+1/epsilon))
        Gamma=upper(T+Khi-Dlo)
        Slow=lower(Klo-Gamma)
        # W is fixed before the solve; trial floors are numerical search aids.
        floors=[]
        for s in ['1e-2','1e-3','1e-4','1e-5','1e-6','1e-7','1e-8','1e-9','1e-10','1e-12','1e-14','1e-16','1e-20','1e-30']:
            if positive(Slow-Whi*af(s)):floors.append(s)
        record={'parity':label,'degrees':list(range(p+2,p+10,2)),'reference_gram':W,'reference_gram_lower':Wlo,'reference_gram_upper':Whi,
          'source_pairings_model':Cmod,'source_pairings_midpoint':C,'source_error_gram_upper':BC,'source_error_operator_bound':delta_source,
          'proposal':P,'finite_midpoint_residual':E0,'finite_residual_gram_upper':finite_error,'old_profile_gram_norm_upper':gold.upper(),
          'B0_h0':mixed,'new_raw_high_model_gram':highgram,'true_high_gram_upper':hh,'high_source_error_column_upper':herr,
          'K_model':K0,'K_lower':Klo,'K_upper':Khi,'D_model':D,'D_lower':Dlo,'D_upper':Dhi,'Gamma_upper':Gamma,'S_lower':Slow,
          'K_error_components':{'old_matrix':GP*alpha,'young_proposal':GP*tau,'young_source':BC/tau,'target_form':eye(NC)*4*gammab},
          'corrected_source_force':v,'corrected_source_energy_upper':V,'force_error_gram_upper':er,'old_source_inverse_energy_upper':T,
          'old_schur_pivots':len(piv),'old_inverse_trace':t,'weighted_coupling_trace':beta,'inverse_check':invreceipt,
          'separate_positive':positive(Slow),'certified_trial_relative_floors':floors,
          'two_source_subblock_positive':positive(sub(Slow,2)),'full_residual':residual,
          'regressions':{'old_mixed_entries_overlap':764//2,'prior_residual_gram_overlap':True,'original_two_proposals_preserved':True},
          'seconds':time.time()-start}
        blocks.append(record)
        (args.out/(label+'.json')).write_text(json.dumps(serial(record),indent=2)+'\n',encoding='utf-8')
        say(label+': lower matrix positive='+str(record['separate_positive'])+' relative floors='+str(floors))
    result={'status':'COMPLETED_FIXED_EIGHT_SOURCE_EXPERIMENT','bits':args.bits,'source_head':'040c1c2f75753d0daa680c55b14b88524955f851',
            'bindings':bindings,'protocol_sha256':sha(HERE/'PROTOCOL.json'),'program_sha256':sha(Path(__file__)),
            'blocks':blocks,'full_old_space_included':True,'full_new_quotient_covered':False,'target_positivity_used':False,'external_review':'OPEN','github_changed':False}
    (args.out/'RESULT.json').write_text(json.dumps(serial(result),indent=2)+'\n',encoding='utf-8')
    say('COMPLETE '+str(args.out))

if __name__=='__main__': main()
