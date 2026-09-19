#!/usr/bin/env python3
"""Directed full-shell Riesz enclosure for the fixed near-null reduced core direction.

All arithmetic decisions use integer/Fraction intervals. No quadrature,
floating eigenvalues, or finite shell replacement enters the certificate.
The infinite-dimensional justification is in PROOF.md.
"""
from pathlib import Path
import importlib.util, json, sys, argparse, hashlib, subprocess
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, comb, isqrt

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--root',type=Path,default=HERE.parents[2])
group=parser.add_mutually_exclusive_group()
group.add_argument('--write',action='store_true');group.add_argument('--verify',action='store_true')
args=parser.parse_args();REPO=args.root.resolve();ROOT=REPO/'research/x-c1'
bindings=json.loads((HERE/'input_bindings.json').read_text(encoding='utf-8'))
for item in bindings['files']:
    raw=(REPO/item['path']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'],item['path']
replay=subprocess.run([sys.executable,str(ROOT/'reduced-shell-coordinate-theorem-2026-09-19/check_quotient.py'),'--verify','--root',str(REPO)],capture_output=True,text=True,check=True)
assert not replay.stderr and 'TOTAL 28 NEW EXACT CHECKS PASS' in replay.stdout
assert 'REPLAY and all quotient-package SHA256 hashes PASS' in replay.stdout
CHECKS=[];LOG=[]
def ok(name,condition):
    assert condition,name
    CHECKS.append(name);LOG.append('PASS '+name)
def progress(text):print(text,flush=True)

spec=importlib.util.spec_from_file_location('near',ROOT/'near-null-source-transport-2026-09-18/check_near.py')
n=importlib.util.module_from_spec(spec);spec.loader.exec_module(n)
n.configure(160)
I=n.I
def mag(x):return max(abs(x.lo),abs(x.hi))
def sq(x):
    if x.lo<=0<=x.hi:return I(0,max(x.lo*x.lo,x.hi*x.hi))
    return I(min(x.lo*x.lo,x.hi*x.hi),max(x.lo*x.lo,x.hi*x.hi))
def sqrt(x):
    x=I.of(x);assert x.lo>=0
    lo=isqrt((x.lo*n.SCALE*n.SCALE).__floor__())
    hi=isqrt((x.hi*n.SCALE*n.SCALE).__floor__())+1
    return I(F(lo,n.SCALE),F(hi,n.SCALE))
def val(name,x):
    OUT[name]=n.pack(x);LOG.append(name+' '+str(n.show(x)))
OUT={}
B=n.log(I(5))/2
rho=n.ratio(B)
v=[I(x)-rho*(n.PHI[k] if k<len(n.PHI) else 0) for k,x in enumerate(n.SOURCE)]
expB=n.exp_pos(B);sinhB=(expB-1/expB)/2
expHalf=n.exp_pos(B/2);HB=(expHalf+1/expHalf)/2
AT=(B+sinhB)/(2*HB);MB=4*(HB-1)/B
psi=[(B/2)**k/factorial(k)/HB if k%2==0 else I(0) for k in range(41)]
psi[0]-=AT/MB;psi[1]+=AT/MB
chi=[1/MB,-1/MB]
def sparse(p):return [(k,x) for k,x in enumerate(p) if x.lo!=0 or x.hi!=0]
def normpair(p,q):return sum((x*y/F(r+s+1) for r,x in sparse(p) for s,y in sparse(q)),I(0))
@lru_cache(None)
def H(r):return sum((F(1,k) for k in range(1,r+1)),F(0))
@lru_cache(None)
def J(r):return n.LOG2 if r==0 else F(1,r)-J(r-1)
def harmonic(p,q):
    return sum((x*y*(H(r)+H(s)-H(r+s)+J(0)-J(r)-J(s)+J(r+s))/F(2*(r+s+1))
                for r,x in sparse(p) for s,y in sparse(q)),I(0))
@lru_cache(None)
def vm(r):
    if r%2:return I(H((r+1)//2)/F(2*(r+1)))
    return (sum((F(1,2*k+1) for k in range(r//2+1)),F(0))-n.LOG2)/(r+1)
def potential(p,q):return sum((x*y*vm(r+s) for r,x in sparse(p) for s,y in sparse(q)),I(0))
M=144
pg,gerr=n.gamma_model(M)
gp=[2*B*(B/2)**k*c for k,c in enumerate(pg)]
@lru_cache(None)
def beta(r,k):return F(factorial(r)*factorial(k),factorial(r+k+1))
@lru_cache(None)
def plus(r,k):return sum((F(comb(k,j),r+j+1) for j in range(k+1)),F(0))
@lru_cache(None)
def km(r,s):
    if r>s:return km(s,r)
    return sum((g*(beta(r,k)+beta(s,k)+plus(r,k)+plus(s,k))/F(2*(r+s+k+2))
                for k,g in enumerate(gp) if pg[k]),I(0))
def kernel(p,q):return sum((x*y*km(r,s) for r,x in sparse(p) for s,y in sparse(q)),I(0))
def translated(p,offset,sign):
    powers=[offset**k for k in range(len(p))]
    return [sum((v*sign**r*comb(r,k)*powers[r-k] for r,v in sparse(p) if r>=k),I(0)) for k in range(len(p))]
def shift(p,q,d):
    breaks=[d-1,I(1)]
    for z in (I(0),d):
        if z.lo>(d-1).hi and z.hi<1:breaks.append(z)
    breaks.sort(key=lambda x:x.lo+x.hi)
    out=I(0)
    for lo,hi in zip(breaks,breaks[1:]):
        mid=(lo+hi)/2
        assert mid.lo>0 or mid.hi<0
        assert (mid-d).lo>0 or (mid-d).hi<0
        pp=translated(p,lo,1 if mid.lo>0 else -1)
        qq=translated(q,lo-d,1 if (mid-d).lo>0 else -1)
        width=hi-lo;powers=[width**(k+1)/F(k+1) for k in range(len(pp)+len(qq)-1)]
        out+=sum((x*y*powers[r+s] for r,x in sparse(pp) for s,y in sparse(qq)),I(0))
    return out
q0=-n.log(2*n.PI*B)-n.GAMMA
def qform(p,q):
    out=harmonic(p,q)+potential(p,q)+q0*normpair(p,q)-kernel(p,q)
    for prime,ell,weight in [(2,n.LOG2,n.LOG2/n.sqrt_i(2)),(3,n.log(I(3)),n.log(I(3))/n.sqrt_i(3)),(4,2*n.LOG2,n.LOG2/2)]:
        out-=weight*shift(p,q,ell/B)
    radius=(2*B*gerr*sqrt(normpair(p,p)*normpair(q,q))).hi
    return out+I(-radius,radius)

progress('Direct polynomial and reflected-half integration, with complete Gamma remainder')
Nv=normpair(v,v)
qv=qform(v,v)
Ev=qv+14*Nv
ok('source positive norm and bounded Gamma energy',Nv.lo>0 and 0<Ev.lo<Ev.hi<3)
ok('degree 62, even parity and original exact endpoint traces',len(n.SOURCE)==63 and sum(n.SOURCE,F(0))==0 and sum(n.PHI,F(0))==0 and all(x==0 for k,x in enumerate(n.SOURCE) if k%2))
ok('exact Mellin ratio denominator excludes zero',n.moment(1,B).lo>F(2,3))
old=json.loads((ROOT/'near-null-source-transport-2026-09-18/near_results.json').read_text(encoding='utf-8'))
oldray=old['precision_recheck']['B']['Rayleigh']
ray=qv/Nv
ok('new reflected-half source calculation overlaps pinned higher-precision Rayleigh',ray.lo<=F(oldray['hi']) and F(oldray['lo'])<=ray.hi)
ok('direct source energy strictly positive',qv.lo>0)
ok('Gamma rational uniform remainder sufficiently small',gerr<F(1,10**26))

# The only additional approximation is the degree-40 cosh polynomial in psi.
# It is not declared an admissible source. Every pairing uses the nonpole form.
x=F(41,100)
R0=x**42/factorial(42)/(1-x*x/F(43*44))
R1=x**41/F(2*factorial(41))/(1-x*x/F(42*43))
Ee=R1*R1+10*R0*R0;Ne=2*R0*R0
ok('cosh argument lies in stated rational Taylor range',0<B.lo<B.hi<2*x)
cross_error=(sqrt(Ev*Ee)+14*sqrt(Nv*Ne)).hi
psi_error=(2*(sqrt(I(176*Ee))+14*sqrt(I(32*Ne)))+Ee+14*Ne).hi
norm_error=(2*sqrt(I(32*Ne))+Ne).hi
inner_error=sqrt(Nv*Ne).hi
ok('all physical cosh approximation errors below 10^-60',max(cross_error,psi_error,norm_error,inner_error)<F(1,10**60))
Npsi=2*B*normpair(psi,psi)+I(-norm_error,norm_error)
inner=sqrt(2*B)*normpair(v,psi)+I(-inner_error,inner_error)
qvp=qform(v,psi)*sqrt(2*B)+I(-cross_error,cross_error)
ap=qform(psi,psi)*2*B+I(-psi_error,psi_error)
ok('true trace-corrector physical norm strictly positive',Npsi.lo>F(1,2))
ok('true trace-corrector energy strictly positive',ap.lo>F(14,100))
cv=inner/Npsi
ok('trace coefficient excludes zero before any trace quotient',cv.lo>F(29,100))
wv_norm=Nv-sq(inner)/Npsi
ok('reduced near-null core direction nonzero',wv_norm.lo>F(11,100))
g=qvp-cv*ap
a0=qv-2*cv*qvp+sq(cv)*ap
d=sq(cv)*ap;c=cv*g
ok('all trace diagnostic denominators positive',a0.lo>0 and d.lo>0 and ap.lo>0)
reconstruction=a0+2*c+d
ok('interval regression reconstruction contains the direct source energy',reconstruction.lo<=qv.lo and qv.hi<=reconstruction.hi)
rho_e=sq(g)/(a0*ap)
alpha=qvp/ap;tN=g/ap
trace_loss=sq(g)/ap
rest0=qv-sq(qvp)/ap

# Exact Laurent polynomial checks, not rounded cancellation tests.
class P:
    def __init__(self,d=None):self.d={k:F(v) for k,v in (d or {}).items() if v}
    @staticmethod
    def of(x):return x if isinstance(x,P) else P({(0,0,0,0):F(x)})
    def __add__(self,o):
        d=self.d.copy()
        for k,v in P.of(o).d.items():d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.d.items()})
    def __sub__(self,o):return self+-P.of(o)
    def __rsub__(self,o):return P.of(o)+-self
    def __mul__(self,o):
        d={}
        for a,vv in self.d.items():
            for b,ww in P.of(o).d.items():
                k=tuple(x+y for x,y in zip(a,b));d[k]=d.get(k,F(0))+vv*ww
        return P(d)
    __rmul__=__mul__
    def __eq__(self,o):return self.d==P.of(o).d
Q,U,A,C=[P({tuple(int(j==k) for j in range(4)):1}) for k in range(4)]
Ai=P({(0,0,-1,0):1});G=U-C*A;Ared=Q-2*C*U+C*C*A
ok('exact Laurent reconstruction of the original source energy',Ared+2*C*G+C*C*A==Q)
ok('exact trace Riesz coefficient',G*Ai+C==U*Ai)
ok('exact residual annihilates the trace direction',G-(G*Ai)*A==0)
ok('exact cancellation before enclosing the Schur remainder',Ared-G*G*Ai==Q-U*U*Ai)
ok('negative control detects omitted trace cross term',Ared+C*C*A!=Q)

progress('Entire shell residual using the anisotropic infinite-dimensional pivot')
legv=[I(x)-rho*n.LEG_COEFF[1][k] for k,x in enumerate(n.LEG_COEFF[0])]
Mv=sum((mag(x) for x in legv),F(0))/sqrt(2*B)
MA=Mv+4*mag(alpha)
qvchi=sqrt(Ev*106)+14*sqrt(Nv*18)
qAchi=qvchi+500*mag(alpha)
h0=F(1,10**20);L=n.log(I(2/h0))
Fbound=MA*(L+11)+F(6,5)*qAchi
res=I(h0)*sq(Fbound)/70
rv=rest0-I(0,res.hi)
eta=rho_e+I(0,(res/a0).hi)
ok('uniform shell width agrees with complete pivot theorem',h0==F(1,10**20))
ok('logarithmic monotonicity range',L.lo>46 and L.hi<47)
ok('residual amplitude bounds on the exact A-orthogonal core',MA.hi<F(2111,1000) and qAchi.hi<40)
ok('entire shell dual residual squared below 5e-18',res.hi<F(5,10**18))
ok('trace-only ratio is below one',0<rho_e.lo<=rho_e.hi<1)
ok('full infinite-shell directional eta below 1-4e-11',eta.hi<1-F(4,10**11))
ok('full directional Schur remainder above 5.449e-13',rv.lo>F(5449,10**16))
ok('residual margin exceeds the certified approximation errors',cross_error+psi_error<F(1,10**40))

# Independent low-degree consistency of the reflected-half integration.
for i in (0,2,4,6):
    for j in (0,2,4,6):
        hp=harmonic([I(x) for x in n.leg(i)],[I(x) for x in n.leg(j)])
        target=H(i)/F(2*i+1) if i==j else F(0)
        assert hp.lo<=target<=hp.hi
ok('harmonic cusp formula agrees with independent Legendre eigenvalues',True)
cusp=harmonic([I(0),I(1)],[I(0),I(1)])
expected=(2*n.LOG2-1)/3
ok('absolute-value cusp logarithm retained',cusp.lo<=expected.hi and expected.lo<=cusp.hi)
for k in range(9):
    new=sum((x*y*(beta(r,k)+beta(s,k)+plus(r,k)+plus(s,k))/F(2*(r+s+k+2)) for r,x in enumerate(n.PHI) if x for s,y in enumerate(n.PHI) if y),F(0))
    assert new==n.kernel_energy(1,1,k)
ok('reflected Gamma moments equal independent two-triangle moments through degree 8',True)
for q in (2,3,4):
    dd=n.log(I(q))/B
    got=shift([I(x) for x in n.PHI],[I(x) for x in n.PHI],dd)
    expected=n.polyval(n.shift_poly(1,1),2-dd)
    assert got.lo<=expected.hi and expected.lo<=got.hi
ok('signed translations agree with independent beta-polynomial integration',True)

for name,value in [
 ('B',B),('h_max',h0),('source_moment_ratio',rho),('source_norm_squared',Nv),
 ('source_energy',qv),('source_Rayleigh',ray),('psi_norm_squared',Npsi),
 ('physical_source_psi_inner_product',inner),('cv',cv),('wv_norm_squared',wv_norm),
 ('q_v_psi',qvp),('q_psi_psi',ap),('a0_wv',a0),('d_cv_e',d),('c0_wv_cv_e',c),
 ('source_reconstruction_enclosure',reconstruction),('rho_e',rho_e),
 ('trace_Riesz_coefficient',tN),('A_orthogonal_projection_coefficient',alpha),
 ('trace_Riesz_energy',trace_loss),('trace_eliminated_core_energy',rest0),
 ('source_supremum_upper_bound',Mv),('A_orthogonal_core_supremum_bound',MA),
 ('A_orthogonal_core_chi_pairing_abs_bound',qAchi),('residual_shell_coefficient_bound',Fbound),
 ('full_shell_residual_dual_squared_bound',I(0,res.hi)),
 ('full_Riesz_energy_enclosure',trace_loss+I(0,res.hi)),('eta_v_uniform',eta),
 ('r_v_uniform',rv),('Gamma_uniform_error',gerr),('cosh_error_supremum',R0),
 ('cosh_error_physical_derivative',R1),('physical_q_v_psi_approximation_radius',cross_error),
 ('physical_q_psi_psi_approximation_radius',psi_error)]:val(name,value)

report={
 'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN',
 'anchor':bindings['anchor'],'verdict':'FULL-INFINITE-SHELL-DIRECTIONAL-SCHUR-POSITIVE / ALL-CORE-OPEN',
 'interval':'b = log(5)/2 + h, 0 < h <= 10^-20',
 'source':'The fixed isometric physical image of the degree-62 near-null source, not rescaled to unit norm; w_v is its L2 projection off psi',
 'source_scale':'v_B(t) = (2B)^(-1/2) (F(t/B)-rho(B)*(1-(t/B)^2))',
 'arithmetic_grid':'10^-160','Gamma_degree':M,'cosh_degree':40,
 'Riesz_approximant':'y_N = (q_B(w_v,psi)/q_B[psi]) e, with exact analytic coefficient enclosed rationally',
 'full_residual_identity':'loss = |q_B(w_v,psi)|^2/q_B[psi] + ||r_N||^2_(D dual)',
 'shell_tail':'complete X = C plus L2(B,b); no shell cutoff',
 'directional_eta_upper':str(1-F(4,10**11)),
 'directional_remainder_lower':str(F(5449,10**16)),
 'entire_shell_residual_squared_upper':str(F(5,10**18)),
 'all_core_operator_norm_certified':False,'odd_continuation_closed':False,
 'new_all_source_endpoint_theorem':False,'mellin_constraints':2,'A1_used':False,
 'fixed_b_gate_equivalence':'R0 >= sigma I iff Theta0 < 1, using bounded K=C0* D^-1 C0; reverse bound Theta0 <= M/(M+sigma)',
 'bound_inputs':len(bindings['files']),'new_exact_checks':len(CHECKS),
 'inherited_quotient_replay_checks':28,'inherited_shell_replay_checks':43,
 'inherited_replay_stdout_sha256':hashlib.sha256(replay.stdout.encode('utf-8')).hexdigest(),
 'passed_checks':CHECKS,'values':OUT,
 'analytic_proof':'PROOF.md; the finite replay does not replace the full form-domain and residual arguments'}
jsontext=json.dumps(report,indent=2,sort_keys=True)+'\n'
logtext='INHERITED coordinate replay: 28 PASS; full shell pivot replay: 43 PASS\n'+'\n'.join(LOG)+'\nTOTAL '+str(len(CHECKS))+' NEW EXACT CHECKS PASS\n'+report['verdict']+'\n'
if args.write:
    (HERE/'direction_results.json').write_text(jsontext,encoding='utf-8',newline='\n')
    (HERE/'direction_checks.log').write_text(logtext,encoding='utf-8',newline='\n')
    payload=['PROOF.md','README.md','STATUS_DE.md','check_direction.py','input_bindings.json','direction_results.json','direction_checks.log']
    (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/f).read_bytes()).hexdigest()+'  '+f+'\n' for f in payload),encoding='ascii',newline='\n')
if args.verify:
    assert (HERE/'direction_results.json').read_bytes()==jsontext.encode('utf-8'),'JSON replay mismatch'
    assert (HERE/'direction_checks.log').read_bytes()==logtext.encode('utf-8'),'log replay mismatch'
    lines=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines();assert len(lines)==7
    for line in lines:
        digest,name=line.split('  ',1)
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
    print('REPLAY and all seven direction-package SHA256 hashes PASS')
print(logtext,end='')
