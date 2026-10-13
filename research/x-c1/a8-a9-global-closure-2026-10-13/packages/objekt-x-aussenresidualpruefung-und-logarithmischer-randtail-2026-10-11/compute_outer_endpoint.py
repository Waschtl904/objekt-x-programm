"""The exact outer logarithmic coefficient of the new residual functions.

Only the direct Q_b term has a logarithmic singularity at x=b. The old
core adjoint has no singular evaluation point there. See ENDPOINT_PROOF.txt.
This does not bound the full residual tail.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys,hashlib
ap=argparse.ArgumentParser()
for name in ['root','responses','out']:ap.add_argument('--'+name,type=Path,required=True)
args=ap.parse_args();ROOT=args.root.resolve()
sys.path[:0]=[str(ROOT/'work/tail-probe-2026-10-10/vendor'),str(ROOT/'work/galerkin84-2026-10-10')]
from flint import arb,arb_mat,ctx
from compute_inverse_energy_gate import af,box
from safe_serial import serial
ctx.prec=1536
def read(p):return json.loads(p.read_bytes())
def mat(a):return arb_mat([[box(v) for v in row] for row in a])
def rat(a):return arb_mat([[af(v) for v in row] for row in a])
def mellin(n,t):
 z=t/2;lead=arb(1)
 for k in range(1,n+1):lead*=z/(2*k+1)
 value=term=arb(1)
 for k in range(256):term*=z*z/(2*(k+1)*(2*n+2*k+3));value+=term
 nxt=term*z*z/(2*257*(2*n+515));ratio=z*z/(2*258*(2*n+517))
 return lead*(value+arb(0,(nxt/(1-ratio)).upper()))
halfpath=ROOT/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/remainder-integration-check-v2/originals/half-inverse/expected/1536.json'
half=read(halfpath);a=3*arb(2).log()/2;b=arb(3).log();h=b-a
rows=[]
for p,label in enumerate(['EVEN','ODD']):
 rp=args.responses/f'RESPONSES_{label}.json';r=read(rp)
 bp=ROOT/f'work/basis-coverage-2026-10-10/BASIS_{label}.json';basis=read(bp)
 Q=mat(half['blocks'][p]['basis_Q_local_coefficients'])
 S=rat(half['blocks'][p]['half_inverse_centre_rational_Q_coefficients'])
 D=rat(basis['D_rational'])
 Z=arb_mat([[D[i,j] if i<8 else int(i-8==j) for j in range(84)] for i in range(92)])
 J=Q*Z;Y=Q*S
 endpoint=arb_mat([[((2*n+1)/(2*h)).sqrt() for n in range(96)]])
 JB=endpoint*J;YB=endpoint*Y
 FB=[((2*n+1)/(2*b)).sqrt()*(1-mellin(n,b)/mellin(p,b)) for n in range(p+2,p+10,2)]+[YB[0,i] for i in range(8)]
 A=arb_mat([[arb(0) if i<191 else FB[i-191] for i in range(203)]])
 X=rat(r['X84x203_rational']);C=((1-af(r['eta']))*JB*X-A)/2
 # Select a low-force column, so the endpoint trace is a fixed rational
 # combination of J, independent of any finite-source operator error.
 j=max(range(191),key=lambda i:float(abs(C[0,i]).mid()))
 assert not C[0,j].contains(0)
 K=rat(r['K12_new_rational']);rho=af(r['rho'])
 clo=arb_mat([[C[0,i] for i in range(191)]]);cfi=arb_mat([[C[0,i] for i in range(191,203)]])
 norm2=(clo*clo.transpose()/(1-rho)+cfi*K.inv()*cfi.transpose())[0,0]
 model_single_log_tail=2*h/104**2*norm2
 DM=arb_mat([[1-rho if i==j and i<191 else K[i-191,j-191] if i>=191 and j>=191 else 0 for j in range(203)] for i in range(203)])
 TB=af(r['beta'])*(DM-rat(r['M_upper_rational']))
 tnorm=(C*TB.inv()*C.transpose())[0,0]
 rows.append({'parity':label.lower(),'outer_log_coefficient_1x203':C,
  'basis84_right_endpoint':JB,'finite12_right_endpoint':FB,
  'nonzero_low_column_one_based':j+1,'nonzero_coefficient_interval':C[0,j],
  'outer_log_coefficient_D_inverse_norm_squared':norm2,
  'isolated_outer_log_full_tail_104_D_norm_squared':model_single_log_tail,
  'outer_log_coefficient_T_budget_inverse_norm_squared':tnorm,
  'isolated_outer_log_full_tail_104_T_budget_norm_squared':2*h/104**2*tnorm,
  'isolated_component_is_not_a_bound_for_the_whole_residual':True,
  'unsubtracted_weighted_derivative_energy_finite':False,
  'full_remainder_certified':False,
  'bindings':{str(q):hashlib.sha256(q.read_bytes()).hexdigest() for q in [halfpath,bp,rp]}})
 print(label,'nonzero column',j+1,'coefficient',C[0,j].str(14),'isolated log tail /D',model_single_log_tail.str(14),'and /T',(2*h/104**2*tnorm).str(14),flush=True)
args.out.write_text(json.dumps(serial({'status':'NONZERO_OUTER_LOG_COEFFICIENT_ENCLOSED','h':h,'a':a,'b':b,'cases':rows,'full_remainder_certified':False},80),indent=2)+'\n')
