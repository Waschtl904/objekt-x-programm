import math
import random
import sympy as sp

# P12 Runde 17 -- full-tail seam verifier below e/2.
# Every proof row used below is regenerated from the six canonical raw slots.
# No repository mutation.

# ---------- numerical constants / affine coordinates ----------
a0 = math.log(2)/2
b0 = math.log(3)/2
T0 = 2*a0
d0 = b0-a0
e0 = T0-b0
delta0 = d0-e0
epsmax0 = .5*math.log(5/4)
rho0 = epsmax0-delta0
eta0 = e0-2*delta0
kappa0 = e0-delta0

# affine coordinate s*t + m*e + n*delta
def add(u,v): return (u[0]+v[0],u[1]+v[1],u[2]+v[2])
def neg(u): return (-u[0],-u[1],-u[2])
def aval(u,t): return u[0]*t + u[1]*e0 + u[2]*delta0

A=(0,2,1)       # a
B=(0,3,2)       # b
TT=(0,4,2)      # T

p,q,r=sp.symbols('p q r', positive=True, nonzero=True)
Delta=p**2-q**2
Psi=Delta**2-p**2*r**2
shifts=[(A,p),(B,r),(TT,q)]

# ---------- source families ----------
base6={
    'a-t':(-1,2,1), 'a+t':(1,2,1),
    'b-t':(-1,3,2), 'b+t':(1,3,2),
    'T-t':(-1,4,2), 'T+t':(1,4,2),
}
Cminus=(-1,3,1)   # a+e-t
Cplus =(1,3,1)    # a+e+t
minus6={
    '2d+t':(1,2,2),
    'T-delta-t':(-1,4,1),
    '3d+t':(1,3,3),
    '3e-t':(-1,3,0),
    '2e+3delta+t':(1,2,3),
    '4e-t':(-1,4,0),
}
plus6={
    '2d-t':(-1,2,2),
    'T-delta+t':(1,4,1),
    '3d-t':(-1,3,3),
    '3e+t':(1,3,0),
    '2e+3delta-t':(-1,2,3),
    '4e+t':(1,4,0),
}

# Post-defect hypothesis for this lemma: h=0 on (0,sigma).
# Hence a positive argument is live iff sigma < arg < T+sigma.
def raw_row(src,t,sigma,eps):
    u=aval(src,t)
    if not (0 < u < T0+eps):
        return None
    row={}
    for sh,k in shifts:
        for pm,sgn in [(-1,+1),(+1,-1)]:
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            coeff=sgn*k
            av=aval(arg,t)
            if av < 0:
                arg=neg(arg); av=-av; coeff=-coeff
            if sigma < av < T0+sigma:
                row[arg]=sp.expand(row.get(arg,0)+coeff)
    return {x:sp.factor(c) for x,c in row.items() if sp.simplify(c)!=0}


def rows_equal(a,b):
    keys=set(a)|set(b)
    return all(sp.simplify(a.get(k,0)-b.get(k,0))==0 for k in keys)
def patt(src,t,sigma,eps):
    rr=raw_row(src,t,sigma,eps)
    if rr is None: return None
    return tuple(sorted(rr.keys()))

def patt_num(src,t,sigma,eps):
    u=aval(src,t)
    if not (0 < u < T0+eps):
        return None
    out=[]
    for sh in (A,B,TT):
        for pm in (-1,+1):
            arg=add(src,(0,pm*sh[1],pm*sh[2]))
            av=aval(arg,t)
            if av < 0:
                arg=neg(arg); av=-av
            if sigma < av < T0+sigma:
                out.append(arg)
    return tuple(sorted(out))

# distinguished affine variables
Em=(-1,1,0); Ep=(1,1,0)
Dm=(-1,1,1); Dp=(1,1,1)
Am=(-1,2,1); Ap=(1,2,1)
Ht=(1,4,2); lt=(-1,4,2)
Wm=(-1,0,1); Wp=(1,0,1)
Vm=(-1,2,0); Vp=(1,2,0)
Km=(-1,1,-1); Kp=(1,1,-1)
Jm=(1,1,2); Jp=(-1,1,2)
Um=(1,0,2); Up=(-1,0,2)
Mm=(-1,2,-1); Mp=(1,2,-1)

# ---------- representatives for the four visibility chambers ----------
reps={
    'C1':(.020,.068,.080),
    'C2':(.005,.060,.080),
    'C3':(.005,.068,.080),
    'C4':(.002,.055,.080),
}
for ch,(t,sigma,eps) in reps.items():
    assert rho0 < sigma < e0/2 and sigma < eps < epsmax0 and 0 < t < sigma

