"""GPT1: independent bindings, exact endpoints, physical metric and lift checks.

Run from this directory with python-flint 0.9.0 available in ./deps.
No source selection, inverse solve, K/F replay or whole-residual integration.
"""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import json, hashlib, zipfile, io, sys, subprocess

H=Path(__file__).resolve().parent
sys.path.insert(0,str(H/'deps'))
from flint import arb, arb_poly, arb_mat, ctx
ctx.prec=1024

def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads(p.read_bytes())
def aq(x):
    z=Q(x);return arb(z.numerator)/z.denominator
def interval(x):
    lo,hi=map(Q,x);need(lo<=hi,'reversed endpoints');return lo,hi
def ball(x): return aq(x[0]).union(aq(x[1]))
def decimal(x):
    with localcontext() as c:
        c.prec=65;return str(Decimal(x.numerator)/Decimal(x.denominator))
def enc(x):
    return [str(Q(str(x.lower().fmpq()))),str(Q(str(x.upper().fmpq())))]

p=H/'input';repo=H/'repo';r=H/'replay'
manifest=read(p/'MANIFEST.json')
need(all(sha((p/n).read_bytes())==v for n,v in manifest.items()),'new package manifest')
need(sha((H.parent/'upload/Objekt-X-Grad11-Machbarkeitsanalyse-GPT2-2026-10-25.zip').read_bytes())=='be2b1ab43514454cfec95dd1283d81e8d2f34745f4cf1554ecfd2d6811888e93','new archive')
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo).decode().strip()
need(head=='137940b4e8ea391af408992ae17fb4eebbd6d7c7','reference checkout')
spec=read(p/'sources/SOURCE_BINDINGS.json')
for name,item in spec['files'].items():
    need(sha((repo/name).read_bytes())==item['sha256'],'source '+name)
aliases={item['alias']:(repo/name) for name,item in spec['files'].items() if 'alias' in item}
cache={}
def get(alias):
    if alias in cache:return cache[alias]
    if alias in spec['nested_members']:
        item=spec['nested_members'][alias]
        with zipfile.ZipFile(io.BytesIO(get(item['archive']))) as z:b=z.read(item['member'])
        need(sha(b)==item['sha256'],'nested '+alias)
    else:b=aliases[alias].read_bytes()
    cache[alias]=b;return b
for name in spec['nested_members']:get(name)
refs=read(p/'REMOTE-REFERENCES.json')['references']
refs['research/x-c1/w9-partial-energy-2026-10-18/certify_k.py']=read(p/'K-CODE-REMOTE.json')
for name,item in refs.items():
    blob=subprocess.check_output(['git','rev-parse','HEAD:'+name],cwd=repo).decode().strip()
    need(blob==item['sha'],'Git blob '+name)

old=H/'inherited/Objekt-X-Zweiraum-Ganzrest-und-Matrixvergleich-2026-10-24.zip'
need(sha(old.read_bytes())=='e1911ce244aa51062f6b06bb767f945922199112380022b59846de4ec7f0e89d','old archive')
with zipfile.ZipFile(old) as z:
    for name in ['preflight.py','DIRECTIONS.json','PLAN.txt','SOURCE_BINDINGS.json','BEWEIS.txt']:
        need(z.read('two-direction-2026-10-24/'+name)==(p/'sources'/name).read_bytes(),'original member '+name)
