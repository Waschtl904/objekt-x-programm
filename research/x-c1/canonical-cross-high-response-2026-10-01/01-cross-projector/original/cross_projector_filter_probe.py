"""Post-integration exploratory enclosure; no GREEN classification by this script.

Butterworth rational spectral filter, eight complex conjugate poles. All
candidate solves are certified by full physical residuals; no finite tail
truncation is substituted for the actual operator. Run only after the
negative block and its registry have both been integrated.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, gzip, hashlib, json, subprocess, sys, time
sys.path.insert(0,str(Path(__file__).resolve().parent/'publication-deps'))
import flint
from flint import arb, arb_mat, acb, acb_mat, ctx

p=argparse.ArgumentParser()
p.add_argument('--repo',type=Path,required=True);p.add_argument('--main',required=True)
p.add_argument('--out',type=Path,required=True);p.add_argument('--bits',type=int,default=1024)
a=p.parse_args();assert a.bits>=1024,'Polynomial overlap recurrence needs at least 1024 bits';ctx.prec=a.bits;assert flint.__version__=='0.9.0'
repo=a.repo.resolve();git=['git','-c','safe.directory='+repo.as_posix(),'-C',str(repo)]
assert subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()==a.main
state=json.loads((repo/'00-uebersicht/RESEARCH_STATE.yaml').read_bytes())
assert not state['pending_packages'] and any(r['id']=='CANONICAL-ODD-BOX-STRUCTURAL-OPEN' and r['integration_status']=='MERGED' for r in state['results'])
assert not a.out.exists()
sys.path.insert(0,str(repo/'research/x-c1/canonical-schur-coupling-2026-09-30/02-resolvent-moments'))
from resolvent_moments import rat, mat, eye, exact, iv, mi, square_bounds, nonnegative_upper
sys.path.insert(0,str(repo/'research/x-c1/renewable-low-schur-spectral-2026-09-29/07-canonical-extension-outer-mass'))
from outer_mass_bounds import legendre
family='research/x-c1/renewable-low-schur-spectral-2026-09-29/'
sources={}
def read(rel,zipped=False):
 raw=(repo/rel).read_bytes();assert raw==subprocess.check_output(git+['show',a.main+':'+rel])
 sources[rel]=hashlib.sha256(raw).hexdigest()
 return json.loads(gzip.decompress(raw) if zipped else raw)
outer=read(family+'07-canonical-extension-outer-mass/primary.json')
vec=read(family+'05-canonical-spectral-ranks/fixed_vectors.json')
def realpart(m):return arb_mat([[m[i,j].real for j in range(m.ncols())] for i in range(m.nrows())])
def imagpart(m):return arb_mat([[m[i,j].imag for j in range(m.ncols())] for i in range(m.nrows())])
def colnorm(m,j):return sum((abs(m[i,j]).upper()**2 for i in range(m.nrows())),arb(0)).sqrt().upper()
def cpoint(m):return acb_mat([[acb(m[i,j].real.mid(),m[i,j].imag.mid()) for j in range(m.ncols())] for i in range(m.nrows())])
def distance(z,x):
 re=z.real-x;im=z.imag
 return (square_bounds(re)[0]+square_bounds(im)[0]).sqrt().lower()
def diag_upper(g,j):return nonnegative_upper(g[j,j])
cache={};results={};t=rat('1/300');degree=8
for name in ('A9','A11'):
 start=time.time();key=name+'-odd';trial=outer['trials'][key];rank=trial['rank']
 base='research/x-c1/chambers-through-a11-2026-09-28/'+name.lower()+'/'
 model=read(base+name.lower()+'_model.json.gz',True);receipt=read(base+'reserve_results.json')
 degrees=list(range(3,model['cutoff']+1,2));n=len(degrees)
 v=arb_mat([[rat(vec[key+'-'+str(j+1)]['coefficients'][i]) for j in range(rank)] for i in range(n)])*mat(trial['orthogonalizer'])
 endpoint=mat([[model['endpoint_interval']]],10**100)[0,0]
 me=arb(3).sqrt()*mat([[model['raw_low_moments'][1]]],10**100)[0,0]
 tl=arb_mat([[arb(2*d+1).sqrt()*mat([[model['raw_low_moments'][d]]],10**100)[0,0]/me] for d in degrees])
 g=eye(n)+tl*tl.transpose();low=mat(model['parities']['odd']['A'],10**100)
 unit=v.transpose()*g*v
 assert all(unit[i,j].contains(int(i==j)) for i in range(rank) for j in range(rank))
 el=rat(receipt['low_form_error_exact']);eb=rat(receipt['parities']['odd']['coupling_operator_error_exact'])
 hup=mat(model['parities']['odd']['complete_model_raw_high_Gram'],10**100)*rat('1001/1000')+eye(n)*(1001*eb*eb)
 rho=((endpoint.sinh()/endpoint-1)/2)/(me*me)
 tail2=nonnegative_upper(rho-1-(tl.transpose()*tl)[0,0]);tail=tail2.sqrt().upper()
 theta=rat(trial['physical_trial_max_Rayleigh_upper_exact']);nu=rat(trial['physical_complement_gap_lower_exact'])
 assert 0<theta<t<nu
 delta=max(((theta/t)**degree/(1+(theta/t)**degree)).upper(),(1/(1+(nu/t)**degree)).upper())
 total=arb_mat(n,rank);error=[delta for j in range(rank)];solves=[]
 for k in range(degree//2):
  ang=arb.pi()*F(2*k+1,degree).numerator/F(2*k+1,degree).denominator
  z=acb(t*ang.cos(),t*ang.sin());assert z.imag>0 and z.real<nu
  dl=distance(z,theta) if z.real>theta else distance(z,arb(0))
  # No pole straddles a critical interval endpoint at this fixed design.
  assert z.real>theta or z.real<0
  dist=min(dl,distance(z,nu));assert dist>0
  x=cpoint((acb_mat(low)-acb_mat(g)*z).solve(acb_mat(g*v),algorithm='precond'))
  residual=acb_mat(g*v)-(acb_mat(low)-acb_mat(g)*z)*x
  xr,xi=realpart(x),imagpart(x)
  hg=xr.transpose()*hup*xr+xi.transpose()*hup*xi
  masshigh=acb_mat(tl.transpose())*(acb_mat(v)+x*z)
  records=[]
  for j in range(rank):
   lowerr=(colnorm(residual,j)+el*colnorm(x,j)).upper()
   coupling=diag_upper(hg,j).sqrt().upper();masserr=(tail*abs(masshigh[0,j]).upper()).upper()
   higherr=(coupling+masserr).upper();rr=(lowerr**2+higherr**2).sqrt().upper()
   term=(2*abs(z).upper()/degree*rr/dist).upper();error[j]=(error[j]+term).upper()
   records.append({'low_residual_upper':exact(lowerr,False),'high_coupling_upper':exact(coupling,False),
    'high_mass_upper':exact(masserr,False),'filter_error_contribution_upper':exact(term,False)})
  total+=realpart(x*(-z/degree))*2
  solves.append({'pole_real':iv(z.real),'pole_imag':iv(z.imag),'spectral_distance_lower':exact(dist),'columns':records})
  print(key,'pole',k+1,'of',degree//2,'certified',flush=True)
 gram=total.transpose()*g*total;rescoef=v-total;rgram=rescoef.transpose()*g*rescoef
 cache[name]={'A':endpoint,'pi':1,'degrees':degrees,'N':model['cutoff'],'rank':rank,'v':v,'p':total,'r':rescoef,'tl':tl,
  'error':error,'pnorm':[diag_upper(gram,j).sqrt().upper() for j in range(rank)],
  'rnorm':[diag_upper(rgram,j).sqrt().upper() for j in range(rank)],'s':mat(trial['physical_Ritz_matrix'])}
 results[name]={'critical_upper':exact(theta,False),'high_lower':exact(nu),'filter_degree':degree,
  'filter_scale':str(F(1,300)),'scalar_filter_error_upper':exact(delta,False),
  'projected_column_error_upper':[exact(e,False) for e in error],
  'solves':solves}
 print(key,'projector column error upper',[float(x) for x in error],flush=True)

aa,bb=cache['A9'],cache['A11'];ratio=aa['A']/bb['A'];count=max(aa['N'],bb['N'])+1
print('Joint polynomial overlaps at',count,'Gauss nodes',flush=True)
nodes=[arb.legendre_p_root(count,k,weight=True) for k in range(count)]
def values(c,points,which):
 co=c[which];carrier=-c['tl'].transpose()*co
 pol=arb_mat([[seq[d]*arb(2*d+1).sqrt() for d in [1]+c['degrees']] for seq in (legendre(x,c['N']) for x in points)])
 coeff=arb_mat([[carrier[0,j] for j in range(c['rank'])]]+[[co[i,j] for j in range(c['rank'])] for i in range(co.nrows())])
 return pol*coeff
av={which:values(aa,[q[0] for q in nodes],which) for which in ('v','p','r')}
bv={which:values(bb,[ratio*q[0] for q in nodes],which) for which in ('v','p','r')}
w=[ratio.sqrt()*q[1]/2 for q in nodes]
def overlap(x,y):return x.transpose()*arb_mat([[y[i,j]*w[i] for j in range(y.ncols())] for i in range(y.nrows())])
raw=overlap(av['v'],bv['v']);kp=overlap(av['p'],bv['p'])
recorded_raw=mat(outer['results']['A9->A11-odd']['trial_overlap'])
assert all(raw[i,j].overlaps(recorded_raw[i,j]) for i in range(aa['rank']) for j in range(bb['rank']))
ma=overlap(av['r'],bv['v']);mb=overlap(av['v'],bv['r']);cc=overlap(av['r'],bv['r'])
identity=raw-ma-mb+cc-kp
assert all(x.contains(0) for x in identity.entries())
assert all(x.rad()<rat('1e-20') for matrix in (raw,kp,ma,mb,cc) for x in matrix.entries()),'Polynomial overlap enclosures too wide; increase arithmetic precision'
targets={}
kenclosure=arb_mat(aa['rank'],bb['rank']);yenclosure=arb_mat(aa['rank'],bb['rank'])
for i in range(aa['rank']):
 for j in range(bb['rank']):
  ea,eb=aa['error'][i],bb['error'][j]
  kr=min(ea*bb['pnorm'][j]+eb,ea+eb*aa['pnorm'][i]).upper()
  yr=(kr+(aa['s'][i,i].upper()*bb['s'][j,j].upper()).sqrt()/17).upper()
  kenclosure[i,j]=kp[i,j]+arb(0,kr)
  yenclosure[i,j]=kp[i,j]+arb(0,yr)
for i in (4,5):
 j=7;ea,eb=aa['error'][i],bb['error'][j]
 kr=min(ea*bb['pnorm'][j]+eb,ea+eb*aa['pnorm'][i]).upper()
 yr=(kr+(aa['s'][i,i].upper()*bb['s'][j,j].upper()).sqrt()/17).upper()
 cr=(ea*bb['rnorm'][j]+eb*aa['rnorm'][i]+ea*eb).upper()
 targets['Y'+str(i+1)+'8']={'K_approx':iv(kp[i,j]),'K_error_upper':exact(kr,False),
  'Y_direct_enclosure':iv(kp[i,j]+arb(0,yr)),
  'mixed_A_enclosure':iv(ma[i,j]+arb(0,ea)),
  'mixed_B_enclosure':iv(mb[i,j]+arb(0,eb)),
  'cross_residual_enclosure':iv(cc[i,j]+arb(0,cr))}
 print('Y'+str(i+1)+'8','center',float(kp[i,j].mid()),'radius',float(yr),flush=True)
report={'status':'EXPLORATORY_RIGOROUS_ENCLOSURES_NOT_GATE_ACCEPTANCE','main':a.main,'bits':a.bits,'flint':flint.__version__,
 'source_sha256':sources,'filter':'1/(1+(lambda/t)^8), four conjugate pairs','results':results,
 'targets':targets,'K_direct_enclosure':mi(kenclosure),'Y_direct_enclosure':mi(yenclosure),
 'quadrature_nodes':count,'joint_residual_identity_checked':True,'published_unfiltered_overlap_crosscheck':True,
 'A13_inputs_used':False,'full_high_response_paid':True,'actual_odd_angle_certified':False}
a.out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
