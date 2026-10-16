"""Separate exact integer lifting of all decisive directional quantities."""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import argparse,json,zipfile

HERE=Path(__file__).resolve().parent
def member(z,suffix):
    hits=[n for n in z.namelist() if n.endswith('/'+suffix)];assert len(hits)==1
    return json.loads(z.read(hits[0]))
def integer_quad(a,u):
    # Clear all denominators first; no rational matrix-vector dot recurrence.
    ud=lcm(*(x.denominator for x in u));iv=[int(x*ud) for x in u]
    den=lcm(*(F(x).denominator for row in a for x in row))
    total=0
    for i,row in enumerate(a):
        for j,val in enumerate(row):total+=int(F(val)*den)*iv[i]*iv[j]
    return F(total,den*ud*ud)
def symmetric_interval_quad(a,u):
    # Unlike the generator, use only symmetric triangular coefficients.
    lo=hi=F(0)
    for i in range(len(u)):
        l,h=map(F,a[i][i]);lo+=u[i]**2*l;hi+=u[i]**2*h
        for j in range(i):
            a0,a1=map(F,a[i][j]);b0,b1=map(F,a[j][i])
            c=u[i]*u[j];ll=a0+b0;hh=a1+b1
            lo+=c*(ll if c>=0 else hh);hi+=c*(hh if c>=0 else ll)
    return lo,hi

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--result',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();assert __debug__ and not a.output.exists()
    result=json.loads(a.result.read_bytes());w=json.loads((HERE/'pr226/WITNESSES.json').read_bytes())
    sources=list(result['input_archives']);checked=0
    with zipfile.ZipFile(a.inputs/sources[0]) as iz,zipfile.ZipFile(a.inputs/sources[1]) as rz:
        for p in ('even','odd'):
            d=member(iz,'INVERSE_'+p.upper()+'.json');r=member(rz,'RESPONSES_'+p.upper()+'.json')
            data=result['parities'][p];rho=F(r['rho']);em=F(r['M_error_coefficient_rational'])
            c=F(data['residual_cap']);s=F(data['S_inverse_norm_upper'])
            for key,row in data['directions'].items():
                u=list(map(F,w['parities'][p][key]));norm=sum(x*x for x in u)
                du=(1-rho)*sum(x*x for x in u[:191])+integer_quad(r['K12_new_rational'],u[191:])
                mu=integer_quad(r['M_upper_rational'],u);eu=integer_quad(d['E_rational'],u)
                ml,mh=symmetric_interval_quad(r['M203_model'],u)
                for k,val in [('D_direction',du),('M_upper_direction',mu),('E_direction',eu),
                              ('E_relative_to_D',eu/du),('analytic_price_over_E',em*du/eu)]:
                    assert F(row[k])==val;checked+=1
                assert list(map(F,row['model_M_interval']))==[ml,mh]
                assert F(row['rounding_upper_over_E'])==(mu-em*du-ml)/eu
                delta_lo,delta_hi=map(F,row['actual_Delta_interval'])
                assert delta_lo==(1-c)*eu and delta_hi==du-ml+em*du
                x=list(map(F,row['X_u']));assert len(x)==84
                for i,r0 in enumerate(d['X84x203_rational']):
                    assert x[i]==sum(F(y)*z for y,z in zip(r0,u));checked+=1
                x2=sum(z*z for z in x);xl=F(row['X_u_norm_lower']);eh=F(row['S_inverse_R_u_norm_upper'])
                assert 0<xl and xl*xl<=x2 and eh*eh>=s*c*eu and xl>eh
                lb=F(row['Hstar_inverse_Rayleigh_at_J_X_u_lower'])
                assert lb==(xl-eh)**2/delta_hi
                if key=='u_E_min':assert lb>(55000 if p=='even' else 9300)
            test=data['W9_scalar_test'];v=list(map(F,test['upper_vector_v']));pv=list(map(F,test['lower_vector_Pv']))
            P=d['P_upper_rational'];vpv=integer_quad(P,v)
            assert F(test['v_P_v'])==vpv and F(test['lower_weight'])==F(11,10)/vpv
            for i,r0 in enumerate(P):assert pv[i]==sum(F(y)*z for y,z in zip(r0,v));checked+=1
            # Exact PSD Cauchy remainder evaluated on four unrelated rational vectors.
            for hv in [v,pv,[F(i==0) for i in range(84)],[F((-1)**i,i+1) for i in range(84)]]:
                assert integer_quad(P,hv)*vpv>=sum(x*y for x,y in zip(pv,hv))**2
    report={'status':'PASS','separate_method':'integer denominator lifting and triangular interval quadratics',
            'exact_scalar_and_vector_equalities':checked,'parities':2,'directions':4,
            'lower_inverse_bounds':[55000,9300],'W9_scalar_Cauchy_controls':8,
            'analytic_and_global_residual_hypotheses_inherited':True,'full_A9_A11_closed':False}
    a.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(report),flush=True)
if __name__=='__main__':main()
