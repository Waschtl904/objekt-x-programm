"""GPT1: exact stored-certificate audit, no native integrations or model search."""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import json, gzip, hashlib, sys, time

sys.set_int_max_str_digits(50000)
if sys.flags.optimize or not __debug__: raise SystemExit('OPTIMIZED_PYTHON_REJECTED')
ROOT = Path(__file__).resolve().parent
H = ROOT / 'merged/workspace/work/breakthrough-2026-10-25'
start = time.monotonic()

def need(ok, text):
    if not ok:
        raise RuntimeError(text)

def read(name):
    return json.loads((H / name).read_bytes())

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def mat(a):
    return [[Q(x) for x in row] for row in a]

def transpose(a):
    return [list(r) for r in zip(*a)]

def mul(a, b):
    return [[sum((x*y for x,y in zip(row,col)), Q()) for col in zip(*b)] for row in a]

def same(a,b):
    return a == b

def bound(boxes, sign):
    a=[[(Q(x)+Q(y))/2 for x,y in row] for row in boxes]
    need(a==transpose(a),'Matrix midpoint not symmetric')
    for i,row in enumerate(boxes):
        a[i][i] += sign * sum(((Q(y)-Q(x))/2 for x,y in row), Q())
    return a

def ldl(a):
    need(a==transpose(a),'LDL matrix not symmetric')
    n=len(a); L=[[Q(i==j) for j in range(n)] for i in range(n)]; d=[]
    for j in range(n):
        p=a[j][j]-sum((L[j][k]**2*d[k] for k in range(j)),Q())
        need(p>0,f'Nonpositive exact LDL pivot {j}')
        d.append(p)
        for i in range(j+1,n):
            L[i][j]=(a[i][j]-sum((L[i][k]*L[j][k]*d[k] for k in range(j)),Q()))/p
    need(mul(mul(L,[[d[i] if i==j else Q() for j in range(n)] for i in range(n)]),transpose(L))==a,'LDL reconstruction')
    return d

def ball(obj):
    m,e,r,s=obj['ball']
    center=Q(m)*Q(2)**e; radius=Q(r)*Q(2)**s
    return center-radius,center+radius

def exact100(obj):
    lo,hi=ball(obj); x=Q(round((lo+hi)/2*10**100),10**100)
    need(lo<=x<=hi and (hi-lo)/2<Q('1e-150'),'Rational test value outside cache ball')
    return x

