#!/usr/bin/env python3
"""Exact witnesses for two excluded C1 readout classes. See PROOF.md.

All computations use integer/Fraction arithmetic. Universal operator and
infinite-series assertions are analytic theorems, not sampled sign tests.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse,hashlib,json

HERE=Path(__file__).resolve().parent
ANCHOR='617ffe2a3bfe12bef768b536b9eeffbbfb21f1da'
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_nonlocal.py','input_bindings.json','nonlocal_results.json','nonlocal_checks.log']

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p
def add(p,q):
    out=[F(0)]*max(len(p),len(q))
    for i,v in enumerate(p):out[i]+=v
    for i,v in enumerate(q):out[i]+=v
    return trim(out)
def scale(p,c):return trim([c*x for x in p])
def mul(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]+=x*y
    return trim(out)
def derivative(p):return trim([i*p[i] for i in range(1,len(p))] or [F(0)])
def evaluate(p,x):
    out=F(0)
    for c in reversed(p):out=out*x+c
    return out
def integral(p,left,right):return sum((v*(right**(i+1)-left**(i+1))/(i+1) for i,v in enumerate(p)),F(0))
def bump(delta):
    base=[F(1),F(0),-1/delta**2]
    psi=mul(mul(base,base),base)
    phi=add(derivative(derivative(psi)),scale(psi,-F(1,4)))
    return psi,phi

def log_bounds(q,terms=180):
    q=F(q);assert q>=1
    x=(q-1)/(q+1);xx=x*x;term=x;total=F(0)
    for k in range(terms):total+=term/(2*k+1);term*=xx
    return (2*total,2*(total+term/(2*terms+1)/(1-xx)))
def exp_bounds(x,terms=40):
    x=F(x);assert 0<=x<terms+2
    term=F(1);total=F(1)
    for k in range(1,terms+1):term*=x/k;total+=term
    next_term=term*x/(terms+1)
    return total,total+next_term/(1-x/(terms+2))
def root_bounds(n):
    scale=10**30;k=isqrt(n*scale**2)
    return F(k,scale),F(k+1,scale)
def interval_add(x,y):return x[0]+y[0],x[1]+y[1]
def interval_scale(x,c):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def interval_sub(x,y):return x[0]-y[1],x[1]-y[0]
def interval_away(x,d):return x[1]<-d or x[0]>d
def out_decimal(x,places=25,upper=False):
    x=F(x);s=10**places
    z=-((-x.numerator*s)//x.denominator) if upper else x.numerator*s//x.denominator
    sign='-' if z<0 else '';z=abs(z)
    return sign+str(z//s)+'.'+str(z%s).zfill(places)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=HERE.parents[2])
    mode=parser.add_mutually_exclusive_group();mode.add_argument('--write',action='store_true');mode.add_argument('--verify',action='store_true')
    args=parser.parse_args();root=args.root.resolve()
    checks=[];values={};log=[]
    def check(name,condition):
        assert condition,name
        checks.append(name);log.append('PASS '+name)
    def record(name,x):
        x=F(x);values[name]=dict(exact=str(x),decimal_lower=out_decimal(x),decimal_upper=out_decimal(x,upper=True))
    binding=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
    check('analytic provenance anchor is 617ffe2',binding['anchor']==ANCHOR)
    check('six distinct immutable analytic provenance files',len(binding['files'])==len({x['path'] for x in binding['files']})==6)
    for item in binding['files']:
        raw=(root/item['path']).read_bytes()
        check('bytes SHA256 and Git blob '+item['path'],len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'])
    logs={q:log_bounds(q) for q in (2,3,4,5,7,8)}
    check('log2 lies strictly between 69 and 70 hundredths',F(69,100)<logs[2][0]<=logs[2][1]<F(7,10))
    check('log3 exceeds one point zero nine',logs[3][0]>F(109,100))
    check('B lies strictly above four fifths',logs[5][0]/2>F(4,5))
    check('strict active set at a one ends at seven',logs[7][1]<2<logs[8][0])
    delta=F(1,100);distance=F(3,4)
    psi,phi=bump(delta);dpsi=derivative(psi);ddpsi=derivative(dpsi)
    check('explicit nonnegative cubic bump factorization has degree six',len(psi)==7 and psi==mul(mul([F(1),F(0),-1/delta**2],[F(1),F(0),-1/delta**2]),[F(1),F(0),-1/delta**2]))
    check('bump and first two derivatives vanish at both support endpoints',all(evaluate(pol,t)==0 for pol in (psi,dpsi,ddpsi) for t in (-delta,delta)))
    check('Mellin-annihilated source has zero traces and is nonzero',evaluate(phi,-delta)==evaluate(phi,delta)==0 and evaluate(phi,0)<0)
    check('differential annihilator identity holds coefficient by coefficient',add(phi,add(scale(ddpsi,-1),scale(psi,F(1,4))))==[F(0)])
    check('exact Mellin exponents are roots of the annihilator',all(lam*lam-F(1,4)==0 for lam in (-F(1,2),F(1,2))))
    check('bump and annihilated source are even',all(v==0 for i,v in enumerate(psi) if i%2) and all(v==0 for i,v in enumerate(phi) if i%2))
    mass=integral(psi,-delta,delta);norm=integral(mul(phi,phi),-delta,delta)
    check('exact positive bump mass is 32 delta over 35',mass==F(32,35)*delta>0)
    check('exact source norm agrees with integrated derivative identity',norm==integral(mul(ddpsi,ddpsi),-delta,delta)+F(1,2)*integral(mul(dpsi,dpsi),-delta,delta)+F(1,16)*integral(mul(psi,psi),-delta,delta))
    check('explicit rational source norm below forty million',0<norm<4*10**7)
    check('two witness supports are disjoint and inside the canonical B core',2*delta<distance and distance/2+delta<F(4,5)<logs[5][0]/2)
    check('all mixed prime channels vanish by the log2 log3 gap',logs[2][1]<distance-2*delta<distance+2*delta<logs[3][0])
    check('fixed witness supports have gap 73 over 100',distance-2*delta==F(73,100))
    check('fixed locality obstruction radius is 73 over 200',(distance-2*delta)/2==F(73,200))
    # Formal polynomial in m: (2m+1/2)^2-1/4 = 2m(2m+1).
    annihilator=add(mul([F(1,2),F(2)],[F(1,2),F(2)]),[-F(1,4)])
    check('all Gamma mode factors satisfy an exact polynomial identity',annihilator==mul([F(0),F(2)],[F(1),F(2)]))
    check('Mellin carrier mode vanishes and every higher integer mode is positive',annihilator==[F(0),F(2),F(4)] and evaluate(annihilator,F(0))==0)
    check('first surviving Gamma mode has exact squared coefficient 36',evaluate(annihilator,F(1))**2==36)
    exponential=exp_bounds(F(5,2)*distance)
    check('exact Taylor remainder certifies exp fifteen eighths below seven',F(5,2)*distance==F(15,8) and exponential[1]<7)
    lower=F(36,7)*mass**2
    check('complete mixed form is strictly below minus one over 2500 via positive series',lower>F(1,2500))
    check('two-state locality approximation error exceeds one e minus eleven',lower/norm>F(1,10**11))
    # Exact linear-algebra identity: orthogonal output images give equal
    # squared norms to u+v and u-v; form energies differ by 4 q(u,v).
    cplus=[F(1),F(1)];cminus=[F(1),F(-1)]
    check('even and odd twin states have equal physical norms',sum(x*x for x in cplus)==sum(x*x for x in cminus)==2)
    check('twin-state polarization difference is four times mixed pairing',2*cplus[0]*cplus[1]-2*cminus[0]*cminus[1]==4)
    eta=F(1,1000)
    check('shifted rank witnesses retain prime-free separated support blocks',logs[2][1]<distance-2*delta-2*eta and distance+2*delta+2*eta<logs[3][0])
    check('all shifted rank witnesses remain inside the canonical B core',distance/2+delta+eta<F(4,5))
    # Concrete rank-three instance; the arbitrary-N Vandermonde proof is
    # analytic in PROOF.md and is not inferred from this finite instance.
    s=F(1001,1000);nodes=[1/s,F(1),s]
    check('explicit reciprocal Vandermonde nodes are positive and distinct',0<nodes[0]<nodes[1]<nodes[2] and nodes[0]*nodes[1]*nodes[2]==1)
    check('node positions one half log z stay within eta',log_bounds(s)[1]/2<eta)
    mat=[[z**m for m in (1,2,3)] for z in nodes]
    determinant=(mat[0][0]*(mat[1][1]*mat[2][2]-mat[1][2]*mat[2][1])
                 -mat[0][1]*(mat[1][0]*mat[2][2]-mat[1][2]*mat[2][0])
                 +mat[0][2]*(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0]))
    vandermonde=nodes[0]*nodes[1]*nodes[2]*(nodes[1]-nodes[0])*(nodes[2]-nodes[0])*(nodes[2]-nodes[1])
    check('rank-three exact determinant equals positive Vandermonde product',determinant==vandermonde>0)
    record('rank_witness_translation_margin',eta);record('rank_three_rational_Vandermonde_determinant',determinant)
    for name,x in [('bump_half_width',delta),('two_bump_center_distance',distance),('bump_mass',mass),('single_source_norm_squared',norm),
                   ('mixed_form_strict_upper',-lower),('fixed_locality_radius_threshold',F(73,200)),('relative_two_state_error_strict_lower',lower/norm),
                   ('published_relative_error_lower',F(1,10**11)),('exp_15_over_8_upper',exponential[1])]:record(name,x)
    for n,v in enumerate(psi):record('psi_coefficient_'+str(n),v)
    for n,v in enumerate(phi):record('phi_coefficient_'+str(n),v)
    # A concrete isolated four-bump certificate for each strict active q at a=1.
    prime_delta=F(1,10000);c=F(1,1000);psi_p,phi_p=bump(prime_delta)
    prime_norm=integral(mul(phi_p,phi_p),-prime_delta,prime_delta)
    check('prime witness bump satisfies identical exact zero-moment and H1 boundary conditions',all(evaluate(pol,t)==0 for pol in (psi_p,derivative(psi_p),derivative(derivative(psi_p)),phi_p) for t in (-prime_delta,prime_delta)))
    check('prime witness norm is positive',prime_norm>0)
    active=[(2,2),(3,3),(4,2),(5,5),(7,7)]
    affine=[(-F(1,2),-1),(-F(1,2),1),(F(1,2),-1),(F(1,2),1)]
    cases=[]
    for q,prime in active:
        ell=logs[q]
        centers=[interval_add(interval_scale(ell,s),(t*c,t*c)) for s,t in affine]
        check('q'+str(q)+' four bumps lie strictly inside endpoint one',centers[0][0]-prime_delta>-1 and centers[-1][1]+prime_delta<1)
        check('q'+str(q)+' four source supports are disjoint',all(centers[i+1][0]-centers[i][1]>2*prime_delta for i in range(3)))
        graph=[[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(i+1,4):
                ds=affine[j][0]-affine[i][0];dt=affine[j][1]-affine[i][1]
                diff=interval_add(interval_scale(ell,ds),(dt*c,dt*c))
                for channel,_ in active:
                    if channel==q and ds==1 and dt==0:graph[i][j]=graph[j][i]=1
                    else:assert interval_away(interval_sub(diff,logs[channel]),2*prime_delta),(q,i,j,channel)
        check('q'+str(q)+' exactly two q edges and no other prime overlaps',graph==[[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]] and 2*prime_delta<logs[2][0])
        rad=root_bounds(q)
        weight=(logs[prime][0]/rad[1],logs[prime][1]/rad[0])
        check('q'+str(q)+' exact von Mangoldt weight is strictly positive',0<weight[0]<=weight[1])
        if q==2:check('q2 signed-channel witnesses already lie inside B',centers[-1][1]+prime_delta<logs[5][0]/2)
        for parity in (0,1):
            for eps in (-1,1):
                sign=(-1)**parity;coeff=[sign,eps,sign*eps,1]
                check('q'+str(q)+' parity '+str(parity)+' sign '+str(eps)+' exact parity norm and isolated-channel Rayleigh identity',
                      list(reversed(coeff))==[sign*x for x in coeff] and sum(x*x for x in coeff)==4
                      and sum(coeff[i]*graph[i][j]*coeff[j] for i in range(4) for j in range(4))==4*eps)
                cases.append(dict(q=q,prime=prime,parity=parity,epsilon=eps,coefficients=coeff,
                    physical_norm_squared=str(4*prime_norm),signed_prime_Rayleigh_multiplier_of_weight=-eps,
                    all_other_prime_quadratic_terms_zero=True))
        record('q'+str(q)+'_weight_lower',weight[0]);record('q'+str(q)+'_weight_upper',weight[1])
    check('both signs in both parities certified for all five channels',len(cases)==20)
    record('prime_witness_half_width',prime_delta);record('prime_witness_offset',c);record('prime_single_bump_norm_squared',prime_norm)
    check('factor 200 refers to immediate b1c0186 outer window',F(1,10**10)/F(5,10**13)==200)
    check('factor 200 million refers to older ca3849a outer window',F(1,10**10)/F(5,10**19)==200000000)
    report=dict(anchor=ANCHOR,status='AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',bound_inputs=6,
        verdict='C1-FINITE-PROPAGATION-PLUS-FINITE-RANK-AND-CHANNEL-GRAM-CLASSES-EXCLUDED',
        checks=checks,check_count=len(checks),values=values,isolated_prime_cases=cases,
        exact_mellin_constraints=2,A1_used=False,source_class='Actual compactly supported physical H1 sources; auxiliary counterexample tests, no change of inherited near-null source.',
        analytic_proof='PROOF.md; Mellin annihilator, full Gamma series, arbitrary-N Vandermonde rank obstruction, and exact isolated-prime constructions.',
        universal_no_go_is_a_finite_sampling_claim=False,omitted_Gamma_modes='Retained in exact convergent series; all higher summands are positive for the mixed witness.',
        forbidden_exact_physical_propagation='R_a<a on any B<=a<=1; output must have a specified physical-position direct-integral support structure.',
        finite_rank_nonlocal_correction_repairs_exact_local_Gram=False,
        infinite_rank_separated_Gamma_pairing_proved=True,
        rank_obstruction='If T=L+K and rank K<=m, separated local outputs give mixed Gram rank<=2m; exact Gamma witnesses have arbitrary rank N, so choose N=2m+1.',
        quantitative_error_relative_to='Physical L2 squared norm; at least one of the fixed even/odd twin states.',
        quantitative_one_e_minus_eleven_error_applies_to='Pure finite propagation T, with no extra finite-rank nonlocal correction, and R<73/200.',
        negative_mixed_pairing_is_negative_Weil_source=False,negative_Weil_source_certified=False,
        arbitrary_nonlocal_C1_readout_excluded=False,indefinite_channel_observables_in_positive_mediator_excluded=False,
        intrinsic_positive_readout_constructed=False,C1_mediator_constructed=False,Object_X_constructed=False,
        new_transport_window_certified=False,moving_191D_low_profile_closed=False,non_summable_transport_certified=False,
        inherited_numerical_matrix_chain_replayed=False,
        reproduction_scope='All new witnesses and rational inequalities rebuilt; six analytic provenance files bound. Prior matrix certificates are unchanged and are not rerun by this checker.')
    log.append('TOTAL '+str(len(checks))+' NEW EXACT CHECKS PASS');log.append(report['verdict'])
    js=json.dumps(report,indent=2,sort_keys=True)+'\n';logtext='\n'.join(log)+'\n'
    if args.write:
        (HERE/'nonlocal_results.json').write_text(js,encoding='utf-8',newline='\n')
        (HERE/'nonlocal_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
        (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in PAYLOAD),encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'nonlocal_results.json').read_bytes()==js.encode('utf-8'),'JSON replay mismatch'
        assert (HERE/'nonlocal_checks.log').read_bytes()==logtext.encode('utf-8'),'log replay mismatch'
        lines=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        assert [x.split('  ',1)[1] for x in lines]==PAYLOAD
        for line in lines:
            digest,name=line.split('  ',1);assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
        print('REPLAY and all seven nonlocal-package SHA256 hashes PASS')
    print(logtext,end='')

if __name__=='__main__':main()
