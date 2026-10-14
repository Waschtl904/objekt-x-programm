"""Replay one sealed A9 follow-up against the exact archived Schur predecessor.

Only new certificate checks are run. Analytic proofs are not machine verified,
and the inherited large integrations are not regenerated.
"""
from pathlib import Path, PurePosixPath
import argparse, hashlib, importlib.util, json, shutil, subprocess, sys, zipfile

REPO = Path(__file__).resolve().parents[1]
PREVIOUS = REPO/'research/x-c1/a8-a9-global-closure-2026-10-13'
SCHUR = '65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba'

def require(ok, message):
    if not ok: raise ValueError(message)

def digest(path):
    with Path(path).open('rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()

def safe(root, name):
    require(isinstance(name,str) and bool(name),'empty path')
    p=PurePosixPath(name)
    require(not p.is_absolute() and ':' not in name and '\\' not in name,'unsafe path')
    require(all(x not in ('','.','..') for x in name.split('/')),'unsafe path')
    dest=(root/p).resolve()
    require(dest.is_relative_to(root.resolve()),'path escape')
    return dest

def archive(path, spec):
    require(path.stat().st_size==spec['bytes'] and digest(path)==spec['sha256'],'archive bytes differ')
    with zipfile.ZipFile(path) as z:
        members=[i for i in z.infolist() if not i.is_dir()]
        require(len(members)==len({i.filename for i in members}),'duplicate member')
        require({i.filename for i in members}==set(spec['members']),'incomplete member catalogue')
        for info in members:
            want=spec['members'][info.filename]
            require(info.file_size==want['bytes'],'member length differs')
            with z.open(info) as stream: got=hashlib.file_digest(stream,'sha256').hexdigest()
            require(got==want['sha256'],'member hash differs')

def execute(command, log):
    with log.open('w',encoding='utf-8') as stream:
        run=subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,encoding='utf-8')
    require(run.returncode==0,'sealed checker failed; see '+str(log))

def match(actual, expected):
    require(actual==expected,'sealed replay receipt differs')

def reconstruct_schur(out):
    catalog=json.loads((PREVIOUS/'SOURCE_BINDINGS.json').read_bytes())
    obj=catalog['objects'][SCHUR]
    require(obj['sha256']==SCHUR and bool(obj['chunks']),'wrong predecessor')
    target=out/'predecessor-schur.zip'
    with target.open('wb') as dest:
        for chunk in obj['chunks']:
            p=safe(PREVIOUS,chunk['path'])
            require(p.stat().st_size==chunk['bytes'] and digest(p)==chunk['sha256'],'predecessor chunk differs')
            with p.open('rb') as src: shutil.copyfileobj(src,dest)
    require(target.stat().st_size==obj['bytes'] and digest(target)==SCHUR,'predecessor archive differs')
    return target

def run(package, out):
    package=package.resolve();out=out.resolve()
    require(package.is_relative_to(REPO/'research'),'package outside research tree')
    require(not out.is_relative_to(REPO) and not out.exists(),'output must be new and outside repository')
    out.mkdir(parents=True)
    catalog_path=package/'SOURCE_BINDINGS.json'
    expected=(package/'SOURCE_BINDINGS.sha256').read_text().split()[0]
    require(digest(catalog_path)==expected,'catalogue hash differs')
    catalog=json.loads(catalog_path.read_bytes())
    for name,spec in catalog['archives'].items():
        archive(safe(package,name),spec)
    for name,row in catalog['visible_copies'].items():
        p=safe(package,name)
        with zipfile.ZipFile(safe(package,row['archive'])) as z:
            require(p.read_bytes()==z.read(row['member']),'readable original differs')
    chosen=catalog['replay_archive'];spec=catalog['archives'][chosen]
    work=out/'original';work.mkdir()
    with zipfile.ZipFile(safe(package,chosen)) as z:
        for member in spec['members']:
            dest=safe(work,member);dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(z.read(member))
    original=safe(work,catalog['package_root'])
    predecessor=reconstruct_schur(out)
    receipt=out/'SEALED_REPLAY.json'
    execute([sys.executable,'-u','-B',str(original/'reproduce.py'),
             '--schur-package',str(predecessor),'--output',str(receipt)],out/'sealed-replay.log')
    actual=json.loads(receipt.read_bytes())
    expected=json.loads((package/'reports/EXPECTED_SEALED_REPLAY.json').read_bytes())
    match(actual,expected)
    result={'status':'PASS_SEALED_A9_FOLLOWUP','archive_sha256':spec['sha256'],
            'all_original_archives_verified':len(catalog['archives']),
            'all_original_members_verified':sum(len(x['members']) for x in catalog['archives'].values()),
            'byte_identical_visible_copies':len(catalog['visible_copies']),
            'predecessor_schur_sha256':SCHUR,'sealed_replay_receipt_matches':True,
            'large_integrations_rerun':False,'analytic_proof_machine_verified':False,
            'external_review_open':True}
    (out/'ACCEPTANCE.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--package',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    run(a.package,a.output)

if __name__=='__main__':main()
