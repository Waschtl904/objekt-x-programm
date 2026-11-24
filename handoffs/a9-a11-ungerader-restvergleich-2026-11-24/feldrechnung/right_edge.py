"""Integrate the complete right endpoint using its signed A(x)+B(x) log(b-x) expansion."""
from pathlib import Path
import json, hashlib
from types import ModuleType
shared=Path(__file__).with_name('panels.py')
setup=shared.read_text(encoding='utf8').split('panels=[]')[0]
assert setup.count('    return mod')==1
exec(compile(setup.replace('    return mod','    mod.formula=src\n    return mod'),str(shared),'exec'))
formula=tm.formula
for before,after in [
    ('val=hjet(ns,x)+peval', 'val=edge_h(ns,x)+peval'),
    ('((x-a).log()+(b-x).log())','((x-a).log()+LOGVAL)'),
    ('((1-x/b).log()+(1+x/b).log())/2','(LOGVAL-b.log()+(1+x/b).log())/2')
]:
    assert formula.count(before)==1,before
    formula=formula.replace(before,after)
edge=ModuleType('odd_right')
exec(compile(formula,'odd_right_taylor','exec'),edge.__dict__)

def divided_exp(t,k):
    # (1-exp(-kt))/t = k * integral_0^1 exp(-ktu)du, including t=0.
    # The disk bound gives a positive-real-part inclusion for the logarithm.
    R=abs(t.b).upper()
    dev=k*((k*R).exp()-1)
    assert dev<k
    return edge.Jet((1-(-k*t.s).exp())/t.s,acb(arb(k,dev),arb(0,dev)))

def edge_h(ns,x):
    # Only the outer call is replaced. The translated core h uses its own cell.
    rs=ns['res']; A,B=rs.a,rs.b
    assert A.overlaps(b) and not A.overlaps(a)
    model=ns['_scalar_model']
    cell=model['records'][rs.cell(x.s[0],x.s[0])]
    t=A-x; ep=(x/2).exp()
    qp=3*arb(2).log()/2+arb.pi()/4-t-(edge.LOGVAL+divided_exp(t,2).log())/2
    qm=arb(2).log()/2+arb.pi()/4-(edge.LOGVAL+divided_exp(t,1).log()-(1+(-t).exp()).log())/2
    y=A+x
    jp=3*arb(2).log()/2+arb.pi()/4-y-(1-(-2*y).exp()).log()/2
    vv=(-y).exp()
    jm=arb(2).log()/2+arb.pi()/4-((1-vv).log()-(1+vv).log())/2
    ms=(ep*(qp+jm)-(qm+jp)/ep)/2
    vlog=-(edge.LOGVAL+(A+x).log()-2*A.log())/2
    P=edge.peval
    shell=(P(model['ell'],x)*((B-x).log()-edge.LOGVAL)+P(model['quot'],x)
           -P(model['ell'],-x)*((B+x).log()-(A+x).log())-P(model['quot'],-x))/2+P(model['gamma'],x)
    def mm(y):
        e=(y/2).exp();return (e-1/e)/2
    prime=edge.jet(0)
    for wt,sh,kind in cell['terms']:
        term=model['ac']*mm(x+sh) if kind=='core' else P(model['ell'],x+sh) if kind=='plus' else -P(model['ell'],-x-sh)
        prime+=wt*term
    return model['ac']*ms-shell-prime-(P(cell['dp'],x/A)+P(model['dv'],x/A)*vlog+model['dm']*mm(x))/(2*A).sqrt()
edge.edge_h=edge_h
import math
right_width=(b-outer_edges[-2])/32
left=b-right_width
for i in range(len(outer_edges)-1):
    assert not (left<outer_edges[i]<b)
models=[]
for lv in [0,1]:
    edge.LOGVAL=arb(lv)
    probe=edge.build(globals(),left,b,4)
    N=16*math.ceil((float((probe['contour_bound']/q('1e-14')).log()/arb(2).log())+12)/16)
    assert 32<=N<=1536
    models.append(edge.build(globals(),left,b,N))
    print('right analytic part',lv,N,flush=True)
A=models[0]['polynomial']
B=models[1]['polynomial']-A
ea=models[0]['taylor_error']
eb=ea+models[1]['taylor_error']
# Transform the directed polynomials to u=(b-x)/width in [0,1].
aff=arb_poly([1,-2])
P=A(aff)+right_width.log()*B(aff)
Q=B(aff)
def log_integral(poly,j):
    return sum((v*((-1)**j)*math.factorial(j)/(n+1)**(j+1) for n,v in enumerate(poly)),arb(0))
energy=2*right_width*(log_integral(P*P,0)+2*log_integral(P*Q,1)+log_integral(Q*Q,2))
assert energy.upper()>=0
log2norm=(right_width.log()**2-2*right_width.log()+2).sqrt()
err=(2*right_width).sqrt()*(ea+eb*log2norm)
cap=(energy.upper().sqrt()+err)**2
samples=[]
for t in [-0.8,0,0.75]:
    v=q(str(t)); x=(left+b)/2+right_width*v/2
    diff=abs(A(v)+B(v)*(b-x).log()-outer_value(x)).upper()
    assert diff < q('1e-13')
    samples.append(c.enc(diff)[1])
assert cap<q('3e-8')
out=dict(width=c.enc(right_width),orders=[m['order'] for m in models], X_squared_upper=c.enc(cap)[1],
         log_remainder_X=c.enc(err)[1],point_checks=samples,includes_endpoint=True,
         cache_sha256=hashlib.sha256(args.cache.read_bytes()).hexdigest())
args.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print('RIGHT WHOLE EDGE',float(cap.upper()),flush=True)
