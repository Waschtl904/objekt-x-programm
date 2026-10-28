"""Targeted controls, no changes to any bound source or frozen package."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import check_source_specific as C
HERE=Path(__file__).resolve().parent
base=(F(720846,10**6),F(215033,50000),F(24,10000),F(437284983429949477,10**17))
cases=[("positive",base,True),
       ("core_lower_too_small",(F(7,10),*base[1:]),False),
       ("core_strictness_lost",(F(18,25),*base[1:]),False),
       ("coupling_lower_too_small",(base[0],F(4),base[2],base[3]),False),
       ("theta_too_large",(base[0],base[1],F(1,300),base[3]),False),
       ("theta_negative",(base[0],base[1],F(-1,400),base[3]),False),
       ("comparison_not_strict",(*base[:3],F(9,2)),False)]
results=[]
for name,values,expected in cases:
    try: C.verify_math(*values);accepted=True
    except RuntimeError: accepted=False
    if accepted!=expected:raise RuntimeError("Wrong control result: "+name)
    results.append({"case":name,"accepted":accepted,"expected":expected})
C.check_bindings()
bad=dict(C.BINDINGS);bad[next(iter(bad))]="0"*64
try:C.check_bindings(bad);accepted=True
except RuntimeError:accepted=False
if accepted:raise RuntimeError("Bad byte binding accepted")
results.append({"case":"incorrect_source_hash","accepted":False,"expected":False})
for opt in ("-O","-OO"):
    run=subprocess.run([sys.executable,opt,str(HERE/"check_source_specific.py")],capture_output=True,text=True)
    if run.returncode==0 or "OPTIMIZED_PYTHON_REJECTED" not in run.stderr:raise RuntimeError("Optimization guard")
    results.append({"case":opt,"accepted":False,"expected":False})
out={"status":"SOURCE_SPECIFIC_CONTROLS_PASS","count":len(results),"controls":results,
     "checker_sha256":hashlib.sha256((HERE/"check_source_specific.py").read_bytes()).hexdigest(),"integration_performed":False}
(HERE/"SOURCE_SPECIFIC_CONTROLS.json").write_text(json.dumps(out,indent=2)+"\n")
print(out["status"],len(results))
