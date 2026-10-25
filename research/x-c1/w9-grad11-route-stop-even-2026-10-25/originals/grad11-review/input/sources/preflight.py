from load_env import *
from fractions import Fraction as Q
def sha(b):return hashlib.sha256(b).hexdigest()
eng,env=load();co=env['common'];q,mat,quad,tr=co.q,co.mat,eng.quad,co.trace
norm,up,low=co.norm,eng.norm_upper,eng.norm_lower
e=env['energy'];W=e.w;Ki,a,GF,GJ=(W[k]for k in ('Ki','a','GF','GJ'))
frozen_raw=(HERE/'DIRECTIONS.json').read_bytes();d=json.loads(frozen_raw)
if sha((HERE/'PLAN.txt').read_bytes())!=d['plan_sha256']:raise RuntimeError('Changed plan')
def column(v):return arb_mat([[q(x)]for x in v])
raw1,raw2=column(d['v1_rational']),column(d['v2_rational'])
c1=raw1/quad(e.G,raw1).sqrt();c2=raw2/quad(e.G,raw2).sqrt()
w1,w2=column(d['w1_rational']),column(d['w2_rational'])
C=arb_mat([[c1[i,0],c2[i,0]]for i in range(12)])
T=arb_mat([[w1[i,0],w2[i,0]]for i in range(84)])
case=env['inp'].json('common')['cases'][0];raw=env['inp'].json('old_sources')['cases'][0]
DL,DU=mat(case['D96_lower_model']),mat(case['D96_upper_model'])
DD=arb_mat([[(DU[i,j]-DL[i,j])/2 for j in range(12,96)]for i in range(12,96)])
DJ=arb_mat([[(DU[i,j]+DL[i,j])/2 for j in range(12,96)]for i in range(12,96)])
UJ=arb_mat([[env['U'][i,j]for j in range(12,96)]for i in range(12,96)])
EJ=2*(co.box(case['tail_feature_error_scalar'])+co.box(raw['galerkin']['high_source_error_norm'])**2/W['delta'])
Bbase=sum((e.components[k]for k in ('high_U8','finite_U8','K_inverse_v')),arb_mat(12,12))
Heta=env['H0']-q('1e-10')*DJ
Fmodel=C.transpose()*Bbase*C+T.transpose()*e.nu*C+C.transpose()*e.nu.transpose()*T-T.transpose()*Heta*T
Fmodel=(Fmodel+Fmodel.transpose())/2
def eval_form(c,w):
 wn=norm(w);gwn=up(quad(GJ,w));delta,rho,gamma=(W[k]for k in ('delta','rho','gamma'))
 cross=up(quad(e.H,c))+gamma*abs((e.eh*c)[0,0]).upper();en=norm(e.ell*c)
 fn=up(quad(mat(e.data['H9_Gram']),c));physnorm=up(quad(e.G,c))
 eWh=norm(W['C'])*(e.eRawA*cross+e.eLowA*en)/(delta*(1-rho).sqrt());whn=norm(e.wh*c)
 fhigh=e.eRawF*tr(Ki).sqrt()*cross+tr(Ki*e.ELF).sqrt()*en
 ev=e.eBareF*tr(Ki).sqrt()*fn+fhigh/delta+tr(Ki*e.wf.transpose()*e.wf).sqrt()*eWh+tr(Ki*e.EF).sqrt()*(whn+eWh)
 base=quad(Bbase,c);basecap=e.bounds['U8_norm_upper']+e.bounds['v_feature_operator_norm_upper']**2
 er=basecap.sqrt()*e.eResidual*physnorm;ef=(eWh**2+ev**2).sqrt()
 blo=max(arb(0),low(base)-er.upper()-ef.upper())**2;bhi=(up(base)+er.upper()+ef.upper())**2
 kw=e.k*w;kwn=norm(kw);kv=Ki*e.v*c;da=W['da']
 dkw=da*tr(Ki*GF*Ki).sqrt()*gwn
 s=arb_mat([[-kw[i,0]]if i<12 else[w[i-12,0]]for i in range(96)])
 UF=arb_mat([[env['U'][i,j]for j in range(12)]for i in range(12)])+W['du']*GF
 joint=up(quad(env['U'],s)+W['du']*quad(W['G'],s))+tr(UF).sqrt()*dkw
 pop=q('1.000502').sqrt()*wn+16*(kwn+dkw)+e.bounds['U8_norm_upper'].sqrt()*joint
 prices={
 'bare':(e.eBareJ*wn+e.eBareF*kwn)*fn,
 'high_raw':(e.eRawJ*wn+e.eRawF*kwn)*cross/delta,
 'low':(e.eLJ*wn+up(quad(e.ELF,kw)))*en/delta,
 'low_high':norm(e.ws*w)*eWh,
 'source_features':(e.eJ*wn+up(quad(e.EF,kw)))*(whn+eWh),
 'a_fin_common':da*gwn*(up(quad(GF,kv))+tr(Ki*GF).sqrt()*ev),
 'whole_residual':pop*e.eResidual*physnorm}
 pair=(w.transpose()*e.nu*c)[0,0];pi=co.pad(pair,sum(prices.values(),arb(0)).upper())
 ew=EJ*(w.transpose()*w)[0,0];uw=quad(UJ,w)
 formprice=2*(uw*ew).sqrt()+ew+quad(DD,w)
 square_price,detail=eng.refined_form_loss(env,w)
 a2=quad(Ki,a*w);ea=da*tr(Ki*GF).sqrt()*gwn
 aslo=max(Q(0),Q(co.enc(a2)[0])-square_price)
 ashi=Q(co.enc(a2)[1])+square_price+Q(co.enc(ea)[1])**2
 bb=list(map(Q,co.enc(quad(env['BJJ'],w))));fp=Q(co.enc(formprice)[1])
 dlo=Q(co.enc(quad(arb_mat([[DL[i,j]for j in range(12,96)]for i in range(12,96)]),w))[0])
 dhi=Q(co.enc(quad(arb_mat([[DU[i,j]for j in range(12,96)]for i in range(12,96)]),w))[1])
 hlo=bb[0]-fp-ashi-Q('1e-10')*dhi;hhi=bb[1]+fp-aslo-Q('1e-10')*dlo
 fl=Q(co.enc(blo)[0])+2*Q(co.enc(pi)[0])-hhi
 fu=Q(co.enc(bhi)[1])+2*Q(co.enc(pi)[1])-hlo
 if fl>fu:raise RuntimeError('Reversed F interval')
 return {'F_interval':[str(fl),str(fu)],'base_interval':[co.enc(blo)[0],co.enc(bhi)[1]],'base_model':co.enc(base),
 'pair_model':co.enc(pair),'pair_interval':co.enc(pi),'pair_prices':co.encode(prices),
 'H_interval':[str(hlo),str(hhi)],'directional_DU_price':co.enc(formprice),'a_cross_price':str(square_price),
 'a_positive_square_price':str(Q(co.enc(ea)[1])**2),'eta_q':[str(Q('1e-10')*dlo),str(Q('1e-10')*dhi)],'physical_W_norm':co.enc(physnorm)}
