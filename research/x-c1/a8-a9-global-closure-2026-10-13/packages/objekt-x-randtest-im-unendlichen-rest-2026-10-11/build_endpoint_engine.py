from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
s=(ROOT/'work/galerkin84-2026-10-10/compute_galerkin84.py').read_text(encoding='utf-8')
s=s[:s.index('# Batched complete integrals.')]
s=s.replace('ROOT=HERE.parents[1]',"ROOT=Path(sys.argv[sys.argv.index('--root')+1]).resolve()")
s=s.replace('from bounded_moments import Moments',"sys.path.insert(0,str(ROOT/'work/galerkin84-2026-10-10'))\nfrom bounded_moments import Moments")
s=s.replace("ap.add_argument('--bits'","ap.add_argument('--root',type=Path,required=True)\nap.add_argument('--cut-power',type=int,default=14)\nap.add_argument('--bits'")
s=s.replace('NC=92','NC=93\nNLOC=104')
s=s.replace('pol=legendre(544)','pol=legendre(544)\newidth=h/2**args.cut_power\nbumpedge=a+ewidth\namplitude=1/(2*ewidth).sqrt()\ncutlocal=-1+2*ewidth/h')
start=s.index('Rmid=arb_mat(');end=s.index("definition=",start)
s=s[:start]+'''frozenpath=ROOT/f'work/galerkin84-2026-10-10/MODEL_RAY_{args.parity.upper()}_3072.json'
bindings['frozen_J']=hashlib.sha256(frozenpath.read_bytes()).hexdigest()
frozen=read(frozenpath)['working_basis_midpoints_rational']
Rmid=ratmat(frozen)
rounding=norm_bound(YL-Rmid)
savedY=ratmat(data['centres']['Y_local_rational_midpoints'])
Yrounding=norm_bound(Yfull-savedY)
assert rounding<af('1e-60') and Yrounding<af('1e-60')
stepcoeff=[h*amplitude*((2*n+1)/(2*h)).sqrt()*pint(pol[n],arb(-1),cutlocal) for n in range(NLOC)]
# Keep one fixed dyadic polynomial centre; all 104 projection errors are paid.
stepmid=[x.mid() for x in stepcoeff]
stepround=sum((abs(x-y).upper()**2 for x,y in zip(stepcoeff,stepmid)),arb(0)).sqrt()
assert stepround<af('1e-200')
Ymid=arb_mat([[Rmid[i,j] if i<96 and j<84 else savedY[i,j-84] if i<96 and j<92 and j>=84 else -stepmid[i] if j==92 else arb(0) for j in range(NC)] for i in range(NLOC)])
''' +s[end:]
s=s.replace("definition='J=Q[D;I84], D=-(S_top^T)^-1 S_bottom^T; plus eight fixed source models for calibration'","definition='J84,Y8, then normalized endpoint step minus its full degree<104 projection; exact W_X projection is enclosed separately'")
s=s.replace('for k in range(96)),arb_poly([]))','for k in range(NLOC)),arb_poly([]))')
s=s.replace('assert Ynorm<12','assert Ynorm<14')
s=s.replace('lam=[d*pint(f*shell_m,arb(-1),arb(1)) for f in Ylocal]',"lam=[d*pint(f*shell_m,arb(-1),arb(1)) for f in Ylocal]\nlam[92]+=amplitude*2*((bumpedge/2).sinh()-(a/2).sinh()) if p==0 else amplitude*2*((bumpedge/2).cosh()-(a/2).cosh())")
s=s.replace("mom=Moments(roots,1100)",'''roots['bumpouter']=bumpedge/a;roots['minus_bumpouter']=-bumpedge/a
# Add all new prime-shift discontinuities of the narrow step. Old endpoints
# remain named exactly, so no numerical equality is used for old cuts.
ends=['zero']+[lo for lo,hi in cells if lo!='zero']+['one']
for q in [2,3,4,5,7,8]:
    for sign in [-1,1]:
        for endsign in [-1,1]:
            x=(endsign*bumpedge-sign*arb(q).log())/a
            if x>0 and x<1:
                name=f'bumpcut{q}_{sign}_{endsign}';roots[name]=x;ends.append(name)
ends.sort(key=lambda key:float(roots[key].mid()))
assert all(roots[x]<roots[y] for x,y in zip(ends[:-1],ends[1:]))
cells=list(zip(ends[:-1],ends[1:]));mom=Moments(roots,2000)''')
s=s.replace('ym=[pint(f*arb_poly([0]*k+[1]),a,b) for k in range(225)]',"ym=[pint(f*arb_poly([0]*k+[1]),a,b)+(amplitude*(bumpedge**(k+1)-a**(k+1))/(k+1) if j==92 else 0) for k in range(225)]")
s=s.replace('total=add_function(sing,qm,-lam[j]/mu)',"if j==92:\n        for key,weight in [('bumpouter',-1),('one',1),('minus_bumpouter',-((-1)**p)),('minus_one',(-1)**p)]:\n            sing[key]=sing.get(key,arb_poly([]))+arb_poly([amplitude*weight/2])\n    total=add_function(sing,qm,-lam[j]/mu)")
s=s.replace('shifts.append((primepart-qmshift[ci]*(lam[j]/mu))*(2*a).sqrt())',"if j==92:\n            for q,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]:\n                sh=arb(q).log();w=arb(prime).log()/arb(q).sqrt()\n                for sign in [-1,1]:\n                    at=mid+sign*sh\n                    if at>a and at<bumpedge:primepart-=arb_poly([amplitude*w])\n                    elif at>-bumpedge and at<-a:primepart-=arb_poly([amplitude*w*((-1)**p)])\n        shifts.append((primepart-qmshift[ci]*(lam[j]/mu))*(2*a).sqrt())")
s+='\n'+(HERE/'endpoint_tail.py').read_text(encoding='utf-8')
(HERE/'compute_endpoint.py').write_text(s,encoding='utf-8')
print('Endpoint source engine generated')
