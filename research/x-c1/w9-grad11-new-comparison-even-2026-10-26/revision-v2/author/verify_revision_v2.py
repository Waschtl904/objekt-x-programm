import sys
if sys.flags.optimize or not __debug__:
    raise SystemExit('OPTIMIZED_PYTHON_REJECTED: use ordinary Python; no certificate was checked.')
"""Verify a bound additive revision and replay rational arithmetic, never integrations."""
import argparse,hashlib,json,os,stat,subprocess,tempfile,zipfile
from pathlib import Path,PurePosixPath
from fractions import Fraction as Q
sys.set_int_max_str_digits(50000)
BASE_SHA='024f20f0c6086aefabb6e3d759f91aaa466906a864c673c0c0b467f3ee627946'
BASE_BYTES=360325509
MANIFEST_SHA='3a388b3051f65b502db718b72c4e690c73c4fbf4a649360ca9afeb66b85389f2'
REL='workspace/work/breakthrough-2026-10-25'
def require(ok,message):
    if not ok:raise RuntimeError(message)
def sha(data):return hashlib.sha256(data).hexdigest()
def digest(path):
    h=hashlib.sha256();n=0
    with path.open('rb')as f:
        while b:=f.read(1024*1024):h.update(b);n+=len(b)
    return n,h.hexdigest()
def safe(name):
    p=PurePosixPath(name)
    require(bool(name)and not p.is_absolute()and '..'not in p.parts and '\\'not in name and ':'not in name,'Unsafe member: '+name)
    require(str(p)==name and not name.endswith('/'),'Noncanonical member: '+name)
    require(all(not c.endswith((' ','.'))for c in p.parts),'Unsafe Windows member: '+name)
    return p
def read_archive(path,manifest_name):
    with zipfile.ZipFile(path)as z:
        names=z.namelist();require(len(names)==len(set(names)),'Duplicate ZIP member')
        for info in z.infolist():
            safe(info.filename)
            require(not stat.S_ISLNK(info.external_attr>>16),'ZIP symlink')
        raw=z.read(manifest_name);m=json.loads(raw)
        rows=m['files'];require(len(rows)==len({r['path']for r in rows}),'Duplicate manifest path')
        require(set(names)=={r['path']for r in rows}|{manifest_name},'ZIP membership mismatch')
        for r in rows:
            safe(r['path']);data=z.read(r['path'])
            require(len(data)==r['bytes']and sha(data)==r['sha256'],'ZIP binding: '+r['path'])
    return m,raw
def unpack_new(path,root):
    with zipfile.ZipFile(path)as z:
        for name in z.namelist():
            p=root.joinpath(*safe(name).parts)
            p.parent.mkdir(parents=True,exist_ok=True)
            require(p.resolve().is_relative_to(root),'Extraction escape')
            with p.open('xb')as f:f.write(z.read(name))
def verify_directory(root,rows):
    for r in rows:
        p=root.joinpath(*safe(r['path']).parts)
        require(p.resolve().is_relative_to(root),'Directory escape')
        q=p
        while q!=root:
            require(not q.is_symlink(),'Directory symlink: '+str(q));q=q.parent
        require(digest(p)==(r['bytes'],r['sha256']),'Directory binding: '+r['path'])
def mat(A):return [[Q(x)for x in row]for row in A]
def mul(A,B):return [[sum((A[i][k]*B[k][j]for k in range(len(B))),Q())for j in range(len(B[0]))]for i in range(len(A))]
def lower(boxes,up=False):
    M=[[(Q(a)+Q(b))/2 for a,b in row]for row in boxes]
    n=len(M);require(all(M[i][j]==M[j][i]for i in range(n)for j in range(n)),'Asymmetric midpoint')
    R=[sum(((Q(b)-Q(a))/2 for a,b in row),Q())for row in boxes]
    return [[M[i][j]+((R[i]if up else-R[i])if i==j else 0)for j in range(n)]for i in range(n)]
def ldl(A):
    n=len(A);L=[[Q(int(i==j))for j in range(n)]for i in range(n)];D=[]
    for j in range(n):
        p=A[j][j]-sum((L[j][k]**2*D[k]for k in range(j)),Q())
        require(p>0,'Nonpositive rational pivot '+str(j));D.append(p)
        for i in range(j+1,n):L[i][j]=(A[i][j]-sum((L[i][k]*L[j][k]*D[k]for k in range(j)),Q()))/p
    require(all(sum((L[i][k]*D[k]*L[j][k]for k in range(n)),Q())==A[i][j]for i in range(n)for j in range(n)),'LDL reconstruction')
    return D
