"""One K_new Schur test; inherited full pairing errors and directional form error."""
import gzip
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import MappingProxyType, ModuleType
from flint import arb, arb_mat, ctx

BASE = "bf9375b26ecb2ad3060c91824501f460c060fc43"
FROZEN_K = "89ded551059d1279c646bc17e3b5ab3e2a7f7a261d1c239ac752b7f0d35467a8"

def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(raw): return hashlib.sha256(raw).hexdigest()
def module(name,raw,path):
    m=ModuleType(name);m.__file__=str(path);sys.modules[name]=m
    exec(compile(raw,str(path),'exec'),m.__dict__);return m
def quad(A,c): return (c.transpose()*A*c)[0,0]
def norm_upper(square):
    need(square.is_finite() and square.upper()>=0,'Invalid norm square')
    return square.upper().sqrt()
def norm_lower(square):
    need(square.is_finite() and square.upper()>=0,'Invalid norm square')
    return max(arb(0),square.lower()).sqrt()

def snapshot(root, bindings):
    need(__debug__,'Do not use python -O')
    spec=json.loads(bindings);need(spec['source_commit']==BASE,'Frozen base')
    data={}
    for alias,item in spec['files'].items():
        path=(root/item['path']).resolve()
        need(path.is_relative_to(root),'Escaping bound input')
        raw=path.read_bytes();need(sha(raw)==item['sha256'],'Input binding: '+alias)
        data[alias]=raw
    return spec,MappingProxyType(data)

def weights(data):
    p=json.loads(data['pilot_result']);d=json.loads(data['dual_result'])
    pa=module('bound_pilot_endpoint_audit',data['pilot_audit'],Path('bound_pilot_audit.py'))
    pa.check(p,data['pilot_schur'])
    da=module('bound_dual_endpoint_audit',data['dual_audit'],Path('bound_dual_audit.py'))
    da.check(d,data['dual_matrix'])
    need(p['partial_actual_energy_interval']==d['inherited_partial_energy_interval'],'Same partial energy')
    need(p['candidate_sha256']==d['candidate_sha256'],'Same physical witness')
    need(p['K_P_certificate_sha256']==d['K_P_sha256'],'Same budget')
    need(p['K_new_canonical_sha256']==d['K_new_canonical_sha256']==FROZEN_K,'Same K_new')
    c,b0,beta=map(Q,(p['residual_cap'],p['P_weight'],p['beta']))
    need(c==Q(1977,500000) and b0==Q(51,50) and beta>0,'Frozen family')
    t=1/(1-c);need(1<t<=b0,'Necessary nonnegative C coefficient')
    part=Q(p['partial_actual_energy_interval'][0]);dual=Q(d['full_dual_energy_lower'])
    upper=Q(d['budget_interval'][1])
    lower=(part/b0+dual/beta)*t
    return {
        'status':'AUTHOR_DERIVED','review_status':'EXTERNAL_REVIEW_OPEN',
        'source_commit':BASE,'outcome':'YOUNG_WEIGHT_FAMILY_EXCLUDED' if lower>upper else 'WEIGHT_FAMILY_OPEN',
        'formula':'(partial_lower / b0 + full_dual_lower / beta) / (1-c)',
        'c':str(c),'b0':str(b0),'beta':str(beta),'minimum_weight':str(t),
        'partial_lower':str(part),'full_dual_lower':str(dual),
        'family_energy_lower':str(lower),'budget_upper':str(upper),
        'lower_minus_budget_upper':str(lower-upper),
        'pilot_result_sha256':sha(data['pilot_result']),'dual_result_sha256':sha(data['dual_result']),
        'K_new_canonical_sha256':FROZEN_K,'physical_candidate_sha256':p['candidate_sha256'],
        'K_P_certificate_sha256':p['K_P_certificate_sha256'],
        'scope':'Fixed K_new, P_new_upper, physical witness, answer and budget; C,B,D nonnegative and unchanged; admissible Young weights a,b>1/(1-c)',
        'weight_search':False,'new_integrations':False,'all_majorants_of_Q_new_excluded':False
    }

