# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This repo is both a monorepo of Claude Code / Codex **skill plugins** and a **Claude Code plugin marketplace** (`.claude-plugin/marketplace.json` at the root). Each top-level directory (e.g. `code-rigor/`) is an independent, self-contained plugin with its own manifest, skills, and tests. There is no shared build system or package manager tying plugins together — each plugin stands alone and can be installed independently via `/plugin install <name>@skills-marketplace`.

## Marketplace catalog

`.claude-plugin/marketplace.json` lists every installable plugin: `name` (required), `owner` (required object), and a `plugins` array where each entry has `name` and `source` (a `./relative-path` to that plugin's directory). When adding a new plugin directory, add a matching entry here or `/plugin install` won't find it. This file is separate from and additional to each plugin's own `.claude-plugin/plugin.json`.

## Plugin anatomy

A plugin directory follows this layout (see `code-rigor/` as the reference example):

```
<plugin-name>/
  .claude-plugin/plugin.json   # Claude Code manifest
  .codex-plugin/plugin.json    # Codex manifest (same fields as above, plus optional `interface`)
  README.md
  skills/
    <skill-name>/SKILL.md      # required: frontmatter `name:` must match the directory name
    <skill-name>/references/*.md  # optional, loaded lazily by the skill
  tests/test_package_integrity.py
```

Both plugin manifests declare `"skills": "./skills/"` and must point at a directory whose immediate subdirectories (each containing a `SKILL.md`) are the actual installable skills.

## Skill authoring conventions (from code-rigor)

- `SKILL.md` frontmatter `name:` must exactly equal the containing directory's name — this is enforced by the integrity test, not just convention.
- Any backtick-quoted `*.md` path inside a `SKILL.md` (e.g. `` `references/testing.md` `` or `` `../other-skill/references/x.md` ``) must resolve to a real file relative to the skill's directory — also enforced by the integrity test.
- Keep `SKILL.md` itself lean: core principles and a references index. Push language/framework/topic-specific detail into `references/*.md` files that are loaded only when relevant, not into the main skill body.
- A plugin can ship multiple cooperating skills (e.g. `code-rigor` for implementation and `code-rigor-review` as an independent reviewer) that cross-reference each other's `references/` files via relative paths.

## Testing

Each plugin has its own `tests/` directory with plain `pytest` tests (no fixtures/frameworks beyond stdlib + pytest). Run a plugin's tests from within the plugin directory or by pointing pytest at it directly:

```bash
pytest code-rigor/tests/
```

The integrity tests (`test_package_integrity.py`) validate structural invariants of the plugin itself:
1. Both manifests' `skills` path resolves to a directory containing exactly the expected set of skill subdirectories (each with a `SKILL.md`).
2. Every skill's `SKILL.md` frontmatter `name` matches its directory name, and every backtick-quoted `.md` reference path it contains actually exists.

When adding a new skill to a plugin, update the corresponding `assert names == {...}` set in that plugin's `test_package_integrity.py`.

## Adding a new plugin

Mirror `code-rigor/`'s structure: dual manifests (`.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`) with matching `name`/`version`/`description`/`skills`, a `README.md` summarizing the skills it ships, and a `tests/test_package_integrity.py` enforcing the same manifest/skill-name/reference invariants.
