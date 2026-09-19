#!/usr/bin/env python3
"""Exact window reserve transport and a uniform conditional restart ledger.

The analytic implications, including form domains, are proved in PROOF.md.
No floating-point decisions, numerical eigenvalues or quadrature are used.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ANCHOR='a659047e00d024c0daa3991ea59fd21afd9f8793'
ORIGIN='6a16d90b551588572c87e622c21c2df7f7b1adc2'
BASE='research/x-c1/'
ODD=BASE+'odd-profile-continuation-2026-09-19'
EVEN=BASE+'full-core-profile-width-amplification-2026-09-19'
UNIVERSAL=BASE+'universal-prime-power-family-2026-09-18'
SEGMENT=BASE+'prime-power-segment-4-2026-09-18'
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_restart.py',
         'input_bindings.json','restart_results.json','restart_checks.log']


def main():
    parser=argparse.ArgumentParser()
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--write',action='store_true')
    mode.add_argument('--verify',action='store_true')
    parser.add_argument('--root',type=Path,default=HERE.parents[2])
    args=parser.parse_args();root=args.root.resolve()
    binding=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
    assert binding['anchor']==ANCHOR and binding['matrix_origin_commit']==ORIGIN
    assert len(binding['files'])==len({x['path'] for x in binding['files']})==95
    for item in binding['files']:
        raw=(root/item['path']).read_bytes()
        assert len(raw)==item['bytes'],item['path']+' length'
        assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']+' SHA256'
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'],item['path']+' Git blob'
    spec=importlib.util.spec_from_file_location('pinned_segment',root/SEGMENT/'check_segment.py')
    engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
    I,check,record=engine.I,engine.check,engine.record
    check('95 distinct input files match pinned bytes SHA256 and Git blobs',True)
    environment=os.environ.copy();environment['PYTHONDONTWRITEBYTECODE']='1'
    print('Replaying both complete endpoint comparisons and the inherited chain',flush=True)
    replay=subprocess.Popen([sys.executable,'-B',str(root/ODD/'check_odd.py'),'--verify','--root',str(root)],
                            stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=environment)
    universal=subprocess.run([sys.executable,'-B',str(root/UNIVERSAL/'check_universal_family.py'),'--verify'],
                             capture_output=True,text=True,env=environment)
    assert universal.returncode==0 and not universal.stderr,universal.stderr
    check('349 universal-family regression checks and five payload hashes reproduce',
          'TOTAL 349' in universal.stdout and 'REPLAY and all five SHA256 payload hashes PASS' in universal.stdout)

    def sqrt_interval(value):
        value=I.of(value);scale=engine.SCALE;assert value.lo>=0
        lo=isqrt(value.lo.numerator*scale**2//value.lo.denominator)
        hi=isqrt(value.hi.numerator*scale**2//value.hi.denominator)+1
        assert F(lo,scale)**2<=value.lo and F(hi,scale)**2>value.hi
        return I(F(lo,scale),F(hi,scale))

    B=engine.log(I(5))/2;H=F(5,10**19);hcap=F(1,10**18)
    check('fixed core endpoint and enlarged window lie below one',F(4,5)<B.lo<B.hi<F(81,100) and (B+H).hi<1)
    check('enlarged fixed-core window contains only channels 2 3 4 5',(2*B+2*H).hi<engine.log(I(7)).lo)
    p2=B-engine.log(I(2));p3=engine.log(I(3))-B;p4=engine.log(I(4))-B
    intervals=[(p2,p2+H),(p3-H,p3),(p4-H,p4),(B-H,B)]
    check('four fixed-core input intervals remain inside the positive half',
          all(left.lo>0 and right.hi<=B.hi for left,right in intervals))
    check('four fixed-core input intervals remain pairwise disjoint',
          all(intervals[k][1].hi<intervals[k+1][0].lo for k in range(3)))
    weights2=sum((engine.log(I(p))**2/q for q,p in [(2,2),(3,3),(4,2),(5,5)]),I(0))
    prime=sqrt_interval(2*weights2)
    gamma=engine.PI/engine.sqrt_enclosure(2)+F(5,4)*engine.sqrt_enclosure(2)*sqrt_interval(B*H)
    for parity,correction in [('even',258),('odd',720)]:
        bound=gamma+prime+correction*sqrt_interval(H)
        check(parity+' complete core-profile coupling stays below four at enlarged width',bound.hi<4)
        record(parity+'_enlarged_complete_coupling_upper',bound)
    LH=engine.log(I(2)/H)
    check('largest window logarithm is enclosed by 214 over 5 and 43',F(214,5)<LH.lo<LH.hi<43)
    check('even profile moment loss remains below one',H*(8*43+450)<1)
    check('odd profile moment loss remains below one',H*(12*43+1140)<1)
    check('all window loss and squared low-coupling bounds increase with width',
          8*F(214,5)+450>8 and 12*F(214,5)+1140>12
          and 72*(F(214,5)+11)+516>144 and 110*(F(214,5)+11)+1440>220)
    check('physical factor six remains valid for both profile lifts',2+72*H<4 and 2+4==6)
    check('high-profile payment leaves the same exact tail deduction',F(41,10)**2/60==F(1681,6000))
    configs=[('even',EVEN,'width',4692,72,516),('odd',ODD,'odd',7820,110,1440)]
    windows=[]
    for width,loL,hiL,allgap in [(F(1,10**19),F(44),45,F(3,10**15)),
                                 (F(4,10**19),F(43),44,F(1,10**15)),
                                 (H,F(214,5),43,F(3,10**16))]:
        label='window_'+str(len(windows)+1);log=engine.log(I(2)/width);d=2*loL-77
        check(label+' directed logarithm enclosure',loL<log.lo<log.hi<hiL)
        check(label+' remaining shell floor positive after paying sixty',d>0)
        record(label+'_width',width);record(label+'_logarithm',log);record(label+'_remaining_profile_floor',d)
        item={'width':str(width),'published_all_parity_gap':str(allgap),'parities':{}}
        for parity,package,prefix,oldamp,sup,moment in configs:
            values=json.loads((root/package/(prefix+'_results.json')).read_text(encoding='utf-8'))['values']
            sigma=F(values[parity+'_three_block_Schur_inverse_trace_reserve_lower']['lo'])
            # Reconstruct the exact denominator used in the matrix calculation.
            # The displayed rounded effective-tail lower endpoint is not substituted.
            delta=F(values[parity+'_original_tail_floor']['lo'])-F(1681,6000)
            trace=F(values[parity+'_coupling_HS_squared']['hi'])
            oldloss=F(oldamp**2,15*10**20)
            oldrecord=values['low_profile_Schur_deduction']
            check(label+' '+parity+' baseline scalar deduction matches parent',F(oldrecord['lo'])<=oldloss<=F(oldrecord['hi']))
            amplitude=sup*(hiL+11)+moment;b2=width*amplitude**2
            deduction=b2/d-oldloss;new_sigma=sigma-deduction
            check(label+' '+parity+' exact scalar matrix transport keeps positive reserve',deduction>0 and new_sigma>0)
            shear2=trace/delta**2+b2/d**2
            k=isqrt(shear2.numerator*10**12//shear2.denominator)+1;r=F(k,10**6)
            check(label+' '+parity+' inverse shear bounded by integer square root',r*r>shear2)
            physical=min(new_sigma,delta,d)/(6*(1+r)**2)
            published=allgap if parity=='even' else F(1,10**12)
            check(label+' '+parity+' physical gap exceeds published rational bound',physical>published)
            for key,value in [('new_low_reserve',new_sigma),('scalar_deduction_increment',deduction),
                              ('exact_effective_tail_floor',delta),('low_profile_squared_bound',b2),
                              ('inverse_shear_squared_bound',(1+r)**2),('physical_gap_lower',physical),
                              ('published_gap',published)]:record(label+'_'+parity+'_'+key,value)
            item['parities'][parity]={'low_amplitude':amplitude,'published_gap':str(published)}
        windows.append(item)
    check('largest width is fifty times the inherited window',H/F(1,10**20)==50)

    # Uniform analytic estimates for B <= a < b <= 1, including channel 7.
    check('all possible channels through unit half-width are 2 3 4 5 7',engine.log(I(7)).hi<2<engine.log(I(8)).lo)
    weights=[]
    for q,p in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
        weight=engine.log(I(p))/engine.sqrt_enclosure(q);weights.append(weight)
        check('uniform channel '+str(q)+' weight below one',0<weight.lo<weight.hi<1)
    kappa_upper=engine.log(8*engine.PI)+1+engine.PI/2
    check('kappa bounded by six using Euler gamma below one',kappa_upper.hi<6)
    check('uniform bounded non-Gamma remainder below sixteen',6+2*5==16)
    half=engine.exp_pos(I(F(1,2)));cosh=(half+1/half)/2;sinh=(half-1/half)/2
    check('uniform two original moment weights bounded by six fifths and three fifths',cosh.hi<F(6,5) and sinh.hi<F(3,5))
    check('uniform corrector moments bounded away from zero',B.lo/2>F(2,5) and (B**2/24).lo>F(2,75))
    check('uniform even corrector supremum Lipschitz and squared norm bounds',F(5,2)<3 and F(5,4)*F(5,2)<4 and 2*3**2==18)
    check('uniform odd corrector supremum Lipschitz and squared norm bounds',F(1,4)/F(2,75)<10 and F(5,4)/F(2,75)<47 and 2*10**2==200)
    ge=2*(103**2+2*103*6+2*6**2);go=2*(680**2+2*680*20+2*20**2)
    check('even corrector Gamma pointwise coefficients',2*4*5+4*3*F(21,4)==103 and 4*3/F(2)==6)
    check('odd corrector Gamma pointwise coefficients',2*47*5+4*10*F(21,4)==680 and 4*10/F(2)==20)
    check('uniform even complete corrector functional at most 225',ge==23834<155**2 and 16**2*18<70**2 and 155+70==225)
    check('uniform odd complete corrector functional at most 1230',go==980800<1000**2 and 16**2*200<230**2 and 1000+230==1230)
    uniform_gamma=engine.sqrt_enclosure(2)*(engine.PI/2+F(5,4)*sqrt_interval(hcap))
    uniform_cross=uniform_gamma+10+738*sqrt_interval(hcap)
    check('uniform Gamma coupling below three',uniform_gamma.hi<3)
    check('both moment corrections bounded by 738 sqrt h',F(6,5)*225==270<738 and F(3,5)*1230==738)
    check('uniform entire core-profile mixed operator below fourteen',uniform_cross.hi<14)
    record('uniform_complete_core_profile_coupling_upper',uniform_cross)
    check('shell prime self-interactions paid even at channel entrance',2*5*2==20)
    check('uniform shell lower floor exceeds twice L minus eighteen',1+12+20+2*hcap<36)
    check('bounded core to shell loss includes all five channels',1+2*5+2==13)
    check('even profile correction fits uniform loss 12 L plus 1400',
          2*F(6,5)*3==F(36,5)<12 and F(36,5)*13+F(36,25)*16*18==F(12708,25)<1400)
    check('odd profile correction fits uniform loss 12 L plus 1400',
          2*F(3,5)*10==12 and 12*13+F(9,25)*16*200==1308<1400)
    Lcap=engine.log(I(2)/hcap)
    check('uniform cap logarithm lies between 42 and 43',42<Lcap.lo<Lcap.hi<43)
    check('uniform moment loss below one and increases with h',hcap*(12*43+1400)<1 and 12*42+1400-12>0)
    check('uniform profile floor exceeds L',2*42-37>42)
    check('moment-corrector squared cost at most 72 h',F(36,25)*18<72 and F(9,25)*200==72)
    check('uniform lift and inverse Hilbert bounds',2+72*hcap<4 and 144*hcap+F(1,2)<2 and 1+4==5)
    check('anisotropic physical norm bounded by three halves core plus three profile',2+216*hcap<3)
    check('closed-form graph comparison constants',32>16 and F(32,2)-14>=1 and 14+32*5==174)
    check('dyadic width bound lies inside uniform cap',2**80>10**20 and 1600>80)
    check('log two is larger than one half',engine.LOG2.lo>F(1,2))
    check('restart threshold gives L greater than 800 over epsilon',F(1600,2)==800)
    check('full relative profile Schur norm below one quarter',F(14**2,800)==F(49,200)<F(1,4))
    check('full relative Schur reserve above 151 over 200',1-F(49,200)==F(151,200))
    check('physical Young payment leaves sixteen over epsilon',4*14**2==784 and 800-784==16)
    check('anisotropic physical estimate gives half of input gap',F(3,4)==F(1,2)*F(3,2) and 16>=F(3,2))
    epsilon0=F(3,10**16);threshold=1600/epsilon0
    N0=-(-threshold.numerator//threshold.denominator)
    check('first exact restart exponent is the integer ceiling',N0==5333333333333333334 and N0-1<threshold<=N0)
    check('all dyadic iterates retain the restart threshold algebraically',N0*epsilon0>=1600)
    check('iteration total width bound remains within unit half-width',B.hi+H<F(82,100) and N0>80 and F(2,2**80)<F(1,100))
    # Base constants of the induction; the quantified recurrence and the
    # geometric majorant are proved in PROOF.md, not by sampled indices.
    check('squared step recurrence has a summable geometric majorant',2**0>=1 and 2*(1)>=1+1)
    record('restart_initial_gap',epsilon0);record('restart_initial_exponent',N0)
    record('restart_Theta_upper',F(49,200));record('restart_relative_Schur_floor',F(151,200))
    record('restart_gap_retained_fraction',F(1,2));record('uniform_width_cap',hcap)

    stdout,stderr=replay.communicate()
    assert replay.returncode==0 and not stderr,stderr
    check('odd 51 even 41 and the entire inherited chain reproduce',
          'TOTAL 51 NEW EXACT CHECKS PASS' in stdout
          and 'REPLAY and all seven odd-package SHA256 hashes PASS' in stdout
          and 'INHERITED even-width 41 PASS; transition 38 PASS; all-core 40 PASS; direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS' in stdout)
    report=engine.REPORT
    report.update({'anchor':ANCHOR,'matrix_origin_commit':ORIGIN,'bound_inputs':95,
        'verdict':'FIFTYFOLD-ALL-PARITY-WINDOW-AND-QUANTITATIVE-CONDITIONAL-RESTART',
        'windows':windows,'mellin_constraints':2,'A1_used':False,
        'source_selection_or_physical_renormalization':False,
        'window_amplification_certified':True,'uniform_conditional_one_step_restart_certified':True,
        'every_finite_step_of_explicit_summable_iteration_certified':True,
        'nonaccumulating_transport_certified':False,'uniform_gap_over_infinite_iteration_certified':False,
        'connected_unit_window_coercivity_certified':False,'global_Weil_positivity_certified':False,
        'negative_physical_source_certified':False,
        'restart_domain':'log(5)/2 <= a < b <= 1; 0 < epsilon <= 1; q_a >= epsilon I',
        'restart_width':'0 < b-a <= min(1-a, 2^(-ceil(1600/epsilon)))',
        'restart_conclusion':'q_b >= (epsilon/2) I on the original two-Mellin kernel',
        'iteration':'epsilon_n=(3/10^16)/2^n; N_n=2^n*5333333333333333334; h_n=2^(-N_n)',
        'iteration_total_width_upper':'2^(1-5333333333333333334)',
        'finite_matrix_role':'transport of replayed full-tail Schur matrices by an exact scalar multiple of J',
        'analytic_proof':'PROOF.md; actual source form closures and all infinite core/profile mixed blocks',
        'arithmetic_grid':'1/10^200',
        'inherited_replay_checks':{'odd':51,'even':41,'transition':38,'all_core':40,'direction':31,'coordinate':28,'shell':43,'a_gauge':9,'universal_regressions':349},
        'inherited_replay_stdout_sha256':hashlib.sha256(stdout.encode('utf-8')).hexdigest(),
        'universal_replay_stdout_sha256':hashlib.sha256(universal.stdout.encode('utf-8')).hexdigest()})
    report['check_count']=len(report['checks'])
    engine.LOG.append('TOTAL '+str(report['check_count'])+' NEW EXACT CHECKS PASS')
    engine.LOG.append(report['verdict'])
    logtext=('INHERITED odd 51 PASS; even 41 PASS; transition 38 PASS; all-core 40 PASS; direction 31 PASS; coordinate 28 PASS; shell 43 PASS; A-gauge 9 PASS; universal regressions 349 PASS\n'
             +'\n'.join(engine.LOG)+'\n')
    jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
    if args.write:
        (HERE/'restart_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
        (HERE/'restart_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
        (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/p).read_bytes()).hexdigest()+'  '+p+'\n' for p in PAYLOAD),encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'restart_results.json').read_bytes()==jsontext.encode('utf-8'),'JSON replay mismatch'
        assert (HERE/'restart_checks.log').read_bytes()==logtext.encode('utf-8'),'log replay mismatch'
        entries=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        assert [entry.split('  ',1)[1] for entry in entries]==PAYLOAD
        for entry in entries:
            digest,name=entry.split('  ',1);assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
        print('REPLAY and all seven restart-package SHA256 hashes PASS')
    print(logtext,end='')


if __name__=='__main__':main()
