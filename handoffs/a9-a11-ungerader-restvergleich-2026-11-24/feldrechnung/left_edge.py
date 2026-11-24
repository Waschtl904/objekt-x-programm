"""Log-polynomial continuation at the left endpoint plus the signed finite Cauchy measure."""
from pathlib import Path
from types import ModuleType
import json,hashlib,math
shared=Path(__file__).with_name('panels.py')
setup=shared.read_text(encoding='utf8').split('panels=[]')[0]
assert setup.count('    return mod')==1
exec(compile(setup.replace('    return mod','    mod.formula=src\n    return mod'),str(shared),'exec'))
edge=ModuleType('odd_left')
before='        gap=z.b.real.lower()-1 if z.b.real>1 else -z.b.real.upper()'
assert tm.formula.count(before)==1
f=tm.formula.replace(before,"        if z.b.real.contains(1): return ans\n"+before)
assert f.count('((x-a).log()+(b-x).log())')==1
f=f.replace('((x-a).log()+(b-x).log())','(LOGVAL+(b-x).log())')
exec(compile(f,'odd_left_taylor','exec'),edge.__dict__)
original_lg=edge.lg
original_ilog=edge.ilog
width=(outer_edges[1]-a)/32
def log_affine(z):
    z=edge.jet(z)
    if not z.b.contains(0):
        return original_lg(z)
    # Singularity is z=x/a-1 or its negative (log 8 = 2a).
    assert z.s.length()==2 and (z.s[0]-z.s[1]).contains(0)
    assert abs(z.s[1]).overlaps(width/(2*a))
    return edge.jet(edge.LOGVAL-a.log())
edge.lg=log_affine
def left_ilog(s,r):
    if not s.b.real.contains(1):
        return original_ilog(s,r)
    t=s.s-1
    t0=t[0]
    assert t0>0
    R=abs(s.b-1).upper()
    assert R<q('0.003')
    fixed=edge.LOGVAL-a.log()
    if r==1:
        # I_1(1+t) = -pi^2/6 - log^2(t)/2 - Li_2(-t).
        # d[-Li_2(-t)]/dt = log(1+t)/t.
        ds=(s.s.log()/t*t[1]).integral()
        initial=-arb.pi()**2/6-fixed**2/2-acb(-t0).polylog(2).real
        M=arb.pi()**2/6+abs(fixed**2)/2+R/(1-R)
        return edge.Jet(ds+initial,acb(arb(0,M.upper()),arb(0,M.upper())))
    sep=abs(1-r)
    assert sep>2*R
    g=edge.lg(s-r)
    g0=sep.log();lr=abs(r).log()
    deriv=(g.s-g0)/t +lr/s.s+(g0-lr+s.s.log())/(s.s-r)
    initial=edge.BASE_ILOG(s.s[0],r)+g.s[0]*t0.log()
    J=(deriv*s.s[1]).integral()+initial
    derivative_cap=1/(sep-R)+abs(lr)/(1-R)+(abs(g0-lr)+R/(1-R))/(sep-R)
    Jcap=abs(initial)+2*R*derivative_cap
    return edge.Jet(J-g.s*fixed,acb(arb(0,Jcap.upper()),arb(0,Jcap.upper()))-g.b*fixed)
edge.ilog=left_ilog
without_atoms=dict(globals(),hpoints=[])
outputs=[]
for lv in (0,1,-1):
    edge.LOGVAL=arb(lv)
    preview=edge.build(without_atoms,a,a+width,4)
    order=16*math.ceil((float((preview['contour_bound']/q('1e-15')).log()/arb(2).log())+12)/16)
    assert 32<=order<=1536
    result=edge.build(without_atoms,a,a+width,order)
    outputs.append(result)
    print('left analytic coefficient model',lv,order,flush=True)