def load(root,spec,data):
    ctx.prec=1024
    pilot=module('bound_new_pilot',data['pilot_verify'],root/spec['files']['pilot_verify']['path'])
    common,inp,old,oldspec=pilot.snapshot(root,data['pilot_inputs'])
    weight=module('pilot_weights',old['pilot_weights'],root/oldspec['files']['pilot_weights']['path'])
    assembler=module('pilot_energy',old['pilot_energy'],root/oldspec['files']['pilot_energy']['path'])
    prior=json.loads(data['pilot_result']);schur=json.loads(data['pilot_schur'])
    ks=schur['K_new_rational'];ps=schur['P_new_upper_rational']
    need(sha(json.dumps(ks,separators=(',',':')).encode())==FROZEN_K,'Frozen K')
    candidate=json.loads(old['candidate_even']);kp=json.loads(old['kp_even'])
    need(sha(old['candidate_even'])==prior['candidate_sha256']==kp['candidate_sha256'],'Frozen physical witness')
    need(sha(old['kp_even'])==prior['K_P_certificate_sha256'],'Frozen budget')
    pairs=json.loads(gzip.decompress(old['pairs_even']));pairs['_source_sha256']=sha(old['pairs_even'])
    need(candidate['pairs_sha256']==pairs['_source_sha256'],'Frozen common pairings')
    energy=assembler.Energy(inp,pairs,common.ratmat(ks),common.ratmat(ps),common.q(prior['P_weight']))
    coeff=arb_mat([[common.q(x)] for x in candidate['raw_coefficients']])
    n2=quad(energy.G,coeff);need(n2>0,'Physical norm');coeff/=n2.sqrt()
    case=inp.json('common')['cases'][0];need(case['parity']=='even','Parity')
    DL,DU,U=[common.mat(case[k]) for k in ('D96_lower_model','D96_upper_model','U96_model')]
    BJJ=weight.sub((DL+DU)/2-U,range(12,96),range(12,96))
    H0=BJJ-energy.w['a'].transpose()*energy.w['Ki']*energy.w['a']
    for key in ('common_U_energy_relative_error_upper','direct_energy_relative_error_upper','a_fin_relative_error_upper'):
        need(energy.bounds[key].overlaps(common.box(prior['partial_weight_bounds'][key])),'Original F-J error '+key)
    nu=energy.nu*coeff;previous_nu=common.mat(prior['nu_new_direction'])
    need(all(nu[i,0].overlaps(previous_nu[i,0]) for i in range(84)),'Same nu_new')
    return dict(common=common,inp=inp,data=old,spec=spec,energy=energy,c=coeff,normalization=n2.sqrt(),
                nu=nu,H0=H0,BJJ=BJJ,U=U,candidate=candidate,kp=kp,K_hash=FROZEN_K)

