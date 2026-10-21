"""Independent rational final audit; no midpoint or coordinate upper bounds."""
import hashlib,json,sys
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
HERE=Path(__file__).resolve().parent

def need(ok,msg):
    if not ok:raise RuntimeError(msg)

def upper(v):
    need(len(v)==2 and Q(v[0])<=Q(v[1]),'Ordered interval')
    return Q(v[1])

def sqrt_up(v):
    v=Q(v);need(v>=0,'Nonnegative square')
    grid=10**100;u=v*grid**2;n=isqrt(u.numerator//u.denominator)
    if n*n<u:n+=1
    out=Q(n,grid);need(out*out>=v,'Outward square root')
    return out

def audit(folder):
    read=lambda name:json.loads((folder/name).read_bytes())
    finite=read('force-results/RESULT.json')
    controls=read('analytic-caps.json')
    need(controls['status']=='ANALYTIC_CAP_INGREDIENTS_DIRECTED_PASS','Analytic ingredients')
    need(controls['caps']['raw_g_X_operator']==100 and controls['caps']['modeled_u_H8_norm']=='1e20','Whole caps')
    need(controls['caps']['outer_endpoint_envelope']=='1e20*(1+log(v)^2)','Tail envelope')
    need(upper(controls['values']['outer_endpoint_coefficient'])<Q('1e20'),'Endpoint coefficient')
    need(upper(controls['values']['raw_g_X_operator'])<100,'Whole g')
    need(upper(controls['values']['u_H8_bound'])<Q('1e20'),'Modeled u')
    cuts=read('cut-audit.json')
    need(cuts['status']=='EXACT_LOG_CUT_COVERAGE_PASS' and cuts['outer_count']==4 and cuts['core_count']==18,'All prime cuts')
    bind=read('taylor-model-panels-205/BINDING.json')
    for key,name in [('source','whole_function_probe.py'),('cache','whole-model-ed58da3caacd.json.gz'),('evaluator','taylor_model.py'),('fast_evaluator','fast_evaluation.py')]:
        need(hashlib.sha256((folder/name).read_bytes()).hexdigest()==bind[key],'Model binding '+key)
    need(bind['panels']==205,'Tail depth')
    total=Q(0)
    for i in range(411):
        item=read(f'taylor-model-panels-205/{i:04d}.json')
        need(item['index']==i and item['status']=='DIRECTED_STORED_MODEL_PANEL_ONLY','Panel identity')
        need(upper(item['midpoint_control'])<Q('1e-15'),'Point control')
        need(upper(item['series_integral'])>=0 and 1<=item['order']<=1536,'Panel norm and order')
        total+=upper(item['model_Xnorm_squared_upper'])
    norm=read('taylor-model-panels-205/SUMMARY.json')
    need(norm['panels']==411 and total<=upper(norm['interior_upper']),'Complete interior sum')
    model=upper(norm['model_Xnorm_squared_conditional_upper'])
    need(total+upper(norm['endpoint_upper_conditional'])<=model+Q('1e-65'),'Tail addition')
    need(model<Q('1e-10'),'Model X norm cap')
    bridge=read('core-model-bridge.json');eb=upper(bridge['full_X_difference_bound'])
    core=read('core-quadrature-control-128.json');ec=upper(core['total_outer_X_error_upper_expression'])
    need(eb<Q('1e-20') and ec<Q('1e-7'),'Complete quadrature and bridge')
    ledger=read('whole-error-ledger.json');eo=upper(ledger['values']['proposed_Ldual_error'])
    need(eo<Q('1e-5'),'Whole operator/model error')
    force=finite['whole_force_transport']
    need(Q(force['force_cap'])==10 and upper(force['values']['full_force_operator_upper'])<10,'Whole force')
    normup=sqrt_up(Q(5,21))*(sqrt_up(model)+eb+ec)+eo
    d=normup**2;dcap=Q('1e-9');need(d<dcap,'Actual whole residual cap')
    fcap=Q(finite['F_upper_cap']);zcap=Q(finite['residual_P_norm_cap'])
    need(upper(finite['F_interval'])<fcap and upper(finite['finite_bounds']['residual_P_norm'])<zcap,'Finite caps')
    beta=Q(finite['beta']);c=Q(finite['c']);need(beta>0 and 0<c<1,'Inverse constants')
    full=fcap+(dcap/beta+zcap*zcap+2*zcap*sqrt_up(c*dcap/beta))/(1-c)
    blo=Q(finite['budget_interval'][0]);need(full<blo,'Full fixed-witness comparison')
    inputs={str(p.relative_to(folder)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in [folder/n for n in ('analytic-caps.json','cut-audit.json','core-model-bridge.json','core-quadrature-control-128.json','whole-error-ledger.json')]+[folder/'taylor-model-panels-205/SUMMARY.json']}
    return {'status':'AUTHOR_DERIVED_EXTERNAL_REVIEW_OPEN',
            'outcome':'FIXED_EVEN_RESIDUAL_CENTERED_COMPARISON_PASS',
            'scope':'Same fixed even physical witness, K_new, answer rule and variational vector as #248.',
            'model_X_norm_squared_upper':str(model),'core_bridge_X_error_upper':str(eb),
            'core_quadrature_X_error_upper':str(ec),'whole_operator_model_Ldual_error_upper':str(eo),
            'actual_whole_residual_Ldual_norm_upper':str(normup),
            'actual_whole_residual_Ldual_energy_upper':str(d),
            'conservative_actual_residual_energy_cap':str(dcap),
            'full_comparison_energy_upper':str(full),'budget_lower':str(blo),
            'strict_margin_lower':str(blo-full),'whole_residual_energy_upper_proved':True,
            'finite_coordinate_upper_substitution_used':False,'model_mesh_difference_used_as_quadrature_bound':False,
            'panels':411,'input_receipts':inputs,
            'milestone_4_closed':False,'N12_closed':False,'Object_X_constructed':False,
            'external_review':'OPEN','old_fixed_Young_family_exclusion_retracted':False}

if __name__=='__main__':
    result=audit(HERE)
    (HERE/'WHOLE_RESULT.json').write_bytes((json.dumps(result,indent=2)+'\n').encode())
    print(result['outcome'],flush=True)
    for key in ('actual_whole_residual_Ldual_energy_upper','full_comparison_energy_upper','budget_lower','strict_margin_lower'):
        print(key,float(Q(result[key])),flush=True)
