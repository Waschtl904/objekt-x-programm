"""Exact finite data for N*Jt. No global function integration is asserted."""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import argparse, hashlib, io, json, zipfile

HERE = Path(__file__).resolve().parent
SPIKE_SHA = '7f7129945b38768a5ec88994b783211db1ceb0810129ffc4ea4ba7db5beb1f5e'
GLOBAL_SHA = '2ca3c682de8a529b12a0d628c2b606fd04df332d1299ccd36dff71ac3e53d80c'
GLOBAL_NAME = 'Objekt-X-Globaler-Gram-und-vollstaendige-Projektion-2026-10-13.zip'

def digest(b): return hashlib.sha256(b).hexdigest()
def member(z, suffix):
    hits = [n for n in z.namelist() if n.endswith('/' + suffix)]
    assert len(hits) == 1, (suffix, hits)
    return z.read(hits[0])
def read(z, suffix): return json.loads(member(z, suffix))
def dot(a, b): return sum((x*y for x, y in zip(a, b)), Q(0))
def mv(a, x): return [dot(row, x) for row in a]
def rat(a): return [[Q(x) for x in row] for row in a]
def upper_sqrt(q):
    assert q >= 0
    scale = 10**90
    n = isqrt(q.numerator*scale*scale//q.denominator)
    if n*n*q.denominator < q.numerator*scale*scale: n += 1
    r = Q(n, scale)
    assert r*r >= q
    return r
def interval_mv(a, t):
    out = []
    for row in a:
        lo = hi = Q(0)
        for interval, x in zip(row, t):
            l, h = map(Q, interval)
            assert l <= h
            lo += x*(l if x >= 0 else h)
            hi += x*(h if x >= 0 else l)
        out.append([lo, hi])
    return out
def ldl(a):
    n = len(a)
    assert all(a[i][j] == a[j][i] for i in range(n) for j in range(n))
    l = [[Q(i == j) for j in range(n)] for i in range(n)]
    d = []
    for i in range(n):
        d.append(a[i][i] - sum((l[i][k]**2*d[k] for k in range(i)), Q(0)))
        assert d[-1] > 0
        for j in range(i+1, n):
            l[j][i] = (a[j][i] - sum((l[j][k]*l[i][k]*d[k] for k in range(i)), Q(0)))/d[i]
    return l, d
def solve(ld, b):
    l, d = ld
    n = len(d)
    y = []
    for i in range(n): y.append(b[i] - dot(l[i][:i], y))
    x = [Q(0)]*n
    for i in range(n-1, -1, -1):
        x[i] = y[i]/d[i] - sum((l[j][i]*x[j] for j in range(i+1, n)), Q(0))
    return x
def dump(p, obj):
    p.write_bytes((json.dumps(obj, indent=2, ensure_ascii=False, default=str)+'\n').encode('utf-8'))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--spike-archive', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert __debug__
    out = args.output.resolve()
    assert not out.exists() and not out.is_relative_to(HERE)
    manifest_path = HERE/'MANIFEST.json'
    if manifest_path.exists():
        for name, wanted in json.loads(manifest_path.read_bytes()).items():
            p = (HERE/name).resolve()
            assert p.is_relative_to(HERE) and digest(p.read_bytes()) == wanted, name
    sb = args.spike_archive.read_bytes()
    gb = (HERE/'inputs'/GLOBAL_NAME).read_bytes()
    assert digest(sb) == SPIKE_SHA
    assert digest(gb) == GLOBAL_SHA
    results = {}
    operators = {}
    checks = {'positive_K_pivots':0, 'exact_Pv_components':0,
              'exact_q_identities':0, 'exact_K_inverse_entries':0,
              'exact_K_k_model_equations':0, 'exact_Sstar_Zt_zeros':0,
              'Jt_local_interval_coefficients':0}
    with zipfile.ZipFile(io.BytesIO(sb)) as sz, zipfile.ZipFile(io.BytesIO(gb)) as gz:
        cert = read(sz, 'BUDGET_CERTIFICATE.json')
        response_name = 'Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip'
        inverse_name = 'Objekt-X-A9-Inverserneuerung-und-Hoher-Schurrest-2026-10-13.zip'
        rb, ib = member(sz, response_name), member(sz, inverse_name)
        assert digest(rb) == '5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3'
        assert digest(ib) == 'a1fa41958d79ab16a7c42b12375c3373f5a86a99993ae2d23c984ff6b3b2e8ae'
        origins = read(gz, 'SNAPSHOT_ORIGINS.json')
        def snapshot(rel):
            raw = member(gz, 'snapshot/'+rel)
            if rel in origins: assert digest(raw) == origins[rel]['snapshot_sha256']
            return json.loads(raw)
        half = snapshot('work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/remainder-integration-check-v2/originals/half-inverse/expected/1536.json')
        common_rel = 'work/direct-rest84-2026-10-11/REFINED_COMMON96.json'
        common = snapshot(common_rel)
        with zipfile.ZipFile(io.BytesIO(rb)) as rz, zipfile.ZipFile(io.BytesIO(ib)) as iz:
            for index, parity in enumerate(['even', 'odd']):
                label = parity.upper()
                response_raw = member(rz, 'RESPONSES_'+label+'.json')
                response = json.loads(response_raw)
                inv = read(iz, 'INVERSE_'+label+'.json')
                assert digest(response_raw) == inv['response_source_sha256']
                assert response['bindings']['REFINED_COMMON96.json'] == origins[common_rel]['original_sha256']
                snap_response = snapshot('work/new-responses84-2026-10-11/RESPONSES_'+label+'.json')
                for field in ['K12_new_rational', 'rho', 'delta']:
                    assert response[field] == snap_response[field]
                ss = cert['parities'][parity]['W9_scalar_test']
                v = list(map(Q, ss['upper_vector_v']))
                p = list(map(Q, ss['lower_vector_Pv']))
                q = Q(ss['v_P_v'])
                assert len(v) == len(p) == 84
                assert mv(rat(inv['P_upper_rational']), v) == p
                checks['exact_Pv_components'] += 84
                assert dot(v, p) == q and q > 0
                checks['exact_q_identities'] += 1
                k = rat(response['K12_new_rational'])
                assert len(k) == 12 and all(len(row) == 12 for row in k)
                ld = ldl(k)
                checks['positive_K_pivots'] += 12
                columns = [solve(ld, [Q(i == j) for i in range(12)]) for j in range(12)]
                kinv = [[columns[j][i] for j in range(12)] for i in range(12)]
                for j in range(12):
                    assert mv(k, columns[j]) == [Q(i == j) for i in range(12)]
                checks['exact_K_inverse_entries'] += 144
                tr_inv = sum((kinv[i][i] for i in range(12)), Q(0))
                cbox = response['C203x84_model'][191:]
                assert len(cbox) == 12 and all(len(row) == 84 for row in cbox)
                cmid = [[(Q(x[0])+Q(x[1]))/2 for x in row] for row in cbox]
                rad2 = sum((((Q(x[1])-Q(x[0]))/2)**2 for row in cbox for x in row), Q(0))
                epsilon_c = Q(response['C_inverse_D_metric_error'][1])
                error_coefficient = epsilon_c + upper_sqrt(tr_inv*rad2)
                d = rat(snapshot('work/basis-coverage-2026-10-10/BASIS_'+label+'.json')['D_rational'])
                hb = half['blocks'][index]
                qbox = hb['basis_Q_local_coefficients']
                s = rat(hb['half_inverse_centre_rational_Q_coefficients'])
                assert len(d) == 8 and all(len(row) == 84 for row in d)
                assert len(qbox) == 96 and all(len(row) == 92 for row in qbox)
                assert len(s) == 92 and all(len(row) == 8 for row in s)
                directions = {}
                for name, t in [('upper_v', v), ('lower_Pv', p)]:
                    zt = mv(d, t)+t
                    assert all(sum((s[i][j]*zt[i] for i in range(92)), Q(0)) == 0 for j in range(8))
                    checks['exact_Sstar_Zt_zeros'] += 8
                    local = interval_mv(qbox, zt)
                    checks['Jt_local_interval_coefficients'] += 96
                    rhs = mv(cmid, t)
                    kmodel = solve(ld, rhs)
                    assert mv(k, kmodel) == rhs
                    checks['exact_K_k_model_equations'] += 12
                    err = error_coefficient*upper_sqrt(dot(t,t))
                    radii = [upper_sqrt(kinv[i][i])*err for i in range(12)]
                    directions[name] = {
                        't_exact_rational':t, 'Zt_exact_rational':zt,
                        'Jt_local_orthonormal_Legendre_coefficients_interval':local,
                        'K_inverse_Cfin_mid_t_exact_rational':kmodel,
                        'actual_k_error_K_norm_upper':err,
                        'actual_k_component_intervals':[[x-r,x+r] for x,r in zip(kmodel,radii)],
                        'chi_function_integrated':False,
                    }
                results[parity] = {'p_Pupper_v_and_q_exactly_checked':True, 'q':q,
                    'source_response_sha256':digest(response_raw),
                    'epsilon_C_upper':epsilon_c, 'Cfin_interval_radius_HS_squared':rad2,
                    'Cfin_midpoint_error_K_inverse_norm_upper':error_coefficient,
                    'directions':directions}
                operators[parity] = {
                    'delta':response['delta'], 'rho':response['rho'],
                    'K12_rational':response['K12_new_rational'], 'K12_inverse_rational':kinv,
                    'inverse_congruence_integer_matrix':common['cases'][index]['inverse_congruence_integer_matrix'],
                    'inverse_congruence_denominator':common['cases'][index]['inverse_congruence_denominator'],
                    'Cinv_original_source_sha256':origins[common_rel]['original_sha256'],
                    'Cinv_convention':'V=Cinv* (Phi* - B8 Th/delta); use this orientation',
                }
                print(parity, 'K pivots 12; v and Pv finite functional inputs checked', flush=True)
    out.mkdir(parents=True)
    dump(out/'DIRECTIONS.json', results)
    dump(out/'OPERATORS.json', operators)
    receipt = {'status':'PASS', 'spike_archive_sha256':SPIKE_SHA,
        'global_source_archive_sha256':GLOBAL_SHA, 'checks':checks,
        'full_U8_action_formula_derived':True,
        'finite_k_models_and_conditional_error_bounds_computed':True,
        'Nstar_Jt_function_integrals_computed':False,
        'W9_exclusion_test_computed':False, 'A9_A11_closed':False,
        'inherited_operator_and_integration_hypotheses_retained':True,
        'historical_574_pivots_replayed':False, 'large_integrations_recomputed':False,
        'current_GitHub_heads_reviewed':False, 'external_review_open':True}
    dump(out/'RECEIPT.json', receipt)
    for name in ['DIRECTIONS.json', 'OPERATORS.json', 'RECEIPT.json']:
        expected = HERE/'expected'/name
        if expected.exists():
            assert expected.read_bytes() == (out/name).read_bytes(), name
    print(json.dumps(receipt['checks']))

if __name__ == '__main__': main()
