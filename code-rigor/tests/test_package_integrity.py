from pathlib import Path
import json
import re

ROOT = Path(__file__).parents[1]


def test_manifests_resolve_skill_package():
    for manifest_path in (
        ROOT / ".codex-plugin/plugin.json",
        ROOT / ".claude-plugin/plugin.json",
    ):
        manifest = json.loads(manifest_path.read_text())
        skills = ROOT / manifest["skills"]
        assert skills.is_dir()

        names = {
            p.name
            for p in skills.iterdir()
            if p.is_dir() and (p / "SKILL.md").is_file()
        }
        assert names == {"code-rigor", "code-rigor-review"}


def test_skill_identities_and_references_resolve():
    skills_root = ROOT / "skills"

    for skill_dir in skills_root.iterdir():
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            continue

        text = skill_file.read_text()
        match = re.search(r"^name:\s*([^\n]+)$", text, re.MULTILINE)
        assert match
        assert match.group(1).strip() == skill_dir.name

        for rel in re.findall(r"`((?:\.\./)?[^`\n]+\.md)`", text):
            target = (skill_dir / rel).resolve()
            assert target.exists(), f"{skill_dir.name}: missing {rel}"