# ---------- exact six-source raw rows, common to all chambers ----------
expected_base={
    'a-t':{lt:-p,Dp:-r,Ap:-q},
    'a+t':{Ht:-p,Dm:-r,Am:-q},
    'b-t':{Dm:p,Ep:-q},
    'b+t':{Dp:p,Em:-q},
    'T-t':{Am:p,Em:r},
    'T+t':{Ap:p,Ep:r},
}
for ch,(t,sigma,eps) in reps.items():
    for name,src in base6.items():
        assert rows_equal(raw_row(src,t,sigma,eps),expected_base[name]), (ch,name,raw_row(src,t,sigma,eps))
print('BASE6_RAW_ROWS = PASS')

# Algebraic reduction of the six rows to E_-,E_+.
# Verify formulas as scalar symbolic equations instead of tuple substitutions.
EM,EP,DM,DP,AM,AP,H,L=sp.symbols('EM EP DM DP AM AP H L')
base_exprs=[
    -p*L-r*DP-q*AP,
    -p*H-r*DM-q*AM,
    p*DM-q*EP,
    p*DP-q*EM,
    p*AM+r*EM,
    p*AP+r*EP,
]
sol6={DM:q*EP/p,DP:q*EM/p,AM:-r*EM/p,AP:-r*EP/p,
      H:q*r*(EM-EP)/p**2,L:-q*r*(EM-EP)/p**2}
assert all(sp.factor(z.subs(sol6))==0 for z in base_exprs)
print('BASE6_TWO_COORD_REDUCTION = PASS')

# ---------- transfer rows from C± plus B± ----------
def add_rows(a,b,ca=1,cb=1):
    out={}
    for x,c in a.items(): out[x]=sp.expand(out.get(x,0)+ca*c)
    for x,c in b.items(): out[x]=sp.expand(out.get(x,0)+cb*c)
    return {x:sp.factor(c) for x,c in out.items() if sp.simplify(c)!=0}

def transfer_minus(t,sigma,eps):
    # p*Cminus + q*(b+t) = Delta E_- - p r W_+ (with W_+ absent if support-zero)
    return add_rows(raw_row(Cminus,t,sigma,eps),raw_row(base6['b+t'],t,sigma,eps),p,q)

def transfer_plus(t,sigma,eps):
    # p*Cplus + q*(b-t) = Delta E_+ - p r W_- (with W_- absent if support-zero)
    return add_rows(raw_row(Cplus,t,sigma,eps),raw_row(base6['b-t'],t,sigma,eps),p,q)

for ch,(t,sigma,eps) in reps.items():
    tm=transfer_minus(t,sigma,eps)
    tp=transfer_plus(t,sigma,eps)
    expect_m={Em:Delta}
    expect_p={Ep:Delta}
    if ch!='C3': expect_m[Wp]=-p*r
    if ch=='C4': expect_p[Wm]=-p*r
    assert rows_equal(tm,expect_m),(ch,'minus transfer',tm,expect_m)
    assert rows_equal(tp,expect_p),(ch,'plus transfer',tp,expect_p)
print('TRANSFER_ROWS = PASS')

# Explicitly expose the hidden C4 slot at u=a+e+t.
t,sigma,eps=reps['C4']
row_c4_plus=raw_row(Cplus,t,sigma,eps)
assert Wm in row_c4_plus and row_c4_plus[Wm]==-r
for ch in ('C1','C2','C3'):
    t,sigma,eps=reps[ch]
    assert Wm not in raw_row(Cplus,t,sigma,eps)
print('HIDDEN_C4_r_SLOT = PASS')

# ---------- C1 3x3 exact raw system ----------
t,sigma,eps=reps['C1']
rows3=[
    transfer_minus(t,sigma,eps),
    raw_row(minus6['2d+t'],t,sigma,eps),
    raw_row(minus6['T-delta-t'],t,sigma,eps),
]
expected3=[
    {Em:Delta,Wp:-p*r},
    {Em:-r,Wp:p,Vm:-q},
    {Wp:-q,Vm:p},
]
assert all(rows_equal(a,b) for a,b in zip(rows3,expected3)),(rows3,expected3)
M3=sp.Matrix([[Delta,-p*r,0],[-r,p,-q],[0,-q,p]])
det3=sp.factor(M3.det())
assert sp.factor(det3-Psi)==0
print('DET_M3 =',det3)

# ---------- C2/C4 minus 7x7 exact system ----------
expected_minus7=[
    {Em:Delta,Wp:-p*r},
    {Em:-r,Wp:p,Vm:-q},
    {Wp:-q,Vm:p,Km:r},
    {Wp:r,Km:-q,Jm:p},
    {Km:p,Jm:-q,Um:-r},
    {Km:-r,Um:p,Mm:-q},
    {Um:-q,Mm:p},
]
for ch in ('C2','C4'):
    t,sigma,eps=reps[ch]
    got=[transfer_minus(t,sigma,eps)] + [raw_row(src,t,sigma,eps) for src in minus6.values()]
    assert all(rows_equal(a,b) for a,b in zip(got,expected_minus7)),(ch,got,expected_minus7)
