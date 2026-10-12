# GitHub handoff

## Repository collaboration

For `br`, export before inspecting the reviewable changes:

```text
br sync --flush-only
git status --short
git diff -- .beads/issues.jsonl
git status --short --ignored -- .beads/
```

Stage the export, relevant plan and coverage or execution artifacts, and the code, tests, and documentation actually changed within scope. Preserve the generated ignore rules and verify that databases, WAL files, locks, recovery data, and machine-specific metadata are excluded. Inspect the staged diff before committing. `br` does not commit, pull, or push automatically, though explicitly requested reporting commands can inspect Git. [VCS integration](https://github.com/Dicklesworthstone/beads_rust/blob/main/docs/VCS_INTEGRATION.md).

Inspect the export itself before public publication: native records can contain absolute `source_repo_path` values as well as private comments, actor identities, source URLs, or sensitive diagnostics. Use supported tracker fields to remove or replace unintended machine-specific values when authorized, then re-export and check the result. Keep legitimate provenance and permissions; do not hand-edit JSONL to conceal tracker state or publish private task history by default. Version 0.7.4 accepts `update --source-repo` and `--source-repo-path`; inspect current help before applying them.

Do not assume generated ignore rules cover every runtime file. Inspect `git status --short --untracked-files=all -- .beads/` and verify suspicious paths with `git check-ignore`. Native br 0.7.4 can create `*.db-lock-*` sidecars in addition to WAL and namespace files. Add narrow rules for confirmed runtime artifacts without hiding the collaboration export or configuration.

Follow the repository's branch and review conventions. Include bead IDs in relevant commit or PR text. A PR should identify the source plan, scope, coverage dispositions, actual tracker counts, validation, ready work, and known open decisions. If GitHub publication was requested, verify the remote and create a reviewable commit or PR within that authorization. Attach a created PR to the current host task when its artifact tool is available.

GitHub Copilot supports repository skills under `.github/skills`, `.claude/skills`, or `.agents/skills`. The portable core of this package is `SKILL.md` with its references and script; `agents/openai.yaml` is Codex interface metadata. Copy a single canonical package into the target client's supported discovery location rather than maintaining divergent versions. [GitHub agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).

## Optional GitHub issue mirror

Mirroring is an opt-in publishing workflow. The repository tracker remains authoritative for bead execution unless the user chooses a different policy. Mirror selected work for human visibility; do not turn every fine-grained bead into public noise by default.

For each mirror, use a stable body marker such as `<!-- beads-id: ACTUAL_ID -->` and preserve the source URL in the bead's supported external reference or notes. Before creating anything, look up a recorded URL or search the full intended repository for the marker. Confirm exact identity in the body; fuzzy search results are insufficient. Treat timeout outcomes as unknown, check for an existing mirror, and retry only when noncreation is established.

Keep bead acceptance criteria readable in the issue body. Preserve human-written issue discussion and fields. Avoid two-way automatic synchronization in this initial skill; field ownership, deletions, concurrent edits, and retry semantics need a separately implemented policy. Verify labels, milestones, and assignees exist before using them.

If GitHub CLI is available, prefer structured arguments and files:

```text
gh issue create --repo OWNER/REPO --title "Reviewed title" --body-file issue-body.md
gh pr create --repo OWNER/REPO --base ACTUAL_BASE --head ACTUAL_BRANCH --title "Create Beads backlog for the approved scope" --body-file pr-body.md
```

These commands publish remotely. Fill repository and branch values from inspected context and honor the user's authorized action. Read-only access to a repository does not grant permission to post comments, issues, or PRs. [Issue creation](https://cli.github.com/manual/gh_issue_create), [PR creation](https://cli.github.com/manual/gh_pr_create).

## Sync and conflict handling

For `br`, preserve local DB-only edits before importing changed JSONL. After an authorized pull or merge, inspect the resulting state; use the supported import or merge mode appropriate to whether both DB and JSONL changed. Resolve Git conflict markers before import. Do not overwrite the full export with one branch's version or apply `--force` reflexively. Upstream guard failures should lead to diagnosis and an explicit conflict decision. [Sync safety](https://github.com/Dicklesworthstone/beads_rust/blob/main/docs/SYNC_SAFETY.md).

For Dolt-backed `bd`, use its native backup and sync procedure instead. JSONL exports can feed viewers or the auditor, but are not the canonical remote synchronization mechanism.

## Finish with evidence

Distinguish the completed states: records created locally, collaboration export updated, commit recorded, branch pushed, PR created, and issues mirrored. Report only observed states. Provide actual bead IDs and PR or issue URLs where applicable. Report missing tools or policy blockers precisely without turning a proposed conversion into a completion claim.
