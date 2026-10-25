#!/usr/bin/env python3
"""Byte-/Bindungsprüfung der Draft-Veröffentlichung; keine Forschungsrechnung."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import zipfile

PACKAGE = "research/x-c1/w9-grad11-route-stop-even-2026-10-25"
MANIFEST = "PUBLICATION_MANIFEST.json"
REVIEW = "Objekt-X-Grad11-Gegenpruefung-GPT1-2026-10-25.zip"
AUTHOR = "Objekt-X-Grad11-Machbarkeitsanalyse-GPT2-2026-10-25.zip"
CHAIN = "Objekt-X-Grad11-Belegkette-GPT1-2026-10-25.txt"
REVIEW_HASH = "9fa36e19fcacc2f0392149d9b8c0f29b9b47a0987ce77be6631a4fcc437c0ca7"
AUTHOR_HASH = "be2b1ab43514454cfec95dd1283d81e8d2f34745f4cf1554ecfd2d6811888e93"
CHAIN_HASH = "7e4e67c889a211c84aa79ef5ec40b660d310ac5e8dc23d22d43401b75d75882c"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def identity(data, size, expected, label):
    require(len(data) == size, f"Bytegröße abweichend: {label}")
    require(digest(data) == expected, f"SHA-256 abweichend: {label}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--git-ref", help="Git-Blobs dieses Commits statt Arbeitsdateien")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    repo = root.parents[2]

    def git(*parts):
        return subprocess.check_output(["git", "-C", str(repo), *parts])

    def read(name):
        require(not name.startswith("/") and ".." not in Path(name).parts,
                "Unzulässiger relativer Paketpfad")
        if args.git_ref:
            return git("cat-file", "blob", f"{args.git_ref}:{PACKAGE}/{name}")
        return (root / name).read_bytes()

    manifest = json.loads(read(MANIFEST))
    entries = manifest["files"]
    if args.git_ref:
        names = git("ls-tree", "-r", "--name-only", args.git_ref, "--", PACKAGE)
        actual = {n[len(PACKAGE) + 1:] for n in names.decode().splitlines()}
    else:
        actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    require(actual == set(entries) | {MANIFEST}, "Manifestabdeckung abweichend")
    data = {}
    for name, item in entries.items():
        data[name] = read(name)
        identity(data[name], item["bytes"], item["sha256"], name)

    descriptor = json.loads(data["archives/ARCHIVE.json"])
    require(descriptor["original_filename"] == REVIEW, "Archivname abweichend")
    parts = descriptor["parts"]
    require(len(parts) == 2, "Archivteilezahl abweichend")
    offset = 0
    buffers = []
    for item in parts:
        require(item["offset"] == offset, "Archivteilreihenfolge abweichend")
        chunk = data[item["path"]]
        identity(chunk, item["bytes"], item["sha256"], item["path"])
        buffers.append(chunk)
        offset += len(chunk)
    review_data = b"".join(buffers)
    identity(review_data, descriptor["original_bytes"], descriptor["original_sha256"], REVIEW)
    identity(review_data, 12838318, REVIEW_HASH, REVIEW)
    identity(data["originals/" + CHAIN], 8880, CHAIN_HASH, CHAIN)
    with zipfile.ZipFile(io.BytesIO(review_data)) as review:
        old_manifest = json.loads(review.read("PACKAGE-MANIFEST.json"))
        require(len(old_manifest) == 54, "GPT1-Originalmanifest unerwartet")
        for member, expected in old_manifest.items():
            require(digest(review.read(member)) == expected, f"GPT1-Mitglied abweichend: {member}")
        require(set(review.namelist()) == set(old_manifest) | {"PACKAGE-MANIFEST.json"},
                "GPT1-Originalmanifestabdeckung abweichend")
        text_members = {n for n in review.namelist() if not n.endswith(".zip")}
        require(len(text_members) == 53, "Textmitgliederzahl abweichend")
        mapped = {v["archive_member"] for v in entries.values()
                  if v["kind"] == "archive_member_original"}
        require(mapped == text_members, "Lesekopien unvollständig")
        for name, item in entries.items():
            if item["kind"] == "archive_member_original":
                require(data[name] == review.read(item["archive_member"]),
                        f"Lesekopie abweichend: {name}")
        author_data = review.read("upload/" + AUTHOR)
        identity(author_data, 875069, AUTHOR_HASH, AUTHOR)
        with zipfile.ZipFile(io.BytesIO(author_data)) as author:
            author_manifest = json.loads(author.read("MANIFEST.json"))
            require(len(author_manifest) == 33, "GPT2-Originalmanifest unerwartet")
            for member, expected in author_manifest.items():
                require(digest(author.read(member)) == expected,
                        f"GPT2-Mitglied abweichend: {member}")
            require(len(author.namelist()) == 35, "GPT2-Dateizahl abweichend")
            for member in author.namelist():
                require(author.read(member) == review.read("grad11-review/input/" + member),
                        f"Eingebettete GPT2-Kopie abweichend: {member}")
    print(json.dumps({"status": "PASS", "mode": "git-blobs" if args.git_ref else "working-files",
                      "git_ref": args.git_ref, "bound_publication_files": len(entries),
                      "original_text_copies": 53, "separate_chain_copies": 1,
                      "gpt1_manifest_entries": 54, "gpt2_manifest_entries": 33,
                      "gpt2_members_compared": 35, "research_calculations": 0}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, zipfile.BadZipFile, subprocess.CalledProcessError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
