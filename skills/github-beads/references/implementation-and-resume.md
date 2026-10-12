# Implementation and resume

Use this workflow for both Codex and Claude Code. The client supplies repository access and tool execution; the plan, coverage map, actual Beads records, code, and evidence carry continuity between sessions.

## Respect the requested mode

- **Plan only:** save the full Markdown plan and report material decisions or unresolved questions. Do not mutate the tracker or implement code.
- **Beads only:** reconcile an existing plan into actual tracker records and audit the conversion. Do not implement code.
- **Implement:** execute the requested existing Beads scope, reconciling its source plan and coverage before starting.
- **End to end:** create or update the Markdown plan, create or reconcile actual Beads, then implement and verify the included scope. A request for this full workflow already authorizes its local stages; do not stop for an additional approval merely because the plan or backlog is now ready.

Honor narrower user limits and repository policies. Resolve routine implementation choices from evidence. Ask for a material missing decision when it changes the requested result, and continue independent work that does not depend on the answer. Keep commits, pushes, PRs, issue mirroring, deployment, and messages governed by the user's request and host permissions.

## Establish the execution state

Read the saved plan, its requirement inventory and coverage map, current repository instructions, and relevant architecture. Inspect `git status --short` and the actual tracker through the selected backend. Reconcile plan changes with [conversion and quality](conversion-and-quality.md) before executing affected work. A receipt, exported snapshot, or Markdown checklist does not override current tracker state.

Use the existing checkout by default. Preserve user edits and unrelated changes, including a dirty working tree; do not reset, stash, discard, or replace them merely to obtain a clean baseline. If concurrent work makes isolation useful, use a worktree only according to the client's and repository's policies, and carry forward the correct source state. Keep the plan, tracker, and code associated with the same intended repository. Do not create a separate planning repository by default.

Confirm installed command contracts using [backend and commands](backend-and-commands.md). Keep an existing `bd` store on `bd`; use `br` for a new store. If the required tracker is unavailable, preserve the Markdown plan and conversion proposal and report the dependency. Do not invent records or silently claim the Beads stage is complete. Continue unrelated authorized work, but do not present it as execution of nonexistent beads.

## Select and claim actual work

Query the native ready set for the included scope. Priorities, prerequisites, existing assignments, and repository policy determine the next task; viewer recommendations are advisory. Inspect already claimed or in-progress work owned by this session when resuming, because ready queries may exclude it. Do not take another worker's claim without resolving ownership.

Immediately before claiming, refresh the candidate's complete record and readiness. Read its description, acceptance criteria, comments, constraints, prerequisite evidence, and linked source. Use a supported atomic claim and inspect the response; stop that claim if another worker acquired it or a gate refused it. If the installed backend lacks atomic claims, follow the project's supported ownership convention and re-read the result; do not pretend a status write provides atomic exclusion.

Representative commands, after checking installed help:

```text
br ready --json
br show ACTUAL_ID --json
br update ACTUAL_ID --claim --json
```

For an established `bd` repository, use the corresponding native interface:

```text
bd ready --json
bd show ACTUAL_ID --json
bd update ACTUAL_ID --claim --json
```

