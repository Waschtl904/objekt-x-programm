"""Reject corrupt or unbound replay inputs; check the actual CI path filters."""
from pathlib import Path
from tempfile import TemporaryDirectory
import fnmatch
from replay import checked_path, manifest, sha, REPO

def reject(action):
    try:action()
    except (AssertionError,FileNotFoundError):return
    raise AssertionError('Invalid replay input accepted')
def main():
    with TemporaryDirectory() as temp:
        root=Path(temp);(root/'input').write_bytes(b'bound')
        (root/'SHA256SUMS').write_text(sha(b'bound')+'  input\n',encoding='utf-8')
        manifest(root)
        (root/'input').write_bytes(b'changed');reject(lambda:manifest(root))
        (root/'input').write_bytes(b'bound');(root/'extra').write_bytes(b'unbound');reject(lambda:manifest(root))
        (root/'extra').unlink();(root/'input').unlink();reject(lambda:manifest(root))
        for name in ('../escape','/absolute','C:/absolute','a\\b','a/../b','a//b'):
            reject(lambda:checked_path(root,name))
    workflow=(REPO/'.github/workflows/canonical-joint-maximizers.yml').read_text(encoding='utf-8')
    filters=[line.strip()[3:-1] for line in workflow.splitlines() if line.strip().startswith('- "')]
    expected=['research/x-c1/**','.github/workflows/canonical-joint-maximizers.yml']
    assert filters==expected+expected,filters
    routed=lambda path:any(fnmatch.fnmatchcase(path,p) for p in expected)
    assert routed('research/x-c1/canonical-joint-maximizers-2026-09-30/01-projected-overlap/verification.json')
    assert routed('research/x-c1/canonical-schur-coupling-2026-09-30/04-extremal-gate/inputs/primary.json')
    assert routed('.github/workflows/canonical-joint-maximizers.yml')
    assert not routed('00-uebersicht/RESEARCH_STATE.yaml') and not routed('README.md')
    assert 'pull_request:' in workflow and 'branches: [main]' in workflow
    assert 'github.event.pull_request.head.sha || github.sha' in workflow and 'fetch-depth: 0' in workflow
    print('Corruption, missing/unbound files, unsafe paths and relevant/irrelevant CI routing: PASS')
if __name__=='__main__':main()
