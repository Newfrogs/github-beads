#!/usr/bin/env python3
"""Read-only structural and coverage audit of a full Beads JSONL export."""

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys
import unicodedata

BLOCKING = {"blocks", "parent-child", "conditional-blocks", "waits-for"}
KNOWN_EDGES = BLOCKING | {
    "related", "discovered-from", "replies-to", "relates-to",
    "duplicates", "supersedes", "caused-by",
}
TERMINAL = {"closed", "tombstone"}


def cycle_components(graph):
    """Iterative Kosaraju traversal; handles deep graphs without recursion."""
    visited, order = set(), []
    for root in sorted(graph):
        if root in visited:
            continue
        visited.add(root)
        stack = [(root, iter(sorted(graph[root])))]
        while stack:
            node, children = stack[-1]
            child = next(children, None)
            if child is None:
                order.append(node)
                stack.pop()
            elif child not in visited:
                visited.add(child)
                stack.append((child, iter(sorted(graph[child]))))
    reverse = {node: set() for node in graph}
    for node, children in graph.items():
        for child in children:
            reverse[child].add(node)
    visited, components = set(), []
    for root in reversed(order):
        if root in visited:
            continue
        visited.add(root)
        component, stack = [], [root]
        while stack:
            node = stack.pop()
            component.append(node)
            for child in sorted(reverse[node]):
                if child not in visited:
                    visited.add(child)
                    stack.append(child)
        if len(component) > 1 or root in graph[root]:
            components.append(sorted(component))
    return sorted(components)


def audit(rows, coverage=None):
    errors, warnings = [], []

    def error(code, **details):
        errors.append({"code": code, **details})

    def warn(code, **details):
        warnings.append({"code": code, **details})

    records, titles = {}, defaultdict(list)
    for number, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            error("invalid_record", record=number)
            continue
        identity = row.get("id")
        if not isinstance(identity, str) or not identity.strip():
            error("invalid_id", record=number)
            continue
        if identity in records:
            error("duplicate_id", id=identity)
            continue
        records[identity] = row
        status = row.get("status")
        if not isinstance(status, str) or not status.strip():
            error("missing_status", id=identity)
        if status == "tombstone":
            continue
        title = row.get("title")
        if not isinstance(title, str) or not title.strip():
            error("missing_title", id=identity)
        else:
            normalized = " ".join(unicodedata.normalize("NFKC", title).casefold().split())
            titles[normalized].append(identity)
        description = row.get("description")
        if not isinstance(description, str) or not description.strip():
            error("missing_description", id=identity)
        priority = row.get("priority")
        if type(priority) is not int or priority not in range(5):
            error("invalid_priority", id=identity)
    for identities in titles.values():
        if len(identities) > 1:
            warn("duplicate_title_candidates", ids=sorted(identities))

    graph = {identity: set() for identity in records}
    edge_count, external = 0, []
    for identity, row in records.items():
        dependencies = row.get("dependencies", [])
        if not isinstance(dependencies, list):
            error("invalid_dependencies", id=identity)
            continue
        seen = set()
        for dependency in dependencies:
            if not isinstance(dependency, dict):
                error("invalid_dependency", id=identity)
                continue
            target, kind = dependency.get("depends_on_id"), dependency.get("type")
            if not isinstance(target, str) or not target.strip() or not isinstance(kind, str) or not kind.strip():
                error("invalid_dependency", id=identity)
                continue
            if dependency.get("issue_id", identity) != identity:
                error("dependency_owner_mismatch", id=identity, target=target)
            edge = (target, kind)
            if edge in seen:
                error("duplicate_typed_edge", id=identity, target=target, type=kind)
                continue
            seen.add(edge)
            edge_count += 1
            if kind not in KNOWN_EDGES:
                warn("custom_edge_not_analyzed", id=identity, target=target, type=kind)
            if target.startswith("external:"):
                external.append({"id": identity, "target": target, "type": kind})
                continue
            if target not in records:
                error("missing_dependency_target", id=identity, target=target, type=kind)
                continue
            if target == identity:
                error("self_dependency", id=identity, type=kind)
            if kind in BLOCKING:
                graph[identity].add(target)

    cycles = cycle_components(graph)
    for component in cycles:
        if all(isinstance(records[node].get("status"), str) and records[node]["status"] in TERMINAL for node in component):
            warn("closed_only_cycle", ids=component)
        else:
            error("active_structural_cycle", ids=component)
    if external:
        warn("external_dependencies_not_verified", edges=external)

    coverage_summary = {"state": "not_checked"}
    if coverage is not None:
        requirements = coverage.get("requirements") if isinstance(coverage, dict) else None
        if not isinstance(requirements, list) or not requirements:
            error("invalid_coverage_manifest")
            requirements = []
        seen_requirements = set()
        counts = {"included": 0, "deferred": 0, "out_of_scope": 0}
        for requirement in requirements:
            if not isinstance(requirement, dict):
                error("invalid_requirement")
                continue
            req_id, disposition = requirement.get("id"), requirement.get("disposition")
            if not isinstance(req_id, str) or not req_id.strip():
                error("invalid_requirement_id")
                continue
            if req_id in seen_requirements:
                error("duplicate_requirement_id", requirement=req_id)
            seen_requirements.add(req_id)
            if not isinstance(disposition, str) or disposition not in counts:
                error("invalid_disposition", requirement=req_id)
                continue
            counts[disposition] += 1
            ids = requirement.get("bead_ids", [])
            if not isinstance(ids, list) or any(not isinstance(node, str) or not node.strip() for node in ids):
                error("invalid_coverage_ids", requirement=req_id)
                continue
            if disposition != "out_of_scope" and not ids:
                error("unmapped_requirement", requirement=req_id)
            reason = requirement.get("reason")
            if disposition != "included" and (not isinstance(reason, str) or not reason.strip()):
                error("missing_disposition_reason", requirement=req_id)
            if len(ids) != len(set(ids)):
                error("duplicate_coverage_id", requirement=req_id)
            for node in ids:
                if node not in records:
                    error("missing_coverage_bead", requirement=req_id, id=node)
                elif records[node].get("status") == "tombstone":
                    error("tombstone_coverage", requirement=req_id, id=node)
        coverage_summary = {"state": "mapping_checked", "requirements": len(requirements), **counts}

    if not records:
        warn("empty_export")
    return {
        "schema_version": 1,
        "ok": not errors,
        "summary": {"issues": len(records), "typed_edges": edge_count, "cycle_components": len(cycles)},
        "coverage": coverage_summary,
        "errors": errors,
        "warnings": warnings,
        "limits": "Structural and mapping checks only; requirement completeness, semantic quality, readiness policy, and external dependencies need separate review.",
    }


def load_jsonl(path):
    data = path.read_bytes()
    rows = []
    for line_number, line in enumerate(data.decode("utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL at line {line_number}: {exc.msg}") from exc
    return rows, hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path, help="Full Beads issue-object-per-line JSONL export")
    parser.add_argument("--coverage", type=Path, help="Requirement coverage map JSON")
    args = parser.parse_args()
    try:
        rows, export_hash = load_jsonl(args.export)
        coverage, coverage_hash = None, None
        if args.coverage:
            data = args.coverage.read_bytes()
            coverage = json.loads(data.decode("utf-8-sig"))
            coverage_hash = hashlib.sha256(data).hexdigest()
        result = audit(rows, coverage)
        result["inputs"] = {"export_sha256": export_hash, "coverage_sha256": coverage_hash}
    except (OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"schema_version": 1, "ok": False, "errors": [{"code": "input_error", "message": str(exc)}]}))
        return 2
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
