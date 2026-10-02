"""Reject corrupt or unbound replay inputs; check the actual CI path filters."""
from pathlib import Path
from tempfile import TemporaryDirectory
import ast,fnmatch,json,subprocess,sys
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
    workflow=(REPO/'.github/workflows/canonical-adaptive-odd-angle.yml').read_text(encoding='utf-8')
    filters=[line.strip()[3:-1] for line in workflow.splitlines() if line.strip().startswith('- "')]
    expected=['research/x-c1/**','.github/workflows/canonical-adaptive-odd-angle.yml']
    assert filters==expected+expected,filters
    routed=lambda path:any(fnmatch.fnmatchcase(path,p) for p in expected)
    assert routed('research/x-c1/canonical-adaptive-odd-angle-2026-10-02/verification.json')
    assert routed('research/x-c1/canonical-schur-coupling-2026-09-30/04-extremal-gate/inputs/primary.json')
    assert routed('.github/workflows/canonical-adaptive-odd-angle.yml')
    assert not routed('00-uebersicht/RESEARCH_STATE.yaml') and not routed('README.md')
    assert 'pull_request:' in workflow and 'branches: [main]' in workflow
    assert 'github.event.pull_request.head.sha || github.sha' in workflow and 'fetch-depth: 0' in workflow
    assert 'runs-on: windows-latest' in workflow
    assert workflow.index('git config --global core.autocrlf false') < workflow.index('uses: actions/checkout@')
    # Review every process boundary: literal program, explicit no-shell policy.
    source=Path(__file__).with_name('replay.py').read_text(encoding='utf-8')
    calls=[node for node in ast.walk(ast.parse(source)) if isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute) and isinstance(node.func.value,ast.Name) and node.func.value.id=='subprocess' and node.func.attr in ('run','check_output')]
    assert len(calls)==2
    for call in calls:
        assert isinstance(call.args[0],ast.List) and isinstance(call.args[0].elts[0],ast.Constant)
        assert call.args[0].elts[0].value in ('git','python')
        assert any(k.arg=='shell' and isinstance(k.value,ast.Constant) and k.value.value is False for k in call.keywords)
    # Actual argument round-trip: spaces and shell metacharacters remain data.
    with TemporaryDirectory() as temp:
        root=Path(temp);script=root/'probe with spaces.py';result=root/'result.json';marker=root/'must-not-exist'
        script.write_text('import json,pathlib,sys\npathlib.Path(sys.argv[1]).write_text(json.dumps(sys.argv[2:]))\n',encoding='utf-8')
        hostile=['; touch '+str(marker),'$(echo injected)','& echo injected','--option-looking-data','a b']
        subprocess.run(['python','-B',str(script),str(result),*hostile],executable=sys.executable,shell=False,check=True)
        assert json.loads(result.read_text())==hostile and not marker.exists()
    print('Corruption, missing/unbound files, unsafe paths and relevant/irrelevant CI routing: PASS')
if __name__=='__main__':main()
