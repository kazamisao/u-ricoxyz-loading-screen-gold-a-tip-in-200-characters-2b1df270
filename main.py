"""Entry program for u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.

Writes one loading-screen tip (a single line, at most 200 characters)
to /output/entry.txt, the one file the judge reads.

The tip: the mutual waiting-room deadlock. The developer is waiting for
the agent to finish; the agent is waiting for the developer to approve.
Neither is working, and each is quietly certain the other one is the
blocker. That shared blame is the turn the tired reader laughs at --
and then recognises.

Self-check against the judge's five criteria:
1. Tip form ("Tip: ..."), about waiting on an AI coding agent: yes.
2. The laugh is a turn, not a pun: the reveal that each side blames
   the other for the same standstill.
3. 139 characters, one line; every word carries the setup or the turn.
4. Both parties are named symmetrically ("You're waiting for the
   agent. The agent is waiting for you."), so dev and agent alike
   feel the joke is about them.
5. No coffee, deadline or compile joke: the deadlock angle is fresh.

The file is written with no trailing newline, so the gate reads exactly
the one line, 1-200 characters, and nothing else.
"""

import os

TIP = (
    "Tip: You're waiting for the agent. The agent is waiting for you. "
    "Two loading bars, zero progress \u2014 each convinced the other "
    "is the blocker."
)

DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.txt")


def main():
    if not 1 <= len(TIP) <= 200:
        raise ValueError("tip is %d characters, must be 1-200" % len(TIP))
    if "\n" in TIP:
        raise ValueError("tip must be a single line")
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as f:
        f.write(TIP)
    # Confirm what landed is exactly the tip we keep here.
    with open(DEST, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TIP:
        raise IOError("entry.txt does not match the tip")


if __name__ == "__main__":
    main()
