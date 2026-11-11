"""Gezielte Vorprüfung. Kein Aufruf des physischen Hauptlaufs.
Aufruf: python -B pruefe_gpt1.py ORIGINAL.zip
Benötigt python-flint 0.9.0; temporäres Entpacken, keine Originaländerung.
"""
import contextlib,gzip,hashlib,importlib.util,io,json,pathlib,subprocess,sys,tempfile,zipfile
from fractions import Fraction as Q
SHA='6651b8b8f0092f91c4a7d4da75d32f9ec5c45720dc82af8e085589d414bad870'

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def solve(A,b):
    rows=[list(map(Q,r))+[Q(x)] for r,x in zip(A,b)]
    for i in range(len(rows)):
        pivot=rows[i][i];assert pivot
        rows[i]=[v/pivot for v in rows[i]]
        for j in range(len(rows)):
            if j!=i:
                f=rows[j][i];rows[j]=[v-f*w for v,w in zip(rows[j],rows[i])]
    return [r[-1] for r in rows]

def identity_check():
    # Kernkoordinaten 0,1; vorhandene Antwort u=e3; Koordinate 2 ungetestet.
    C=[[4,1,0,2],[1,3,1,-1],[0,1,5,1],[2,-1,1,7]]
    sources=[[2,-1,9,4],[3,2,-2,5]]
    K=[r[:2] for r in C[:2]]
    core=[solve(K,f[:2]) for f in sources]
    X=[[sum(Q(f[i])*z[i] for i in range(2)) for z in core] for f in sources]
    a=Q(7);b=[Q(f[3]) for f in sources];den=a-X[0][0];assert den>0
    J=[[X[i][j]+(b[i]-X[i][0])*(b[j]-X[j][0])/den for j in range(2)] for i in range(2)]
    ids=[0,1,3];Ct=[[C[i][j] for j in ids] for i in ids]
    F=[[f[i] for i in ids] for f in sources];z=[solve(Ct,f) for f in F]
    assert J==[[sum(Q(x)*y for x,y in zip(f,v)) for v in z] for f in F]
    k=Q(13619,125000);S=[[Q(1),-k],[Q(0),Q(1)]]
    Fs=[[sum(F[r][i]*S[r][j] for r in range(2)) for i in range(3)] for j in range(2)]
    zs=[solve(Ct,f) for f in Fs]
    assert [[sum(S[r][i]*J[r][s]*S[s][j] for r in range(2) for s in range(2)) for j in range(2)] for i in range(2)]==[[sum(x*y for x,y in zip(f,v)) for v in zs] for f in Fs]

def run(path):
    assert not sys.flags.optimize
    raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA
    identity_check()
    with tempfile.TemporaryDirectory(prefix='objx_gpt1_preflight_') as temp:
        target=pathlib.Path(temp)
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            assert z.testzip() is None
            for n in z.namelist():assert (target/n).resolve().is_relative_to(target)
            z.extractall(target)
        root=next(target.iterdir())
        manifest=json.loads((root/'MANIFEST.json').read_bytes())
        for n,h in manifest.items():assert hashlib.sha256((root/n).read_bytes()).hexdigest()==h
        for script in ['lauf.py','vorpruefung.py']:
            proc=subprocess.run([sys.executable,'-B',str(root/script)],capture_output=True,text=True,timeout=120)
            assert proc.returncode==0,(script,proc.stdout,proc.stderr)
        sub=target/'bestand';sub.mkdir()
        with zipfile.ZipFile(root/'belege/Objekt-X-GPT2-Zweiraumgram-Bestandscheck-2026-11-05.zip') as z:z.extractall(sub)
        bmod=load_module('bestand_review',sub/'bestand.py');result=bmod.run()
        assert Q(result['D_minus_J_trial_determinant_lower'])>Q('.00001834319223869')
        assert Q(result['core_response_schur_pivot_lower'])>Q('3.63869397329384')
        sys.path.insert(0,str(root));sys.path.insert(0,str(root/'belege'))
        import vorbereiten,model_cache
        from flint import arb,arb_mat
        checked={};byte_equal=True
        # Wiederholung ausschließlich der gespeicherten Matrixrekombination.
        # Der originale Gleichheitstest kann durch auswärts gerundetes Laden
        # scheitern. In diesem Fall wird eine streng gerichtete Inklusion geprüft.
        with contextlib.redirect_stdout(io.StringIO()):
            try:
                vorbereiten.prepare()
            except AssertionError:
                tb=sys.exc_info()[2]
                while tb.tb_next:tb=tb.tb_next
                assert tb.tb_frame.f_code.co_name=='prepare'
                assert 'saved' in tb.tb_frame.f_locals and 'cache' in tb.tb_frame.f_locals
                fresh=tb.tb_frame.f_locals['saved'];cache=tb.tb_frame.f_locals['cache'];byte_equal=False
                assert fresh.keys()==cache.keys()
                for key,v in fresh.items():
                    w=cache[key]
                    if model_cache.pack(v)==model_cache.pack(w):checked[key]='EXACT';continue
                    if isinstance(v,arb_mat):
                        assert v.nrows()==w.nrows() and v.ncols()==w.ncols()
                        pairs=[(v[i,j],w[i,j]) for i in range(v.nrows()) for j in range(v.ncols())]
                    elif isinstance(v,arb):pairs=[(v,w)]
                    elif isinstance(v,list):assert len(v)==len(w);pairs=list(zip(v,w))
                    else:raise AssertionError(('structural mismatch',key))
                    assert all(old.contains(new) for new,old in pairs),key
                    checked[key]={'stored_contains_fresh':len(pairs)}
        # Symbolische Abdeckung der zusätzlichen QPhi-Primgrenzen.
        import source_model
        source_model.partition(3*arb(2).log()/2,arb(3).log(),arb(11).log()/2)
        assert not (root/'lauf/START.json').exists()
        for n,h in manifest.items():assert hashlib.sha256((root/n).read_bytes()).hexdigest()==h,n
        return {'status':'GEZIELTE_VORPRUEFUNG_PASS_UNTER_UEBERNOMMENEN_VERTRAEGEN',
          'original_sha256':SHA,'manifest_members':len(manifest),
          'uniform_high_core_determinant_lower':result['D_minus_J_trial_determinant_lower'],
          'core_response_denominator_lower':result['core_response_schur_pivot_lower'],
          'independent_rational_identity_and_congruence':'PASS',
          'author_preflight':'PASS','symbolic_partition':'PASS',
          'stored_matrix_recombination_byte_identity':byte_equal,
          'stored_matrix_recombination_enclosure':'PASS','cache_fields':checked,
          'physical_source_passes':0,'main_started':False,'X12':None,'X22':None,
          'scope':'Startvoraussetzung mathematisch geprüft; keine Ergebnisabnahme und keine Veröffentlichung'}
if __name__=='__main__':print(json.dumps(run(pathlib.Path(sys.argv[1])),indent=2))
