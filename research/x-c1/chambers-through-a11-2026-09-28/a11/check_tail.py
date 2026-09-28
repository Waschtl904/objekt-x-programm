"""Exact arithmetic supporting the A11 full-tail proof; no low positivity verdict."""
import argparse,hashlib,json,subprocess,sys
from pathlib import Path
from fractions import Fraction as F
from math import factorial,isqrt
import rational_bounds as rb
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(100000)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repository',type=Path);ap.add_argument('--output',type=Path)
    args=ap.parse_args();here=Path(__file__).resolve().parent;checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
    scale=10**12
    def down(x):return F(x.numerator*scale//x.denominator,scale)
    def up(x):return -down(-x)
    r,z=F(6,5),F(3,5)
    logs={q:rb.log_bounds(q) for q in [2,3,4,5,7,8,9,11]}
    check('1 < A9 < A11 < 6/5',1<logs[3][0] and logs[3][1]<logs[11][0]/2 and logs[11][1]/2<r)
    check('q2 four-node bound 8 < 11 < 16',8<11<16)
    check('q3 three-node bound 9 < 11 < 27',9<11<27)
    check('remaining shifts exceed one',all(q*q>11 for q in [4,5,7,8,9]))
    check('q11 endpoint contact inactive',11==11 and logs[9][1]<logs[11][0])
    roots={}
    for q in [2,3,4,5,7,8,9]:
        lo=F(isqrt(q*scale*scale),scale);hi=lo+F(1,scale)
        check('rational square root enclosure '+str(q),lo*lo<=q<hi*hi)
        roots[q]=(lo,hi)
    channels=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
    weights={q:up(logs[p][1]/roots[q][0]) for q,p in channels}
    ds={q:(down(2*logs[q][0]/logs[11][1]),up(2*logs[q][1]/logs[11][0])) for q,p in channels}
    def complement(interval):return 1-interval[1],1-interval[0]
    def minusone(interval):return interval[0]-1,interval[1]-1
    breaks=[(F(0),F(0)),complement(ds[3]),minusone(ds[4]),minusone(ds[5]),
            complement(ds[2]),minusone(ds[7]),minusone(ds[8]),minusone(ds[9]),(F(1),F(1))]
    check('all eight positive cells rigorously ordered',all(a[1]<b[0] for a,b in zip(breaks,breaks[1:])))
    # A shift is active throughout each cell exactly when its threshold is to
    # the left/right of that cell. No sampled frequency or integral is used.
    cells=[]
    expected=[{2:2,3:2},{2:2,3:1},{2:2,3:1,4:1},
              {2:2,3:1,4:1,5:1},{2:1,3:1,4:1,5:1},
              {2:1,3:1,4:1,5:1,7:1},{2:1,3:1,4:1,5:1,7:1,8:1},
              {2:1,3:1,4:1,5:1,7:1,8:1,9:1}]
    for i,(left,right) in enumerate(zip(breaks,breaks[1:])):
        probe=(left[1]+right[0])/2
        counts={}
        for q,p in channels:
            for sign in [-1,1]:
                interval=(probe+ds[q][0],probe+ds[q][1]) if sign==1 else (probe-ds[q][1],probe-ds[q][0])
                active=-1<interval[0] and interval[1]<1
                check(f'cell {i+1} q{q} sign{sign} resolved',active or interval[1]<-1 or interval[0]>1)
                if active:counts[q]=counts.get(q,0)+1
        check(f'cell {i+1} exact active translation count',counts==expected[i])
        row=sum((weights[q]*count for q,count in counts.items()),F(0))
        # V is increasing on [0,1); use the lower enclosure of the left edge.
        vlower=rb.log_bounds(1/(1-left[0]**2))[0]/2
        combined=row-vlower
        check(f'cell {i+1} full S-minus-V form loss < 59/20',combined<F(59,20))
        cells.append({'left_interval':[str(v) for v in left],'right_interval':[str(v) for v in right],
                      'active_counts':counts,'row_upper_exact':str(row),
                      'V_lower_exact':str(vlower),'combined_upper_display':rb.decimal_display(combined)})
    phi=(1+roots[5][1])/2
    shift=phi*weights[2]+roots[2][1]*weights[3]+sum((weights[q] for q in [4,5,7,8,9]),F(0))
    check('separate full shift norm < 33/8',shift<F(33,8))
    check('q9 plus old s<12 gives s<13',logs[3][1]/3<F(11,30) and 12+2*F(11,30)<13)
    b=sum((r**(2*k)/factorial(2*k+3) for k in range(21)),F(0))
    b+=r**42/factorial(45)/(1-r*r/(46*47))
    lower=(1/rb.cosh_upper(r)-r*b/(1+r*r/6))/4
    check('kernel monotonic auxiliary majorant applies',r*r<6)
    check('regular Gamma kernel floor > 47/500',lower>F(47,500))
    kernel_loss=2*r*(F(1,4)-F(47,500))
    check('mean-zero Gamma loss 234/625',kernel_loss==F(234,625))
    a5,b5=rb.atan_bounds(F(1,5));a239,b239=rb.atan_bounds(F(1,239))
    check('Machin enclosure pi < 22/7',16*b5-4*a239<F(22,7))
    euler=sum((F(1,j) for j in range(1,8193)),F(0))-13*logs[2][0]
    check('Euler constant upper witness',euler<F(5773,10000))
    q0=rb.log_bounds(2*F(22,7)*r)[1]+F(5773,10000)
    check('q0 loss < 13/5',q0<F(13,5))
    loss=F(13,5)+kernel_loss+F(59,20)
    check('combined high loss exactly 14811/2500',loss==F(14811,2500))
    check('mixed moment-carrier form bound < 7',2+r/2+F(33,8)<7)
    check('full Q moment-carrier norm < 11',1+2+F(13,5)+r/2+F(33,8)<11)
    check('full Mellin map norm <=2',1+(rb.cosh_upper(z)-1)**2<4 and 1+(z*z/(3*(1-z*z/20)))**2<4)
    rows=[];coarse=F(1,10**6)
    for n,delta in [(410,F(2,3)),(484,F(5,6)),(572,F(1))]:
        harmonic=sum((F(1,k) for k in range(1,n+1)),F(0))
        eps=[]
        for p in [0,1]:
            j=n+p;ep=z**j/factorial(j)/(1-z*z/((j+1)*(j+2)))*(4 if p else 1)
            check(f'N{n} parity{p} complete Mellin correction',ep<coarse)
            eps.append(ep)
        corrected=(harmonic-loss-14*coarse-11*coarse**2)/(1+coarse**2)
        check(f'N{n} corrected full high floor exceeds {delta}',corrected>delta)
        dim=n//2-1
        check(f'N{n} both exact codimensions',len(range(2,n,2))==len(range(3,n+1,2))==dim)
        rows.append({'high_even_degree':n,'high_odd_degree':n+1,'low_dimension_per_parity':dim,
                     'physical_floor':str(delta),'high_defect_floor':str(delta/(delta+13)),
                     'corrected_floor_lower_display':rb.decimal_display(corrected),
                     'actual_mellin_bounds_exact':[str(x) for x in eps]})
    harmonic=sum((F(1,k) for k in range(1,573)),F(0))
    check('H572 > 6927/1000',harmonic>F(6927,1000))
    check('short high-floor certificate > 1',F(6927,1000)-loss-14*coarse-11*coarse**2>1+coarse**2)
    check('high defect floor 1/14',F(1)/(1+13)==F(1,14))
    rb.checks.clear();gamma={}
    for degree in [320,368,416]:
        bound=rb.gamma_bound(degree,r)
        gamma[str(degree)]={'kernel_error_upper_exact':str(bound),'kernel_error_upper_display':rb.decimal_display(bound),
                            'operator_error_upper_exact':str(2*r*bound),'operator_error_upper_display':rb.decimal_display(2*r*bound)}
    checks.extend(rb.checks)
    check('M416 kernel error below 1e-47',F(gamma['416']['kernel_error_upper_exact'])<F(1,10**47))
    bindings=json.loads((here/'SOURCE_BINDINGS.json').read_bytes())
    for item in bindings['copied_inputs']:
        check('copied source '+item['package_path'],hashlib.sha256((here/item['package_path']).read_bytes()).hexdigest()==item['sha256'])
    source_state='REPOSITORY_PINS_NOT_RECHECKED'
    if args.repository:
        for item in bindings['repository_inputs']:
            raw=subprocess.check_output(['git','show',item['commit']+':'+item['path']],cwd=args.repository)
            check('repository source '+item['label'],hashlib.sha256(raw).hexdigest()==item['sha256'])
        source_state='ALL_REPOSITORY_PINS_VERIFIED'
    result={'status':'THIRD_CHAMBER_HIGH_TAIL_CHECKS_PASS','full_terminal_positivity':'OPEN',
            'checks_passed':len(checks),'checks':checks,'source_bindings':source_state,
            'selected_high_even_degree':572,'selected_dimension_per_parity':285,
            'ledger':{'radius':'6/5','moment_radius':'3/5','shift_norm_upper':'33/8',
                      'shift_minus_potential_form_upper':'59/20','kernel_floor':'47/500',
                      'mean_zero_kernel_loss':str(kernel_loss),'q0_loss':'13/5','total_high_loss':str(loss),
                      'kernel_floor_computed_display':rb.decimal_display(lower)},
            'positive_cells':cells,'cutoffs':rows,'gamma_preparation':gamma,
            'file_sha256':{name:hashlib.sha256((here/name).read_bytes()).hexdigest()
                           for name in ['PROOF.md','check_tail.py','rational_bounds.py','SOURCE_BINDINGS.json']},
            'external_analytic_review':'OPEN','github_writes':False}
    out=args.output or here/'CHECK_RESULTS.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','checks_passed','source_bindings','selected_dimension_per_parity']}))
    print('Cell loss upper displays:',[cell['combined_upper_display'] for cell in cells])
    print('Gamma error displays:',{d:v['kernel_error_upper_display'] for d,v in gamma.items()})

if __name__=='__main__':main()
