"""Certified block factorization of the inherited A8 Schur inverse.

This computes an old-metric tool, not the force values on half-inverse errors.
No A9 form or positive target operator is used.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,sys,json,gzip,hashlib,time

ROOT=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser()
ap.add_argument('--bits',type=int,required=True)
ap.add_argument('--out',type=Path,required=True)
ap.add_argument('--deps',type=Path,default=ROOT/'work/inverse-energy-deps')
ap.add_argument('--model',type=Path,default=ROOT/'outputs/a8_model.json.gz')
ap.add_argument('--half',type=Path,default=ROOT/'outputs/Objekt-X-Restpilot-Halbinverse-2026-10-06/expected/1536.json')
args=ap.parse_args();sys.path.insert(0,str(args.deps))
from flint import arb,arb_mat,fmpq,ctx
import flint
ctx.prec=args.bits
def af(x):
    q=F(x);return arb(fmpq(q.numerator,q.denominator))
def box(x,den=1):
    l,u=[F(v)/den for v in x]
    return af((l+u)/2)+arb(0,af((u-l)/2).upper())
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def sub(a,rows,cols):return arb_mat([[a[i,j] for j in cols] for i in rows])
def sym(a):return (a+a.transpose())*af(F(1,2))
def norminf(a):return max(sum((abs(a[i,j]).upper() for j in range(a.ncols())),arb(0)) for i in range(a.nrows()))
def ldl(a):
    n=a.nrows();ls=eye(n);ds=[]
    for j in range(n):
        d=a[j,j]-sum((ls[j,k]**2*ds[k] for k in range(j)),arb(0))
        assert d>0,('LDL',j,d)
        ds.append(d)
        for i in range(j+1,n):ls[i,j]=(a[i,j]-sum((ls[i,k]*ls[j,k]*ds[k] for k in range(j)),arb(0)))/d
    return ds
def serial(x):
    if isinstance(x,arb):
        s=10**70
        def dyad(v):
            m,e=map(int,v.man_exp());return F(m*2**e) if e>=0 else F(m,2**(-e))
        lo=dyad(x.lower())*s;hi=dyad(x.upper())*s
        return [str(F(lo.numerator//lo.denominator,s)),str(F(-((-hi.numerator)//hi.denominator),s))]
    if isinstance(x,arb_mat):return [[serial(x[i,j]) for j in range(x.ncols())] for i in range(x.nrows())]
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x
def say(s):print(time.strftime('%H:%M:%S')+' '+s,flush=True)
def rational_lower(a):
    n=a.nrows();s=10**90;ints=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            ints[i][j]=ints[j][i]=int((a[i,j].mid()*s).floor().unique_fmpz())
    mid=arb_mat([[af(F(x,s)) for x in row] for row in ints])
    rad=norminf(a-mid)
    units=int((rad*s).ceil().unique_fmpz())
    for i in range(n):ints[i][i]-=units
    lo=arb_mat([[af(F(x,s)) for x in row] for row in ints])
    return lo,ints,units,rad
assert __debug__ and flint.__version__=='0.9.0' and not args.out.exists()
raw=args.model.read_bytes();digest=hashlib.sha256(raw).hexdigest()
assert digest=='5f8935d53f8518540ef25e6f2d511955bad688cf5905cb63e8d89f03aae2474b'
data=json.loads(gzip.decompress(raw));N=191;records=[]
halfraw=args.half.read_bytes();half=json.loads(halfraw)
assert half['status']=='FULL_SPACE_HALF_INVERSE_ENCLOSURES_COMPUTED_OPERATOR_GATE_OPEN'
gamma=af(F(21,10)*F(data['Gamma_kernel_error_exact']))
for p,label in enumerate(('even','odd')):
    start=time.monotonic()
    A=arb_mat([[box(v,10**100) for v in row] for row in data['parities'][label]['A']])
    G=arb_mat([[box(v,10**100) for v in row] for row in data['parities'][label]['complete_model_raw_high_Gram']])
    em=af(F(21,40)**(384+p)/factorial(384+p)/(1-F(21,40)**2/((385+p)*(386+p)))*(4 if p else 1))
    eb=2*gamma+24*em
    HB=G*af(F(1001,1000))+eye(N)*1001*eb**2
    FF=sym(A-eye(N)*4*gamma-HB*af(F(3,2)))
    Fbar,ints,units,rad=rational_lower(FF)
    piv=ldl(Fbar);say(label+': exact rational lower matrix positive')
    scan=[];chosen=None
    for r in range(1,9):
        I=list(range(r));J=list(range(r,N))
        D=sub(Fbar,J,J);K=sub(Fbar,I,J);Dinv=sym(D.inv())
        trace=Dinv.trace()
        rho=norminf(eye(N-r)-Dinv*D);assert rho<af('1e-100')
        print(label,r,'trace(D^-1)',trace.str(14),flush=True)
        scan.append({'rank':r,'tail_inverse_trace':trace,'direct_inverse_residual_infinity_upper':rho})
        if r==6:
            chosen=(r,D,K,Dinv)
            # Rank six was selected after the initial old-only diagnostic.
            # The frozen eight-dimensional NEW pilot is unchanged.
        elif chosen is not None:break
    assert chosen is not None
    r,D,K,Dinv=chosen
    T=-K*Dinv
    S=sym(sub(Fbar,list(range(r)),list(range(r)))+T*K.transpose())
    sp=ldl(S);Sinv=sym(S.inv());assert norminf(eye(r)-S*Sinv)<af('1e-100')
    # Rationalize the small Schur inverse upward in Loewner order.
    scale=10**70
    smid=arb_mat([[af(F(int((Sinv[i,j].mid()*scale).floor().unique_fmpz()),scale)) for j in range(r)] for i in range(r)])
    smid=sym(smid);sr=norminf(Sinv-smid)
    sup=smid+eye(r)*sr.upper()
    # The complement inverse is bounded by its full trace (no omitted modes).
    absinv=arb_mat([[abs(Dinv[i,j]).upper() for j in range(N-r)] for i in range(N-r)])
    weights=arb_mat([[arb(1)] for i in range(N-r)])
    invbounds=[Dinv.trace().upper(),norminf(Dinv)]
    for step in range(12):
        action=absinv*weights
        invbounds.append(max((action[i,0]/weights[i,0]).upper() for i in range(N-r)))
        mx=max(action[i,0].upper() for i in range(N-r))
        weights=arb_mat([[(action[i,0]/mx).mid()] for i in range(N-r)])
        assert all(weights[i,0]>0 for i in range(N-r))
    invnorm=min(invbounds)
    kappa=F(int((invnorm*10**6).ceil().unique_fmpz())+1,10**6)
    fullK=sym(Fbar.inv())
    Tfull=arb_mat([[int(i==j) if j<r else T[i,j-r] for j in range(N)] for i in range(r)])
    base=Tfull.transpose()*Sinv*Tfull
    for i in range(N-r):
        for j in range(N-r):base[r+i,r+j]+=Dinv[i,j]
    diff=fullK-base
    assert all(diff[i,j].contains(0) for i in range(N) for j in range(N))
    width=norminf(diff);assert width<af('1e-40')
    # Certify directly that kappa I dominates D^-1.
    tailpiv=ldl(D-eye(N-r)/af(kappa))
    # Propagate the already certified COMMON half-inverse error through only
    # the bounded high and complementary-old maps. The six sensitive forces
    # and all four C-couplings remain uncomputed.
    hh=half['blocks'][p];eps=af(hh['joint_half_inverse_error_upper_rational'])
    mu=box(hh['mu']);lambdaR=box(hh['lambda_on_R_norm_squared']).sqrt()
    qcore_norm=box(hh['core_form_absolute_bound'])/(2*mu).sqrt()
    gnorm=af(F(16,5))+lambdaR*qcore_norm/mu
    hnorm=gnorm*(1+em**2).sqrt()
    moments=data['raw_low_moments']
    cn=[af(F(2*k+1,2*p+1)).sqrt()*box(moments[k],10**100)/box(moments[p],10**100) for k in range(p+2,p+384,2)]
    goldJ=1+sum((v*v for v in cn[r:]),arb(0));assert goldJ<af('1.002')
    HBJ=sub(HB,list(range(r,N)),list(range(r,N)))
    bnorm2=min(HBJ.trace().upper(),norminf(HBJ))
    vJnorm=goldJ.sqrt()*gnorm+af(F(3,2))*bnorm2.sqrt()*hnorm
    errHigh=af(F(3,2))*hnorm**2*eps**2
    errTail=af(kappa)*vJnorm**2*eps**2
    say(label+': joint error Gram scalars high='+errHigh.str(12)+' complement='+errTail.str(12))
    say(f'{label}: rank {r} retained; complement energy <= {float(kappa):.6f} ||v_J||^2')
    records.append({'parity':label,'old_dimension':N,'rational_lower_scale_digits':90,
        'rational_Fbar_integer_matrix':[[str(v) for v in row] for row in ints],
        'lowering_diagonal_grid_units':units,'rounding_operator_error_upper':rad,
        'Fbar_positive_pivots':len(piv),'scan':scan,'retained_rank':r,
        'retained_old_degrees':list(range(p+2,p+2+2*r,2)),
        'tail_inverse_trace':Dinv.trace(),'tail_energy_kappa':str(kappa),
        'tail_inverse_norm_bounds':invbounds,'tail_weighted_schur_weights':weights,
        'tail_gap_lower':'1/('+str(kappa)+')','tail_shifted_positive_pivots':len(tailpiv),
        'corrected_force_transform_T':Tfull,'small_schur_matrix':S,
        'small_schur_inverse':Sinv,'small_schur_inverse_upper':sup,
        'small_schur_positive_pivots':len(sp),
        'full_inverse_trace':fullK.trace(),'block_inverse_identity_residual_upper':width,
        'half_inverse_error_upper':hh['joint_half_inverse_error_upper_rational'],
        'old_high_moment_tail':em,'g_R_operator_norm_upper':gnorm,
        'h_R_operator_norm_upper':hnorm,'tail_low_source_synthesis_norm_squared':goldJ,
        'tail_BBstar_norm_upper':bnorm2,'v_J_operator_norm_upper':vJnorm,
        'joint_high_weighted_error_gram_scalar_upper':errHigh,
        'joint_complement_weighted_error_gram_scalar_upper':errTail,
        'joint_high_plus_complement_error_gram_scalar_upper':errHigh+errTail,
        'sensitive_six_force_error_gram':None,'four_C_coupling_error_gram':None,
        'new_force_values_computed':False,'weighted_half_inverse_error_gram_computed':False,
        'seconds':time.monotonic()-start})
args.out.parent.mkdir(parents=True,exist_ok=True)
result={'status':'OLD_RESPONSE_FACTORIZATION_COMPUTED_NEW_FORCE_GRAMS_OPEN',
    'bits':args.bits,'source_a8_sha256':digest,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_half_inverse_sha256':hashlib.sha256(halfraw).hexdigest(),
    'factor_rank_selection':'six leading old coordinates, selected after an exploratory old-only rank scan; ranks 1..7 are reported',
    'old_space_high_floor':'2/3','target_positivity_used':False,'new_operator_integration':False,
    'blocks':records,'U00':None,'G01':None,'gamma01':None,'beta_tail':None,'full_remainder_certified':False}
args.out.write_text(json.dumps(serial(result),indent=2)+'\n',encoding='utf-8')
say('Saved '+str(args.out))
