#!/usr/bin/env python3
"""ai-happy-01 entry: copy the joyful golden-retriever puppy image
(entry.png, sitting next to this script) into the output directory.

Python standard library only. Deterministic: the output is a byte-for-byte
copy of entry.png, so repeated runs produce identical results.
"""

import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_NAME = "entry.png"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        print(f"error: {SOURCE} not found", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, OUTPUT_NAME)
    shutil.copyfile(SOURCE, dest)
    # Verify the copy is byte-identical to the source.
    if _sha256(SOURCE) != _sha256(dest):
        print("error: output does not match source", file=sys.stderr)
        return 1
    print(f"Wrote {dest} ({os.path.getsize(dest)} bytes, sha256 verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
