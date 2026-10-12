# Install GitHub Beads in Claude Code

The same `skills/github-beads` package works in Codex and Claude Code. Choose either the plugin installation or the folder installation below. The plugin uses the repository's canonical skill without maintaining a separate Claude copy.

## Install as a plugin

With Claude Code installed, run these commands in your terminal. They work in PowerShell and in macOS/Linux shells:

```text
claude plugin marketplace add Newfrogs/github-beads
claude plugin install github-beads@github-beads --scope user
claude plugin list
```

The first command registers this repository's marketplace. The second installs the plugin for your user across projects on this machine. It should appear as `github-beads@github-beads`, enabled, in the last command's output. This is an independent community plugin.

Start a new Claude Code session in the repository you want to work on. At the Claude prompt, invoke the skill with its plugin namespace:

```text
/github-beads:github-beads Convert plans/feature.md into real Beads tasks. Preserve requirements and rationale, add dependencies, include acceptance criteria and verification, and audit coverage.
```

For an existing backlog:

```text
/github-beads:github-beads Reconcile the revised plan with the existing backlog. Reuse completed work where appropriate and report actual created, updated, and reused bead IDs.
```

You can also add the marketplace inside a Claude session with `/plugin marketplace add Newfrogs/github-beads`, then open `/plugin install github-beads@github-beads` and select the installation scope in the plugin panel. See [Anthropic's installation documentation](https://code.claude.com/docs/en/discover-plugins) for client-specific behavior.

For a shared plugin configuration, run the following **from the target repository**:

```text
claude plugin marketplace add Newfrogs/github-beads --scope project
claude plugin install github-beads@github-beads --scope project
```

Review and commit the resulting `.claude/settings.json` changes. Each teammate must also install the plugin on their machine. Alternatively, the project folder installation below checks the entire skill into the target repository.

## Install the skill folder directly

Clone the public repository once and enter it:

```text
git clone https://github.com/Newfrogs/github-beads.git
cd github-beads
```

For a personal skill on macOS/Linux:

```bash
mkdir -p "$HOME/.claude/skills"
if [ -e "$HOME/.claude/skills/github-beads" ] || [ -L "$HOME/.claude/skills/github-beads" ]; then
  echo 'A github-beads skill already exists. Review it before replacing it.' >&2
else
  cp -R skills/github-beads "$HOME/.claude/skills/github-beads"
fi
```

For a personal skill on Windows with PowerShell:

```powershell
$skillDestination = Join-Path $HOME '.claude\skills\github-beads'
if (Test-Path -LiteralPath $skillDestination) {
    throw 'A github-beads skill already exists. Review it before replacing it.'
}
New-Item -ItemType Directory -Path (Split-Path $skillDestination) -Force | Out-Null
Copy-Item -LiteralPath '.\skills\github-beads' -Destination $skillDestination -Recurse
```

For a project skill, copy that entire folder to `<target-repository>/.claude/skills/github-beads` instead and commit it with the project. The resulting path must be `.claude/skills/github-beads/SKILL.md`, with `references/`, `scripts/`, and `LICENSE` alongside it. `agents/openai.yaml` contains optional Codex UI metadata; Claude uses `SKILL.md`.

Start Claude Code in the target repository and invoke a folder-installed skill without a plugin prefix:

```text
/github-beads Convert plans/feature.md into Beads tasks with dependencies, acceptance criteria, verification, and a coverage audit.
```

Personal skills live at `~/.claude/skills`; project skills live at `.claude/skills` in the target repository. These locations and the `/skill-name` syntax are documented in [Anthropic's skill guide](https://code.claude.com/docs/en/skills).

## Requirements and verification

Install the appropriate `br` or `bd` tracker and Python 3.10+ as described in the [main README](../README.md#prerequisites). The plugin and folder installations supply the skill, references, and auditor; tracker binaries are installed separately. Run the skill in a session with access to the intended repository and its tracker.

For a plugin installation, type `/` in Claude Code and look for `/github-beads:github-beads`. For a folder installation, look for `/github-beads`. If it is missing, confirm the paths or enabled plugin with `claude plugin list`, then start a new session.

The auditor can also be verified from the cloned repository:

```text
python skills/github-beads/scripts/audit_beads.py examples/sample-export.jsonl --coverage examples/sample-coverage.json
```

Use `python3` if that is your Python 3 command. The synthetic example should produce `"ok": true` and exit successfully. Live `br`, `bd`, and `bv` integration remains a separate validation gate described in the README.

## Update or remove

To refresh a plugin installation:

```text
claude plugin marketplace update github-beads
claude plugin update github-beads@github-beads
```

Start a new session to load the updated version. To remove a user-scope plugin installation:

```text
claude plugin uninstall github-beads@github-beads --scope user
```

For a folder installation, compare the existing folder with the latest `skills/github-beads` and replace it after preserving any local edits. A copied skill does not update when you pull this source repository.

## Maintainer checks

Claude Code provides native checks for both manifests:

```text
claude plugin validate .claude-plugin/plugin.json --strict
claude plugin validate .claude-plugin/marketplace.json --strict
```

Bump the version in `.claude-plugin/plugin.json` when publishing a changed plugin so installed copies can update. The root `skills/` directory is the standard plugin discovery location; see the [plugin manifest reference](https://code.claude.com/docs/en/plugins-reference) and [marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).
