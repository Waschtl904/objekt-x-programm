# Full one-sided finite parts and exact carrier integrals, without sampling.
def trace_endpoint(fun,shifts):
 al=fun.get('one',arb_poly([]))(arb(1))
 fin=fun.get(None,arb_poly([]))(arb(1))+al*(h/a).log()+shifts[-1](arb(1))
 for tag,poly in fun.items():
  if tag is not None and tag!='one':fin+=poly(arb(1))*abs(1-roots[tag]).log()
 return al,fin

def carrier(fun,shifts):
 mm=function_moments(fun,mom,'zero','one',p)
 for ci,(lo,hi) in enumerate(cells):
  add=mom.polynomial_moments(shifts[ci],lo,hi,p)
  mm=[v+w for v,w in zip(mm,add)]
 return pair(pol[p],mm)*arb(2*p+1).sqrt()

endpointJY=[trace_endpoint(fun,sh) for fun,sh in zip(globalF,cellF)]
carrierJY=[carrier(fun,sh) for fun,sh in zip(globalF,cellF)]
say('92 full endpoint finite parts and carrier integrals completed')

# The four physical z functions are smooth across a. Their exact logarithms
# at +/-b are retained here, rather than Taylor-expanded.
endpointZ=[];carrierZ=[]
for n in range(p+2,p+10,2):
 cnz=arb(2*n+1).sqrt()/arb(2*p+1).sqrt()*mellin(n,b)/mellin(p,b)
 ls=[arb(0)]*(n+1);ls[n]=((2*n+1)/(2*b)).sqrt();ls[p]=-cnz*((2*p+1)/(2*b)).sqrt()
 f=sum((pol[k]*ls[k] for k in range(n+1)),arb_poly([]))
 dh=sum((pol[k]*(ls[k]*sum((arb(1)/v for v in range(1,k+1)),arb(0))) for k in range(n+1)),arb_poly([]))
 smooth=dh+f*(-(2*arb.pi()*b).log()-arb.const_euler())-kernel(f,ls,b,gamma,p)
 f=f(arb_poly([0,1/r]));smooth=smooth(arb_poly([0,1/r]))
 action=multiply_fun({None:smooth+f*r.log(),'outer':f*(-arb(1)/2),'minus_outer':f*(-arb(1)/2)},(2*a).sqrt())
 sh=[]
 for lo,hi in cells:
  mid=(roots[lo]+roots[hi])/2;z=arb_poly([])
  for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:
   shift=arb(q).log()/a;weight=arb(prime).log()/arb(q).sqrt()
   for sign in [-1,1]:
    if abs(mid+sign*shift)<r:z-=f(arb_poly([sign*shift,1]))*weight
  sh.append(z*(2*a).sqrt())
 endpointZ.append(trace_endpoint(action,sh));carrierZ.append(carrier(action,sh))
say('four physical z endpoint finite parts and carrier integrals completed')

# Q_a ell_p: one complete source gives every carrier of Q_a Phi_i by
# symmetry. This uses precisely the old degree-160 Gamma model of A.
fp=pol[p]*arb(2*p+1).sqrt();ls=[arb(0)]*(p+1);ls[p]=arb(2*p+1).sqrt()
hp=sum((arb(1)/k for k in range(1,p+1)),arb(0))
q0={None:fp*(hp-(2*arb.pi()*a).log()-arb.const_euler())-kernel(fp,ls,a,gammaOld,p), 'one':fp*(-arb(1)/2),'minus_one':fp*(-arb(1)/2)}
q0sh=[]
for lo,hi in cells:
 mid=(roots[lo]+roots[hi])/2;v=arb_poly([])
 for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:
  shift=arb(q).log()/a;weight=arb(prime).log()/arb(q).sqrt()
  for sign in [-1,1]:
   if abs(mid+sign*shift)<1:v-=fp(arb_poly([sign*shift,1]))*weight
 q0sh.append(v)
