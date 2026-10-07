"""Generate rational preconditioners; the separate checker proves their use.
An approximate preconditioner itself is not trusted as a certificate.
"""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time,argparse
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True)
ap.add_argument('--out',type=Path,required=True);ap.add_argument('--deps',type=Path,default=ROOT/'work/inverse-energy-deps')
args=ap.parse_args();sys.path.insert(0,str(args.deps))
from flint import arb,arb_mat,fmpq,ctx
ctx.prec=1024
def af(x):
    x=F(x);return arb(fmpq(x.numerator,x.denominator))
def invchol(a):
    n=a.nrows();ls=arb_mat([[int(i==j) for j in range(n)] for i in range(n)]);ds=[]
    for j in range(n):
        d=a[j,j]-sum((ls[j,k]**2*ds[k] for k in range(j)),arb(0));assert d>0
        ds.append(d)
        for i in range(j+1,n):ls[i,j]=(a[i,j]-sum((ls[i,k]*ls[j,k]*ds[k] for k in range(j)),arb(0)))/d
    li=ls.inv();return arb_mat([[li[i,j]/ds[i].sqrt() for j in range(n)] for i in range(n)])
def floor_scaled(x,s):
    m,e=map(int,x.mid().man_exp());f=F(m*2**e) if e>=0 else F(m,2**(-e))
    f*=s;return f.numerator//f.denominator
data=json.loads(args.source.read_bytes());out=[];scale=10**60
for b in data['blocks']:
    ints=[[int(v) for v in row] for row in b['rational_Fbar_integer_matrix']]
    den=10**90;r=b['retained_rank'];kappa=F(b['tail_energy_kappa'])
    variants=[('Fbar',ints,den)]
    small=[[ints[i][j]*kappa.numerator-(den*kappa.denominator if i==j else 0) for j in range(r,191)] for i in range(r,191)]
    variants.append(('tail_gap',small,den*kappa.numerator))
    for name,m,d in variants:
        a=arb_mat([[af(F(v,d)) for v in row] for row in m]);x=invchol(a)
        xi=[[str(floor_scaled(x[i,j],scale)) if j<=i else '0' for j in range(x.ncols())] for i in range(x.nrows())]
        out.append({'parity':b['parity'],'matrix':name,'dimension':len(m),'matrix_denominator':str(d),
            'preconditioner_scale_digits':60,'lower_triangular_preconditioner_integers':xi})
        print(time.strftime('%H:%M:%S'),b['parity'],name,'preconditioner generated',flush=True)
path=args.out;assert not path.exists()
path.write_text(json.dumps({'status':'PRECONDITIONERS_TO_BE_VERIFIED_BY_INTEGER_CONGRUENCE','certificates':out},indent=2)+'\n')
