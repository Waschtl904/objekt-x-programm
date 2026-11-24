"""Bound individual operator differences for the frozen odd source in the inherited form metrics."""
import sys
from pathlib import Path

shared = Path(__file__).with_name("features.py")
program = shared.read_text(encoding="utf8")
exec(compile(program[:program.index("out={}")], str(shared), "exec"))
from residuals import Residuals
from directed_output import upper_decimal
from old_fields import gamma_coefficients

a, b = e.a8, e.a
mu = (a.sinh()-a)/2
lam = ((b.sinh()-a.sinh()-(b-a))/4).sqrt()
lift = (1+2*lam**2/mu).sqrt()
tr = json.loads(args.transport.read_bytes())
cross = q(tr["raw_cross"])
qm = q(tr["core_Qm"])
gcap = cross+qm*lam/mu

# Recheck the midpoint of the actual response used in the 3072-bit builder.
res = Residuals(inputs, "odd")
dnorm = []
for fn in res.funcs:
    field = fn["D"]
    scalar = sum(abs(q(v)) for v in field["polynomial"])
    scalar += 2*sum(abs(q(v)) for v in field["V_multiplier"])
    scalar += abs(q(field["moment_multiplier"]))*(b/2).exp()
    scalar += sum(abs(q(v)) for st in field["shift_terms"] for v in st["polynomial"])
    dnorm.append(scalar)
new_t = norm(res.T_enclosure-res.T)*sum(x*x for x in dnorm).sqrt()
old_t = e.residual_errors["frozen_T_Hilbert"]
extra_t = max(arb(0), (new_t-old_t).upper())*2
assert norm(coef)<2
assert new_t<old_t and gamma>=1
fdata=inputs.json("functions")["parities"]["odd"]
fresponse=inputs.json("response")["parities"]["odd"]["fixed_X"]
d_delta=Fraction(fdata["whole_D12_operator_error_upper"])
t_sq=Fraction(fresponse["T_norm_squared_upper"])
d_bound=Fraction(fresponse["whole_Hilbert_residual_model_error_upper"])
assert d_delta*d_delta*t_sq<=d_bound*d_bound

# Measure the exact appended midpoint freezes in local orthonormal coordinates.
def diff_exact(A, data):
    expected = fmpq_mat([[fmpq(x) for x in row] for row in data])
    assert A.nrows()==expected.nrows() and A.ncols()==expected.ncols()
    total=fmpq(0)
    for i in range(A.nrows()):
        for j in range(A.ncols()):
            assert A[i,j].is_exact()
            total += (A[i,j].fmpq()-expected[i,j])**2
    return arb(total).sqrt()
dy = diff_exact(model["Y"],inputs.json("frozen_Y_odd")["Y_local_rational_midpoints"])
dj = diff_exact(model["J"],inputs.json("frozen_J_odd")["working_basis_midpoints_rational"])
dw = diff_exact(w,[[x] for x in finite["w_rational"]])
ybare, jbare = e.eBareF+dy*lift,e.eBareJ+dj*lift
jn = lift*norm(model["J"])+jbare
yn = lift*norm(model["Y"])+ybare
zn2 = sum((sum(v*v*2*b/(2*i+1) for i,v in enumerate(ls)) for _,ls in model["zp"]),arb(0))
fn = (zn2+yn**2).sqrt()
reg = e.bounds["old_FJ_regular_kernel_uniform_error"]
wn,pn,fnorm = norm(w),norm(p),norm(ff)

# Compare raw sources with exact moment carrier throughout this step.
rawF = 2*b*reg*fn+1000*ybare
rawJ = 2*b*reg*jn+1000*jbare
physical_h = eps_h+extra_t
raw_err = gamma.sqrt()*(rawJ*wn+rawF*pn+e.eRawA*fnorm+physical_h)
low_err = e.eLJ*wn+quad(e.ELF,p).abs_upper().sqrt()+e.eLowA*fnorm+gamma.sqrt()*physical_h
old = inputs.json('a8_model')
coeffs_old = list(map(q,old['Gamma_polynomial_coefficients']))
assert len(coeffs_old)==161
theory=gamma_coefficients(160)
stored_gamma_error=sum((abs(x-y).upper()*a**j for j,(x,y) in enumerate(zip(coeffs_old,theory))),arb(0))
assert stored_gamma_error<q('1e-800')
raw_err+=gamma.sqrt()*2*a*stored_gamma_error*gamma.sqrt()*fnorm
Am = arb_mat([[q(lo).union(q(hi))/10**100 for lo,hi in row] for row in old["parities"]["odd"]["A"]])
cs = mat(raw['galerkin']['old_low_c_model'])*w-e.ell*coef-mat(raw['old_certificate']['source_c_model'])*p
low_round = norm(cs-Am*ff-low)
# The two inputs compared here are the true high vector and the unlifted
# raw-minus-low reconstruction. The subsequent high lift has its own row.
high_raw_X = gcap*(raw_err+low_err+low_round)/delta
assert gcap<100 and lift<2
oldq = q(tr["q_relative_L"])
H95 = sum((arb(1)/k for k in range(1,96)),arb(0))
w_round_dual = oldq*(H95+q("1.1")).sqrt()*jn*dw

# L2 operator on the bounded-degree shell basis, including the core lift
# and the scalar moment adjoint. All terms are in the raw, half-shell norm.
moment_op = lam/mu
regK=q('0.5')+reg
shell_log = 96*arb(2).sqrt()  # sum of both half-log potentials on (0,1)
shellQ = H95 + abs((2*arb.pi()*(b-a)).log()+arb.const_euler()) + shell_log
shellQ += 2*(b-a)*regK+(b-a)/(2*a)
crossK=cross+2*b*reg
qmK=qm+2*b*reg*(2*mu).sqrt()
frozen_cap = shellQ + crossK*moment_op*(2*mu).sqrt()
frozen_cap += moment_op*(2*mu).sqrt()*crossK+moment_op**2*(2*mu).sqrt()*qmK
q_coord = frozen_cap*(jbare*wn+ybare*pn)
q_gamma = lift*2*b*reg*(jn*wn+fn*pn)
h_direct = lift*physical_h
high_plus_direct=(q("5/21")).sqrt()*(high_raw_X+q_coord+q_gamma+h_direct)
assert frozen_cap<1000 and crossK+qmK*moment_op<1000
observed=dict(raw_source=raw_err,low_source=low_err,low_rounding=low_round,
              high_to_shell_X=high_raw_X,shell_partial_dual=high_plus_direct,
              cross_lift_X=gcap,shell_basis_cap=frozen_cap,
              q_coord_X=q_coord,q_gamma_X=q_gamma,direct_h_X=h_direct,
              extra_response_h=extra_t,response_T_old=old_t,response_T_here=new_t,
              frozen_J_error=dj,frozen_Y_error=dy,frozen_w_error=dw,w_round_dual=w_round_dual,
              lift=lift,F_norm=fn,J_norm=jn,finite_feature_error=eta_err,
              stored_gamma_coefficients_error=stored_gamma_error)
result={k:upper_decimal(v) for k,v in observed.items()}
result['scope']='RAW_MINUS_LOW_AND_DIRECT_SOURCE_DIFFERENCES'
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print({k:float(v.upper()) for k,v in observed.items()},flush=True)
