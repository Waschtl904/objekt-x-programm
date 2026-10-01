"""Stage 0: complete-Gram-normalized directional capture diagnostic."""
from pathlib import Path
import argparse,gzip,hashlib,json,subprocess,time
import flint
from flint import arb,arb_mat,acb,acb_mat,ctx
from high_common_capture import *

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
 p.add_argument('--chamber',choices=['A9','A11'],required=True);p.add_argument('--count',type=int,default=128)
 p.add_argument('--resume-low',type=Path)
 args=p.parse_args();ctx.prec=1024;assert flint.__version__=='0.9.0'
 repo=args.repo.resolve();pin='6302a47cab2132f0d87dec29bbf21d7ce98e8f75';sources={}
 git=['git','-c','safe.directory='+repo.as_posix(),'-c','core.longpaths=true','-C',str(repo)]
 assert subprocess.check_output(git+['rev-parse','HEAD']).decode().strip()==pin
 def read(rel):
  raw=(repo/rel).read_bytes();assert raw==subprocess.check_output(git+['show',pin+':'+rel]);sources[rel]=hashlib.sha256(raw).hexdigest()
  return json.loads(gzip.decompress(raw) if rel.endswith('.gz') else raw)
 name=args.chamber;key=name+'-odd';base='research/x-c1/chambers-through-a11-2026-09-28/'+name.lower()+'/'
 data=read(base+name.lower()+'_model.json.gz');receipt=read(base+'reserve_results.json')
 fam='research/x-c1/renewable-low-schur-spectral-2026-09-29/'
 trial=read(fam+'07-canonical-extension-outer-mass/primary.json')['trials'][key]
 vec=read(fam+'05-canonical-spectral-ranks/fixed_vectors.json')
 N=data['cutoff'];degrees=list(range(3,N+1,2));n=len(degrees);rank=trial['rank'];selected=[4,5] if name=='A9' else [7]
 fullv=arb_mat([[rat(vec[key+'-'+str(j+1)]['coefficients'][i]) for j in range(rank)] for i in range(n)])*mat(trial['orthogonalizer'])
 v=arb_mat([[fullv[i,j] for j in selected] for i in range(n)])
 a=arb(3).log() if name=='A9' else arb(11).log()/2
 assert a.overlaps(mat([[data['endpoint_interval']]],10**100)[0,0])
 me=arb(3).sqrt()*moment(a,1)
 for d in [1]+degrees:assert moment(a,d).overlaps(mat([[data['raw_low_moments'][d]]],10**100)[0,0])
 tl=arb_mat([[arb(2*d+1).sqrt()*moment(a,d)/me] for d in degrees])
 g=eye(n)+tl*tl.transpose();low=mat(data['parities']['odd']['A'],10**100)
 gram=mat(data['parities']['odd']['complete_model_raw_high_Gram'],10**100)
 xx=[];poles=[];cached=cmat(json.loads(gzip.decompress(args.resume_low.read_bytes()))['low_candidates']) if args.resume_low else None
 for k in range(4):
  angle=arb.pi()*(2*k+1)/8;z=acb(angle.cos()/300,angle.sin()/300)
  x=acb_mat([[cached[i,k*len(selected)+j] for j in range(len(selected))] for i in range(n)]) if cached is not None else point((acb_mat(low)-acb_mat(g)*z).solve(acb_mat(g*v),algorithm='precond'))
  xx.append(x);poles.append(z)
  print(name,'candidate pole',k+1,flush=True)
 X=acb_mat([[xx[k][i,j] for k in range(4) for j in range(len(selected))] for i in range(n)])
 q=acb_mat(N+1,X.ncols());carrier=-acb_mat(tl.transpose())*X
 for j in range(X.ncols()):q[1,j]=arb(3).sqrt()*carrier[0,j]
 for i,d in enumerate(degrees):
  for j in range(X.ncols()):q[d,j]=arb(2*d+1).sqrt()*X[i,j]
 indices=list(range(N+2,N+2+2*args.count,2))
 h,parts=high_coefficients(q,data['Gamma_polynomial_coefficients'],a,name,indices,lambda s:print(name,s,flush=True))
 total=real(X).transpose()*gram*real(X)+imag(X).transpose()*gram*imag(X)
 checkpoint={'low_candidates':cmi(X),'high_model_coefficients':cmi(h),'full_energies':[iv(total[c,c]) for c in range(total.ncols())],'source_sha256':sources}
 args.out.with_name(args.out.stem+'.checkpoint.gz').write_bytes(gzip.compress(json.dumps(checkpoint).encode(),mtime=0))
 reports=[]
 for k in range(4):
  for jj,j in enumerate(selected):
   c=k*len(selected)+jj;tot=total[c,c];assert tot>0
   captured=[];s=arb(0)
   for ii,degree in enumerate(indices):
    s+=h[ii,c].real*h[ii,c].real+h[ii,c].imag*h[ii,c].imag
    if ii+1 in (8,16,32,64,128,args.count):
     rho=s/tot;assert rho.lower()>=0 and rho.upper()<=1,(name,k,j+1,ii+1,rho,tot,s)
     captured.append({'modes':ii+1,'last_degree':degree,'energy':iv(s),'fraction':iv(rho),'omitted_energy':iv(tot-s)})
   reports.append({'pole':k,'trial_column':j+1,'full_model_energy':iv(tot),'full_model_norm':iv(tot.sqrt()),'captures':captured})
   print(name,'pole',k,'column',j+1,'capture',float((s/tot).mid()),flush=True)
 assert all(abs(v.real.rad())<rat('1e-25') and abs(v.imag.rad())<rat('1e-25') for v in h.entries())
 out={'stage':'CAPTURE_DIAGNOSTIC','main':pin,'bits':1024,'flint':flint.__version__,'chamber':name,'raw_cutoff':N,'selected_trial_columns':[j+1 for j in selected],'high_degrees':indices,'poles':[ci(z) for z in poles],'source_sha256':sources,'reports':reports,'low_candidates':cmi(X),'high_model_coefficients':cmi(h),'quadrature_nodes':parts['quadrature_nodes'],'complete_Gram_used':True,'true_coupling_model_error_upper':receipt['parities']['odd']['coupling_operator_error_exact'],'A13_inputs_used':False}
 assert not args.out.exists();args.out.write_bytes(gzip.compress((json.dumps(out,separators=(',',':'))+'\n').encode(),mtime=0))
if __name__=='__main__':main()