P0,P1,Pm=[row['polynomial'] for row in outputs]
e0,e1,em=[row['taylor_error'] for row in outputs]
approx=[P0,(P1-Pm)*q('1/2'),(P1+Pm)*q('1/2')-P0]
errors=[e0,(e1+em)/2,(e1+em)/2+e0]
pieces=[]
for poly,error in zip(approx,errors):
    # Uniform bound in the original real Taylor coordinate |t|<=1.
    cut=min(128,len(poly))
    tail=sum((abs(poly[i]).upper() for i in range(cut,len(poly))),arb(0))
    pieces.append(arb_poly(list(poly)[:cut]))
    assert tail<q('1e-12')
    errors[len(pieces)-1]+=tail
def abs_coeff(p):
    return sum((abs(v).upper() for v in p),arb(0))
atoms=[(a-y,wh/(2*delta)) for y,wh in hpoints]+[(a+y,-wh/(2*delta)) for y,wh in hpoints]
assert all(g>0 for g,wgt in atoms)
atom_cap=sum((abs(wgt).upper()/g for g,wgt in atoms),arb(0))
envelope=atom_cap+sum((abs_coeff(p)+er for p,er in zip(pieces,errors)),arb(0))
def tail_energy(d):
    t=-d.log()
    return 2*envelope**2*d*(29+28*t+14*t*t+4*t**3+t**4)
k=0
while tail_energy(width/2**k)>q('1e-13'):
    k+=1
    assert k<214

def direct_nonatomic(x):
    sig=sum((wgt/(g+x-a) for g,wgt in atoms),arb(0))
    return outer_value(x)-sig
checks=[]
for tt in (q('-.8'),q('0'),q('.75')):
    v=width*(1+tt)/2; x=a+v; lg=v.log()
    err=abs(sum((p(tt)*lg**j for j,p in enumerate(pieces)),arb(0))-direct_nonatomic(x)).upper()
    assert err < q('1e-11')
    checks.append(c.enc(err)[1])
total=arb(0);rows=[]
for n in range(k):
    left=width/2**(n+1); mid=3*left/2; rad=left/2
    # On each dyad all ratios are at most 1/3. Keep the signed model to
    # this point, together with the rational Cauchy atoms.
    N=48
    aff=arb_poly([2*mid/width-1,2*rad/width])
    lp=arb_poly([mid.log()]+[arb((-1)**(j+1))*(rad/mid)**j/j for j in range(1,N)])
    lerr=(rad/mid)**N/(N*(1-rad/mid))
    lmax=abs(left.log()).upper()
    worst=sum((err*lmax**j for j,err in enumerate(errors)),arb(0))
    worst+=lerr*(abs_coeff(pieces[1])+(2*lmax+lerr)*abs_coeff(pieces[2]))
    pol=pieces[0](aff)+pieces[1](aff)*lp+pieces[2](aff)*lp*lp
    co=[arb(0)]*N
    for gap,wgt in atoms:
        den=gap+mid;ratio=-rad/den
        term=wgt/den
        # The shorter series is priced in the same supremum error.
        top=abs(term).upper(); rr=abs(ratio).upper()
        J=min(N,max(1,math.ceil(float((q('1e-26')*(1-rr)/(top+q('1e-100'))).log()/rr.log()))))
        for j in range(J):co[j]+=term;term*=ratio
        worst+=top*rr**J/(1-rr)
    pol+=arb_poly(co)
    integ=2*rad*c.pint(pol*pol,arb(-1),arb(1))
    price=(integ.upper().sqrt()+(4*rad).sqrt()*worst)**2
    total+=price
    rows.append(c.enc(price)[1])
result=total+tail_energy(width/2**k)
assert result<q('3e-8')
out=dict(X_squared_upper=c.enc(result)[1],endpoint_X_squared_upper=c.enc(tail_energy(width/2**k))[1],
         envelope=c.enc(envelope)[1],extra_dyads=k,dyadic_upper=rows,orders=[v['order'] for v in outputs],
         point_checks=checks,width=c.enc(width),includes_endpoint=True,
         cache_sha256=hashlib.sha256(args.cache.read_bytes()).hexdigest())
args.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('LEFT WHOLE EDGE',k,float(envelope.upper()),float(result.upper()),flush=True)
