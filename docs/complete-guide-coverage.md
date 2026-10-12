# Complete-guide coverage for GitHub Beads 0.3.0

The [Agent Flywheel complete guide](https://agent-flywheel.com/complete-guide)
was inspected in full on 12 October 2026, including its operator library,
learning loop, prompt families, deployment caveats, and final setup material.
The private inspection snapshot contained 805 extracted text lines; those ranges
below identify the reviewed snapshot, not stable public page anchors. The source
page and its code/prompts are not bundled or relicensed here.

This independently written implementation accounts for every substantive guide
practice. **Incorporated/extended** means usable guidance is implemented;
**optional** means it depends on available tools and the requested outcome;
**adapted** preserves the purpose while fitting repository/client/user scope;
**excluded as a mandate** identifies an example, quota, unsupported guarantee,
or environmental assumption that should not become a universal skill rule.
Coverage does not mean every external tool was installed or exercised.

The implementation is one portable skill for Claude Code and Codex:

- [Entrypoint](../skills/github-beads/SKILL.md)
- [Planning](../skills/github-beads/references/markdown-planning.md) and [existing projects](../skills/github-beads/references/existing-projects.md)
- [Conversion and quality](../skills/github-beads/references/conversion-and-quality.md)
- [Coordination](../skills/github-beads/references/swarm-coordination.md) and [implementation/resume](../skills/github-beads/references/implementation-and-resume.md)
- [Toolchain and learning](../skills/github-beads/references/toolchain-and-learning.md)
- [Backend commands](../skills/github-beads/references/backend-and-commands.md) and [GitHub handoff](../skills/github-beads/references/github-handoff.md)
- [Original workflow prompts](../skills/github-beads/assets/workflow-prompts.md), [plan template](../skills/github-beads/assets/plan-template.md), [operating contract](../skills/github-beads/assets/agent-instructions-template.md), and [feedback template](../skills/github-beads/assets/agent-feedback-template.md)

The [implementation plan](../plans/guide-complete-skill.md), [granular TODO](../plans/guide-complete-todo.md), [actual requirement mapping](../plans/guide-complete-coverage.json), and [validation receipt](../plans/guide-complete-receipt.md) connect this coverage to real executed work. All package paths in the tables refer to the canonical `skills/github-beads` directory unless fully qualified.

## Planning, translation, refinement, and existing projects

| Guide subsection / practice and capture lines | Disposition | Package location and rationale |
| --- | --- | --- |
| Complete workflow: intent → written plan → Beads → implementation → hardening; 6–31 | Existing, strengthened | `SKILL.md` stage selection and execution; `references/markdown-planning.md` explicit real transition. Intermediate artifacts are not completion of downstream stages. |
| Compounding artifacts preserve intent and make later cycles more informed; 9–18 | Existing | Plan provenance, stable requirement IDs, actual Beads evidence, resume receipt; no simulated productivity percentages adopted. |
| Explain idea, goals, user interactions, purpose before design; 19–20, 46–49 | Extended | `references/markdown-planning.md` foundation/user journeys; `assets/plan-template.md` user-workflows section. |
| Independent alternative plans and synthesis; 21–22 | Extended | Optional independent perspectives, common input context, per-proposal comparison and accepted/adapted/rejected/deferred disposition. |
| Refine until material issues settle; 23, 25, 28 | Modified | Evidence-driven refinement and readiness criteria in planning/conversion references; repeat only when findings or changes justify it. |
| Specific time allocation, 3,000–6,000 lines, 200–500 tasks, fixed review/swarm counts; 23–30, 35–45, 125–126, 181 | Not adopted as mandates | Examples are not appropriate universal quotas. Scope, acceptance evidence, actual dependencies, and actionable design determine useful depth. |
| CASS project output, speed, line counts, and ship guarantees; 29–31 | Not generalized | Source anecdotes and illustrative exhibits are not measured evidence about this skill's performance. |
| Glossary: plan / bead / code reasoning spaces; 32–33, 56–70 | Existing, clarified | `SKILL.md` modes; plan stores design, native records store executable memory, code/tests prove behavior. Plan is retained rather than forbidden after conversion. |
| AGENTS reload, fungible agents, compaction continuity, human swarm tending; 26–27, 33 | Delegated | Covered by implementation/coordination owner; not added to the planning mode as required swarm overhead. |
| Front-load whole-system reasoning while representation is manageable; 35–45, 50 | Extended | Read complete input, settle choices that affect downstream work, include architecture/contracts/workflows; no required planning percentage or context-size guarantee. |
| Discover requirements rather than assume omniscience; 51–55 | Extended | User journeys expose omitted outcomes; external-system research is an optional grounded method for major capabilities. |
| Context horizon/rework cost illustrations and 1x/5x/25x multipliers; 38–40, 58–68 | Not generalized | Illustrative charts are not benchmarks or completion gates. Their qualitative lesson is reflected in early design decisions. |
| Foundation bundle: stack, architecture, instructions, current guidance; 73–77 | Extended and scoped | `references/markdown-planning.md` foundation section; template input evidence. Existing instructions and stack are inspected; no automatic unrelated configuration rewrites. |
| Copy a known-good AGENTS and refresh project content/guides; 75–76 | Modified | Preserve valid shared rules, deliberately adapt project-specific paths/rules, verify version-sensitive guidance. Copying or creating instructions happens only when project bootstrap scope warrants it. |
| Dated provider/model lineup, reasoning settings, preferred framework versions and language choices; 79–81 | Modified / not fixed | Use user's/installed tools and established stack. Research concrete capabilities for an undecided stack; do not hard-code dated model rankings or unrelated technologies. |
| Notes-app example: upload, failure review, search/filter, permissions, operator flows, e2e; 82–90 | Generalized into workflow guidance | Plan template covers success, progress, failures, recovery, permission boundaries, and operator workflows where relevant; domain-specific example not imposed on every project. |
| Multi-model initial independent designs, best-of-all-worlds prompt; 91–98 | Extended | `references/markdown-planning.md` synthesis: shared background, compare individual strengths/tradeoffs, integrate compatible ideas into current file. No obligation to use four paid providers. |
| Integrate synthesis diffs in place and critically classify revisions; 99–104 | Extended | Precise edits against current file; accept/adapt/reject/defer with reasons; preserve intent and confirm each accepted change appears in the integrated plan. |
| Synthesis studio percentages; 105–110 | Not generalized | No simulation quality scores adopted. |
| Fresh conversation refinement, rationale and git-style changes; 111–120 | Extended and proportional | Focused review request, precise edits, fresh perspective where anchoring matters, evidence-driven repeat criteria. No mandatory fresh session or four/five rounds. |
| Overshoot mismatch hunt / assert 80 missed errors; 121–124 | Replaced | Use exhaustive source/feedback-to-section accounting with factual findings. Inventing a quota or lying about known defects encourages fabricated issues and unnecessary review. |
| When to stop plan refinement; 127 | Extended | Move when included design is actionable and remaining questions concern execution structure, sequencing, verification, and local context. Independent settled slices can proceed. |
| Explicit plan-to-Beads transition to avoid stalled conversion; 129–130 | Extended | Save the plan then make native tracker mutations for an authorized Beads/full-pipeline stage, or report the precise incomplete stage. |
| Plan separate from Beads; epics/tasks/subtasks with graph; 131–132 | Existing, corrected where needed | Planning and task translation are distinct. Existing selected backend and native storage/export remain authoritative; do not assume every `.beads` store is JSONL-native. |
| Full conversion prompt, rich future-self context, only real tracker changes; 133–138 | Existing, strengthened | `references/conversion-and-quality.md` execution-relevant intent; WHAT/WHY/HOW audit; no pseudo-Beads Markdown. Selected existing `bd` remains supported rather than forcing `br` migration. |
| Read complete named source plan for existing project; 137 | Extended | Complete input includes background, decisions, workflows, failure handling, and verification; refinement preserves existing IDs and source pointers. |
| Thin vs rich bead exhibit: outcomes, admin hooks, recovery, permissions, test fixtures; 139–165 | Generalized | Bead body and context sufficiency require important interfaces, permissions, recovery, and meaningful verification; illustrative IDs/counts and invented domain requirements not copied. |
| Executable memory, long descriptions/embedded Markdown, complete coverage; 166–174 | Existing, extended | Records contain enough local context; length itself is not quality. Source remains available for provenance and changing requirements. Bidirectional coverage and semantic review remain required. |
| Comprehensive unit/e2e with detailed logging; 173, 177–180, 193 | Modified and extended | Appropriate test layers, fixtures, negative cases, expected outcomes, and useful diagnostics. Respect sensitive-data rules; no mandatory e2e suite for documentation or trivial changes. |
| CLI quick reference, priorities, types, SQLite/JSONL storage; 183–186 | Existing / delegated technical verification | `references/backend-and-commands.md` documents verified contracts and policy-aware priorities. This owner added no new tool command forms; guide's `--title` and blanket storage assumptions are not adopted. |
| Polishing prompt reloads instructions and preserves functionality; 188–196 | Extended | Current instructions for fresh reviewer; change actual records by demonstrated defects and preserve included functionality unless scope is explicitly changed. |
| Duplicate checks, WHAT/WHY/HOW, empty descriptions, dependency fixes; 201 | Extended | Explicit WHAT/WHY/HOW and canonical dedup workflow in `references/conversion-and-quality.md`. |
| Cross-reference both plan→records and records→plan including closed work; 202 | Existing | Semantic bidirectional coverage, evidence for closed records, complete backlog search. |
| Convergence metrics, review phases, weighted score thresholds; 197–207 | Replaced | Actionable content, accounted coverage, adequate verification, truthful blockers, graph integrity. Output size or resemblance cannot certify readiness. |
| Oscillation, expansion, low-quality plateau red flags; 207 | Extended | Resolve disputed acceptance/decision from evidence, separate optional scope, investigate missing facts rather than repeat cosmetic edits. |
| Fresh-eyes prompts: reread instructions/README/architecture, use tracker/viewer; 208–217 | Extended and proportional | Independent/fresh-context review for consequential conversions or evidence of anchoring; reviewer gets complete source/current records/diagnostics. No mandatory final model pass. |
| Dedicated dedup after large creation batches; 218–221 | Extended | Choose canonical survivor by acceptance/context/test/dependency correctness; transfer missing content, rewire incoming/outgoing links, redirect map, preserve history, verify readiness. |
| Existing-project Idea-Wizard grounding in instructions/backlog; 222–224 | New reference | `references/existing-projects.md`, linked from planning. Complete open/closed backlog and actual code evidence prevent duplicate ideas. |
| Divergent idea generation, winnowing, next-best ideas/novelty; 225–226, 230–232 | Modified | Generate useful alternatives and compare value, novelty, feasibility, effort/dependencies, architecture fit, and risk. No universal 30→5→15 count. |
| Human selects ideas, then create and refine records; 227–229 | Scoped | Await selection only when user requested selection. Existing authorization/selected outcome proceeds directly; no new interstage approval ceremony. |
| Bounded ad-hoc durable TODO alternative; 233–237 | Scoped | Ordinary checklist only when user chose that workflow and did not request Beads; growth/shared graph/permanent work goes to actual records. No silent fallback for requested pipeline. |
| Retroactively record meaningful completed ad-hoc work; 237 | Scoped | Accurate retrospective evidence when requested or project policy requires; do not create duplicate active tasks or fabricate historic completion. |
| Major feature: investigate external mature project using existing context; 238–246 | New reference | Inspect authoritative source/docs, cite revision/paths, study in a separate disposable directory if useful and authorized, preserve target-specific primitives and license/compatibility constraints. |
| Iterative deepening and ambitious architecture; 247–251 | Modified | Ask for concrete user value, interface changes, feasibility, and verification; novelty and forceful adjectives are not quality criteria. |
| Invert comparison using target's unique guarantees; 252–256 | New reference | Evidence-based opportunities from actual target capabilities; no unsupported claims that upstream cannot support them. |
| Repeated 5x blunder hunts after every expansion; 257–262 | Modified | Critique correctness/lifecycle/resource/failure/boundaries after meaningful design additions; further review based on substantive findings and risk, not exact prompt quotas. |
| Close concrete design gaps with source research; 263–269 | New reference | Resolve by authoritative evidence, focused feasibility experiment, or explicit gated investigation; do not leave honest gaps as vague future work. |
| Self-contained backgrounds for cross-model review; 270–275 | New reference | Proposal explains relevant mechanisms of both systems, constraints, sources, and tradeoffs so reviewers do not need prior conversation. |
| Independent feedback in diff format; synthesize/apply/de-slopify; 276–284 | Extended | Precise current-file revisions and per-suggestion critical disposition; remove unsupported/ornamental wording while retaining necessary detail. Review/model quotas omitted. |
| External proposal feeds ordinary Beads/implementation; 285 | Existing, reinforced | Link grounded proposal into main plan, preserve rationale in executable records, continue authorized standard pipeline rather than ending at research prose. |
| Coordination triangle, mail, reservations/macros, worktree/main policy, bv robot interface and graph metrics; 286–330 | Delegated, outside this owner's edit boundary | The following coordination section maps these practices. Existing native readiness and advisory viewer treatment remain intact; this owner does not impose shared-main/no-worktree policy. |

## Coordination, launch, execution, and hardening

| Guide section/practice | Disposition and reason | Artifact |
| --- | --- | --- |
| Coordination triangle: durable tasks, communication, graph routing | Adapted: distinct roles with single-agent fallback; no mandatory stack | `references/swarm-coordination.md` |
| Agent Mail advisory leases, inbox, identity and macros | Optional: discovered connected service and installed contract; current Rust recommended for new installs | `references/swarm-coordination.md` |
| Reservations before edits | Incorporated: narrow paths, explicit IDs/TTL, inspect grants and conflicts, renew/release lifecycle | `references/swarm-coordination.md` |
| Expired/crashed-agent locks | Adapted: expiry alone does not prove inactivity; inspect ownership/diff/thread, policy-governed handoff | `references/swarm-coordination.md` |
| Broadcast versus point-to-point | Adapted: target affected participants only under human/host messaging authorization | `references/swarm-coordination.md` |
| Graph compass: PageRank, bridges, critical path, parallel tracks | Optional: refreshed export, robot output, actual native readiness/ownership authority | `references/swarm-coordination.md` |
| Viewer-generated claim commands | Adapted: source-authority/route/snapshot checks; no blind shell execution or invented route | `references/swarm-coordination.md` |
| Bead IDs as thread/reservation/commit anchors | Incorporated: actual IDs throughout, commits only when authorized | `references/swarm-coordination.md`; `assets/agent-instructions-template.md` |
| AGENTS.md operating manual | Incorporated: concrete template merges existing client instructions and project checks | `assets/agent-instructions-template.md` |
| Post-compaction reset | Incorporated: reload instructions/source/actual claim, bounded receipt recovery | `references/swarm-coordination.md`; `references/implementation-and-resume.md` |
| Human override, no destructive Git, no overwrite of other work | Adapted: established instruction hierarchy/authorization, guards, preserve concurrent edits | `references/swarm-coordination.md`; `assets/agent-instructions-template.md` |
| Blanket no deletions, always main, manual-only changes | Excluded as universal policy: honor real repo/client policy and authorized edits instead | `references/swarm-coordination.md`; `assets/agent-instructions-template.md` |
| Single-branch model, no worktrees | Adapted: shared-checkout Git serialization plus policy-based worktrees and task-state integration | `references/swarm-coordination.md` |
| Automatic pull/edit/commit/push/release loop | Adapted: explicit publication scope, intentional staging, reviewed revision, lease lifecycle | `references/swarm-coordination.md`; `references/implementation-and-resume.md` |
| Pre-commit reservation guards and DCG | Optional: preserve existing guards, diagnose refusals; no silent installation or bypass | `references/swarm-coordination.md` |
| Fungible/generalist agents, crash recovery | Adapted: durable context and explicit ownership transfer; skills/specialists when useful | `references/swarm-coordination.md` |
| Generic marching-order prompts | Incorporated: bounded kickoff packet supplies actual paths, ID, acceptance, integration scope | `assets/agent-instructions-template.md`; `references/swarm-coordination.md` |
| Security at every layer | Incorporated execution portion: real auth/trust-boundary/sensitive-data tests, limits of scanners | `references/implementation-and-resume.md` |
| NTM, tmux, WezTerm, terminal operator UI | Optional: supported existing orchestrator, no fleet/toolchain installation requirement | `references/swarm-coordination.md` |
| ACFS queue planner/startup packets/simulation | Optional: version-help-gated existing capability, launch based on capacity and ready frontier | `references/swarm-coordination.md` |
| First operating loop | Incorporated: context → identify → route/claim → reserve → relevant thread → code/evidence | `references/swarm-coordination.md`; `references/implementation-and-resume.md` |
| Dated model/vendor ratios and open-bead staffing table | Excluded as rules: capability/access/coordination cost determines scaling | `references/swarm-coordination.md` |
| Thundering herd | Incorporated: distinct packets and observation-driven staggered admission | `references/swarm-coordination.md` |
| Fixed 30-second spacing, terminal double-submit workaround | Excluded: environment-specific; no delays or repeated input without evidence | `references/swarm-coordination.md` |
| Human tending/monitoring cadence | Adapted: decision-changing signals, natural boundaries, no perpetual polling | `references/swarm-coordination.md` |
| CAAM account switching / rate limits | Excluded as automatic action: report limits, preserve account/authorization boundaries | `references/swarm-coordination.md` |
| Stuck swarm diagnosis | Incorporated: duplicate claims, conflicts, abandoned tasks, compaction, capacity, drift | `references/swarm-coordination.md` |
| Busy work versus strategic result | Incorporated: compare observable goal with remaining graph, revise missing requirements | `references/swarm-coordination.md`; `references/implementation-and-resume.md` |
| Fresh-eyes per-bead review | Adapted: purpose/flow/edge-case review, related pattern search, repeat for changed evidence only | `references/implementation-and-resume.md` |
| Test coverage, E2E logs, unit/integration boundaries | Adapted: meaningful real journeys, justified mocks/fixtures, log evidence; no arbitrary test volume | `references/implementation-and-resume.md` |
| Compiler/lint/build checks | Incorporated: task and repository required checks; do not transplant Rust/Bun/Go commands blindly | `references/implementation-and-resume.md` |
| UBS before every commit/full scans | Optional: correct scan scope, inspect findings/partial failures, retain repo required gates | `references/implementation-and-resume.md` |
| RCH offloading | Optional: existing approved service, direct argv, source/artifact identity, fail-open caveat | `references/implementation-and-resume.md` |
| UI/UX scrutiny and polish | Adapted: inspect actual flow, desktop/mobile/accessibility/states; select useful in-scope enhancements | `references/implementation-and-resume.md` |
| Documentation de-slopification | Incorporated: direct prose review, factual claims and clear terminology | `references/implementation-and-resume.md` |
| Deep cross-agent reviews/random exploration | Adapted: distinct interface/flow hypotheses, relevant surrounding code, no unbounded randomness | `references/implementation-and-resume.md` |
| Scheduled repeated reviews / consecutive clean-round quotas | Excluded: new findings/changes/risk/required gates justify repetition | `references/implementation-and-resume.md` |
| Organized commits | Adapted: serialized authorized Git work and intentional coherent staging; no collect-all agent edits | `references/swarm-coordination.md`; `references/implementation-and-resume.md` |
| README revision | Adapted: actual current behavior and compatibility, preserve useful content, no length inflation | `references/implementation-and-resume.md` |
| Catch-all oversight | Adapted: source/risk-linked omission check with evidence stopping condition | `references/implementation-and-resume.md` |
| Landing the plane | Adapted: actual follow-up tasks/state/checks/sync/leases/receipt; requested publication verified remotely | `references/implementation-and-resume.md` |
| Always push / stage all .beads / blind pull-rebase | Excluded as blanket commands: user authorization, backend-native handoff, private-state excludes and concurrency policy | `references/implementation-and-resume.md` |
| Final integrated status gate | Incorporated: refreshed full export and `--require-closed --coverage` check plus separate actual acceptance evidence | `references/implementation-and-resume.md` |

## Primary contract checks and guide drift

- Python Agent Mail README is now a maintenance notice directing new installations to Rust. New references preserve existing deployments rather than alias/migrate trackers.
- Rust `file_reservation_paths` can return partial/empty grants and conflicts. Historical Python behavior granted contested leases. Read both fields and never infer filesystem exclusivity.
- Rust `macro_file_reservation_cycle(auto_release=true)` acquires/releases inside one call; it does not protect future edit commands.
- Current `bv --robot-next` has actionable/source-authority facts and origin-bound actions, while triage recommendations may not be claimable. Live native tracker refresh remains required.
- RCH can fail open locally by default; remote-only policy requires supported configured mode and observed remote execution evidence.
- UBS is supplementary static analysis and may return partial-run errors; it cannot establish semantic/security completeness or justify infinite cleanup.

Primary links are attached to the relevant canonical references. No upstream source code or prompt text was copied; the workflow is independently written and safely adapted.

## Toolchain, learning, operators, invariants, and setup

Resources:

- **TL:** `skills/github-beads/references/toolchain-and-learning.md`.
- **FB:** `skills/github-beads/assets/agent-feedback-template.md`.
- **MP:** `skills/github-beads/references/markdown-planning.md`.
- **CQ:** `skills/github-beads/references/conversion-and-quality.md`.
- **EP:** `skills/github-beads/references/existing-projects.md`.
- **IR:** `skills/github-beads/references/implementation-and-resume.md`.
- **GH:** `skills/github-beads/references/github-handoff.md`.
- **BC:** `skills/github-beads/references/backend-and-commands.md`.
- **SC:** `skills/github-beads/references/swarm-coordination.md`.
- **WP:** `skills/github-beads/assets/workflow-prompts.md` (original operator packets).
- **SK:** `skills/github-beads/SKILL.md` (root integrates conditional routing).

## Toolchain, onboarding, and operating patterns

| Guide lines | Substantive practice | Disposition and implementation |
| --- | --- | --- |
| 553–555 | Manifest-backed complete toolchain; 28-module snapshot; free/open-source description | Adapted in TL discovery. Enumerates every guide tool by capability; reads current upstream manifest and individual licensing/version requirements rather than freezing counts or making a blanket license claim. |
| 555 | `br`, `bv` | Native tracker plus optional graph advice: BC/CQ/SK, listed in TL. Existing `bd` remains supported rather than migrated. |
| 555 | Agent Mail (`am`) and `ntm` | Optional shared coordination/session capabilities: TL discovery/portability and SC execution. MCP and CLI availability differ. |
| 555 | `ubs`, `dcg`, `slb` | Relevant scanning and installed command guards: TL onboarding/environment boundaries and IR verification. Guards do not authorize bypasses. |
| 555 | `cass`, `cm`, `ee`, `fsfs` | Optional scoped history, procedural memory, and local retrieval: TL retrieval/memory/privacy. No automatic global indexing or shared memory setup. |
| 555 | `apr`, `brenner` | Optional plan/refinement/research tooling: TL discovery and MP/EP research. Choose by available capability, not mandatory dependency. |
| 555 | `ms`, `jfp` | Optional skill/prompt discovery: TL discovery and refinement/distribution. Preserve provenance, license, applicability, and client compatibility. |
| 555 | `asb`, `casr`, `pcr` / `claude-post-compact-reminder`, `pfr` | Optional backup/resumption/compaction adapters: TL discovery/portability. Configuration/history can contain secrets; current instructions and native state remain authoritative. |
| 555 | `pi`, `caam` | Optional agent/account environment configuration: TL discovery/capacity. No implicit credential access, switching, or provider installation. |
| 555 | `rch`, `dsr`, `ru` | Optional remote compilation/release/repository-fleet tooling: TL discovery/capacity. Remote transfer, releases, and fleet mutations require their actual scope. |
| 555 | `pt`, `sysmoni`, `sbh` | Optional process/resource/disk tooling: TL discovery/capacity. Inspection does not imply permission to kill or delete. |
| 555 | `fmd` | Optional presentation/rendering: TL discovery. Does not replace source review or become a delivery prerequisite. |
| 556 | CLI versus MCP surfaces; generated installation dependency closure | TL version/interface discovery and environment setup. Primary ACFS resolver contract verified; no installer executed. |
| 557–560 | Spawn -> instructions -> registration -> task priority/claim -> reservation -> implement/test/scan -> publish -> history/memory | Adapted across IR/GH/TL. Stages depend on actual availability and user scope; publication/history ingestion are not unconditional completion steps. |
| 561–565 | Ubuntu user, zsh, workspace, passwordless sudo, tmux prefix; `acfs newproj` scaffolding | Environment-specific examples, addressed by TL setup boundaries. Preserve the existing host/repository; full machine setup or new-project bootstrap only when requested. |
| 566–572 | Core trio first; progressively add scanner, guard, history, then memory | TL onboarding. Existing trio retained; a solo worker can begin with the native tracker and project checks. No forced tool installation. |
| 573 | Avoid hasty plans/single-pass conversion; fixed three-polish minimum | MP/CQ substantive source/quality review retained. Fixed pass quotas replaced with demonstrated defects, coverage, and convergence; no artificial delay before authorized implementation. |
| 574–575 | Project-size, agent-count, and completion-time examples | TL capacity states anecdotes are neither prerequisites nor delivery guarantees; MP/CQ do not enforce line/task counts. |
| 576–577 | Generate wider ideas, then filter and deepen selected promising ideas; 30/5/15 funnel | EP useful alternatives, novelty/value/effort, and scoped selection. Exact counts are illustrative rather than a universal quota. |
| 578 | Parallelize bulk bead creation by independent subsets | SC ownership boundaries and CQ actual-ID/source reconciliation. Never assume a returned ID, concurrent-safe mutation, or a complete graph before native readback. |
| 579 | Stagger agent starts to avoid contention | SC admission/capacity/staggering and TL observed workload. Useful under measured shared-service contention; no required 30–60 second sleep for every launch. |
| 580 | One Git operator for coherent shared changes | SC shared integration and GH coordinated handoff when needed. No permanent special-agent dependency; commits/pushes stay governed by authorization. |
| 581–583 | Avoid single-pass bead quality and skipped plan-to-bead validation; fixed 4–5 passes | CQ source/graph checks and proportional convergence. Retain validation; discard unconditional pass counts and unsupported claims that all first drafts fail. |
| 584 | Avoid communication purgatory | IR act on eligible work, bounded coordination, factual blockers; TL capacity removes redundant review/overlap. |
| 585 | Short file-reservation lifetimes; release after use | SC Agent Mail lease lifecycle. Reservation lifecycle tied to actual ownership/work; release does not depend on an unauthorized commit. |
| 586 | Reload AGENTS.md after compaction | TL portability and IR resume. Reload applicable instructions/artifacts, then inspect actual state. Optional PCR hook is one client adapter. |
| 587–588 | Foundation artifacts, current best-practices guides, Markdown source, ACFS bootstrap/doctor, NTM palette, tool skills | MP foundation and TL onboarding/interface/setup. Reuse relevant maintained resources; no wholesale copying or compulsory VPS tooling. |
| 589–592, 595 | Skills as operational know-how distinct from tool capabilities; bundled tool skills | TL agent-first interfaces and tested distribution. SK remains discoverable/reusable; version compatibility and actual use matter. Universal “every tool” bundling claims are not assumed. |
| 593–594 | Free/open-source and paid prompt/skill offerings; active development/refunds | TL optional prompt discovery, licensing and current terms. External subscription purchase/support/refund claims are not execution requirements; no copied prices or implied subscription. |
| 596–598 | Avoid provider lock-in through common task/communication primitives | TL portable substrate/client adapters, BC backend continuity, IR current-state recovery. Does not claim every client's hooks/interfaces/authentication are identical. |
| 599–601 | Foundation, plan, translation, bead, launch, ship gates; return to a failed phase | MP readiness; CQ coverage/context/dependencies; IR claim/concurrency/code acceptance; GH truthful publication state; TL feedback. Gate relevant prerequisites by mode and availability, not a mandatory installed fleet. |
| 602–606 | Full-permission aliases; large model memory flags; claim DCG makes bypass viable | Unsafe/environment-specific assumptions adapted by TL setup boundaries. Do not adopt bypass/sudo aliases or infer guard completeness; primary DCG limitations verified. No model/provider flags frozen into a portable skill. |
| 607–609 | Open-source tool cost versus provider/server costs; starter capacity; operator account/token snapshot | TL measured cost/capacity. Separate real costs; inspect current official prices/terms when a purchase is requested. Snapshot is not a minimum or recommendation; no account-limit evasion. |

## Learning, memory, and improvement

| Guide lines | Substantive practice | Disposition and implementation |
| --- | --- | --- |
| 611–618 | Compounding planning, execution, tools, and memory; extraordinary speed claims | TL feedback cycle retains reuse of tested evidence and reusable artifacts. Claimed speed/productivity/automatic exponential improvement is not treated as a guarantee. |
| 619–620 | Capture session evidence, reflect patterns, retrieve relevant prior rules, improve checks/guidance between projects | TL retrieval/memory/refinement. Corrects distinction: CASS indexes existing supported histories, not guaranteed recording of every session. CM reflection may invoke a provider and write rules; manual, scoped receipts are a valid fallback. |
| 621–625 | Structured feedback after real tool use; helpfulness, signal/noise, strengths, errors, ratings, recommendations, suggested changes | TL feedback with FB artifact. Optional dimensions/ratings must cite observed use; unknown measurement is distinct from poor performance. Feedback transmission needs actual messaging/publication authorization. |
| 626–627 | Diverse agents/projects; feature opinions are unreliable until implemented and used | TL gather distinct cases/counterexamples and forward-test hypotheses. Diversity is evidence breadth, not proof; no fictional ratings/acceptance. |
| 628–631 | Episodic evidence -> working diary -> procedural playbook | TL memory layer separation. Retain provenance and useful scope; do not confuse generated summary with raw evidence or reusable rule. |
| 632 | Ninety-day half-life, harmful multiplier, maturity stages | TL configurable decay/maturity and observed harmful/helpful evidence. Upstream CM confirms these defaults/configuration, but the skill does not hard-code them as proof or universal policy. |
| 633–635 | `cm context`, recall, reflect, helpful/harmful marking; mandatory pre-task ritual | TL relevant bounded authorized retrieval and actual returned rule IDs. No unconditional global context/history read or reflect; inspect installed contract/provider/privacy/budget and continue without optional memory. |
| 636–641 | Mine skill use across sessions; confusion, mistakes, skipped steps, workarounds; fresh rewrite/test; 10-session/3–4-cycle assumptions | TL bounded improvement loop. Smallest evidenced correction, realistic independent test, provenance/limits. Counts and cycles do not replace outcomes or become mandatory quotas. |
| 642–648 | Ritual detection; repeat-count buckets; wildcard/line-number/title-prefix grouping query | TL scoped pattern detection. Deduplicate inherited/copied prompts and separate distinct sessions/outcomes; counts prioritize investigation, not correctness. Inspect actual citation schema; do not assume prompt line positions or globally mine all histories. |
| 649–650 | Layer context: plan intent, task execution, project rules, implementation | MP/CQ/IR/TL portable artifact separation. Keep global/source context available while tasks remain self-contained. |
| 661–663 | Phase time-investment and multi-session examples | TL workload-based capacity and proportional review; no imposed hours, sessions, line counts, or speed promise. |
| 664–668 | Self-contained converged tasks enable execution; human intervention when flow breaks; revisit missing architecture/context | IR/CQ current acceptance and blocker recovery; MP refine affected decisions. Adapt “foregone conclusion” to evidence and real outcomes; not every code discovery implies planning failure. |
| 669–670 | Repeat planning/Beads/implementation for later versions/features | EP feature scale and MP/CQ/IR same authorized pipeline; no requirement to implement all future work in v1. |
| 671–674 | Agent-first robot modes, usable tool blurbs, feedback from actual agent use | TL structured bounded noninteractive interfaces, relevant AGENTS.md guidance, and real caller tests; tool improvement only within scope. |
| 675–679 | Recursive tool/skill improvements from observed sessions | TL learning loop and privacy/data boundaries. Measured improvement rather than automatic “training” or unrequested source/tool edits. |
| 680–685 | Baseline tool/skill, real work, mine history, fresh rewrite, repeat | TL progressive learning, demonstrated fixes, independent realistic forward tests, and stop criteria. Shipping and production use follow actual authorization; controlled pilots are valid verification. |
| 686–694 | Scoped search; inspect clarification, repeated mistakes, workarounds, failures; reusable meta-skill | TL source classification/refinement. A new meta-skill is optional; do not install/generate one for every feature. Clarifying questions can be legitimate missing intent, not automatically bad instructions. |
| 695–707 | Four levels: forms, session mining, generated improvement work, bundled optimized skills | TL starts with feedback; advances only with evidence/need. Ideas remain proposals until authorized; distribution retains privacy/license/version and tested behavior. No automatic tracker expansion or installer mutation. |
| 708–712 | Cross-tool improvement compounding and optimization | TL bounded evidence/capacity; no percentage/exponential guarantee. Improve the reusable artifact that demonstrated need. |
| 713–721 | Elicit specialized knowledge; inspect advanced algorithms; benchmark before/after; retain successful techniques | TL hypothesis/benchmark guidance and EP primary research. Apply only to an observed bottleneck and comparable workload; named algorithms/model confidence are not evidence of benefit. |
| 788–789 | Public prompt library, verbatim prompts, paid offerings and managers | TL discovery/provenance. This implementation uses original instructions, not verbatim prompt reproduction; provider/subscription offers remain optional and time-sensitive. |

## Nine invariants and eight operators

| Guide lines | Invariant or operator | Resource and adaptation |
| --- | --- | --- |
| 651–652 | Invariant1: global decisions in plan space | MP design and foundation. |
| 653 | Invariant2: comprehensive scoped plan before implementation | MP readiness; scope-complete rather than padded or all future features. |
| 654 | Invariant3: distinct plan-to-Beads translation | CQ actual IDs, embedded rationale, complete coverage. |
| 655 | Invariant4: tasks carry executable local context | CQ WHAT/WHY/HOW and native records; original plan retained for provenance/global review. |
| 656 | Invariant5: convergence beyond first drafts | MP/CQ evidenced corrections and stop criteria, no pass quota. |
| 657 | Invariant6: workers replaceable through shared artifacts | IR ownership/state and TL client portability, no special-agent dependency. |
| 658 | Invariant7: continuity through crashes/compaction | IR receipt/current-state reconciliation and TL optional recovery adapters. |
| 659 | Invariant8: learn from session history | TL authorized scoped mining, redaction, tested lessons. |
| 660 | Invariant9: verify/review and reuse feedback beyond implementation | IR acceptance and TL feedback closure; scanner only relevant/available, no scope expansion or compulsory retrospective. |
| 722–731 | Operator1: plan-first expansion | MP clarify workflows/architecture/failure paths/tests before execution. |
| 732–739 | Operator2: competing-plan triangulation | MP independent alternatives, compare assumptions, explicit accepted/rejected feedback, synthesize one plan. Optional when useful; not every task needs several paid models. |
| 740–747 | Operator3: overshoot mismatch hunt | MP/CQ systematic source cross-reference and missing/contradictory evidence. Adapt fabricated defect assertions into exhaustive accountable coverage; do not lie or demand invented findings. |
| 748–755 | Operator4: plan-to-Beads transfer audit | CQ two-way source/record coverage and executable task context; actual edits fix demonstrated gaps. |
| 756–763 | Operator5: convergence polish loop | MP/CQ compare meaningful revisions, affected checks, bounded stopping; no automatic endless fresh sessions. |
| 764–771 | Operator6: fresh-eyes reset | MP fresh independent review when useful, restore instructions/source rather than canned repeat cycles. |
| 772–779 | Operator7: fungible swarm launch | SC eligible owned work, concurrency boundaries/coordination and TL capability/capacity. Stagger only for relevant contention; no forced swarm or permanent overseer. |
| 780–787 | Operator8: feedback-to-infrastructure closure | TL real evidence -> narrow tested reusable lesson, FB validation/provenance. No raw history publication or unauthorized upstream mutation. |

## Failure recovery and setup tail

| Guide lines | Substantive practice | Disposition and implementation |
| --- | --- | --- |
| 790–791 | Missing Agent Mail binary: use another supported interface | TL capability/interface discovery; IR optional shared coordination. Discover authenticated supported MCP/API contracts and project identity, not invented REST routes or credential exposure. |
| 792 | Context exhaustion during polishing: fresh session | MP proportional fresh review and IR/TL current-state resume, no assumed session pass limit. |
| 793 | Duplicates at large task scale | CQ canonical task reconciliation, preserve history/context/edges, actual native updates; no threshold needed before correcting a known duplicate. |
| 794 | Plan revision -> bead creation stalls | MP explicit readiness transition and SK/IR carry authorized full pipeline without a new stage approval. |
| 795–798 | VPS rental/SSH, floating or pinned curl-pipe installer, onboard, newproj, mixed agent spawn | TL explicit separate environment setup; inspect pinned source/dependency plan/integrity/platform and side effects. Existing repository is default; machine, provider, project creation, and swarm launch are not implied by feature work. No dangerous convenience command copied. |
| 799 | Begin with one provider; scale after measured queueing/limits; Rust RCH where available | TL cost/capacity with independent eligible work and authorized remote source/data handling. |
| 800–801 | Personal support promise and motivational claims | Non-operative source rhetoric, excluded from executable skill guarantees; ordinary upstream support channels need separate messaging authorization. |
| 802–805 | Setup wizard CTA and full environment count/validation | Optional external environment pathway in TL; no installer run, account purchase, or fixed tool-count contract. |

WP supplies original reusable request packets for all eight operator families.
TL also distinguishes supporting capabilities from the 28-module guide
inventory: ACFS, existing `bd`, GitHub CLI, project-selected QMD retrieval, and
tmux/WezTerm/Zellij/Ghostty/FrankenTerm/WezTerm Automata. QMD is an additional
available alternative, not a claim that it appears in this guide snapshot.
Primary upstream sources for these alternatives were inspected; installed
interfaces, history capture, collection creation, and resumption were not run.

## Additional implemented gaps found during this work

- The read-only auditor now optionally checks that every record mapped to included scope is exactly closed. It requires a coverage map, preserves ordinary conversion-time audits, and has real CLI/read-only regression tests. Actual acceptance evidence remains a separate requirement.
- Current br 0.7.4 supports a literal full description file during creation; the command reference avoids lossy bulk Markdown imports for individual bodies.
- Native exports can include machine-specific source paths. The handoff guidance now checks export contents as well as ignore rules. This repository cleared its unintended absolute source paths through native updates before publication.
- Git inspection found native `*.db-lock-*` runtime sidecars missing from generated ignores. The repository excludes those observed files and the handoff guidance verifies actual ignore behavior before staging.
- The existing-project workflow explicitly traces real entrypoints and checks finished but unconnected code before proposing replacements.

The guide's repeated-review prescriptions are interpreted through [evidence-before-ceremony](https://github.com/Newfrogs/evidence-before-ceremony): retain checks that resolve meaningful questions, preserve required gates, and move to the next actual outcome once those questions are resolved. Do not substitute a clean status report for integrated behavior or remove controls to obtain a green result.
