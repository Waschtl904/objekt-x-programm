#!/usr/bin/env python3
"""Route the frozen C-even gate using committed provenance, never a cache hit.

Only stdlib and Git are used. Numerical sources are inspected as bytes, never
imported. A changed/missing dependency requests a fresh run; corrupt historical
evidence fails the gate. A PR cannot approve its own new reuse policy.
"""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

WORKFLOW = '.github/workflows/a1-c-even-exact-matrix-build.yml'
DIRECTORY = '.github/certificates/a1-c-even/'
MANIFEST = DIRECTORY + 'manifest.json'
SCRIPT = 'scripts/a1_certificate_reuse.py'
TEST = 'tests/test_a1_certificate_reuse.py'
JOBS = ('exact-matrix-build', 'exact-artifact-spd-ldl', 'manual-eigenvalue-audit')
MATRIX = '97b761e9f89517303f557d3c18061cc1b232c821e5804fcf9071298e17e60183'
CERTIFICATES = {
    'build.txt': (
        'MATRIX_SHA256=' + MATRIX,
        'CERTIFIED: exact C-even integer matrix artifact round-trip matches frozen fingerprint',
    ),
    'ldl.txt': (
        'MATRIX_SHA256=' + MATRIX,
        'CERTIFIED: exact hash-fixed 1075x1075 C-even integer matrix is positive definite by Arb LDL',
        'CERTIFIED: A_e >= 1e-35 I_1075 after the frozen finite-model ledger',
    ),
    'gate.txt': ('CERTIFIED: A1-relevant PR passed fresh build, fingerprint and rigorous LDL',),
}


class InvalidEvidence(ValueError):
    pass


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], check=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def commit(root, ref):
    if not re.fullmatch(r'[0-9a-f]{40}', ref):
        raise InvalidEvidence('a full commit SHA is required')
    if git(root, 'rev-parse', '--verify', ref + '^{commit}').decode().strip() != ref:
        raise InvalidEvidence('commit identity mismatch')
    return ref


def tree(root, ref):
    result = {}
    for entry in git(root, 'ls-tree', '-r', '-z', ref).split(b'\0'):
        if entry:
            header, name = entry.split(b'\t', 1)
            mode, kind, oid = header.decode('ascii').split()
            result[name.decode('utf-8')] = (mode, kind, oid)
    return result


def read(root, entries, path):
    if path not in entries or entries[path][:2] != ('100644', 'blob'):
        raise InvalidEvidence('missing or nonregular bound file: ' + path)
    return git(root, 'cat-file', 'blob', entries[path][2])


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise InvalidEvidence('duplicate JSON key: ' + key)
        out[key] = value
    return out


def parse(data):
    return json.loads(data, object_pairs_hook=unique_object)


def is_dependency(path):
    """Frozen runtime chain plus conservative guards for A1 ledger/proof edits."""
    p = PurePosixPath(path)
    if path in (SCRIPT, WORKFLOW):
        return False
    if p.parent == PurePosixPath('scripts') and re.match(
            r'(check_a1_|certify_a1_|a1_)', p.name):
        return True
    if p.parent == PurePosixPath('.github/workflows') and p.name.startswith('a1-'):
        return True
    if p.parent == PurePosixPath('audits') and p.name.startswith('P11_A1_'):
        return True
    if path == 'research/x-c0/A1_COMP_STATUS_CAPSULE.md':
        return True
    if path.startswith('.github/actions/'):
        return True
    if p.parent == PurePosixPath('.'):
        return (p.name in ('.gitattributes', '.gitmodules', '.python-version',
                           'pyproject.toml', 'setup.py', 'setup.cfg', 'pip.conf',
                           'sitecustomize.py', 'usercustomize.py')
                or p.name.startswith(('requirements', 'constraints', 'Dockerfile'))
                or p.suffix in ('.lock', '.pth', '.pyd', '.so'))
    return False


def bindings(root, entries):
    return {p: digest(read(root, entries, p)) for p in sorted(entries) if is_dependency(p)}


