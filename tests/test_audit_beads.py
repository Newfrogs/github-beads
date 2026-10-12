import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/github-beads/scripts/audit_beads.py"
SPEC = importlib.util.spec_from_file_location("audit_beads", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def issue(identity, target=None, kind="blocks", status="open"):
    row = {"id": identity, "title": f"Deliver {identity}", "description": "Observable outcome and verification.", "status": status, "priority": 2}
    if target is not None:
        row["dependencies"] = [{"issue_id": identity, "depends_on_id": target, "type": kind}]
    return row


class AuditTests(unittest.TestCase):
    def codes(self, result, key="errors"):
        return {entry["code"] for entry in result[key]}

    def test_valid_dag_and_mapping(self):
        result = MODULE.audit([issue("a", "b"), issue("b")], {"requirements": [{"id": "R1", "disposition": "included", "bead_ids": ["a"]}]})
        self.assertTrue(result["ok"])
        self.assertEqual(result["coverage"]["state"], "mapping_checked")

    def test_duplicate_ids_and_missing_endpoints(self):
        result = MODULE.audit([issue("a", "missing"), issue("a")])
        self.assertEqual(self.codes(result), {"duplicate_id", "missing_dependency_target"})

    def test_cycle_is_exact_component_not_downstream(self):
        result = MODULE.audit([issue("a", "b"), issue("b", "a"), issue("c", "a")])
        cycle = next(entry for entry in result["errors"] if entry["code"] == "active_structural_cycle")
        self.assertEqual(cycle["ids"], ["a", "b"])

    def test_parent_child_and_conditional_cycles(self):
        for kind in ("parent-child", "conditional-blocks", "waits-for"):
            with self.subTest(kind=kind):
                result = MODULE.audit([issue("a", "b", kind), issue("b", "a", kind)])
                self.assertIn("active_structural_cycle", self.codes(result))

    def test_related_edges_do_not_create_blocking_cycles(self):
        result = MODULE.audit([issue("a", "b", "related"), issue("b", "a", "related")])
        self.assertTrue(result["ok"])

    def test_closed_cycle_is_a_warning(self):
        result = MODULE.audit([issue("a", "b", status="closed"), issue("b", "a", status="closed")])
        self.assertTrue(result["ok"])
        self.assertIn("closed_only_cycle", self.codes(result, "warnings"))

    def test_typed_edges_and_owner_identity(self):
        row = issue("a", "b")
        row["dependencies"].append({"issue_id": "a", "depends_on_id": "b", "type": "related"})
        self.assertTrue(MODULE.audit([row, issue("b")])["ok"])
        row["dependencies"].append({"issue_id": "wrong", "depends_on_id": "b", "type": "blocks"})
        result = MODULE.audit([row, issue("b")])
        self.assertTrue({"duplicate_typed_edge", "dependency_owner_mismatch"}.issubset(self.codes(result)))

    def test_external_and_unknown_edges_are_explicit(self):
        result = MODULE.audit([issue("a", "external:api:api-1"), issue("b", "a", "custom-policy")])
        self.assertTrue(result["ok"])
        self.assertEqual(self.codes(result, "warnings"), {"external_dependencies_not_verified", "custom_edge_not_analyzed"})

    def test_coverage_gaps_and_tombstones(self):
        manifest = {"requirements": [
            {"id": "R1", "disposition": "included", "bead_ids": []},
            {"id": "R2", "disposition": "deferred", "bead_ids": ["missing"]},
            {"id": "R3", "disposition": "included", "bead_ids": ["deleted"]},
        ]}
        result = MODULE.audit([issue("deleted", status="tombstone")], manifest)
        self.assertEqual(self.codes(result), {"unmapped_requirement", "missing_disposition_reason", "missing_coverage_bead", "tombstone_coverage"})

    def test_missing_manifest_is_not_coverage_success(self):
        self.assertEqual(MODULE.audit([issue("a")])["coverage"]["state"], "not_checked")
        self.assertFalse(MODULE.audit([issue("a")], {"requirements": []})["ok"])

    def test_completion_gate_is_opt_in_and_needs_coverage(self):
        self.assertTrue(MODULE.audit([issue("a")])["ok"])
        self.assertEqual(MODULE.audit([issue("a")])["completion"]["state"], "not_checked")
        result = MODULE.audit([issue("a")], require_closed=True)
        self.assertFalse(result["ok"])
        self.assertIn("completion_requires_coverage", self.codes(result))
        self.assertEqual(result["completion"]["state"], "unavailable")

    def test_completion_rejects_open_in_progress_and_custom_status(self):
        for status in ("open", "in_progress", "deferred", "awaiting-review"):
            with self.subTest(status=status):
                manifest = {"requirements": [{"id": "R1", "disposition": "included", "bead_ids": ["a"]}]}
                result = MODULE.audit([issue("a", status=status)], manifest, require_closed=True)
                self.assertEqual(self.codes(result), {"included_bead_not_closed"})
                self.assertEqual(result["errors"][0]["status"], status)
                self.assertEqual(result["completion"]["closed_beads"], 0)

    def test_completion_allows_deferred_excluded_and_unmapped_backlog(self):
        manifest = {"requirements": [
            {"id": "R1", "disposition": "included", "bead_ids": ["a"]},
            {"id": "R2", "disposition": "deferred", "bead_ids": ["b"], "reason": "Approved for later delivery"},
            {"id": "R3", "disposition": "out_of_scope", "bead_ids": [], "reason": "User excluded it"},
        ]}
        result = MODULE.audit([issue("a", status="closed"), issue("b", status="deferred"), issue("unrelated")], manifest, require_closed=True)
        self.assertTrue(result["ok"], result)
        self.assertEqual(result["completion"], {"state": "included_status_checked", "included_beads": 1, "closed_beads": 1})

    def test_completion_shared_bead_count_and_invalid_coverage(self):
        manifest = {"requirements": [{"id": key, "disposition": "included", "bead_ids": ["a"]} for key in ("R1", "R2")]}
        result = MODULE.audit([issue("a", status="closed")], manifest, require_closed=True)
        self.assertTrue(result["ok"])
        self.assertEqual(result["completion"]["included_beads"], 1)
        result = MODULE.audit([issue("a", status="closed")], {"requirements": []}, require_closed=True)
        self.assertFalse(result["ok"])
        self.assertIn("invalid_coverage_manifest", self.codes(result))

    def test_completion_missing_and_tombstone_records_never_pass(self):
        manifest = {"requirements": [{"id": "R1", "disposition": "included", "bead_ids": ["missing", "deleted"]}]}
        result = MODULE.audit([issue("deleted", status="tombstone")], manifest, require_closed=True)
        self.assertFalse(result["ok"])
        self.assertTrue({"missing_coverage_bead", "tombstone_coverage", "included_bead_not_closed"}.issubset(self.codes(result)))

    def test_completion_cli_rejects_unfinished_scope_without_changing_input(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as directory:
            export = Path(directory) / "issues.jsonl"
            coverage = Path(directory) / "coverage.json"
            export.write_text(json.dumps(issue("a")) + "\n", encoding="utf-8")
            coverage.write_text(json.dumps({"requirements": [{"id": "R1", "disposition": "included", "bead_ids": ["a"]}]}), encoding="utf-8")
            before = (export.read_bytes(), coverage.read_bytes())
            result = subprocess.run([sys.executable, str(SCRIPT), str(export), "--coverage", str(coverage), "--require-closed"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(json.loads(result.stdout)["errors"][0]["code"], "included_bead_not_closed")
            self.assertEqual((export.read_bytes(), coverage.read_bytes()), before)
            export.write_text(json.dumps(issue("a", status="closed")) + "\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(export), "--coverage", str(coverage), "--require-closed"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["completion"]["closed_beads"], 1)

    def test_duplicate_requirement_and_title_review(self):
        a, b = issue("a"), issue("b")
        a["title"], b["title"] = "  Same TITLE  ", "same title"
        manifest = {"requirements": [{"id": "R1", "disposition": "included", "bead_ids": ["a"]}] * 2}
        result = MODULE.audit([a, b], manifest)
        self.assertIn("duplicate_requirement_id", self.codes(result))
        self.assertIn("duplicate_title_candidates", self.codes(result, "warnings"))

    def test_deep_dag_avoids_recursion_limit(self):
        rows = [issue(str(index), str(index + 1) if index < 2999 else None) for index in range(3000)]
        self.assertTrue(MODULE.audit(rows)["ok"])

    def test_malformed_fields_are_reported(self):
        rows = [[], {"id": []}, {"id": "a", "status": "custom-review", "priority": True, "title": None, "description": "", "dependencies": None}]
        result = MODULE.audit(rows, {"requirements": [{"id": "R1", "disposition": [], "bead_ids": []}]})
        self.assertTrue({"invalid_record", "invalid_id", "invalid_priority", "missing_title", "missing_description", "invalid_dependencies", "invalid_disposition"}.issubset(self.codes(result)))

    def test_invalid_status_with_cycle_does_not_crash(self):
        row = issue("a", "a")
        row["status"] = []
        result = MODULE.audit([row])
        self.assertTrue({"missing_status", "self_dependency", "active_structural_cycle"}.issubset(self.codes(result)))

    def test_cli_is_read_only_and_has_meaningful_exit_codes(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as directory:
            path = Path(directory) / "issues.jsonl"
            body = json.dumps(issue("čvor-1"), ensure_ascii=False).encode("utf-8") + b"\n"
            path.write_bytes(body)
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(path.read_bytes(), body)
            self.assertEqual(json.loads(result.stdout)["coverage"]["state"], "not_checked")
            path.write_text(json.dumps(issue("a", "missing")) + "\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(result.stdout)["errors"][0]["code"], "missing_dependency_target")
            path.write_text("<<<<<<< branch\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stdout)["errors"][0]["code"], "input_error")


if __name__ == "__main__":
    unittest.main()
