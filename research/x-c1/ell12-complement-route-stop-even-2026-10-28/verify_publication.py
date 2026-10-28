"""Check original bytes and the bounded rational decision; never integrate."""
from pathlib import Path, PurePosixPath
import hashlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile

if sys.flags.optimize:
    raise SystemExit("OPTIMIZED_PYTHON_REJECTED")
HERE = Path(__file__).resolve().parent
ARCHIVE_HASH = "cdde0859a0869feaea3e38ecb579d7e94d28e00339f665d876470ea0712266ce"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def identity(raw, record, label):
    need(len(raw) == record["bytes"], "byte count: " + label)
    need(hashlib.sha256(raw).hexdigest() == record["sha256"], "SHA-256: " + label)


def main():
    manifest = json.loads((HERE / "PUBLICATION_MANIFEST.json").read_bytes())
    actual = {p.relative_to(HERE).as_posix() for p in HERE.rglob("*") if p.is_file()}
    need(actual == set(manifest["files"]) | {"PUBLICATION_MANIFEST.json"}, "publication coverage")
    for name, record in manifest["files"].items():
        need(not PurePosixPath(name).is_absolute() and ".." not in PurePosixPath(name).parts, "unsafe publication path")
        identity((HERE / name).read_bytes(), record, name)
    descriptor = json.loads((HERE / "ARCHIVE.json").read_bytes())
    need(descriptor["sha256"] == ARCHIVE_HASH and descriptor["bytes"] == 19944025, "frozen original identity")
    pieces = []
    for part in descriptor["transport_parts"]:
        need(PurePosixPath(part["name"]).name == part["name"], "unsafe part path")
        raw = (HERE / "archives" / part["name"]).read_bytes()
        identity(raw, part, part["name"])
        pieces.append(raw)
    archive_bytes = b"".join(pieces)
    identity(archive_bytes, descriptor, "reassembled original archive")
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as z:
        names = z.namelist()
        need(len(names) == len(set(names)) == 584, "original members")
        need(z.testzip() is None, "CRC")
        internal = json.loads(z.read("ARCHIVE_MANIFEST.json"))
        need(set(names) == set(internal["files"]) | {"ARCHIVE_MANIFEST.json"}, "original manifest coverage")
        for name, record in internal["files"].items():
            need(not PurePosixPath(name).is_absolute() and ".." not in PurePosixPath(name).parts, "unsafe archive path")
            identity(z.read(name), record, name)
        for local, member in descriptor["readable_originals"].items():
            need((HERE / local).read_bytes() == z.read(member), "original reading copy: " + local)
        with tempfile.TemporaryDirectory(prefix="objx-ell12-publication-") as tmp:
            z.extractall(tmp)
            base = Path(tmp) / "joint-energy-2026-10-28/gpt1-metric"
            output = Path(tmp) / "fresh-decision.json"
            subprocess.run([sys.executable, "-B", str(base / "check_coupling_only_decision.py"), "--output", str(output)], check=True, cwd=tmp)
            expected = json.loads((HERE / "review/COUPLING_ONLY_DECISION_RATIONAL.json").read_bytes())
            need(json.loads(output.read_bytes()) == expected, "fresh rational result")
            subprocess.run([sys.executable, "-B", str(base / "check_coupling_decision_controls.py")], check=True, cwd=tmp)
            # A later, separate bounded investigation. Its original scripts
            # receive their unchanged historical relative paths in a temp copy.
            shutil.copytree(HERE / "source-specific", Path(tmp), dirs_exist_ok=True)
            targets = [
                ("gpt1", "check_source_specific.py", "SOURCE_SPECIFIC_RATIONAL.json"),
                ("gpt1", "check_source_specific_controls.py", "SOURCE_SPECIFIC_CONTROLS.json"),
                ("gpt2", "check_selected_source_price.py", "SELECTED_SOURCE_PRICE_RECHECK.json"),
            ]
            for agent, script, result in targets:
                relative = Path("source-specific-2026-10-28") / agent
                work = Path(tmp) / relative
                subprocess.run([sys.executable, "-B", str(work / script)], check=True, cwd=tmp)
                expected = json.loads((HERE / "source-specific" / relative / result).read_bytes())
                need(json.loads((work / result).read_bytes()) == expected, "source-price rational recombination: " + result)
    print("PUBLICATION_PASS: 584 original members, reading copies, route decision, controls and separate source-price checks; no integration")


if __name__ == "__main__":
    main()
