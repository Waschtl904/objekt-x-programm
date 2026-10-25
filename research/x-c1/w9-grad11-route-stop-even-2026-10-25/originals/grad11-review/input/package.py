from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,zipfile,shutil
H=Path(__file__).resolve().parent
OUT=H.parents[1]/'outputs'
OUT.mkdir(exist_ok=True)
B=H/'delivery';B.mkdir(exist_ok=True)
PRIOR=Path(r'C:\Users\sebas\Documents\Codex\2026-10-21\github-plugin-github-openai-curated-remote\work')
ROOT=PRIOR/'repo'
def sha(x):return hashlib.sha256(x).hexdigest()
def need(ok,msg):
    if not ok:raise RuntimeError(msg)
def write(path,obj):path.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def blob(raw):return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
refs=json.loads((H/'REMOTE-REFERENCES.json').read_bytes())
model=json.loads((H/'MODEL.json').read_bytes())
diag=json.loads((H/'DIRECTED-DIAGNOSTIC.json').read_bytes())
audit=json.loads((H/'ENDPOINT-AUDIT.json').read_bytes())
for path,r in refs['references'].items():
    raw=r['content'].encode('utf-8');need(blob(raw)==r['sha'],'Remote text/blob '+path)
    target=B/'references'/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
    if path.endswith('/HYPOTHESEN.txt')or path.endswith('/HYPOTHESEN_QUELLEN.json'):
        (B/Path(path).name).write_bytes(raw)
    if path.endswith('/PROOF.md'):
        need((ROOT/path).read_bytes()==raw,'Local/remote proof '+path)
kremote=json.loads((H/'K-CODE-REMOTE.json').read_bytes())
kraw=kremote['content'].encode();need(blob(kraw)==kremote['sha'],'K remote blob')
need(sha(kraw)==diag['K_code_sha256'],'Executed K code equals main')
original=PRIOR/'guard-review-2026-10-24/fresh/originals/Objekt-X-Zweiraum-Ganzrest-und-Matrixvergleich-2026-10-24.zip'
need(sha(original.read_bytes())==model['receipt']['archive_sha256'],'Original archive')
with zipfile.ZipFile(original)as z:
    for name in ['PLAN.txt','DIRECTIONS.json','SOURCE_BINDINGS.json','BEWEIS.txt','preflight.py']:
        target=B/'sources'/name;target.parent.mkdir(exist_ok=True);target.write_bytes(z.read('two-direction-2026-10-24/'+name))
need(sha((B/'sources/preflight.py').read_bytes())==diag['F_function_source_sha256'],'Executed F source')
need(sha((B/'sources/DIRECTIONS.json').read_bytes())==model['receipt']['directions_sha256'],'Frozen directions')
# Bind exact executed local inputs, including inherited field/member inventories.
input_specs={}
for path in ['research/x-c1/w9-new-k-schur-underform-even-2026-10-20/INPUT_BINDINGS.json',
             'research/x-c1/w9-matrix-error-pilot-even-2026-10-20/INPUT_BINDINGS.json',
             'research/x-c1/w9-partial-energy-2026-10-18/INPUT_BINDINGS.json']:
    input_specs[path]=json.loads((ROOT/path).read_bytes())
inventory={'scope':'All 94 archived source-file bindings checked. Detailed numerical fields below; inherited JSON member/field inventories retained separately.',
 'files_checked':model['receipt']['files_checked'],'transitive_binding_specs':input_specs,
 'numerical_field_roles':{
  'DIRECTIONS.json.v1_rational,v2_rational,w1_rational,w2_rational':'INHERITED_FIXED_SELECTION; no alteration',
  'PAIRS_even.G_W,H8_Gram,H9_Gram,e_h,Phi_star_h,high_cross_models,bare_F_J_pairs,high_Gram,Fhat,T,T_enclosure':'NEW_RAW_DATA with inherited directed integration/model-error certificates',
  'K_MAP_even_128.K_P_model':'NEW_RAW_DATA / EXPLORATORY_NOT_DIRECTED; direction discovery only',
  'REFINED_COMMON96.cases[0].D96_lower_model,D96_upper_model,U96_model,finite_feature_error_gram,tail_feature_error_scalar and shared force coefficients':'DIRECTED_CERTIFICATE / INHERITED_HYPOTHESIS; complete common F/J families',
  'REFINED_INPUT.cases[0].old_certificate and galerkin source coordinates, high and low Grams, full-source errors':'OLD_A9_CERTIFICATE / INHERITED_HYPOTHESIS; all coefficient combinations',
  'SCHUR.K_new_rational,P_new_upper_rational and pilot.RESULT.P_weight':'DIRECTED_CERTIFICATE / old fixed admissible comparison',
  'FROZEN_RESPONSE12.parities.even.X; FRESH_A12.parities.even.midpoint':'fixed outer response and raw old A9 form; no new selection',
  'RESPONSE_ENERGY.parities.even.fixed_X.whole_Hilbert_residual_model_error_upper,direct_K_error_upper':'DIRECTED_CERTIFICATE / global operator error; not a transferred scalar witness price',
  'FUNCTIONS12.parities.even.functions[].D':'NEW_RAW_DATA / whole physical response functions',
  'bound inverse, domain, response and variational proof anchors':'ANALYTIC_IDENTITY / INHERITED_HYPOTHESIS',
  'historical candidates, paired-source controls, previous K certificate':'bindings and consistency controls, no new replay or target-positive input'},
 'forbidden_target_positivity_used':False,'new_odd_parity_calculations':False,
 'qualification':'This is GPT2 input inventory for GPT1 review; it is not an independent proof of inherited analytic hypotheses.'}
