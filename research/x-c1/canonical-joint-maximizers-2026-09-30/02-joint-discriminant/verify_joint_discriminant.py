"""Joint generalized discriminant from rational interval and minimax bounds.

No Cholesky transform of M is formed. Inherited trial-resolvent and energy
factors keep the common annihilator visible. See JOINT_DISCRIMINANT.md.
"""
from interval_tools import *

def addmat(a,b):return [[add(x,y) for x,y in zip(row,col)] for row,col in zip(a,b)]
def submat(a,b):return [[sub(x,y) for x,y in zip(row,col)] for row,col in zip(a,b)]
def scale(a,s):return [[mul(x,point(s)) for x in row] for row in a]
def square(x):
    lo=F(0) if x[0]<=0<=x[1] else min(abs(x[0]),abs(x[1]))**2
    return rounded((lo,max(abs(x[0]),abs(x[1]))**2))
def frobenius(a):return total(square(x) for row in a for x in row)
def trace(a):return total(a[i][i] for i in range(len(a)))
def determinant(a):
    assert len(a)==len(a[0])==2
    return sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0]))
def positive2(a):assert a[0][0][0]>0 and determinant(a)[0]>0
def intersect(a,b):
    out=(max(a[0],b[0]),min(a[1],b[1]));assert out[0]<=out[1];return out
def intersectmat(a,b):return [[intersect(x,y) for x,y in zip(row,col)] for row,col in zip(a,b)]
def eye(n):return [[point(i==j) for j in range(n)] for i in range(n)]
def absolute_matrix(a):return [[absolute(x) for x in row] for row in a]
def pointmat(a):return [[point(x) for x in row] for row in a]
def sqrt_lower(x):
    assert x>=0;k=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    r=F(k,SCALE);assert r*r<=x;return r
def hull_from_order(lo,hi):
    out=scale(addmat(lo,hi),F(1,2));delta=submat(hi,lo)
    for i in range(len(lo)):
        for j in range(len(lo)):
            assert delta[i][i][1]>=0 and delta[j][j][1]>=0
            r=sqrt_upper(delta[i][i][1]*delta[j][j][1])/2
            out[i][j]=add(out[i][j],(-r,r))
    return symmetric(out)

def functional_enclosure(f,y,mc,n):
    """Enclose F N jointly using H Y_left=F_left and a right Neumann bound."""
    yl=[row[:6] for row in y];yr=[row[6:] for row in y]
    fl=[row[:6] for row in f];fr=[row[6:] for row in f]
    inverse_center=inverse(mc)
    error=submat(yl,mc);a=mm(error,inverse_center)
    absolute_a=absolute_matrix(a)
    contraction=max(map(sum,absolute_a));assert contraction<1
    h0=mm(fl,inverse_center)
    residual=mm(mm(h0,error),inverse_center)
    residual_abs=absolute_matrix(residual)
    resolvent=inverse(submat(eye(6),pointmat(absolute_a)))
    proposal=mm(pointmat(residual_abs),resolvent)
    radii=[[x[1]*(1+F('1e-60'))+F('1e-100') for x in row] for row in proposal]
    margins=[]
    for i in range(len(f)):
        for j in range(6):
            margin=radii[i][j]-residual_abs[i][j]-sum(radii[i][k]*absolute_a[k][j] for k in range(6))
            assert margin>0,('functional supersolution',i,j)
            margins.append(margin)
    h=[[add(h0[i][j],(-radii[i][j],radii[i][j])) for j in range(6)] for i in range(len(f))]
    joint=submat(fr,mm(h,yr))
    out=intersectmat(joint,mm(f,n))
    return out,{'right_contraction':contraction,'minimum_supersolution_margin':min(margins),
                'H_enclosure':h,'factor_on_N':out}

def atan_point(x,terms=60):
    assert abs(x)<1
    if x<0:return neg(atan_point(-x,terms))
    xx=point(x);power=xx;out=point(0)
    for k in range(terms):
        term=div(power,point(2*k+1))
        out=add(out,term if k%2==0 else neg(term))
        power=mul(power,mul(xx,xx))
    remainder=absolute(power)/F(2*terms+1)
    return add(out,(-remainder,remainder))
def angle_degrees(slope):
    assert absolute(slope)<1
    radians=(atan_point(slope[0])[0],atan_point(slope[1])[1])
    pi=sub(mul(point(16),atan_point(F(1,5))),mul(point(4),atan_point(F(1,239))))
    assert F(3)<pi[0]<pi[1]<F(22,7)
    return div(mul(point(180),radians),pi)

