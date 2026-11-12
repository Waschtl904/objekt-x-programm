"""Reject concrete publication corruptions and unjustified status promotions."""
from pathlib import Path
from copy import deepcopy
import hashlib, json, os, shutil, tempfile, unittest
from unittest.mock import patch
import verify_integration as checker
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

class PackageControls(unittest.TestCase):
    """Exercise the public verifier even when an editor refreshes MANIFEST.json."""

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='objx-guards-')
        self.addCleanup(self.temporary.cleanup)
        self.work = Path(self.temporary.name)
        self.root = self.work / 'package'
        shutil.copytree(ROOT, self.root)

    def replace(self, name, raw):
        (self.root / name).write_bytes(raw)
        manifest = json.loads((self.root / 'MANIFEST.json').read_bytes())
        manifest['files'][name] = {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
        (self.root / 'MANIFEST.json').write_text(json.dumps(manifest), encoding='utf-8')

    def replace_json(self, name, value):
        self.replace(name, json.dumps(value, ensure_ascii=False).encode('utf-8'))

    def reject(self, message, root=None, replay=False):
        with patch.object(checker.subprocess, 'run') as execute:
            with self.assertRaisesRegex(ValueError, message):
                verify(root=self.root if root is None else root, replay=replay)
            execute.assert_not_called()

    def directory_link(self, target, link):
        if os.name == 'nt':
            # A real Windows directory reparse point; no administrator privilege.
            import _winapi
            _winapi.CreateJunction(str(target), str(link))
            self.addCleanup(os.rmdir, link)
        else:
            link.symlink_to(target, target_is_directory=True)
            self.addCleanup(link.unlink)

    def file_link(self, target, link):
        try:
            link.symlink_to(target)
        except OSError as error:
            if os.name == 'nt' and error.winerror == 1314:
                self.skipTest('Windows does not grant file-symlink privilege')
            raise
        self.addCleanup(link.unlink)

    def test_unchanged_package_passes(self):
        self.assertEqual(verify(root=self.root, replay=False)['status'], 'INTEGRATION_BINDINGS_PASS')

    def test_expected_file_cannot_escape_package_root(self):
        outside = self.work / 'outside.txt'
        outside.write_bytes(b'outside')
        with self.assertRaisesRegex(ValueError, 'escapes package root'):
            identity(outside, {'bytes': 7, 'sha256': hashlib.sha256(b'outside').hexdigest()}, self.root)

    def test_each_historical_integration_field_is_pinned(self):
        original = json.loads((self.root / 'SCOPE.json').read_bytes())
        for key, value in [('GPT1_scope_review', 'APPROVED'),
                           ('public_push_authorized', True), ('merge_authorized', True),
                           ('public_push_authorized', 0), ('merge_authorized', 0)]:
            with self.subTest(field=key, value=value):
                altered = deepcopy(original)
                altered['integration'][key] = value
                self.replace_json('SCOPE.json', altered)
                self.reject('Historical integration')
        for key in original['integration']:
            with self.subTest(removed=key):
                altered = deepcopy(original)
                del altered['integration'][key]
                self.replace_json('SCOPE.json', altered)
                self.reject('Historical integration')

    def test_each_missing_original_cannot_be_removed_or_rewritten(self):
        original = json.loads((self.root / 'SOURCE_INDEX.json').read_bytes())
        for position, record in enumerate(original['missing_originals']):
            with self.subTest(removed=position):
                altered = deepcopy(original)
                del altered['missing_originals'][position]
                self.replace_json('SOURCE_INDEX.json', altered)
                self.reject('Missing-original records')
            for key in record:
                with self.subTest(position=position, field=key):
                    altered = deepcopy(original)
                    altered['missing_originals'][position][key] = 'ALTERED'
                    self.replace_json('SOURCE_INDEX.json', altered)
                    self.reject('Missing-original records')

    def test_each_native_narrative_entry_is_pinned(self):
        name = 'NATIVE_PROVENANCE.md'
        original = (self.root / name).read_text(encoding='utf-8')
        lead, *sections = original.split('\n## ')
        self.assertEqual(len(sections), 3)
        for position in range(3):
            with self.subTest(removed=position):
                self.replace(name, (lead + ''.join('\n## ' + s for i, s in enumerate(sections)
                                                   if i != position)).encode('utf-8'))
                self.reject('Byte identity')
            with self.subTest(changed=position):
                changed = list(sections)
                changed[position] = changed[position].replace('Erwarteter SHA256:', 'Geschlossen:', 1)
                self.replace(name, (lead + ''.join('\n## ' + s for s in changed)).encode('utf-8'))
                self.reject('Byte identity')

    def test_native_machine_record_cannot_be_omitted_from_source_index(self):
        name = 'originals/gpt2-second-column-2026-11-11/NATIVE_BINDING_RESULT.json'
        index = json.loads((self.root / 'SOURCE_INDEX.json').read_bytes())
        records = index['readable_originals']
        position = next(i for i, record in enumerate(records) if record['target'] == name)
        # Keep the old count of 34 to exercise more than the count check.
        records[position] = deepcopy(records[0])
        original_index = (self.root / 'SOURCE_INDEX.json').read_bytes()
        self.replace_json('SOURCE_INDEX.json', index)
        self.reject('Native source-index')
        self.replace('SOURCE_INDEX.json', original_index)
        native = json.loads((self.root / name).read_bytes())
        for position in range(3):
            with self.subTest(removed=position):
                altered = deepcopy(native)
                del altered['files'][position]
                self.replace_json(name, altered)
                self.reject('Byte identity')
            with self.subTest(closed=position):
                altered = deepcopy(native)
                altered['files'][position]['matches_expected'] = True
                self.replace_json(name, altered)
                self.reject('Byte identity')

    def test_package_root_link_is_rejected(self):
        link = self.work / 'linked-package'
        self.directory_link(self.root, link)
        self.reject('Link/reparse', root=link)

    def test_package_ancestor_link_is_rejected(self):
        parent = self.work / 'parent'
        parent.mkdir()
        # Only this test's temporary package is moved.
        self.root.rename(parent / 'package')
        link = self.work / 'linked-parent'
        self.directory_link(parent, link)
        self.reject('Link/reparse', root=link / 'package')

    def test_expected_directory_link_is_rejected(self):
        target = self.work / 'external-originals'
        (self.root / 'originals').rename(target)
        self.directory_link(target, self.root / 'originals')
        self.reject('Link/reparse')

    def test_unlisted_directory_link_is_rejected(self):
        target = self.work / 'extra'
        target.mkdir()
        (target / 'extra.txt').write_text('not in manifest', encoding='utf-8')
        self.directory_link(target, self.root / 'unlisted-link')
        self.reject('Link/reparse')

    def test_file_symlink_is_rejected(self):
        name = 'SCOPE.json'
        target = self.work / name
        (self.root / name).rename(target)
        self.file_link(target, self.root / name)
        self.reject('Link/reparse')

    def test_dangling_symlink_is_rejected(self):
        self.file_link(self.work / 'missing.txt', self.root / 'dangling-link')
        self.reject('Link/reparse')

    def test_manifest_symlink_is_rejected_before_reading(self):
        target = self.work / 'manifest.json'
        (self.root / 'MANIFEST.json').rename(target)
        self.file_link(target, self.root / 'MANIFEST.json')
        self.reject('Link/reparse')

    def test_replay_root_cannot_redirect_script_execution(self):
        original = json.loads((self.root / 'SOURCE_INDEX.json').read_bytes())
        for value in ('', '..', '../outside', '/tmp/outside', 'C:/outside',
                      str(self.work / 'outside'), 'different-member-root'):
            with self.subTest(root=value):
                altered = deepcopy(original)
                record = next(a for a in altered['archives'] if a['id'] == 'gpt2-second-column-2026-11-11')
                record['original_root'] = value
                self.replace_json('SOURCE_INDEX.json', altered)
                self.reject('Scalar replay root', replay=True)

    def test_changed_script_archive_is_rejected_before_execution(self):
        index = json.loads((self.root / 'SOURCE_INDEX.json').read_bytes())
        record = next(a for a in index['archives'] if a['id'] == 'gpt2-second-column-2026-11-11')
        raw = (self.root / record['target']).read_bytes() + b'changed'
        self.replace(record['target'], raw)
        record['sha256'] = hashlib.sha256(raw).hexdigest()
        record['bytes'] = len(raw)
        self.replace_json('SOURCE_INDEX.json', index)
        self.reject('Original source hash', replay=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
