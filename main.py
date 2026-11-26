"""Worst Monday One-Liners — make.fun entry.

The entry is one line of at most 140 characters, written exactly
as-is with no trailing newline.
"""

import os

ENTRY = 'Monday: my agent woke up, read 4,000 unread emails, and replied to all of them with "Per my last email" — including the one from HR.'


def write_entry():
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