def certificate(r,nr,outer,key,alpha):
    n=matrix(nr['N']);y=matrix(nr['Y']);mc=matrix(r['central_left'])
    g=symmetric(matrix(nr['compressed_moment_entries']['G0']));positive2(g);gi=inverse(g,positive_pivots=True)
    flo=matrix(r['trial_resolvent_lower_factor']);fhi=matrix(r['trial_resolvent_upper_factor'])
    ll=symmetric(matrix(r['energy_Loewner_lower_in_raw_basis']))
    lu=symmetric(matrix(r['energy_Loewner_upper_in_raw_basis']))
    cl=matrix(r['energy_lower_factor']);cu=matrix(r['energy_upper_factor'])
    positive2(ll);positive2(lu)
    assert all(flo[i][i][0]>0 and fhi[i][i][0]>0 for i in range(8))
    terminal=outer['trials'][key.split('->')[1]]
    sb=symmetric(matrix(terminal['physical_Ritz_matrix']))
    en=symmetric(mm(mm(tr(n),sb),n));positive2(en)
    nu=F(terminal['physical_complement_gap_lower_exact'])
    theta=F(r['physical_energy_uniform_upper_exact']);assert 0<theta<nu
    fnlo,diagnostic_lo=functional_enclosure(flo,y,mc,n)
    fnhi,diagnostic_hi=functional_enclosure(fhi,y,mc,n)
    inverse_high_loss=trace(mm(mm(mm(gi,ll),gi),en))[1]/nu**2
    assert inverse_high_loss>=0
    phi_lower=frobenius(mm(mm(fnlo,gi),cl))[0]-inverse_high_loss
    assert phi_lower>0
    trace_lower=289*phi_lower/(17+theta)**2
    eps=theta*(theta+34)/289
    assert alpha[0]==1
    df=[[sub(fhi[i][j],mul(point(alpha[i]),fhi[0][j])) for j in range(8)] for i in range(8)]
    df[0]=[point(0) for _ in range(8)] # exact row subtraction, including shared entries
    dn,diagnostic_rest=functional_enclosure(df,y,mc,n)
    dn[0]=[point(0),point(0)]
    beta_minus_upper=frobenius(mm(mm(dn,gi),cu))[1]+eps
    gap_lower=trace_lower-2*beta_minus_upper
    assert gap_lower>0,('joint gap not certified',key)
    beta_plus_lower=trace_lower-beta_minus_upper
    phi_upper=frobenius(mm(mm(fnhi,gi),cu))[1]
    beta_plus_upper=phi_upper+eps
    assert 1<beta_minus_upper<beta_plus_lower<beta_plus_upper
    dg=determinant(g);assert dg[0]>0
    det_l_upper=min(determinant(en)[1],determinant(lu)[1]);assert det_l_upper>0
    a_lower=17**4*dg[0]**2/det_l_upper
    gg=norm_upper(g)
    bupper=addmat(lu,scale(eye(2),17*gg))
    a_upper=determinant(bupper)[1]**2/determinant(ll)[0]
    assert 0<a_lower<a_upper
    discriminant_lower=a_lower**2*gap_lower**2
    # Enclosures of the invariant coefficients; their correlations are retained
    # by the gap proof, not recovered by subtracting independent coefficient boxes.
    a_range=(a_lower,a_upper)
    b_range=(a_lower*trace_lower,a_upper*(phi_upper+2*eps))
    c_range=(a_lower*beta_plus_lower,a_upper*beta_plus_upper*beta_minus_upper)
    result={'positive_joint_discriminant':True,'trace_lower':trace_lower,
            'beta_minus_interval':(F(1),beta_minus_upper),
            'beta_plus_interval':(beta_plus_lower,beta_plus_upper),
            'gap_lower':gap_lower,'gap_squared_lower':gap_lower**2,
            'a_interval':a_range,'b_interval':b_range,'c_interval':c_range,
            'discriminant_lower':discriminant_lower,
            'one_minus_kappa_interval':(1/beta_plus_upper,1/beta_plus_lower),
            'trace_lower_display':sci(trace_lower),
            'beta_minus_display':display((F(1),beta_minus_upper)),
            'beta_plus_display':display((beta_plus_lower,beta_plus_upper)),
            'gap_lower_display':sci(gap_lower),
            'a_lower_display':sci(a_lower),
            'discriminant_lower_display':sci(discriminant_lower),
            'one_minus_kappa_display':display((1/beta_plus_upper,1/beta_plus_lower)),
            'inverse_high_loss_upper':inverse_high_loss,
            'small_pencil_term_upper':eps,'G_enclosure':g,
            'functional_lower':diagnostic_lo,'functional_upper':diagnostic_hi,
            'functional_remainder':diagnostic_rest,'rank_one_multipliers':alpha}
    # Try the requested projective chart, using raw moment enclosures.
    l=hull_from_order(ll,lu)
    l=symmetric(intersectmat(l,matrix(nr['compressed_moment_entries']['L0'])));positive2(l)
    z=hull_from_order(matrix(r['inverse_lower_family_in_raw_basis']),matrix(r['inverse_upper_family_in_raw_basis']))
    z=symmetric(intersectmat(z,matrix(nr['compressed_moment_entries']['Z0'])))
    rr=addmat(addmat(l,scale(g,34)),scale(z,289))
    m=addmat(addmat(l,scale(g,34)),scale(mm(mm(g,inverse(l,positive_pivots=True)),g),289))
    beta=(beta_plus_lower,beta_plus_upper)
    denominator=sub(rr[0][0],mul(beta,m[0][0]))
    numerator=sub(mul(beta,m[0][1]),rr[0][1])
    direction={'chart_x2_nonzero_certified':denominator[0]*denominator[1]>0,
               'first_row_denominator':denominator}
    if direction['chart_x2_nonzero_certified']:
        slope=div(numerator,denominator)
        # Divide the exact eigenvector equation by beta before interval evaluation
        # to avoid duplicating the same large uncertain eigenvalue.
        invbeta=(1/beta[1],1/beta[0])
        normalized_denominator=sub(mul(rr[0][0],invbeta),m[0][0])
        if normalized_denominator[0]*normalized_denominator[1]>0:
            normalized_slope=div(sub(m[0][1],mul(rr[0][1],invbeta)),normalized_denominator)
            slope=intersect(slope,normalized_slope)
        physical_slope=div(add(mul(g[0][0],slope),g[0][1]),(sqrt_lower(dg[0]),sqrt_upper(dg[1])))
        direction.update({'x1_over_x2':slope,'x1_over_x2_display':display(slope),
                          'physical_slope_from_second_basis_axis':physical_slope})
        if absolute(physical_slope)<1:
            angle=angle_degrees(physical_slope)
            direction.update({'physical_angle_degrees':angle,'physical_angle_display':display(angle)})
    result['direction_chart']=direction
    return result

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    base=Path(__file__).resolve().parent;bindings=json.loads((base/'input_bindings.json').read_bytes())
    data={}
    for name,sha in bindings['sha256'].items():
        raw=(base/'inputs'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha,('input hash mismatch',name)
        data[name]=json.loads(raw)
    projected=data['projected_verification.json'];assert projected['status']=='CERTIFIED_PROJECTED_OVERLAP_JOINT_MOMENT_GATE'
    assert data['projected_source_audit.json']['status']=='PASS'
    inherited=data['resolvent_verification.json']
    assert inherited['status']=='RATIONAL_CANONICAL_RESOLVENT_AUDIT_PASS'
    assert inherited['primary_sha256']==bindings['sha256']['primary.json']
    assert inherited['crosscheck_sha256']==bindings['sha256']['crosscheck.json']
    for name in ['primary.json','crosscheck.json','outer_primary.json']:
        assert projected['input_sha256'][name]==bindings['sha256'][name]
    proposal_raw=(base/'rank_one_parameters.json').read_bytes();proposal=json.loads(proposal_raw)
    results={}
    for run in ['primary.json','crosscheck.json']:
        d=data[run];assert d['source_commit']==bindings['source_commit']
        assert d['status']=='CANONICAL_EXTENSION_RESOLVENT_MOMENTS_CERTIFIED'
        assert d['uses_existing_terminal_positivity'] is True
        assert d['global_terminal_floor_inverse_used'] is False
        results[run]={}
        for key in ['A9->A11-even','A9->A11-odd']:
            r=certificate(d['results'][key],projected['runs'][run]['results'][key],data['outer_primary.json'],key,list(map(F,proposal[key])))
            results[run][key]=r
            print(run,key,'gap >=',r['gap_lower_display'],'discriminant >=',r['discriminant_lower_display'],flush=True)
            print('beta-',r['beta_minus_display'],'beta+',r['beta_plus_display'],'direction',r['direction_chart'].get('x1_over_x2_display','chart unresolved'),flush=True)
    out={'status':'JOINT_GENERALIZED_DISCRIMINANT_STRICTLY_POSITIVE',
         'research_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN',
         'source_commit':bindings['source_commit'],'integration_base':bindings['integration_base'],
         'input_sha256':bindings['sha256'],'rank_one_parameters_sha256':hashlib.sha256(proposal_raw).hexdigest(),
         'rounding_decimal_places':DIGITS,'results':results,
         'both_true_generalized_maxima_simple':True,'cholesky_transform_of_M_used':False,
         'large_operator_solves_rerun':False,'uses_existing_terminal_positivity':True,
         'forward_renewal_proved':False,'global_result_proved':False}
    a.out.write_text(json.dumps(rational(out),indent=2)+'\n',encoding='utf-8',newline='\n')
    print('BOTH JOINT GENERALIZED DISCRIMINANTS STRICTLY POSITIVE: PASS',flush=True)

if __name__=='__main__':main()
