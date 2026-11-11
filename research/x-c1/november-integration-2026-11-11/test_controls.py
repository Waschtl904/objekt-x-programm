"""Reject concrete publication corruptions and unjustified status promotions."""
from pathlib import Path
from copy import deepcopy
import hashlib, json, tempfile, unittest
from verify_integration import ROOT, identity, validate_scope, verify

class Controls(unittest.TestCase):
    def setUp(self):
        self.scope = json.loads((ROOT / 'SCOPE.json').read_bytes())

    def test_changed_original_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'original.txt'
            raw = (ROOT / 'originals/gpt2-run-2026-11-05/BERICHT.txt').read_bytes()
            record = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
            p.write_bytes(raw.replace(b'518,110', b'519,110', 1))
            with self.assertRaisesRegex(ValueError, 'Byte identity'):
                identity(p, record)

    def test_false_second_energy_or_reachability(self):
        for key in ('Qq_bound_achieved', 'Qq_reachability_proved'):
            s = deepcopy(self.scope); s['second_column'][key] = True
            with self.assertRaisesRegex(ValueError, 'Second-column promotion'):
                validate_scope(s)

    def test_native_contract_cannot_disappear(self):
        for section, key, value in [('native_bindings', 'resolved', True),
              ('second_column', 'native_X12_contract_conditional', False),
              ('budget', 'native_X12_ancestry_unresolved', False)]:
            s = deepcopy(self.scope); s[section][key] = value
            with self.assertRaisesRegex(ValueError, 'Native ancestry'):
                validate_scope(s)

    def test_start_review_is_not_result_review(self):
        self.scope['kernel_run']['result_review_original_available'] = True
        with self.assertRaisesRegex(ValueError, 'Start/result'):
            validate_scope(self.scope)

    def test_no_circular_A11_input_or_global_closure(self):
        for key in ('two_space_closed', 'point4_closed', 'new_physical_main_run_justified',
                    'historical_A11_positivity_used_as_input'):
            s = deepcopy(self.scope); s['overall'][key] = True
            with self.assertRaisesRegex(ValueError, 'Unjustified'):
                validate_scope(s)

    def test_extra_file_is_not_silently_published(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'MANIFEST.json').write_text('{"files":{}}', encoding='utf-8')
            (root / 'unlisted.txt').write_text('extra', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'exact file set'):
                verify(root=root, replay=False)

if __name__ == '__main__':
    unittest.main(verbosity=2)
