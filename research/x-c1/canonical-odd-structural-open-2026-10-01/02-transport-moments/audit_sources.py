"""Fresh read-only comparison with canonical Main and the older source pins."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile
from verify_transport_gate import BASE,dependencies

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    bindings=json.loads((BASE/'source_bindings.json').read_bytes())
    git=['git','-c','safe.directory='+a.repo.resolve().as_posix(),'-C',str(a.repo)]
    for row in bindings['repository_inputs']:
        raw=(BASE/'inputs'/row['input']).read_bytes();assert hashlib.sha256(raw).hexdigest()==row['sha256']
        assert subprocess.check_output(git+['show',row['commit']+':'+row['path']])==raw==(a.repo/row['path']).read_bytes()
    family=a.repo/'research/x-c1/canonical-joint-maximizers-2026-09-30'
    with tempfile.TemporaryDirectory(prefix='transport-source-audit-') as name:
        _,_,_,dep=dependencies(Path(name),False)
        output=Path(name)/'audit.json'
        subprocess.run([sys.executable,'-B',str(dep/'audit_sources.py'),'--repo',str(a.repo),
            '--projected-archive',str(family/'archives/Gemeinsame-Projektorueberlappungen-2026-09-30.zip'),
            '--out',str(output)],check=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
        inherited=json.loads(output.read_bytes())
    result={'status':'PASS','integration_base':bindings['integration_base'],'new_repository_proof_bindings':bindings['repository_inputs'],
        'inherited_audit':inherited,'observed_local_head':subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()}
    a.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Two additional canonical proofs plus all inherited source bindings: PASS')
if __name__=='__main__':main()
