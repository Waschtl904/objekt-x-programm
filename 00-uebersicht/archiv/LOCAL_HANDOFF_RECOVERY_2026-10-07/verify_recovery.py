"""Verify historical source bytes. Does not execute or validate research code."""
from pathlib import Path
from functools import lru_cache
import argparse
import hashlib
import io
import json
import re
import subprocess
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EXPECTED_CATALOG_SHA256 = 'c425c9bc37523b253e6ecaa7d8af762645d674fd9a9e03212beb45b45a135296'


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def verify(originals=None):
    catalog_bytes = (HERE / 'CATALOG.json').read_bytes()
    if sha256(catalog_bytes) != EXPECTED_CATALOG_SHA256:
        raise ValueError('Frozen catalog binding mismatch')
    catalog = json.loads(catalog_bytes)
    commit = catalog['base_main']
    if not re.fullmatch('[0-9a-f]{40}', commit):
        raise ValueError('Invalid baseline commit')
    archive = (HERE / 'recovered-sources.zip').read_bytes()
    binding = catalog['recovery_archive']
    if sha256(archive) != binding['sha256'] or len(archive) != binding['bytes']:
        raise ValueError('Recovery archive binding mismatch')
    recovered = {}
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        for info in z.infolist():
            if not re.fullmatch(r'files/[0-9a-f]{64}', info.filename):
                raise ValueError('Unexpected recovery member')
            data = z.read(info)
            sha = info.filename.split('/')[1]
            if sha256(data) != sha or sha in recovered:
                raise ValueError('Recovery member hash or uniqueness mismatch')
            recovered[sha] = data

    @lru_cache(None)
    def base_bytes(location):
        if '!' in location:
            outer, member = location.rsplit('!', 1)
            with zipfile.ZipFile(io.BytesIO(base_bytes(outer))) as z:
                return z.read(member)
        if location.startswith('/') or '..' in location.split('/'):
            raise ValueError('Invalid repository location')
        return subprocess.check_output(
            ['git', '-C', str(ROOT), 'show', commit + ':' + location]
        )

    used = set()
    visited = set()

    def check(entry, ancestors=()):
        sha = entry['sha256']
        if not re.fullmatch('[0-9a-f]{64}', sha):
            raise ValueError('Invalid source digest')
        storage = entry['storage']
        if storage == 'CONTAINER_CATALOG':
            if sha in ancestors or entry['container'] != sha:
                raise ValueError('Invalid or cyclic container reference')
            container = catalog['containers'][sha]
            if entry['bytes'] != container['original_zip_bytes']:
                raise ValueError('Container size mismatch')
            if sha not in visited:
                for member in container['files']:
                    check(member, ancestors + (sha,))
                visited.add(sha)
            return
        if storage == 'BASE_MAIN':
            # One verified location suffices; further locations are duplicate copies.
            data = base_bytes(entry['locations'][0])
        elif storage == 'RECOVERED_BYTES':
            if entry['path'] != 'files/' + sha:
                raise ValueError('Invalid recovered path')
            data = recovered[sha]
            used.add(sha)
        else:
            raise ValueError('Unknown storage type')
        if sha256(data) != sha or len(data) != entry['bytes']:
            raise ValueError('Source member binding mismatch')

    for source in catalog['sources'] + catalog['local_commit_sources'] + catalog['standalone_notes']:
        check(source)
    counts = {
        'source_archives': len(catalog['sources']),
        'local_commit_files': len(catalog['local_commit_sources']),
        'standalone_notes': len(catalog['standalone_notes']),
        'exact_archive_instances_in_main': sum(s['storage'] == 'BASE_MAIN' for s in catalog['sources']),
        'catalogued_unique_containers': len(visited),
        'recovered_unique_files': len(recovered),
        'recovered_file_bytes': sum(map(len, recovered.values())),
    }
    if used != set(recovered) or visited != set(catalog['containers']) or counts != catalog['counts']:
        raise ValueError('Coverage or count mismatch')

    checked_containers = set()
    if originals is not None:
        # The local map contains original outer ZIP digest -> filename.
        # It is an input locator, not trusted evidence: every ZIP is hashed.
        paths = json.loads(Path(originals).read_text(encoding='utf-8'))

        def check_original(data, expected_sha):
            if sha256(data) != expected_sha:
                raise ValueError('Original ZIP digest mismatch')
            if expected_sha not in catalog['containers'] or expected_sha in checked_containers:
                return
            container = catalog['containers'][expected_sha]
            if len(data) != container['original_zip_bytes']:
                raise ValueError('Original ZIP size mismatch')
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                members = [i for i in z.infolist() if not i.is_dir()]
                expected = container['files']
                if [i.filename for i in members] != [e['member_path'] for e in expected]:
                    raise ValueError('Original ZIP complete member list mismatch')
                for info, entry in zip(members, expected):
                    member = z.read(info)
                    if sha256(member) != entry['sha256'] or len(member) != entry['bytes']:
                        raise ValueError('Original ZIP member binding mismatch')
                    if entry['storage'] == 'CONTAINER_CATALOG':
                        check_original(member, entry['sha256'])
            checked_containers.add(expected_sha)

        for source in catalog['sources']:
            if source['storage'] == 'CONTAINER_CATALOG':
                check_original(Path(paths[source['sha256']]).read_bytes(), source['sha256'])
        if checked_containers != set(catalog['containers']):
            raise ValueError('Original ZIP coverage mismatch')
    print(json.dumps({'status': 'PASS_SOURCE_BYTES', 'base_main': commit,
                      **counts, 'catalog_sha256': EXPECTED_CATALOG_SHA256,
                      'original_containers_verified': len(checked_containers),
                      'original_container_bytes_verified': originals is not None,
                      'mathematical_replay_performed': False}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--originals', type=Path, help='JSON map: original outer ZIP SHA-256 to local filename')
    verify(parser.parse_args().originals)
