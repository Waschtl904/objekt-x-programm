#!/usr/bin/env python3
"""Deterministic research navigation; no mathematical theorem promotion.

The .yaml inputs use the JSON subset of YAML 1.2, parsed with Python's
standard library. Duplicate keys and non-finite numeric values are rejected.
"""
from __future__ import annotations
import hashlib, json, re, subprocess
import posixpath
from pathlib import Path, PurePosixPath
STATE = '00-uebersicht/RESEARCH_STATE.yaml'
GENERATED = ('00-uebersicht/CURRENT_STATE.md', '00-uebersicht/NEXT_GATES.md', '00-uebersicht/SURVIVOR_REGISTRY.md')
SHA = re.compile('^[0-9a-f]{40}$')
DIGEST = re.compile('^[0-9a-f]{64}$')
ID = re.compile('^[A-Za-z0-9][A-Za-z0-9_.-]*$')
STATUSES = {'AUTHOR_DERIVED', 'AUTHOR_DERIVED_NO_GO', 'OPEN', 'NOT_CONSTRUCTED'}
INTEGRATION = {'MERGED', 'RESEARCH_BRANCH_UNMERGED'}
REPRO = {'RECORDED_PACKAGE_CHECKS', 'ANALYTIC_ONLY', 'NOT_APPLICABLE'}
REVIEW = {'EXTERNAL_REVIEW_OPEN', 'EXTERNALLY_REVIEWED_WITH_PROVENANCE'}
POLARITY = {'POSITIVE_RESULT', 'CONSTRUCTION', 'EQUIVALENCE_OR_REDUCTION', 'NEGATIVE_FOR_CANDIDATE_CLASS'}

class StateError(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise StateError(message)

def unique_object(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, 'Duplicate key: ' + k)
        out[k] = v
    return out

def load(path):
    try:
        return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=unique_object, parse_constant=lambda x: (_ for _ in ()).throw(StateError('Non-finite value: ' + x)))
    except (OSError, json.JSONDecodeError) as e:
        raise StateError(str(e)) from e

def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')

def fields(obj, names, where, optional=()):
    require(isinstance(obj, dict), where + ' must be an object')
    require(set(names) <= set(obj), where + ' missing fields: ' + ', '.join(sorted(set(names) - set(obj))))
    require(set(obj) <= set(names) | set(optional), where + ' unknown fields: ' + ', '.join(sorted(set(obj) - set(names) - set(optional))))

def string(value, where):
    require(isinstance(value, str) and bool(value.strip()) and ('\x00' not in value), where + ' must be nonempty text')

def strings(value, where, nonempty=False):
    require(isinstance(value, list) and (not nonempty or bool(value)), where + ' must be a list' + (' with entries' if nonempty else ''))
    for x in value:
        string(x, where)
    require(len(value) == len(set(value)), where + ' contains duplicates')

def relative(path):
    string(path, 'path')
    p = PurePosixPath(path)
    require(not p.is_absolute() and '\\' not in path and (':' not in path) and (not any((x in ('', '.', '..') for x in path.split('/')))), 'Unsafe repository path: ' + path)
    return path

def ref_fields(ref, where):
    fields(ref, ('commit', 'path', 'sha256'), where)
    require(isinstance(ref['commit'], str) and bool(SHA.fullmatch(ref['commit'])), where + ' commit must be a full lowercase SHA')
    relative(ref['path'])
    require(isinstance(ref['sha256'], str) and bool(DIGEST.fullmatch(ref['sha256'])), where + ' invalid SHA256')

def git(root, *args, check=True):
    p = subprocess.run(['git', '-c', 'safe.directory=' + Path(root).resolve().as_posix(), '-C', str(root), *args], capture_output=True)
    if check:
        require(p.returncode == 0, 'Git check failed: ' + ' '.join(args[:2]) + ' ' + p.stderr.decode('utf-8', 'replace').strip())
    return p

def git_blob(root, commit, path, missing_ok=False):
    p = git(root, 'cat-file', 'blob', commit + ':' + relative(path), check=not missing_ok)
    return p.stdout if p.returncode == 0 else None

def ancestor(root, old, new):
    p = git(root, 'merge-base', '--is-ancestor', old, new, check=False)
    require(p.returncode in (0, 1), 'Cannot inspect ancestry; use a full-history checkout')
    return p.returncode == 0

