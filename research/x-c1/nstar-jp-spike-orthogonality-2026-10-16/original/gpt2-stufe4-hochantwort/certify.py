"""Complete high U8 remainder and scalar D-model error, standard library only.

All mathematical decisions use directed integer intervals. Quadrature values in
the incoming diagnostic package are not used as certified numerical inputs.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,io,json,sys,zipfile
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'vendor'))
import source_core as sc
sc.DIGITS=180;sc.S=10**180
I=sc.I
BRIDGE='b48e3895d57cc5cc2c11ca170e32d6af5fbdfcde9948b4db7c370d3376b6d57b'
STAGE3='ab7116f74c9d81b877bec28ac547cc275ca142033a0004ffc3c699c63dd96b52'
GLOBAL='2ca3c682de8a529b12a0d628c2b606fd04df332d1299ccd36dff71ac3e53d80c'
STAGE1='940cd40e08be5884e6cd2a7e96e2e5815892bfb14a9e9c2d9b04d8aab317dd49'
INCOMING='88a68c9c51e00fb7024ebaa6db0c72e4dafd5f65a3b98cddb2300dee511ff5df'
RESPONSE='b8677c0bb085f40052e52953ec39112894fbaa0f9f5d9997df8ae546238f41ee'

def sha(b):return hashlib.sha256(b).hexdigest()
def member(z,suffix):
    names=[n for n in z.namelist() if n==suffix or n.endswith('/'+suffix)]
    assert len(names)==1,(suffix,names)
    return z.read(names[0])
def read(z,suffix):return json.loads(member(z,suffix))
def box(v):
    a,b=map(F,v);assert a<=b
    return I.raw(I(a).lo,I(b).hi)
def bm(a):return [[box(v) for v in r] for r in a]
def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b)),I(0))
def mv(a,x):return [dot(row,x) for row in a]
def quad(a,x):return dot(x,mv(a,x))
def norm(x):return sum((v**2 for v in x),I(0)).sqrt()
def trprod(a,b):return sum((a[i][j]*b[j][i] for i in range(len(a)) for j in range(len(a))),I(0))
def encode(v):
    if isinstance(v,I):return v.frac()
    if isinstance(v,F):return str(v)
    if isinstance(v,dict):return {k:encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    return v
def dump(p,v):p.write_bytes((json.dumps(encode(v),indent=2,ensure_ascii=False)+'\n').encode())

def rational_controls():
    # Exact cancellation with B0*=diag(1/1000,2), c0=(1000,2), y0=(3,4).
    yy=F(25);cross=F(19);bb=F(17)
    assert yy-2*cross+bb==4
    assert yy+bb!=4 and yy-2*cross-bb<0
    # C=diag(1000,1/2); B0*C=I. Directional sensitivity is not ||C||.
    a=[F(3,500),F(4,500)]
    dc=[1000*a[0],a[1]/2]
    bdc=[dc[0]/1000,2*dc[1]]
    assert sum(v*v for v in bdc)==F(1,10000)
    assert sum(v*v for v in bdc)<=2*sum(v*v for v in a)
    # Physical high lift is not an isometry if its carrier correction is nonzero.
    assert F(1)+F(1,10)**2>1
    return {'complete_Gram_identity':True,'omitted_cross_term_rejected':True,
            'wrong_sign_Gram_rejected':True,'weighted_C_sensitivity':True,
            'physical_moment_lift_is_not_an_isometry':True}

def main():
    ap=argparse.ArgumentParser()
    for name in ['bridge-archive','stage3-archive','response-archive','output']:
        ap.add_argument('--'+name,type=Path,required=True)
    args=ap.parse_args();assert __debug__
    out=args.output.resolve();assert not out.exists() and not out.is_relative_to(HERE)
    if (HERE/'MANIFEST.json').exists():
        for name,h in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            p=(HERE/name).resolve();assert p.is_relative_to(HERE) and sha(p.read_bytes())==h,name
    bb=args.bridge_archive.read_bytes();assert sha(bb)==BRIDGE
    with zipfile.ZipFile(io.BytesIO(bb)) as z:
        ops=read(z,'expected/OPERATORS.json');directions=read(z,'expected/DIRECTIONS.json')
        gb=member(z,'Objekt-X-Globaler-Gram-und-vollstaendige-Projektion-2026-10-13.zip')
    assert sha(gb)==GLOBAL
    with zipfile.ZipFile(io.BytesIO(gb)) as z:
        origins=read(z,'SNAPSHOT_ORIGINS.json')
        assert sha(member(z,'vendor/source_core.py'))==sha((HERE/'vendor/source_core.py').read_bytes())
    ab=args.stage3_archive.read_bytes();assert sha(ab)==STAGE3
    bound_sources={}
    with zipfile.ZipFile(io.BytesIO(ab)) as z:
        inputs={}
        for name in ['REFINED_INPUT.json','REFINED_COMMON96.json']:
            raw=gzip.decompress(member(z,'inputs/'+name+'.gz'))
            key='work/direct-rest84-2026-10-11/'+name
            assert sha(raw)==origins[key]['original_sha256']
            inputs[name]=json.loads(raw);bound_sources[name]=sha(raw)
        finite=read(z,'expected/FINITE_ACTION.json')
        s1=member(z,'Objekt-X-Stufe1-Intervallzertifikat-Momentkorrektur-und-W9-Diagnose-2026-10-16.zip')
    assert sha(s1)==STAGE1
    with zipfile.ZipFile(io.BytesIO(s1)) as z:
        psi=read(z,'expected/PSI_CORRECTED.json')['data']
        geometry=read(z,'expected/DIRECTED_RESULTS.json')
    oldraw=(HERE/'inputs/a8_model.json.gz').read_bytes()
    key='work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09/work/remainder-integration-check-v2/originals/weighted-response/inputs/a8_model.json.gz'
    assert sha(oldraw)==origins[key]['original_sha256']
    old=json.loads(gzip.decompress(oldraw));bound_sources['a8_model.json.gz']=sha(oldraw)
    assert old['generator_sha256']==sha((HERE/'sources/generate_a8.py').read_bytes())
    rb=args.response_archive.read_bytes();assert sha(rb)==RESPONSE
    with zipfile.ZipFile(io.BytesIO(rb)) as z:
        energy=read(z,'RESPONSE_ENERGY.json');funcs=read(z,'inputs/FUNCTIONS12.json')
        frozen=read(z,'inputs/FROZEN_RESPONSE12.json')
        for name in ['FUNCTIONS12.json','FROZEN_RESPONSE12.json']:
            assert sha(member(z,'inputs/'+name))==energy['source_bindings']['inputs/'+name]
    assert frozen['rule_id']=='A9_A11_N12_MIDPOINT_INVERSE_60_V1'
    incoming=(HERE/'inputs/Objekt-X-Stufe1-4-Diagnose-2026-10-16.zip').read_bytes()
    assert sha(incoming)==INCOMING
    with zipfile.ZipFile(io.BytesIO(incoming)) as z:
        manifest=read(z,'MANIFEST.json')
        for name,h in manifest['files'].items():assert sha(member(z,name))==h,name
    inp=inputs['REFINED_INPUT.json'];common=inputs['REFINED_COMMON96.json']
    allr={};prices={};checks={'whole_y_Gram_vs_U96_identity_intersections':0,
                            'Bh_model_coordinate_intersections':0}
    for sigma,p in enumerate(['even','odd']):
        print(p,'full high Gram and complete error transport',flush=True)
        co=common['cases'][sigma];raw=inp['cases'][sigma];base=finite[p]
        for key in ['inverse_congruence_integer_matrix','inverse_congruence_denominator','delta','rho']:
            assert co[key]==ops[p][key]
        hf=bm(raw['old_certificate']['source_h_gram_model'])
        hj=[[box(x)*F(91,50) for x in row] for row in raw['galerkin']['H84_model']]
        cross=bm(raw['galerkin']['complete_source_high_cross_model'])
        ef=bm(raw['old_certificate']['joint_high_source_error_gram'])
        ej=box(raw['galerkin']['high_source_error_norm'])
        eb=box(raw['old_certificate']['old_coupling_error_norm'])
        assert eb.intersects(box(raw['galerkin']['old_coupling_error_norm']))
        assert raw['old_raw_coupling_gram']==old['parities'][p]['complete_model_raw_high_Gram']
        g0=[[box(x)/10**100 for x in row] for row in old['parities'][p]['complete_model_raw_high_Gram']]
        hb=[[I(F(x)/F(co['HB_denominator'])) for x in row] for row in co['HB_integer_matrix']]
        ki=[[I(F(x)) for x in row] for row in ops[p]['K12_inverse_rational']]
        tau=trprod(ki,hf);eps=trprod(ki,ef)
        u96=bm(co['U96_model'])
        bf=bm(raw['old_certificate']['source_Bh_model'])
        bj=bm(raw['galerkin']['old_low_Bh_model'])
        ci=[[int(x) for x in row] for row in co['inverse_congruence_integer_matrix']]
        hi=[[int(x) for x in row] for row in co['HB_integer_matrix']]
        n=191
        assert all(ci[i][j]==0 for i in range(n) for j in range(i))
        ccstar=[[sum(ci[i][k]*ci[j][k] for k in range(max(i,j),n)) for j in range(n)] for i in range(n)]
        exact_trace=F(sum(ccstar[i][j]*hi[j][i] for i in range(n) for j in range(n)),
            int(co['inverse_congruence_denominator'])**2*int(co['HB_denominator']))/(1-F(co['rho']))
        txh=I(exact_trace);assert 0<txh.lo<=txh.hi<I(F(463,100)**2).lo
        a=3*sc.log_point(F(2))/2
        gamma=box(psi[p]['mu'])/(a*(2*sigma+1)*sc.mellin(sigma,a)**2)
        delta=I(F(co['delta']));rho=I(F(co['rho']))
        dd=F(funcs['parities'][p]['whole_D12_operator_error_upper'])
        er=energy['parities'][p]['fixed_X'];tn=F(er['T_norm_upper'])
        dr=F(er['whole_Hilbert_residual_model_error_upper'])
        assert dr>=dd*tn and tn**2>=F(er['T_norm_squared_upper'])
        result={};price={}
        for name in ['upper_v','lower_Pv','orthogonal_difference']:
            pr=psi[p]['directions'][name];rr=base['directions'][name];gg=geometry[p]['directions'][name]
            t=[I(F(x)) for x in pr['t_exact']];k=[I(F(x)) for x in pr['k_model_exact']]
            c=[box(x) for x in rr['c_model']];bh=[box(x) for x in rr['B_Th_f_model']]
            alternate_bh=[x-y for x,y in zip(mv(bj,t),mv(bf,k))]
            for x,y in zip(bh,alternate_bh):assert x.intersects(y)
            checks['Bh_model_coordinate_intersections']+=191
            yy=quad(hj,t)-2*dot(k,mv(cross,t))+quad(hf,k)
            vv=[box(x) for x in rr['Vf_model']]
            alternate_y=delta*(quad(u96,[-x for x in k]+t)-norm(vv)**2/(1-rho))
            assert yy.intersects(alternate_y)
            checks['whole_y_Gram_vs_U96_identity_intersections']+=1
            cb=dot(c,bh);bb0=quad(g0,c);bbu=quad(hb,c)
            r2=yy-2*cb+bb0
            assert r2.lo>0 and (bbu-bb0).lo>=0
            eta=box(pr['actual_k_minus_kmodel_K_norm_upper'])
            ey_fixed=ej*norm(t)+quad(ef,k).sqrt()
            ey_k=(tau.sqrt()+eps.sqrt())*eta
            ey=ey_fixed+ey_k
            epsi=box(rr['fixed_k_feature_error_bound'])+box(rr['k_change_feature_error_bound'])
            perturb=ey+eb*norm(c)+txh.sqrt()*epsi
            actual_r=r2.sqrt()+perturb
            high=gamma.sqrt()*actual_r/delta
            psi_upper=norm([box(gg['actual_core_norm_before_U8']),box(gg['actual_shell_norm'])])
            cerror=box(rr['c_error_norm_bound'])
            chi_upper=psi_upper+gamma.sqrt()*(norm(c)+cerror)+high
            chi_lower=F(rr['full_chi_norm_lower_rational'])
            assert I(chi_lower).hi<chi_upper.lo
            psi_error=norm([box(pr['core_model_error_norm_upper']),box(pr['shell_model_error_norm_upper'])])
            result[name]={'full_model_y_norm_squared':yy,'model_c_Bh_cross':cb,
                'full_model_Bstar_c_norm_squared':bb0,'actual_Bstar_c0_norm_squared_upper':bbu,
                'full_model_high_difference_norm_squared':r2,
                'HB_based_model_expression':yy-2*cb+bbu,
                'y_fixed_k_error_upper':ey_fixed,'y_k_change_error_upper':ey_k,
                'y_total_error_upper':ey,'normalized_feature_total_error_upper':epsi,
                'high_difference_error_upper':perturb,'actual_high_difference_norm_upper':actual_r,
                'whole_physical_high_U8_part_norm_upper':high,
                'whole_physical_chi_norm_lower_rational_inherited':chi_lower,
                'whole_physical_chi_norm_upper':chi_upper,
                'whole_psi_model_error_upper':psi_error,
                'finite_pairing_feature_error_multiplier':epsi/(1-rho).sqrt(),
                'whole_high_function_pointwise_computed':False}
            price[name]={'D12_scalar_model_error_operator_norm_upper':chi_upper*dd,
                         'fixed_X_residual_scalar_model_error_operator_norm_upper':chi_upper*dr}
            print(p,name,'high <=',high.display(),'chi <=',chi_upper.display(),flush=True)
        q=I(F(directions[p]['q']))
        rankone=(I(F(11,10))/q)*price['lower_Pv']['fixed_X_residual_scalar_model_error_operator_norm_upper']**2
        price['rank_one_weighted_residual_error_Gram_norm_upper']=rankone
        price['full_W9_weighted_error_certified']=False
        assert result['upper_v']['whole_physical_high_U8_part_norm_upper'].hi<I(F('0.016' if sigma==0 else '0.00245')).lo
        assert result['upper_v']['whole_physical_chi_norm_upper'].hi<I(F('1.352e13' if sigma==0 else '1.023e12')).lo
        assert result['lower_Pv']['whole_physical_high_U8_part_norm_upper'].hi<I(902 if sigma==0 else 23).lo
        assert result['orthogonal_difference']['whole_physical_high_U8_part_norm_upper'].hi<I(F('4.43e-10' if sigma==0 else '5.61e-11')).lo
        assert price['lower_Pv']['fixed_X_residual_scalar_model_error_operator_norm_upper'].hi<I(F('1.86e-13' if sigma==0 else '2.668e-16')).lo
        assert rankone.hi<I(F('6.71e-31' if sigma==0 else '8.35e-36')).lo
        print(p,'p residual scalar error <=',price['lower_Pv']['fixed_X_residual_scalar_model_error_operator_norm_upper'].display(),flush=True)
        allr[p]={'tr_X_HB_exact_rational':exact_trace,'tr_X_HB':txh,'full_M_norm_squared':gamma,
                 'trace_Kinverse_hF0':tau,'trace_Kinverse_high_error':eps,'directions':result}
        prices[p]={'delta_D_upper':dd,'fixed_X_T_norm_upper':tn,'whole_Hilbert_residual_model_error_upper':dr,
                   'q':F(directions[p]['q']),'bounds':price}
    out.mkdir(parents=True)
    dump(out/'COMPLETE_HIGH_RESPONSE.json',allr)
    dump(out/'SPIKE_SCALAR_D_MODEL_ERROR.json',prices)
    receipt={'status':'PASS_UNDER_BOUND_COMPLETE_SOURCE_GRAM_AND_OPERATOR_HYPOTHESES',
        'bridge_sha256':BRIDGE,'stage3_sha256':STAGE3,'global_sha256':GLOBAL,
        'response_archive_sha256':RESPONSE,'incoming_diagnostic_sha256':INCOMING,
        'source_hashes':bound_sources,'incoming_manifest_files_checked':len(manifest['files']),
        'checks':checks,'rational_controls':rational_controls(),
        'complete_high_response_norm_for_v_p_e_certified':True,
        'whole_chi_norm_upper_for_v_p_e_certified':True,
        'D_model_error_for_rank_one_spike_test_certified':True,
        'incoming_quadratures_used_as_bounds':False,'new_large_integrations':False,
        'D12_pairings_certified':False,'exact_A9_orthogonality_proved':False,
        'N12_test_done':False,'N12_excluded':False,'full_W9_error_bound':False,
        'A9_A11_closed':False,'github_changed':False,'external_review_open':True}
    dump(out/'RECEIPT.json',receipt)
    if (HERE/'expected').exists():
        for name in ['COMPLETE_HIGH_RESPONSE.json','SPIKE_SCALAR_D_MODEL_ERROR.json','RECEIPT.json']:
            assert (out/name).read_bytes()==(HERE/'expected'/name).read_bytes(),name
    print('PASS',checks,flush=True)

if __name__=='__main__':main()
