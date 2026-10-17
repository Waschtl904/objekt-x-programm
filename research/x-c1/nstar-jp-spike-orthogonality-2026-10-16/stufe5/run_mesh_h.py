"""f_t = Pi8[Q^np psi_t] auf dem mit den h-Schnittstellen (c_tilde, Dhat) vereinigten Netz (Stufe 5)."""
import sys, json, time
import mpmath as mp
from qnp_psi import *
par=sys.argv[1]; direction=sys.argv[2] if len(sys.argv)>2 else 'upper_v'
g=setup(22); a8=g['a8']; a=mp.log(3); b=mp.log(11)/2
psi=Psi(g,par,direction)
L={q: mp.log(q) for q in [2,3,4,5,7,8]}
cuts=[a-L[2], b-L[2], b-a]+[L[q]-a for q in (4,5,7,8)]+[L[q]-b for q in (4,5,7,8)]+[2*a-b]
inner=sorted(set(interior_breakpoints(g)) | set(c for c in cuts if 0<c<a8))
# nahe beieinander liegende Punkte (<1e-12) zusammenlegen
merged=[]
for x in inner:
    if not merged or abs(x-merged[-1])>mp.mpf(10)**-12: merged.append(x)
nodes,cells=mesh(g,merged,n_per_cell=12,grade_levels=28)
out={'parity':par,'direction':direction,'dps':22,'interior_breakpoints':[str(b_) for b_ in merged],
     'cells':[[str(a_),str(b_)] for a_,b_ in cells],'nodes':[]}
print(len(cells),'Zellen',len(nodes),'Knoten',flush=True)
t0=time.time()
for i,(x,w) in enumerate(nodes):
    hg=h_gamma(psi,x,g); sv=s_shift(psi,x,g); pv=psi(x)
    out['nodes'].append({'x':str(x),'w':str(w),'psi':str(pv),'H_gamma_psi':str(hg),'S_psi':str(sv),'Q_raw':str(hg-g['kappa']*pv-sv)})
    if i%48==0: print(i,len(nodes),'%.0fs'%(time.time()-t0),flush=True)
json.dump(out,open(f'MESHH_{par}_{direction}.json','w'))
print('done',time.time()-t0)
