"""Bounded replay of sealed certificates; no new operator integration."""
from pathlib import Path, PurePosixPath
import argparse
import fnmatch
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
REL = HERE.relative_to(REPO).as_posix()
WORKFLOW = '.github/workflows/a8-a9-remainder-progress.yml'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_path(root, name):
    p = PurePosixPath(name)
    assert name and '\\' not in name and ':' not in name and not p.is_absolute(), name
    assert all(x not in ('', '.', '..') for x in name.split('/')), name
    dest = root.joinpath(*p.parts)
    assert dest.resolve().is_relative_to(root.resolve()) and not dest.is_symlink(), name
    return dest


def verify_files(root, spec):
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    assert actual == set(spec['files']), 'closed extracted tree'
    for name, sha in spec['files'].items():
        assert digest(safe_path(root, name).read_bytes()) == sha, name
    manifest = {}
    for line in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        sha, name = line.split('  ', 1)
        assert name not in manifest, 'duplicate manifest member'
        manifest[name] = sha
        assert digest(safe_path(root, name).read_bytes()) == sha, name
    assert set(spec['files']) == set(manifest) | {'SHA256SUMS'}, 'closed manifest'


def extract(archive, root, spec):
    assert digest(archive.read_bytes()) == spec['archive_sha256'], 'archive hash'
    prefix = spec['prefix']
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        assert len(names) == len(set(names)), 'duplicate ZIP member'
        assert set(names) == {prefix+n for n in spec['files']}, 'archive members'
        assert z.testzip() is None, 'archive CRC'
        for name, sha in spec['files'].items():
            dest = safe_path(root, name)
            info = z.getinfo(prefix+name)
            assert (info.external_attr >> 16) & 0o170000 != 0o120000, 'archive symlink'
            raw = z.read(info)
            assert digest(raw) == sha, 'file hash'
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(raw)
    verify_files(root, spec)


def execute(command, log, env):
    with log.open('wb') as stream:
        result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, env=env)
    assert result.returncode == 0, 'Checker failed: '+str(log)


def controls():
    rejected = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name in ('../escape', '/absolute', 'x/../escape', 'x\\escape', 'C:escape'):
            try:
                safe_path(root, name)
            except AssertionError:
                rejected.append(name)
            else:
                raise AssertionError('unsafe path accepted')
        data = b'bound input\n'
        manifest = (digest(data)+'  data.txt\n').encode()
        archive = root/'tiny.zip'
        with zipfile.ZipFile(archive, 'w') as z:
            z.writestr('data.txt', data)
            z.writestr('SHA256SUMS', manifest)
        spec = {'prefix':'', 'archive_sha256':digest(archive.read_bytes()),
                'files':{'data.txt':digest(data), 'SHA256SUMS':digest(manifest)}}
        extract(archive, root/'valid', spec)
        for kind in ('archive_hash', 'file_hash', 'members'):
            bad = json.loads(json.dumps(spec))
            if kind == 'archive_hash':
                bad['archive_sha256'] = '0'*64
            elif kind == 'file_hash':
                bad['files']['data.txt'] = '0'*64
            else:
                bad['files']['missing.txt'] = '0'*64
            try:
                extract(archive, root/kind, bad)
            except AssertionError:
                rejected.append(kind)
            else:
                raise AssertionError('damaged binding accepted')
        try:
            execute([sys.executable, '-c', 'raise SystemExit(7)'], root/'failure.log', os.environ)
        except AssertionError:
            rejected.append('failed_checker')
        else:
            raise AssertionError('failed checker accepted')
    workflow = (REPO/WORKFLOW).read_text(encoding='utf-8')
    patterns = [REL+'/**', WORKFLOW]
    found = [line.strip()[3:-1] for line in workflow.splitlines() if line.strip().startswith('- "')]
    assert found == patterns+patterns
    routed = lambda name: any(fnmatch.fnmatchcase(name, p) for p in patterns)
    assert routed(REL+'/replay.py') and routed(REL+'/archives/certificate.zip')
    assert routed(REL+'/packages/domain/LEMMATA.txt') and routed(WORKFLOW)
    assert not routed('README.md') and not routed('00-uebersicht/RESEARCH_STATE.yaml')
    assert 'pull_request:' in workflow and 'branches: [main]' in workflow
    assert 'github.event.pull_request.head.sha || github.sha' in workflow
    assert workflow.index('core.autocrlf false') < workflow.index('actions/checkout@')
    return {'valid_archive_accepted':True, 'rejected_controls':rejected, 'ci_routing':'PASS'}


