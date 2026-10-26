"""GPT1 negative controls on fresh inputs; originals are never edited."""
import sys, os, json, hashlib, zipfile, subprocess
from pathlib import Path
if sys.flags.optimize or not __debug__:raise SystemExit('OPTIMIZED_PYTHON_REJECTED')
P=Path(__file__).resolve().parent;C=P/'own-negative-controls-portable';C.mkdir(exist_ok=False)
root=P/'merged';H=root/'workspace/work/breakthrough-2026-10-25'
base=P.parent/'upload/Objekt-X-Neuer-Vergleich-Grad11-GPT2-2026-10-26.zip'
revision=P.parent/'upload/Objekt-X-Grad11-Revision-v2-2026-10-26.zip'
oldbad=P/'original_gpt1_invalid_miniarchive.zip'
sha=lambda b:hashlib.sha256(b).hexdigest()
def need(ok,msg):
    if not ok:raise RuntimeError(msg)
cases=[]
def run(label,script,args=(),mode='normal',expected=1,diagnostic=None):
    env=os.environ.copy();env.pop('PYTHONOPTIMIZE',None);flags=[]
    if mode in ['-O','-OO']:flags=[mode]
    if mode.startswith('env'):env['PYTHONOPTIMIZE']=mode[-1]
    cmd=[sys.executable,'-B',*flags,str(script),*map(str,args)]
    r=subprocess.run(cmd,env=env,capture_output=True,text=True,timeout=120)
    need(r.returncode==expected,label+': unexpected exit '+str(r.returncode))
    if expected:need('PASS'not in r.stdout,label+': false success output')
    if diagnostic:need(diagnostic in r.stderr,label+': wrong diagnostic '+r.stderr)
    cases.append({'label':label,'mode':mode,'command':cmd,'environment_PYTHONOPTIMIZE':env.get('PYTHONOPTIMIZE'),
                  'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})

for mode in ['normal','-O','-OO','env1','env2']:
    run('original_GPT1_invalid_miniarchive',H/'verify_handoff_v2.py',['--zip',oldbad],mode,
        diagnostic='OPTIMIZED_PYTHON_REJECTED'if mode!='normal'else None)
    args=['--base',base,'--revision',revision,'--revision-sha256',sha(revision.read_bytes()),'--directory',root]
    run('valid_v2',root/'verify_revision_v2.py',args,mode,0 if mode=='normal'else 1,
        diagnostic='OPTIMIZED_PYTHON_REJECTED'if mode!='normal'else None)

with zipfile.ZipFile(revision)as z:original={n:z.read(n)for n in z.namelist()}
rel='workspace/work/breakthrough-2026-10-25/revision_v2/'
def mutate(label,change,diagnostic):
    files=dict(original)
    def load(name):return json.loads(files[rel+name])
    def save(name,data):files[rel+name]=(json.dumps(data,indent=2)+'\n').encode()
    change(load,save,files)
    manifest=json.loads(files['REVISION_MANIFEST.json'])
    for row in manifest['files']:
        data=files[row['path']];row['bytes']=len(data);row['sha256']=sha(data)
    files['REVISION_MANIFEST.json']=(json.dumps(manifest,indent=2)+'\n').encode()
    archive=C/(label+'.zip')
    with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED)as z:
        for n,b in files.items():z.writestr(n,b)
    run(label,root/'verify_revision_v2.py',
        ['--base',base,'--revision',archive,'--revision-sha256',sha(archive.read_bytes()),'--destination',C/(label+'-extracted')],
        diagnostic=diagnostic)
def omitted_formula(load,save,files):
    a=load('EXACT_GRAM_RADIUS_AUDIT_V2.json');a['rational_formula_upper_diagonals']['h_high_linear'][96]='0';save('EXACT_GRAM_RADIUS_AUDIT_V2.json',a)
def unpaid_price(load,save,files):
    a=load('SOURCE_BLOCK_LEDGER_V2.json');a['matrices']['radius_added_upper'][96][96]=['0','0'];save('SOURCE_BLOCK_LEDGER_V2.json',a)
    b=load('EXACT_GRAM_RADIUS_AUDIT_V2.json');b['source_ledger_sha256']=sha(files[rel+'SOURCE_BLOCK_LEDGER_V2.json']);save('EXACT_GRAM_RADIUS_AUDIT_V2.json',b)
def forged_result(load,save,files):
    a=load('JOINT_REST_BUDGET_V2.json');a['relative_rest_upper']='2';a['whole_joint_pass']=False;a['resulting_GW_floor']='-1';save('JOINT_REST_BUDGET_V2.json',a)
mutate('omitted_radius_formula',omitted_formula,'Radius price formula')
mutate('unpaid_h_coordinate',unpaid_price,'Unpaid radius coordinate')
mutate('forged_final_result',forged_result,'Rest replay mismatch')
(P/'INDEPENDENT_CHECKER_CONTROLS.json').write_text(json.dumps({'status':'GPT1_INDEPENDENT_NEGATIVE_CONTROLS_PASS','cases':cases,'changed_originals':False},indent=2)+'\n')
print('GPT1_INDEPENDENT_NEGATIVE_CONTROLS_PASS:',len(cases),'fresh cases; exact original counterexample and three internally rehashed invalid revisions rejected')