def import_surface(entries):
    """Reject new importable siblings, including stdlib/flint shadow packages.

    Existing numerical imports are frozen. Introducing a new scripts/ module or
    package needs review even when its name looks unrelated. Root Python startup
    hooks are separately guarded. Unrelated research/ packages cannot enter the
    frozen commands' module search path.
    """
    surface = set()
    for path in entries:
        if path == SCRIPT:
            continue
        parts = PurePosixPath(path).parts
        if len(parts) >= 2 and parts[0] == 'scripts':
            if len(parts) > 2 or PurePosixPath(parts[1]).suffix in ('.py', '.pyc', '.pyd', '.so'):
                surface.add('/'.join(parts[:2]))
        if len(parts) == 1 and PurePosixPath(path).suffix in ('.py', '.pyc'):
            surface.add(path)
        if (len(parts) > 1 and parts[0] != 'scripts' and parts[0].isidentifier()
                and PurePosixPath(path).suffix in ('.py', '.pyc', '.pyd', '.so')):
            surface.add('root-package:' + parts[0])
    return sorted(surface)


def execution_contract(data):
    """Byte-bind the unchanged heavy jobs, including tools, versions and commands.

    This deliberately supports the current simple workflow layout only. It is
    not a YAML interpreter. New layout/global execution context forces review.
    """
    text = data.decode('utf-8')
    if '\r' in text or '\t' in text:
        raise InvalidEvidence('unsupported workflow whitespace')
    top = list(re.finditer(r'^([A-Za-z][A-Za-z_-]*):(?:\s.*)?$', text, re.M))
    sections = {m.group(1): text[m.start():top[i + 1].start() if i + 1 < len(top) else len(text)]
                for i, m in enumerate(top)}
    if len(sections) != len(top) or 'jobs' not in sections:
        raise InvalidEvidence('ambiguous workflow layout')
    allowed = {'name', 'on', 'permissions', 'concurrency', 'jobs', 'env', 'defaults', 'run-name'}
    if set(sections) - allowed:
        raise InvalidEvidence('unknown workflow-level context')
    jobs = sections['jobs']
    starts = list(re.finditer(r'^  ([a-z][a-z0-9-]*):\s*$', jobs, re.M))
    blocks = {m.group(1): jobs[m.start():starts[i + 1].start() if i + 1 < len(starts) else len(jobs)].rstrip() + '\n'
              for i, m in enumerate(starts)}
    if len(blocks) != len(starts) or not set(JOBS).issubset(blocks):
        raise InvalidEvidence('missing/duplicate numerical job')
    record = {key: blocks[key] for key in JOBS}
    record.update({key: sections.get(key, '') for key in ('env', 'defaults')})
    return digest(json.dumps(record, sort_keys=True).encode('utf-8'))


