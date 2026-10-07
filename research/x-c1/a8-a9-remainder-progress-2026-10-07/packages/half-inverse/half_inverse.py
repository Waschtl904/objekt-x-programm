"""Full-space half-inverse enclosures for the frozen eight-column pilot.

The auxiliary Galerkin space is only used for centres. Its infinite residual
is bounded by complete logarithmic Gram integrals, not by a second truncation.
See DERIVATION.txt in the accompanying output package.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse, hashlib, json, sys, time

ROOT = Path(__file__).resolve().parents[2]
ap = argparse.ArgumentParser()
ap.add_argument('--bits', type=int, required=True)
ap.add_argument('--size', type=int, required=True)
ap.add_argument('--panels', type=int, default=256)
ap.add_argument('--out', type=Path, required=True)
ap.add_argument('--deps', type=Path, default=ROOT/'work/inverse-energy-deps')
ap.add_argument('--input-dir', type=Path, default=ROOT/'outputs/Objekt-X-Restpilot-Protokoll-2026-10-06')
args = ap.parse_args()
sys.path.insert(0, str(args.deps))
import flint
from flint import arb, arb_poly, arb_mat, fmpq, ctx
ctx.prec = args.bits

def af(x):
    x=F(x); return arb(fmpq(x.numerator, x.denominator))
def box(x):
    l,u=map(F,x); return af((l+u)/2)+arb(0,af((u-l)/2).upper())
def eye(n): return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def mat(x): return arb_mat([[box(v) for v in row] for row in x])
def tr(x): return sum((x[i,i] for i in range(x.nrows())),arb(0))
def frob(x): return sum((x[i,j]**2 for i in range(x.nrows()) for j in range(x.ncols())),arb(0)).sqrt()
def sym(x): return (x+x.transpose())*af(F(1,2))
def chol(x):
    n=x.nrows(); out=arb_mat(n,n)
    for i in range(n):
        for j in range(i+1):
            v=x[i,j]-sum((out[i,k]*out[j,k] for k in range(j)),arb(0))
            if i==j:
                assert v>0, ('chol',i,v)
                out[i,j]=v.sqrt()
            else: out[i,j]=v/out[j,j]
    return out
def zero(x, bound='1e-45'):
    assert all(x[i,j].contains(0) for i in range(x.nrows()) for j in range(x.ncols()))
    w=max((2*x[i,j].rad().upper() for i in range(x.nrows()) for j in range(x.ncols())))
    assert w<af(bound), w
    return w
def serial(x):
    if isinstance(x,arb):
        s=10**65
        return [str(F(int((x.lower()*s).floor().unique_fmpz()),s)),str(F(int((x.upper()*s).ceil().unique_fmpz()),s))]
    if isinstance(x,arb_mat): return [[serial(x[i,j]) for j in range(x.ncols())] for i in range(x.nrows())]
    if isinstance(x,dict): return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [serial(v) for v in x]
    return x
def say(x): print(time.strftime('%H:%M:%S')+' '+x,flush=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def integrate(poly, moments): return sum((poly[k]*moments[k] for k in range(len(poly))),arb(0))
def integral(poly): return sum((2*poly[k]/(k+1) for k in range(0,len(poly),2)),arb(0))
def legendre(n):
    x=arb_poly([0,1]); pp=[arb_poly([1]),x]
    for k in range(1,n): pp.append(((2*k+1)*x*pp[-1]-k*pp[-2])*af(F(1,k+1)))
    return pp[:n]

assert __debug__ and flint.__version__=='0.9.0'
assert args.size>=12 and args.size<=160 and args.panels>=16 and not args.out.exists()
start=time.monotonic(); N=args.size; n=N-4
protocol_path=args.input_dir/'PROTOCOL.json'
geometry_path=args.input_dir/'GEOMETRY_1024.json'
assert sha(protocol_path)=='7572ce23726101c4c82c06a5381f2544d2c84c882b564046ff20b10c4b30407a'
protocol=json.loads(protocol_path.read_bytes()); geom=json.loads(geometry_path.read_bytes())
assert protocol['right_shell_legendre_seed_degrees']==list(range(4,12))
a=3*arb(2).log()/2; b=arb(3).log(); h=b-a; c=(a+b)/2; d=h/2
c0=19-(arb.pi()*h).log()-arb.const_euler()
reg_global=h*(af(F(1,2))+1/(4*a))
pol=legendre(N)
ell=[pol[k]*((2*k+1)/(2*h)).sqrt() for k in range(N)]
mom1=[];mom2=[];o=arb(0);o2=arb(0);log2=arb(2).log()
for k in range(2*N-1):
    if k%2==0:
        o+=arb(1)/(k+1);o2+=arb(1)/(k+1)**2
        mom1.append(2*(o-log2)/(k+1))
        mom2.append(2*((o-log2)**2+o2-arb.pi()**2/12)/(k+1))
    else: mom1.append(arb(0));mom2.append(arb(0))
VM=arb_mat(N,N);V2=arb_mat(N,N)
for i in range(N):
    for j in range(i,N):
        if (i+j)%2:continue
        product=ell[i]*ell[j]
        VM[i,j]=VM[j,i]=h*integrate(product,mom1)
        V2[i,j]=V2[j,i]=h*integrate(product,mom2)
harm=arb(0); L=arb_mat(N,N)
for k in range(N):
    if k:harm+=arb(1)/k
    L[k,k]=c0+harm
T=L+VM
say(f'{N} local polynomials: complete V and V^2 moments integrated')
records=[]
for p,label in enumerate(('even','odd')):
    old=geom['blocks'][p]
    C=arb_mat(N,4)
    for i in range(12):
        for j in range(4): C[i,j]=box(old['tested_source_coefficients_12x4'][i][j])
    z=d/2; co=(c/2).cosh(); si=(c/2).sinh()
    terms=256
    mp=arb_poly([z**k/factorial(k)*(co if (k+p)%2==0 else si) for k in range(terms+1)])
    mtail=(c/2).exp()*z**(terms+1)/factorial(terms+1)/(1-z/(terms+2))
    lam=arb_mat([[d*integral(e*mp)+arb(0,((h/2).sqrt()*mtail).upper()) for e in ell]])
    mu=(a.sinh()+(a if p==0 else -a))/2
    nu=(b.sinh()-a.sinh()+(h if p==0 else -h))/2
    W=eye(N)+lam.transpose()*lam*(2/mu)
    WV=sym(C.transpose()*W*C)
    J=C*chol(WV).inv().transpose()
    rho=eye(N)-J*J.transpose()*W
    raw=arb_mat([[rho[i,j] for j in range(4,N)] for i in range(N)])
    Q=raw*chol(sym(raw.transpose()*W*raw)).inv().transpose()
    Z=arb_mat([[J[i,j] if j<4 else Q[i,j-4] for j in range(N)] for i in range(N)])
    orth=zero(Z.transpose()*W*Z-eye(N))
    assert all(Q[i,j].overlaps(box(old['normalized_pilot_coefficients_12x8'][i][j])) for i in range(12) for j in range(8))
    assert all(Q[i,j].contains(0) for i in range(12,N) for j in range(8))
    lc=lam*C
    ellR2=mu*nu/(2*(mu+nu))-(lc*WV.inv()*lc.transpose())[0,0]
    assert ellR2>0
    ellR=ellR2.sqrt()
    # The constant parts of both regular kernels are almost annihilated on R.
    # Bound their full R compression using the exact dual norm of integral s.
    m_integral=2*((b/2).sinh()-(a/2).sinh()) if p==0 else 2*((b/2).cosh()-(a/2).cosh())
    tint=arb_mat([[((h/2).sqrt() if i==0 else arb(0)) for i in range(N)]])
    tc=tint*C
    tauR2=h/2-m_integral**2/(2*(mu+nu))-(tc*WV.inv()*tc.transpose())[0,0]
    assert tauR2>0
    kcentre=(-c).exp()/(1-(-4*c).exp())
    ka=(-a).exp()/(1-(-4*a).exp())
    kder=ka*(af(F(1,2))+2*(-4*a).exp()/(1-(-4*a).exp()))
    self_osc=(h/2).cosh()*(h*h/32+h/48)
    reg=2*(af(F(1,4))+kcentre)*tauR2+h*(self_osc+h*kder)
    assert reg<reg_global
    # Global full-remainder moment correction, including the 19 W_X shift.
    dnorm=af(F(16,5))*(2*mu).sqrt()
    M=(a/2).cosh(); Lip=M/2
    HG=(2*Lip+20*M)*(2*a+2).sqrt()+4*M*arb(2).sqrt()+2*arb(2).sqrt()*2*a*M
    qcore=(2*mu).sqrt()*(HG+18*(2*mu).sqrt())
    mom=2*ellR*dnorm/mu+qcore*ellR2/(mu*mu)+38*ellR2/mu
    delta=reg+mom
    plower=c0*(1-2*ellR2/mu)-reg-2*ellR*dnorm/mu-qcore*ellR2/(mu*mu)
    m=int(plower.lower().floor().unique_fmpz()); assert m>=19
    A=sym(Q.transpose()*T*Q)
    amin=int((c0*(1-2*ellR2/mu)).lower().floor().unique_fmpz())
    chol(A-eye(n)*amin)
    amax=int(max(sum((abs(A[i,j]).upper() for j in range(n)),arb(0)) for i in range(n)).ceil().unique_fmpz())
    chol(eye(n)*amax-A)
    D=Z.transpose()*T*Q
    FP=L*Q-Z*D
    GF=sym(FP.transpose()*FP+FP.transpose()*VM*Q+Q.transpose()*VM*FP+Q.transpose()*V2*Q)
    # These are COMPLETE residual norms: log^2 moments cover all omitted modes.
    # GF is a Gram matrix by the complete integral identity. Its smallest
    # eigenvalues approach zero rapidly; strict positive definiteness is not
    # required. The traces used below are checked directly with intervals.
    assert all(GF[i,i]>0 for i in range(n))
    rnorm=tr(GF).sqrt()
    metric_error=2*ellR/mu*frob(lam*Z*D)
    constant_error=delta+metric_error
    E=arb_mat([[int(i==j) for j in range(8)] for i in range(n)])
    # Finite inverse square root, uniformly convergent binomial series.
    Rmat=eye(n)-A/amax; power=E; finite=E; coeff=af(1); contraction=1-af(F(amin,amax))
    k=0
    while True:
        k+=1;power=Rmat*power;coeff*=af(F(2*k-1,2*k));finite+=power*coeff
        rem=contraction**(k+1)/(1-contraction)/arb(amax).sqrt()
        if rem<af('1e-45'):break
        assert k<2000
    finite=finite/arb(amax).sqrt()
    rational=[];roundsq=arb(0)
    for i in range(n):
        row=[]
        for j in range(8):
            v=F(int((finite[i,j].mid()*10**55).floor().unique_fmpz()),10**55)
            row.append(str(v));roundsq+=(finite[i,j]-af(v))**2
        rational.append(row)
    rounderr=roundsq.sqrt(); polynomial_error=rem+rounderr
    say(f'{label}: P_R >= {m}, finite spectrum in [{amin},{amax}], half-inverse series {k} terms')
    # Log-spaced t panels. Enclose the infinite resolvent residual integral.
    # Variation on each panel is bounded in OPERATOR norm, with ||E||=1.
    end=af(128); ratio=(arb(1)+end).log()/args.panels
    nodes=[(ratio*i).exp()-1 for i in range(args.panels+1)]
    nodes[0]=arb(0);nodes[-1]=end
    midpoint_sum=arb(0);variation_sum=arb(0)
    for idx in range(args.panels):
        lo=nodes[idx];hi=nodes[idx+1];mid=(lo+hi)/2
        sol=(A+eye(n)*(mid*mid)).solve(E)
        contracted=sym(sol.transpose()*GF*sol)
        trace=tr(contracted);assert trace>0
        rows=max(sum((abs(contracted[i,j]).upper() for j in range(8)),arb(0)) for i in range(8))
        point=(trace if trace.upper()<rows else rows).sqrt()
        dist=max(abs(hi*hi-mid*mid).upper(),abs(mid*mid-lo*lo).upper())
        var=rnorm*dist/((amin+lo*lo)*(amin+mid*mid))
        weight=((hi/arb(m).sqrt()).atan()-(lo/arb(m).sqrt()).atan())/arb(m).sqrt()
        assert weight>0
        midpoint_sum+=point*weight;variation_sum+=var*weight
        if (idx+1)%(max(1,args.panels//4))==0:say(f'{label}: residual panels {idx+1}/{args.panels}')
    scale=2/arb.pi()
    residual_mid=scale*midpoint_sum
    residual_variation=scale*variation_sum
    integration_tail=scale*rnorm/(3*end**3)
    bounded_part=constant_error/(arb(m).sqrt()*arb(amin).sqrt()*(arb(m).sqrt()+arb(amin).sqrt()))
    err=residual_mid+residual_variation+integration_tail+bounded_part+polynomial_error
    half_floor=reg/(arb(m).sqrt()*arb(amin).sqrt()*(arb(m).sqrt()+arb(amin).sqrt()))
    assert err>0 and err<af(F(1,10)), ('too broad',err)
    normcentres=[sum((af(rational[i][j])**2 for i in range(n)),arb(0)).sqrt() for j in range(8)]
    epsq=F(int((err.upper()*10**12).ceil().unique_fmpz()),10**12)
    sq=[[F(v) for v in row] for row in rational]
    centregram=[[sum((row[i]*row[j] for row in sq),F(0)) for j in range(8)] for i in range(8)]
    cnorm=af(max(sum(map(abs,row),F(0)) for row in centregram)).sqrt()
    young=F(int(((af(epsq)/cnorm).upper()*10**12).ceil().unique_fmpz()),10**12)
    upper19=[[19*((1+young)*centregram[i][j]+((1+1/young)*epsq**2 if i==j else 0)) for j in range(8)] for i in range(8)]
    upper19norm=max(sum(map(abs,row),F(0)) for row in upper19)
    assert upper19norm<1
    record={'parity':label,'auxiliary_dimension':n,'max_polynomial_degree':N-1,
        'exact_basis_definition':'W_X Gram-Schmidt/positive Cholesky: V first, then projected ell_4,...,ell_(N-1); Q are last N-4 columns; first eight equal frozen e_j',
        'basis_Q_local_coefficients':Q,'basis_Z_local_coefficients':Z,'WX_gram':W,'orthogonality_width':orth,
        'lambda_on_R_norm_squared':ellR2,'integral_on_R_norm_squared':tauR2,'mu':mu,'nu':nu,'P_R_lower_integer':m,
        'P_R_lower_bound':plower,'finite_A_spectrum':[amin,amax],'finite_model_A':A,
        'finite_model_action_coefficients':D,'complete_log_residual_gram':GF,
        'complete_log_residual_operator_upper':rnorm,'regular_gamma_global_bound':reg_global,
        'regular_gamma_bound':reg,'moment_correction_bound':mom,
        'core_form_absolute_bound':qcore,'metric_residual_bound':metric_error,
        'half_inverse_centre_rational_Q_coefficients':rational,'finite_series_terms':k,
        'column_centre_norms':normcentres,
        'error_budget':{'log_residual_integral_midpoint_sum':residual_mid,
            'log_residual_panel_variation':residual_variation,'resolvent_infinite_tail':integration_tail,
            'bounded_operator_perturbations':bounded_part,'finite_series_and_rounding':polynomial_error,
            'regular_gamma_current_bound_floor':half_floor},
        'joint_half_inverse_error_norm_upper':err,
        'joint_half_inverse_error_gram_upper_scalar':err**2,
        'joint_half_inverse_error_upper_rational':str(epsq),
        'shift19_young_parameter':str(young),
        'shift19_B00_Loewner_upper':[[str(v) for v in row] for row in upper19],
        'shift19_B00_operator_norm_upper':str(upper19norm),
        'shift19_is_only_one_of_three_B00_terms':True,
        'U00':None,'G01':None,'gamma01':None,'beta_tail':None,'eta':None,'alpha':None}
    records.append(record)
    say(f'{label}: JOINT eight-column half-inverse error <= {err.str(14)}; centre norms {normcentres[0].str(10)}..{normcentres[-1].str(10)}')
out={'status':'FULL_SPACE_HALF_INVERSE_ENCLOSURES_COMPUTED_OPERATOR_GATE_OPEN',
    'bits':args.bits,'size':N,'resolvent_panels':args.panels,'python_flint':flint.__version__,
    'protocol_sha256':sha(protocol_path),'geometry_sha256':sha(geometry_path),'program_sha256':sha(Path(__file__)),
    'source_nonpole_form_identity_inherited':True,'target_positivity_used':False,
    'full_remainder_certified':False,'new_horizon':False,'github_changed':False,
    'common_constants':{'a':a,'b':b,'h':h,'model_scalar_c0':c0},'blocks':records,'seconds':time.monotonic()-start}
args.out.parent.mkdir(parents=True,exist_ok=True)
args.out.write_text(json.dumps(serial(out),indent=2)+'\n',encoding='utf-8')
say('Saved '+str(args.out))
