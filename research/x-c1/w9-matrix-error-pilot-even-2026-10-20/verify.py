"""One frozen #245 matrix-error pilot; no search, integration or dual evaluation."""
import argparse
import gzip
import hashlib
import json
import subprocess
import sys
import time
from fractions import Fraction as Q
from pathlib import Path
from types import ModuleType, MappingProxyType
from flint import arb, arb_mat, ctx

HERE=Path(__file__).resolve().parent
OUTPUTS=('SCHUR.json','RESULT.json')
STEP=Q(13,10**8)
C_RESIDUAL=Q(1977,500000)
B_WEIGHT=Q(51,50)
A_WEIGHT=Q(500000,399173)
FROZEN_K='89ded551059d1279c646bc17e3b5ab3e2a7f7a261d1c239ac752b7f0d35467a8'


def need(ok,message):
    if not ok: raise RuntimeError(message)


def sha(raw): return hashlib.sha256(raw).hexdigest()


def module(name,raw,path):
    value=ModuleType(name);value.__file__=str(path)
    sys.modules[name]=value
    exec(compile(raw,str(path),'exec'),value.__dict__)
    return value


def snapshot(root,raw):
    spec=json.loads(raw); data={}
    for alias,e in spec['files'].items():
        path=(root/e['path']).resolve()
        need(path.is_relative_to(root),'Escaping input path')
        buf=path.read_bytes();need(sha(buf)==e['sha256'],'Input binding: '+alias)
        data[alias]=buf
    common=module('common',data['common'],root/spec['files']['common']['path'])
    need(common.ROOT==root,'Inherited repository root')
    inputs=common.Inputs(binding_bytes=data['inherited_inputs'])
    return common,inputs,MappingProxyType(data),spec


