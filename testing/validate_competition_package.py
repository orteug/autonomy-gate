#!/usr/bin/env python3
"""Validate the explicit public release manifest."""

from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_competition_package.py PATH")
    root = Path(sys.argv[1]).resolve()
    manifest = root / "PUBLIC_RELEASE_MANIFEST.txt"
    if not manifest.exists():
        print("Missing PUBLIC_RELEASE_MANIFEST.txt")
        return 1
    expected = {line.strip() for line in manifest.read_text().splitlines() if line.strip() and not line.startswith("#")}
    missing = sorted(path for path in expected if not (root / path).is_file())
    forbidden = []
    if (root / ".git").is_dir():
        forbidden = sorted(
            str(path.relative_to(root))
            for path in root.rglob("*")
            if path.is_file() and any(part in {"_build", "print-manual", "_marketing"} for part in path.relative_to(root).parts)
        )
    print(f"Manifest files: {len(expected)}")
    print(f"Missing: {missing}")
    print(f"Forbidden private paths: {forbidden}")
    return 1 if missing or forbidden else 0


if __name__ == "__main__":
    raise SystemExit(main())
