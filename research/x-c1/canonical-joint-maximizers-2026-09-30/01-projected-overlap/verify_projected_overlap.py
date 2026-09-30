"""Rational audit of joint-moment projector bounds and fixed countermodels.

Only the Python standard library is required. Source full-operator resolvent
bounds are inherited, hash-bound inputs; no finite matrix is called Q itself.
See PROJECTED_OVERLAP.md for the operator argument.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse, hashlib, json, sys

sys.set_int_max_str_digits(0)
DIGITS = 160
SCALE = 10 ** DIGITS

def point(x):
    x = F(x)
    return x, x

def interval(x):
    a, b = map(F, x)
    assert a <= b
    return a, b

def rounded(x):
    a, b = x[0] * SCALE, x[1] * SCALE
    return F(a.numerator // a.denominator, SCALE), F(-((-b.numerator) // b.denominator), SCALE)

def add(a, b): return rounded((a[0] + b[0], a[1] + b[1]))
def neg(a): return -a[1], -a[0]
def sub(a, b): return add(a, neg(b))
def mul(a, b):
    vals = [x*y for x in a for y in b]
    return rounded((min(vals), max(vals)))
def div(a, b):
    assert b[0] * b[1] > 0, 'zero-containing divisor'
    return mul(a, (1 / b[1], 1 / b[0]))
def absolute(a): return max(abs(a[0]), abs(a[1]))
def total(xs):
    out = point(0)
    for x in xs: out = add(out, x)
    return out
def sqrt_upper(x):
    assert x >= 0, 'negative square-root bound'
    k = isqrt(x.numerator * SCALE*SCALE // x.denominator)
    if F(k*k, SCALE*SCALE) < x: k += 1
    out = F(k, SCALE)
    assert out*out >= x
    return out
def tr(a): return list(map(list, zip(*a)))
def matrix(a): return [[interval(x) for x in row] for row in a]
def mm(a, b):
    assert len(a[0]) == len(b)
    return [[total(mul(x,y) for x,y in zip(row,col)) for col in tr(b)] for row in a]
def inverse(a, positive_pivots=False):
    n = len(a)
    m = [row[:] + [point(i == j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot = m[j][j]
        if positive_pivots: assert pivot[0] > 0, ('unproved positive pivot', j)
        m[j] = [div(x, pivot) for x in m[j]]
        m[j][j] = point(1)
        for i in range(n):
            if i == j: continue
            c = m[i][j]
            m[i] = [sub(x, mul(c,y)) for x,y in zip(m[i],m[j])]
            m[i][j] = point(0)
    return [row[n:] for row in m]
def symmetric(a):
    n = len(a)
    out = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            lo, hi = max(a[i][j][0],a[j][i][0]), min(a[i][j][1],a[j][i][1])
            assert lo <= hi
            out[i][j] = lo,hi
    return out
def norm_upper(a):
    return max(sum(absolute(x) for x in row) for row in a)
def rational(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,(tuple,list)): return [rational(z) for z in x]
    if isinstance(x,dict): return {k:rational(v) for k,v in x.items()}
    return x
def sci(x, upper=False, digits=8):
    if not x: return '0'
    if x < 0: return '-' + sci(-x,not upper,digits)
    e = 0
    while x < 1: x *= 10; e -= 1
    while x >= 10: x /= 10; e += 1
    scale = 10**(digits-1); z = x*scale; k = z.numerator//z.denominator
    if upper and F(k) < z: k += 1
    return f'{k//scale}.{k%scale:0{digits-1}d}e{e:+d}'
def display(a): return [sci(a[0]),sci(a[1],True)]

def moment_bound(source, trial):
    s = symmetric(matrix(trial['physical_Ritz_matrix']))
    hi = symmetric(matrix(source['trial_resolvent_upper']))
    lo = symmetric(matrix(source['trial_resolvent_lower']))
    c = symmetric(inverse(hi,positive_pivots=True))
    n = len(s); nu = F(trial['physical_complement_gap_lower_exact'])
    theta = F(trial['physical_trial_max_Rayleigh_upper_exact'])
    assert 0 < theta < nu
    # C = T_upper^{-1}; the common measure gives residual Gram <= S-C.
    e = [[sub(s[i][j],c[i][j]) for j in range(n)] for i in range(n)]
    assert all(e[i][i][1] >= 0 for i in range(n))
    b = [[absolute(c[j][i])/nu for j in range(n)] for i in range(n)]
    contraction = max(map(sum,b)); assert contraction < 1
    a = [sqrt_upper(e[i][i][1]/nu) for i in range(n)]
    ident_minus_b = [[point(F(i==j)-b[i][j]) for j in range(n)] for i in range(n)]
    solution = mm(inverse(ident_minus_b),[[point(x)] for x in a])
    # Verify a rational supersolution explicitly, including numerical rounding.
    residual_eta = [solution[i][0][1]*(1+F('1e-60'))+F('1e-100') for i in range(n)]
    assert all(x > 0 for x in residual_eta)
    margins = [residual_eta[i]-a[i]-sum(b[i][j]*residual_eta[j] for j in range(n)) for i in range(n)]
    assert min(margins) > 0
    energy_eta = [sqrt_upper(s[i][i][1]/nu) for i in range(n)]
    eta = [min(x,y) for x,y in zip(residual_eta,energy_eta)]
    assert all(0 < x < 1 for x in eta)
    # D1_jj <= nu eta_j^2; D0_jj <= eta_j^2; D-1_jj <= eta_j^2/nu.
    # Each minimum also has its own energy proof, not only an L2 proof.
    gp,lp,zp = [],[],[]
    for i in range(n):
        gr,lr,zr = [],[],[]
        for j in range(n):
            r = eta[i]*eta[j]
            d0 = (F(0),r) if i==j else (-r,r)
            gr.append(sub(point(i==j),d0))
            lr.append(sub(s[i][j],mul(point(nu),d0)))
            # T_lower <= T <= T_upper, followed by a correlated high-moment loss.
            di = sub(hi[i][i],lo[i][i])[1]
            dj = sub(hi[j][j],lo[j][j])[1]
            assert di >= 0 and dj >= 0, 'inconsistent resolvent order bounds'
            rad = sqrt_upper(di*dj)/2
            center = mul(point(F(1,2)),add(lo[i][j],hi[i][j]))
            tij = add(center,(-rad,rad))
            zr.append(sub(tij,div(d0,point(nu))))
        gp.append(gr);lp.append(lr);zp.append(zr)
    gram_lower = 1-sum(x*x for x in eta)
    assert gram_lower > 0
    return {'C':c,'residual_Gram_upper_entries':e,'comparison_matrix':b,
            'comparison_contraction':contraction,'supersolution':residual_eta,
            'supersolution_minimum_margin':min(margins),'eta':eta,'energy_eta':energy_eta,
            'high_energy_diagonal_upper':[nu*x*x for x in eta],
            'high_mass_diagonal_upper':[x*x for x in eta],
            'high_inverse_diagonal_upper':[x*x/nu for x in eta],
            'projected_Gram':gp,'projected_energy':lp,'projected_inverse':zp,
            'projected_Gram_uniform_lower':gram_lower,
            'eta_display_upper':[sci(x,True) for x in eta]}

def overlap_bound(key,outer,bounds,old_run):
    trans,par = key.rsplit('-',1); old,new = trans.split('->')
    at,bt = outer['trials'][old+'-'+par],outer['trials'][new+'-'+par]
    sa,sb = matrix(at['physical_Ritz_matrix']),matrix(bt['physical_Ritz_matrix'])
    nu = F(bt['physical_complement_gap_lower_exact'])
    ea,eb = bounds[old+'-'+par]['eta'],bounds[new+'-'+par]['eta']
    qa,qb = [sa[i][i][1] for i in range(6)],[sb[j][j][1] for j in range(8)]
    m = matrix(outer['results'][key]['trial_overlap'])
    y, radii = [],[]
    for i in range(6):
        row,rs = [],[]
        for j in range(8):
            mass = sub(point(1),total(mul(m[k][j],m[k][j]) for k in range(6)))
            rem = sqrt_upper(mass[1])
            err = ea[i]*(sum(ea[k]*absolute(m[k][j]) for k in range(6))+rem)
            err += sqrt_upper(qa[i]/nu)*eb[j] + sqrt_upper(qa[i]*qb[j])/17
            cell = add(m[i][j],(-err,err))
            old_cell = interval(old_run['annihilator_Y'][i][j])
            cell = max(cell[0],old_cell[0]), min(cell[1],old_cell[1])
            assert cell[0] <= cell[1]
            row.append(cell);rs.append(err)
        y.append(row);radii.append(rs)
    # A complete annihilator enclosure with the original final identity block.
    yl = [row[:6] for row in y];yr = [row[6:] for row in y]
    inv = inverse(yl)
    n = [[neg(x) for x in row] for row in mm(inv,yr)] + [[point(1),point(0)],[point(0),point(1)]]
    for i in range(8):
        for j in range(2):
            old_cell = interval(old_run['canonical_N'][i][j])
            n[i][j] = max(n[i][j][0],old_cell[0]),min(n[i][j][1],old_cell[1])
            assert n[i][j][0] <= n[i][j][1]
    # Same N and same projected moment matrices; these are enclosure outputs,
    # not independent free choices of Gram, energy, inverse or annihilator.
    moments = bounds[new+'-'+par]
    compress = {name:mm(mm(tr(n),moments[field]),n) for name,field in
                [('G0','projected_Gram'),('L0','projected_energy'),('Z0','projected_inverse')]}
    return {'Y':y,'Y_error_upper':radii,'N':n,'compressed_moment_entries':compress,
            'Y68_display':display(y[5][7]),'Y68_radius_upper':radii[5][7]}

def candidates(key,proposal,cross):
    base = cross['results'][key]['annihilator_Y']
    plans = {'axis_one':[['0','0'],['0',proposal[key]['last_right_radius_multiplier']]]}
    if 'double_parameters' in proposal[key]: plans['double']=proposal[key]['double_parameters']
    out={}
    for kind,parameters in plans.items():
        cells={}
        for i in range(2):
            for j in range(2):
                lo,hi=map(F,base[4+i][6+j])
                cells[(4+i,6+j)]=(lo+hi)/2+(hi-lo)/2*F(parameters[i][j])
        out[kind]=cells
    return out

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();base=Path(__file__).resolve().parent
    bindings=json.loads((base/'input_bindings.json').read_bytes());data={}
    for name,sha in bindings['sha256'].items():
        raw=(base/'inputs'/name).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==sha,('input hash mismatch',name)
        data[name]=json.loads(raw)
    outer=data['outer_primary.json'];cross=data['crosscheck.json'];proposal=data['candidate_proposals.json']
    old=data['extremal_verification.json']
    assert old['status']=='SYMMETRIC_PENCIL_GATE_AUDITED'
    assert old['input_sha256']['primary.json']==bindings['sha256']['primary.json']
    assert old['input_sha256']['crosscheck.json']==bindings['sha256']['crosscheck.json']
    assert old['input_sha256']['outer_primary.json']==bindings['sha256']['outer_primary.json']
    runs={}
    for run_name in ['primary.json','crosscheck.json']:
        src=data[run_name];assert src['source_commit']==bindings['source_commit']
        assert src['status']=='CANONICAL_EXTENSION_RESOLVENT_MOMENTS_CERTIFIED'
        assert src['uses_existing_terminal_positivity'] is True
        assert src['global_terminal_floor_inverse_used'] is False
        outer_path='research/x-c1/renewable-low-schur-spectral-2026-09-29/07-canonical-extension-outer-mass/primary.json'
        assert src['source_sha256'][outer_path]==bindings['sha256']['outer_primary.json']
        bounds={}
        for key,r in src['results'].items():
            assert r['whole_high_response_included'] is True
            name=key.split('->')[1]
            bounds[name]=moment_bound(r,outer['trials'][name])
            print(run_name,name,'eta <=',bounds[name]['eta_display_upper'][-1],flush=True)
        results={}
        for key in proposal:
            result=overlap_bound(key,outer,bounds,src['results'][key])
            excluded={}
            for kind,cells in candidates(key,proposal,cross).items():
                assert kind in old['results'][key]['candidates']
                violations=[]
                for (i,j),value in cells.items():
                    lo,hi=result['Y'][i][j]
                    distance=max(lo-value,value-hi)
                    if distance>0:
                        violations.append({'row':i+1,'column':j+1,'candidate':value,
                                           'enclosure':(lo,hi),'strict_separation':distance,
                                           'candidate_display':display((value,value)),
                                           'enclosure_display':display((lo,hi)),
                                           'separation_display_lower':sci(distance)})
                assert violations,('candidate not excluded',run_name,key,kind)
                excluded[kind]={'excluded':True,'violations':violations}
            result['excluded_candidates']=excluded;results[key]=result
            print(run_name,key,'Y68',result['Y68_display'],'all fixed candidates excluded',flush=True)
        runs[run_name]={'precision_bits_inherited':src['precision_bits'],'trials':bounds,'results':results}
    # Both inherited precision runs must enclose the same physical matrices.
    # C and E are auxiliary bounds and can depend on the arithmetic precision.
    def compatible(x,y):
        assert len(x)==len(y) and len(x[0])==len(y[0])
        assert all(max(x[i][j][0],y[i][j][0])<=min(x[i][j][1],y[i][j][1]) for i in range(len(x)) for j in range(len(x[0])))
    for name in runs['primary.json']['trials']:
        x=runs['primary.json']['trials'][name];y=runs['crosscheck.json']['trials'][name]
        for field in ['projected_Gram','projected_energy','projected_inverse']:
            compatible(x[field],y[field])
    for key in proposal:
        x=runs['primary.json']['results'][key];y=runs['crosscheck.json']['results'][key]
        for field in ['Y','N']:compatible(x[field],y[field])
        for field in ['G0','L0','Z0']:compatible(x['compressed_moment_entries'][field],y['compressed_moment_entries'][field])
    result={'status':'CERTIFIED_PROJECTED_OVERLAP_JOINT_MOMENT_GATE',
            'research_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN',
            'source_commit':bindings['source_commit'],'integration_base':bindings['integration_base'],
            'input_sha256':bindings['sha256'],'rounding_decimal_places':DIGITS,'runs':runs,
            'all_three_fixed_alternatives_excluded_in_both_runs':True,
            'actual_projectors_directly_solved':False,'joint_projected_moment_constraints_used':True,
            'large_operator_solves_rerun':False,'actual_maximizer_isolated':False,
            'actual_strict_extremal_gap_proved':False,'forward_renewal_proved':False}
    args.out.write_text(json.dumps(rational(result),indent=2)+'\n',encoding='utf-8',newline='\n')
    print('JOINT MOMENT PROJECTOR BOUNDS AND THREE FIXED EXCLUSIONS PASS',flush=True)

if __name__=='__main__':main()
