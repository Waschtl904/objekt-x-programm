"""Independent Fraction evaluation of the upper-form rays, plus two extensions.

No floating point, external numerical library, or eigenvalue search is used.
The analytic operator enclosures are inherited from the bound input package.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def mv(a,x):return [dot(row,x) for row in a]
def mat(a):return [[F(v) for v in row] for row in a]
def transpose(a):return [list(row) for row in zip(*a)]
def quad(a,x):return dot(x,mv(a,x))
def inverse(a):
    n=len(a);m=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        d=m[j][j];assert d
        m[j]=[v/d for v in m[j]]
        for i in range(n):
            if i!=j:
                k=m[i][j];m[i]=[v-k*u for v,u in zip(m[i],m[j])]
    ans=[row[n:] for row in m]
    assert [[dot(row,col) for col in zip(*ans)] for row in a]==[[F(i==j) for j in range(n)] for i in range(n)]
    return ans
def sup(x,digits=55):
    assert x>=0;den=10**digits;n=isqrt(x.numerator*den*den//x.denominator)
    if F(n*n,den*den)<x:n+=1
    return F(n,den)
def isum(vals):
    vals=list(vals);return sum((v[0] for v in vals),F(0)),sum((v[1] for v in vals),F(0))
def times(v,q):
    q=F(q);return (v[0]*q,v[1]*q) if q>=0 else (v[1]*q,v[0]*q)
def prod(a,b):
    vals=[x*y for x in a for y in b];return min(vals),max(vals)
def divide(a,b):
    assert b[0]>0;return prod(a,(1/b[1],1/b[0]))
def boxes(a):return [[tuple(map(F,v)) for v in row] for row in a]
def iq(a,x):return isum(times(v,x[i]*x[j]) for i,row in enumerate(a) for j,v in enumerate(row))
def ilin(a,co):return isum(times(v,co[i][j]) for i,row in enumerate(a) for j,v in enumerate(row))
def display_up(q):
    d=10**12;return str(F(-((-q.numerator*d)//q.denominator),d))
def dump(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,(list,tuple)):return [dump(v) for v in x]
    if isinstance(x,dict):return {k:dump(v) for k,v in x.items()}
    return x

def log_box(q,n=60):
    """atanh series, with its complete geometric tail."""
    q=F(q);assert q>0
    if q<1:
        lo,hi=log_box(1/q,n);return -hi,-lo
    z=(q-1)/(q+1)
    total=2*sum((z**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    tail=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return total,total+tail
def atan_box(q,n=12):
    assert n%2==0 and 0<q<1
    lo=sum(((-1)**k*q**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    return lo,lo+q**(2*n+1)/F(2*n+1)
def floor_grid(q):
    d=10**15;return F(q.numerator*d//q.denominator,d)
def constant_bound():
    # Machin identity, with a rational check of tan(4 atan(1/5)-atan(1/239))=1.
    re,im=F(1),F(0)
    for _ in range(4):re,im=re-im/5,im+re/5
    re,im=re+im/239,im-re/239
    assert re==im and re>0
    a=atan_box(F(1,5));b=atan_box(F(1,239))
    pi_lo=floor_grid(16*a[0]-4*b[1])
    l2=log_box(2);l3=log_box(3)
    h_lo=floor_grid(l3[0]-F(3,2)*l2[1]);assert 0<h_lo<F(1,16)
    # Convexity of 1/x and the trapezoidal bound give
    # EulerGamma >= H_n-log(n)-1/(2n). 1000=(5/4)^3*2^9.
    n=1000;hn=sum((F(1,k) for k in range(1,n+1)),F(0))
    ln_n_hi=3*log_box(F(5,4))[1]+9*l2[1]
    gamma_lo=hn-ln_n_hi-F(1,2*n)
    alpha_hi=2*l2[1]-log_box(4*pi_lo*h_lo)[0]-gamma_lo-F(11,10)
    cap=F(10113,10**6)
    assert alpha_hi<cap
    return {'constant':'-log(pi*(log(3)-3*log(2)/2))-EulerGamma-11/10',
            'pi_lower':pi_lo,'h_lower':h_lo,'EulerGamma_lower':gamma_lo,
            'alpha_upper_derived':alpha_hi,'alpha_upper_used':cap,
            'method':'Rational atanh/arctangent tails and trapezoidal EulerGamma lower bound'}

def control(root):
    read=lambda n:json.loads((root/n).read_bytes())
    data=read('AUDIT_INPUT.json');obs=read('OPTIMISTIC_OBSTRUCTION.json')['cases']
    original=read('AUDIT.json')['cases'];constant=constant_bound();rows=[]
    eta=F(1,10**10);alpha=constant['alpha_upper_used']
    for p,label in enumerate(['EVEN','ODD']):
        c=data['cases'][p];o=obs[p];new=read(f'DIRECT_Y_{label}_3072.json')
        g=c['galerkin'];pot=c['potential'];cert=c['certificate'];rv=c['review'];br=c['bridge']
        K=mat(br['K12_lower']);Ki=inverse(K);P=mat(br['P'])
        U0=boxes(cert['model_upper_energy']);Err=boxes(cert['energy_model_error_gram'])
        tau=ilin(U0,transpose(Ki))[1];ef2=ilin(Err,transpose(Ki))[1]
        assert tau>0 and 0<ef2<F(3,10**25)
        gamma=2*sup(tau*ef2)+ef2
        u=[F(v[0]) for v in o['u_rational']];t=[F(v[0]) for v in o['t_rational']];w=[F(v[0]) for v in o['w_rational']]
        assert (len(u),len(t),len(w))==(191,12,84)
        Dw=mv(mat(c['D']),w);assert mv(transpose(mat(c['S'])),Dw+w)==[0]*8
        wn=dot(w,w);WX=wn+dot(Dw,Dw);tk=quad(K,t);assert tk>0
        x,y=t[:4],t[4:];rho=F(cert['rho']);assert 0<rho<1
        U=mat(rv['old_energy_upper']);CU=mat(rv['C_U_centre'])
        B=[[CU[i][j]+U[i][j+4] for j in range(8)] for i in range(4)]
        M=mat(rv['C_error_metric']);eps=F(rv['C_error_norm_upper'])
        direct=quad(mat(rv['D_z_upper']),x)+2*dot(x,mv(B,y))+iq(boxes(new['D_Y_model']),y)[1]
        direct+=F(new['operator_error'])*dot(y,y)+eps*(quad(M,x)+dot(y,y))
        fupper=direct-iq(U0,t)[0]+gamma*tk
        weights=u+[a+b for a,b in zip(x,mv(P,y))]+y
        C=boxes(g['C84_model']);cross=2*ilin(C,[[z*v for v in w] for z in weights])[1]
        bmodel=iq(boxes(g['B84_model']),w)[1]+(1-eta)*iq(boxes(pot['potential84_model']),w)[1]
        berror=F(pot['Bplus_operator_error_scalar'][1])*wn
        aerror=2*F(g['C84_D0_inverse_metric_error_norm'][1])*sup(wn*((1-rho)*dot(u,u)+tk))
        Hupper=iq(boxes(g['H84_model']),w)[1]+F(g['H84_operator_error_scalar'][1])*wn
        lowvals=[isum(times(v,w[j]) for j,v in enumerate(row)) for row in C[:191]]
        lowmodel=sum(max(abs(lo),abs(hi))**2 for lo,hi in lowvals)/(1-rho)
        Utail=Hupper+(sup(lowmodel)+sup(F(g['weighted_low_error_squared'][1])*wn))**2
        sourceprice=2*sup(ef2*Utail*tk)
        q_eta=fupper+cross+(1-rho)*dot(u,u)+bmodel+berror+aerror+sourceprice
        assert q_eta<0
        assert abs(q_eta-F(original[p]['optimistic_common_form_ray_upper']))<F(1,10**40)
        # Restore the entire eta reserve, without changing any other block.
        Lplus_upper=(bmodel+berror+Hupper)/(1-eta)
        assert Lplus_upper>0
        q_zero=q_eta+eta*Lplus_upper
        # Even this optimistic tail bonus is too small. ||Jw||_X^2 <= ||Jw||_WX^2.
        q_constant=q_zero+alpha*WX
        assert q_zero<0 and q_constant<0
        # Check the signed moment formula entrywise with rational intervals.
        lam=[tuple(map(F,v)) for v in new['lambda_model']];ms=[tuple(map(F,v)) for v in new['M_source_model']]
        mu=tuple(map(F,new['mu']));qmm=tuple(map(F,new['Q_mm_model']));assert mu[0]>0
        for i in range(8):
            for j in range(8):
                v1=divide(isum([prod(lam[i],ms[j]),prod(ms[i],lam[j])]),mu)
                v2=divide(prod(prod(lam[i],lam[j]),qmm),prod(mu,mu))
                calc=times(isum([v1,v2]),-1);target=tuple(map(F,new['moment_correction_model'][i][j]))
                assert max(calc[0],target[0])<=min(calc[1],target[1])
        rows.append({'parity':label.lower(),'full_comparison_upper_eta':q_eta,'full_comparison_upper_eta_display':display_up(q_eta),
             'finite_energy_relative_error_upper':gamma,'C_error_charge':aerror,'B_error_charge':berror,
             'finite_source_switch_charge':sourceprice,'w_norm_squared':wn,'Jw_WX_norm_squared':WX,
             'Lplus_ray_upper':Lplus_upper,'eta_restoration_upper':eta*Lplus_upper,
             'comparison_upper_without_eta':q_zero,'constant_bonus_upper':alpha*WX,
             'comparison_upper_without_eta_plus_full_constant_bonus':q_constant,
             'comparison_upper_with_constant_display':display_up(q_constant),
             'necessary_scalar_bonus_lower_from_ray':-q_zero/WX,
             'rational_moment_formula_entry_comparisons':64,
             'negative_actual_schur_witness':False,'full_remainder_certified':False})
        print(label,'comparison <=',display_up(q_eta),'even with full constant bonus <=',display_up(q_constant),flush=True)
    sources={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ['AUDIT_INPUT.json','OPTIMISTIC_OBSTRUCTION.json','AUDIT.json','DIRECT_Y_EVEN_3072.json','DIRECT_Y_ODD_3072.json']}
    return dump({'status':'PASS_INDEPENDENT_RATIONAL_COMPARISON_CONTROL','sources':sources,'constant_certificate':constant,'cases':rows,
                 'constant_bonus_is_optimistic_not_a_new_lower_bound':True,'inherited_operator_bounds_assumed':True,
                 'external_mathematical_review':False,'full_remainder_certified':False})

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    args.out.write_text(json.dumps(control(args.root),indent=2)+'\n')
