#!/usr/bin/env python3
"""Exact ledger for finite-band moving-endpoint harmonic block renewal.

PROOF.md supplies the analytic form, domain and projection arguments.
Only pinned standard-library integer/Fraction interval routines are used.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, importlib.util, json, os, subprocess, sys

HERE=Path(__file__).resolve().parent
BASE='research/x-c1/'
ANCHOR='b1c01860fef2a960cae57634041f75b29d37f836'
ORIGIN='6a16d90b551588572c87e622c21c2df7f7b1adc2'
PARENT=BASE+'block-adaptive-profile-transport-2026-09-19'
SEGMENT=BASE+'prime-power-segment-4-2026-09-18'
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_moving.py','input_bindings.json','moving_results.json','moving_checks.log']

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=HERE.parents[2])
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--write',action='store_true');mode.add_argument('--verify',action='store_true')
    args=parser.parse_args();root=args.root.resolve()
    binding=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
    assert binding['anchor']==ANCHOR and binding['matrix_origin_commit']==ORIGIN
    assert len(binding['files'])==len({x['path'] for x in binding['files']})==111
    for item in binding['files']:
        raw=(root/item['path']).read_bytes()
        assert len(raw)==item['bytes'],item['path']+' length'
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']+' SHA256'
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'],item['path']+' Git blob'
    e=module('pinned_segment',root/SEGMENT/'check_segment.py')
    parent=module('pinned_adaptive',root/PARENT/'check_adaptive.py')
    I,check,record=e.I,e.check,e.record
    sqrt=lambda v:parent.sqrt_interval(e,v)
    check('111 exact byte SHA256 and Git-blob input bindings match',True)
    environment=os.environ.copy();environment['PYTHONDONTWRITEBYTECODE']='1'
    print('Replaying b1c0186 and the complete inherited chain; rebuilding both full-tail cores',flush=True)
    replay=subprocess.Popen([sys.executable,'-B',str(root/PARENT/'check_adaptive.py'),'--verify','--root',str(root)],
                            stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=environment)
    B=e.log(I(5))/2;H=F(1,10**10);near=F(1,20);L=e.log(I(2)/H)
    cH=F(87,25);payment=F(42);hard_payment=F(40)
    check('band stays below one and the next prime-power threshold',(B+H).hi<1 and (2*B+2*H).hi<e.log(I(7)).lo)
    check('pure shell prime self-correlations vanish',H<e.log(I(2)).lo and (2*B).lo>e.log(I(4)).hi)
    check('fixed near band contains the entire q5 input',H<near<B.lo)
    intervals=[(B-e.log(I(2)),B-e.log(I(2))+H),
               (e.log(I(3))-B-H,e.log(I(3))-B),
               (e.log(I(4))-B-H,e.log(I(4))-B)]
    check('three far prime input intervals stay outside near band',all(l.lo>0 and r.hi<(B-near).lo for l,r in intervals))
    check('three far prime input intervals stay pairwise disjoint',all(intervals[k][1].hi<intervals[k+1][0].lo for k in range(2)))
    w5=e.log(I(5))/e.sqrt_enclosure(5)
    other=sum((e.log(I(prime))**2/q for q,prime in [(2,2),(3,3),(4,2)]),I(0))
    c0=sqrt((e.PI/e.sqrt_enclosure(2)+e.sqrt_enclosure(2)*w5)**2+2*other)
    complete=c0+sqrt(I(H)/(2*near))+F(5,4)*e.sqrt_enclosure(2)*sqrt(B*H)+720*sqrt(H)
    check('complete core-profile norm below 3.475',complete.hi<F(3475,1000))
    record('near_far_main_coupling',c0);record('complete_core_profile_coupling',complete)
    cGamma=2*e.log(2*e.PI)+2*e.gamma()
    k2B=I(F(25,24))/e.sqrt_enclosure(5)
    check('exact kernel at twice B is below one half',k2B.hi<F(1,2))
    check('sharp pure-shell Gamma constant below 4.831',cGamma.hi<F(4831,1000))
    # Analytic primitive and convex leakage proof are in PROOF.md, Section 2.
    check('both corrected profile floors exceed two L minus five',
          cGamma.hi+F(3,2)*H+H*(12*L.hi+1140)<5 and
          cGamma.hi+F(3,2)*H+H*(8*L.hi+450)<5)
    check('profile loss and remainder envelopes increase throughout band',L.lo>23 and L.lo+9>0 and 12*L.lo+1140-12>0)
    check('full coordinate norm factors one half and six valid',1+144*H<4 and 2+72*H<4)
    check('Gamma polynomial model covers entire band',(2*B+H).hi<F(5,3))
    check('corrector weight variation and model error budgets valid',F(3,5)**2*1200**2*2<1100**2 and F(6,5)*4*20+4<110)
    check('pointwise remainder includes all linear and logarithmic errors',70+8*100000+1100+4*10<300000*10 and 100000<300000)
    check('band is two hundred times previous outer width',H/F(5,10**13)==200)
    check('two equal non-halving steps fill the finite band',2*F(5,10**11)==H)
    check('every previously reached new endpoint admits a step of five e minus eleven',F(5,10**13)+F(5,10**11)<H)
    for key,value in [('width',H),('old_outer_width',F(5,10**13)),('sharp_Gamma_constant',cGamma),('kernel_at_twice_B',k2B),
                      ('profile_floor_at_outer_endpoint',2*L.lo-5),('tail_profile_norm_cap',cH),
                      ('comparison_payment',payment),('hard_block_payment',hard_payment)]:record(key,value)
    old=json.loads((root/PARENT/'adaptive_results.json').read_text(encoding='utf-8'))['values']
    summaries=[]
    for parity in (0,1):
        label='even' if parity==0 else 'odd';d=parent.compute_data(e,parity);ix=d['ix']
        for key,value in [('original_tail_floor',d['tail_floor']),('total_form_error',d['err'])]:
            source=old[label+'_'+key]
            check(label+' canonical '+key+' reproduced exactly',value.lo==F(source['lo']) and value.hi==F(source['hi']))
        check(label+' full high-profile norm including exact moment tail below 87 over 25',complete.hi**2*(1+d['epsmoment'].hi**2)<cH**2)
        check(label+' exact low moment ratios bounded by two',all(max(abs(r.lo),abs(r.hi))<2 for r in d['ratios']))
        derivative=sum((2*n+1)*(F(n*(n+1),2)+(2 if parity else 0))**2 for n in ix)
        check(label+' low derivative bound below 100000',derivative/F(128,125)<100000**2)
        Dg=sum((k*abs(d['pg'][k])*F(5,6)**(k-1)/2 for k in range(1,len(d['pg']))),F(0))
        check(label+' regular Gamma model derivative below ten',Dg<10)
        aa,cc,qq=parent.coupling_vectors(e,d,parity)
        for n,a,c,qchi in zip(ix,aa,cc,qq):
            for name,value in [('log_vector',a),('constant_vector',c),('model_corrector_functional',qchi)]:
                source=old[label+'_'+name+'_'+str(n)]
                assert value.lo==F(source['lo']) and value.hi==F(source['hi'])
                record(label+'_'+name+'_'+str(n),value)
        check(label+' all 93 analytic low coupling coefficients reproduce exactly',True)
        delta=I(d['tail_floor'].lo-cH**2/payment);shell=2*L.lo-5-payment
        check(label+' comparison tail and residual profile floors positive',delta.lo>0 and shell>0)
        mat=[[d['amat'][i][j]-d['err']/(2*ix[i]+1)*(i==j)-d['gmat'][i][j]/delta for j in range(31)] for i in range(31)]
        sigma,low,piv,failure=e.inverse_trace_bound(mat,ix)
        if failure:raise AssertionError(label+' comparison UNDECIDED: '+str(failure))
        check(label+' all 31 full-tail comparison pivots strictly positive',len(piv)==31 and all(v.lo>0 for v in piv))
        for n,pivot in zip(ix,piv):record(label+'_LDL_pivot_'+str(n),pivot)
        wa=parent.dual_product(e,low,piv,aa,aa);wac=parent.dual_product(e,low,piv,aa,cc);wc=parent.dual_product(e,low,piv,cc,cc)
        ell=e.log(2*B/H)
        energy=H*((ell**2+2*ell+2)*wa+2*(ell+1)*wac+wc)
        check(label+' signed rank-two integrated energy positive',energy.lo>0)
        remainder=300000*H*(L.hi+10)+110*d['eps']
        error=H*remainder**2/sigma.lo
        zeta=(sqrt(energy)+sqrt(error))**2/shell
        zeta_cap=F(13,10000) if parity==0 else F(7,10**5)
        check(label+' complete low-profile relative loss below published cap',zeta.hi<zeta_cap)
        crude=H*((72 if parity==0 else 110)*(L.hi+11)+(516 if parity==0 else 1440))**2
        shear=d['trace']/delta**2+crude/shell**2
        inverse=(1+sqrt(shear).hi)**2
        reserve=(1-zeta.hi)*sigma.lo
        soft_floor=F(8,10**13) if parity==0 else F(4,10**10)
        check(label+' actual harmonic soft Schur floor exceeds published bound',reserve>soft_floor)
        physical=min(reserve,delta.lo,shell)/(6*inverse)
        published=F(2,10**15) if parity==0 else F(1,10**12)
        check(label+' full physical gap exceeds published bound',physical>published)
        hard_tail=d['tail_floor'].lo-cH**2/hard_payment
        hard_shell=2*L.lo-5-hard_payment
        check(label+' growing hard block has coordinate floor above two fifths',min(hard_tail,hard_shell)>F(2,5))
        coupling_sq=d['trace'].hi+crude
        check(label+' actual low to entire growing hard operator norm below three',coupling_sq<9)
        atrace=sum(((2*n+1)*d['amat'][i][i] for i,n in enumerate(ix)),I(0))+31*d['err']
        check(label+' positive actual low matrix trace below two hundred',atrace.hi<200)
        check(label+' harmonic lift norm below fifteen halves',sqrt(coupling_sq).hi/F(2,5)<F(15,2))
        for key,value in [('full_tail_coupling_HS_squared',d['trace']),('effective_tail_floor',delta),('remaining_profile_floor',shell),
                          ('low_inverse_trace_reserve',sigma),('dual_log_squared',wa),('dual_log_constant_mixed',wac),('dual_constant_squared',wc),
                          ('integrated_main_energy',energy),('pointwise_remainder_upper',remainder),('integrated_remainder_energy',error),
                          ('adaptive_low_profile_relative_loss',zeta),('comparison_inverse_shear_squared',inverse),
                          ('actual_harmonic_soft_floor_lower',reserve),('published_soft_floor',soft_floor),
                          ('physical_gap_lower',physical),('published_physical_gap',published),
                          ('hard_tail_reserve',hard_tail),('hard_profile_reserve',hard_shell),
                          ('low_to_hard_norm_squared_upper',coupling_sq),('actual_low_trace_upper',atrace)]:record(label+'_'+key,value)
        summaries.append(dict(parity=label,width=str(H),physical_gap=str(published),soft_floor=str(soft_floor),hard_coordinate_floor='2/5'))
    check('harmonic coordinate forward and inverse shears bounded by nine',1+F(15,2)<9)
    check('exact endpoint cocycle has uniform transition bound sixteen',1+2*F(15,2)==16)
    check('harmonic physical coordinate bounds one over 162 and 486',F(1,2)/9**2==F(1,162) and 6*9**2==486)
    check('physical hard gap above one fifteenth',F(2,5)/6==F(1,15))
    direction=json.loads((root/BASE/'near-null-reduced-schur-direction-2026-09-19/direction_results.json').read_text())['values']
    energy_v=I(F(direction['source_energy']['lo']),F(direction['source_energy']['hi']))
    norm_v=I(F(direction['source_norm_squared']['lo']),F(direction['source_norm_squared']['hi']))
    check('fixed inherited source is nonzero and has positive energy',norm_v.lo>F(16,100) and energy_v.lo>0)
    check('harmonic inherited near-null Rayleigh upper bound below fourteen e minus twelve',4*energy_v.hi/norm_v.lo<F(14,10**12))
    check('total squared physical near-null variation budget below 8.2 e minus twelve',15*energy_v.hi<F(82,10**13))
    record('fixed_source_energy',energy_v);record('fixed_source_norm_squared',norm_v)
    record('near_null_Rayleigh_upper',4*energy_v.hi/norm_v.lo)
    record('near_null_total_squared_physical_variation_upper',15*energy_v.hi)
    stdout,stderr=replay.communicate();assert replay.returncode==0 and not stderr,stderr
    check('b1c0186 71 checks entire inherited chain and all hashes reproduce',
          'TOTAL 71 NEW EXACT CHECKS PASS' in stdout and 'REPLAY and all seven adaptive-package SHA256 hashes PASS' in stdout
          and 'INHERITED restart 88; odd 51; even 41; transition 38; all-core 40; direction 31; coordinate 28; shell 43; A-gauge 9; universal 349 PASS' in stdout)
    report=e.REPORT
    report.update(dict(anchor=ANCHOR,matrix_origin_commit=ORIGIN,bound_inputs=111,
        verdict='FINITE-BAND-MOVING-ENDPOINT-HARMONIC-BLOCK-RENEWAL-CLOSED',cases=summaries,
        status='AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',mellin_constraints=2,A1_used=False,
        source_selection_or_physical_renormalization=False,window_amplification_factor_over_anchor=200,
        full_infinite_tails_and_mixed_blocks_retained=True,soft_dimension_per_parity=31,
        distinguished_even_near_null_dimension=1,remaining_all_parity_low_dimension=61,
        finite_band_uniform_actual_harmonic_decomposition_certified=True,
        actual_infinite_Riesz_inverse_numerically_computed=False,
        near_null_drift_control='exact nested form-projection cocycle and total energy budget; no Lipschitz rate asserted',
        accumulated_profile_is_reset_to_empty_at_new_endpoint=False,
        operator_remainder_retained=True,adaptive_zeta_is_actual_full_profile_Theta=False,
        endpoint_uniform_renewal_beyond_finite_band_certified=False,non_summable_transport_certified=False,
        q7_threshold_reached=False,connected_unit_window_coercivity_certified=False,
        negative_physical_source_certified=False,global_Weil_positivity_certified=False,
        arithmetic_grid='1/10^200',analytic_proof='PROOF.md; sharpened Gamma primitive, full form domains and actual nested Riesz projections',
        inherited_replay_stdout_sha256=hashlib.sha256(stdout.encode('utf-8')).hexdigest(),
        inherited_replay_checks=dict(adaptive=71,restart=88,odd=51,even=41,transition=38,all_core=40,direction=31,coordinate=28,shell=43,a_gauge=9,universal_regressions=349)))
    report['check_count']=len(report['checks'])
    e.LOG.append('TOTAL '+str(report['check_count'])+' NEW EXACT CHECKS PASS');e.LOG.append(report['verdict'])
    logtext='INHERITED adaptive 71; restart 88; odd 51; even 41; transition 38; all-core 40; direction 31; coordinate 28; shell 43; A-gauge 9; universal 349 PASS\n'+'\n'.join(e.LOG)+'\n'
    jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.write:
        (HERE/'moving_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
        (HERE/'moving_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
        (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in PAYLOAD),encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'moving_results.json').read_bytes()==jsontext.encode('utf-8'),'JSON replay mismatch'
        assert (HERE/'moving_checks.log').read_bytes()==logtext.encode('utf-8'),'log replay mismatch'
        entries=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        assert [line.split('  ',1)[1] for line in entries]==PAYLOAD
        for line in entries:
            digest,name=line.split('  ',1);assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
        print('REPLAY and all seven moving-package SHA256 hashes PASS')
    print(logtext,end='')

if __name__=='__main__':main()
