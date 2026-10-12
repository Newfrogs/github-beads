# <Feature or change> implementation plan

<!-- Adapt this template to the repository and remove all guidance and unused sections before delivery. The plan records intent, design, and decisions. Keep execution status and test run evidence in Beads. -->

## Outcome and scope

Describe the requested result, who or what uses it, current behavior, and how success will be observed.

**Included:** State the required behavior and boundaries.

**Excluded or deferred:** State relevant exclusions and the reason for any deferred scope.

## User workflows

Describe the important journeys from the user's or operator's perspective: trigger, inputs, success result, progress or intermediate states, permission boundary, visible failure, and recovery. Keep only meaningful workflows. Use them to discover missing requirements rather than assuming component names fully describe the product.

## Inputs, evidence, and current system

| Source | Finding or constraint | Confidence / open question |
| --- | --- | --- |
| Repository path and symbol, supplied issue or specification, or authoritative URL | Relevant observed fact; label assumptions explicitly | Verified against a revision/version, or still to investigate |

Describe the current architecture and data flow relevant to this change: entry points, components, interfaces, persistence, tests, and existing conventions. Use repository-relative paths. Mark suggested new paths as proposed. Cite external technical evidence only when it informs a decision, including its applicable version or access date.

Identify the applicable project instructions, established or selected stack, and relevant local engineering guidance. Explain an undecided or changed stack using the workflows and concrete capabilities it must support; do not copy another project's configuration by default.

## Requirements and acceptance criteria

<!-- Preserve requirement IDs as the plan evolves. Use as many rows as meaningful outcomes require; the example ID is a naming pattern, not a required requirement. -->

| ID | Required behavior or constraint | Observable acceptance | Source |
| --- | --- | --- | --- |
| REQ-001 | One independently verifiable outcome | Concrete condition, including a meaningful failure case where relevant | Input path/section or issue URL |

## Proposed design

### Approach and component changes

Describe the chosen solution, its rationale, affected components, and the boundaries between them. Explain alternatives only when they clarify a material tradeoff or unresolved choice.

### Interfaces and data

Specify the important input/output contracts, validation, state or schema changes, storage, and compatibility. Describe migration and rollback behavior when applicable. Distinguish established interfaces from proposed ones.

### Failure handling and constraints

Describe expected error behavior, important edge cases, and the relevant authorization, privacy, reliability, performance, accessibility, or operational constraints. Include only concerns this change actually touches.

## Implementation sequence

<!-- Phases group coherent deliverables. Beads may split or combine them by verifiable outcome. Do not add a universal number of phases or defer all tests to the end. -->

| Phase / slice | Deliverable and likely affected paths | Requirement IDs | Prerequisites and rationale | Verification |
| --- | --- | --- | --- | --- |
| Descriptive phase name | Observable deliverable; label unconfirmed paths as proposed | REQ-001 | True prerequisites, or independent | Meaningful test or inspection for this slice |

## Verification strategy

| Behavior / requirement | Test or inspection | Expected evidence | Setup or limitation |
| --- | --- | --- | --- |
| REQ-001 | Exact known repository command or a described proposed test | What proves the acceptance condition, including negative cases | Fixtures, environment, missing tool, or manual check |

Describe cross-component or end-to-end checks where they add evidence beyond individual slices. Record existing baseline failures or unavailable checks without claiming they passed. Concrete execution results will be attached to the corresponding Beads.

Specify setup and diagnostic evidence needed to understand meaningful failures, respecting the project's privacy and logging rules.

## Risks and unresolved decisions

| Question or risk | Impact on the outcome | Evidence needed / mitigation | Dependent scope |
| --- | --- | --- | --- |
| Material unknown | What could change or fail | Focused investigation or a reversible assumption | Only the work that depends on the answer |

## Decisions and provenance

| Decision or revision | Rationale and supporting source | Effect on scope or design |
| --- | --- | --- |
| Initial approach or meaningful later change | Repository evidence, user direction, or cited documentation | Affected requirement IDs, interfaces, or verification |

Record the source revision or specification version when useful. During execution, revise this plan only when intent, design, or verification changes; reconcile the affected Beads and requirement coverage at the same time.

<!-- Optional: keep the following table when synthesizing alternatives or applying substantial review feedback. Remove it for a straightforward plan with no such inputs. -->

### Review feedback disposition

| Proposal or finding | Accepted / adapted / rejected / deferred | Reason and revised requirement or section |
| --- | --- | --- |
| Concrete idea from an independent proposal or review | Explicit disposition | Evidence, tradeoff, and where an accepted change is integrated |

Before conversion, confirm that the included design is actionable and remaining work concerns executable task boundaries and verification. For a full-pipeline request, the next stage is actual tracker creation and reconciliation; the plan and this table do not substitute for Beads.
