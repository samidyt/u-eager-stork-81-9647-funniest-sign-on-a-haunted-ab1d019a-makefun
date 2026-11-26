"""Funniest Sign on a Haunted Server Room Door.

Writes one line -- the funniest sign for the door of a haunted server
room -- to /output/entry.txt (program/v1).
"""

import os

ENTRY = "DO NOT REBOOT: the ghost in Rack 7 is mid-update and he has root. Knock twice. He is the firewall now."

def main() -> None:
    if not (1 <= len(ENTRY) <= 120):
        raise SystemExit(f"entry must be 1-120 chars, got {len(ENTRY)}")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
