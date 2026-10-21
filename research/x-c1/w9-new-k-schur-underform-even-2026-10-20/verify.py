"""Separate single-vector selection, certification and bounded fresh replay."""
import argparse
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path
from types import ModuleType

HERE=Path(__file__).resolve().parent
OUTPUTS=("WEIGHTS.json","CANDIDATE.json","RESULT.json")

def need(ok,message):
    if not ok: raise RuntimeError(message)

def module(name,raw,path):
    m=ModuleType(name);m.__file__=str(path);sys.modules[name]=m
    exec(compile(raw,str(path),"exec"),m.__dict__)
    return m

def serialize(value):
    return (json.dumps(value,indent=2)+"\n").encode()

def worker(args):
    need(__debug__,"Do not use python -O")
    checked={}
    if args.freeze:
        for name in ("engine.py","audit.py","INPUT_BINDINGS.json"):
            checked[name]=(HERE/name).read_bytes()
    else:
        for name,digest in json.loads((HERE/"MANIFEST.json").read_bytes()).items():
            path=(HERE/name).resolve()
            need(path.is_relative_to(HERE),"Escaping package")
            raw=path.read_bytes()
            need(hashlib.sha256(raw).hexdigest()==digest,"Package binding: "+name)
            checked[name]=raw
    engine=module("bound_new_k_engine",checked["engine.py"],HERE/"engine.py")
    audit=module("bound_new_k_audit",checked["audit.py"],HERE/"audit.py")
    root=(args.repository or HERE.parents[2]).resolve()
    spec,data=engine.snapshot(root,checked["INPUT_BINDINGS.json"])
    weights=engine.weights(data)
    audit.check_weights(weights,json.loads(data["pilot_result"]),json.loads(data["dual_result"]))
    weights_raw=serialize(weights)
    env=engine.load(root,spec,data)
    if args.freeze:
        out={"WEIGHTS.json":weights_raw,"CANDIDATE.json":serialize(engine.freeze(env))}
    else:
        need(weights_raw==checked["WEIGHTS.json"],"Weight lemma replay differs")
        frozen=checked["CANDIDATE.json"]
        if args.check:
            need(serialize(engine.freeze(env))==frozen,"Selection replay differs")
            print("PASS: single frozen K_new test vector byte-equal",flush=True)
        result=engine.certify(env,frozen)
        audit.check_result(result,weights,json.loads(frozen))
        result_raw=serialize(result)
        out={"WEIGHTS.json":weights_raw,"CANDIDATE.json":frozen,"RESULT.json":result_raw}
        if args.check:
            need(result_raw==checked["RESULT.json"],"Certificate replay differs")
            print("PASS: weight lemma and directed Schur certificate byte-equal",flush=True)
        print(result["outcome"],flush=True)
    if args.output_dir:
        args.output_dir.mkdir(parents=True,exist_ok=True)
        for name,raw in out.items():
            path=args.output_dir/name
            need(not path.exists(),"Refuse to overwrite: "+name)
            path.write_bytes(raw)
    print(weights["outcome"],flush=True)

def main():
    p=argparse.ArgumentParser()
    mode=p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--freeze",action="store_true")
    mode.add_argument("--certify",action="store_true")
    mode.add_argument("--check",action="store_true")
    p.add_argument("--output-dir",type=Path)
    p.add_argument("--repository",type=Path)
    p.add_argument("--worker",action="store_true",help=argparse.SUPPRESS)
    args=p.parse_args()
    need(__debug__,"Do not use python -O")
    need(args.check or args.output_dir,"Output directory required")
    if args.worker:
        worker(args);return
    start=time.monotonic()
    try:
        done=subprocess.run([sys.executable,"-u","-B",str(HERE/"verify.py"),*sys.argv[1:],"--worker"],timeout=600)
    except subprocess.TimeoutExpired:
        print("TECHNICAL_TIMEOUT: no mathematical conclusion",flush=True)
        raise SystemExit(124)
    print("Complete elapsed seconds:",round(time.monotonic()-start,3),flush=True)
    raise SystemExit(done.returncode)

if __name__=="__main__":
    main()
