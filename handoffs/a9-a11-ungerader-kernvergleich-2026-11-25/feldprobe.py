"""Build a quadrature diagnostic of the restored odd-shell source."""
import argparse
import hashlib
import sys
from pathlib import Path

here=Path(__file__).resolve().parent
sys.path.insert(0,str(here))
opts=argparse.ArgumentParser(add_help=False)
opts.add_argument("--case",choices=("s","e"),default="s")
choice,rest=opts.parse_known_args()
sys.argv[1:]=rest
parent_dir=Path(sys.argv.pop(1)).resolve()
source=parent_dir/"odd_field_control.py"
def git_blob(path):
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
assert git_blob(source)=="ae80dcef68c98497278cf7904558536000ab07a8"
assert git_blob(parent_dir/"measure.py")=="a2f597fb35c5befad1a655fee1c0bb10224f72da"
code=source.read_bytes().decode().replace("\r\n","\n")
def replace(old,new):
    global code
    assert code.count(old)==1,old
    code=code.replace(old,new)
start=code.index("class View:")
end=code.index("res=resmod.Residuals")
code=code[:start]+'''case_data=bound["trial_"+DIRECTION]
wv=c.ratmat([[v] for v in case_data["test"][12:]]);w=wv
ytrue=c.ratmat([[v] for v in case_data["test"][:12]])
e=Energy(inps,load_pairs(src/"expected/PAIRS_odd.json.gz"))
cc0=c.ratmat([[v] for v in case_data["raw"]])
env={"inp":inps,"c":cc0/quad(e.G,cc0).sqrt()}
'''+code[end:]
replace('pv=midmat(ki*(aa*w-e.v*coeff))','pv=midmat(-ytrue)')
replace("ff=midmat(C*C.transpose()*(cs-bys/delta)/(1-rho))",'''old_delta=delta
delta=q("1.84298")
data=inps.json("common")["cases"][1]
def scaled_int(rows,den):
    return arb_mat([[q(v)/q(den) for v in row] for row in rows])
F8=scaled_int(data["F_integer_matrix"],data["F_denominator"])
HB=scaled_int(data["HB_integer_matrix"],data["HB_denominator"])
G0=midmat(c.mat(raw["old_raw_coupling_gram"])/q(10**100))
M=midmat(C.transpose()*(F8+HB/old_delta-G0/delta)*C)
ff=midmat(C*M.solve(C.transpose()*(cs-bys/delta)))''')
replace("eta=q('1e-10');zero=", "eta=q('0');zero=")
sys.path.insert(0,str(parent_dir))
# Scope of this driver is a numerical field diagnostic. The old 84 reference
# in measure.py belongs to another rule. Suppress it and its comparison.
replace("from measure import measure",'''measure_code=(PARENT/"measure.py").read_text(encoding="utf8")
measure_code=measure_code[:measure_code.index("    direct_lo=")]+measure_code[measure_code.index("    span="):]
measure_code=measure_code[:measure_code.index("    rj=")]+measure_code[measure_code.index("    return dict(nodes="):]
measure_code=measure_code[:measure_code.index("                norm_P_feature_mismatch=")].rstrip(",\\n")+")"
exec(compile(measure_code,"field_measure","exec"),globals())''')
exec(compile(code,str(source)+"::restored", "exec"),{"__name__":"__main__","__file__":str(Path(__file__).resolve()),"PARENT":parent_dir,"DIRECTION":choice.case})
