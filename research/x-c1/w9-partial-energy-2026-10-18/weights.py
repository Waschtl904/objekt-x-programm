"""Useful norm control for the FOUR computed features (RL is excluded)."""
import json
from math import factorial
from flint import arb, arb_poly, arb_series, arb_mat, ctx
from common import Inputs, q, mat, ratmat, box, trace, norm, need, encode, HERE


def sub(a,rows,cols):
    return arb_mat([[a[i,j] for j in cols] for i in rows])


def gamma_error(n,r):
    """Uniform real regular-kernel error, from reciprocal-series residuals.

    k_reg(2z)=1/4[sech(z)+(1/sinh(z)-1/z)]. For real |z|<=r,
    cosh(z)>=1 and sinh(z)/z>=1. Residual coefficient bounds therefore
    control both reciprocal errors, including the complete entire tails.
    """
    D=max(256,n+20);D+=D%2;ctx.cap=n+2
    c=[arb(1)/factorial(k) if k%2==0 else arb(0) for k in range(D+1)]
    s=[arb(1)/factorial(k+1) if k%2==0 else arb(0) for k in range(D+1)]
    pc=arb_poly(list(1/arb_series(c[:n+1],prec=n+1)))
    ps=arb_poly(list(1/arb_series(s[:n+2],prec=n+2)))
    rc=pc*arb_poly(c)-1;rs=ps*arb_poly(s)-1
    for k in range(n+1):need(rc[k].contains(0),'cosh inverse identity')
    for k in range(n+2):need(rs[k].contains(0),'sinhc inverse identity')
    fc=sum((abs(rc[k]).upper()*r**k for k in range(n+1,len(rc))),arb(0))
    fs=sum((abs(rs[k]).upper()*r**(k-1) for k in range(n+2,len(rs))),arb(0))
    tc=r**(D+2)/factorial(D+2)/(1-r*r/((D+3)*(D+4)))
    ts=r**(D+1)/factorial(D+3)/(1-r*r/((D+4)*(D+5)))
    nc=sum((abs(v).upper()*r**k for k,v in enumerate(pc)),arb(0))
    ns=sum((abs(v).upper()*r**k for k,v in enumerate(ps)),arb(0))
    return (fc+fs+nc*tc+ns*ts)/4


