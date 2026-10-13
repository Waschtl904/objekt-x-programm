"""Reproduce sealed bindings and the rational basis/coverage checks."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,zipfile
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_bytes())
def verify(root):
    rows=read(root/'MANIFEST.json')['files']
    rows=rows.items() if isinstance(rows,dict) else [(r['path'],r['sha256']) for r in rows]
    n=0
    for rel,h in rows:
        p=(root/rel.replace('\\','/')).resolve()
        assert p.is_relative_to(root.resolve()) and sha(p)==h,rel
        n+=1
    return n
def unpack(src,dest,digest):
    assert sha(src)==digest,src
    dest.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(src) as z:
        for rel in z.namelist():assert (dest/rel).resolve().is_relative_to(dest.resolve())
        z.extractall(dest)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--compute',action='store_true',help='Also repeat directed function and norm calculations; requires python-flint.')
    ap.add_argument('--deps',type=Path,help='Optional directory containing python-flint.')
    args=ap.parse_args();env=os.environ.copy()
    if args.deps:env['PYTHONPATH']=str(args.deps.resolve())+os.pathsep+env.get('PYTHONPATH','')
    def run(p,*a):
        # Explicit sibling path also supports long Windows extraction paths.
        launch="import runpy,sys;from pathlib import Path;p=sys.argv[1];sys.argv=sys.argv[1:];sys.path.insert(0,str(Path(p).parent));runpy.run_path(p,run_name='__main__')"
        subprocess.run([sys.executable,'-B','-c',launch,str(p),*map(str,a)],cwd=ROOT,env=env,check=True)
    counts={'this_package':verify(ROOT)}
    incoming='Objekt-X-Basisabdeckung-und-Fehlerbudget-2026-10-10'
    unpack(ROOT/'inputs'/f'{incoming}.zip',ROOT/'work/basisabdeckung-input-2026-10-10',
           '0c54178047cabfe7afb688338b508b4201ae2e0e39e1e20ee025919f561b4c0b')
    user=ROOT/'work/basisabdeckung-input-2026-10-10'/incoming
    run(user/'verify_package.py');counts[incoming]=verify(user)
    older='Objekt-X-Tailarchitektur-und-64er-Lemma-2026-10-09'
    unpack(user/'inputs'/f'{older}.zip',ROOT/'work/tail64-input-2026-10-10',
           '2fe86339d80f96a0d8e37420f79a101ecc78c9e835012ebe5a6c9216b3a360c6')
    op=ROOT/'work/tail64-input-2026-10-10'/older
    run(op/'check_tail.py');counts[older]=verify(op)
    last='Objekt-X-Gemeinsame-Verlustbilanz-2026-10-10'
    unpack(ROOT/'inputs'/f'{last}.zip',ROOT/'work/previous-loss',
           'aa1077fc6772c4dc5d440e6c823e87c8e080c0b8c92711a69f31a6cce2a212a4')
    parent=ROOT/'work/previous-loss'/last;counts[last]=verify(parent)
    prev='Objekt-X-Gemeinsame-Restantwort-2026-10-09'
    unpack(parent/'inputs'/f'{prev}.zip',ROOT/'work/previous-response',
           '12ca23c1fb5a098d47075809303c17210560f42fdd382f125bb43495eec0a008')
    parent=ROOT/'work/previous-response'/prev;counts[prev]=verify(parent)
    for stem,digest in [
      ('Alte-Hohe-Tailantwort','b07d0c51abb31817dfd53f0776df2d1a4ad61e88c1e0126d397cd6fa41266689'),
      ('Unendlicher-Rest-Vergleich','b29841feb0ff2d7abf30a522674f7891f8d705cd627687abb8905ecf790625d2'),
      ('Endlicher-Schuranschluss','884cf43ebb157187e5a54039cdc7be352eda4d8369f24d36196724d7981c6b71')]:
        name=f'Objekt-X-{stem}-2026-10-09'
        unpack(parent/'inputs'/f'{name}.zip',ROOT/'work/inherited',digest)
        parent=ROOT/'work/inherited'/name;counts[name]=verify(parent)
    task=ROOT/'work/basis-coverage-2026-10-10'
    if args.compute:run(task/'compute_basis_coverage.py')
    run(task/'audit_basis.py')
    assert read(task/'AUDIT.json')==read(ROOT/'expected/AUDIT.json')
    receipt={'status':'PASS_ACTUAL_BASIS_AND_PARTIAL_COVERAGE_PACKAGE',
      'manifest_counts':counts,'directed_calculation_repeated':args.compute,
      'basis_dimension_per_parity':84,'exact_null_relations_per_parity':672,
      'basis_gram_bounds':'I <= W <= 2 I','first_65_full_error_gram_bound':'1e-70 I',
      'complete_coverage_gate':'COVERAGE_BOUND_INCONCLUSIVE','tail_floor_certified':False,
      'full_L2_Schur_residual_computed':False,'full_remainder_certified':False,
      'external_review':'OPEN'}
    (ROOT/'REPLAY.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt,indent=2),flush=True)
if __name__=='__main__':main()
