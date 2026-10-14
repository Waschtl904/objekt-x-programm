"""Exact arithmetic and source checks for the complementary-space transfer.

The infinite-dimensional theorem is proved in HERLEITUNG.txt. Finite controls
below check identities and failure modes; they are not its proof.
Python standard library only. No imports from the predecessor's arithmetic.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse, hashlib, io, json, subprocess, sys, tempfile, zipfile

HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def sha(b):return hashlib.sha256(b).hexdigest()
def member(z,suffix):
    names=[n for n in z.namelist() if n==suffix or n.endswith('/'+suffix)]
    assert len(names)==1,(suffix,names)
    return z.read(names[0])
def T(A):return list(map(list,zip(*A)))
def mm(A,B):return [[sum((x*y for x,y in zip(a,b)),F(0)) for b in T(B)] for a in A]
def add(A,B,k=1):return [[x+k*y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,k):return [[k*x for x in row] for row in A]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(A):
    n=len(A);B=[list(r)+e for r,e in zip(A,eye(n))]
    for j in range(n):
        k=next(k for k in range(j,n) if B[k][j]);B[j],B[k]=B[k],B[j]
        v=B[j][j];B[j]=[x/v for x in B[j]]
        for i in range(n):
            if i!=j:
                v=B[i][j];B[i]=[x-v*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]
def gram(A,J):return mm(mm(T(J),A),J)
def positive(A):
    assert A==T(A)
    B=[row[:] for row in A]
    for j in range(len(B)):
        assert B[j][j]>0
        for i in range(j+1,len(B)):
            for k in range(j+1,len(B)):
                B[i][k]-=B[i][j]*B[j][k]/B[j][j]
    return True
def schur(Q,J,V):
    C=mm(mm(T(J),Q),V)
    return add(gram(Q,V),mm(mm(T(C),inv(gram(Q,J))),C),-1)

def exact_controls():
    W=[[F(2),F(1,3),F(0)],[F(1,3),F(3),F(1,4)],[F(0),F(1,4),F(4)]]
    L=[[F(6),F(1),F(1,2)],[F(1),F(7),F(1,3)],[F(1,2),F(1,3),F(8)]]
    Q=[[F(4),F(1),F(1,5)],[F(1),F(5),F(1,4)],[F(1,5),F(1,4),F(6)]]
    J=[[F(2)],[F(1)],[F(0)]]
    for A in (W,L,Q):positive(A)
    w=mm(T(J),W)[0]
    Z=[[ -w[1]/w[0],-w[2]/w[0]],[F(1),F(0)],[F(0),F(1)]]
    assert mm(mm(T(J),W),Z)==[[0,0]]
    P=mm(mm(J,inv(gram(L,J))),mm(T(J),L))
    V=mm(add(eye(3),P,-1),Z);PZ=mm(P,Z)
    assert mm(mm(T(J),L),V)==[[0,0]]
    assert V!=Z and gram(W,J)!=[[F(1)]]
    assert add(gram(W,V),gram(W,Z),-1)==gram(W,PZ)
    assert schur(Q,J,V)==schur(Q,J,Z)
    C=mm(mm(T(J),Q),Z)
    assert add(gram(Q,Z),schur(Q,J,Z),-1)==mm(mm(T(C),inv(gram(Q,J))),C)
    delta=F(2,3)
    positive(add(schur(Q,J,V),scale(gram(W,V),delta),-1))
    positive(add(schur(Q,J,Z),scale(gram(W,Z),delta),-1))
    # L-compression inverse is not its inverse restriction on a W-complement.
    L2=[[F(1),F(0)],[F(0),F(4)]];j2=[[F(1)],[F(1)]];z2=[[F(1)],[F(-1)]]
    assert gram(L2,z2)==[[F(5)]]
    assert schur(L2,j2,z2)==[[F(16,5)]]
    # A positive restriction alone does not pay its coupling to the finite block.
    bad=[[F(1),F(2)],[F(2),F(401,100)]]
    assert bad[1][1]>delta and bad[1][1]-bad[0][1]**2/bad[0][0]<delta
    # A tilted target complement cannot inherit the original Hilbert floor.
    # diag(1/100,1), K=span(e1), high=e2; target vector (10,1).
    assert F(1,100)*100+1 < 100+1
    # A tail estimate does not apply on all T.
    assert F(1,100)<F(1,20)
    return {'nonidentity_W_and_nonorthonormal_J':True,'different_L_and_W_complements':True,
      'exact_Schur_coset_invariance':True,'exact_Pythagoras_identity':True,
      'restriction_minus_Schur_is_positive_square':True,
      'inverse_restriction_not_inverse_compression':True,
      'restriction_only_without_Schur_coupling_rejected':True,
      'tilted_target_without_W_orthogonality_rejected':True,
      'promotion_of_tail_floor_to_whole_T_rejected':True}

def optional_schur_binding(path,records,binding):
    assert sha(path.read_bytes())==binding['original_schur_package']['sha256']
    with zipfile.ZipFile(path) as z:
        b=json.loads(member(z,'INPUT_BINDINGS.json'));assembly=json.loads(member(z,'ASSEMBLY_AUDIT.json'))
        raw=member(z,b['responses']['filename']);assert sha(raw)==b['responses']['sha256']
        with zipfile.ZipFile(io.BytesIO(raw)) as rz:
            for label,d in records.items():
                raw=member(rz,f'RESPONSES_{label}.json');assert sha(raw)==d['response_source_sha256']
                r=json.loads(raw);rho=F(r['rho']);K=r['K12_new_rational'];M=r['M_upper_rational']
                for i in range(203):
                    for j in range(203):
                        v=(1-rho) if i==j and i<191 else F(K[i-191][j-191]) if i>=191 and j>=191 else F(0)
                        assert F(d['E_rational'][i][j])==v-F(M[i][j])
                assert r['X84x203_rational']==d['X84x203_rational'] and r['beta']==d['beta']
                a=next(a for a in assembly['cases'] if a['parity']==label.lower())
                assert a['complete_QR_relative_T_simple_upper']==d['residual_cap']
    return {'source_archive_hash_verified':True,'exact_E_entries':2*203**2,'exact_X_entries':2*84*203,
            'beta_and_complete_residual_caps_verified':True}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--schur-package',type=Path)
    ap.add_argument('--basis-package',type=Path);ap.add_argument('--replay-inverse',action='store_true')
    ap.add_argument('--output',type=Path,default=HERE/'REPLAY.json');args=ap.parse_args()
    if (HERE/'MANIFEST.json').exists():
        for name,d in read(HERE/'MANIFEST.json')['files'].items():
            raw=(HERE/name).read_bytes()
            assert sha(raw)==d['sha256'] and len(raw)==d['bytes'],name
    b=read(HERE/'SOURCE_BINDINGS.json')
    for name,d in b['sources'].items():
        raw=(HERE/name).read_bytes();assert len(raw)==d['bytes'] and sha(raw)==d['sha256'],name
    package=next((HERE/'inputs').glob('*.zip'))
    with zipfile.ZipFile(package) as z:
        manifest=json.loads(member(z,'MANIFEST.json'))['files']
        for name,d in manifest.items():
            raw=member(z,name);assert sha(raw)==d['sha256'] and len(raw)==d['bytes'],name
        records={s:json.loads(member(z,f'INVERSE_{s}.json')) for s in ('EVEN','ODD')}
        domain=json.loads(member(z,'sources/DOMAIN_BOUND_INPUTS.json'))
        oldaudit=json.loads(member(z,'AUDIT.json'))
    basis_bound=False
    if args.basis_package:
        assert sha(args.basis_package.read_bytes())==b['original_basis_package']['sha256']
        with zipfile.ZipFile(args.basis_package) as z:
            for s in ('EVEN','ODD'):
                assert member(z,f'BASIS_{s}.json')==(HERE/'sources'/f'BASIS_{s}.json').read_bytes()
            assert member(z,'HERLEITUNG.txt')==(HERE/'sources/BASIS84_HERLEITUNG.txt').read_bytes()
            coverage=member(z,'Objekt-X-Basisabdeckung-und-Fehlerbudget-2026-10-10.zip')
            with zipfile.ZipFile(io.BytesIO(coverage)) as cz:
                assert member(cz,'HERLEITUNG.txt')==(HERE/'sources/COVERAGE_HERLEITUNG.txt').read_bytes()
                tail=member(cz,'Objekt-X-Tailarchitektur-und-64er-Lemma-2026-10-09.zip')
                with zipfile.ZipFile(io.BytesIO(tail)) as tz:
                    assert member(tz,'HERLEITUNG.txt')==(HERE/'sources/TAIL64_HERLEITUNG.txt').read_bytes()
        basis_bound=True
    results=[]
    for s,rec in records.items():
        basis=read(HERE/'sources'/f'BASIS_{s}.json');dcase=next(x for x in domain['cases'] if x['parity']==s.lower())
        assert basis['bindings']['half']==domain['source_half_json_sha256']
        D=[[F(x) for x in row] for row in basis['D_rational']]
        S=[[F(x) for x in row] for row in dcase['Y_coefficients_in_exact_WX_isometry_Q']]
        assert len(S)==92 and all(len(r)==8 for r in S)
        assert len(D)==8 and all(len(r)==84 for r in D)
        inv(S[:8])
        for i in range(8):
            for j in range(84):assert sum(S[k][i]*D[k][j] for k in range(8))+S[8+j][i]==0
        trace=sum((x*x for row in D for x in row),F(0))
        assert trace==F(basis['gram_extra_trace_exact']) and 1+trace<F(500251,500000)
        assert basis['exact_function_basis_dimension']==84 and basis['ambient_polynomial_dimension']==96
        beta=F(rec['beta']);cap=F(rec['residual_cap']);a=(1-cap)*beta
        assert beta==F(20209999981781,182190000000000)==F(dcase['beta'])
        assert cap==F(dcase['whole_residual_simple_cap'])=={'EVEN':F(1,250),'ODD':F(71,10000)}[s]
        generic=a*F(21,5);assert a>F(11,100) and generic>F(231,500)>F(1,20)
        moment=F(3,100)*(4*F(3,200)**96/F(factorial(96)))**2
        d95=F(11,10)+sum((F(1,n) for n in range(1,96)),F(0));d96=d95+F(1,96)
        assert moment<F(1,10**600) and d95<7 and d96>F(31,5)
        assert 23*(1+F(2)*F(5,21)*7)/4<30 and 30**2+23*9**2<3000
        high=a*d96/(1+3000*moment)
        assert d96/(1+3000*moment)>F(61,10)
        assert high>F(671,1000)>F(2,3)>F(1,20)
        old=next(x for x in oldaudit['cases'] if x['parity']==s.lower())
        assert high==F(old['deflated_full_high_floor_relative_WX'])
        assert generic==F(old['generic_deflated_floor_relative_WX'])
        results.append({'parity':s.lower(),'exact_basis_null_relations':672,
          'same_half_inverse_source_hash':basis['bindings']['half'],'basis_gram_upper':'500251/500000',
          'original_tail':'Z84=(ran J84)^(perp W_X) in R12',
          'generic_tail_floor_relative_WX':str(generic),'generic_simple_floor':'231/500',
          'transferred_simple_floor_relative_WX':'2/3','tail_inverse_norm_upper':'3/2',
          'tail_floor_1_over_20_proved_under_bound_hypotheses':True})
    source_binding=optional_schur_binding(args.schur_package,records,b) if args.schur_package else None
    inverse_replay=None
    if args.replay_inverse:
        with tempfile.TemporaryDirectory(prefix='tail-replay-') as tmp:
            with zipfile.ZipFile(package) as z:
                for n in z.namelist():
                    p=(Path(tmp)/n).resolve();assert p.is_relative_to(Path(tmp).resolve())
                z.extractall(tmp)
            root=next(Path(tmp).iterdir());cmd=[sys.executable,str(root/'reproduce.py')]
            if args.schur_package:cmd+=['--schur-package',str(args.schur_package.resolve())]
            subprocess.run(cmd,cwd=root,check=True)
            inverse_replay=read(root/'REPLAY.json')
    out={'status':'PASS_CONDITIONAL_ORIGINAL_BASIS84_TAIL_FLOOR',
      'cases':results,'exact_controls':exact_controls(),
      'embedded_source_file_bindings_verified':len(b['sources']),
      'inverse_archive_manifest_files_verified':len(manifest),
      'original_basis_archive_byte_comparison':basis_bound,'original_Schur_data_binding':source_binding,
      'fresh_inverse_replay':inverse_replay,'proof_of_infinite_space_transfer':'HERLEITUNG.txt sections 2-5',
      'old_268_functional_coverage_gate_proved':False,'new_large_integrations_rerun':False,
      'new_L2_Schur_residual_with_factor20_computed':False,'floor_2_over_3_on_all_R12_claimed':False,
      'all_horizons_certified':False,'object_X_constructed':False,'RH_proved':False,
      'external_mathematical_review_open':True,'github_modified':False}
    args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
