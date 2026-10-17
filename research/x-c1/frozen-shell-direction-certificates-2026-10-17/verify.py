"""Replay both directed scalar enclosures, including own and input bindings."""
import hashlib,json,os,subprocess,sys,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PACKAGE=HERE.parent/'nstar-jp-spike-orthogonality-2026-10-16'

def main():
    for rel,digest in json.loads((HERE/'MANIFEST.json').read_text()).items():
        assert hashlib.sha256((HERE/rel).read_bytes()).hexdigest()==digest,rel
    bindings=json.loads((HERE/'INPUT_BINDINGS.json').read_text())
    for rel,digest in bindings['archive_sha256'].items():
        assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest,rel
    with tempfile.TemporaryDirectory(prefix='objekt-x-l00-') as td:
        td=Path(td);inputs=td/'inputs';out=td/'out'
        subprocess.run([sys.executable,'-B',str(PACKAGE/'stufe5/prepare_inputs.py'),str(inputs)],check=True)
        env=dict(os.environ,OBJEKT_X_STAGE5_INPUTS=str(inputs),OBJEKT_X_FROZEN_OUTPUT=str(out))
        for par in ('even','odd'):
            subprocess.run([sys.executable,'-B',str(HERE/'certify.py'),par],env=env,check=True)
            name=f'FROZEN_CERTIFICATE_{par}.json'
            assert (out/name).read_bytes()==(HERE/'expected'/name).read_bytes(),name
    print('PASS: both directed scalar certificates replayed byte-for-byte; external mathematical review open')

if __name__=='__main__':main()
