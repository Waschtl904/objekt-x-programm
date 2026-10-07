"""Fixed eight-dimensional W_X pilot geometry. No operator energies."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,json,sys,hashlib

ROOT=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser()
ap.add_argument('--bits',type=int,required=True)
ap.add_argument('--out',type=Path,required=True)
ap.add_argument('--deps',type=Path,default=ROOT/'work/inverse-energy-deps')
ap.add_argument('--quotient-input',type=Path,default=ROOT/'outputs/Objekt-X-A8-Acht-Quellen-2026-10-05/QUOTIENT_NORM.json')
ap.add_argument('--protocol',type=Path,default=ROOT/'outputs/Objekt-X-Restpilot-Protokoll-2026-10-06/PROTOCOL.json')
args=ap.parse_args()
sys.path.insert(0,str(args.deps))
import flint
from flint import arb,arb_poly,arb_mat,fmpq,ctx
ctx.prec=args.bits

def af(x):
    v=F(x);return arb(fmpq(v.numerator,v.denominator))
def box(v):
    a,b=map(F,v);return af((a+b)/2)+arb(0,af((b-a)/2))
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def sym(m):
    n=m.nrows();r=arb_mat(n,n)
    for i in range(n):
        for j in range(i,n):r[i,j]=r[j,i]=(m[i,j]+m[j,i])/2
    return r
def integral(p,left=-1):
    if left==0:return sum((p[k]/(k+1) for k in range(len(p))),arb(0))
    return sum((2*p[k]/(k+1) for k in range(0,len(p),2)),arb(0))
def legendre(n):
    x=arb_poly([0,1]);ps=[arb_poly([1]),x]
    for j in range(1,n):ps.append(((2*j+1)*x*ps[-1]-j*ps[-2])*af(F(1,j+1)))
    return ps
def ldl(m):
    n=m.nrows();ls=eye(n);ds=[]
    for j in range(n):
        d=m[j,j]-sum((ls[j,k]**2*ds[k] for k in range(j)),arb(0))
        assert d>0,('LDL',j,d)
        ds.append(d)
        for i in range(j+1,n):
            ls[i,j]=(m[i,j]-sum((ls[i,k]*ls[j,k]*ds[k] for k in range(j)),arb(0)))/d
    return ls,ds
def cholesky(m):
    n=m.nrows();lower=arb_mat(n,n)
    for i in range(n):
        for j in range(i+1):
            v=m[i,j]-sum((lower[i,k]*lower[j,k] for k in range(j)),arb(0))
            if i==j:
                assert v>0;lower[i,j]=v.sqrt()
            else:lower[i,j]=v/lower[j,j]
    return lower
def zero_check(m):
    assert all(m[i,j].contains(0) for i in range(m.nrows()) for j in range(m.ncols()))
    width=max((2*m[i,j].rad().upper() for i in range(m.nrows()) for j in range(m.ncols())))
    assert width<af('1e-120'),width
    return width
def serial(x):
    if isinstance(x,arb):
        scale=10**90
        return [str(F(int((x.lower()*scale).floor().unique_fmpz()),scale)),
                str(F(int((x.upper()*scale).ceil().unique_fmpz()),scale))]
    if isinstance(x,arb_mat):return [[serial(x[i,j]) for j in range(x.ncols())] for i in range(x.nrows())]
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serial(v) for v in x]
    return x

assert not args.out.exists()
protocol=json.loads(args.protocol.read_bytes())
assert protocol['right_shell_legendre_seed_degrees']==list(range(4,12))
assert protocol['projection_geometry']=='W_X'
known=json.loads(args.quotient_input.read_bytes())
a=3*arb(2).log()/2;b=arb(3).log();h=b-a;c=(a+b)/2;d=h/2
ps=legendre(11)
ell=[ps[n]*((2*n+1)/(2*h)).sqrt() for n in range(12)]
localGram=arb_mat([[h*integral(f*g) for g in ell] for f in ell])
zero_check(localGram-eye(12))
records=[]
for p,label in enumerate(('even','odd')):
    z=b/2
    mp=arb_poly([z**k/factorial(k) if k%2==p else arb(0) for k in range(161)])
    mtail=z**161/factorial(161)/(1-z/162)
    moments=[integral(ps[n]*mp,0)+arb(0,mtail.upper()) for n in range(p,p+10,2)]
    profiles=[]
    for j,n in enumerate(range(p+2,p+10,2)):
        ratio=arb(F(2*n+1,2*p+1).numerator).sqrt()/arb(F(2*n+1,2*p+1).denominator).sqrt()
        cn=ratio*moments[j+1]/moments[0]
        physical=(ps[n]*arb(2*n+1).sqrt()-ps[p]*cn*arb(2*p+1).sqrt())*(1/(2*b).sqrt())
        profiles.append(physical(arb_poly([c/b,d/b])))
    # Exact local coefficients of the four old tested shell polynomials.
    C=arb_mat(12,4)
    for i in range(12):
        for j,n in enumerate(range(p+2,p+10,2)):
            if i>n:
                assert integral(ell[i]*profiles[j]).contains(0)
                C[i,j]=0
            else:C[i,j]=h*integral(ell[i]*profiles[j])
    minor=arb_mat([[C[i,j] for j in range(4)] for i in range(4)]).det()
    assert not minor.contains(0),('first-four minor',p,minor)
    # Mellin moments on the physical shell; uniform exponential tail included.
    co=(c/2).cosh();si=(c/2).sinh();z=d/2
    shell_m=arb_poly([z**k/factorial(k)*(co if (k+p)%2==0 else si) for k in range(161)])
    shell_tail=(c/2).exp()*z**161/factorial(161)/(1-z/162)
    lam=[d*integral(f*shell_m)+arb(0,((h/2).sqrt()*shell_tail).upper()) for f in ell]
    mu=(a.sinh()+(a if p==0 else -a))/2
    assert mu>0
    WX=arb_mat([[int(i==j)+2*lam[i]*lam[j]/mu for j in range(12)] for i in range(12)])
    Q=sym(C.transpose()*WX*C)
    _,qpiv=ldl(Q)
    supplied=known['blocks'][p]['L2_quotient_gram']
    assert all(Q[i,j].overlaps(box(supplied[i][j])) for i in range(4) for j in range(4))
    test_projection=C*Q.inv()*C.transpose()*WX
    rho=eye(12)-test_projection
    V=arb_mat([[rho[i,j] for j in range(4,12)] for i in range(12)])
    orthogonality_width=zero_check(C.transpose()*WX*V)
    H=sym(V.transpose()*WX*V)
    _,hpiv=ldl(H)
    L=cholesky(H)
    E=V*L.transpose().inv()
    normalized_width=zero_check(E.transpose()*WX*E-eye(8))
    zero_check(C.transpose()*WX*E)
    P8=E*E.transpose()*WX
    zero_check(P8*P8-P8)
    zero_check(P8.transpose()*WX-WX*P8)
    records.append({'parity':label,'test_degrees':list(range(p+2,p+10,2)),
      'first_four_test_coefficients_determinant':minor,
      'shell_moment_norm_core':mu,'shell_legendre_moments':lam,
      'WX_gram_12':WX,'tested_source_coefficients_12x4':C,'tested_quotient_gram':Q,
      'tested_quotient_ldl_pivots':qpiv,'raw_pilot_coefficients_12x8':V,
      'raw_pilot_WX_gram':H,'raw_pilot_ldl_pivots':hpiv,
      'normalized_pilot_coefficients_12x8':E,
      'P8_restriction_to_polynomials_12x12':P8,
      'orthogonality_interval_width_upper':orthogonality_width,
      'normalized_gram_interval_width_upper':normalized_width,
      'rank_eight_certified':True,'source_quotient_gram_overlap':True})
out={'status':'PASS_FIXED_PILOT_GEOMETRY_ONLY','bits':args.bits,'python_flint':flint.__version__,
     'protocol_sha256':hashlib.sha256(args.protocol.read_bytes()).hexdigest(),
     'source_quotient_sha256':hashlib.sha256(args.quotient_input.read_bytes()).hexdigest(),
     'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'a':a,'b':b,'h':h,'blocks':records,
     'B00_computed':False,'cross_gram_computed':False,'tail_norm_computed':False,
     'full_remainder_certified':False,'new_operator_integration':False}
args.out.write_text(json.dumps(serial(out),indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'bits':args.bits,
  'parities':[{'parity':r['parity'],'dimension':8,'first_four_minor':r['first_four_test_coefficients_determinant'].str(12),
    'smallest_raw_LDL_pivot':min(x.lower() for x in r['raw_pilot_ldl_pivots']).str(12)} for r in records]},indent=2))
