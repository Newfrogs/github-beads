# Markdown planning

Use this reference when the user needs an implementation plan, including the planning stage of an end-to-end request. A plan explains the intended behavior and design; actual work status and execution evidence belong in Beads.

## Establish the planning scope

Read the user's request, supplied plans or issues, applicable repository instructions, and the code and tests that implement related behavior. Use the repository's existing planning convention; otherwise save the plan at `plans/<descriptive-slug>.md`. Keep the plan and implementation in the selected project repository. Creating separate planning or coding repositories is a separate user choice.

Preserve the requested mode. A plan-only request ends with a saved plan and its unresolved decisions. A request to plan, create Beads, and implement authorizes proceeding through those stages without a new approval ceremony between them. Ask only for information that materially changes the outcome and cannot be resolved from available evidence; continue independent work while it is pending. Do not assume that implementing code also requests deployment, an issue mirror, or other publication.

For an existing plan, refine it in place where practical. Preserve its intent, useful detail, stable requirement IDs, source links, and recorded decisions. Resolve contradictions using the user's current request and repository evidence; record any scope change explicitly. Avoid replacing an agreed design with a fresh outline merely because its formatting differs from the template.

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

## Check the plan and hand it to Beads

Review it in both directions: each requested outcome has an acceptance condition and implementation coverage; each proposed phase serves an outcome or a justified prerequisite. Check that interfaces agree, important failure cases have verification, and no phase relies on an unstated decision. Resolve demonstrated gaps, then save the plan.

For the next stage, use [conversion and quality](conversion-and-quality.md). Carry requirement IDs and exact plan section pointers into the coverage map and executable Beads. A phase is a sequencing aid, not necessarily one bead: split or combine by independently verifiable outcome. Keep the plan as the design source and Beads as the execution tracker; do not maintain competing task status checklists in the plan.

During implementation, update the plan when discovered facts or code changes invalidate its design, requirements, or verification approach. Preserve IDs and record the reason for a meaningful decision change. Reconcile affected Beads and coverage together; do not silently delete deferred requirements to make a report look complete. Report the saved plan path, what was actually inspected, and any decisions that still block dependent work.
