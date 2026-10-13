"""Rational rebuild of all 203 outer-log coefficients and their full tail.

The matrix comparison is in the actual directional budget metric. The
analytic identification of the endpoint coefficient is a separate lemma.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,json,sys
ap=argparse.ArgumentParser()
for name in ['responses','data','out']:ap.add_argument('--'+name,type=Path,required=True)
args=ap.parse_args();sys.path.insert(0,str(args.responses))
import audit as h
ld=h.ld;S=ld.SCALE
def read(p):return json.loads(p.read_bytes())
def pt(v):return ld.point(v)
def sqrt_int(x):
 assert x[0]>=0
 lo=isqrt(x[0]*S);hi=isqrt(x[1]*S)
 if hi*hi<x[1]*S:hi+=1
 return lo,hi
def log_bound(q,k):
 z=F(q-1,q+1);v=2*sum((z**(2*j+1)/F(2*j+1) for j in range(k)),F(0))
 return v,v+2*z**(2*k+1)/F(2*k+1)/(1-z*z)
def mellin(n,b):
 z=ld.div(b,pt(2));lead=pt(1)
 for k in range(1,n+1):lead=ld.mul(lead,ld.div(z,pt(2*k+1)))
 val=term=pt(1)
 for k in range(96):
  term=ld.mul(term,ld.div(ld.mul(z,z),pt(2*(k+1)*(2*n+2*k+3))))
  val=ld.add(val,term)
 ratio=ld.div(ld.mul(z,z),pt(2*97*(2*n+195)))
 error=ld.div(ld.mul(term,ratio),ld.sub(pt(1),ratio))
 return ld.mul(lead,ld.add(val,(0,error[1])))
assert __debug__
base=read(args.data/'ENDPOINT_BASIS_INPUT.json')['cases']
endpoint=read(args.data/'OUTER_ENDPOINT.json')
logtail=read(args.data/'LOG_TAIL_104.json')
b=ld.interval(log_bound(3,240));a=ld.mul(pt(F(3,2)),ld.interval(log_bound(2,160)))
width=ld.sub(b,a)
N=104;dN=F(11,10)+sum((F(1,k) for k in range(1,N+1)),F(0))
rows=[]
for p,label in enumerate(['EVEN','ODD']):
 n=base[p];r=read(args.responses/f'RESPONSES_{label}.json');saved=endpoint['cases'][p]
 ew=[[sqrt_int(ld.div(pt(2*i+1),ld.mul(pt(2),width))) for i in range(96)]]
 eq=h.mmI(ew,h.im(n['Q']))
 jb=[[ld.add(eq[0][j+8],sumv) for j,sumv in enumerate(h.mmI([eq[0][:8]],h.pts(h.rat(n['D'])))[0])]]
 yb=h.mmI(eq,h.pts(h.rat(n['S'])))
 fb=[]
 for k in range(p+2,p+10,2):
  fb.append(ld.mul(sqrt_int(ld.div(pt(2*k+1),ld.mul(pt(2),b))),ld.sub(pt(1),ld.div(mellin(k,b),mellin(p,b)))))
 fb+=yb[0]
 aj=[[pt(0)]*191+fb]
 c=h.sc(h.add(h.sc(h.mmI(jb,h.pts(h.rat(r['X84x203_rational']))),1-F(r['eta'])),aj,-1),F(1,2))
 h.overlaps(jb,h.im(saved['basis84_right_endpoint']))
 h.overlaps(c,h.im(saved['outer_log_coefficient_1x203']))
 j=saved['nonzero_low_column_one_based']-1
 assert 0<=j<191 and (c[0][j][1]<0 or c[0][j][0]>0)
 K=h.rat(r['K12_new_rational']);rho=F(r['rho']);beta=F(r['beta'])
 D=[[1-rho if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
 M=h.rat(r['M_upper_rational']);T=[[beta*(D[i][j]-M[i][j]) for j in range(203)] for i in range(203)]
 cap=F(7,10000) if p==0 else F(8,10000)
 # Sum_{n>=N}|log(1-u)_n|^2/d_n <=2h/(N^2 d_N).
 bottom=F(N*N)*dN/(2*h.upper(width))
 block=[[pt(cap*T[i][j]) if i<203 and j<203 else c[0][i] if i<203 else c[0][j] if j<203 else pt(bottom) for j in range(204)] for i in range(204)]
 proof=ld.positive(block)
 rows.append({'parity':label.lower(),'outer_log_coefficients_rebuilt':203,
  'nonzero_column_one_based':j+1,'nonzero_coefficient_rational_interval':[str(F(x,S)) for x in c[0][j]],
  'full_weighted_outer_log_tail_from_104_relative_to_T_upper':str(cap),
  'rational_tail_matrix_proof':proof,
  'raw_weighted_derivative_energy_infinite_under_endpoint_lemma':True,
  'outer_component_bound_is_not_a_full_residual_bound':True,'full_remainder_certified':False})
 print(label,'203 endpoint coefficients rebuilt; 204 rational pivots; isolated full outer-log tail <',float(cap)*100,'% of T',flush=True)
# Verify the complete auxiliary tail Gram is positively enclosed and its
# fixed rational upper pays every directed entry error.
gi=[[tuple(map(F,x)) for x in row] for row in logtail['full_tail_Gram_intervals']]
gu=h.rat(logtail['full_tail_Gram_rational_upper'])
for i in range(3):
 room=gu[i][i]-gi[i][i][1]
 need=sum(max(abs(gu[i][j]-gi[i][j][0]),abs(gu[i][j]-gi[i][j][1])) for j in range(3) if j!=i)
 assert room>=need
gproof=ld.positive([[ld.interval(x) for x in row] for row in logtail['full_tail_Gram_intervals']])
out={'status':'PASS_EXACT_ENDPOINT_COEFFICIENTS_AND_COMPLETE_OUTER_LOG_TAIL',
 'cases':rows,'full_log_template_Gram_positive':gproof,
 'complete_regular_residual_Gram_available':False,'full_remainder_certified':False}
args.out.write_text(json.dumps(out,indent=2)+'\n')
