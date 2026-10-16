"""Receipt and catalog guards for the spike budget / N*Jp addendum replay."""
from pathlib import Path
import copy, json, sys, unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import replay_spike_budget_nstar as replay


class SpikeBudgetNstarTests(unittest.TestCase):
    def setUp(self):
        self.b = json.loads((replay.PACKAGE/'reports/EXPECTED_BUDGET_RECEIPT.json').read_bytes())
        self.n = json.loads((replay.PACKAGE/'reports/EXPECTED_NSTAR_RECEIPT.json').read_bytes())
        self.catalog = json.loads((replay.PACKAGE/'SOURCE_BINDINGS.json').read_bytes())

    def test_expected_receipts_accepted(self):
        replay.check_budget_receipt(copy.deepcopy(self.b), self.b)
        replay.check_nstar_receipt(copy.deepcopy(self.n), self.n)

    def test_budget_scope_guarded(self):
        a = copy.deepcopy(self.b); a['full_A9_inverse_claim'] = True
        with self.assertRaisesRegex(ValueError, 'scope promoted'): replay.check_budget_receipt(a, self.b)

    def test_nstar_scope_guarded(self):
        for key in ('Nstar_Jt_function_integrals_computed', 'W9_exclusion_test_computed', 'A9_A11_closed'):
            a = copy.deepcopy(self.n); a[key] = True
            with self.assertRaisesRegex(ValueError, 'scope promoted'): replay.check_nstar_receipt(a, self.n)

    def test_nstar_counts_guarded(self):
        a = copy.deepcopy(self.n); a['checks']['positive_K_pivots'] = 23
        with self.assertRaises(ValueError): replay.check_nstar_receipt(a, self.n)

    def test_catalog_identity(self):
        replay.check_catalog(self.catalog)
        c = copy.deepcopy(self.catalog); c['archives'][c['budget_archive']]['sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError, 'budget archive identity'): replay.check_catalog(c)
        c = copy.deepcopy(self.catalog); c['identity_reconciliation']['identical'] = False
        with self.assertRaises(ValueError): replay.check_catalog(c)

    def test_catalog_hash_bound(self):
        self.assertEqual(replay.digest(replay.PACKAGE/'SOURCE_BINDINGS.json'),
                         (replay.PACKAGE/'SOURCE_BINDINGS.sha256').read_text().split()[0])

    def test_repository_output_rejected(self):
        with self.assertRaisesRegex(ValueError, 'output must be new'):
            replay.run(ROOT/'unsafe-spike-output')

    def test_ci_routing(self):
        wf = '.github/workflows/a9-inverse-spike-calibration.yml'
        raw = (ROOT/wf).read_text(encoding='utf-8')
        for p in ['scripts/replay_spike_budget_nstar.py', 'tests/test_spike_budget_nstar_replay.py']:
            self.assertIn(p, raw)


if __name__ == '__main__':
    unittest.main()
