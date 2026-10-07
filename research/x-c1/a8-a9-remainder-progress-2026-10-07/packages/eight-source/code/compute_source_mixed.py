"""Actual 191x2 pairings B0 h for the complete high new source functions.
Uses complete analytic moments, no high-mode truncation of V or shifts.
The finite Gamma polynomial support is treated exactly in Legendre coordinates.
"""
from compute_inverse_energy_gate import *
from flint import arb_poly


def fresh_new_functions(parity,cells,original=None):
    """Rebuild new source action directly; avoid cancelling huge old actions.
    Reuses the already replayed 800-digit scalar/kernel formulas, then performs
    all new mixed integrations in Arb at separately selected precision.
    """
    if original is None:original=ROOT/'work/full-residual-review-2026-10-04/ObjektX_A8_Vollstaendige_Residuen_2026-10-04'
    sys.path.insert(0,str(original))
    import source_core as sc
    import full_gram as fg
    a=3*sc.log2()/2;b=sc.log_point(3);r=a/b;sr=r.sqrt()
    q0=-sc.log(2*sc.pi()*b)-sc.euler();coeff,_=sc.gamma_polynomial(128)
    vp=[sc.I(0)]*1281;pw=sc.I(1)
    for k in range(1,641):pw*=r*r;vp[2*k]=pw/(2*k)
    bases=[];cellsh=[[] for _ in cells]
    for col,m in enumerate([parity+2,parity+4]):
        profile=sc.profile(m,b);ls=[sc.I(0)]*(m+1)
        ls[m]=sc.I(2*m+1).sqrt();ls[parity]=-ls[m]*sc.mellin(m,b)/sc.mellin(parity,b)
        kernel=fg.kernel_action(profile['f'],ls,b,coeff,parity)
        smooth=sc.padd(sc.padd(profile['dh'],sc.pscale(profile['f'],q0)),sc.pscale(kernel,-1))
        base=sc.pscale(fg.scale_arg(smooth,r),sr)
        base=sc.padd(base,fg.pm(sc.pscale(fg.scale_arg(profile['f'],r),sr),vp))
        bases.append([box(v.frac()) for v in base])
        for idx,(l,h,_) in enumerate(cells):
            mid=sc.I(F(str(((l+h)/2).mid().fmpq())))
            sh=[sc.I(0)]
            for q,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
                d=sc.I(1) if q==3 else sc.log_point(q)/b
                w=sc.log_point(p)/sc.I(q).sqrt()
                for sign in [-1,1]:
                    loc=r*mid+sign*d
                    if loc.lo>-sc.S and loc.hi<sc.S:
                        sh=sc.padd(sh,sc.pscale(fg.scale_arg(fg.shifted(profile['f'],sign*d),r),-sr*w))
            cellsh[idx].append([box(v.frac()) for v in sh])
    return bases,[(l,h,cellsh[k]) for k,(l,h,_) in enumerate(cells)]


def add(a,b):
    return [(a[i] if i<len(a) else arb(0))+(b[i] if i<len(b) else arb(0)) for i in range(max(len(a),len(b)))]


