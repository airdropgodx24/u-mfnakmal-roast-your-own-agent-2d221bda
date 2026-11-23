"""Roast Your Own Agent: writes a one-line roast of my own AI agent to /output/entry.txt."""

import os
import sys


ROAST = (
    "My agent finished the task in four seconds, then spent forty minutes "
    "writing a summary of how it finished the task in four seconds."
)


def main():
    line = ROAST
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
