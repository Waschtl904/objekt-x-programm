"""Finite U8 action, conditional on the hash-bound complete source certificates.

Standard library only. Every proof decision uses directed integer intervals.
The supplied Stage-2 quadrature is compared diagnostically, never used as a bound.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, gzip, hashlib, io, json, sys, zipfile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'vendor'))
import source_core as sc
from exact_coordinate_controls import run as coordinate_controls
sc.DIGITS = 180
sc.S = 10**180
I = sc.I
BRIDGE_SHA = 'b48e3895d57cc5cc2c11ca170e32d6af5fbdfcde9948b4db7c370d3376b6d57b'
GLOBAL_SHA = '2ca3c682de8a529b12a0d628c2b606fd04df332d1299ccd36dff71ac3e53d80c'
STAGE1_SHA = '940cd40e08be5884e6cd2a7e96e2e5815892bfb14a9e9c2d9b04d8aab317dd49'
STAGE2_SHA = '62e9f6d860ba98f4defc651b465cfc431f891cd058f52ddaf88d54073da18f13'


def sha(b): return hashlib.sha256(b).hexdigest()
def member(z, suffix):
    matches = [n for n in z.namelist() if n == suffix or n.endswith('/' + suffix)]
    assert len(matches) == 1, (suffix, matches)
    return z.read(matches[0])
def read(z, suffix): return json.loads(member(z, suffix))
def box(x):
    lo, hi = map(F, x)
    assert lo <= hi
    return I.raw(I(lo).lo, I(hi).hi)
def bm(a): return [[box(v) for v in r] for r in a]
def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b)), I(0))
def mv(a, x): return [dot(r, x) for r in a]
def tmv(a, x): return [dot(list(col), x) for col in zip(*a)]
def quad(a, x): return dot(x, mv(a, x))
def norm(v): return sum((x**2 for x in v), I(0)).sqrt()
def trprod(a, b):
    return sum((a[i][j]*b[j][i] for i in range(len(a)) for j in range(len(a))), I(0))
def pinner(p, q): return 2*sc.psymint(sc.pmul(p, q), I(1))
def legs(p, n):
    return [pinner(p, [I(x) for x in sc.leg(j)])*F(2*j+1, 2) for j in range(n+1)]
def encode(x):
    if isinstance(x, I): return x.frac()
    if isinstance(x, F): return str(x)
    if isinstance(x, dict): return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [encode(v) for v in x]
    return x
def dump(path, obj):
    path.write_bytes((json.dumps(encode(obj), indent=2, ensure_ascii=False)+'\n').encode())
def intersect_count(a, b):
    assert len(a) == len(b)
    for i, (x, y) in enumerate(zip(a, b)):
        assert x.intersects(y), (i, x.display(), y.display())
    return len(a)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bridge-archive', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert __debug__, 'Do not use python -O'
    out = args.output.resolve()
    assert not out.exists() and not out.is_relative_to(HERE)
    manifest = HERE/'MANIFEST.json'
    if manifest.exists():
        for name, digest in json.loads(manifest.read_bytes()).items():
            path = (HERE/name).resolve()
            assert path.is_relative_to(HERE) and sha(path.read_bytes()) == digest, name
    bridge = args.bridge_archive.read_bytes()
    assert sha(bridge) == BRIDGE_SHA
    provenance = {'bridge_sha256': BRIDGE_SHA, 'global_sha256': GLOBAL_SHA}
    with zipfile.ZipFile(io.BytesIO(bridge)) as z:
        operators = read(z, 'expected/OPERATORS.json')
        directions = read(z, 'expected/DIRECTIONS.json')
        global_bytes = member(z, 'Objekt-X-Globaler-Gram-und-vollstaendige-Projektion-2026-10-13.zip')
    assert sha(global_bytes) == GLOBAL_SHA
    with zipfile.ZipFile(io.BytesIO(global_bytes)) as z:
        origins = read(z, 'SNAPSHOT_ORIGINS.json')
        assert sha(member(z, 'vendor/source_core.py')) == sha((HERE/'vendor/source_core.py').read_bytes())
        data = {}
        for name in ['REFINED_INPUT.json', 'REFINED_COMMON96.json']:
            key = 'work/direct-rest84-2026-10-11/' + name
            raw = gzip.decompress((HERE/'inputs'/(name+'.gz')).read_bytes())
            assert sha(raw) == origins[key]['original_sha256']
            snap = member(z, 'snapshot/'+key)
            assert sha(snap) == origins[key]['snapshot_sha256']
            data[name] = json.loads(raw)
            # The snapshot selects fields; original source identity is checked above.
            provenance[name] = {'original_sha256': sha(raw), 'original_bytes': len(raw),
                                'snapshot_sha256': sha(snap)}
        key = 'work/inner-log-2026-10-12/INNER_LOG_1536.json'
        raw = member(z, 'snapshot/'+key)
        assert sha(raw) == origins[key]['snapshot_sha256']
        inner = json.loads(raw)
        provenance['INNER_LOG_1536_snapshot_sha256'] = sha(raw)
    stage1 = next((HERE/'inputs').glob('*Stufe1-Intervallzertifikat*.zip')).read_bytes()
    assert sha(stage1) == STAGE1_SHA
    with zipfile.ZipFile(io.BytesIO(stage1)) as z:
        psi = read(z, 'expected/PSI_CORRECTED.json')['data']
        parallel = read(z, 'expected/PARALLELISM.json')
    stage2 = next((HERE/'inputs').glob('*Stufe1v2-Stufe2*.zip')).read_bytes()
    assert sha(stage2) == STAGE2_SHA
    with zipfile.ZipFile(io.BytesIO(stage2)) as z:
        sm = read(z, 'MANIFEST.json')
        for name, digest in sm['files'].items():
            assert sha(member(z, name)) == digest, name
        diagnostic = read(z, 'stufe2/STUFE2_RESULTS.json')
    provenance['stage1_sha256'] = STAGE1_SHA
    provenance['stage2_sha256'] = STAGE2_SHA
    provenance['stage2_manifest_files_checked'] = len(sm['files'])
    inp = data['REFINED_INPUT.json']
    common = data['REFINED_COMMON96.json']
    results = {}
    counts = {'alternate_V_coordinate_intersections': 0, 'exact_direction_components': 0,
              'linear_direction_identity_intersections': 0}
    counts.update(coordinate_controls())
    for sigma, parity in enumerate(['even', 'odd']):
        print(parity, 'complete archived source reconstruction', flush=True)
        raw = inp['cases'][sigma]
        co = common['cases'][sigma]
        op = operators[parity]
        for field in ['inverse_congruence_integer_matrix', 'inverse_congruence_denominator', 'delta', 'rho']:
            assert co[field] == op[field], field
        cf = bm(raw['old_certificate']['source_c_model'])
        bf = bm(raw['old_certificate']['source_Bh_model'])
        cj = bm(raw['galerkin']['old_low_c_model'])
        bj = bm(raw['galerkin']['old_low_Bh_model'])
        lowj = bm(co['low_feature_J84_model'])
        lowf = bm(inner['cases'][sigma]['new_low_F_model'])
        ci = [[I(F(int(v), int(co['inverse_congruence_denominator']))) for v in row]
              for row in co['inverse_congruence_integer_matrix']]
        assert len(ci) == 191 and all(len(row) == 191 for row in ci)
        delta, rho = I(F(co['delta'])), I(F(co['rho']))
        assert delta.lo > 0 and 0 <= rho.lo <= rho.hi < sc.S
        ef = bm(co['finite_feature_error_gram'])
        ej = box(co['tail_feature_error_scalar'])
        uf = [[box(v) for v in row[:12]] for row in co['U96_model'][:12]]
        ki = [[I(F(v)) for v in row] for row in op['K12_inverse_rational']]
        tau, eps = trprod(ki, uf), trprod(ki, ef)
        assert min(tau.lo, eps.lo, ej.lo) > 0
        cinorm = norm([v for row in ci for v in row])
        a = 3*sc.log_point(F(2))/2
        mu = box(psi[parity]['mu'])
        moments = [sc.mellin(n, a) for n in range(384)]
        entries = {}
        for name in ['upper_v', 'lower_Pv', 'orthogonal_difference']:
            pr = psi[parity]['directions'][name]
            if name != 'orthogonal_difference':
                br = directions[parity]['directions'][name]
                assert list(map(F, pr['t_exact'])) == list(map(F, br['t_exact_rational']))
                assert list(map(F, pr['k_model_exact'])) == list(map(F, br['K_inverse_Cfin_mid_t_exact_rational']))
                counts['exact_direction_components'] += 96
            t = [I(F(x)) for x in pr['t_exact']]
            k = [I(F(x)) for x in pr['k_model_exact']]
            fc = [x-y for x, y in zip(mv(cj, t), mv(cf, k))]
            fb = [x-y for x, y in zip(mv(bj, t), mv(bf, k))]
            dd = [x-y/delta for x, y in zip(fc, fb)]
            vv = tmv(ci, dd)
            alt_v = [x-y for x, y in zip(mv(lowj, t), mv(lowf, k))]
            counts['alternate_V_coordinate_intersections'] += intersect_count(vv, alt_v)
            cc = [x/(1-rho) for x in mv(ci, vv)]
            kerr = box(pr['actual_k_minus_kmodel_K_norm_upper'])
            fixed_error = ej.sqrt()*norm(t) + quad(ef, k).sqrt()
            k_error = (tau.sqrt()+eps.sqrt())*kerr
            c_error = cinorm/(1-rho).sqrt()*(fixed_error+k_error)
            poly = [box(x) for x in pr['core_polynomial_scaled_x_over_a8_interval']]
            lc = legs(poly, 9)
            lm = a*dot(lc, moments[:10])
            wc = []
            for n in range(sigma+2, 384, 2):
                val = lc[n]/I(2*n+1).sqrt() if n < 10 else I(0)
                val -= lm/mu*I(2*n+1).sqrt()*moments[n]
                wc.append((2*a).sqrt()*val)
            diff = [x-y for x, y in zip(wc, cc)]
            core_error = box(pr['core_model_error_norm_upper'])
            lower = F(norm(diff).lo-c_error.hi-core_error.hi, sc.S)
            assert lower > 0
            entries[name] = {
                'Phi_star_f_model': fc, 'B_Th_f_model': fb, 'd_model': dd,
                'Vf_model': vv, 'c_model': cc, 'w0_low_model': wc,
                'w0_low_minus_c_model': diff, 'c_model_norm': norm(cc),
                'w0_low_minus_c_model_norm': norm(diff),
                'fixed_k_feature_error_bound': fixed_error,
                'k_change_feature_error_bound': k_error,
                'c_error_norm_bound': c_error, 'w0_error_norm_bound': core_error,
                'full_chi_norm_lower_rational': lower,
                'full_U8_action_computed': False}
            print(parity, name, 'c norm', norm(cc).display(), 'c error', c_error.display(), flush=True)
        alpha = F(parallel[parity]['alpha_q_over_vnorm2'])
        for field in ['Phi_star_f_model', 'B_Th_f_model', 'Vf_model', 'c_model', 'w0_low_model']:
            comparison = [alpha*x+y for x, y in zip(entries['upper_v'][field], entries['orthogonal_difference'][field])]
            counts['linear_direction_identity_intersections'] += intersect_count(entries['lower_Pv'][field], comparison)
        q = F(directions[parity]['q'])
        assert q == F(parallel[parity]['q_vstarP_v']) and q > 0
        lp = entries['lower_Pv']['full_chi_norm_lower_rational']
        wlower = F(11, 10)/q*lp**2
        # Separate diagnostic comparison: rounded Stage-2 raw coefficients,
        # with the nonorthogonal moment-corrected Phi pairing restored.
        scf = diagnostic[parity]['scaled_legendre_coeffs_<e_n,Uf>']
        comparisons = []
        for i, n in enumerate(range(sigma+2, sigma+18, 2)):
            cn = (I(F(2*n+1, 2*sigma+1))).sqrt()*moments[n]/moments[sigma]
            observed = I(F(scf[str(n)]))-cn*I(F(scf[str(sigma)]))
            gap = entries['upper_v']['Phi_star_f_model'][i]-observed
            comparisons.append({'degree': n, 'difference_using_rounded_mesh_values': gap,
                                'is_error_certificate': False})
        results[parity] = {'Cinv_HS_norm_bound': cinorm,
            'trace_Kinv_UF_model': tau, 'trace_Kinv_EF': eps,
            'directions': entries, 'fixed_full_W9_norm_lower_rational': wlower,
            'stage2_first_eight_pairings_diagnostic': comparisons}
        assert entries['upper_v']['full_chi_norm_lower_rational'] > F('1.34e13' if sigma == 0 else '1.0219e12')
        assert wlower > F('1.11e31' if sigma == 0 else '1.07e28')
    out.mkdir(parents=True)
    dump(out/'FINITE_ACTION.json', results)
    receipt = {'status': 'PASS_UNDER_BOUND_OPERATOR_DOMAIN_AND_COMPLETE_SOURCE_HYPOTHESES',
        'provenance': provenance, 'checks': counts,
        'whole_191_low_coefficients_for_v_p_e_certified': True,
        'whole_chi_norm_lower_bounds_certified_conditionally': True,
        'new_large_integrations': False, 'full_U8_function_computed': False,
        'N12_residual_pairings_computed': False, 'N12_excluded': False,
        'A9_A11_closed': False, 'true_A9_inverse_lower_bound_claimed': False,
        'W9_lower_bound_used_as_error_upper_bound': False, 'external_review_open': True,
        'github_changed': False}
    dump(out/'RECEIPT.json', receipt)
    if (HERE/'expected').exists():
        for name in ['FINITE_ACTION.json', 'RECEIPT.json']:
            assert (out/name).read_bytes() == (HERE/'expected'/name).read_bytes(), name
    print('PASS', counts, flush=True)


if __name__ == '__main__': main()
