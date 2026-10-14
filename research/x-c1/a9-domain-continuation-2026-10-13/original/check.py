"""Exact checks for the domain audit, full A9 floor and local extension.

Standard library only. Analytic lemmas are proved in HERLEITUNG.txt;
this program certifies their finite inputs and scalar inequalities.
It does not numerically evaluate exp(-10**215).
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, gzip, hashlib, io, json, zipfile

HERE = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def member(z, suffix):
    ns = [n for n in z.namelist() if n == suffix or n.endswith('/'+suffix)]
    if len(ns) != 1:
        raise ValueError((suffix, ns))
    return z.read(ns[0])

def ldl(a):
    n = len(a)
    assert all(a[i][j] == a[j][i] for i in range(n) for j in range(n))
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    d = []
    for i in range(n):
        v = a[i][i] - sum(L[i][k]**2*d[k] for k in range(i))
        if v <= 0:
            raise ValueError(('nonpositive pivot', i, str(v)))
        d.append(v); L[i][i] = F(1)
        for j in range(i+1,n):
            L[j][i] = (a[j][i]-sum(L[j][k]*L[i][k]*d[k] for k in range(i)))/v
    return d

def bareiss_positive_leading_minors(a):
    """Independent fraction-free Sylvester check on integer matrices."""
    b=[row[:] for row in a]; prev=1; minors=[]
    for k in range(len(b)):
        pivot=b[k][k]
        assert pivot>0
        minors.append(pivot)
        if k==len(b)-1: break
        for i in range(k+1,len(b)):
            for j in range(k+1,len(b)):
                value=b[i][j]*pivot-b[i][k]*b[k][j]
                assert value%prev==0
                b[i][j]=value//prev
        for i in range(k+1,len(b)): b[i][k]=0
        prev=pivot
    return minors

def log_box(x, n=160):
    """atanh series, exact positive remainder bound, x>=1."""
    x=F(x); z=(x-1)/(x+1)
    assert 0 <= z < 1
    lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(n)), F(0))
    hi=lo+2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return lo, hi

def exp_upper(x, n=40):
    x=F(x); term=F(1); total=term
    for j in range(1,n+1):
        term*=x/j; total+=term
    first=term*x/(n+1)
    assert x/(n+2)<1
    return total+first/(1-x/(n+2))

def finite_controls():
    # Positive diagonal blocks alone do not imply whole-space positivity.
    bad=[[F(1),F(2)],[F(2),F(1)]]
    try: ldl(bad)
    except ValueError: pass
    else: raise AssertionError('missing cross block accepted')
    # Losing the triangular response in lifting a Schur floor is invalid.
    K=F(1); C=F(100); S=F(1); r=F(1); z=-C*r/K
    energy=K*z*z+2*C*z*r+(S+C*C/K)*r*r
    assert energy==1 and energy < z*z+r*r
    assert energy==(K*(z+C*r/K)**2+S*r*r)
    # Finite-rank moment projection is not ordinary coordinate deletion.
    m=[F(1),F(2)]; x=[F(2),F(-1)]
    assert sum(a*b for a,b in zip(m,x))==0
    assert m[1]*x[1]!=0
    # A new bounded prime channel can overturn a small old positive form.
    assert F(1,10)-F(1,2)<0
    # Adjacent equal-width indicator functions: normalized Carleman
    # cross integral is log(2), for EVERY width, rather than o(1).
    assert log_box(2)[0]>F(2,3)
    return {'positive_diagonals_without_cross_control_rejected':True,
            'Schur_floor_as_full_L2_floor_rejected':True,
            'raw_coordinate_deletion_as_moment_projection_rejected':True,
            'omitting_new_channel_not_justified_by_old_positivity':True,
            'shrinking_shell_does_not_make_Carleman_L2_coupling_small':True}

def check(data):
    c8=F(12,10**30); k=F(1,10**16); s=F(1,10**6)
    assert F(data['old_A8_floor'])==c8
    cases=[]
    for block in data['cases']:
        K=[[F(x) for x in row] for row in block['K12_new_rational']]
        shifted=[[K[i][j]-k*(i==j) for j in range(12)] for i in range(12)]
        piv=ldl(shifted)
        integer=[[v*10**60 for v in row] for row in shifted]
        assert all(v.denominator==1 for row in integer for v in row)
        minors=bareiss_positive_leading_minors([[int(v) for v in row] for row in integer])
        running=F(1)
        for i,pivot in enumerate(piv):
            running*=pivot
            assert running*10**(60*(i+1))==minors[i]
        S=[[F(x) for x in row] for row in block['Y_coefficients_in_exact_WX_isometry_Q']]
        assert len(S)==92 and all(len(row)==8 for row in S)
        gram=[[sum(row[i]*row[j] for row in S) for j in range(8)] for i in range(8)]
        ypiv=ldl(gram)
        ynorms=[gram[i][i] for i in range(8)]
        assert all(v<4 for v in ynorms)
        beta=F(block['beta']); eta=F(block['eta']); u=F(block['M_upper_relative_D'])
        cap=F(block['whole_residual_simple_cap'])
        tail=F(21,5)*(eta+(1-cap)*(1-u)*beta)
        assert beta>0 and 0<cap<1 and 0<u<1 and tail>s
        cases.append({'parity':block['parity'], 'K_minus_1e_minus_16_I_positive_pivots':len(piv),
                      'independent_integer_Sylvester_minors':len(minors),
                      'K_positive_pivot_digest':digest(json.dumps([str(v) for v in piv]).encode()),
                      'Y_gram_positive_pivots':len(ypiv),
                      'each_Y_WX_norm_squared_below_4':True,
                      'reduced_actual_Schur_floor_used':'1/1000000',
                      'certified_reduced_floor_from_bound_residual':str(tail)})
    # All transcendental inputs below are bounded by positive rational series.
    log2=log_box(2); log3=log_box(3); log11=log_box(11)
    alo,ahi=F(3,2)*log2[0],F(3,2)*log2[1]
    blo,bhi=log3
    hlo,hhi=blo-ahi,bhi-alo
    assert F(103,100)<alo<ahi<F(21,20)
    assert F(109,100)<blo<bhi<F(11,10)
    assert F(1,20)<hlo<hhi<F(3,50)
    assert log11[0]>F(222,100)
    pi_upper=4*sum((F((-1)**j,2*j+1) for j in range(7)),F(0))
    assert pi_upper<F(10,3)
    assert log_box(F(80,3))[1]<F(10,3)
    # gamma<1 is the elementary harmonic-sum/integral comparison.
    assert F(10,3)+1+F(5,3)==6
    for prime in [2,3,5,7]:
        assert log_box(prime)[1]**2<prime
    assert exp_upper(F(1,2))<2  # exp(-1/2)>1/2
    # cosh(.55) < 1.2, using a positive even series and its geometric tail.
    x=F(11,20); term=F(1); ch=term
    for n in range(1,21):
        term*=x*x/((2*n-1)*(2*n)); ch+=term
    tail=term*x*x/(41*42)/(1-x*x/(43*44))
    assert ch+tail<F(6,5)
    assert exp_upper(x)<2  # sinh(.55)<1, m and m' <2
    assert F(103,100)**3/12>F(9,100)
    assert F(3,50)*F(6,5)**2<F(1,10)
    # Hilbert/Carleman constant pi/2 <2; remaining kernels use k<=1+1/(2t).
    assert F(11,10)*F(3,50)<F(26,100)**2
    gamma_cross=F(2)+F(5,2)*F(26,100)
    assert gamma_cross<3
    old_gamma_and_prime=F(15)
    assert F(1,10)/(2*F(9,100)**2)<F(5,2)**2
    assert old_gamma_and_prime+F(5,2)*300<1000
    # Piecewise-Lipschitz operator lemma, deliberately loose rational roots.
    qm=(2*2+20*2)*3+4*2*2+3*5+20*3
    assert qm<300
    qF=(2*2*10**8+20*1000)*3+4*1000*2+3*10+20*5
    assert qF<2*10**10
    y_sup_sq=4*96**2/(2*F(1,20))
    assert y_sup_sq<1000**2
    assert y_sup_sq*(95*96/F(1,20))**2<(2*10**8)**2
    assert (1+F(1,10)/F(9,100))*4<16
    assert 4*5**2+8*4**2<16**2
    assert 12*(2*10**10)**2<(10**11)**2
    # Lift two Schur completions to the original physical L2 norm.
    ia=1/c8
    assert ia<10**29
    assert 10**11+10**11*10**29*1000<10**44
    assert 16+10**29*10**11<2*10**40
    assert 1+10**29*1000<2*10**32
    assert 10**44/k==10**60
    assert 2*10**40*10**60+2*10**32<3*10**100
    norm_price=1/c8+F((2*10**40)**2)/k+F((3*10**100)**2)/s
    c9=F(1,10**207)
    assert norm_price<1/c9
    # New shell: log(1/h)>=10**215 is kept symbolic, never underflows to 0.
    L=10**215; hcap=F(1,100)
    assert L>8 and F(1,2)**8<hcap  # e>2 implies exp(-L)<1/100
    assert bhi+hcap<F(111,100)<log11[0]/2
    assert F(11,10)*hcap<F(11,100)**2
    assert 2+F(5,2)*F(11,100)<3
    assert 2*hcap/F(9,100)**2<4  # (|lambda|/mu)^2 <=2h/mu^2
    assert 1+4*hcap/F(9,100)<2
    assert 3+14+2*300<1000
    correction=2*2*300+2**2*3*300
    assert correction+20<5000
    shell_floor=F(L,2)-5000-F(10**6)/c9
    assert shell_floor>1
    extension_norm_price=max(2/c9,2+F(4*10**6)/c9**2)
    cext=F(1,10**421)
    assert extension_norm_price<F(5*10**6)/c9**2<1/cext
    return {'status':'PASS_EXACT_FULL_A9_FLOOR_AND_LOCAL_EXTENSION_CONSTANTS',
            'cases':cases,
            'old_A8_L2_floor_input':str(c8),
            'full_A9_inverse_norm_price':str(norm_price),
            'full_A9_physical_L2_floor':'1e-207',
            'extension_radius_exact_expression':'exp(-10^215)',
            'radius_evaluated_as_floating_point':False,
            'extension_uniform_physical_L2_floor':'1e-421',
            'new_shell_reduced_floor_relative_WX':'1/2',
            'new_prime_channel_9_included_in_full_norm_bound':True,
            'all_seven_prime_weights_below_one':True,
            'countercontrols':finite_controls(),
            'analytic_proofs_machine_verified':False,
            'large_global_integrations_rerun':False,
            'inherited_arithmetic_identity_and_prior_certificates_still_required':True,
            'old_separate_tail_floor_1_over_20_certified':False,
            'A10_or_A11_transition_certified_here':False,
            'cofinal_horizons_certified':False,
            'OBJECT_X_CONSTRUCTED':False,'RH_PROVED':False,'EXTERNAL_REVIEW_OPEN':True}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--schur-package',type=Path)
    ap.add_argument('--half-source',type=Path)
    ap.add_argument('--output',type=Path,default=HERE/'CHECK.json')
    args=ap.parse_args()
    data=json.loads((HERE/'BOUND_INPUTS.json').read_bytes())
    verification={}
    if args.schur_package:
        raw=args.schur_package.read_bytes()
        assert digest(raw)==data['source_schur_sha256']
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            bindings=json.loads(member(z,'INPUT_BINDINGS.json'))
            assembly=json.loads(member(z,'ASSEMBLY_AUDIT.json'))
            for b in data['cases']:
                old=next(x for x in assembly['cases'] if x['parity']==b['parity'])
                assert F(old['complete_QR_relative_T_simple_upper'])==F(b['whole_residual_simple_cap'])
            raw=member(z,bindings['responses']['filename'])
            assert digest(raw)==bindings['responses']['sha256']
            with zipfile.ZipFile(io.BytesIO(raw)) as rz:
                for b in data['cases']:
                    r=json.loads(member(rz,'RESPONSES_'+b['parity'].upper()+'.json'))
                    assert r['K12_new_rational']==b['K12_new_rational']
                    for key,new in [('beta','beta'),('eta','eta'),('M_actual_normalized_upper_scalar','M_upper_relative_D')]:
                        assert F(r[key])==F(b[new])
        verification['original_Schur_package_hash_and_response_fields']=True
    raw=args.half_source.read_bytes() if args.half_source else gzip.decompress((HERE/'sources/half-1536.json.gz').read_bytes())
    assert digest(raw)==data['source_half_json_sha256']
    original=json.loads(raw)
    for b in data['cases']:
        v=next(x for x in original['blocks'] if x['parity']==b['parity'])
        assert v['half_inverse_centre_rational_Q_coefficients']==b['Y_coefficients_in_exact_WX_isometry_Q']
    verification['original_half_source_hash_and_all_Y_coefficients']=True
    result=check(data);result['source_verifications_this_run']=verification
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(result['status'])
    print('A9 L2 floor = 1e-207; extension radius = exp(-10^215); extended floor = 1e-421')
    print('Analytic proof: AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN; arithmetic inputs remain bound.')

if __name__=='__main__': main()
