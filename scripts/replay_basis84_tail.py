"""Replay both sealed Tail84 packages with full original source and pivot checks."""
from pathlib import Path
import argparse, importlib.util, json, sys, zipfile
from replay_a9_sealed import archive, digest, execute, match, require, safe

REPO = Path(__file__).resolve().parents[1]
PACKAGE = REPO/'research/x-c1/basis84-tail-closure-2026-10-14'
PREVIOUS = REPO/'research/x-c1/a8-a9-global-closure-2026-10-13'
SCHUR = '65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba'
BASIS = 'dd0e30a27d66f38503b217fa3279f62173ee1360eeca06eb5fdb698c7deeaec5'
SEALED_ARCHIVES = {
    'author': 'aaa21cb4cbab92f10c128b7709b011ca51b68cb0b53f2738b2eb64597701d818',
    'countercheck': 'ab90bab116e16cbf4206c7be0dcba52628d4ea7d4b1dd00b0bb77acfcf0dcbac',
}


def check_historical_archives(catalog):
    rows = list(catalog['archives'].values())
    require(len(rows) == len(SEALED_ARCHIVES), 'historical archive count differs')
    require({row['role']: row['sha256'] for row in rows} == SEALED_ARCHIVES,
            'historical archive identity differs')


def check_receipt(actual, full, independent):
    require(actual['status'] == 'PASS_CONDITIONAL_TAIL_COUNTERCHECK', 'countercheck failed')
    match(actual['current_original_checker'], full)
    match(actual['mathematical_checks'], independent['mathematical_checks'])
    match(actual['current_response_to_original_basis_chain'], independent['current_response_to_original_basis_chain'])
    require(actual['current_response_to_original_basis_chain'] is not None, 'missing source chain')
    require(full['fresh_inverse_replay']['new_complete_positive_LDL_pivots'] == 574, 'missing full pivot replay')
    require(sum(c['exact_basis_null_relations'] for c in full['cases']) == 1344, 'missing basis relations')
    require(actual['large_integrations_rerun'] is False and actual['external_mathematical_review_open'] is True,
            'incorrect review scope')


def predecessor_sources(out):
    path = PREVIOUS/'SOURCE_BINDINGS.json'
    require(digest(path) == (PREVIOUS/'SOURCE_BINDINGS.sha256').read_text().split()[0], 'predecessor catalog changed')
    catalog = json.loads(path.read_bytes())
    selected = {}; active = set()
    def include(h):
        require(h not in active, 'cyclic predecessor')
        if h in selected: return
        active.add(h)
        obj = catalog['objects'][h]
        for edge in obj.get('nested_sources', []): include(edge['container'])
        selected[h] = obj
        active.remove(h)
    include(SCHUR); include(BASIS)
    spec = importlib.util.spec_from_file_location('tail_predecessor_replay', PREVIOUS/'replay.py')
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    subset = {'objects': selected, 'imports': [], 'visible_copies': {}, 'standalone': []}
    return module.materialize(subset, out/'predecessors', package=PREVIOUS)


def run(out):
    require(__debug__, 'Run without optimization flags')
    out = out.resolve()
    require(not out.exists() and not out.is_relative_to(REPO), 'output must be new and outside repository')
    out.mkdir(parents=True)
    path = PACKAGE/'SOURCE_BINDINGS.json'
    require(digest(path) == (PACKAGE/'SOURCE_BINDINGS.sha256').read_text().split()[0], 'catalog hash differs')
    catalog = json.loads(path.read_bytes())
    check_historical_archives(catalog)
    for name, row in catalog['archives'].items(): archive(safe(PACKAGE, name), row)
    for name, row in catalog['visible_copies'].items():
        with zipfile.ZipFile(safe(PACKAGE, row['archive'])) as z:
            require(safe(PACKAGE, name).read_bytes() == z.read(row['member']), 'visible original differs')
    chosen = catalog['replay_archive']; spec = catalog['archives'][chosen]
    work = out/'original'
    with zipfile.ZipFile(safe(PACKAGE, chosen)) as z:
        for member in spec['members']:
            target = safe(work, member); target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(member))
    original = safe(work, catalog['package_root'])
    sources = predecessor_sources(out)
    receipt = out/'FULL_TAIL_REPLAY.json'
    execute([sys.executable, '-B', '-X', 'utf8', str(original/'verify.py'), '--full-source-replay',
             '--schur-package', str(sources[SCHUR]), '--basis-package', str(sources[BASIS]),
             '--output', str(receipt)], out/'full-tail-replay.log')
    actual = json.loads(receipt.read_bytes())
    full = json.loads((PACKAGE/'reports/EXPECTED_FULL_SOURCE_REPLAY.json').read_bytes())
    independent = json.loads((PACKAGE/'reports/EXPECTED_INDEPENDENT_AUDIT.json').read_bytes())
    check_receipt(actual, full, independent)
    result = {'status':'PASS_BOTH_BASIS84_TAIL_PACKAGES',
              'archives':{row['role']:row['sha256'] for row in catalog['archives'].values()},
              'original_members_verified':sum(len(row['members']) for row in catalog['archives'].values()),
              'byte_identical_visible_copies':len(catalog['visible_copies']),
              'original_schur_sha256':SCHUR, 'original_basis_sha256':BASIS,
              'full_inverse_pivots_recomputed':574, 'exact_basis_relations':1344,
              'independent_math_fields_and_source_chain_match':True,
              'large_integrations_rerun':False, 'analytic_proof_machine_verified':False,
              'external_mathematical_review_open':True}
    data = (json.dumps(result, indent=2)+'\n').encode('utf-8')
    (out/'ACCEPTANCE.json').write_bytes(data)
    expected = PACKAGE/'reports/ACCEPTANCE.json'
    if expected.exists(): match(result, json.loads(expected.read_bytes()))
    print(data.decode('utf-8'))
    return result


if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--output', type=Path, required=True)
    run(ap.parse_args().output)