def all_paths(root):
    return set(git(root, 'ls-files', '--cached', '--others', '--exclude-standard', '-z').stdout.decode('utf-8').rstrip('\x00').split('\x00')) - {''}

def tree_paths(root, sha):
    return set(git(root, 'ls-tree', '-r', '--name-only', '-z', sha).stdout.decode('utf-8').rstrip('\x00').split('\x00')) - {''}

def proof_paths(paths):
    return {str(PurePosixPath(p).parent) for p in paths if p.startswith('research/') and p.endswith('/PROOF.md')}

def pinned_link(state, ref, label):
    return '[' + label + '](https://github.com/' + state['repository'] + '/blob/' + ref['commit'] + '/' + ref['path'] + ')'

def commit_link(state, sha):
    return '[' + sha[:7] + '](https://github.com/' + state['repository'] + '/commit/' + sha + ')'

def validate_structure(s):
    fields(s, ('schema_version', 'render_version', 'state_date', 'repository', 'published_baseline', 'live_frontier', 'authority_roles', 'fronts', 'obligations', 'results', 'global_status', 'historical_navigation', 'navigation_exceptions', 'metadata_policy', 'pending_packages'), 'state')
    require(type(s['schema_version']) is int and s['schema_version'] == 1, 'Unsupported schema_version')
    require(type(s['render_version']) is int and s['render_version'] >= 1, 'Invalid render_version')
    require(isinstance(s['state_date'], str) and re.fullmatch('\\d{4}-\\d{2}-\\d{2}', s['state_date']), 'state_date must be YYYY-MM-DD')
    require(s['repository'] == 'Waschtl904/objekt-x-programm', 'Unexpected repository')
    base = s['published_baseline']
    front = s['live_frontier']
    fields(base, ('branch', 'sha', 'integration_status', 'meaning', 'mathematical_status', 'review_status'), 'baseline')
    require(base['branch'] == 'main' and base['integration_status'] == 'MERGED', 'Baseline must be a merged main snapshot')
    require(isinstance(base['sha'], str) and SHA.fullmatch(base['sha']), 'Invalid baseline SHA')
    require(base['mathematical_status'] == 'AUTHOR_DERIVED' and base['review_status'] == 'EXTERNAL_REVIEW_OPEN', 'Invalid baseline epistemic status')
    string(base['meaning'], 'baseline meaning')
    fields(front, ('branch', 'verified_through', 'integration_status', 'review_status', 'head_policy'), 'frontier')
    string(front['branch'], 'frontier branch')
    require(isinstance(front['verified_through'], str) and SHA.fullmatch(front['verified_through']), 'Invalid verified_through SHA')
    require(front['integration_status'] == 'RESEARCH_BRANCH_UNMERGED' and front['review_status'] == 'EXTERNAL_REVIEW_OPEN', 'Invalid frontier status')
    require(front['head_policy'] == 'VERIFIED_SNAPSHOT_NOT_CURRENT_HEAD', 'verified_through must not be presented as current HEAD')
    require(isinstance(s['authority_roles'], dict) and set(s['authority_roles']) == {'definition', 'review_rules', 'proof_principle'}, 'Missing authority roles')
    for key in ('definition', 'review_rules'):
        ref_fields(s['authority_roles'][key], key)
    string(s['authority_roles']['proof_principle'], 'proof authority principle')
    ids = set()
    result_ids = set()
    open_ids = set()
    by_id = {}
    require(isinstance(s['results'], list) and bool(s['results']), 'Survivor registry must not be empty')
    for r in s['results']:
        fields(r, ('id', 'title', 'mathematical_status', 'review_status', 'integration_status', 'strategic_status', 'reproduction_status', 'reproduction_evidence', 'claim_polarity', 'scope', 'claim', 'depends_on', 'supersedes', 'replaced_by', 'canonical_commit', 'canonical_proof', 'proof_sha256', 'negative_claim_boundary', 'does_not_claim'), 'result', ('external_review_evidence',))
        require(isinstance(r['id'], str) and ID.fullmatch(r['id']) and (r['id'] not in ids), 'Duplicate/invalid result ID')
        ids.add(r['id'])
        result_ids.add(r['id'])
        by_id[r['id']] = r
        for name in ('title', 'scope', 'negative_claim_boundary'):
            string(r[name], r['id'] + ' ' + name)
        for name in ('claim', 'does_not_claim'):
            strings(r[name], r['id'] + ' ' + name, True)
        for name in ('depends_on', 'supersedes', 'replaced_by'):
            strings(r[name], r['id'] + ' ' + name)
        require(r['mathematical_status'] in {'AUTHOR_DERIVED', 'AUTHOR_DERIVED_NO_GO'}, 'Survivor cannot also be OPEN: ' + r['id'])
        require(r['review_status'] in REVIEW and r['integration_status'] in INTEGRATION, 'Invalid orthogonal status: ' + r['id'])
        require(r['strategic_status'] == 'REUSABLE_COMPONENT', 'Survivors are reusable components, not automatic active fronts')
        require(r['claim_polarity'] in POLARITY, 'Invalid claim polarity')
        require((r['mathematical_status'] == 'AUTHOR_DERIVED_NO_GO') == (r['claim_polarity'] == 'NEGATIVE_FOR_CANDIDATE_CLASS'), 'No-go polarity/status mismatch')
        require(not r['replaced_by'], 'Replaced results must leave the current survivor selection')
        require(r['reproduction_status'] in REPRO, 'Unknown reproduction status')
        require(isinstance(r['reproduction_evidence'], list), 'Reproduction evidence must be a list')
        require(bool(r['reproduction_evidence']) == (r['reproduction_status'] == 'RECORDED_PACKAGE_CHECKS'), 'Reproduction evidence/status mismatch')
        for ref in r['reproduction_evidence']:
            ref_fields(ref, 'reproduction evidence')
        ref_fields({'commit': r['canonical_commit'], 'path': r['canonical_proof'], 'sha256': r['proof_sha256']}, r['id'] + ' proof')
        if r['review_status'] == 'EXTERNALLY_REVIEWED_WITH_PROVENANCE':
            require(bool(r.get('external_review_evidence')), 'External review needs pinned provenance')
            ref_fields(r['external_review_evidence'], 'external review')
    require(isinstance(s['obligations'], list), 'Obligations must be a list')
    for o in s['obligations']:
        fields(o, ('id', 'title', 'mathematical_status', 'scope'), 'obligation')
        require(isinstance(o['id'], str) and ID.fullmatch(o['id']) and (o['id'] not in ids), 'Result/obligation ID overlap or duplicate')
        ids.add(o['id'])
        open_ids.add(o['id'])
        require(o['mathematical_status'] == 'OPEN', 'Obligation must be OPEN')
        string(o['title'], 'obligation title')
        string(o['scope'], 'obligation scope')
    require(isinstance(s['fronts'], dict) and set(s['fronts']) == {'transport', 'c1'}, 'Exactly the Transport and C1 primary fronts are required')
    for f in s['fronts'].values():
        fields(f, ('id', 'title', 'mathematical_status', 'strategic_status', 'target_scope', 'obligation_ids', 'uses_results', 'accepted_progress', 'insufficient', 'candidate'), 'front')
        require(f['mathematical_status'] == 'OPEN' and f['strategic_status'] == 'ACTIVE_FRONT', 'Active front must be OPEN')
        for name in ('id', 'title', 'target_scope'):
            string(f[name], 'front ' + name)
        for name in ('obligation_ids', 'uses_results', 'accepted_progress', 'insufficient'):
            strings(f[name], 'front ' + name, True)
        require(set(f['obligation_ids']) <= open_ids, 'Active front references a missing or closed obligation')
        require(set(f['uses_results']) <= result_ids, 'Unknown active-front input')
        require(f['candidate'] is None or f['candidate'] in result_ids, 'Unknown candidate')
    for r in s['results']:
        require(set(r['depends_on'] + r['supersedes'] + r['replaced_by']) <= ids, 'Unknown result relation: ' + r['id'])
        require(r['id'] not in r['depends_on'] + r['supersedes'], 'Self-dependent result')

    def visit(i, active, done):
        require(i not in active, 'Cyclic survivor dependency')
        if i in done or i not in by_id:
            return
        for dep in by_id[i]['depends_on']:
            visit(dep, active | {i}, done)
        done.add(i)
    done = set()
    for i in result_ids:
        visit(i, set(), done)
    gs = s['global_status']
    fields(gs, ('connected_unit_window_coercivity', 'strong_terminal', 'full_c1_geom', 'object_x', 'global_weil_gram_identity', 'global_weil_positivity', 'rh'), 'global status')
    require(all((v in STATUSES for v in gs.values())), 'Unknown global mathematical status')
    require(not (gs['object_x'] == 'NOT_CONSTRUCTED' and gs['global_weil_gram_identity'] == 'AUTHOR_DERIVED'), 'Global Gram closure contradicts the declared unconstructed Object X state')
    require(isinstance(s['historical_navigation'], list), 'historical_navigation must be a list')
    require(isinstance(s['navigation_exceptions'], list), 'navigation_exceptions must be a list')
    for h in s['historical_navigation']:
        fields(h, ('path', 'as_of', 'content_commit', 'content_sha256', 'note'), 'historical navigation')
        ref_fields({'path': h['path'], 'commit': h['content_commit'], 'sha256': h['content_sha256']}, 'historical original')
        string(h['as_of'], 'historical date')
        string(h['note'], 'historical note')
    for e in s['navigation_exceptions']:
        fields(e, ('path', 'role', 'reason'), 'navigation exception')
        relative(e['path'])
        string(e['role'], 'exception role')
        string(e['reason'], 'exception reason')
    require(len({h['path'] for h in s['historical_navigation']}) == len(s['historical_navigation']), 'Duplicate historical path')
    require(len({e['path'] for e in s['navigation_exceptions']}) == len(s['navigation_exceptions']), 'Duplicate navigation exception')
    require(not {h['path'] for h in s['historical_navigation']} & {e['path'] for e in s['navigation_exceptions']}, 'Conflicting navigation role')
    mp = s['metadata_policy']
    fields(mp, ('enforced_after', 'discovery', 'format'), 'metadata policy')
    require(isinstance(mp['enforced_after'], str) and SHA.fullmatch(mp['enforced_after']), 'Invalid metadata introduction anchor')
    require(mp['discovery'] == 'NEW_RESEARCH_PROOF_DIRECTORIES' and mp['format'] == 'JSON_SUBSET_OF_YAML_1_2', 'Unsupported metadata policy')
    require(isinstance(s['pending_packages'], list), 'pending_packages must be a list')
    pending_ids = set()
    for p in s['pending_packages']:
        fields(p, ('id', 'meta_path', 'status'), 'pending package')
        string(p['id'], 'pending ID')
        relative(p['meta_path'])
        require(p['id'] not in pending_ids and p['id'] not in result_ids, 'Duplicate or already registered pending package')
        pending_ids.add(p['id'])
        require(p['status'] == 'PENDING_STATUS_REVIEW', 'Pending package is not a theorem promotion')
    return (result_ids, open_ids)

