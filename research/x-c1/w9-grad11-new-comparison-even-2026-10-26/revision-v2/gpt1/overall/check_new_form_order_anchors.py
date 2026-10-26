"""GPT1: exact new form-order anchors; no model search or quadratures."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import sys, json, hashlib, time
if sys.flags.optimize or not __debug__:raise SystemExit('OPTIMIZED_PYTHON_REJECTED')
P=Path(__file__).resolve().parent;A=P.parent/'new-comparison-review-2026-10-26/author'
H=A/'workspace/work/breakthrough-2026-10-25'
sys.dont_write_bytecode=True
sys.path.insert(0,str(P.parent/'grad11-review/deps'))
sys.path.insert(0,str(A/'repository/research/x-c1/w9-partial-energy-2026-10-18'))
from common import Inputs
start=time.monotonic()
def need(v,msg):
    if not v:raise RuntimeError(msg)
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
inp=Inputs();common=inp.json('common')['cases'][0];old=inp.json('old_sources')['cases'][0]
low=read(H/'LOW_SCHUR_CERTIFICATE.json');gr=read(H/'GAMMA_RESERVE.json')
n=191;d0=Q(low['delta0']);p0=Q(low['p0']);p1=Q(low['p1']);eb=Q(old['old_certificate']['old_coupling_error_norm'][1])
need(eb==Q(low['coupling_error_upper']),'e_B binding')
need(p0==Q(common['coupling_padding']) and 0<p1<p0 and d0==Q(common['delta']),'Parameters')
HB0=[[Q(int(x),int(common['HB_denominator']))for x in row]for row in common['HB_integer_matrix']]
HB1=[[Q(int(x),int(low['HB1_denominator']))for x in row]for row in low['HB1_integer']]
F8=[[Q(int(x),int(common['F_denominator']))for x in row]for row in common['F_integer_matrix']]
F1=[[Q(x)for x in row]for row in low['F1_rational']]
GB=[[(Q(int(a),10**100),Q(int(b),10**100))for a,b in row]for row in old['old_raw_coupling_gram']]
need(HB1==list(map(list,zip(*HB1))) and F1==list(map(list,zip(*F1))),'Symmetric exact matrices')
need(all(F1[i][j]==F8[i][j]+(HB0[i][j]-HB1[i][j])/d0 for i in range(n)for j in range(n)),'F1 exact identity')
def enclosure(p):
    return [[((1+p)*lo+(1+1/p)*eb**2*(i==j),(1+p)*hi+(1+1/p)*eb**2*(i==j))for j,(lo,hi)in enumerate(row)]for i,row in enumerate(GB)]
def difference_bounds(M,I):
    lower=[];upper=[]
    for i in range(n):
        off=sum((max(abs(M[i][j]-I[i][j][0]),abs(M[i][j]-I[i][j][1]))for j in range(n)if i!=j),Q())
        lower.append(M[i][i]-I[i][i][1]-off);upper.append(M[i][i]-I[i][i][0]+off)
    return min(lower),max(upper)
l1,u1=difference_bounds(HB1,enclosure(p1));l0,u0=difference_bounds(HB0,enclosure(p0))
need(l1>=0,'HB1 does not majorize the actual Young envelope')
deficit=max(Q(),-l0)
need(u1==Q(low['HB1_rounding_operator_bound']) and deficit==Q(low['HB0_comparison_deficit']),'Recorded enclosure errors')
loss=((1/p1-1/p0)*eb**2+u1+deficit)/d0
r=Q(gr['reserve_added_to_A0']);need(r==Q('1e-40') and r-loss>0,'Monotonicity margin')
need(r-loss==Q(gr['HB_monotonicity_exact_lower_I']),'Monotonicity output')
print('EXACT_HB1_AND_LOW_ORDER_PASS',flush=True)

# Recompute the uniform real remainder of the same exact Gamma224 polynomial.
# Its coefficient identity was already audited; no new polynomial is chosen.
cor=read(H/'inputs/CORRECTION_4096.json');gamma=list(map(Q,cor['Gamma_new_coefficients']))
pc=[4*gamma[k] if k%2==0 else Q()for k in range(225)]
ps=[Q(1)]+[4*gamma[k-1] if k%2==0 else Q()for k in range(1,226)]
def conv(a,b):
    v=[Q()for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:v[i+j]+=x*y
    return v
cc=[Q(1,factorial(k))if k%2==0 else Q()for k in range(257)]
ss=[Q(1,factorial(k+1))if k%2==0 else Q()for k in range(257)]
rc=conv(pc,cc);rs=conv(ps,ss);rc[0]-=1;rs[0]-=1
need(not any(rc[:225]) and not any(rs[:226]),'Exact reciprocal identities')
rad=Q(26,25)
fc=sum((abs(x)*rad**k for k,x in enumerate(rc)if k>=225),Q())
fs=sum((abs(x)*rad**(k-1)for k,x in enumerate(rs)if k>=226),Q())
tc=rad**258/factorial(258)/(1-rad**2/(259*260))
ts=rad**257/factorial(259)/(1-rad**2/(260*261))
nc=sum((abs(x)*rad**k for k,x in enumerate(pc)),Q());ns=sum((abs(x)*rad**k for k,x in enumerate(ps)),Q())
kernel=(fc+fs+nc*tc+ns*ts)/4
need(kernel<=Q(gr['new_kernel_error'][1]),'Saved new kernel upper bound')
oldkernel=Q(cor['Gamma_new_kernel_error_exact'])
recovered=Q(42,5)*(oldkernel-kernel)
need(recovered>r,'Insufficient Gamma reserve recovery')
print('EXACT_SAME_POLYNOMIAL_GAMMA_RESERVE_PASS',flush=True)
out={'status':'GPT1_NEW_FORM_ORDER_ANCHORS_PASS','no_quadratures':True,
     'HB1_dimension':191,'actual_coupling_is_still_assumed_under_H2_H3':True,
     'HB1_Young_enclosure_lower':str(l1),'HB1_rounding_operator_upper':str(u1),
     'F1_identity_all_entries':True,'positive_monotonicity_margin':str(r-loss),
     'same_Gamma224_real_error_upper_exact':str(kernel),'recovered_low_reserve_exact':str(recovered),
     'paid_reserve':'1/10000000000000000000000000000000000000000',
     'source_sha256':{f:sha(H/f)for f in ['LOW_SCHUR_CERTIFICATE.json','GAMMA_RESERVE.json','inputs/CORRECTION_4096.json']},
     'seconds':time.monotonic()-start}
(P/'NEW_FORM_ORDER_ANCHORS.json').write_text(json.dumps(out,indent=2)+'\n')
print('Anchors finished',round(out['seconds'],2),'seconds',flush=True)
