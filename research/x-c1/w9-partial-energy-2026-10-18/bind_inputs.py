"""Create an explicit input inventory; never called by the certificate replay."""
import hashlib
import io
import json
from pathlib import Path
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INVENTORY = HERE.parent/'w9-energy-inventory-2026-10-17/INPUT_BINDINGS.json'


def main():
    spec = json.loads(INVENTORY.read_bytes())
    spec['previous_inventory_source_commit'] = spec['source_commit']
    spec['source_commit'] = '0144b2feeb732c506f9ac19c059b2b849104dc0e'
    for group in ('files','members'):
        for item in spec[group].values():
            if 'used_fields' in item:
                item['previous_inventory_used_fields'] = item.pop('used_fields')
    spec['usage_note'] = ('Every listed file/member is bound in full. Previous inventory field lists '
                          'describe #237 only. Current numerical consumers and complete block roles '
                          'are specified below and in PROOF.md; inherited derivations are not re-audited.')
    # Preserve the previous inventory's exact file and archive-member anchors.
    cache = {}
    for alias, item in spec['files'].items():
        raw = (ROOT/item['path']).read_bytes()
        if hashlib.sha256(raw).hexdigest() != item['sha256']:
            raise RuntimeError(alias)
        cache[alias] = raw
    for alias, item in spec['members'].items():
        with zipfile.ZipFile(io.BytesIO(cache[item['archive']])) as z:
            raw = z.read(item['member'])
        if hashlib.sha256(raw).hexdigest() != item['sha256']:
            raise RuntimeError(alias)
        cache[alias] = raw
    outer_alias = 'nstar_archive'
    outer_path = 'research/x-c1/a9-inverse-spike-calibration-2026-10-15/archives/Objekt-X-Nstar-Jp-Funktionsanschluss-und-Koeffizienten-2026-10-16.zip'
    cache[outer_alias] = (ROOT/outer_path).read_bytes()
    spec['files'][outer_alias] = {'path': outer_path,
        'sha256': hashlib.sha256(cache[outer_alias]).hexdigest(),
        'role': 'Previously bound complete old function archive'}
    def add_member(alias, archive, suffix):
        with zipfile.ZipFile(io.BytesIO(cache[archive])) as z:
            names = [n for n in z.namelist() if n.endswith(suffix)]
            if len(names) != 1:
                raise RuntimeError((alias, names))
            raw = z.read(names[0])
        spec['members'][alias] = {'archive': archive, 'member': names[0],
                                  'sha256': hashlib.sha256(raw).hexdigest(),
                                  'role': 'Bound old function reconstruction'}
        cache[alias] = raw
    add_member('global_archive', outer_alias,
               'Objekt-X-Globaler-Gram-und-vollstaendige-Projektion-2026-10-13.zip')
    add_member('frozen_response', 'response_archive', '/inputs/FROZEN_RESPONSE12.json')
    add_member('fresh_A12', 'response_archive', '/inputs/FRESH_A12.json')
    for alias, suffix in {
        'a8_model': '/weighted-response/inputs/a8_model.json.gz',
        'half': '/half-inverse/expected/1536.json',
        'basis_even': '/basis-coverage-2026-10-10/BASIS_EVEN.json',
        'basis_odd': '/basis-coverage-2026-10-10/BASIS_ODD.json',
        'frozen_J_even': '/galerkin84-2026-10-10/MODEL_RAY_EVEN_3072.json',
        'frozen_J_odd': '/galerkin84-2026-10-10/MODEL_RAY_ODD_3072.json',
        'frozen_Y_even': '/u00-2026-10-07/CENTRES_EVEN_4096.json',
        'frozen_Y_odd': '/u00-2026-10-07/CENTRES_ODD_4096.json',
        'old_global_code': '/global-model-2026-10-12/compute_global_model.py',
        'old_source_code': '/vendor/source_core.py',
        'old_kernel_code': '/vendor/eight_source_refined.py',
    }.items():
        add_member(alias, 'global_archive', suffix)
    for alias, rel in {
        'inventory_proof': 'research/x-c1/w9-energy-inventory-2026-10-17/PROOF.md',
        'sharp_kp_proof': 'research/x-c1/sharp-kp-frozen-directions-2026-10-17/PROOF.md',
        'common96_builder': 'research/x-c1/a8-a9-global-closure-2026-10-13/packages/objekt-x-direkte-restform-und-positiver-96er-block-2026-10-11/refine_old_majorant.py',
        'previous_maps_code': 'research/x-c1/shell-polynomial-direction-search-2026-10-17/build_data.py',
        'previous_interval_code': 'research/x-c1/l00-z0-directed-interval-2026-10-17/certify.py',
        'kp_budget': 'research/x-c1/nstar-jp-spike-orthogonality-2026-10-16/original/gpt2-kp-budgets/expected/BUDGET_BOUNDS.json',
        'kp_even': 'research/x-c1/sharp-kp-frozen-directions-2026-10-17/expected/SHARP_K_even.json',
        'kp_odd': 'research/x-c1/sharp-kp-frozen-directions-2026-10-17/expected/SHARP_K_odd.json',
        'old_candidate_even': 'research/x-c1/shell-polynomial-direction-search-2026-10-17/data/FROZEN_even.json',
        'old_candidate_odd': 'research/x-c1/shell-polynomial-direction-search-2026-10-17/data/FROZEN_odd.json',
        'kp_model_even': 'research/x-c1/shell-search-reassessment-2026-10-17/data/K_MAP_even_128.json',
        'kp_model_odd': 'research/x-c1/shell-search-reassessment-2026-10-17/data/K_MAP_odd_128.json',
        'psi': 'research/x-c1/nstar-jp-spike-orthogonality-2026-10-16/original/gpt1-stufe1-zertifikat/expected/PSI_CORRECTED.json',
        'finite_action': 'research/x-c1/nstar-jp-spike-orthogonality-2026-10-16/original/gpt2-stufe3-endliche-u8-antwort/expected/FINITE_ACTION.json',
        'l00_even': 'research/x-c1/l00-z0-directed-interval-2026-10-17/expected/L00_CERTIFICATE_even.json',
        'l00_odd': 'research/x-c1/l00-z0-directed-interval-2026-10-17/expected/L00_CERTIFICATE_odd.json',
    }.items():
        raw = (ROOT/rel).read_bytes()
        spec['files'][alias] = {'path': rel, 'sha256': hashlib.sha256(raw).hexdigest(),
                               'role': 'Analytic formula and quadrature provenance'}
    spec['current_numerical_consumers'] = {
        'common': 'G96, U96, D96 lower/upper, a_fin model, finite feature errors, C8, delta, rho',
        'old_sources': 'low and high old F/J source coordinates, source errors and high Grams',
        'inverse_even/inverse_odd': 'P_upper_rational',
        'coherent': 'K_rational and K_inverse_rational',
        'high_response': 'tr_X_HB_exact_rational and full_M_norm_squared',
        'functions': 'all twelve analytic F/D functions and whole_D12_operator_error_upper',
        'response': 'whole_Hilbert_residual_model_error_upper and direct_K_error_upper',
        'a8_model': 'Gamma polynomial and A model intervals',
        'half': 'basis_Q_local_coefficients and half_inverse_centre_rational_Q_coefficients',
        'basis_even/basis_odd': 'D_rational',
        'frozen_Y_even/frozen_Y_odd': 'Y_local_rational_midpoints',
        'frozen_J_even/frozen_J_odd': 'working_basis_midpoints_rational',
        'frozen_response/fresh_A12': 'exact X and A12 model midpoint for the fixed rule',
        'maps_even_512/maps_odd_512': 'feature_factor and b_F, consistency controls only',
        'psi/finite_action/l00_even/l00_odd': 'independent z0 I0 consistency control',
        'old_candidate_even/old_candidate_odd/kp_even/kp_odd/kp_budget': 'previous fixed directions and directed budgets',
        'kp_model_even/kp_model_odd': 'exploratory candidate selection only'
    }
    (HERE/'INPUT_BINDINGS.json').write_text(json.dumps(spec, indent=2, ensure_ascii=False)+'\n')


if __name__ == '__main__':
    main()
