#!/usr/bin/env python3
"""Clone the pinned upstream and hydrate LFS pointers with SHA-256 verification."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
from pathlib import Path
import re
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".upstream/moe-blogpost"
URL = "https://huggingface.co/spaces/huggingface/moe-blogpost"
SHA = "ef70726e6f8b99d74298a16a4894340f288a58c2"


def main():
    if not DEST.exists():
        DEST.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", URL, str(DEST)], check=True)
        subprocess.run(["git", "-C", str(DEST), "checkout", SHA], check=True)
    actual = subprocess.check_output(["git", "-C", str(DEST), "rev-parse", "HEAD"], text=True).strip()
    if actual != SHA:
        raise SystemExit(f"Existing clone is at {actual}; expected {SHA}. Refusing to overwrite it.")
    names = subprocess.check_output(["git", "-C", str(DEST), "ls-files", "-z"]).decode().split("\0")

    def hydrate(name):
        path = DEST / name
        data = path.read_bytes()
        if not data.startswith(b"version https://git-lfs.github.com/spec/v1"):
            return 0
        expected = re.search(rb"oid sha256:([a-f0-9]{64})", data)[1].decode()
        size = int(re.search(rb"size (\d+)", data)[1])
        with urllib.request.urlopen(f"{URL}/resolve/{SHA}/{name}", timeout=120) as response:
            content = response.read()
        if len(content) != size or hashlib.sha256(content).hexdigest() != expected:
            raise RuntimeError(f"LFS integrity failure: {name}")
        path.write_bytes(content)
        return 1

    with ThreadPoolExecutor(max_workers=8) as pool:
        count = sum(pool.map(hydrate, filter(None, names)))
    print(f"Upstream pinned at {SHA}; hydrated {count} LFS assets")


if __name__ == "__main__":
    main()