def validate_certificate(root, head_tree):
    manifest = parse(read(root, head_tree, MANIFEST))
    if manifest['schema'] != 1 or manifest['matrix_sha256'] != MATRIX:
        raise InvalidEvidence('unsupported certificate or matrix')
    source = commit(root, manifest['source_commit'])
    source_tree = tree(root, source)
    if bindings(root, source_tree) != manifest['dependencies']:
        raise InvalidEvidence('incomplete or incorrect historical dependency inventory')
    if execution_contract(read(root, source_tree, WORKFLOW)) != manifest['execution_contract_sha256']:
        raise InvalidEvidence('historical execution contract mismatch')
    expected = {'run.json', *CERTIFICATES}
    if set(manifest['evidence_sha256']) != expected:
        raise InvalidEvidence('incomplete certificate evidence')
    evidence = {}
    for name, sha in manifest['evidence_sha256'].items():
        evidence[name] = read(root, head_tree, DIRECTORY + name)
        if digest(evidence[name]) != sha:
            raise InvalidEvidence('damaged archived evidence: ' + name)
    meta = parse(evidence['run.json'])
    run = meta['run']
    if (meta['repository'] != 'Waschtl904/objekt-x-programm'
            or run['id'] != manifest['run_id'] or run['run_attempt'] != manifest['run_attempt']
            or run['head_sha'] != source or run['path'] != WORKFLOW
            or run['event'] not in ('pull_request', 'workflow_dispatch')
            or run['status'] != 'completed' or run['conclusion'] != 'success'):
        raise InvalidEvidence('historical run identity/status mismatch')
    required = {'a1-c-even-classify', 'a1-c-even-fresh-matrix-build',
                'a1-c-even-rigorous-ldl', 'a1-c-even-gate'}
    jobs = meta['jobs']
    if len(jobs) != len(required) or {j['name'] for j in jobs} != required:
        raise InvalidEvidence('missing/duplicate required historical job')
    for job in jobs:
        if (job['run_id'] != run['id'] or job['run_attempt'] != run['run_attempt']
                or job['head_sha'] != source or job['status'] != 'completed'
                or job['conclusion'] != 'success'):
            raise InvalidEvidence('historical job identity/status mismatch')
    for name, lines in CERTIFICATES.items():
        # Accept actual timestamped output only, not an echoed shell grep command.
        outputs = {line.split('Z ', 1)[1] for line in evidence[name].decode('utf-8').splitlines()
                   if re.match(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ', line)}
        if not set(lines).issubset(outputs):
            raise InvalidEvidence('missing actual certificate output: ' + name)
    return manifest, source_tree


def ancestor(root, older, newer):
    result = subprocess.run(['git', '-C', str(root), 'merge-base', '--is-ancestor', older, newer],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode not in (0, 1):
        raise InvalidEvidence('cannot establish ancestry')
    return result.returncode == 0


def classify(root, base, head, event):
    head = commit(root, head)
    entries = tree(root, head)
    manifest, source_tree = validate_certificate(root, entries)
    if event == 'workflow_dispatch':
        return True, 'manual-audit'
    if event != 'pull_request':
        return True, 'unsupported-event'
    base = commit(root, base)
    base_tree = tree(root, base)
    policy = {SCRIPT, TEST, WORKFLOW} | {p for p in entries if p.startswith(DIRECTORY)}
    policy |= {p for p in base_tree if p.startswith(DIRECTORY)}
    if any(entries.get(p) != base_tree.get(p) for p in policy):
        return True, 'reuse-policy-or-evidence-changed'
    if not ancestor(root, manifest['source_commit'], base) or not ancestor(root, base, head):
        return True, 'unestablished-certificate-ancestry'
    if bindings(root, entries) != manifest['dependencies']:
        return True, 'a1-dependency-changed'
    if import_surface(entries) != import_surface(source_tree):
        return True, 'python-import-surface-changed'
    if execution_contract(read(root, entries, WORKFLOW)) != manifest['execution_contract_sha256']:
        return True, 'a1-execution-contract-changed'
    return False, 'bound-certificate-unchanged'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--base', default='')
    parser.add_argument('--head', required=True)
    parser.add_argument('--event', choices=('pull_request', 'workflow_dispatch'), required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    actual = git(args.root, 'rev-parse', 'HEAD').decode().strip()
    if actual != args.head:
        raise InvalidEvidence('checked-out HEAD mismatch')
    # CI checks a clean checkout. Never certify a mixture of committed and local bytes.
    if git(args.root, 'status', '--porcelain', '--untracked-files=no').strip():
        raise InvalidEvidence('tracked working tree differs from HEAD')
    heavy, reason = classify(args.root, args.base, args.head, args.event)
    result = f'a1_required={str(heavy).lower()}\nreason={reason}\n'
    print(result, end='')
    if not heavy:
        manifest = parse(read(args.root, tree(args.root, args.head), MANIFEST))
        print(f"REUSED: run={manifest['run_id']} attempt={manifest['run_attempt']} source={manifest['source_commit']}")
        print('SCOPE: frozen C-even certificate only; no new computation or status promotion')
    if args.output:
        with args.output.open('a', encoding='utf-8') as stream:
            stream.write(result)


if __name__ == '__main__':
    main()
