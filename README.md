# GitHub Beads

A reusable skill for Claude Code and Codex that writes a full Markdown plan, turns it into dependency-aware Beads tasks, then implements and verifies the code in your project repository. It supports existing-project discovery, independent plan synthesis, optional swarm coordination, recovery, integrated review, delivery, and evidence-driven learning, with reusable templates and a read-only Python auditor.

The skill prefers Beads Rust (`br`) for new workspaces and preserves an existing original Beads (`bd`) backend. You can request the full workflow or stop at planning or Beads creation. GitHub publication follows your request; issue mirroring is optional.

## Install in Codex

Ask Codex:

```text
$skill-installer install https://github.com/Newfrogs/github-beads/tree/main/skills/github-beads
```

If the skill does not appear after installation, restart Codex. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for current discovery locations and client behavior.

For a manual personal installation, clone this repository and copy `skills/github-beads` into your client's personal skills directory. Current Codex documentation lists `~/.agents/skills`; some installations use the configured `$CODEX_HOME/skills` directory. Choose the directory your client uses and avoid installing duplicate copies.

From the cloned repository, on Linux or macOS:

```bash
mkdir -p "$HOME/.agents/skills"
test ! -e "$HOME/.agents/skills/github-beads" || exit 1
cp -R skills/github-beads "$HOME/.agents/skills/github-beads"
```

On Windows with PowerShell:

```powershell
$skillDestination = Join-Path $HOME '.agents\skills\github-beads'
if (Test-Path -LiteralPath $skillDestination) {
    throw 'A github-beads skill already exists. Review it before replacing it.'
}
New-Item -ItemType Directory -Path (Split-Path $skillDestination) -Force | Out-Null
Copy-Item -LiteralPath '.\skills\github-beads' -Destination $skillDestination -Recurse
```

## Install in Claude Code

Run these commands in your terminal:

```text
claude plugin marketplace add Newfrogs/github-beads
claude plugin install github-beads@github-beads --scope user
```

Start Claude Code in the repository you want to work on, then invoke:

```text
/github-beads:github-beads Write a full Markdown plan for FEATURE, turn it into Beads, then implement and verify the code in this repository.
```

The [Claude installation guide](docs/claude-installation.md) also covers Windows and macOS/Linux folder installation, personal and project scopes, verification, updates, and removal. A folder installation uses `/github-beads`; the plugin installation uses `/github-beads:github-beads`. See [Anthropic's plugin documentation](https://code.claude.com/docs/en/discover-plugins) for supported clients.

## Share within a repository

Copy the same `skills/github-beads` folder into the target repository's `.agents/skills/github-beads` directory. Codex discovers repository skills there. GitHub Copilot also supports `.github/skills`, `.claude/skills`, and `.agents/skills`; see [GitHub's documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) for supported clients.

`SKILL.md`, the references, and the Python helper form the portable package. `agents/openai.yaml` supplies Codex interface metadata.

## Update an existing installation

For Claude's plugin installation:

```text
claude plugin marketplace update github-beads
claude plugin update github-beads@github-beads
```

For a copied Codex or Claude skill, pull the latest source, compare it with your installed `github-beads` folder, preserve any local edits, and refresh the entire package including its references and assets. The installer and copy examples above intentionally refuse an existing destination. Start a new client session after updating.

## Prerequisites

- A coding agent that supports `SKILL.md` skills, or an agent instructed to read this package directly.
- Beads Rust (`br`) for a new `br` workspace, or the native `bd` CLI for an existing `bd` workspace.
- Python 3.10 or newer to run the auditor. It has no third-party runtime dependencies.
- Git for repository collaboration. `bv` is optional; GitHub CLI or a connected GitHub interface is needed only for remote publication.

Use `python3` instead of `python` in the commands below if that is how your system names Python 3.

