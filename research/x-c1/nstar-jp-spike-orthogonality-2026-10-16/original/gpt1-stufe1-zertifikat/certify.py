"""Directed whole-polynomial shell audit and corrected moment lift.

Only standard-library rational/integer interval operations. Inherited
operator/input certificates remain assumptions; no U8 action is evaluated.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, io, json, sys, zipfile

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'vendor'))
import source_core as sc
sc.DIGITS=180
sc.S=10**180
I=sc.I
BRIDGE_SHA='b48e3895d57cc5cc2c11ca170e32d6af5fbdfcde9948b4db7c370d3376b6d57b'
GLOBAL_SHA='2ca3c682de8a529b12a0d628c2b606fd04df332d1299ccd36dff71ac3e53d80c'

def sha(x):return hashlib.sha256(x).hexdigest()
def raw_member(z,suffix):
    names=[n for n in z.namelist() if n.endswith('/'+suffix)]
    assert len(names)==1,(suffix,names)
    return z.read(names[0])
def read(z,s):return json.loads(raw_member(z,s))
def box(x):
    lo,hi=map(F,x);assert lo<=hi
    return I.raw(I(lo).lo,I(hi).hi)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),I(0))
def exactdot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def exp_pos(x):
    assert x.lo>=0 and x.hi<2*sc.S
    term=I(1);total=term
    for n in range(1,401):term=term*x/n;total+=term
    nxt=term*x/401
    tail=nxt/(1-x/402)
    return total+I.raw(0,tail.hi)
def cosh(x):return (exp_pos(x)+1/exp_pos(x))/2
def sinh(x):return (exp_pos(x)-1/exp_pos(x))/2
def norm(v):return sum((x**2 for x in v),I(0)).sqrt()
def matvec_box(a,t):return [dot(row,[I(x) for x in t]) for row in a]
def poly_value(p,x):
    y=I(0)
    for v in reversed(p):y=y*x+v
    return y
def pinner(p,q):return 2*sc.psymint(sc.pmul(p,q),I(1))
def legendre_coefficients(p,n):
    return [pinner(p,[I(x) for x in sc.leg(j)])*F(2*j+1,2) for j in range(n+1)]
def norm_interval_with_error(model,e):
    assert model.lo>=0 and e.lo>=0
    return I.raw(max(0,model.lo-e.hi),model.hi+e.hi)
def bound_value_with_error(value,e):return value.inflate(e)
def serialize(x):
    if isinstance(x,I):return x.frac()
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serialize(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [serialize(v) for v in x]
    return x
def dump(path,x):path.write_bytes((json.dumps(serialize(x),indent=2,ensure_ascii=False)+'\n').encode())

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bridge-archive',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    assert __debug__ and not args.output.exists()
    out=args.output.resolve();assert not out.is_relative_to(HERE)
    if (HERE/'MANIFEST.json').exists():
        for name,d in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            p=(HERE/name).resolve();assert p.is_relative_to(HERE) and sha(p.read_bytes())==d,name
    incoming=json.loads((HERE/'incoming/STUFE1_SHELL_RESULTS_original.json').read_bytes())
    incoming_psi=json.loads((HERE/'incoming/PSI_DEFINITION_original.json').read_bytes())
    bb=args.bridge_archive.read_bytes();assert sha(bb)==BRIDGE_SHA
    with zipfile.ZipFile(io.BytesIO(bb)) as bz:
        dirs=read(bz,'expected/DIRECTIONS.json');ops=read(bz,'expected/OPERATORS.json')
        gb=raw_member(bz,'Objekt-X-Globaler-Gram-und-vollstaendige-Projektion-2026-10-13.zip')
        assert sha(gb)==GLOBAL_SHA
        with zipfile.ZipFile(io.BytesIO(gb)) as gz:
            half=read(gz,'half-inverse/expected/1536.json')
            assert sha(raw_member(gz,'vendor/source_core.py'))==sha((HERE/'vendor/source_core.py').read_bytes())
    a=3*sc.log_point(F(2))/2;b=sc.log_point(F(3));h=b-a;c=(a+b)/2
    assert 0<h.lo<h.hi<sc.S//10
    ellnorm=[(I(2*n+1)/(2*h)).sqrt() for n in range(96)]
    results={};psi_data={};parallel={}
    for sigma,parity in enumerate(['even','odd']):
        print(parity,'begin directed polynomial and moment construction',flush=True)
        hb=half['blocks'][sigma];qbox=[[box(v) for v in row] for row in hb['basis_Q_local_coefficients']]
        smat=[[F(x) for x in row] for row in hb['half_inverse_centre_rational_Q_coefficients']]
        ycols=[matvec_box(qbox,[row[j] for row in smat]) for j in range(8)]
        mu=(sinh(a)+(1 if sigma==0 else -1)*a)/2
        lam_ell=[h*ellnorm[n]*(cosh(c/2) if (n+sigma)%2==0 else sinh(c/2))*sc.mellin(n,h/2) for n in range(96)]
        lam_y=[dot(y,lam_ell) for y in ycols]
        zshell=[];zcore=[];zc_mom=[];zc_leg=[]
        for n in range(sigma+2,sigma+10,2):
            prof=sc.profile(n,b)['f']
            phys=sc.pscale(prof,1/(2*b).sqrt())
            sh=sc.pcompose(phys,c/b,h/(2*b))
            core=sc.pcompose(phys,I(0),a/b)
            sh_coeff=[h*ellnorm[j]*pinner(sh,[I(v) for v in sc.leg(j)]) for j in range(10)]+[I(0)]*86
            zshell.append(sh_coeff);zcore.append(core)
            lc=legendre_coefficients(core,9);zc_leg.append(lc)
            cm=a*dot(lc,[sc.mellin(j,a) for j in range(10)])
            zc_mom.append(cm)
            # Exact physical moment-null identity, independently split at a8.
            assert (cm+dot(sh_coeff,lam_ell)).contains_zero()
            # Two exact finite polynomial integrations of the shell norm.
            assert sum((x**2 for x in sh_coeff),I(0)).intersects(h*pinner(sh,sh))
        fsh=zshell+ycols
        gsh=[[dot(x,y) for y in fsh] for x in fsh]
        gc=[]
        for i in range(12):
            row=[]
            for j in range(12):
                if i<4 and j<4:v=a*pinner(zcore[i],zcore[j])
                elif i<4:v=-2*zc_mom[i]*lam_y[j-4]/mu
                elif j<4:v=-2*zc_mom[j]*lam_y[i-4]/mu
                else:v=2*lam_y[i-4]*lam_y[j-4]/mu
                row.append(v)
            gc.append(row)
        kinv=[[F(x) for x in row] for row in ops[parity]['K12_inverse_rational']]
        tr_sh=sum((I(kinv[i][j])*gsh[j][i] for i in range(12) for j in range(12)),I(0))
        tr_core=sum((I(kinv[i][j])*gc[j][i] for i in range(12) for j in range(12)),I(0))
        assert tr_sh.lo>0 and tr_core.lo>0
        lam_force=[I(0)]*4+lam_y
        lam_dual2=sum((lam_force[i]*I(kinv[i][j])*lam_force[j] for i in range(12) for j in range(12)),I(0))
        assert lam_dual2.lo>0
        base=dirs[parity]['directions'];v=list(map(F,base['upper_v']['t_exact_rational']));p=list(map(F,base['lower_Pv']['t_exact_rational']))
        q=F(dirs[parity]['q']);vv=exactdot(v,v);pp=exactdot(p,p);alpha=q/vv
        e=[x-alpha*y for x,y in zip(p,v)];e2=exactdot(e,e)
        assert exactdot(v,p)==q and exactdot(v,e)==0 and e2>0 and pp!=q*q
        parallel[parity]={'v_norm_squared':vv,'q_vstarP_v':q,'p_norm_squared':pp,
            'alpha_q_over_vnorm2':alpha,'e_exact':e,'e_norm_squared':e2,
            'relative_e_norm_upper':(I(e2)/I(pp)).sqrt(),
            'exact_parallel':False,'q_equals_p_norm':False,
            'identity':'p=alpha v+e; ell_p=alpha ell_v+ell_e; full ell_e not evaluated'}
        entries={}
        for name in ['upper_v','lower_Pv','orthogonal_difference']:
            if name=='orthogonal_difference':
                t=e
                zt=[F(x)-alpha*F(y) for x,y in zip(base['lower_Pv']['Zt_exact_rational'],base['upper_v']['Zt_exact_rational'])]
                k0=[F(x)-alpha*F(y) for x,y in zip(base['lower_Pv']['K_inverse_Cfin_mid_t_exact_rational'],base['upper_v']['K_inverse_Cfin_mid_t_exact_rational'])]
            else:
                dd=base[name];t=list(map(F,dd['t_exact_rational']));zt=list(map(F,dd['Zt_exact_rational']));k0=list(map(F,dd['K_inverse_Cfin_mid_t_exact_rational']))
            k=list(map(I,k0));r=matvec_box(qbox,zt)
            # Combine before multiplying by the interval Q: r-Y k_tail.
            ww=[zt[i]-exactdot(smat[i],k0[4:]) for i in range(92)]
            w=matvec_box(qbox,ww)
            lam_r=dot(r,lam_ell);lam_total=dot(w,lam_ell)
            lam_sum=dot(k[4:],lam_y)
            assert lam_total.intersects(lam_r-lam_sum)
            psi_sh=[w[n]-sum((k[j]*zshell[j][n] for j in range(4)),I(0)) for n in range(96)]
            psi_poly=[I(0)]
            for j in range(4):psi_poly=sc.padd(psi_poly,sc.pscale(zcore[j],-k[j]))
            poly_mom=-dot(k[:4],zc_mom);dm=-lam_total/mu
            core_n2=a*pinner(psi_poly,psi_poly)+4*dm*poly_mom+2*dm**2*mu
            assert core_n2.lo>0
            shell_model_norm=norm(psi_sh);core_model_norm=core_n2.sqrt()
            source_error=I(F(dirs[parity]['Cfin_midpoint_error_K_inverse_norm_upper']))*I(exactdot(t,t)).sqrt()
            err_sh=source_error*tr_sh.sqrt();err_core=source_error*tr_core.sqrt()
            lam_error=source_error*lam_dual2.sqrt()
            actual_sh=norm_interval_with_error(shell_model_norm,err_sh)
            actual_core=norm_interval_with_error(core_model_norm,err_core)
            # True moment vanishes for EVERY k, not just the model k0.
            moment_check=poly_mom-lam_total+dot(psi_sh,lam_ell)
            assert moment_check.contains_zero()
            wrong_moment_model=poly_mom-(lam_r+lam_sum)+dot(psi_sh,lam_ell)
            wrong_moment=wrong_moment_model.inflate(2*lam_error)
            if name!='orthogonal_difference':assert not wrong_moment.contains_zero()
            endpoints=[]
            for sign in [-1,1]:
                val=sum((psi_sh[n]*ellnorm[n]*(sign**n) for n in range(96)),I(0))
                fvals=[sum((col[n]*ellnorm[n]*(sign**n) for n in range(96)),I(0)) for col in fsh]
                ev2=sum((fvals[i]*I(kinv[i][j])*fvals[j] for i in range(12) for j in range(12)),I(0))
                assert ev2.lo>0
                endpoints.append(val.inflate(source_error*ev2.sqrt()))
            # The z columns are continuous at a8 and cancel out of the jump.
            ma=cosh(a/2) if sigma==0 else sinh(a/2)
            jump_model=sum((w[n]*ellnorm[n]*((-1)**n) for n in range(96)),I(0))+lam_total*ma/mu
            jump_f=[I(0)]*4+[sum((col[n]*ellnorm[n]*((-1)**n) for n in range(96)),I(0))+ly*ma/mu for col,ly in zip(ycols,lam_y)]
            jump_dual2=sum((jump_f[i]*I(kinv[i][j])*jump_f[j] for i in range(12) for j in range(12)),I(0))
            assert jump_dual2.lo>0
            jump=jump_model.inflate(source_error*jump_dual2.sqrt())
            if name!='orthogonal_difference':
                old=incoming[parity]['directions'][name]
                assert (shell_model_norm-I(F(old['shell_chi_X_norm']))).absolute().hi < sc.S*F(1,10**25)*max(F(1),F(old['shell_chi_X_norm']))
                assert (I(F(old['core_moment_coefficient_lambda_total']))-(lam_r+lam_sum)).absolute().hi<sc.S*F(1,10**25)
                assert F(incoming_psi[parity]['directions'][name]['lambda_total_mid'])==F(old['core_moment_coefficient_lambda_total'])
            entries[name]={'t_exact':t,'k_model_exact':k0,
                'actual_k_minus_kmodel_K_norm_upper':source_error,
                'analytic_function_error_structure':'psi_actual-psi_model=-F*(k_actual-k_model); retain this structure for Q/U8 transport',
                'shell_model_coefficients_interval':psi_sh,'core_polynomial_scaled_x_over_a8_interval':psi_poly,
                'lambda_total_model_interval':lam_total,'actual_lambda_total_interval':lam_total.inflate(lam_error),
                'core_m_multiplier_model_interval':dm,
                'shell_model_norm':shell_model_norm,'actual_shell_norm':actual_sh,
                'shell_model_error_norm_upper':err_sh,'core_model_norm':core_model_norm,
                'actual_core_norm_before_U8':actual_core,'core_model_error_norm_upper':err_core,
                'model_full_moment_zero_check':moment_check,
                'wrong_plus_sign_full_moment_interval':wrong_moment,
                'shell_endpoint_a8_plus':endpoints[0],'shell_endpoint_b9_minus':endpoints[1],
                'jump_at_a8_actual_interval':jump,
                'coefficient_of_log_a8_minus_x_in_Pi8_Qpsi':jump/2,
                'U8_action_computed':False,'chi_core_norm_computed':False}
            print(parity,name,'shell',actual_sh.display(),'core before U8',actual_core.display(),'jump',jump.display(),flush=True)
        results[parity]={'mu':mu,'lambda_Y':lam_y,'trace_Kinverse_Gshell':tr_sh,
            'trace_Kinverse_Gcore':tr_core,'directions':entries}
        shell_lower=F(entries['lower_Pv']['actual_shell_norm'].lo,sc.S)
        w9_lower=F(11,10)/q*shell_lower**2
        coarse=F(252000000000 if parity=='even' else 49800000000)
        assert w9_lower>coarse
        results[parity]['full_W9_operator_norm_lower_rational']=w9_lower
        results[parity]['full_W9_operator_norm_strict_lower_simple']=coarse
        results[parity]['W9_lower_scope']='Full chosen majorant W9 on H9; NOT true A9 inverse, NOT an error upper bound, NOT N12 exclusion.'
        psi_data[parity]={'parity':sigma,'mu':mu,'directions':{name:{key:row[key] for key in ['t_exact','k_model_exact','actual_k_minus_kmodel_K_norm_upper','analytic_function_error_structure','shell_model_coefficients_interval','core_polynomial_scaled_x_over_a8_interval','core_m_multiplier_model_interval','actual_lambda_total_interval','shell_model_error_norm_upper','core_model_error_norm_upper']} for name,row in entries.items()}}
    out.mkdir(parents=True)
    dump(out/'DIRECTED_RESULTS.json',results)
    dump(out/'PARALLELISM.json',parallel)
    dump(out/'PSI_CORRECTED.json',{'definition':'psi=Lambda Jt-Fk; core polynomial in x/a8 plus coefficient*m(x); model coefficient intervals and separate full analytic errors',
        'lambda_total':'lambda(Jt)-sum_j k_(4+j)*lambda(Y_j)',
        'model_k_not_exact_k':True,'data':psi_data})
    dump(out/'RECEIPT.json',{'status':'PASS','bridge_archive_sha256':BRIDGE_SHA,
        'global_source_archive_sha256':GLOBAL_SHA,'directed_decimal_digits':180,
        'original_shell_diagnostics_match_within_relative_1e_minus_25':True,
        'wrong_core_moment_sign_rejected':True,'exact_parallelism_rejected':True,
        'full_W9_norm_lower_certified_under_inherited_hypotheses':True,
        'inherited_hypotheses_retained':True,'U8_action_computed':False,
        'residual_pairings_computed':False,'N12_rule_excluded':False,'A9_A11_closed':False,
        'external_review_open':True})
    for name in ['DIRECTED_RESULTS.json','PARALLELISM.json','PSI_CORRECTED.json','RECEIPT.json']:
        if (HERE/'expected'/name).exists():assert (HERE/'expected'/name).read_bytes()==(out/name).read_bytes()

if __name__=='__main__':main()
