"""Real logarithmic envelope at both endpoints of the stored signed model."""
from pathlib import Path
code=Path(__file__).with_name('panels.py').read_text(encoding='utf8')
exec(compile(code[:code.index('cuts=list(res.cuts)')],str(Path(__file__).with_name('panels.py')),'exec'))
from math import factorial
def sup(p,l,r): return poly_sup(p,l,r)
def mag(v):return abs(v).upper()
prime=2*sum((wt for _,wt in channels),arb(0))
B=res.b
# h(y) on the old domain: |h(y)| <= HC*(1+|log(b-y)|).
# Exp, jump, and the nonsingular logarithm arguments are bounded on
# [0,b]. The elementary identity 1-e^-t >= t e^-t controls the singular ones.
model=_scalar_model
dp0=sum((res.Dpoly[j]*cc[j] for j in range(12)),arb_poly([]))
tc=res.T*arb_mat([[v] for v in cc])
dpsum=sup(dp0,arb(0),arb(1))
for j,fj in enumerate(res.funcs):
    for term in fj['D']['shift_terms']:
        dpsum+=mag(tc[j,0])*sup(arb_poly(list(map(q,term['polynomial']))),arb(0),arb(1))
ac=mag(model['ac'])
ell=sup(model['ell'],-B,B)
quot=sup(model['quot'],-b,b)
gam=sup(model['gamma'],arb(0),b)
dv=sup(model['dv'],arb(0),arb(1))
HC=100*(1+ac+ell+quot+gam+dv+mag(model['dm'])+dpsum)
assert 1<a<b<B<q('1.2') and 0<hs<1 and arb(3).log()<q('1.1')
assert sum((mag(v)*q('1.1')**k for k,v in enumerate(gamma)),arb(0))<2
# Physical z and Phi on their own full interval; Legendre sup <= 1.
ph=arb(0); phH=arb(0)
for i,n in enumerate(range(3,384,2)):
    top=(arb(2*n+1)/(2*a)).sqrt()
    low1=top*c.mellin(n,a)/c.mellin(1,a)
    ph+=mag(ff[i,0])*(top+mag(low1))
    phH+=mag(ff[i,0])*(top*harm[n]+mag(low1))
z=arb(0);zH=arb(0)
for i,(p,ls) in enumerate(zp):
    z+=mag(pv[i,0])*sum(map(mag,ls),arb(0))
    zH+=mag(pv[i,0])*sum((mag(v)*harm[k] for k,v in enumerate(ls)),arb(0))
oldgamma=list(map(q,inps.json('a8_model')['Gamma_polynomial_coefficients']))
assert sum((mag(v)*a**k for k,v in enumerate(oldgamma)),arb(0))<2
JY=J*w-Y*arb_mat([[pv[i,0]] for i in range(4,12)])
sup_s=c.norm(JY)*96/(2*hs).sqrt()
mom_s=c.norm(JY)*((b.sinh()-a.sinh()-hs)/4).sqrt()
mc=arb_poly([(a/2)**k/factorial(k) if k%2==1 else arb(0) for k in range(161)])
ms=sum(map(mag,mc),arb(0))
mdh=arb(0)
for n in range(1,161,2):
    mdh+=mag((2*n+1)*c.pint(mc*leg[n]))*harm[n]
# Q_l p on its interval is D_H p plus the local logarithmic potential,
# the regular kernel and the active translations. The separated shell-to-core
# Cauchy integral of a bounded local polynomial is <=(3+|log(a-y)|) sup.
assert prime<12 and ms<1 and delta>1
gcap=phH+zH+(25+prime)*(ph+z)+(8+prime)*sup_s+(mom_s/mu)*(mdh+(25+prime)*ms)
hmabs=sum((mag(wt) for _,wt in hpoints),arb(0))
hmC=sum((mag(wt)/(a-y) for y,wt in hpoints),arb(0))
assert all(y<a for y,wt in hpoints)
# int_0^a(1+|log(a-y)|)dy<3 when 1<a<1.1.
assert a<q('1.1')
alpha=(3*gcap+hmabs)/(a*c.mellin(1,a))
lowcap=c.norm(low)*384/(2*a).sqrt()
u_static=gcap/delta+ph+(lowcap+alpha*ms)/delta
out_static=u_static+ms*mag(lm)/mu
core_h=HC*(2+mag(hs.log()))
u_core=u_static+core_h/delta
for sh,_ in channels:
    assert sh<=2*a or (sh-2*a).contains(0)
    assert sh+a>b
# If a shifted point is in the core, a-|x-sh| >= min(x-a,b-x).
# For v=min(x-a,b-x), t=-log(v)>1, the entire absolute Cauchy integral
# int_0^a(1+|log u|)/(v+u)du <= 10(1+t^2). Split at v and 1.
outer_bound=10*out_static+hmC/delta+sup(outerreg,a,b)
ss=sup(sp,arb(-1),arb(1)); dhcap=sup(dh,arb(-1),arb(1))
# Reproduce the shell singular kernel as an integral, so the polynomial
# quotient and logarithm in the Cauchy formula cancel before domination.
shell_bound=dhcap+ss*(10+4*hs+hs/(2*a))
# Complete physical z parity fields, with prime shifts and both boundary logs.
z_bound=zH+(25+prime)*z
prime_bound=3*prime*(u_core+mag(lm)/mu+ss)
assert (b/2).sinh()<1
C=2*HC+shell_bound+outer_bound+z_bound+prime_bound+mag(momentR)/mu
assert C.is_finite()
edges0=[a]
# Recover the genuine outer cell breaks exactly as in the builder.
cuts=list(res.cuts)
for edge in edges:
    for sh,_ in channels: cuts.extend([edge+sh,edge-sh,sh-edge,-edge-sh])
for x in sorted((x for x in cuts if a<x<b),key=float):
    if not x.overlaps(edges0[-1]):edges0.append(x)
edges0.append(b)
def tail(d):
    t=-d.log()
    return 2*C*C*d*(29+28*t+14*t*t+4*t**3+t**4)
widths=[edges0[1]-a,b-edges0[-2]]
cost5=sum((tail(width/32) for width in widths),arb(0))
depth=5
while sum((tail(width/2**depth) for width in widths),arb(0))>q('1e-12'):
    depth+=1
    assert depth<=3000
cost=sum((tail(width/2**depth) for width in widths),arb(0))
assert cost<q('1e-12')
out=dict(endpoint_envelope=c.enc(C)[1],depth=depth,two_extreme_tails_model_X_squared=c.enc(cost)[1],
         bound_on_original_two_edge_panels=c.enc(cost5)[1], left_width=c.enc(widths[0]/2**depth),
         right_width=c.enc(widths[1]/2**depth),compact_join_certified=False,physical_residual_certified=False)
args.output.write_text(json.dumps(out,indent=2),encoding='utf8')
print("ENDPOINTS",float(C.upper()),depth,float(cost.upper()),float(cost5.upper()),flush=True)
