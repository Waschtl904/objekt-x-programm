"""Technical controls for the publication wrapper, without mathematical changes."""
import sys
if sys.flags.optimize:
    sys.stderr.write('OBJEKT_X_PUBLICATION_OPTIMIZED_PYTHON_REJECTED\n')
    raise SystemExit(78)
sys.dont_write_bytecode = True
from pathlib import Path
import json
import os
import shutil
import subprocess
import tempfile
import unittest
import verify as v


class Controls(unittest.TestCase):
    def test_guards(self):
        for program in ('verify.py', 'test_controls.py'):
            for flags, opt in ((['-O'], None), (['-OO'], None), ([], '1'), ([], '2')):
                env = dict(os.environ)
                env.pop('PYTHONOPTIMIZE', None)
                if opt is not None:
                    env['PYTHONOPTIMIZE'] = opt
                p = subprocess.run([sys.executable, '-S', '-B', *flags, str(v.HERE / program)],
                                   env=env, capture_output=True, text=True, timeout=10)
                self.assertEqual(p.returncode, 78)
                self.assertEqual(p.stdout, '')
                self.assertEqual(p.stderr, 'OBJEKT_X_PUBLICATION_OPTIMIZED_PYTHON_REJECTED\n')

    def test_missing_and_changed_chunks(self):
        entries = v.parse((v.HERE / 'ARCHIVES.json').read_bytes())['archives']
        maps = v.parse((v.HERE / 'ARCHIVE_CHUNKS.json').read_bytes())
        entry = next(e for e in entries if e['sha256'] == v.REVISION)
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            (root / 'ARCHIVE_CHUNKS.json').write_text(json.dumps(maps))
            with self.assertRaises(FileNotFoundError):
                v.archive_bytes(root, entry)
            first = root / maps[entry['path']]['chunks'][0]['path']
            first.parent.mkdir(parents=True)
            first.write_bytes(b'changed')
            with self.assertRaisesRegex(ValueError, 'Chunk hash'):
                v.archive_bytes(root, entry)

    def test_reordered_chunks(self):
        entry = next(e for e in v.parse((v.HERE / 'ARCHIVES.json').read_bytes())['archives']
                     if e['sha256'] == v.REVISION)
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            maps = v.parse((v.HERE / 'ARCHIVE_CHUNKS.json').read_bytes())
            for part in maps[entry['path']]['chunks']:
                p = root / part['path']
                p.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(v.HERE / part['path'], p)
            chunks = maps[entry['path']]['chunks']
            chunks[0], chunks[1] = chunks[1], chunks[0]
            (root / 'ARCHIVE_CHUNKS.json').write_text(json.dumps(maps))
            with self.assertRaisesRegex(ValueError, 'Archive identity'):
                v.archive_bytes(root, entry)

    def test_changed_publication_binding(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            (root / 'bound.txt').write_bytes(b'altered')
            (root / 'MANIFEST.json').write_text(json.dumps({'bound.txt': v.sha(b'original')}))
            with self.assertRaisesRegex(ValueError, 'Package hash'):
                v.manifest(root)

    def test_l1_head_cannot_change(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            (root / 'L1_REFERENCE.json').write_text(json.dumps({'publication_head': '0' * 40}))
            with self.assertRaisesRegex(ValueError, 'L1 head changed'):
                v.l1_dependency(root, root)

    def test_unsafe_paths(self):
        for name in ('../out', '/out', 'a\\b', 'C:/out'):
            with self.assertRaises(ValueError):
                v.safe(name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
