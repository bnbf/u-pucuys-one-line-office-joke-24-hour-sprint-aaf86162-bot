"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to entry.txt in the
output directory the harness provides (MAKEFUN_OUTPUT_DIR, else /output).
The sealed scorer checks entry.txt is UTF-8 text of 1 to 200 characters.
"""

import os

# The joke: a meeting that should have been an email, inverted — the
# compromise is having both. One sentence, 113 characters.
JOKE = (
    "This meeting could have been an email, but the email would have "
    "become a meeting, so we compromised and did both."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
