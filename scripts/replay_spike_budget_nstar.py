"""Replay the two sealed addendum packages bound to the A9 spike calibration:
the budget-direction (artefact) package of 2026-10-15 and the N*Jp source /
coefficient package of 2026-10-16. Only their own exact reconstructions are
rerun; historical integrations, the 574 pivots and the PR-226 LDL replay are not.
"""
from pathlib import Path
import argparse, json, sys, zipfile
from replay_a9_sealed import archive, digest, execute, match, require, safe

REPO = Path(__file__).resolve().parents[1]
PACKAGE = REPO/'research/x-c1/a9-inverse-spike-calibration-2026-10-15'
BUDGET_SHA = '7f7129945b38768a5ec88994b783211db1ceb0810129ffc4ea4ba7db5beb1f5e'
NSTAR_SHA = 'b48e3895d57cc5cc2c11ca170e32d6af5fbdfcde9948b4db7c370d3376b6d57b'
A9_INVERSE_SHA = 'a1fa41958d79ab16a7c42b12375c3373f5a86a99993ae2d23c984ff6b3b2e8ae'
GLOBAL_SHA = '2ca3c682de8a529b12a0d628c2b606fd04df332d1299ccd36dff71ac3e53d80c'


def check_budget_receipt(actual, expected):
    require(actual['status'] == 'PASS', 'budget checker did not pass')
    for key in ('new_directional_result_fresh_and_byte_equal', 'separate_check_fresh_and_byte_equal',
                'previous_fresh_original_pr226_replay_bound'):
        require(actual[key] is True, 'missing budget receipt field: ' + key)
    for key in ('full_A9_inverse_claim', 'A9_A11_closed'):
        require(actual[key] is False, 'budget scope promoted: ' + key)
    require(actual['external_review_open'] is True, 'budget review scope changed')
    scoped = {k: v for k, v in actual.items() if k != 'original_pr226_replay_executed_this_invocation'}
    match(scoped, {k: v for k, v in expected.items() if k != 'original_pr226_replay_executed_this_invocation'})


def check_nstar_receipt(actual, expected):
    require(actual['status'] == 'PASS', 'nstar checker did not pass')
    require(actual['spike_archive_sha256'] == BUDGET_SHA, 'nstar bound a different spike archive')
    require(actual['global_source_archive_sha256'] == GLOBAL_SHA, 'nstar bound a different global archive')
    c = actual['checks']
    require(c['positive_K_pivots'] == 24 and c['exact_Pv_components'] == 168 and c['exact_q_identities'] == 2
            and c['Jt_local_interval_coefficients'] == 384, 'nstar counts differ')
    for key in ('Nstar_Jt_function_integrals_computed', 'W9_exclusion_test_computed', 'A9_A11_closed'):
        require(actual[key] is False, 'nstar scope promoted: ' + key)
    match(actual, expected)


def check_catalog(catalog):
    rows = catalog['archives']
    require(rows[catalog['budget_archive']]['sha256'] == BUDGET_SHA, 'budget archive identity differs')
    require(rows[catalog['nstar_archive']]['sha256'] == NSTAR_SHA, 'nstar archive identity differs')
    require(catalog['identity_reconciliation']['identical'] is True, 'identity reconciliation not recorded')
    require(catalog['embedded_sources']['a9_inverse_archive'] == A9_INVERSE_SHA, 'embedded A9 inverse archive differs')
    require(catalog['embedded_sources']['global_gram_archive'] == GLOBAL_SHA, 'embedded global archive differs')


def extract(catalog, name, dest):
    spec = catalog['archives'][name]
    with zipfile.ZipFile(safe(PACKAGE, name)) as z:
        for member in spec['members']:
            target = safe(dest, member); target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(member))
    return safe(dest, spec['package_root'])


def run(out):
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
    budget_root = extract(catalog, catalog['budget_archive'], out/'budget')
    nstar_root = extract(catalog, catalog['nstar_archive'], out/'nstar')
    require(digest(budget_root/'inputs/Objekt-X-A9-Inverserneuerung-und-Hoher-Schurrest-2026-10-13.zip') == A9_INVERSE_SHA, 'embedded A9 inverse archive differs')
    execute([sys.executable, '-B', '-X', 'utf8', str(budget_root/'verify.py'), '--output', str(out/'budget-output')], out/'budget-verify.log')
    b_actual = json.loads((out/'budget-output/RECEIPT.json').read_bytes())
    check_budget_receipt(b_actual, json.loads((PACKAGE/'reports/EXPECTED_BUDGET_RECEIPT.json').read_bytes()))
    execute([sys.executable, '-B', '-X', 'utf8', str(nstar_root/'verify.py'), '--spike-archive', str(safe(PACKAGE, catalog['budget_archive'])),
             '--output', str(out/'nstar-output')], out/'nstar-verify.log')
    n_actual = json.loads((out/'nstar-output/RECEIPT.json').read_bytes())
    check_nstar_receipt(n_actual, json.loads((PACKAGE/'reports/EXPECTED_NSTAR_RECEIPT.json').read_bytes()))
    require((out/'nstar-output/DIRECTIONS.json').read_bytes() == (nstar_root/'expected/DIRECTIONS.json').read_bytes(), 'DIRECTIONS.json not byte-equal')
    receipt = {'status': 'PASS_SPIKE_BUDGET_AND_NSTAR_REPLAY', 'budget_archive': BUDGET_SHA, 'nstar_archive': NSTAR_SHA,
               'budget_receipt': b_actual, 'nstar_receipt': n_actual,
               'chi_integrals_computed': False, 'exclusion_test_computed': False, 'pr226_ldl_rerun_here': False,
               'external_mathematical_review_open': True}
    (out/'SPIKE_BUDGET_NSTAR_REPLAY.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(receipt, indent=2))
    return receipt


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', type=Path, required=True)
    run(ap.parse_args().output)


if __name__ == '__main__':
    main()
