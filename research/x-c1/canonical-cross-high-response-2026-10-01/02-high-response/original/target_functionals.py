"""Only Y58/Y68: physical polynomial overlaps plus full projector errors."""
from pathlib import Path
import argparse,gzip,hashlib,json
from flint import arb,arb_mat,ctx
from high_common import *

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--a9',type=Path,required=True);p.add_argument('--a11',type=Path,required=True);p.add_argument('--previous',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();ctx.prec=1024
 old=json.loads(a.previous.read_bytes());aa=json.loads(gzip.decompress(a.a9.read_bytes()));bb=json.loads(gzip.decompress(a.a11.read_bytes()))
 assert aa['main']==bb['main']==old['main'] and aa['full_high_space_paid'] and bb['full_high_space_paid']
 source={**old['source_sha256'],**aa['source_sha256'],**bb['source_sha256']}
 fam='research/x-c1/renewable-low-schur-spectral-2026-09-29/07-canonical-extension-outer-mass/primary.json'
 raw=(a.repo/fam).read_bytes();assert hashlib.sha256(raw).hexdigest()==source[fam];outer=json.loads(raw)
 A=arb(3).log();B=arb(11).log()/2;ratio=A/B
 count=(aa['high_last_degree']+bb['high_last_degree']+2)//2
 nodes=[arb.legendre_p_root(count,k,weight=True) for k in range(count)]
 def samples(data,endpoint,xs,source_basis=False):
  co=mat(data['source_low_coefficients'] if source_basis else data['projected_normalized_coefficients']);degrees=data['degrees'][:co.nrows()];N=degrees[-1];me=arb(3).sqrt()*moment(endpoint,1)
  tv=arb_mat([[arb(2*d+1).sqrt()*moment(endpoint,d)/me] for d in degrees]);carrier=-tv.transpose()*co
  polys=arb_mat([[seq[d]*arb(2*d+1).sqrt() for d in [1]+degrees] for seq in (values(x,N) for x in xs)])
  coeff=arb_mat([[carrier[0,j] for j in range(co.ncols())]]+[[co[i,j] for j in range(co.ncols())] for i in range(co.nrows())])
  return polys*coeff
 av=samples(aa,A,[x for x,w in nodes]);bv=samples(bb,B,[ratio*x for x,w in nodes])
 def overlap(x,y):return x.transpose()*arb_mat([[y[i,j]*ratio.sqrt()*nodes[i][1]/2 for j in range(y.ncols())] for i in range(y.nrows())])
 kp=overlap(av,bv)
 ua=samples(aa,A,[x for x,w in nodes],True);ub=samples(bb,B,[ratio*x for x,w in nodes],True)
 identity=overlap(ua,ub)-overlap(ua-av,ub)-overlap(ua,ub-bv)+overlap(ua-av,ub-bv)-kp
 assert all(x.contains(0) for x in identity.entries())
 SA=mat(outer['trials']['A9-odd']['physical_Ritz_matrix']);SB=mat(outer['trials']['A11-odd']['physical_Ritz_matrix'])
 targets={};ken=old['K_direct_enclosure'];yen=old['Y_direct_enclosure']
 for col,i in enumerate((4,5)):
  ea=rat(aa['projected_column_error_upper'][col]);eb=rat(bb['projected_column_error_upper'][0]);va=rat(aa['projected_norm_upper'][col]);vb=rat(bb['projected_norm_upper'][0])
  kr=min((ea*vb+eb).upper(),(ea+eb*va).upper());energy=(SA[i,i].upper()*SB[7,7].upper()).sqrt()/17;yr=(kr+energy).upper()
  kc=iv(kp[col,0]+arb(0,kr));yc=iv(kp[col,0]+arb(0,yr));assert kp[col,0].rad()<rat('1e-20')
  def intersect(x,y):
   lo=max(F(x[0]),F(y[0]));hi=min(F(x[1]),F(y[1]));assert lo<=hi;return [str(lo),str(hi)]
  kn=intersect(ken[i][7],kc);yn=intersect(yen[i][7],yc)
  targets['Y'+str(i+1)+'8']={'polynomial_K':iv(kp[col,0]),'K_error_upper':exact(kr,False),'energy_conversion_error_upper':exact(energy,False),'direct_Y':yc,'previous_Y':yen[i][7],'intersected_Y':yn,'strictly_improved':yn!=yen[i][7]}
  ken[i][7]=kn;yen[i][7]=yn
  print('Y'+str(i+1)+'8','center',float(kp[col,0].mid()),'radius',float(yr),'improved',targets['Y'+str(i+1)+'8']['strictly_improved'],flush=True)
 report={'status':'EXPLORATORY_RIGOROUS_ENCLOSURES_NOT_GATE_ACCEPTANCE','stage':'HIGH_RESPONSE_CORRECTED_TARGETS','main':aa['main'],'source_sha256':source,
  'input_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (a.a9,a.a11,a.previous)},'targets':targets,'K_direct_enclosure':ken,'Y_direct_enclosure':yen,
  'joint_residual_identity_checked':True,'full_high_response_paid':True,'A13_inputs_used':False,'actual_odd_angle_certified':False,'quadrature_nodes':count}
 a.out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
