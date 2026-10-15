"""Replay the sealed whole-response-Gram package (A9->A11 response norm and model error).

Only the package's own new certificate computation is rerun (whole response
Grams, separate exact check). The incoming F12/D12 full replay is optional
(--full-input). Analytic hypotheses are inherited, not machine verified; no
W9 energy is computed.
"""
from pathlib import Path
import argparse, json, sys, zipfile
from replay_a9_sealed import archive, digest, execute, match, require, safe

REPO = Path(__file__).resolve().parents[1]
PACKAGE = REPO/'research/x-c1/a9-a11-whole-response-gram-2026-10-15'
SEALED_ARCHIVE = 'b8677c0bb085f40052e52953ec39112894fbaa0f9f5d9997df8ae546238f41ee'
NESTED_FUNCTIONS = '0a7bda3d2d896801f757c3b658d9ad559529409c64dd489283e656b95710d3d3'
FROZEN_RESPONSE = '132959da5d34c0c89471ee15f7c34d8b4a42ad48c641b6c4db5181113d11426a'


def check_receipt(actual, expected):
    require(actual['status'] == 'PASS', 'sealed checker did not pass')
    for key in ('exact_Gram_entry_comparisons', 'positive_upper_Gram_pivots', 'manifest_bindings',
                'original_function_members_byte_equal'):
        require(actual[key] == expected[key], 'receipt count differs: ' + key)
    require(actual['exact_Gram_entry_comparisons'] == 576 and actual['positive_upper_Gram_pivots'] == 48,
            'missing Gram comparisons or pivots')
    for key in ('fixed_response_unchanged', 'new_energy_JSON_fresh_and_byte_equal',
                'new_separate_check_fresh_and_byte_equal', 'exact_D_projection_required',
                'complete_response_Gram_certified_under_inherited_hypotheses',
                'direct_K_model_error_certified_under_inherited_hypotheses'):
        require(actual[key] is True, 'missing positive receipt field: ' + key)
    for key in ('W9_norm_certified', 'Q_D_certified', 'whole_W9_residual_energy_certified',
                'new_A9_A11_certificate_closed'):
        require(actual[key] is False, 'scope promoted: ' + key)
    require(actual['external_review_open'] is True, 'external review scope changed')
    scoped = {k: v for k, v in actual.items() if k != 'incoming_full_replay_rerun_in_this_invocation'}
    match(scoped, {k: v for k, v in expected.items() if k != 'incoming_full_replay_rerun_in_this_invocation'})


def check_catalog(catalog):
    rows = catalog['archives']
    require(len(rows) == 1 and next(iter(rows.values()))['sha256'] == SEALED_ARCHIVE, 'archive identity differs')
    require(catalog['nested_original_function_archive']['sha256'] == NESTED_FUNCTIONS, 'nested function archive differs')
    require(catalog['frozen_response_rule']['sha256'] == FROZEN_RESPONSE, 'frozen response rule differs')
    spec = next(iter(rows.values()))['members']
    require(spec[catalog['nested_original_function_archive']['member']]['sha256'] == NESTED_FUNCTIONS, 'nested member hash differs')
    require(spec[catalog['frozen_response_rule']['member']]['sha256'] == FROZEN_RESPONSE, 'frozen member hash differs')


def run(out, full_input=False):
    require(__debug__, 'Run without optimization flags')
    out = out.resolve()
    require(not out.exists() and not out.is_relative_to(REPO), 'output must be new and outside repository')
    path = PACKAGE/'SOURCE_BINDINGS.json'
    require(digest(path) == (PACKAGE/'SOURCE_BINDINGS.sha256').read_text().split()[0], 'catalog hash differs')
    catalog = json.loads(path.read_bytes())
    check_catalog(catalog)
    for name, row in catalog['archives'].items(): archive(safe(PACKAGE, name), row)
    for name, row in catalog['visible_copies'].items():
        with zipfile.ZipFile(safe(PACKAGE, row['archive'])) as z:
            require(safe(PACKAGE, name).read_bytes() == z.read(row['member']), 'visible original differs: ' + name)
    out.mkdir(parents=True)
    chosen = catalog['replay_archive']; spec = catalog['archives'][chosen]
    work = out/'original'
    with zipfile.ZipFile(safe(PACKAGE, chosen)) as z:
        for member in spec['members']:
            target = safe(work, member); target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(member))
    original = safe(work, catalog['package_root'])
    result = out/'sealed-output'
    cmd = [sys.executable, '-B', '-X', 'utf8', str(original/'verify.py'), '--output', str(result)]
    if full_input: cmd.append('--full-input')
    execute(cmd, out/'sealed-verify.log')
    actual = json.loads((result/'RECEIPT.json').read_bytes())
    expected = json.loads((PACKAGE/'reports/EXPECTED_RECEIPT.json').read_bytes())
    check_receipt(actual, expected)
    receipt = {'status': 'PASS_WHOLE_RESPONSE_GRAM_REPLAY', 'archive': SEALED_ARCHIVE,
               'original_members_verified': len(spec['members']),
               'byte_identical_visible_copies': len(catalog['visible_copies']),
               'sealed_receipt': actual, 'incoming_full_replay_rerun': full_input,
               'W9_energy_computed': False, 'analytic_proof_machine_verified': False,
               'external_mathematical_review_open': True}
    (out/'WHOLE_RESPONSE_GRAM_REPLAY.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(receipt, indent=2))
    return receipt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--full-input', action='store_true')
    a = ap.parse_args()
    run(a.output, a.full_input)


if __name__ == '__main__':
    main()
