"""Small dependency-free structural check for the team skills bundle."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
errors = []
for relative in manifest["skills"]:
    skill = ROOT / relative / "SKILL.md"
    if not skill.is_file():
        errors.append(f"missing {relative}/SKILL.md")
    else:
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "name:" not in text.split("---", 2)[1]:
            errors.append(f"invalid frontmatter in {relative}/SKILL.md")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(manifest['skills'])} skills and plugin.json are present")
