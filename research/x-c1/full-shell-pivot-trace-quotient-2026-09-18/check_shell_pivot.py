#!/usr/bin/env python3
"""Directed constants and exact rational ledger for the full shell pivot.
General analytic claims, completions and the quotient proof are in PROOF.md.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,importlib.util,json
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
source=ROOT/'research/x-c1/inherited-resonance-shell-coordinates-2026-09-18/check_shell_coordinate_constants.py'
spec=importlib.util.spec_from_file_location('shell_constants',source)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
I=m.I
checks=[]
def ok(name,condition):
 assert condition,name
 checks.append(name)
def enc(x):
 x=I.of(x)
 return {'lo':str(x.lo),'hi':str(x.hi)}
h0=F(1,10**20);eps=F(1,10**13);alpha=eps/16;delta=alpha/2
B=m.B;L0=m.log_point(F(2)/h0)
# The parent uses its directed log function name for its final text log.
# log_point remains the original rational atanh enclosure function.
log7=m.log_point(F(7));log2=m.LOG2
kappa_upper=m.log_point(8*m.PI.hi)+1+m.PI/2
ok('parent coordinate constants pass',len(m.checks)==11)
ok('B enclosure in (4/5,81/100)',F(4,5)<B.lo<=B.hi<F(81,100))
ok('A_T < 1',m.AT.hi<1)
ok('M_B > 2/5',m.MB.lo>F(2,5))
ok('H maximum < 6/5',m.Hmax.hi<F(6,5))
ok('kappa < 6 using gamma < 1',kappa_upper.hi<6)
ok('full interval stays below unit window',(B+h0).hi<1)
ok('all core to shell distances bounded by 2',(2*B+h0).hi<2)
ok('shell width below every arithmetic shift',h0<log2.lo)
ok('next prime power 7 inactive',2*(B+h0).hi<log7.lo)
ok('endpoint logarithm between 46 and 47',46<L0.lo<=L0.hi<47)
# Enumerate prime powers through 7 with exact trial division.
channels=[]
for q in range(2,8):
 for prime in range(2,q+1):
  if any(prime%d==0 for d in range(2,prime)):continue
  power=prime
  while power<q:power*=prime
  if power==q:channels.append((q,prime));break
ok('active prime-power labels including correct base for 4',[x for x in channels if x[0]<7]==[(2,2),(3,3),(4,2),(5,5)])
for q,prime in channels:
 if q<7:
  ell=m.log_point(F(prime))
  ok('channel '+str(q)+' weight < 1',ell.hi**2<q)
ok('psi supremum < 4',1+F(5,2)<4)
ok('psi internal Lipschitz < 4',F(1,2)+F(5,2)*F(5,4)<4)
ok('chi supremum < 3',F(5,2)<3)
ok('chi internal Lipschitz < 4',F(5,2)*F(5,4)<4)
ok('trace strip exists inside core',F(1,8)<B.lo)
ok('psi lower norm by its two trace strips',2*F(1,8)*F(1,2)**2==F(1,16))
ok('non-Gamma bounded operator ledger',6+2*4==14)
# Integral_0^2 (2-r)(r/2+r^2/4) dr is a polynomial integral.
poly={1:F(1),2:F(0),3:F(-1,4)}
internal=sum(c*F(2**(n+1),n+1) for n,c in poly.items())
ok('complete internal Gamma polynomial integral',internal==1)
ok('complete boundary Gamma integral bound',2*(4+1)==10)
Epsi=4**2+10*4**2;Echi=4**2+10*3**2
ok('Gamma energies ledger',(Epsi,Echi)==(176,106))
ok('core mixed form bound < 500',F(Epsi+Echi,2)+14*24<500)
ok('chi lower energy loss',14*18==252)
ok('Gamma opposite-shell kernel < 1',F(1,4)*F(5,4)+F(1,4)<1)
ok('logarithmic square remainder coefficients',121-(81+18+2)==20 and 22-20==2)
# The actual difference is 2L+20; nonnegative for L>=46.
ok('trace-shell mixed coefficient',4*11+F(6,5)*500==644)
moment_L=F(36,5);moment_c=moment_L*11+F(9072,25)
ok('shell moment loss dominated by 8L+450',moment_L<8 and moment_c<450)
ok('Young coefficient exactly 32 times 10^13',2/alpha==32*10**13)
ok('linear h-loss derivative positive',8*46+442>0)
ok('quadratic h-loss derivative positive',(4*46+644)*(4*46+636)>0)
reserve=2*(46-8)-h0*(8*47+450)-(2/alpha)*h0*(4*47+644)**2
ok('uniform rational shell reserve > 70',reserve>70)
ok('trace reserve delta positive',delta>0)
ok('lift forward physical norm bound',2*32<=64 and 2+F(1296,25)*h0<64)
ok('lift inverse and reduced coordinate norm bound',1+F(20736,25)*h0<64)
ok('full physical coordinate forward bound',1+8**2==65)
ok('physical lifted-source gap conversion',delta/64==F(1,2048*10**13))
# Exact coefficient-level cancellation of q[a psi+t psi].
quadratic={(2,0):F(1),(1,1):F(2),(0,2):F(1)}
ok('trace redundancy homogeneous quadratic cancellation',sum(c*(-1)**a for (a,t),c in quadratic.items())==0)
ok('trace redundancy nonzero coordinate pair',(-1,1)!=(0,0))
report={
 'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
 'parent':bindings['parent'],
 'verdict':'FULL-SHELL-PIVOT-POSITIVE / REDUCED-SCHUR-UNDECIDED',
 'B':enc(B),'h_max':str(h0),'endpoint_logarithm':enc(L0),
 'kappa_upper_with_gamma_less_than_one':enc(kappa_upper),
 'core_gap_import':str(eps),'psi_core_energy_lower':str(alpha),
 'trace_pivot_lower':str(delta),'shell_L2_coefficient_lower':'70',
 'uniform_rational_reserve':str(reserve),'D_inverse_norm_upper':str(1/delta),
 'lifted_physical_gap_lower':str(delta/64),'physical_coordinate_norm_squared_upper':65,
 'input_files':len(bindings['files']),'checks':len(checks),'passed_checks':checks,
 'uncompressed_Schur':'exact zero direction psi in completed old core; no strictly positive uniform bound possible',
 'remaining_obligation':'R0=A0-C0*D^-1 C0 >= sigma I on K_B intersect psi-perp; full coupling and inverse shear; odd continuation separately',
 'new_all_source_endpoint':False,
 'analytic_dependency':'Infinite-dimensional estimates and all-space coordinate arguments are proved in PROOF.md; finite checks do not replace them.'
}
jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
logtext='\n'.join('PASS '+name for name in checks)+'\nTOTAL '+str(len(checks))+' PASS\n'+report['verdict']+'\n'
if args.write:
 (HERE/'shell_pivot_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
 (HERE/'shell_pivot_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
 names=['PROOF.md','STATUS_DE.md','README.md','check_shell_pivot.py','input_bindings.json','shell_pivot_checks.log','shell_pivot_results.json']
 (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names),encoding='ascii',newline='\n')
if args.verify:
 assert (HERE/'shell_pivot_results.json').read_bytes()==jsontext.encode('utf-8')
 assert (HERE/'shell_pivot_checks.log').read_bytes()==logtext.encode('utf-8')
 for line in (HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines():
  digest,name=line.split('  ',1)
  assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
 print('REPLAY and all payload SHA256 hashes PASS')
print(logtext,end='')
