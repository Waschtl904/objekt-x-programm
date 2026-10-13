"""Rebuild the common old majorant at a stronger inherited high floor.

The full 96-column comparison is built before any finite elimination.
All three blocks of the old response change together.
"""
from pathlib import Path
from fractions import Fraction as F
import json,sys,gzip,hashlib,math
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/compute-deps'),str(ROOT/'work/galerkin84-2026-10-10'),str(ROOT/'work/tail-probe-2026-10-10/vendor')]
from flint import arb,arb_mat,fmpq,fmpz_mat,ctx
from safe_serial import serial
from compute_inverse_energy_gate import ldl
ctx.prec=768
def af(x):
 q=F(x);return arb(fmpq(q.numerator,q.denominator))
def box(v):return af(v[0]).union(af(v[1]))
def mat(a):return arb_mat([[box(x) for x in r] for r in a])
def rat(a):return arb_mat([[af(x) for x in r] for r in a])
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def sym(a):return (a+a.transpose())/2
def sub(a,ii,jj):return arb_mat([[a[i,j] for j in jj] for i in ii])
def tr(a):return sum((a[i,i] for i in range(a.nrows())),arb(0))
def cat(a,b):return arb_mat([[a[i,j] if j<a.ncols() else b[i,j-a.ncols()] for j in range(a.ncols()+b.ncols())] for i in range(a.nrows())])
def read(p):
 b=p.read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)
def ints(a,den):return arb_mat([[af(F(int(x),den)) for x in r] for r in a])
def down_rational(a,digits=90):
 vals=serial(sym(a),digits);n=len(vals);den=10**digits
 mid=[[sum(map(F,v))/2 for v in r] for r in vals]
 out=[[F(round(mid[i][j]*den),den) for j in range(n)] for i in range(n)]
 for i in range(n):
  radius=sum(max(abs(F(vals[i][j][0])-out[i][j]),abs(F(vals[i][j][1])-out[i][j])) for j in range(n))
  out[i][i]-=F(math.ceil(radius*den),den)
 return [[int(v*den) for v in r] for r in out]
def up_rational(a,digits=90):return [[-v for v in r] for r in down_rational(-a,digits)]
fin=ROOT/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09'
floorpath=fin/'work/high-floor-2026-10-08/check_floor.py'
sys.path.insert(0,str(floorpath.parent));from check_floor import prove
floor=prove();delta=F(18219,10000);oldelta=F(91,50)
raw=F(floor['raw_high_floor']);corrected=raw-16*F(1,10**6)-12*F(1,10**12)
assert corrected==F(floor['moment_corrected_floor_over_raw_norm'])
assert corrected>delta*(1+F(1,10**12)) and delta>oldelta
floorcert={'inherited_floor_proof_sha256':hashlib.sha256(floorpath.read_bytes()).hexdigest(),
 'inherited':floor,'new_physical_high_floor':str(delta),
 'exact_positive_margin':str(corrected-delta*(1+F(1,10**12))),
 'same_high_space_and_operator_hypotheses':True}
