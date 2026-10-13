"""Adversarial tests of source preservation and replay failure propagation."""
from pathlib import Path
import copy
import fnmatch
import hashlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
import replay

def digest(raw): return hashlib.sha256(raw).hexdigest()

class PreservationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.package = self.root/'package'; self.package.mkdir()
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w') as z: z.writestr('original.txt', b'exact\r\nbytes\n')
        self.raw = buf.getvalue(); self.h = digest(self.raw)
        part = self.package/'chunk.bin'; part.write_bytes(self.raw)
        self.spec = {'sha256':self.h, 'name':'original.zip', 'bytes':len(self.raw),
                     'chunks':[{'path':'chunk.bin','bytes':len(self.raw),'sha256':self.h}],
                     'members':[{'name':'original.txt','bytes':13,'sha256':digest(b'exact\r\nbytes\n')}]}
        self.catalog = {'objects':{self.h:self.spec},
                        'imports':[{'name':'original.zip','bytes':len(self.raw),'sha256':self.h}],
                        'visible_copies':{}, 'standalone':[]}

    def tearDown(self): self.temp.cleanup()

    def run_catalog(self, catalog=None):
        return replay.materialize(catalog or self.catalog, self.root/'out', self.package)

    def test_original_bytes_preserved(self):
        paths = self.run_catalog()
        self.assertEqual(paths[self.h].read_bytes(), self.raw)
        self.assertEqual((self.root/'out/originals/original.zip').read_bytes(), self.raw)

    def test_corrupted_chunk_rejected(self):
        raw = bytearray(self.raw); raw[20] ^= 1
        (self.package/'chunk.bin').write_bytes(raw)
        with self.assertRaisesRegex(ValueError,'chunk mismatch'): self.run_catalog()

    def test_incomplete_member_catalog_rejected(self):
        self.spec['members'] = []
        with self.assertRaisesRegex(ValueError,'member catalog'): self.run_catalog()

    def test_wrong_member_hash_rejected(self):
        self.spec['members'][0]['sha256'] = '0'*64
        with self.assertRaisesRegex(ValueError,'member hash'): self.run_catalog()

    def test_wrong_archive_length_rejected(self):
        self.spec['bytes'] += 1
        with self.assertRaisesRegex(ValueError,'archive bytes differ'): self.run_catalog()

    def test_unsafe_paths_rejected(self):
        for path in ['../escape','/absolute','a/../b','a//b','C:drive','a\\b','']:
            with self.subTest(path=path), self.assertRaises(ValueError):
                replay.safe_path(self.root,path)

    def test_missing_parent_rejected(self):
        del self.spec['chunks']
        self.spec['nested_sources']=[{'container':'0'*64,'member':'file.zip'}]
        with self.assertRaisesRegex(ValueError,'missing or cyclic'): self.run_catalog()

    def test_cyclic_parent_rejected(self):
        del self.spec['chunks']
        self.spec['nested_sources']=[{'container':self.h,'member':'file.zip'}]
        with self.assertRaisesRegex(ValueError,'missing or cyclic'): self.run_catalog()

    def test_changed_readable_copy_rejected(self):
        (self.package/'copy.txt').write_bytes(b'wrong')
        self.catalog['visible_copies']['copy.txt']={
            'bytes':13,'sha256':digest(b'exact\r\nbytes\n'),
            'container_sha256':self.h,'member':'original.txt'}
        with self.assertRaisesRegex(ValueError,'readable copy'): self.run_catalog()

    def test_failed_checker_rejected(self):
        with self.assertRaisesRegex(ValueError,'checker failed'):
            replay.execute([sys.executable,'-c','print("PASS"); raise SystemExit(7)'],
                           self.root/'failure.log','PASS')

    def test_missing_completion_marker_rejected(self):
        with self.assertRaisesRegex(ValueError,'completion marker'):
            replay.execute([sys.executable,'-c','print("started")'],self.root/'early.log','PASS')

    def test_ci_routing(self):
        rel = replay.HERE.relative_to(replay.REPO).as_posix()
        workflow = '.github/workflows/a8-a9-global-closure.yml'
        text = (replay.REPO/workflow).read_text()
        patterns = [rel+'/**',workflow]
        actual = [line.strip()[3:-1] for line in text.splitlines() if line.strip().startswith('- "')]
        self.assertEqual(actual,patterns+patterns)
        routed = lambda p:any(fnmatch.fnmatchcase(p,x) for x in patterns)
        for p in [rel+'/replay.py',rel+'/archive-chunks/hash/000.bin',rel+'/PROOF.md',workflow]:
            self.assertTrue(routed(p))
        for p in ['README.md','00-uebersicht/RESEARCH_STATE.yaml','research/unrelated/file.py']:
            self.assertFalse(routed(p))
        self.assertIn('pull_request:',text)
        self.assertIn('branches: [main]',text)
        self.assertIn('github.event.pull_request.head.sha || github.sha',text)

if __name__ == '__main__': unittest.main()