mm=function_moments(q0,mom,'zero','one',383)
for ci,(lo,hi) in enumerate(cells):
 add=mom.polynomial_moments(q0sh[ci],lo,hi,383)
 mm=[v+w for v,w in zip(mm,add)]
carrierPhi=[pair(f,mm) for f in phi]

# The finite part at t=1 is evaluated from endpoint moments, avoiding a
# degree-543 monomial action for each of the 191 old basis functions.
endpointPhi=[];shiftvals={q:[f(1-arb(q).log()/a) for f in phi] for q in [2,3,4,5,7]}
for j,n in enumerate(range(p+2,384,2)):
 ls={n:arb(2*n+1).sqrt(),p:-cn[j]*arb(2*p+1).sqrt()}
 fv=sum(ls.values(),arb(0));dh=sum((v*sum((arb(1)/i for i in range(1,k+1)),arb(0)) for k,v in ls.items()),arb(0))
 kv=arb(0)
 for k,ck in enumerate(gammaOld):
  if not ck:continue
  mk=sum((v*af(F((-1)**l*2**(k+1)*factorial(k)**2,factorial(k-l)*factorial(k+l+1))) for l,v in ls.items() if l<=k),arb(0))
  kv+=a*af(ck)*(a/2)**k*mk
 fin=dh+fv*(-(2*arb.pi()*a).log()-arb.const_euler())-kv-fv*(2*h/a).log()/2
 for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:fin-=shiftvals[q][j]*arb(prime).log()/arb(q).sqrt()
 endpointPhi.append([-fv/2,fin])

# Direct independent finite-part check on several old basis functions.
checks=[]
for j in [0,17,90,190]:
 n=p+2+2*j;ls=[arb(0)]*(n+1);ls[n]=arb(2*n+1).sqrt();ls[p]=-cn[j]*arb(2*p+1).sqrt()
 dh=pol[n]*(ls[n]*sum((arb(1)/i for i in range(1,n+1)),arb(0)))+pol[p]*(ls[p]*hp)
 smooth=dh+phi[j]*(-(2*arb.pi()*a).log()-arb.const_euler())-kernel(phi[j],ls,a,gammaOld,p)
 fin=smooth(arb(1))-phi[j](arb(1))*(2*h/a).log()/2
 for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7)]:fin-=shiftvals[q][j]*arb(prime).log()/arb(q).sqrt()
 diff=fin-endpointPhi[j][1];assert diff.contains(0) and abs(diff)<af('1e-60')
 checks.append({'column':j,'difference':diff})
say('191 old action traces and carriers completed, with four independent action checks')
result={'parity':args.parity,'bits':args.bits,'normalization':'normalized core t=x/a, multiply physical values by sqrt(2a); finite parts use log(s/h)',
 'source_JY_endpoint_log_and_finite':endpointJY,'source_JY_carrier':carrierJY,
 'source_Z_endpoint_log_and_finite':endpointZ,'source_Z_carrier':carrierZ,
 'old_Qphi_endpoint_log_and_finite':endpointPhi,'old_Qphi_carrier':carrierPhi,
 'old_moment_coefficients_cn':cn,'old_endpoint_raw_low_weights':[arb(2*n+1).sqrt() for n in range(p+2,384,2)],
 'old_endpoint_carrier_weight':arb(2*p+1).sqrt()+sum((arb(2*n+1).sqrt()*cn[j] for j,n in enumerate(range(p+2,384,2))),arb(0)),
 'independent_action_checks':checks,'gamma224_error':epsGamma,'J_rounding':rounding,'Y_rounding':Yrounding,
 'bindings':bindings,'seconds':time.monotonic()-start,'full_remainder_certified':False}
args.out.write_text(json.dumps(serial(result,80),indent=2)+'\n',encoding='utf-8')
say('DONE complete endpoint models; operator error and final residual composition are separate')
