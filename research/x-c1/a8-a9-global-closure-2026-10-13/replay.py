"""Preserve complete source ZIP bytes and replay the conditional Schur closure.

Only the Python standard library is required. Large analytic integrations
are bound inputs; the full saved rational certificate chain is executed.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import zipfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
FINAL = '65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba'
REVIEW = '6b29274d3eadf5ca0c97c65176bc20dfb9cfff42f9b36739028674edb14469d8'

def require(condition, message):
    if not condition:
        raise ValueError(message)

def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def read(path):
    return json.loads(Path(path).read_bytes())

def safe_path(root, name):
    require(isinstance(name, str) and bool(name), 'empty path')
    p = PurePosixPath(name)
    require(not p.is_absolute() and '\\' not in name and ':' not in name,
            'nonportable or absolute path: '+name)
    require(all(x not in ('', '.', '..') for x in name.split('/')),
            'noncanonical path: '+name)
    dest = Path(root).joinpath(*p.parts)
    require(dest.resolve().is_relative_to(Path(root).resolve()), 'path escape')
    require(not dest.is_symlink(), 'symlink destination')
    return dest

def verify_archive(path, obj):
    require(path.stat().st_size == obj['bytes'] and sha(path) == obj['sha256'],
            'original archive bytes differ: '+obj['name'])
    expected = {r['name']: r for r in obj['members']}
    require(len(expected) == len(obj['members']), 'duplicate catalog member')
    with zipfile.ZipFile(path) as z:
        entries = [r for r in z.infolist() if not r.is_dir()]
        require(len(entries) == len({r.filename for r in entries}), 'duplicate ZIP member')
        require({r.filename for r in entries} == set(expected), 'incomplete ZIP member catalog')
        for info in entries:
            row = expected[info.filename]
            require(info.file_size == row['bytes'], 'member length')
            with z.open(info) as stream:
                digest = hashlib.file_digest(stream, 'sha256').hexdigest()
            require(digest == row['sha256'], 'member hash: '+info.filename)

def materialize(catalog, out, package=HERE):
    objects = catalog['objects']
    done = {}; active = set()
    cache = out/'containers'; cache.mkdir(parents=True)

    def obtain(h):
        if h in done:
            return done[h]
        require(h in objects and h not in active, 'missing or cyclic source container')
        active.add(h); obj = objects[h]
        require(h == obj['sha256'], 'object key/hash mismatch')
        target = safe_path(cache, h+'.zip')
        require(('chunks' in obj) != ('nested_sources' in obj), 'ambiguous storage')
        if 'chunks' in obj:
            require(bool(obj['chunks']), 'empty chunks')
            with target.open('wb') as dest:
                for row in obj['chunks']:
                    part = safe_path(package, row['path'])
                    require(part.stat().st_size == row['bytes'] and sha(part) == row['sha256'],
                            'archive chunk mismatch')
                    with part.open('rb') as src:
                        shutil.copyfileobj(src, dest)
        else:
            require(bool(obj['nested_sources']), 'empty nested sources')
            source = obj['nested_sources'][0]
            parent = obtain(source['container'])
            with zipfile.ZipFile(parent) as z, z.open(source['member']) as src, target.open('wb') as dest:
                shutil.copyfileobj(src, dest)
        verify_archive(target, obj)
        active.remove(h); done[h] = target
        return target

    for h in sorted(objects):
        obtain(h)
    # Check every cataloged containment edge, not just the chosen storage edge.
    for h, obj in objects.items():
        for source in obj.get('nested_sources', []):
            with zipfile.ZipFile(done[source['container']]) as z, z.open(source['member']) as stream:
                require(hashlib.file_digest(stream, 'sha256').hexdigest() == h,
                        'alternate nested source mismatch')
    originals = out/'originals'; originals.mkdir()
    require(len({r['name'] for r in catalog['imports']}) == len(catalog['imports']),
            'duplicate import name')
    for row in catalog['imports']:
        require(row['bytes'] == objects[row['sha256']]['bytes'], 'import length')
        target = safe_path(originals, row['name'])
        require(target.parent == originals, 'import name must be a basename')
        try:
            os.link(done[row['sha256']], target)
        except OSError:
            shutil.copyfile(done[row['sha256']], target)
    for name, row in catalog['visible_copies'].items():
        target = safe_path(package, name)
        require(target.stat().st_size == row['bytes'] and sha(target) == row['sha256'],
                'readable copy differs: '+name)
        with zipfile.ZipFile(done[row['container_sha256']]) as z:
            require(target.read_bytes() == z.read(row['member']), 'source/copy mismatch')
    for row in catalog['standalone']:
        target = safe_path(package, row['path'])
        require(target.stat().st_size == row['bytes'] and sha(target) == row['sha256'],
                'standalone file mismatch')
    return done

def extract(archive, target):
    with zipfile.ZipFile(archive) as z:
        require(len(z.namelist()) == len(set(z.namelist())), 'duplicate ZIP path')
        for info in z.infolist():
            name = info.filename.rstrip('/') if info.is_dir() else info.filename
            dest = safe_path(target, name)
            require(((info.external_attr >> 16) & 0o170000) != 0o120000, 'ZIP symlink')
            if info.is_dir():
                dest.mkdir(parents=True, exist_ok=True)
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                with z.open(info) as src, dest.open('wb') as out:
                    shutil.copyfileobj(src, out)

def execute(command, log, marker):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
    with log.open('wb') as stream:
        result = subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, env=env)
    require(result.returncode == 0, 'checker failed; see '+str(log))
    require(marker in log.read_text(encoding='utf-8'), 'checker completion marker missing')

def main():
    require(__debug__, 'Run without Python optimization flags')
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--sources-only', action='store_true', help='Archive check only; no mathematical replay claim')
    args = ap.parse_args()
    out = args.output.resolve()
    require(not out.exists() and not out.is_relative_to(REPO), 'Use a new directory outside the repository')
    out.mkdir(parents=True)
    wanted, filename = (HERE/'SOURCE_BINDINGS.sha256').read_text().strip().split('  ')
    require(filename == 'SOURCE_BINDINGS.json' and sha(HERE/filename) == wanted, 'catalog binding')
    catalog = read(HERE/filename)
    paths = materialize(catalog, out)
    print('PASS all original archives, members, containment edges and readable copies', flush=True)
    result = {'status': 'PASS_SOURCE_ARCHIVE_RECONSTRUCTION', 'source_catalog_sha256': wanted,
              'counts': catalog['counts'], 'full_rational_chain_repeated': False,
              'large_global_integrations_repeated': False}
    if not args.sources_only:
        work = out/'work'; work.mkdir()
        extract(paths[FINAL], work); extract(paths[REVIEW], work)
        final = work/'Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13'
        review = work/'Objekt-X-Schurabschluss-Gegenpruefung-und-Reserve-2026-10-13'
        print('RUN full rational predecessor chain and final Schur assembly', flush=True)
        execute([sys.executable, '-u', '-B', str(final/'reproduce.py'),
                 '--receipt', str(out/'FULL_CHAIN.json')], out/'FULL_CHAIN.log',
                'PASS_FRESH_FINAL_SCHUR_ASSEMBLY')
        full = read(out/'FULL_CHAIN.json')
        require(full['full_bound_input_replays_performed'] and
                len(full['completed_replays']) == 4, 'incomplete full chain')
        require(full == read(review/'OUR_FULL_CHAIN_REPLAY.json'), 'bound full-chain result differs')
        print('PASS full rational predecessor chain and final Schur assembly', flush=True)
        execute([sys.executable, '-u', '-B', str(review/'reproduce_review.py'),
                 '--input-zip', str(paths[FINAL]), '--receipt', str(out/'RESERVE_REVIEW.json')],
                out/'RESERVE_REVIEW.log', 'PASS_SCHUR_COUNTERREVIEW_PACKAGE')
        result.update(status='PASS_CONDITIONAL_A8_A9_INTEGRATION_REPLAY',
                      full_rational_chain_repeated=True,
                      full_chain=full, reserve_review=read(out/'RESERVE_REVIEW.json'),
                      conditional_A8_to_A9_positivity_confirmed=True,
                      inherited_operator_domain_decomposition_hypotheses_required=True,
                      tail_floor_1_over_20_certified=False, all_horizons_certified=False,
                      object_X_constructed=False, RH_proved=False,
                      external_mathematical_review_open=True)
    expected = HERE/'reports/ACCEPTANCE.json'
    if not args.sources_only and expected.exists():
        require(result == read(expected), 'commit-bound integration receipt differs')
    (out/'ACCEPTANCE.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('ACCEPTANCE_SHA256', sha(out/'ACCEPTANCE.json'), flush=True)
    print(result['status'], flush=True)

if __name__ == '__main__':
    main()