(HERE/'REFINED_HIGH_FLOOR.json').write_text(json.dumps(floorcert,indent=2)+'\n')
oldpath=fin/'work/remainder-integration-check-v2/originals/weighted-response/inputs/a8_model.json.gz';old=read(oldpath)
rp=ROOT/'work/directional-bridge-2026-10-11/review-rebuild/BRIDGE_OBSTRUCTION_INPUT.json';rv=read(rp)['cases']
bp=ROOT/'work/inherited/Objekt-X-Unendlicher-Rest-Vergleich-2026-10-09/work/infinite-tail-2026-10-09/FINITE_BRIDGE.json';bridges=read(bp)['cases']
rows=[]
for p,label in enumerate(['EVEN','ODD']):
 cp=fin/f'work/gamma-low-2026-10-09/CERTIFICATE_{label}_gamma224_tight_4096.json';c=read(cp)
 gp=ROOT/f'work/galerkin84-2026-10-10/GALERKIN_{label}_3072.json';g=read(gp)
 dp=HERE/f'DIRECT_REST_{label}_3072.json';d=read(dp);r=rv[p];br=bridges[p+2]
 Fold=ints(c['F_integer_matrix'],int(c['F_denominator']));HBold=ints(c['HB_integer_matrix'],int(c['HB_denominator']))
 coupling_padding=F(1,10**10)
 eB=box(c['old_coupling_error_norm'])
 rawHG=arb_mat([[box(v)/af(10**100) for v in row] for row in old['parities'][label.lower()]['complete_model_raw_high_Gram']])
 HBi=up_rational(rawHG*af(1+coupling_padding)+eye(191)*af(1+1/coupling_padding)*eB**2)
 HB=ints(HBi,10**90)
 Fnewi=down_rational(Fold+HBold/af(oldelta)-HB/af(delta));Fm=ints(Fnewi,10**90)
 lf,ds,fail=ldl(Fm);assert fail is None
 invt=arb_mat(lf).transpose().inv();Cpre=arb_mat([[invt[i,j]/ds[j].sqrt() for j in range(191)] for i in range(191)])
 Ci=[[int((Cpre[i,j].mid()*10**80).floor().unique_fmpz()) if i<=j else 0 for j in range(191)] for i in range(191)]
 product=fmpz_mat(Ci).transpose()*fmpz_mat(Fnewi)*fmpz_mat(Ci);den=10**250
 rn=max(sum(abs(int(product[i,j])-(den if i==j else 0)) for j in range(191)) for i in range(191));rho=F(rn,den);assert rho<F(1,10**40)
 AC=ints(Ci,10**80);X=AC*AC.transpose()/af(1-rho)
 print(label,'new 191D inverse certified; rho',float(rho),flush=True)
 cf=mat(c['source_c_model']);bf=mat(c['source_Bh_model']);cj=mat(g['old_low_c_model']);bj=mat(g['old_low_Bh_model'])
 HGf=mat(c['source_h_gram_model']);HGj=mat(g['H84_model'])*af(oldelta);HGcross=mat(g['complete_source_high_cross_model'])
 HG=arb_mat([[HGf[i,j] if i<12 and j<12 else HGcross[i,j-12] if i<12 else HGcross[j,i-12] if j<12 else HGj[i-12,j-12] for j in range(96)] for i in range(96)])
 vv=cat(cf,cj)-cat(bf,bj)/af(delta);low=AC.transpose()*vv
 U=sym(HG/af(delta)+low.transpose()*low/af(1-rho))
 # New feature-error Gram: the same source/function errors, new inverse metric.
 Ec=mat(c['joint_low_source_error_gram']);Eh=mat(c['joint_high_source_error_gram']);HGfup=rat(c['source_h_gram_upper_rational'])
 Ev=3*(Ec*tr(X)+Eh*tr(X*HB)/af(delta**2)+HGfup*tr(X)*eB**2/af(delta**2))
 EF=sym(Eh/af(delta)+Ev)
 moments=[box(v)/af(10**100) for v in old['raw_low_moments']]
 cn=[af(F(2*n+1,2*p+1)).sqrt()*moments[n]/moments[p] for n in range(p+2,384,2)]
 Gm=eye(191)+arb_mat([[x*y for y in cn] for x in cn])
 ef=box(g['source_model_error_norm']);eh=box(g['high_source_error_norm']);eBj=box(g['old_coupling_error_norm'])
 ELj=3*(tr(X*Gm)*ef**2+tr(X*HB)*eh**2/af(delta**2)+tr(X)*eBj**2*tr(HGj)/af(delta**2))
 EJ=eh**2/af(delta)+ELj
 K=rat(br['K12_lower']);Ki=K.inv()
 G=arb_mat([[K[i,j] if i<12 and j<12 else int(i==j) if i>=12 and j>=12 else 0 for j in range(96)] for i in range(96)])
 eps2=2*(tr(Ki*EF)+84*EJ);tau=tr(Ki*sub(U,range(12),range(12)))+tr(sub(U,range(12,96),range(12,96)))
 gamma=2*(eps2*tau).sqrt()+eps2
 # Direct full 96 matrix: physical z4, fixed Y8, then J84.
 Uold=rat(r['old_energy_upper']);Dzlo=rat(br['N'])+sub(Uold,range(4),range(4));Dzhi=rat(r['D_z_upper'])
 Bzy=rat(r['C_U_centre'])+sub(Uold,range(4),range(4,12));Dzj=sub(mat(g['direct_cross_model']),range(4),range(84))
 D92=mat(d['D92_model']);idx=list(range(84,92))+list(range(84))
 rest=sub(D92,idx,idx)
 Dlo=arb_mat([[Dzlo[i,j] if i<4 and j<4 else Bzy[i,j-4] if i<4 and j<12 else Dzj[i,j-12] if i<4 else Bzy[j,i-4] if j<4 and i<12 else Dzj[j,i-12] if j<4 else rest[i-4,j-4] for j in range(96)] for i in range(96)])
 Dhi=Dlo+arb_mat([[Dzhi[i,j]-Dzlo[i,j] if i<4 and j<4 else 0 for j in range(96)] for i in range(96)])
 eps=af(r['C_error_norm_upper']);M=rat(r['C_error_metric'])
 crosscharge=arb_mat([[eps*M[i,j] if i<4 and j<4 else eps if 4<=i<12 and i==j else 0 for j in range(96)] for i in range(96)])
 directerror=af('96e-25');Dlo=sym(Dlo-crosscharge-eye(96)*directerror);Dhi=sym(Dhi+crosscharge+eye(96)*directerror)
 lower=sym(Dlo-U-gamma*G);upper=sym(Dhi-U+gamma*G)
 positive=ldl(lower)[2] is None
 gl,gd,gfail=ldl(G);assert gfail is None
 ginv=arb_mat(gl).transpose().inv()
 whitening=arb_mat([[ginv[i,j]/gd[j].sqrt() for j in range(96)] for i in range(96)])
 normalized=sym(whitening.transpose()*lower*whitening)
 mineig=float(np.linalg.eigvalsh(np.array([[float(normalized[i,j].mid()) for j in range(96)] for i in range(96)]))[0])
 reserve=F(math.floor(mineig*10**9)-2,10**9)
 if positive:assert reserve>0 and ldl(lower-af(reserve)*G)[2] is None
 print(label,'new actual common 96D lower positive:',positive,'feature price',gamma.str(10),flush=True)
 print(label,'certified reserve relative to diag(K12_old,I84):',reserve,flush=True)
 # Save all pieces for independent rational congruence and block checks.
 record={'parity':label.lower(),'delta':str(delta),'F_integer_matrix':[[str(x) for x in row] for row in Fnewi],
  'coupling_padding':str(coupling_padding),'HB_integer_matrix':[[str(x) for x in row] for row in HBi],'HB_denominator':str(10**90),
  'F_denominator':str(10**90),'inverse_congruence_integer_matrix':[[str(x) for x in row] for row in Ci],
  'inverse_congruence_denominator':str(10**80),'congruence_error_numerator':str(rn),'congruence_error_denominator':str(den),'rho':str(rho),
  'U96_model':U,'D96_lower_model':Dlo,'D96_upper_model':Dhi,
  'G96_rational':[[br['K12_lower'][i][j] if i<12 and j<12 else str(int(i==j)) if i>=12 and j>=12 else '0' for j in range(96)] for i in range(96)],
  'finite_feature_error_gram':EF,'tail_feature_error_scalar':EJ,'complete_feature_error_metric_trace':eps2,
  'complete_model_feature_metric_trace':tau,'complete_energy_relative_error':gamma,
  'common96_lower_model':lower,'common96_upper_model':upper,'common96_lower_positive':positive,
  'common96_positive_reserve_relative_to_G':str(reserve),
  'H84_new_model':HGj/af(delta),'low_feature_J84_model':sub(low,range(191),range(12,96)),
  'finite_cross_C84_new_model':sub((Dlo+crosscharge+eye(96)*directerror)-U,range(12),range(12,96)),
  'bindings':{str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [cp,gp,dp,rp,bp,oldpath,floorpath]},
  'full_remainder_certified':False,'negative_actual_schur_witness':False}
 rows.append(record)
(HERE/'REFINED_COMMON96.json').write_text(json.dumps(serial({'status':'REFINED_HIGH_FLOOR_COMMON96_TEST','cases':rows,'full_remainder_certified':False},80),indent=2)+'\n')
