# Coordinating multiple agents

Load this reference when more than one agent works on the repository or a handoff crosses sessions. A single agent can use native Beads claims and a resume receipt. Agent Mail, `bv`, a session manager, remote builds, and extra models are optional capabilities; installing this skill does not install or authorize them.

## Establish a shared operating contract

Read the applicable `AGENTS.md`, `CLAUDE.md`, README, source plan, and actual bead before editing. Honor each client's instruction discovery and hierarchy. Merge useful project rules into existing instructions only when needed and authorized; use [the operating-contract template](../assets/agent-instructions-template.md) as a starting point, not an overwrite operation.

Keep the same source requirement and actual bead ID across task status, coordination thread, reservation reason, review receipt, and any authorized commit. Generic kickoff prompts work because concrete scope, decisions, acceptance, and verification live in these artifacts. A replacement agent should recover from them without the previous worker's private memory. After compaction or a confused restart, reload repository instructions and the current task state before continuing.

## Admit useful parallel work

Count independently claimable outcomes and inspect overlapping edit surfaces, host CPU and memory, build queues, available tools, and rate limits. Add another agent only when it can advance a distinct outcome at an acceptable coordination cost. Model choice follows required capabilities and available access; avoid a fixed vendor mix, agent count, or model recommendation that will age out of date.

Use the client's supported delegation/session tools. If an existing ACFS or NTM setup is configured, its current planning/packet tools can help with capacity and bounded startup context; inspect installed help. Do not install a VPS stack, launch terminal fleets, change accounts, or bypass rate limits to satisfy an ordinary feature request. A terminal multiplexer is an operator convenience rather than a prerequisite.

Give each worker a bounded kickoff packet: repository location, instruction paths, source plan and map, candidate bead ID, backend, expected outcome, likely edit surface, material constraints, required checks, and integration responsibility. Launch in response to observed available work: confirm the first worker has claimed a distinct task and obtained a clear edit surface before admitting overlapping workers. Do not inject the same unconstrained prompt into every terminal or rely on fixed delays and repeated Enter presses.

## Route work with the graph

Refresh the selected backend's compatible collaboration export before viewer analysis. Start with native ready work; use `bv --robot-next` for a narrow candidate, `bv --robot-triage` for ranked context, `bv --robot-plan` for independent tracks, and `bv --robot-insights` for a demonstrated bottleneck or cycle question. Inspect installed help and output shape; use only robot modes from automation.

High prerequisite centrality or a bridge between tracks can indicate useful unblock work; it does not override the user's priorities, ownership, or an acceptance gate. Triage and planning may include assigned or otherwise unclaimable work. Current `--robot-next` reports actionable/source-authority facts and an origin-bound action route. Treat that as a snapshot: verify the target repository, backend, actual record and readiness before claiming. Do not execute a returned shell string blindly or invent a command when it reports no safe action. [bv robot interface](https://github.com/Dicklesworthstone/beads_viewer#-agent-quickstart-robot-mode).

## Use Agent Mail when configured and authorized

Beads owns task status and dependencies; Agent Mail owns conversations and advisory edit leases. A task claim and a file reservation are different: claiming a bead does not reserve its files, and reserving files does not assign its bead. Neither a message nor a lease proves implementation or exclusive filesystem enforcement.

Inspect the connected server's tool schema and identity/authentication requirements. Use the established project key so all workers address the same coordination scope; with worktrees, verify the deployment's common-project/product convention rather than assume different absolute paths share leases. Keep server and registration secrets in the client's credential mechanism, outside plans, receipts, code, and public URLs.

