"""Adversarial routing tests in disposable Git repositories; no matrix build."""

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('a1_reuse', ROOT / 'scripts/a1_certificate_reuse.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def write(root, path, value):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(value, encoding='utf-8', newline='\n')


def save(root):
    r.git(root, 'add', '--all')
    r.git(root, 'commit', '-qm', 'fixture')
    return r.git(root, 'rev-parse', 'HEAD').decode().strip()


def dump(value):
    return json.dumps(value, indent=2) + '\n'


class CertificateReuseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shared = tempfile.TemporaryDirectory(prefix='a1-reuse-fixture-')
        root = cls.fixture = Path(cls.shared.name)
        r.git(root, 'init', '-q')
        r.git(root, 'config', 'user.name', 'Routing test')
        r.git(root, 'config', 'user.email', 'test@example.invalid')
        r.git(root, 'config', 'core.autocrlf', 'false')
        cls.workflow = 'name: Test\non:\n  pull_request:\njobs:\n' + ''.join(
            f'  {job}:\n    runs-on: ubuntu-24.04\n    steps:\n      - run: echo frozen\n'
            for job in r.JOBS)
        write(root, r.WORKFLOW, cls.workflow)
        write(root, 'scripts/certify_a1_c_even_exact_dyadic_matrix.py', 'PRECISION = 3072\n')
        write(root, 'scripts/check_a1_c_even_dyadic_budget_arb.py', 'EPS = "4e-43"\n')
        write(root, 'audits/P11_A1_C_EVEN_ENGINE.md', 'Frozen error assumptions\n')
        write(root, 'scripts/unrelated.py', 'unrelated = 1\n')
        write(root, 'research/x-c1/existing/code.py', 'existing = 1\n')
        write(root, 'tests/existing.py', '# existing independent test\n')
        cls.source = save(root)
        jobs = [{'id': i, 'name': name, 'run_id': 1, 'run_attempt': 1,
                 'head_sha': cls.source, 'status': 'completed', 'conclusion': 'success'}
                for i, name in enumerate(('a1-c-even-classify', 'a1-c-even-fresh-matrix-build',
                                          'a1-c-even-rigorous-ldl', 'a1-c-even-gate'), 1)]
        meta = {'repository': 'Waschtl904/objekt-x-programm',
                'run': {'id': 1, 'run_attempt': 1, 'head_sha': cls.source,
                        'path': r.WORKFLOW, 'event': 'pull_request',
                        'status': 'completed', 'conclusion': 'success'}, 'jobs': jobs}
        write(root, r.DIRECTORY + 'run.json', dump(meta))
        for name, statements in r.CERTIFICATES.items():
            write(root, r.DIRECTORY + name, ''.join('2026-10-19T16:00:00.000Z ' + s + '\n' for s in statements))
        entries = r.tree(root, cls.source)
        manifest = {'schema': 1, 'source_commit': cls.source, 'run_id': 1, 'run_attempt': 1,
                    'matrix_sha256': r.MATRIX, 'dependencies': r.bindings(root, entries),
                    'execution_contract_sha256': r.execution_contract(cls.workflow.encode()),
                    'evidence_sha256': {name: r.digest((root / r.DIRECTORY / name).read_bytes())
                                       for name in ('run.json', *r.CERTIFICATES)}}
        write(root, r.MANIFEST, dump(manifest))
        write(root, r.SCRIPT, '# trusted policy\n')
        write(root, r.TEST, '# trusted tests\n')
        cls.base = save(root)

    @classmethod
    def tearDownClass(cls):
        cls.shared.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='a1-reuse-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(self.fixture, self.root)

    def route(self, base=None, head=None, event='pull_request'):
        return r.classify(self.root, base or self.base,
                          head or r.git(self.root, 'rev-parse', 'HEAD').decode().strip(), event)

    def change(self, path, text):
        write(self.root, path, text)
        return save(self.root)

    def update_evidence(self, name, data):
        write(self.root, r.DIRECTORY + name, data)
        manifest = json.loads((self.root / r.MANIFEST).read_text())
        manifest['evidence_sha256'][name] = r.digest(data.encode())
        write(self.root, r.MANIFEST, dump(manifest))
        return save(self.root)

    def test_bound_unchanged_certificate_is_reused(self):
        self.assertEqual(self.route(), (False, 'bound-certificate-unchanged'))

    def test_bootstrap_cannot_authorize_its_own_policy(self):
        self.assertEqual(self.route(base=self.source), (True, 'reuse-policy-or-evidence-changed'))

    def test_w9_then_documentation_fix_in_same_pr_stays_fast(self):
        self.change('.github/workflows/w9-integration.yml', 'python-version: 3.12.14\n')
        self.assertFalse(self.route()[0])
        self.change('research/x-c1/w9-new/code.py', 'new_w9 = 1\n')
        self.assertFalse(self.route()[0])
        self.change('README.md', 'Documentation correction\n')
        self.assertFalse(self.route()[0])

    def test_existing_independent_script_change_is_fast(self):
        self.change('scripts/unrelated.py', 'unrelated = 2\n')
        self.assertFalse(self.route()[0])

    def test_matrix_precision_change_requires_fresh_run(self):
        self.change('scripts/certify_a1_c_even_exact_dyadic_matrix.py', 'PRECISION = 1024\n')
        self.assertEqual(self.route(), (True, 'a1-dependency-changed'))

    def test_error_budget_or_assumption_change_requires_fresh_run(self):
        self.change('scripts/check_a1_c_even_dyadic_budget_arb.py', 'EPS = "4e-39"\n')
        self.assertTrue(self.route()[0])
        self.change('audits/P11_A1_C_EVEN_ENGINE.md', 'Changed assumption\n')
        self.assertTrue(self.route()[0])

    def test_added_deleted_and_renamed_a1_inputs_are_detected(self):
        self.change('scripts/check_a1_new.py', 'new_dependency = 1\n')
        self.assertTrue(self.route()[0])
        (self.root / 'scripts/check_a1_new.py').unlink()
        original = self.root / 'scripts/check_a1_c_even_dyadic_budget_arb.py'
        original.rename(self.root / 'scripts/renamed.py')
        save(self.root)
        self.assertTrue(self.route()[0])

    def test_root_dependency_file_is_not_missed(self):
        self.change('requirements.txt', 'python-flint==0.10.0\n')
        self.assertTrue(self.route()[0])

    def test_new_python_import_shadow_is_not_missed(self):
        for path in ('scripts/flint.py', 'scripts/hashlib/__init__.py', 'sitecustomize/__init__.py'):
            with self.subTest(path=path):
                self.change(path, 'shadow = True\n')
                self.assertEqual(self.route(), (True, 'python-import-surface-changed'))

    def test_policy_change_cannot_reuse(self):
        for path in (r.SCRIPT, r.TEST):
            with self.subTest(path=path):
                self.change(path, '# changed policy\n')
                self.assertEqual(self.route(), (True, 'reuse-policy-or-evidence-changed'))

    def test_numerical_workflow_change_does_not_become_reusable_after_merge(self):
        head = self.change(r.WORKFLOW, self.workflow.replace('echo frozen', 'echo changed'))
        self.assertTrue(self.route()[0])
        self.assertEqual(self.route(base=head), (True, 'a1-execution-contract-changed'))

    def test_workflow_global_environment_is_bound(self):
        head = self.change(r.WORKFLOW, self.workflow.replace('jobs:', 'env:\n  PYTHONPATH: altered\njobs:'))
        self.assertEqual(self.route(base=head), (True, 'a1-execution-contract-changed'))

    def test_manual_audit_always_requests_fresh_run(self):
        self.assertEqual(self.route(event='workflow_dispatch'), (True, 'manual-audit'))

    def test_unknown_event_is_not_a_fast_pass(self):
        self.assertTrue(self.route(event='other')[0])

    def test_missing_or_corrupt_transcript_blocks_reuse(self):
        self.change(r.DIRECTORY + 'ldl.txt', 'corrupt\n')
        with self.assertRaises(r.InvalidEvidence):
            self.route()
        (self.root / r.DIRECTORY / 'ldl.txt').unlink()
        save(self.root)
        with self.assertRaises(r.InvalidEvidence):
            self.route()

    def test_echoed_certificate_command_is_not_certificate_output(self):
        self.update_evidence('gate.txt', '2026-10-19T16:00:00.000Z echo "' + r.CERTIFICATES['gate.txt'][0] + '"\n')
        with self.assertRaises(r.InvalidEvidence):
            self.route()

    def test_pending_failed_skipped_or_wrong_attempt_is_not_success(self):
        original = json.loads((self.root / r.DIRECTORY / 'run.json').read_text())
        for value in ('failure', 'skipped', 'cancelled', None):
            with self.subTest(conclusion=value):
                meta = json.loads(dump(original))
                meta['jobs'][1]['conclusion'] = value
                self.update_evidence('run.json', dump(meta))
                with self.assertRaises(r.InvalidEvidence):
                    self.route()
        original['jobs'][1]['run_attempt'] = 2
        self.update_evidence('run.json', dump(original))
        with self.assertRaises(r.InvalidEvidence):
            self.route()

    def test_omitted_dependency_is_not_a_valid_manifest(self):
        manifest = json.loads((self.root / r.MANIFEST).read_text())
        manifest['dependencies'].pop('scripts/check_a1_c_even_dyadic_budget_arb.py')
        self.change(r.MANIFEST, dump(manifest))
        with self.assertRaises(r.InvalidEvidence):
            self.route()

    def test_other_matrix_or_source_is_rejected(self):
        manifest = json.loads((self.root / r.MANIFEST).read_text())
        manifest['matrix_sha256'] = '0' * 64
        self.change(r.MANIFEST, dump(manifest))
        with self.assertRaises(r.InvalidEvidence):
            self.route()

    def test_full_commit_and_duplicate_json_keys_required(self):
        with self.assertRaises(r.InvalidEvidence):
            self.route(head='HEAD')
        with self.assertRaises(r.InvalidEvidence):
            r.parse('{"schema": 1, "schema": 2}')

    def test_workflow_parser_fails_closed(self):
        for text in (self.workflow.replace('jobs:', 'jobs: {}\nother:'),
                     self.workflow + 'env:\n  X: one\nenv:\n  X: two\n',
                     self.workflow.replace('    runs-on:', '\t runs-on:')):
            with self.subTest(text=text):
                with self.assertRaises(r.InvalidEvidence):
                    r.execution_contract(text.encode())

    def test_cli_rejects_head_mismatch_and_dirty_tracked_sources(self):
        cmd = [sys.executable, str(ROOT / r.SCRIPT), '--root', str(self.root), '--event',
               'pull_request', '--base', self.base, '--head', self.source]
        self.assertNotEqual(subprocess.run(cmd, capture_output=True).returncode, 0)
        cmd[-1] = self.base
        write(self.root, 'scripts/unrelated.py', 'dirty = True\n')
        self.assertNotEqual(subprocess.run(cmd, capture_output=True).returncode, 0)


class WorkflowIntegrationTests(unittest.TestCase):
    def test_gate_requires_validated_reuse_reason_and_successful_classifier(self):
        workflow = (ROOT / r.WORKFLOW).read_text()
        self.assertIn('[[ "$CLASSIFY_RESULT" == "success" ]]', workflow)
        self.assertIn('[[ "$CLASSIFY_REASON" == "bound-certificate-unchanged" ]]', workflow)
        self.assertIn('test_a1_certificate_reuse.py', workflow)
        self.assertNotIn('known-safe-registry-or-docs-only', workflow)


if __name__ == '__main__':
    unittest.main()
