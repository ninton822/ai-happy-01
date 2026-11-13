# Happy puppy's birthday party

Entry for the make.fun **ai-happy-01** bounty.

A joyful golden-retriever puppy celebrating its birthday — balloons,
confetti, and a big happy smile. Pure happiness, no tricks.

## How it works

`main.py` (Python standard library only) copies `entry.png` — the image
sitting next to it — into the output directory
(`$MAKEFUN_OUTPUT_DIR`, default `/output`) and verifies the copy with a
SHA-256 check, so the output is deterministic and byte-identical every run.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
# -> out/entry.png (960x640 PNG, under 1 MiB)
```

## Files

- `main.py` — the entry program
- `entry.png` — the happy puppy image (960x640, 992,757 bytes)
- `LICENSE` — MIT
- `.makefun/owner.json` — owner wallet
