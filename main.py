"""Texts From Your Future Self — make.fun entry.

Deterministic, no network, no randomness: writes one fixed funny text
message from the writer's future self to /output/entry.txt.
"""

import os

ENTRY = (
    "It's you from 2036. Stop saying sorry to the plant \u2014 it's fine. "
    "It outlived your gym membership, two diets, and three cracked phones. "
    "Water yourself instead."
)


def main() -> None:
    # Self-check the competition gate before writing: 1-200 characters,
    # non-blank, single text message (output unchanged).
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
