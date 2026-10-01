"""Locate the remaining full residual beyond the candidate's last degree.

One representative (first upper) pole, all requested trial columns. Complete
potential/shift norms and exact Gamma support are compared to finite Parseval
sums. The joint residual uses the already independently integrated full norm.
"""
from pathlib import Path
import argparse,gzip,hashlib,json
from flint import arb,arb_mat,acb,acb_mat,arb_poly,ctx
from high_common import *
from full_residual import affine_expansion,v2mom,dotpoly,integrate

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--capture',type=Path,required=True);p.add_argument('--corrected',type=Path,required=True);p.add_argument('--candidates',type=Path,required=True);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
 cap=json.loads(gzip.decompress(args.capture.read_bytes()));rec=json.loads(gzip.decompress(args.corrected.read_bytes()));fixed=json.loads(gzip.decompress(args.candidates.read_bytes()))
 assert fixed['sources']==rec['source_sha256']==cap['source_sha256'];sources=rec['source_sha256'];name=rec['chamber'];key=name+'-odd'
 def read(rel):
  raw=(args.repo/rel).read_bytes();assert hashlib.sha256(raw).hexdigest()==sources[rel]
  return json.loads(gzip.decompress(raw) if rel.endswith('.gz') else raw)
 data=read('research/x-c1/chambers-through-a11-2026-09-28/'+name.lower()+'/'+name.lower()+'_model.json.gz')
 fam='research/x-c1/renewable-low-schur-spectral-2026-09-29/';trial=read(fam+'07-canonical-extension-outer-mass/primary.json')['trials'][key];vec=read(fam+'05-canonical-spectral-ranks/fixed_vectors.json')
 ctx.prec=1024;degrees=rec['degrees'];n=(data['cutoff']-1)//2;h=rec['high_modes'];s=len(rec['selected_trial_columns']);rank=trial['rank'];K=degrees[-1]
 fv=arb_mat([[rat(vec[key+'-'+str(j+1)]['coefficients'][i]) for j in range(rank)] for i in range(n)])*mat(trial['orthogonalizer'])
 v0=arb_mat([[fv[i,j-1].mid() for j in rec['selected_trial_columns']] for i in range(n)])
 W=mat(fixed['basis']);sol=cmat(fixed['solutions'][0]);r=W.ncols()
 ctx.prec=3072;a=arb(3).log() if name=='A9' else arb(11).log()/2
 z=acb((arb.pi()/8).cos()/300,(arb.pi()/8).sin()/300)
 nc=acb_mat([[sol[i,j] if i<n else sum((W[i-n,l]*sol[n+l,j] for l in range(r)),acb(0)) for j in range(s)] for i in range(n+h)])
 tv=arb_mat([[arb(2*d+1).sqrt()*moment(a,d)/(arb(3).sqrt()*moment(a,1))] for d in degrees])
 w=acb_mat(K+1,s);u=acb_mat(K+1,s);wc=-acb_mat(tv.transpose())*nc
 for j in range(s):
  w[1,j]=arb(3).sqrt()*wc[0,j];u[1,j]=-arb(3).sqrt()*sum((tv[i,0]*v0[i,j] for i in range(n)),arb(0))
  for i,d in enumerate(degrees):
   w[d,j]=arb(2*d+1).sqrt()*nc[i,j]
   if i<n:u[d,j]=arb(2*d+1).sqrt()*v0[i,j]
 indices=[1]+degrees
 action,parts=finite_action(w,data['Gamma_polynomial_coefficients'],a,name,indices,lambda st:print(name,st,flush=True),return_parts=True)
 residual=acb_mat([[(u[d,j]+z*w[d,j])/arb(2*d+1).sqrt()-action[ii,j] for j in range(s)] for ii,d in enumerate(indices)])
 wp=affine_expansion(w,arb(0),arb(1));v2=v2mom(2*K);Vtotal=[dotpoly(wr*wr+wi*wi,v2) for wr,wi in wp]
 ch=channels(a,name);edges=[arb(0),arb(1)]
 for _,_,d in ch:
  for sign in (-1,1):
   for e in (-1,1):
    v=e-sign*d
    if 0<v<1 and not any(v.overlaps(b) for b in edges):edges.append(v)
 edges.sort(key=lambda x:float(x.mid()));Stotal=[arb(0) for j in range(s)]
 for l,r in zip(edges,edges[1:]):
  mid=(l+r)/2;length=r-l
  for j in range(s):
   sr=arb_poly([]);si=arb_poly([])
   for _,weight,d in ch:
    for sign in (-1,1):
     shift=sign*d
     if -1<mid+shift<1:
      rr,ii=[p(arb_poly([l+shift,length])) for p in wp[j]];sr+=weight*rr;si+=weight*ii
   Stotal[j]+=length*integrate(sr*sr+si*si,arb(0),arb(1))
 ga=parts['gamma_polynomial'];rows=[]
 for j,column in enumerate(rec['selected_trial_columns']):
  rawtotal=ball(rec['full_residual_records'][j]['raw_model_residual_norm_squared'])
  normal=ball(rec['full_residual_records'][j]['normal_removed_model_residual_norm_squared'])
  tail=rawtotal-normsq(residual,j);vtail=Vtotal[j]-normsq(parts['potential'],j);stail=Stotal[j]-normsq(parts['shift'],j)
  gtail=sum(((ga[k,j].real**2+ga[k,j].imag**2)/(2*k+1) for k in range(K+1,ga.nrows())),arb(0))
  def valid(x):
   assert x.lower()>0 and x.rad()<rat('1e-20'),x
   return iv(x)
  assert (tail/normal).upper()<=1
  row={'trial_column':column,'pole':0,'beyond_degree':K,'joint_residual_tail_energy':valid(tail),'fraction_of_normal_removed_residual':iv(tail/normal),
   'potential_tail_energy':valid(vtail),'shift_tail_energy':valid(stail),'Gamma_tail_energy':iv(gtail),
   'joint_tail_norm':iv(tail.sqrt()),'potential_tail_norm':iv(vtail.sqrt()),'shift_tail_norm':iv(stail.sqrt())}
  rows.append(row);print(name,column,'tail fraction',float((tail/normal).mid()),'norms joint,V,S',float(tail.sqrt().mid()),float(vtail.sqrt().mid()),float(stail.sqrt().mid()),flush=True)
 result={'main':rec['main'],'chamber':name,'bits':3072,'rows':rows,'source_sha256':sources,'input_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (args.capture,args.corrected,args.candidates)},'full_infinite_tail_from_Parseval':True,'first_pole_only':True,'A13_inputs_used':False}
 args.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
