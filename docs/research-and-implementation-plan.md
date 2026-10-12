# GitHub Beads Skill Research and Implementation Plan

Prepared 12 October 2026 for a reusable skill across GitHub repositories.

Create a portable `github-beads` skill that writes full Markdown implementation plans, translates their requirements into executable Beads records, checks coverage and dependency integrity, implements and verifies the included code, and prepares repository changes for review. Use Beads Rust (`br`) for new Flywheel-style workspaces, respect an existing original Beads (`bd`) setup, and make remote issue mirroring an explicit option. Version 0.1 focused on plan-to-Beads conversion; version 0.2 extends the shared Claude Code and Codex workflow through planning, implementation, and resume.

## Version 0.2 workflow extension

The canonical skill now routes four intents: planning only, Beads only, a complete planning-to-code workflow, and implementation or resume of existing work. A full workflow request authorizes its ordinary local stages without another approval checkpoint after the plan or graph is ready. Narrower requests retain their stopping point. Publication, deployment, and destructive actions remain governed by the user's request and client permissions.

The new Markdown planning reference and bundled template cover the outcome, boundaries, repository evidence, stable requirement identifiers, observable acceptance, architecture and design, important interfaces and failure cases, implementation sequence, verification, risks, and decision provenance. Plans follow repository conventions or live at `plans/<feature-slug>.md`. Beads hold execution status and evidence; a coverage map links actual IDs back to the saved source. Planning and code use the same repository by default.

The implementation reference specifies native readiness and claims, code changes tied to task acceptance, appropriate verification, recorded evidence before closure, and reconciliation of findings into the plan and affected tasks. A resume receipt preserves paths, actual IDs, checks, blockers, and publication state. Resuming requires fresh tracker and code inspection rather than rebuilding the graph or treating an old receipt as authoritative.

Both clients load the same portable package. Claude's plugin wrapper is versioned 0.2.0, and Codex's interface prompt requests the complete workflow. There is no separate client-specific implementation logic. Missing tracker executables leave the Beads stage explicitly incomplete; a structural audit or a written plan cannot stand in for delivered behavior.

## Research findings

### The method worth preserving

