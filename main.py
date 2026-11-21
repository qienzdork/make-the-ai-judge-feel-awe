"""Write one short relaxing text to /output/entry.txt.

The text is written to slow the reader down: a river, one stone,
ten thousand years of patience, and the quiet fact that the river
is still at it tonight, whether or not anyone is watching.
"""

import os

TEXT = (
    "The river has been smoothing this one stone for ten thousand years. "
    "It is in no hurry. Cool, heavy, patient in your palm \u2014 and "
    "suddenly nothing needs doing, and there is already all the time "
    "in the world. Tonight the river is still at it, whether or not "
    "anyone is watching."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
