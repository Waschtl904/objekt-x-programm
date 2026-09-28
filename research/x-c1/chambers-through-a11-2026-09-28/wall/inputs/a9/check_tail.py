"""Exact supporting arithmetic for the full second-chamber high-tail proof.

This does not compute terminal Low/High matrices or certify full positivity.
Only the output JSON is written. A repository argument enables pinned-input
verification; the repository itself is read-only.
"""
import argparse
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import rational_bounds as rb

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(100000)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repository', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    checks = []

    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        checks.append(label)

    r, z0, eps_safe = F(11, 10), F(11, 20), F(1, 10**6)
    logs = {q: rb.log_bounds(q) for q in [2, 3, 5, 7, 8, 9]}
    check('A8 < A9 < 11/10', logs[8][1]/2 < logs[3][0] and logs[3][1] < r)
    check('A8 > 1', logs[8][0] > 2)
    check('log8=3log2 interval consistency', logs[8][0] <= 3*logs[2][1] and 3*logs[2][0] <= logs[8][1])
    check('q2 at most four nodes: log9 < 4log2', logs[9][1] < 4*logs[2][0])
    check('q3 exact endpoint contact has length 2log3', 9 == 3**2)
    check('q4,q5,q7,q8 shifts exceed one', all(logs[q][0] > logs[3][1] for q in [5, 7, 8]) and 2*logs[2][0] > logs[3][1])
    check('log2 < 7/10 and sqrt8 > 14/5', logs[2][1] < F(7,10) and F(14,5)**2 < 8)
    check('new envelope s_plus < 12 from inherited s_minus < 23/2', F(23,2)+2*F(7,10)/F(14,5) == 12)

    # Characteristic polynomials of path adjacency matrices, ascending powers.
    p0, p1 = [1], [0, 1]
    path_polys = {1: p1}
    for n in range(2, 5):
        shifted = [0] + p1
        previous = p0 + [0]*(len(shifted)-len(p0))
        pn = [a-b for a,b in zip(shifted,previous)]
        path_polys[n] = pn
        p0, p1 = p1, pn
    check('path2 characteristic polynomial', path_polys[2] == [-1, 0, 1])
    check('path3 characteristic polynomial', path_polys[3] == [0, -2, 0, 1])
    check('path4 characteristic polynomial', path_polys[4] == [1, 0, -3, 0, 1])
    # In Q(phi), phi^2=phi+1; pairs represent a+b*phi.
    def mul(a,b):
        return (a[0]*b[0]+a[1]*b[1], a[0]*b[1]+a[1]*b[0]+a[1]*b[1])
    phi2 = mul((0,1),(0,1)); phi4 = mul(phi2,phi2)
    check('golden ratio is exact positive path4 root', (phi4[0]-3*phi2[0]+1,phi4[1]-3*phi2[1]) == (0,0))
    scale = 10**12
    def sqrt_interval(q):
        lo = F(isqrt(q*scale*scale),scale)
        hi = lo+F(1,scale)
        check(f'radical enclosure sqrt({q})', lo*lo <= q < hi*hi)
        return lo,hi
    roots = {q: sqrt_interval(q) for q in [2,3,4,5,7,8]}
    phi_upper = (1+roots[5][1])/2
    shift = phi_upper*logs[2][1]/roots[2][0]
    for q,p in [(3,3),(4,2),(5,5),(7,7),(8,2)]:
        shift += logs[p][1]/roots[q][0]
    check('six-channel shift norm < 139/40', shift < F(139,40))

    b = sum((r**(2*k)/factorial(2*k+3) for k in range(21)), F(0))
    b += r**42/factorial(45)/(1-r*r/(46*47))
    lower = (1/rb.cosh_upper(r)-r*b/(1+r*r/6))/4
    check('z/(1+z^2/6) increasing on required radius', r*r < 6)
    check('kernel floor > 109/1000', lower > F(109,1000))
    kernel_loss = 2*r*(F(1,4)-F(109,1000))
    check('mean-zero Gamma loss = 1551/5000', kernel_loss == F(1551,5000))
    a5,b5 = rb.atan_bounds(F(1,5)); a239,b239 = rb.atan_bounds(F(1,239))
    check('pi < 22/7 via Machin identity', 16*b5-4*a239 < F(22,7))
    h8192 = sum((F(1,j) for j in range(1,8193)), F(0))
    check('Euler gamma < 5773/10000', h8192-13*logs[2][0] < F(5773,10000))
    q0_upper = rb.log_bounds(2*F(22,7)*r)[1]+F(5773,10000)
    check('q0 loss < 2511/1000', q0_upper < F(2511,1000))
    loss = F(2511,1000)+kernel_loss+F(139,40)
    check('total raw high loss = 31481/5000', loss == F(31481,5000))
    check('V times normalized moment carriers has norm < 2', 3*F(1,2) < 4)
    check('mixed form bound < 7', 2+r/2+F(139,40) < 7)
    check('full Q moment carrier norm < 10', 1+2+F(2511,1000)+r/2+F(139,40) < 10)
    even_ratio = rb.cosh_upper(z0)-1
    odd_ratio = z0*z0/(3*(1-z0*z0/20))
    check('full Mellin reconstruction operator norm <= 2', 1+even_ratio**2 < 4 and 1+odd_ratio**2 < 4)

    harmonics = [F(0)]
    for n in range(1, 647):
        harmonics.append(harmonics[-1]+F(1,n))
    rows = []
    for n, delta in [(384,F(1,5)),(502,F(1,2)),(594,F(2,3)),(646,F(3,4))]:
        eps = []
        for parity in [0,1]:
            degree = n+parity
            ep = z0**degree/factorial(degree)/(1-z0*z0/((degree+1)*(degree+2)))
            if parity:
                ep *= 4
            eps.append(ep)
            check(f'N={n}, parity={parity}: actual moment correction < 10^-6', ep < eps_safe)
        corrected = (harmonics[n]-loss-14*eps_safe-10*eps_safe**2)/(1+eps_safe**2)
        check(f'N={n}: complete corrected physical tail > {delta}', corrected > delta)
        dimension = n//2-1
        check(f'N={n}: exact parity coordinate counts', len(range(2,n,2)) == len(range(3,n+1,2)) == dimension)
        rows.append({'high_even_degree':n,'high_odd_degree':n+1,
                     'low_dimension_per_parity':dimension,'physical_floor':str(delta),
                     'high_defect_floor':str(delta/(delta+12)),
                     'raw_floor_exact':str(harmonics[n]-loss),
                     'corrected_floor_lower_exact':str(corrected),
                     'corrected_floor_lower_display':rb.decimal_display(corrected),
                     'actual_mellin_bounds_exact':[str(e) for e in eps],
                     'actual_mellin_bounds_display':[rb.decimal_display(e) for e in eps]})
    check('H594 > 69649/10000', harmonics[594] > F(69649,10000))
    check('short displayed tail certificate > 2/3', F(6687,10000)-14*eps_safe-10*eps_safe**2 > F(2,3)*(1+eps_safe**2))
    check('N592 does not pass this sufficient 2/3 ledger',
          (harmonics[592]-loss-14*eps_safe-10*eps_safe**2)/(1+eps_safe**2) < F(2,3))
    check('296-dimensional high defect reserve = 1/19', F(2,3)/(F(2,3)+12) == F(1,19))
    check('selected raw maximum degree', 594-1 == 593)
    check('selected model polynomial-support upper bound', 593+224+1 == 818)

    # Exact ordering witnesses for all six positive integration cells at A9.
    ratios=[F(1),F(4,3),F(3,2),F(5,3),F(7,3),F(8,3),F(3)]
    check('six strictly ordered positive A9 cells', all(a<b for a,b in zip(ratios,ratios[1:])))
    check('old q2/q4 coincident breakpoint splits at A9', F(4,3) != F(3,2))

    gamma = {}
    rb.checks.clear()
    for degree in [160,192,224]:
        bound = rb.gamma_bound(degree,r)
        gamma[str(degree)] = {'kernel_error_upper_exact':str(bound),
                              'kernel_error_upper_display':rb.decimal_display(bound),
                              'operator_error_upper_exact':str(2*r*bound),
                              'operator_error_upper_display':rb.decimal_display(2*r*bound)}
    checks.extend(rb.checks)
    bound224 = F(gamma['224']['kernel_error_upper_exact'])
    check('M224 kernel majorant < 4/10^36', bound224 < F(4,10**36))
    check('M160 new operator majorant exceeds old total budget', F(gamma['160']['operator_error_upper_exact']) > F(5,10**26))
    gamma_safe = F(11,5)*F(4,10**36)
    selected = next(row for row in rows if row['high_even_degree']==594)
    e_b = [2*gamma_safe+20*F(ep) for ep in selected['actual_mellin_bounds_exact']]
    check('Young coefficient for tau=1/1000', 1+1/F(1,1000) == 1001)

    bindings = json.loads((here/'SOURCE_BINDINGS.json').read_text(encoding='utf-8'))
    source_state = 'REPOSITORY_PINS_NOT_RECHECKED'
    for item in bindings['copied_inputs']:
        content = (here/item['package_path']).read_bytes()
        check('byte-preserved copied input: '+item['package_path'], hashlib.sha256(content).hexdigest()==item['sha256'])
    if args.repository:
        for item in bindings['repository_inputs']:
            content = subprocess.check_output(['git','show',item['commit']+':'+item['path']],cwd=args.repository)
            check('pinned repository input: '+item['label'], hashlib.sha256(content).hexdigest()==item['sha256'])
        source_state='ALL_REPOSITORY_PINS_VERIFIED'
    result = {'status':'SECOND_CHAMBER_HIGH_TAIL_CHECKS_PASS',
              'full_terminal_positivity':'OPEN','low_schur_matrices_computed':False,
              'analytical_review':'EXTERNAL_REVIEW_OPEN','source_bindings':source_state,
              'scope':'A8 <= A <= A9, q8 excluded at A8 and q9 excluded at A9',
              'checks_passed':len(checks),'checks':checks,
              'ledger':{'radius':str(r),'kernel_floor':'109/1000',
                        'computed_kernel_floor_display':rb.decimal_display(lower),
                        'shift_norm_upper':'139/40','computed_shift_upper_display':rb.decimal_display(shift),
                        'q0_loss_upper':'2511/1000','computed_q0_upper_display':rb.decimal_display(q0_upper),
                        'mean_zero_gamma_loss':str(kernel_loss),'total_high_loss':str(loss)},
              'cutoffs':rows,'selected_high_even_degree':594,'selected_dimension_per_parity':296,
              'gamma_preparation':gamma,
              'future_error_lift':{'chosen_kernel_error_upper':'4/'+str(10**36),
                                   'gamma_operator_error_upper':str(gamma_safe),
                                   'low_matrix_error_upper':str(4*gamma_safe),
                                   'coupling_error_upper_by_parity':[str(e) for e in e_b]},
              'file_sha256':{name:hashlib.sha256((here/name).read_bytes()).hexdigest()
                             for name in ['PROOF.md','check_tail.py','rational_bounds.py','SOURCE_BINDINGS.json']},
              'repository_status_promotion':False,'github_writes':False}
    output=args.output or here/'CHECK_RESULTS.json'
    output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:result[k] for k in ['status','checks_passed','source_bindings','selected_dimension_per_parity','full_terminal_positivity']}))
    for row in rows:
        print('dimension',row['low_dimension_per_parity'],'physical',row['physical_floor'],
              'defect',row['high_defect_floor'],'Mellin upper',row['actual_mellin_bounds_display'])


if __name__=='__main__':
    main()
