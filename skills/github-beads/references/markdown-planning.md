# Markdown planning

Use this reference when the user needs an implementation plan, including the planning stage of an end-to-end request. A plan explains the intended behavior and design; actual work status and execution evidence belong in Beads.

## Establish the planning scope

Read the user's request, supplied plans or issues, applicable repository instructions, and the code and tests that implement related behavior. Use the repository's existing planning convention; otherwise save the plan at `plans/<descriptive-slug>.md`. Keep the plan and implementation in the selected project repository. Creating separate planning or coding repositories is a separate user choice.

Preserve the requested mode. A plan-only request ends with a saved plan and its unresolved decisions. A request to plan, create Beads, and implement authorizes proceeding through those stages without a new approval ceremony between them. Ask only for information that materially changes the outcome and cannot be resolved from available evidence; continue independent work while it is pending. Do not assume that implementing code also requests deployment, an issue mirror, or other publication.

For an existing plan, refine it in place where practical. Preserve its intent, useful detail, stable requirement IDs, source links, and recorded decisions. Resolve contradictions using the user's current request and repository evidence; record any scope change explicitly. Avoid replacing an agreed design with a fresh outline merely because its formatting differs from the template.

## Assemble useful foundation context

Before choosing a design, establish the target users and their workflows, why the outcome matters, the existing or user-selected stack, and the architectural constraints. Read `AGENTS.md`, `CLAUDE.md`, the README, and local engineering guides when applicable. Check which rules actually belong to this project. A known-good instruction document can inform a requested project bootstrap, but copying another project's paths, tool names, permissions, or outdated framework advice creates false context. Preserve valid shared rules and adapt project-specific content deliberately; do not rewrite repository instructions just to complete a plan.

For a new project with an undecided stack, compare plausible choices against the requested workflows, deployment environment, maintainability, and concrete library capabilities. Use current primary documentation where version-sensitive decisions matter. For an existing project, prefer its established stack and explain any proposed deviation. Keep a small reusable engineering guide locally only if it will help this project, and cite its sources and versions; a planning request does not require a new collection of best-practice documents.

Work from user journeys, not a list of component names. Spell out representative actions, input validation, intermediate or progress states, visible failures, recovery or retry behavior, permission boundaries, and operator workflows where relevant. Discover omitted requirements while the design is still easy to change, and distinguish necessary implications of the goal from optional product ideas. If the request is feature discovery or a major integration into an existing project, use [existing-project workflows](existing-projects.md).

## Build a plan grounded in the repository

Adapt [the plan template](../assets/plan-template.md) to the work. Remove inapplicable sections and instruction text; expand only sections needed to make implementation and verification possible. Completeness means accounting for the outcome and its important constraints, not filling a prescribed page count.

- **Outcome and boundaries:** Describe the user-visible result, current behavior, success conditions, and explicit exclusions. Separate required work from deferred ideas.
- **Evidence and current architecture:** Name relevant files, interfaces, data flows, tests, and compatibility contracts. Distinguish inspected facts from assumptions and proposed paths. Research external APIs or unstable technical claims when needed; cite authoritative sources and identify the version or access date that matters. Never invent findings, benchmarks, or a claimed repository inspection.
- **Requirements:** Assign stable IDs such as `REQ-001` to independently verifiable outcomes. Give each an observable acceptance condition and a source pointer. Keep an ID when its meaning persists; assign new IDs to new requirements and record replacements or removals. Avoid converting every prose paragraph into a requirement.
- **Design:** Explain the chosen approach and why it fits the existing system. Specify component boundaries, interfaces and data changes, compatibility or migrations, and important failure cases. Cover authorization, privacy, reliability, performance, accessibility, or operational concerns where the proposed feature touches them. Label unresolved design choices and their dependent scope.
- **Implementation sequence:** Organize coherent phases or slices with deliverables, covered requirement IDs, true prerequisites, and verification. Leave independent work parallelizable. Mention tests alongside the behavior they prove; a separate verification phase is useful only for checks that span slices.
- **Verification:** State concrete commands or inspections and the evidence they should establish. Include representative success and failure cases. Mark commands that are proposed or depend on missing tools; writing a plan does not mean those checks have run.
- **Risks and decisions:** Record material unknowns, their impact, an investigation or mitigation, and what would change the approach. Avoid padding the plan with hypothetical risks unrelated to the feature.

