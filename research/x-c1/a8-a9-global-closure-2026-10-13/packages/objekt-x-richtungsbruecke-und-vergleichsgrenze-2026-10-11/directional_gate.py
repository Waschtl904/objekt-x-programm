"""Directed finite test with the complete signed Y moment correction."""
from pathlib import Path
from fractions import Fraction as F
import json,sys,math,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/compute-deps'),str(ROOT/'work/galerkin84-2026-10-10')]
from flint import arb,arb_mat,fmpq,ctx
from safe_serial import serial
import numpy as np
from scipy.linalg import eigh
ctx.prec=768
def af(x):
 q=F(x);return arb(fmpq(q.numerator,q.denominator))
def box(x):return af(x[0]).union(af(x[1]))
def mat(a):return arb_mat([[box(x) for x in r] for r in a])
def rat(a):return arb_mat([[af(x) for x in r] for r in a])
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def sym(a):return (a+a.transpose())/2
def sub(a,l,h):return arb_mat([[a[i,j] for j in range(a.ncols())] for i in range(l,h)])
def pos(a):
 a=sym(a);n=a.nrows();l=[[arb(0) for _ in range(n)] for _ in range(n)];ds=[]
 for j in range(n):
  d=a[j,j]-sum((l[j][k]**2*ds[k] for k in range(j)),arb(0))
  if not d>0:return False,j
  ds.append(d);l[j][j]=arb(1)
  for i in range(j+1,n):l[i][j]=(a[i,j]-sum((l[i][k]*l[j][k]*ds[k] for k in range(j)),arb(0)))/d
 return True,n
def lower(a,e):
 n=len(a);m=[[sum(map(F,v))/2 for v in r] for r in a]
 out=[[(m[i][j]+m[j][i])/2 for j in range(n)] for i in range(n)]
 for i in range(n):out[i][i]-=F(e)+sum((F(a[i][j][1])-F(a[i][j][0]))/2+abs(m[i][j]-m[j][i])/2 for j in range(n))
 return out
