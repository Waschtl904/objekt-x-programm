"""Replay small checks and bindings; --full also repeats both Arb filter runs."""
from pathlib import Path,PurePosixPath
from fractions import Fraction as F
import argparse,hashlib,json,os,subprocess,sys,tempfile
from combine_cross_projector import combine
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name):return json.loads((HERE/name).read_bytes())
def safe(root,name):
 p=PurePosixPath(name);assert name and not p.is_absolute() and '\\' not in name and ':' not in name
 assert all(x not in ('','.','..') for x in name.split('/'))
 q=root.joinpath(*p.parts);assert q.resolve().is_relative_to(root.resolve()) and not q.is_symlink()
 return q
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
 p.add_argument('--full',action='store_true');a=p.parse_args();repo=a.repo.resolve()
 manifest={n:h for h,n in (line.split('  ',1) for line in (HERE/'SHA256SUMS').read_text().splitlines())}
 assert all(sha(safe(HERE,n))==h for n,h in manifest.items())
 assert {p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()}==set(manifest)|{'SHA256SUMS'}
 binding=read('SOURCE_BINDINGS.json');git=['git','-c','safe.directory='+repo.as_posix(),'-c','core.longpaths=true','-C',str(repo)]
 assert subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()==binding['main']
 for rel,h in binding['source_sha256'].items():
  raw=safe(repo,rel).read_bytes();assert hashlib.sha256(raw).hexdigest()==h
  assert raw==subprocess.check_output(git+['show',binding['main']+':'+rel])
 primary=read('filter_1024.json');second=read('filter_1536.json');stage_a=read('stage_a.json')
 assert primary['bits']==1024 and second['bits']==1536 and primary['flint']==second['flint']=='0.9.0'
 assert primary['source_sha256']==second['source_sha256']
 assert all(r['main']==binding['main'] and not r['A13_inputs_used'] for r in (primary,second,stage_a))
 outer=json.loads((repo/'research/x-c1/renewable-low-schur-spectral-2026-09-29/07-canonical-extension-outer-mass/primary.json').read_bytes())
 for result in (primary,second):
  assert result['joint_residual_identity_checked'] and result['published_unfiltered_overlap_crosscheck']
  for chamber,n in [('A9',6),('A11',8)]:
   r=result['results'][chamber];t=F(r['filter_scale']);m=r['filter_degree'];assert m==8 and t==F(1,300)
   trial=outer['trials'][chamber+'-odd'];theta=F(trial['physical_trial_max_Rayleigh_upper_exact']);nu=F(trial['physical_complement_gap_lower_exact'])
   assert 0<theta<t<nu
   exact_delta=max((theta/t)**m/(1+(theta/t)**m),1/(1+(nu/t)**m))
   assert F(r['scalar_filter_error_upper'])>=exact_delta
   assert len(r['solves'])==4 and len(r['projected_column_error_upper'])==n
   for solve in r['solves']:
    assert F(solve['spectral_distance_lower'])>0 and F(solve['pole_imag'][0])>0
    assert len(solve['columns'])==n
    for col in solve['columns']:assert all(F(x)>=0 for x in col.values())
   for j in range(n):
    subtotal=F(r['scalar_filter_error_upper'])+sum(F(s['columns'][j]['filter_error_contribution_upper']) for s in r['solves'])
    assert F(r['projected_column_error_upper'][j])>=subtotal
 for key in ('K_direct_enclosure','Y_direct_enclosure'):
  for i in range(6):
   for j in range(8):
    one=list(map(F,primary[key][i][j]));two=list(map(F,second[key][i][j]))
    assert max(one[0],two[0])<=min(one[1],two[1])
 for key in ('Y58','Y68'):
  for result in (primary,second):
   lo,hi=map(F,result['targets'][key]['K_approx']);assert 0<=hi-lo<F('1e-20')
 assert read('combined.json')==combine([HERE/n for n in ('stage_a.json','filter_1024.json','filter_1536.json')])
 steps=[]
 with tempfile.TemporaryDirectory(prefix='verify-cross-projector-') as directory:
  temp=Path(directory)
  def run(name,args):
   cp=subprocess.run([sys.executable,'-B',str(HERE/name)]+args,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True)
   assert cp.returncode==0,(name,cp.stdout,cp.stderr)
   steps.append(name);print(name+': PASS',flush=True)
  run('check_cross_filter_math.py',[])
  fresh=temp/'stage_a.json'
  run('cross_projector_stage_a.py',['--repo',str(repo),'--main',binding['main'],'--out',str(fresh)])
  assert fresh.read_bytes()==(HERE/'stage_a.json').read_bytes()
  for name in ('stage_a','combined'):
   fresh=temp/(name+'_gate.json')
   run('evaluate_cross_projector.py',['--repo',str(repo),'--input',str(HERE/(name+'.json')),'--out',str(fresh)])
   assert fresh.read_bytes()==(HERE/(name+'_gate.json')).read_bytes()
  if a.full:
   for bits in (1024,1536):
    fresh=temp/('filter_'+str(bits)+'.json')
    run('cross_projector_filter_probe.py',['--repo',str(repo),'--main',binding['main'],'--bits',str(bits),'--out',str(fresh)])
    assert fresh.read_bytes()==(HERE/fresh.name).read_bytes()
 gate=read('combined_gate.json');assert gate['status'] in ('GREEN','UNRESOLVED') and not gate['STRUCTURAL_OPEN_2_claimed']
 if gate['status']=='GREEN':
  assert F(gate['certified_common_corridor_total_degrees_upper'])<10
  assert any(gate['previous_counterfamily_exclusions'].values())
 report={'status':'PASS','gate_status':gate['status'],'main':binding['main'],
  'source_files_checked':len(binding['source_sha256']),'filter_precisions':[1024,1536],
  'small_replays_byte_identical':True,'filter_enclosures_overlap':True,'full_operator_runs_replayed':a.full,
  'operator_evidence':'Directed Arb generator at two precisions; the small replay checks bindings and analytic guards, not an independent implementation of the full operator solves.',
  'input_sha256':{n:sha(HERE/n) for n in ('stage_a.json','stage_a_gate.json','filter_1024.json','filter_1536.json','combined.json','combined_gate.json')},
  'steps':steps,'global_mathematical_status_change':False,'A13_inputs_used':False}
 a.out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
 print('CROSS-PROJECTOR CHECKS PASS:',gate['status'],flush=True)
if __name__=='__main__':main()
