"""Complete force transport on the existing finite response, with D weights."""
from fractions import Fraction as Q
from math import factorial
from flint import arb,arb_mat,arb_poly,arb_series,ctx


def run(root,data,env,module):
    ctx.prec=3072
    rv=module('bound_force_rest_matrices',data['rest_verify'],root/'bound_rest_verify.py')
    rd=rv.snapshot(root,data['rest_bindings'])
    Er,Dr,Xr,_=rv.matrices(rd)
    c=env['common'];q,quad,tr=c.q,lambda A,v:(v.transpose()*A*v)[0,0],c.trace
    e=env['energy'];case=env['inp'].json('common')['cases'][0]
    X=rv.mat(Xr);E=rv.mat(Er);K=rv.mat([row[191:]for row in Dr[191:]])
    Ki=K.inv();rho=q(case['rho'])
    Xlo=arb_mat([[X[i,j]for j in range(191)]for i in range(84)])
    Xfi=arb_mat([[X[i,j+191]for j in range(12)]for i in range(84)])
    PD=Xlo*Xlo.transpose()/(1-rho)+Xfi*Ki*Xfi.transpose()
    trDE=sum((E[i,i]/(1-rho)for i in range(191)),arb(0))
    trDE+=tr(Ki*arb_mat([[E[i+191,j+191]for j in range(12)]for i in range(12)]))
    a=3*arb(2).log()/2;b=arb(3).log();hs=b-a;mid=(a+b)/2;mu=(a+a.sinh())/2
    J=c.ratmat(env['inp'].json('frozen_J_even')['working_basis_midpoints_rational'])
    R=J*PD*J.transpose();normJ=tr(R).sqrt()
    lv=arb_mat([[(hs*(2*n+1)/2).sqrt()*c.mellin(n,hs/2)*((mid/2).cosh()if n%2==0 else(mid/2).sinh())]for n in range(96)])
    lam=quad(PD,J.transpose()*lv).sqrt()
    H=[arb(0)];H2=[arb(0)]
    for n in range(1,193):H.append(H[-1]+arb(1)/n);H2.append(H2[-1]+arb(1)/n**2)
    dh2=sum((R[n,n]*H[n]**2 for n in range(96)),arb(0))
    polys=[p(arb_poly([-1,2]))*(arb(2*n+1)/(2*hs)).sqrt()for n,p in enumerate(c.legs(96))]
    A=arb_mat([[polys[i][k]for k in range(96)]for i in range(96)])
    coef=A.transpose()*R*A
    density=arb_poly([sum((coef[i,k-i]for i in range(max(0,k-95),min(95,k)+1)),arb(0))for k in range(191)])
    v0=-(2*arb.pi()).log()-arb.const_euler()-hs.log();mult2=arb(0)
    for n,p in enumerate(density):
        N=arb(n+1);h=H[n+1];h2=H2[n+1]
        l0=-1/N**2;l1=-h/N;l00=2/N**3;l11=(h*h+h2)/N
        l01=h/N**2-(arb.pi()**2/6-h2)/N
        mult2+=2*hs*p*(v0*v0/N-v0*(l0+l1)+(l00+2*l01+l11)/4)
    assert dh2>=0 and mult2>0 and trDE>0
    prime=2*sum((arb(p).log()/arb(n).sqrt()for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2))),arb(0))
    # Same reciprocal series as the bound Gamma polynomial; the inherited
    # uniform error completes the finite sum on |z|<=11/10.
    ctx.cap=226
    co=arb_series([arb(1)/factorial(k)if k%2==0 else arb(0)for k in range(226)],prec=226)
    sh=arb_series([arb(1)/factorial(k+1)if k%2==0 else arb(0)for k in range(226)],prec=226)
    pc=1/co;ps=1/sh
    regular_abs=sum((abs((pc[k]+ps[k+1])/4).upper()*q('11/10')**k for k in range(225)),arb(0))
    regular_abs+=e.bounds['old_FJ_regular_kernel_uniform_error']
    assert b<q('11/10') and regular_abs<2
    reg=q('2')
    cross=arb.pi()/2+(hs/a).sqrt()/2+2*reg*(a*hs).sqrt()+prime
    # Whole Q8 m: D_H difference quotient, logarithmic potential, bounded
    # regular kernel and all prime shifts. m is even cosh(x/2).
    mmax=(a/2).cosh();mn=(2*a).sqrt()*mmax
    cv=abs(-(2*arb.pi()).log()-arb.const_euler()-a.log()).upper()
    qm=(2*a).sqrt()*a*(a/2).sinh()/2+mn*(cv+arb(2).sqrt()/2+arb(2).log()/2+2*a*reg+prime)
    assert qm<100
    # A coarse whole Q bound for any degree <=95 local polynomial, used
    # solely for the already tiny frozen-J coordinate discrepancy.
    lambda_op=((hs+b.sinh()-a.sinh())/4).sqrt()
    core_op=cross+100*lambda_op/mu
    shell_op=H[95]+96*(abs(v0).upper()+arb(2).sqrt())+hs/(2*a)+2*reg*hs+prime+cross*(2*mu).sqrt()*lambda_op/mu
    q_op=(core_op**2+shell_op**2).sqrt()
    assert q_op<10000
    roundJ=c.box(e.data['old_J_coordinate_rounding_norm'])
    rounding=10000*roundJ*tr(PD).sqrt()
    core=cross*normJ+100*lam/mu
    shell=dh2.sqrt()+mult2.sqrt()+(hs/(2*a)+2*reg*hs+prime)*normJ+cross*(2*mu).sqrt()*lam/mu
    QJ=(core**2+shell**2).sqrt()+rounding
    UJ=arb_mat([[env['U'][i,j]for j in range(12,96)]for i in range(12,96)])
    hightrace=tr(PD*UJ)+e.w['du']*tr(PD*e.w['GJ'])
    assert hightrace>0
    hrel=q('16198/18219');eta=q('1e-10')
    sforce=(1-eta)*q('5/21').sqrt()*QJ+(hrel*hightrace).sqrt()
    cap=q('1977/500000');beta=q('20209999981781/182190000000000')
    force=sforce+(cap*beta*trDE).sqrt()
    assert force<10
    values=dict(trace_Dinv_E=trDE,regular_kernel_abs_upper=regular_abs,
                cross_operator_upper=cross,Q8_m_upper=qm,local_degree95_Q_upper=q_op,
                frozen_J_rounding=rounding,QJ_response_HS_upper=QJ,
                high_response_trace_upper=hightrace,S_response_Ldual_HS_upper=sforce,
                full_force_operator_upper=force)
    return dict(outcome='WHOLE_FORCE_TRANSPORT_BOUND',
                definition='||R_L^(1/2) A_force* D_new^-1/2|| <= force_cap',
                force_cap='10',values=c.encode(values),
                whole_residual_error_inventory_complete=False,
                does_not_bound_actual_residual_energy=True)