The Flywheel guide separates system planning from conversion into a dependency graph. Its central requirement is that executable beads retain the context, rationale, acceptance criteria, and verification obligations needed by a fresh agent. It also emphasizes reviewing the conversion against the source and creating actual tracker records rather than stopping at a Markdown task list. These principles inform the proposed skill. Its prescribed review counts, plan lengths, and swarm sizes are not acceptance requirements for this package. [Complete Flywheel guide](https://agent-flywheel.com/complete-guide).

For this skill, the practical quality gate is observable: requirements have explicit dispositions, tasks have usable completion contracts, and the graph has no unresolved active structural cycles. An exhaustive plan does not require hundreds of beads; a small change can produce a small graph. Review continues while it finds material defects.

### Select the backend explicitly

| Component | Verified role | Design decision |
| --- | --- | --- |
| Beads Rust `br` | Local SQLite tracker with JSONL collaboration export | Default for new workspaces following the guide |
| Original Beads `bd` | Current implementation uses Dolt and native database synchronization | Retain in repositories already using it |
| Beads Viewer `bv` | Reads compatible exports and offers graph analysis through robot commands | Optional analysis aid |
| Git and GitHub | Review and distribution of repository artifacts | Prepare local changes first; publish when requested |
| GitHub Issues | Optional online presentation of selected work | Define mirror identity and ownership before publication |

The distinction between `br` and `bd` is architectural, not an interchangeable executable name. In particular, current `bd` documentation identifies JSONL as an interchange/viewer export rather than its canonical storage or backup. [Beads Rust](https://github.com/Dicklesworthstone/beads_rust), [original Beads](https://github.com/gastownhall/beads).

On the research date, the latest release links resolved to `br v0.7.4` and `bv v0.25.2`. These are reference points for a future pilot; the package's automated checks do not exercise these tools. Development-branch documentation can describe additional behavior; the installed executable's help must determine which options the skill uses. [br release](https://github.com/Dicklesworthstone/beads_rust/releases/tag/v0.7.4), [bv release](https://github.com/Dicklesworthstone/beads_viewer/releases/tag/v0.25.2).

### Resolve documentation drift

There are concrete inconsistencies that a reusable instruction pack must handle. The guide shows a title flag where a positional title is a more dependable command form. The bundled `br` skill calls synchronization exclusively explicit and says the tool never runs Git, while current documentation describes default JSONL auto-flush/auto-import and explicitly invoked reporting commands that inspect Git. The reliable invariant is that tracker synchronization does not itself commit, pull, or push. A final export check remains useful. [Bundled br skill](https://github.com/Dicklesworthstone/beads_rust/blob/main/.claude/skills/br/SKILL.md), [current CLI reference](https://github.com/Dicklesworthstone/beads_rust/blob/main/docs/CLI_REFERENCE.md), [VCS integration](https://github.com/Dicklesworthstone/beads_rust/blob/main/docs/VCS_INTEGRATION.md).

The implementation therefore checks versions and help, treats upstream examples as adaptable, and distinguishes observation from mutation. It also avoids asserting that a command is strictly read-only when automatic import can refresh the store.

### Use structured interfaces and literal text

Agent-facing outputs have explicit schemas and pagination conventions. A conversion needs the complete relevant backlog, including closed work, before deciding whether a requirement needs a new record. Parsers should inspect returned shape and completeness rather than assuming every list is a bare array. [Agent integration](https://github.com/Dicklesworthstone/beads_rust/blob/main/docs/AGENT_INTEGRATION.md).

Rich descriptions are important enough to preserve verbatim. Current CLI implementation provides `update --description-file`; `create --file` instead refers to bulk import. The skill checks installed support and otherwise recommends a subprocess argument array with shell interpretation disabled. This prevents Markdown backticks, dollar signs, quotations, and newlines from becoming shell instructions. [CLI implementation](https://github.com/Dicklesworthstone/beads_rust/blob/main/src/cli/mod.rs).

### Treat graph structure and readiness separately

The upstream model serializes typed dependencies with source and target IDs and identifies several blocking relationship categories. The auditor uses these categories for structural cycle checks, including containment and conditional relationships. It deliberately does not reproduce the tracker's workflow policy or decide whether conditional gates are satisfied. Native readiness queries remain necessary. [Issue and dependency model](https://github.com/Dicklesworthstone/beads_rust/blob/main/src/model/mod.rs).

`bv` offers robot triage, planning, and graph insights and warns agents against launching its bare interactive interface. Its analysis can help identify bottlenecks, but a recommended task or suggested command still needs interpretation in the selected repository. [Beads Viewer](https://github.com/Dicklesworthstone/beads_viewer).

### GitHub distribution and issue visibility

GitHub documents repository skill discovery under `.github/skills`, `.claude/skills`, and `.agents/skills`. The portable instruction package can therefore be shared through a repository; Codex-specific interface metadata is kept separate in `agents/openai.yaml`. [GitHub agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).

GitHub CLI supports file-backed issue and PR bodies, and its current issue-creation interface includes dependency flags. Online dependencies are useful for human review, but the local tracker still needs its own execution graph. The first version prepares optional mirrors without implementing automatic two-way synchronization. [Issue creation](https://cli.github.com/manual/gh_issue_create), [PR creation](https://cli.github.com/manual/gh_pr_create).

## Scope and operating modes

The skill should recognize requests to turn a plan, specification, or selected GitHub issues into Beads; improve an existing conversion; reconcile changed requirements; and prepare those changes for review. Generic GitHub administration should not activate it.

| Mode | Main input | Result |
| --- | --- | --- |
| Convert | Repository and source requirements | Actual beads, typed dependencies, and a coverage report |
| Refine | Existing beads and source | Targeted corrections and an audit receipt |
| Reconcile | Changed source plus current backlog | Reused, updated, or newly created records with preserved history |
| Handoff | Completed local conversion | Export and reviewable repository changes; publication if requested |
| Mirror | Explicit selection and publication request | Linked GitHub issues with stable identity |

A plan-only request produces a conversion proposal and says so. A creation request with a missing tracker completes independent preparation but reports that real records could not be written. A request to create a backlog does not automatically launch implementation agents.

## Proposed architecture

Keep one concise entrypoint and load supporting references only when needed.

```text
skills/github-beads/
  SKILL.md
  agents/openai.yaml
  references/
    backend-and-commands.md
    conversion-and-quality.md
    github-handoff.md
  scripts/
    audit_beads.py
tests/
  test_audit_beads.py
docs/
  research-and-implementation-plan.md
```

The installed package contains the skill directory. Tests and this research document remain development and review artifacts.

`SKILL.md` handles repository selection, backend routing, conversion, quality gates, and evidence-based reporting. The backend reference explains interface differences and failure handling. The conversion reference defines useful bead content and the coverage map. The handoff reference covers Git review, optional mirroring, and synchronization conflicts.

The auditor uses Python's standard library and reads a complete exported JSONL file. It opens no database, executes no tracker or Git commands, and changes no inputs. Its receipt includes input hashes so a later reviewer can identify the audited snapshots.

## Conversion design

### Establish the complete input

Read the applicable repository instructions, source plan, relevant implementation, and current tracker configuration. A remote URL alone is insufficient to choose a destination. Determine whether requirements are new, already satisfied, changed, deferred, or explicitly excluded.

Give source requirements stable identifiers. A file section or issue URL plus requirement ID provides useful identity across sessions. Store that identity inside the bead and in the coverage report.

Missing architectural decisions become explicit questions or investigation tasks. Do not fill gaps by inventing user requirements, performance targets, or unavailable interfaces.

### Reconcile before creating

Search current and closed records and inspect plausible matches. An exact title is only a candidate. Match source identity, intended outcome, and completion evidence. Reuse completed work when it satisfies the current requirement; otherwise create the actual missing delta or reopen only when appropriate.

Creation can return an uncertain outcome after a timeout. Before retrying, inspect the tracker for the source identity and recover the returned record if it exists. Stop an ambiguous mutation rather than minting duplicates. Keep successful IDs as the conversion proceeds.

### Decompose into useful outcomes

Create leaves that can be implemented and verified coherently. Split work when prerequisites, ownership, or acceptance evidence differ. Use epics for meaningful grouping rather than adding hierarchy mechanically.

Each leaf should carry its outcome, why it matters, scope, relevant interfaces and constraints, acceptance criteria, verification, prerequisites, and source. Include failure handling where it changes correct behavior. Avoid empty template headings and task bodies that simply say “see the plan.”

Creation and dependency mutation go through the chosen tracker. A coverage report is supplementary provenance, not an alternative status database.

### Wire prerequisites deliberately

Create endpoints first, then add typed relationships using actual IDs. Prerequisites should express a concrete execution need, not a vague association. Containment groups work; readiness must be checked under the selected backend's policy.

A useful hypothetical parser sequence is contract → implementation → cross-feature verification, with a separate documentation update dependent only on the contract where possible. This example illustrates the decision rule; it does not imply real records were created.

### Review source and graph

Review in both directions: every source requirement has a disposition, and every new record has a source or a justified prerequisite. Validate that acceptance criteria cover the source's material behaviors. Check that proposed tests demonstrate outcomes rather than repeat implementation details.

The coverage map records `included`, `deferred`, or `out_of_scope`. Included and deferred entries point to real non-tombstoned records; deferred and excluded entries include reasons. Deferral must also be represented in tracker policy.

Stop refinement when material coverage gaps and graph defects are resolved and leaf context is executable. Restart affected checks only after a change or newly discovered concern.

## Auditor design and limits

| Check | Behavior |
| --- | --- |
| Duplicate record IDs | Error |
| Empty basic task content or invalid numeric priority | Error |
| Missing local dependency endpoint | Error |
| Duplicate typed edge or mismatched owner | Error |
| Active structural cycle | Error |
| Cycle whose entire component is terminal | Warning |
| Similar normalized titles | Warning requiring semantic review |
| External dependency | Explicitly reported for separate verification |
| Custom relationship type | Warning because blocking semantics are unknown |
| Missing coverage reference or required disposition reason | Error |
| No coverage map supplied | Coverage marked `not_checked` |

Cycle detection uses an iterative strongly connected component algorithm so deep task chains do not hit Python's recursion limit. Distinct relationship types between the same endpoints are preserved.

The result cannot prove that the source inventory includes every requirement, that prose is accurate, that implementation exists, or that backend-specific gates are satisfied. Empty or filtered exports require special attention. These limits stay visible in both instructions and audit receipts; a clean structural result is not a completion certificate.

## Implementation and rollout plan

### Phase 1 Build the portable package

Create the entrypoint, interface metadata, references, auditor, and meaningful tests. Validate frontmatter and routing. Keep automatic discovery available for relevant Beads requests.

Acceptance: complete references, no unfinished scaffold, a valid skill package, and working read-only audit behavior. The source package implements this phase.

### Phase 2 Make the skill discoverable

Install the validated package in the target client's supported personal or repository skills directory, preserving any existing unrelated skills. Keep `skills/github-beads` as the canonical distribution source. Exclude generated bytecode. The repository README provides installation instructions.

Acceptance: installed contents match the reviewed package and the client discovers the skill. Package installation supplies instructions and the helper, not tracker executables.

### Phase 3 Exercise a real tracker in an isolated pilot

Use a disposable repository with a checksum-verified `br` release. Cover a modest source with independent tasks, a prerequisite, an epic, one deferred requirement, and an excluded requirement. Use installed help rather than assuming development-branch options.

Acceptance:
- Real IDs and stored bodies match the intended source.
- Export can be inspected with both the native tracker and auditor.
- A second conversion reuses records rather than duplicating them.
- A changed requirement updates only affected work.
- Readiness matches intended sequencing.
- Unicode, newlines, quotes, and shell metacharacters remain literal.

Version 0.2 includes a scoped live pilot with checksum-verified `br v0.7.4` on Windows. It exercises a saved Markdown plan, real records and descriptions, a prerequisite edge and native readiness, claims, implementation, acceptance evidence, closure, export, and the auditor. Broader cases remain: epic policy, deferral and exclusions in a live store, repeated conversion and changed requirements, and concurrent recovery. The automated CI suite still uses exported-data fixtures rather than installing a tracker.

### Phase 4 Verify existing backend compatibility

Run a separate pilot in a repository configured for current `bd`. Confirm the skill routes to its native commands and preserves its database and synchronization model.

Acceptance: no `br` mutation of the `bd` store, no unintended migration, and no treatment of JSONL as a Dolt backup. This is a separate compatibility gate, not a claim made by the fixture tests.

### Phase 5 Validate GitHub review

Select an actual destination repository and its conventions. Review the ignore rules and export, commit the appropriate files, and create a PR if publication is requested. For skill distribution, choose a supported skill directory and one canonical package.

Acceptance: only intended files are staged, local machine state is excluded, the PR describes actual changes and checks, and its URL is verified. This skill repository includes an MIT license for its original files; referenced projects retain their own terms. Remote review of an actual backlog conversion remains a separate integration gate.

### Phase 6 Add optional issue mirroring

Start with a small explicit selection. Define which fields the mirror owns, use a stable bead-ID marker, verify exact existing identity before creating, and save the resulting URL in the bead.

Acceptance: reruns do not duplicate issues; ambiguous timeout outcomes stop publication; human-authored content is preserved. Automatic two-way sync, deletions, project-board automation, and bulk issue publication need separately implemented policies.

### Phase 7 Maintain against real use

Refresh command assumptions after a relevant version change or demonstrated failure. Add narrow regression cases based on observed defects. Do not accumulate mandatory tools or review rounds merely because the broader Flywheel stack contains them.

Acceptance: changes have an identifiable behavior benefit and existing invariants still pass.

## Validation results and remaining gates

The package passes the bundled skill validator. All 15 automated auditor tests pass. They cover valid DAGs, duplicate IDs, missing endpoints, exact cycle components, blocking categories, nonblocking relationships, closed cycles, typed-edge identity, external and custom references, coverage gaps, tombstones, missing manifests, malformed fields, Unicode, CLI exit codes, and preservation of input bytes. A 3,000-record chain exercises deep traversal.

The version 0.2 workflow was also exercised in disposable projects:

- **Planning-only scope probe:** saved a 76-line Markdown plan with five requirements; original code bytes stayed unchanged, and no tracker or implementation artifacts were created.
- **Full workflow pilot:** an agent loaded the canonical skill and saved a plan with eight requirements, created actual `br` tasks `e2e-mjq` and `e2e-epu` with one prerequisite edge, implemented an ASCII slug function and CLI, and recorded acceptance evidence before closing both tasks. All 13 project tests passed, including the two pre-existing tests. The requested CLI returned `hello-world` with exit 0; an empty-slug input returned exit 2 with a clear stderr message. The existing function and test file were preserved.
- **Native tracker checks:** the ready and blocked sets were empty after completion, cycle detection found no cycles, and native diagnostics reported a healthy store. The full export's structural and eight-requirement mapping audit passed. These are actual tracker operations, not fabricated JSONL records.
- **Package checks:** Codex's skill validator and Claude Code's strict plugin and marketplace validators passed. The same ten-file canonical skill package supplies both clients.

The Windows pilot encountered a path-resolution failure in the restricted environment before initialization; no database override variables were set. An explicit pilot-local database path and normal permission escalation kept subsequent operations in the disposable repository. The backend guidance now requires confirming the resolved database and export before mutation. This does not establish an upstream root cause for that initial failure.

These checks validate the helper, package, planning scope, and one real `br` planning-to-code workflow. They do not exercise live `bd` or `bv`, GitHub issue mirroring, concurrent claim races, deployment, or complete model-driven sessions in both external clients. Client discovery and installation are separate packaging checks. The broader pilots and actual backlog review gates remain as listed above. The public repository includes runnable auditor examples and GitHub Actions checks on Windows and Linux.

## Principal decisions and risks

| Decision or risk | Handling |
| --- | --- |
| Backend ambiguity | Inspect project instructions and configuration; choose one native tool |
| Upstream documentation drift | Verify installed help and record versions |
| Duplicate creation on retry | Recover by stable source identity before another mutation |
| Requirement silently omitted | Compare source and coverage inventory in both directions |
| Lost description detail | Literal file or argument-array input and saved-body inspection |
| Conditional or custom graph semantics | Use native readiness and review auditor warnings |
| Divergent database and export edits | Preserve both sources; diagnose guarded sync rather than force overwrite |
| Publishing beyond the requested scope | Keep local creation, PR publication, and issue mirroring distinct |
| Excessive fragmentation or review | Size by outcomes and stop after material defects are resolved |
| Client-specific packaging | Keep portable instructions separate from UI metadata |

The main design choice is to preserve a traceable path from written intent through actual records to verified behavior. GitHub provides sharing and review, while optional tooling can enrich the workflow when a repository needs it.
