import hashlib
import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_repository import validate_repository_manifest  # noqa: E402


def write_manifest(root: Path, entries: list[dict[str, object]]) -> Path:
    manifest = {
        "repository": "RyouRey/CoGo-Knowledge",
        "edition": "repository-focused",
        "manifest_version": 1,
        "manifest_excludes_self": True,
        "file_count": len(entries),
        "files": entries,
    }
    path = root / "repository_manifest.json"
    path.write_text(json.dumps(manifest), encoding="utf-8")
    return path


def entry_for(root: Path, relative: str) -> dict[str, object]:
    path = root / relative
    data = path.read_bytes()
    return {"path": relative, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


class RepositoryManifestTests(unittest.TestCase):
    def test_valid_manifest_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("hello", encoding="utf-8")
            manifest_path = write_manifest(root, [entry_for(root, "README.md")])
            errors, info = validate_repository_manifest(root, manifest_path)
            self.assertEqual(errors, [])
            self.assertTrue(any("1 entries" in line for line in info))

    def test_hash_or_size_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("hello", encoding="utf-8")
            entry = entry_for(root, "README.md")
            entry["sha256"] = "0" * 64
            manifest_path = write_manifest(root, [entry])
            errors, _ = validate_repository_manifest(root, manifest_path)
            self.assertTrue(any("SHA-256 mismatch" in error for error in errors))

    def test_unlisted_file_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("hello", encoding="utf-8")
            (root / "extra.md").write_text("new", encoding="utf-8")
            manifest_path = write_manifest(root, [entry_for(root, "README.md")])
            errors, _ = validate_repository_manifest(root, manifest_path)
            self.assertTrue(any("omits files" in error for error in errors))

    def test_path_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest_path = write_manifest(root, [{"path": "../secret", "bytes": 1, "sha256": "x"}])
            errors, _ = validate_repository_manifest(root, manifest_path)
            self.assertTrue(any("unsafe/invalid path" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
