"""Exercise the actual publication loop against temporary local Git remotes."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import textwrap
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASH = shutil.which('bash')
if os.name == 'nt':
    BASH = str(Path(os.environ.get('ProgramFiles', 'C:/Program Files')) / 'Git/bin/bash.exe')


class IntegrityWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='integrity-test-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.remote = self.base / 'remote.git'
        self.worker = self.base / 'worker'
        self.sibling = self.base / 'sibling'
        self.env = dict(os.environ, GIT_AUTHOR_NAME='Integrity test',
                        GIT_AUTHOR_EMAIL='integrity@example.invalid',
                        GIT_COMMITTER_NAME='Integrity test',
                        GIT_COMMITTER_EMAIL='integrity@example.invalid',
                        GIT_CONFIG_COUNT='1', GIT_CONFIG_KEY_0='core.autocrlf',
                        GIT_CONFIG_VALUE_0='false')
        self.run_cmd(['git', 'init', '--bare', '--initial-branch=main', str(self.remote)], self.base)
        self.run_cmd(['git', 'clone', str(self.remote), str(self.worker)], self.base)
        for name in ('build_integrity.sh', 'verify_integrity.sh'):
            dest = self.worker / 'scripts' / name
            dest.parent.mkdir(exist_ok=True)
            dest.write_bytes((ROOT / 'scripts' / name).read_bytes())
        generator = (self.worker / 'scripts/build_integrity.sh').read_text(encoding='utf-8')
        self.inputs = re.findall(r'^  "([^"]+)"$', generator, flags=re.M)
        self.assertEqual(len(self.inputs), 11)
        for name in self.inputs:
            dest = self.worker / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text('initial fixture\n', encoding='utf-8')
        self.run_cmd(['git', 'add', '.'], self.worker)
        self.run_cmd(['git', 'commit', '-m', 'fixture'], self.worker)
        self.run_cmd(['git', 'push', 'origin', 'main'], self.worker)
        self.run_cmd(['git', 'clone', str(self.remote), str(self.sibling)], self.base)
        # Read the production shell block; no second implementation in the test.
        workflow = (ROOT / '.github/workflows/integrity.yml').read_text(encoding='utf-8')
        block = workflow.split('      - name: Recompute-and-publish loop\n', 1)[1]
        self.loop = textwrap.dedent(block.split('        run: |\n', 1)[1])

    def run_cmd(self, args, cwd, check=True):
        p = subprocess.run(args, cwd=cwd, env=self.env, capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=90)
        if check:
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        return p

    def shell(self, script, cwd=None, check=True):
        # Bash reads stdin to avoid Windows command-line quoting differences.
        p = subprocess.run([BASH, '-s'], input=script, cwd=cwd or self.worker,
                           env=self.env, capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=90)
        if check:
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        return p

    def publish(self, mode='none', check=True):
        self.env['TEST_SIBLING'] = self.sibling.as_posix()
        self.env['TEST_RACE_MODE'] = mode
        hook = '''
        pushes=0
        git() {
          if [[ "$1" == push && "$2" == origin && "$3" == HEAD:main ]]; then
            pushes=$((pushes + 1))
            if [[ "$TEST_RACE_MODE" == fail ]]; then return 1; fi
            if [[ "$TEST_RACE_MODE" == race && "$pushes" == 1 ]] ||
               [[ "$TEST_RACE_MODE" == exhaust ]] ||
               [[ "$TEST_RACE_MODE" == sibling ]]; then
              (
                cd "$TEST_SIBLING"
                command git fetch --quiet origin main
                command git checkout --quiet -B main origin/main
                printf 'concurrent change %s\\n' "$pushes" >> LICENSE
                if [[ "$TEST_RACE_MODE" == sibling && "$pushes" == 3 ]]; then
                  bash scripts/build_integrity.sh > INTEGRITY.md
                fi
                command git add LICENSE
                if [[ "$TEST_RACE_MODE" == sibling && "$pushes" == 3 ]]; then command git add INTEGRITY.md; fi
                command git commit --quiet -m "concurrent update $pushes"
                command git push --quiet origin main
              ) || return 9
            fi
          fi
          command git "$@"
        }
        '''
        return self.shell(textwrap.dedent(hook) + self.loop, check=check)

    def remote_manifest_matches(self):
        self.run_cmd(['git', 'fetch', 'origin', 'main'], self.sibling)
        self.run_cmd(['git', 'checkout', '-B', 'main', 'origin/main'], self.sibling)
        self.shell('bash scripts/verify_integrity.sh INTEGRITY.md', self.sibling)

    def test_generation_is_deterministic_and_verifies(self):
        a = self.shell('bash scripts/build_integrity.sh').stdout
        b = self.shell('bash scripts/build_integrity.sh').stdout
        self.assertEqual(a, b)
        self.shell('bash scripts/build_integrity.sh > INTEGRITY.md\nbash scripts/verify_integrity.sh')

    def test_missing_input_fails_before_manifest_output(self):
        (self.worker / 'LICENSE').unlink()
        p = self.shell('bash scripts/build_integrity.sh', check=False)
        self.assertNotEqual(p.returncode, 0)
        self.assertEqual(p.stdout, '')
        self.assertIn('required file missing', p.stderr)

    def test_tampered_manifest_and_changed_source_are_rejected(self):
        self.shell('bash scripts/build_integrity.sh > INTEGRITY.md')
        p = self.worker / 'INTEGRITY.md'
        p.write_bytes(p.read_bytes() + b'tampered\n')
        self.assertNotEqual(self.shell('bash scripts/verify_integrity.sh', check=False).returncode, 0)
        self.shell('bash scripts/build_integrity.sh > INTEGRITY.md')
        (self.worker / 'LICENSE').write_text('changed\n', encoding='utf-8')
        self.assertNotEqual(self.shell('bash scripts/verify_integrity.sh', check=False).returncode, 0)

    def test_missing_remote_manifest_is_created_and_next_run_is_noop(self):
        self.publish()
        self.remote_manifest_matches()
        first = self.run_cmd(['git', 'rev-parse', 'HEAD'], self.worker).stdout
        self.assertIn('nothing to publish', self.publish().stdout)
        self.assertEqual(first, self.run_cmd(['git', 'rev-parse', 'HEAD'], self.worker).stdout)

    def test_concurrent_source_change_is_preserved_and_recomputed(self):
        p = self.publish('race')
        self.assertIn('published on attempt 2', p.stdout)
        self.remote_manifest_matches()
        self.assertIn('concurrent change 1', (self.sibling / 'LICENSE').read_text())

    def test_exhausted_races_fail_when_remote_manifest_is_stale(self):
        self.publish()
        self.shell('printf "change\\n" >> LICENSE\ngit add LICENSE\ngit commit -m source\ngit push origin main')
        p = self.publish('exhaust', check=False)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn('remote INTEGRITY.md does NOT match', p.stdout)

    def test_sibling_publication_is_accepted_after_three_rejections(self):
        p = self.publish('sibling')
        self.assertIn('accepting sibling publication', p.stdout)
        self.remote_manifest_matches()
        self.assertIn('concurrent change 3', (self.sibling / 'LICENSE').read_text())

    def test_non_race_push_failures_do_not_report_success(self):
        p = self.publish('fail', check=False)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn('gave up after 3 attempts', p.stdout)


if __name__ == '__main__':
    unittest.main()
