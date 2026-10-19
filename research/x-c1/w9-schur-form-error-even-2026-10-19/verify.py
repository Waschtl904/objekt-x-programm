"""Hash-bound fixed-vector refinement; no selection or historical replay."""
import argparse
import hashlib
import json
import signal
import time
from pathlib import Path
from types import ModuleType

HERE = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def snapshot(root, entries):
    result = {}
    for name, entry in entries.items():
        path = (root / entry['path']).resolve()
        need(path.is_relative_to(root), 'Escaping bound path')
        raw = path.read_bytes()
        need(hashlib.sha256(raw).hexdigest() == entry['sha256'], 'Hash mismatch: ' + name)
        result[name] = raw
    return result


def module(name, raw, path):
    result = ModuleType(name)
    result.__file__ = str(path)
    exec(compile(raw, str(path), 'exec'), result.__dict__)
    return result


def timeout(signum, frame):
    raise TimeoutError('TECHNICAL_TIMEOUT; no mathematical conclusion')


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write', action='store_true')
    g.add_argument('--check', action='store_true')
    args = ap.parse_args()
    need(__debug__, 'Do not run with -O')
    start = time.monotonic()
    signal.signal(signal.SIGALRM, timeout)
    signal.setitimer(signal.ITIMER_REAL, 1800)
    manifest = json.loads((HERE/'MANIFEST.json').read_bytes())
    checked = snapshot(HERE, {k:{'path':k,'sha256':v} for k,v in manifest.items()})
    spec = json.loads(checked['INPUT_BINDINGS.json'])
    root = HERE.parents[2].resolve()
    old = snapshot(root, spec['files'])
    previous = module('bound_previous_schur', old['engine'], root/spec['files']['engine']['path'])
    env = previous.load(root, old['bindings'])
    engine = module('bound_refinement', checked['engine.py'], HERE/'engine.py')
    result = engine.certify(previous, env, old['candidate'], old['result'])
    auditor = module('bound_endpoint_audit', checked['audit.py'], HERE/'audit.py')
    print(auditor.check(result, json.loads(old['result'])))
    serialized = (json.dumps(result, indent=2)+'\n').encode()
    if args.check:
        need(serialized == checked['RESULT.json'], 'Directed refinement replay differs')
        print('PASS: fixed-vector directed refinement byte-equal')
    else:
        need(not (HERE/'RESULT.json').exists(), 'Refuse to overwrite a result')
        (HERE/'RESULT.json').write_bytes(serialized)
    print(result['outcome'])
    print('Elapsed seconds:', round(time.monotonic()-start,3))
    signal.setitimer(signal.ITIMER_REAL, 0)


if __name__ == '__main__':
    main()
