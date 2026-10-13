"""Exploratory Gaussian integration of the complete raw function model.

All point values use Arb; the quadrature remainder is NOT certified.
The output must never be used as a global Gram upper bound.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,sys,runpy,json,time
ap=argparse.ArgumentParser()
ap.add_argument('--package',type=Path,required=True)
ap.add_argument('--parity',choices=['even','odd'],required=True)
ap.add_argument('--outdir',type=Path,required=True)
ap.add_argument('--orders',default='128,256')
args=ap.parse_args();args.outdir.mkdir(parents=True,exist_ok=True)
pkg=args.package.resolve();outdir=args.outdir.resolve();label=args.parity.upper()
sys.path.insert(0,str(pkg))
sys.argv=[str(pkg/'compute_global_model.py'),'--root',str(pkg/'snapshot'),'--bits','3072','--parity',args.parity,'--out',str(outdir/f'REBUILT_{label}.json')]
v=runpy.run_path(str(pkg/'compute_global_model.py'))
g=v['raw_residual_model'].__globals__
globals().update({k:g[k] for k in ['arb','arb_mat','arb_poly','ctx','af','row','matrix_value','polycols','cauchy_moments','row_pair','a','b','h','p','gamma','core_mom','mcore','cells','roots','sourcecoeff','qcoeff','X','phi_matrix']})
import numpy as np
from scipy.special import roots_legendre
from scipy.linalg import eigh

# Exact algebraic precomposition; no change of the model.
def addmat(x,y):
    return arb_mat([[ (x[i,j] if i<x.nrows() else 0)+(y[i,j] if i<y.nrows() else 0) for j in range(203)] for i in range(max(x.nrows(),y.nrows()))])
cm={tag:mat*sourcecoeff for tag,mat in g['source_matrices'].items()}
for tag,mat in g['low_matrices'].items():cm[tag]=addmat(cm.get(tag,arb_mat(1,203)),mat*qcoeff)
cc=[mat*sourcecoeff for mat in g['source_cell_matrices']]
phiq=phi_matrix*qcoeff
from math import comb
rw=arb_mat([[af(gamma[i+l])*comb(i+l,l)*a**l*((-1)**l+(-1)**p)/(2**(i+l)) if i+l<len(gamma) else 0 for l in range(225)] for i in range(225)])
regcoeff=rw*core_mom
fm=arb_mat([[g['pint'](mcore*arb_poly([0]*k+[1]))] for k in range(225)])
regm=rw*fm
def core_cauchy_fast(s):
    ans=arb_mat(1,203)
    for tag,mat in cm.items():
        ans+=row_pair(cauchy_moments(s,arb(0),arb(1),mat.nrows()-1,None if tag is None else roots[tag]),mat,arb_mat)
    for (lo,hi),mat in zip(cells,cc):ans+=row_pair(cauchy_moments(s,roots[lo],roots[hi],mat.nrows()-1),mat,arb_mat)
    for sh,lo,hi,weight in g['old_shifts']:ans+=row_pair(cauchy_moments(s+sh,lo+sh,hi+sh,383),phiq,arb_mat)*weight
    return ans
def core_value_fast(t):
    sign=1
    if t<0:t=-t;sign=(-1)**p
    ans=arb_mat(1,203)
    for tag,mat in cm.items():
        val=matrix_value(mat,t)
        if tag is not None:val*=abs(t-roots[tag]).log()
        ans+=val
    matches=[i for i,(lo,hi) in enumerate(cells) if roots[lo]<t and t<roots[hi]]
    assert len(matches)==1
    ans+=matrix_value(cc[matches[0]],t)
    for sh,lo,hi,weight in g['old_shifts']:
        if lo<t and t<hi:ans+=matrix_value(phiq,t+sh)*weight
    return ans*sign
def exterior_fast(x):
    s=x/a
    ans=-(core_cauchy_fast(s)-((-1)**p)*core_cauchy_fast(-s))/(2*(2*a).sqrt())
    ans-=(2*a).sqrt()/2*matrix_value(regcoeff,x)
    for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:ans-=core_value_fast((x-arb(q).log())/a)*(arb(prime).log()/arb(q).sqrt()/(2*a).sqrt())
    return ans
def core_polynomial_fast(f,x):
    assert f is mcore
    sing=-(sum((f[k]*z for k,z in enumerate(cauchy_moments(x/a,arb(0),arb(1),len(f)-1))),arb(0))-((-1)**p)*sum((f[k]*z for k,z in enumerate(cauchy_moments(-x/a,arb(0),arb(1),len(f)-1))),arb(0)))/2
    reg=-a*matrix_value(regm,x)[0,0]
    sh=-sum((arb(prime).log()/arb(q).sqrt()*f((x-arb(q).log())/a) for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]),arb(0))
    return sing+reg+sh
g['exterior_core']=exterior_fast;g['core_polynomial_exterior']=core_polynomial_fast
raw=g['raw_residual_model'];serial=g['serial']
target=json.loads((pkg/'data/DIRECTIONAL_DERIVATIVE_TARGET.json').read_text())['cases'][p]
C0=g['ratmat'](target['coefficient_midpoints_3x203'])
K=g['ratmat'](g['resp']['K12_new_rational'])
# Arb Cholesky whitening: D=L L^T; row*L^-T has the D-dual norm.
L=[[arb(0) for _ in range(12)] for _ in range(12)]
for i in range(12):
    for j in range(i+1):
        val=K[i,j]-sum((L[i][k]*L[j][k] for k in range(j)),arb(0))
        L[i][j]=val.sqrt() if i==j else val/L[j][j]
Wi=arb_mat(L).transpose().inv();invlow=1/(1-g['rho']).sqrt()
def white(rr):
    last=arb_mat([[rr[0,j] for j in range(191,203)]])*Wi
    return arb_mat([[rr[0,j]*invlow if j<191 else last[0,j-191] for j in range(203)]])
def value(u):
    rr=raw(a+h*u)-row([u.log(),u.log()**2,(1-u).log()])*C0
    return white(rr)*(2*h).sqrt()
ctx.prec=2048
start=time.monotonic()
for pt in g['out']['points']:
    u=af(pt['u']);rr=raw(a+h*u)
    ref=pt['raw_residual_model_1x203']
    assert all(rr[0,j].overlaps(ref[0,j]) for j in range(203))
    radius=max(float(rr[0,j].rad()) for j in range(203))
    assert radius<1e-35,radius
print(label,'FAST_MODEL_CHECK_PASS seconds',time.monotonic()-start,flush=True)
results=[]
for order in map(int,args.orders.split(',')):
    ts,ws=roots_legendre(order);us=(ts+1)/2;ws=ws/2
    yy=[];point_boxes=[];start=time.monotonic();maxrad=0.
    for i,u in enumerate(us):
        vv=value(af(F.from_float(float(u))))
        vals=[float(vv[0,j].mid()) for j in range(203)]
        rad=max(float(vv[0,j].rad()) for j in range(203));maxrad=max(rad,maxrad)
        assert rad<1e-30,(i,rad)
        yy.append(vals);point_boxes.append(serial(vv,45)[0])
        if i%32==0:print(label,'order',order,'point',i,'elapsed',time.monotonic()-start,flush=True)
    yy=np.array(yy)
    V=np.polynomial.legendre.legvander(ts,103)*np.sqrt(2*np.arange(104)+1)
    coeff=V.T@(ws[:,None]*yy)
    remainder=yy-V@coeff
    gram=remainder.T@(ws[:,None]*remainder)
    eigen=np.linalg.eigvalsh(gram)
    record={'order':order,'max_point_radius':maxrad,'quadrature_gram_trace_in_D':float(np.trace(gram)),'quadrature_gram_max_eigenvalue_in_D':float(eigen[-1]),'seconds':time.monotonic()-start}
    results.append(record)
    np.savez(outdir/f'EXPLORATORY_{label}_{order}.npz',nodes=us,weights=ws,values=yy,coefficients=coeff,gram=gram)
    (outdir/f'POINTS_{label}_{order}.json').write_text(json.dumps({'parity':args.parity,'nodes_rational':[str(F.from_float(float(u))) for u in us],'whitened_regularized_values':point_boxes,'rigorous_quadrature_remainder_included':False})+'\n')
    (outdir/f'EXPLORATORY_{label}.json').write_text(json.dumps({'parity':args.parity,'results':results,'global_model_Gram_upper_certified':False,'full_global_model_error_certified':False,'full_remainder_certified':False},indent=2)+'\n')
    print(label,record,flush=True)
