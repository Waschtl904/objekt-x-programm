"""Receipt and catalog guards for the sealed whole-response-Gram replay."""
from pathlib import Path
import copy, json, sys, unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import replay_whole_response_gram as replay


class WholeResponseGramReplayTests(unittest.TestCase):
    def setUp(self):
        self.expected = json.loads((replay.PACKAGE/'reports/EXPECTED_RECEIPT.json').read_bytes())
        self.actual = copy.deepcopy(self.expected)
        self.catalog = json.loads((replay.PACKAGE/'SOURCE_BINDINGS.json').read_bytes())

    def test_expected_receipt_accepted(self):
        replay.check_receipt(self.actual, self.expected)

    def test_full_input_flag_is_not_part_of_identity(self):
        self.actual['incoming_full_replay_rerun_in_this_invocation'] = True
        replay.check_receipt(self.actual, self.expected)

    def test_pivot_count_guarded(self):
        self.actual['positive_upper_Gram_pivots'] = 47
        with self.assertRaises(ValueError): replay.check_receipt(self.actual, self.expected)

    def test_gram_comparison_count_guarded(self):
        self.actual['exact_Gram_entry_comparisons'] = 575
        with self.assertRaises(ValueError): replay.check_receipt(self.actual, self.expected)

    def test_scope_cannot_be_promoted(self):
        for key in ('W9_norm_certified', 'Q_D_certified', 'whole_W9_residual_energy_certified', 'new_A9_A11_certificate_closed'):
            a = copy.deepcopy(self.expected); a[key] = True
            with self.assertRaisesRegex(ValueError, 'scope promoted'): replay.check_receipt(a, self.expected)

    def test_external_review_not_closed(self):
        self.actual['external_review_open'] = False
        with self.assertRaises(ValueError): replay.check_receipt(self.actual, self.expected)

    def test_catalog_identity(self):
        replay.check_catalog(self.catalog)
        c = copy.deepcopy(self.catalog); c['nested_original_function_archive']['sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError, 'nested function archive'): replay.check_catalog(c)
        c = copy.deepcopy(self.catalog); c['frozen_response_rule']['sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError, 'frozen response rule'): replay.check_catalog(c)

    def test_addendum_receipt_guards(self):
        exp = json.loads((replay.PACKAGE/'reports/EXPECTED_ADDENDUM_RECEIPT.json').read_bytes())
        replay.check_addendum_receipt(copy.deepcopy(exp), exp)
        a = copy.deepcopy(exp); a['lower_norm_substitution_rejected'] = False
        with self.assertRaises(ValueError): replay.check_addendum_receipt(a, exp)
        a = copy.deepcopy(exp); a['A9_A11_closed'] = True
        with self.assertRaisesRegex(ValueError, 'scope promoted'): replay.check_addendum_receipt(a, exp)

    def test_parity_constants(self):
        out = replay.check_parity_constants()
        self.assertIn('g_even_enclosure', out); self.assertIn('g_odd_enclosure', out)

    def test_addendum_identity_guarded(self):
        c = copy.deepcopy(self.catalog); c['archives'][c['addendum_archive']]['embeds_original_archive_sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError, 'embeds a different original'): replay.check_catalog(c)

    def test_catalog_hash_bound(self):
        self.assertEqual(replay.digest(replay.PACKAGE/'SOURCE_BINDINGS.json'),
                         (replay.PACKAGE/'SOURCE_BINDINGS.sha256').read_text().split()[0])

    def test_repository_output_rejected(self):
        with self.assertRaisesRegex(ValueError, 'output must be new'):
            replay.run(ROOT/'unsafe-response-gram-output')

    def test_ci_routing(self):
        wf = '.github/workflows/a9-a11-whole-response-gram.yml'
        raw = (ROOT/wf).read_text(encoding='utf-8')
        for p in ['research/x-c1/a9-a11-whole-response-gram-2026-10-15/**', 'scripts/replay_whole_response_gram.py',
                  'scripts/replay_a9_sealed.py', 'tests/test_whole_response_gram_replay.py', wf]:
            self.assertIn(p, raw)


if __name__ == '__main__':
    unittest.main()
