import math, random
import sympy as sp

# Runde 16 hard-horizon full-kill verifier.
# Generates every matrix row from the six canonical raw operator slots.

# ---------- constants ----------
a0=math.log(2)/2
b0=math.log(3)/2
T0=2*a0
d0=b0-a0
e0=T0-b0
delta0=d0-e0
epsmax0=.5*math.log(5/4)
rho0=epsmax0-delta0
eta0=e0-2*delta0
theta0=2*e0-3*delta0

p,q,r=sp.symbols("p q r", positive=True, nonzero=True)
Delta=p**2-q**2
Psi=Delta**2-p**2*r**2

A=(0,2,1)
B=(0,3,2)
TT=(0,4,2)
shifts_sym=[(A,p),(B,r),(TT,q)]
shifts_num=[A,B,TT]

def add(u,v):
    return (u[0]+v[0],u[1]+v[1],u[2]+v[2])
def neg(u):
    return (-u[0],-u[1],-u[2])
def aval(u,x):
    return u[0]*x+u[1]*e0+u[2]*delta0

# committed 18 hard-horizon sources
base18=[
(-1,3,2),(1,3,2),(-1,2,1),(-1,4,2),(1,4,2),(1,3,1),
(-1,1,0),(-1,3,1),(1,1,1),(1,3,3),(1,2,2),(-1,2,0),
(-1,4,1),(1,0,1),(1,1,2),(1,2,3),(-1,4,0),(-1,5,1)
]

# new 11 x-transfer sources
x11=[
(-1,3,0),(1,3,4),(-1,1,-1),(-1,2,-1),(1,0,2),(1,1,3),
(-1,5,0),(1,2,4),(-1,4,-1),(-1,5,-1),(1,1,4)
]

sources29=base18+x11

# old 19-source family, used only to define selected translated y sources
old19=[
(-1,3,2),(1,3,2),(-1,2,1),(-1,4,2),(1,4,2),(1,3,1),
(-1,1,0),(-1,3,1),(1,1,1),(1,3,3),(1,2,2),(-1,2,0),
(-1,4,1),(1,0,1),(-1,5,2),(1,1,2),(1,2,3),(-1,4,0),(-1,5,1)
]

# y = theta-x = -x+2e-3delta
def y_to_x(src):
    s,m,n=src
    return (-s, 2*s+m, -3*s+n)

translated_y=[y_to_x(s) for s in old19]
selected_y_indices=[0,2,3,4,5,6,8,11,13,14,15]
y11=[translated_y[i] for i in selected_y_indices]

u_star=(1,-1,2)  # x-eta
sources41=sources29+y11+[u_star]

# ---------- raw row generator ----------
def raw_row_symbolic(src,x,R,sigma,eps):
    u=aval(src,x)
    if not (0<u<T0+eps):
        return None
    row={}
    for sh,k in shifts_sym:
        for pm,sgn in [(-1,+1),(+1,-1)]:
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            coeff=sgn*k
            av=aval(arg,x)
            if av<0:
                arg=neg(arg)
                av=-av
                coeff=-coeff
            if R<av<T0+sigma:
                row[arg]=sp.expand(row.get(arg,0)+coeff)
    return {arg:sp.simplify(c) for arg,c in row.items()
            if sp.simplify(c)!=0}

def make_matrix(sources,x,R,sigma,eps):
    rows=[raw_row_symbolic(s,x,R,sigma,eps) for s in sources]
    assert all(rr is not None for rr in rows)
    variables=sorted(set().union(*[set(rr) for rr in rows]))
    M=sp.zeros(len(rows),len(variables))
    for i,rr in enumerate(rows):
        for v,c in rr.items():
            M[i,variables.index(v)]=c
    return M,variables,rows

# ---------- Case A reference: reflected y is support-zero ----------
RA=.055
xA=.061
sigA=.066
epsA=.072
yA=theta0-xA
assert xA>delta0
assert yA<RA

M29A,v29A,rows29A=make_matrix(sources29,xA,RA,sigA,epsA)
assert M29A.shape==(29,29)

