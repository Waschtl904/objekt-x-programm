"""Bound small-matrix preanalysis; no residual integration or response search."""
from pathlib import Path
from fractions import Fraction
import sys, json, hashlib, importlib.util, zipfile, time, threading, os
HERE=Path(__file__).resolve().parent
sys.dont_write_bytecode=True
sys.path.insert(0,str(HERE/'deps'))
from flint import arb,arb_mat,ctx
PRIOR=HERE.parent
ROOT=PRIOR/'repo'
ARCHIVE=PRIOR/'inherited/Objekt-X-Zweiraum-Ganzrest-und-Matrixvergleich-2026-10-24.zip'
def sha(b): return hashlib.sha256(b).hexdigest()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def write(name,obj): (HERE/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def load():
    raw=ARCHIVE.read_bytes()
    need(sha(raw)=='e1911ce244aa51062f6b06bb767f945922199112380022b59846de4ec7f0e89d','Original archive hash')
    with zipfile.ZipFile(ARCHIVE) as z:
        manifest=json.loads(z.read('MANIFEST.json'))
        source=z.read('two-direction-2026-10-24/SOURCE_BINDINGS.json')
        directions=z.read('two-direction-2026-10-24/DIRECTIONS.json')
        # The archive as a whole is hash-bound; retain exact member digests.
    spec=json.loads(source)
    receipts=[]
    for rel,item in spec['files'].items():
        data=(ROOT/rel).read_bytes()
        need(sha(data)==item['sha256'],'Source mismatch: '+rel)
        receipts.append({'path':rel,'sha256':sha(data),'role':item.get('role'),'alias':item.get('alias')})
    engpath=ROOT/'research/x-c1/w9-new-k-schur-underform-even-2026-10-20/engine.py'
    s=importlib.util.spec_from_file_location('grad11_bound_schur',engpath)
    eng=importlib.util.module_from_spec(s);s.loader.exec_module(eng)
    bindings,data=eng.snapshot(ROOT,(engpath.parent/'INPUT_BINDINGS.json').read_bytes())
    env=eng.load(ROOT,bindings,data)
    return eng,env,json.loads(directions),{'archive_sha256':sha(raw),'directions_sha256':sha(directions),'source_bindings_sha256':sha(source),'files_checked':receipts}
def main():
    start=time.monotonic()
    eng,env,d,receipt=load();co=env['common'];e=env['energy'];ctx.prec=1024
    def col(v):return arb_mat([[co.q(x)]for x in v])
    v=col(d['v1_rational']);u=col(d['v2_rational']);w1=col(d['w1_rational']);w2=col(d['w2_rational'])
    need(d['second_basis_index']==0 and d['independence_witness_coordinate']==1,'Frozen coordinate extension')
    N=eng.quad(e.G,v).sqrt();M=eng.quad(e.G,u).sqrt()
    T=arb_mat(84,12)
    for i in range(84):
        T[i,0]=M*w2[i,0]
        T[i,1]=(N*w1[i,0]-M*v[0,0]*w2[i,0])/v[1,0]
    for C,w in [(v/N,w1),(u/M,w2)]:
        need(all((T*C)[i,0].overlaps(w[i,0])for i in range(84)),'Old test preserved')
    B=arb_mat([[((v/N)[i,0]if j==0 else (u/M)[i,0]if j==1 else arb(int(i==j)))for j in range(12)]for i in range(12)])
    case=env['inp'].json('common')['cases'][0]
    DL,DU=co.mat(case['D96_lower_model']),co.mat(case['D96_upper_model'])
    DJ=arb_mat([[(DU[i,j]+DL[i,j])/2 for j in range(12,96)]for i in range(12,96)])
    H=env['H0']-co.q('1e-10')*DJ
    base=sum((e.components[k]for k in ('high_U8','finite_U8','K_inverse_v')),arb_mat(12,12))
    F=base+T.transpose()*e.nu+e.nu.transpose()*T-T.transpose()*H*T
    F=(F+F.transpose())/2
    km=env['inp'].json('kp_model_even')['K_P_model']
    K=arb_mat([[co.q(str(x))for x in row]for row in km]);K=(K+K.transpose())/2
    P=e.w['P'];R=e.nu-H*T;Z=R.transpose()*P*R
    vals={'G_W':e.G,'basis_B':B,'T_raw':T,'B_base':base,'nu_model':e.nu,'H_model':H,
          'K_model_ONLY':K,'F_model':F,'gap_model_ONLY':K-F,'finite_Z_model':Z,
          'G_in_basis':B.transpose()*e.G*B,'K_in_basis_model_ONLY':B.transpose()*K*B,
          'F_in_basis_model':B.transpose()*F*B,'gap_in_basis_model_ONLY':B.transpose()*(K-F)*B,
          'Z_in_basis_model':B.transpose()*Z*B}
    out={'status':'EXPLORATORY_FULL_SPACE_MODEL_ONLY','plan_sha256':sha((HERE/'PLAN.txt').read_bytes()),
         'prec_bits':ctx.prec,'matrices':co.encode(vals),'receipt':receipt,
         'normalizations':co.encode({'N':N,'M':M}),
         'inherited_error_parameters':co.encode({'bounds':e.bounds,'residual_errors':e.residual_errors,
           'eResidual':e.eResidual,'eBareF':e.eBareF,'eRawF':e.eRawF,'eRawA':e.eRawA,'eLowA':e.eLowA}),
         'elapsed_seconds':time.monotonic()-start,'new_residual_integrations':0,'new_test_solves':0}
    write('MODEL.json',out)
    print(json.dumps({'status':out['status'],'seconds':out['elapsed_seconds'],'source_files_checked':len(receipt['files_checked'])}))
if __name__=='__main__':
    timer=threading.Timer(600,lambda:os._exit(124));timer.daemon=True;timer.start()
    main();timer.cancel()