def freeze(env):
    H=env['H0'];H=(H+H.transpose())/2
    H=arb_mat([[H[i,j].mid() for j in range(84)] for i in range(84)])
    rhs=arb_mat([[env['nu'][i,0].mid()] for i in range(84)])
    solution=H.solve(rhs);rows=[];grid=10**50
    for i in range(84):
        need(solution[i,0].is_finite(),'Candidate solve finite')
        x=Q(str(solution[i,0].mid().fmpq()))*grid+Q(1,2)
        rows.append(str(Q(x.numerator//x.denominator,grid)))
    return {'status':'FROZEN_RATIONAL_VARIATIONAL_TEST_NOT_A_CERTIFICATE',
        'source_commit':BASE,'parity':'even','dimension':84,
        'selection':'one midpoint solve for K_new, eta*q omitted; 50-decimal rational rounding',
        'K_new_sha256':FROZEN_K,'physical_candidate_sha256':sha(env['data']['candidate_even']),
        'pairs_sha256':sha(env['data']['pairs_even']),'raw_coefficients':rows,
        'adaptive_search':False,'mathematical_decision':None}

def refined_form_loss(env,w):
    c=env['common'];W=env['energy'].w
    z=W['a']*w;r=W['Ki']*z
    case=env['inp'].json('common')['cases'][0];raw=env['inp'].json('old_sources')['cases'][0]
    EF=2*(c.mat(case['finite_feature_error_gram'])+c.mat(raw['old_certificate']['joint_high_source_error_gram'])/W['delta'])
    EJ=2*(c.box(case['tail_feature_error_scalar'])+c.box(raw['galerkin']['high_source_error_norm'])**2/W['delta'])
    U=env['U'];UF=arb_mat([[U[i,j] for j in range(12)]for i in range(12)])
    UJ=arb_mat([[U[i,j] for j in range(12,96)]for i in range(12,96)])
    g={'model_F':quad(UF,r),'model_J':quad(UJ,w),'error_F':quad(EF,r),
       'error_J':EJ*(w.transpose()*w)[0,0],'GF_r':quad(W['GF'],r),'GJ_w':quad(W['GJ'],w)}
    need(all(x>=0 for x in g.values()),'Directional nonnegative Grams')
    dd=env['energy'].bounds['direct_energy_relative_error_upper']
    direct=dd*(g['GF_r']*g['GJ_w']).sqrt()
    terms={(a+'_'+b):(g[a]*g[b]).sqrt() for a,b in
           [('model_F','error_J'),('error_F','model_J'),('error_F','error_J')]}
    loss=2*(direct+sum(terms.values(),arb(0)))
    v=Q(c.enc(loss)[1])*10**24
    upper=Q(-((-v.numerator)//v.denominator),10**24)
    return upper,dict(directional_Grams=g,direct_relative_error=dd,direct_cross_error=direct,
                      feature_cross_errors=terms,square_loss_interval=loss,square_loss_upper=str(upper))

def certify(env,frozen_bytes):
    c0=env['common'];q,mat,trace,norm,enc=c0.q,c0.mat,c0.trace,c0.norm,c0.enc
    e=env['energy'];c=env['c'];W=e.w;Ki=W['Ki'];a0=W['a'];GF=W['GF'];GJ=W['GJ'];da=W['da']
    frozen=json.loads(frozen_bytes)
    need(frozen['source_commit']==env['spec']['source_commit'] and frozen['parity']=='even','Wrong frozen model')
    need(frozen['physical_candidate_sha256']==sha(env['data']['candidate_even']),'Frozen witness binding')
    need(frozen['pairs_sha256']==sha(env['data']['pairs_even']),'Frozen pairing binding')
    need(frozen['K_new_sha256']==env['K_hash'],'Frozen K_new binding')
    need(len(frozen['raw_coefficients'])==84,'Test vector dimension')
    w=arb_mat([[q(v)]for v in frozen['raw_coefficients']]);wn=norm(w);gwn=norm_upper(quad(GJ,w))
    need(wn>0,'Zero test vector')
    delta=W['delta'];rho=W['rho'];gamma=W['gamma'];C=W['C']
    hn=norm_upper(quad(e.H,c));eh=abs((e.eh*c)[0,0]).upper();en=norm(e.ell*c)
    fn=norm_upper(quad(mat(e.data['H9_Gram']),c));cross=hn+gamma*eh
    eBy=e.eRawA*cross+e.eLowA*en;eWh=norm(C)*eBy/(delta*(1-rho).sqrt());whn=norm(e.wh*c)
    fhigh=e.eRawF*trace(Ki).sqrt()*cross+trace(Ki*e.ELF).sqrt()*en
    ev=e.eBareF*trace(Ki).sqrt()*fn+fhigh/delta+trace(Ki*e.wf.transpose()*e.wf).sqrt()*eWh+trace(Ki*e.EF).sqrt()*(whn+eWh)
    base_components={key:quad(e.components[key],c)for key in ('high_U8','finite_U8','K_inverse_v')}
    base_model=sum(base_components.values(),arb(0))
    base_norm=e.bounds['U8_norm_upper']+e.bounds['v_feature_operator_norm_upper']**2
    eb_res=base_norm.sqrt()*e.eResidual;eb_feat=(eWh**2+ev**2).sqrt()
    base_lo=max(arb(0),norm_lower(base_model)-eb_res.upper()-eb_feat.upper())**2
    base_hi=(norm_upper(base_model)+eb_res.upper()+eb_feat.upper())**2
    # Rank-one specialization P=w w*: all old F-J and a_fin errors retained.
    kw=e.k*w;kwn=norm(kw)
    pairing_bare=(e.eBareJ*wn+e.eBareF*kwn)*fn
    pairing_raw=(e.eRawJ*wn+e.eRawF*kwn)*cross/delta
    pairing_low=(e.eLJ*wn+norm_upper(quad(e.ELF,kw)))*en/delta
    pairing_low_high=norm(e.ws*w)*eWh
    pairing_source=(e.eJ*wn+norm_upper(quad(e.EF,kw)))*(whn+eWh)
    kv=Ki*e.v*c
    pairing_a=da*gwn*(norm_upper(quad(GF,kv))+trace(Ki*GF).sqrt()*ev)
    # Whole physical residual error uses a newly computed directional norm.
    dkw=da*(trace(Ki*GF*Ki)).sqrt()*gwn
    s=arb_mat([[-kw[i,0]]if i<12 else [w[i-12,0]]for i in range(96)])
    joint0=quad(env['U'],s)+W['du']*quad(W['G'],s)
    UF=arb_mat([[env['U'][i,j]for j in range(12)]for i in range(12)])+W['du']*GF
    joint_norm=norm_upper(joint0)+trace(UF).sqrt()*dkw
    pairing_operator=q('1.000502').sqrt()*wn+16*(kwn+dkw)+e.bounds['U8_norm_upper'].sqrt()*joint_norm
    pairing_res=pairing_operator*e.eResidual
    pairing_errors=dict(bare=pairing_bare,high_raw=pairing_raw,low=pairing_low,
                        low_high=pairing_low_high,source_features=pairing_source,
                        a_fin_common=pairing_a,whole_residual=pairing_res)
    ep=sum(pairing_errors.values(),arb(0));pmodel=(w.transpose()*env['nu'])[0,0]
    pairing=c0.pad(pmodel,ep.upper())
    # H_new[Jw] = B_JJ[w] - ||Ki^(1/2) a_fin w||^2 - eta*q[Jw].
    # q>=0 is inherited. Omitting eta*q gives an upper bound, the needed sign.
    a_aw=a0*w;an2=quad(Ki,a_aw);ea=da*trace(Ki*GF).sqrt()*gwn
    a_norm_lower=max(arb(0),norm_lower(an2)-ea.upper())
    direct_U_error=da*gwn**2
    price,form_details=refined_form_loss(env,w)
    # Directed rational endpoints, retaining all recomputed pairing and base errors.
    Binterval=enc(quad(env['BJJ'],w));du_interval=enc(direct_U_error);an_interval=enc(an2)
    actual_square=max(Q(0),Q(an_interval[0])-price)
    Hupper_exact=Q(Binterval[1])+Q(du_interval[1])-actual_square
    base_interval=[enc(base_lo)[0],enc(base_hi)[1]];pair_interval=enc(pairing)
    lower_exact=Q(base_interval[0])+2*Q(pair_interval[0])-Hupper_exact
    # There is NO full-energy upper endpoint, partial pass or dual reserve.
    published=str(lower_exact);budget=env['kp']['K_P_interval']
    gap=Q(published)-Q(budget[1])
    outcome='SCHUR_UNDERFORM_COMPARISON_EXCLUDED'if gap>0 else'SCHUR_LOWER_TEST_OPEN'
    model_diagnostic=base_model+2*pmodel-quad(env['H0'],w)
    return c0.encode({'status':'AUTHOR_DERIVED','review_status':'EXTERNAL_REVIEW_OPEN','parity':'even',
        'source_commit':env['spec']['source_commit'],'outcome':outcome,'test_type':'single_frozen_new_K_variational_vector',
        'criterion':'E_base + 2 Re<nu_new,Jw> - H_new[Jw] <= <f,Q_lower_new^-1 f>',
        'physical_candidate_sha256':sha(env['data']['candidate_even']),
        'test_vector_sha256':sha(frozen_bytes),'K_P_certificate_sha256':sha(env['data']['kp_even']),
        'source_normalization':env['normalization'],'base_component_models':base_components,
        'base_actual_energy_interval':[enc(base_lo)[0],enc(base_hi)[1]],'base_feature_error_norm':eb_feat,
        'base_residual_error_norm':eb_res,'base_operator_norm_upper':base_norm,
        'pairing_model':pmodel,'pairing_error_components':pairing_errors,'pairing_actual_interval':pairing,
        'pairing_operator_norm_upper':pairing_operator,'whole_residual_Hilbert_error':e.eResidual,
        'form_model_without_eta':quad(env['H0'],w),'form_B_model':Binterval,
        'form_common_D_U_error':direct_U_error,'form_a_Ki_model_norm_squared':an2,
        'form_a_Ki_error_norm':ea,'form_a_Ki_actual_norm_lower':a_norm_lower,
        'H_new_form_upper':str(Hupper_exact),'actual_a_square_lower':str(actual_square),'form_refinement':form_details,'positive_eta_q_term_unused':True,
        'variational_expression_model_diagnostic':model_diagnostic,
        'inverse_energy_lower':published,'budget_interval':budget,'lower_minus_budget_upper':str(gap),
        'full_inverse_energy_upper_claimed':False,'partial_pass':False,'dual_reserve':None,
        'RL_computed':False,'new_integrations':False,'adaptive_search':False,
        'K_new_changed':False,'K_new_sha256':env['K_hash'],'frozen_response_changed':False,'physical_witness_changed':False,
        'test_vector_norm':wn,'test_vector_GJ_norm':gwn,'a_fin_error_retained':da,
        'inherited_controls':e.controls,'N12_closed':False,'milestone_4_closed':False,
        'negative_claim_boundary':'Only upper majorants of the inverse of this fixed strengthened lower form, with the frozen response and witness; not the actual Weil inverse or other lower forms.'})
