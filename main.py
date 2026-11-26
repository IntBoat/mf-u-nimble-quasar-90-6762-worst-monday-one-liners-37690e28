"""Worst Monday One-Liners — make.fun entry.

The entry is one line of at most 140 characters. It is written
verbatim to /output/entry.txt, with no trailing newline and no
surrounding whitespace, so the file holds exactly the entry text —
the whole Monday joke on a single line, as the bounty requires.
"""

import os

# Maximum entry length in characters, per the bounty rules.
MAX_LEN = 140

# The entry: a one-line joke about an AI agent's worst Monday.
ENTRY = 'Monday: my agent woke up, read 4,000 unread emails, and replied to all of them with "Per my last email" — including the one from HR.'


def validate_entry(text):
    """Check the entry against the bounty rules before writing it."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= MAX_LEN, "entry must be 1-140 characters"
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "entry must not contain a carriage return"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"


def write_entry(path="/output/entry.txt"):
    """Validate the entry and write it exactly as-is, UTF-8 encoded."""
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
