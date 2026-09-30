"""Fresh source audit for inherited operator and local projected-overlap inputs."""
from pathlib import Path
import argparse,hashlib,json,subprocess,zipfile

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--projected-archive',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();base=Path(__file__).resolve().parent
    bindings=json.loads((base/'input_bindings.json').read_bytes());data={}
    for name,sha in bindings['sha256'].items():
        raw=(base/'inputs'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha;data[name]=json.loads(raw)
    git=['git','-c','safe.directory='+a.repo.resolve().as_posix(),'-c','core.longpaths=true','-C',str(a.repo)]
    def blob(ref,path):return subprocess.check_output(git+['show',ref+':'+path])
    sources={}
    for name in ['primary.json','crosscheck.json','outer_primary.json']:
        for path,sha in data[name]['source_sha256'].items():
            if path in sources:assert sources[path]==sha
            sources[path]=sha
    for path,sha in sources.items():
        raw=blob(bindings['source_commit'],path)
        assert hashlib.sha256(raw).hexdigest()==sha and raw==(a.repo/path).read_bytes(),path
    anchor='b5dc05f7fcc133ab2aeb3132d4bce0fa74f55a5d'
    prefix='research/x-c1/canonical-schur-coupling-2026-09-30/04-extremal-gate/inputs/'
    for name in ['primary.json','crosscheck.json','outer_primary.json','resolvent_verification.json']:
        assert blob(anchor,prefix+name)==(base/'inputs'/name).read_bytes(),name
    assert hashlib.sha256(a.projected_archive.read_bytes()).hexdigest()==bindings['projected_archive_sha256']
    with zipfile.ZipFile(a.projected_archive) as z:
        assert z.testzip() is None
        prefix='canonical-projected-overlap-2026-09-30/'
        for line in z.read(prefix+'SHA256SUMS').decode().splitlines():
            sha,name=line.split('  ',1);assert hashlib.sha256(z.read(prefix+name)).hexdigest()==sha
        for name,old in [('projected_verification.json','verification.json'),('projected_source_audit.json','source_audit.json')]:
            assert z.read(prefix+old)==(base/'inputs'/name).read_bytes()
    result={'status':'PASS','source_commit':bindings['source_commit'],'published_anchor':anchor,
            'source_sha256':sources,'repository_source_count':len(sources),
            'unchanged_published_inputs':4,'unchanged_projected_archive_inputs':2,
            'projected_archive_sha256':bindings['projected_archive_sha256'],
            'input_sha256':bindings['sha256'],
            'observed_local_head':subprocess.check_output(git+['rev-parse','HEAD']).decode().strip(),
            'large_integrals_or_operator_solves_rerun':False}
    a.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(len(sources),'original source files, four published inputs, two local archive inputs: PASS')

if __name__=='__main__':main()
