"""Verify the separately bound GPT1 correction; no numerical integration."""
from pathlib import Path, PurePosixPath
from fractions import Fraction as F
import argparse
import binascii
import hashlib
import io
import json
import struct
import runpy
import sys
import tempfile
import zipfile
import zlib

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ORIGINAL_SHA = "0ae5879e0783a88d102def93c5cce3a768e42dbc3c09209bac703822a154515e"
GPT1_MANIFEST_SHA = "22ffd6c5f23e11963b7e40271d6ca5d14027714613f2c4815d925e560ae86fd6"
DOWNLOAD_SHA = "904187291a9e55456468414172077c7a28eafcdd8e508371129270e79204b90c"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def identity(raw, record, name):
    need(len(raw) == record["bytes"], "byte count: " + name)
    need(hashlib.sha256(raw).hexdigest() == record["sha256"], "SHA-256: " + name)


def safe(name):
    p = PurePosixPath(name)
    need(not p.is_absolute() and ".." not in p.parts and "\\" not in name
         and ":" not in name, "unsafe path: " + name)


def complete_prefix_members(raw):
    """Read only complete local members; never repair or accept a truncated ZIP."""
    offset, members = 0, {}
    while raw[offset:offset+4] == b"PK\x03\x04":
        need(offset+30 <= len(raw), "complete local header")
        h = struct.unpack_from("<IHHHHHIIIHH", raw, offset)
        flags, method, crc, compressed, size, namesize, extrasize = h[2], h[3], h[6], h[7], h[8], h[9], h[10]
        need(flags == 0 and method in (0, 8), "supported original local ZIP member")
        name = raw[offset+30:offset+30+namesize].decode("utf-8")
        safe(name)
        start = offset+30+namesize+extrasize
        if start+compressed > len(raw):
            break
        content = raw[start:start+compressed]
        if method == 8:
            content = zlib.decompress(content, -15)
        need(len(content) == size and binascii.crc32(content) & 0xffffffff == crc, "local member CRC")
        need(name not in members, "duplicate local member")
        members[name] = content
        offset = start+compressed
    return members


def verify(root=HERE, original_archive=None):
    publication = json.loads((root/"PUBLICATION_MANIFEST.json").read_bytes())
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    need(actual == set(publication["files"]) | {"PUBLICATION_MANIFEST.json"}, "publication coverage")
    for name, record in publication["files"].items():
        safe(name)
        identity((root/name).read_bytes(), record, name)
    descriptor = json.loads((root/"ARCHIVE.json").read_bytes())
    original = descriptor["GPT2_original"]
    need(original["sha256"] == ORIGINAL_SHA and original["bytes"] == 267597341, "frozen GPT2 identity")
    incomplete = descriptor["GPT1_incomplete_download"]
    need(incomplete["sha256"] == DOWNLOAD_SHA and incomplete["valid_complete_zip"] is False, "truncated transfer is explicit")
    raw_download = (root/"archives"/incomplete["filename"]).read_bytes()
    identity(raw_download, incomplete, "unchanged incomplete download")
    need(not zipfile.is_zipfile(io.BytesIO(raw_download)), "do not call the truncated download a full archive")
    received = complete_prefix_members(raw_download)
    transport = descriptor["GPT1_verified_transport"]
    need(transport["role"] == "TRANSPORT_RECONSTRUCTION_ALL_MEMBER_BYTES_MATCH_GPT1_MANIFEST", "transport role")
    transport_raw = (root/"archives"/transport["filename"]).read_bytes()
    identity(transport_raw, transport, "reconstructed transport")
    prefix = transport["root"] + "/"
    with zipfile.ZipFile(io.BytesIO(transport_raw)) as z:
        names = z.namelist()
        need(len(names) == len(set(names)) == 152, "all correction members")
        for name in names:
            safe(name)
        need(z.testzip() is None, "transport CRC")
        manifest_raw = z.read(prefix+"MANIFEST.json")
        need(hashlib.sha256(manifest_raw).hexdigest() == GPT1_MANIFEST_SHA, "unchanged GPT1 manifest")
        manifest = json.loads(manifest_raw)
        need(len(manifest) == 151, "151 correction bindings")
        need(set(names) == {prefix+n for n in manifest} | {prefix+"MANIFEST.json"}, "complete correction coverage")
        for name, record in manifest.items():
            identity(z.read(prefix+name), record, "GPT1 original member " + name)
        for name, content in received.items():
            need(z.read(name) == content, "retained downloaded member: " + name)
        for name in descriptor["readable_originals"]:
            need((root/"review"/name).read_bytes() == z.read(prefix+name), "byte-exact reading copy " + name)
        original_manifest_raw = z.read(prefix+"inputs/ORIGINAL_MANIFEST.json")
        need(hashlib.sha256(original_manifest_raw).hexdigest() == original["manifest_sha256"], "bound GPT2 manifest")
        original_manifest = json.loads(original_manifest_raw)
        need(len(original_manifest) == 226, "full original manifest retained")
        sources = json.loads(z.read(prefix+"SOURCES.json"))
        need(sources["GPT2_original_archive"]["sha256"] == ORIGINAL_SHA, "GPT1 names same GPT2 original")
        need(sources["original_manifest_sha256"] == original["manifest_sha256"], "same input manifest")
        result = json.loads(z.read(prefix+"GPT1_FINAL_REVIEW.json"))
        need(F(result["r_upper"]) == F("0.058383477345103"), "corrected rest endpoint")
        need(F(result["complete_data_price_once"]) == F("0.004356223514"), "data price exactly once")
        need(result["old_partial_price_added_again"] is False, "no data double counting")
        need(F(result["display_E_upper"]) == F("0.000949781310484370"), "corrected energy endpoint")
        need(F(result["display_E_star_lower"]) == F("0.000972717481018334"), "unchanged threshold endpoint")
        need(F(result["display_strict_slack_lower"]) == F("0.000022936170533964"), "corrected positive margin")
        need(F(result["original_rational_energy_upper"]) < F(result["E_star"]), "strict original rational inequality")
        need(result["new_quadrature_evaluations"] == 0 and result["originals_changed"] is False, "saved recombination only")
        if original_archive is not None:
            raw = Path(original_archive).read_bytes()
            identity(raw, original, "complete GPT2 original")
            oprefix = original["filename"].removesuffix(".zip") + "/"
            with zipfile.ZipFile(io.BytesIO(raw)) as oz:
                need(oz.testzip() is None, "full GPT2 CRC")
                need(set(oz.namelist()) == {oprefix+n for n in original_manifest} | {oprefix+"MANIFEST.json"}, "GPT2 full coverage")
                need(oz.read(oprefix+"MANIFEST.json") == original_manifest_raw, "same original manifest bytes")
                for name, record in original_manifest.items():
                    identity(oz.read(oprefix+name), record, "GPT2 original " + name)
        with tempfile.TemporaryDirectory(prefix="objx-fixed24-") as temporary:
            z.extractall(temporary)
            checker = Path(temporary)/transport["root"]/"check_final_review.py"
            # Execute only the unchanged checker bound by GPT1_MANIFEST_SHA.
            # No shell, command construction, or external process is involved.
            runpy.run_path(str(checker), run_name="__main__")
    print("PUBLICATION_PASS: all 151 GPT1 bindings, unchanged incomplete source transfer, complete reconstructed transport, corrected rational close; zero new integrals")
    if original_archive:
        print("FULL_ORIGINAL_PASS: 267597341 bytes, CRC and 226 GPT2 manifest bindings")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--original-archive", type=Path)
    args = parser.parse_args()
    verify(original_archive=args.original_archive)
