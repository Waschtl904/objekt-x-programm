"""Stdlib receipt audit; --arb adds small controls, --full repeats the runs.

Without --full this does NOT independently recompute the large full-operator
integrals. It validates hashes, interval budgets, stored capture arithmetic,
and a byte-identical replay of the joint direction gate.
"""
from pathlib import Path,PurePosixPath
from fractions import Fraction as F
import argparse,gzip,hashlib,json,os,subprocess,sys,tempfile,zipfile
HERE=Path(__file__).resolve().parent
PIN='6302a47cab2132f0d87dec29bbf21d7ce98e8f75'
PREVIOUS='8476534383e49bc042e235baa01fb34edbd38b61a03a79707bb1de08c255eb45'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def safe(root,name):
 pp=PurePosixPath(name);assert name and not pp.is_absolute() and '\\' not in name and ':' not in name
 assert all(x not in ('','.','..') for x in name.split('/'))
 p=root.joinpath(*pp.parts);assert p.resolve().is_relative_to(root.resolve()) and not p.is_symlink();return p
def sq(iv):
 lo,hi=map(F,iv);assert lo<=hi
 return (F(0) if lo<=0<=hi else min(lo*lo,hi*hi),max(lo*lo,hi*hi))
def overlaps(x,y):return max(F(x[0]),F(y[0]))<=min(F(x[1]),F(y[1]))
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--arb',action='store_true');p.add_argument('--full',action='store_true');args=p.parse_args();repo=args.repo.resolve()
 pairs=[line.split('  ',1) for line in (HERE/'SHA256SUMS').read_text().splitlines()];manifest={n:h for h,n in pairs};assert len(manifest)==len(pairs)
 assert set(manifest)|{'SHA256SUMS'}=={p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()}
 assert all(sha(safe(HERE,n))==h for n,h in manifest.items())
 archive=HERE/'inputs/previous_cross_projector.zip';assert sha(archive)==PREVIOUS
 with zipfile.ZipFile(archive) as z:
  assert z.testzip() is None
  root='canonical-cross-projector-residual-2026-10-01/'
  entries=[line.split('  ',1) for line in z.read(root+'SHA256SUMS').decode().splitlines()]
  assert all(hashlib.sha256(z.read(root+n)).hexdigest()==h for h,n in entries)
  assert z.read(root+'combined.json')==(HERE/'inputs/combined.json').read_bytes()
 git=['git','-c','safe.directory='+repo.as_posix(),'-c','core.longpaths=true','-C',str(repo)]
 assert subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()==PIN
 sources=read(HERE/'SOURCE_BINDINGS.json')['source_sha256']
 for name,h in sources.items():
  raw=safe(repo,name).read_bytes();assert hashlib.sha256(raw).hexdigest()==h and raw==subprocess.check_output(git+['show',PIN+':'+name])
 capture_rows=0;residual_rows=0
 names={'A9':'corrected_A9_final.json.gz','A11':'corrected_A11_accepted.json.gz'}
 receipts={}
 outer=read(repo/'research/x-c1/renewable-low-schur-spectral-2026-09-29/07-canonical-extension-outer-mass/primary.json')
 for chamber in ('A9','A11'):
  capfile=HERE/('capture_'+chamber+'.json.gz');cap=read(capfile);recfile=HERE/names[chamber];rec=read(recfile);receipts[chamber]=rec
  assert cap['main']==rec['main']==PIN and not cap['A13_inputs_used'] and not rec['A13_inputs_used']
  assert cap['bits']==rec['candidate_bits']==1024 and rec['full_integral_bits']==3072
  assert cap['complete_Gram_used'] and rec['full_high_space_paid'] and rec['finite_solve_is_candidate_only']
  assert rec['capture_sha256']==sha(capfile) and rec['source_sha256']==cap['source_sha256']
  assert all(sources[k]==v for k,v in cap['source_sha256'].items())
  s=len(cap['selected_trial_columns']);assert len(cap['reports'])==len(rec['full_residual_records'])==4*s
  trial=outer['trials'][chamber+'-odd'];theta=F(trial['physical_trial_max_Rayleigh_upper_exact']);nu=F(trial['physical_complement_gap_lower_exact']);scale=F(1,300)
  assert 0<theta<scale<nu
  delta=max((theta/scale)**8/(1+(theta/scale)**8),1/(1+(nu/scale)**8))
  assert F(rec['scalar_filter_error_upper'])>=delta
  for row in cap['reports']:
   c=row['pole']*s+cap['selected_trial_columns'].index(row['trial_column']);lo=hi=F(0);total=list(map(F,row['full_model_energy']));assert 0<total[0]<=total[1]
   at={r['modes']:r for r in row['captures']};previous=F(0)
   for i,coeffrow in enumerate(cap['high_model_coefficients']):
    rr,ii=coeffrow[c];lr,hr=sq(rr);li,hi_i=sq(ii);lo+=lr+li;hi+=hr+hi_i
    if i+1 in at:
     q=at[i+1];ql,qh=map(F,q['fraction']);assert 0<=ql<=qh<=1 and ql>=previous;previous=ql
     assert overlaps(q['energy'],[lo,hi]) and overlaps(q['fraction'],[lo/total[1],hi/total[0]])
     assert overlaps(q['omitted_energy'],[total[0]-hi,total[1]-lo])
   capture_rows+=1
  for j in range(s):
   sum_terms=F(rec['scalar_filter_error_upper'])
   for k in range(4):
    r=rec['full_residual_records'][k*s+j];assert r['all_high_modes_included']
    norm=list(map(F,r['normal_removed_model_residual_norm_squared']));assert 0<=norm[0]<=norm[1]
    model=F(r['complete_model_residual_upper']);normal=F(r['Mellin_normal_Taylor_error_upper'])
    assert model>=normal>=0 and (model-normal)**2>=norm[1]
    rho=F(r['full_physical_residual_upper']);assert rho>=model+F(r['Gamma_model_error_upper'])+F(r['source_rounding_error_upper'])
    distance=F(r['spectral_distance_lower']);term=F(r['filter_error_contribution_upper']);assert distance>0 and term>=rho/(1200*distance)
    sum_terms+=term;residual_rows+=1
   assert F(rec['projected_column_error_upper'][j])>=sum_terms
  tail=read(HERE/('tail_'+chamber+'.json'));assert tail['full_infinite_tail_from_Parseval'] and tail['first_pole_only']
  for row in tail['rows']:
   l,h=map(F,row['fraction_of_normal_removed_residual']);assert 0<l<=h<=1
 targets=read(HERE/'targets.json')
 for j,i in enumerate((4,5)):
  t=targets['targets']['Y'+str(i+1)+'8'];ar,br=receipts['A9'],receipts['A11']
  ea=F(ar['projected_column_error_upper'][j]);eb=F(br['projected_column_error_upper'][0]);va=F(ar['projected_norm_upper'][j]);vb=F(br['projected_norm_upper'][0])
  radius=F(t['K_error_upper']);assert radius>=min(ea*vb+eb,ea+eb*va)
  energy=F(t['energy_conversion_error_upper']);lo,hi=map(F,t['polynomial_K']);yl,yh=map(F,t['direct_Y']);assert yl<=lo-radius-energy and yh>=hi+radius+energy
  sa=F(outer['trials']['A9-odd']['physical_Ritz_matrix'][i][i][1]);sb=F(outer['trials']['A11-odd']['physical_Ritz_matrix'][7][7][1]);assert energy*energy>=sa*sb/289
  pl,ph=map(F,t['previous_Y']);assert list(map(F,t['intersected_Y']))==[max(pl,yl),min(ph,yh)]
  assert targets['Y_direct_enclosure'][i][7]==t['intersected_Y']
 steps=[]
 with tempfile.TemporaryDirectory(prefix='high-response-audit-') as directory:
  temp=Path(directory)
  def run(name,arguments):
   cp=subprocess.run([sys.executable,'-B',str(HERE/name)]+arguments,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),capture_output=True,text=True)
   assert cp.returncode==0,(name,cp.stdout[-4000:],cp.stderr[-4000:]);steps.append(name);print(name+': PASS',flush=True)
  run('evaluate_high_response.py',['--repo',str(repo),'--input',str(HERE/'targets.json'),'--out',str(temp/'gate.json')])
  assert (temp/'gate.json').read_bytes()==(HERE/'gate.json').read_bytes()
  if args.arb or args.full:
   run('check_high_capture.py',['--repo',str(repo)]);run('check_full_residual.py',['--repo',str(repo)])
  if args.full:
   for chamber in ('A9','A11'):
    cap='capture_'+chamber+'.json.gz';corrected=names[chamber];candidates=Path(corrected).stem+'.candidates.gz'
    run('capture_high.py',['--repo',str(repo),'--chamber',chamber,'--resume-low',str(HERE/cap),'--out',str(temp/cap)])
    assert (temp/cap).read_bytes()==(HERE/cap).read_bytes()
    run('corrected_resolvent.py',['--repo',str(repo),'--capture',str(HERE/cap),'--resume-candidates',str(HERE/candidates),'--out',str(temp/corrected)])
    assert (temp/corrected).read_bytes()==(HERE/corrected).read_bytes()
    run('diagnose_high_tail.py',['--repo',str(repo),'--capture',str(HERE/cap),'--corrected',str(HERE/corrected),'--candidates',str(HERE/candidates),'--out',str(temp/('tail_'+chamber+'.json'))])
    assert (temp/('tail_'+chamber+'.json')).read_bytes()==(HERE/('tail_'+chamber+'.json')).read_bytes()
   run('target_functionals.py',['--repo',str(repo),'--a9',str(HERE/names['A9']),'--a11',str(HERE/names['A11']),'--previous',str(HERE/'inputs/combined.json'),'--out',str(temp/'targets.json')])
   assert (temp/'targets.json').read_bytes()==(HERE/'targets.json').read_bytes()
 gate=read(HERE/'gate.json');assert gate['status'] in ('GREEN','PARTIAL_GREEN','UNRESOLVED') and not gate['STRUCTURAL_OPEN_2_claimed']
 if gate['status']!='UNRESOLVED':assert gate['previous_counterfamily_exclusions']['rotated']
 if gate['status']=='GREEN':assert F(gate['certified_common_corridor_total_degrees_upper'])<10
 result={'status':'PASS','gate_status':gate['status'],'main':PIN,'source_files_checked':len(sources),'capture_rows_checked':capture_rows,'complete_residual_budgets_checked':residual_rows,
  'joint_direction_replay_byte_identical':True,'small_Arb_controls_rerun':args.arb or args.full,'large_operator_integrals_replayed':args.full,'steps':steps,
  'scope':'Receipt/source/interval-budget audit and joint-direction replay. The full large operator integrals are only repeated with --full; this is not an independent implementation of the large solves.',
  'A13_inputs_used':False,'review':'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN'}
 args.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print('HIGH-RESPONSE CHECKS PASS:',gate['status'])
if __name__=='__main__':main()
