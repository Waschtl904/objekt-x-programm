import json
import mpmath as mp
from qnp_psi import *
g=setup(22); a8=g['a8']
out={}
for par in ['even','odd']:
    psi=Psi(g,par,'upper_v')
    bps=interior_breakpoints(g)
    eps=mp.mpf('1e-12')
    rows=[]
    for b in bps:
        l=q_raw(psi,b-eps,g); r=q_raw(psi,b+eps,g)
        # welche Verschiebung?
        src=[]
        for q,w,lq in g['shifts']:
            for wall,name in [(a8,'a8'),(g['b9'],'b9')]:
                for cand,desc in [(wall-lq,f'x+log{q} trifft +{name}'),(lq-wall,f'x-log{q} trifft -{name}')]:
                    if abs(cand-b)<mp.mpf('1e-15'): src.append(desc)
        rows.append({'x':mp.nstr(b,12),'quelle':src,'Q_raw_links':mp.nstr(l,12),'Q_raw_rechts':mp.nstr(r,12),'Sprung':mp.nstr(r-l,10)})
        print(par,rows[-1])
    j=psi.shell_val(a8)-psi.core(a8)
    val=q_raw(psi,a8-mp.mpf('1e-10'),g)
    out[par]={'interior_jumps':rows,'jump_psi_a8':mp.nstr(j,14),'log_coefficient_j/2':mp.nstr(j/2,14),
              'Q_raw(a8-1e-10)':mp.nstr(val,12),'Q_raw - (j/2)log(a8-x) at 1e-10':mp.nstr(val-(j/2)*mp.log(mp.mpf('1e-10')),12)}
    print(par,'j=',out[par]['jump_psi_a8'],' Konstante:',out[par]['Q_raw - (j/2)log(a8-x) at 1e-10'])
json.dump(out,open('STUFE2_JUMPS.json','w'),indent=1)
