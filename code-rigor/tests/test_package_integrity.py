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

    # Every backticked .md path in every document must resolve from that
    # document's own directory. References cross-link each other, and a broken
    # sibling link fails silently for a reader who trusts it.
    for doc in skills_root.rglob("*.md"):
        for rel in re.findall(r"`((?:\.\./)*[^`\n]+\.md)`", doc.read_text()):
            target = (doc.parent / rel).resolve()
            assert target.exists(), f"{doc.relative_to(ROOT)}: missing {rel}"


SKILL_DOCS = sorted((ROOT / "skills").rglob("*.md"))


def _lines(path):
    for number, line in enumerate(path.read_text().splitlines(), start=1):
        yield number, line


def test_skill_offers_every_reference_on_disk():
    """The always-loaded SKILL.md is the one list of references. It must match
    the directory, and the review skill must point at that list, not copy it."""
    skill = (ROOT / "skills/code-rigor/SKILL.md").read_text()
    offered = set(re.findall(r"`references/([a-z-]+\.md)`", skill))
    on_disk = {p.name for p in (ROOT / "skills/code-rigor/references").glob("*.md")}
    assert offered == on_disk, f"offered-not-on-disk {offered - on_disk}, on-disk-not-offered {on_disk - offered}"

    review = (ROOT / "skills/code-rigor-review/SKILL.md").read_text()
    assert "`../code-rigor/references/" in review, "review lost its pointer to the references"


def test_no_vague_verbs():
    """The skill bans "check" and "consider" where a directive applies. The ban
    holds for the skill's own text, in both skills and every reference."""
    allowed = ("complexity checks", "coverage checks", "weaken a check", "Do not use \u201ccheck")
    verb = re.compile(r"\b(check|consider)(s|ed|ing)?\b", re.IGNORECASE)
    offences = [
        f"{path.name}:{number}: {line.strip()}"
        for path in SKILL_DOCS
        for number, line in _lines(path)
        if verb.search(line) and not any(a in line for a in allowed)
    ]
    assert not offences, offences


def test_no_hedges():
    """A hedge converts a rule into a suggestion. Rules state their exception or
    state none."""
    hedge = re.compile(r"when practical|when possible|if possible|where appropriate|as needed", re.IGNORECASE)
    offences = [
        f"{path.name}:{number}: {line.strip()}"
        for path in SKILL_DOCS
        for number, line in _lines(path)
        if hedge.search(line)
    ]
    assert not offences, offences


def test_one_spelling_per_directive():
    """"Do NOT" was a second spelling of the defined directive "Do not"."""
    offences = [
        f"{path.name}:{number}" for path in SKILL_DOCS
        for number, line in _lines(path) if "Do NOT" in line
    ]
    assert not offences, offences


def test_terms_are_defined_once():
    """Terms in code-rigor/SKILL.md are the single vocabulary. A bold definition
    of the same word anywhere else is a second source of truth."""
    skill = (ROOT / "skills/code-rigor/SKILL.md").read_text()
    terms = set(re.findall(r"^- \*\*([a-z ]+)\*\* —", skill, re.MULTILINE))
    assert terms, "Terms section not found"
    offences = [
        f"{path.name}: redefines {word!r}"
        for path in SKILL_DOCS
        if path != ROOT / "skills/code-rigor/SKILL.md"
        for word in re.findall(r"^- \*\*([a-z ]+)\*\* —", path.read_text(), re.MULTILINE)
        if word in terms
    ]
    assert not offences, offences
