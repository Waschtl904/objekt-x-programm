import math, random
import sympy as sp

# P12 Runde 15H — independent 18-source hard-horizon verifier
# No repo mutation.  Generates rows from the canonical raw operator first,
# then compares to the claimed 18 equations and proves an exact rank-18 minor.

# ---------- constants ----------
a0=math.log(2)/2
b0=math.log(3)/2
T0=2*a0
d0=b0-a0
e0=T0-b0
delta0=d0-e0
epsmax0=.5*math.log(5/4)
rho0=epsmax0-delta0

# affine coordinate sx*x + me*e + md*delta
def add(u,v): return tuple(u[i]+v[i] for i in range(3))
def neg(u): return tuple(-z for z in u)
def aval(u,x): return u[0]*x+u[1]*e0+u[2]*delta0

A=(0,2,1)       # a
B=(0,3,2)       # b
TT=(0,4,2)      # T

p,q,r=sp.symbols("p q r", positive=True, nonzero=True)
shifts=[(A,p,"a"),(B,r,"b"),(TT,q,"T")]

# Hard-horizon 18 sources = old 19-source list without u15=T+e-x.
sources=[
(-1,3,2),(1,3,2),(-1,2,1),(-1,4,2),(1,4,2),(1,3,1),
(-1,1,0),(-1,3,1),(1,1,1),(1,3,3),(1,2,2),(-1,2,0),
(-1,4,1),(1,0,1),(1,1,2),(1,2,3),(-1,4,0),(-1,5,1)
]
source_names=[
"b-x","b+x","a-x","T-x","T+x","a+e+x",
"e-x","a+e-x","d+x","3d+x","2d+x","2e-x",
"T-delta-x","delta+x","d+delta+x","a+2delta+x",
"4e-x","a+3e-x"
]

# 19 live variables in the hard-horizon pattern.
# Tuple -> display variable.
varmap={
 (1,0,2):"A=h(2delta+x)",
 (1,1,2):"B=h(d+delta+x)",
 (1,0,1):"C=h(delta+x)",
 (1,3,3):"D=h(3d+x)",
 (1,2,2):"E=h(2d+x)",
 (-1,1,1):"F=h(d-x)",
 (1,1,1):"G=h(d+x)",
 (1,0,0):"X=h(x)",
 (1,3,2):"I=h(b+x)",
 (-1,2,1):"J=h(a-x)",
 (1,2,1):"K=h(a+x)",
 (1,1,0):"L=h(e+x)",
 (-1,4,2):"M=h(T-x)",
 (-1,3,1):"N=h(a+e-x)",
 (-1,2,0):"O=h(2e-x)",
 (-1,4,1):"Q=h(T-delta-x)",
 (-1,3,0):"U=h(3e-x)",
 (-1,2,-1):"W=h(a-2delta-x)",
 (-1,1,0):"Z=h(e-x)",
}
reverse={v.split("=")[0]:k for k,v in varmap.items()}

# Representative point strictly inside hard-horizon chamber.
R0=.055
sigma0=.058
eps0=.060
x0=.056
assert rho0 < R0 < e0/2
assert R0 < x0 < sigma0 < eps0 < epsmax0
assert e0-x0 > eps0
S0=T0+sigma0
H0=T0+eps0

def raw_reduce(src):
    """Generate one equation ONLY from six canonical slots."""
    u=aval(src,x0)
    assert 0<u<H0, ("source horizon",src,u,H0)
    row={}
    logs=[]
    for sh,k,sname in shifts:
        for pm,sgn,slotname in [
            (-1,+1,f"u-{sname}"),
            (+1,-1,f"u+{sname}")
        ]:
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            coeff=sgn*k
            num=aval(arg,x0)
            anti=False
            if num<0:
                arg=neg(arg); num=-num; coeff=-coeff; anti=True
            live=R0<num<S0
            logs.append((slotname,arg,coeff,num,anti,live))
            if live:
                if arg not in varmap:
                    raise AssertionError(("unexpected live variable",src,slotname,arg,num))
                row[arg]=sp.expand(row.get(arg,0)+coeff)
    return {k:sp.simplify(v) for k,v in row.items() if sp.simplify(v)!=0}, logs

generated=[]
for j,(src,name) in enumerate(zip(sources,source_names),1):
    row,logs=raw_reduce(src)
    generated.append(row)
    print(f"\nSOURCE {j:02d}: u={name}, affine={src}, value={aval(src,x0):.12f}")
    for slot,arg,c,num,anti,live in logs:
        label=varmap.get(arg,f"dead affine {arg}")
        print(f"  {slot:5s} {sp.sstr(c):>3s} * {label:24s} "
              f"|arg|={num:.12f} {'LIVE' if live else 'ZERO'}"
              f"{' anti' if anti else ''}")

# Claimed rows, encoded only AFTER raw generation.
A1,B1,C1,D1,E1,F1,G1,X,I,J,K,L,M,N,O,Q,U,W,Z=sp.symbols(
    "A1 B1 C1 D1 E1 F1 G1 X I J K L M N O Q U W Z")
vars=[A1,B1,C1,D1,E1,F1,G1,X,I,J,K,L,M,N,O,Q,U,W,Z]

