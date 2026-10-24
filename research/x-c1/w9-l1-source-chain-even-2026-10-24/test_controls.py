"""Adversarial controls for receipt, original input binding and replay results."""
from pathlib import Path
import copy
import json
import os
import subprocess
import shutil
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
import verify


class Controls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='objekt-x-l1-controls-')
        cls.work = Path(cls.temp.name)
        cls.members = verify.read_archive(verify.ROOT / verify.ARCHIVE)
        cls.author = cls.work / 'author'
        for name, raw in cls.members.items():
            p = cls.author / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def run_original(self):
        return subprocess.run([sys.executable, '-B', str(self.author / 'verify_chain.py'),
                               '--bindings', str(self.author / 'SOURCE_BINDINGS.json'),
                               '--output', str(self.work / 'MUST-NOT-EXIST.json')],
                              capture_output=True, text=True, timeout=60)

    def test_missing_original_input_is_rejected(self):
        p = self.author / 'inputs/old_fields.py'
        raw = p.read_bytes()
        try:
            p.unlink()
            run = self.run_original()
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('FileNotFoundError', run.stderr)
            self.assertFalse((self.work / 'MUST-NOT-EXIST.json').exists())
        finally:
            p.write_bytes(raw)

    def test_changed_original_input_is_rejected(self):
        p = self.author / 'inputs/old_fields.py'
        raw = p.read_bytes()
        try:
            p.write_bytes(raw + b'\n# altered control\n')
            run = self.run_original()
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('Source changed: old_fields', run.stderr)
            self.assertFalse((self.work / 'MUST-NOT-EXIST.json').exists())
        finally:
            p.write_bytes(raw)

    def test_archive_byte_change_rejected(self):
        p = self.work / 'changed.zip'
        raw = bytearray(verify.archive_bytes(verify.ROOT / verify.ARCHIVE))
        raw[-1] ^= 1
        p.write_bytes(raw)
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            verify.read_archive(p)

    def test_missing_chunk_rejected(self):
        root = self.work / 'missing-chunk-package'
        shutil.copytree(verify.ROOT, root)
        spec = verify.parse((root / 'AUTHOR_ARCHIVE_CHUNKS.json').read_bytes())
        (root / spec['chunks'][0]['path']).unlink()
        with self.assertRaises(FileNotFoundError):
            verify.read_archive(root / verify.ARCHIVE)

    def test_reordered_chunks_rejected(self):
        root = self.work / 'reordered-chunk-package'
        shutil.copytree(verify.ROOT, root)
        path = root / 'AUTHOR_ARCHIVE_CHUNKS.json'
        spec = verify.parse(path.read_bytes())
        spec['chunks'][0], spec['chunks'][1] = spec['chunks'][1], spec['chunks'][0]
        path.write_text(json.dumps(spec))
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            verify.read_archive(root / verify.ARCHIVE)

    def test_readable_copy_cannot_change_silently(self):
        p = self.work / 'copy-package'
        (p / 'author-text').mkdir(parents=True)
        (p / 'author-text/L1-BEWEIS.txt').write_bytes(self.members['L1-BEWEIS.txt'] + b' altered')
        with self.assertRaisesRegex(ValueError, 'Author copy differs'):
            verify.check_copies(p, self.members)

    def test_changed_result_is_rejected(self):
        expected = verify.parse(self.members['RESULT.json'])
        altered = copy.deepcopy(expected)
        altered['new_integration'] = True
        with self.assertRaisesRegex(ValueError, 'result differs'):
            verify.compare_result(altered, expected)

    def test_unsafe_archive_names_rejected(self):
        for name in ('../outside', '/outside', 'C:/outside', 'a\\b', 'a/../b'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                verify.safe_name(name)

    def test_output_cannot_overwrite_evidence(self):
        with self.assertRaisesRegex(ValueError, 'outside'):
            verify.output_path(verify.ROOT / 'evidence/FRESH-RESULT.json', verify.ROOT)
        p = self.work / 'existing.json'
        p.write_text('keep')
        with self.assertRaisesRegex(ValueError, 'overwrite'):
            verify.output_path(p, verify.ROOT)

    def test_optimized_mode_is_rejected(self):
        for flag in ('-O', '-OO'):
            run = subprocess.run([sys.executable, '-B', flag, str(verify.ROOT / 'verify.py')],
                                 capture_output=True, text=True, timeout=30)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn('Optimized Python', run.stderr)


if __name__ == '__main__':
    if sys.flags.optimize:
        raise SystemExit('Optimized Python is not a supported audit mode')
    unittest.main(verbosity=2)
