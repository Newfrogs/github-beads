---
name: github-beads
license: MIT
description: "Write full Markdown plans, convert requirements into dependency-aware Beads, and implement and verify the code in a repository. Use for idea-to-plan, plan-to-beads, end-to-end feature delivery, backlog reconciliation, and resuming Beads implementation in Claude Code or Codex. Prefer Beads Rust (br) for new workspaces; preserve an existing bd backend. Do not use for generic GitHub administration."
---

# GitHub Beads

Carry the user's requested outcome through a written plan, actual tracker records, and verified code. Use the same workflow in Claude Code and Codex; adapt invocation syntax and available tools to the client. Keep the plan, Beads collaboration artifacts, and implementation in the target repository unless the user specifies a different arrangement.

## Choose the requested stages

| User intent | Work to perform |
| --- | --- |
| Write or refine a plan; planning only | Save a complete Markdown plan and report open decisions. Stop at the plan. |
| Convert a supplied plan to Beads; backlog work only | Read the source, create or reconcile actual records, and audit coverage. Stop before coding. |
| Plan, create Beads, and implement; build a feature using Beads | Write or refine the plan, create or reconcile records, audit, then implement and verify the included scope. |
| Implement or resume an existing Beads plan | Inspect the current plan, tracker, and code; continue unfinished authorized work without recreating completed tasks. |

Infer the mode from the user's concrete request and existing session authorization. If the desired outcome is genuinely unclear, ask one focused question while continuing useful inspection. A full pipeline request authorizes ordinary planning, task creation, and code edits; do not introduce a new approval checkpoint between these stages. Honor an explicit plan-only request or requested review checkpoint. Commits, pushes, PRs, issue mirroring, deployment, and destructive operations follow the user's scope and the host's permissions.

## Select the repository and backend

Read applicable repository instructions, the relevant architecture, and the complete idea, input plan, or issue set. Inspect the working tree, remote, existing `.beads/` configuration, available tools, and project test commands. Preserve unrelated edits. Confirm a target repository only if context does not identify it. A GitHub URL is not evidence that the checkout or configured remote is the intended destination. Planning-only work does not require a tracker or initialize one.

Read [backend and commands](references/backend-and-commands.md) before the first tracker mutation. Prefer `br` for a new Flywheel-style workspace. Preserve an established `bd` workspace and use its native interface; never point both tools at the same store. Do not infer the backend from issue prefixes or a JSONL filename. Treat backend migrations as separate work.

Check the installed version and command help; documentation on an upstream development branch can describe features absent from a release. Use structured JSON where supported. If a requested tracker stage cannot run, finish the useful Markdown plan and a clearly labeled conversion proposal, report the missing dependency, and keep the dependent tracked workflow incomplete. Do not claim records were created, manufacture `.beads/issues.jsonl`, or silently replace the requested pipeline with untracked coding. An explicitly authorized coding fallback can proceed with its limitations recorded.

## Write or refine the Markdown plan

Read [Markdown planning](references/markdown-planning.md) and adapt the bundled [plan template](assets/plan-template.md). Follow existing repository conventions; otherwise save `plans/<feature-slug>.md`. Research and inspect enough to make the design implementable, citing actual sources and labeling assumptions and proposed paths. Preserve the user's supplied plan and settled decisions when refining it.

Include the goal and exclusions, current behavior and architecture, stable requirement IDs with observable acceptance criteria, proposed design and important failure cases, interfaces and data changes where relevant, ordered implementation outcomes, verification, material risks, and unresolved decisions. A full plan is complete for the requested scope, not padded to a prescribed length. Resolve routine choices from evidence; ask about choices that materially affect the requested behavior while progressing independent work.

Check the plan against the source in both directions. Save it before task conversion and retain its path and revision or hash as provenance. For the full pipeline, continue directly into Beads creation once the scoped design is actionable. Keep genuine unresolved dependencies visible and continue independent work; never invent the user's answer.

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

Fix demonstrated defects through the tracker, then repeat only affected checks. The conversion is ready when source coverage is accounted for, executable beads have enough context, and active dependency cycles or unexplained blockers have been resolved. In a full workflow, continue into implementation of eligible work. Do not keep polishing after the remaining changes are cosmetic.

## Implement and verify the code

When coding is in scope, read [implementation and resume](references/implementation-and-resume.md). Query the selected backend's ready set, inspect the full bead and its source requirements, and claim eligible work through the native tracker. Respect existing claims and project transition rules. Re-read current state before changing it; a stale receipt is not authority to overwrite another agent's progress.

Implement the observable outcome in the target codebase, including relevant documentation and meaningful checks. Record actual changed paths and acceptance evidence in the bead using supported notes or comments. Close it only after its acceptance criteria pass; a commit, a green structural audit, or a successful mock alone does not prove the feature is done. Failed or unavailable checks remain explicit incomplete verification.

Repeat for the authorized included scope, refreshing readiness as prerequisites finish. On new findings, update the affected plan decisions, coverage, and actual records without expanding scope silently. If no work is ready, diagnose missing prerequisites or external blockers and continue independent eligible work instead of polling unchanged state. Preserve blocked work and report the precise remaining condition.

On resume, reconcile saved artifacts with the current plan, tracker, working tree, and test evidence. Reuse work that still meets the requirement; do not recreate the graph or reopen completed tasks merely because the session changed. Keep a concise repository-local execution receipt alongside the plan when the work spans sessions.

## Prepare the GitHub handoff

Read [GitHub handoff](references/github-handoff.md) for export, review, optional issue mirroring, and conflict handling. Export before inspecting the final Git diff. Track the collaboration export and appropriate configuration; keep databases, locks, recovery snapshots, and machine-specific state out of commits.

Honor existing authorization for commits, pushes, PRs, and issue publication. A request to create local beads authorizes local tracker changes; it does not by itself request a public issue mirror or remote publication. Preserve unrelated work when staging. Link created PRs through the host's artifact attachment tool when available.

Before reporting a full pipeline complete, compare the implementation with every included requirement, run the appropriate final project checks, inspect the tracker and diff, and export the collaboration state. Unresolved included requirements, open or blocked included implementation tasks, and missing acceptance evidence prevent a full completion claim. Explicitly deferred or excluded work stays visible in the result.

Report the saved plan and coverage paths, actual created/updated/reused/completed bead IDs, changed code, acceptance evidence and test results, unresolved decisions or blockers, and local versus published state. Distinguish a proposed conversion, records written to the tracker, implemented behavior, and changes shared on GitHub. Do not report a code stage for a plan-only or Beads-only request.
