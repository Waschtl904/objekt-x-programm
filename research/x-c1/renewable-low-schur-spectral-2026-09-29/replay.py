"""Replay the seven preserved spectral packages without changing their bytes."""
from pathlib import Path
import argparse,hashlib,io,json,os,shutil,subprocess,sys,time,zipfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PIN='d16ba43ebb20f2c61f43379fc65d7a9b9dba76de'
def require(v,m):
    if not v:raise RuntimeError(m)
def digest(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(p.read_bytes())
def verify():
    b=read(HERE/'SOURCE_BINDINGS.json');count=0
    def manifest(get,names):
        nonlocal count
        for line in get('SHA256SUMS').decode().splitlines():
            h,n=line.split('  ',1)
            require(n in names and not Path(n).is_absolute() and '..' not in Path(n).parts,'Unsafe manifest')
            require(digest(get(n))==h,'Hash mismatch '+n);count+=1
    def archive(raw):
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            manifests=[n for n in z.namelist() if n=='SHA256SUMS' or n.endswith('/SHA256SUMS')]
            require(len(manifests)==1,'Expected one manifest per reference archive')
            prefix=manifests[0][:-len('SHA256SUMS')]
            manifest(lambda n:z.read(prefix+n),[n[len(prefix):] for n in z.namelist() if n.startswith(prefix)])
            for n in z.namelist():
                if n.endswith('.zip'):archive(z.read(n))
    manifest(lambda n:(HERE/n).read_bytes(),{p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()})
    for p in b['packages']:
        d=HERE/p['folder'];manifest(lambda n:(d/n).read_bytes(),{x.name for x in d.iterdir()})
        require((d/'PROOF.md').read_bytes()==(d/p['original_proof']).read_bytes(),'Proof copy mismatch')
        for z in d.glob('*.zip'):archive(z.read_bytes())
    for r in b['original_files']:require(digest((HERE/r['path']).read_bytes())==r['sha256'],'Original changed '+r['path'])
    for r in b['repository_inputs']:
        for rev in (PIN,'HEAD'):
            raw=subprocess.check_output(['git','show',rev+':'+r['path']],cwd=ROOT)
            require(digest(raw)==r['sha256'],'Repository input changed '+r['path'])
    return {'manifest_entries':count,'original_files':len(b['original_files']),'repository_inputs':len(b['repository_inputs'])}
def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--case',type=int,choices=range(1,8));p.add_argument('--verify-only',action='store_true');a=p.parse_args()
    v=verify();print('PASS preserved inputs '+json.dumps(v),flush=True)
    if a.verify_only:return
    require(a.output is not None,'Missing output');out=a.output.resolve()
    require(not out.exists() and not out.is_relative_to(ROOT),'Use a new output directory outside checkout');out.mkdir(parents=True)
    source=out/'pinned-source'
    subprocess.run(['git','clone','--quiet','--shared','--no-checkout',str(ROOT),str(source)],check=True)
    subprocess.run(['git','-C',str(source),'checkout','--quiet','--detach',PIN],check=True)
    copy=out/'packages';copy.mkdir();bindings=read(HERE/'SOURCE_BINDINGS.json')
    adapters=[]
    for pkg in bindings['packages']:
        d=copy/pkg['folder'];shutil.copytree(HERE/pkg['folder'],d)
        for script in d.glob('*.py'):
            s=script.read_text(encoding='utf-8');old="r'C:\\Program Files\\Git\\cmd\\git.exe'"
            if old in s:
                patched=s.replace(old,repr(shutil.which('git')))
                script.write_text(patched,encoding='utf-8',newline='\n')
                adapters.append({'path':script.relative_to(copy).as_posix(),'change':'Git executable lookup only'})
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHONUTF8='1');steps=[]
    def run(label,script,*args):
        print('RUN '+label,flush=True);start=time.time()
        with (out/(label+'.log')).open('w',encoding='utf-8') as log:
            r=subprocess.run([sys.executable,str(script),*map(str,args)],stdout=log,stderr=subprocess.STDOUT,env=env)
        require(r.returncode==0,label+' failed: '+str(out/(label+'.log')))
        steps.append({'name':label,'returncode':0,'seconds':time.time()-start});print('PASS '+label,flush=True)
    for case in ([a.case] if a.case else range(1,8)):
        d=copy/bindings['packages'][case-1]['folder'];w=out/('case'+str(case));w.mkdir()
        def call(label,script,*args):run(str(case)+'-'+label,d/script,*args)
        def verify_receipts(label,script,primary,cross,*extra):
            call(label,script,'--repo',source,'--primary',primary,'--crosscheck',cross,*extra,'--out',w/(label+'.json'))
        if case==1:
            call('stored','low_schur_verify_diagnostics.py','--repo',source,'--diagnostics',d/'diagnostics.json','--vectors',d/'critical_vectors.json','--precision-check',d/'precision-check.json','--out',w/'stored.json')
            call('arb768','low_schur_compare.py','--repo',source,'--out',w/'primary','--bits',768)
            call('arb1024','low_schur_compare.py','--repo',source,'--out',w/'cross','--bits',1024,'--only','A11-even')
            call('angles','low_schur_physical_angles.py','--input',w/'primary/critical_vectors.json','--output',w/'angles.json')
            call('fresh','low_schur_verify_diagnostics.py','--repo',source,'--diagnostics',w/'primary/diagnostics.json','--vectors',w/'primary/critical_vectors.json','--precision-check',w/'cross/diagnostics.json','--out',w/'fresh.json')
        elif case in (2,3):
            stem='coupling' if case==2 else 'gap';script='critical_subspace_coupling.py' if case==2 else 'old_complement_gap.py';ver='verify_'+script
            extra=['--vectors',d/('critical_vectors.json' if case==2 else 'fixed_vectors.json')]
            if case==3:extra+=['--old-vectors',d/'old_vectors.json']
            verify_receipts('stored',ver,d/(stem+'_bounds.json'),d/(stem+'_bounds_crosscheck.json'),*extra)
            arbextra=['--vectors',d/'critical_vectors.json'] if case==2 else ['--old-vectors',d/'old_vectors.json','--fixed-vectors',d/'fixed_vectors.json']
            for name,bits in [('primary',1024),('cross',1280)]:
                q=['--quadrature-extra',8] if case==2 and name=='cross' else []
                call(name,script,'--repo',source,*arbextra,'--out',w/name,'--bits',bits,*q)
            if case==3:
                # The producer binds its own serialization (LF on Linux, CRLF
                # on Windows). Check all coefficients before using those bytes.
                primary_vectors=w/'primary/fixed_vectors.json'
                cross_vectors=w/'cross/fixed_vectors.json'
                require(read(primary_vectors)==read(cross_vectors)==read(d/'fixed_vectors.json'),
                        'Regenerated fixed coefficients differ from delivered vectors')
                require(primary_vectors.read_bytes()==cross_vectors.read_bytes(),
                        'The two generated vector serializations differ')
                extra=['--vectors',primary_vectors,'--old-vectors',d/'old_vectors.json']
            verify_receipts('fresh',ver,w/('primary/'+stem+'_bounds.json'),w/('cross/'+stem+'_bounds.json'),*extra)
        elif case==4:
            extra=['--vectors',d/'fixed_vectors.json','--proposal',d/'cut_preconditioners.json.gz','--projection',d/'old_projection.json']
            verify_receipts('stored','verify_a11_spectral_cut.py',d/'spectral_bounds.json',d/'spectral_bounds_crosscheck.json',*extra)
            for name,bits in [('primary',512),('cross',768)]:call(name,'true_spectrum_a11.py','--repo',source,'--old-projection',d/'old_projection.json','--out',w/name,'--bits',bits)
            verify_receipts('fresh','verify_a11_spectral_cut.py',w/'primary/spectral_bounds.json',w/'cross/spectral_bounds.json',*extra)
        elif case==5:
            extra=['--vectors',d/'fixed_vectors.json','--proposal',d/'proposals.json.gz']
            verify_receipts('stored','verify_spectral_ranks.py',d/'inputs512.json',d/'inputs768.json',*extra)
            for bits in (512,768):call('arb'+str(bits),'spectral_rank_inputs.py','--repo',source,'--vectors',d/'fixed_vectors.json','--bits',bits,'--out',w/('inputs'+str(bits)+'.json'))
            verify_receipts('fresh','verify_spectral_ranks.py',w/'inputs512.json',w/'inputs768.json',*extra)
        elif case==6:
            call('integer','verify_spectral_transport.py','--repo',source,'--reference',d/'rank_reference.zip','--proposal',d/'gap_proposals.json.gz','--out',w/'verification.json')
        elif case==7:
            extra=['--transport-reference',d/'transport_reference.zip','--a8-gap',d/'a8_gap_verification.json','--a8-proposal',d/'a8_gap_proposals.json.gz']
            verify_receipts('stored','verify_outer_mass.py',d/'primary.json',d/'crosscheck.json',*extra)
            call('inputs','prepare_outer_inputs.py','--reference',d/'transport_reference.zip','--out',w/'inputs')
            call('a8-gap','verify_a8_outer_gap.py','--repo',source,'--reference',w/'inputs/rank_reference.zip','--proposal',d/'a8_gap_proposals.json.gz','--out',w/'a8-gap.json')
            for name,bits,nodes in [('primary',1024,0),('cross',1280,8)]:
                call(name,'outer_mass_bounds.py','--repo',source,'--vectors',w/'inputs/fixed_vectors.json','--transport',w/'inputs/transport_verification.json','--a8-gap',d/'a8_gap_verification.json','--bits',bits,'--extra-nodes',nodes,'--out',w/(name+'.json'))
            verify_receipts('fresh','verify_outer_mass.py',w/'primary.json',w/'cross.json',*extra)
    require(not subprocess.check_output(['git','status','--porcelain'],cwd=source).strip(),'Pinned source changed')
    receipt={'status':'PASS','case':a.case,'integration_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip(),'source_commit':PIN,'input_checks':v,'adapters':adapters,'steps':steps}
    (out/'REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print('ALL SELECTED SPECTRAL REPLAYS PASS',flush=True)
if __name__=='__main__':main()
