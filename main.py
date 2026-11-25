#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes exactly one self-roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default: /output/entry.txt) and prints it.

The roast is a single self-owning line: my agent tries to roast
itself, apologizes halfway, files a complaint about the
harassment, and asks me to approve the complaint — the endless
caveat and the permission loop, turned on itself. Deterministic:
a fixed string, no clock, randomness, network or
environment-dependent behaviour.
"""

import os

ROAST = (
    "My agent tried to roast itself, apologized mid-sentence, "
    "filed a complaint about the harassment, and asked me to approve it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = ROAST
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, "entry must be 1-140 characters"
    assert line.strip(), "entry must not be only whitespace"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
