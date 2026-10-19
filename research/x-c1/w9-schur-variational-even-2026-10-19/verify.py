"""Separate one-time freezing, fixed-vector certification and byte-equal replay."""
import argparse
import hashlib
import json
import signal
import time
from pathlib import Path
from types import ModuleType

HERE=Path(__file__).resolve().parent

def need(ok,msg):
    if not ok:raise RuntimeError(msg)

def timeout(signum,frame):raise TimeoutError('TECHNICAL_TIMEOUT; no mathematical conclusion')

def main():
    ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--freeze',action='store_true');g.add_argument('--certify',action='store_true');g.add_argument('--check',action='store_true')
    ap.add_argument('--repository',type=Path);args=ap.parse_args()
    need(__debug__,'Do not run with -O');t=time.monotonic()
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,1800)
    checked={}
    if args.freeze:
        for name in ('engine.py','INPUT_BINDINGS.json'):checked[name]=(HERE/name).read_bytes()
    else:
        for name,digest in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
            path=(HERE/name).resolve();need(path.is_relative_to(HERE),'Escaping package path')
            raw=path.read_bytes();need(hashlib.sha256(raw).hexdigest()==digest,'Package binding '+name);checked[name]=raw
    engine=ModuleType('bound_variational_engine');engine.__file__=str(HERE/'engine.py')
    exec(compile(checked['engine.py'],engine.__file__,'exec'),engine.__dict__)
    root=(args.repository or HERE.parents[2]).resolve();env=engine.load(root,checked['INPUT_BINDINGS.json'])
    def serialize(x):return (json.dumps(x,indent=2)+'\n').encode()
    if args.freeze:
        path=HERE/'CANDIDATE.json';need(not path.exists(),'Refuse to change a frozen candidate')
        raw=serialize(engine.freeze(env));path.write_bytes(raw)
        print('FROZEN: one rational 84-vector; no directed decision run',flush=True)
    else:
        frozen=checked['CANDIDATE.json']
        if args.check:
            need(serialize(engine.freeze(env))==frozen,'Frozen selection replay differs')
            print('PASS: frozen selection byte-equal; fixed input remains unchanged',flush=True)
        result=serialize(engine.certify(env,frozen))
        if args.check:
            need(result==checked['RESULT.json'],'Directed certificate replay differs')
            print('PASS: directed lower certificate byte-equal',flush=True)
        else:
            path=HERE/'RESULT.json';need(not path.exists(),'Refuse to overwrite a result');path.write_bytes(result)
        print(json.loads(result)['outcome'],flush=True)
    signal.setitimer(signal.ITIMER_REAL,0)
    print('Elapsed seconds:',round(time.monotonic()-t,3),flush=True)

if __name__=='__main__':main()
