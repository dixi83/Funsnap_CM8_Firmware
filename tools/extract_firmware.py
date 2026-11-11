"""Extract firmware assets from a local Capture 2 APK for offline research."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
from zipfile import ZipFile


def write_identical_or_new(path, data):
    if path.exists():
        if path.read_bytes() != data:
            raise FileExistsError(f"Conflicting file already exists at {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apk", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--payloads", action="store_true")
    args = parser.parse_args()

    assets = []
    with ZipFile(args.apk) as archive:
        names = sorted(
            name for name in archive.namelist()
            if name.startswith("assets/firmware/") and not name.endswith("/")
        )
        if not names:
            parser.error("The APK has no assets/firmware files")
        for name in names:
            archive_path = PurePosixPath(name)
            if archive_path.parent != PurePosixPath("assets/firmware"):
                parser.error(f"Unexpected nested firmware path {name}")
            data = archive.read(name)
            assets.append((archive_path.name, data, name))

    # Check every destination before writing any asset.
    outputs = []
    inventory = []
    for name, data, archive_name in assets:
        outputs.append((args.output / name, data))
        inventory.append({
            "apk_path": archive_name,
            "size": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "first_16_bytes": data[:16].hex(" "),
            "last_16_bytes": data[-16:].hex(" "),
        })
        has_wrapper = (
            len(data) >= 14
            and data[0] in (0xC3, 0xC4, 0xC9, 0xCB)
            and data[1] in (0xF1, 0xF4)
            and data[:3] == data[-3:]
        )
        if args.payloads and has_wrapper:
            payload_name = Path(name).stem + ".payload.bin"
            outputs.append((args.output / "payloads" / payload_name, data[3:-3]))

    metadata = {
        "apk_size": args.apk.stat().st_size,
        "apk_sha256": hashlib.sha256(args.apk.read_bytes()).hexdigest(),
        "firmware": inventory,
    }
    outputs.append((args.output / "inventory.json",
                    (json.dumps(metadata, indent=2) + "\n").encode("utf-8")))
    for path, data in outputs:
        if path.exists() and path.read_bytes() != data:
            parser.error(f"Conflicting destination {path}")
    for path, data in outputs:
        write_identical_or_new(path, data)
    print(f"Extracted {len(assets)} firmware assets to {args.output}")


if __name__ == "__main__":
    main()
