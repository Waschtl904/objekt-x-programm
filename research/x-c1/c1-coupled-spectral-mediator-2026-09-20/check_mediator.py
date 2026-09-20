#!/usr/bin/env python3
"""Exact arithmetic ledger for the coupled spectral candidate.

The analytic theorems are in PROOF.md. This is neither numerical spectral
sampling as a proof nor an independent analytic audit. Standard library only.
"""
from fractions import Fraction as F
from math import factorial,isqrt
from pathlib import Path
import argparse,hashlib,json

HERE=Path(__file__).resolve().parent
ANCHOR='f77116a890410dfbb2c612956dee9e5342247cd7'
PAYLOAD=['PROOF.md','README.md','STATUS_DE.md','check_mediator.py','input_bindings.json','mediator_results.json','mediator_checks.log']

def log_bounds(x,terms=120):
    x=F(x);assert x>=1
    z=(x-1)/(x+1);z2=z*z;t=z;s=F(0)
    for j in range(terms):s+=t/(2*j+1);t*=z2
    return 2*s,2*(s+t/((2*terms+1)*(1-z2)))

def atan_bounds(x,terms=32):
    x=F(x);assert 0<x<1 and terms%2==0
    s=sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(terms)),F(0))
    return s,s+x**(2*terms+1)/(2*terms+1)

def root_bounds(n):
    den=10**24;k=isqrt(n*den**2)
    if k*k==n*den**2:return F(k,den),F(k,den)
    return F(k,den),F(k+1,den)

def exp_bounds(x,terms=24):
    x=F(x);t=F(1);s=t
    for j in range(1,terms+1):t*=x/j;s+=t
    nxt=t*x/(terms+1)
    return s,s+nxt/(1-x/(terms+2))