write(B/'SOURCE-INVENTORY.json',inventory)
summary={'status':'AUTHOR_DERIVED_CONDITIONAL_VARIATIONAL_OBSTRUCTION_GPT1_REVIEW_PENDING',
 'reference_commit':refs['ref'],'reference_tree':refs['tree'],
 'decision':'STOP_WHOLE_RESIDUAL_INTEGRATION_FOR_FIXED_Q_NEW_AND_OUTER_RESPONSE',
 'strict_obstruction_lower':'1.0476e-6','exact_F_lower_minus_K_upper':diag['F_lower_minus_K_upper'],
 'K_interval':diag['K']['K_P_interval'],'F_interval':diag['F']['F_interval'],
 'diagnostic_direction_sha256':diag['diagnostic_direction_sha256'],
 'conditional_on':'H1-H4, full original wording and source map included',
 'mathematical_scope':'E_fix=<f,Q_new^-1 f> >= F_T > K_P for one new admissible W-unit vector; not actual Weil negativity',
 'fixed_T':True,'outer_response_changed':False,'K_new_changed':False,
 'new_whole_residual_integrations':0,'new_direct_K_evaluations':1,'new_test_solves':0,
 'internal_endpoint_audit':audit['status'],'independent_GPT1_review':'PENDING','external_review':'OPEN',
 'previous_two_space_result_reopened':False,'milestone4_closed':False,
 'runtime_seconds':{'matrix_assembly':model['elapsed_seconds'],'directed_diagnostic_with_setup':diag['total_seconds'],'direct_K':diag['budget_seconds']},
 'next_block':'Targeted GPT1 input, scope and one-direction arithmetic countercheck. No further whole residual calculation for unchanged comparison.'}
write(B/'ERGEBNIS.json',summary)
names=['PLAN.txt','BERICHT.txt','REPRODUKTION.txt','HANDOFF-GPT1.txt','MODEL.json','SPECTRUM.json','DIAGNOSTIC-DIRECTION.json','DIRECTED-DIAGNOSTIC.json','ENDPOINT-AUDIT.json','REMOTE-REFERENCES.json','K-CODE-REMOTE.json','analyze.py','spectrum.py','freeze_diagnostic.py','directed_diagnostic.py','endpoint_audit.py','package.py']
for name in names:shutil.copyfile(H/name,B/name)
manifest={p.relative_to(B).as_posix():sha(p.read_bytes())for p in sorted(B.rglob('*'))if p.is_file()and p.name!='MANIFEST.json'}
write(B/'MANIFEST.json',manifest)
stem='Objekt-X-Grad11-Machbarkeitsanalyse-GPT2-2026-10-25'
shutil.copyfile(B/'BERICHT.txt',OUT/(stem+'.txt'))
shutil.copyfile(B/'ERGEBNIS.json',OUT/(stem+'.json'))
shutil.copyfile(B/'HANDOFF-GPT1.txt',OUT/(stem+'-Uebergabe-GPT1.txt'))
archive=OUT/(stem+'.zip')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9)as z:
    for p in sorted(B.rglob('*')):
        if p.is_file():z.write(p,p.relative_to(B).as_posix())
with zipfile.ZipFile(archive)as z:
    embedded=json.loads(z.read('MANIFEST.json'))
    need(all(sha(z.read(n))==s for n,s in embedded.items()),'Delivery manifest')
receipt={'archive':str(archive),'bytes':archive.stat().st_size,'sha256':sha(archive.read_bytes()),'manifest_files_checked':len(manifest),'remote_reference_blobs_checked':len(refs['references'])+1,'K_main_code_match':True,'proof_main_matches':True}
write(OUT/(stem+'-Beleg.json'),receipt)
print(json.dumps(receipt,indent=2))
