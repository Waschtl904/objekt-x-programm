"""Replay both directed scalar enclosures without starting child processes."""
import hashlib
import importlib.util
import json
import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PACKAGE = HERE.parent / 'nstar-jp-spike-orthogonality-2026-10-16'


def check_hashes(base, bindings):
    for rel, digest in bindings.items():
        path = (base / rel).resolve()
        if not path.is_relative_to(base) or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise RuntimeError(f'Hash binding failed: {rel}')


def load_module(name, path):
    # Both callers below use fixed repository paths checked before import.
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    if not __debug__:
        raise RuntimeError('Run certificate verification without python -O')
    check_hashes(HERE, json.loads((HERE / 'MANIFEST.json').read_text()))
    bindings = json.loads((HERE / 'INPUT_BINDINGS.json').read_text())
    check_hashes(ROOT, bindings['repository_files'])
    check_hashes(ROOT, bindings['archive_sha256'])
    with tempfile.TemporaryDirectory(prefix='objekt-x-l00-') as td, patch.object(sys, 'dont_write_bytecode', True):
        td = Path(td)
        inputs, out = td / 'inputs', td / 'out'
        prepare_path = PACKAGE / 'stufe5/prepare_inputs.py'
        prepare = load_module('l00_prepare_inputs', prepare_path)
        with patch.object(sys, 'argv', [str(prepare_path), str(inputs)]):
            prepare.main()
        check_hashes(inputs, bindings['prepared_inputs'])
        with patch.dict(os.environ, OBJEKT_X_STAGE5_INPUTS=str(inputs), OBJEKT_X_L00_OUTPUT=str(out)):
            certify = load_module('l00_certify', HERE / 'certify.py')
            for par in ('even', 'odd'):
                certify.main(par)
                name = f'L00_CERTIFICATE_{par}.json'
                if (out / name).read_bytes() != (HERE / 'expected' / name).read_bytes():
                    raise RuntimeError(f'Certificate replay differs: {name}')
    print('PASS: both directed scalar certificates replayed byte-for-byte; external mathematical review open')


if __name__ == '__main__':
    main()