def rational_upper(matrix,digits=60):
    """Symmetric midpoint plus row-radius diagonal and 10^-40 strict pad."""
    n=matrix.nrows();grid=10**digits;boxes=[]
    for i in range(n):
        row=[]
        for j in range(n):
            x=matrix[i,j];need(x.is_finite(),'Nonfinite Schur solution')
            lo=Q(str(x.lower().fmpq()))*grid;hi=Q(str(x.upper().fmpq()))*grid
            row.append((Q(lo.numerator//lo.denominator,grid),Q(-((-hi.numerator)//hi.denominator),grid)))
        boxes.append(row)
    out=[[(lo+hi)/2 for lo,hi in row] for row in boxes]
    for i in range(n):out[i][i]+=sum((hi-lo)/2 for lo,hi in boxes[i])+Q(1,10**40)
    need(all(out[i][j]==out[j][i] for i in range(n) for j in range(n)),'Asymmetric rational P')
    return [[str(x) for x in row] for row in out]


def run(root,checked):
    common,inp,data,spec=snapshot(root,checked['INPUT_BINDINGS.json'])
    decision=module('bound_decision',data['decision_verifier'],root/spec['files']['decision_verifier']['path'])
    decision_result=decision.run(root,data['decision_inputs'])
    need(decision_result==json.loads(data['decision_expected']),'Bound K admissibility replay')
    ctx.prec=1024
    q,mat,ratmat,trace=common.q,common.mat,common.ratmat,common.trace
    source=inp.json('common')['cases'][0];co=inp.json('coherent')['parities']['even']
    inv=inp.json('inverse_even');need(inv['parity']=='even','Inverse parity')
    receipt=json.loads(data['closure_acceptance'])['reserve_review']['independent_rational_review']
    need(receipt['source_zip_sha256']=='65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba','Full residual provenance')
    cap=next(v for v in receipt['cases'] if v['parity']=='even')
    need(Q(cap['new_simple_cap'])==C_RESIDUAL,'Fixed complete residual cap')
    need(Q(cap['new_complete_QR_upper'])<C_RESIDUAL<Q(inv['residual_cap'])<Q(1,121),'Full residual cap hierarchy')
    need(Q(cap['beta'])==Q(inv['beta']),'Inherited beta')
    a_weight=A_WEIGHT
    need(a_weight*(1-C_RESIDUAL)>1 and B_WEIGHT*(1-C_RESIDUAL)>1 and
         (a_weight*(1-C_RESIDUAL)-1)*(B_WEIGHT*(1-C_RESIDUAL)-1)==C_RESIDUAL,
         'Exact Young-weight admissibility')
    gf=[r[:12] for r in source['G96_rational'][:12]]
    old_star=[[str(Q(co['K_rational'][i][j])+STEP*Q(gf[i][j])) for j in range(12)]for i in range(12)]
    need(sha(json.dumps(old_star,separators=(',',':')).encode())==decision_result['K_preliminary_certificate']['K_star_canonical_rows_sha256'],'Inherited K-star changed')
    selected=json.loads(data['selection_expected'])
    selected_audit=module('bound_selection_audit',data['selection_audit'],root/spec['files']['selection_audit']['path'])
    selected_audit.check(selected)
    need(selected['K_star_rational']==old_star,'K-star provenance')
    ks=selected['K_new_rational']
    need(sha(json.dumps(ks,separators=(',',':')).encode())==FROZEN_K==selected['K_new_canonical_sha256'],'Frozen K-new changed')
    # Reconstruct the same matrix-Young enclosure, without selecting or searching.
    selected_code=module('bound_selection_code',data['selection_verifier'],root/spec['files']['selection_verifier']['path'])
    U=mat(source['U96_model']); DL=mat(source['D96_lower_model'])
    U=arb_mat([[U[i,j] for j in range(12)] for i in range(12)])
    DL=arb_mat([[DL[i,j] for j in range(12)] for i in range(12)])
    eps=Q(selected['epsilon'])
    need(eps==selected_code.EPSILON,'Frozen epsilon')
    ceiling=DL-(1+q(eps))*U-q(1+1/eps)*mat(source['finite_feature_error_gram'])
    rebuilt,ceiling_box=selected_code.rational_lower(ceiling)
    need(rebuilt==ks and ceiling_box==selected['K_ceiling_enclosure'],'Candidate enclosure replay')
    need(Q(selected['weights']['a'])==A_WEIGHT and Q(selected['weights']['b'])==B_WEIGHT
         and Q(selected['weights']['c'])==C_RESIDUAL,'Frozen weights changed')
    need(Q(selected['weights']['beta'])==Q(inv['beta']),'Frozen beta')
    er=[[Q(v) for v in row]for row in inv['E_rational']]
    need(len(er)==203 and all(len(r)==203 for r in er),'E dimensions')
    for i in range(12):
        for j in range(12):er[191+i][191+j]+=Q(ks[i][j])-Q(co['K_rational'][i][j])
    need(all(er[i][j]==er[j][i]for i in range(203)for j in range(203)),'E symmetry')
    E=ratmat(er);X=ratmat(inv['X84x203_rational'])
    need(X.nrows()==84 and X.ncols()==203,'X dimensions')
    print('1024-bit solve: E_new Y = X_ans* (203 x 84)',flush=True)
    Y=E.solve(X.transpose())
    P=X*Y;P=(P+P.transpose())/2
    ps=rational_upper(P)
    audit=module('bound_rational_audit',data['rational_auditor'],root/spec['files']['rational_auditor']['path'])
    xr=inv['X84x203_rational']
    block=[[audit.point(er[i][j]) if i<203 and j<203 else
            audit.point(xr[j-203][i]) if i<203 else
            audit.point(xr[i-203][j]) if j<203 else audit.point(ps[i-203][j-203])
            for j in range(287)]for i in range(287)]
    print('Directed rational audit: complete 287 x 287 block',flush=True)
    certificate=audit.positive(block,True)
    need(certificate['positive_pivots']==287,'Incomplete audit')
    weights=module('pilot_weights',data['pilot_weights'],root/spec['files']['pilot_weights']['path'])
    energy_module=module('pilot_energy',data['pilot_energy'],root/spec['files']['pilot_energy']['path'])
    pairs=json.loads(gzip.decompress(data['pairs_even']));pairs['_source_sha256']=sha(data['pairs_even'])
    candidate=json.loads(data['candidate_even']);kp=json.loads(data['kp_even'])
    need(sha(data['candidate_even'])==selected['physical_candidate_sha256'],'Frozen physical witness')
    need(sha(data['kp_even'])==selected['budget_sha256'],'Frozen budget')
    energy=energy_module.Energy(inp,pairs,ratmat(ks),ratmat(ps),q(B_WEIGHT))
    # Common F-J/a_fin errors are reconstructed with their ORIGINAL formulas;
    # the new F-only admissibility cap must not enter these prices.
    old_weights=json.loads(data['weights'])['even']
    for key in ('common_U_energy_relative_error_upper','direct_energy_relative_error_upper','a_fin_relative_error_upper'):
        need(energy.bounds[key].overlaps(common.box(old_weights[key])),'Changed common error: '+key)
    result=energy.certificate(candidate['raw_coefficients'],kp['K_P_interval'],'frozen_even_matrix_error_K_pilot')
    elo,ehi=map(Q,result['partial_actual_energy_interval']);klo,khi=map(Q,kp['K_P_interval'])
    need(klo<=khi and elo<=ehi,'Interval order')
    outcome=('PILOT_COMPARISON_EXCLUDED' if elo>khi else
             'PILOT_PARTIAL_PASS' if ehi<klo else 'PILOT_INCONCLUSIVE')
    beta=Q(inv['beta']);need(beta>0 and 0<C_RESIDUAL<Q(1,121),'Residual parameters')
    result.update(status='AUTHOR_DERIVED',review_status='EXTERNAL_REVIEW_OPEN',
                  source_commit=spec['source_commit'],outcome=outcome,
                  budget_interval=kp['K_P_interval'],K_P_certificate_sha256=sha(data['kp_even']),
                  candidate_sha256=sha(data['candidate_even']),
                  energy_minus_budget_interval=[str(elo-khi),str(ehi-klo)],
                  partial_pass_reserve=str(klo-ehi)if outcome=='PILOT_PARTIAL_PASS'else None,
                  sufficient_actual_dual_energy_upper=str(beta*(klo-ehi)/A_WEIGHT)if outcome=='PILOT_PARTIAL_PASS'else None,
                  partial_weight_bounds=energy.bounds,common_residual_Hilbert_errors=energy.residual_errors,
                  controls=energy.controls,beta=str(beta),residual_cap=str(C_RESIDUAL),
                  dual_weight=str(A_WEIGHT/beta),a_weight=str(A_WEIGHT),P_weight=str(B_WEIGHT),
                  a_fin_error_paid_once=True,common_FJ_errors_retained=True,
                  frozen_response_changed=False,frozen_direction_changed=False,K_P_changed=False,
                  milestone_4_closed=False,new_integrations=False,
                  complete_287_block=certificate,
                  K_new_admissibility_positive_pivots=[12,12],K_new_canonical_sha256=FROZEN_K,
                  new_partial_norm_recomputed=True,
                  nu_new_direction=energy.nu*(arb_mat([[q(v)]for v in candidate['raw_coefficients']])/result['normalization']))
    schur={'status':'FULL_RATIONAL_BLOCK_CERTIFIED','parity':'even','bits':1024,
           'K_new_rational':ks,'P_new_upper_rational':ps,
           'E_new_definition':'bound E0 + diag(0_191, K_new - K_old)',
           'E_new_canonical_rows_sha256':sha(json.dumps([[str(v)for v in r]for r in er],separators=(',',':')).encode()),
           'X_ans_unchanged':True,'rounding_decimal_digits':60,'strict_diagonal_padding':'1/10000000000000000000000000000000000000000',
           'audit_decimal_digits':120,'complete_287_block':certificate}
    schur_raw=(json.dumps(schur,indent=2)+'\n').encode()
    result['SCHUR_sha256']=sha(schur_raw)
    raw=(json.dumps(common.encode(result),indent=2)+'\n').encode()
    print(outcome,flush=True)
    return {'SCHUR.json':schur_raw,'RESULT.json':raw}



def worker(args):
    need(__debug__,'Do not use python -O')
    checked={}
    if args.check:
        for name,digest in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            path=(HERE/name).resolve();need(path.is_relative_to(HERE),'Escaping package path')
            raw=path.read_bytes();need(sha(raw)==digest,'Package binding: '+name);checked[name]=raw
    else:
        checked['INPUT_BINDINGS.json']=(HERE/'INPUT_BINDINGS.json').read_bytes()
    root=(args.repository or HERE.parents[2]).resolve()
    need(json.loads(checked['INPUT_BINDINGS.json'])['source_commit']=='a60f7602335f654ca7b42e8362e47af243e20462','Frozen source head')
    out=run(root,checked)
    if args.check:
        for name,raw in out.items():need(raw==checked[name],'Replay differs: '+name)
        print('PASS: both pilot files byte-equal; complete 287 rational pivots positive',flush=True)
    if args.output_dir:
        args.output_dir.mkdir(parents=True,exist_ok=True)
        for name,raw in out.items():(args.output_dir/name).write_bytes(raw)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--check',action='store_true')
    ap.add_argument('--output-dir',type=Path)
    ap.add_argument('--repository',type=Path)
    ap.add_argument('--worker',action='store_true',help=argparse.SUPPRESS)
    args=ap.parse_args()
    need(__debug__,'Do not use python -O')
    need(args.check or args.output_dir,'Select check or output')
    if args.worker:
        worker(args)
        return
    start=time.monotonic()
    # A separate parent enforces the deadline on Windows and POSIX alike.
    try:
        completed=subprocess.run([sys.executable,'-u','-B',str(HERE/'verify.py'),
                                  *sys.argv[1:],'--worker'],timeout=1800,check=False)
    except subprocess.TimeoutExpired:
        print('PILOT_TECHNICAL_TIMEOUT: stopped at 30 minutes; no energy decision',flush=True)
        raise SystemExit(124)
    print('Complete elapsed seconds:',round(time.monotonic()-start,3),flush=True)
    raise SystemExit(completed.returncode)


if __name__=='__main__':main()
