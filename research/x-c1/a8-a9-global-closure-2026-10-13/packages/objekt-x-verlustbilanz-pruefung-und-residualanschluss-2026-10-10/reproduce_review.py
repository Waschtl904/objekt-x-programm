"""Reproduce this bounded review from the separately supplied original ZIP."""
from pathlib import Path
from zipfile import ZipFile
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("original_zip", type=Path)
    ap.add_argument("--work", type=Path, required=True, help="New extraction directory")
    ap.add_argument("--deps", type=Path)
    ap.add_argument("--direct-integrations", action="store_true")
    args = ap.parse_args()
    bindings = json.loads((ROOT/"SOURCE_BINDINGS.json").read_text())
    assert digest(args.original_zip) == bindings["original_zip"]["sha256"]
    manifest = json.loads((ROOT/"MANIFEST.json").read_text())["files"]
    for name, sha in manifest.items():
        file = (ROOT/name).resolve()
        assert file.is_relative_to(ROOT) and digest(file) == sha, name
    work = args.work.resolve()
    assert not work.exists(), "Choose a fresh work directory"
    work.mkdir(parents=True)
    with ZipFile(args.original_zip) as z:
        for name in z.namelist():
            assert (work/name).resolve().is_relative_to(work)
        z.extractall(work)
    package = work/bindings["original_zip"]["root_directory"]
    env = os.environ.copy()
    if args.deps:
        env["PYTHONPATH"] = str(args.deps.resolve())+os.pathsep+env.get("PYTHONPATH", "")
    def run(script, *opts):
        subprocess.run([sys.executable,str(script),*map(str,opts)],check=True,env=env)
    run(package/"reproduce.py")
    run(ROOT/"independent_checks.py",package,"--out",work/"INDEPENDENT_CHECKS.json")
    assert json.loads((work/"INDEPENDENT_CHECKS.json").read_text()) == json.loads((ROOT/"expected/INDEPENDENT_CHECKS.json").read_text())
    direct_status=[]
    if args.direct_integrations:
        source=package/"work/tail-probe-2026-10-10"
        target=package/"work/review-directcheck"
        target.mkdir()
        for file in source.glob("*.py"):
            shutil.copy2(file,target/file.name)
        shutil.copytree(source/"vendor",target/"vendor")
        for par in ["EVEN","ODD"]:
            shutil.copy2(source/f"PROBE_{par}_12_3072.json",target/f"PROBE_{par}_12_3072.json")
            out=target/f"DIRECT_CALIBRATION_{par}_3072.json"
            run(target/"compute_direct_calibration.py","--parity",par.lower(),"--bits",3072,"--calibration","--out",out)
            data=json.loads(out.read_text())
            assert data["status"] == "DIRECT_FORM_CALIBRATION_PASS"
            direct_status.append(par.lower())
    result={"status":"PASS_BOUNDED_REVIEW_REPLAY",
            "review_manifest_files":len(manifest),
            "original_package_replay_passed":True,
            "separate_rational_output_reproduced":True,
            "direct_calibration_integrations_repeated":direct_status,
            "all_original_source_integrations_repeated":False,
            "full_remainder_certified":False}
    (work/"REVIEW_REPLAY.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