K=2*p**2-2*q**2-r**2
det29=sp.factor(M29A.det(method="domain-ge"))
target29=sp.factor(
    2*p**11*q*r**3*(p-q)**2*(p+q)**2
    *(Delta-p*r)**2*(Delta+p*r)**2*K
)
print("DET29 =",det29)
print("DET29_DIFF =",sp.factor(det29-target29))
assert sp.factor(det29-target29)==0

# ---------- Case B: y live, H(z) dead ----------
RB=.053
xB=.055
sigB=.0575
epsB=.060
yB=theta0-xB
zB=e0-yB
assert RB<yB
assert zB>sigB

M29B,v29B,rows29B=make_matrix(sources29,xB,RB,sigB,epsB)
assert M29B.shape==(29,30)

Xaff=(1,0,0)
Yaff=(-1,2,-3)
Zyaff=(1,-1,3)
ix=v29B.index(Xaff)
iy=v29B.index(Yaff)
iz=v29B.index(Zyaff)

def det_delete(M,j):
    cols=[k for k in range(M.cols) if k!=j]
    return sp.factor(M[:,cols].det(method="domain-ge"))

DY=det_delete(M29B,iy)
DX=det_delete(M29B,ix)
DZ=det_delete(M29B,iz)

target_DY=target29
target_DX=sp.factor(
    -p**10*q**2*r**5*(p-q)**2*(p+q)**2
    *(Delta-p*r)**2*(Delta+p*r)**2
)
target_DZ=sp.factor(
    2*p**11*q**2*r**4*(p-q)**3*(p+q)**3
    *(Delta-p*r)*(Delta+p*r)*K
)

assert sp.factor(DY-target_DY)==0
assert sp.factor(DX-target_DX)==0
assert sp.factor(DZ-target_DZ)==0

# For a full-row-rank m x (m+1) matrix, null-vector cofactors are
# (-1)^j det(M with column j deleted).
lambda_expr=sp.factor(
    sp.Integer((-1)**(iy-ix))*DY/DX
)
gamma_expr=sp.factor(
    sp.Integer((-1)**(iz-iy))*DZ/DY
)

target_lambda=sp.factor(-2*p*K/(q*r**2))
target_gamma=sp.factor(-q*r*Delta/Psi)

print("LAMBDA =",lambda_expr)
print("LAMBDA_DIFF =",sp.factor(lambda_expr-target_lambda))
print("GAMMA =",gamma_expr)
print("GAMMA_DIFF =",sp.factor(gamma_expr-target_gamma))
assert sp.factor(lambda_expr-target_lambda)==0
assert sp.factor(gamma_expr-target_gamma)==0

# ---------- Case C: long tail ----------
RC=.053
xC=.0545
sigC=.088
epsC=.089
yC=theta0-xC
zC=e0-yC
assert RC<yC
assert zC<sigC

M41,v41,rows41=make_matrix(sources41,xC,RC,sigC,epsC)
assert M41.shape==(41,41)

Fpoly=2*p**4-3*p**2*q**2-p**2*r**2+q**4-q**2*r**2
Gpoly=(12*p**6-24*p**4*q**2-14*p**4*r**2
       +12*p**2*q**4+18*p**2*q**2*r**2+4*p**2*r**4
       -4*q**4*r**2-3*q**2*r**4)

det41=sp.factor(M41.det(method="domain-ge"))
target41=sp.factor(
    p**16*q*r**6*(p-q)**2*(p+q)**2
    *(Delta-p*r)*(Delta+p*r)*Fpoly*Gpoly
)
print("DET41 =",det41)
print("DET41_DIFF =",sp.factor(det41-target41))
assert sp.factor(det41-target41)==0

# ---------- exact arithmetic inequality checks ----------
assert 3**12 > 2**19
assert 3**5 < 2**8
assert 20000 > 19683      # (2/3)^(3/2) > 27/50 after squaring
assert 2048 < 2187        # (2/3)^(3/2) < 9/16 after squaring
assert 50 > 49            # u > 7/20
assert 8 < 9              # u < 3/8
assert 625 < 648          # beta < 3/5
assert 116281 < 121032    # u < 123/341
assert 32768 < 32805      # theta < epsmax

