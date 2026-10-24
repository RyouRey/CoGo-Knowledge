#!/usr/bin/env python3
"""Validate the CoGo-Knowledge JSONL dataset without third-party dependencies."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = {
    "canonical_id", "origin_stage", "origin_record_id", "topic", "statement",
    "cogo_version_scope", "evidence_class", "verification_status", "confidence",
    "source_urls", "retrieved_at", "original_record", "origin_records",
}
STANDARD_EVIDENCE_CLASSES = {
    "official_current", "official_versioned", "official_test_definition", "source_stage",
    "android_platform", "derived_guidance", "reference_code_unverified", "device_verified",
}
STANDARD_CONFIDENCE = {"high", "medium", "low"}
STANDARD_VERIFICATION = {
    "documented", "recommended", "source_reviewed", "source_reviewed_not_executed",
    "not_independently_verified", "not_device_verified", "device_verified",
}


def parse_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return [], [f"Could not read {path}: {exc}"]
    for line_no, raw in enumerate(lines, start=1):
        if not raw.strip():
            errors.append(f"Line {line_no}: blank lines are not permitted in JSONL")
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"Line {line_no}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(value, dict):
            errors.append(f"Line {line_no}: expected a JSON object, got {type(value).__name__}")
            continue
        records.append(value)
    return records, errors


def validate_records(records: list[dict[str, Any]]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    seen_ids: set[str] = set()
    evidence_counts: dict[str, int] = {}
    confidence_counts: dict[str, int] = {}
    verification_counts: dict[str, int] = {}
    local_refs: list[dict[str, str]] = []

    for index, record in enumerate(records, start=1):
        where = f"record #{index} ({record.get('canonical_id', 'no canonical_id')})"
        missing = sorted(field for field in REQUIRED_FIELDS if field not in record)
        if missing:
            errors.append(f"{where}: missing required fields: {', '.join(missing)}")
        cid = record.get("canonical_id")
        if not isinstance(cid, str) or not cid.strip():
            errors.append(f"{where}: canonical_id must be a non-empty string")
        elif cid in seen_ids:
            errors.append(f"{where}: duplicate canonical_id {cid}")
        else:
            seen_ids.add(cid)
        if not isinstance(record.get("statement"), str) or not record.get("statement", "").strip():
            errors.append(f"{where}: statement must be a non-empty string")
        if not isinstance(record.get("topic"), str) or not record.get("topic", "").strip():
            errors.append(f"{where}: topic must be a non-empty string")
        urls = record.get("source_urls")
        if not isinstance(urls, list) or any(not isinstance(url, str) for url in urls):
            errors.append(f"{where}: source_urls must be a list of strings")
            urls = []
        for url in urls:
            if url.startswith("local:"):
                local_refs.append({"canonical_id": str(cid), "source": url})
            elif not (url.startswith("https://") or url.startswith("http://")):
                warnings.append(f"{where}: source reference is neither HTTP(S) nor local: ({url})")
        if not isinstance(record.get("original_record"), dict):
            errors.append(f"{where}: original_record must be a JSON object")
        if not isinstance(record.get("origin_records"), list):
            errors.append(f"{where}: origin_records must be a list")

        evidence = str(record.get("evidence_class", "<missing>"))
        confidence = str(record.get("confidence", "<missing>"))
        verification = str(record.get("verification_status", "<missing>"))
        evidence_counts[evidence] = evidence_counts.get(evidence, 0) + 1
        confidence_counts[confidence] = confidence_counts.get(confidence, 0) + 1
        verification_counts[verification] = verification_counts.get(verification, 0) + 1
        if evidence not in STANDARD_EVIDENCE_CLASSES:
            # The source dataset uses broader/legacy labels; preserve them and report, don't rewrite.
            pass
        if confidence not in STANDARD_CONFIDENCE:
            pass
        if verification not in STANDARD_VERIFICATION:
            warnings.append(f"{where}: verification_status '{verification}' is outside the documented vocabulary")

    legacy_evidence = {k: v for k, v in evidence_counts.items() if k not in STANDARD_EVIDENCE_CLASSES}
    legacy_confidence = {k: v for k, v in confidence_counts.items() if k not in STANDARD_CONFIDENCE}
    if legacy_evidence:
        warnings.append("Legacy/non-canonical evidence_class labels found: " + ", ".join(f"{k} ({v})" for k, v in sorted(legacy_evidence.items())))
    if legacy_confidence:
        warnings.append("Legacy confidence values found (some represent evidence type): " + ", ".join(f"{k} ({v})" for k, v in sorted(legacy_confidence.items())))
    if local_refs:
        warnings.append(f"{len(local_refs)} local: source references found; resolve them against reference_material/ before treating them as external links")
    return {
        "record_count": len(records),
        "unique_canonical_ids": len(seen_ids),
        "errors": errors,
        "warnings": warnings,
        "evidence_class_counts": evidence_counts,
        "confidence_counts": confidence_counts,
        "verification_status_counts": verification_counts,
        "local_source_refs": local_refs,
    }


def validate_dataset(path: Path) -> dict[str, Any]:
    records, parse_errors = parse_jsonl(path)
    result = validate_records(records)
    result["errors"] = parse_errors + result["errors"]
    result["path"] = str(path)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=Path(__file__).resolve().parents[1] / "11_MASTER_KNOWLEDGE_DATASET.jsonl", help="JSONL file to validate")
    parser.add_argument("--json", action="store_true", help="Print full report as JSON")
    args = parser.parse_args()
    report = validate_dataset(args.file)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Dataset: {report['path']}")
        print(f"Records parsed: {report['record_count']}; unique IDs: {report['unique_canonical_ids']}")
        print(f"Errors: {len(report['errors'])}; warnings: {len(report['warnings'])}")
        for err in report["errors"]:
            print(f"ERROR: {err}")
        for warning in report["warnings"]:
            print(f"WARNING: {warning}")
    return 1 if report["errors"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
