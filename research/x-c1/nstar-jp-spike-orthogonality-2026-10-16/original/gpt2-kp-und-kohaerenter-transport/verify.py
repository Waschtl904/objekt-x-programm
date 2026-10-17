"""Bind existing certificates and prepare exact coherent k-error metrics.

No integration, D12 pairing, Cp pairing or L0 enclosure is performed here.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,io,json,zipfile

HERE=Path(__file__).resolve().parent
BRIDGE_SHA='b48e3895d57cc5cc2c11ca170e32d6af5fbdfcde9948b4db7c370d3376b6d57b'
BUDGET_SHA='87540b07fb22c90867bae4ddcbefcdab66c455f786ec19f50ce0193455ff00d3'
def need(ok,label):
    if not ok:raise AssertionError(label)
def sha(b):return hashlib.sha256(b).hexdigest()
def member(z,suffix):
    names=[n for n in z.namelist() if n==suffix or n.endswith('/'+suffix)]
    need(len(names)==1,('unique member',suffix));return z.read(names[0])
def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    if isinstance(x,list):return [enc(v) for v in x]
    return x
def dump(p,x):p.write_bytes((json.dumps(enc(x),ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def pivots(a):
    n=len(a);b=[row[:] for row in a];result=[]
    need(all(len(row)==n for row in a),'square matrix')
    need(all(a[i][j]==a[j][i] for i in range(n) for j in range(n)),'exact symmetry')
    for k in range(n):
        d=b[k][k];need(d>0,('strictly positive exact pivot',k));result.append(d)
        for i in range(k+1,n):
            for j in range(k+1,n):b[i][j]-=b[i][k]*b[k][j]/d
    return result
def sqrt_upper(x,digits=80):
    x=F(x);need(x>=0,'nonnegative radicand');scale=10**digits
    n=isqrt(x.numerator*scale*scale//x.denominator)
    if F(n*n,scale*scale)<x:n+=1
    result=F(n,scale);need(result*result>=x,'outward rational root');return result
def quadratic(a,g):
    return sum((a[i]*g[i][j]*a[j] for i in range(len(a)) for j in range(len(a))),F(0))
def scalar_error_upper(metric,midpoint,radii):
    """Real rational box for a=H*h; returned error covers Delta k only.

    The caller must independently certify |a_i-midpoint_i|<=radii_i.
    This function does not create those enclosures.
    """
    g=[[F(x) for x in row] for row in metric]
    a=list(map(F,midpoint));r=list(map(F,radii));n=len(g)
    need(len(a)==len(r)==n and all(x>=0 for x in r),'pairing box dimensions')
    # The first quadratic keeps every signed cross term. The second bounds
    # only uncertainty, by entrywise absolute values and the triangle inequality.
    centre=quadratic(a,g)
    radius=quadratic(r,[[abs(x) for x in row] for row in g])
    return sqrt_upper(centre)+sqrt_upper(radius)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--bridge-archive',type=Path,required=True)
    ap.add_argument('--budget-archive',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();out=args.output.resolve()
    need(not out.exists() and not out.is_relative_to(HERE),'new output outside package')
    if (HERE/'MANIFEST.json').exists():
        for rel,h in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            p=(HERE/rel).resolve();need(p.is_relative_to(HERE) and sha(p.read_bytes())==h,('manifest',rel))
    bridge=args.bridge_archive.read_bytes();budget=args.budget_archive.read_bytes()
    need(sha(bridge)==BRIDGE_SHA,'bridge archive hash');need(sha(budget)==BUDGET_SHA,'unchanged budget archive hash')
    with zipfile.ZipFile(io.BytesIO(bridge)) as z:
        opraw=member(z,'expected/OPERATORS.json');drraw=member(z,'expected/DIRECTIONS.json')
        op=json.loads(opraw);directions=json.loads(drraw)
    with zipfile.ZipFile(io.BytesIO(budget)) as z:bd=json.loads(member(z,'expected/BUDGET_BOUNDS.json'))
    need(bd['rule_id']=='A9_A11_N12_MIDPOINT_INVERSE_60_V1','unchanged fixed rule')
    result={'status':'EXACT_COHERENT_ERROR_INPUTS_CONDITIONAL_ON_INHERITED_SOURCE_CERTIFICATE',
        'bridge_archive_sha256':BRIDGE_SHA,'budget_archive_sha256':BUDGET_SHA,
        'operators_source_sha256':sha(opraw),'directions_source_sha256':sha(drraw),
        'rule_id':bd['rule_id'],'scope':'fixed_X; actual p directly; real pairing vectors',
        'parities':{},'pairings_H_star_h_integrated':False,'L0_computed':False}
    identity=[[F(int(i==j)) for j in range(12)] for i in range(12)]
    for p in ['even','odd']:
        k=[[F(x) for x in row] for row in op[p]['K12_rational']]
        kinv=[[F(x) for x in row] for row in op[p]['K12_inverse_rational']]
        need(len(k)==12 and len(kinv)==12,'fixed 12-dimensional K')
        kp=pivots(k)
        need(mm(k,kinv)==identity and mm(kinv,k)==identity,'two-sided exact inverse')
        need(directions[p]['p_Pupper_v_and_q_exactly_checked'],'inherited actual p definition')
        need(F(bd['parities'][p]['q'])==F(directions[p]['q']),'same spike q')
        entry={'K_rational':k,'K_inverse_rational':kinv,'K_positive_pivots':kp,
            'q':F(directions[p]['q']),'directions':{}}
        for t,key in [('v','upper_v'),('p','lower_Pv')]:
            src=directions[p]['directions'][key]
            eta=F(src['actual_k_error_K_norm_upper']);need(eta>0,'positive inherited eta')
            g=[[eta*eta*x for x in row] for row in kinv]
            trace=sum((g[i][i] for i in range(12)),F(0))
            # Twelve independent exact evaluations via a=K e_j verify the
            # scaling and all signed cross terms against eta^2 K_jj.
            for j in range(12):
                a=[k[i][j] for i in range(12)]
                need(quadratic(a,g)==eta*eta*k[j][j],('metric identity',p,t,j))
                bound=scalar_error_upper(g,a,[0]*12)
                need(bound*bound>=eta*eta*k[j][j],('scalar routine',p,t,j))
            entry['directions'][t]={'source_direction_key':key,'eta_K_norm_upper':eta,
                'fixed_k0_rational':src['K_inverse_Cfin_mid_t_exact_rational'],
                'metric_G_equals_eta_squared_K_inverse':g,
                'Euclidean_fallback_multiplier_upper':sqrt_upper(trace)}
        first=bd['parities'][p]['individual_directions'][0]
        need(first['degree']==0,'exact first shell test')
        entry['z0_budget']=first
        rounded=F('980.113997' if p=='even' else '398.766496')
        need(rounded>=F(first['exclusion_if_model_pairing_distance_exceeds']),'safe rounded sufficient threshold')
        entry['safe_sufficient_distance_for_z0']=rounded
        result['parities'][p]=entry
        print(p,'exact K inverse and coherent metrics for v,p: PASS',flush=True)
    out.mkdir(parents=True)
    dump(out/'COHERENT_TRANSPORT_INPUTS.json',result)
    receipt={'status':'PASS_INPUT_PREPARATION_ONLY','source_archive_hashes_checked':2,
        'positive_K_pivots':24,'exact_inverse_product_entries_checked':576,
        'exact_metric_identities_checked':48,'coherent_metrics_prepared':4,
        'pairing_integrations_performed':0,'L0_computed':False,'D12_coherent_error_evaluated':False,
        'upstream_big_replays_repeated':False,'external_mathematical_review_open':True,
        'github_changed':False}
    dump(out/'RECEIPT.json',receipt)
    if (HERE/'expected').exists():
        for name in ['COHERENT_TRANSPORT_INPUTS.json','RECEIPT.json']:
            need((out/name).read_bytes()==(HERE/'expected'/name).read_bytes(),('byte-identical replay',name))
    print('PASS: exact error metrics prepared; no residual pairing or L0 claimed',flush=True)
if __name__=='__main__':main()
