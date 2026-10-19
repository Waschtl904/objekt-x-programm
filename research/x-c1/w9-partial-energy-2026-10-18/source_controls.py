"""Independent direct-kernel controls of low and high old polynomial sources."""
import gc
import json
from flint import arb,acb,arb_poly,ctx
from common import Inputs,Poly,q,pint,need,pad,encode,HERE
from residuals import Residuals
from old_fields import OldFields,kernel,gamma_coefficients
from source_bounds import SourceBounds
from weights import gamma_error
from integrate import ellipse,cheb_error


def run():
    ctx.prec=1600;inp=Inputs();report={}
    nodes256=[arb.legendre_p_root(256,k,weight=True)for k in range(256)]
    nodes512=[arb.legendre_p_root(512,k,weight=True)for k in range(512)]
    full_kernel=lambda r:(-r/2).exp()/(1-(-2*r).exp())
    for par in ('even','odd'):
        res=Residuals(inp,par);fields=OldFields(inp,res);a=res.a8;b=res.a;hs=b-a
        source_bounds=SourceBounds(fields,inp)
        records=[];eps=gamma_error(224,q('11/10'))
        for j in (0,8,91):
            f=Poly(fields.local[j]);norm2=hs*pint(fields.local[j]*fields.local[j],arb(-1),arb(1))
            need(norm2>0,'Source norm')
            for fraction in (q('2/5'),q('9/10')):
                x=a*fraction
                def integrand(y):
                    return -f((2*y-a-b)/hs)*(full_kernel(y-x)+res.eps*full_kernel(y+x))
                direct=sum((hs*w/2*integrand((a+b)/2+hs*z/2)for z,w in nodes256),arb(0))
                yy=ellipse(a,b);M=abs(integrand(yy)).upper()
                direct=pad(direct,cheb_error(a,b,256)*M)
                field=fields.global_fields[195+j]
                model=field[None](fraction)+fields.lam[j]/res.mu8*fields.qm[None](fraction)
                for tag in ('one','minus_one','outer','minus_outer'):
                    coefficient=field.get(tag,arb_poly([]))(fraction)+fields.lam[j]/res.mu8*fields.qm.get(tag,arb_poly([]))(fraction)
                    model+=coefficient*abs(fraction-fields.roots[tag]).log()
                error=eps*(2*hs*norm2).sqrt()
                need(abs(direct-model)<error,'Independent old shell kernel control')
                full_model=field[None](fraction)
                for tag in ('one','minus_one','outer','minus_outer'):
                    full_model+=field.get(tag,arb_poly([]))(fraction)*abs(fraction-fields.roots[tag]).log()
                analytic_bound=source_bounds.ellipse(acb(x),[arb(0)]*92)[j]
                need(abs(full_model)<analytic_bound,'Whole integral source majorant')
                records.append({'source_column':j,'x_over_a8':fraction,'difference':direct-model,'kernel_error_bound':error})
        report[par]={'direct_shell_kernel_controls':records}
        del res,fields;gc.collect()
    # Independent real integration of the absolute-value kernel, split at x.
    # Its removable value at zero is handled by analyticity for the remainder.
    a=3*arb(2).log()/2;t=q('1/3');leg=__import__('common').legs(384)
    records=[];cs=gamma_coefficients(160);eps=gamma_error(160,q('21/20'))
    for n in (2,3,382,383):
        f=leg[n];ls=[arb(0)]*(n+1);ls[n]=arb(1)
        model=kernel(f,ls,a,cs,n%2)(t);direct=arb(0)
        for lo,hi,sign in ((arb(-1),t,-1),(t,arb(1),1)):
            def value(u):
                r=a*sign*(u-t)
                return a*f(u)*((r/2).exp()/(2*r.sinh())-1/(2*r))
            direct+=sum(((hi-lo)*w/2*value((lo+hi)/2+(hi-lo)*z/2)for z,w in nodes512),arb(0))
            uu=ellipse(lo,hi)
            need(abs(a*sign*(uu-t)).upper()<3,'Regular-kernel analytic disk')
            # On |r|=3, |sinh r|>=1/10, so |k_reg(r)|<24. Maximum modulus
            # gives the same bound throughout the disk, including r=0.
            M=24*a*abs(Poly(f)(uu)).upper()
            direct=pad(direct,cheb_error(lo,hi,512)*M)
        need(abs(model-direct)<2*a*eps,'Independent full old core kernel control')
        records.append({'degree':n,'difference':model-direct,'kernel_error_bound':2*a*eps})
    report['absolute_kernel_action']=records
    return report


if __name__=='__main__':
    (HERE/'SOURCE_CONTROLS.json').write_text(json.dumps(encode(run()),indent=2)+'\n')
    print('PASS: 12 independent shell-kernel and four complete absolute-kernel controls')
