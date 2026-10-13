"""Byte bindings and stored synthetic replay only; no operator certification."""
from pathlib import Path
import hashlib
import json
from test_protocol import run

ROOT = Path(__file__).resolve().parent


def main():
    expected = json.loads((ROOT/'MANIFEST.json').read_bytes())['files']
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
              if p.is_file() and p.name != 'MANIFEST.json' and '__pycache__' not in p.parts}
    if actual != set(expected):
        raise ValueError('Manifest member coverage mismatch')
    for name, digest in expected.items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != digest:
            raise ValueError('Byte binding mismatch: '+name)
    checks, fixtures = run()
    if checks != json.loads((ROOT/'checks.json').read_bytes()):
        raise ValueError('Synthetic replay receipt mismatch')
    for name, data in fixtures.items():
        if data != json.loads((ROOT/'examples'/name).read_bytes()):
            raise ValueError('Synthetic input mismatch: '+name)
    print(json.dumps({'status': 'PASS_BINDINGS_AND_SYNTHETIC_REPLAY',
                      'files': len(expected), 'actual_operator_inputs_audited': False,
                      'full_remainder_certified': False}, indent=2))


if __name__ == '__main__':
    main()
