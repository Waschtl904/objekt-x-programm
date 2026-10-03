"""Replay the sealed common Y-kernel package at the checked-out commit."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,os,subprocess,sys,zipfile
HERE=Path(__file__).resolve().parent;REPO=HERE.parents[2]
def sha(raw):return hashlib.sha256(raw).hexdigest()
def checked_path(root,name):
    p=PurePosixPath(name);assert name and '\\' not in name and ':' not in name and not p.is_absolute()
    assert all(x not in ('','.','..') for x in name.split('/'))
    target=root.joinpath(*p.parts);assert target.resolve().is_relative_to(root.resolve()) and not target.is_symlink();return target
def manifest(root):
    rows={}
    for line in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        digest,name=line.split('  ',1);assert name not in rows and len(digest)==64
        assert sha(checked_path(root,name).read_bytes())==digest,name;rows[name]=digest
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    assert actual==set(rows)|{'SHA256SUMS'},(actual-set(rows),set(rows)-actual);return rows
def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    out=a.output.resolve();assert not out.exists() and not out.is_relative_to(REPO.resolve())
    manifest(HERE);binding=json.loads((HERE/'SOURCE_BINDINGS.json').read_bytes());out.mkdir(parents=True)
    archive=checked_path(HERE,binding['archive']);assert sha(archive.read_bytes())==binding['archive_sha256']
    package=out/binding['original_folder']
    with zipfile.ZipFile(archive) as z:
        prefix=binding['original_folder']+'/'
        expected={prefix+n for n in binding['original_sha256']}
        assert set(z.namelist())==expected and len(z.namelist())==len(expected) and z.testzip() is None
        for name,digest in binding['original_sha256'].items():
            raw=z.read(prefix+name);assert sha(raw)==digest
            target=checked_path(package,name);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
    for original,visible in binding['visible_copies'].items():
        assert checked_path(package,original).read_bytes()==checked_path(HERE,visible).read_bytes()
    for source,digest in binding['source_sha256'].items():assert sha(checked_path(REPO,source).read_bytes())==digest
    head=subprocess.check_output(['git','-c','safe.directory='+REPO.as_posix(),'-C',str(REPO),'rev-parse','HEAD'],shell=False).decode().strip()
    allowed={(HERE/'check_replay.py').resolve(),(package/'replay.py').resolve()};steps=[]
    def run(label,script,args):
        script=script.resolve();assert script in allowed
        with (out/(label+'.log')).open('wb') as log:
            proc=subprocess.run(['python','-B',str(script),*map(str,args)],executable=sys.executable,shell=False,
                                env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),stdout=log,stderr=subprocess.STDOUT)
        assert proc.returncode==0,label+' failed';steps.append(label);print(label+': PASS',flush=True)
    run('integration_controls',HERE/'check_replay.py',[])
    run('full_19_case_replay',package/'replay.py',['--out',out/'numerical','--repo',REPO])
    inner=json.loads((out/'numerical/REPLAY.json').read_bytes())
    assert inner['status']=='PASS' and inner['full_case_replays']==19 and inner['inherited_files_unchanged']==59
    assert inner['outcome']=='UNRESOLVED' and not inner['new_operator_integrals'] and not inner['A13_inputs_used']
    for row in inner['receipts']:
        assert (out/'numerical'/row['file']).read_bytes()==(package/row['file']).read_bytes()
    record={'status':'PASS','integration_commit':head,'canonical_base':binding['canonical_base'],
            'publication_manifest_sha256':sha((HERE/'SHA256SUMS').read_bytes()),'original_files':len(binding['original_sha256']),
            'archive_sha256':binding['archive_sha256'],'receipts':inner['receipts'],'steps':steps,
            'full_case_replays':19,'inherited_files_unchanged':59,'outcome':'UNRESOLVED',
            'new_operator_integrals':False,'A13_inputs_used':False,'global_verification_snapshot_changed':False}
    (out/'REPLAY.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Y-KERNEL SECOND-ORDER PUBLICATION REPLAY PASS',flush=True)
if __name__=='__main__':main()