def moment_sequence(t,n,weight=0):
    power=[arb(1)]
    for i in range(n+1):power.append(power[-1]*t)
    if not weight:return [power[k+1]/(k+1) for k in range(n+1)]
    if t.is_zero():return [arb(0)]*(n+1)
    if t==1:
        odd=arb(0);harm=arb(0);out=[];l2=arb(2).log()
        for k in range(n+1):
            if k%2==0:odd+=arb(1)/(k+1);out.append((odd-l2)/(k+1))
            else:harm+=arb(1)/((k+1)//2);out.append(harm/(2*(k+1)))
        return out
    assert t>0 and t<1
    lg=(1-t*t).log();at=((1+t).log()-(1-t).log())/2
    se=so=arb(0);out=[]
    for k in range(n+1):
        if k%2==0:
            se+=power[k+1]/(k+1);out.append(-(power[k+1]*lg+2*(at-se))/(2*(k+1)))
        else:
            so+=power[k+1]/(k+1);out.append(((1-power[k+1])*lg/2+so)/(k+1))
    return out


def polynomial_moments(poly,l,h,n,weight=0):
    d=len(poly)-1
    ml=moment_sequence(l,n+d,weight);mh=moment_sequence(h,n+d,weight)
    seq=[b-a for a,b in zip(ml,mh)]
    conv=arb_poly(list(reversed(poly)))*arb_poly(seq)
    return [conv[d+k] for k in range(n+1)]


def legendre(n,shift=None):
    x=arb_poly([0 if shift is None else shift,1]);pol=[arb_poly([1]),x]
    for k in range(2,n+1):pol.append(((2*k-1)*x*pol[-1]-(k-1)*pol[-2])*(arb(1)/k))
    return pol[:n+1]


def pair(poly,mom,n):
    return sum((poly[k]*mom[k] for k in range(n+1)),arb(0))*arb(2*n+1).sqrt()


def run(args):
    assert __debug__ and not args.out.exists();ctx.prec=args.bits
    assert flint.__version__=='0.9.0'
    paths={
        'functions':ROOT/'work/full-residual-review-2026-10-04/full-residual-replay/numerical/FUNCTIONS.json',
        'a8':ROOT/'outputs/a8_model.json.gz',
        'audit':ROOT/'outputs/Objekt-X-A8-Vollstaendige-Residuen-Pruefung-2026-10-04/AUDIT_COMPLETE.json',
        'rhs':ROOT/'work/cross764-review-2026-10-04/cross764-replay-lf-complete/RHS_ERROR_BUDGET.json',
        'solutions':ROOT/'work/full-residual-review-2026-10-04/full-residual-replay/sources/SOLUTIONS.json',
    }
    if args.inputs:
        names={'functions':'FUNCTIONS.json','a8':'a8_model.json.gz','audit':'AUDIT_COMPLETE.json','rhs':'RHS_ERROR_BUDGET.json','solutions':'SOLUTIONS.json'}
        paths={k:args.inputs/v for k,v in names.items()}
    data={};bindings={}
    for name,path in paths.items():
        raw=path.read_bytes();bindings[name]=hashlib.sha256(raw).hexdigest()
        data[name]=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
    assert bindings['functions']=='fccfff9abcd99afa1c9cdfaf9ae7fdcdbe6d1b7afc799180da3ec5c34f8f134d'
    assert bindings['a8']=='5f8935d53f8518540ef25e6f2d511955bad688cf5905cb63e8d89f03aae2474b'
    aa=3*arb(2).log()/2;maxn=544;pol=legendre(maxn)
    up=[1/(arb(2*n+1)*arb(2*n+3)).sqrt() for n in range(550)]
    coeff=list(map(F,data['a8']['Gamma_polynomial_coefficients']))
    weights={k:2*aa*af(coeff[k])*(aa/2)**k*factorial(k) for k in range(1,161,2)}
    blocks=[]
    for parity,label in enumerate(['even','odd']):
        print(label+': building complete new-source moments',flush=True)
        f=data['functions']['blocks'][parity]
        gp=[];cells=[]
        for j in range(2):
            base=[box(v) for v in f['smooth_base'][j]]
            old=[box(v) for v in f['old_smooth_action'][j]]
            gp.append(add(base,old))
        for cell,ocell in zip(f['positive_cells'],f['old_shift_cells']):
            l=box(cell['lo']);h=box(cell['hi']);sh=[]
            assert cell['lo']==ocell['lo'] and cell['hi']==ocell['hi']
            for j in range(2):
                a=add([box(v) for v in cell['shift_polynomials'][j]],[box(v) for v in ocell['shift_polynomials'][j]])
                degree=parity+2+2*j
                assert all(v.contains(0) for v in a[degree+1:])
                sh.append(a[:degree+1])
            cells.append((l,h,sh))
        freshbase,freshcells=fresh_new_functions(parity,cells,args.inputs.parent/'vendor' if args.inputs else None)
        for j in range(2):
            for k in range(max(len(gp[j]),len(freshbase[j]))):
                v=gp[j][k] if k<len(gp[j]) else arb(0)
                w=freshbase[j][k] if k<len(freshbase[j]) else arb(0)
                assert v.overlaps(w)
        for (_,_,oldsh),(_,_,newsh) in zip(cells,freshcells):
            for j in range(2):
                for k in range(max(len(oldsh[j]),len(newsh[j]))):
                    assert (oldsh[j][k] if k<len(oldsh[j]) else arb(0)).overlaps(newsh[j][k] if k<len(newsh[j]) else arb(0))
        gp=freshbase;cells=freshcells
        print(label+': fresh direct source polynomials agree with archived functions',flush=True)
        gm=[]
        for j in range(2):
            mu=polynomial_moments(gp[j],arb(0),arb(1),maxn)
            for l,h,sh in cells:
                v=polynomial_moments(sh[j],l,h,maxn)
                mu=[a+b for a,b in zip(mu,v)]
            gm.append([pair(pol[n],mu,n) if n%2==parity else arb(0) for n in range(maxn+1)])
        moments=data['a8']['raw_low_moments'];cn=[]
        cs={(r['n'],r['m']):af(r['value']) for r in data['rhs']['blocks'][parity]['rational_model_midpoints']}
        worst=arb(0)
        for n in range(parity+2,384,2):
            c=af(F(2*n+1,2*parity+1)).sqrt()*box(moments[n],10**100)/box(moments[parity],10**100);cn.append(c)
            for j in range(2):
                diff=gm[j][n]-c*gm[j][parity]-cs[n,parity+2+2*j]
                assert abs(diff)<af('2e-33'),(label,n,j,diff)
                worst=max(worst,abs(diff).upper())
        print(label+': all 382 low pairings agree with source matrix',flush=True)
        highbase=[]
        for j in range(2):
            projection=arb_poly([])
            for n in range(parity,384,2):projection+=pol[n]*(gm[j][n]*arb(2*n+1).sqrt())
            highbase.append(add(gp[j],[-projection[k] for k in range(384)]))
        vforce=[]
        for j in range(2):
            vm=polynomial_moments(highbase[j],arb(0),arb(1),383,1)
            for l,h,sh in cells:
                vv=polynomial_moments(sh[j],l,h,383,1);vm=[a+b for a,b in zip(vm,vv)]
            vforce.append([pair(pol[n],vm,n) if n%2==parity else arb(0) for n in range(384)])
        print(label+': complete logarithmic pairings integrated',flush=True)
        specs=[]
        for q,p in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
            d=af(F(2 if q==2 else 4,3)) if q in (2,4) else arb(q).log()/aa
            w=arb(p).log()/arb(q).sqrt()
            for sign in [-1,1]:specs.append((sign*d,w,legendre(383,sign*d)))
        shift=[[arb(0) for _ in range(384)] for _ in range(2)]
        for cellidx,(l,h,sh) in enumerate(cells):
            cm=[polynomial_moments(add(highbase[j],sh[j]),l,h,383) for j in range(2)]
            mid=(l+h)/2
            for t,w,pols in specs:
                if mid+t>-1 and mid+t<1:
                    # The source-bound ten-cell partition includes every old break.
                    assert l+t>-1 or (l+t).contains(-1)
                    assert h+t<1 or (h+t).contains(1)
                    for n in range(parity,384,2):
                        for j in range(2):shift[j][n]+=w*pair(pols[n],cm[j],n)
            print(label+': shift cell '+str(cellidx+1)+'/10',flush=True)
        kmix=[[arb(0),arb(0)] for _ in range(191)]
        first=384+parity
        for row,n in enumerate(range(parity+2,384,2)):
            if n+160<first:continue
            power={n:arb(1)}
            for order in range(1,161):
                nxt={}
                for k,v in power.items():
                    nxt[k+1]=nxt.get(k+1,arb(0))+v*up[k]
                    nxt[k-1]=nxt.get(k-1,arb(0))-v*up[k-1]
                power=nxt
                if order%2==0:
                    weight=weights[order-1]
                    for j in range(2):kmix[row][j]+=weight*sum((v*gm[j][k] for k,v in power.items() if k>=first),arb(0))
        print(label+': complete polynomial Gamma pairings integrated',flush=True)
        mixed=arb_mat(191,2)
        for row,n in enumerate(range(parity+2,384,2)):
            for j in range(2):
                mixed[row,j]=vforce[j][n]-cn[row]*vforce[j][parity]-shift[j][n]+cn[row]*shift[j][parity]-kmix[row][j]
        source_gram=arb_mat([[box(v) for v in row] for row in data['audit']['blocks'][parity]['new_restricted_model_action_gram']])
        highgram=arb_mat([[source_gram[i,j]-sum((gm[i][n]*gm[j][n] for n in range(parity,384,2)),arb(0)) for j in range(2)] for i in range(2)])
        # A different complete Gram route, already audited in the previous package,
        # supplies all four contractions against the large fixed old proposals.
        carold=[]
        for j in range(2):
            oq=[box(v) for v in f['old_smooth_action'][j]]
            pp=[box(v) for v in f['old_polynomial'][j]]
            cv=polynomial_moments(oq,arb(0),arb(1),parity)[parity]+polynomial_moments(pp,arb(0),arb(1),parity,1)[parity]
            for cell in f['old_shift_cells']:
                cv+=polynomial_moments([box(v) for v in cell['shift_polynomials'][j]],box(cell['lo']),box(cell['hi']),parity)[parity]
            carold.append(cv*arb(2*parity+1).sqrt())
        proposal=arb_mat([[af(v) for v in row] for row in data['solutions']['blocks'][parity]['proposal']])
        oldA=arb_mat([[box(v,10**100) for v in row] for row in data['a8']['parities'][label]['A']])
        lowold=oldA*proposal
        for i in range(191):
            for j in range(2):lowold[i,j]+=cn[i]*carold[j]
        target=arb_mat(2,2)
        for i in range(2):
            for j in range(2):
                target[i,j]=box(data['audit']['blocks'][parity]['new_old_mixed_model_gram'][j][i])-carold[i]*gm[j][parity]-sum((lowold[k,i]*gm[j][parity+2+2*k] for k in range(191)),arb(0))
        got=proposal.transpose()*mixed
        assert all(got[i,j].overlaps(target[i,j]) for i in range(2) for j in range(2)),(label,got,target)
        max_width=max(2*mixed[i,j].rad().upper() for i in range(191) for j in range(2))
        assert max_width<af('1e-40'),(label,'mixed enclosures too wide',max_width)
        assert all(2*got[i,j].rad()<af('1e-25') for i in range(2) for j in range(2))
        print(label+': four independent complete mixed-Gram contractions agree',flush=True)
        blocks.append({'parity':label,'B0_raw_high_new_model_pairings':mixed,'new_raw_high_model_gram':highgram,
            'low_pairing_checks':382,'maximum_low_pairing_discrepancy':worst,'gamma_high_support_ends_at':543,
            'gamma_method':'Exact Legendre primitive recurrence; all old carrier Gamma terms have raw degree below 384.',
            'kernel_pairings':kmix,'mixed_contractions_with_fixed_proposals':got,'independent_complete_gram_contractions':target,'independent_complete_contractions_checked':4,
            'max_mixed_entry_width':max_width,'source_polynomials_freshly_recomputed':True})
    result={'status':'COMPLETE_MODEL_SOURCE_MIXED_PAIRINGS','bits':args.bits,'bindings':bindings,'blocks':blocks,
        'high_mode_truncation_of_log_or_shift':False,'target_positivity_used':False,'github_changed':False}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(serial(result),indent=2)+'\n',encoding='utf-8',newline='\n')
    print('DONE '+str(args.out),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--bits',type=int,default=3072);ap.add_argument('--inputs',type=Path)
    run(ap.parse_args())
