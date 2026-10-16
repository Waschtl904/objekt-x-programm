import time
import mpmath as mp
from qnp_psi import *
g=setup(25); a8=g['a8']
for par in ['even','odd']:
    psi=Psi(g,par,'upper_v')
    j=psi.shell_val(a8)-psi.core(a8)
    print(par,'Sprung j_v =',mp.nstr(j,12),'  psi(a8-)=',mp.nstr(psi.core(a8),10),' psi(a8+)=',mp.nstr(psi.shell_val(a8),10),' psi(b9-)=',mp.nstr(psi.shell_val(g['b9']),8))
    t0=time.time()
    for e in ['1e-2','1e-3','1e-4','1e-6','1e-8','1e-10']:
        e=mp.mpf(e); x=a8-e
        val=q_raw(psi,x,g)
        print('   x=a8-%s: Q psi = %s ;  Q psi - (j/2) log(a8-x) = %s'%(mp.nstr(e,2),mp.nstr(val,10),mp.nstr(val-(j/2)*mp.log(e),10)))
    print('   Zeit pro Auswertung ~%.2fs'%((time.time()-t0)/6))
