# Agent Skills Marketplace

A marketplace of skills for coding agents. Each plugin is a self-contained set of instructions (`SKILL.md` plus optional reference files) that any agent capable of reading such files can use — some plugins additionally ship a `.claude-plugin/plugin.json` and/or `.codex-plugin/plugin.json` manifest for package-manager-style install.

## Install (Claude Code)

```
/plugin marketplace add jlotthammer/skills
/plugin install code-rigor@skills-marketplace
```

(Testing locally before pushing: `/plugin marketplace add ./` from this directory, then the same `/plugin install` command.)

## Install (Codex)

```
codex plugin marketplace add jlotthammer/skills
codex plugin add code-rigor@skills-marketplace
```

Codex reads its own catalog at `.agents/plugins/marketplace.json` — a different path and schema from Claude Code's `.claude-plugin/marketplace.json`, so both files are maintained here.

## Install (other agents)

For generic `AGENTS.md`-reading agents with no package manager of their own, point the agent at, or copy in, the plugin's `skills/<skill-name>/` directory directly — the skill content itself is agent-agnostic even where a plugin only ships one ecosystem's manifest today.

## Plugins

- [`code-rigor`](code-rigor/README.md) — software engineering discipline for maintainable architecture, dataflow, ownership, testing, and optimization. Ships two skills: `code-rigor` (implementation/refactoring/debugging) and `code-rigor-review` (independent diff review). Works with both Claude Code and Codex (dual manifests).
- [`labcoat`](https://github.com/jlotthammer/labcoat) — local-first experimental provenance workspace (desktop app + CLI) that also ships an agent skill for hypothesis-driven experiment tracking, with integration notes for both `AGENTS.md`- and `CLAUDE.md`-reading agents. Lives in its own repo; listed in both catalogs here via a remote source, so it installs by name from this marketplace like any other plugin.

## Adding a plugin to this marketplace

Add an entry to **both** catalogs — `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json` — since each agent reads only its own.

Two ways to list a plugin, depending on where its code lives:

- **In this repo**: add a new top-level directory with the plugin's own `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`, plus `skills/` and `tests/`. Reference it by relative path — Claude: `"source": "./<dir>"`; Codex: `"source": { "source": "local", "path": "./<dir>" }`. Run its integrity tests, e.g. `pytest code-rigor/tests/`.
- **In its own repo** (e.g. a plugin that's more than a skill — has its own app, build pipeline, or release process): give that repo its own `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` at its root (both auto-discover `./skills/`), then reference it remotely — Claude: `{ "source": "github", "repo": "owner/repo" }`; Codex: `{ "source": "url", "url": "https://github.com/owner/repo" }`. Both ecosystems also support a subdirectory-of-external-repo source (`"source": "git-subdir"` with a `path`), and pinning via `ref`/`sha`.