def sqrt_up(x):
    need(x>=0,'Negative square root')
    scale=10**80; n=isqrt(x.numerator*scale*scale//x.denominator)
    if Q(n,scale)**2<x:n+=1
    y=Q(n,scale);need(y*y>=x,'Square-root upper bound')
    return y

def overlap(x,y):
    return max(x[0],y[0])<=min(x[1],y[1])

def affine(a,b,t):
    return ((1-t)*a[0]+t*b[0],(1-t)*a[1]+t*b[1])

closure=read('revision_v2/SOURCE_ARITHMETIC_CLOSURE_V2.json')
Gp=bound(closure['remaining_gap'],-1)
metric=read('../fo-response-reach-2026-10-25/frozen/MODEL.json')['matrices']['G_W']
Gu=bound(metric,1)
floor=Q(read('revision_v2/SOURCE_CLOSED_GAP_EXACT_AUDIT_V2.json')['proved_W_floor_for_stored_ledger'])
need(floor==Q('4e-19'),'Corrected threshold')
ldl(Gp);ldl(Gu)
pivots=ldl([[Gp[i][j]-floor*Gu[i][j] for j in range(12)] for i in range(12)])
geom=read('revision_v2/JOINT_TAIL_GEOMETRY_V2.json'); tests=read('COMMON_TEST_MAP_EXACT.json')
need(geom['source_closure_sha256']==sha(H/'revision_v2/SOURCE_ARITHMETIC_CLOSURE_V2.json'),'Closure binding')
need(geom['basis']==read('JOINT_TAIL_GEOMETRY.json')['basis'] and geom['caches']==read('JOINT_TAIL_GEOMETRY.json')['caches'],'Unchanged frame and cache bindings')
need(tests['frame_sha256']==sha(H/'JOINT_TAIL_GEOMETRY.json'),'Test map binding')
B=mat(geom['basis']);Y=mat(tests['test_images_in_F12_J84_order'])
need(B==mat(tests['input_frame']),'Common input basis')
C=mul(mul(transpose(B),Gp),B)
need(C==mat(geom['finite_gap_lower_in_basis']),'C = B*GpB')
cpivots=ldl(C);A=mat(geom['inverse'])
need(A==transpose(A),'Inverse symmetry')
need(mul(C,A)==[[Q(i==j) for j in range(12)] for i in range(12)],'C inverse exact')
gamma=list(map(Q,read('inputs/CORRECTION_4096.json')['Gamma_new_coefficients']))
rows=[];norms=[];total_cells=0
beta=sqrt_up(Q(5,21))
for i, item in enumerate(geom['caches']):
    label=f'T{i:02d}'; cache=H/item['cache'];raw=cache.read_bytes()
    need(item['label']==label and hashlib.sha256(raw).hexdigest()==item['sha256'],'Cache binding '+label)
    body=json.loads(gzip.decompress(raw));payload=body['payload'].encode()
    need(hashlib.sha256(payload).hexdigest()==body['payload_sha256'],'Payload '+label)
    v=dict(json.loads(payload)['mapping'])
    need([exact100(x) for x in v['cc']]==[r[i] for r in B],'Input image '+label)
    yc=[-exact100(r[0]) for r in v['pv']['matrix']]+[exact100(r[0]) for r in v['w']['matrix']]
    need(yc==[r[i] for r in Y],'Fixed test image '+label)
    need(len(v['gamma'])==225,'Gamma count')
    for box,coefficient in zip(v['gamma'],gamma):
        lo,hi=ball(box);need(lo<=coefficient<=hi,'Gamma coefficient '+label)
    lo,hi=ball(v['delta']);need(lo<=Q('1.84298')<=hi,'Delta '+label)
    bind=read(f'directed-whole-{label}/BINDING.json')
    need(bind['cache']==item['sha256'],'Integration cache '+label)
    for name,digest in bind['sources'].items():need(sha(H/name)==digest,'Source '+name)
    edges=[tuple(map(Q,x)) for x in bind['outer_edges']];depth=bind['depth']
    need(all(a[1]<b[0] for a,b in zip(edges,edges[1:])),'Separated outer cuts')
    panels=[]
    for k,(lo,hi) in enumerate(zip(edges,edges[1:])):
        if k==0:
            panels.extend((affine(lo,hi,Q(1,2**(j+1))),affine(lo,hi,Q(1,2**j))) for j in range(depth))
        elif k==len(edges)-2:
            panels.extend((affine(lo,hi,1-Q(1,2**j)),affine(lo,hi,1-Q(1,2**(j+1)))) for j in range(depth))
        else:panels.append((lo,hi))
    need(len(panels)==bind['panel_count'],'Panel count')
    energy=Q();hashes=[]
    for k,(lo,hi) in enumerate(panels):
        path=H/f'directed-whole-{label}/{k:04d}.json';row=json.loads(path.read_bytes())
        need(row['index']==k and row['status']=='DIRECTED_NEW_MODEL_INTERVAL','Cell status')
        need(overlap(tuple(map(Q,row['lo'])),lo) and overlap(tuple(map(Q,row['hi'])),hi),'Cell boundary consistency')
        need(Q(row['weighted_remainder'][1])<Q('1e-21') and Q(row['midpoint_difference'][1])<Q('1e-40'),'Stored controls')
        e=Q(row['values']['model_Xnorm_squared_upper'][1]);need(e>=0,'Cell energy')
        energy+=e;hashes.append(sha(path))
    E=Q(read('CONTOUR_CAPS_'+label+'.json')['whole_endpoint_log_squared_envelope']);tails=Q()
    for left,right in ((edges[0],edges[1]),(edges[-2],edges[-1])):
        dl=(right[0]-left[1])/2**depth;du=(right[1]-left[0])/2**depth
        need(0<dl<=du<Q(1,2**150),'Tail domain')
        k=max(1,dl.denominator.bit_length()-dl.numerator.bit_length()+1)
        while Q(1,2**k)>dl:k+=1
        while k>1 and Q(1,2**(k-1))<=dl:k-=1
        need(Q(1,2**k)<=dl,'Log envelope')
        tails+=2*E*E*du*(29+28*k+14*k*k+4*k**3+k**4)
    pfile=f'revision_v2/WHOLE_PHYSICAL_ERROR_V2_{label}.json'
    p=read(pfile);core=read(('RETAINED_CORE_QUADRATURE_' if i==0 else 'RETAINED_CORE_QUADRATURE_R2875_')+label+'.json')
    strip=read('CORE_TAIL_VARIATION_'+label+'.json')
    small=read('SMALL_MODEL_CHANGES_'+label+'.json')
    need(Q(small['small_raw_upper'])<Q('1e-150'),'Small residual allowance')
    nonmodel=beta*(Q(core['quantities']['combined_X_error'][1])+Q(strip['quantities']['whole_X_error_from_strip_variation'][1]))+Q(p['quantities']['full_Qold_dual_error_expression'][1])
    n=beta*sqrt_up(energy+tails)+nonmodel;norms.append(n)
    saved=read('revision_v2/JOINT_REST_BUDGET_V2.json')['directions'][i]
    need(n==Q(saved['whole_dual_norm_upper']),'Norm recombination '+label)
    need(energy+tails==Q(saved['model_energy_upper']),'Energy recombination '+label)
    need(hashlib.sha256(''.join(hashes).encode()).hexdigest()==saved['interval_manifest_sha256'],'Section hash sequence')
    total_cells+=len(panels)
    rows.append({'direction':label,'sections':len(panels),'norm_upper':str(n),'norm_float_for_display':float(n),'physical_error_file':pfile})
    print(label,'cache, test, Gamma, section boundaries and exact recombination PASS',flush=True)
theta=sum((abs(A[i][j])*norms[i]*norms[j] for i in range(12) for j in range(12)),Q())
need(theta==Q(read('revision_v2/JOINT_REST_BUDGET_V2.json')['relative_rest_upper']),'Joint trace recombination')
need(theta<Q('0.002403782')<1,'Common positive reserve')
need((1-theta)*floor==Q(read('revision_v2/JOINT_REST_BUDGET_V2.json')['resulting_GW_floor']),'Resulting exact floor')
need((1-Q('0.002403782'))*floor==Q('3.990384872e-19'),'Public conservative floor')
need(total_cells==4704,'All 4704 sections accounted for')
result={'revision_archive_sha256':'aa5d5df0a068991972ba7eb5f60de9106f865cc53a891330394847666251e4fa','floor_exact':str((1-theta)*floor),'status':'GPT1_EXACT_STORED_CERTIFICATE_CHECK_PASS','archive_sha256':'024f20f0c6086aefabb6e3d759f91aaa466906a864c673c0c0b467f3ee627946','finite_gap_positive_LDL_pivots':len(pivots),'frame_positive_LDL_pivots':len(cpivots),'sections':total_cells,'directions':rows,'theta_exact':str(theta),'theta_float_for_display':float(theta),'conservative_GW_floor':'3.990384872e-19','cache_Gamma_memberships':2700,'fixed_test_coefficients':1152,'native_integrations_replayed':False,'physical_error_application_proved_by_this_script':False,'seconds':time.monotonic()-start}
(ROOT/'INDEPENDENT_EXACT_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['directions','theta_exact','floor_exact']},indent=2))
