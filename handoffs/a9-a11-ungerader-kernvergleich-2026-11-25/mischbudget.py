"""Actual mixed K_P by polarization of two rational, scaled directions."""
import argparse
from fractions import Fraction as F
from pathlib import Path
import json
import sys
from bindungen import checked_pkg, PAIRS
parser=argparse.ArgumentParser()
for k in ("root","sources","output"): parser.add_argument(k,type=Path)
args=parser.parse_args()
pkg=checked_pkg(args.root)
sys.path.insert(0,str(pkg))
from common import Inputs, enc, q, box, mat
from assemble import load_pairs,quad
from certify_k import certify
from flint import arb_mat,ctx
ctx.prec=1536
inputs=Inputs()
t=json.loads(args.sources.read_bytes())
e=list(map(F,t["trial_e"]["raw"])); s=list(map(F,t["trial_s"]["raw"]))
pairs=load_pairs(pkg/"expected/PAIRS_odd.json.gz")
assert pairs["_source_sha256"]==PAIRS
G=mat(pairs["G_W"])
def norm2(x):return quad(G,arb_mat([[q(z)] for z in x]))
factor=10**7
legs=[]
for k in (factor,-factor):
    v=[sv+k*ev for sv,ev in zip(s,e)]
    cert=certify(inputs,pairs,list(map(str,v)))
    legs.append(cert["K_P_interval"]*norm2(v))
mix=(legs[0]-legs[1])/(4*factor*(norm2(s)*norm2(e)).sqrt())
print("mixed direct K",enc(mix),flush=True)
args.output.write_text(json.dumps(dict(scale=factor,mixed=enc(mix)),indent=2)+"\n",encoding="utf8")
