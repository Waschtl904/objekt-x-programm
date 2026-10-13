"""Verify sealed inputs and replay the finite rational certificates."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify(root):
    rows=read(root/'MANIFEST.json')['files']
    rows=rows.items() if isinstance(rows,dict) else [(r['path'],r['sha256']) for r in rows]
    count=0
    for rel,digest in rows:
        p=(root/rel.replace('\\','/')).resolve()
        assert p.is_relative_to(root.resolve()) and sha(p)==digest,rel
        count+=1
    return count
def unpack(src,dest,digest):
    assert sha(src)==digest,src
    dest.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(src) as z:
        for rel in z.namelist():assert (dest/rel).resolve().is_relative_to(dest.resolve())
        z.extractall(dest)
def run(p,*args):
    launch="import runpy,sys;from pathlib import Path;p=sys.argv[1];sys.argv=sys.argv[1:];sys.path.insert(0,str(Path(p).parent));runpy.run_path(p,run_name='__main__')"
    subprocess.run([sys.executable,'-B','-c',launch,str(p),*map(str,args)],cwd=ROOT,check=True)
def main():
    counts={'this_package':verify(ROOT)}
    incoming='Objekt-X-Basis84-Pruefung-und-L-Energie-2026-10-10'
    unpack(ROOT/'inputs'/f'{incoming}.zip',ROOT/'work/basis84-energy-input-2026-10-10','5466bd9a66ba1173e706ea09a6dd664a9f7fd8b28aa7149bf3cd764284a73151')
    counts[incoming]=verify(ROOT/'work/basis84-energy-input-2026-10-10'/incoming)
    previous='Objekt-X-Basis84-und-Abdeckungspruefung-2026-10-10'
    unpack(ROOT/'inputs'/f'{previous}.zip',ROOT/'work/previous-basis','dd0e30a27d66f38503b217fa3279f62173ee1360eeca06eb5fdb698c7deeaec5')
    parent=ROOT/'work/previous-basis'/previous;counts[previous]=verify(parent)
    for name,digest,dest in [
      ('Objekt-X-Gemeinsame-Verlustbilanz-2026-10-10','aa1077fc6772c4dc5d440e6c823e87c8e080c0b8c92711a69f31a6cce2a212a4','previous-loss'),
      ('Objekt-X-Gemeinsame-Restantwort-2026-10-09','12ca23c1fb5a098d47075809303c17210560f42fdd382f125bb43495eec0a008','previous-response'),
      ('Objekt-X-Alte-Hohe-Tailantwort-2026-10-09','b07d0c51abb31817dfd53f0776df2d1a4ad61e88c1e0126d397cd6fa41266689','inherited'),
      ('Objekt-X-Unendlicher-Rest-Vergleich-2026-10-09','b29841feb0ff2d7abf30a522674f7891f8d705cd627687abb8905ecf790625d2','inherited'),
      ('Objekt-X-Endlicher-Schuranschluss-2026-10-09','884cf43ebb157187e5a54039cdc7be352eda4d8369f24d36196724d7981c6b71','inherited')]:
        unpack(parent/'inputs'/f'{name}.zip',ROOT/'work'/dest,digest)
        parent=ROOT/'work'/dest/name;counts[name]=verify(parent)
    task=ROOT/'work/galerkin84-2026-10-10'
    run(task/'audit_input.py');run(task/'audit_galerkin.py');run(task/'audit_witness.py');run(task/'audit_positive_blocks.py')
    for name in ['INPUT_AUDIT.json','AUDIT.json','WITNESS_AUDIT.json','POSITIVE_BLOCK_AUDIT.json']:
        assert read(task/name)==read(ROOT/'expected'/name),name
    cases=read(task/'AUDIT.json')['cases']
    receipt={'status':'PASS_GALERKIN84_PACKAGE_RATIONAL_REPLAY','manifest_counts':counts,
      'fresh_operator_integrations_in_this_replay':False,
      'H84_shape':[84,84],'C84_shape':[203,84],'rational_X_shape':[84,203],
      'cases':[{k:c[k] for k in ['parity','status','ratio_display','joint_loss_ratio_display']} for c in cases],
      'rational_positive_block_checks':read(task/'POSITIVE_BLOCK_AUDIT.json'),
      'independent_witness_checks':read(task/'WITNESS_AUDIT.json'),
      'full_remainder_certified':False,'review_status':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN'}
    (ROOT/'REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2),flush=True)
if __name__=='__main__':main()
