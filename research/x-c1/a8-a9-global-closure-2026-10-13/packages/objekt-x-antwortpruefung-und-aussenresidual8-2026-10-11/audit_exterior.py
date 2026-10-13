"""Independent rational construction and 211-pivot exterior-budget audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse, json, sys
ap=argparse.ArgumentParser()
for name in ['responses','parent','data','prior-data','connection','out']:
 ap.add_argument('--'+name,type=Path,required=True)
args=ap.parse_args();sys.path.insert(0,str(args.responses))
import audit as au
ld=au.ld;S=ld.SCALE
def read(p):return json.loads(p.read_bytes())
def hi(v):return F(v[1])
def sub(a,ii,jj):return [[a[i][j] for j in jj] for i in ii]
def scalar_trace(a,ii):return sum((au.upper(a[i][i]) for i in ii),F(0))
assert __debug__
ndata=read(args.parent/'REFINED_COMMON96.json')['cases']
idata=read(args.parent/'REFINED_INPUT.json')['cases']
connection=read(args.connection)['cases'];rows=[]
for p,label in enumerate(['EVEN','ODD']):
 d=read(args.responses/f'RESPONSES_{label}.json');n=ndata[p];old=idata[p]['old_certificate']
 g=read(args.prior_data/f'PROBE_{label}_3072.json')
 cross=read(args.data/f'CROSS_{label}_3072.json')
 result=read(args.data/f'RESIDUAL_{label}_3072.json')
 delta=F(d['delta']);rho=F(d['rho']);eta=F(d['eta']);beta=F(d['beta'])
 K=au.rat(d['K12_new_rational']);Ki=au.inv(K);kii=au.pts(Ki)
 ci=[[int(v) for v in row] for row in n['inverse_congruence_integer_matrix']]
 cd=int(n['inverse_congruence_denominator'])
 AC=au.pts([[F(v,cd) for v in row] for row in ci])
 vF=au.add(au.im(old['source_c_model']),au.sc(au.im(old['source_Bh_model']),1/delta),-1)
 vK=sub(au.add(au.im(g['source_c_model']),au.sc(au.im(g['source_Bh_model']),1/delta),-1),range(191),range(1,9))
 lF=au.mmI(au.T(AC),vF);lK=au.mmI(au.T(AC),vK)
 hFK=sub(au.im(g['source_high_cross_model']),range(12),range(1,9))
 hKK=sub(au.im(g['Hgram']),range(1,9),range(1,9))
 UFK=au.add(au.sc(hFK,1/delta),au.sc(au.mmI(au.T(lF),lK),1/(1-rho)))
 UKK=au.add(au.sc(hKK,1/delta),au.sc(au.mmI(au.T(lK),lK),1/(1-rho)))
 DFK=sub(au.im(g['direct_F_cross_model']),range(12),range(1,9))
 CK=lK+au.add(DFK,UFK,-1)
 hJK=sub(au.im(cross['Hgram']),range(84),range(84,92))
 dJK=sub(au.im(cross['direct_probe_model']),range(84),range(84,92))
 SJK=au.add(au.sc(dJK,1-eta),au.sc(hJK,1/delta),-1)
 RK=au.add(au.T(CK),au.mmI(au.T(SJK),au.pts(au.rat(d['X84x203_rational']))),-1)
 au.overlaps(RK,au.im(result['new_R_on_K_model']))
 ds=[F(11,10)+sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(96,104)]
 D=[[F(1-rho) if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
 M=au.rat(d['M_upper_rational'])
 T=[[beta*(D[i][j]-M[i][j]) for j in range(203)] for i in range(203)]
 cap=F(result['model_relative_to_directional_budget_upper'])
 block=[]
 for i in range(211):
  block.append([ld.point(cap*T[i][j]) if i<203 and j<203 else
                RK[j-203][i] if i<203 else RK[i-203][j] if j<203 else
                ld.point(ds[i-203] if i==j else 0) for j in range(211)])
 pivots=ld.positive(block)
 print(label,'211 rational pivots: finite model Gram fits directional budget',flush=True)
 # Recompute all complete analytic error charges in the actual new metric.
 xi=[[sum(ci[i][k]*ci[j][k] for k in range(max(i,j),191)) for j in range(191)] for i in range(191)]
 factor=F(1,cd**2)/(1-rho)
 XI=au.pts([[v*factor for v in row] for row in xi])
 tx=sum(xi[i][i] for i in range(191))*factor
 cn=[[ld.interval(v)] for v in g['moment_basis_coefficients']]
 txgm=tx+au.upper(au.mmI(au.T(cn),au.mmI(XI,cn))[0][0])
 hb=[[int(v) for v in row] for row in n['HB_integer_matrix']]
 txhb=sum(xi[i][j]*hb[j][i] for i in range(191) for j in range(191))*factor/F(n['HB_denominator'])
 ef=hi(g['source_model_error_norm']);eh=hi(g['high_source_error_norm']);eb=hi(g['old_coupling_error_norm'])
 ek=eh**2/delta+3*(txgm*ef**2+txhb*eh**2/delta**2+tx*eb**2*scalar_trace(au.im(g['Hgram']),range(9))/delta**2)
 eK=8*ek;eF=au.pair_upper(au.im(n['finite_feature_error_gram']),au.T(kii))
 tauF=au.pair_upper(sub(au.im(n['U96_model']),range(12),range(12)),au.T(kii));tauK=au.itr(UKK)
 sqrt=au.sqrtup
 eC=sqrt(eK)+sqrt(eF*tauK)+sqrt(tauF*eK)+sqrt(eF*eK)+sqrt(12*8*au.tr(Ki))*F(1,10**20)
 ehc=hi(cross['high_source_error_norm']);HH=au.im(cross['Hgram'])
 eH=(sqrt(scalar_trace(HH,range(84)))*ehc+ehc*sqrt(scalar_trace(HH,range(84,92)))+ehc**2)/delta
 eS=(1-eta)*sqrt(F(84*8))*F(1,10**20)+eH
 eR=eC+eS*sqrt(hi(d['fixed_X_squared_HS_in_D_inverse_metric']))
 budget=F(d['sufficient_complete_QR_normalized_budget'])
 ew=sqrt(eR**2/(ds[0]*budget))
 charge=2*sqrt(cap)*ew+ew**2
 certified=F(result['true_eight_term_Gram_in_T_upper'])
 assert cap+charge<=certified
 finite=F(connection[p]['full_finite_J_dual_Gram_D_normalized_upper'])
 geometry=F(1,10**250)
 full=F(result['true_finite_J_plus_eight_terms_and_geometry_in_T_upper'])
 assert certified+(finite+geometry)/budget<=full<1
 friendly=F(1,5000) if p==0 else F(13,20000)
 assert full<friendly
 rows.append({'parity':label.lower(),'residual_entries_rebuilt':8*203,
  'rational_directional_Gram_test':pivots,'model_budget_fraction_upper':str(cap),
  'analytic_Gram_error_budget_fraction_upper':str(charge),
  'certified_J_eight_exterior_terms_and_geometry_budget_fraction_upper':str(full),
  'friendly_budget_fraction_upper':str(friendly),
  'remaining_sufficient_tail_budget_fraction':str(1-friendly),
  'uncomputed_degrees':'104 and all above','full_remainder_certified':False})
 print(label,'PASS: all computed contributions <',float(friendly)*100,'% of T_budget',flush=True)
out={'status':'PASS_RATIONAL_NEW_RESIDUAL_EIGHT_EXTERIOR_TERMS',
 'rational_grid_digits':100,'cases':rows,'full_remainder_certified':False}
args.out.write_text(json.dumps(out,indent=2)+'\n')
