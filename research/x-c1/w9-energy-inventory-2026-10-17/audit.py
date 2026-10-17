"""Data inventory and exact coarse norm arithmetic; no new energy integration."""
import argparse
import gzip
import hashlib
import io
import json
from fractions import Fraction as Q
from pathlib import Path
from types import MappingProxyType
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


class Inputs:
    def __init__(self):
        self.bindings = json.loads((HERE / 'INPUT_BINDINGS.json').read_bytes())
        data = {}
        for alias, spec in self.bindings['files'].items():
            path = (ROOT / spec['path']).resolve()
            need(path.is_relative_to(ROOT), 'Escaping input path')
            raw = path.read_bytes()
            need(hashlib.sha256(raw).hexdigest() == spec['sha256'], alias)
            data[alias] = raw
        self.data = MappingProxyType(data)

    def json(self, alias):
        return json.loads(self.data[alias])

    def member(self, alias):
        spec = self.bindings['members'][alias]
        with zipfile.ZipFile(io.BytesIO(self.data[spec['archive']])) as z:
            raw = z.read(spec['member'])
        need(hashlib.sha256(raw).hexdigest() == spec['sha256'], alias)
        return json.loads(gzip.decompress(raw) if spec['member'].endswith('.gz') else raw)


def shape(m, rows, cols):
    need(len(m) == rows and all(len(row) == cols for row in m), 'Unexpected matrix shape')
    return [rows, cols]


def positive_pivots(rows):
    a = [[Q(x) for x in row] for row in rows]
    n = len(a)
    need(all(a[i][j] == a[j][i] for i in range(n) for j in range(n)), 'Not symmetric')
    for k in range(n):
        need(a[k][k] > 0, 'Nonpositive exact pivot')
        for i in range(k + 1, n):
            for j in range(i, n):
                a[j][i] = a[i][j] = a[i][j] - a[i][k] * a[j][k] / a[k][k]
    return n


def power_cap(value):
    """Strict rational decimal power upper bound, without floating point."""
    need(value > 0, 'Nonpositive bound')
    cap, exponent = Q(1), 0
    while cap <= value:
        cap *= 10
        exponent += 1
    while cap / 10 > value:
        cap /= 10
        exponent -= 1
    return cap, f'1e{exponent}'