Installing the skill does not install tracker binaries. Follow the [br](https://github.com/Dicklesworthstone/beads_rust#installation), [bd](https://github.com/gastownhall/beads), and optional [bv](https://github.com/Dicklesworthstone/beads_viewer#installation) instructions. Check the installed version's help before using command examples. Never run `br` and `bd` against the same store.

## Use the skill

For the full workflow in Codex:

```text
Use $github-beads to write a full Markdown plan for FEATURE in this
repository, create dependency-aware Beads from it, then implement the
included scope and verify its acceptance criteria. Save the plan,
coverage map, and execution evidence. Continue through all three stages.
```

In Claude Code with the plugin:

```text
/github-beads:github-beads Write a full Markdown plan for FEATURE in this repository, create Beads from it, then implement and verify the included scope. Save the plan, coverage map, and execution evidence. Continue through all three stages.
```

Replace `FEATURE` with the behavior you want and any constraints. A folder-installed Claude skill uses `/github-beads` instead.

| Requested mode | Result |
| --- | --- |
| Plan only | A saved Markdown plan with requirements, design, implementation sequence, verification, and open decisions |
| Beads only | Actual tracker records, dependencies, and a coverage audit of the supplied plan |
| Full workflow | Plan, Beads, implemented code, and acceptance evidence |
| Implement or resume | Continued work from the saved plan and actual tracker state |

For planning only:

```text
Use $github-beads to write a full Markdown plan for FEATURE. Planning only:
save the plan, but do not create Beads or change implementation code.
```

For an existing plan:

```text
Use $github-beads to convert plans/feature.md into real Beads tasks in this
repository. Preserve the requirements and rationale, add dependencies,
include acceptance criteria and verification, and audit coverage.
```

```text
Use $github-beads to reconcile the revised plan with the existing backlog.
Reuse completed work where it still satisfies the requirements and report
the actual created, updated, and reused bead IDs.
```

To resume coding:

```text
Use $github-beads to resume implementation from plans/feature.md and its
existing Beads. Inspect current code and tracker state, preserve completed
work, implement the remaining included requirements, and verify them.
```

Use the same instructions after `/github-beads:github-beads` in Claude Code. The invocation prefix is the client-specific part; the workflow and supporting files are shared.

## Where the plan, tasks, and code live

The agent follows your project's conventions. Otherwise, it writes the plan to `plans/<feature-slug>.md`, keeps a requirement coverage map and a concise execution receipt alongside it, creates actual tasks in the selected Beads store, and edits the project's existing code and tests. Planning and coding use the same repository by default.

The [plan template](skills/github-beads/assets/plan-template.md) covers the goal, scope, evidence, stable requirement IDs, observable acceptance criteria, architecture, design, failure handling, implementation sequence, verification, risks, and decisions. The [planning guide](skills/github-beads/references/markdown-planning.md) explains how to adapt it to the work.

The agent checks for existing tasks before creating records, audits source coverage and dependencies, claims eligible work through the native tracker, implements it, and records acceptance evidence before closing tasks. The [implementation and resume guide](skills/github-beads/references/implementation-and-resume.md) describes that loop and recovery after interruptions.

For an existing project, the [discovery guide](skills/github-beads/references/existing-projects.md) traces real user paths and checks for completed code that needs connecting. Substantial plans can use independent proposals and selective synthesis without a fixed provider roster or review quota. The [coordination guide](skills/github-beads/references/swarm-coordination.md) separates task claims, file reservations, messages, and Git integration, and diagnoses stalled work. The [toolchain and learning guide](skills/github-beads/references/toolchain-and-learning.md) inventories all 28 guide modules and routes optional tools by actual need, capacity, and data scope.

The [workflow request packets](skills/github-beads/assets/workflow-prompts.md), [project instructions template](skills/github-beads/assets/agent-instructions-template.md), and [feedback template](skills/github-beads/assets/agent-feedback-template.md) support synthesis, transfer audits, recovery, review, and tested lesson capture. Adapt them to the repository; installing the skill does not overwrite project instructions, install the tool stack, or change host permissions.

A full workflow request continues through the local stages without another planning approval. Material missing decisions and host permissions still apply; independent work continues when possible. Commits, pushes, PRs, deployment, and issue publication follow your request. A passing structural audit alone does not establish that code is implemented or correct.

## Run the auditor on its own

From this repository's root:

```bash
python skills/github-beads/scripts/audit_beads.py examples/sample-export.jsonl --coverage examples/sample-coverage.json
```

The example files are synthetic snapshots for demonstrating the auditor. They are not a tracker database and should not be imported as your project's backlog.

For your own full export, replace those paths with the export and coverage-map paths. For `br`, refresh the export using `br sync --flush-only` first.

The auditor prints a JSON receipt, with input hashes, errors, warnings, and coverage state. Exit codes are `0` for no audit errors, `1` for audit errors, and `2` for invalid or unreadable input. It changes no input files and opens no database.

It checks duplicate IDs, basic content, typed-edge integrity, missing local endpoints, structural cycles, and coverage references. Duplicate titles, external references, and custom edge types are flagged for review. Without a coverage map, coverage is explicitly `not_checked`.

These checks do not prove semantic completeness, implementation, or backend-specific readiness. See the [coverage schema and audit limits](skills/github-beads/references/conversion-and-quality.md) for supported checks and their limits.

Before claiming included work complete, add the optional status gate:

```bash
python skills/github-beads/scripts/audit_beads.py .beads/issues.jsonl --coverage plans/feature-coverage.json --require-closed
```

It requires a coverage map and rejects included records that are not closed. Deferred/excluded scope and unrelated backlog need not close. Its `completion` receipt counts unique included and closed records; status alone still needs actual acceptance and integration evidence. The default audit remains suitable for a newly created unfinished backlog.

## Contribute

Run the tests and example before proposing changes:

```bash
python -m unittest discover -s tests -v
python skills/github-beads/scripts/audit_beads.py examples/sample-export.jsonl --coverage examples/sample-coverage.json
```

GitHub Actions runs these checks on Windows and Linux. Keep the canonical package in `skills/github-beads`, preserve backend boundaries, and add a regression test when changing auditor behavior. Report the tracker version when proposing a command correction.

## Attribution

The methodology was informed by Jeffrey Emanuel's [Agent Flywheel guide](https://agent-flywheel.com/complete-guide). The package is independently written and is not an official distribution of Agent Flywheel, Beads Rust, original Beads, or Beads Viewer.

Primary upstream documentation is linked in the skill's references.

## License

This repository's original files are available under the [MIT License](LICENSE). Referenced tools, websites, and documentation retain their own licenses and terms; they are not bundled here.
