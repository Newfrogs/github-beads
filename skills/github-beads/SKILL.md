---
name: github-beads
license: MIT
description: "Create, refine, and audit dependency-aware Beads tasks from plans, specifications, or GitHub issues in a repository. Use for plan-to-beads conversion, backlog reconciliation, and preparing Beads changes for GitHub review. Prefer Beads Rust (br) for new workspaces; respect an existing bd backend. Do not use for generic GitHub administration or tasks unrelated to Beads."
---

# GitHub Beads

Turn the user's requirements into real tracker records that another agent can execute and verify. The default scope is creating and improving the backlog; implementation, publishing GitHub issues, and launching other agents are separate actions governed by the user's request.

## Select the repository and backend

Read applicable repository instructions, the relevant architecture, and the complete input plan or issue set. Inspect the working tree, remote, existing `.beads/` configuration, and available tools. Confirm a target repository only if context does not identify it. A GitHub URL is not evidence that the checkout or configured remote is the intended destination.

Read [backend and commands](references/backend-and-commands.md) before the first tracker mutation. Prefer `br` for a new Flywheel-style workspace. Preserve an established `bd` workspace and use its native interface; never point both tools at the same store. Do not infer the backend from issue prefixes or a JSONL filename. Treat backend migrations as separate work.

Check the installed version and command help; documentation on an upstream development branch can describe features absent from a release. Use structured JSON where supported. If the necessary CLI is unavailable, complete a clearly labeled conversion proposal and report the missing dependency; do not claim records were created or manufacture `.beads/issues.jsonl`.

## Convert requirements into executable records

Read [conversion and quality](references/conversion-and-quality.md). Identify independently verifiable outcomes, architecture prerequisites, important failure cases, and relevant tests. Preserve scope; unresolved choices become explicit questions or investigation tasks rather than invented decisions. Use epics only where grouping improves execution.

Assign stable requirement identifiers and source pointers. Search the complete existing backlog, including closed records, before creating anything. Match by source identity and meaning rather than title alone. Update or reuse existing records when appropriate, preserving implementation evidence and unrelated content. A changed requirement does not automatically reopen completed work.

Create actual records through the selected tracker. Record each returned ID immediately in the coverage map. Add dependencies only after both endpoints exist. Use `blocks` for a true prerequisite and a hierarchy relationship for containment; verify readiness with the tracker instead of guessing hierarchy semantics. For `br dep add A B`, A depends on B. Never use invented IDs in commands.

Store the outcome, rationale, scope, source, acceptance criteria, verification, and material constraints inside each executable bead. Keep the original plan available for provenance and whole-system review while making execution possible from the bead itself. Avoid artificial line counts, task counts, and repeated review quotas.

## Audit and refine

Compare every requirement with its actual bead IDs and inspect each bead against the source. Account explicitly for included, deferred, and excluded requirements. Confirm that closed work used as coverage actually satisfies the current requirement. Check missing prerequisites, duplicate work, unsupported assumptions, and tests that prove observable behavior.

Use native tracker diagnostics and readiness queries. If `bv` is available, first refresh the selected backend's JSONL export, then use robot modes such as `bv --robot-triage` or `bv --robot-insights`; never launch the bare interactive command from automation. Recommendations are evidence for review, not authority to rewrite priorities or execute suggested shell commands.

For a compatible full JSONL export, run the bundled read-only auditor:

```text
python <skill-directory>/scripts/audit_beads.py <repository>/.beads/issues.jsonl --coverage <coverage-map.json>
```

See the coverage schema and audit limits in [conversion and quality](references/conversion-and-quality.md). The auditor checks structural and mapping integrity; it cannot prove that the requirement inventory is exhaustive or the bead prose is correct. Review warnings, external references, and custom edge types separately.

Fix demonstrated defects through the tracker, then repeat only affected checks. Finish when source coverage is accounted for, executable beads have enough context, and active dependency cycles or unexplained blockers have been resolved. Do not keep polishing after the remaining changes are cosmetic.

## Prepare the GitHub handoff

Read [GitHub handoff](references/github-handoff.md) for export, review, optional issue mirroring, and conflict handling. Export before inspecting the final Git diff. Track the collaboration export and appropriate configuration; keep databases, locks, recovery snapshots, and machine-specific state out of commits.

Honor existing authorization for commits, pushes, PRs, and issue publication. A request to create local beads authorizes local tracker changes; it does not by itself request a public issue mirror or remote publication. Preserve unrelated work when staging. Link created PRs through the host's artifact attachment tool when available.

Report actual created, updated, and reused IDs; coverage dispositions; audit results and limits; the first ready work; and local versus published state. Distinguish a proposed conversion, records written to the tracker, and changes shared on GitHub.