def dependency_checks(roots, binding):
    checks = []
    def equal(left, right):
        assert left.read_bytes() == right.read_bytes(), (left, right)
        base = roots['eight-source'].parent
        checks.append({'left':left.relative_to(base).as_posix(),
                       'right':right.relative_to(base).as_posix() if right.is_relative_to(base) else right.relative_to(REPO).as_posix(),
                       'sha256':digest(left.read_bytes())})
    old = REPO/'research/x-c1/a8-four-source-inverse-energy-2026-10-04/inputs/ObjektX_A8_Inverse_Energie_2026-10-04.zip'
    equal(roots['eight-source']/'inputs/ObjektX_A8_Inverse_Energie_2026-10-04.zip', old)
    equal(roots['remainder']/'inputs/EIGHT_SOURCE_PROOF.txt', roots['eight-source']/'PROOF.txt')
    equal(roots['remainder']/'inputs/EIGHT_SOURCE_REMAINDER_CANDIDATE.txt', roots['eight-source']/'REMAINDER_CANDIDATE.txt')
    # This is the compact review package's source map, not a copy of the
    # full package's differently structured SOURCE_BINDINGS.json.
    compact = json.loads((roots['remainder']/'inputs/EIGHT_SOURCE_SOURCE_BINDINGS.json').read_bytes())
    assert compact['source_main'] == binding['source_main']
    assert compact['full_package_zip_sha256'] == binding['packages']['eight-source']['archive_sha256']
    for row in compact['original_results']:
        assert digest((roots['eight-source']/f"expected/{row['bits']}/RESULT.json").read_bytes()) == row['original_result_sha256']
    for name, sha in compact['copies'].items():
        assert digest(safe_path(roots['eight-source'], name).read_bytes()) == sha
    checks.append({'kind':'compact_eight_source_map','package_and_result_hashes_match':True})
    equal(roots['domain']/'inputs/Objekt-X-A8-A9-Vollstaendiger-Rest-2026-10-05.zip', HERE/binding['packages']['remainder']['archive'])
    equal(roots['pilot']/'inputs/Objekt-X-Rest-Domaene-Kompaktheit-2026-10-06.zip', HERE/binding['packages']['domain']['archive'])
    equal(roots['pilot']/'inputs/QUOTIENT_NORM.json', roots['eight-source']/'QUOTIENT_NORM.json')
    for name, key, source in [
        ('DOMAIN_LEMMATA.txt','domain','LEMMATA.txt'),
        ('GEOMETRY_1024.json','pilot','GEOMETRY_1024.json'),
        ('PROTOCOL.json','pilot','PROTOCOL.json'),
        ('PROTOKOLL.txt','pilot','PROTOKOLL.txt'),
        ('REMAINDER_PROOF.txt','remainder','BEWEIS.txt')]:
        equal(roots['half-inverse']/'inputs'/name, roots[key]/source)
    for name, key, source in [
        ('FULL_REMAINDER_PROOF.txt','remainder','BEWEIS.txt'),
        ('HALF_1536.json','half-inverse','expected/1536.json'),
        ('HALF_INVERSE_DERIVATION.txt','half-inverse','HERLEITUNG.txt'),
        ('A8_PROOF.md','remainder','inputs/A8_PROOF.md')]:
        equal(roots['weighted-response']/'inputs'/name, roots[key]/source)
    assert digest((roots['weighted-response']/'inputs/a8_model.json.gz').read_bytes()) == '5f8935d53f8518540ef25e6f2d511955bad688cf5905cb63e8d89f03aae2474b'
    state = json.loads((roots['weighted-response']/'PILOT_STATE.json').read_bytes())
    assert state['frozen_new_pilot_dimension_per_parity'] == 8
    assert not state['new_pilot_geometry_changed'] and not state['full_remainder_certified']
    for key in ('U00','G01','gamma01','beta_tail','eta','alpha','six_sensitive_force_error_gram','four_C_coupling_error_gram'):
        assert state[key] is None, key
    return checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path)
    ap.add_argument('--controls-only', action='store_true')
    args = ap.parse_args()
    assert __debug__
    checked = controls()
    if args.controls_only:
        print(json.dumps(checked))
        return
    assert args.output
    out = args.output.resolve()
    assert not out.exists() and not out.is_relative_to(REPO)
    out.mkdir(parents=True)
    binding = json.loads((HERE/'SOURCE_BINDINGS.json').read_bytes())
    roots = {}
    for key, spec in binding['packages'].items():
        roots[key] = out/'originals'/key
        extract(safe_path(HERE, spec['archive']), roots[key], spec)
        for name, row in spec['visible_copies'].items():
            raw = safe_path(HERE, name).read_bytes()
            assert digest(raw) == row['sha256']
            assert raw == safe_path(roots[key], row['source']).read_bytes(), name
    dependencies = dependency_checks(roots, binding)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
    records = []

    def run(key, script, extra, expected, emitted=None):
        log = out/(key+'.log')
        execute([sys.executable, '-B', str(roots[key]/script)]+list(map(str, extra)), log, env)
        result_path = emitted or log
        actual = json.loads(result_path.read_bytes())
        assert actual == json.loads((roots[key]/expected).read_bytes()), key+' expected result'
        if emitted is None:
            (out/(key+'.json')).write_bytes(log.read_bytes())
        records.append({'package':key, 'status':actual['status'], 'saved_result_reproduced':True,
                        'sha256':digest(result_path.read_bytes())})
        print(key+': PASS', flush=True)

    r = roots['eight-source']
    run('eight-source', 'code/audit_eight.py',
        ['--primary',r/'expected/3072/RESULT.json','--higher',r/'expected/4096/RESULT.json','--out',out/'eight-source.json'],
        'EXACT_CHECK.json',out/'eight-source.json')
    run('remainder','check_remainder.py',[],'CHECK_RESULT.json')
    run('pilot','check_geometry.py',[],'EXACT_GEOMETRY_CHECK.json')
    run('half-inverse','check_half_inverse.py',[],'EXACT_CHECK.json')
    run('weighted-response','check_weighted_response.py',
        ['--out',out/'weighted-response.json','--majorant-out',out/'RATIONAL_MAJORANT.json'],
        'EXACT_CHECK.json',out/'weighted-response.json')
    assert json.loads((out/'RATIONAL_MAJORANT.json').read_bytes()) == json.loads((roots['weighted-response']/'RATIONAL_MAJORANT.json').read_bytes())
    for key, spec in binding['packages'].items():
        verify_files(roots[key], spec)
        assert digest((HERE/spec['archive']).read_bytes()) == spec['archive_sha256']
    head = subprocess.check_output(['git','-c','safe.directory='+REPO.as_posix(),'-C',str(REPO),'rev-parse','HEAD']).decode().strip()
    record = {'status':'PASS_BOUNDED_CERTIFICATE_REPLAY','integration_commit':head,
        'source_main':binding['source_main'],'source_bindings_sha256':digest((HERE/'SOURCE_BINDINGS.json').read_bytes()),
        'archives':{key:spec['archive_sha256'] for key,spec in binding['packages'].items()},
        'original_files_checked':sum(len(x['files']) for x in binding['packages'].values()),
        'archives_and_original_files_preserved':True,'visible_copies_byte_identical':True,
        'publication_controls':checked,'dependency_checks':dependencies,'certificate_checks':records,
        'rational_majorant_reproduced':True,'analytic_domain_lemmas_machine_verified':False,
        'new_operator_integrations_performed':False,'full_numerical_replay_performed':False,
        'full_remainder_certified':False,'external_review':'OPEN',
        'U00':None,'G01':None,'gamma01':None,'beta_tail':None,'eta':None,'alpha':None}
    (out/'REPLAY.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('BOUNDED REMAINDER CERTIFICATE REPLAY PASS', flush=True)


if __name__ == '__main__':
    main()
