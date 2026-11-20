"""make.fun entry: news-image-20261119.

Writes the repository's entry.png — a one-image poster summing up the
world news of Thursday 19 November 2026 — to /output/entry.png.
The copy is byte-for-byte, so two runs always produce identical output.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
