"""Replay actual K_P enclosures for the two already frozen candidates."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent

def main():
    for name, digest in json.loads((HERE / "MANIFEST.json").read_text()).items():
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == digest, name
    with tempfile.TemporaryDirectory(prefix="objekt-x-sharp-k-") as td:
        env = dict(os.environ, OBJEKT_X_SHARP_K_OUTPUT=td)
        env.pop("OBJEKT_X_CORRELATION_PROBE", None)
        for parity in ("even", "odd"):
            subprocess.run([sys.executable, "-B", str(HERE / "certify.py"), parity],
                           env=env, check=True)
            name = f"SHARP_K_{parity}.json"
            assert (Path(td) / name).read_bytes() == (HERE / "expected" / name).read_bytes(), name
    subprocess.run([sys.executable, "-B", str(HERE / "audit_correlation.py")], check=True)
    print("PASS: both actual K_P certificates reproduced byte-for-byte; 24 numerical controls; external review open")

if __name__ == "__main__":
    main()