checks={name:eval_form(cc,ww)for name,cc,ww in [('one',c1,w1),('two',c2,w2),('plus',c1+c2,w1+w2),('minus',c1-c2,w1-w2)]}
F1,F2,Fp,Fm=[list(map(Q,checks[n]['F_interval']))for n in ('one','two','plus','minus')]
cross=[(Fp[0]-Fm[1])/4,(Fp[1]-Fm[0])/4]
Fbox=[[F1,cross],[cross,F2]]
def sandwich(boxes):
 mid=[[(v[0]+v[1])/2 for v in row]for row in boxes]
 rad=[sum((v[1]-v[0])/2 for v in row)for row in boxes]
 lo=[[mid[i][j]-(rad[i]if i==j else 0)for j in range(2)]for i in range(2)]
 hi=[[mid[i][j]+(rad[i]if i==j else 0)for j in range(2)]for i in range(2)]
 return {'lower':[[str(x)for x in row]for row in lo],'upper':[[str(x)for x in row]for row in hi],'row_radius':[str(x)for x in rad]}
km=env['inp'].json('kp_model_even')['K_P_model'];K0=arb_mat([[q(str(x))for x in row]for row in km]);K0=(K0+K0.transpose())/2
Kmodel=C.transpose()*K0*C;gap=Kmodel-Fmodel
budgetdata=env['inp'].json('kp_budget')['parities']['even']
e0budget=next(x for x in budgetdata['individual_directions']if x['degree']==d['second_basis_index'])
def display(A):return [[float(A[i,j].mid())for j in range(A.ncols())]for i in range(A.nrows())]
orig=json.loads((ROOT/'research/x-c1/w9-residual-centered-control-even-2026-10-21/RESULT.json').read_bytes())
prev=list(map(Q,orig['F_interval']))
if not(F1[0]<=prev[1]and prev[0]<=F1[1]):raise RuntimeError('Old F interval control')
sourcefiles={str(p.relative_to(ROOT)):sha(p.read_bytes())for p in [PATH/'engine.py',PATH/'INPUT_BINDINGS.json',PATH/'CANDIDATE.json',ROOT/'research/x-c1/w9-partial-energy-2026-10-18/INPUT_BINDINGS.json']}
result={'status':'DIRECTED_VARIATIONAL_FORM_WITH_MODEL_BUDGET_ONLY','directions_sha256':sha(frozen_raw),'prec_bits':ctx.prec,
 'common_physical_W_gram':co.encode(C.transpose()*e.G*C),'K_budget_model_ONLY':co.encode(Kmodel),'F_model':co.encode(Fmodel),
 'gap_model_ONLY':co.encode(gap),'F_directed_entry_intervals':[[[str(x)for x in v]for v in row]for row in Fbox],
 'F_Loewner':sandwich(Fbox),'scalar_polarization_checks':checks,'known_budget11':env['kp']['K_P_interval'],
 'known_budget22_upper':e0budget,'budget_cross_directed':'MISSING','new_residual_gram':'MISSING',
 'old_F_overlap_control':True,'historical_source_files':sourcefiles,'new_full_integration':False,'outer_response_changed':False,
 'interpretation':'No two-dimensional pass: exploratory K model is not a budget certificate; residual positive price not yet included.'}
(HERE/'PREFLIGHT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'K_model':display(Kmodel),'F_model':display(Fmodel),'gap_model':display(gap),
 'F_intervals':[[[float(x)for x in v]for v in row]for row in Fbox],
 'budget22':e0budget,'old_F_control':True},indent=2))
