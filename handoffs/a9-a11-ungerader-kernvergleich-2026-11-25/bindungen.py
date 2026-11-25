"""Check the upstream executable sources and physical input identifiers."""
from hashlib import sha1
from pathlib import Path

PACKAGE=Path("research/x-c1/w9-partial-energy-2026-10-18")
PAIRS="85a6e0309caa2272ea2f763653d4382b21d9041f754158401563e5c5a41c9bd4"
VARIATION="d2ff0793c1253fe7555c4fb682ae822307b2e52e"
PINS={
    "INPUT_BINDINGS.json":"a57030f51a827598cc41b923b8cfd23410cfd0b2",
    "common.py":"1a88b1d72daa3fe6aeccee0449ecc6998c466a6f",
    "assemble.py":"aeadc048c4928bf739c70a1cbf49b8651cf73544",
    "certify_k.py":"460b011613c683c43b3625c71dbf0fa116cf81b5",
    "weights.py":"adc250e1a3cf0d842fea94806fdb6bfa5e3a6f95",
    "expected/CANDIDATE_odd.json":"4e21fad9f0569fe1738e328e620f4da4075b7e76",
}
def git_blob(path):
    data=path.read_bytes()
    return sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def checked_pkg(root):
    pkg=root.resolve()/PACKAGE
    for filename,digest in PINS.items():
        if git_blob(pkg/filename)!=digest:
            raise ValueError(f"Input differs from the pinned Git blob: {filename}")
    return pkg
