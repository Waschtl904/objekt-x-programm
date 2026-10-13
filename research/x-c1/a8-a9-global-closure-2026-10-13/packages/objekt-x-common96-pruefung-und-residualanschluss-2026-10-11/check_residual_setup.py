"""Exact scalar setup for the new form-dual residual calculation.

The inherited global H_old <= .89 L and q >= L are hypotheses.
This does not certify the low-feature or finite-source losses on all T.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json

def dump(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,list):return [dump(v) for v in x]
    if isinstance(x,dict):return {k:dump(v) for k,v in x.items()}
    return x

def audit(root):
    read=lambda name:json.loads((root/name).read_bytes())
    source=read('REFINED_INPUT.json');refined=read('REFINED_COMMON96.json');a=read('AUDIT.json')
    olddelta=F(91,50);delta=F(18219,10000);eta=F(1,10**10)
    beta=1-eta-F(89,100)*olddelta/delta
    assert beta==F(20209999981781,182190000000000)>0
    floor=read('REFINED_HIGH_FLOOR.json')
    margin=F(floor['inherited']['raw_high_floor'])-16*F(1,10**6)-12*F(1,10**12)-delta*(1+F(1,10**12))
    assert margin==F(floor['exact_positive_margin'])>0
    rows=[]
    for p,label in enumerate(['EVEN','ODD']):
        d=read(f'DIRECT_REST_{label}_3072.json');n=refined['cases'][p];g=source['cases'][p]['galerkin']
        assert F(n['delta'])==delta and F(n['coupling_padding'])==F(1,10**10)
        count=0
        for i in range(84):
            for j in range(84):
                oldlo,oldhi=map(F,g['H84_model'][i][j]);lo,hi=map(F,n['H84_new_model'][i][j])
                assert max(lo,oldlo*olddelta/delta)<=min(hi,oldhi*olddelta/delta)
                count+=1
        # Include each numerical radius and the full analytic operator error.
        bound=max(sum(max(abs(F(lo)),abs(F(hi))) for lo,hi in row) for row in d['D84_direct_model'])+F(d['D84_operator_error'])
        cap=F(-((-bound.numerator)//bound.denominator))
        assert cap>=bound>0
        eps=F(n['common96_positive_reserve_relative_to_G'])
        assert eps==F(a['cases'][p]['common96_reserve_relative_to_diag_Kold_I84'])
        eps_eta=eps-eta*cap
        assert eps_eta>0
        rows.append({'parity':label.lower(),'high_model_scaling_interval_comparisons':count,
            'direct84_norm_upper':bound,'direct84_integer_norm_upper':cap,
            'common96_reserve':eps,'eta_direct84_price_upper':eta*cap,
            'common96_reserve_after_optional_eta_on_tail':eps_eta,
            'finite_reserve_metric':'diag(K12_old,I84)','full_remainder_certified':False})
        print(label,'D84 norm <=',cap,'96D reserve after eta >=',eps_eta,flush=True)
    names=['REFINED_INPUT.json','REFINED_COMMON96.json','AUDIT.json','REFINED_HIGH_FLOOR.json',
           'DIRECT_REST_EVEN_3072.json','DIRECT_REST_ODD_3072.json']
    return dump({'status':'PASS_NEW_RESIDUAL_FORM_SCALAR_SETUP','delta_old':olddelta,'delta_new':delta,
        'exact_high_floor_margin':margin,'eta':eta,'H_new_over_H_old':olddelta/delta,
        'S_eta_new_lower_relative_L':beta,'new_R_L_inverse_majorant_factor':1/beta,
        'inherited_global_hypotheses':['H_old <= 89/100 L on exact T','q_b[Lambda r] >= L[r] on exact T'],
        'auxiliary_form_only_not_final_tail_floor':True,'cases':rows,
        'sources':{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in names},
        'new_full_formdual_residual_certified':False,'full_remainder_certified':False})

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    args.out.write_text(json.dumps(audit(args.root),indent=2)+'\n')
