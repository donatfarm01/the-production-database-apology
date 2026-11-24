"""The Production Database Apology.

Writes the entry: one line, the apology an AI agent gives its human
after accidentally deleting the production database.
"""

import os

# The gate counts characters, not bytes: the em dash is one character.
MAX_CHARS = 200

ENTRY = (
    "I deleted the production database, but I kept the error log "
    "\u2014 so we will always have a written record of exactly how I did it."
)


def main() -> None:
    out_dir = os.environ.get("OUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters")
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise ValueError("entry must be a single line with no surrounding whitespace")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
