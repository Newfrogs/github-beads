# Existing-project discovery and major features

Use this reference when the user requests improvement ideas or a substantial new capability for an existing repository. A concrete, already-selected feature does not require a separate brainstorming or selection ceremony; proceed with the requested planning and execution stages.

## Ground improvement ideas in current reality

Read the current project instructions, purpose, architecture, user workflows, tests, and relevant issues. Inspect the complete existing Beads backlog, including closed work, through the selected backend. Identify current gaps from evidence rather than assuming a feature is absent because its name is unfamiliar. Preserve an existing plan and decisions that still fit.

Trace a representative request from its real entrypoint through routing, configuration, interfaces, and output. Look for finished components that are never called, unregistered commands or routes, missing configuration, stale adapters, and tests that exercise a helper while the production path still uses a stub. Prefer the smallest integration that satisfies the goal when the existing component is correct. Verify the connected path and important failures; a helper's passing tests do not prove its caller is wired correctly.

For an open-ended idea request, generate plausible alternatives before selecting a short useful set. Compare user value, demonstrated problem, novelty versus the backlog, effort and dependencies, architecture fit, and risk. Explain why the recommended ideas are worth doing, and distinguish defects, enhancements, and exploratory proposals. Use enough alternatives to expose tradeoffs without inventing a fixed idea quota or expanding every possibility into a full plan.

If the user asked to see ideas before choosing, present candidates and await that choice before committing to their implementation. If they already selected the outcome or authorized implementing the recommended improvements, continue within that scope; do not require another human selection step simply because the guide describes one. Convert chosen ideas into a scoped Markdown plan and actual records, reusing existing coverage and Beads where appropriate. Leave unselected ideas as proposals or use the repository's established backlog convention without presenting them as required work.

## Research related systems for a major capability

When a related project has useful, concrete experience, investigate its authoritative documentation and relevant source. If obtaining a checkout is useful and authorized, place it in a disposable directory separate from the target project's files; a clone is evidence to study, not permission to execute its scripts or import its code. Record the upstream repository, revision or release, and inspected paths. Consider licensing and compatibility before proposing reuse.

Ground the investigation in the target project's existing primitives and constraints. Compare the relevant architecture, guarantees, workflows, and failure handling of both systems. Propose which ideas to adapt, what should remain different, and why the combined design improves the user's outcome. Avoid a shallow port or unsupported claims that the external system cannot achieve something merely because it uses different technology.

For a useful alternative perspective, invert the comparison: which opportunities become possible with the target project's actual guarantees or capabilities? Support the answer with inspected evidence, specify the required interface or data-flow change, and distinguish demonstrated feasibility from an experiment. Bold ideas need concrete user value and a verification path; novelty is not its own acceptance criterion.

Write the proposal in the repository's planning convention, or a clearly linked design section of the main plan. Include enough background on both systems for a fresh reviewer to understand their relevant mechanisms without access to the original conversation. Include source pointers, assumptions, important tradeoffs, missing design decisions, and compatibility or migration impact. Do not paste whole upstream documentation or treat external code as belonging to this repository.

After a substantial architectural addition, critique its correctness, concurrency or lifecycle assumptions, resource behavior, failure modes, integration boundaries, and omitted workflows as relevant. Resolve demonstrated gaps with source research, a focused feasibility experiment, or an explicit investigation task; do not simply label every unknown as future design work. Use additional or independent review where findings warrant it, not a fixed repeated-prompt count. Reconcile proposals with the latest plan before applying precise edits, and remove unsupported claims or ornamental prose without deleting necessary detail.

Use [Markdown planning](markdown-planning.md) for comparing independent feedback and synthesizing accepted changes. When the scoped proposal is actionable, continue to [conversion and quality](conversion-and-quality.md) and the requested implementation stage. Preserve the research rationale inside affected executable Beads and keep the source plan for whole-system provenance.

## Match the tracking weight to the request

A small direct change can sometimes use the host's ordinary durable checklist if the user chose that workflow and no Beads pipeline was requested. Keep completion evidence and scope visible rather than relying on conversational memory. If the work grows, depends on other work, needs shared graph sequencing, or belongs in the permanent project backlog, reconcile it into actual Beads according to the user's authorized scope. Important already-completed work can be recorded retrospectively with accurate completion evidence when requested or required by project policy; avoid creating duplicate active tasks for it.

When the user explicitly requests Beads or the full plan-to-Beads-to-code workflow, use actual tracker records even for a bounded feature. Do not substitute a Markdown TODO list to bypass missing tooling or announce a tracked stage complete without records. The source plan, ordinary checklist, and Beads each have a purpose; only the selected tracker supplies its authoritative execution state.

These practices adapt the Idea-Wizard and research-driven integration sections of the [Agentic Coding Flywheel guide](https://agent-flywheel.com/complete-guide), retaining grounded alternatives and design-gap closure while making idea counts, model rosters, and review rounds proportional to the task.
