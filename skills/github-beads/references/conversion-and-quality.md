# Conversion and quality

## Prepare a requirement inventory

Capture the user's goal, inputs and outputs, boundaries, constraints, and repository-specific architecture. Extract independently testable requirements without treating every paragraph as a task. Give each requirement a stable identifier tied to a source path, section, or GitHub URL. Keep assumptions explicit. When the source lacks a needed decision, represent the investigation and the affected downstream work.

Use this planning aid before creating records; it is a coverage inventory, not a substitute tracker. Beads status and executable scope live in actual tracker records.

Treat conversion as preservation of execution-relevant intent, not extraction of short titles. Read the complete supplied plan, including background, decisions, user workflows, failure handling, and verification. Transfer the local context an implementing agent needs into the actual record. Retain the original plan for provenance and whole-system decisions; self-contained Beads reduce routine reloading rather than forbidding source checks when requirements change.

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

Check each executable record using **WHAT / WHY / HOW**: what observable outcome it delivers, why the product or architecture needs it, and how its constraints and verification distinguish a correct result. A fresh implementing agent should not have to invent missing interfaces, hidden permissions, or recovery policy. Long descriptions and embedded Markdown are appropriate when they preserve necessary context; length itself is not quality.

For code changes, include meaningful unit or integration checks and end-to-end flows where the behavior crosses components. Specify fixture setup, important negative cases, expected outcomes, and diagnostic evidence useful when a check fails, such as the failing stage, request identifier, or retry outcome. Respect the project's sensitive-data and logging rules; detailed diagnostics do not justify recording secrets or user content indiscriminately. Avoid requiring unit and end-to-end suites for every document or small configuration task.

## Reconcile duplicates without losing context

Search existing open and closed work before creation; after a substantial creation batch, inspect exact duplicates and meaningful overlaps. Matching titles alone do not establish equivalence. Compare outcomes, acceptance criteria, source identity, ownership, prerequisites, and any implementation already delivered. Related tasks can share a component without being duplicates.

When two records truly represent the same work, choose a canonical survivor that best preserves the full acceptance contract, useful context, test obligations, and correct dependencies. Priority alone is not a reason to discard richer requirements. Transfer missing context and valid links through the native tracker, preserving comments and completed evidence. Redirect coverage references and supported duplicate relationships to the survivor, and disposition the redundant record according to repository policy with an explicit canonical ID. Reconcile both incoming and outgoing prerequisites; remove accidental self-edges and validate readiness after the change. Do not delete history, reopen completed work reflexively, or close partly distinct work as a duplicate to reduce counts.

## Review the graph and source coverage

Review the whole conversion in both directions: every requirement has a disposition; every new bead serves an identified requirement or a justified prerequisite. Closed beads can supply coverage only when their implementation evidence satisfies the current source. Exact title matches are candidates for review, not proof of duplication.

Check edge direction, missing endpoints, self-dependencies, active cycles, duplicate typed edges, unexplained blockers, and prerequisites that unnecessarily serialize independent work. Explain external dependencies and ownership boundaries. If an epic and a child appear to deadlock under project policy, inspect the policy and correct the actual relationship instead of adding inverse edges speculatively.

Polish records by demonstrated defects: missing WHAT / WHY / HOW, omitted source behavior, unsupported decisions, unsuitable boundaries, inaccurate priorities, unclear verification, or faulty edges. Update actual records through the selected backend, then read back changes and repeat affected checks. Keep accepted features and failure cases while simplifying; removal of an included requirement needs an explicit scope decision and coverage update.

An independent or fresh-context reviewer is useful when a consequential graph was created in one long session, there is evidence of anchoring, or a complex conversion needs another perspective. Give the reviewer current repository instructions and purpose, the complete source, current records, and native diagnostics. Ask for precise findings and revisions rather than a fixed issue count or a mandatory second model. A clean automated export is evidence of structural integrity, not proof that all meaning survived.

Stop polishing when source coverage is accounted for, executable context and acceptance checks are adequate, and active cycles or unexplained blockers are resolved. A lower rate of substantial defects can support that judgment, but fixed pass counts, output-length trends, or a numerical convergence score cannot certify readiness. On repeated design oscillation, return the specific unresolved choice to the plan; on uncontrolled expansion, separate optional ideas; on a low-quality plateau, obtain missing evidence instead of extending the review loop.

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

For a delivery audit, optionally add `--require-closed` with the coverage map:

```text
python <skill-directory>/scripts/audit_beads.py <full-export.jsonl> --coverage <coverage-map.json> --require-closed
```

This reports unique included-Bead and closed-Bead counts and rejects any record referenced by an `included` requirement whose status is not exactly `closed`. It also rejects use without a coverage map. Deferred and excluded scope is not required to be closed. The default audit permits unfinished included records so it remains useful immediately after conversion. An omitted requirement or an unreferenced task can still escape this status guard; a closed status alone does not establish acceptance evidence or prove the user goal is delivered.

The auditor cannot detect a requirement omitted from the inventory, verify semantic completeness, prove implementation, assess permissions, or validate backend-specific workflow policy. A clean output is one part of the quality gate. When no coverage map is supplied, coverage is explicitly `not_checked`.

This workflow adapts the conversion, executable-memory, polishing, fresh-review, and deduplication practices in the [Agentic Coding Flywheel guide](https://agent-flywheel.com/complete-guide). It preserves their purpose while using evidence of completeness and actual tracker state instead of universal task counts or review quotas.
