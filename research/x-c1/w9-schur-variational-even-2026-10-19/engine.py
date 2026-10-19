"""Directed data and scalar controls for a single fixed K-star Schur test."""
import gzip
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import MappingProxyType,ModuleType
from flint import arb,arb_mat,ctx

HERE=Path(__file__).resolve().parent
STEP=Q(13,10**8)

def need(ok,msg):
    if not ok:raise RuntimeError(msg)

def sha(raw):return hashlib.sha256(raw).hexdigest()

def module(name,raw,path):
    m=ModuleType(name);m.__file__=str(path);sys.modules[name]=m
    exec(compile(raw,str(path),'exec'),m.__dict__);return m

def quad(A,c):return (c.transpose()*A*c)[0,0]

def norm_upper(square):
    need(square.upper()>=0,'Negative norm-square upper bound')
    return square.upper().sqrt()

def norm_lower(square):
    need(square.upper()>=0,'Negative norm-square upper bound')
    return max(arb(0),square.lower()).sqrt()

def load(root,bindings):
    ctx.prec=1024;spec=json.loads(bindings);data={}
    for alias,e in spec['files'].items():
        path=(root/e['path']).resolve();need(path.is_relative_to(root),'Escaping input path')
        raw=path.read_bytes();need(sha(raw)==e['sha256'],'Input binding: '+alias);data[alias]=raw
    common=module('common',data['common'],root/spec['files']['common']['path'])
    need(common.ROOT==root,'Inherited root')
    inp=common.Inputs(binding_bytes=data['inherited_inputs'])
    weight=module('pilot_weights',data['pilot_weights'],root/spec['files']['pilot_weights']['path'])
    energy_module=module('pilot_energy',data['pilot_energy'],root/spec['files']['pilot_energy']['path'])
    schur=json.loads(gzip.decompress(data['pilot_schur']));pilot=json.loads(data['pilot_result'])
    candidate=json.loads(data['candidate_even']);kp=json.loads(data['kp_even'])
    need(sha(data['pilot_schur'])==pilot['SCHUR_sha256'],'Inherited matrix binding')
    need(schur['complete_287_block']['positive_pivots']==287,'Inherited positivity')
    manifest=json.loads(data['pilot_manifest'])
    for alias,name in [('pilot_schur','SCHUR.json.gz'),('pilot_result','RESULT.json'),('pilot_weights','pilot_weights.py'),('pilot_energy','pilot_energy.py'),('pilot_proof','PROOF.md'),('pilot_acceptance','ACCEPTANCE.json')]:
        need(manifest[name]==sha(data[alias]),'Inherited manifest: '+name)
    need(sha(data['candidate_even'])==pilot['candidate_sha256']==kp['candidate_sha256'],'Frozen physical witness')
    need(candidate['pairs_sha256']==sha(data['pairs_even']),'Frozen pairs')
    need(pilot['K_P_certificate_sha256']==sha(data['kp_even']),'Frozen budget')
    common_case=inp.json('common')['cases'][0];need(common_case['parity']=='even','Parity')
    co=inp.json('coherent')['parities']['even'];gf=[r[:12]for r in common_case['G96_rational'][:12]]
    ks=[[str(Q(co['K_rational'][i][j])+STEP*Q(gf[i][j]))for j in range(12)]for i in range(12)]
    need(ks==schur['K_star_rational'],'K-star unchanged')
    pairs=json.loads(gzip.decompress(data['pairs_even']));pairs['_source_sha256']=sha(data['pairs_even'])
    energy=energy_module.Energy(inp,pairs,common.ratmat(ks),common.ratmat(schur['P_star_upper_rational']),common.q(pilot['P_weight']))
    coeff=arb_mat([[common.q(v)]for v in candidate['raw_coefficients']]);n2=quad(energy.G,coeff)
    need(n2>0,'Physical witness norm');coeff/=n2.sqrt()
    DL=common.mat(common_case['D96_lower_model']);DU=common.mat(common_case['D96_upper_model']);U=common.mat(common_case['U96_model'])
    B=(DU+DL)/2-U;BJJ=weight.sub(B,range(12,96),range(12,96))
    a0=energy.w['a'];Ki=energy.w['Ki']
    H0=BJJ-a0.transpose()*Ki*a0
    for key in ('common_U_energy_relative_error_upper','direct_energy_relative_error_upper','a_fin_relative_error_upper'):
        need(energy.bounds[key].overlaps(common.box(pilot['partial_weight_bounds'][key])),'Inherited common error '+key)
    return dict(common=common,inp=inp,data=MappingProxyType(data),spec=spec,energy=energy,c=coeff,normalization=n2.sqrt(),
                nu=energy.nu*coeff,H0=H0,BJJ=BJJ,U=U,candidate=candidate,kp=kp)

def midpoint_matrix(A):
    return arb_mat([[A[i,j].mid() for j in range(A.ncols())]for i in range(A.nrows())])

