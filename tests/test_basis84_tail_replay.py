"""Require the full source/pivot run and preserve its mathematical scope."""
from pathlib import Path
import copy, fnmatch, json, sys, unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import replay_basis84_tail as replay


class TailReplayTests(unittest.TestCase):
    def setUp(self):
        p=ROOT/'research/x-c1/basis84-tail-closure-2026-10-14/reports'
        self.full=json.loads((p/'EXPECTED_FULL_SOURCE_REPLAY.json').read_bytes())
        self.independent=json.loads((p/'EXPECTED_INDEPENDENT_AUDIT.json').read_bytes())
        self.actual=copy.deepcopy(self.independent)
        self.actual['current_original_checker']=copy.deepcopy(self.full)
    def check(self): replay.check_receipt(self.actual,self.full,self.independent)
    def test_complete_receipt(self): self.check()
    def test_fast_replay_cannot_replace_full_run(self):
        self.actual['current_original_checker']['fresh_inverse_replay']=None
        with self.assertRaises(ValueError): self.check()
    def test_changed_basis_equation_count(self):
        self.actual['current_original_checker']['cases'][0]['exact_basis_null_relations']=671
        with self.assertRaises(ValueError): self.check()
    def test_missing_external_basis_comparison(self):
        self.actual['current_original_checker']['original_basis_archive_byte_comparison']=False
        with self.assertRaises(ValueError): self.check()
    def test_missing_independent_source_chain(self):
        self.actual['current_response_to_original_basis_chain']=None
        with self.assertRaises(ValueError): self.check()
    def test_changed_inverse_bound(self):
        self.actual['mathematical_checks']['cases'][0]['conditional_restriction_inverse_norm_upper']='20'
        with self.assertRaises(ValueError): self.check()
    def test_review_scope_not_promoted(self):
        self.actual['external_mathematical_review_open']=False
        with self.assertRaises(ValueError): self.check()
    def test_repository_output_rejected(self):
        with self.assertRaisesRegex(ValueError,'output must be new'):
            replay.run(ROOT/'unsafe-tail-output')
    def test_coordinated_catalog_archive_replacement_rejected(self):
        catalog={'archives':{'a':{'role':'author','sha256':replay.SEALED_ARCHIVES['author']},
                             'b':{'role':'countercheck','sha256':replay.SEALED_ARCHIVES['countercheck']}}}
        replay.check_historical_archives(catalog)
        catalog['archives']['b']['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'historical archive identity'):
            replay.check_historical_archives(catalog)
    def test_repeated_attempt_artifacts_have_distinct_names(self):
        text=(ROOT/'.github/workflows/basis84-tail-closure.yml').read_text(encoding='utf-8')
        self.assertIn('name: basis84-tail-check-${{ github.run_id }}-${{ github.run_attempt }}',text)
    def test_ci_routing(self):
        wf='.github/workflows/basis84-tail-closure.yml'
        patterns=['research/x-c1/basis84-tail-closure-2026-10-14/**',
                  'scripts/replay_basis84_tail.py','scripts/replay_a9_sealed.py',
                  'tests/test_basis84_tail_replay.py','tests/test_a9_sealed_replay.py',
                  'research/x-c1/a8-a9-global-closure-2026-10-13/**',wf]
        raw=(ROOT/wf).read_text(encoding='utf-8')
        got=[line.strip()[3:-1] for line in raw.splitlines() if line.strip().startswith('- "')]
        self.assertEqual(got,patterns+patterns)
        for p in [patterns[0][:-2]+'archives/source.zip',patterns[1],patterns[3],patterns[5][:-2]+'replay.py',wf]:
            self.assertTrue(any(fnmatch.fnmatchcase(p,x) for x in patterns))
        for p in ['README.md','00-uebersicht/RESEARCH_STATE.yaml','research/unrelated/input.json']:
            self.assertFalse(any(fnmatch.fnmatchcase(p,x) for x in patterns))


if __name__=='__main__': unittest.main()