def banner(s, h):
    link = PurePosixPath(h['path']).parent
    destination = posixpath.relpath(STATE, str(link))
    readable = posixpath.relpath(GENERATED[0], str(link))
    lines = [
        '> [!WARNING]',
        '> **HISTORICAL SNAPSHOT — nur die operative Navigation ist ersetzt.**',
        '>',
        '> As of: ' + h['as_of'],
        '> Nicht zur Bestimmung der aktuellen Forschungsfront verwenden.',
        '> Kanonischer Status: [RESEARCH_STATE.yaml](' + destination + ').',
        '> Lesbarer Einstieg: [CURRENT_STATE.md](' + readable + ').',
        '> ' + h['note'],
        '> Mathematische Inhalte werden durch diesen Hinweis nicht pauschal verworfen.',
        '',
    ]
    if h['path'].endswith(('.yaml', '.yml')):
        return ('\n'.join(('# ' + line if line else '#' for line in lines)) + '\n').encode('utf-8')
    return ('\n'.join(lines) + '\n').encode('utf-8')

def render(s):
    generated = '> GENERATED FILE — DO NOT EDIT\n> Quelle: [RESEARCH_STATE.yaml](RESEARCH_STATE.yaml). Navigation, keine Satzpromotion.\n'
    b = s['published_baseline']
    f = s['live_frontier']
    current = ['# Aktueller Forschungsstand', '', generated, 'Stand: ' + s['state_date'] + '.', '', '## Gemergte Basis', '', '`main@' + b['sha'][:7] + '` — ' + commit_link(s, b['sha']) + '. ' + b['meaning'], 'Mathematik: ' + b['mathematical_status'] + '; externe Prüfung: ' + b['review_status'] + '.', '', '## Verifizierter Forschungsstand', '', 'Geprüft bis ' + commit_link(s, f['verified_through']) + ' auf `' + f['branch'] + '`.', '**Dies ist ein geprüfter Snapshot, keine Behauptung über den dauerhaft aktuellen Branch-HEAD.**', 'Integration: ' + f['integration_status'] + '; externe Prüfung: ' + f['review_status'] + '.', '', '## Zwei aktive Hauptfronten', '']
    for key, front in s['fronts'].items():
        current += ['- **' + front['title'] + '** — `' + front['id'] + '`, OPEN. ' + front['target_scope']]
    current += ['', '## Verwendbare Bausteine', '', '| ID | Mathematischer Status | Beleg |', '|---|---|---|']
    for r in s['results']:
        current += ['| `' + r['id'] + '` | ' + r['mathematical_status'] + ' | ' + pinned_link(s, {'commit': r['canonical_commit'], 'path': r['canonical_proof']}, r['canonical_commit'][:7]) + ' |']
    current += ['', 'Details zu Scope, Abhängigkeiten und Grenzen: [SURVIVOR_REGISTRY](SURVIVOR_REGISTRY.md).', '', '## Globale Grenzen', '']
    current += ['- `' + k + '`: **' + v + '**.' for k, v in s['global_status'].items()]
    current += ['', 'Dokumentierte Checkerläufe sind von externer Prüfung und Git-Integration getrennt. Diese Statusansicht führt die mathematischen Checker nicht erneut aus.']
    if s['pending_packages']:
        current += ['', '## Noch nicht in den geprüften Stand übernommene Pakete', ''] + ['- `' + p['id'] + '`: ' + p['status'] + ' — `' + p['meta_path'] + '`.' for p in s['pending_packages']]
    current += ['', 'Einstieg: [NEXT_GATES](NEXT_GATES.md) · [Architektur](OBJEKT_X_ARCHITECTURE.md) · [Pflege und Prüfungen](RESEARCH_STATE_MAINTENANCE.md).']
    gates = ['# Nächste Forschungsaufgaben', '', generated, 'Genau zwei Hauptfronten. Die vollständigen Beweise und Eingabebindungen stehen in den verlinkten Paketen.', '']
    by_ob = {o['id']: o for o in s['obligations']}
    for front in s['fronts'].values():
        gates += ['## ' + front['title'], '', '`' + front['id'] + '` — OPEN. ' + front['target_scope'], '', 'Offene Obligationen:', '']
        gates += ['- `' + i + '`: ' + by_ob[i]['title'] + ' — ' + by_ob[i]['scope'] for i in front['obligation_ids']]
        gates += ['', 'Akzeptierter strategischer Fortschritt:', ''] + ['- ' + x for x in front['accepted_progress']]
        gates += ['', 'Nicht ausreichend:', ''] + ['- ' + x for x in front['insufficient']]
        gates += ['', 'Verwendbare Registereinträge: ' + ', '.join(('`' + x + '`' for x in front['uses_results'])) + '.', '']
    gates += ['Horizont und Testklasse sind gemäß dem jeweiligen Scope zu beachten. Ein lokaler Gate-Abschluss ist keine RH-Promotion.']
    survivors = ['# Survivor Registry', '', generated, 'Kompakte Auswahl heute verwendbarer Bausteine; kein Gesamtaudit aller historischen Resultate. Beziehungen nennen ausgewählte Register-Abhängigkeiten. Vollständige mathematische Inputs stehen in den Beweispaketen.', '']
    for r in s['results']:
        survivors += ['## ' + r['id'], '', r['title'], '', '- Mathematical status: `' + r['mathematical_status'] + '`.', '- Review status: `' + r['review_status'] + '`.', '- Integration status: `' + r['integration_status'] + '`.', '- Strategic status: `' + r['strategic_status'] + '`.', '- Reproduction status: `' + r['reproduction_status'] + '`.', '- Scope: ' + r['scope'], '- Canonical commit: ' + commit_link(s, r['canonical_commit']) + '.', '- Canonical proof: ' + pinned_link(s, {'commit': r['canonical_commit'], 'path': r['canonical_proof']}, r['canonical_proof']) + '.']
        for key in ('depends_on', 'supersedes', 'replaced_by'):
            survivors += ['- ' + key + ': ' + (', '.join(('`' + x + '`' for x in r[key])) if r[key] else '[]') + '.']
        survivors += ['- Claim polarity: `' + r['claim_polarity'] + '`.', '- Negative claim boundary: ' + r['negative_claim_boundary'], '', 'Aussage:', ''] + ['- ' + x for x in r['claim']]
        survivors += ['', 'Does not claim:', ''] + ['- ' + x for x in r['does_not_claim']]
        if r['reproduction_evidence']:
            survivors += ['', 'Dokumentierte Reproduktion: ' + ', '.join((pinned_link(s, e, Path(e['path']).name) for e in r['reproduction_evidence'])) + '.']
        survivors += ['']
    return {path: ('\n'.join(lines).rstrip() + '\n').encode('utf-8') for path, lines in zip(GENERATED, (current, gates, survivors))}

