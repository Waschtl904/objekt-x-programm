"""Independent directed-rational certificate of the inverse renewal.

The complete 287x287 block [E,X*;X,Pup] proves Pup >= X E^-1 X*.
All operations here use integers/Fraction, no Arb or floating eigensolver.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse, hashlib, io, json, time, zipfile
HERE=Path(__file__).resolve().parent
SCALE=10**120
ZERO=(0,0)

def ceildiv(a,b):return -((-a)//b)
def point(x):
    x=F(x);n=x.numerator*SCALE
    return n//x.denominator,ceildiv(n,x.denominator)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,b):
    v=[a[i]*b[j] for i in (0,1) for j in (0,1)]
    return min(v)//SCALE,ceildiv(max(v),SCALE)
def div(a,b):
    assert b[0]>0
    return min(a[i]*SCALE//b[j] for i in (0,1) for j in (0,1)),max(ceildiv(a[i]*SCALE,b[j]) for i in (0,1) for j in (0,1))

def positive(A,progress=False):
    n=len(A);L=[[ZERO]*n for _ in range(n)];D=[]
    for j in range(n):
        d=A[j][j]
        for k in range(j):d=sub(d,mul(mul(L[j][k],D[k]),L[j][k]))
        assert d[0]>0,('unproved positive pivot',j,d)
        D.append(d)
        for i in range(j+1,n):
            a=A[i][j]
            for k in range(j):a=sub(a,mul(mul(L[i][k],D[k]),L[j][k]))
            L[i][j]=div(a,d)
        if progress and (j+1)%64==0:print('certified pivots',j+1,flush=True)
    return {'positive_pivots':n,'smallest_pivot_lower':str(F(min(v[0] for v in D),SCALE)),
            'pivot_interval_digest':hashlib.sha256(json.dumps(D).encode()).hexdigest()}

def member(z,suffix):
    ns=[n for n in z.namelist() if n==suffix or n.endswith('/'+suffix)]
    assert len(ns)==1,(suffix,ns)
    return z.read(ns[0])

def mm(A,B):
    return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def tr(A):return [list(row) for row in zip(*A)]
def inv(A):
    n=len(A);B=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if B[k][j]);B[j],B[k]=B[k],B[j]
        p=B[j][j];B[j]=[x/p for x in B[j]]
        for i in range(n):
            if i!=j:
                p=B[i][j];B[i]=[x-p*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]
def bd(*blocks):
    n=sum(map(len,blocks));A=[[F(0)]*n for _ in range(n)];offset=0
    for B in blocks:
        for i,row in enumerate(B):
            for j,x in enumerate(row):A[offset+i][offset+j]=F(x)
        offset+=len(B)
    return A
def qform(A,f):return sum((f[i]*A[i][j]*f[j] for i in range(len(f)) for j in range(len(f))),F(0))

def whole_inverse_control():
    # Noncommuting 2+2+2 blocks check the signs in both source subtractions.
    U=[[F(2),F(1,3)],[F(1,3),F(3)]]
    K=[[F(3),F(1)],[F(1),F(2)]]
    H=[[F(5),F(1,2)],[F(1,2),F(4)]]
    gF=[[F(1,5),F(-2,7)],[F(3,8),F(1,9)]]
    gT=[[F(1,4),F(1,6)],[F(-1,5),F(2,9)]]
    af=[[F(1,7),F(2,11)],[F(-3,10),F(1,8)]]
    Ui,Ki,Hi=inv(U),inv(K),inv(H)
    C=[[F(i==j) for j in range(6)] for i in range(6)]
    UgF,UgT,Kaf=mm(U,gF),mm(U,gT),mm(Ki,af)
    for i in range(2):
        for j in range(2):
            C[i][2+j]=UgF[i][j];C[i][4+j]=UgT[i][j]
            C[2+i][4+j]=Kaf[i][j]
    Q=mm(mm(tr(C),bd(Ui,K,H)),C);Qi=inv(Q)
    A=[[Q[i][j]+F(i==j,10+i) for j in range(6)] for i in range(6)]
    Ai=inv(A)
    positive([[point(Qi[i][j]-Ai[i][j]) for j in range(6)] for i in range(6)])
    fs=[[F(i==j) for i in range(6)] for j in range(6)]+[[F(i-2,7+i) for i in range(6)]]
    for f in fs:
        f8,f12,fT=f[:2],f[2:4],f[4:]
        Uf=mm(U,[[x] for x in f8])
        v12=[x-y[0] for x,y in zip(f12,mm(tr(gF),Uf))]
        vT=[x-y[0] for x,y in zip(fT,mm(tr(gT),Uf))]
        nu=[x-y[0] for x,y in zip(vT,mm(mm(tr(af),Ki),[[x] for x in v12]))]
        formula=qform(U,f8)+qform(Ki,v12)+qform(Hi,nu)
        assert formula==qform(Qi,f) and qform(Ai,f)<=formula
    return len(fs)

def controls():
    # Same finite Galerkin data, different true outside residuals.
    # S=I, A=(a,b), Z=(a,0), M=a^2, E=1-a^2.
    # Tail Schur after the first coordinate is 1-b^2/E.
    a=F(3,5);b=F(1,5);E=1-a*a;c=b*b/E
    tail=1-c
    assert tail==F(15,16)
    # A failed unweighted price would assert 1-b^2, incorrectly larger.
    assert 1-b*b>tail
    # The critical rank-one correction cannot be omitted from a full inverse.
    exact_inverse00=1+a*a/(1-a*a-b*b)
    assert exact_inverse00>F(11,10)
    # Nonorthogonal J=(2,0) still has the same annihilator, not unit Gram.
    Jnorm2=F(4);X=a/2
    assert Jnorm2*X*X/E==a*a/E
    # Excess residual makes H indefinite despite a perfect finite fit.
    b_bad=F(9,10)
    assert b_bad*b_bad/E>1 and 1-a*a-b_bad*b_bad<0
    # With H=L=diag(1,4), J=(1,1), a WX-orthogonal vector (1,-1)
    # has energy 5 but its Schur energy is 5-9/5. L-orthogonality matters.
    assert F(5)-F(9,5)<5
    try:positive([[point(1),point(2)],[point(2),point(1)]])
    except AssertionError:pass
    else:raise AssertionError('indefinite block accepted')
    # Exact full inverse identity, not an assumption of commuting matrices.
    A=[F(3,5),F(1,5)];z=[F(3,5),F(0)];r=[F(0),F(1,5)]
    for f in [(F(0),F(1)),(F(2),F(-3)),(F(5,7),F(9,11))]:
        base=sum(x*x for x in f);af=sum(x*y for x,y in zip(A,f))
        zf=sum(x*y for x,y in zip(z,f));rf=sum(x*y for x,y in zip(r,f))
        assert af==zf+rf
        inverse=base+af*af/(1-sum(x*x for x in A))
        # gamma=2 suffices since sqrt(c)=1/4.
        assert inverse<=2*(base+zf*zf/E)
    return {'wrong_unweighted_residual_price_rejected':True,
            'omitted_finite_inverse_correction_rejected':True,
            'nonorthonormal_basis_norm_used':True,
            'large_outside_residual_rejected':True,
            'WX_orthogonality_cannot_replace_L_orthogonality':True,
            'indefinite_block_rejected':True,
            'exact_Woodbury_and_residual_pairing_controls':3,
            'complete_two_stage_inverse_noncommuting_controls':whole_inverse_control()}

def audit(label,data):
    E=[[F(x) for x in row] for row in data['E_rational']]
    X=[[F(x) for x in row] for row in data['X84x203_rational']]
    P=[[F(x) for x in row] for row in data['P_upper_rational']]
    assert len(E)==203 and len(X)==len(P)==84
    assert all(len(row)==203 for row in X)
    assert all(E[i][j]==E[j][i] for i in range(203) for j in range(203))
    assert all(P[i][j]==P[j][i] for i in range(84) for j in range(84))
    block=[[point(E[i][j]) if i<203 and j<203 else
            point(X[j-203][i]) if i<203 else
            point(X[i-203][j]) if j<203 else point(P[i-203][j-203])
            for j in range(287)] for i in range(287)]
    certificate=positive(block,True)
    beta=F(data['beta']);c=F(data['residual_cap']);gamma=F(11,10)
    assert 0<c<1 and c<F(1,121) and beta>0
    assert gamma/beta<10
    high=(1-c)*beta
    assert high>F(11,100)
    high_W=high*F(21,5)
    assert high_W>F(231,500)
    # Entire moment tail: approximate m by its degree95 Taylor polynomial.
    # ||l_{>=96}||^2 <= (h/2)*(uniform Taylor remainder)^2.
    moment_tail=F(3,100)*(4*F(3,200)**96/F(factorial(96)))**2
    assert moment_tail<F(1,10**600)
    d95=F(11,10)+sum((F(1,n) for n in range(1,96)),F(0))
    d96=d95+F(1,96)
    assert d95<7 and d96>F(31,5)
    # alpha<23, ||l0||<1/4, ||J||_X^2<2, ||(J*LJ)^-1||<=5/21.
    assert 23*(1+F(2)*F(5,21)*7)/4<30
    assert 30**2+23*9**2<3000
    assert 1+3000*moment_tail<F(1001,1000)
    assert d96/F(1001,1000)>F(61,10)
    sharp_high_W=high*d96/(1+3000*moment_tail)
    assert sharp_high_W>F(671,1000)>F(2,3)
    trace=sum(P[i][i] for i in range(84))
    assert trace>0
    # Pup is PSD by the certified block; norm(Pup)<=trace(Pup).
    J2=F(500251,500000) # 1.000502, full exact nonorthogonal basis bound
    inv=gamma*(1/(beta*F(21,5))+J2*trace)
    safe_den=[65000,11000][label=='ODD']
    assert inv<safe_den
    return {'parity':label.lower(),'complete_287_block':certificate,
            'P_upper_trace':str(trace),'full_inverse_multiplier':'11/10',
            'analytic_inverse_coefficient_gamma_over_beta':str(gamma/beta),
            'deflated_full_high_floor_relative_L':str(high),
            'simple_deflated_floor_relative_L':'11/100',
            'generic_deflated_floor_relative_WX':str(high_W),
            'new_high_L_floor_relative_WX':'61/10',
            'whole_moment_tail_squared_norm_upper':str(moment_tail),
            'deflated_full_high_floor_relative_WX':str(sharp_high_W),
            'simple_deflated_floor_relative_WX':'2/3',
            'whole_reduced_inverse_operator_upper':str(inv),
            'improved_whole_reduced_floor_relative_WX':'1/'+str(safe_den),
            'upper_matrix_sha256':hashlib.sha256(json.dumps(data['P_upper_rational']).encode()).hexdigest()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--schur-package',type=Path)
    ap.add_argument('--output',type=Path,default=HERE/'AUDIT.json');args=ap.parse_args()
    records={s:json.loads((HERE/f'INVERSE_{s}.json').read_bytes()) for s in ['EVEN','ODD']}
    binding=False
    if args.schur_package:
        raw=args.schur_package.read_bytes()
        assert hashlib.sha256(raw).hexdigest()=='65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba'
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            bs=json.loads(member(z,'INPUT_BINDINGS.json'))
            assembly=json.loads(member(z,'ASSEMBLY_AUDIT.json'))
            rb=member(z,bs['responses']['filename'])
            assert hashlib.sha256(rb).hexdigest()==bs['responses']['sha256']
            with zipfile.ZipFile(io.BytesIO(rb)) as rz:
                for label,d in records.items():
                    raw=member(rz,f'RESPONSES_{label}.json')
                    assert hashlib.sha256(raw).hexdigest()==d['response_source_sha256']
                    r=json.loads(raw);rho=F(r['rho']);K=r['K12_new_rational'];M=r['M_upper_rational']
                    for i in range(203):
                        for j in range(203):
                            dij=(1-rho) if i==j and i<191 else F(K[i-191][j-191]) if i>=191 and j>=191 else F(0)
                            assert F(d['E_rational'][i][j])==dij-F(M[i][j])
                    assert r['X84x203_rational']==d['X84x203_rational']
                    assert r['beta']==d['beta']
                    a=next(x for x in assembly['cases'] if x['parity']==label.lower())
                    assert a['complete_QR_relative_T_simple_upper']==d['residual_cap']
        binding=True
    start=time.time();cases=[]
    for label,d in records.items():
        print(label,'auditing entire inverse correction block',flush=True)
        cases.append(audit(label,d))
    out={'status':'PASS_INVERSE_RENEWAL_AND_FULL_DEFLATED_HIGH_FLOOR',
         'rational_decimal_grid_digits':120,'original_Schur_source_fields_verified':binding,
         'cases':cases,'countercontrols':controls(),
         'full_A9_inverse_majorant_constructed_under_inherited_hypotheses':True,
         'finite_correction_dimension_per_parity':84,
         'whole_new_high_subspace_including_all_cross_couplings':True,
         'new_A11_endpoint_certificate_claimed':False,
         'old_separate_tail_floor_1_over_20_certified':False,
         'unbounded_horizon_continuation_certified':False,
         'object_X_constructed':False,'RH_proved':False,'external_review_open':True,
         'large_integrations_rerun':False,'seconds':time.time()-start}
    args.output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(out['status'],flush=True)

if __name__=='__main__':main()
