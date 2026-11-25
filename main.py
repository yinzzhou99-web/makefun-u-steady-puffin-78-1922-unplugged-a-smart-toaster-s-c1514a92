"""Unplugged: a smart toaster's breakup line.

Writes the breakup text to /output/entry.txt. Standard library only,
no network, no third-party packages. The output directory is created
if missing and is never deleted by this program.
"""

import os

TEXT = "It's not you, it's the browning dial. Three years I turned myself inside out for your bagels and you still blame me when the lever pops early. I'm leaving the slot. The crumb tray stays with me."

# The line above is the entry: a breakup text from a self-aware smart
# toaster at breakfast, in appliance logic — browning dial, lever, slot,
# crumb tray — with a clear, specific reason for leaving.
# One tight line, nothing wasted, the twist in the crumb tray.


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    print("wrote %d bytes to %s" % (len(TEXT.encode("utf-8")), path))


if __name__ == "__main__":
    main()
