#!/usr/bin/env python3
"""Validate the explicit public release manifest."""

from pathlib import Path
import subprocess
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
    extras = []
    if (root / ".git").is_dir():
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        actual = {line for line in result.stdout.splitlines() if line}
        extras = sorted(actual - expected)
        forbidden = sorted(
            path
            for path in actual
            if any(part in {"_build", "print-manual", "_marketing"} for part in Path(path).parts)
        )
    print(f"Manifest files: {len(expected)}")
    print(f"Missing: {missing}")
    print(f"Unexpected public files: {extras}")
    print(f"Forbidden private paths: {forbidden}")
    return 1 if missing or extras or forbidden else 0


if __name__ == "__main__":
    raise SystemExit(main())
