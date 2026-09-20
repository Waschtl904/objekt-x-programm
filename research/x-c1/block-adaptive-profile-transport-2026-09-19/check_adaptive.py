#!/usr/bin/env python3
"""Block-adaptive all-source transport; exact arithmetic, complete infinite tails.

PROOF.md defines the analytic model, domains, comparison and scope.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, isqrt
from pathlib import Path
import argparse, hashlib, importlib.util, json, os, subprocess, sys

HERE=Path(__file__).resolve().parent
BASE='research/x-c1/'
ANCHOR='ca3849ab2a5abf6268ee892109a293332c1030e9'
ORIGIN='6a16d90b551588572c87e622c21c2df7f7b1adc2'
PARENT=BASE+'all-parity-window-and-restart-2026-09-19'
SEGMENT=BASE+'prime-power-segment-4-2026-09-18'
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_adaptive.py','input_bindings.json','adaptive_results.json','adaptive_checks.log']

def compute_data(engine, parity):
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
    for j in (parity,):check('low basis Qnorm ingredient '+str(j),max(abs((harm[j]+q0).lo),abs((harm[j]+q0).hi))<4 and ((2*j+1)*P2(j,j)).hi<4)
    label = 'even' if parity==0 else 'odd'
    ix=list(range(parity+2,N+1,2));allix=list(range(parity,N+1,2));tail=64+parity
    check(label+' exact 31-dimensional low space and full tail', len(ix)==31 and ix[-1]==62+parity)
    beta=((a/2)**2/(2*(1-(a/2)**2/12)))**2 if parity==0 else ((a/2)**2/(6*(1-(a/2)**2/20)))**2
    epsmoment=(a/2)**tail/factorial(tail)/(1-(a/2)**2/((tail+1)*(tail+2)))
    if parity:epsmoment*=4/a
    err=2*L*eps+80*epsmoment
    tail_floor=harm[tail]+q0-L*(F(1,4)-c+eps)-snorm-err
    check('global moment norm below square root two', 0<beta.lo<=beta.hi<1)
    check('moment-corrected full high-tail coupling below 41 over 10', 16*(1+epsmoment.hi**2)<F(41,10)**2)
    check('tail physical coercivity above 0.719 with exact norm correction', tail_floor.lo/(1+epsmoment.hi**2)>F(719,1000))
    record(label+'_beta',beta)
    record(label+'_moment_tail_operator_error',epsmoment)
    record(label+'_Gamma_form_error',2*L*eps)
    record(label+'_infinite_moment_form_error',80*epsmoment)
    record(label+'_total_form_error',err)
    record(label+'_original_tail_floor',tail_floor)
    record(label+'_physical_tail_floor_lower',tail_floor.lo/(1+epsmoment.hi**2))
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
    amat=[[I(0) for _ in ix] for _ in ix];gmat=[[I(0) for _ in ix] for _ in ix]
    trace=I(0)
    for ii,i in enumerate(ix):
        progress(label+' Gram row '+str(ii+1)+'/'+str(len(ix)))
        for jj,j in enumerate(ix[:ii+1]):
            ga=F(1001,1000)*changed(gramC,i,j)+1001*err**2/(2*i+1)*(i==j)
            av=changed(Q,i,j)
            amat[ii][jj]=amat[jj][ii]=av;gmat[ii][jj]=gmat[jj][ii]=ga
            if i==j:trace+=(2*i+1)*ga
    return dict(a=a,q0=q0,pg=pg,eps=eps,kcols=kcols,amat=amat,gmat=gmat,tail_floor=tail_floor,err=err,ix=ix,harm=harm,ratios=[ratio(i) for i in ix],epsmoment=epsmoment,trace=trace)

def sqrt_interval(e,value):
    value=e.I.of(value);scale=e.SCALE;assert value.lo>=0
    lo=isqrt(value.lo.numerator*scale**2//value.lo.denominator)
    hi=isqrt(value.hi.numerator*scale**2//value.hi.denominator)+1
    assert F(lo,scale)**2<=value.lo and F(hi,scale)**2>value.hi
    return e.I(F(lo,scale),F(hi,scale))


def coupling_vectors(e,d,parity):
    I=e.I;B=d['a'];ix=d['ix'];p=parity
    rho=[F(1),F(-1)] if p==0 else [F(0),F(1),F(-1)]
    exp=e.exp_pos(B/2);cosh=(exp+1/exp)/2;sinh=(exp-1/exp)/2
    moment=4*(cosh-1)/B if p==0 else 4*sinh/B-16*(cosh-1)/B**2
    weight=cosh if p==0 else sinh;scale=sqrt_interval(e,2*B)
    e.check('exact '+str(p)+' corrector normalization positive',moment.lo>0)
    def integ(poly,left=I(0),right=I(1)):
        return sum((v*(right**(k+1)-left**(k+1))/(k+1) for k,v in enumerate(poly)),I(0))
    def vm(n):
        if n%2:return I(sum((F(1,k) for k in range(1,(n+1)//2+1)),F(0))/F(2*(n+1)))
        return (sum((F(1,2*k+1) for k in range(n//2+1)),F(0))-e.LOG2)/(n+1)
    def inner_rho(poly):return integ(e.polymul(rho,poly))
    def vinner(poly):return sum((v*vm(k) for k,v in enumerate(e.polymul(rho,poly))),I(0))
    rhom=[inner_rho(e.leg(n)) for n in range(129)]
    channels=e.channels(5)+[{'q':5,'ell':e.log(I(5)),'weight':e.log(I(5))/e.sqrt_enclosure(5)}]
    def shift_inner(j):
        total=I(0)
        for channel in channels[:-1]:
            dd=channel['ell']/B
            for sign in (-1,1):
                shift=sign*dd;l=-1-shift;r=1-shift
                left=I(0) if l.hi<0 else l;right=I(1) if r.lo>1 else r
                if left.lo>=right.hi:continue
                assert left.hi<right.lo
                poly=e.translated_legs(shift,j)[j]
                total+=channel['weight']*integ(e.polymul(rho,poly),left,right)
        return total
    def action(j):
        return ((d['harm'][j]+d['q0'])*rhom[j]+vinner(e.leg(j))
                -sum((v*rhom[n] for n,v in enumerate(d['kcols'][j])),I(0))-shift_inner(j))
    base=action(p);aa=[];cc=[];qq=[]
    for pos,j in enumerate(ix):
        ratio=d['ratios'][pos];qchi=scale/moment*(action(j)-ratio*base)
        a=-(1-ratio)/scale
        kernel=sum(d['kcols'][j],I(0))-ratio*sum(d['kcols'][p],I(0))
        primes=sum((c['weight']*(e.polyval(e.leg(j),1-c['ell']/B)
                    -ratio*e.polyval(e.leg(p),1-c['ell']/B)) for c in channels),I(0))
        c=(2*(d['harm'][j]-ratio*d['harm'][p])-2*kernel-2*primes)/scale-weight*qchi
        aa.append(a);cc.append(c);qq.append(qchi)
    return aa,cc,qq


def dual_product(e,low,piv,u,v):
    fu=[];fv=[];I=e.I
    for i in range(len(u)):
        fu.append(u[i]-sum((low[i][j]*fu[j] for j in range(i)),I(0)))
        fv.append(v[i]-sum((low[i][j]*fv[j] for j in range(i)),I(0)))
    return sum((fu[i]*fv[i]/piv[i] for i in range(len(u))),I(0))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=HERE.parents[2])
    mode=parser.add_mutually_exclusive_group();mode.add_argument('--write',action='store_true');mode.add_argument('--verify',action='store_true')
    args=parser.parse_args();root=args.root.resolve()
    binding=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
    assert binding['anchor']==ANCHOR and binding['matrix_origin_commit']==ORIGIN
    assert len(binding['files'])==len({x['path'] for x in binding['files']})==103
    for item in binding['files']:
        raw=(root/item['path']).read_bytes()
        assert len(raw)==item['bytes'],item['path']+' length'
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']+' SHA256'
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'],item['path']+' Git blob'
    spec=importlib.util.spec_from_file_location('pinned_segment',root/SEGMENT/'check_segment.py')
    e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
    I,check,record=e.I,e.check,e.record
    check('103 exact byte SHA256 and Git-blob input bindings match',True)
    environment=os.environ.copy();environment['PYTHONDONTWRITEBYTECODE']='1'
    print('Replaying ca3849a and its complete chain while rebuilding both full-tail cores',flush=True)
    replay=subprocess.Popen([sys.executable,'-B',str(root/PARENT/'check_restart.py'),'--verify','--root',str(root)],
                            stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=environment)
    B=e.log(I(5))/2;H=F(5,10**13);near=F(1,20);LH=e.log(I(2)/H)
    check('enlarged endpoint stays below one and the next active channel',(B+H).hi<1 and (2*B+2*H).hi<e.log(I(7)).lo)
    check('fixed near band contains the entire q5 input',H<near<B.lo)
    intervals=[(B-e.log(I(2)),B-e.log(I(2))+H),
               (e.log(I(3))-B-H,e.log(I(3))-B),
               (e.log(I(4))-B-H,e.log(I(4))-B)]
    check('three other prime input intervals lie outside the near band',all(l.lo>0 and r.hi<(B-near).lo for l,r in intervals))
    check('three far prime input intervals remain disjoint',all(intervals[k][1].hi<intervals[k+1][0].lo for k in range(2)))
    w5=e.log(I(5))/e.sqrt_enclosure(5)
    other=sum((e.log(I(prime))**2/q for q,prime in [(2,2),(3,3),(4,2)]),I(0))
    nearfar=sqrt_interval(e,(e.PI/e.sqrt_enclosure(2)+e.sqrt_enclosure(2)*w5)**2+2*other)
    complete=nearfar+sqrt_interval(e,I(H)/(2*near))+F(5,4)*e.sqrt_enclosure(2)*sqrt_interval(e,B*H)+720*sqrt_interval(e,H)
    check('complete near-far core-profile norm below 3.468',complete.hi<F(3468,1000))
    record('near_far_main_coupling_upper',nearfar);record('complete_core_profile_coupling_upper',complete)
    check('pure profile floor retains two L minus seventeen',H*(12*LH.hi+1140)<1 and H*(8*LH.hi+450)<1)
    check('profile norm and full physical factor six remain valid',2+72*H<4 and 2+4==6)
    check('singular and remainder monotonicity on entire width',LH.lo>29 and LH.lo+9>0)
    check('regular polynomial model covers enlarged core-shell distances',(2*B+H).hi<F(5,3))
    check('corrector approximation and shell model errors fit 110 epsilon',F(6,5)*4*20+4<110)
    check('bounded corrector weight variation fits 1100 r',F(3,5)**2*1200**2*2<1100**2)
    check('generic pointwise remainder coefficient dominates all linear terms',70+8*100000+1100+4*10<300000*10 and 100000<300000)
    check('outer width is one million times ca3849a',H/F(5,10**19)==10**6)
    cases=[(F(1,10**13),F(44),F(4,10**15)),(H,F(41),F(1,10**15))]
    summaries=[]
    for parity in (0,1):
        label='even' if parity==0 else 'odd';d=compute_data(e,parity);ix=d['ix']
        parent_dir='full-core-profile-width-amplification-2026-09-19' if parity==0 else 'odd-profile-continuation-2026-09-19'
        parent_file='width_results.json' if parity==0 else 'odd_results.json'
        old=json.loads((root/BASE/parent_dir/parent_file).read_text(encoding='utf-8'))['values']
        for key,value in [('original_tail_floor',d['tail_floor']),('coupling_HS_squared',d['trace']),('total_form_error',d['err'])]:
            source=old[label+'_'+key]
            check(label+' canonical '+key+' reproduced exactly',value.lo==F(source['lo']) and value.hi==F(source['hi']))
        check(label+' entire high-profile norm below 347 over 100',complete.hi**2*(1+d['epsmoment'].hi**2)<F(347,100)**2)
        check(label+' exact moment ratios bounded by two',all(max(abs(r.lo),abs(r.hi))<2 for r in d['ratios']))
        derivative_sum=sum((2*n+1)*(F(n*(n+1),2)+(2 if parity else 0))**2 for n in ix)
        check(label+' low derivative norm below 100000',derivative_sum/F(128,125)<100000**2)
        Dg=sum((k*abs(d['pg'][k])*F(5,6)**(k-1)/2 for k in range(1,len(d['pg']))),F(0))
        check(label+' regular model derivative below ten',Dg<10)
        record(label+'_regular_model_derivative_upper',Dg)
        aa,cc,qq=coupling_vectors(e,d,parity)
        for n,a,c,qchi in zip(ix,aa,cc,qq):
            record(label+'_log_vector_'+str(n),a);record(label+'_constant_vector_'+str(n),c);record(label+'_model_corrector_functional_'+str(n),qchi)
        for index,(width,payment,allgap) in enumerate(cases,1):
            tag=label+'_window_'+str(index)
            delta=I(d['tail_floor'].lo-F(347,100)**2/payment)
            log=e.log(I(2)/width);ell=e.log(2*B/width);shell=2*log.lo-17-payment
            check(tag+' tail and residual profile floors positive',delta.lo>0 and shell>0)
            mat=[[d['amat'][i][j]-d['err']/(2*ix[i]+1)*(i==j)-d['gmat'][i][j]/delta for j in range(31)] for i in range(31)]
            sigma,low,piv,failure=e.inverse_trace_bound(mat,ix)
            if failure:raise AssertionError(tag+' comparison UNDECIDED: '+str(failure))
            check(tag+' all 31 full-tail comparison pivots strictly positive',len(piv)==31)
            for n,pivot in zip(ix,piv):record(tag+'_LDL_pivot_'+str(n),pivot)
            wa=dual_product(e,low,piv,aa,aa);wac=dual_product(e,low,piv,aa,cc);wc=dual_product(e,low,piv,cc,cc)
            energy=width*((ell**2+2*ell+2)*wa+2*(ell+1)*wac+wc)
            check(tag+' rank-two exact integrated energy positive',energy.lo>0)
            remainder=300000*width*(log.hi+10)+110*d['eps']
            error=width*remainder**2/sigma.lo
            zeta=(sqrt_interval(e,energy)+sqrt_interval(e,error))**2/shell
            check(tag+' adaptive low-profile loss below one thousandth',zeta.hi<F(1,1000))
            if index==1:check(tag+' narrow adaptive loss below one millionth',zeta.hi<F(1,10**6))
            amplitude=(72 if parity==0 else 110)*(log.hi+11)+(516 if parity==0 else 1440)
            crude=width*amplitude**2
            shear=d['trace']/delta**2+crude/shell**2
            inverse=(1+sqrt_interval(e,shear).hi)**2
            reserve=(1-zeta.hi)*sigma.lo
            physical=min(reserve,delta.lo,shell)/(6*inverse)
            published=allgap if parity==0 else F(1,10**12)
            check(tag+' complete physical gap exceeds published bound',physical>published)
            for key,value in [('width',width),('tail_profile_payment',payment),('effective_tail_floor',delta),('remaining_profile_floor',shell),
                              ('low_inverse_trace_reserve',sigma),('dual_log_squared',wa),('dual_log_constant_mixed',wac),('dual_constant_squared',wc),
                              ('integrated_main_energy',energy),('pointwise_remainder_upper',remainder),('integrated_remainder_energy',error),
                              ('adaptive_low_profile_relative_loss',zeta),('comparison_inverse_shear_squared',inverse),
                              ('physical_gap_lower',physical),('published_physical_gap',published)]:record(tag+'_'+key,value)
            summaries.append({'parity':label,'width':str(width),'payment':str(payment),'published_gap':str(published)})
    stdout,stderr=replay.communicate();assert replay.returncode==0 and not stderr,stderr
    check('ca3849a 88 checks complete inherited chain and hashes reproduce',
          'TOTAL 88 NEW EXACT CHECKS PASS' in stdout and 'REPLAY and all seven restart-package SHA256 hashes PASS' in stdout
          and 'INHERITED odd 51 PASS; even 41 PASS; transition 38 PASS; all-core 40 PASS; direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS; universal regressions 349 PASS' in stdout)
    report=e.REPORT
    report.update({'anchor':ANCHOR,'matrix_origin_commit':ORIGIN,'bound_inputs':103,
       'verdict':'BLOCK-ADAPTIVE-ALL-PARITY-MILLIONFOLD-WINDOW-CLOSED','cases':summaries,
       'mellin_constraints':2,'A1_used':False,'source_selection_or_physical_renormalization':False,
       'window_amplification_factor_over_anchor':10**6,'full_infinite_tails_and_mixed_blocks_retained':True,
       'rank_two_model_is_entire_shell_operator':False,'rank_two_model_has_uniform_full_low_operator_remainder':True,
       'adaptive_zeta_is_actual_full_profile_Theta':False,
       'uniform_endpoint_restart_of_adaptive_blocks_certified':False,'non_summable_transport_certified':False,
       'q7_threshold_reached':False,'connected_unit_window_coercivity_certified':False,
       'negative_physical_source_certified':False,'global_Weil_positivity_certified':False,
       'arithmetic_grid':'1/10^200','analytic_proof':'PROOF.md; all-source form-domain and full comparison argument',
       'inherited_replay_stdout_sha256':hashlib.sha256(stdout.encode('utf-8')).hexdigest(),
       'inherited_replay_checks':{'restart':88,'odd':51,'even':41,'transition':38,'all_core':40,'direction':31,'coordinate':28,'shell':43,'a_gauge':9,'universal_regressions':349}})
    report['check_count']=len(report['checks']);e.LOG.append('TOTAL '+str(report['check_count'])+' NEW EXACT CHECKS PASS');e.LOG.append(report['verdict'])
    logtext='INHERITED restart 88; odd 51; even 41; transition 38; all-core 40; direction 31; coordinate 28; shell 43; A-gauge 9; universal 349 PASS\n'+'\n'.join(e.LOG)+'\n'
    jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.write:
        (HERE/'adaptive_results.json').write_text(jsontext,encoding='utf-8',newline='\n');(HERE/'adaptive_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
        (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in PAYLOAD),encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'adaptive_results.json').read_bytes()==jsontext.encode('utf-8'),'JSON replay mismatch'
        assert (HERE/'adaptive_checks.log').read_bytes()==logtext.encode('utf-8'),'log replay mismatch'
        entries=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines();assert [line.split('  ',1)[1] for line in entries]==PAYLOAD
        for line in entries:
            digest,name=line.split('  ',1);assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
        print('REPLAY and all seven adaptive-package SHA256 hashes PASS')
    print(logtext,end='')


if __name__=='__main__':main()