For new Agent Mail installations, upstream now directs users to the Rust implementation; preserve an existing configured service and verify its behavior rather than migrate it implicitly. [Current Agent Mail](https://github.com/Dicklesworthstone/mcp_agent_mail_rust), [Python maintenance notice](https://github.com/Dicklesworthstone/mcp_agent_mail).

### Join and communicate

1. Bootstrap with supported `macro_start_session(human_key, program, model, ...)`, or ensure the project and register an identity separately. Retain the actual returned name and project key. Join an existing task thread with `macro_prepare_thread` when available. Do not invent an identity, impersonate another worker, or adopt a retired identity without resolving ownership. [Session macro contracts](https://github.com/Dicklesworthstone/mcp_agent_mail_rust/blob/main/crates/mcp-agent-mail-tools/src/macros.rs).
2. Fetch a bounded inbox with `fetch_inbox(project_key, agent_name, ...)`; inspect relevant bodies and acknowledge requests that require acknowledgment. A read acknowledgment confirms receipt, not agreement or completion. Use supported unread/cursor filters to avoid rereading the same history. Check at join, before decisions affected by others, and natural task boundaries rather than a constant polling loop.
3. When human authorization and host policy permit team messages, send to the specific registered participants affected by a claim, interface decision, blocker, or completion. Use `thread_id=ACTUAL_BEAD_ID`, a subject beginning `[ACTUAL_BEAD_ID]`, and concise context/evidence. Reply in the existing thread and avoid default broadcasts. Contact permissions and successful authentication establish technical access, not authority to message unrelated people or projects. Use a supported contact handshake only within that authorization; do not auto-approve another participant's contact policy. [Messaging contracts](https://github.com/Dicklesworthstone/mcp_agent_mail_rust/blob/main/crates/mcp-agent-mail-tools/src/messaging.rs).

### Reserve the edit surface

Request narrow project-relative paths or globs with `file_reservation_paths`. Supply the actual registered name, a TTL suited to the expected edit window, `exclusive=true` for an exclusive edit intent, and the actual bead ID in `reason`. Inspect the response's granted paths/IDs, expiry, and conflicts before editing. Historical Python behavior could grant contested reservations; current Rust can return partial or empty grants. Success alone is insufficient evidence that the entire edit surface is clear.

For a conflict, inspect the holder and affected paths. Narrow the task boundary, choose independent work, or coordinate a safe handoff. Renew only your own lease while actively working using the supported renewal tool, then release its specific paths or IDs when the edit work ends or ownership transfers. Release calls can cover all of the caller's leases when selectors are omitted; use explicit selectors when other work is active. [Reservation contracts](https://github.com/Dicklesworthstone/mcp_agent_mail_rust/blob/main/crates/mcp-agent-mail-tools/src/reservations.rs).

Lease expiry does not prove that the worker stopped editing. Refresh activity, task ownership and the working diff before reacquiring. Use supported stale-release diagnostics only for a demonstrated abandoned reservation and under repository policy; inspect notification side effects and their messaging authorization before any forced release. Do not force-release an active worker to obtain a preferred task. After a timeout, inspect actual lease state before retrying. Some installed versions support exact-request acquisition idempotency; inspect installed contracts and do not infer that every mutation is idempotent.

`macro_file_reservation_cycle(auto_release=true)` in the checked Rust implementation releases within that tool call; it does not hold a reservation across subsequent coding commands. Use a retained lease and a later explicit release for real editing. Do not install or bypass a reservation guard merely to make a commit pass. [Macro implementation](https://github.com/Dicklesworthstone/mcp_agent_mail_rust/blob/main/crates/mcp-agent-mail-tools/src/macros.rs).

## Protect a shared checkout and integrate worktrees

Follow the repository's actual branch/review policy. The guide's shared-branch approach exposes interface changes immediately, but it does not authorize committing to `main` in every repository. In a shared checkout, preserve other workers' changes, serialize Git index/commit/rebase operations, and stage only reviewed intended paths or hunks. Inspect staged content again before the commit; concurrent edits can invalidate an earlier review. Never stash, reset, revert, or overwrite someone else's work to isolate your own patch.

For worktrees, follow host policy and identify the checkout, branch, tracker store, coordination project, and integration destination in each packet. Do not assume independent tracker clones synchronize themselves or that reservations automatically span worktrees. Keep interface changes visible through actual artifacts and authorized messages. Reconcile task state as well as text conflicts, then verify the integrated behavior: a clean merge can still break an API contract. Optional destructive-command or pre-commit guards supplement these practices; keep existing guards enabled and diagnose refusals instead of bypassing them.

## Diagnose stalls and recover

Use observations that change the next decision, not a fixed monitoring cadence:

| Signal | Inspect | Useful action |
| --- | --- | --- |
| Duplicate candidates or claims | Actual assignments, claim responses, startup packet scopes | Respect the existing owner; route the newcomer to distinct ready work and admit workers more slowly. |
| Conflicting edits or implementations | Reservation grants/conflicts, diff, source contracts, thread decisions | Preserve both edits, resolve interface intent, and narrow or reorder affected beads. |
| Long-lived in-progress bead | Owner activity, receipt, inbox/thread, partial code, failed check or blocker | Determine whether it is actively progressing, blocked, or abandoned; record a blocker or perform an explicit handoff. Age alone does not permit takeover. |
| Confusion after compaction | Current repository instructions and actual bead | Reload bounded context, recover the claim and next unfinished criterion; restart only if the supported host workflow requires it. |
| Saturated builds or rate limits | Queue, CPU/memory, tool access and running checks | Reduce launch pressure, schedule independent work, or use an already authorized build service. Report access limits without changing accounts or evading them. |
| Messages and reviews replace delivery | Unfinished acceptance criteria and the evidence behind progress claims | Stop redundant coordination and execute the next useful authorized action. |
| All planned tasks could finish but the goal would remain unmet | Current product behavior versus source plan and graph | Correct the plan and requirement coverage, reconcile missing work, then resume the corrected frontier. |

For an abandoned worker, recover the actual bead, source and partial changes before transferring ownership. Resolve the claim through the native tracker and the project's handoff policy; refresh and reacquire the necessary leases. Preserve useful code and check results, record the new owner and remaining acceptance work, and continue. Do not automatically reopen closed tasks or steal live claims. Generalist workers can replace one another when the durable task context is sufficient; specialist expertise remains useful when the task actually requires it.

Finish with the implementation and [resume receipt](implementation-and-resume.md#leave-and-consume-a-resume-receipt), plus lease cleanup and an authorized thread update when relevant. A future session must be able to establish what is implemented, what remains, who owns it, and where the evidence lives.
