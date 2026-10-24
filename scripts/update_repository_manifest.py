#!/usr/bin/env python3
"""Regenerate repository_manifest.json for the current tracked file tree."""
from __future__ import annotations
from datetime import date
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_NAME = "repository_manifest.json"
EXCLUDED_PARTS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache"}

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    entries = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.name == MANIFEST_NAME:
            continue
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS for part in rel.parts):
            continue
        entries.append({"path": rel.as_posix(), "bytes": path.stat().st_size, "sha256": digest(path)})
    metadata = {
        "repository": "RyouRey/CoGo-Knowledge",
        "edition": "repository-focused",
        "manifest_version": 1,
        "generated_on": date.today().isoformat(),
        "research_snapshot_date": "2026-10-13",
        "original_stage7_manifest": "13_FINAL_PACKAGE_MANIFEST.json",
        "manifest_excludes_self": True,
        "file_count": len(entries),
        "files": entries,
        "notes": [
            "This inventory covers the repository-focused edition and is separate from the historical Stage 7 manifest.",
            "The research corpus was not revalidated or refreshed merely by regenerating this manifest."
        ]
    }
    (ROOT / MANIFEST_NAME).write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {MANIFEST_NAME}: {len(entries)} files")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