def rational_audit(root):
    H=root/REL;R=H/'revision_v2'
    def load(name):return json.loads((R/name).read_bytes())
    ledger=load('SOURCE_BLOCK_LEDGER_V2.json');r=load('EXACT_GRAM_RADIUS_AUDIT_V2.json')
    require(r['source_ledger_sha256']==sha((R/'SOURCE_BLOCK_LEDGER_V2.json').read_bytes()),'Gram audit ledger binding')
    old=json.loads((H/'SOURCE_BLOCK_LEDGER_RESERVE.json').read_bytes())
    require(old['young_parameters']==ledger['young_parameters'],'Original lambda schedule changed')
    diag={}
    for name,g in r['grams'].items():
        M=mat(g['midpoint_exact']);E=mat(g['entry_radius_exact']);d=list(map(Q,g['radius_diagonal_exact']));n=len(d)
        rawM=mat(g['raw_midpoint_exact']);rawE=mat(g['raw_entry_radius_exact'])
        for i in range(n):
            for j in range(n):
                lo=max(rawM[i][j]-rawE[i][j],rawM[j][i]-rawE[j][i])
                hi=min(rawM[i][j]+rawE[i][j],rawM[j][i]+rawE[j][i])
                require(lo<=hi and M[i][j]==(rawM[i][j]+rawM[j][i])/2,'Gram intersection/midpoint')
                require(E[i][j]==max(abs(lo-M[i][j]),abs(hi-M[i][j])),'Gram intersection radius')
        require(all(M[i][j]==M[j][i]for i in range(n)for j in range(n)),'Asymmetric exact midpoint')
        require(all(d[i]>=sum(E[i],Q()) and all(x>=0 for x in E[i])for i in range(n)),'Gram row radius')
        diag[name]=d
    delta=Q(r['delta_exact']);eb=Q(r['coupling_error_upper_exact']);tr=Q(r['inverse_metric_trace_upper_exact']);N=r['original_error_component_count']
    require(delta>0 and eb>=0 and tr>0 and N==11,'Invalid transport inputs')
    lam={k:Q(v['lambda_exact'])for k,v in ledger['radius_cross_terms'].items()}
    require(all(x>0 for x in lam.values()),'Nonpositive lambda')
    prices={}
    def charge(name,block,factor,start):
        x=[Q()for _ in range(108)]
        for i,v in enumerate(diag[block]):x[start+i]=v*factor
        prices[name]=x
    charge('old96_high_linear','old96',lam['old96_high_linear']/delta,0)
    charge('h_high_linear','h',lam['h_high_linear']/delta,96)
    for block,start in [('F',0),('J',12)]:
        charge(block+'_h_physical',block,2*lam[block+'_h_physical']/delta,start)
        charge(block+'_old_B',block,eb**2/(delta**2*lam[block+'_old_B']),start)
        charge(block+'_second_variation',block,N*tr*eb**2/delta**2,start)
    require(prices=={k:list(map(Q,v))for k,v in r['rational_formula_upper_diagonals'].items()},'Radius price formula')
    added=ledger['matrices']['radius_added_upper']
    require(all(Q(added[i][i][1])>=sum((v[i]for v in prices.values()),Q())for i in range(108)),'Unpaid radius coordinate')
    close=load('SOURCE_ARITHMETIC_CLOSURE_V2.json');audit=load('SOURCE_CLOSED_GAP_EXACT_AUDIT_V2.json');geom=load('JOINT_TAIL_GEOMETRY_V2.json')
    require(close['source_ledger_sha256']==sha((R/'SOURCE_BLOCK_LEDGER_V2.json').read_bytes()),'Closure ledger binding')
    require(audit['ledger_sha256']==geom['source_closure_sha256']==sha((R/'SOURCE_ARITHMETIC_CLOSURE_V2.json').read_bytes()),'Closure geometry binding')
    G=lower(close['remaining_gap']);W=lower(json.loads((H.parent/'fo-response-reach-2026-10-25/frozen/MODEL.json').read_bytes())['matrices']['G_W'],True)
    threshold=Q(audit['proved_W_floor_for_stored_ledger'])
    require(threshold>0,'Nonpositive threshold')
    ldl(G);ldl(W);ldl([[G[i][j]-threshold*W[i][j]for j in range(12)]for i in range(12)])
    B=mat(geom['basis']);C=mat(geom['finite_gap_lower_in_basis']);A=mat(geom['inverse'])
    oldgeom=json.loads((H/'JOINT_TAIL_GEOMETRY.json').read_bytes())
    require(geom['basis']==oldgeom['basis']and geom['caches']==oldgeom['caches'],'Frame/cache change')
    require(mul(mul(list(map(list,zip(*B))),G),B)==C,'C congruence')
    ldl(C);require(mul(C,A)==[[Q(int(i==j))for j in range(12)]for i in range(12)],'Inverse identity')
    stored=load('JOINT_REST_BUDGET_V2.json')
    with tempfile.TemporaryDirectory(prefix='objekt-x-v2-rational-')as temp:
        output=Path(temp)/'fresh.json'
        run=subprocess.run([sys.executable,'-B',str(H/'joint_rest_budget_v2.py'),'--output',str(output)],capture_output=True,text=True)
        require(run.returncode==0,'Rest replay failed: '+run.stdout+run.stderr)
        fresh=json.loads(output.read_bytes())
    for key in ('relative_rest_upper','resulting_GW_floor','whole_joint_pass','directions','common_frame_sha256'):
        require(fresh[key]==stored[key],'Rest replay mismatch: '+key)
    theta=Q(stored['relative_rest_upper']);floor=Q(stored['resulting_GW_floor'])
    require(0<=theta<1 and floor==(1-theta)*threshold>0,'Final reserve inequality')
    return {'original_sections_recombined':sum(x['complete_intervals']for x in stored['directions']),
      'direction_count':len(stored['directions']),'mixed_terms':144,'positive_exact_C_pivots':12,
      'corrected_finite_W_floor':str(threshold),'relative_rest_upper':str(theta),'resulting_GW_floor':str(floor)}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base',type=Path,required=True);p.add_argument('--revision',type=Path,required=True)
    p.add_argument('--revision-sha256',required=True)
    g=p.add_mutually_exclusive_group(required=True);g.add_argument('--destination',type=Path);g.add_argument('--directory',type=Path)
    p.add_argument('--report',type=Path);args=p.parse_args()
    require(digest(args.base)==(BASE_BYTES,BASE_SHA),'Wrong original v1 archive')
    require(digest(args.revision)[1]==args.revision_sha256.lower(),'Wrong revision ZIP hash')
    base,braw=read_archive(args.base,'MANIFEST.json');require(sha(braw)==MANIFEST_SHA,'Original manifest hash')
    revision,rraw=read_archive(args.revision,'REVISION_MANIFEST.json')
    require(revision['base_archive_sha256']==BASE_SHA,'Revision base identity')
    basepaths={r['path']for r in base['files']}|{'MANIFEST.json'}
    require(not basepaths.intersection(r['path']for r in revision['files']),'Revision overwrites frozen original')
    if args.destination:
        require(not args.destination.exists(),'Destination already exists; choose a new directory')
        root=args.destination.resolve();root.mkdir(parents=True,exist_ok=False)
        unpack_new(args.base,root);unpack_new(args.revision,root)
    else:root=args.directory.resolve();require(root.is_dir(),'Missing directory')
    rows=base['files']+revision['files']+[
      {'path':'MANIFEST.json','bytes':len(braw),'sha256':sha(braw)},
      {'path':'REVISION_MANIFEST.json','bytes':len(rraw),'sha256':sha(rraw)}]
    verify_directory(root,rows)
    result=rational_audit(root)
    out={'status':'REVISION_BYTES_AND_RATIONAL_ARITHMETIC_PASS','overall_mathematical_review':'UNRESOLVED_PENDING_GPT1_TARGETED_REVIEW',
      'author_derived':True,'external_review_open':True,'fresh_integrations':False,
      'original_files_unchanged':len(base['files']),'additive_files':len(revision['files']),
      'base_archive_sha256':BASE_SHA,'revision_archive_sha256':args.revision_sha256.lower(),
      'optimized_python_supported':False,'results':result}
    if args.report:
        with args.report.open('x',encoding='utf8')as f:f.write(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items()if k!='results'},indent=2))
try:
    if __name__=='__main__':main()
except Exception as exc:
    print('REVISION_REJECTED: '+str(exc),file=sys.stderr);sys.exit(1)
