# GitHub Beads

A reusable agent skill that turns repository plans into Beads tasks with enough context to implement and verify them. It includes a Python auditor for dependency and requirement-mapping checks.

The skill prefers Beads Rust (`br`) for new workspaces and preserves an existing original Beads (`bd`) backend. It guides plan conversion, backlog refinement, reconciliation, and GitHub review. GitHub issue mirroring is optional.

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

## Share within a repository

Copy the same `skills/github-beads` folder into the target repository's `.agents/skills/github-beads` directory. Codex discovers repository skills there. GitHub Copilot also supports `.github/skills`, `.claude/skills`, and `.agents/skills`; see [GitHub's documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) for supported clients.

`SKILL.md`, the references, and the Python helper form the portable package. `agents/openai.yaml` supplies Codex interface metadata.

## Prerequisites

- A coding agent that supports `SKILL.md` skills, or an agent instructed to read this package directly.
- Beads Rust (`br`) for a new `br` workspace, or the native `bd` CLI for an existing `bd` workspace.
- Python 3.10 or newer to run the auditor. It has no third-party runtime dependencies.
- Git for repository collaboration. `bv` is optional; GitHub CLI or a connected GitHub interface is needed only for remote publication.

Installing the skill does not install tracker binaries. Follow the [br](https://github.com/Dicklesworthstone/beads_rust#installation), [bd](https://github.com/gastownhall/beads), and optional [bv](https://github.com/Dicklesworthstone/beads_viewer#installation) instructions. Check the installed version's help before using command examples. Never run `br` and `bd` against the same store.

## Use the skill

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

The agent reads repository instructions, selects the existing backend, checks for duplicates, creates or updates real records, audits the graph and source coverage, and prepares a reviewable handoff. Commit, PR, implementation, and issue-publication scope follow your request.

## Run the auditor on its own

From this repository's root:

```bash
python skills/github-beads/scripts/audit_beads.py examples/sample-export.jsonl --coverage examples/sample-coverage.json
```

The example files are synthetic snapshots for demonstrating the auditor. They are not a tracker database and should not be imported as your project's backlog.

For your own full export, replace those paths with the export and coverage-map paths. For `br`, refresh the export using `br sync --flush-only` first.

The auditor prints a JSON receipt, with input hashes, errors, warnings, and coverage state. Exit codes are `0` for no audit errors, `1` for audit errors, and `2` for invalid or unreadable input. It changes no input files and opens no database.

It checks duplicate IDs, basic content, typed-edge integrity, missing local endpoints, structural cycles, and coverage references. Duplicate titles, external references, and custom edge types are flagged for review. Without a coverage map, coverage is explicitly `not_checked`.

These checks do not prove semantic completeness, implementation, or backend-specific readiness. Live `br`, `bd`, and `bv` integration has not yet been validated for this package. See the [coverage schema and audit limits](skills/github-beads/references/conversion-and-quality.md).

## Contribute

Run the tests and example before proposing changes:

```bash
python -m unittest discover -s tests -v
python skills/github-beads/scripts/audit_beads.py examples/sample-export.jsonl --coverage examples/sample-coverage.json
```

GitHub Actions runs these checks on Windows and Linux. Keep the canonical package in `skills/github-beads`, preserve backend boundaries, and add a regression test when changing auditor behavior. Report the tracker version when proposing a command correction.

## Research and attribution

The methodology was informed by Jeffrey Emanuel's [Agent Flywheel guide](https://agent-flywheel.com/complete-guide). The package is independently written and is not an official distribution of Agent Flywheel, Beads Rust, original Beads, or Beads Viewer.

The [research and implementation plan](docs/research-and-implementation-plan.md) covers the design decisions and remaining live integration gates. Tool commands and behavior are checked against primary upstream documentation linked in the references.

## License

This repository's original files are available under the [MIT License](LICENSE). Referenced tools, websites, and documentation retain their own licenses and terms; they are not bundled here.