claimed=[
 p*F1-r*X-q*L,
 p*G1+r*X-q*Z,
 -p*X-p*M-r*G1-q*K,
 p*J+r*Z-q*X,
 p*K+r*L+q*X,
 p*L-q*F1,
 -p*G1-p*N-r*E1-r*M-q*I,
 p*Z-r*C1-q*G1,
 -p*Z-p*I-r*J-q*N,
 p*B1+r*C1,
 p*C1-r*Z-q*O,
 -p*C1-p*Q-r*B1-q*E1,
 p*O-q*C1,
 -p*O-p*E1-r*N-r*D1-q*Q,
 -p*D1-r*O-q*U,
 p*A1-q*W,
 p*W-q*A1,
 p*U+r*W
]

sym_to_aff={
 A1:(1,0,2), B1:(1,1,2), C1:(1,0,1), D1:(1,3,3),
 E1:(1,2,2), F1:(-1,1,1), G1:(1,1,1), X:(1,0,0),
 I:(1,3,2), J:(-1,2,1), K:(1,2,1), L:(1,1,0),
 M:(-1,4,2), N:(-1,3,1), O:(-1,2,0), Q:(-1,4,1),
 U:(-1,3,0), W:(-1,2,-1), Z:(-1,1,0)
}

for j,(grow,expr) in enumerate(zip(generated,claimed),1):
    expected={}
    ex=sp.expand(expr)
    for v in vars:
        c=sp.simplify(ex.coeff(v))
        if c:
            expected[sym_to_aff[v]]=c
    keys=set(grow)|set(expected)
    diff={k:sp.simplify(grow.get(k,0)-expected.get(k,0)) for k in keys}
    diff={k:v for k,v in diff.items() if v!=0}
    assert not diff,(j,diff)
    print(f"EXACT_RAW_ROW_MATCH {j:02d}: PASS")

# Exact 18x19 coefficient matrix and rank-18 minor.
Mat=sp.Matrix([[sp.expand(eq).coeff(v) for v in vars] for eq in claimed])
assert Mat.shape==(18,19)
minor_without_Z=Mat[:,:18]  # Z is final column
det_minor=sp.factor(minor_without_Z.det(method="domain-ge"))
target_det=sp.factor(
    -p**6*q*r*(p-q)**3*(p+q)**3
    *(p**2-p*r-q**2)*(p**2+p*r-q**2)
)
print("\nDET_MINOR_WITHOUT_Z =",det_minor)
print("DET_MINUS_TARGET =",sp.factor(det_minor-target_det))
assert sp.factor(det_minor-target_det)==0

# Short gamma relation check.
Delta=p**2-q**2
Psi=Delta**2-p**2*r**2
gamma=-q*r*Delta/Psi

# E11 + E13
C_expr=p*r/Delta*Z
# E2
G_expr=(q*Z-r*X)/p
E8res=sp.factor((p*Z-r*C1-q*G1).subs({C1:C_expr,G1:G_expr}))
target_gamma_eq=sp.factor((Psi*Z+q*r*Delta*X)/(p*Delta))
print("E8_AFTER_E11_E13_E2 =",E8res)
print("GAMMA_RELATION_DIFF =",sp.factor(E8res-target_gamma_eq))
assert sp.factor(E8res-target_gamma_eq)==0

# E17/E18/E19 auxiliary zeros.
pairdet=sp.factor(p**2-q**2)
print("PAIR_DETERMINANT =",pairdet)

# Numeric arithmetic coefficients.
p0=math.sqrt(math.log(2))*2**(-3/4)
r0=math.sqrt(math.log(3))*3**(-3/4)
q0=math.sqrt(math.log(2))*2**(-3/2)
D0=p0*p0-q0*q0
alpha0=p0*r0/D0
Psi0=D0*D0-p0*p0*r0*r0
gamma0=-q0*r0*D0/Psi0
print("actual alpha =",alpha0)
print("actual Psi =",Psi0)
print("actual gamma =",gamma0)
assert alpha0>1
assert abs(gamma0*gamma0-1)>1e-6

# Adversarial uniform-pattern/horizon stress.
ref=[set(raw_reduce(s)[0].keys()) for s in sources]

def pattern_at(src,x,R,sigma,eps):
    u=aval(src,x)
    if not (0<u<T0+eps):
        return None
    out=set()
    for sh,_,_ in shifts:
        for pm in (-1,+1):
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            num=aval(arg,x)
            if num<0:
                arg=neg(arg); num=-num
            if R<num<T0+sigma:
                out.add(arg)
    return out

random.seed(15018)
n=0
for _ in range(100000):
    R=random.uniform(rho0+1e-9,e0/2-1e-9)
    # Hard horizon requires some eps<e-R.
    eps_hi=min(epsmax0,e0-R)-1e-9
    if eps_hi<=R+3e-9:
        continue
    eps=random.uniform(R+2e-9,eps_hi)
    sigma=random.uniform(R+1e-9,eps-1e-9)
    x_hi=min(sigma,d0-sigma,e0-eps)
    if x_hi<=R+1e-9:
        continue
    x=random.uniform(R+1e-10,x_hi-1e-10)
    pats=[pattern_at(s,x,R,sigma,eps) for s in sources]
    assert all(z is not None for z in pats)
    assert pats==ref,(R,sigma,eps,x)
    n+=1

print("HARD_HORIZON_18_SOURCE_STRESS = PASS",n)
print("ROUND15H_18_SOURCE_VERIFY = PASS")
