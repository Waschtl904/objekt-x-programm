"""Independent rational endpoint and square-root audit, without Arb."""
from fractions import Fraction as Q
from math import isqrt


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sqrt_up(x):
    x = Q(x)
    need(x >= 0, 'Negative square')
    grid = 10**100
    scaled = x*grid*grid
    n = isqrt(scaled.numerator//scaled.denominator)
    if n*n < scaled:
        n += 1
    out = Q(n,grid)
    need(out*out >= x, 'Square root outward')
    return out


def check(r, old, rest):
    def up(v):
        need(len(v)==2 and Q(v[0]) <= Q(v[1]), 'Ordered interval')
        return Q(v[1])
    v = {k:up(x) for k,x in r['ingredients'].items()}
    need(all(x>=0 for x in v.values()), 'Nonnegative ingredients')
    b = {k:up(x) for k,x in r['finite_bounds'].items()}
    prod = lambda a,b: sqrt_up(v[a]*v[b])
    du = 2*prod('uw','ew')+v['ew']
    # A small rational pad only absorbs different outward evaluation orders.
    pad = Q(1,10**65)
    need(du <= b['directional_U_price']+pad, 'U form arithmetic')
    need(v['dw'] <= b['directional_D_price']+pad, 'D form arithmetic')
    price = Q(r['directional_form_price_upper'])
    need(du+v['dw'] <= price, 'Common form price: strict outward bound')
    oldprice = Q(old['form_common_D_U_error'][1])
    need(Q(r['old_form_price_upper']) == oldprice, 'Old exact upper price')
    need(list(map(Q,r['F_interval'])) == [Q(rest['F_interval'][0])+oldprice-price,
                                       Q(rest['F_interval'][1])-oldprice+price], 'F endpoint replacement')
    dd = v['dd']
    ea = dd*prod('tkG','gw')+prod('tkU','ew')+prod('tkE','uw')+prod('tkE','ew')
    left = dd*prod('gr','tpG')+prod('tpU','er')+prod('tpE','ur')+prod('tpE','er')
    hs = dd*prod('tkG','tpG')+prod('tkU','tpE')+prod('tkE','tpU')+prod('tkE','tpE')
    square = left+(sqrt_up(v['a0_HS_squared'])+hs)*ea
    uerr = prod('tpU','ew')+prod('tpE','uw')+prod('tpE','ew')
    derr = prod('tpD','dw')
    # Divide by a rational lower square-root enclosure.
    weightlo = Q(r['ingredients']['pilot_P_weight'][0])
    den = weightlo/sqrt_up(weightlo)
    nu = (v['nu_feature_error']+v['nu_whole_error'])/den
    z = sqrt_up(v['model_P_square'])+nu+(1+Q('1e-10'))*derr+uerr+square
    for k,x in [('a_direction_Ki_error',ea),('a_left_P_error',left),('a_error_HS',hs),
                ('a_square_P_error',square),('U_action_P_error',uerr),('D_action_P_error',derr),
                ('nu_P_error',nu),('residual_P_norm',z)]:
        need(x <= b[k]+pad, 'Finite error arithmetic: '+k)
    zcap, fcap, dcap, c, beta = map(Q,(r['residual_P_norm_cap'],r['F_upper_cap'],
                                    r['sufficient_whole_residual_Ldual_upper'],r['c'],r['beta']))
    need(0 <= z < zcap and Q(r['F_interval'][1]) < fcap and dcap>0 and 0<c<1 and beta>0, 'Strict caps')
    full = fcap+(dcap/beta+zcap*zcap+2*zcap*sqrt_up(c*dcap/beta))/(1-c)
    budgetlo = Q(r['budget_interval'][0])
    need(full < budgetlo, 'Conditional whole comparison with full cross term')
    need(not r['whole_residual_energy_computed'] and not r['whole_comparison_pass']
         and r['conditional_threshold_satisfied_by_actual_residual'] is None, 'No invented whole residual')
    need(not r['milestone_4_closed'] and not r['N12_closed'], 'Scope')
    force=r['whole_force_transport']; fv={k:up(x)for k,x in force['values'].items()}
    need(fv['regular_kernel_abs_upper']<2 and fv['Q8_m_upper']<100
         and fv['local_degree95_Q_upper']<10000,'Whole force elementary caps')
    S=(1-Q('1e-10'))*sqrt_up(Q(5,21))*fv['QJ_response_HS_upper']
    S+=sqrt_up(Q(16198,18219)*fv['high_response_trace_upper'])
    force_upper=S+sqrt_up(c*beta*fv['trace_Dinv_E'])
    need(force_upper<Q(force['force_cap'])==10,'Whole force transport cap')
    need(not force['whole_residual_error_inventory_complete']
         and force['does_not_bound_actual_residual_energy'],'Force scope')
    return {'status':'PASS_INDEPENDENT_RATIONAL_SCALAR_AUDIT',
            'conditional_upper_rational':str(full), 'conditional_margin_lower':str(budgetlo-full),
            'whole_force_upper_rational':str(force_upper),
            'scope':'Arithmetic on directed matrix-derived scalar inputs, not external analytic review'}