Use IDs returned by the actual tracker and pass the ID explicitly to every mutation. Current primary references document these claim forms; released versions and project transition policies can differ. Re-read concurrent edits and use a supported revision guard when changing accumulated text. [br CLI](https://github.com/Dicklesworthstone/beads_rust/blob/main/docs/CLI_REFERENCE.md), [bd CLI](https://github.com/gastownhall/beads/blob/main/docs/CLI_REFERENCE.md).

## Implement and verify each outcome

Make the code or artifact deliver the bead's observable outcome in the real repository. Inspect existing interfaces and conventions before editing; use working code and concrete behavior to resolve assumptions. Keep changes within the claimed scope while including the prerequisites needed to make them work. Parallelize independent tasks only when ownership and file boundaries are clear; delegation and extra reviewers are optional tools, not completion requirements.

Run verification appropriate to the changed behavior and the bead's acceptance criteria. This may include focused tests, negative cases, integration checks, a build, or inspection of a low-impact document or configuration change. Run repository-required checks. Do not add tests that only repeat implementation details or enforce a fixed test count. Broaden verification when failures, wider impact, or unresolved risk justify it; do not keep rerunning checks after an unchanged result.

Inspect the final diff for the task. Record actual changed paths, the checks run and their results, and evidence for its acceptance criteria in the bead using supported comments or append operations. Distinguish passing checks from failures, unrun checks, unavailable tools, and pre-existing failures. Preserve prior evidence and human-authored context.

Close only when the task's acceptance criteria and required checks are satisfied. A passing structural audit, a created stub, delegated work, or a generated plan is insufficient evidence of implementation. Use an explicit ID and a factual reason through the installed native command, for example:

```text
br close ACTUAL_ID --reason "Implemented acceptance criteria; evidence recorded in task comments" --json
bd close ACTUAL_ID --reason "Implemented acceptance criteria; evidence recorded in task comments" --json
```

Run only the command for the selected backend, and check help first. Never use `--force` to bypass dependencies, capacity, ownership, or workflow gates. Read back the result and refresh readiness before selecting the next task. Close an epic only when its own completion contract is met, including any integration criteria beyond child completion. The syntax and close behavior are described in the [br CLI](https://github.com/Dicklesworthstone/beads_rust/blob/main/docs/CLI_REFERENCE.md) and [bd CLI](https://github.com/gastownhall/beads/blob/main/docs/CLI_REFERENCE.md).

## Handle discoveries and blockers

When implementation exposes a missing requirement or prerequisite, update the source Markdown plan and coverage map, then reconcile affected beads and edges before executing the changed scope. Record the decision and evidence. Keep stable requirement IDs where the meaning is unchanged; add IDs for new requirements. Do not expand the user's goal merely to improve adjacent code.

Preserve satisfied closed work. A wording change or a resumed session does not require reopening it. A demonstrated regression or changed acceptance criterion may justify reopening under repository policy or creating a linked follow-up; state which criterion no longer holds and preserve the earlier completion evidence.

For a real blocker, record its cause, the affected acceptance criterion, and the event or decision that would unblock it. Use supported dependency, gate, deferred, or blocked states according to the repository's policy; a receipt alone cannot prevent a task from appearing ready. Resolve causes that are within scope, then continue other ready work. If nothing can proceed, report the precise blocker and required input or external change. Do not blindly poll an unchanged queue, retry a lock indefinitely, or close blocked work as complete. Scheduled watching requires a user request and a supported host mechanism.

## Reconcile the delivered result

When the included execution scope is finished, review the saved plan against actual implementation in both directions: every included requirement has acceptance evidence, and each delivered change serves the intended scope. Refresh tracker state and confirm no required task remains open, claimed, blocked, or unexpectedly deferred. Report deferred and excluded requirements with their reasons rather than counting them as delivered.

Run the cross-feature acceptance checks specified by the plan and required repository checks. Use native diagnostics and a refreshed compatible export with the bundled auditor when useful; structural coverage is not proof of behavior. Update coverage and delivery evidence to reflect observed results. Export and hand off through [GitHub handoff](github-handoff.md) when sharing was requested, preserving the selected backend's native synchronization model.

Completion requires the observable user goal and its required checks, not just an empty ready list or closed tracker records. If acceptance remains blocked, report partial delivery precisely and leave truthful task state for the next session. Distinguish implemented locally, committed, pushed, PR created, merged, and deployed; claim only observed states requested by the user.

## Leave and consume a resume receipt

For interrupted, partial, or completed work, keep a concise receipt beside the repository's planning artifacts, or update its existing handoff document. Record useful facts rather than a second task system:

- Source plan and coverage paths and the source revision or hash when known.
- Selected backend and intended repository; actual completed, claimed, and blocked bead IDs.
- Changed code paths and whether changes are local or published, with verified commit or PR references when applicable.
- Commands or checks actually run, results, acceptance evidence, and remaining verification.
- Concrete blocker causes, important decisions, and the next action or ready candidates observed at the time.

On resume, re-read the receipt, inspect the working tree, reload the saved plan and map, and query the actual tracker. Recover an existing claim owned by this session before choosing new work. Verify that prior completion evidence still matches the current requirement; do not automatically rerun unchanged checks or reopen satisfied work. Recover uncertain mutation results by inspecting actual records before retrying. Reconcile stale paths, IDs, ownership, and external state, then continue from the first unfinished authorized outcome.
