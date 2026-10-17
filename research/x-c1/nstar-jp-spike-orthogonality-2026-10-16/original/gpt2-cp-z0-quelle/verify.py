"""Reproduce directed evaluation of the elementary Cp z0 source formula."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,io,json,zipfile
import cp_z0 as c
HERE=Path(__file__).resolve().parent
BRIDGE='b48e3895d57cc5cc2c11ca170e32d6af5fbdfcde9948b4db7c370d3376b6d57b'
HIGH='1ccb6be11c6a8b4e325338b80f2136990b464b4a70e724a02ca7addbe7ba99b0'
def need(ok,label):
    if not ok:raise AssertionError(label)
def sha(b):return hashlib.sha256(b).hexdigest()
def member(z,suffix):
    ns=[n for n in z.namelist() if n==suffix or n.endswith('/'+suffix)]
    need(len(ns)==1,('unique member',suffix));return z.read(ns[0])
def enc(x):
    if isinstance(x,c.I):return x.frac()
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x
def dump(p,x):p.write_bytes((json.dumps(enc(x),ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bridge-archive',type=Path,required=True)
    ap.add_argument('--high-archive',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();out=args.output.resolve()
    need(not out.exists() and not out.is_relative_to(HERE),'new output outside package')
    if (HERE/'MANIFEST.json').exists():
        for rel,h in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            p=(HERE/rel).resolve();need(p.is_relative_to(HERE) and sha(p.read_bytes())==h,('manifest',rel))
    raw=args.bridge_archive.read_bytes();need(sha(raw)==BRIDGE,'bridge archive')
    with zipfile.ZipFile(io.BytesIO(raw)) as z:source=member(z,'sources/A9_A11_SOURCE_PROOF.txt')
    need(source==(HERE/'sources/A9_A11_SOURCE_PROOF.txt').read_bytes(),'original Cp definition')
    raw=args.high_archive.read_bytes();need(sha(raw)==HIGH,'high archive')
    with zipfile.ZipFile(io.BytesIO(raw)) as z:core=member(z,'vendor/source_core.py')
    need(core==(HERE/'vendor/source_core.py').read_bytes(),'inherited directed arithmetic')
    cuts=c.interior_cuts();edges=[c.I(0)]+[v for _,v in cuts]+[c.geometry(0)['a']]
    result={'status':'AUTHOR_DERIVED_ELEMENTARY_SOURCE_FORMULA_WITH_DIRECTED_EVALUATOR',
        'external_review_open':True,'bridge_archive_sha256':BRIDGE,'high_archive_sha256':HIGH,
        'definition_source_sha256':sha(source),'interval_arithmetic_sha256':sha(core),
        'meaning':'c_tilde modulo Mellin carrier; Pi_a c_tilde=C_sigma z0',
        'shift_discontinuities':cuts,'parities':{}}
    count=0
    for sigma,label in [(0,'even'),(1,'odd')]:
        g=c.geometry(sigma);rows=[]
        for j,(l,r) in enumerate(zip(edges,edges[1:])):
            x=(l+r)/2;v=c.raw_source(x,sigma)
            need(v.hi-v.lo<10**40,'sample enclosure width below 1e-80')
            rows.append({'cell':j,'x':x,'raw_source':v});count+=1
        endpoint=[]
        limit=c.regular_left_limit(sigma)
        for k in [6,12,24]:
            gap=F(1,10**k);x=g['a']-gap;v=c.raw_source(x,sigma);reg=c.regular_part(x,sigma)
            need(v.hi-v.lo<10**40,'near-end enclosure width below 1e-80')
            # Only a check at these explicit points, not a uniform remainder claim.
            difference=(reg-limit).absolute()
            need(difference.hi<(100*c.I(gap).sqrt()).lo,'explicit regular-part limit check')
            endpoint.append({'gap':gap,'raw_source':v,'regular_part':reg,'difference_from_limit':difference});count+=1
        result['parities'][label]={'geometry':{k:v for k,v in g.items() if k!='shifts'},
            'log_coefficient_at_a':c.log_coefficient(g['a'],sigma),
            'regular_part_left_limit':limit,
            'cell_midpoints':rows,'near_endpoint':endpoint}
        print(label,'13 cells; 3 near-endpoint points; elementary source PASS',flush=True)
    # Interval boxes straddling a shift discontinuity must be rejected.
    rejected=0
    for sigma in [0,1]:
        x=c.I.hull(cuts[0][1]-F(1,10**8),cuts[0][1]+F(1,10**8))
        try:c.raw_source(x,sigma)
        except ValueError:rejected+=1
    need(rejected==2,'discontinuity boxes rejected')
    out.mkdir(parents=True);dump(out/'CP_Z0_SOURCE.json',result)
    receipt={'status':'PASS_DIRECTED_POINT_EVALUATIONS_UNDER_BOUND_OPERATOR_DEFINITION',
        'source_archives_checked':2,'interior_prime_discontinuities':12,
        'directed_point_values':count,'discontinuity_boxes_rejected':2,
        'Gamma_inner_quadrature_used':False,'full_pairing_quadrature_remainder_proved':False,
        'moment_projected_Cp_point_values_computed':False,
        'Cp_source_representative_modulo_m_constructed':True,
        'chi_p_residual_pairing_computed':False,'L0_computed':False,'N12_resolved':False,
        'external_mathematical_review_open':True,'github_changed':False}
    dump(out/'RECEIPT.json',receipt)
    if (HERE/'expected').exists():
        for name in ['CP_Z0_SOURCE.json','RECEIPT.json']:
            need((out/name).read_bytes()==(HERE/'expected'/name).read_bytes(),('byte-identical replay',name))
    print('PASS: elementary source evaluator; no L0 enclosure claimed',flush=True)
if __name__=='__main__':main()
