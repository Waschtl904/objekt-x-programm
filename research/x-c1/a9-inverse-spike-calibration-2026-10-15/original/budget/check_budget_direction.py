"""Exact directional dissection of the bound A8->A9 comparison budget.

The true M and residual bounds remain inherited analytic hypotheses.
All new arithmetic is Fraction/isqrt; float is used only for display.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import argparse,hashlib,json,zipfile

HERE=Path(__file__).resolve().parent
DEFAULT_INPUTS=HERE.parents[1]/'outputs'
INV_NAME='Objekt-X-A9-Inverserneuerung-und-Hoher-Schurrest-2026-10-13.zip'
RESP_NAME='Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip'
INV_SHA='a1fa41958d79ab16a7c42b12375c3373f5a86a99993ae2d23c984ff6b3b2e8ae'
RESP_SHA='5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3'

def sha(raw):return hashlib.sha256(raw).hexdigest()
def member(z,suffix):
    hits=[n for n in z.namelist() if n==suffix or n.endswith('/'+suffix)]
    assert len(hits)==1,(suffix,hits)
    return z.read(hits[0])
def rat(a):return [[Q(x) for x in r] for r in a]
def dot(x,y):return sum((a*b for a,b in zip(x,y)),Q(0))
def mv(a,v):return [dot(row,v) for row in a]
def quad(a,v):return dot(v,mv(a,v))
def iquad(a,v):
    lo=hi=Q(0)
    for i,x in enumerate(v):
        for j,y in enumerate(v):
            z=x*y;l,h=map(Q,a[i][j]);assert l<=h
            lo+=z*(l if z>=0 else h);hi+=z*(h if z>=0 else l)
    return lo,hi
def sqrt_box(x,digits=100):
    assert x>=0;n=10**digits;k=isqrt(x.numerator*n*n//x.denominator)
    lo,hi=Q(k,n),Q(k+1,n);assert lo*lo<=x<hi*hi
    return lo,hi
def encode(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def countercontrols():
    # Tiny Euclidean E is a coordinate-dependent quantity.
    d=Q(1,10**12);e=d/1000
    assert e==Q(1,10**15) and e/d==Q(1,1000)
    scale=10**6;assert scale**2*e==Q(1,1000) and scale**2*d==1
    # A one-direction reduced inverse does not bound the omitted old block.
    U8=Q(10**9);Hinv=Q(2)
    assert U8>Hinv and U8>5 # f=(1,0), no coupling, W9=diag(U8,Hinv)
    # Monotone inverses may be uniformly bounded for arbitrarily many steps.
    C=Q(62282)
    for n in range(1,9):
        invdiag=[C]+[Q(1)]*(n-1)
        assert max(invdiag)==C and min(1/x for x in invdiag)==1/C
    # Failure of an upper estimate is not failure of the actual energy gate.
    energy,cap,loose=Q(1),Q(2),Q(100)
    assert energy<cap<loose
    # Exact residual/Woodbury toy: S=2, A=1, D=1, Z=2/5.
    S,A,D,Z=Q(2),Q(1),Q(1),Q(2,5)
    r=A-S*Z;M=2*A*Z-Z*S*Z;E=D-M;Delta=D-A*A/S
    assert Delta==E-r*r/S==Q(1,2)
    h=S-A*A/D;assert 1/h==1/S+(A/S)**2/Delta
    return ['coordinate rescaling','missing old inverse energy','uniform nondecreasing chain',
            'upper bound failure not necessary failure','scalar residual identity']

def run(invpath,resppath):
    assert sha(invpath.read_bytes())==INV_SHA
    assert sha(resppath.read_bytes())==RESP_SHA
    wraw=(HERE/'pr226/WITNESSES.json').read_bytes();w=json.loads(wraw)
    assert w['source_archive_sha256']==INV_SHA
    out={'status':'PASS_CONDITIONAL_DIRECTIONAL_BUDGET_AND_REDUCED_INVERSE',
       'pr226_head':'ed31c343d9870d71b18e65bca1a1fa47cc097a23',
       'input_archives':{INV_NAME:INV_SHA,RESP_NAME:RESP_SHA},
       'witness_file_sha256':sha(wraw),'parities':{},'countercontrols':countercontrols(),
       'inherited_full_residual_and_operator_hypotheses':True,
       'new_big_integrations':False,'new_574_pivot_replay':False,
       'full_A9_inverse_one_direction_claim':False,'A9_A11_closed':False,
       'external_review_open':True}
    with zipfile.ZipFile(invpath) as iz,zipfile.ZipFile(resppath) as rz:
        binding=json.loads(member(iz,'SCHUR_INPUT_BINDINGS.json'))
        assert binding['responses']['sha256']==RESP_SHA
        for p in ('even','odd'):
            dr=member(iz,'INVERSE_'+p.upper()+'.json');d=json.loads(dr)
            rr=member(rz,'RESPONSES_'+p.upper()+'.json');r=json.loads(rr)
            assert sha(rr)==d['response_source_sha256']
            E=rat(d['E_rational']);M=rat(r['M_upper_rational']);K=rat(r['K12_new_rational'])
            X=rat(d['X84x203_rational']);assert X==rat(r['X84x203_rational'])
            rho=Q(r['rho']);em=Q(r['M_error_coefficient_rational'])
            beta=Q(d['beta']);c=Q(d['residual_cap']);snorm=Q(5,21)/beta
            assert beta==Q(20209999981781,182190000000000)
            assert c==(Q(1,250) if p=='even' else Q(71,10000))
            D=[[(1-rho) if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else Q(0) for j in range(203)] for i in range(203)]
            assert all(E[i][j]==D[i][j]-M[i][j] for i in range(203) for j in range(203))
            rows={}
            for key in ('u_E_min','u_E_second'):
                u=list(map(Q,w['parities'][p][key]));n=dot(u,u)
                du,mu,eu=quad(D,u),quad(M,u),quad(E,u)
                assert du>eu>0 and du-mu==eu
                ml,mh=iquad(r['M203_model'],u)
                rounding=(mu-em*du-mh,mu-em*du-ml)
                assert rounding[0]>0
                assert rounding[1]/eu<Q(1,10**36)
                modelgap=(du-mh,du-ml)
                actualM=(ml-em*du,mh+em*du)
                # Actual Delta = D-M-R*S^-1 R, with 0<=R*S^-1R<=c E.
                actualdelta=((1-c)*eu,du-actualM[0])
                assert actualdelta[1]>=actualdelta[0]>0
                x=mv(X,u);x2=dot(x,x)
                xlo=sqrt_box(x2)[0];errhi=sqrt_box(snorm*c*eu)[1]
                assert xlo>errhi
                invlower=(xlo-errhi)**2/actualdelta[1]
                row={'u_norm_squared':n,'u_low191_norm_fraction':dot(u[:191],u[:191])/n,
                     'D_direction':du,'M_upper_direction':mu,'E_direction':eu,
                     'D_Rayleigh':du/n,'M_upper_Rayleigh':mu/n,'E_Rayleigh':eu/n,
                     'E_relative_to_D':eu/du,'model_M_interval':[ml,mh],
                     'model_gap_interval':modelgap,'analytic_M_price':em*du,
                     'analytic_price_over_E':em*du/eu,'rounding_price_interval':rounding,
                     'rounding_upper_over_E':rounding[1]/eu,
                     'model_interval_width_over_E':(mh-ml)/eu,
                     'actual_M_interval':actualM,'actual_Delta_interval':actualdelta,
                     'actual_Delta_over_E':[v/eu for v in actualdelta],
                     'actual_Delta_relative_to_D':[v/du for v in actualdelta],
                     'X_u':x,'X_u_norm_squared':x2,'X_u_norm_lower':xlo,
                     'S_inverse_R_u_norm_upper':errhi,
                     'Hstar_inverse_Rayleigh_at_J_X_u_lower':invlower}
                if key=='u_E_min':
                    assert invlower>(55000 if p=='even' else 9300)
                    assert actualdelta[1]/eu<(Q(101755,100000) if p=='even' else Q(1000112,1000000))
                    assert em*du/eu<(Q(8775,10**6) if p=='even' else Q(5592,10**8))
                rows[key]=row
                print(p,key,'E/D',float(eu/du),'M-price/E',float(em*du/eu),
                     'Delta/E upper',float(actualdelta[1]/eu),'Hstar inverse lower',float(invlower),flush=True)
            P=rat(d['P_upper_rational']);v=list(map(Q,w['parities'][p]['v_hat']))
            pv=mv(P,v);vpv=dot(v,pv);assert vpv>0
            off=Q(11,10)*(snorm+Q(1000502,10**6)*Q(w['parities'][p]['eps']))
            assert off<(Q(468,100) if p=='even' else Q(277,100))
            out['parities'][p]={'response_member_sha256':sha(rr),'inverse_member_sha256':sha(dr),
                               'all_E_identity_entries_checked':203**2,'all_X_entries_matched':84*203,
                               'M_error_coefficient':em,'beta':beta,'residual_cap':c,
                               'S_inverse_norm_upper':snorm,'Hstar_inverse_off_spike_upper':off,
                               'W9_scalar_test':{'upper_vector_v':v,'lower_vector_Pv':pv,
                                  'v_P_v':vpv,'lower_weight':Q(11,10)/vpv,
                                  'upper_weight':Q(11,10)*Q(w['parities'][p]['mu']),
                                  'source_transform':'nu=N f, not f itself',
                                  'inequality':'(11/10)|<J P_upper v,N f>|^2/(v*P_upper*v) <= <f,W9 f>',
                                  'new_scalar_function_integrations_done':False},
                               'directions':rows}
    return encode(out)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--inputs',type=Path,default=DEFAULT_INPUTS)
    ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    assert __debug__ and not args.output.exists()
    result=run(args.inputs/INV_NAME,args.inputs/RESP_NAME)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(result['status'],flush=True)
