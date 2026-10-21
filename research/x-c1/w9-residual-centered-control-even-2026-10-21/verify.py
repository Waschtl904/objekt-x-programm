"""Hash-bound finite control and byte replay; the full residual remains open."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from types import ModuleType

HERE=Path(__file__).resolve().parent


def need(ok,message):
    if not ok:
        raise RuntimeError(message)


def module(name,raw,path):
    m=ModuleType(name)
    m.__file__=str(path)
    sys.modules[name]=m
    exec(compile(raw,str(path),'exec'),m.__dict__)
    return m


def dump(v):
    return (json.dumps(v,indent=2)+'\n').encode()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repository',type=Path,default=HERE.parents[2])
    ap.add_argument('--output-dir',type=Path)
    ap.add_argument('--check',action='store_true')
    ap.add_argument('--worker',action='store_true',help=argparse.SUPPRESS)
    a=ap.parse_args()
    need(__debug__,'Do not use python -O')
    if not a.worker:
        subprocess.run([sys.executable,'-u','-B',str(HERE/'verify.py'),*sys.argv[1:],'--worker'],check=True,timeout=300)
        return
    checked={}
    if a.check:
        for name,want in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            path=(HERE/name).resolve()
            need(path.is_relative_to(HERE),'Escaping package')
            raw=path.read_bytes()
            need(hashlib.sha256(raw).hexdigest()==want,'Package hash: '+name)
            checked[name]=raw
    else:
        checked={name:(HERE/name).read_bytes() for name in ('engine.py','audit.py','INPUT_BINDINGS.json')}
    engine=module('bound_residual_center_engine',checked['engine.py'],HERE/'engine.py')
    audit=module('bound_residual_center_audit',checked['audit.py'],HERE/'audit.py')
    spec,data=engine.snapshot(a.repository.resolve(),checked['INPUT_BINDINGS.json'])
    result=engine.run(a.repository.resolve(),spec,data)
    audit_result=audit.check(result,json.loads(data['schur_result']),json.loads(data['rest_result']))
    for name,value in (('RESULT.json',result),('AUDIT.json',audit_result)):
        raw=dump(value)
        if a.check:
            need(raw==checked[name],'Byte replay: '+name)
        if a.output_dir:
            a.output_dir.mkdir(parents=True,exist_ok=True)
            target=a.output_dir/name
            need(not target.exists(),'Refuse overwrite: '+name)
            target.write_bytes(raw)
    print('PASS:',result['outcome'],flush=True)


if __name__=='__main__':
    main()
