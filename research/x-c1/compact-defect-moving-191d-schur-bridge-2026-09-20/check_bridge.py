#!/usr/bin/env python3
"""Exact ledger for the compact-defect/moving-191D bridge.

Universal statements are proved analytically in PROOF.md. Rational model
matrices below check block algebra only, never the physical 191D sign.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,subprocess,sys

HERE=Path(__file__).resolve().parent
ANCHOR='5557d94d048dc05e7c3b4534a5a2d1711bdc71dc'
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_bridge.py','input_bindings.json','bridge_results.json','bridge_checks.log']

def transpose(a):return [list(x) for x in zip(*a)]
def matmul(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,t):return [[x*t for x in r] for r in a]
def identity(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inverse(a):
    n=len(a);v=[list(r)+s for r,s in zip(a,identity(n))]
    for i in range(n):
        k=next(k for k in range(i,n) if v[k][i]);v[i],v[k]=v[k],v[i]
        pivot=v[i][i];v[i]=[x/pivot for x in v[i]]
        for j in range(n):
            if i!=j:
                c=v[j][i];v[j]=[x-c*y for x,y in zip(v[j],v[i])]
    return [r[n:] for r in v]
def ldl_positive(a):
    assert a==transpose(a)
    a=[list(r) for r in a];pivots=[]
    for k in range(len(a)):
        pivot=a[k][k]
        if pivot<=0:return False,pivots+[pivot]
        pivots.append(pivot)
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):a[i][j]-=a[i][k]*a[k][j]/pivot
    return True,pivots
def power(a,n):
    out=identity(len(a))
    for _ in range(n):out=matmul(out,a)
    return out
def decimal(x,places=24,upper=False):
    x=F(x);scale10=10**places
    n=-((-x.numerator*scale10)//x.denominator) if upper else x.numerator*scale10//x.denominator
    sign='-' if n<0 else '';n=abs(n)
    return sign+str(n//scale10)+'.'+str(n%scale10).zfill(places)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=HERE.parents[2])
    mode=ap.add_mutually_exclusive_group();mode.add_argument('--write',action='store_true');mode.add_argument('--verify',action='store_true')
    args=ap.parse_args();root=args.root.resolve();checks=[];values={};replays=[]
    def check(name,condition):
        assert condition,name
        checks.append(name)
    binding=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
    check('current mathematical anchor is 5557d94',binding['anchor']==ANCHOR)
    check('24 distinct complete-package and dependency bindings',len(binding['files'])==len({x['path'] for x in binding['files']})==24)
    for item in binding['files']:
        raw=(root/item['path']).read_bytes()
        check('input bytes SHA256 and Git blob '+item['path'],len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'])
    jobs=[
      ('candidate frozen replay','research/x-c1/c1-coupled-spectral-mediator-2026-09-20/check_mediator.py',['--verify'],['PASS 53 exact arithmetic checks','PASS byte-identical JSON/log and seven payload hashes'],53),
      ('moving-tail frozen math-only replay','research/x-c1/moving-endpoint-uniform-high-tail-2026-09-19/check_tail.py',['--math-only','--verify'],['TOTAL 25 MOVING-ENDPOINT HIGH-TAIL EXACT CHECKS PASS','REPLAY and all seven moving-tail package SHA256 hashes PASS'],25),
      ('moving-tail full provenance run','research/x-c1/moving-endpoint-uniform-high-tail-2026-09-19/check_tail.py',[],['TOTAL 26 MOVING-ENDPOINT HIGH-TAIL EXACT CHECKS PASS','PASS all bound input bytes SHA256 and Git blobs match'],26),
    ]
    for label,path,flags,markers,count in jobs:
        run=subprocess.run([sys.executable,str(root/path),'--root',str(root),*flags],capture_output=True,text=True,encoding='utf-8',check=False)
        check(label,run.returncode==0 and all(marker in run.stdout for marker in markers))
        replays.append(dict(label=label,path=path,arguments=flags,reported_checks=count,stdout_sha256=hashlib.sha256(run.stdout.encode()).hexdigest(),scope='Arithmetic reproduction, not independent analytic audit'))
    s_upper=F(23,2);gamma_floor=F(1,41)
    delta=gamma_floor/(s_upper+gamma_floor);theta=s_upper/(s_upper+gamma_floor)
    check('full high defect reserve is exactly two over 945',delta==F(2,945))
    check('full high defect norm squared upper is exactly 943 over 945',theta==F(943,945))
    check('high contraction and positive reserve sum to one',0<delta<1 and 0<theta<1 and delta+theta==1)
    check('norm floor conversion denominator is 945 halves',1+41*s_upper==F(945,2))
    check('full high inverse norm upper is 945 halves',1/delta==F(945,2))
    check('singular tail itself is below 999 over 1000',theta<F(999,1000)**2)
    even=list(range(2,384,2));odd=list(range(3,385,2))
    check('191 even low coordinates with next degree 384',len(even)==191 and even[0]==2 and even[-1]+2==384)
    check('191 odd low coordinates with next degree 385',len(odd)==191 and odd[0]==3 and odd[-1]+2==385)
    check('critical singular indices are 192 per parity and 383 jointly',len(even)+1==len(odd)+1==192 and len(even)+len(odd)+1==383)
    check('bounded transfer input norm and physical inverse are consistent',F(12)*F(15,2)==90)
    check('sharper s bound is compatible with the inherited norm ninety',s_upper*F(15,2)<90)
    check('Neumann remainder prefactor is 42525',90/delta==42525)
    check('one exact block of 1024 high powers is below one eighth',theta**1024<F(1,8))
    remainder_examples=[]
    for k,target in [(16,F(2,10**10)),(20,F(4,10**14)),(22,F(6,10**16))]:
        n=1024*k-2;upper=F(42525,8**k)
        check('geometric full-response error after '+str(n)+' powers meets the rational target',upper<target)
        remainder_examples.append(dict(N=n,block_count=k,strict_upper=str(upper),published_upper=str(target),decimal_upper=decimal(upper,upper=True),operator_powers_evaluated=False))
    check('entrywise radius converts to a 191 dimensional operator radius',191*F(1,10**20)<F(2,10**18))
    # Exact, noncommuting rational model; no entry is an actual physical coefficient.
    I=identity(2)
    K=[[F(1,4),F(1,16)],[F(1,16),F(1,3)]]
    alpha=[[F(1,2),F(1,20)],[F(1,20),F(2,5)]]
    beta=[[F(1,10),F(1,15)],[-F(1,20),F(1,12)]]
    bt=transpose(beta);hard=add(I,scale(K,-1));hard_inv=inverse(hard)
    C=[alpha[0]+bt[0],alpha[1]+bt[1],beta[0]+K[0],beta[1]+K[1]]
    Qfull=add(identity(4),scale(C,-1))
    schur=add(add(I,scale(alpha,-1)),scale(matmul(matmul(bt,hard_inv),beta),-1))
    check('algebra model C is positive by exact LDL',ldl_positive(C)[0])
    check('algebra model high block lies below the proved theta',ldl_positive(K)[0] and ldl_positive(add(scale(I,theta),scale(K,-1)))[0])
    check('algebra model mixed block inequality holds',ldl_positive(add(scale(alpha,theta),scale(matmul(bt,beta),-1)))[0])
    check('algebra model is not falsely treated as block diagonal',matmul(K,beta)!=matmul(beta,K) and any(x for row in beta for x in row))
    X=matmul(hard_inv,beta)
    # h=(x, Xx+z) changes the full form to diag(S,hard).
    zero=[[F(0),F(0)],[F(0),F(0)]]
    tri=[I[0]+zero[0],I[1]+zero[1],X[0]+I[0],X[1]+I[1]]
    diagonal=[schur[0]+zero[0],schur[1]+zero[1],zero[0]+hard[0],zero[1]+hard[1]]
    check('exact noncommuting square completion has the claimed signs',matmul(matmul(transpose(tri),Qfull),tri)==diagonal)
    A=[[F(2),F(1)],[F(1),F(3)]] # positive square root of the model low Gram
    W=[[F(1,7),-F(1,9)],[F(2,11),F(1,13)]]
    Fmap=A+W
    Hmap=zero+I
    core=matmul(matmul(transpose(Fmap),Qfull),Fmap)
    mix=matmul(matmul(transpose(Hmap),Qfull),Fmap)
    phys=add(core,scale(matmul(matmul(transpose(mix),hard_inv),mix),-1))
    check('model low Gram square root is strictly positive',ldl_positive(A)[0])
    check('physical Schur and defect Schur have exact low-Gram congruence',phys==matmul(matmul(A,schur),A))
    check('adding an arbitrary high lift does not alter the model quotient Schur form',phys==matmul(matmul(transpose(A),schur),A))
    model_residuals=[]
    for N in (0,2,5):
        series=[[F(0),F(0)],[F(0),F(0)]]
        for j in range(N+1):series=add(series,power(K,j))
        exact_tail=add(hard_inv,scale(series,-1))
        check('model resolvent full-tail identity at N '+str(N),exact_tail==matmul(power(K,N+1),hard_inv))
        check('model omitted response is strictly positive at N '+str(N),ldl_positive(exact_tail)[0])
        S_N=add(add(I,scale(alpha,-1)),scale(matmul(matmul(bt,series),beta),-1))
        epsilon=90*theta**(N+2)/delta
        remainder=add(S_N,scale(schur,-1))
        check('model Schur enclosure retains the complete response at N '+str(N),ldl_positive(remainder)[0] and ldl_positive(add(scale(I,epsilon),scale(remainder,-1)))[0])
        model_residuals.append(dict(N=N,exact_resolvent_tail=[[str(x) for x in r] for r in exact_tail]))
    # Lambda version must specialize exactly to the contraction bound.
    for N in (0,2,17):
        lam=F(1);generic=90*theta/(lam-theta)*(theta/lam)**(N+1)
        check('upper-singular certificate specializes at Lambda one N '+str(N),generic==90*theta**(N+2)/delta)
    check('failed coarse largest-norm bound is not a contraction certificate',90>1)
    values.update(delta=str(delta),theta=str(theta),s192_upper='999/1000',high_inverse_upper=str(1/delta),critical_dimension_per_parity=191,critical_dimension_total=382,Neumann_prefactor=str(90/delta),remainder_examples=remainder_examples,model_residuals=model_residuals)
    result=dict(status='AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',anchor=ANCHOR,verdict='UNIFORM-191D-COMPACT-DEFECT-SCHUR-BRIDGE-CLOSED',
      checks_passed=len(checks),checks=checks,values=values,inherited_replays=replays,input_files_bound=24,
      new_analytic_theorems=['complete high defect contraction','critical singular multiplicity bound','physical/defect Schur congruence','Neumann complete-response enclosure','moving singular-value continuity and monotonicity'],
      finite_model_role='Noncommuting block algebra only; not actual physical 191D entries or spectral evidence',
      actual_191D_matrix_entries_certified=False,actual_191D_matrix_sign_certified=False,
      full_R_one_contraction_certified=False,new_positive_window=False,negative_actual_Weil_source=False,
      moving_profile_renewal_closed=False,full_positive_C1_closed=False,Object_X_constructed=False,
      singular_modes_equal_physical_Legendre_low_basis=False,
      scope='Both parities, original two Mellin constraints, fixed horizon log(5)/2<=a<=1',
      inherited_mode_note='25-check math-only frozen replay plus 26-check full provenance run; their stored historical files are not changed.',
      review_note='Analytic theorems are in PROOF.md. Reproduction is not independent external review; no old finite matrix chain replay.')
    raw=(json.dumps(result,sort_keys=True,indent=2)+'\n').encode()
    log=('\n'.join('PASS '+name for name in checks)+'\nPASS '+str(len(checks))+' bridge checks\nINHERITED candidate 53; moving-tail frozen 25; moving-tail full 26\nSTATUS AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN\n').encode()
    if args.write:
        (HERE/'bridge_results.json').write_bytes(raw);(HERE/'bridge_checks.log').write_bytes(log)
        (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in PAYLOAD),encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'bridge_results.json').read_bytes()==raw,'result bytes differ'
        assert (HERE/'bridge_checks.log').read_bytes()==log,'log bytes differ'
        lines=(HERE/'SHA256SUMS').read_text().splitlines();assert [line.split('  ',1)[1] for line in lines]==PAYLOAD
        for line in lines:
            digest,name=line.split('  ',1);assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
    print(log.decode(),end='')
    if args.verify:print('PASS byte-identical JSON/log and seven payload hashes')

if __name__=='__main__':main()
