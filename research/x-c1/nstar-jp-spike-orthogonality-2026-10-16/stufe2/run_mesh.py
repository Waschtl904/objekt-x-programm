import sys, json, time
import mpmath as mp
from qnp_psi import *
par=sys.argv[1]; direction=sys.argv[2] if len(sys.argv)>2 else 'upper_v'
g=setup(22); a8=g['a8']
psi=Psi(g,par,direction)
inner=interior_breakpoints(g)
nodes,cells=mesh(g,inner,n_per_cell=12,grade_levels=28)
out={'parity':par,'direction':direction,'dps':22,'interior_breakpoints':[str(b) for b in inner],
     'cells':[[str(a),str(b)] for a,b in cells],'nodes':[]}
t0=time.time()
for i,(x,w) in enumerate(nodes):
    hg=h_gamma(psi,x,g); sv=s_shift(psi,x,g); pv=psi(x)
    out['nodes'].append({'x':str(x),'w':str(w),'psi':str(pv),'H_gamma_psi':str(hg),'S_psi':str(sv),'Q_raw':str(hg-g['kappa']*pv-sv)})
    if i%24==0:
        print(i,len(nodes),'%.0fs'%(time.time()-t0),flush=True)
        json.dump(out,open(f'MESH_{par}_{direction}.json','w'))
json.dump(out,open(f'MESH_{par}_{direction}.json','w'))
print('done',time.time()-t0)