def build(inp,parity):
    p=int(parity=='odd');c=inp.json('common')['cases'][p];raw=inp.json('old_sources')['cases'][p]
    inverse=inp.json('inverse_'+parity);co=inp.json('coherent')['parities'][parity]
    Ki=ratmat(co['K_inverse_rational']);K=ratmat(co['K_rational']);P=ratmat(inverse['P_upper_rational'])
    need(norm(K*Ki-arb_mat([[int(i==j)for j in range(12)]for i in range(12)]))<q('1e-150'),'K inverse')
    G=ratmat(c['G96_rational']);Gi=G.inv();GF=sub(G,range(12),range(12));GJ=sub(G,range(12,96),range(12,96))
    need(all(G[i,j].is_zero() for i in range(12) for j in range(12,96)),'Common metric block geometry')
    U=mat(c['U96_model']);UF=sub(U,range(12),range(12))
    delta=q(c['delta']);rho=q(c['rho'])
    ef=mat(c['finite_feature_error_gram'])+mat(raw['old_certificate']['joint_high_source_error_gram'])/delta
    ej=box(c['tail_feature_error_scalar'])+box(raw['galerkin']['high_source_error_norm'])**2/delta
    # Even if the inherited feature price already contains the high error,
    # adding it again is conservative. The factor two covers cross errors.
    E=arb_mat([[2*ef[i,j] if i<12 and j<12 else 2*ej if i==j and i>=12 else 0 for j in range(96)]for i in range(96)])
    te=trace(Gi*E);tu=trace(Gi*U)
    need(te>0 and tu>0,'Common feature traces')
    du=2*(te*tu).sqrt()+te
    DL=mat(c['D96_lower_model']);DU=mat(c['D96_upper_model'])
    dd=trace(Gi*(DU-DL))/2
    need(dd>=0,'Direct-model sandwich width')
    da=du+dd
    a=mat(c['finite_cross_C84_new_model'])
    D0=(DU+DL)/2
    a0=sub(D0-U,range(12),range(12,96))
    need(all(a[i,j].overlaps(a0[i,j]) for i in range(12) for j in range(84)),'a_fin model identification')
    a=a.union(a0) if hasattr(a,'union') else arb_mat([[a[i,j].union(a0[i,j])for j in range(84)]for i in range(12)])
    k=Ki*a
    s=arb_mat([[-k[i,j] if i<12 else int(i-12==j) for j in range(84)]for i in range(96)])
    high=inp.json('high_response')[parity]
    gamma=q(high['full_M_norm_squared'][1]);trXHB=q(high['tr_X_HB_exact_rational'])
    C=arb_mat([[arb(int(v))/int(c['inverse_congruence_denominator'])for v in row]for row in c['inverse_congruence_integer_matrix']])
    trXi=trace(C.transpose()*C)/(1-rho)
    u=gamma*(1/delta+2*trXi+2*trXHB/delta**2)
    UFupper=UF+GF*du
    trP=trace(P);trPGJ=trace(P*GJ)
    dkP=da*(trace(Ki*GF*Ki)*trPGJ).sqrt()
    kP=trace(P*k.transpose()*k).sqrt()+dkP
    us0=trace(P*s.transpose()*U*s)+du*trace(P*s.transpose()*G*s)
    need(us0>0,'Joint source U8 norm')
    us=(us0.sqrt()+trace(UFupper).sqrt()*dkP)**2
    vstar=16*trace(Ki).sqrt()+(u*trace(Ki*UFupper)).sqrt()
    jstar=(q('1.000502')*trP).sqrt()+16*kP+(u*us).sqrt()
    w=u+vstar**2+q('11/10')*jstar**2
    response=inp.json('response')['parities'][parity]['fixed_X']
    dd12=q(inp.json('functions')['parities'][parity]['whole_D12_operator_error_upper'])
    eh=q(response['whole_Hilbert_residual_model_error_upper'])
    result={'parity':parity,'status':'AUTHOR_DERIVED_CONDITIONAL_PARTIAL_WEIGHT_BOUND_EXTERNAL_REVIEW_OPEN',
        'included_features':['high_U8','finite_U8','K_inverse_v','P_upper_J_star_nu'],
        'RL_included':False,'U8_norm_upper':u,'common_U_energy_relative_error_upper':du,
        'direct_energy_relative_error_upper':dd,'a_fin_relative_error_upper':da,
        'weighted_k_model_HS_squared':trace(P*k.transpose()*k),'weighted_k_error_HS_upper':dkP,
        'weighted_joint_U8_source_squared_upper':us,'v_feature_operator_norm_upper':vstar,
        'P_feature_operator_norm_without_11_over_10_upper':jstar,
        'partial_W9_norm_upper':w,'D12_partial_weighted_Gram_scalar_upper':w*dd12**2,
        'whole_residual_partial_error_energy_upper':w*eh**2,
        'new_regular_kernel_uniform_error':gamma_error(360,q('6/5')),
        'old_QPhi_regular_kernel_uniform_error':gamma_error(160,q('21/20')),
        'old_FJ_regular_kernel_uniform_error':gamma_error(224,q('11/10')),
        'global_full_W9_norm_claimed':False}
    return result,{'C':C,'Ki':Ki,'K':K,'P':P,'G':G,'GF':GF,'GJ':GJ,'a':a,'du':du,'da':da,'gamma':gamma,'delta':delta,'rho':rho,'w':w}


if __name__=='__main__':
    ctx.prec=800;inp=Inputs();out={}
    for par in ('even','odd'):
        result,_=build(inp,par);out[par]=result
        print(par,'partial norm',result['partial_W9_norm_upper'],'D-residual energy',result['whole_residual_partial_error_energy_upper'],flush=True)
    (HERE/'WEIGHT_BOUNDS.json').write_text(json.dumps(encode(out),indent=2)+'\n')
