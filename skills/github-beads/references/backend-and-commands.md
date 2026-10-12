# Backend selection and command handling

Checked against primary upstream documentation on 12 October 2026. Verify the installed CLI before applying examples.

## Choose one store

New Flywheel workspaces should normally use Beads Rust, whose operational store is SQLite with a JSONL collaboration export. Current original Beads uses Dolt and a separate synchronization model. A `.beads/` directory can belong to either implementation. Read the project's instructions and configuration and inspect the native CLI; a `bd-` ID can also exist in a `br` project. [Beads Rust](https://github.com/Dicklesworthstone/beads_rust), [original Beads](https://github.com/gastownhall/beads).

For a repository already using `bd`, retain it. Use installed help and its official documentation for creation, descriptions, hierarchy, dependencies, claims, and Dolt handoff. This package's `br` commands are not a migration recipe. The bundled auditor may inspect a compatible exported JSONL file, but that file is not a Dolt backup.

Check database-location overrides such as `BEADS_DB` and explicit `--db` arguments, as well as project configuration. Confirm the resolved store and export belong to the intended repository before any mutation; a correct working directory alone does not guarantee this. If an ambient override redirects the tool elsewhere, use the installed backend's supported repository-local location option or resolve the configuration conflict. Do not initialize or claim work in the redirected store, bypass its lock, or change global configuration merely to make the command succeed.

## Inspect before mutation

At the repository root:

```text
git status --short
git remote -v
br --version
br create --help
br update --help
br dep --help
br list --help
br sync --help
```

`br capabilities --format json`, if supported, exposes command contracts. Fetch complete lists using supported pagination or `--limit 0`; include closed work. Current `list --json` may return a wrapper with `issues` and pagination fields, whereas some earlier versions return arrays. Validate the shape instead of hard-coding one parser. [Agent integration](https://github.com/Dicklesworthstone/beads_rust/blob/main/docs/AGENT_INTEGRATION.md).

Read-only commands can still refresh tracker state when auto-import is enabled. If the task requires a strict no-change inspection, verify and use the installed `--no-auto-import --no-auto-flush` flags. Do not call repair, force, upgrade, or initialization commands merely to inspect an existing project.

## Create and refine with br

Initialize only if there is no existing store and creation is within scope. Never use `br init --force` as normal setup.

Representative command forms:

```text
br init
br create "Implement the parser contract" --type task --priority 2 --description "Source: PLAN.md#REQ-PARSE-01; preserve the documented input rules." --json
br create "Implement the parser contract" --type task --priority 2 --description-file bead-body.md --json
br show ACTUAL_ID --json
br update ACTUAL_ID --description-file bead-body.md --json
br create "Parser delivery" --type epic --priority 2 --description "Scope and completion contract for parser delivery." --json
br create "Reject malformed input" --type task --parent ACTUAL_EPIC_ID --priority 2 --description "Complete executable task body." --json
br dep add ACTUAL_CONSUMER_ID ACTUAL_PREREQUISITE_ID --type blocks --json
br comments add ACTUAL_ID --file review-note.md --json
br dep cycles --json
br ready --json
br blocked --json
br sync --flush-only
```

Substitute IDs returned by the tracker. The positional title avoids relying on the guide's `--title` example. `create --file` means bulk creation from a specially parsed Markdown file, not reading one bead description. Version 0.7.4 supports `create --description-file` for a complete literal body in one mutation. Current `update --description-file` replaces the entire description verbatim; re-read the bead and preserve existing content before using it. Check help before relying on these flags in older versions. [CLI reference](https://github.com/Dicklesworthstone/beads_rust/blob/main/docs/CLI_REFERENCE.md), [CLI implementation](https://github.com/Dicklesworthstone/beads_rust/blob/main/src/cli/mod.rs).

For long bodies, prefer a supported file input or a subprocess API argument array; keep newlines, quotes, backticks, Unicode, and dollar signs literal. If no file option exists, use an argument array with shell interpretation disabled. Do not build shell code from plan text. Verify the saved body with `show` after creation or update. A two-step create and body update must leave an explicit unfinished record if the second step fails.

Use priorities 0 through 4 according to the repository's conventions. Choose the ordinary supported types unless the project defines custom ones. Preserve policy-specific statuses and transition requirements. Do not assume an upstream default applies to a configured project.

## Recovery after an uncertain result

Creation is not automatically idempotent. Before retrying a timed-out mutation, query the store using the source requirement identity, inspect candidate records, and recover their actual IDs. Keep a receipt of successful changes. If matching is ambiguous, stop that mutation and report the conflict; continue independent authorized work.

Do not repeatedly retry a database lock or bypass a guard. Inspect the stated condition and native diagnostics. Re-read a bead before changing a concurrently edited record; use a supported revision guard where available. Preserve both sources of intent when a conflict is real.

## Tool availability on Windows

Check `Get-Command br,bd,bv,git,gh -ErrorAction SilentlyContinue` in PowerShell. Current `br` and `bv` documentation lists native Scoop packages as well as other platforms; WSL is an alternative, not a universal requirement. Verify release checksums if installing an archive. Installation of the instruction package does not install these binaries. [br installation](https://github.com/Dicklesworthstone/beads_rust#installation), [bv installation](https://github.com/Dicklesworthstone/beads_viewer#installation).

`br` is required for a new `br` store. `bv` improves graph analysis but is optional for small conversions. `gh` or a connected GitHub interface is needed only for remote issue or PR work; local Beads creation works without it.
