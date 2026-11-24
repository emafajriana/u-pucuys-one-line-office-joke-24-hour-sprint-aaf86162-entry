"""One-Line Office Joke — make.fun entry.

Writes one joke (<= 200 characters) about office life. Output goes to
/output/entry.txt by default, or to $MAKEFUN_OUTPUT_DIR/entry.txt when
that variable is set.
"""

import os
import sys

# The joke (81 characters, one line, no trailing newline).
# Setup: the office fridge, a sandwich from 2019. Punchline: it has
# more tenure than half the team — the absurd-but-recognisable twist
# lands at the very end.
LINE = "The office fridge holds a sandwich from 2019 with more tenure than half the team."


def output_path():
    """Resolve the output file path from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def verify(path):
    """Read the file back and enforce the competition gate: UTF-8 text,
    1 to 200 characters, not only whitespace, exactly one line."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars, got %d" % len(text)
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text == LINE, "entry does not match the chosen line"
    return text


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    text = verify(path)
    print("wrote %s (%d chars)" % (path, len(text)))
    return path


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print("verification failed: %s" % exc, file=sys.stderr)
        sys.exit(1)
