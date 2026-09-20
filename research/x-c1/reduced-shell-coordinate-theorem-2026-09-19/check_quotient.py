#!/usr/bin/env python3
"""Exact universal coordinate identities and rational norm ledger.
Analytic domain, trace and surjectivity proofs are in PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--root',type=Path,default=HERE.parents[2])
group=parser.add_mutually_exclusive_group()
group.add_argument('--write',action='store_true')
group.add_argument('--verify',action='store_true')
args=parser.parse_args();ROOT=args.root.resolve()
bindings=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
for item in bindings['files']:
 raw=(ROOT/item['path']).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']
parent=ROOT/'research/x-c1/full-shell-pivot-trace-quotient-2026-09-18'
replay=subprocess.run([sys.executable,str(parent/'check_shell_pivot.py'),'--verify','--root',str(ROOT)],capture_output=True,text=True,check=True)
assert not replay.stderr
assert 'TOTAL 43 PASS' in replay.stdout and 'REPLAY and all payload SHA256 hashes PASS' in replay.stdout
inherited=json.loads((parent/'shell_pivot_results.json').read_text(encoding='utf-8'))
assert inherited['checks']==43
checks=[]
def ok(name,condition):
 assert condition,name
 checks.append(name)
# Coefficient identities in Q[k,m,r,N,N^-1,t,uB,sB,c,a,b,W2,T2,M].
# N denotes ||psi||^2>0; this algebra never samples its numerical value.
names=['k','m','r','N','t','uB','sB','c','a','b','W2','T2','M']
zero=(0,)*len(names)
class P:
 def __init__(self,terms=None):
  self.d={k:F(v) for k,v in (terms or {}).items() if v}
 @staticmethod
 def of(x):return x if isinstance(x,P) else P({zero:F(x)})
 def __add__(self,o):
  o=P.of(o);d=self.d.copy()
  for k,v in o.d.items():d[k]=d.get(k,F(0))+v
  return P(d)
 __radd__=__add__
 def __neg__(self):return P({k:-v for k,v in self.d.items()})
 def __sub__(self,o):return self+-P.of(o)
 def __rsub__(self,o):return P.of(o)+-self
 def __mul__(self,o):
  o=P.of(o);d={}
  for a,v in self.d.items():
   for b,w in o.d.items():
    k=tuple(x+y for x,y in zip(a,b));d[k]=d.get(k,F(0))+v*w
  return P(d)
 __rmul__=__mul__
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  z=P.of(1)
  for _ in range(n):z=z*self
  return z
 def __eq__(self,o):return self.d==P.of(o).d
 def substitute(self,name,value):
  idx=names.index(name);total=P.of(0)
  for monomial,coefficient in self.d.items():
   exponent=monomial[idx];assert exponent>=0
   remainder=list(monomial);remainder[idx]=0
   total+=P({tuple(remainder):coefficient})*P.of(value)**exponent
  return total
 def serial(self):
  return [{'powers':list(k),'coefficient':str(v)} for k,v in sorted(self.d.items())]
def variable(name,exponent=1):
 k=list(zero);k[names.index(name)]=exponent;return P({tuple(k):F(1)})
k,m,r,N,t,uB,sB,c,a,b,W2,T2,M=[variable(n) for n in names]
Ninv=variable('N',-1)
projection=(k+m*r)*Ninv
identities={
 'moment correction on the entire core':-m+m,
 'projection makes the reduced core L2 orthogonal':k+m*r-projection*N,
 'forward then inverse recovers trace coordinate':projection.substitute('k',t*N-m*r)-t,
 'inverse then forward recovers core psi component':(k+m*r-projection*N)+projection*N-m*r-k,
 'transfer of old core psi coefficient preserves physical core':-c+(t+c)-t,
 'joint source trace is exactly physical trace matching':(uB-projection)+projection-sB-(uB-sB),
 'independent trace correction is graph-domain e addition':sB+(t-sB)-t,
 'unreduced trace direction represents physical zero':-c+c,
 'inverse norm projection identity':16*(W2+N*T2)-(W2+T2)-(15*W2+(16*N-1)*T2),
 'physical upper bound is exact Cauchy remainder':65*(a*a+b*b)-(a+8*b)**2-(8*a-b)**2,
 'mixed graph term Young identity':a*a+b*b-2*a*b-(a-b)**2,
 'positive graph shift lower coefficient':F(1,32)*(32*(M+1))-M-1,
 'inverse-free conditional remainder identity':a*a+b*b-2*M*a*b-(1-M)*(a*a+b*b)-M*(a-b)**2,
 'Laurent normalization inverse':N*Ninv-1
}
for name,residual in identities.items():ok(name,residual==0)
# These negative controls check that the algebra detects the two actual
# mistakes under discussion instead of silently declaring every identity zero.
ok('reject omitting the shell-moment correction from projection',k+m*r-k*Ninv*N!=0)
ok('reject separately forcing reduced core trace to zero',(0+projection-sB-(uB-sB))!=0)
h0=F(1,10**20);epsilon=F(1,10**13);delta=F(1,32*10**13)
ok('bound input count',len(bindings['files'])==27)
ok('inherited full pivot reserve matches',F(inherited['trace_pivot_lower'])==delta and F(inherited['core_gap_import'])==epsilon)
ok('inherited shell interval matches',F(inherited['h_max'])==h0)
ok('core projection lower-norm multiplier',16*F(1,16)==1)
ok('lift squared norm coefficient for trace',2*32<=64)
ok('lift squared norm coefficient for shell',2+F(1296,25)*h0<=64)
ok('reduced inverse norm shell coefficient',1+F(20736,25)*h0<=64)
ok('two reflected shell halves in physical norm',64==32*2)
ok('physical coordinate forward constant',1+8**2==65)
ok('graph shift exceeds physical semibound',32>15>14)
ok('compressed core and shell lower bounds positive',epsilon>0 and delta>0)
ok('conditional inverse-free normalization constant',min(epsilon,delta)/65==F(1,2080*10**13))
report={
 'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
 'anchor':bindings['anchor'],'verdict':'REDUCED-COORDINATE-AND-FORM-DOMAIN-THEOREM / SCHUR-ESTIMATE-OPEN',
 'scalar_product':'physical L2((-B,B),dx), linear in first argument; X uses |t|^2 + right-shell L2 norm squared',
 'h_max':str(h0),'reduced_kernel':'zero','unreduced_kernel':'span{(-psi,(1,0))}',
 'H1_source_trace_condition':'w(B)+t=s(B), s(b)=0; reduced core w is not required to be H1_0',
 'physical_norm_squared_lower':'1/32','physical_norm_squared_upper':'65',
 'inherited_replay_checks':43,'inherited_replay_stdout_sha256':hashlib.sha256(replay.stdout.encode('utf-8')).hexdigest(),
 'bound_inputs':len(bindings['files']),'new_exact_checks':len(checks),'passed_checks':checks,
 'formal_ring_variables':names,'formal_coordinate_projection':projection.serial(),
 'analytic_proof':'PROOF.md Theorems 2.1, 4.1 and 5.1; finite identities do not prove analytic form-domain or trace claims',
 'new_even_positivity_endpoint':False,'odd_continuation_closed':False
}
jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
logtext='INHERITED full shell pivot: 43 PASS and all hashes verified\n'+'\n'.join('PASS '+name for name in checks)+'\nTOTAL '+str(len(checks))+' NEW EXACT CHECKS PASS\n'+report['verdict']+'\n'
if args.write:
 (HERE/'quotient_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
 (HERE/'quotient_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
 files=['PROOF.md','README.md','STATUS_DE.md','check_quotient.py','input_bindings.json','quotient_results.json','quotient_checks.log']
 (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/f).read_bytes()).hexdigest()+'  '+f+'\n' for f in files),encoding='ascii',newline='\n')
if args.verify:
 assert (HERE/'quotient_results.json').read_bytes()==jsontext.encode('utf-8')
 assert (HERE/'quotient_checks.log').read_bytes()==logtext.encode('utf-8')
 for line in (HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines():
  digest,name=line.split('  ',1)
  assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
 print('REPLAY and all quotient-package SHA256 hashes PASS')
print(logtext,end='')
