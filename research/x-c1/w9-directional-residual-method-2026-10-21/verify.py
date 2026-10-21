"""Fixed-vector method pilot. No integration, candidate search, or N12 claim."""
import argparse
import gzip
import hashlib
import io
import json
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
from zipfile import ZipFile
from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
BASE = '639d25e38b453f2e10b859553ca49a7a0e4fafdb'

def need(ok, message):
    if not ok:
        raise ValueError(message)

def sha(raw): return hashlib.sha256(raw).hexdigest()
def dump(value): return (json.dumps(value, indent=2)+'\n').encode()
def q(v):
    v=Q(v)
    return arb(v.numerator)/v.denominator
def box(v):
    need(Q(v[0]) <= Q(v[1]), 'Reversed interval')
    return q(v[0]).union(q(v[1]))
def mat(rows): return arb_mat([[box(v) for v in row] for row in rows])
def ratmat(rows): return arb_mat([[q(v) for v in row] for row in rows])
def trace(A): return sum((A[i,i] for i in range(A.nrows())),arb(0))
def sub(A,I,J): return arb_mat([[A[i,j] for j in J] for i in I])
def quad(A,v): return (v.transpose()*A*v)[0,0]
def enc(x):
    need(x.is_finite(),'Nonfinite interval')
    scale=10**80
    lo=Q(str(x.lower().fmpq()))*scale
    hi=Q(str(x.upper().fmpq()))*scale
    return [str(Q(lo.numerator//lo.denominator,scale)),
            str(Q(-((-hi.numerator)//hi.denominator),scale))]
def upnorm(x):
    need(x.is_finite() and x.upper() >= 0,'Invalid norm square')
    return x.upper().sqrt()
def sqrt_upper(x):
    x=Q(x); need(x>=0,'Negative square')
    scale=10**80
    k=isqrt(x.numerator*scale*scale//x.denominator)
    if Q(k*k,scale*scale)<x: k+=1
    return Q(k,scale)

def snapshot(root, bindings):
    need(__debug__,'python -O is not allowed')
    spec=json.loads(bindings); need(spec['source_commit']==BASE,'Wrong base')
    data={}
    for alias,e in spec['files'].items():
        p=(root/e['path']).resolve()
        need(p.is_relative_to(root),'Escaping input')
        raw=p.read_bytes();need(sha(raw)==e['sha256'],'Hash mismatch: '+alias)
        data[alias]=raw
    inherited=json.loads(data['partial_bindings'])
    archive=data['stage3_archive']
    need(sha(archive)==inherited['files']['stage3_archive']['sha256'],'Archive binding')
    with ZipFile(io.BytesIO(archive)) as z:
        for alias in ('common','old_sources'):
            e=inherited['members'][alias]
            need(e['archive']=='stage3_archive','Unexpected archive')
            raw=z.read(e['member']);need(sha(raw)==e['sha256'],'Member hash: '+alias)
            data[alias]=gzip.decompress(raw)
    return data

def scalar_pilot(data):
    a=json.loads(data['schur_result']);b=json.loads(data['rest_result'])
    p=json.loads(data['pilot_result'])
    need(a['test_vector_sha256']==b['test_vector_sha256']==sha(data['candidate']),'Fixed w')
    need(a['K_new_sha256']==b['K_new_sha256']==p['K_new_canonical_sha256'],'Fixed K')
    need(a['budget_interval']==b['budget_interval']==p['budget_interval'],'Fixed budget')
    need(sha(data['pilot_matrix'])==p['SCHUR_sha256'],'Bound P certificate')
    need(p['complete_287_block']['positive_pivots']==287,'Inherited P audit')
    g=a['form_refinement']['directional_Grams']
    upper=lambda x:Q(x[1])
    d=upper(a['form_refinement']['direct_relative_error'])*upper(g['GJ_w'])
    u=2*sqrt_upper(upper(g['model_J'])*upper(g['error_J']))+upper(g['error_J'])
    new=d+u;old=upper(a['form_common_D_U_error'])
    need(0<=new<old,'No directional improvement')
    flo=Q(b['F_interval'][0])+old-new
    fhi=Q(b['F_interval'][1])-old+new
    margin=Q(b['budget_interval'][0])-fhi
    need(flo<=fhi and margin>0,'No room for a residual test')
    return {'status':'AUTHOR_DERIVED','review_status':'EXTERNAL_REVIEW_OPEN',
            'source_commit':BASE,'outcome':'METHOD_PILOT_REQUIRES_FULL_RESIDUAL',
            'test_vector_sha256':a['test_vector_sha256'],'K_new_sha256':a['K_new_sha256'],
            'physical_candidate_sha256':a['physical_candidate_sha256'],
            'directional_direct_price_upper':str(d),'directional_U_price_upper':str(u),
            'old_common_B_price_upper':str(old),'new_directional_B_price_upper':str(new),
            'F_interval':[str(flo),str(fhi)],'budget_interval':b['budget_interval'],
            'budget_lower_minus_F_upper':str(margin),
            'beta':b['beta'],'c':b['c'],'old_kappa':b['kappa'],
            'full_residual_computed':False,'full_inverse_upper_certified':False,
            'partial_pass':False,'milestone_4_closed':False,'N12_closed':False,
            'new_integration':False,'new_physical_direction':False}

def finite_pilot(data):
    ctx.prec=1024
    case=json.loads(data['common'])['cases'][0]
    old=json.loads(data['old_sources'])['cases'][0]
    schur=json.loads(data['pilot_matrix']);pilot=json.loads(data['pilot_result'])
    prior=json.loads(data['schur_result']);frozen=json.loads(data['candidate'])
    need(case['parity']==old['parity']==frozen['parity']=='even','Parity')
    P=ratmat(schur['P_new_upper_rational']);K=ratmat(schur['K_new_rational']);Ki=K.inv()
    w=arb_mat([[q(v)]for v in frozen['raw_coefficients']])
    n=mat(pilot['nu_new_direction'])
    F=range(12);J=range(12,96)
    G=ratmat(case['G96_rational']);GF=sub(G,F,F);GJ=sub(G,J,J)
    U=mat(case['U96_model']);UF=sub(U,F,F);UJ=sub(U,J,J)
    DL=mat(case['D96_lower_model']);DU=mat(case['D96_upper_model']);D0=(DL+DU)/2
    a=sub(D0-U,F,J);stored=mat(case['finite_cross_C84_new_model'])
    for i in range(12):
        for j in range(84):
            need(a[i,j].overlaps(stored[i,j]),'a model mismatch')
            a[i,j]=a[i,j].union(stored[i,j])
    B=sub(D0-U,J,J);H0=B-a.transpose()*Ki*a
    r0=n-H0*w
    dd=box(pilot['partial_weight_bounds']['direct_energy_relative_error_upper'])
    da=box(pilot['partial_weight_bounds']['a_fin_relative_error_upper'])
    EF=2*(mat(case['finite_feature_error_gram'])+
          mat(old['old_certificate']['joint_high_source_error_gram'])/q(case['delta']))
    ej=2*(box(case['tail_feature_error_scalar'])+
          box(old['galerkin']['high_source_error_norm'])**2/q(case['delta']))
    EJ=arb_mat([[ej if i==j else 0 for j in range(84)]for i in range(84)])
    g=quad(GJ,w);ew=quad(EJ,w);uw=quad(UJ,w)
    pg=trace(P*GJ);pe=trace(P*EJ);pu=trace(P*UJ)
    # These source identities bind the directional refinement to the full
    # original feature Gram, including factor 2 and high-error overcoverage.
    recorded=prior['form_refinement']['directional_Grams']
    for key,v in [('GJ_w',g),('model_J',uw),('error_J',ew)]:
        need(v.overlaps(box(recorded[key])),'Directional Gram provenance: '+key)
    terms={'model_finite_residual':upnorm(quad(P,r0))}
    # Retain the old sqrt(b)>1 factor, conservatively; no second nu derivation.
    need(Q(pilot['P_weight'])>=1,'P weight needed for inherited nu bound')
    terms['nu_feature']=box(pilot['feature_error_norms']['P_upper_J_star_nu'])
    terms['nu_physical_residual']=box(pilot['partial_weight_bounds']['P_feature_operator_norm_without_weight_upper'])*box(prior['whole_residual_Hilbert_error'])
    terms['D_JJ']=dd*upnorm(pg*g)
    terms['U_JJ']=upnorm(pu*ew)+upnorm(pe*uw)+upnorm(pe*ew)
    rF=Ki*a*w
    terms['a_left']=dd*upnorm(quad(GF,rF)*pg)+upnorm(quad(UF,rF)*pe)+upnorm(quad(EF,rF)*pu)+upnorm(quad(EF,rF)*pe)
    Z=Ki*a
    tg=trace(P*Z.transpose()*GF*Z);tu=trace(P*Z.transpose()*UF*Z);te=trace(P*Z.transpose()*EF*Z)
    terms['a_right']=dd*upnorm(tg*g)+upnorm(tu*ew)+upnorm(te*uw)+upnorm(te*ew)
    ea=box(prior['form_a_Ki_error_norm'])
    terms['a_quadratic']=da*upnorm(trace(Ki*GF)*pg)*ea
    qJJup=sub(DU,J,J)
    terms['eta_q']=q('1e-10')*upnorm(trace(P*qJJup)*quad(qJJup,w))
    # Round every summand outwards before summing exactly.
    enclosed={key:enc(v) for key,v in terms.items()}
    y=sum((Q(v[1]) for v in enclosed.values()),Q(0))
    return {'terms':enclosed,'finite_P_residual_norm_upper':str(y),
            'finite_P_residual_energy_upper':str(y*y),
            'trace_P':enc(trace(P)),'bits':1024,
            'full_infinite_residual_computed':False}

def complete(result, finite):
    m=Q(result['budget_lower_minus_F_upper']);beta=Q(result['beta']);c=Q(result['c'])
    y=Q(finite['finite_P_residual_norm_upper'])
    # A simple rational target chosen after the exploratory pilot.
    # This is a future acceptance threshold, NOT a measured residual value.
    target=Q(19,10**9)
    x2=target/beta
    residual_price=(x2+y*y+2*sqrt_upper(c*x2*y*y))/(1-c)
    need(residual_price<m,'Proposed whole-residual target is insufficient')
    result.update(finite_P_residual_norm_upper=str(y),
                  finite_P_residual_energy_upper=str(y*y),
                  proposed_full_Ldual_energy_target=str(target),
                  conditional_remainder_price_upper=str(residual_price),
                  conditional_total_energy_upper=str(Q(result['F_interval'][1])+residual_price),
                  conditional_margin=str(m-residual_price),
                  old_floor_price_at_same_target=str(target/(Q(result['old_kappa'])*beta)),
                  zero_finite_leakage_target_NOT_ACTUAL=str((1-c)*beta*m),
                  zero_leakage_threshold_gain_over_old_floor=str((1-c)/Q(result['old_kappa'])),
                  condition='The ACTUAL whole r=nu-HJw, with all model/integration errors, has L-dual energy <=19/10^9. This has NOT been computed.')
    return result

def run(root,bindings):
    data=snapshot(root,bindings)
    result=scalar_pilot(data);finite=finite_pilot(data)
    return {'RESULT.json':dump(complete(result,finite)),'FINITE.json':dump(finite)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repository',type=Path,default=HERE.parents[2])
    ap.add_argument('--check',action='store_true');ap.add_argument('--output-dir',type=Path)
    args=ap.parse_args();need(__debug__,'python -O is not allowed')
    bindings=(HERE/'INPUT_BINDINGS.json').read_bytes()
    if args.check:
        for name,digest in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            p=(HERE/name).resolve();need(p.is_relative_to(HERE),'Escaping package')
            need(sha(p.read_bytes())==digest,'Package hash: '+name)
    outputs=run(args.repository.resolve(),bindings)
    for name,raw in outputs.items():
        if args.check: need(raw==(HERE/name).read_bytes(),'Replay mismatch: '+name)
        if args.output_dir:
            args.output_dir.mkdir(parents=True,exist_ok=True);(args.output_dir/name).write_bytes(raw)
    result=json.loads(outputs['RESULT.json'])
    print('PASS: directional F and finite residual pilot; FULL RESIDUAL REMAINS OPEN')
    for key in ('F_interval','budget_lower_minus_F_upper','finite_P_residual_energy_upper',
                'proposed_full_Ldual_energy_target','conditional_margin'):
        value=result[key]
        print(key,[float(Q(x)) for x in value] if isinstance(value,list) else float(Q(value)))

if __name__=='__main__': main()