def freeze(env):
    common=env['common'];H=env['H0'];H=(H+H.transpose())/2
    midpoint=midpoint_matrix(H);rhs=midpoint_matrix(env['nu'])
    # Only candidate generation, never a true inverse certificate.
    solution=midpoint.solve(rhs);rows=[];grid=10**50
    for i in range(84):
        need(solution[i,0].is_finite(),'Unresolved candidate solve')
        value=Q(str(solution[i,0].mid().fmpq()))*grid
        rounded=(value+Q(1,2)).numerator//(value+Q(1,2)).denominator
        rows.append(str(Q(rounded,grid)))
    return {'status':'FROZEN_RATIONAL_VARIATIONAL_TEST_NOT_A_CERTIFICATE','parity':'even',
            'source_commit':env['spec']['source_commit'],'dimension':84,'rounding_decimal_digits':50,
            'selection':'one midpoint solve of (Dmid-U)_JJ-a0*Ki*a0; eta*q term omitted',
            'K_star_sha256':sha(json.dumps(json.loads(gzip.decompress(env['data']['pilot_schur']))['K_star_rational'],separators=(',',':')).encode()),
            'physical_candidate_sha256':sha(env['data']['candidate_even']),
            'pairs_sha256':sha(env['data']['pairs_even']),
            'selection_inputs_sha256':{k:sha(env['data'][k])for k in ('pilot_schur','pilot_energy','pilot_weights','inherited_inputs')},
            'raw_coefficients':rows,'adaptive_search':False,'mathematical_decision':None}

def certify(env,frozen_bytes):
    c0=env['common'];q,mat,trace,norm,enc=c0.q,c0.mat,c0.trace,c0.norm,c0.enc
    e=env['energy'];c=env['c'];W=e.w;Ki=W['Ki'];a0=W['a'];GF=W['GF'];GJ=W['GJ'];da=W['da']
    frozen=json.loads(frozen_bytes)
    need(frozen['source_commit']==env['spec']['source_commit'] and frozen['parity']=='even','Wrong frozen model')
    need(frozen['physical_candidate_sha256']==sha(env['data']['candidate_even']),'Frozen witness binding')
    need(frozen['pairs_sha256']==sha(env['data']['pairs_even']),'Frozen pairing binding')
    need(frozen['K_star_sha256']==sha(json.dumps(json.loads(gzip.decompress(env['data']['pilot_schur']))['K_star_rational'],separators=(',',':')).encode()),'Frozen K-star binding')
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
    # H_star[Jw] = B_JJ[w] - ||Ki^(1/2) a_fin w||^2 - eta*q[Jw].
    # q>=0 is inherited. Omitting eta*q gives an upper bound, the needed sign.
    a_aw=a0*w;an2=quad(Ki,a_aw);ea=da*trace(Ki*GF).sqrt()*gwn
    a_norm_lower=max(arb(0),norm_lower(an2)-ea.upper())
    direct_U_error=da*gwn**2
    Hupper=(quad(env['BJJ'],w)+direct_U_error).upper()-a_norm_lower**2
    lower=base_lo+2*pairing.lower()-Hupper.upper()
    # There is NO full-energy upper endpoint, partial pass or dual reserve.
    published=enc(lower)[0];budget=env['kp']['K_P_interval']
    gap=Q(published)-Q(budget[1])
    outcome='SCHUR_UNDERFORM_COMPARISON_EXCLUDED'if gap>0 else'SCHUR_LOWER_TEST_OPEN'
    model_diagnostic=base_model+2*pmodel-quad(env['H0'],w)
    return c0.encode({'status':'AUTHOR_DERIVED','review_status':'EXTERNAL_REVIEW_OPEN','parity':'even',
        'source_commit':env['spec']['source_commit'],'outcome':outcome,
        'criterion':'E_base + 2 Re<nu_star,Jw> - H_star[Jw] <= <f,Q_lower_star^-1 f>',
        'physical_candidate_sha256':sha(env['data']['candidate_even']),
        'test_vector_sha256':sha(frozen_bytes),'K_P_certificate_sha256':sha(env['data']['kp_even']),
        'source_normalization':env['normalization'],'base_component_models':base_components,
        'base_actual_energy_interval':[enc(base_lo)[0],enc(base_hi)[1]],'base_feature_error_norm':eb_feat,
        'base_residual_error_norm':eb_res,'base_operator_norm_upper':base_norm,
        'pairing_model':pmodel,'pairing_error_components':pairing_errors,'pairing_actual_interval':pairing,
        'pairing_operator_norm_upper':pairing_operator,'whole_residual_Hilbert_error':e.eResidual,
        'form_model_without_eta':quad(env['H0'],w),'form_B_model':quad(env['BJJ'],w),
        'form_common_D_U_error':direct_U_error,'form_a_Ki_model_norm_squared':an2,
        'form_a_Ki_error_norm':ea,'form_a_Ki_actual_norm_lower':a_norm_lower,
        'H_star_form_upper':enc(Hupper)[1],'positive_eta_q_term_unused':True,
        'variational_expression_model_diagnostic':model_diagnostic,
        'inverse_energy_lower':published,'budget_interval':budget,'lower_minus_budget_upper':str(gap),
        'full_inverse_energy_upper_claimed':False,'partial_pass':False,'dual_reserve':None,
        'RL_computed':False,'new_integrations':False,'adaptive_search':False,
        'K_star_changed':False,'frozen_response_changed':False,'physical_witness_changed':False,
        'test_vector_norm':wn,'test_vector_GJ_norm':gwn,'a_fin_error_retained':da,
        'inherited_controls':e.controls,'N12_closed':False,'milestone_4_closed':False,
        'negative_claim_boundary':'Only upper majorants of the inverse of this fixed strengthened lower form, with the frozen response and witness; not the actual Weil inverse or other lower forms.'})
