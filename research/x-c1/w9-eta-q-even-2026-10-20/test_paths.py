"""Portable binding regression tests; no mathematical calculation."""
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

import verify


class PortableBindings(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.outer = Path(self.tmp.name)
        self.root = self.outer / "repository"
        self.root.mkdir()
        self.common = b"bound common member"
        buf = io.BytesIO()
        with ZipFile(buf, "w") as archive:
            archive.writestr("source/common.json", self.common)
        self.archive = buf.getvalue()
        self.source = json.dumps({
            "files": {"stage3_archive": {"sha256": verify.sha(self.archive)}},
            "members": {"common": {"archive": "stage3_archive",
                                    "member": "source/common.json",
                                    "sha256": verify.sha(self.common)}}
        }).encode()
        self.files = {"source_bindings": ("inputs/nested/bindings.json", self.source),
                      "stage3_archive": ("inputs/nested/archive.zip", self.archive)}
        for name, raw in self.files.values():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)

    def spec(self, separator="/"):
        return {"source_commit": verify.BASE,
                "files": {alias: {"path": name.replace("/", separator),
                                  "sha256": verify.sha(raw)}
                          for alias, (name, raw) in self.files.items()}}

    def snapshot(self, spec):
        return verify.snapshot(self.root, json.dumps(spec).encode())

    def test_forward_backward_and_mixed_paths_read_identical_bytes(self):
        expected = self.snapshot(self.spec())
        for separator in ("\\", "/\\"):
            with self.subTest(separator=separator):
                actual = self.snapshot(self.spec(separator))
                self.assertEqual(actual, expected)
                self.assertEqual(actual["common"], self.common)

    def test_snapshot_is_immutable_and_retains_checked_bytes(self):
        data = self.snapshot(self.spec("\\"))
        (self.root / self.files["source_bindings"][0]).write_bytes(b"modified")
        self.assertEqual(data["source_bindings"], self.source)
        with self.assertRaises(TypeError):
            data["source_bindings"] = b"replacement"
        with self.assertRaisesRegex(RuntimeError, "Input hash: source_bindings"):
            self.snapshot(self.spec("\\"))

    def test_wrong_digest_rejected_for_both_spellings(self):
        for separator in ("/", "\\"):
            spec = self.spec(separator)
            spec["files"]["source_bindings"]["sha256"] = "0" * 64
            with self.subTest(separator=separator):
                with self.assertRaisesRegex(RuntimeError, "Input hash: source_bindings"):
                    self.snapshot(spec)

    def test_same_file_alias_does_not_bypass_hash_check(self):
        spec = self.spec()
        spec["files"]["second_alias"] = {
            "path": self.files["source_bindings"][0].replace("/", "\\"),
            "sha256": "0" * 64}
        with self.assertRaisesRegex(RuntimeError, "Input hash: second_alias"):
            self.snapshot(spec)

    def test_parent_escape_rejected_for_both_spellings(self):
        outside = self.outer / "outside.json"
        outside.write_bytes(self.source)
        for path in ("../outside.json", "..\\outside.json", "inputs/../../outside.json"):
            spec = self.spec()
            spec["files"]["source_bindings"]["path"] = path
            with self.subTest(path=path):
                with self.assertRaisesRegex(RuntimeError, "Escaping input"):
                    self.snapshot(spec)

    def test_absolute_and_drive_relative_paths_rejected(self):
        paths = ["/tmp/input", "\\rooted", "C:\\input", "C:/input", "C:input",
                 "\\\\server\\share\\input", "//server/share/input",
                 "\\\\?\\C:\\input", str((self.root / self.files["source_bindings"][0]).resolve())]
        for path in paths:
            spec = self.spec()
            spec["files"]["source_bindings"]["path"] = path
            with self.subTest(path=path):
                with self.assertRaisesRegex(RuntimeError, "Absolute input path"):
                    self.snapshot(spec)

    def test_invalid_path_types_rejected(self):
        for path in (None, 12, "", "nul\x00path"):
            spec = self.spec()
            spec["files"]["source_bindings"]["path"] = path
            with self.subTest(path=path):
                with self.assertRaisesRegex(RuntimeError, "Invalid input path"):
                    self.snapshot(spec)

    def test_symlink_escape_rejected(self):
        outside = self.outer / "outside.json"
        outside.write_bytes(self.source)
        link = self.root / "inputs/nested/link.json"
        try:
            link.symlink_to(outside)
        except OSError as error:
            if os.name != "nt":
                raise
            self.skipTest("Symlink creation unavailable: " + str(error))
        for path in ("inputs/nested/link.json", "inputs\\nested\\link.json"):
            spec = self.spec()
            spec["files"]["source_bindings"]["path"] = path
            with self.subTest(path=path):
                with self.assertRaisesRegex(RuntimeError, "Escaping input"):
                    self.snapshot(spec)

    def test_nested_member_hash_still_checked(self):
        source = json.loads(self.source)
        source["members"]["common"]["sha256"] = "0" * 64
        raw = json.dumps(source).encode()
        (self.root / self.files["source_bindings"][0]).write_bytes(raw)
        spec = self.spec("\\")
        spec["files"]["source_bindings"]["sha256"] = verify.sha(raw)
        with self.assertRaisesRegex(RuntimeError, "Nested common hash"):
            self.snapshot(spec)

    def test_package_paths_and_hashes_use_same_boundary(self):
        for separator in ("/", "\\"):
            name = self.files["source_bindings"][0].replace("/", separator)
            manifest = self.root / "MANIFEST.json"
            manifest.write_text(json.dumps({name: verify.sha(self.source)}), encoding="utf-8")
            self.assertEqual(verify.checked_package(self.root)[name], self.source)
            manifest.write_text(json.dumps({name: "0" * 64}), encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "Package hash"):
                verify.checked_package(self.root)
        for name in ("../outside.json", "..\\outside.json", "C:outside.json"):
            manifest.write_text(json.dumps({name: verify.sha(self.source)}), encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "Escaping|Absolute"):
                verify.checked_package(self.root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
