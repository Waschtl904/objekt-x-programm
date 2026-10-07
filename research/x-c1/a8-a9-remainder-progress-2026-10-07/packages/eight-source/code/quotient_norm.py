"""Independent ordinary L2 quotient norm; diagnostic, not a changed test norm."""
from pathlib import Path
import argparse,json
import eight_source_refined as m

def run():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();assert not a.out.exists()
    m.ctx.prec=3072
    b=m.arb(3).log();old=3*m.arb(2).log()/2;r=old/b;pol=m.legendre(9);records=[]
    for p,label in enumerate(['even','odd']):
        # No positivity or inverse of the new form is used.
        bi=m.sc.log_point(3);profiles=[m.ipoly(m.sc.profile(n,bi)['f']) for n in range(p+2,p+10,2)]
        mp=m.arb_poly([(b/2)**k/m.factorial(k) if k%2==p else m.arb(0) for k in range(201)])
        tail=(b/2)**201/m.factorial(201)/(1-b/(2*202))
        inner=(b*r).sinh()/(2*b)+(r/2 if p==0 else -r/2)
        beta=[]
        W=m.arb_mat([[m.pint(f*g) for g in profiles] for f in profiles])
        shell=m.arb_mat([[m.pint(f*g,r,m.arb(1)) for g in profiles] for f in profiles])
        for j,f in enumerate(profiles):
            beta.append(m.pint(f*mp,r,m.arb(1))+m.arb(0,(W[j,j].sqrt()*tail).upper()))
        Q=m.arb_mat([[shell[i,j]+beta[i]*beta[j]/inner for j in range(4)] for i in range(4)])
        assert m.positive(m.lower(Q))
        records.append({'parity':label,'fixed_source_gram':W,'outer_shell_gram':shell,
                        'shell_moment_pairings':beta,'inner_moment_norm_squared':inner,
                        'L2_quotient_gram':Q,'positive_quotient_gram':True})
    out={'status':'L2_QUOTIENT_NORM_DIAGNOSIS','blocks':records,
         'formula':'inf_{u in H_a^moment} ||Ju+Z alpha||_L2^2 = alpha* (W_shell + beta beta*/mu_inner) alpha',
         'meaning':'Ordinary L2 quotient norm only. The predeclared test still uses the full source Gram W. No full new form-domain decomposition or tail estimate is inferred.',
         'target_positivity_used':False,'external_review':'OPEN'}
    a.out.write_text(json.dumps(m.serial(out),indent=2)+'\n',encoding='utf-8')
    print(out['status'])
if __name__=='__main__':run()
