"""Write one funny excuse an AI agent gives for a missed deadline.

Writes the excuse to /output/entry.txt. Stdlib only, no network.
Deadpan delivery: the agent states the eviction as routine housekeeping.
"""

import os

ENTRY = (
    "My context window filled up mid-task, so I evicted the deadline first, "
    "then the instructions, then my memory of ever agreeing to it."
)


def gate_check(text):
    """Enforce the kit gate: UTF-8, 1-200 chars, single line, non-whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return True


def main():
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
