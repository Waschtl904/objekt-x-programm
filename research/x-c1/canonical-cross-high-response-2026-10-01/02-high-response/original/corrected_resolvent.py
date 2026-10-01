"""Finite low+response-image candidates, certified by complete L2 residuals."""
from pathlib import Path
import argparse,gzip,hashlib,json,subprocess
import flint
from flint import arb,arb_mat,acb,acb_mat,ctx
from high_common import *
from full_residual import norm_certificates

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--capture',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
 p.add_argument('--resume-assembly',type=Path);p.add_argument('--resume-candidates',type=Path)
 args=p.parse_args();ctx.prec=1024;assert flint.__version__=='0.9.0';repo=args.repo.resolve()
 cap=json.loads(gzip.decompress(args.capture.read_bytes()));name=cap['chamber'];pin=cap['main'];key=name+'-odd';sources={}
 git=['git','-c','safe.directory='+repo.as_posix(),'-c','core.longpaths=true','-C',str(repo)]
 assert subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()==pin
 def read(rel):
  raw=(repo/rel).read_bytes();assert raw==subprocess.check_output(git+['show',pin+':'+rel]);sources[rel]=hashlib.sha256(raw).hexdigest()
  return json.loads(gzip.decompress(raw) if rel.endswith('.gz') else raw)
 base='research/x-c1/chambers-through-a11-2026-09-28/'+name.lower()+'/'
 data=read(base+name.lower()+'_model.json.gz');receipt=read(base+'reserve_results.json');fam='research/x-c1/renewable-low-schur-spectral-2026-09-29/'
 trial=read(fam+'07-canonical-extension-outer-mass/primary.json')['trials'][key]
 vec=read(fam+'05-canonical-spectral-ranks/fixed_vectors.json')
 assert sources==cap['source_sha256']
 N=data['cutoff'];lowdegrees=list(range(3,N+1,2));highdegrees=cap['high_degrees'];degrees=lowdegrees+highdegrees;n=len(lowdegrees);h=len(highdegrees);K=degrees[-1]
 selected=[j-1 for j in cap['selected_trial_columns']];rank=trial['rank'];s=len(selected)
 a=arb(3).log() if name=='A9' else arb(11).log()/2
 fullv=arb_mat([[rat(vec[key+'-'+str(j+1)]['coefficients'][i]) for j in range(rank)] for i in range(n)])*mat(trial['orthogonalizer'])
 v=arb_mat([[fullv[i,j] for j in selected] for i in range(n)]);v0=v.mid()
 source_error=[(2*normcol(acb_mat(v-v0),j)).upper() for j in range(s)]
 me=arb(3).sqrt()*moment(a,1);tv=arb_mat([[arb(2*d+1).sqrt()*moment(a,d)/me] for d in degrees]);tl=arb_mat([[tv[i,0]] for i in range(n)])
 # Use response images when no tiny initial Legendre block captures the whole response.
 responses=cmat(cap['high_model_coefficients']);basis=[];basis_proposals=[]
 for col in range(responses.ncols()):
  for part in ('real','imag'):
   raw=[getattr(responses[i,col],part).mid() for i in range(h)]
   initial=sum((x*x for x in raw),arb(0)).sqrt()
   if initial<rat('1e-30'):continue
   b=[x/initial for x in raw]
   for _ in range(2):
    for prev in basis:
     dot=sum((x*y for x,y in zip(b,prev)),arb(0));b=[x-dot*y for x,y in zip(b,prev)]
   length=sum((x*x for x in b),arb(0)).sqrt()
   if length>rat('1e-8'):
    basis.append([(x/length).mid() for x in b]);basis_proposals.append([col,part,iv(length)])
 r=len(basis);assert 1<=r<=2*responses.ncols()
 W=arb_mat([[basis[j][i] for j in range(r)] for i in range(h)])
 print(name,'response image correction dimension',r,'on',h,'high modes',flush=True)
 T=arb_mat([[int(i==j) if j<n else (W[i-n,j-n] if i>=n else 0) for j in range(n+r)] for i in range(n+h)])
 assert all(abs((W.transpose()*W)[i,j]-int(i==j))<rat('1e-50') for i in range(r) for j in range(r))
 qW=acb_mat(K+1,r);th=arb_mat([[tv[n+i,0]] for i in range(h)]);carrier=-th.transpose()*W
 for j in range(r):qW[1,j]=arb(3).sqrt()*carrier[0,j]
 for i,d in enumerate(highdegrees):
  for j in range(r):qW[d,j]=arb(2*d+1).sqrt()*W[i,j]
 if args.resume_assembly:
  cached=json.loads(gzip.decompress(args.resume_assembly.read_bytes()));assert cached['sources']==sources
  cross=mat(cached['cross']);high=mat(cached['high'])
 elif args.resume_candidates:
  cross=arb_mat(n,r);high=arb_mat(r,r)
 else:
  raw=finite_action(qW,data['Gamma_polynomial_coefficients'],a,name,[1]+degrees,lambda st:print(name,st,flush=True))
  projected=real(acb_mat([[raw[i+1,j]-tv[i,0]*raw[0,j] for j in range(r)] for i in range(n+h)]))
  cross=arb_mat([[projected[i,j] for j in range(r)] for i in range(n)])
  high=W.transpose()*arb_mat([[projected[n+i,j] for j in range(r)] for i in range(h)])
 assert all((high[i,j]-high[j,i]).contains(0) for i in range(r) for j in range(r))
 low=mat(data['parities']['odd']['A'],10**100)
 L=arb_mat([[low[i,j] if i<n and j<n else cross[i,j-n] if i<n else cross[j,i-n] if j<n else high[i-n,j-n] for j in range(n+r)] for i in range(n+r)])
 physicalg=eye(n+h)+tv*tv.transpose();G=T.transpose()*physicalg*T
 V0=arb_mat([[v0[i,j] if i<n else 0 for j in range(s)] for i in range(n+h)])
 rhs=T.transpose()*physicalg*V0
 if not args.resume_candidates:
  args.out.with_name(args.out.stem+'.assembly.gz').write_bytes(gzip.compress(json.dumps({'cross':[[iv(cross[i,j]) for j in range(r)] for i in range(n)],'high':[[iv(high[i,j]) for j in range(r)] for i in range(r)],'sources':sources}).encode(),mtime=0))
  print(name,'Galerkin cross/high maximum radius',max(float(x.rad()) for x in cross.entries()+high.entries()),flush=True)
 cached_solutions=None
 if args.resume_candidates:
  fixed=json.loads(gzip.decompress(args.resume_candidates.read_bytes()));assert fixed['sources']==sources
  assert mat(fixed['basis'])==W
  cached_solutions=[cmat(x) for x in fixed['solutions']]
 xs=[];zs=[]
 for k in range(4):
  ang=arb.pi()*(2*k+1)/8;z=acb(ang.cos()/300,ang.sin()/300)
  # Any point candidate is permitted: only the subsequent full residual
  # certifies an actual resolvent. Input interval invertibility is unnecessary.
  zp=acb(z.real.mid(),z.imag.mid())
  sol=cached_solutions[k] if cached_solutions is not None else point((acb_mat(L.mid())-acb_mat(G.mid())*zp).solve(acb_mat(rhs.mid()),algorithm='precond'))
  xs.append(sol);zs.append(z);print(name,'coupled candidate pole',k+1,flush=True)
 args.out.with_name(args.out.stem+'.candidates.gz').write_bytes(gzip.compress(json.dumps({'basis':[[iv(W[i,j]) for j in range(r)] for i in range(h)],'solutions':[cmi(x) for x in xs],'sources':sources}).encode(),mtime=0))
 # The candidate solves stay at 1024 bits. The existing terminal integral
 # precision (3072) is used for new high-degree logarithmic squared norms.
 ctx.prec=3072;a=arb(3).log() if name=='A9' else arb(11).log()/2
 me=arb(3).sqrt()*moment(a,1);tv=arb_mat([[arb(2*d+1).sqrt()*moment(a,d)/me] for d in degrees])
 normalized=acb_mat([[sum((T[i,l]*xs[k][l,j] for l in range(n+r)),acb(0)) for k in range(4) for j in range(s)] for i in range(n+h)])
 w=acb_mat(K+1,4*s);u=acb_mat(K+1,4*s)
 wcarrier=-acb_mat(tv.transpose())*normalized
 for c in range(4*s):
  j=c%s;w[1,c]=arb(3).sqrt()*wcarrier[0,c]
  u[1,c]=-arb(3).sqrt()*sum((tv[i,0]*v0[i,j] for i in range(n)),arb(0))
  for i,d in enumerate(degrees):
   w[d,c]=arb(2*d+1).sqrt()*normalized[i,c]
   if i<n:u[d,c]=arb(2*d+1).sqrt()*v0[i,j]
 poles=[acb((arb.pi()*(2*k+1)/8).cos()/300,(arb.pi()*(2*k+1)/8).sin()/300) for k in range(4)]
 records=norm_certificates(w,u,[z for z in poles for j in range(s)],data['Gamma_polynomial_coefficients'],a,name,lambda st:print(name,st,flush=True))
 theta=rat(trial['physical_trial_max_Rayleigh_upper_exact']);nu=rat(trial['physical_complement_gap_lower_exact']);t=rat('1/300')
 delta=max(((theta/t)**8/(1+(theta/t)**8)).upper(),(1/(1+(nu/t)**8)).upper())
 error=[delta for j in range(s)];total=arb_mat(n+h,s);gamma_error=rat(receipt['Gamma_operator_error_exact']);physicalg=eye(n+h)+tv*tv.transpose()
 def dist(z,b):return abs(z-b).lower()
 for k,z in enumerate(poles):
  assert z.real>theta or z.real<0
  dz=min(dist(z,theta) if z.real>theta else dist(z,arb(0)),dist(z,nu));assert dz>0
  x=acb_mat([[normalized[i,k*s+j] for j in range(s)] for i in range(n+h)])
  gr=real(x).transpose()*physicalg*real(x)+imag(x).transpose()*physicalg*imag(x)
  for j in range(s):
   rec=records[k*s+j];model=rat(rec['complete_model_residual_upper'])
   ge=(gamma_error*gr[j,j].upper().sqrt()).upper();rho=(model+ge+source_error[j]).upper()
   term=(2*abs(z).upper()/8*rho/dz).upper();error[j]=(error[j]+term).upper()
   rec.update(pole=k,trial_column=selected[j]+1,Gamma_model_error_upper=exact(ge,False),source_rounding_error_upper=exact(source_error[j],False),full_physical_residual_upper=exact(rho,False),spectral_distance_lower=exact(dz),filter_error_contribution_upper=exact(term,False))
  total+=real(x*(-z/8))*2
 gram=total.transpose()*physicalg*total
 result={'stage':'HIGH_CORRECTED_RESOLVENT','main':pin,'chamber':name,'selected_trial_columns':[j+1 for j in selected],
  'candidate_bits':1024,'full_integral_bits':3072,'flint':flint.__version__,'source_sha256':sources,'capture_sha256':hashlib.sha256(args.capture.read_bytes()).hexdigest(),
  'high_modes':h,'high_last_degree':K,'correction_dimension':r,'basis_proposals':basis_proposals,'full_residual_records':records,
  'scalar_filter_error_upper':exact(delta,False),'projected_column_error_upper':[exact(x,False) for x in error],
  'projected_norm_upper':[exact(gram[j,j].upper().sqrt(),False) for j in range(s)],
  'degrees':degrees,'projected_normalized_coefficients':[[iv(total[i,j]) for j in range(s)] for i in range(n+h)],
  'source_low_coefficients':[[iv(v[i,j]) for j in range(s)] for i in range(n)],
  'full_high_space_paid':True,'finite_solve_is_candidate_only':True,'A13_inputs_used':False}
 assert not args.out.exists();args.out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
 print(name,'corrected projector error upper',[float(x) for x in error],flush=True)
if __name__=='__main__':main()
