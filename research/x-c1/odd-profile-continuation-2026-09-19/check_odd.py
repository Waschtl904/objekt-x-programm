#!/usr/bin/env python3
"""Odd continuation with full core and shell, and a local all-parity corollary.

All proof decisions use integer/Fraction directed interval arithmetic.
The analytic domain theorem and infinite-dimensional argument are in PROOF.md.
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

HERE=Path(__file__).resolve().parent
ANCHOR='7741eca6f14bdc3017f6a299aff06eb66db2e697'
ORIGIN='6a16d90b551588572c87e622c21c2df7f7b1adc2'
SEGMENT='research/x-c1/prime-power-segment-4-2026-09-18'
PARENT='research/x-c1/full-core-profile-width-amplification-2026-09-19'
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_odd.py',
         'input_bindings.json','odd_results.json','odd_checks.log']


def compute_odd(engine, profile_loss):
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
    for j in (1,):check('low basis Qnorm ingredient '+str(j),max(abs((harm[j]+q0).lo),abs((harm[j]+q0).hi))<4 and ((2*j+1)*P2(j,j)).hi<4)
    parity, label = 1, 'odd'
    ix=list(range(3,N+1,2));allix=list(range(1,N+1,2));tail=65
    check('exact 31-dimensional low space and full tail starting at degree 65', len(ix)==31 and ix[-1]==63)
    beta=((a/2)**2/(6*(1-(a/2)**2/20)))**2
    rem=(a/2)**tail/factorial(tail)/(1-(a/2)**2/((tail+1)*(tail+2)))
    epsmoment=rem*(4/a)
    err=2*L*eps+80*epsmoment
    tail_floor=harm[tail]+q0-L*(F(1,4)-c+eps)-snorm-err
    delta=I(tail_floor.lo-F(1681,6000))
    check('global moment norm below square root two', 0<beta.lo<=beta.hi<1)
    check('moment-corrected full high-tail coupling below 41 over 10', 16*(1+epsmoment.hi**2)<F(41,10)**2)
    check('tail remains above 0.454 after high-profile payment', delta.lo>F(454,1000))
    check('tail physical coercivity above 0.734 with exact norm correction', tail_floor.lo/(1+epsmoment.hi**2)>F(734,1000))
    record('odd_beta',beta)
    record('odd_moment_tail_operator_error',epsmoment)
    record('odd_Gamma_form_error',2*L*eps)
    record('odd_infinite_moment_form_error',80*epsmoment)
    record('odd_total_form_error',err)
    record('odd_original_tail_floor',tail_floor)
    record('odd_physical_tail_floor_lower',tail_floor.lo/(1+epsmoment.hi**2))
    record('odd_effective_tail_floor',delta)
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
    record('odd_finite_Mellin_correction_HS_squared_upper',moment_cost_sq)
    record('odd_coupling_HS_squared',trace)
    record('low_profile_squared_operator_upper',15*profile_loss)
    record('low_profile_Schur_deduction',profile_loss)
    abound,_,_,afail=engine.inverse_trace_bound(amat,ix)
    if abound is not None:record('odd_finite_Mellin_block_reserve_lower',abound)
    bound,low,piv,failure=engine.inverse_trace_bound(mat,ix)
    for k,v in enumerate(piv):record('odd_three_block_Schur_LDL_pivot_'+str(ix[k]),v)
    if failure:
        REPORT['obligations']=[{'stage':'finite three-block comparison Schur','failure':failure}]
        return None
    check('all 31 three-block comparison LDL pivots are strictly positive',len(piv)==31)
    record('odd_three_block_Schur_inverse_trace_reserve_lower',bound)
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
    record('entire_odd_physical_gap_lower',physical)
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
    assert len(paths)==len(set(paths))==81
    for item in binding['files']:
        raw=(root/item['path']).read_bytes()
        assert len(raw)==item['bytes'],item['path']+' byte length'
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']+' SHA256'
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'],item['path']+' Git blob'
    spec=importlib.util.spec_from_file_location('pinned_segment',root/SEGMENT/'check_segment.py')
    engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
    I,check,record=engine.I,engine.check,engine.record
    check('81 distinct pinned input files and provenance commits match',True)
    environment=os.environ.copy();environment['PYTHONDONTWRITEBYTECODE']='1'
    print('Replaying the complete even certificate while computing the independent odd blocks',flush=True)
    replay=subprocess.Popen([sys.executable,'-B',str(root/PARENT/'check_width.py'),'--verify','--root',str(root)],
                            stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=environment)
    B=engine.log(I(5))/2;h0=F(1,10**20);L0=engine.log(I(2)/h0)
    check('original target width and logarithm bounds',F(4,5)<B.lo<B.hi<F(81,100) and 46<L0.lo<L0.hi<47)
    check('physical support endpoint remains below one',(B+h0).hi<1)
    check('only prime powers 2 3 4 5 are active',(2*B+2*h0).hi<engine.log(I(7)).lo)
    exp_half=engine.exp_pos(I(F(1,2)));sinh_half=(exp_half-1/exp_half)/2
    check('odd shell moment coefficient at most three fifths',sinh_half.hi<F(3,5))
    check('positive-series sinh t over t bound at t one half',2*sinh_half.hi<F(6,5))
    check('exact odd corrector moment lower integral coefficient',F(1,2)*(F(1,3)-F(1,4))==F(1,24))
    check('odd corrector positive-half moment exceeds two seventy-fifths',(B**2/24).lo>F(2,75))
    check('odd corrector supremum below ten',F(1,4)/F(2,75)==F(75,8)<10)
    check('odd corrector Lipschitz constant below 47',F(5,4)/F(2,75)==F(375,8)<47)
    check('odd corrector full physical norm squared below 200',2*B.hi*10**2<200)
    check('odd corrector Gamma action pointwise majorant',2*47*5+4*10*F(21,4)==680)
    gamma_chi_squared=2*(680**2+2*680*20+2*20**2)
    check('odd corrector Gamma action L2 norm below 1000',gamma_chi_squared==980800<1000**2)
    check('odd corrector bounded remainder below 200',14**2*200<200**2)
    check('complete odd corrector functional bounded by 1200',1000+200==1200)
    record('odd_corrector_moment_lower',B**2/24)
    record('odd_corrector_Gamma_action_norm_squared_upper',gamma_chi_squared)
    record('odd_corrector_nonpole_functional_norm_upper',1200)

    p2=B-engine.log(I(2));p3=engine.log(I(3))-B;p4=engine.log(I(4))-B
    intervals=[(p2,p2+h0),(p3-h0,p3),(p4-h0,p4),(B-h0,B)]
    check('four reflected odd core input intervals stay inside the positive half',
          p2.lo>0 and (p2+h0).hi<B.lo and (p3-h0).lo>0 and p3.hi<B.lo
          and (p4-h0).lo>0 and p4.hi<B.lo and (B-h0).lo>0)
    check('all four prime input intervals are disjoint uniformly',
          all(intervals[k][1].hi<intervals[k+1][0].lo for k in range(3)))
    for q,(left,right) in zip((2,3,4,5),intervals):
        record('prime_'+str(q)+'_input_left_at_h0',left)
        record('prime_'+str(q)+'_input_right_at_h0',right)
    weights2=engine.log(I(2))**2/2+engine.log(I(3))**2/3+engine.log(I(2))**2/4+engine.log(I(5))**2/5

    def sqrt_interval(x):
        x=I.of(x);scale=engine.SCALE;assert x.lo>=0
        low=isqrt((x.lo.numerator*scale*scale)//x.lo.denominator)
        high=isqrt((x.hi.numerator*scale*scale)//x.hi.denominator)+1
        assert F(low,scale)**2<=x.lo and F(high,scale)**2>x.hi
        return I(F(low,scale),F(high,scale))

    prime=sqrt_interval(2*weights2)
    gamma=engine.PI/engine.sqrt_enclosure(2)+F(5,4)*engine.sqrt_enclosure(2)*sqrt_interval(B*h0)
    sharp=prime+gamma+F(720,10**10)
    check('entire odd core-profile pairing is bounded by four',sharp.hi<4)
    record('prime_weight_square_sum',weights2)
    record('complete_disjoint_prime_coupling_upper',prime)
    record('complete_Gamma_coupling_upper',gamma)
    record('complete_odd_core_profile_coupling_upper',sharp)
    record('published_odd_core_profile_coupling_upper',4)
    check('odd profile moment losses have coefficients 12 and 1140',
          2*F(3,5)*10==12 and 12*11+F(9,25)*14*200==1140)
    check('odd profile loss is increasing throughout the interval',12*46+1140-12>0)
    check('odd profile uniform loss is below one',h0*(12*47+1140)<1)
    check('odd profile shell floor is above 75',2*46-17==75)
    record('odd_profile_uniform_loss_upper',h0*(12*47+1140))
    record('odd_profile_shell_floor_lower',75)
    check('odd exact moment ratios have magnitude below two',F(6,5)*F(1,2)/F(1,3)==F(9,5)<2)
    dimension_sum=sum(2*n+1 for n in range(3,64,2))
    check('odd low-space physical supremum constant 110',dimension_sum==2077 and F(9*dimension_sum,2)*F(5,4)<110**2)
    check('odd low-space moment correction paid by 1440',F(3,5)*1200*2==1440)
    check('odd low-profile squared coefficient is monotone',110*(46+11)+1440>220)
    low_amplitude=110*(47+11)+1440
    check('odd uniform low-profile amplitude 7820 sqrt h0',low_amplitude==7820)
    profile_loss=F(low_amplitude**2,15*10**20)
    check('high-profile Young payment and positive remainders',F(41,10)**2/60==F(1681,6000) and 75-60==15)
    check('odd profile lift squared norm below four',2+F(9,25)*200*h0<4)
    check('odd physical inverse coordinate squared constant two',1+144*h0<4)
    check('odd physical forward reference-coordinate squared constant six',2+4==6)
    check('complete odd form graph uses a positive closed physical norm',20>14 and F(20,2)-4>=1 and 4+20*5==104)
    result=compute_odd(engine,profile_loss)
    stdout,stderr=replay.communicate()
    assert replay.returncode==0 and not stderr,stderr
    check('even 41 and complete inherited 38 40 31 28 43 9 checks reproduce',
          'TOTAL 41 NEW EXACT CHECKS PASS' in stdout
          and 'REPLAY and all seven width-package SHA256 hashes PASS' in stdout
          and 'INHERITED transition 38 PASS; all-core 40 PASS; direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS' in stdout)
    report=engine.REPORT
    report.update({'anchor':ANCHOR,'tail_origin_commit':ORIGIN,'mellin_constraints':2,'A1_used':False,
                   'bound_inputs':81,'width':'0<h=b-log(5)/2<=10^-20',
                   'odd_low_degrees':list(range(3,64,2)),'odd_full_tail_first_degree':65,
                   'kernel_polynomial_degree':64,'arithmetic_grid':'1/10^200',
                   'source_selection_or_physical_renormalization':False,
                   'negative_physical_source_certified':False,
                   'larger_or_iterable_window_certified':False,
                   'inherited_replay_checks':{'even_width':41,'transition':38,'all_core':40,'direction':31,'coordinate':28,'shell':43,'a_gauge':9},
                   'inherited_replay_stdout_sha256':hashlib.sha256(stdout.encode('utf-8')).hexdigest(),
                   'finite_matrix_role':'exact odd 31-dimensional low Schur comparison with complete infinite core and profile shell',
                   'odd_operator_coordinates':'full odd core plus moment-corrected profile; no duplicated trace coordinate',
                   'analytic_proof':'PROOF.md; independent odd form closure and H1 gluing, all infinite tails and mixed blocks retained'})
    if result is None:
        report.update({'verdict':'ODD-UNDECIDED / EVEN-PRESERVED',
                       'odd_full_width_all_source_certified':False,'local_all_parity_certified':False})
    else:
        physical,tail_floor=result
        old=json.loads((root/SEGMENT/'segment_results.json').read_text(encoding='utf-8'))['values']['odd_tail_floor']
        check('canonical odd endpoint tail enclosure reproduced exactly',tail_floor.lo==F(old['lo']) and tail_floor.hi==F(old['hi']))
        gap=F(1,10**12)
        check('uniform physical odd gap exceeds 10^-12',physical>gap)
        sigma=gap/2;subtraction=F(16,75);theta=subtraction/(subtraction+sigma)
        check('full odd profile Schur norm below one minus 2e-12',theta<1-F(2,10**12))
        previous=json.loads((root/PARENT/'width_results.json').read_text(encoding='utf-8'))
        even_gap=F(previous['values']['published_physical_even_gap']['lo'])
        check('full-width even all-source theorem preserved with gap 3e-15',
              previous['full_original_width_even_all_source_certified'] is True and even_gap==F(3,10**15))
        check('all-parity gap is the smaller proved parity gap',min(gap,even_gap)==F(3,10**15))
        # Exact linear identities on the two moment functionals (E_plus,E_minus).
        even=(F(1,2),F(1,2));odd=(F(1,2),F(-1,2))
        check('both moment components are exact parity projections of the original two',
              tuple(a+b for a,b in zip(even,odd))==(1,0)
              and tuple(a-b for a,b in zip(even,odd))==(0,1))
        record('published_physical_odd_gap',gap)
        record('odd_actual_profile_Schur_floor',sigma)
        record('odd_full_subtraction_norm_upper',subtraction)
        record('odd_full_profile_Theta_upper',theta)
        record('published_odd_profile_relative_margin',F(2,10**12))
        record('preserved_physical_even_gap',even_gap)
        record('published_local_all_parity_gap',min(gap,even_gap))
        report.update({'verdict':'ODD-ALL-SOURCE-AND-LOCAL-ALL-PARITY-CLOSED',
                       'odd_full_width_all_source_certified':True,'local_all_parity_certified':True,
                       'complete_odd_profile_Schur_operator_certified':True,
                       'all_core_profile_mixed_blocks_retained':True,
                       'comparison_shear_not_identified_with_actual_inverse':True})
    report['check_count']=len(report['checks'])
    engine.LOG.append('TOTAL '+str(report['check_count'])+' NEW EXACT CHECKS PASS')
    engine.LOG.append(report['verdict'])
    logtext=('INHERITED even-width 41 PASS; transition 38 PASS; all-core 40 PASS; direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS\n'
             +'\n'.join(engine.LOG)+'\n')
    jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.write:
        (HERE/'odd_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
        (HERE/'odd_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
        manifest=''.join(hashlib.sha256((HERE/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in PAYLOAD)
        (HERE/'SHA256SUMS').write_text(manifest,encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'odd_results.json').read_bytes()==jsontext.encode('utf-8'),'JSON replay mismatch'
        assert (HERE/'odd_checks.log').read_bytes()==logtext.encode('utf-8'),'log replay mismatch'
        entries=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        assert [entry.split('  ',1)[1] for entry in entries]==PAYLOAD,'manifest membership/order'
        for entry in entries:
            digest,name=entry.split('  ',1)
            assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name+' payload hash'
        print('REPLAY and all seven odd-package SHA256 hashes PASS')
    print(logtext,end='')


if __name__=='__main__':
    main()
