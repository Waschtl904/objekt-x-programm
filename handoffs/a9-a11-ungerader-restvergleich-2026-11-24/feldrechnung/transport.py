"""Whole odd force estimate; input is the published finite result from 0cc0da9."""
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx

ctx.prec = 256
buf=Path(sys.argv[1]).read_bytes()
assert hashlib.sha1(b'blob '+str(len(buf)).encode()+b'\0'+buf).hexdigest()=='0cd7325cfed36fb357d6c44c0f2b7e14eeb491be'
published=json.loads(buf)
def q(value):
    v=Fraction(value)
    return arb(v.numerator)/v.denominator
def ub(v):
    return str(Fraction(str(v.upper().fmpq())))
a=3*arb(2).log()/2
b=arb(3).log()
h=b-a
mu=(a.sinh()-a)/2
lam=((b.sinh()-a.sinh()-h)/4).sqrt()
prime=2*sum((arb(p).log()/arb(n).sqrt() for p,n in [(2,2),(3,3),(2,4),(5,5),(7,7),(2,8)]),arb(0))
assert b<q("1.1") and (1+b*b.cosh()/6)/4<q("0.5")
reg=q("0.5")
cross=arb.pi()/2+(h/a).sqrt()/2+2*reg*(a*h).sqrt()+prime
norm_m=(2*mu).sqrt()
cv=abs((2*arb.pi()*a).log()+arb.const_euler())
vmax=(a/2).sinh()
q_m=(2*a).sqrt()*(a*(a/2).cosh()/2+vmax*(cv+arb(2).sqrt()/2+2*a*reg+prime))
lift=2*cross*norm_m*lam/mu+q_m*norm_m*(lam/mu)**2
shell=abs((2*arb.pi()*h).log()+arb.const_euler())+4+h/(2*a)+2*reg*h
# No same-wing shift is active. Opposite-wing distances range from log 8
# to log 9 and contain no prime-power shift in the open interval.
u0=shell+lift
C=9+max(arb(0),(u0-9*q("1.1")).upper())*5/21
force=C.sqrt()
err=force*q(published["grouped_force_error_K_inverse_upper"])
print({k:float(v.upper()) for k,v in dict(cross=cross,Qm=q_m,lift=lift,shell=shell,C=C,force=force,price=err).items()})
assert C<25 and force<5 and err<q("1.21e-9")
out={k:ub(v) for k,v in dict(raw_cross=cross,core_Qm=q_m,lift=lift,shell_constant=shell,
                              q_relative_L=C,force_cap=force,grouped_force_dual_error=err).items()}
out["whole_residual_certified"]=False
Path(sys.argv[2]).write_text(json.dumps(out,indent=2)+"\n",encoding='utf-8')
