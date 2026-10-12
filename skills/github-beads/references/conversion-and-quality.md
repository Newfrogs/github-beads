# Conversion and quality

## Prepare a requirement inventory

Capture the user's goal, inputs and outputs, boundaries, constraints, and repository-specific architecture. Extract independently testable requirements without treating every paragraph as a task. Give each requirement a stable identifier tied to a source path, section, or GitHub URL. Keep assumptions explicit. When the source lacks a needed decision, represent the investigation and the affected downstream work.

Use this planning aid before creating records; it is a coverage inventory, not a substitute tracker. Beads status and executable scope live in actual tracker records.

## Size work by a verifiable outcome

Split when work has distinct completion evidence, ownership, prerequisites, or failure handling. Combine fragments that cannot be usefully executed or verified separately. A leaf should be small enough for one coherent implementation effort and substantial enough to deliver an outcome. Do not enforce a universal duration or task count.

Epics describe shared goals, boundaries, and completion conditions. Children carry their own local context; a child must not depend on reading the whole epic to discover its acceptance criteria. Use containment for grouping and explicit prerequisite edges for sequencing. Parent relationships may participate in backend readiness policy, so inspect the actual ready set after adding them.

## Bead body

Adapt this structure to the task rather than writing empty headings:

```markdown
## Outcome
What observable behavior or artifact is delivered.

## Context and rationale
Why it is needed and the architectural decision already made.

## Scope and constraints
Interfaces, relevant paths, compatibility rules, important failure handling,
and explicit exclusions. Label proposed paths as proposed.

## Acceptance criteria
Concrete conditions that distinguish done from partially implemented.

## Verification
Tests or inspections that prove the criteria, fixtures and negative cases
where relevant, and expected evidence. Do not claim unrun checks passed.

## Dependencies
Prerequisites and why they are needed. Tracker edges encode the sequence.

## Source
Stable requirement IDs and exact source sections or issue URLs.
```

An implementation task should name its meaningful checks. Create separate test tasks only when they deliver independent fixtures, infrastructure, or cross-feature verification. Avoid deferring all validation into one final testing bead. For low-impact documentation or configuration work, a concrete inspection can be sufficient.

## Review the graph and source coverage

Review the whole conversion in both directions: every requirement has a disposition; every new bead serves an identified requirement or a justified prerequisite. Closed beads can supply coverage only when their implementation evidence satisfies the current source. Exact title matches are candidates for review, not proof of duplication.

Check edge direction, missing endpoints, self-dependencies, active cycles, duplicate typed edges, unexplained blockers, and prerequisites that unnecessarily serialize independent work. Explain external dependencies and ownership boundaries. If an epic and a child appear to deadlock under project policy, inspect the policy and correct the actual relationship instead of adding inverse edges speculatively.

For `bv`, use the selected backend's refreshed export and robot modes. Inspect any incomplete or timed-out analysis; a missing metric is not evidence of graph health. Native readiness remains the authority for which records can be claimed. [bv robot interface](https://github.com/Dicklesworthstone/beads_viewer#-agent-quickstart-robot-mode).

## Coverage map schema

Supply a JSON object with a nonempty `requirements` array to the auditor. `included` and `deferred` entries need at least one real bead ID. `deferred` and `out_of_scope` entries need an explicit reason. A deferred bead must also be gated appropriately in the tracker; the map alone does not defer it.

```json
{
  "requirements": [
    {"id": "REQ-PARSE-01", "disposition": "included", "bead_ids": ["actual-id"]},
    {"id": "REQ-EXPORT-02", "disposition": "deferred", "bead_ids": ["another-id"], "reason": "Requires the approved export contract"},
    {"id": "REQ-HOST-03", "disposition": "out_of_scope", "bead_ids": [], "reason": "User excluded hosted deployment"}
  ]
}
```

Place coverage reports where the repository keeps planning artifacts, outside the tracker's internal storage. Capture source revision or file hash and meaningful acceptance evidence in the report when useful. Never treat an illustrative ID in this reference as an actual bead.

## Read-only auditor

`scripts/audit_beads.py` accepts a full issue-object-per-line JSONL export. It does not open SQLite, execute tracker commands, run Git, or modify inputs. It returns JSON and exits 0 with no errors, 1 with audit errors, or 2 for unreadable/invalid input. Warnings require human or agent review.

Checks include record identity, required basic content, duplicate titles as warnings, typed edge identity, missing local endpoints, blocking strongly connected components, and coverage references. It understands the checked upstream model's `blocks`, `parent-child`, `conditional-blocks`, and `waits-for` edge types for structural cycle detection. This is a conservative structural check, not a simulation of conditional gates or readiness. Closed-only cycles are warnings; cycles touching nonterminal records are errors. [Upstream issue and dependency model](https://github.com/Dicklesworthstone/beads_rust/blob/main/src/model/mod.rs).

External endpoints starting with `external:` and unknown custom relationship types are reported for separate review. Supply a complete export to avoid false missing-endpoint reports. Tombstones may appear in exports and are not acceptable live coverage records.

The auditor cannot detect a requirement omitted from the inventory, verify semantic completeness, prove implementation, assess permissions, or validate backend-specific workflow policy. A clean output is one part of the quality gate. When no coverage map is supplied, coverage is explicitly `not_checked`.
