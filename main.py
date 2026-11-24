"""Weirdest Job Title: Blind Judge Showdown -- make.fun entry.

A single weird job title, 60 characters or fewer and nothing else:
Senior Vice President of Apologising to the Printer. No sentence,
no punctuation, just the title. This script checks that the title
is a single bare line within the limit, prints it, and stores it
in /output/entry.txt for the judges to read.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

# The job title itself: bare, capitalised, no punctuation at all.
LINE = "Senior Vice President of Apologising to the Printer"

MAX_CHARS = 60
OUTPUT_PATH = "/output/entry.txt"

FORBIDDEN_MARKS = (".", "!", "?", ":", ";")


def validate(line):
    """Check that the line is one bare job title within the limit."""
    if not isinstance(line, str):
        raise ValueError("job title must be text")
    if not line or line != line.strip():
        raise ValueError("job title must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("job title must not contain a line break")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "job title is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if any(mark in line for mark in FORBIDDEN_MARKS):
        raise ValueError("job title must carry no sentence punctuation")
    if not line[0].isupper():
        raise ValueError("job title must start with a capital letter")
    return line


def store(line):
    """Print the job title and save it to the entry file."""
    print(line)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main():
    # Validate first, so only a well-formed title is ever stored.
    store(validate(LINE))


if __name__ == "__main__":
    main()
