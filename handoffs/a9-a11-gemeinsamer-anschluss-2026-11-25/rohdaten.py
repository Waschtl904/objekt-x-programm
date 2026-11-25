"""Generate fresh raw full-interval Grams from the old A8 engine, without terminal data."""
import hashlib
import sys
from pathlib import Path
from flint import ctx
from gamma_neu import coefficient_data

old = Path(sys.argv[1])
sys.path.insert(0, str(old))
for name, expected in {
    "generate_a8.py":"49de5bdeb80dc618206b34c4db3adcb07c602758fcc343b26498b31b5cfc5213",
    "rational_bounds.py":"8e9ae5784a341ae3ba4f5db07c6c6ebbdee4fbc375a59a963b071f77c14b7d5c",
}.items():
    content=(old/name).read_bytes()
    assert expected in {hashlib.sha256(content).hexdigest(),
                        hashlib.sha256(content.replace(b"\r\n",b"\n")).hexdigest()}
source = (old / "generate_a8.py").read_text(encoding="utf-8")
def replace(before, after):
    global source
    if source.count(before) != 1:
        raise RuntimeError(before)
    source = source.replace(before, after)

replace("a=3*arb(2).log()/2", "a=arb(11).log()/2")
replace("arb(2)/3 if q==2 else arb(4)/3 if q==4 else arb(q).log()/a", "arb(q).log()/a")
replace("[(2,2),(3,3),(4,2),(5,5),(7,7)]","[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]")
replace("assert 1<a<arb(21)/20 and channels[-1][2]<2 and channels[1][2]>1", "assert 1<a<arb(6)/5 and channels[-1][2]<2")
replace("Fraction(21,20)", "Fraction(6,5)")
replace("breaks=[arb(0),arb(1)/3,arb(1)]","breaks=[arb(0),arb(1)]")
replace("if q not in (2,4):breaks.append(b)\n                    else:assert b.overlaps(arb(1)/3)", "breaks.append(b)")
replace("'active_prime_powers':[2,3,4,5,7], 'exact_shift_relations':{'d2':'2/3','d4':'4/3'}", "'active_prime_powers':[2,3,4,5,7,8,9], 'exact_shift_relations':{}")
source = source.replace("3*log(2)/2", "log(11)/2").replace("Terminal A8=", "Raw joint interval A=")
replace("(Path(__file__).parent/'rational_bounds.py')","(OLD_ENGINE/'rational_bounds.py')")
space = {"__file__": __file__, "__name__": "old_engine_adapted", "OLD_ENGINE": old}
exec(compile(source, "old_engine_adapted", "exec"), space)
ctx.threads = 4
space["gamma_polynomial"] = lambda m: (coefficient_data(m)[0], None)
space["gamma_bound"] = lambda m, r: coefficient_data(m)[1]
output = Path(sys.argv[2]) if len(sys.argv)>2 else Path(__file__).with_name("raw_joint_cheb.json.gz")
space["compute"](383, 160, 2304, str(output))
