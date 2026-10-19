"""Hash-check and replay the one frozen-even certificate without subprocesses."""
import hashlib
import importlib.util
import json
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    if not __debug__:
        raise RuntimeError('Run verification without python -O')
    for name, digest in json.loads((HERE / 'MANIFEST.json').read_text()).items():
        path = (HERE / name).resolve()
        if not path.is_relative_to(HERE) or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise RuntimeError(f'Hash binding failed: {name}')
    spec = importlib.util.spec_from_file_location('coherent_even_certifier', HERE / 'certify.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory(prefix='objekt-x-coherent-even-') as td:
        module.main(td)
        name = 'COHERENT_K_EVEN.json'
        if (Path(td) / name).read_bytes() != (HERE / 'expected' / name).read_bytes():
            raise RuntimeError('Frozen even certificate differs')
    print('PASS: one common-k certificate byte-identical; external mathematical review open')


if __name__ == '__main__':
    main()