# actual coefficients: numeric sanity only
p0=math.sqrt(math.log(2))*2**(-3/4)
r0=math.sqrt(math.log(3))*3**(-3/4)
q0=math.sqrt(math.log(2))*2**(-3/2)
D0=p0*p0-q0*q0
Psi0=D0*D0-p0*p0*r0*r0
K0=2*p0*p0-2*q0*q0-r0*r0
lam0=-2*p0*K0/(q0*r0*r0)
gam0=-q0*r0*D0/Psi0
F0=float(Fpoly.subs({p:p0,q:q0,r:r0}))
G0=float(Gpoly.subs({p:p0,q:q0,r:r0}))
print("actual lambda =",lam0)
print("actual gamma =",gam0)
print("actual K,F,G =",K0,F0,G0)
assert abs(lam0)>1
assert 0<gam0<1
assert K0>0
assert F0<0
assert G0>0

# ---------- fast numeric pattern stress ----------
def pattern(src,x,R,sigma,eps):
    u=aval(src,x)
    if not (0<u<T0+eps):
        return None
    out=[]
    for sh in shifts_num:
        for pm in (-1,+1):
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            av=aval(arg,x)
            if av<0:
                arg=neg(arg); av=-av
            if R<av<T0+sigma:
                out.append(arg)
    return tuple(sorted(out))

refA=[pattern(s,xA,RA,sigA,epsA) for s in sources29]
refB=[pattern(s,xB,RB,sigB,epsB) for s in sources29]
refC=[pattern(s,xC,RC,sigC,epsC) for s in sources41]

random.seed(20260823)

# A: y<=R
nA=0
for _ in range(120000):
    R=random.uniform(rho0+1e-10,e0/2-1e-10)
    eps_hi=min(epsmax0,e0-R)-1e-10
    if eps_hi<=R: continue
    eps=random.uniform(R+1e-9,eps_hi)
    sigma=random.uniform(R+1e-10,eps-1e-10)
    xhi=min(sigma,d0-sigma,e0-eps)
    if xhi<=R: continue
    x=random.uniform(R+1e-10,xhi-1e-10)
    y=theta0-x
    if y>R: continue
    assert [pattern(s,x,R,sigma,eps) for s in sources29]==refA
    nA+=1

# B: y>R, z>=sigma
nB=0
for _ in range(180000):
    R=random.uniform(rho0+1e-10,e0/2-1e-10)
    eps_hi=min(epsmax0,e0-R)-1e-10
    if eps_hi<=R: continue
    eps=random.uniform(R+1e-9,eps_hi)
    sigma=random.uniform(R+1e-10,eps-1e-10)
    xhi=min(sigma,d0-sigma,e0-eps)
    if xhi<=R: continue
    x=random.uniform(R+1e-10,xhi-1e-10)
    y=theta0-x
    z=e0-y
    if not (y>R and z>=sigma): continue
    assert [pattern(s,x,R,sigma,eps) for s in sources29]==refB
    nB+=1

# C: y>R, z<sigma
nC=0
attempts=0
while nC<30000 and attempts<1000000:
    attempts+=1
    R=random.uniform(rho0+1e-10,delta0-1e-10)
    x=random.uniform(R+1e-10,delta0-1e-10)
    y=theta0-x
    if y<=R: continue
    z=e0-y
    sigma_lo=max(R,z)+1e-10
    eps_hi=min(epsmax0,e0-x)-1e-10
    if sigma_lo>=eps_hi: continue
    eps=random.uniform(sigma_lo+1e-10,eps_hi)
    sigma=random.uniform(sigma_lo,eps-1e-10)
    if not (x<sigma and x<d0-sigma): continue
    assert [pattern(s,x,R,sigma,eps) for s in sources41]==refC
    nC+=1

print("PATTERN_STRESS_A =",nA)
print("PATTERN_STRESS_B =",nB)
print("PATTERN_STRESS_C =",nC)
assert nA>1000 and nB>1000 and nC==30000

print("ROUND16_HARD_HORIZON_FULL_KILL_VERIFY = PASS")
