#!/usr/bin/env python3
"""Run repository-level integrity checks for CoGo-Knowledge."""
from __future__ import annotations
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from typing import Any
from validate_dataset import validate_dataset

ROOT = Path(__file__).resolve().parents[1]

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_repository_manifest(root: Path, manifest_path: Path) -> tuple[list[str], list[str]]:
    """Validate the current repository inventory independently of the historical Stage 7 manifest."""
    errors: list[str] = []
    info: list[str] = []
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Could not parse repository manifest: {exc}"], info

    if manifest.get("repository") != "RyouRey/CoGo-Knowledge":
        errors.append("Repository manifest has an unexpected repository identifier")
    if manifest.get("manifest_excludes_self") is not True:
        errors.append("Repository manifest must explicitly exclude itself from its inventory")

    entries = manifest.get("files")
    if not isinstance(entries, list):
        return errors + ["Repository manifest 'files' must be a list"], info
    declared_count = manifest.get("file_count")
    if declared_count != len(entries):
        errors.append(f"Repository manifest file_count mismatch (declared {declared_count}, entries {len(entries)})")

    listed: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("Repository manifest contains a non-object file entry")
            continue
        rel = entry.get("path")
        if not isinstance(rel, str) or not rel or Path(rel).is_absolute() or ".." in Path(rel).parts:
            errors.append(f"Repository manifest contains an unsafe/invalid path: {rel!r}")
            continue
        normalized = Path(rel).as_posix()
        if normalized in listed:
            errors.append(f"Repository manifest contains duplicate path: {normalized}")
            continue
        listed.add(normalized)
        target = root / normalized
        if not target.is_file():
            errors.append(f"Repository manifest file is missing: {normalized}")
            continue
        expected_size = entry.get("bytes")
        actual_size = target.stat().st_size
        if expected_size != actual_size:
            errors.append(f"Repository manifest size mismatch: {normalized} (expected {expected_size}, got {actual_size})")
        expected_sha = entry.get("sha256")
        actual_sha = sha256_file(target)
        if expected_sha != actual_sha:
            errors.append(f"Repository manifest SHA-256 mismatch: {normalized}")

    excluded_parts = {".git", ".venv", "venv", "__pycache__", ".pytest_cache"}
    actual_paths = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file()
        and path != manifest_path
        and not any(part in excluded_parts for part in path.relative_to(root).parts)
    }
    missing_entries = sorted(actual_paths - listed)
    stale_entries = sorted(listed - actual_paths)
    if missing_entries:
        errors.append("Repository manifest omits files: " + ", ".join(missing_entries))
    if stale_entries:
        errors.append("Repository manifest lists files not in the current tree: " + ", ".join(stale_entries))
    info.append(f"Current repository manifest checked: {len(listed)} entries")
    return errors, info

def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    info: list[str] = []

    required_paths = [
        "README.md", "CONTRIBUTING.md", "CHANGELOG.md", "01_MASTER_INDEX.md",
        "11_MASTER_KNOWLEDGE_DATASET.jsonl", "12_DATASET_QA_REPORT.json",
        "13_FINAL_PACKAGE_MANIFEST.json", "repository_manifest.json", "docs/DATASET_SCHEMA.md",
    ]
    for rel in required_paths:
        if not (ROOT / rel).is_file():
            errors.append(f"Required file is missing: {rel}")

    # Validate the master dataset.
    dataset_report = validate_dataset(ROOT / "11_MASTER_KNOWLEDGE_DATASET.jsonl")
    errors.extend(f"Dataset: {item}" for item in dataset_report["errors"])
    warnings.extend(f"Dataset: {item}" for item in dataset_report["warnings"])
    info.append(f"Master dataset: {dataset_report['record_count']} records, {dataset_report['unique_canonical_ids']} unique IDs")

    # Parse all JSON metadata files except JSONL (already handled above).
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"Invalid JSON file {path.relative_to(ROOT).as_posix()}: {exc}")
    info.append("JSON metadata syntax checked")

    # Current repository inventory includes maintenance files and is distinct from Stage 7.
    current_manifest = ROOT / "repository_manifest.json"
    if current_manifest.exists():
        manifest_errors, manifest_info = validate_repository_manifest(ROOT, current_manifest)
        errors.extend(manifest_errors)
        info.extend(manifest_info)
    else:
        errors.append("Current repository manifest is missing: repository_manifest.json")

    # Historical Stage 7 manifest is immutable evidence for the original package.
    manifest_path = ROOT / "13_FINAL_PACKAGE_MANIFEST.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            for entry in manifest.get("files", []):
                rel = entry.get("path")
                if not isinstance(rel, str):
                    errors.append("Historical manifest contains an entry without a string path")
                    continue
                target = ROOT / rel
                if not target.is_file():
                    errors.append(f"Historical manifest file is missing: {rel}")
                    continue
                actual_size = target.stat().st_size
                if actual_size != entry.get("bytes"):
                    errors.append(f"Historical manifest size mismatch: {rel} (expected {entry.get('bytes')}, got {actual_size})")
                actual_sha = sha256_file(target)
                if actual_sha != entry.get("sha256"):
                    errors.append(f"Historical manifest SHA-256 mismatch: {rel}")
            info.append(f"Historical Stage 7 manifest checked: {len(manifest.get('files', []))} files")
        except Exception as exc:
            errors.append(f"Could not validate historical manifest: {exc}")

    # Test every preserved stage archive.
    archive_paths = sorted((ROOT / "prior_stages").glob("*.zip"))
    if not archive_paths:
        errors.append("No prior-stage ZIP archives found under prior_stages/")
    for archive_path in archive_paths:
        try:
            with zipfile.ZipFile(archive_path) as archive:
                damaged = archive.testzip()
                if damaged:
                    errors.append(f"Corrupt ZIP entry in {archive_path.relative_to(ROOT)}: {damaged}")
                else:
                    info.append(f"Archive OK: {archive_path.relative_to(ROOT).as_posix()}")
        except Exception as exc:
            errors.append(f"Could not read archive {archive_path.relative_to(ROOT)}: {exc}")

    print("CoGo-Knowledge repository validation")
    for item in info:
        print(f"OK: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    for item in errors:
        print(f"ERROR: {item}")
    print(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
