"""Portable exact replay of the three immutable joint-maximizer packages."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, os, subprocess, sys, zipfile

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
def sha(raw):return hashlib.sha256(raw).hexdigest()
def checked_path(root,name):
    p=PurePosixPath(name)
    assert name and '\\' not in name and ':' not in name and not p.is_absolute()
    assert all(x not in ('','..','.') for x in name.split('/')),name
    target=root.joinpath(*p.parts)
    assert target.resolve().is_relative_to(root.resolve()),name
    assert not target.is_symlink(),name
    return target
def manifest(root, extra=()):
    rows={}
    for line in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        digest,name=line.split('  ',1)
        assert name not in rows and len(digest)==64
        raw=checked_path(root,name).read_bytes();assert sha(raw)==digest,name
        rows[name]=digest
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    assert actual==set(rows)|{'SHA256SUMS'}|set(extra),(actual-set(rows),set(rows)-actual)
    return rows
def bindings():
    family=manifest(HERE)
    data=json.loads((HERE/'SOURCE_BINDINGS.json').read_bytes())
    for item in data['original_files']:
        assert sha(checked_path(HERE,item['path']).read_bytes())==item['sha256']
    for pkg in data['packages']:
        root=checked_path(HERE,pkg['folder'])
        files=manifest(root,('PROOF.md','META.yaml'))
        assert (root/'PROOF.md').read_bytes()==(root/pkg['original_proof']).read_bytes()
        archive=checked_path(HERE,pkg['archive'])
        assert sha(archive.read_bytes())==pkg['archive_sha256']
        with zipfile.ZipFile(archive) as z:
            prefix=pkg['original_folder']+'/'
            expected={prefix+n for n in set(files)|{'SHA256SUMS'}}
            assert set(z.namelist())==expected and len(z.namelist())==len(expected)
            assert z.testzip() is None
            for name in expected:assert z.read(name)==(root/name[len(prefix):]).read_bytes(),name
    return data,family
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    out=args.output.resolve()
    assert not out.is_relative_to(REPO.resolve()),'Replay outputs must be outside the checkout'
    assert not out.exists(),'Use a fresh output directory'
    data,family=bindings();out.mkdir(parents=True)
    git=['git','-c','safe.directory='+REPO.as_posix(),'-C',str(REPO)]
    head=subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()
    receipts=[];steps=[]
    def run(name,root,argv):
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
        with (out/(name+'.log')).open('wb') as log:
            proc=subprocess.run([sys.executable,'-B']+argv,cwd=root,env=env,stdout=log,stderr=subprocess.STDOUT)
        assert proc.returncode==0,name+' failed: '+str(out/(name+'.log'))
        steps.append({'name':name,'exit_code':proc.returncode});print(name+': PASS',flush=True)
    for pkg,stem in zip(data['packages'],('projected_overlap','joint_discriminant','schur_defect')):
        root=HERE/pkg['folder'];output=out/(stem+'.json')
        run('verify_'+stem,root,['verify_'+stem+'.py','--out',str(output)])
        assert output.read_bytes()==(root/'verification.json').read_bytes(),stem+' replay differs'
        receipts.append({'package':pkg['id'],'file':output.name,'sha256':sha(output.read_bytes()),'byte_identical':True})
        run('check_'+stem,root,['check_'+stem+'.py'])
        if stem!='schur_defect':
            audit=out/(stem+'_source_audit.json')
            argv=['audit_sources.py','--repo',str(REPO),'--out',str(audit)]
            if stem=='joint_discriminant':argv+=['--projected-archive',str(HERE/data['packages'][0]['archive'])]
            run('audit_'+stem,root,argv)
            actual=json.loads(audit.read_bytes());original=json.loads((root/'source_audit.json').read_bytes())
            assert actual['observed_local_head']==head
            actual.pop('observed_local_head');original.pop('observed_local_head');assert actual==original
    run('replay_controls',HERE,['check_replay.py'])
    report={'status':'PASS','integration_commit':head,'publication_base':data['publication_base'],
        'source_commit':data['source_commit'],'published_package_anchor':data['published_package_anchor'],
        'family_manifest_sha256':sha((HERE/'SHA256SUMS').read_bytes()),'family_files':len(family),
        'original_files':len(data['original_files']),'receipts':receipts,'steps':steps,
        'large_integrals_and_operator_solves_rerun':False,'mathematical_review_changed':False}
    (out/'REPLAY.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('ALL JOINT MAXIMIZER REPLAYS PASS',flush=True)
if __name__=='__main__':main()
