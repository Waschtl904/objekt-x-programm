"""Publish and replay the unchanged four-source inverse-energy package."""
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


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def safe_path(root, name):
    p = PurePosixPath(name)
    assert name and '\\' not in name and ':' not in name and not p.is_absolute(), name
    assert all(x not in ('', '.', '..') for x in name.split('/')), name
    target = root.joinpath(*p.parts)
    assert target.resolve().is_relative_to(root.resolve()) and not target.is_symlink(), name
    return target


def extract(archive, target, binding):
    assert digest(archive.read_bytes()) == binding['archive_sha256'], 'archive hash'
    prefix = binding['folder'] + '/'
    with zipfile.ZipFile(archive) as z:
        expected = {prefix + name for name in binding['files']}
        assert len(z.namelist()) == len(expected) and set(z.namelist()) == expected, 'archive members'
        assert z.testzip() is None, 'archive CRC'
        for name, expected_hash in binding['files'].items():
            p = safe_path(target, name)
            info = z.getinfo(prefix + name)
            assert (info.external_attr >> 16) & 0o170000 != 0o120000, 'archive symlink'
            raw = z.read(prefix + name)
            assert digest(raw) == expected_hash, 'file hash: ' + name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw)
    manifest = {}
    for line in (target/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        sha, name = line.split('  ', 1)
        assert name not in manifest
        manifest[name] = sha
        assert digest(safe_path(target,name).read_bytes()) == sha
    assert set(binding['files']) == set(manifest) | {'SHA256SUMS'}, 'closed manifest'


def controls():
    rejected = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name in ('../escape', '/absolute', 'x/../escape', 'x\\escape', 'C:escape'):
            try:
                safe_path(root,name)
            except AssertionError:
                rejected.append(name)
            else:
                raise AssertionError('unsafe path accepted: '+name)
        raw = b'bound input\n'
        manifest = (digest(raw)+'  data.txt\n').encode()
        archive = root/'tiny.zip'
        with zipfile.ZipFile(archive,'w') as z:
            z.writestr('original/data.txt',raw)
            z.writestr('original/SHA256SUMS',manifest)
        spec = {'folder':'original','archive_sha256':digest(archive.read_bytes()),
                'files':{'data.txt':digest(raw),'SHA256SUMS':digest(manifest)}}
        extract(archive,root/'valid',spec)
        for kind in ('archive_hash','file_hash','members'):
            bad = json.loads(json.dumps(spec))
            if kind == 'archive_hash':
                bad['archive_sha256'] = '0'*64
            elif kind == 'file_hash':
                bad['files']['data.txt'] = '0'*64
            else:
                bad['files']['missing.txt'] = '0'*64
            try:
                extract(archive,root/kind,bad)
            except AssertionError:
                rejected.append(kind)
            else:
                raise AssertionError('damaged binding accepted: '+kind)
    workflow = (REPO/'.github/workflows/a8-four-source-inverse-energy.yml').read_text(encoding='utf-8')
    patterns = ['research/x-c1/a8-four-source-inverse-energy-2026-10-04/**',
                '.github/workflows/a8-four-source-inverse-energy.yml']
    found = [line.strip()[3:-1] for line in workflow.splitlines() if line.strip().startswith('- "')]
    assert found == patterns + patterns
    routed = lambda name:any(fnmatch.fnmatchcase(name,p) for p in patterns)
    assert routed(patterns[0][:-2]+'replay.py')
    assert routed(patterns[0][:-2]+'inputs/certificate.zip')
    assert routed(patterns[1])
    assert not routed('README.md') and not routed('00-uebersicht/RESEARCH_STATE.yaml')
    assert 'pull_request:' in workflow and 'branches: [main]' in workflow
    assert 'github.event.pull_request.head.sha || github.sha' in workflow
    assert workflow.index('core.autocrlf false') < workflow.index('actions/checkout@')
    assert len(rejected) == 8
    return {'valid_archive_accepted':True,'rejected_controls':rejected,'ci_routing':'PASS'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output',type=Path)
    ap.add_argument('--deps',type=Path,help='Optional existing python-flint package directory')
    ap.add_argument('--controls-only',action='store_true')
    args = ap.parse_args()
    assert __debug__
    checked = controls()
    if args.controls_only:
        print(json.dumps(checked))
        return
    assert args.output
    out = args.output.resolve()
    assert not out.exists() and not out.is_relative_to(REPO.resolve())
    binding = json.loads((HERE/'SOURCE_BINDINGS.json').read_bytes())
    out.mkdir(parents=True)
    original = out/'original'
    archive = safe_path(HERE,binding['archive'])
    extract(archive,original,binding)
    for name,row in binding['visible_copies'].items():
        raw = safe_path(HERE,name).read_bytes()
        assert digest(raw) == row['sha256']
        assert raw == safe_path(original,row['source']).read_bytes(),name
    env = dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONIOENCODING='utf-8')
    command = [sys.executable,'-B',str(original/'reproduce.py'),'--out',str(out/'calculation'),'--second-precision']
    if args.deps:
        command.extend(['--deps',str(args.deps.resolve())])
    with (out/'reproduce.log').open('wb') as log:
        proc = subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,env=env)
    assert proc.returncode == 0,'Original replay failed; inspect logs'
    replay = json.loads((out/'calculation/REPRODUCTION.json').read_bytes())
    assert replay['status'] == 'PASS' and replay['mixed_4096_recomputed_this_run']
    assert replay['manifest_unchanged_after_run'] and replay['bound_package_files'] == 31
    assert replay['exact_floor_checks_passed'] and replay['exact_gamma_controls'] == 36
    assert digest(archive.read_bytes()) == binding['archive_sha256']
    for name,sha in binding['files'].items():
        assert digest(safe_path(original,name).read_bytes()) == sha
    head = subprocess.check_output(['git','-c','safe.directory='+REPO.as_posix(),'-C',str(REPO),'rev-parse','HEAD']).decode().strip()
    record = {'status':'PASS','integration_commit':head,'source_head':binding['source_head'],
              'source_binding_sha256':digest((HERE/'SOURCE_BINDINGS.json').read_bytes()),
              'original_archive_sha256':binding['archive_sha256'],
              'original_archive_preserved':True,'original_files_checked':len(binding['files']),
              'visible_copies_byte_identical':True,'publication_controls':checked,
              'reproduction':replay,'schur_coefficient_floors':{'even':'1/100000','odd':'33/1000000'},
              'target_positivity_used':False,'full_new_quotient_covered':False,
              'scope':'New complete mixed pairings and energy bounds replayed; inherited form identities and original models remain source-bound. External review open.'}
    (out/'REPLAY.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('FOUR-SOURCE INVERSE-ENERGY REPLAY PASS',flush=True)


if __name__ == '__main__':
    main()
