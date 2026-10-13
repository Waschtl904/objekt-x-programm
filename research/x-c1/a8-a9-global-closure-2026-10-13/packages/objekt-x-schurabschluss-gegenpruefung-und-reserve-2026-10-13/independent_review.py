"""Independent exact scalar reconstruction of the complete Schur closure.

Reads only the fixed source ZIP. No imported assembly code, floating
arithmetic, eigensolver, or finite truncation of an infinite residual.
The analytic enclosures are bound hypotheses, checked by the chain replay.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, io, json, zipfile

INPUT_SHA='65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba'

def member(z,suffix):
    names=[n for n in z.namelist() if n==suffix or n.endswith('/'+suffix)]
    if len(names)!=1: raise ValueError((suffix,names))
    return z.read(names[0])

def read(z,suffix): return json.loads(member(z,suffix))
def child(z,name,want=None):
    data=member(z,name)
    if want is not None: assert hashlib.sha256(data).hexdigest()==want
    return zipfile.ZipFile(io.BytesIO(data))

def inverse2(a):
    det=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det>0
    return [[a[1][1]/det,-a[0][1]/det],[-a[1][0]/det,a[0][0]/det]]

def controls():
    K=[[F(2),F(1)],[F(1),F(3)]]
    actual=[[F(3),F(1,2)],[F(1,2),F(4)]]
    Ki,Ai=inverse2(K),inverse2(actual)
    difference=[[Ki[i][j]-Ai[i][j] for j in range(2)] for i in range(2)]
    assert difference[0][0]>0
    assert difference[0][0]*difference[1][1]-difference[0][1]**2>0
    assert Ai[0][0]-Ki[0][0]<0  # Reversing the inverse inequality fails.
    beta=F(1,3); L=F(2); S=F(1)
    assert S>=beta*L and 1/S<=1/(beta*L)
    assert not 1/S<=beta/L  # beta, rather than beta^-1, is invalid.
    log,regular=F(1,10),F(3,10)
    assert (log+regular)**2>log**2+regular**2
    for z,r in [(F(-1),F(2)),(F(2),F(-3)),(F(5,7),F(-2,11))]:
        k,c,t=F(2),F(1),F(3)
        assert k*z*z+2*c*z*r+t*r*r==k*(z+c*r/k)**2+(t-c*c/k)*r*r
    return {'inverse_order_reversal_rejected':True,
            'missing_inverse_beta_rejected':True,
            'omitted_log_cross_term_rejected':True,
            'exact_schur_completion_controls':3}

def review(path):
    with path.open('rb') as f: digest=hashlib.file_digest(f,'sha256').hexdigest()
    assert digest==INPUT_SHA
    outer=zipfile.ZipFile(path)
    bindings=read(outer,'INPUT_BINDINGS.json'); original=read(outer,'ASSEMBLY_AUDIT.json')
    zips={k:child(outer,b['filename'],b['sha256']) for k,b in bindings.items() if k!='common'}
    target=read(zips['logreview'],'data/DIRECTIONAL_DERIVATIVE_TARGET.json')
    assert target==read(zips['gram'],'snapshot/work/global-model-2026-10-12/DIRECTIONAL_DERIVATIVE_TARGET.json')
    inner=child(zips['logreview'],'Objekt-X-Innere-Randterme-und-Gemeinsamer-Logrest-2026-10-12.zip')
    outerlog=child(inner,'Objekt-X-Aussenresidualpruefung-und-Logarithmischer-Randtail-2026-10-11.zip')
    exterior=child(outerlog,'Objekt-X-Zusammengesetzte-Aussenresiduen-und-Momentanschluss-2026-10-11.zip')
    gates=read(exterior,'ATTACHMENT_GATES.json')['cases']
    exterior_audit=read(exterior,'AUDIT_EXTERIOR.json')['cases']
    d=F(11,10)+sum((F(1,n) for n in range(1,105)),F(0))
    assert d>6 and d-F(1,104)==F(11,10)+sum((F(1,n) for n in range(1,104)),F(0))
    cases=[]
    for i,label in enumerate(['EVEN','ODD']):
        r=read(zips['responses'],f'RESPONSES_{label}.json')
        t=target['cases'][i]; g=gates[i]; x=exterior_audit[i]; old=original['cases'][i]
        audit=read(zips['gram'],f'data/AUDIT_{label}_3072.json')
        assert all(v['parity']==label.lower() for v in [t,g,x,old,audit])
        beta=1-F(r['eta'])-F(16198,18219)
        assert beta==F(r['beta'])==F(old['beta'])>0
        u=F(r['M_actual_normalized_upper_scalar']); sigma=beta*(1-u)
        assert 0<u<1 and sigma==F(r['sufficient_complete_QR_normalized_budget'])
        j=F(g['basis84_dual_contribution_relative_to_D_upper'])
        assert j==F(x['basis84_dual_price_relative_to_D'])==F(old['basis84_price_relative_D'])
        e=j+F(1,10**300)
        assert 0<=F(g['geometric_correction_computed_upper'])<F(1,10**300)
        c8=F(x['actual_first_eight_weighted_gram_relative_to_directional_budget_upper'])
        clog=F(t['joint_log_upper_relative_to_T']); theta=F(t['young_parameter'])
        assert c8==[F(1,5000),F(13,20000)][i]
        assert clog==[F(1,500),F(1,250)][i] and theta==[F(21),F(15)][i]
        q=F(3,10000); s=[F(3,8),F(4,15)][i]
        assert F(audit['actual_regularized_Gram_relative_H_upper'])<q
        # Reconstruct all three coefficients of the exact H identity.
        a=F(t['derivative_target_coefficient_T'])/10920
        b=F(t['derivative_target_subtracted_coefficient_D'])/10920
        c=F(t['derivative_target_subtracted_coefficient_CtGC'])/10920
        qC=F(t['weighted_joint_log_upper_coefficient_CtGC'])
        qD=F(t['weighted_joint_log_upper_coefficient_D'])
        assert qC>0 and qD>=0
        assert a==d*theta/(1+theta)*(1-c8)
        assert b==d*theta/(1+theta)*e+d*theta*qD
        assert c==d*theta*qC
        inherited_cap=[F(1,250),F(71,10000)][i]
        loose=e/sigma+c8+(1+s)*clog+(1+1/s)*q*theta/(1+theta)*(1-c8)
        assert loose==F(old['complete_QR_relative_T_scalar_upper'])<inherited_cap
        # Substitute H BEFORE taking scalar majorants. Keep its negative
        # D and Qlog terms; the remaining three coefficients are positive.
        f=(1+1/s)*q*theta/(1+theta)
        coeff_D=1-f; coeff_T=c8+f*(1-c8); coeff_log=1+s-f*(1+theta)
        assert coeff_D>0 and coeff_T>0 and coeff_log>0
        tight=coeff_D*e/sigma+coeff_T+coeff_log*clog
        assert loose-tight==f*e/sigma+f*(1+theta)*clog>0
        # Also verify the noncommutative matrix identity coefficientwise
        # in the formal basis (D,T,C0*G*C0), using rational arithmetic.
        factor=(1+1/s)*q/d
        assert e+(1+s)*qD-factor*b==coeff_D*e+coeff_log*qD
        assert c8+factor*a==coeff_T
        assert (1+s)*qC-factor*c==coeff_log*qC
        cap=[F(1977,500000),F(6967,10**6)][i]
        assert tight<cap<inherited_cap<1
        old_kappa=(1-inherited_cap)*(1-u)
        assert old_kappa==F(old['ASinvAstar_gap_relative_D'])
        old_floor=F(21,5)*(F(r['eta'])+old_kappa*beta)
        assert old_floor==F(old['reduced_comparison_form_lower_relative_WX'])
        assert old_floor>F(old['simple_lower_relative_WX'])>0
        kappa=(1-cap)*(1-u)
        # Two equivalent expansions independently verify the gap sign.
        assert 1-kappa==cap+(1-cap)*u
        Lfloor=F(r['eta'])+kappa*beta; Wfloor=F(21,5)*Lfloor
        easy=[F(13285,10**10),F(79795,10**10)][i]
        assert Wfloor>easy>F(old['simple_lower_relative_WX'])
        cases.append({'parity':label.lower(),'d104':str(d),'beta':str(beta),'sigma':str(sigma),
            'inherited_full_QR_upper':str(loose),'inherited_simple_cap':str(inherited_cap),
            'substitution_factor_f':str(f),'coefficient_D':str(coeff_D),
            'coefficient_T':str(coeff_T),'coefficient_Qlog':str(coeff_log),
            'new_complete_QR_upper':str(tight),'new_simple_cap':str(cap),
            'new_ASinvAstar_gap_relative_D':str(kappa),
            'new_Schur_floor_relative_L':str(Lfloor),'new_Schur_floor_relative_WX':str(Wfloor),
            'new_simple_Schur_floor_relative_WX':str(easy),
            'original_203_pivots':old['final_203x203_directional_LDL']['positive_pivots'],
            'original_gap_203_pivots':old['M_upper_scalar_gap_LDL']['positive_pivots']})
        assert cases[-1]['original_203_pivots']==cases[-1]['original_gap_203_pivots']==203
        print(label,'PASS independent exact full residual bound',str(cap),flush=True)
    return {'status':'PASS_INDEPENDENT_SCHUR_REVIEW_AND_TIGHTER_SCALAR_CLOSURE',
        'source_zip_sha256':digest,'cases':cases,'countercontrols':controls(),
        'conditional_A8_to_A9_positivity_confirmed':True,
        'inherited_analytic_operator_domain_and_complete_decomposition_hypotheses_required':True,
        'new_203_matrix_LDL_executed_by_this_script':False,
        'method':'Exact coefficientwise identity plus positive scalar combinations of bound global matrix inequalities.',
        'tail_floor_1_over_20_certified':False,'all_horizons_certified':False,
        'object_X_constructed':False,'RH_proved':False,'external_mathematical_review_open':True}

if __name__=='__main__':
    if not __debug__: raise RuntimeError('Run without Python optimization flags.')
    ap=argparse.ArgumentParser();ap.add_argument('--input-zip',type=Path,required=True)
    ap.add_argument('--receipt',type=Path,required=True);args=ap.parse_args()
    result=review(args.input_zip)
    args.receipt.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(result['status'],flush=True)