def read(p):return json.loads(p.read_bytes())
def floats(a):return np.array([[float(a[i,j].mid()) for j in range(a.ncols())] for i in range(a.nrows())])
def form(a,w):return (w.transpose()*a*w)[0,0]
bp=ROOT/'work/inherited/Objekt-X-Unendlicher-Rest-Vergleich-2026-10-09/work/infinite-tail-2026-10-09/FINITE_BRIDGE.json'
sp=ROOT/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/gamma-low-2026-10-09/SCHUR_SHELL_TIGHT_4096.json'
bridge=read(bp);schur=read(sp);rows=[]
for p,label in enumerate(['EVEN','ODD']):
 dp=HERE/f'DIRECT_Y_{label}_3072.json';new=read(dp)
 gp=ROOT/f'work/galerkin84-2026-10-10/GALERKIN_{label}_3072.json';g=read(gp)
 cp=ROOT/f'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/gamma-low-2026-10-09/CERTIFICATE_{label}_gamma224_tight_4096.json'
 cert=read(cp);br=bridge['cases'][p+2];s=schur['cases'][p]
 DY=lower(new['D_Y_model'],new['operator_error'])
 change=[[DY[i][j]-F(s['D_Y_lower'][i][j]) for j in range(8)] for i in range(8)]
 Qhat=[[F(br['Q8'][i][j])+change[i][j] for j in range(8)] for i in range(8)]
 improves=pos(rat(change));assert improves[0],improves
 assert pos(rat(Qhat))[0]
 C=mat(g['C84_model']);cl=sub(C,0,191);cz=sub(C,191,195);cy=sub(C,195,203)
 base=cl.transpose()*cl/(1-af(cert['rho']))+2*cz.transpose()*rat(br['N']).inv()*cz
 R=sym(base+cy.transpose()*rat(Qhat).inv()*cy)
 B=mat(g['B84_model'])+af('9999999999/10000000000')*mat(g['optional_positive_potential_comparison']['potential84_model'])
 er=box(g['R84_operator_error_scalar']);eb=box(g['optional_positive_potential_comparison']['Bplus_operator_error_scalar'])
 assert pos(B-eye(84)*eb)[0]
 gate=pos(B-R-eye(84)*(er+eb))
 ev,vec=eigh(floats(R),floats(B));w=vec[:,-1];w/=np.linalg.norm(w)
 wr=[F(round(float(x)*10**12),10**12) for x in w];wa=arb_mat([[af(x)] for x in wr]);w2=form(eye(84),wa)
 elo=F(math.floor(ev[-1]*10**6)-2,10**6);ehi=F(math.ceil(ev[-1]*10**6)+2,10**6)
 assert pos(af(ehi)*B-R-eye(84)*(af(ehi)*eb+er))[0]
 quotient=(form(R,wa)-er*w2)/(form(B,wa)+eb*w2)
 assert quotient>af(elo)
 record={'parity':label.lower(),'D_Y_lower_new':DY,'D_Y_lower_improvement':change,'Qhat8':Qhat,
  'D_Y_improvement_positive':True,'compatible_common_bridge_proved_conditional_on_inherited_operator_bounds':True,
  'finite_gate_positive':gate[0],'finite_generalized_eigenvalue_lower':elo,'finite_generalized_eigenvalue_upper':ehi,
  'rational_witness':wr,'witness_ratio_lower':quotient,'R84_new_model':R,'R84_error_scalar':er,
  'Bplus_error_scalar':eb,'bindings':{str(q.relative_to(ROOT)):hashlib.sha256(q.read_bytes()).hexdigest() for q in [dp,gp,cp,bp,sp]},
  'new_full_residual_computed':False,'full_remainder_certified':False}
 rows.append(record)
 print(label,'certified interval',str(elo),str(ehi),'gate',gate[0],flush=True)
 # Almost all of N can be retained: the residual R after the fixed P is tiny.
 # F >= diag(theta*N, K_lower + change - Gamma/(1-theta)) in T_P coordinates.
 theta=F(9999999999,10**10)
 Qfull=[[F(s['K_lower'][i][j])+change[i][j]-F(s['Gamma_R_upper'][i][j])/(1-theta) for j in range(8)] for i in range(8)]
 assert pos(rat(Qfull)-rat(br['Q8']))[0]
 Rfull=sym(cl.transpose()*cl/(1-af(cert['rho']))+cz.transpose()*rat(br['N']).inv()*cz/af(theta)+cy.transpose()*rat(Qfull).inv()*cy)
 ev2,vec2=eigh(floats(Rfull),floats(B));w=vec2[:,-1];w/=np.linalg.norm(w)
 wr2=[F(round(float(x)*10**12),10**12) for x in w];wa2=arb_mat([[af(x)] for x in wr2]);w22=form(eye(84),wa2)
 lo2=F(math.floor(ev2[-1]*10**6)-2,10**6);hi2=F(math.ceil(ev2[-1]*10**6)+2,10**6)
 assert pos(af(hi2)*B-Rfull-eye(84)*(af(hi2)*eb+er))[0]
 quotient2=(form(Rfull,wa2)-er*w22)/(form(B,wa2)+eb*w22)
 assert quotient2>af(lo2)
 record['retained_four_block']={'theta':theta,'Qhat8':Qfull,'finite_generalized_eigenvalue_lower':lo2,
  'finite_generalized_eigenvalue_upper':hi2,'rational_witness':wr2,'witness_ratio_lower':quotient2,
  'R84_model':Rfull,'finite_gate_positive':pos(B-Rfull-eye(84)*(er+eb))[0]}
 print(label,'retained-four interval',str(lo2),str(hi2),flush=True)
(HERE/'DIRECTIONAL_GATE.json').write_text(json.dumps(serial({'status':'DIRECTIONAL_FINITE_BRIDGE_TESTED','cases':rows,'full_remainder_certified':False},80),indent=2)+'\n')