d=read(p/'DIAGNOSTIC-DIRECTION.json');s=read(p/'SPECTRUM.json');m=read(p/'MODEL.json')
need(d['source_sha256']==sha((p/'SPECTRUM.json').read_bytes()),'spectrum freeze link')
need(s['model_sha256']==sha((p/'MODEL.json').read_bytes()),'model link')
need(m['plan_sha256']==sha((p/'PLAN.txt').read_bytes()),'plan link')
coeff=list(map(Q,d['raw_coefficients']))
rounded=[]
for x in s['first_critical_raw_vector']:
    t=Q(str(x))*10**12+Q(1,2);rounded.append(Q(t.numerator//t.denominator,10**12))
need(coeff==rounded,'declared rational rounding')
prior=read(p/'sources/DIRECTIONS.json');v=list(map(Q,prior['v1_rational']))
rem=[coeff[j]-coeff[1]*v[j]/v[1] for j in range(2,12)]
need(any(rem),'outside old two-space')

delivered=read(p/'DIRECTED-DIAGNOSTIC.json');fresh=read(r/'DIRECTED-DIAGNOSTIC.json')
diff=[k for k in delivered if delivered[k]!=fresh.get(k)]
need(set(diff)<= {'budget_seconds','total_seconds'},'replay mathematical-field discrepancy')
need(fresh['diagnostic_direction_sha256']==sha((p/'DIAGNOSTIC-DIRECTION.json').read_bytes()),'fixed new direction')
f=fresh['F'];B=interval(f['base_interval']);P=interval(f['pair_interval']);HH=interval(f['H_interval'])
F=interval(f['F_interval']);K=interval(fresh['K']['K_P_interval'])
need(F==(B[0]+2*P[0]-HH[1],B[1]+2*P[1]-HH[0]),'independent signed F recombination')
gap=F[0]-K[1]
need(gap==Q(fresh['F_lower_minus_K_upper']) and gap>Q('1.0476e-6'),'strict gap')
need(interval(fresh['K_minus_F_interval'])==(K[0]-F[1],K[1]-F[0]),'comparison gap')
need(all(interval(x)[0]>=0 for x in f['pair_prices'].values()),'error prices')

# Independent physical Gram from exact moment lift.  On the positive half:
# W(z)=sum z_i^2 + 2 lambda(z)^2/mu, lambda_i=int_a^b ell_i cosh(x/2) dx.
# The Taylor remainder bounds exp(x/2), hence also the truncated cosh series.
a=arb(3).log();b=arb(11).log()/2;h=b-a;mu=(a+a.sinh())/2
t=arb_poly([0,1]);leg=[arb_poly([1]),t]
for n in range(1,11):leg.append(((2*n+1)*t*leg[-1]-n*leg[-2])*(arb(1)/(n+1)))
cosh_poly=arb_poly([arb(0) if n%2 else arb(1)/(2**n*arb.fac_ui(n)) for n in range(161)])
tail=(b/2).exp()*(b/2)**161/arb.fac_ui(161)
mom=[]
for n in range(12):
    scale=(arb(2*n+1)/(2*h)).sqrt()
    ell=scale*leg[n](arb_poly([-1-2*a/h,2/h]))
    primitive=(ell*cosh_poly).integral()
    err=h*scale*tail
    mom.append(primitive(b)-primitive(a)+arb(0,err.upper()))
G=arb_mat([[arb(int(i==j))+2*mom[i]*mom[j]/mu for j in range(12)] for i in range(12)])
import gzip
pairs=json.loads(gzip.decompress((repo/'research/x-c1/w9-partial-energy-2026-10-18/expected/PAIRS_even.json.gz').read_bytes()))
contained=all(ball(pairs['G_W'][i][j]).contains(G[i,j]) for i in range(12) for j in range(12))
need(contained,'independent moment-lift Gram containment')
c=arb_mat([[aq(x)]for x in coeff]);n2=(c.transpose()*G*c)[0,0]
need(n2>0,'positive new physical norm')
N=n2.sqrt();need(ball(fresh['normalization']).contains(N),'F normalization independently enclosed')
need(fresh['normalization']==fresh['K']['normalization'],'same F/K normalization')
lam=sum((aq(coeff[i])*mom[i]for i in range(12)),arb(0))/N
lift=-lam/mu
need((mu*lift+lam).contains(0),'moment cancellation')
# eval_form stores sqrt(upper(c^T G c)), an upper norm bound, not the
# enclosing ball of the actual unit norm.  Its lower endpoint may exceed 1.
normcap=interval(f['physical_W_norm'])
need(normcap[0]>=1 and normcap[1]<1+Q('1e-70'),'conservative unit-norm price')
need(ball(fresh['K']['unit_autocorrelation']).contains(1),'unit physical autocorrelation')
out={
 'status':'GPT1_TARGETED_CONDITIONAL_OBSTRUCTION_CONFIRMED',
 'reference_commit':head,'manifest_files':len(manifest),'bound_files':len(spec['files']),
 'bound_nested_members':len(spec['nested_members']),'git_blob_references':len(refs),
 'source_families':'H1-H4 inherited; inspected general source/form-error and operator-norm scope',
 'replay_mathematical_fields_exactly_identical':True,'only_changed_fields':diff,
 'F_interval':list(map(str,F)),'K_interval':list(map(str,K)),
 'F_lower_minus_K_upper':str(gap),'gap_decimal':decimal(gap),'strict_floor':'1.0476e-6',
 'independent_G_W_entries_contained':144,'positive_metric_reason':'I + 2 lambda lambda^T/mu, mu>0',
 'normalization_independently_contained':True,'moment_lift':enc(lift),
 'outside_old_two_space':True,'outside_remainder_coordinate2':str(rem[0]),
 'T_preservation':'symbolic: T(v/N)=w1, T(e0/M)=w2; T(e_j)=0 for j=2,...,11',
 'model_eigenvalues_used_for_certificate':False,
 'chronology_limit':'Hash chain and declared rounding checked; no independent timestamp attestation. Fixed-witness validity does not require spectral optimality.',
 'new_F_evaluations':1,'new_K_evaluations':1,'K_panels':55,'K_nodes_per_panel':128,
 'new_whole_residual_integrations':0,'new_inner_test_solves':0,
 'runtime_seconds':{'total':fresh['total_seconds'],'K':fresh['budget_seconds']},
 'scope':'Fixed outer response and Q_new comparison inverse; any majorant of Q_new^-1 also fails at this witness. No negative actual Weil direction.',
 'previous_two_space_reopened':False,'external_review':'OPEN','checklist':'3/10 unchanged',
 'github_writes':False,'other_chats_messaged':False
}
(H/'INDEPENDENT-AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['status','manifest_files','bound_files','bound_nested_members','git_blob_references','gap_decimal','independent_G_W_entries_contained','runtime_seconds']},indent=2))
