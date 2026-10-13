"""Verify sealed inputs and replay algebra; optionally repeat integrations."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parent
PARENT='Objekt-X-Gemeinsame-Restantwort-2026-10-09'
PARENT_SHA='12ca23c1fb5a098d47075809303c17210560f42fdd382f125bb43495eec0a008'
CHAIN=[('Alte-Hohe-Tailantwort','b07d0c51abb31817dfd53f0776df2d1a4ad61e88c1e0126d397cd6fa41266689'),
       ('Unendlicher-Rest-Vergleich','b29841feb0ff2d7abf30a522674f7891f8d705cd627687abb8905ecf790625d2'),
       ('Endlicher-Schuranschluss','884cf43ebb157187e5a54039cdc7be352eda4d8369f24d36196724d7981c6b71')]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_bytes())
def manifest(root):
    data=read(root/'MANIFEST.json')['files']
    rows=data.items() if isinstance(data,dict) else [(d['path'],d['sha256']) for d in data]
    n=0
    for rel,digest in rows:
        p=(root/rel.replace('\\','/')).resolve()
        assert p.is_relative_to(root.resolve()) and sha(p)==digest,rel
        n+=1
    return n
def unpack(archive,dest,digest):
    assert sha(archive)==digest
    dest.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        for name in z.namelist():assert (dest/name).resolve().is_relative_to(dest.resolve())
        z.extractall(dest)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--deps',type=Path,help='Optional directory containing python-flint.')
    ap.add_argument('--integrate',action='store_true',help='Repeat all new source integrations; substantially slower.')
    args=ap.parse_args();env=os.environ.copy()
    if args.deps:env['PYTHONPATH']=str(args.deps.resolve())+os.pathsep+env.get('PYTHONPATH','')
    def run(script,*opts):subprocess.run([sys.executable,str(script),*map(str,opts)],cwd=ROOT,env=env,check=True)
    own=manifest(ROOT)
    dest=ROOT/'work/prior-package'
    unpack(ROOT/'inputs'/f'{PARENT}.zip',dest,PARENT_SHA)
    parent=dest/PARENT;counts={PARENT:manifest(parent)}
    for stem,digest in CHAIN:
        name=f'Objekt-X-{stem}-2026-10-09'
        unpack(parent/'inputs'/f'{name}.zip',ROOT/'work/inherited',digest)
        parent=ROOT/'work/inherited'/name;counts[name]=manifest(parent)
    task=ROOT/'work/tail-probe-2026-10-10'
    run(task/'audit_results.py')
    audit=read(task/'AUDIT.json')
    assert audit==read(ROOT/'expected/AUDIT.json')
    if args.integrate:
        again=ROOT/'work/tail-reintegration'
        assert not again.exists(),'Use a fresh extraction for a fresh integration run.'
        again.mkdir()
        for script in task.glob('*.py'):shutil.copy2(script,again/script.name)
        shutil.copytree(task/'vendor',again/'vendor')
        for par,bits in [('even',3072),('odd',3072),('even',4096)]:
            out=again/f'PROBE_{par.upper()}_12_{bits}.json'
            run(again/'compute_tail_probe.py','--parity',par,'--bits',bits,'--degree',12,'--out',out)
        run(again/'compute_tail_probe.py','--parity','even','--bits',3072,'--calibration','--out',again/'CALIBRATION_EVEN_3072.json')
        for par,bits in [('even',3072),('odd',3072),('even',4096)]:
            run(again/'compute_joint_probe.py','--parity',par,'--bits',bits,'--degree',12,
                '--out',again/f'JOINT_{par.upper()}_12_{bits}.json')
        for par in ['even','odd']:
            run(again/'compute_direct_calibration.py','--parity',par,'--bits',3072,'--calibration',
                '--out',again/f'DIRECT_CALIBRATION_{par.upper()}_3072.json')
        run(again/'audit_results.py')
        assert read(again/'AUDIT.json')['status']==audit['status']
    receipt={'status':'PASS_SEALED_PACKAGE_REPLAY','manifest_files':own,
             'inherited_manifest_files':counts,'interval_comparisons':audit['interval_comparisons'],
             'new_source_integrations_repeated':args.integrate,'split_89_11_refuted':True,
             'two_full_loss_probes_below_one':True,'full_203_tail_gram_computed':False,
             'full_remainder_certified':False,'external_review':'OPEN'}
    (ROOT/'REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2),flush=True)
if __name__=='__main__':main()
