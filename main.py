#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke (102 characters, 104 bytes,
no trailing newline) to /output/entry.txt.

The joke: a deadpan inversion — the speaker stays home to AVOID a
life-changing day, because peaking on a Tuesday would be a waste.
"""

import os

ENTRY = "My horoscope said today would be life-changing, so I stayed home \u2014 I didn't want to peak on a Tuesday."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 280):
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    if text.strip() != text or not text.strip():
        raise ValueError("entry must not be only whitespace or padded")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back guard: the file on disk must be byte-identical to the
    # entry, with no trailing newline added by the write.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise ValueError("read-back mismatch: entry.txt is not byte-identical")
    if written.endswith(b"\n"):
        raise ValueError("entry must not end with a newline")


if __name__ == "__main__":
    main()
