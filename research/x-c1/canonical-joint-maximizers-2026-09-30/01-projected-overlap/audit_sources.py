"""Optional fresh byte comparison against the two immutable Git proof anchors."""
from pathlib import Path
import argparse,hashlib,json,subprocess

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    base=Path(__file__).resolve().parent
    bindings=json.loads((base/'input_bindings.json').read_bytes())
    git=['git','-c','safe.directory='+a.repo.resolve().as_posix(),'-c','core.longpaths=true','-C',str(a.repo)]
    def blob(ref,path):return subprocess.check_output(git+['show',ref+':'+path])
    sources={}
    for name in ['primary.json','crosscheck.json','outer_primary.json']:
        raw=(base/'inputs'/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==bindings['sha256'][name]
        for path,sha in json.loads(raw)['source_sha256'].items():
            if path in sources:assert sources[path]==sha
            sources[path]=sha
    for path,sha in sources.items():
        raw=blob(bindings['source_commit'],path)
        assert hashlib.sha256(raw).hexdigest()==sha,path
        assert (a.repo/path).read_bytes()==raw,path
    anchor='b5dc05f7fcc133ab2aeb3132d4bce0fa74f55a5d'
    prefix='research/x-c1/canonical-schur-coupling-2026-09-30/04-extremal-gate/'
    source_paths={n:prefix+'inputs/'+n for n in ['primary.json','crosscheck.json','outer_primary.json']}
    source_paths['candidate_proposals.json']=prefix+'candidate_proposals.json'
    source_paths['extremal_verification.json']=prefix+'verification.json'
    for name,path in source_paths.items():
        raw=(base/'inputs'/name).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==bindings['sha256'][name]
        assert blob(anchor,path)==raw,path
    result={'status':'PASS','source_commit':bindings['source_commit'],
            'published_package_anchor':anchor,'repository_source_count':len(sources),
            'source_sha256':sources,'unchanged_published_inputs':source_paths,
            'input_sha256':bindings['sha256'],
            'observed_local_head':subprocess.check_output(git+['rev-parse','HEAD']).decode().strip(),
            'large_integrals_and_operator_solves_rerun':False}
    a.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(len(sources),'original repository files and five published inputs: byte comparison PASS')

if __name__=='__main__':main()
