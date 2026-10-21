"""Directed finite control for the whole residual; no whole-dual certificate."""
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import ModuleType, MappingProxyType
from flint import arb, arb_mat, ctx

BASE = '639d25e38b453f2e10b859553ca49a7a0e4fafdb'
VECTOR = '70e8f72ab0cb8ca1ac0d254392384a2040a9d76d04ebf82587c48771e9f34628'
KNEW = '89ded551059d1279c646bc17e3b5ab3e2a7f7a261d1c239ac752b7f0d35467a8'


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def module(name, raw, path):
    m = ModuleType(name)
    m.__file__ = str(path)
    sys.modules[name] = m
    exec(compile(raw, str(path), 'exec'), m.__dict__)
    return m


def snapshot(root, raw):
    need(__debug__, 'Do not use python -O')
    spec = json.loads(raw)
    need(spec['source_commit'] == BASE, 'Base')
    data = {}
    for alias, entry in spec['files'].items():
        path = (root / entry['path'].replace('\\', '/')).resolve()
        need(path.is_relative_to(root), 'Escaping input')
        buf = path.read_bytes()
        need(sha(buf) == entry['sha256'], 'Input binding: ' + alias)
        data[alias] = buf
    return spec, MappingProxyType(data)


def run(root, spec, data):
    ctx.prec = 1024
    eng = module('bound_residual_schur_engine', data['schur_engine'], root/spec['files']['schur_engine']['path'])
    inherited, olddata = eng.snapshot(root, data['schur_bindings'])
    env = eng.load(root, inherited, olddata)
    c = env['common']
    q, mat, quad, tr = c.q, c.mat, eng.quad, c.trace
    frozen = json.loads(data['vector'])
    old = json.loads(data['schur_result'])
    rest = json.loads(data['rest_result'])
    prior = json.loads(olddata['pilot_result'])
    need(sha(data['vector']) == old['test_vector_sha256'] == rest['test_vector_sha256'] == VECTOR, 'Fixed vector')
    need(env['K_hash'] == rest['K_new_sha256'] == KNEW, 'Fixed K_new')
    need(old['budget_interval'] == rest['budget_interval'], 'Fixed budget')
    need(old['physical_candidate_sha256'] == prior['candidate_sha256'], 'Fixed physical witness')
    w = arb_mat([[q(v)] for v in frozen['raw_coefficients']])
    e = env['energy']
    case = env['inp'].json('common')['cases'][0]
    raw = env['inp'].json('old_sources')['cases'][0]
    UJ = arb_mat([[env['U'][i,j] for j in range(12,96)] for i in range(12,96)])
    EJ = 2*(c.box(case['tail_feature_error_scalar']) + c.box(raw['galerkin']['high_source_error_norm'])**2/e.w['delta'])
    ew = EJ*(w.transpose()*w)[0,0]
    uw = quad(UJ,w)
    need(uw >= 0 and ew >= 0, 'Directional feature squares')
    directional_u = 2*(uw*ew).sqrt()+ew
    DL, DU = mat(case['D96_lower_model']), mat(case['D96_upper_model'])
    DD = arb_mat([[(DU[i,j]-DL[i,j])/2 for j in range(12,96)] for i in range(12,96)])
    directional_d = quad(DD,w)
    need(directional_d >= 0, 'Directional direct form bound')
    price_grid = Q(c.enc(directional_u+directional_d)[1])*10**30
    new_price = Q(-((-price_grid.numerator)//price_grid.denominator),10**30)
    old_price = Q(old['form_common_D_U_error'][1])
    need(0 <= new_price < old_price, 'Strictly sharper form price')
    flo = Q(rest['F_interval'][0])+old_price-new_price
    fup = Q(rest['F_interval'][1])-old_price+new_price
    need(flo <= fup < Q(rest['budget_interval'][0]), 'F enclosure and room for residual')

    # Bound P^(1/2) J*(nu-HJw), keeping source errors shared at each
    # bilinear product. P is the already certified rational upper matrix.
    P, Ki, a, GF, GJ = (e.w[k] for k in ('P','Ki','a','GF','GJ'))
    UF = arb_mat([[env['U'][i,j] for j in range(12)] for i in range(12)])
    EF = 2*(mat(case['finite_feature_error_gram']) + mat(raw['old_certificate']['joint_high_source_error_gram'])/e.w['delta'])
    rcoef = Ki*a*w
    vals = dict(ew=ew, uw=uw, dw=directional_d,
                gr=quad(GF,rcoef), ur=quad(UF,rcoef), er=quad(EF,rcoef), gw=quad(GJ,w),
                tpG=tr(P*GJ), tpU=tr(P*UJ), tpE=EJ*tr(P),
                tkG=tr(Ki*GF), tkU=tr(Ki*UF), tkE=tr(Ki*EF),
                a0_HS_squared=tr(P*a.transpose()*Ki*a), tpD=tr(P*DD))
    need(all(v >= 0 for v in vals.values()), 'Nonnegative Gram ingredients')
    rootn = eng.norm_upper
    dd = e.bounds['direct_energy_relative_error_upper']
    vals['dd'] = dd
    gr, ur, er, gw = (vals[k] for k in ('gr','ur','er','gw'))
    tpG, tpU, tpE, tkG, tkU, tkE = (vals[k] for k in ('tpG','tpU','tpE','tkG','tkU','tkE'))
    ea = dd*rootn(tkG*gw)+rootn(tkU*ew)+rootn(tkE*uw)+rootn(tkE*ew)
    left = dd*rootn(gr*tpG)+rootn(tpU*er)+rootn(tpE*ur)+rootn(tpE*er)
    hs = dd*rootn(tkG*tpG)+rootn(tkU*tpE)+rootn(tkE*tpU)+rootn(tkE*tpE)
    square_error = left+(rootn(vals['a0_HS_squared'])+hs)*ea
    u_error = rootn(tpU*ew)+rootn(tpE*uw)+rootn(tpE*ew)
    d_error = rootn(vals['tpD']*directional_d)
    eta = q('1e-10')
    DJ = arb_mat([[(DU[i,j]+DL[i,j])/2 for j in range(12,96)] for i in range(12,96)])
    nmodel = env['nu']-env['H0']*w+eta*DJ*w
    vals['model_P_square'] = quad(P,nmodel)
    vals['pilot_P_weight'] = q(prior['P_weight'])
    vals['nu_feature_error'] = c.box(prior['feature_error_norms']['P_upper_J_star_nu'])
    vals['nu_whole_error'] = c.box(prior['residual_model_error_norm'])
    need(vals['model_P_square'] >= 0, 'Nonnegative model residual norm')
    nu_error = (vals['nu_feature_error']+vals['nu_whole_error'])/vals['pilot_P_weight'].sqrt()
    z = rootn(vals['model_P_square'])+nu_error+(1+eta)*d_error+u_error+square_error
    # Fixed simple constants are independently audited over the rationals.
    zcap, fcap, dcap = Q('0.00001'), Q('0.000053941654'), Q('0.000000019')
    need(Q(c.enc(z)[1]) < zcap and fup < fcap, 'Frozen conservative caps')
    cap, beta = Q(rest['c']), Q(rest['beta'])
    need(cap == Q(1977,500000) and beta == Q(20209999981781,182190000000000), 'Inherited inverse constants')
    x2 = q(dcap/beta)
    delta_cap = (x2+q(zcap*zcap)+2*(q(cap)*x2).sqrt()*q(zcap))/(1-q(cap))
    conditional_up = q(fcap)+delta_cap
    need(conditional_up < q(rest['budget_interval'][0]), 'Conditional complete comparison')
    scalars = dict(directional_U_price=directional_u, directional_D_price=directional_d,
                   a_direction_Ki_error=ea, a_left_P_error=left, a_error_HS=hs,
                   a_square_P_error=square_error, U_action_P_error=u_error,
                   D_action_P_error=d_error, nu_P_error=nu_error,
                   residual_P_norm=z, conditional_full_inverse_upper=conditional_up)
    result = dict(status='AUTHOR_DERIVED', review_status='EXTERNAL_REVIEW_OPEN', source_commit=BASE,
                outcome='RESIDUAL_CENTERED_FINITE_CONTROL_CERTIFIED_FULL_RESIDUAL_OPEN',
                test_vector_sha256=VECTOR, K_new_sha256=KNEW,
                physical_candidate_sha256=old['physical_candidate_sha256'],
                K_P_certificate_sha256=old['K_P_certificate_sha256'],
                F_interval=[str(flo),str(fup)], old_form_price_upper=str(old_price),
                directional_form_price_upper=str(new_price), budget_interval=rest['budget_interval'],
                budget_lower_minus_F_upper=str(Q(rest['budget_interval'][0])-fup),
                ingredients=c.encode(vals), finite_bounds=c.encode(scalars),
                F_upper_cap=str(fcap), residual_P_norm_cap=str(zcap),
                sufficient_whole_residual_Ldual_upper=str(dcap), c=str(cap), beta=str(beta),
                conditional_formula='F_cap+(d/beta+z_cap^2+2*sqrt(c*d/beta)*z_cap)/(1-c)',
                whole_residual='r=nu-H_new Jw on the complete exact T',
                whole_residual_energy_computed=False, full_inverse_upper_computed=False,
                conditional_threshold_satisfied_by_actual_residual=None,
                whole_comparison_pass=False, underform_excluded=False,
                new_integration=False, new_physical_direction=False, test_vector_changed=False,
                N12_closed=False, milestone_4_closed=False)
    force = module('bound_whole_force_control', data['force_engine'],
                   root/spec['files']['force_engine']['path'])
    result['whole_force_transport'] = force.run(root,data,env,module)
    return result
