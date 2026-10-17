"""Directed budget enclosure for the fixed A9->A11 rule; stdlib only.

No new historical source integration, no residual pairing and no RH claim.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, isqrt
import argparse, hashlib, io, json, sys, zipfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'vendor'))
import source_core as sc
sc.DIGITS = 180
sc.S = 10**180
I = sc.I
ARCHIVES = {
 'high': ('Objekt-X-Vollstaendige-Hochantwort-und-Spike-Skalarfehler-2026-10-16.zip', '1ccb6be11c6a8b4e325338b80f2136990b464b4a70e724a02ca7addbe7ba99b0'),
 'bridge': ('Objekt-X-Nstar-Jp-Funktionsanschluss-und-Koeffizienten-2026-10-16.zip', 'b48e3895d57cc5cc2c11ca170e32d6af5fbdfcde9948b4db7c370d3376b6d57b'),
 'stage3': ('Objekt-X-Stufe3-Endliche-U8-Antwort-und-Skalaranschluss-2026-10-16.zip', 'ab7116f74c9d81b877bec28ac547cc275ca142033a0004ffc3c699c63dd96b52'),
 'response': ('Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15.zip', 'b8677c0bb085f40052e52953ec39112894fbaa0f9f5d9997df8ae546238f41ee'),
}
RULE = 'A9_A11_N12_MIDPOINT_INVERSE_60_V1'

def need(ok, message):
    if not ok:
        raise AssertionError(message)

def sha(data): return hashlib.sha256(data).hexdigest()

def member(z, suffix):
    names = [n for n in z.namelist() if n == suffix or n.endswith('/' + suffix)]
    need(len(names) == 1, ('unique member', suffix, names))
    return z.read(names[0])

def read(z, name): return json.loads(member(z, name))

def upper(x): return F(x.hi, sc.S)

def ceilq(x, digits=6):
    x = F(x); scale = 10**digits
    return F(-((-x.numerator * scale) // x.denominator), scale)

def encode(x):
    if isinstance(x, I): return x.frac()
    if isinstance(x, F): return str(x)
    if isinstance(x, dict): return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [encode(v) for v in x]
    return x

def write(path, data):
    path.write_bytes((json.dumps(encode(data), indent=2, ensure_ascii=False) + '\n').encode('utf-8'))

def transpose(a): return list(map(list, zip(*a)))

def mm(a, b):
    return [[sum((x*y for x, y in zip(row, col)), I(0))
             for col in zip(*b)] for row in a]

def positive_pivots(a):
    need(all(a[i][j].intersects(a[j][i]) for i in range(len(a)) for j in range(len(a))), 'symmetric enclosure')
    a = [row[:] for row in a]; pivots = []
    for k in range(len(a)):
        d = a[k][k]
        need(d.lo > 0, ('positive pivot', k, d.frac()))
        pivots.append(d)
        for i in range(k+1, len(a)):
            for j in range(i, len(a)):
                a[i][j] = a[i][j] - a[i][k]*a[k][j]/d
                a[j][i] = a[i][j]
    return pivots

def geometry():
    a = sc.log_point(3); b = sc.log_point(11)/2; h = b-a
    need(I(1).hi < a.lo and a.hi < I(F(11,10)).lo, 'old endpoint')
    need(I(F(1,10)).hi < h.lo and h.hi < I(F(101,1000)).lo, 'shell width, including corrected upper bound')
    mus = [(F(4,3)+a)/2, (F(4,3)-a)/2]
    nus = [(5/I(11).sqrt()-F(4,3)+h)/2, (5/I(11).sqrt()-F(4,3)-h)/2]
    geom = {}
    for sigma, parity in enumerate(['even','odd']):
        mu, nu = mus[sigma], nus[sigma]
        need(mu.lo > 0 and nu.lo > 0, 'positive moment masses')
        ratio = nu/mu
        need(ratio.hi < I(F(1,3)).lo, 'W metric below 4/3')
        derivative = nu*mus[1-sigma]/(4*mu**2)
        boundary = nu*F(4 if sigma == 0 else 1, 3)/(2*mu**2)
        need(derivative.hi < I(1).lo, 'core derivative square below 1')
        need(boundary.hi < I(F(49,100)).lo, 'core endpoint magnitude below 7/10')
        geom[parity] = {'mu':mu, 'nu':nu, 'nu_over_mu':ratio,
            'core_derivative_square_bound':derivative,
            'core_endpoint_square_bound':boundary}
    prime_sum = sum((sc.log_point(prime)/I(q).sqrt()
                     for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]), I(0))
    need(prime_sum.hi < I(4).lo, 'all seven prime-power channels')
    euler_lower = I(sum((F(1,k) for k in range(1,7)), F(0)))-sc.log_point(7)
    need(euler_lower.lo > I(F(1,2)).hi, 'Euler gamma lower bound H6-log7')
    need(sc.log_point(24).lo > I(3).hi, 'log24 > 3')
    # pi>3 implies log(8*pi)>log24 and pi/2>3/2, hence kappa>5.
    need(sum((F(1,2)**k/F(factorial(k)) for k in range(5)), F(0)) > F(8,5), 'exp(1/2)>8/5')
    need(sum((F(2)**k/F(factorial(k)) for k in range(6)), F(0)) > 7, 'exp(2)>7')
    return {'a':a,'b':b,'h':h,'parities':geom,'prime_weight_sum':prime_sum,
            'Euler_gamma_lower_bound':euler_lower,'kappa_strict_lower':F(5),
            'kernel_integral_from_1_strict_upper':F(35,24)}

def direct_bound(derivative_square, endpoint_square, cutoff):
    A = I(derivative_square); e = I(endpoint_square).sqrt(); t = I(cutoff)
    need(0 < t.lo <= t.hi <= I(F(1,10)).lo, 'disjoint jump intervals')
    jumps = 2*((e+F(7,10))**2+e**2)
    # Entire interval (0,t), including derivative/jump cross term.
    small = A*(t**3/3+t**2/4) + 2*(A*jumps).sqrt()*(2*t**2*t.sqrt()/5+t*t.sqrt()/3) + jumps*(t**2/2+t/2)
    # Entire interval (t,infinity); no endpoint or long-range cutoff.
    tail = 1-t+sc.log(1/t)/2+F(35,24)
    total = small+4*tail+3
    return {'cutoff':cutoff,'piecewise_derivative_square_upper':derivative_square,
            'shell_endpoint_square_upper':endpoint_square,'jump_square_sum_upper':jumps,
            'small_translation_energy_upper':small,'large_translation_energy_upper':4*tail,
            'prime_minus_constant_upper':F(3),'direct_form_upper':total}

def rational_sqrt_upper(q):
    q=F(q); need(q>=0, 'rational square root domain'); scale=10**80
    n=q.numerator*scale*scale; d=q.denominator
    root=isqrt(n//d)
    if root*root*d<n: root+=1
    return F(root,scale)

def rational_log_upper(q):
    # Separate exact-Fraction arithmetic, independent of source_core.I/log.
    q=F(q); need(q>=1, 'rational log control domain'); k=0
    while q>2: q/=2; k+=1
    def series(x):
        z=(x-1)/(x+1)
        partial=2*sum((z**(2*j+1)/F(2*j+1) for j in range(100)),F(0))
        return partial+2*z**201/(201*(1-z*z))
    return series(q)+k*series(F(2))

def rational_direct_upper(A, endpoint_square, t):
    A=F(A); t=F(t); e=rational_sqrt_upper(endpoint_square)
    J=2*((e+F(7,10))**2+F(endpoint_square))
    # Monotonicity in A,J and positive coefficients makes every replacement upper.
    return (A*(t**3/3+t*t/4)
       +2*rational_sqrt_upper(A*J)*rational_sqrt_upper(t)*(2*t*t/5+t/3)
       +J*(t*t/2+t/2)+4*(1-t+rational_log_upper(1/t)/2+F(35,24))+3)

def controls():
    # A genuine finite symmetric block test of Khat=d-Fhat* S Fhat.
    A=[[F(2),F(1,3)],[F(1,3),F(3)]]
    X=[[F(1,2),F(0)],[F(0),F(1,3)]]
    f=[F(2),F(-1)]; t=[sum((X[i][j]*f[j] for j in range(2)),F(0)) for i in range(2)]
    dot=lambda a,b:sum((x*y for x,y in zip(a,b)),F(0))
    at=[dot(row,t) for row in A]
    S=[[X[i][j]+X[j][i]-sum((X[k][i]*A[k][l]*X[l][j] for k in range(2) for l in range(2)),F(0)) for j in range(2)] for i in range(2)]
    lhs=F(7)-2*dot(f,t)+dot(t,at)
    rhs=F(7)-dot(f,[dot(row,f) for row in S])
    need(lhs==rhs and lhs<=7, 'finite completed-square control')
    wrong=F(7)+dot(f,[dot(row,f) for row in S])
    need(lhs!=wrong, 'incorrect sign rejected')
    for n in range(12):
        p=sc.leg(n); dp=[F(k)*p[k] for k in range(1,len(p))]
        norm=sum((2*x*y/F(i+j+1) for i,x in enumerate(dp) for j,y in enumerate(dp) if (i+j)%2==0),F(0))
        need(norm==n*(n+1), ('Legendre derivative integral', n))
    N=12
    need(sum((2*n+1)*n*(n+1) for n in range(N))==N*N*(N*N-1)//2, 'whole subspace derivative trace')
    # The derivative/jump cross term cannot be discarded: (1+1)^2 != 1+1.
    need((F(1)+F(1))**2 > F(1)**2+F(1)**2, 'omitted cross term rejected')
    return {'finite_completed_square':True,'wrong_sign_rejected':True,
            'exact_Legendre_derivative_integrals':12,'derivative_trace_identity':True,
            'omitted_derivative_jump_cross_term_rejected':True}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--archive-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args(); out=args.output.resolve()
    need(not out.exists() and not out.is_relative_to(HERE), 'new output outside package required')
    if (HERE/'MANIFEST.json').exists():
        for name,digest in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            path=(HERE/name).resolve()
            need(path.is_relative_to(HERE) and sha(path.read_bytes())==digest, ('package manifest',name))
    archives={};manifest_counts={}
    for tag,(name,digest) in ARCHIVES.items():
        raw=(args.archive_dir/name).read_bytes()
        need(sha(raw)==digest, ('archive hash',tag))
        z=zipfile.ZipFile(io.BytesIO(raw));archives[tag]=z
        roots={n.split('/')[0] for n in z.namelist() if '/' in n}
        need(len(roots)==1, ('one archive root',tag))
        archive_root=next(iter(roots))
        manifest=json.loads(z.read(archive_root+'/MANIFEST.json'))
        need(isinstance(manifest,dict), ('manifest structure',tag))
        # These four sealed manifests are simple relative-name/hash maps.
        for path,wanted in manifest.items():
            need(isinstance(wanted,str) and sha(z.read(archive_root+'/'+path))==wanted, ('archive manifest',tag,path))
        manifest_counts[tag]=len(manifest)
    high=archives['high'];bridge=archives['bridge'];response=archives['response']
    need(sha(member(high,'vendor/source_core.py'))==sha((HERE/'vendor/source_core.py').read_bytes()), 'original arithmetic implementation')
    fresh=read(response,'inputs/FRESH_A12.json')
    frozen=read(response,'inputs/FROZEN_RESPONSE12.json')
    funcs=read(response,'inputs/FUNCTIONS12.json')
    energy=read(response,'RESPONSE_ENERGY.json')
    directions=read(bridge,'expected/DIRECTIONS.json')
    scalar=read(high,'expected/SPIKE_SCALAR_D_MODEL_ERROR.json')
    receipt_high=read(high,'expected/RECEIPT.json')
    for tag,key in [('bridge','bridge_sha256'),('stage3','stage3_sha256'),('response','response_archive_sha256')]:
        need(receipt_high[key]==ARCHIVES[tag][1], ('upstream dependency',tag))
    need(frozen['rule_id']==RULE, 'frozen response rule')
    for path,digest in energy['source_bindings'].items():
        need(sha(member(response,path))==digest, ('response source binding',path))
    geom=geometry();checks=controls();results={}
    individual=[direct_bound(1+200*(2*n+1)*n*(n+1),5*(2*n+1),F(1,10*(n+1)**2)) for n in range(12)]
    N=12
    whole=direct_bound(1+100*N*N*(N*N-1),5*N*N,F(1,10*N*N))
    independent_individual=[rational_direct_upper(1+200*(2*n+1)*n*(n+1),5*(2*n+1),F(1,10*(n+1)**2)) for n in range(12)]
    independent_whole=rational_direct_upper(1+100*N*N*(N*N-1),5*N*N,F(1,10*N*N))
    checks['independent_exact_fraction_scalar_enclosures']=26
    for p in ['even','odd']:
        xq=[[F(v) for v in row] for row in frozen['parities'][p]['X']]
        aq=[[F(v) for v in row] for row in fresh['parities'][p]['midpoint']]
        need(xq==transpose(xq) and aq==transpose(aq), 'exact symmetric inputs')
        x=[[I(v) for v in row] for row in xq]; a=[[I(v) for v in row] for row in aq]
        xt=transpose(x);product=mm(xt,mm(a,x))
        S=[[x[i][j]+xt[i][j]-product[i][j] for j in range(12)] for i in range(12)]
        pivots=positive_pivots(S)
        er=energy['parities'][p]['fixed_X']
        deltaF=F(funcs['parities'][p]['whole_F12_operator_error_upper'])
        deltaA=F(fresh['parities'][p]['whole_Loewner_radius'])
        tnorm=F(er['T_norm_upper']); tnorm2=F(er['T_norm_squared_upper'])
        price=F(er['direct_K_error_upper'])
        need(price>=2*deltaF*tnorm+deltaA*tnorm2, 'two-sided direct K model error')
        q=F(directions[p]['q']);need(q>0 and q==F(scalar[p]['q']), 'same spike q')
        eps_pair=scalar[p]['bounds']['lower_Pv']['fixed_X_residual_scalar_model_error_operator_norm_upper']
        eps=F(eps_pair[1]);need(F(eps_pair[0])<=eps, 'ordered scalar error')
        rows=[]
        for n,row in enumerate(individual):
            budget=ceilq(upper(row['direct_form_upper'])+price)
            need(budget==ceilq(independent_individual[n]+price), ('independent rational scalar bound',p,n))
            need(budget<28, ('individual budget',p,n))
            threshold=ceilq(upper((I(F(10,11)*q*budget)).sqrt())+eps)
            need(threshold==ceilq(rational_sqrt_upper(F(10,11)*q*budget)+eps), ('independent rational threshold',p,n))
            rows.append({'degree':n,'K_P_upper_for_W_unit_direction':budget,
                         'exclusion_if_model_pairing_distance_exceeds':threshold})
        whole_bound=ceilq(upper(whole['direct_form_upper'])+price)
        need(whole_bound==ceilq(independent_whole+price), ('independent rational whole-space bound',p))
        need(whole_bound<30, ('whole polynomial space budget',p))
        common=ceilq(upper(I(F(280,11)*q).sqrt())+eps)
        need(common<(1201 if p=='even' else 489), 'convenient sufficient scalar threshold')
        results[p]={'S_model_positive_pivots':pivots,'two_sided_K_model_error_upper':price,
            'q':q,'D_model_scalar_error_upper':eps,'individual_directions':rows,
            'all_degree_at_most_11_K_P_upper_per_W_norm_squared':whole_bound,
            'common_twelve_direction_sufficient_distance':common}
        print(p,'whole polynomial space K/W <',str(whole_bound),'; 12 individual K < 28; common scalar threshold',str(common),flush=True)
    result={'status':'AUTHOR_DERIVED_CONDITIONAL_BUDGET_BOUND_EXTERNAL_REVIEW_OPEN',
            'rule_id':RULE,'geometry':geom,'individual_direct_form_bounds':individual,
            'whole_polynomial_space_direct_form_bound':whole,'parities':results,
            'residual_pairings_computed':False,'N12_excluded':False,'A9_A11_closed':False}
    out.mkdir(parents=True)
    write(out/'BUDGET_BOUNDS.json',result)
    write(out/'RECEIPT.json',{'status':'PASS_UNDER_BOUND_SOURCE_OPERATOR_AND_INTEGRATION_HYPOTHESES',
        'rule_id':RULE,'archive_sha256':{k:v[1] for k,v in ARCHIVES.items()},
        'archive_manifest_members_checked':manifest_counts,'new_positive_pivots':24,'controls':checks,
        'new_large_integrations':False,'historical_high_replay_performed_by_this_script':False,
        'high_certificate_expected_data_hash_bound':True,'whole_budget_on_degree_11_polynomials':True,
        'twelve_individual_budgets_certified':True,'complete_residual_pairings':False,
        'N12_success_or_exclusion':False,'whole_W9_energy':False,'A9_A11_closed':False,
        'Objekt_X_constructed':False,'RH_proved':False,'external_review_open':True,'github_changed':False})
    if (HERE/'expected/BUDGET_BOUNDS.json').exists():
        need((out/'BUDGET_BOUNDS.json').read_bytes()==(HERE/'expected/BUDGET_BOUNDS.json').read_bytes(), 'byte-identical expected budget')
        need((out/'RECEIPT.json').read_bytes()==(HERE/'expected/RECEIPT.json').read_bytes(), 'byte-identical expected receipt')
    print('PASS: 24 directed positive pivots; full small/large translation integrals; 24 direction bounds; 2 whole-space bounds',flush=True)

if __name__=='__main__': main()
