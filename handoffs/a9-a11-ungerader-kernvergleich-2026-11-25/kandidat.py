"""Directed K_P for the rational direction selected by the finite diagnostic."""
import argparse
import json
import sys
from pathlib import Path
from flint import ctx
from bindungen import checked_pkg, PAIRS

parser=argparse.ArgumentParser()
for key in ("root","source","output"): parser.add_argument(key,type=Path)
args=parser.parse_args()
pkg=checked_pkg(args.root)
sys.path.insert(0,str(pkg))
from common import Inputs, encode
from assemble import load_pairs
from certify_k import certify
data=json.loads(args.source.read_bytes())
coeffs=list(map(str,data["trial_min_model"]["raw"]))
ctx.prec=1536
pairs=load_pairs(pkg/"expected/PAIRS_odd.json.gz")
assert pairs["_source_sha256"]==PAIRS
result=encode(certify(Inputs(),pairs,coeffs))
args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf8")
from fractions import Fraction as F
lo,hi=map(F,result["K_P_interval"])
l,u=map(F,data["trial_min_model"]["price"])
print("K_P",float(lo),float(hi),"K_P minus tested value",[float(lo-u),float(hi-l)],flush=True)