def directed(x,places=22,upper=False):
    x=F(x);den=10**places
    num=-((-x.numerator*den)//x.denominator) if upper else x.numerator*den//x.denominator
    sign='-' if num<0 else '';num=abs(num)
    return sign+str(num//den)+'.'+str(num%den).zfill(places)

def rational_enclosure(pair,places=22):
    # Decimal strings denote exact decimal rationals, rounded outwards.
    return dict(lower=directed(pair[0],places),upper=directed(pair[1],places,True))

def g_bounds(x,terms=128):
    x=F(x)
    s=sum((2*x*x/(F(4*j+1,2)*(F(4*j+1,2)**2+x*x)) for j in range(terms)),F(0))
    lam=F(4*terms+1,2)
    return s,s+2*x*x*(1/lam**3+1/(4*lam**2))

# Exact sparse multivariate polynomial arithmetic: g,kappa,omega,c.
def const(x):return {(0,0,0,0):F(x)} if x else {}
def var(j):
    e=[0]*4;e[j]=1;return {tuple(e):F(1)}
def add(*polys):
    out={}
    for p in polys:
        for e,v in p.items():out[e]=out.get(e,F(0))+v
    return {e:v for e,v in out.items() if v}
def scale(p,x):return {e:v*x for e,v in p.items() if v*x}
def mul(p,q):
    out={}
    for e,v in p.items():
        for f,w in q.items():
            h=tuple(a+b for a,b in zip(e,f));out[h]=out.get(h,F(0))+v*w
    return {e:v for e,v in out.items() if v}
def square(p):return mul(p,p)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=HERE.parents[2])
    mode=parser.add_mutually_exclusive_group();mode.add_argument('--write',action='store_true');mode.add_argument('--verify',action='store_true')
    args=parser.parse_args();root=args.root.resolve();checks=[];values={}
    def check(name,condition):
        assert condition,name
        checks.append(name)
    binding=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
    check('fixed analytic provenance anchor',binding['anchor']==ANCHOR)
    check('five distinct immutable analytic provenance inputs',len(binding['files'])==len({x['path'] for x in binding['files']})==5)
    for item in binding['files']:
        raw=(root/item['path']).read_bytes()
        check('byte SHA256 and Git binding '+item['path'],len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'])

    logs={q:log_bounds(q) for q in (2,3,5,7,8,9)}
    check('fixed horizon active prime powers stop at seven',logs[7][1]<2<logs[8][0])
    check('B lies inside four fifths and one',F(4,5)<logs[5][0]/2<logs[5][1]/2<1)
    # Machin identity: tan(4 atan(1/5)-atan(1/239))=1 with the angle in (0,pi/2).
    a=F(1,5);tan2=2*a/(1-a*a);tan4=2*tan2/(1-tan2*tan2);b=F(1,239)
    check('exact tangent calculation for the Machin pi identity',(tan4-b)/(1+tan4*b)==1 and 0<tan2<tan4 and 4*a<1)
    at5=atan_bounds(a);at239=atan_bounds(b)
    pi=(16*at5[0]-4*at239[1],16*at5[1]-4*at239[0])
    check('directed Machin intervals prove three less than pi less than 22 over seven',3<pi[0]<pi[1]<F(22,7))
    h8=sum((F(1,j) for j in range(1,9)),F(0))
    gamma=(h8-logs[9][1],h8-logs[8][0])
    check('integral-test Euler constant enclosure lies between one half and two thirds',F(1,2)<gamma[0]<gamma[1]<F(2,3))
    # log(8*pi) = 3 log2 + log pi. Monotonicity avoids huge compounded denominators.
    logpi_lo=log_bounds(pi[0])[0];logpi_hi=log_bounds(pi[1])[1]
    kappa=(3*logs[2][0]+logpi_lo+gamma[0]+pi[0]/2,3*logs[2][1]+logpi_hi+gamma[1]+pi[1]/2)
    check('intrinsic kappa is strictly between five and eleven halves',5<kappa[0]<kappa[1]<F(11,2))
    weights={}
    for q,p in ((2,2),(3,3),(4,2),(5,5),(7,7)):
        rt=root_bounds(q);weights[q]=(logs[p][0]/rt[1],logs[p][1]/rt[0])
        check('positive directed prime-power weight '+str(q),0<weights[q][0]<=weights[q][1]<1)
    check('q4 uses the prime logarithm log2 and exact square root two',weights[4]==(logs[2][0]/2,logs[2][1]/2))
    omega=(sum(v[0] for v in weights.values()),sum(v[1] for v in weights.values()))
    check('sum of all five horizon weights is between five halves and three',F(5,2)<omega[0]<omega[1]<3)
    s=(kappa[0]+2*omega[0],kappa[1]+2*omega[1])
    check('intrinsic envelope constant is between ten and 23 halves',10<s[0]<s[1]<F(23,2)<12)
    values.update(pi=rational_enclosure(pi),Euler_gamma=rational_enclosure(gamma),kappa=rational_enclosure(kappa),omega=rational_enclosure(omega),s=rational_enclosure(s),weights={str(q):rational_enclosure(v) for q,v in weights.items()})

    g,k,w,c=[var(j) for j in range(4)]
    A=add(g,k,scale(w,2));m=add(g,w,scale(c,-1));n=add(k,w,c);form=add(g,scale(k,-1),scale(c,-2))
    check('formal common-envelope sum m plus n equals A',add(m,n)==A)
    check('formal difference m minus n equals the full signed symbol',add(m,scale(n,-1))==form)
    check('exact Gram factorization holds as a four-variable polynomial',add(square(m),scale(square(n),-1))==mul(A,form))
    check('positive readout includes the Gamma Prime cross term',square(m)[(1,0,0,1)]==-2)
    check('positive readout includes the square of the common prime sum',square(m)[(0,0,0,2)]==1)
    check('defect includes coupled mass prime and prime prime terms',square(n)==add(square(k),square(w),square(c),scale(mul(k,w),2),scale(mul(k,c),2),scale(mul(w,c),2)))

    check('exact exponential tail proves e less than three',exp_bounds(1)[1]<3)
    ell=F(4,3);s_upper=F(12);floor=ell**2/(ell+s_upper)
    check('Jensen physical readout floor is two fifteenths',floor==F(2,15))
    check('physical inverse norm squared bound is fifteen halves',1/floor==F(15,2))
    check('bounded defect transfer norm squared bound is ninety',s_upper/floor==90)
    check('form completion comparison constant is 257 halves',1+17/floor==F(257,2))
    check('graph shift dominates the defect bound by five',17-s_upper==5)
    check('Gamma observation bound is ninety one',1+s_upper/floor==91)
    check('small-frequency Gamma coefficient bound is 131 eighths',16+F(1,4)*(1+F(1,2))==F(131,8))
    values['uniform_rational_constants']={key:str(val) for key,val in dict(physical_T_floor=floor,inverse_squared=1/floor,R_squared_bound=90,form_comparison=F(257,2),Gamma_observation_bound=91).items()}

    lower_y=F(2,5);upper_y=F(9,20)
    first=lambda y:4*y*y/(F(1,4)-y*y)
    rest=lambda y:(3*y*y/8)/(1-4*y*y/25)
    check('lower imaginary-axis endpoint first Gamma term is 64 ninths',first(lower_y)==F(64,9))
    check('all remaining imaginary Gamma modes have the stated convergent majorant',0<4*lower_y*lower_y/25<1 and F(1,4)*(1+F(1,2))==F(3,8))
    check('lower endpoint complete absolute Gamma bound is below eight',first(lower_y)+rest(lower_y)<8<10<s[0])
    check('upper endpoint first Gamma term is 324 nineteenth',first(upper_y)==F(324,19))
    check('upper endpoint already makes the envelope strictly negative',first(upper_y)>12>s[1])
    check('imaginary zero bracket stays strictly between zero and Mellin exponent',0<lower_y<upper_y<F(1,2))
    check('Mellin annihilator is nonzero throughout the imaginary zero bracket',upper_y**2-F(1,4)<0 and lower_y>0)
    values['imaginary_pole_bracket']={'lower':str(lower_y),'upper':str(upper_y),'strict':True,'lower_Gamma_absolute_upper':str(first(lower_y)+rest(lower_y))}

    gamma_samples={}
    for frequency in (F(1),F(4),F(16)):
        enclosure=g_bounds(frequency)
        check('positive complete Gamma interval at frequency '+str(frequency),0<enclosure[0]<enclosure[1])
        half=g_bounds(frequency,64)
        check('nested Gamma interval after doubling exact modes at frequency '+str(frequency),half[0]<enclosure[0] and enclosure[1]<half[1])
        gamma_samples[str(frequency)]=rational_enclosure(enclosure)
    n_modes=8;M=F(16)
    harmonic=sum((F(1,j) for j in range(1,n_modes+1)),F(0))/2
    reciprocal=sum((1/F(4*j+1,2) for j in range(n_modes)),F(0))
    partial=sum((2*M*M/(F(4*j+1,2)*(F(4*j+1,2)**2+M*M)) for j in range(n_modes)),F(0))
    check('harmonic divergence lower bound has a verified finite instance',M>=F(4*(n_modes-1)+1,2) and partial>=reciprocal>harmonic)
    values['Gamma_directed_intervals']=gamma_samples
    N=128;g16=g_bounds(M)[0]
    polynomial_error=8*M*M**(2*N+2)/factorial(N+1)**2
    approx_error=F(15,2)*(144/(g16+10)+polynomial_error)
    check('rank 129 Taylor cutoff factor is less than one e minus one hundred',polynomial_error<F(1,10**100))
    check('explicit rational finite-rank approximation error squared is below seventy',approx_error<70)
    check('this conservative error bound does not certify contraction',approx_error>1)
    values['finite_rank_example']={'M':str(M),'N':N,'rank_at_most':N+1,'squared_operator_error_upper':rational_enclosure((approx_error,approx_error)),'proves_contraction':False}
    # Algebra behind transfer of an inherited physical gap; it is conditional.
    # (s+delta)*D^2 <= s*T^2 follows from delta*D^2 <= s*q.
    X=var(0);delta=var(1);ss=var(2);Q=var(3)
    lhs=mul(add(ss,delta),X);rhs=mul(ss,add(Q,X))
    check('conditional contraction comparison has the exact cleared-denominator identity',add(rhs,scale(lhs,-1))==add(mul(ss,Q),scale(mul(delta,X),-1)))

    result=dict(status='AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',anchor=ANCHOR,checks_passed=len(checks),checks=checks,values=values,
      verdict='C1-CANDIDATE-CONSTRUCTED-INTERTWINING-PROVED-COMPACT-GRAM-DEFECT-EXPLICIT',
      domain='Original two-Mellin physical sources; fixed horizon B<=a<=1',
      candidate='T=(g+omega-c)/sqrt(g+kappa+2omega) times the unitary Fourier transform',
      Gram_error='E_a(u,v)=-<D u,D v>; strictly negative on every nonzero diagonal',
      candidate_intertwining_proved=True,defect_naturality_proved=True,
      defect_compact=True,defect_infinite_rank=True,physical_nonlocality_proved=True,
      candidate_properties_are_analytic_theorems_not_inferred_from_finite_checks=True,
      C1c_exact_positive_Gram_proved=False,full_C1_closed=False,
      R_one_contraction_certified=False,negative_full_Weil_source_certified=False,
      new_transport_window_certified=False,moving_191D_low_profile_closed=False,
      unrestricted_horizon_compatibility_proved=False,Object_X_constructed=False,
      reproduction_scope='New exact arithmetic and five provenance bindings only. No inherited matrix-chain replay; no independent analytic audit.')
    raw=(json.dumps(result,indent=2,sort_keys=True)+'\n').encode()
    log=('\n'.join('PASS '+name for name in checks)+'\nPASS '+str(len(checks))+' exact arithmetic checks\nSTATUS AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN\n').encode()
    if args.write:
        (HERE/'mediator_results.json').write_bytes(raw);(HERE/'mediator_checks.log').write_bytes(log)
        (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in PAYLOAD),encoding='ascii',newline='\n')
    if args.verify:
        assert (HERE/'mediator_results.json').read_bytes()==raw,'result bytes differ'
        assert (HERE/'mediator_checks.log').read_bytes()==log,'log bytes differ'
        lines=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        assert [line.split('  ',1)[1] for line in lines]==PAYLOAD
        for line in lines:
            digest,name=line.split('  ',1);assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
    print(log.decode(),end='')
    if args.verify:print('PASS byte-identical JSON/log and seven payload hashes')

if __name__=='__main__':main()
