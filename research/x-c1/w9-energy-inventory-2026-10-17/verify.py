"""Replay bound inventory and exact interface arithmetic without child processes."""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    if not __debug__:
        raise RuntimeError('Run verification without python -O')
    own = {}
    for name, digest in json.loads((HERE/'MANIFEST.json').read_bytes()).items():
        path = (HERE/name).resolve()
        if not path.is_relative_to(HERE):
            raise RuntimeError('Escaping package path')
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != digest:
            raise RuntimeError('Own binding failed: '+name)
        own[name] = raw
    sys.path.insert(0,str(HERE))
    import audit
    import algebra_checks
    for name, value in [('INVENTORY.json',audit.build()),
                        ('ALGEBRA_CHECKS.json',algebra_checks.run())]:
        raw = (json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode()
        if raw != own[name]:
            raise RuntimeError('Replay differs: '+name)
    print('PASS: bound inventory and exact weighted-error interface replayed byte-for-byte; full W9 energy and N12 remain open')


if __name__ == '__main__':
    main()