def build():
    inp = Inputs()
    common = inp.member('common')['cases']
    old = inp.member('old_sources')['cases']
    response = inp.member('response')['parities']
    functions = inp.member('functions')['parities']
    high = inp.json('high_response')
    coherent = inp.json('coherent')['parities']
    domain = inp.json('domain_check')
    result = {'status': 'AUTHOR_DERIVED_CONDITIONAL_INTERFACE_EXTERNAL_REVIEW_OPEN',
              'full_energy_matrix_computed': False, 'N12_decided': False,
              'old_large_integrations_rerun': False, 'parities': {}}
    for sigma, par in enumerate(('even', 'odd')):
        c, raw = common[sigma], old[sigma]
        inverse = inp.member('inverse_' + par)
        k = [[Q(v) for v in row] for row in coherent[par]['K_rational']]
        ki = [[Q(v) for v in row] for row in coherent[par]['K_inverse_rational']]
        shape(k, 12, 12); shape(ki, 12, 12)
        need(all(sum(k[i][l] * ki[l][j] for l in range(12)) == int(i == j)
                 for i in range(12) for j in range(12)), 'K inverse identity')
        k_floor = [[k[i][j] - (Q(1, 10**16) if i == j else 0)
                    for j in range(12)] for i in range(12)]
        pivots = positive_pivots(k_floor)
        need(domain['cases'][sigma]['K_minus_1e_minus_16_I_positive_pivots'] == pivots,
             'Inherited K floor mismatch')
        ci = c['inverse_congruence_integer_matrix']; shape(ci, 191, 191)
        delta, rho = Q(c['delta']), Q(c['rho'])
        need(delta == Q(18219, 10000) and 0 <= rho < 1, 'Invalid U8 weights')
        tr_xi = Q(sum(int(v)**2 for row in ci for v in row),
                  int(c['inverse_congruence_denominator'])**2) / (1-rho)
        tr_xi_hb = Q(high[par]['tr_X_HB_exact_rational'])
        gamma = Q(high[par]['full_M_norm_squared'][1])
        need(gamma >= 1 and 0 < tr_xi_hb < Q(463, 100)**2, 'Invalid inherited bounds')
        u8 = gamma * (1/delta + 2*tr_xi + 2*tr_xi_hb/delta**2)
        u, u_text = power_cap(u8)
        p = inverse['P_upper_rational']; shape(p, 84, 84)
        tr_p = sum(Q(p[i][i]) for i in range(84))
        need(tr_p == Q(inverse['candidate_P_upper_trace']), 'P trace mismatch')
        beta = Q(inverse['beta'])
        h = Q(11,10) * (Q(5,21)/beta + Q(500251,500000)*tr_p)
        h_cap = 65000 if par == 'even' else 11000
        need(0 < h < h_cap, 'H majorant norm bound failed')
        # Norms from the bound A9 domain proof: Lambda is an isometry,
        # ||F_old||<16, ||g_F|| and ||Q9 F_old||<1e11, ||g||<1000.
        v_cap = 16 + 10**11*u
        a_cap = 10**11 + 10**14*u
        n_cap = 1 + 1000*u + a_cap*10**16*v_cap
        w = u + 10**16*v_cap**2 + h_cap*n_cap**2
        w_cap, w_text = power_cap(w)
        energy = response[par]['fixed_X']
        gt = energy['physical_TT_adjoint_upper']; shape(gt, 12, 12)
        trace_gt = sum(Q(gt[i][i]) for i in range(12))
        need(trace_gt <= Q(energy['T_norm_squared_upper']), 'T Gram trace')
        dd = Q(functions[par]['whole_D12_operator_error_upper'])
        e = Q(energy['whole_Hilbert_residual_model_error_upper'])
        need(e*e >= dd*dd*trace_gt, 'Inherited Hilbert residual error')
        q_cap, q_text = power_cap(w_cap*dd*dd)
        residual_cap, residual_text = power_cap(w_cap*e*e)
        maps = {}
        for resolution in (384, 512):
            m = inp.json(f'maps_{par}_{resolution}')
            need(m['status'] == 'EXPLORATORY_NOT_DIRECTED', 'Map status')
            maps[str(resolution)] = {
                key: shape(m[key], rows, cols) for key, rows, cols in
                [('G_W',12,12),('H_gram',12,12),('H8_gram',12,12),
                 ('feature_factor',191,12),('b_F',12,12),('Fhat',12,12),('T',12,12)]}
        old_shapes = {}
        for section, key, rows, cols in [
            ('old_certificate','source_c_model',191,12),
            ('old_certificate','source_Bh_model',191,12),
            ('old_certificate','source_h_gram_model',12,12),
            ('old_certificate','joint_high_source_error_gram',12,12),
            ('galerkin','old_low_c_model',191,84),
            ('galerkin','old_low_Bh_model',191,84),
            ('galerkin','H84_model',84,84),
            ('galerkin','complete_source_high_cross_model',12,84)]:
            old_shapes[section+'.'+key] = shape(raw[section][key],rows,cols)
        shape(c['finite_cross_C84_new_model'],12,84)
        result['parities'][par] = {
            'K_inverse_exact_entries_checked':144,'K_floor_positive_pivots':pivots,
            'old_source_shapes':old_shapes,'stored_new_map_shapes':maps,
            'U8_norm_upper_decimal_power':u_text,
            'high_Schur_inverse_majorant_norm_upper':str(h_cap),
            'W9_norm_upper_decimal_power':w_text,
            'Q_D_scalar_identity_upper_decimal_power':q_text,
            'whole_residual_error_energy_upper_decimal_power':residual_text,
            'coarse_bound_suitable_for_N12_decision':False,
            'bound_interpretation':'Sufficient upper bounds only; not estimates of actual errors.',
            'partial_E8_finite_upper_formula':'2 gamma tr(Xi) + 2 gamma tr(Xi HB)/delta^2'}
    result['missing_new_residual_features'] = [
        'Full y_h^* y_h with y_h=T_h J_old^* Rhat Z (or exact e_sigma moment and H8/Phi Grams)',
        'B8 y_h: 191x12, required in V8 h8; C_inv^* Phi^* h8 alone is insufficient',
        'y_F^* y_h: 12x12 and y_J^* y_h: 84x12, with complete high projection',
        '(Lambda J)^* Rhat Z: 84x12 with exact old-shell geometry',
        'Whole T-functional nu and its complete R_L dual Gram, including constrained tail',
        'Useful weighted DeltaD Gram or five common feature-error Grams',
        'Directed remainders for every newly used integration and joint cross term']
    result['decision'] = 'DO_NOT_ASSEMBLE_OR_LABEL_A_FULL_NUMERICAL_W9_GRAM_FROM_CURRENT_MAPS'
    result['next_stage'] = 'Build missing full high cross maps and 84 bare pairings; then full nu/L-dual action, jointly preserving correlations.'
    return result


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output',type=Path)
    args = ap.parse_args()
    output = (json.dumps(build(),indent=2,ensure_ascii=False)+'\n').encode()
    if args.output:
        args.output.write_bytes(output)
    else:
        need(output == (HERE/'INVENTORY.json').read_bytes(), 'Inventory replay differs')
        print('PASS: exact norm/interface arithmetic and bound data inventory; full W9 Gram remains uncomputed')


if __name__ == '__main__':
    main()