If the repository is unavailable, produce a useful provisional plan with assumptions and an explicit repository discovery step. Do not claim file paths, interfaces, or tests exist. When a critical choice remains unknown, define a focused investigation and gate only dependent implementation rather than treating speculation as a settled design.

## Refine and synthesize when it adds evidence

For a consequential design, independent alternatives or a fresh reviewer can expose different assumptions. Use available agents, user-supplied proposals, or authorized model access; do not require particular providers, model versions, or a fixed number of participants. Give each reviewer the same goal, constraints, relevant background, and complete current plan so differences reflect design judgment rather than missing inputs. Independent proposals are optional for bounded changes with a clear design.

Evaluate proposed changes individually. Compare their user benefit, architecture, failure handling, testability, complexity, and fit with the existing system. Record whether a substantive suggestion is accepted, adapted, rejected, or deferred, with its reason and affected requirement or section. Synthesize compatible strengths into the existing plan; do not concatenate mutually inconsistent alternatives, adopt every novel feature, or silently lose functionality while simplifying prose.

Make revision feedback concrete: explain the problem and rationale, then give an exact replacement or diff against the current file when that is useful. Inspect supplied patches before applying them, reconcile edits against the latest version, and check that the integrated document actually contains every accepted change. A feedback-to-section checklist is useful for a large batch; invented claims that dozens of errors must exist are not evidence of thoroughness.

A focused review request can be:

> Compare this complete plan with the requested user workflows and repository constraints. Identify missing behavior, incompatible assumptions, failure handling gaps, or unnecessary complexity. For each material finding, explain its consequence and propose a precise change. Account for earlier feedback by pointing to the revised section or explaining why it was not adopted.

Use a fresh perspective when anchoring or an unresolved tradeoff is the problem. Repeat review only when new feedback, substantive edits, or demonstrated gaps justify another pass. If proposals oscillate between designs, identify the disputed acceptance condition and decide from evidence. If revisions keep expanding scope, separate optional ideas from the requested deliverable. If a plan remains inadequate despite cosmetic edits, investigate the missing source facts rather than polishing the same assumptions.

## Check the plan and hand it to Beads

Review it in both directions: each requested outcome has an acceptance condition and implementation coverage; each proposed phase serves an outcome or a justified prerequisite. Check that interfaces agree, important failure cases have verification, and no phase relies on an unstated decision. Resolve demonstrated gaps, then save the plan.

Keep system-wide product or architecture choices in plan space while they materially affect downstream work. Move into Beads when the included design is actionable and remaining questions concern task boundaries, sequencing, test obligations, and local execution context. Unresolved independent work does not prevent conversion of a settled slice. Plan length, time spent, review count, and apparent similarity between review outputs are not readiness evidence.

For the next stage, use [conversion and quality](conversion-and-quality.md). Carry requirement IDs and exact plan section pointers into the coverage map and executable Beads. A phase is a sequencing aid, not necessarily one bead: split or combine by independently verifiable outcome. Keep the plan as the design source and Beads as the execution tracker; do not maintain competing task status checklists in the plan.

For an authorized end-to-end or plan-to-Beads request, make the transition real: start native tracker creation or reconciliation after saving the actionable plan. A revised document and a description of intended tasks do not complete that stage. If tooling or a decision prevents it, report the exact incomplete stage and continue independent authorized work rather than presenting the plan as an executed backlog.

During implementation, update the plan when discovered facts or code changes invalidate its design, requirements, or verification approach. Preserve IDs and record the reason for a meaningful decision change. Reconcile affected Beads and coverage together; do not silently delete deferred requirements to make a report look complete. Report the saved plan path, what was actually inspected, and any decisions that still block dependent work.

These refinements adapt the planning, synthesis, and transition practices in the [Agentic Coding Flywheel guide](https://agent-flywheel.com/complete-guide). Its project-size examples, dated model recommendations, review quotas, and illustrative scores are not requirements or measured guarantees for this skill.
