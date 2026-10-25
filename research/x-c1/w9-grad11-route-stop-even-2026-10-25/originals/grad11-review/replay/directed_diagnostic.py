import ast, importlib.util
from analyze import *
def main():
    start=time.monotonic();eng,env,d,receipt=load();co=env['common'];ctx.prec=1024
    q,mat,quad,tr=co.q,co.mat,eng.quad,co.trace
    norm,up,low=co.norm,eng.norm_upper,eng.norm_lower
    e=env['energy'];W=e.w;Ki,a,GF,GJ=(W[k]for k in ('Ki','a','GF','GJ'))
    case=env['inp'].json('common')['cases'][0];raw=env['inp'].json('old_sources')['cases'][0]
    DL,DU=mat(case['D96_lower_model']),mat(case['D96_upper_model'])
    DD=arb_mat([[(DU[i,j]-DL[i,j])/2 for j in range(12,96)]for i in range(12,96)])
    DJ=arb_mat([[(DU[i,j]+DL[i,j])/2 for j in range(12,96)]for i in range(12,96)])
    UJ=arb_mat([[env['U'][i,j]for j in range(12,96)]for i in range(12,96)])
    EJ=2*(co.box(case['tail_feature_error_scalar'])+co.box(raw['galerkin']['high_source_error_norm'])**2/W['delta'])
    Bbase=sum((e.components[k]for k in ('high_U8','finite_U8','K_inverse_v')),arb_mat(12,12))
    with zipfile.ZipFile(ARCHIVE)as z:
        code=z.read('two-direction-2026-10-24/preflight.py').decode('utf-8')
    tree=ast.parse(code);fun=next(n for n in tree.body if isinstance(n,ast.FunctionDef)and n.name=='eval_form')
    namespace=dict(locals());namespace.update(Q=Fraction,arb=arb,arb_mat=arb_mat)
    exec(compile(ast.Module(body=[fun],type_ignores=[]),'bound_original_eval_form','exec'),namespace)
    frozen=(HERE/'DIAGNOSTIC-DIRECTION.json').read_bytes();vdiag=json.loads(frozen)['raw_coefficients']
    col=lambda v:arb_mat([[q(x)]for x in v])
    v=col(d['v1_rational']);u=col(d['v2_rational']);N=quad(e.G,v).sqrt();M=quad(e.G,u).sqrt()
    c=col(vdiag);normalization=quad(e.G,c).sqrt();c/=normalization
    alpha=N*c[1,0]/v[1,0];bet=M*(c[0,0]-v[0,0]*c[1,0]/v[1,0])
    w=alpha*col(d['w1_rational'])+bet*col(d['w2_rational'])
    f=namespace['eval_form'](c,w)
    part=ROOT/'research/x-c1/w9-partial-energy-2026-10-18'
    sys.path.insert(0,str(part))
    kp=part/'certify_k.py';spec=importlib.util.spec_from_file_location('grad11_direct_budget',kp)
    kmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(kmod)
    budget_start=time.monotonic()
    kval=co.encode(kmod.certify(env['inp'],e.data,vdiag,128))
    K=list(map(Fraction,kval['K_P_interval']));F=list(map(Fraction,f['F_interval']))
    out={'status':'CONDITIONAL_VARIATIONAL_OBSTRUCTION'if F[0]>K[1]else'DIRECTED_DIAGNOSTIC_UNRESOLVED',
      'scope':'Fixed inherited comparison inverse, outer response and published linear T; not actual Weil-form negativity.',
      'hypotheses':'H1-H4 inherited in their source-family scope; no external review',
      'diagnostic_direction_sha256':sha(frozen),'normalization':co.enc(normalization),
      'inner_test_coefficients':co.encode({'alpha':alpha,'beta':bet}),
      'F':f,'K':kval,'K_minus_F_interval':[str(K[0]-F[1]),str(K[1]-F[0])],
      'F_lower_minus_K_upper':str(F[0]-K[1]),'new_direct_K_evaluations':1,
      'new_whole_residual_integrations':0,'test_solves':0,
      'F_function_source_sha256':sha(code.encode()),'K_code_sha256':sha(kp.read_bytes()),
      'budget_seconds':time.monotonic()-budget_start,'total_seconds':time.monotonic()-start,
      'T_unchanged':True,'outer_response_unchanged':True}
    write('DIRECTED-DIAGNOSTIC.json',out)
    print(json.dumps({'status':out['status'],'K':[float(x)for x in K],'F':[float(x)for x in F],
      'gap':[float(Fraction(x))for x in out['K_minus_F_interval']],
      'seconds':out['total_seconds'],'prices':{k:[float(Fraction(y))for y in v]for k,v in f['pair_prices'].items()}},indent=2))
if __name__=='__main__':
    timer=threading.Timer(600,lambda:os._exit(124));timer.daemon=True;timer.start()
    main();timer.cancel()
