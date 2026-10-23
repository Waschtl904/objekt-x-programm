"""Negative checks for the publication layer; inherited controls remain separate."""
import sys
if not __debug__:
    raise SystemExit('Python -O/-OO is rejected')
sys.dont_write_bytecode = True
import copy
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import verify as v

class Controls(unittest.TestCase):
    def test_optimized_modes(self):
        for mode in ('-O', '-OO'):
            p = subprocess.run([sys.executable, '-B', mode, str(v.HERE / 'verify.py')], capture_output=True, text=True)
            self.assertNotEqual(p.returncode, 0)
            self.assertIn('rejected', p.stderr)

    def test_bound_source_change(self):
        with self.assertRaises(ValueError):
            v.check_bytes(b'changed', v.digest(b'original'), 'source')

    def test_missing_bound_source(self):
        with tempfile.TemporaryDirectory() as t:
            with self.assertRaises(FileNotFoundError):
                v.bound_path(Path(t), 'missing').read_bytes()

    def test_escaping_source_path(self):
        for name in ('../source', '/source', 'a\\b'):
            with self.assertRaises(ValueError):
                v.bound_path(v.HERE, name)

    def test_l1_cannot_close(self):
        scope = v.read(v.HERE / 'STATUS.json'); scope['L1']['status'] = 'PASS'
        with self.assertRaises(ValueError):
            v.check_scope(scope)

    def test_l1_cannot_shrink_to_low_coordinates(self):
        scope = v.read(v.HERE / 'STATUS.json'); scope['L1']['includes'] = ['H-SOURCE']
        with self.assertRaises(ValueError):
            v.check_scope(scope)

    def test_changed_result_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / 'package'; shutil.copytree(v.HERE, root)
            path = root / 'finite-audit/evidence/cache-price.json'
            path.write_bytes(path.read_bytes() + b' ')
            with self.assertRaisesRegex(ValueError, 'Bound bytes differ'):
                v.check_package(root)

    def test_bad_exponent_rejected_by_rational_bound(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / 'package'; shutil.copytree(v.HERE, root)
            path = root / 'finite-audit/evidence/rational-cross-audit.json'
            value = v.read(path); value['repaired_Ldual_energy_upper'] = '4.632e+11'
            path.write_text(json.dumps(value))
            with self.assertRaisesRegex(ValueError, 'Numeric cap failed'):
                v.canonical_numbers(root)

if __name__ == '__main__':
    unittest.main(verbosity=2)