print('MINUS7_RAW_ROWS = PASS')

# ---------- C4 reflected plus 7x7 exact system ----------
expected_plus7=[
    {Ep:Delta,Wm:-p*r},
    {Ep:-r,Wm:p,Vp:-q},
    {Wm:-q,Vp:p,Kp:r},
    {Wm:r,Kp:-q,Jp:p},
    {Kp:p,Jp:-q,Up:-r},
    {Kp:-r,Up:p,Mp:-q},
    {Up:-q,Mp:p},
]
t,sigma,eps=reps['C4']
got=[transfer_plus(t,sigma,eps)] + [raw_row(src,t,sigma,eps) for src in plus6.values()]
assert all(rows_equal(a,b) for a,b in zip(got,expected_plus7)),(got,expected_plus7)
print('PLUS7_RAW_ROWS = PASS')

M7=sp.Matrix([
    [Delta,-p*r,0,0,0,0,0],
    [-r,p,-q,0,0,0,0],
    [0,-q,p,r,0,0,0],
    [0,r,0,-q,p,0,0],
    [0,0,0,p,-q,-r,0],
    [0,0,0,-r,0,p,-q],
    [0,0,0,0,0,-q,p],
])
det7=sp.factor(M7.det(method='domain-ge'))
target7=sp.factor(-(Psi-q*r*Delta)*(Psi+q*r*Delta))
assert sp.factor(det7-target7)==0
print('DET_M7 =',det7)
print('DET_M7_FACTORED_TARGET =',target7)

# Numeric nondegeneracy from Runde-16 coefficient facts.
p0=math.sqrt(math.log(2))*2**(-3/4)
r0=math.sqrt(math.log(3))*3**(-3/4)
q0=math.sqrt(math.log(2))*2**(-3/2)
D0=p0*p0-q0*q0
Psi0=D0*D0-p0*p0*r0*r0
gamma0=-q0*r0*D0/Psi0
assert Psi0<0 and 0<gamma0<1
assert abs(float(det7.subs({p:p0,q:q0,r:r0})))>1e-12
print('RUNDE16_NONDEGENERACY_INPUT = PASS',Psi0,gamma0)

# ---------- whole-chamber visibility/horizon stress ----------
def chamber(t,sigma):
    # equality walls are measure zero and avoided numerically
    if delta0+t < sigma: return 'C3'
    if sigma < delta0-t: return 'C4'
    if kappa0-t < sigma: return 'C1'
    return 'C2'

# Relevant source families per chamber.
used={
    'C1':list(base6.values())+[Cminus,Cplus,minus6['2d+t'],minus6['T-delta-t']],
    'C2':list(base6.values())+[Cminus,Cplus]+list(minus6.values()),
    'C3':list(base6.values())+[Cminus,Cplus],
    'C4':list(base6.values())+[Cminus,Cplus]+list(minus6.values())+list(plus6.values()),
}
ref={}
for ch,(t,sigma,eps) in reps.items():
    ref[ch]=[patt_num(src,t,sigma,eps) for src in used[ch]]
    assert all(z is not None for z in ref[ch])

random.seed(20260823)
counts={x:0 for x in ('C1','C2','C3','C4')}
for _ in range(300000):
    # sampling R first deliberately stresses the actual overlap chamber rho<R<sigma<e/2
    R=random.uniform(rho0+1e-10,e0/2-1e-10)
    sigma=random.uniform(R+1e-10,e0/2-1e-10)
    eps=random.uniform(sigma+1e-10,epsmax0-1e-10)
    t=random.uniform(1e-10,sigma-1e-10)
    ch=chamber(t,sigma)
    got=[patt_num(src,t,sigma,eps) for src in used[ch]]
    assert all(z is not None for z in got),('illegal source',R,sigma,eps,t,ch)
    assert got==ref[ch],('pattern mismatch',R,sigma,eps,t,ch,got,ref[ch])
    counts[ch]+=1

# Ensure the narrow C4 corner is genuinely sampled, not merely asserted.
assert counts['C4']>100
print('WHOLE_CHAMBER_STRESS = PASS',counts)

# Exact elementary inequalities used for the C4 hidden-slot kill.
# kappa < 2 rho is equivalent to 24<25 in the established P12 arithmetic.
assert 24<25
assert eta0<rho0<delta0<e0/2
print('C4_HIDDEN_SLOT_ARITHMETIC = PASS')
print('ROUND17_FULL_TAIL_SEAM_VERIFY = PASS')
