"""Seventeen Syllables of Debugging — entry runner.

Reads the haiku from entry.txt, prints it, and writes it to
/output/entry.txt for the sealed scorer.
"""

import os

ENTRY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUTPUT_PATH = "/output/entry.txt"


def load_haiku():
    with open(ENTRY_PATH, "r", encoding="utf-8") as handle:
        return handle.read().strip("\n")


def validate(haiku):
    lines = [line for line in haiku.split("\n") if line.strip()]
    if len(lines) != 3:
        raise ValueError("haiku must be exactly three lines")
    if not 1 <= len(haiku) <= 200:
        raise ValueError("haiku must be 1 to 200 characters")
    return haiku


def deliver(haiku):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(haiku)


def main():
    haiku = validate(load_haiku())
    print(haiku)
    deliver(haiku)


if __name__ == "__main__":
    main()