def validate_meta(meta, directory, root, known_ids):
    fields(meta, ('schema_version', 'id', 'date', 'kind', 'strategic', 'local_only', 'mathematical_status', 'review_status', 'integration_status', 'scope', 'claim_polarity', 'negative_claim_boundary', 'depends_on', 'closes', 'opens', 'supersedes', 'does_not_claim', 'canonical_proof'), 'META')
    require(type(meta['schema_version']) is int and meta['schema_version'] == 1, 'Unsupported META schema')
    require(isinstance(meta['id'], str) and ID.fullmatch(meta['id']), 'Invalid META ID')
    require(isinstance(meta['date'], str) and re.fullmatch('\\d{4}-\\d{2}-\\d{2}', meta['date']), 'Invalid META date')
    require(meta['kind'] in {'THEOREM', 'NO_GO', 'CONSTRUCTION', 'REDUCTION', 'DIAGNOSTIC'}, 'Unknown META kind')
    require(type(meta['strategic']) is bool and type(meta['local_only']) is bool and (meta['strategic'] != meta['local_only']), 'Choose strategic or local_only')
    require(meta['mathematical_status'] in STATUSES and meta['review_status'] == 'EXTERNAL_REVIEW_OPEN' and (meta['integration_status'] == 'RESEARCH_BRANCH_UNMERGED'), 'META cannot self-promote review or integration')
    string(meta['scope'], 'META scope')
    string(meta['negative_claim_boundary'], 'META negative claim boundary')
    require(meta['claim_polarity'] in POLARITY, 'Invalid META claim polarity')
    negative = meta['claim_polarity'] == 'NEGATIVE_FOR_CANDIDATE_CLASS'
    require(negative == (meta['kind'] == 'NO_GO') == (meta['mathematical_status'] == 'AUTHOR_DERIVED_NO_GO'), 'META no-go kind/status/polarity mismatch')
    for key in ('depends_on', 'closes', 'opens', 'supersedes', 'does_not_claim'):
        strings(meta[key], 'META ' + key, key == 'does_not_claim')
    require(not meta['strategic'] or bool(meta['closes'] + meta['opens'] + meta['supersedes']), 'Strategic META must declare closes, opens or supersedes')
    require(not meta['local_only'] or not meta['closes'] + meta['opens'] + meta['supersedes'], 'local_only cannot silently claim strategic gate changes')
    require(set(meta['depends_on'] + meta['closes'] + meta['opens'] + meta['supersedes']) <= known_ids, 'META effects/dependencies must be declared in the operative registry')
    proof = meta['canonical_proof']
    fields(proof, ('path', 'sha256'), 'META proof')
    relative(proof['path'])
    require(proof['path'] == directory + '/PROOF.md', 'META proof must be its own package PROOF.md')
    require(isinstance(proof['sha256'], str) and DIGEST.fullmatch(proof['sha256']), 'Invalid META proof hash')
    require((root / proof['path']).is_file(), 'Missing current META proof')
    require(hashlib.sha256((root / proof['path']).read_bytes()).hexdigest() == proof['sha256'], 'META proof hash mismatch')

