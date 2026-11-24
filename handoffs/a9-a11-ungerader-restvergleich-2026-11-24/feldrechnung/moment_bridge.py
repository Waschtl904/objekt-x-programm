"""Odd continuous model: moment carrier, final high lift and outer regular kernel."""
from pathlib import Path
import sys, json

# Reuse the signed, pinned field, before integrating any outer panel.
# root, cache, output, 5, source_bridge.json, transport.json
src_report, transport_report = map(Path,sys.argv[5:7])
assert len(sys.argv)==7
del sys.argv[5:]
shared=Path(__file__).with_name('panels.py')
exec(compile(shared.read_text(encoding='utf8').split('cuts=list(res.cuts)')[0], str(shared), 'exec'))
source=json.loads(src_report.read_bytes())
transport=json.loads(transport_report.read_bytes())
from weights import gamma_error
from directed_output import upper_decimal
reg=gamma_error(224,q('1.1'))
cross=q(transport['raw_cross'])
qm=q(transport['core_Qm'])
lam=((b.sinh()-a.sinh()-hs)/4).sqrt()
mn=(2*mu).sqrt()
lift=q(source['lift'])
crossK=cross+2*b*reg
qmK=qm+2*b*reg*mn
# The true response has a bounded model h on the entire smaller core.
# Each analytic expression is continued only from its own fixed prime cell.
ctx.cap=4;tm.Jet.N=4
hmax=arb(0)
for l,r in zip(edges[:-1],edges[1:]):
    xx=tm.Jet(arb_series([(l+r)/2,(r-l)/2],prec=4), acb(l.union(r),arb(0)))
    hmax=max(hmax,abs(tm.hjet(globals(),xx).b).upper())
hmodel=(2*a).sqrt()*hmax
efirst=arb(6*a).sqrt()*c.mellin(1,a)
assert efirst>0 and arb(1)<a<b<q('1.1')
eps=2/arb.fac_ui(160)
assert (a/2).exp()*(a/2)**159/arb.fac_ui(159)<eps
dm=(2*a).sqrt()*eps
# Supremum and physical derivative of sinh(x/2)-m160 are <=eps.
# In the whole core the Legendre difference operator on a Lipschitz
# function is bounded pointwise by a*Lip. The log potential is in L2.
prime=2*sum((wt for _,wt in channels),arb(0))
const=max(abs((2*arb.pi()*a).log()+arb.const_euler()).upper(),
          abs((2*arb.pi()*b).log()+arb.const_euler()).upper())
regK=q('0.5')+reg
assert const<4 and prime<12 and regK<1
Qdm=(2*a).sqrt()*(a+const+2+2*a*regK+prime)*eps
# On either entire old interval polynomial degree <=383 implies
# ||p||_infty<=384/sqrt(2*length)*||p||. The normalized L2 norm of
# -log(1-x^2)/2 is <=1 on (-1,1) with probability measure dx/2.
assert harm[383]+const+384+2*b*regK+prime<500
polycap=arb(500)
mg=mn+dm
# Keep the full finite H8 source for Phi, including its first odd grade.
phnorm=sum((abs(ff[i,0]).upper()*(1+(c.mellin(n,a)/c.mellin(1,a))**2*(2*n+1)/3).sqrt()
            for i,n in enumerate(range(3,384,2))),arb(0))
znorm=sum((abs(pv[i,0]).upper()*(sum((v*v*(2*b)/(2*j+1) for j,v in enumerate(ls)),arb(0))).sqrt()
            for i,(_,ls) in enumerate(zp)),arb(0))
shellnorm=c.norm(J*w)+c.norm(Y*arb_mat([[pv[i,0]] for i in range(4,12)]))
lamcoef=lam*shellnorm/mu
gmodel=polycap*(phnorm+znorm)+crossK*shellnorm+lamcoef*(qmK+Qdm)
gmoment=lamcoef*Qdm
alpha_bound=(gmodel+hmodel)/efirst
dn=(gmoment*(1+mn/efirst)+alpha_bound*dm)/delta
u0=phnorm+(gmodel+hmodel+c.norm(low)+alpha_bound*mg)/delta
moment_change=crossK*(dn+lamcoef*dm)+lam/mu*(dm*gmodel+mn*gmoment+dn*qmK+u0*Qdm)
moment_change+=prime*lamcoef*dm
# For the exact high vector (Legendre degrees >=385), pairing with m
# equals pairing with m-m160. The other factor of the oblique correction
# is a unit vector. Coordinate leakage is already priced before this step.
rawsource=q(source['raw_source'])
gnorm=gmodel+hmodel+gmoment+rawsource
gamma=q(inps.json('high_response')['odd']['full_M_norm_squared'][1])
high_lift=dm*gamma.sqrt()*gnorm/efirst
raw_g=q(source["cross_lift_X"])
high_lift_X=raw_g*high_lift/delta
# Two uses of the outer Gamma kernel in the adjoint coupling: action on the
# shell and contraction with the core moment. The full lifted test has
# norm <=lift times the shell norm. Include the direct negative core lift.
u_cap=u0+dn+lamcoef*mn
outer_gamma=lift*2*b*reg*u_cap
more=(q('5/21')).sqrt()*(moment_change+high_lift_X+outer_gamma)
all_subtotal=more+q(source['shell_partial_dual'])+q(source['w_round_dual'])
out=dict(model_h_core=hmodel,first_pairing=efirst,delta_m=dm,Q_delta_m=Qdm,g_model=gmodel,
         alpha_bound=alpha_bound,u0_norm=u0,moment_change_X=moment_change,high_lift_X=high_lift_X,
         outer_gamma_X=outer_gamma,more_dual=more,combined_dual=all_subtotal)
result={k:upper_decimal(v) for k,v in out.items()}
result['scope']='CONTINUOUS_MODEL_TO_PHYSICAL_FUNCTIONAL_UNDER_INHERITED_CONTRACTS'
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print({k:float(v.upper()) for k,v in out.items()},flush=True)
