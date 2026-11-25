#!/usr/bin/env python3
"""Write the 3 AM commit message entry to the output directory.

Stdlib only. Reads the output dir from MAKEFUN_OUTPUT_DIR with a
fallback of /output, creates it if needed, and never deletes it.
"""

import os

# Verified: exactly 100 characters, within the 1-200 gate.
ENTRY = "fix: my 3am cleanup deleted prod; the error rate is now zero, which I am choosing to report as a win"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200) or not text:
        raise SystemExit("entry fails the 1-200 character gate")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