def validate(root, base_ref=None):
    root = Path(root).resolve()
    paths = all_paths(root)
    require([p for p in paths if PurePosixPath(p).name.upper() == 'RESEARCH_STATE.YAML'] == [STATE], 'Exactly one canonical RESEARCH_STATE.yaml is required')
    s = load(root / STATE)
    result_ids, open_ids = validate_structure(s)
    for sha in (s['published_baseline']['sha'], s['live_frontier']['verified_through'], s['metadata_policy']['enforced_after']):
        git(root, 'cat-file', '-e', sha + '^{commit}')
    require(ancestor(root, s['metadata_policy']['enforced_after'], s['live_frontier']['verified_through']), 'Metadata enforcement anchor cannot move beyond verified_through')
    refs = [s['authority_roles'][key] for key in ('definition', 'review_rules')]
    for r in s['results']:
        refs.append({'commit': r['canonical_commit'], 'path': r['canonical_proof'], 'sha256': r['proof_sha256']})
        refs += r['reproduction_evidence']
        if r.get('external_review_evidence'):
            refs.append(r['external_review_evidence'])
        target = s['published_baseline']['sha'] if r['integration_status'] == 'MERGED' else s['live_frontier']['verified_through']
        require(ancestor(root, r['canonical_commit'], target), 'Result commit outside declared integration scope: ' + r['id'])
        if r['integration_status'] == 'RESEARCH_BRANCH_UNMERGED':
            require(not ancestor(root, r['canonical_commit'], s['published_baseline']['sha']), 'Result already included in the declared merged baseline: ' + r['id'])
    for commit in sorted({ref['commit'] for ref in refs}):
        git(root, 'cat-file', '-e', commit + '^{commit}')
    for ref in refs:
        raw = git_blob(root, ref['commit'], ref['path'])
        require(hashlib.sha256(raw).hexdigest() == ref['sha256'], 'Pinned evidence hash mismatch: ' + ref['path'])
    for path, expected in render(s).items():
        require((root / path).is_file() and (root / path).read_bytes() == expected, 'Generated file differs: ' + path)
    historical = {h['path'] for h in s['historical_navigation']}
    exceptions = {e['path'] for e in s['navigation_exceptions']}
    for h in s['historical_navigation']:
        raw = git_blob(root, h['content_commit'], h['path'])
        require(hashlib.sha256(raw).hexdigest() == h['content_sha256'], 'Historical original hash mismatch')
        require((root / h['path']).read_bytes() == banner(s, h) + raw, 'Historical banner/original bytes changed: ' + h['path'])
    for path in paths:
        p = PurePosixPath(path)
        nav_scope = len(p.parts) == 1 or p.parts[0] in {'00-uebersicht', '00-grundlegung'}
        named = any((x in p.name.upper() for x in ('CURRENT', 'ACTIVE', 'AKTUELL')))
        if nav_scope and named and (p.suffix in {'.md', '.yaml', '.yml'}) and (path not in GENERATED):
            require(path in historical or path in exceptions, 'Unclassified current/active navigation: ' + path)
    for e in s['navigation_exceptions']:
        require(e['path'] in paths, 'Missing navigation exception path')
    before = proof_paths(tree_paths(root, s['metadata_policy']['enforced_after']))
    now = proof_paths(paths)
    pending = {p['id']: p for p in s['pending_packages']}
    meta_ids = set()
    for directory in sorted(now - before):
        path = directory + '/META.yaml'
        require(path in paths and (root / path).is_file(), 'New research package requires META.yaml: ' + directory)
        meta = load(root / path)
        validate_meta(meta, directory, root, result_ids | open_ids)
        require(meta['id'] not in meta_ids, 'Duplicate new META ID')
        meta_ids.add(meta['id'])
        registered = [r for r in s['results'] if str(PurePosixPath(r['canonical_proof']).parent) == directory]
        require(meta['local_only'] or registered or (meta['id'] in pending and pending[meta['id']]['meta_path'] == path), 'New strategic package missing from registered or pending status: ' + directory)
    require(set(pending) <= meta_ids, 'Pending entry has no new META package')
    if base_ref:
        require(re.fullmatch('[0-9a-f]{40}', base_ref) is not None, 'base-ref must be a full commit SHA')
        previous = git_blob(root, base_ref, STATE, missing_ok=True)
        if previous is not None:
            old = json.loads(previous, object_pairs_hook=unique_object)
            require(old['metadata_policy']['enforced_after'] == s['metadata_policy']['enforced_after'], 'Cannot reset metadata enforcement to grandfather new packages')
        generated_changed = any((git_blob(root, base_ref, p, missing_ok=True) != (root / p).read_bytes() for p in GENERATED))
        require(not generated_changed or previous != (root / STATE).read_bytes(), 'Generated Markdown changed without a state change')
    return {'results': len(s['results']), 'evidence_refs': len(refs), 'historical_banners': len(historical), 'new_metadata_packages': len(meta_ids), 'verified_through': s['live_frontier']['verified_through']}
