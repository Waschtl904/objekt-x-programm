"""Whole raw core/shell cap from the exact real Gamma kernel.

Conditional on the inherited identification of Q with the displayed physical
operator. No inherited polynomial Gamma remainder is used in this cap proof.
"""
import sys
if not __debug__:raise SystemExit('Assertions required')
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib
from fractions import Fraction
from flint import arb,fmpq,ctx
ctx.prec=512
W=Path(__file__).resolve().parent
R=W.parent/'pr254-review'
proof=R/'research/x-c1/a9-inverse-spike-calibration-2026-10-15/original/nstar/FUNKTIONSANSCHLUSS.txt'
source_manifest=json.loads((W.parent/'binding-model-review-2026-10-23/SOURCE_BINDINGS.json').read_bytes())['repository_files']
assert hashlib.sha256(proof.read_bytes()).hexdigest()==source_manifest[proof.relative_to(R).as_posix()]['sha256']
q=lambda n,d=1:arb(fmpq(n,d))
a=3*arb(2).log()/2;b=arb(3).log();hs=b-a;mu=(a+a.sinh())/2
assert 0<a<b<q(11,10)
assert q(11,10).cosh()<2
# Gamma(z)=(sech z+csch z-1/z)/4, 0<z<=b.
# 0<=1/z-csch z<=(sinh z-z)/z²<=z*cosh(11/10)/6.
assert (1+Fraction(11,10)*2/6)/4==Fraction(41,120)
gamma_exact_cap=q(41,120)
assert gamma_exact_cap<q(1,2)
prime=2*sum((arb(p).log()/arb(n).sqrt()for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2))),arb(0))
lambdaop=((hs+b.sinh()-a.sinh())/4).sqrt()
mn=(2*a).sqrt()*(a/2).cosh()
cv=abs(-(2*arb.pi()).log()-arb.const_euler()-a.log()).upper()
def caps(reg):
    cross=arb.pi()/2+(hs/a).sqrt()/2+2*reg*(a*hs).sqrt()+prime
    qm=(2*a).sqrt()*a*(a/2).sinh()/2+mn*(cv+arb(2).sqrt()/2+arb(2).log()/2+2*a*reg+prime)
    raw=cross+lambdaop*qm/mu
    # Full degree <=95 lifted shell functions; low polynomial leakage allowed.
    harmonic95=sum((q(1,n)for n in range(1,96)),arb(0))
    v0=-(2*arb.pi()).log()-arb.const_euler()-hs.log()
    core=cross+qm*lambdaop/mu
    shell=harmonic95+96*(abs(v0).upper()+arb(2).sqrt())+hs/(2*a)+2*reg*hs+prime+cross*(2*mu).sqrt()*lambdaop/mu
    local=(core**2+shell**2).sqrt()
    return {'cross':cross,'Q8_m':qm,'raw_g_and_density_adjoint':raw,'local_degree95_Q':local}
tighter=caps(q(1,2));legacy=caps(q(2))
assert legacy['cross']<q(9023,1000)
assert legacy['Q8_m']<q(23401,1000)
assert legacy['raw_g_and_density_adjoint']<q(13066,1000)<100
assert tighter['raw_g_and_density_adjoint']<legacy['raw_g_and_density_adjoint']
assert legacy['local_degree95_Q']<10000
# D_H x^k = H_k*x^k - sum_{j odd<k} x^(k-1-j)/(j+1), from
# splitting its difference-quotient integral at x. Verify all degrees used
# in the finite shell cap, exactly, not by samples.
F=Fraction
legendre=[[F(1)],[F(0),F(1)]]
for n in range(1,95):
    pn=[F(0)]+[F(2*n+1,n+1)*v for v in legendre[-1]]
    for k,v in enumerate(legendre[-2]):pn[k]-=F(n,n+1)*v
    legendre.append(pn)
harmonic=[F(0)]
for n in range(1,96):harmonic.append(harmonic[-1]+F(1,n))
for n,pn in enumerate(legendre):
    action=[F(0)]*len(pn)
    for k,v in enumerate(pn):
        action[k]+=v*harmonic[k]
        for j in range(1,k,2):action[k-1-j]-=v/F(j+1)
    assert action==[harmonic[n]*v for v in pn],n
enc=lambda v:[str(v.lower().fmpq()),str(v.upper().fmpq())]
out={'status':'RAW_OPERATOR_CAP_DERIVED_AND_CHECKED_CONDITIONAL_ON_PHYSICAL_Q',
 'physical_Q_source':str(proof.relative_to(R)).replace('\\','/'),'physical_Q_source_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'Gamma_exact_uniform_cap':'41/120','used_real_Gamma_cap':'1/2','Gamma_polynomial_error_used':False,
 'bounds_with_half':{k:enc(v)for k,v in tighter.items()},
 'bounds_with_legacy_two':{k:enc(v)for k,v in legacy.items()},
 'raw_cap_100_valid_including_low_leakage':True,'full_Q8_m_bound_100_valid':True,
 'local_degree95_cap_10000_valid':True,'finite_coordinates_used_to_estimate_whole_operator':False,
 'exact_DH_Legendre_actions_verified':96,
 'force_cap_10_independently_reproved':False,'arithmetic_form_identification_reproved':False,
 'Gamma_model_approximation_error_reproved':False,'external_acceptance':False}
(W/'raw-operator-result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'half_cap_values':{k:v.str(15)for k,v in tighter.items()},'legacy_two_values':{k:v.str(15)for k,v in legacy.items()}},indent=2))
