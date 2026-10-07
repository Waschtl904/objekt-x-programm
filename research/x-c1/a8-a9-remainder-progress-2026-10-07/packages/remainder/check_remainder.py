"""Exact arithmetic checks for the new shell-coordinate research note.

This verifies constants and geometry, not the analytic form-domain theorem
or positivity of the complete remainder. Standard library only.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,runpy,io,contextlib


def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[1],-x[0])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    v=[a*b for a in x for b in y]
    return min(v),max(v)
def scale(x,c): return mul(x,(F(c),F(c)))
def sq(x):
    assert x[0]>=0
    return x[0]**2,x[1]**2


def log_interval(x,n=400):
    x=F(x)
    assert x>=1
    t=(x-1)/(x+1)
    s=2*sum((t**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    rem=2*t**(2*n+1)/(F(2*n+1)*(1-t*t))
    return s,s+rem


def atan_interval(x,n=90):
    x=F(x)
    s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    nxt=(-1)**n*x**(2*n+1)/F(2*n+1)
    return min(s,s+nxt),max(s,s+nxt)


def exp_interval(x,n=100):
    x=F(x);t=s=F(1)
    for k in range(1,n+1):t*=x/k;s+=t
    nxt=t*x/(n+1)
    return s,s+nxt/(1-x/F(n+2))


def bounds_text(x):
    # Short outward decimal endpoints; no floating-point certification.
    d=10**24
    lo=(x[0]*d).__floor__()
    hi=-(-x[1]*d).__floor__()
    def dec(v):
        sign='-' if v<0 else '';v=abs(v)
        return sign+str(v//d)+'.'+str(v%d).zfill(24)
    return [dec(lo),dec(hi)]


def run():
    package=Path(__file__).resolve().parent
    bindings=json.loads((package/'SOURCE_BINDINGS.json').read_bytes())
    for item in bindings['inputs']:
        actual=hashlib.sha256((package/item['copy']).read_bytes()).hexdigest()
        assert actual==item['sha256'],item['copy']
    buffer=io.StringIO()
    with contextlib.redirect_stdout(buffer):
        runpy.run_path(str(package/'inputs/check_matrices.py'),run_name='__main__')
    old_check=json.loads(buffer.getvalue())
    assert old_check['status']=='PASS_FINAL_MATRICES_ONLY'
    logs={p:log_interval(p) for p in (2,3,5,7)}
    a=scale(logs[2],F(3,2));b=logs[3];h=sub(b,a)
    assert a[0]>1 and a[1]<F(21,20)
    assert b[1]<F(11,10) and 0<h[0]<h[1]<F(3,50)
    assert h[1]<logs[2][0]
    # A linear combination of log(2),log(3),log(5),log(7).
    primes=(2,3,5,7)
    def expr(v):
        out=(F(0),F(0))
        for p,c in zip(primes,v):out=add(out,scale(logs[p],c))
        return out
    def vs(x,y):return tuple(i-j for i,j in zip(x,y))
    def vn(x):return tuple(-i for i in x)
    aa=(F(3,2),0,0,0);bb=(0,1,0,0)
    qlog={2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),
          5:(0,0,1,0),7:(0,0,0,1),8:(3,0,0,0)}
    intervals=[]
    for q,lq in qlog.items():
        left,right=vs(aa,lq),vs(bb,lq)
        for sign,l,r in [(1,left,right),(-1,vn(right),vn(left))]:
            lower=expr(vs(l,vn(aa)));upper=expr(vs(aa,r))
            assert lower[0]>=0 and upper[0]>=0
            assert expr(vs(r,l))[0]>0
            intervals.append({'q':q,'source_shell':sign,'l':l,'r':r})
    intervals.sort(key=lambda row:sum(expr(row['l'])))
    touching=[]
    for x,y in zip(intervals,intervals[1:]):
        diff=vs(y['l'],x['r'])
        if all(c==0 for c in diff):touching.append([x['q'],y['q']])
        else:assert expr(diff)[0]>0
    weightsq=(F(0),F(0))
    for q,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
        assert sq(logs[p])[1]<q
        weightsq=add(weightsq,scale(sq(logs[p]),F(1,q)))
    assert weightsq[1]<F(121,64) # prime norm <11/8
    pi=sub(scale(atan_interval(F(1,5)),16),scale(atan_interval(F(1,239)),4))
    assert pi[1]<F(22,7)
    assert F(251,1000)**2>F(63,1000)
    gamma_cross_bound=F(11,7)+F(251,1000)
    assert gamma_cross_bound<F(73,40)
    assert F(73,40)+F(11,8)==F(16,5)
    assert exp_interval(F(5,3))[1]<F(175,33)
    gamma_euler_upper=F(5773,10000) # inherited A9 analytic bound
    shell_floor=F(5,3)-gamma_euler_upper-F(9,200)
    assert shell_floor>1
    kappa_upper=log_interval(F(176,7))[1]+gamma_euler_upper+F(11,7)
    assert kappa_upper<6
    high_error=F(1,10**6)
    high_inverse_loss=F(3,2)*F(16,5)**2*(1+high_error**2)
    N=2**21
    remote_tail_floor=21*logs[2][0]+1-high_inverse_loss
    assert remote_tail_floor>F(1,10)
    coarse_zero_mode_floor=1-high_inverse_loss
    assert coarse_zero_mode_floor<0
    # The scalar separated remainder conditions are sufficient, not necessary.
    t=(F(1),F(100));coupling=(F(0),F(99))
    assert all(x-y==1 for x,y in zip(t,coupling))
    assert max(coupling)>min(t)
    rows=[]
    for r in intervals:
        rows.append({'q':r['q'],'source_shell':r['source_shell'],
                     'left':bounds_text(expr(r['l'])),
                     'right':bounds_text(expr(r['r']))})
    out={
      'status':'PASS_GEOMETRY_AND_RATIONAL_BOUNDS_ONLY',
      'bound_input_files_verified':len(bindings['inputs']),
      'inherited_final_matrix_checks':len(old_check['checks']),
      'a':bounds_text(a),'b':bounds_text(b),'shell_width':bounds_text(h),
      'prime_image_intervals':rows,'touching_endpoints':touching,
      'prime_norm_squared':bounds_text(weightsq),
      'prime_norm_upper':'11/8','gamma_cross_norm_upper':'73/40',
      'combined_core_shell_norm_upper':'16/5',
      'raw_shell_floor_strictly_above':str(shell_floor),
      'adopted_raw_shell_floor':'1',
      'high_only_inverse_energy_loss_upper':str(high_inverse_loss),
      'coarse_N0_lower_bound':str(coarse_zero_mode_floor),
      'separated_scalar_conditions_not_equivalent':True,
      'remote_tail_N':N,'remote_tail_extra_constraints_at_most':200,
      'remote_tail_lower_floor':'1/10',
      'remote_tail_conditions':'shell moment zero; first N local Legendre moments zero; 191 exact corrected old forces zero; four quotient-orthogonality and four tested-Schur-coupling constraints',
      'full_remainder_positive':False,
      'analytic_domain_proof_machine_verified':False,
      'new_operator_integration':False,
      'target_positivity_used':False,
      'external_review':'OPEN'
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':
    assert __debug__
    run()
