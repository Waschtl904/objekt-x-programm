from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile
from fractions import Fraction as F
HERE=Path(__file__).resolve().parent
SCOPE={
 'prime2-interval-continuation-2026-09-18':('check_interval.py','interval'),
 'prime3-transition-unified-shifts-2026-09-18':('check_prime3.py','prime3'),
 'active-set-segment-schur-2026-09-18':('check_active_set_gram.py','active_set_gram'),
 'universal-prime-power-family-2026-09-18':('check_universal_family.py','universal_family'),
 'prime-power-segment-4-2026-09-18':('check_segment.py','segment'),
 'near-null-source-transport-2026-09-18':('check_near.py','near'),
 'window-gap-monotonicity-2026-09-18':('check_window_gap_monotonicity.py','window_gap_monotonicity')}
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def scan_manifest(p):
 entries=[]
 for line in p.read_text(encoding='utf-8-sig').splitlines():
  if not line.strip():continue
  parts=line.split(maxsplit=1)
  if len(parts)!=2:entries.append({'line':line,'status':'UNPARSEABLE'});continue
  old,name=parts;name=name.lstrip('*');q=p.parent/name
  if not q.is_file():entries.append({'path':name,'expected':old,'status':'MISSING'});continue
  b=q.read_bytes();actual=hashlib.sha256(b).hexdigest();e={'path':name,'expected':old,'actual':actual,'status':'PASS' if old.lower()==actual else 'MISMATCH'}
  if e['status']=='MISMATCH':e['matches_after_CRLF_to_LF']=hashlib.sha256(b.replace(b'\r\n',b'\n')).hexdigest()==old.lower()
  entries.append(e)
 return entries
def check(root):
 inv=read(HERE/'frozen_inputs.json');bound=inv['files'];paths={x['path'] for x in bound};assert len(paths)==len(bound)==134
 assert inv['anchor']=='fc597f6129db57787c85ec20627ed608233187ba'
 for f in bound:
  p=root/f['path'];b=p.read_bytes()
  assert len(b)==f['bytes'] and sha(p)==f['sha256'],f['path']
  assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==f['git_blob'],f['path']
 audit=read(HERE/'historical_manifest_audit.json');assert len(audit)==19
 for a in audit:
  e=scan_manifest(root/a['manifest']);assert e==a['entries'],a['manifest']
  assert all(x['status']=='PASS' for x in e)==a['all_match']
 bad=[x for x in audit if not x['all_match']];assert len(bad)==5
 assert sum(e['status']!='PASS' for a in bad for e in a['entries'])==9
 for name in SCOPE:assert next(a['all_match'] for a in audit if a['manifest']=='research/x-c1/'+name+'/SHA256SUMS')
 gaps=[('prime2-interval-continuation-2026-09-18','interval','1/100000',22),('prime3-transition-unified-shifts-2026-09-18','prime3','1/100000000000',23),('prime-power-segment-4-2026-09-18','segment','1/10000000000000',15)]
 for name,stem,gap,count in gaps:
  d=read(root/'research/x-c1'/name/(stem+'_results.json'))
  assert d['mellin_constraints']==2 and F(d['uniform_gap'])==F(gap) and d['check_count']==count
  assert d['status']=='AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN'
 near=read(root/'research/x-c1/near-null-source-transport-2026-09-18/near_results.json')
 source=root/'research/x-c1/prime-power-segment-4-2026-09-18/segment_results.json'
 assert near['source_json_sha256']==sha(source)
 assert near['check_count']==27 and near['mellin_conditions']==2
 assert near['external_audit_completed'] is False and near['new_all_source_endpoint_theorem'] is False
 assert F(near['transport_Rayleigh_lower'])==F(1,10**12)
 reports=read(HERE/'replay_results.json');assert {x['package'] for x in reports}==set(SCOPE)
 for x in reports:
  assert x['passed'] and all(x['checks'].values()),x['package']
  assert sha(HERE/x['archived_stdout'])==x['archived_stdout_sha256']
 summary={'frozen_anchor':inv['anchor'],'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN','bound_input_files':134,'historical_manifests':19,'historical_manifests_matching':14,'historical_manifests_with_discrepancies':5,'historical_mismatched_entries':9,'central_packages_manifest_clean':7,'central_replays_passed':7,'new_endpoint_claim':False,'external_review_completed':False,'shell_H1_orthogonal_split':'NOT_VALID_AS_STATED; see OPEN_PROBLEMS.md','all_historical_manifests_clean':False}
 assert read(HERE/'consolidation_results.json')==summary
 entries=scan_manifest(HERE/'SHA256SUMS');assert all(x['status']=='PASS' for x in entries)
 actual={p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file() and p.name!='SHA256SUMS' and '__pycache__' not in p.parts}
 assert {e['path'] for e in entries}==actual
 print('PASS 134 frozen Git blobs, byte lengths and SHA256 bindings')
 print('PASS historical inventory reproduced: 14 clean, 5 discrepant manifests / 9 entries')
 print('PASS 7 central manifests; exact scope and two-moment/source bindings')
 print('PASS archived fresh replay evidence for all 7 central checkers')
 print('PASS consolidation payload SHA256SUMS; external review remains open')
 print('NOTICE historical manifest mismatches are recorded findings, not repaired successes')
 return paths

def replay(root,rel):
 script=root/rel;name=script.parent.name;text=script.read_text(encoding='utf-8-sig');verify='--verify' in text
 before={p:sha(p) for p in script.parent.iterdir() if p.is_file()}
 with tempfile.TemporaryDirectory(prefix='pr137-replay-') as tmp:
  p=subprocess.run([sys.executable,str(script)]+(['--verify'] if verify else []),cwd=tmp,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  out=p.stdout.decode('utf-8').replace('\r\n','\n');err=p.stderr.decode('utf-8');sys.stdout.write(out)
  if err:sys.stderr.write(err)
  assert p.returncode==0,rel+' failed'
  if name in SCOPE and not verify:
   stem=SCOPE[name][1];assert read(Path(tmp)/(stem+'_results.json'))==read(script.parent/(stem+'_results.json'))
   assert out==(script.parent/(stem+'_checks.log')).read_text(encoding='utf-8').replace('\r\n','\n')
  generated=[]
  for q in sorted(Path(tmp).glob('*.json')):
   original=script.parent/q.name
   generated.append({'name':q.name,'semantic_equal':read(q)==read(original) if original.is_file() else None})
  if name not in SCOPE:print('ARCHIVE-ONLY execution; not theorem promotion. Generated JSON comparisons: '+json.dumps(generated))
 assert before=={p:sha(p) for p in script.parent.iterdir() if p.is_file()},'input mutation'
 print('PASS unchanged inputs after checker '+rel)

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--root',type=Path,default=HERE.parents[2])
 parser.add_argument('--replay-scope',action='store_true')
 parser.add_argument('--list-checkers',action='store_true')
 parser.add_argument('--run-checker',help='one exact inventory-relative checker path; isolated output directory')
 args=parser.parse_args();root=args.root.resolve();paths=check(root)
 catalog=sorted(p for p in paths if p.endswith('.py') and Path(p).name.startswith('check'))
 if args.list_checkers:
  for p in catalog:print(p)
 if args.run_checker:
  assert args.run_checker in catalog,'checker must be in frozen inventory';replay(root,args.run_checker)
 if args.replay_scope:
  for name,(script,stem) in SCOPE.items():replay(root,'research/x-c1/'+name+'/'+script)
if __name__=='__main__':main()
