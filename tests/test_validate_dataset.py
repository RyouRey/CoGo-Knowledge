import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_dataset import validate_dataset, validate_records  # noqa: E402


def sample_record(**overrides):
    row = {
        "canonical_id": "TEST-0001",
        "origin_stage": "STAGE1",
        "origin_record_id": "test-1",
        "topic": "testing",
        "question": None,
        "statement": "A documented sample statement.",
        "procedure": None,
        "expected_result": None,
        "failure_modes": None,
        "cogo_version_scope": "unknown",
        "evidence_class": "official_current",
        "verification_status": "source_reviewed",
        "confidence": "high",
        "source_urls": ["https://example.com/source"],
        "retrieved_at": "2026-10-13",
        "caveat": None,
        "original_record": {"id": "test-1"},
        "origin_records": [{"stage": "STAGE1", "record_id": "test-1"}],
    }
    row.update(overrides)
    return row

class ValidateRecordsTests(unittest.TestCase):
    def test_clean_record_has_no_errors(self):
        report = validate_records([sample_record()])
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["record_count"], 1)

    def test_duplicate_canonical_ids_are_errors(self):
        report = validate_records([sample_record(), sample_record()])
        self.assertTrue(any("duplicate canonical_id" in item for item in report["errors"]))

    def test_missing_statement_is_error(self):
        report = validate_records([sample_record(statement="")])
        self.assertTrue(any("statement must be a non-empty string" in item for item in report["errors"]))

    def test_local_source_is_reported_as_warning(self):
        report = validate_records([sample_record(source_urls=["local:notes/example.md"])])
        self.assertEqual(report["errors"], [])
        self.assertEqual(len(report["local_source_refs"]), 1)
        self.assertTrue(any("local:" in item for item in report["warnings"]))

    def test_legacy_confidence_is_reported(self):
        report = validate_records([sample_record(confidence="official-current")])
        self.assertEqual(report["errors"], [])
        self.assertTrue(any("Legacy confidence values" in item for item in report["warnings"]))

    def test_real_master_dataset_is_structurally_valid(self):
        report = validate_dataset(ROOT / "11_MASTER_KNOWLEDGE_DATASET.jsonl")
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["record_count"], 184)
        self.assertEqual(report["unique_canonical_ids"], 184)
        self.assertGreaterEqual(len(report["warnings"]), 1)

if __name__ == "__main__":
    unittest.main()
