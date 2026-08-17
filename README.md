# Skills Marketplace

A Claude Code plugin marketplace. Add this repo once, then install any plugin it lists by name.

## Install

```
/plugin marketplace add jlotthammer/skills
/plugin install code-rigor@code-rigor-marketplace
```

(Testing locally before pushing: `/plugin marketplace add ./` from this directory, then the same `/plugin install` command.)

## Plugins

- [`code-rigor`](code-rigor/README.md) — software engineering discipline for maintainable architecture, dataflow, ownership, testing, and optimization. Ships two skills: `code-rigor` (implementation/refactoring/debugging) and `code-rigor-review` (independent diff review).

## Adding a plugin to this marketplace

1. Add a new top-level directory with the plugin's own `.claude-plugin/plugin.json` (and `.codex-plugin/plugin.json` if it should also work as a Codex skill-only plugin), `skills/`, and `tests/`.
2. Add an entry to `plugins` in `.claude-plugin/marketplace.json`: `{ "name": "...", "source": "./<dir>", "description": "..." }`.
3. Run that plugin's integrity tests, e.g. `pytest code-rigor/tests/`.
