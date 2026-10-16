"""Whole-shell response norm: polynomial/log integrals, with complete remainders.

This is not a W9 energy computation. All certification arithmetic is directed
integer arithmetic or exact fractions. No point samples enter a bound.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb
import sys,json,argparse,hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE/'input/objekt-x-f12-d12-audit-2026-10-15'))
from independent_check import I,logq,logi,up,need,strict_ldl

def add(a,b):
    return [(a[i] if i<len(a) else I(0))+(b[i] if i<len(b) else I(0)) for i in range(max(len(a),len(b)))]
def scale(a,c):return [v*c for v in a]
def multiply(a,b):
    out=[I(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
    return out
def affine(a,s):
    # Exact binomial formula for a(1+s*u); shared geometry stays enclosed.
    out=[];power=I(1)
    for k in range(len(a)):
        out.append(power*sum((Q(c)*comb(j,k) for j,c in enumerate(a) if j>=k),Q(0)))
        power=power*s
    return out
def whole_square(a,l):
    # Integral_0^1 [a(u)-l(u)log(u)]^2, including its logarithmic endpoint.
    out=I(0)
    for i,x in enumerate(a):
        for j in range(i,len(a)):out=out+x*a[j]*Q(1 if i==j else 2,i+j+1)
    for i,x in enumerate(a):
        for j,y in enumerate(l):out=out+2*x*y/Q((i+j+1)**2)
    for i,x in enumerate(l):
        for j in range(i,len(l)):out=out+x*l[j]*Q(2 if i==j else 4,(i+j+1)**3)
    return out
def ceilq(v,d=80):
    n=10**d;return Q(-((-v.numerator*n)//v.denominator),n)
def rounded(a,d=90):
    n=10**d;out=[];err=Q(0)
    for v in a:
        m=(v.low+v.high)/2
        q=Q((2*m.numerator*n+m.denominator)//(2*m.denominator),n)
        out.append(q);err+=max(abs(v.low-q),abs(v.high-q))
    return out,err
def bilinear(a,l,b,k):
    # Exact scalar product of a-l log(u) and b-k log(u).
    z=Q(0)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z+=x*y/Q(i+j+1)
        for j,y in enumerate(k):z+=x*y/Q((i+j+1)**2)
    for i,x in enumerate(l):
        for j,y in enumerate(b):z+=x*y/Q((i+j+1)**2)
        for j,y in enumerate(k):z+=2*x*y/Q((i+j+1)**3)
    return z

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    need(not args.output.exists(),'new output required')
    fp=HERE/'inputs/FUNCTIONS12.json'
    xp=HERE/'inputs/FROZEN_RESPONSE12.json'
    apath=HERE/'inputs/FRESH_A12.json'
    sp=HERE/'inputs/OLD_A9_N12.json'
    fs=json.loads(fp.read_bytes());xs=json.loads(xp.read_bytes());aa=json.loads(apath.read_bytes());ss=json.loads(sp.read_bytes())
    a=logq(Q(3));b=logq(Q(11))/2;h=b-a;s=h/a;r=s/2
    need(0<s.low<s.high<Q(1,10),'whole shell radius')
    mdegree=80;ldegree=120;keep=80
    em=ceilq(4*Q(101,2000)**(mdegree+1)/factorial(mdegree+1),250)
    el=ceilq(r.high**(ldegree+1)/((ldegree+1)*(1-r.high)),200)
    lp=[logi(2/s)]+[(-1)**(k+1)*r**k/k for k in range(1,ldegree+1)]
    out={'status':'WHOLE_RESPONSE_NORM_CONDITIONAL','method':'complete polynomial/log square integral plus full Taylor and polynomial-tail errors',
         'source_bindings':{str(p.relative_to(HERE)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in (fp,xp,apath,sp)},
         'log_Taylor_degree':ldegree,'moment_Taylor_degree':mdegree,'retained_regular_degree':keep,
         'full_logarithmic_endpoint_included':True,'point_sampling_used_in_certificate':False,
         'W9_norm_or_energy_computed':False,'parities':{}}
    for parity,p in [('even',0),('odd',1)]:
        mu=a/2+Q(2,3) if p==0 else -a/2+Q(2,3)
        mut=b/2+5/(2*I(11).sqrt()) if p==0 else -b/2+5/(2*I(11).sqrt())
        g=mut/mu;need(1<g.low<g.high<4,'physical W metric')
        mc=[I(2 if (k+p)%2==0 else 1)/I(3).sqrt()*(h/2)**k/factorial(k) for k in range(mdegree+1)]
        model=[]
        for row in fs['parities'][parity]['functions']:
            f=row['F'];pol=affine(f['polynomial'],s);log=affine(f['log_ratio_multiplier'],s);c=Q(f['physical_W_moment_multiplier'])
            reg=add(add(pol,scale(mc,c)),multiply(log,lp))
            model.append((reg,log,c))
        candidates={'fixed_X':[[Q(v) for v in row] for row in xs['parities'][parity]['X']],
          'audit_S':[[(Q(x)+Q(y))/2 for x,y in zip(l,u)] for l,u in zip(ss['parities'][parity]['inverse_lower_Loewner'],ss['parities'][parity]['inverse_upper_Loewner'])]}
        result={}
        for label,mat in candidates.items():
            need(mat==list(map(list,zip(*mat))),'symmetric response');strict_ldl(mat)
            norms=[];models=[];errors=[]
            for index,row in enumerate(mat):
                reg=[I(0)];log=[I(0)];c=Q(0)
                for x,(ar,al,ac) in zip(row,model):reg=add(reg,scale(ar,x));log=add(log,scale(al,x));c+=x*ac
                tail=sum((up(v) for v in reg[keep+1:]),Q(0))
                error=ceilq(tail+abs(c)*em+sum((up(v) for v in log),Q(0))*el,200)
                reg=reg[:keep+1];raw=whole_square(reg,log)
                need(raw.low>0,'positive response square integral')
                ar,er=rounded(reg);lr,elr=rounded(log)
                error=ceilq(error+er+2*elr,200)
                exact=bilinear(ar,lr,ar,lr)
                need(exact>0,'positive rational square')
                # Independent interval assembly must contain the rational
                # polynomial/log norm up to the separately paid rounding.
                need(I(exact).sqrt().high <= I(raw.high).sqrt().high+er+2*elr,'diagonal integral assembly')
                models.append((ar,lr));errors.append(error)
                norms.append({'index':index,'polynomial_log_square_interval':raw.pair(),
                  'whole_bracket_L2_error_upper':str(error),
                  'regular_rational_coefficients':[str(v) for v in ar],
                  'log_rational_coefficients':[str(v) for v in lr]})
            gram=[[Q(0)]*12 for _ in range(12)]
            for i,(ar,lr) in enumerate(models):
                for j in range(i,12):
                    gram[i][j]=gram[j][i]=bilinear(ar,lr,*models[j])
            e2=sum((v*v for v in errors),Q(0));tr0=sum(gram[i][i] for i in range(12))
            price=ceilq(2*I(tr0*e2).sqrt().high+e2,150)
            metric=ceilq((s*g).high,100)
            upper=[[metric*(v+(price if i==j else 0)) for j,v in enumerate(row)] for i,row in enumerate(gram)]
            strict_ldl(upper)
            trace=ceilq(sum(upper[i][i] for i in range(12)));tnorm=ceilq(I(trace).sqrt().high)
            dD=Q(fs['parities'][parity]['whole_D12_operator_error_upper']);dF=Q(fs['parities'][parity]['whole_F12_operator_error_upper']);dA=Q(aa['parities'][parity]['whole_Loewner_radius'])
            kerr=ceilq(2*dF*tnorm+dA*trace)
            r2=ceilq(dD*dD*trace,150)
            result[label]={'rows':norms,'T_norm_squared_upper':str(trace),'T_norm_upper':str(tnorm),
              'rational_whole_reference_Gram':[[str(v) for v in row] for row in gram],
              'whole_reference_Gram_Loewner_error':str(price),'physical_metric_factor_upper':str(metric),
              'physical_TT_adjoint_upper':[[str(v) for v in row] for row in upper],
              'direct_K_error_upper':str(kerr),'weighted_residual_error_factor_per_unit_W9_norm':str(r2),
              'whole_Hilbert_residual_model_error_upper':str(ceilq(dD*tnorm,100))}
            print(parity,label,'T <=',float(tnorm),'K error <=',float(kerr),'weighted factor <=',float(r2),flush=True)
        out['parities'][parity]=result
    args.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':main()
