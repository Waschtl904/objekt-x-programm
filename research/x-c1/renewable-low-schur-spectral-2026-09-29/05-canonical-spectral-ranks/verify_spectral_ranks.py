"""Standard-library integer-interval replay of A8/A9 canonical spectral ranks.

The input models and complete-high/physical trial bounds are pinned and checked.
No floating-point spectral solver, new trial vectors, or eigenvectors are used.
Arb trace/mass/trial enclosures remain separately certified input calculations.
"""
from pathlib import Path
from fractions import Fraction as Q
import argparse, gzip, hashlib, json, shutil, subprocess, time

SCALE = 10**200
ZERO = (0, 0)
ONE = (SCALE, SCALE)
PIN = 'd16ba43ebb20f2c61f43379fc65d7a9b9dba76de'
CASES = {
    'A8': ('research/x-c1/first-chamber-o8-o9-2026-09-27/o8-rechenstand', 'reserve_refined', 5),
    'A9': ('research/x-c1/chambers-through-a11-2026-09-28/a9', 'reserve_results', 6),
}

def ceildiv(a, b): return -((-a)//b)
def add(a, b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[1], -a[0])
def sub(a, b): return add(a, neg(b))
def mul(a, b):
    values = [x*y for x in a for y in b]
    return (min(values)//SCALE, ceildiv(max(values), SCALE))
def div(a, b):
    assert b[0]*b[1] > 0
    return (min(x*SCALE//y for x in a for y in b),
            max(ceildiv(x*SCALE, y) for x in a for y in b))
def isum(values):
    out = ZERO
    for v in values: out = add(out, v)
    return out
def irat(value):
    x = Q(value)*SCALE
    return (x.numerator//x.denominator, ceildiv(x.numerator, x.denominator))
def decode(pair):
    lo, hi = map(int, pair)
    assert lo <= hi
    return lo*10**100, hi*10**100
def positive_pivots(a):
    n = len(a)
    L = [[ZERO]*n for _ in range(n)]
    d = []
    for i in range(n):
        pivot = sub(a[i][i], isum(mul(mul(L[i][k], L[i][k]), d[k]) for k in range(i)))
        assert pivot[0] > 0, (i, 'uncertified pivot')
        d.append(pivot)
        L[i][i] = ONE
        for j in range(i+1, n):
            L[j][i] = div(sub(a[j][i], isum(mul(mul(L[j][k], L[i][k]), d[k]) for k in range(i))), pivot)
    return [str(Q(x[0], SCALE)) for x in d]

def trial_bound(case):
    rank = case['trial_rank']
    s = case['physical_form_gram']
    g = case['physical_L2_gram']
    assert len(s) == len(g) == rank
    for mat in (s, g):
        assert all(len(row) == rank for row in mat)
        assert all(Q(x[0]) <= Q(x[1]) for row in mat for x in row)
    su = max(Q(s[i][i][1]) + sum(max(abs(Q(s[i][j][0])), abs(Q(s[i][j][1])))
             for j in range(rank) if j != i) for i in range(rank))
    gl = min(Q(g[i][i][0]) - sum(max(abs(Q(g[i][j][0])), abs(Q(g[i][j][1])))
             for j in range(rank) if j != i) for i in range(rank))
    assert gl > 0 and su > 0
    return su/gl, su, gl

def main():
    p = argparse.ArgumentParser()
    for k in ('repo', 'vectors', 'proposal', 'primary', 'crosscheck', 'out'):
        p.add_argument('--'+k, type=Path, required=True)
    a = p.parse_args()
    git = shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe'
    assert subprocess.check_output([git, 'rev-parse', 'HEAD'], cwd=a.repo).decode().strip() == PIN
    primary = json.loads(a.primary.read_bytes())
    cross = json.loads(a.crosscheck.read_bytes())
    proposal = json.loads(gzip.decompress(a.proposal.read_bytes()))
    vectors = json.loads(a.vectors.read_bytes())
    vh = hashlib.sha256(a.vectors.read_bytes()).hexdigest()
    assert primary['vectors_sha256'] == cross['vectors_sha256'] == proposal['vectors_sha256'] == vh
    assert primary['source_commit'] == cross['source_commit'] == PIN
    assert primary['source_sha256'] == cross['source_sha256']
    assert primary['precision_bits'] == 512 and cross['precision_bits'] == 768
    sources = dict(primary['source_sha256'])
    for name, digest in sources.items():
        raw = (a.repo/name).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        assert raw == subprocess.check_output([git, 'show', PIN+':'+name], cwd=a.repo)
    for name, digest in proposal['source_F_sha256'].items():
        assert sources[name] == digest
    results = {}
    cut = Q(17, 9999)
    for name, (rel, stem, rank) in CASES.items():
        folder = a.repo/rel
        fdata = json.loads(gzip.decompress((folder/(stem+'_lower_matrices.json.gz')).read_bytes()))
        model_raw = (folder/(name.lower()+'_model.json.gz')).read_bytes()
        model = json.loads(gzip.decompress(model_raw))
        receipt = json.loads((folder/(stem+'.json')).read_bytes())
        assert receipt['model_sha256'] == hashlib.sha256(model_raw).hexdigest()
        assert receipt['both_parities_strictly_certified'] is True
        delta = Q(receipt['full_high_physical_floor'])
        assert delta == Q(2, 3)
        # Bind the analytical complete-tail inputs as well as numerical blobs.
        tail_filename = 'refined_tail.json' if name == 'A8' else 'CHECK_RESULTS.json'
        for filename in ('PROOF.md', tail_filename):
            path = folder/filename
            raw = path.read_bytes()
            rp = path.relative_to(a.repo).as_posix()
            assert raw == subprocess.check_output([git, 'show', PIN+':'+rp], cwd=a.repo)
            sources[rp] = hashlib.sha256(raw).hexdigest()
        assert receipt['refined_tail_binding_sha256'] == sources[rel+'/'+tail_filename]
        for parity in ('even', 'odd'):
            start = time.time()
            key = name+'-'+parity
            pp = proposal['results'][key]
            pr, cr = primary['results'][key], cross['results'][key]
            assert pp['rank'] == pr['trial_rank'] == cr['trial_rank'] == rank
            assert Q(pr['delta_exact']) == Q(cr['delta_exact']) == delta
            s = Q(pp['comparison_cut_exact'])
            assert s == Q(1, 400)
            rows = fdata['parities'][parity]['lower_matrix']
            n = len(rows)
            assert n == (191 if name == 'A8' else 296) == pr['dimension'] == cr['dimension']
            fi = [[decode(x) for x in row] for row in rows]
            # Exact enclosure audit: saved F contains L0-eL I-delta^-1 Hup.
            eB = irat(receipt['parities'][parity]['coupling_operator_error_exact'])
            eL = irat(receipt['low_form_error_exact'])
            gram = model['parities'][parity]['complete_model_raw_high_Gram']
            low = model['parities'][parity]['A']
            for i in range(n):
                for j in range(n):
                    h = mul(irat('1001/1000'), decode(gram[i][j]))
                    if i == j: h = add(h, mul(irat(1001), mul(eB, eB)))
                    f = sub(decode(low[i][j]), mul(irat(1/delta), h))
                    if i == j: f = sub(f, eL)
                    assert fi[i][j][0] <= f[0] <= f[1] <= fi[i][j][1], (key, i, j, 'F enclosure')
            v = [[irat(vectors[key+'-'+str(j+1)]['coefficients'][i]) for j in range(rank)] for i in range(n)]
            shifted = [[sub(fi[i][j], irat(s)) if i == j else fi[i][j] for j in range(n)] for i in range(n)]
            r = [[int(x) for x in row] for row in pp['R_upper_grid']]
            t = [[int(x) for x in row] for row in pp['T_upper_grid']]
            grid = int(proposal['factor_scale'])
            grid2 = grid*grid
            assert SCALE % grid2 == 0
            assert len(r) == len(t) == n and all(len(row) == n for row in r+t)
            assert all(r[i][i] > 0 and t[i][i] > 0 and all(r[i][j] == t[i][j] == 0 for j in range(i)) for i in range(n))
            print(key, 'integer reconstruction of repaired matrix', flush=True)
            error_rows = []
            for i in range(n):
                row_error = 0
                for j in range(n):
                    repaired = add(shifted[i][j], isum(mul(v[i][k], v[j][k]) for k in range(rank)))
                    rr = sum(r[k][i]*r[k][j] for k in range(min(i,j)+1))*(SCALE//grid2)
                    row_error += max(abs(repaired[0]-rr), abs(repaired[1]-rr))
                error_rows.append(row_error)
            epsilon = Q(max(error_rows), SCALE)
            rt_rows, rt_cols = [0]*n, [0]*n
            for i in range(n):
                for j in range(i, n):
                    error = abs((grid2 if i == j else 0)-sum(r[i][k]*t[k][j] for k in range(i, j+1)))
                    rt_rows[i] += error
                    rt_cols[j] += error
            eta = Q(max(rt_rows+rt_cols), grid2)
            tnorm = Q(sum(x*x for row in t for x in row), grid2)
            assert eta < 1
            repaired_floor = (1-eta)**2/tnorm-epsilon
            assert repaired_floor > 0
            fv = [[isum(mul(shifted[i][k], v[k][j]) for k in range(n)) for j in range(rank)] for i in range(n)]
            compression = [[neg(isum(mul(v[k][i], fv[k][j]) for k in range(n))) for j in range(rank)] for i in range(rank)]
            pivots = positive_pivots(compression)
            # Comparison F-sI has exactly rank negative eigenvalues, zero kernel.
            gamma = Q(37 if name == 'A8' else 61)
            rho = Q(1003, 1000)
            for inp in (pr, cr):
                assert 0 < Q(inp['gamma_interval'][0]) <= Q(inp['gamma_interval'][1]) < gamma
                assert 1 < Q(inp['mass_norm_squared_interval'][0]) <= Q(inp['mass_norm_squared_interval'][1]) < rho
            for field in ('gamma_interval', 'mass_norm_squared_interval'):
                assert max(Q(pr[field][0]), Q(cr[field][0])) <= min(Q(pr[field][1]), Q(cr[field][1]))
            for field in ('physical_form_gram', 'physical_L2_gram'):
                for i in range(rank):
                    for j in range(rank):
                        px, cx = pr[field][i][j], cr[field][i][j]
                        assert max(Q(px[0]), Q(cx[0])) <= min(Q(px[1]), Q(cx[1]))
            tt = rho*cut
            aa = 1-gamma*tt/(delta*(delta-tt))
            margin = aa*s-tt
            assert 0 < tt < delta and aa > 0 and margin > 0
            upper, su, gl = trial_bound(pr)
            cu, cs, cg = trial_bound(cr)
            upper = max(upper, cu)
            assert upper < cut
            results[key] = {
                'matrix_dimension': n, 'comparison_cut_exact': str(s),
                'comparison_negative_count': rank, 'comparison_zero_count': 0,
                'repair_floor_exact': str(repaired_floor),
                'repair_residual_norm_upper_exact': str(epsilon),
                'approximate_inverse_residual_upper_exact': str(eta),
                'inverse_factor_frobenius_squared_exact': str(tnorm),
                'negative_compression_positive_pivots': pivots,
                'full_high_floor_exact': str(delta), 'gamma_used': str(gamma), 'rho_used': str(rho),
                'whole_space_transfer_margin_exact': str(margin),
                'physical_trial_rank': rank, 'physical_trial_upper_exact': str(upper),
                'physical_trial_b_quotient_upper_exact': str(upper/(upper+17)),
                'physical_trial_form_upper_exact': str(max(su, cs)),
                'physical_trial_mass_lower_exact': str(min(gl, cg)),
                'physical_cut_exact': str(cut), 'b_spectral_cut_exact': '1/10000',
                'true_spectral_projector_rank': rank, 'physical_cut_is_in_resolvent': True,
                'minimal_rank_for_complement_b_gap_at_least_cut': rank,
                'seconds': time.time()-start,
            }
            print(key, 'PASS: exact physical rank', rank, 'below q/b = 1/10000', flush=True)
    out = {
        'status': 'CERTIFIED_A8_A9_CANONICAL_SPECTRAL_RANKS', 'source_commit': PIN,
        'scope': 'Ranks at fixed terminals only; high and mass input bounds separately certified by Arb. No new eigenvectors, projector transports, or renewal theorem.',
        'integer_decimal_places': 200, 'bound_source_sha256': sources,
        'primary_sha256': hashlib.sha256(a.primary.read_bytes()).hexdigest(),
        'crosscheck_sha256': hashlib.sha256(a.crosscheck.read_bytes()).hexdigest(),
        'proposal_sha256': hashlib.sha256(a.proposal.read_bytes()).hexdigest(), 'vectors_sha256': vh,
        'results': results,
        'two_parity_projector_ranks': {name: sum(results[name+'-'+p]['true_spectral_projector_rank'] for p in ('even','odd')) for name in CASES},
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print('ALL SPECTRAL RANK CHECKS PASS', flush=True)

if __name__ == '__main__':
    main()
