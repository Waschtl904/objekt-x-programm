"""Directed K and full old inverse-energy upper bounds on four fixed sources.
Only original A8 positivity is used. All new-terminal data are form entries.
"""
from pathlib import Path
import sys, json, gzip, hashlib, argparse, time
from fractions import Fraction as F
from math import factorial
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'work/inverse-energy-deps'))
import flint
from flint import arb, arb_mat, fmpq, ctx


def af(x):
    x=F(x)
    return arb(fmpq(x.numerator,x.denominator))


def box(pair,scale=None):
    l,h=map(F,pair)
    if scale: l/=scale;h/=scale
    assert l<=h
    return af((l+h)/2)+arb(0,af((h-l)/2))


def serial(v,digits=70):
    if isinstance(v,arb):
        s=10**digits
        return [str(F(int((v.lower()*s).floor().unique_fmpz()),s)),str(F(int((v.upper()*s).ceil().unique_fmpz()),s))]
    if isinstance(v,arb_mat):return [[serial(v[i,j],digits) for j in range(v.ncols())] for i in range(v.nrows())]
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {k:serial(x,digits) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [serial(x,digits) for x in v]
    return v


def trace_product(a,b):
    return sum((a[i,j]*b[j,i] for i in range(a.nrows()) for j in range(a.ncols())),arb(0))


def inverse_traces(a,h):
    n=a.nrows()
    mid=arb_mat([[a[i,j].mid() for j in range(n)] for i in range(n)])
    raw=mid.inv()
    jmat=arb_mat(n,n)
    for i in range(n):
        for j in range(i+1):
            v=((raw[i,j].mid()+raw[j,i].mid())/2).mid()
            jmat[i,j]=jmat[j,i]=v
    identity=arb_mat(n,n)
    for i in range(n):identity[i,i]=1
    residual=identity-jmat*a
    rho=max(sum((abs(residual[i,j]) for j in range(n)),arb(0)).upper() for i in range(n))
    jnorm=max(sum((abs(jmat[i,j]) for j in range(n)),arb(0)).upper() for i in range(n))
    assert rho<af('0.5')
    error=(jnorm*rho/(1-rho)).upper()
    # Actual inverse and symmetric rational/dyadic J differ in 2-norm by error.
    # H is the actual PSD coupling majorant, so |tr((F^-1-J)H)| <= error tr(H).
    tr=jmat.trace()+arb(0,n*error)
    beta=trace_product(jmat,h)+arb(0,(error*h.trace().upper()).upper())
    return tr,beta,jmat,error,{'approximate_inverse_residual_infinity_norm_upper':rho,'inverse_error_operator_norm_upper':error,'preconditioner_symmetric':True}


def new_high_gram(fun, audit, old_model, p, cmodel):
    """Full raw-high Gram of the NEW restricted action, using known low moments.
    The new source action is obtained by adding old action to residual model;
    its logarithmic old parts cancel exactly. Only polynomial integrals remain.
    """
    f=fun['blocks'][p];carrier=[]
    def integrate(poly,l,h):
        # e_p = sqrt(2p+1)*x^p for p=0,1; half measure by parity.
        total=arb(0);lp=l**(p+1);hp=h**(p+1)
        for k,v in enumerate(poly):
            total+=v*(hp-lp)/(k+p+1);lp*=l;hp*=h
        return total*arb(2*p+1).sqrt()
    for col in range(2):
        b=f['smooth_base'][col];o=f['old_smooth_action'][col]
        pol=[(box(b[k]) if k<len(b) else arb(0))+(box(o[k]) if k<len(o) else arb(0)) for k in range(max(len(b),len(o)))]
        v=integrate(pol,arb(0),arb(1))
        for cell,oldcell in zip(f['positive_cells'],f['old_shift_cells']):
            assert cell['lo']==oldcell['lo'] and cell['hi']==oldcell['hi']
            b=cell['shift_polynomials'][col];o=oldcell['shift_polynomials'][col]
            pol=[(box(b[k]) if k<len(b) else arb(0))+(box(o[k]) if k<len(o) else arb(0)) for k in range(max(len(b),len(o)))]
            v+=integrate(pol,box(cell['lo']),box(cell['hi']))
        carrier.append(v)
    moments=old_model['raw_low_moments'];low=[]
    for k,n in enumerate(range(p+2,384,2)):
        cn=af(F(2*n+1,2*p+1)).sqrt()*box(moments[n],10**100)/box(moments[p],10**100)
        low.append([cmodel[k,j]+arb(0,af('2e-33'))+cn*carrier[j] for j in range(2)])
    gm=arb_mat([[box(v) for v in row] for row in audit['new_restricted_model_action_gram']])
    high=arb_mat(2,2)
    for i in range(2):
        for j in range(2):
            high[i,j]=gm[i,j]-carrier[i]*carrier[j]-sum((row[i]*row[j] for row in low),arb(0))
    _,hu=loewner_bounds(high)
    assert hu[0,0]>0 and hu[1,1]>0
    # Gamma + potential remainder + complete high Mellin correction are
    # checked below to be <7e-21 per column. Young bounds their joint Gram.
    eps=af('1e-16')
    truehu=hu*(1+eps)
    for i in range(2):truehu[i,i]+=(1+1/eps)*2*af('7e-21')**2
    _,truehu=loewner_bounds(truehu)
    return truehu,{'carrier_pairings':carrier,'model_raw_high_gram':high,'true_high_dual_gram_upper':truehu,'low_model_pairing_comparison_radius':'2e-33','true_action_error_each_column_upper':'7e-21'}


def ldl(a):
    n=a.nrows();l=[[arb(0) for _ in range(n)] for _ in range(n)];ds=[]
    for i in range(n):
        d=a[i,i]-sum((l[i][k]**2*ds[k] for k in range(i)),arb(0))
        if not d>0:return None,ds,d
        ds.append(d);l[i][i]=arb(1)
        for j in range(i+1,n):
            l[j][i]=(a[j,i]-sum((l[j][k]*l[i][k]*ds[k] for k in range(i)),arb(0)))/d
    return l,ds,None


def upper_point(x):return x.upper()


def loewner_bounds(a):
    n=a.nrows();lo=arb_mat(n,n);hi=arb_mat(n,n)
    a=arb_mat([[a[i,j] for j in range(n)] for i in range(n)])
    for i in range(n):
        for j in range(i):
            v=(a[i,j]+a[j,i])/2
            a[i,j]=a[j,i]=v
    for i in range(n):
        radius=sum((a[i,j].rad() for j in range(n)),arb(0)).upper()
        for j in range(n):
            assert a[i,j].overlaps(a[j,i])
            lo[i,j]=a[i,j].mid();hi[i,j]=a[i,j].mid()
        lo[i,i]-=radius;hi[i,i]+=radius
    return lo,hi


def spd2(a):
    return bool(a[0,0]>0 and a[1,1]>0 and a[0,0]*a[1,1]-a[0,1]*a[1,0]>0)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);ap.add_argument('--bits',type=int,default=2048);ap.add_argument('--mixed',type=Path);ap.add_argument('--inputs',type=Path)
    args=ap.parse_args();assert __debug__ and not args.out.exists()
    ctx.prec=args.bits; assert flint.__version__=='0.9.0'
    paths={
        'a8':ROOT/'outputs/a8_model.json.gz',
        'a9':ROOT/'work/root-finish/research/x-c1/chambers-through-a11-2026-09-28/a9/a9_model.json.gz',
        'solutions':ROOT/'work/full-residual-review-2026-10-04/full-residual-replay/sources/SOLUTIONS.json',
        'rhs_budget':ROOT/'work/cross764-review-2026-10-04/cross764-replay-lf-complete/RHS_ERROR_BUDGET.json',
        'own_finite_audit':ROOT/'outputs/Objekt-X-A8-Vier-Antworten-Pruefung-2026-10-04/INDEPENDENT_INTEGER_AUDIT.json',
        'full_gram_audit':ROOT/'outputs/Objekt-X-A8-Vollstaendige-Residuen-Pruefung-2026-10-04/AUDIT_COMPLETE.json',
        'functions':ROOT/'work/full-residual-review-2026-10-04/full-residual-replay/numerical/FUNCTIONS.json',
        'full_gram':ROOT/'outputs/Objekt-X-A8-Vollstaendige-Residuen-Pruefung-2026-10-04/FULL_GRAM.json',
    }
    if args.inputs:
        names={'a8':'a8_model.json.gz','a9':'a9_model.json.gz','solutions':'SOLUTIONS.json','rhs_budget':'RHS_ERROR_BUDGET.json',
               'own_finite_audit':'INDEPENDENT_INTEGER_AUDIT.json','full_gram_audit':'AUDIT_COMPLETE.json','functions':'FUNCTIONS.json','full_gram':'FULL_GRAM.json'}
        paths={k:args.inputs/v for k,v in names.items()}
    if args.mixed:paths['mixed']=args.mixed
    data={};bindings={}
    for k,p in paths.items():
        raw=p.read_bytes();bindings[k]={'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
        data[k]=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
    assert bindings['a8']['sha256']=='5f8935d53f8518540ef25e6f2d511955bad688cf5905cb63e8d89f03aae2474b'
    assert bindings['solutions']['sha256']=='0ee0c0c4daed17ad3d68f3a340d236504b370fc72879363315884082c75120b5'
    assert bindings['a9']['sha256']=='a1cb251d5563cffb01eec3fbbf11c891851b677bd4f4ec7f5fba37164d14ab72'
    a8=data['a8'];a9=data['a9'];assert a8['scale_digits']==a9['scale_digits']==100
    assert a8['cutoff']==383 and a8['Gamma_degree']==160
    assert a9['endpoint']=='log(3)' and a9['Gamma_degree']==224
    gamma8=af(F(21,10)*F(a8['Gamma_kernel_error_exact']))
    gamma9=af(F(11,5)*F(a9['Gamma_kernel_error_exact']))
    delta=af(F(2,3));z=F(21,40);records=[]
    for p,label in enumerate(['even','odd']):
        start=time.time();print(label+': reading form and coupling matrices',flush=True)
        A=arb_mat([[box(v,10**100) for v in row] for row in a8['parities'][label]['A']])
        G=arb_mat([[box(v,10**100) for v in row] for row in a8['parities'][label]['complete_model_raw_high_Gram']])
        P=arb_mat([[af(v) for v in row] for row in data['solutions']['blocks'][p]['proposal']])
        assert A.nrows()==191 and P.nrows()==191 and P.ncols()==2
        bud=data['rhs_budget']['blocks'][p]
        cs={(v['n'],v['m']):F(v['value']) for v in bud['rational_model_midpoints']}
        C=arb_mat([[af(cs[(n,m)]) for m in [p+2,p+4]] for n in range(p+2,384,2)])
        BC=arb_mat([[af(v) for v in row] for row in bud['complete_rhs_error_gram_upper']])
        A0=arb_mat([[af(sum(map(F,a8['parities'][label]['A'][i][j]))/(2*10**100)) for j in range(191)] for i in range(191)])
        D=arb_mat([[box(a9['parities'][label]['A'][i][j],10**100) for j in range(2)] for i in range(2)])
        gp=P.transpose()*P
        E0=C-A0*P
        assert all(abs(E0[i,j])<af('1e-98') for i in range(191) for j in range(2))
        # Symmetric stable identity equivalent to D-C*P-P*C+P*A0*P.
        K0=D-(C.transpose()*P+P.transpose()*C)/2-(P.transpose()*E0+E0.transpose()*P)/2
        alpha=af('9.55e-99')+af(F(501,500))*gamma8
        K=arb_mat(2,2)
        for i in range(2):
            for j in range(2):
                err=alpha*(gp[i,i]*gp[j,j]).sqrt()+(gp[i,i]*BC[j,j]).sqrt()+(gp[j,j]*BC[i,i]).sqrt()+4*gamma9
                K[i,j]=K0[i,j]+arb(0,err.upper())
        Kentrylo,Kentryhi=loewner_bounds(K)
        tau=af(F(1,10**(32 if p==0 else 31)))
        shared_error=gp*(alpha+tau)+BC/tau
        for i in range(2):shared_error[i,i]+=4*gamma9
        Klo,_=loewner_bounds(K0-shared_error)
        _,Khi=loewner_bounds(K0+shared_error)
        print(label+': K '+str([[K[i,j].str(18) for j in range(2)] for i in range(2)]),flush=True)
        n=384+p
        em=z**n/factorial(n)/(1-z*z/((n+1)*(n+2))) * (4 if p else 1)
        eb=2*gamma8+24*af(em)
        H=G*af(F(1001,1000))
        for i in range(191):H[i,i]+=1001*eb**2
        lower=A-H/delta
        for i in range(191):lower[i,i]-=4*gamma8
        _,ds,fail=ldl(lower)
        assert fail is None and len(ds)==191
        print(label+': 191 positive old Schur pivots',flush=True)
        t,beta,jinv,inv_error,inverse_receipt=inverse_traces(lower,H)
        assert t>0 and beta>0
        print(label+': tr(F^-1 H) '+beta.str(18)+'; tr(F^-1) '+t.str(18),flush=True)
        BE=arb_mat([[af(v) for v in row] for row in data['own_finite_audit']['blocks'][p]['additional_profile_norm_refinement']['finite_residual_gram_upper_exact']])
        GR=arb_mat([[af(v) for v in row] for row in data['full_gram_audit']['blocks'][p]['complete_gram_loewner_upper']])
        HH=GR*(1+af(em)**2)
        theta_values=[F(1,10),F(1),F(10),F(100),F(1000),F(10000)]
        trials=[]
        for theta in theta_values:
            # q_old lower block retains B. Young is used only after exact shear.
            W=HH*(1/delta+(1+1/af(theta))*beta.upper()/delta**2)+BE*((1+af(theta))*t.upper())
            _,Wu=loewner_bounds(W)
            Slo=Klo-Wu
            positive=spd2(Slo)
            tr=Slo.trace();det=Slo.det()
            margin=det/tr if positive else None
            trials.append({'young_parameter':theta,'inverse_energy_upper':Wu,'schur_lower':Slo,'positive':positive,'margin_det_over_trace':margin})
            print(label+': theta '+str(theta)+' Wtrace '+W.trace().str(12)+' positive '+str(positive),flush=True)
        # Direct source energy route, mathematically the same Schur value.
        fr=data['full_gram'];vt=box(fr['new_potential_uniform_tail'])
        assert vt*af('1.002')+af('1e-75')<af('2e-33')
        for j in range(2):
            zn=box(fr['blocks'][p]['new_source_norms'][j])
            d=af(F(11,5))*af(fr['new_kernel_error'])*zn+vt*zn+af(em)*(box(data['full_gram_audit']['blocks'][p]['new_restricted_model_action_gram'][j][j]).sqrt()+1)
            assert d<af('7e-21')
        hnew,hreceipt=new_high_gram(data['functions'],data['full_gram_audit']['blocks'][p],a8,p,C)
        cfc=C.transpose()*jinv*C+(C.transpose()*C)*inv_error
        _,cfc=loewner_bounds(cfc)
        ec=af('1e-7')
        cfc=cfc*(1+ec)+BC*((1+1/ec)*t.upper())
        _,cfc=loewner_bounds(cfc)
        dlo,_=loewner_bounds(D)
        for j in range(2):dlo[j,j]-=4*gamma9
        source_trials=[]
        print(label+': new high Gram '+str([[hnew[i,j].str(15) for j in range(2)] for i in range(2)]),flush=True)
        print(label+': C*F^-1 C upper '+str([[cfc[i,j].str(15) for j in range(2)] for i in range(2)]),flush=True)
        for theta in [F(1,10000),F(1,1000),F(1,100),F(1,10),F(1),F(10)]:
            T=cfc*(1+af(theta))+hnew*(1/delta+(1+1/af(theta))*beta.upper()/delta**2)
            _,tu=loewner_bounds(T)
            sl=dlo-tu
            pos=spd2(sl)
            source_trials.append({'theta':theta,'old_source_inverse_energy_upper':tu,'schur_lower':sl,'positive':pos,'margin_det_over_trace':sl.det()/sl.trace() if pos else None})
            print(label+': source theta '+str(theta)+' Ttrace '+T.trace().str(12)+' Dtrace '+D.trace().str(12)+' positive '+str(pos),flush=True)
        mixed_trials=[];mixed_details=None
        if args.mixed:
            mix=data['mixed']['blocks'][p]
            assert mix['independent_complete_contractions_checked']==4 and mix['low_pairing_checks']==382
            Dmix=arb_mat([[box(v) for v in row] for row in mix['B0_raw_high_new_model_pairings']])
            v0=C-Dmix/delta
            vm=v0.transpose()*jinv*v0+(v0.transpose()*v0)*inv_error
            _,vmu=loewner_bounds(vm)
            eh=arb_mat([[2*af('7e-21')**2 if i==j else arb(0) for j in range(2)] for i in range(2)])
            er=(BC*t.upper()+eh*(beta.upper()/delta**2)+hnew*(t.upper()*eb**2/delta**2))*3
            _,eru=loewner_bounds(er)
            mixed_details={'model_corrected_force_energy_upper':vmu,'weighted_force_error_gram_upper':eru,
                           'model_corrected_force':v0,'coupling_difference_norm_upper':eb}
            for eta in [F(1,10**9),F(1,10**8),F(1,10**7),F(1,10**6),F(1,10**5)]:
                tupper=hnew/delta+vmu*(1+af(eta))+eru*(1+1/af(eta))
                _,tu=loewner_bounds(tupper)
                sl=dlo-tu
                positive=spd2(sl)
                _,wu=loewner_bounds(tu+Khi-dlo)
                separated=Klo-wu
                sep_positive=spd2(separated)
                mixed_trials.append({'young_parameter':eta,'old_source_inverse_energy_upper':tu,
                    'correlated_schur_lower':sl,'correlated_positive':positive,'correlated_margin':sl.det()/sl.trace() if positive else None,
                    'fixed_proposal_residual_inverse_energy_upper':wu,'separate_K_minus_W_lower':separated,
                    'separate_positive':sep_positive,'separate_margin':separated.det()/separated.trace() if sep_positive else None})
                print(label+': MIXED eta '+str(eta)+' correlated '+str(positive)+' separate '+str(sep_positive)+' S '+str([[sl[i,j].str(12) for j in range(2)] for i in range(2)]),flush=True)
        records.append({'parity':label,'K_model':K0,'K_interval':K,'K_loewner_lower':Klo,'K_loewner_upper':Khi,
            'K_lower_positive':spd2(Klo),'old_schur_positive_pivots':len(ds),'old_inverse_trace':t,
            'weighted_coupling_trace':beta,'inverse_receipt':inverse_receipt,'high_mellin_error_exact':em,'trials':trials,
            'source_profile_matrix_error_norm_upper':alpha,'new_high_receipt':hreceipt,'source_trials':source_trials,'source_C_F_inverse_C_upper':cfc,
            'mixed_details':mixed_details,'mixed_trials':mixed_trials,'seconds':time.time()-start})
    result={'status':'COMPLETED_DIRECTED_GATE','bindings':bindings,'bits':args.bits,'flint':flint.__version__,
        'blocks':records,'uses_target_positivity':False,'full_old_low_high_coupling_retained':True,
        'new_high_response_computed':False,'full_quotient_coverage_proved':False,'github_changed':False}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(serial(result),indent=2)+'\n',encoding='utf-8',newline='\n')
    print('DONE '+str(args.out),flush=True)


if __name__=='__main__':main()
