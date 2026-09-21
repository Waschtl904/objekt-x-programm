"""Navigation invariants and adversarial changes, using isolated Git histories.

These tests exercise the governance checks, not the mathematical claims.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import research_state as rs


class StructureTests(unittest.TestCase):
    def setUp(self):
        self.state = rs.load(ROOT / rs.STATE)

    def test_current_selection_has_exactly_two_fronts(self):
        ids, _ = rs.validate_structure(self.state)
        self.assertIn(set(self.state['fronts']), ({'transport', 'c1'}, {'unified_terminal', 'global_continuation'}))
        self.assertTrue(ids)

    def test_determinism_survives_serialization(self):
        first = rs.render(self.state)
        second = rs.render(json.loads(rs.encoded(self.state)))
        self.assertEqual(first, second)
        for raw in first.values():
            self.assertNotIn(b'\r', raw)
            self.assertTrue(raw.endswith(b'\n'))

    def test_duplicate_keys_are_not_silently_overwritten(self):
        with self.assertRaisesRegex(rs.StateError, 'Duplicate key'):
            json.loads('{"status":"OPEN","status":"AUTHOR_DERIVED"}',
                       object_pairs_hook=rs.unique_object)

    def test_short_commit_is_rejected(self):
        self.state['verified_research_snapshot']['verified_through'] = '7998887'
        with self.assertRaisesRegex(rs.StateError, 'verified_through'):
            rs.validate_structure(self.state)

    def test_documentary_branch_head_has_snapshot_semantics(self):
        front = self.state['verified_research_snapshot']
        self.assertRegex(front['observed_branch_head'], rs.SHA)
        self.assertRegex(front['verified_through'], rs.SHA)
        self.assertEqual(front['head_policy'], 'VERIFIED_SNAPSHOT_NOT_CURRENT_HEAD')

    def test_short_documentary_branch_head_is_rejected(self):
        self.state['verified_research_snapshot']['observed_branch_head'] = 'f1fa23f'
        with self.assertRaisesRegex(rs.StateError, 'observed_branch_head'):
            rs.validate_structure(self.state)

    def test_current_head_claim_is_rejected(self):
        self.state['verified_research_snapshot']['head_policy'] = 'CURRENT_HEAD'
        with self.assertRaisesRegex(rs.StateError, 'current HEAD'):
            rs.validate_structure(self.state)

    def test_registry_sync_cannot_change_mathematical_review(self):
        self.state['registry_sync']['mathematical_review_changed'] = True
        with self.assertRaisesRegex(rs.StateError, 'cannot silently change'):
            rs.validate_structure(self.state)

    def test_registry_sync_base_must_match_published_baseline(self):
        self.state['registry_sync']['base_sha'] = '0' * 40
        with self.assertRaisesRegex(rs.StateError, 'must equal published baseline'):
            rs.validate_structure(self.state)

    def test_open_result_cannot_be_a_survivor(self):
        self.state['results'][0]['mathematical_status'] = 'OPEN'
        with self.assertRaisesRegex(rs.StateError, 'Survivor cannot'):
            rs.validate_structure(self.state)

    def test_result_and_open_obligation_cannot_share_id(self):
        self.state['obligations'][0]['id'] = self.state['results'][0]['id']
        with self.assertRaisesRegex(rs.StateError, 'ID overlap'):
            rs.validate_structure(self.state)

    def test_unconstructed_x_cannot_have_closed_global_gram_identity(self):
        self.state['global_status']['global_weil_gram_identity'] = 'AUTHOR_DERIVED'
        with self.assertRaisesRegex(rs.StateError, 'contradicts'):
            rs.validate_structure(self.state)

    def test_scope_and_claim_limits_are_mandatory(self):
        for field, value in [('scope', ' '), ('does_not_claim', []),
                             ('negative_claim_boundary', '')]:
            with self.subTest(field=field):
                changed = deepcopy(self.state)
                changed['results'][0][field] = value
                with self.assertRaises(rs.StateError):
                    rs.validate_structure(changed)

    def test_no_go_cannot_be_relabelled_as_full_negative_result(self):
        nogo = next(r for r in self.state['results']
                    if r['mathematical_status'] == 'AUTHOR_DERIVED_NO_GO')
        nogo['claim_polarity'] = 'POSITIVE_RESULT'
        with self.assertRaisesRegex(rs.StateError, 'No-go polarity'):
            rs.validate_structure(self.state)

    def test_active_front_needs_an_open_obligation(self):
        next(iter(self.state['fronts'].values()))['obligation_ids'] = []
        with self.assertRaisesRegex(rs.StateError, 'obligation_ids'):
            rs.validate_structure(self.state)

    def test_active_front_cannot_point_to_survivor_as_open_gate(self):
        next(iter(self.state['fronts'].values()))['obligation_ids'] = [self.state['results'][0]['id']]
        with self.assertRaisesRegex(rs.StateError, 'missing or closed obligation'):
            rs.validate_structure(self.state)

    def test_cyclic_dependencies_are_rejected(self):
        first, second = self.state['results'][:2]
        first['depends_on'] = [second['id']]
        second['depends_on'] = [first['id']]
        with self.assertRaisesRegex(rs.StateError, 'Cyclic'):
            rs.validate_structure(self.state)

    def test_external_review_requires_provenance(self):
        self.state['results'][0]['review_status'] = 'EXTERNALLY_REVIEWED_WITH_PROVENANCE'
        with self.assertRaisesRegex(rs.StateError, 'External review needs'):
            rs.validate_structure(self.state)

    def test_reproduction_is_not_inferred_from_math_status(self):
        self.state['results'][0]['reproduction_evidence'] = []
        with self.assertRaisesRegex(rs.StateError, 'Reproduction evidence/status'):
            rs.validate_structure(self.state)

    def test_integration_observation_is_required_and_does_not_promote(self):
        for field, value in [('mathematical_status_change', True),
                             ('ci_run_id', True), ('ci_run_attempt', 0),
                             ('main_sha', 'f822859'), ('observed_at', '2026-02-30')]:
            with self.subTest(field=field):
                changed = deepcopy(self.state)
                changed['current_integration_observation'][field] = value
                with self.assertRaises(rs.StateError):
                    rs.validate_structure(changed)
        del self.state['current_integration_observation']
        with self.assertRaisesRegex(rs.StateError, 'missing fields'):
            rs.validate_structure(self.state)

    def test_observation_cannot_bind_a_different_ci_head_or_repository(self):
        for field, value in [('ci_head_sha', '0' * 40),
                             ('ci_url', 'https://github.com/other/repo/actions/runs/1'),
                             ('ci_conclusion', 'failure')]:
            with self.subTest(field=field):
                changed = deepcopy(self.state)
                changed['current_integration_observation'][field] = value
                with self.assertRaises(rs.StateError):
                    rs.validate_structure(changed)

    def test_observation_rendering_preserves_frozen_anchors_and_statuses(self):
        before = deepcopy(self.state)
        current = rs.render(self.state)[rs.GENERATED[0]].decode()
        self.assertEqual(before, self.state)
        for sha in (self.state['published_baseline']['sha'],
                    self.state['verified_research_snapshot']['verified_through'],
                    self.state['verified_research_snapshot']['observed_branch_head'],
                    self.state['current_integration_observation']['main_sha'],
                    self.state['current_integration_observation']['integrated_research_head']):
            self.assertIn(sha, current)
        self.assertIn('Registry-Sync-Kandidat', current)
        self.assertIn('keine mathematische Neuverifikation', current)


class IntegrationCITests(unittest.TestCase):
    def setUp(self):
        self.s = rs.load(ROOT / rs.STATE)
        o = self.s['current_integration_observation']
        self.run = {'id': o['ci_run_id'], 'run_attempt': o['ci_run_attempt'],
                    'head_sha': o['main_sha'], 'head_branch': 'main', 'event': 'push',
                    'path': rs.INTEGRATION_CI_WORKFLOW, 'status': 'completed',
                    'conclusion': 'success', 'html_url': o['ci_url'],
                    'updated_at': o['observed_at'] + 'T03:18:07Z'}

    def test_exact_run_attempt_metadata_passes(self):
        rs.validate_integration_ci_run(self.s, self.run)

    def test_ci_identity_and_commit_mismatches_are_rejected(self):
        for field, value in [('id', self.run['id'] + 1), ('run_attempt', 2),
                             ('head_sha', '0' * 40), ('head_branch', 'research/other'),
                             ('event', 'pull_request'), ('path', '.github/workflows/other.yml'),
                             ('html_url', 'https://github.com/other/repo/actions/runs/1')]:
            with self.subTest(field=field):
                changed = dict(self.run, **{field: value})
                with self.assertRaisesRegex(rs.StateError, 'metadata mismatch: ' + field):
                    rs.validate_integration_ci_run(self.s, changed)

    def test_incomplete_failed_and_future_ci_are_rejected(self):
        for field, value in [('status', 'in_progress'), ('conclusion', 'cancelled'),
                             ('updated_at', '2099-01-01T00:00:00Z'), ('updated_at', None)]:
            with self.subTest(field=field, value=value):
                with self.assertRaises(rs.StateError):
                    rs.validate_integration_ci_run(self.s, dict(self.run, **{field: value}))

    def test_online_check_requests_the_recorded_attempt(self):
        from io import BytesIO
        with patch.object(rs, 'urlopen', return_value=BytesIO(json.dumps(self.run).encode())) as fetch:
            result = rs.check_integration_ci(ROOT)
        o = self.s['current_integration_observation']
        request = fetch.call_args.args[0]
        self.assertEqual(request.full_url, 'https://api.github.com/repos/' + self.s['repository']
                         + '/actions/runs/' + str(o['ci_run_id']) + '/attempts/' + str(o['ci_run_attempt']))
        self.assertEqual(result['head_sha'], o['main_sha'])

    def test_online_failure_is_not_treated_as_verified(self):
        with patch.object(rs, 'urlopen', side_effect=rs.URLError('offline')):
            with self.assertRaisesRegex(rs.StateError, 'Could not verify integration CI'):
                rs.check_integration_ci(ROOT)


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='objekt-x-state-tests-')
        cls.base_dir = Path(cls.temp.name) / 'fixture'
        cls.base_dir.mkdir()
        root = cls.base_dir
        rs.git(root, 'init', '--quiet')
        rs.git(root, 'config', 'user.name', 'Research state fixture')
        rs.git(root, 'config', 'user.email', 'fixture@example.invalid')
        rs.git(root, 'config', 'core.autocrlf', 'false')
        rs.git(root, 'config', 'commit.gpgsign', 'false')
        rs.git(root, 'config', 'core.hooksPath', str(root / '.git' / 'fixture-hooks'))

        def put(path, raw):
            dest = root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(raw)

        def commit(message):
            rs.git(root, 'add', '--all')
            rs.git(root, 'commit', '--quiet', '-m', message)
            return rs.git(root, 'rev-parse', 'HEAD').stdout.decode().strip()

        def ref(sha, path):
            raw = rs.git_blob(root, sha, path)
            return {'commit': sha, 'path': path,
                    'sha256': hashlib.sha256(raw).hexdigest()}

        definition = '00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md'
        put('research/frozen/PROOF.md', b'Frozen baseline fixture.\n')
        put('CURRENT-FRONT.md', b'Historical navigation.\r\n')
        put(definition, b'Independent mathematical definition.\n')
        baseline = commit('fixture baseline')
        put('research/frontier/PROOF.md', b'Frontier proof fixture.\n')
        frontier = commit('fixture frontier')
        # Real divergent history and merge, separate from the frozen math snapshot.
        rs.git(root, 'branch', 'fixture-research')
        rs.git(root, 'checkout', '--quiet', '-b', 'fixture-main', baseline)
        put('integration-note.md', b'Documentary main-side change.\n')
        commit('fixture main-side documentation')
        rs.git(root, 'merge', '--quiet', '--no-ff', '-m', 'fixture integration', 'fixture-research')
        integrated = rs.git(root, 'rev-parse', 'HEAD').stdout.decode().strip()
        state = rs.load(ROOT / rs.STATE)
        # Repository-level pending packages are not part of this isolated fixture.
        # Individual tests add their own pending package when exercising that lifecycle.
        state['pending_packages'] = []
        state['published_baseline']['sha'] = baseline
        state['verified_research_snapshot']['verified_through'] = frontier
        state['verified_research_snapshot']['observed_branch_head'] = frontier
        state['registry_sync']['branch'] = 'fixture/registry-sync'
        state['registry_sync']['base_sha'] = baseline
        state['registry_sync']['candidate_head_at_generation'] = integrated
        state['registry_sync']['mathematical_review_changed'] = False
        state['current_integration_observation'].update(
            main_sha=integrated, integrated_research_branch='fixture-research',
            integrated_research_head=frontier, reconciliation_merge=integrated,
            ci_head_sha=integrated)
        state['metadata_policy']['enforced_after'] = frontier
        state['authority_roles']['definition'] = ref(baseline, definition)
        state['authority_roles']['review_rules'] = ref(baseline, definition)
        state['results'] = state['results'][:2]
        # Keep the isolated fixture's integration scopes explicit instead of
        # inheriting the repository's current merged/unmerged selection.
        state['results'][0]['integration_status'] = 'MERGED'
        state['results'][1]['integration_status'] = 'RESEARCH_BRANCH_UNMERGED'
        for item, sha, path in zip(state['results'], [baseline, frontier],
                                  ['research/frozen/PROOF.md', 'research/frontier/PROOF.md']):
            evidence = ref(sha, path)
            item['canonical_commit'] = sha
            item['canonical_proof'] = path
            item['proof_sha256'] = evidence['sha256']
            item['reproduction_evidence'] = [evidence]
        for front in state['fronts'].values():
            front['uses_results'] = [state['results'][0]['id']]
            front['candidate'] = None
        original = ref(frontier, 'CURRENT-FRONT.md')
        state['historical_navigation'] = [{
            'path': original['path'], 'as_of': '2026-09-20',
            'content_commit': frontier, 'content_sha256': original['sha256'],
            'note': 'Fixture: only navigation is superseded.'}]
        # Navigation roles belong to this isolated fixture, not the live repo.
        state['navigation_exceptions'] = [{
            'path': definition, 'role': 'MATHEMATICAL_DEFINITION',
            'reason': 'Independent fixture definition.'}]
        put(rs.STATE, rs.encoded(state))
        for path, raw in rs.render(state).items():
            put(path, raw)
        historical = state['historical_navigation'][0]
        put(historical['path'], rs.banner(state, historical)
            + rs.git_blob(root, frontier, historical['path']))
        cls.initial_commit = commit('fixture canonical registry')
        cls.state = state

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory(dir=self.temp.name, prefix='case-')
        self.root = Path(self.test_dir.name) / 'repo'
        shutil.copytree(self.base_dir, self.root)
        self.s = deepcopy(self.state)

    def tearDown(self):
        self.test_dir.cleanup()

    def put(self, path, raw):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)

    def save_state(self):
        self.put(rs.STATE, rs.encoded(self.s))
        for path, raw in rs.render(self.s).items():
            self.put(path, raw)

    def commit(self, message):
        rs.git(self.root, 'add', '--all')
        rs.git(self.root, 'commit', '--quiet', '-m', message)
        return rs.git(self.root, 'rev-parse', 'HEAD').stdout.decode().strip()

    def package(self, strategic=True, pending=True):
        directory = 'research/new-package'
        raw = b'New explicitly scoped proof fixture.\n'
        self.put(directory + '/PROOF.md', raw)
        meta = json.loads((ROOT / 'scripts/schemas/META.example.json').read_text(encoding='utf-8'))
        meta.update(id='NEW-PACKAGE', strategic=strategic, local_only=not strategic,
                    scope='Explicit fixture source class.',
                    negative_claim_boundary='No full Weil negativity claim.')
        meta['canonical_proof'] = {'path': directory + '/PROOF.md',
                                   'sha256': hashlib.sha256(raw).hexdigest()}
        meta['opens'] = [self.s['obligations'][0]['id']] if strategic else []
        self.put(directory + '/META.yaml', rs.encoded(meta))
        if pending:
            self.s['pending_packages'] = [{'id': 'NEW-PACKAGE',
                'meta_path': directory + '/META.yaml', 'status': 'PENDING_STATUS_REVIEW'}]
        self.save_state()
        return meta

    def test_valid_snapshot_need_not_equal_head(self):
        result = rs.validate(self.root, self.initial_commit)
        self.assertEqual(result['results'], 2)
        self.assertNotEqual(result['verified_through'], self.initial_commit)

    def test_observed_integration_does_not_self_reclassify_fixture_results(self):
        before = deepcopy(self.s)
        rs.validate(self.root)
        self.assertEqual(self.s, before)
        self.assertEqual(self.s['results'][1]['integration_status'], 'RESEARCH_BRANCH_UNMERGED')
        o = self.s['current_integration_observation']
        self.assertNotEqual(o['main_sha'], self.initial_commit)
        self.assertTrue(rs.ancestor(self.root, self.s['verified_research_snapshot']['verified_through'], o['main_sha']))

    def test_unintegrated_research_head_is_rejected(self):
        self.s['current_integration_observation']['integrated_research_head'] = self.initial_commit
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'research head is not integrated'):
            rs.validate(self.root)

    def test_unintegrated_reconciliation_is_rejected(self):
        self.s['current_integration_observation']['reconciliation_merge'] = self.initial_commit
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'Reconciliation merge is not integrated'):
            rs.validate(self.root)

    def test_linear_commit_is_not_a_reconciliation_merge(self):
        self.s['current_integration_observation']['reconciliation_merge'] = self.s['published_baseline']['sha']
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'must identify a merge commit'):
            rs.validate(self.root)

    def test_unknown_observed_commit_is_rejected(self):
        self.s['current_integration_observation']['integrated_research_head'] = '0' * 40
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'Git check failed'):
            rs.validate(self.root)

    def test_unrelated_observed_main_is_rejected(self):
        tree = rs.git(self.root, 'rev-parse', 'HEAD^{tree}').stdout.decode().strip()
        unrelated = rs.git(self.root, 'commit-tree', tree, '-m', 'unrelated root').stdout.decode().strip()
        self.s['current_integration_observation'].update(main_sha=unrelated, ci_head_sha=unrelated)
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'outside checkout ancestry'):
            rs.validate(self.root)

    def test_duplicate_state_anywhere_is_rejected(self):
        self.put('research/RESEARCH_STATE.yaml', rs.encoded(self.s))
        with self.assertRaisesRegex(rs.StateError, 'Exactly one'):
            rs.validate(self.root)

    def test_pinned_proof_must_exist(self):
        self.s['results'][0]['canonical_proof'] = 'research/missing/PROOF.md'
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'Git check failed'):
            rs.validate(self.root)

    def test_pinned_hash_must_match(self):
        self.s['results'][0]['proof_sha256'] = '0' * 64
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'Pinned evidence hash mismatch'):
            rs.validate(self.root)

    def test_merge_status_cannot_be_self_promoted(self):
        self.s['results'][1]['integration_status'] = 'MERGED'
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'outside declared integration scope'):
            rs.validate(self.root)

    def test_manual_edit_of_each_generated_view_fails(self):
        for path in rs.GENERATED:
            with self.subTest(path=path):
                original = (self.root / path).read_bytes()
                self.put(path, original + b'Unauthorized manual drift.\n')
                with self.assertRaisesRegex(rs.StateError, 'Generated file differs'):
                    rs.validate(self.root)
                self.put(path, original)

    def test_historical_body_is_byte_preserved(self):
        path = self.root / 'CURRENT-FRONT.md'
        path.write_bytes(path.read_bytes().replace(b'Historical navigation.', b'Rewritten navigation.'))
        with self.assertRaisesRegex(rs.StateError, 'Historical banner/original bytes changed'):
            rs.validate(self.root)

    def test_active_readme_is_editable_without_unfreezing_historical_navigation(self):
        self.s['navigation_exceptions'].append({
            'path': 'README.md', 'role': 'ACTIVE_REPOSITORY_ENTRY',
            'reason': 'Editable entry; canonical research status is managed separately.'})
        self.put('README.md', b'Active repository entry.\n')
        self.save_state()
        rs.validate(self.root)
        self.put('README.md', b'Updated entry and neutral bibliographic wording.\n')
        rs.validate(self.root)
        historical = self.root / 'CURRENT-FRONT.md'
        historical.write_bytes(historical.read_bytes() + b'Unauthorized historical rewrite.\n')
        with self.assertRaisesRegex(rs.StateError, 'Historical banner/original bytes changed'):
            rs.validate(self.root)

    def test_new_current_document_needs_explicit_role(self):
        self.put('00-uebersicht/NEW_CURRENT.md', b'Alternate current frontier.\n')
        with self.assertRaisesRegex(rs.StateError, 'Unclassified current/active'):
            rs.validate(self.root)

    def test_frozen_packages_need_no_meta(self):
        self.assertFalse((self.root / 'research/frozen/META.yaml').exists())
        self.assertEqual(rs.validate(self.root)['new_metadata_packages'], 0)

    def test_new_proof_requires_metadata(self):
        self.put('research/new-package/PROOF.md', b'New proof.\n')
        with self.assertRaisesRegex(rs.StateError, 'requires META.yaml'):
            rs.validate(self.root)

    def test_new_strategic_package_requires_pending_or_registered_entry(self):
        self.package(pending=False)
        with self.assertRaisesRegex(rs.StateError, 'missing from registered or pending'):
            rs.validate(self.root)

    def test_strategic_pending_package_is_visible_without_snapshot_promotion(self):
        self.package()
        result = rs.validate(self.root, self.initial_commit)
        self.assertEqual(result['new_metadata_packages'], 1)
        self.assertEqual(result['verified_through'], self.state['verified_research_snapshot']['verified_through'])
        self.assertIn(b'PENDING_STATUS_REVIEW', (self.root / rs.GENERATED[0]).read_bytes())

    def test_published_pending_package_can_be_registered_at_its_actual_commit(self):
        meta = self.package()
        package_commit = self.commit('fixture publish pending package')
        item = deepcopy(self.s['results'][1])
        item.update(id=meta['id'], canonical_commit=package_commit,
                    canonical_proof=meta['canonical_proof']['path'],
                    proof_sha256=meta['canonical_proof']['sha256'],
                    reproduction_status='ANALYTIC_ONLY', reproduction_evidence=[])
        self.s['results'].append(item)
        self.s['pending_packages'] = []
        self.s['verified_research_snapshot']['verified_through'] = package_commit
        self.s['verified_research_snapshot']['observed_branch_head'] = package_commit
        self.save_state()
        checked = rs.validate(self.root, self.initial_commit)
        self.assertEqual(checked['results'], 3)
        self.assertEqual(checked['verified_through'], package_commit)

    def test_local_only_package_needs_no_strategic_state_change(self):
        self.package(strategic=False, pending=False)
        self.assertEqual(rs.validate(self.root, self.initial_commit)['new_metadata_packages'], 1)
        self.assertEqual(self.s, self.state)

    def test_strategic_package_must_declare_effect(self):
        meta = self.package()
        meta['opens'] = []
        self.put('research/new-package/META.yaml', rs.encoded(meta))
        with self.assertRaisesRegex(rs.StateError, 'must declare closes, opens or supersedes'):
            rs.validate(self.root)

    def test_meta_no_go_needs_consistent_polarity(self):
        meta = self.package()
        meta['kind'] = 'NO_GO'
        self.put('research/new-package/META.yaml', rs.encoded(meta))
        with self.assertRaisesRegex(rs.StateError, 'no-go kind/status/polarity'):
            rs.validate(self.root)

    def test_local_only_cannot_hide_strategic_effects(self):
        meta = self.package(strategic=False)
        meta['closes'] = [self.s['obligations'][0]['id']]
        self.put('research/new-package/META.yaml', rs.encoded(meta))
        with self.assertRaisesRegex(rs.StateError, 'local_only cannot'):
            rs.validate(self.root)

    def test_unknown_meta_obligation_is_rejected(self):
        meta = self.package()
        meta['opens'] = ['UNDECLARED-GATE']
        self.put('research/new-package/META.yaml', rs.encoded(meta))
        with self.assertRaisesRegex(rs.StateError, 'effects/dependencies'):
            rs.validate(self.root)

    def test_meta_binds_actual_new_proof_bytes(self):
        self.package()
        self.put('research/new-package/PROOF.md', b'Different proof.\n')
        with self.assertRaisesRegex(rs.StateError, 'META proof hash mismatch'):
            rs.validate(self.root)

    def test_metadata_anchor_cannot_be_reset_to_grandfather_new_package(self):
        self.put('research/new-package/PROOF.md', b'Undeclared new proof.\n')
        added = self.commit('fixture attempt to grandfather new package')
        self.s['metadata_policy']['enforced_after'] = added
        self.s['verified_research_snapshot']['verified_through'] = added
        self.s['verified_research_snapshot']['observed_branch_head'] = added
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'Cannot reset metadata enforcement'):
            rs.validate(self.root, self.initial_commit)

    def test_generated_format_change_requires_state_change(self):
        self.put(rs.GENERATED[0], b'Previous generator format.\n')
        previous = self.commit('fixture previous generator format')
        self.save_state()
        with self.assertRaisesRegex(rs.StateError, 'without a state change'):
            rs.validate(self.root, previous)
        self.s['render_version'] += 1
        self.save_state()
        rs.validate(self.root, previous)

    def test_safe_paths_reject_repository_escape(self):
        self.s['results'][0]['canonical_proof'] = '../outside.md'
        with self.assertRaisesRegex(rs.StateError, 'Unsafe repository path'):
            rs.validate_structure(self.s)


if __name__ == '__main__':
    unittest.main()
