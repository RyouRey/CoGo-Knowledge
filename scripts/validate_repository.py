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
