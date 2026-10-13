"""Check the numerical constants used in the full function-error lemmas."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import sys,json,gzip,argparse
HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=HERE.parents[1]);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();ROOT=args.root
sys.path[:0]=[str(ROOT/'work/compute-deps'),str(ROOT/'work/galerkin84-2026-10-10'),str(ROOT/'work/tail-probe-2026-10-10/vendor')]
from flint import arb,ctx,fmpq
from safe_serial import serial
from source_core import gamma_polynomial
ctx.prec=1536
def af(v):
 q=F(v);return arb(fmpq(q.numerator,q.denominator))
def read(p):
 b=p.read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b'\x1f\x8b' else b)
base=ROOT/'work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09'
shell=read(base/'work/gamma-low-2026-10-09/SHELL_GAMMA_4096.json')
old=read(base/'work/remainder-integration-check-v2/originals/weighted-response/inputs/a8_model.json.gz')
inp=read(ROOT/'work/direct-rest84-2026-10-11/REFINED_INPUT.json')['cases']
a=3*arb(2).log()/2;b=arb(3).log();h=b-a
assert a>1 and a<af('1.05') and h>af('0.05') and h<af('0.06')
_,eg=gamma_polynomial(224);eg=af(eg);assert eg<af('1e-34')
es=af(shell['self_kernel_error_exact']);assert es<af('1e-50')
em=(-129*a).exp()/(1-(-4*a).exp());assert em<af('1e-50')
core0=2*(a/2)**161/factorial(161)/(1-a/(2*162))
core1=(a/2)**160/factorial(160)/(1-a/(2*161))
shell0=2*(h/4)**161/factorial(161)/(1-h/(4*162))
assert core0<af('1e-300') and core1<af('1e-300') and shell0<af('1e-300')
rows=[]
for p,P in enumerate(['EVEN','ODD']):
 tr=read(ROOT/f'work/inner-log-2026-10-12/TRACES_{P}_3072.json')
 assert F(tr['J_rounding'][1])<F(1,10**60) and F(tr['Y_rounding'][1])<F(1,10**60)
 def width(mm):return max(F(v[1])-F(v[0]) for rr in mm for v in rr)
 assert width(inp[p]['old_certificate']['source_c_model'])<F(1,10**69)
 assert width(inp[p]['galerkin']['old_low_c_model'])<F(1,10**79)
 assert max(F(v[1])-F(v[0]) for v in tr['old_Qphi_carrier'])<F(1,10**79)
 aa=old['parities'][P.lower()]['A']
 aw=max(F(int(v[1])-int(v[0]),10**100) for rr in aa for v in rr)
 assert aw<F(1,10**69)
 # Global Q graph bound 1e20 on the fixed degree <=95 source span.
 # Factor 1000 covers all Gamma-source norms; constants are derived in PROOF.
 sourcecap=1000*eg+af('1e-40')+100*es+100*em
 assert sourcecap<af('1e-28')
 rows.append({'parity':P.lower(),'complete_source_function_error_per_column_cap':sourcecap,'old_A_interval_width':str(aw),
  'local_J_rounding_upper':tr['J_rounding'][1],'local_Y_rounding_upper':tr['Y_rounding'][1]})
out={'status':'PASS_FULL_FUNCTION_ERROR_PARAMETERS','Gamma224_error':eg,'shell_self_error':es,'whole_mirror_tail':em,'core_moment_uniform_error':core0,'core_moment_derivative_error':core1,'shell_moment_uniform_error':shell0,'certified_moment_remainder_caps':{'core_function':'1e-300','core_derivative':'1e-300','shell_function':'1e-300'},'cases':rows,'full_remainder_certified':False}
args.out.write_text(json.dumps(serial(out,100),indent=2)+'\n');print('PASS complete function-error constants',flush=True)
