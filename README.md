# Skills Marketplace

A Claude Code plugin marketplace. Add this repo once, then install any plugin it lists by name.

## Install

```
/plugin marketplace add jlotthammer/skills
/plugin install code-rigor@skills-marketplace
```

(Testing locally before pushing: `/plugin marketplace add ./` from this directory, then the same `/plugin install` command.)

## Plugins

- [`code-rigor`](code-rigor/README.md) — software engineering discipline for maintainable architecture, dataflow, ownership, testing, and optimization. Ships two skills: `code-rigor` (implementation/refactoring/debugging) and `code-rigor-review` (independent diff review).
- [`labcoat`](https://github.com/jlotthammer/labcoat) — local-first experimental provenance workspace (desktop app + CLI) that also ships a Claude skill for hypothesis-driven experiment tracking. Lives in its own repo, not this one; listed here via a `github` source pointing at `jlotthammer/labcoat`.

## Adding a plugin to this marketplace

Two ways to list a plugin, depending on where its code lives:

- **In this repo**: add a new top-level directory with the plugin's own `.claude-plugin/plugin.json` (and `.codex-plugin/plugin.json` if it should also work as a Codex skill-only plugin), `skills/`, and `tests/`. Reference it with a relative path: `{ "name": "...", "source": "./<dir>", "description": "..." }`. Run its integrity tests, e.g. `pytest code-rigor/tests/`.
- **In its own repo** (e.g. a plugin that's more than a skill — has its own app, build pipeline, or release process): give that repo its own `.claude-plugin/plugin.json` at its root (auto-discovers `./skills/`), then reference it here with `{ "name": "...", "source": { "source": "github", "repo": "owner/repo" }, "description": "..." }`. Use `source: "git-subdir"` with a `path` field instead if only a subdirectory of that repo should be installed.
