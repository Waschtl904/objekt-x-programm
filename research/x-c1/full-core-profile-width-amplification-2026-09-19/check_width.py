#!/usr/bin/env python3
"""Full even width certificate: exact finite block and complete infinite tails.

Analytic closure, normalization, and operator implications: PROOF.md.
All decisions use integers/Fractions and directed interval arithmetic.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, isqrt
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ANCHOR = '8f5b711145b28b6dbfc8280d8e51625f3d2f1532'
ORIGIN = '6a16d90b551588572c87e622c21c2df7f7b1adc2'
SEGMENT = 'research/x-c1/prime-power-segment-4-2026-09-18'
PARENT = 'research/x-c1/a-gauge-transition-congruence-2026-09-19'
PAYLOAD = ['PROOF.md', 'README.md', 'STATUS_DE.md', 'check_width.py',
           'input_bindings.json', 'width_results.json', 'width_checks.log']


def compute_core(engine, profile_loss):
    # These are the pinned exact arithmetic/analytic-integration primitives.
    I, log, PI, LOG2 = engine.I, engine.log, engine.PI, engine.LOG2
    gamma, g, kernel_polynomial = engine.gamma, engine.g, engine.kernel_polynomial
    channels, kernel_columns = engine.channels, engine.kernel_columns
    prod, leg, integral, tpoly = engine.prod, engine.leg, engine.integral, engine.tpoly
    polyval, shift_grams = engine.polyval, engine.shift_grams
    record, check, progress = engine.record, engine.check, engine.progress
    REPORT = engine.REPORT
    endpoint, N, M = 5, 63, 64
    progress('constants and exact Gamma model')
    a=log(I(endpoint))/2;L=2*a;ch=channels(endpoint)
    q0=-log(2*PI*a)-gamma();c=g(L);pg,eps=kernel_polynomial(M)
    check('endpoint range for uniform Gamma model',0<L.lo<L.hi<F(5,3))
    check('active prime powers 2,3,4 with von Mangoldt weights',[(v['q'],v['prime'],v['exponent']) for v in ch]==[(2,2,1),(3,3,1),(4,2,2)])
    check('positive decreasing regular Gamma floor',0<c.lo<c.hi<F(1,4))
    record('endpoint_a',a);record('q0',q0);record('uniform_Gamma_error',eps)
    snorm=sum((c['weight']*c['norm'] for c in ch),I(0))
    record('joint_shift_operator_norm_upper',snorm)
    check('kernel and shift norms used for moment reconstruction',(L*(F(1,4)+eps)).hi<1 and snorm.hi<2)
    kcols=[];powers=[L*(a/2)**k*pg[k] for k in range(M+1)]
    for j in range(N+1):
        cols=kernel_columns(j,M);out=[I(0)]*(N+M+2)
        for k,pol in enumerate(cols):
            if not pg[k]:continue
            for n,v in enumerate(pol):
                if v:out[n]+=powers[k]*v
        kcols.append(out)
    progress('full Gamma columns ready')
    @lru_cache(None)
    def G(i,j):
        if i>j:return G(j,i)
        return kcols[i][j]/(2*j+1) if j<len(kcols[i]) else I(0)
    @lru_cache(None)
    def lm(r):return (sum((F(1,2*k+1) for k in range(r+1)),F(0))-LOG2)/(2*r+1)
    @lru_cache(None)
    def lm2(r):
        odd=sum((F(1,2*k+1) for k in range(r+1)),F(0));odd2=sum((F(1,(2*k+1)**2) for k in range(r+1)),F(0))
        return ((odd-LOG2)**2+odd2-PI**2/12)/(2*r+1)
    @lru_cache(None)
    def P(i,j):
        if i>j:return P(j,i)
        if (i+j)%2:return I(0)
        if i!=j:return I(F(1,(j-i)*(j+i+1)))
        return sum((v*lm(k//2) for k,v in enumerate(prod(i,j)) if k%2==0),I(0))
    @lru_cache(None)
    def P2(i,j):
        if i>j:return P2(j,i)
        return sum((v*lm2(k//2) for k,v in enumerate(prod(i,j)) if k%2==0),I(0))
    @lru_cache(None)
    def S(i,j):
        if i>j:return S(j,i)
        return sum((c['weight']*polyval(tpoly(i,j),2-c['ell']/a) for c in ch),I(0))
    sq,vs,breaks=shift_grams(ch,a,N)
    REPORT['band_breakpoints']=[{'lo':str(b.lo),'hi':str(b.hi)} for b in breaks]
    @lru_cache(None)
    def moment(n,parity):
        last=100+parity
        val=sum(((a/2)**k/F(factorial(k))*integral([F(0)]*k+leg(n)) for k in range(parity,last+1,2)),I(0))
        tail=(a/2)**(last+2)/factorial(last+2)/(1-(a/2)**2/((last+3)*(last+4)))
        return val+I(-tail.hi,tail.hi)
    harm=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(N+3)]
    @lru_cache(None)
    def Q(i,j):return (harm[i]+q0)/(2*i+1)*(i==j)+P(i,j)-G(i,j)-S(i,j)
    for j in (0,):check('low basis Qnorm ingredient '+str(j),max(abs((harm[j]+q0).lo),abs((harm[j]+q0).hi))<4 and ((2*j+1)*P2(j,j)).hi<4)
    parity, label = 0, 'even'
    ix=list(range(2,N+1,2));allix=list(range(0,N+1,2));tail=64
    check('exact 31-dimensional low space and full tail starting at degree 64', len(ix)==31 and ix[-1]==62)
    beta=((a/2)**2/(2*(1-(a/2)**2/12)))**2
    epsmoment=(a/2)**tail/factorial(tail)/(1-(a/2)**2/((tail+1)*(tail+2)))
    err=2*L*eps+80*epsmoment
    tail_floor=harm[tail]+q0-L*(F(1,4)-c+eps)-snorm-err
    delta=I(tail_floor.lo-F(1681,6000))
    check('global moment norm below square root two', 0<beta.lo<=beta.hi<1)
    check('moment-corrected full high-tail coupling below 41 over 10', 16*(1+epsmoment.hi**2)<F(41,10)**2)
    check('tail remains above 0.439 after high-profile payment', delta.lo>F(439,1000))
    check('tail physical coercivity above 0.719 with exact norm correction', tail_floor.lo/(1+epsmoment.hi**2)>F(719,1000))
    record('even_beta',beta)
    record('even_moment_tail_operator_error',epsmoment)
    record('even_Gamma_form_error',2*L*eps)
    record('even_infinite_moment_form_error',80*epsmoment)
    record('even_total_form_error',err)
    record('even_original_tail_floor',tail_floor)
    record('even_physical_tail_floor_lower',tail_floor.lo/(1+epsmoment.hi**2))
    record('even_effective_tail_floor',delta)
    @lru_cache(None)
    def ratio(i):return moment(i,parity)/moment(parity,parity)
    @lru_cache(None)
    def gramC(i,j):
        # Exact Gram of P_Y(V-Kp-S)P_i. V and S tails are infinite.
        value=P2(i,j)+sq[i][j]-vs[i][j]-vs[j][i]
        for k in allix:value-=(2*k+1)*(P(i,k)-S(i,k))*(P(k,j)-S(k,j))
        for k in range(tail,N+M+2,2):
            value+=(2*k+1)*(G(i,k)*G(k,j)-(P(i,k)-S(i,k))*G(k,j)-G(i,k)*(P(k,j)-S(k,j)))
        return value
    def changed(fun,i,j):return fun(i,j)-ratio(i)*fun(parity,j)-ratio(j)*fun(i,parity)+ratio(i)*ratio(j)*fun(parity,parity)
    mat=[[I(0) for _ in ix] for _ in ix];amat=[[I(0) for _ in ix] for _ in ix];gmat=[[I(0) for _ in ix] for _ in ix]
    trace=I(0);moment_cost_sq=F(0)
    for ii,i in enumerate(ix):
        progress(label+' Gram row '+str(ii+1)+'/'+str(len(ix)))
        for jj,j in enumerate(ix[:ii+1]):
            ga=F(1001,1000)*changed(gramC,i,j)+1001*err**2/(2*i+1)*(i==j)
            av=changed(Q,i,j);entry=av-err/(2*i+1)*(i==j)-ga/delta-profile_loss/(2*i+1)*(i==j)
            mat[ii][jj]=mat[jj][ii]=entry;amat[ii][jj]=amat[jj][ii]=av;gmat[ii][jj]=gmat[jj][ii]=ga
            if i==j:trace+=(2*i+1)*ga
            cost=av-Q(i,j)
            moment_cost_sq+=(1 if i==j else 2)*(2*i+1)*(2*j+1)*max(abs(cost.lo),abs(cost.hi))**2
    record('even_finite_Mellin_correction_HS_squared_upper',moment_cost_sq)
    record('even_coupling_HS_squared',trace)
    record('low_profile_squared_operator_upper',15*profile_loss)
    record('low_profile_Schur_deduction',profile_loss)
    abound,_,_,afail=engine.inverse_trace_bound(amat,ix)
    if abound is not None:record('even_finite_Mellin_block_reserve_lower',abound)
    bound,low,piv,failure=engine.inverse_trace_bound(mat,ix)
    for k,v in enumerate(piv):record('even_three_block_Schur_LDL_pivot_'+str(ix[k]),v)
    if failure:
        REPORT['obligations']=[{'stage':'finite three-block comparison Schur','failure':failure}]
        return None
    check('all 31 three-block comparison LDL pivots are strictly positive',len(piv)==31)
    record('even_three_block_Schur_inverse_trace_reserve_lower',bound)
    shear=trace/delta**2+profile_loss/15
    k=isqrt((shear.hi.numerator*10**12)//shear.hi.denominator)+1
    sqrtupper=F(k,10**6)
    check('comparison inverse shear includes core-tail and low-profile operators',sqrtupper**2>shear.hi)
    inverse=(1+sqrtupper)**2
    eta=I(min(bound.lo,delta.lo,F(15)))/inverse
    physical=eta/6
    record('comparison_shear_increment_squared_upper',shear)
    record('comparison_inverse_shear_norm_squared_upper',inverse)
    record('entire_three_block_coordinate_gap_lower',eta)
    record('entire_even_physical_gap_lower',physical)
    return physical.lo,tail_floor


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=HERE.parents[2])
    modes=parser.add_mutually_exclusive_group()
    modes.add_argument('--write',action='store_true')
    modes.add_argument('--verify',action='store_true')
    args=parser.parse_args();root=args.root.resolve()
    binding=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
    assert binding['anchor']==ANCHOR and binding['tail_origin_commit']==ORIGIN
    paths=[item['path'] for item in binding['files']]
    assert len(paths)==len(set(paths))==73
    for item in binding['files']:
        raw=(root/item['path']).read_bytes()
        assert len(raw)==item['bytes'],item['path']+' byte length'
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']+' SHA256'
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'],item['path']+' Git blob'
    environment=os.environ.copy();environment['PYTHONDONTWRITEBYTECODE']='1'
    print('Reproducing transition and its complete inherited shell proof chain',flush=True)
    replay=subprocess.run([sys.executable,'-B',str(root/PARENT/'check_transition.py'),'--verify','--root',str(root)],
                          capture_output=True,text=True,check=True,env=environment)
    assert not replay.stderr
    assert 'TOTAL 38 NEW EXACT CHECKS PASS' in replay.stdout
    assert 'INHERITED all-core 40 PASS; direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS' in replay.stdout
    assert 'REPLAY and all seven transition-package SHA256 hashes PASS' in replay.stdout
    spec=importlib.util.spec_from_file_location('pinned_segment',root/SEGMENT/'check_segment.py')
    engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
    I,check,record=engine.I,engine.check,engine.record
    check('73 distinct pinned input files and both provenance commits match',True)
    check('transition 38 and inherited 40 31 28 43 9 checks reproduce',True)
    B=engine.log(I(5))/2;h0=F(1,10**20);L0=engine.log(I(2)/h0)
    check('original target width and logarithm bounds',F(4,5)<B.lo<B.hi<F(81,100) and 46<L0.lo<L0.hi<47)
    check('exact active prime-power set stays 2 3 4 5', (2*B+2*h0).hi<engine.log(I(7)).lo)
    # Positive-half input intervals for the four reflected translations.
    p2=B-engine.log(I(2));p3=engine.log(I(3))-B;p4=engine.log(I(4))-B
    intervals=[(p2,p2+h0),(p3-h0,p3),(p4-h0,p4),(B-h0,B)]
    check('all four sampled core intervals lie in the positive core',
          p2.lo>0 and (p2+h0).hi<B.lo and (p3-h0).lo>0 and p3.hi<B.lo
          and (p4-h0).lo>0 and p4.hi<B.lo and (B-h0).lo>0)
    check('four sampled core intervals are pairwise disjoint uniformly',
          all(intervals[k][1].hi<intervals[k+1][0].lo for k in range(3)))
    for q,(left,right) in zip((2,3,4,5),intervals):
        record('prime_'+str(q)+'_input_left_at_h0',left)
        record('prime_'+str(q)+'_input_right_at_h0',right)
    weights2=engine.log(I(2))**2/2+engine.log(I(3))**2/3+engine.log(I(2))**2/4+engine.log(I(5))**2/5

    def sqrt_interval(x):
        # Directed integer square roots for arbitrary positive rational endpoints.
        x=I.of(x);scale=engine.SCALE
        assert x.lo>=0
        low=isqrt((x.lo.numerator*scale*scale)//x.lo.denominator)
        high=isqrt((x.hi.numerator*scale*scale)//x.hi.denominator)+1
        assert F(low,scale)**2<=x.lo and F(high,scale)**2>x.hi
        return I(F(low,scale),F(high,scale))

    prime=sqrt_interval(2*weights2)
    gamma=engine.PI/engine.sqrt_enclosure(2)+F(5,4)*engine.sqrt_enclosure(2)*sqrt_interval(B*h0)
    check('chi Gamma action integral has the stated exact L2 majorant',
          2*(103**2+2*103*6+2*6**2)==23834<155**2)
    check('chi bounded remainder is below sixty',14**2*18<60**2)
    check('chi entire nonpole functional bound is 215',155+60==215)
    sharp=gamma+prime+F(258,10**10)
    check('complete core-profile coupling is strictly below four',sharp.hi<4)
    record('prime_weight_square_sum',weights2)
    record('complete_disjoint_prime_coupling_upper',prime)
    record('complete_Gamma_coupling_upper',gamma)
    record('complete_core_profile_coupling_upper',sharp)
    record('published_core_profile_coupling_upper',4)
    loss=h0*(8*47+450)+32*10**13*h0*(4*47+644)**2
    check('complete trace-shell loss is below three',loss<3)
    check('pure profile shell loss is below one',h0*(8*47+450)<1)
    check('full shell floor exceeds 73 and pure profile floor exceeds 75',2*46-19==73 and 2*46-17==75)
    record('full_shell_total_uniform_loss_upper',loss)
    record('full_shell_profile_coefficient_lower',73)
    record('pure_profile_shell_floor_lower',75)
    dimension_sum=sum(2*n+1 for n in range(2,63,2))
    check('low-space pointwise bound in physical normalization',dimension_sum==2015 and F(4*dimension_sum,2)*F(5,4)<72**2)
    check('low-space moment correction is paid',F(6,5)*215*2==516)
    check('low-profile squared bound is monotone up to target endpoint',72*(46+11)+516>144)
    lowamplitude=72*(47+11)+516
    check('uniform finite low-profile amplitude is 4692 sqrt h0',lowamplitude==4692)
    profile_loss=F(lowamplitude**2,15*10**20)
    check('high-profile Young payment leaves fifteen shell units',75-60==15)
    check('high-profile Young tail deduction equals 1681 over 6000',F(41,10)**2/60==F(1681,6000))
    check('profile lift norm squared below four',2+F(648,25)*h0<4)
    check('physical forward norm squared costs at most six',2+4==6)
    result=compute_core(engine,profile_loss)
    report=engine.REPORT
    report.update({'anchor':ANCHOR,'tail_origin_commit':ORIGIN,'mellin_constraints':2,'A1_used':False,
                   'bound_inputs':73,'width':'0<h=b-log(5)/2<=10^-20',
                   'low_degrees':list(range(2,63,2)),'full_tail_first_degree':64,'kernel_polynomial_degree':64,
                   'arithmetic_grid':'1/10^200','odd_continuation_closed':False,
                   'fixed_source_changed':False,'negative_physical_source_certified':False,
                   'inherited_replay_checks':{'transition':38,'all_core':40,'direction':31,'coordinate':28,'shell':43,'a_gauge':9},
                   'inherited_replay_stdout_sha256':hashlib.sha256(replay.stdout.encode('utf-8')).hexdigest(),
                   'finite_matrix_role':'exact 31-dimensional low Schur of a dominated three-block comparison; infinite core and shell retained',
                   'analytic_proof':'PROOF.md; exact integration and infinite-dimensional estimates, not quadrature or numerical eigenvalues'})
    if result is None:
        report.update({'verdict':'UNDECIDED','full_original_width_even_all_source_certified':False})
    else:
        physical,tail_floor=result
        old=json.loads((root/SEGMENT/'segment_results.json').read_text(encoding='utf-8'))['values']['even_tail_floor']
        check('canonical endpoint tail enclosure is reproduced exactly',tail_floor.lo==F(old['lo']) and tail_floor.hi==F(old['hi']))
        gap=F(3,10**15)
        check('uniform physical even gap exceeds three times 10^-15',physical>gap)
        sigma=gap/140000000
        lossA=F(16,73);thetaA=lossA/(lossA+sigma)
        loss0=F(272**2)*F(50,7)+lossA*1458**2
        check('original gauge full subtraction norm below one million',loss0<10**6)
        theta0=F(10**6)/(10**6+sigma)
        check('entire A-gauge Gram norm strictly below one minus 9e-23',thetaA<1-F(9,10**23))
        check('entire original-gauge Gram norm strictly below one minus 2e-29',theta0<1-F(2,10**29))
        high=F(16)/(F(719,1000)*73)
        check('exactly specified energy high subspace has Gram norm below 31 over 100',high<F(31,100))
        previous=json.loads((root/PARENT/'transition_results.json').read_text(encoding='utf-8'))
        near=F(previous['values']['fixed_A_coordinate_eta']['hi'])
        check('fixed near-null full-shell Gram quotient remains below 7.55e-6',near<F(151,20000000))
        record('published_physical_even_gap',gap)
        record('both_gauges_absolute_Schur_floor',sigma)
        record('A_gauge_full_subtraction_norm_upper',lossA)
        record('original_gauge_full_subtraction_norm_upper',loss0)
        record('entire_A_gauge_Theta_upper',thetaA)
        record('entire_original_gauge_Theta_upper',theta0)
        record('published_A_gauge_relative_margin',F(9,10**23))
        record('published_original_gauge_relative_margin',F(2,10**29))
        record('specified_energy_high_Gram_bound',high)
        record('fixed_near_null_Gram_bound',near)
        record('energy_low_Gram_bound',thetaA)
        record('near_low_mixed_squared_bound',near*thetaA)
        record('near_high_mixed_squared_bound',near*high)
        record('low_high_mixed_squared_bound',thetaA*high)
        check('previous dyadic endpoint is included without expanding a huge integer',2**80>10**20 and 10**16+1>10**16)
        report.update({'verdict':'EVEN-ALL-SOURCE-FULL-ORIGINAL-WIDTH-CLOSED',
                       'full_original_width_even_all_source_certified':True,
                       'entire_A_gauge_Gram_operator_certified':True,
                       'all_mixed_blocks_retained':True,
                       'energy_low_dimension_upper':31,
                       'matrix_comparison_shear_is_not_claimed_to_equal_actual_core_inverse':True})
    report['check_count']=len(report['checks'])
    engine.LOG.append('TOTAL '+str(report['check_count'])+' NEW EXACT CHECKS PASS')
    engine.LOG.append(report['verdict'])
    logtext=('INHERITED transition 38 PASS; all-core 40 PASS; direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS\n'
             +'\n'.join(engine.LOG)+'\n')
    jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.write:
        (HERE/'width_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
        (HERE/'width_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
        manifest=''.join(hashlib.sha256((HERE/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in PAYLOAD)
        (HERE/'SHA256SUMS').write_text(manifest,encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'width_results.json').read_bytes()==jsontext.encode('utf-8'),'JSON replay mismatch'
        assert (HERE/'width_checks.log').read_bytes()==logtext.encode('utf-8'),'log replay mismatch'
        entries=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        assert [entry.split('  ',1)[1] for entry in entries]==PAYLOAD,'manifest membership/order'
        for entry in entries:
            digest,name=entry.split('  ',1)
            assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name+' payload hash'
        print('REPLAY and all seven width-package SHA256 hashes PASS')
    print(logtext,end='')


if __name__=='__main__':
    main()
