"""Exact scalar endpoint audit and coupled-model countercontrols, no Arb."""
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def need(ok,message):
    if not ok: raise ValueError(message)
def js(path): return json.loads(path.read_bytes())
def root_bound(x,digits=90):
    x=F(x);need(x>=0,'negative radicand')
    scale=10**digits;k=isqrt(x.numerator*scale*scale//x.denominator)
    lo=F(k,scale);hi=lo if lo*lo==x else F(k+1,scale)
    need(lo*lo<=x<=hi*hi,'root enclosure')
    return lo,hi

def endpoint_audit():
    spec=js(HERE/'INPUT_BINDINGS.json');data={}
    for alias in ('schur_result','rest_result'):
        e=spec['files'][alias];raw=(ROOT/e['path']).read_bytes()
        need(hashlib.sha256(raw).hexdigest()==e['sha256'],'input hash')
        data[alias]=json.loads(raw)
    a=data['schur_result'];b=data['rest_result'];r=js(HERE/'RESULT.json');f=js(HERE/'FINITE.json')
    g=a['form_refinement']['directional_Grams'];up=lambda x:F(x[1])
    direct=up(a['form_refinement']['direct_relative_error'])*up(g['GJ_w'])
    rad=up(g['model_J'])*up(g['error_J']);lo,hi=root_bound(rad)
    u=F(r['directional_U_price_upper']);candidate=(u-up(g['error_J']))/2
    need(candidate>=0 and candidate*candidate>=rad,'feature upper root')
    need(2*lo+up(g['error_J'])<=u<=2*hi+up(g['error_J'])+F(2,10**80),'outward grid')
    new=direct+u;old=up(a['form_common_D_U_error'])
    need(F(r['new_directional_B_price_upper'])==new<old,'new B price')
    expected=[F(b['F_interval'][0])+old-new,F(b['F_interval'][1])-old+new]
    need(list(map(F,r['F_interval']))==expected,'F endpoints')
    m=F(b['budget_interval'][0])-expected[1]
    need(m==F(r['budget_lower_minus_F_upper'])>0,'F margin')
    y=sum((F(v[1]) for v in f['terms'].values()),F(0))
    need(y==F(f['finite_P_residual_norm_upper'])==F(r['finite_P_residual_norm_upper']),'finite sum')
    need(y*y==F(f['finite_P_residual_energy_upper'])==F(r['finite_P_residual_energy_upper']),'finite square')
    c=F(r['c']);beta=F(r['beta']);target=F(r['proposed_full_Ldual_energy_target'])
    need(target==F(19,10**9),'fixed future target')
    x2=target/beta;price=F(r['conditional_remainder_price_upper'])
    cross=(price*(1-c)-x2-y*y)/2
    need(cross>=0 and cross*cross>=c*x2*y*y,'whole residual bound')
    need(price<m and F(r['conditional_margin'])==m-price,'conditional margin')
    need(F(r['conditional_total_energy_upper'])==expected[1]+price,'conditional total')
    need(F(r['zero_leakage_threshold_gain_over_old_floor'])==307061,'floor comparison')
    for key in ('full_residual_computed','full_inverse_upper_certified','partial_pass','milestone_4_closed','N12_closed'):
        need(r[key] is False,'scope overclaim: '+key)
    return {'F_endpoint_check':True,'finite_norm_sum_check':True,
            'conditional_target_check':True,'scope_check':True}

def coupled_model():
    # S=L=diag(2,3), A=(1,1), D=5, J=e1, Z=(2/5,0).
    # All arithmetic is exact. The residual is nonzero and H is coupled.
    D=F(5);z=F(2,5);cap=F(2,25)
    M=2*z-2*z*z;E=D-M
    R=[1-2*z,F(1)];rnorm=R[0]**2/2+R[1]**2/3
    need(rnorm<=cap*E,'full model residual premise')
    H=[[F(2)-1/D,-1/D],[-1/D,F(3)-1/D]]
    det=H[0][0]*H[1][1]-H[0][1]*H[1][0]
    Hi=[[H[1][1]/det,-H[0][1]/det],[-H[1][0]/det,H[0][0]/det]]
    count=0
    for i in range(-4,5):
        for j in range(-4,5):
            r=[F(i,3),F(j,5)]
            actual=sum(r[a]*Hi[a][b]*r[b] for a in range(2) for b in range(2))
            x2=r[0]**2/2+r[1]**2/3;y2=(z*r[0])**2/E
            gap=actual*(1-cap)-x2-y2
            need(gap<=0 or gap*gap<=4*cap*x2*y2,'general residual lemma')
            count+=1
    # A zero finite projection does not imply a zero full residual.
    need(Hi[1][1]>0 and Hi[1][1]<=F(1,3)/(1-cap),'infinite-part countercontrol')
    # Exact variational residual identity for an unrelated fixed t.
    f=[F(2,7),F(-3,5)];t=[F(4,9),F(1,6)]
    r=[f[i]-sum(H[i][j]*t[j] for j in range(2)) for i in range(2)]
    energy=lambda v:sum(v[i]*Hi[i][j]*v[j]for i in range(2)for j in range(2))
    var=2*sum(f[i]*t[i]for i in range(2))-sum(t[i]*H[i][j]*t[j]for i in range(2)for j in range(2))
    need(energy(f)==var+energy(r),'variational identity')
    return {'exact_coupled_model_cases':count,'zero_finite_projection_not_zero_residual':True,
            'variational_residual_identity':True}

if __name__=='__main__':
    need(__debug__,'python -O is not allowed')
    print(json.dumps({**endpoint_audit(),**coupled_model()},indent=2))
