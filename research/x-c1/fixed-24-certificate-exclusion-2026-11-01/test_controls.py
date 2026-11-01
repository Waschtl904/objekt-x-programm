"""Negative controls for byte bindings and the inherited rational decision."""
from pathlib import Path
import contextlib
import hashlib
import io
import json
import runpy
import shutil
import sys
import tempfile
import zipfile
from verify_publication import HERE, verify

sys.dont_write_bytecode = True


def identity(raw):
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def refresh_manifest(root):
    files = {p.relative_to(root).as_posix(): identity(p.read_bytes())
             for p in sorted(root.rglob("*"))
             if p.is_file() and p.name != "PUBLICATION_MANIFEST.json"}
    (root/"PUBLICATION_MANIFEST.json").write_text(json.dumps({"files": files}), encoding="utf-8")


def rejected(action, expected):
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            action()
    except (ValueError, RuntimeError) as error:
        if expected not in str(error):
            raise AssertionError("unexpected rejection: " + str(error)) from error
    else:
        raise AssertionError("invalid case accepted: " + expected)


def publication_case(mutate, expected):
    with tempfile.TemporaryDirectory(prefix="objx-24-control-") as temporary:
        root = Path(temporary)/"package"
        shutil.copytree(HERE, root)
        descriptor = json.loads((root/"ARCHIVE.json").read_bytes())
        mutate(root, descriptor)
        refresh_manifest(root)
        rejected(lambda: verify(root), expected)


def damaged_transport(root, descriptor):
    path = root/"archives"/descriptor["GPT1_verified_transport"]["filename"]
    raw = bytearray(path.read_bytes())
    raw[len(raw)//2] ^= 1
    path.write_bytes(raw)


def wrong_copy(root, descriptor):
    path = root/"review/BERICHT.txt"
    path.write_bytes(path.read_bytes()+b"\nchanged\n")


def missing_input(root, descriptor):
    transport = descriptor["GPT1_verified_transport"]
    path = root/"archives"/transport["filename"]
    with zipfile.ZipFile(path) as old:
        members = [(i, old.read(i.filename)) for i in old.infolist()
                   if not i.filename.endswith("inputs/norm-panels/001.json")]
    with zipfile.ZipFile(path, "w") as new:
        for info, content in members:
            new.writestr(info, content)
    transport.update(identity(path.read_bytes()))
    (root/"ARCHIVE.json").write_text(json.dumps(descriptor), encoding="utf-8")


def false_threshold():
    descriptor = json.loads((HERE/"ARCHIVE.json").read_bytes())
    transport = descriptor["GPT1_verified_transport"]
    with tempfile.TemporaryDirectory(prefix="objx-24-threshold-") as temporary:
        with zipfile.ZipFile(HERE/"archives"/transport["filename"]) as z:
            z.extractall(temporary)
        module = runpy.run_path(str(Path(temporary)/transport["root"]/"check_final_review.py"))
        calculate = module["calculate"]
        scope = calculate.__globals__
        original_read = scope["read"]
        def changed_read(name):
            value = original_read(name)
            if name == "gpt1-review/GPT1_BUDGET.json":
                value["E_star"] = "1/2000"
            return value
        scope["read"] = changed_read
        rejected(calculate, "original strict gradient threshold")


if __name__ == "__main__":
    publication_case(damaged_transport, "SHA-256: reconstructed transport")
    publication_case(missing_input, "all correction members")
    publication_case(wrong_copy, "byte-exact reading copy")
    false_threshold()
    print("CONTROLS_PASS: damaged transport, missing input, false reading copy and false threshold rejected")
