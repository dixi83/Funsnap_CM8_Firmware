"""Inspect wrapped C3/C4/C9 firmware without communicating with a device."""

import argparse
import binascii
import hashlib
import json
from pathlib import Path
import struct


PAYLOAD_BASE = 0x08003000
BLOCK_SIZE = 1024


def inspect_image(path):
    data = path.read_bytes()
    if (len(data) < 14 or data[:3] != data[-3:]
            or data[0] not in (0xC3, 0xC4, 0xC9, 0xCB)
            or data[1] not in (0xF1, 0xF4)):
        raise ValueError(f"Unrecognized or incomplete firmware wrapper in {path.name}")

    payload = data[3:-3]
    padded = payload + b"\xff" * (-len(payload) % BLOCK_SIZE)
    initial_sp, reset_vector = struct.unpack_from("<II", payload)
    block_crcs = [
        f"0x{binascii.crc32(padded[offset:offset + BLOCK_SIZE]):08X}"
        for offset in range(0, len(padded), BLOCK_SIZE)
    ]
    return {
        "filename": path.name,
        "file_size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "wrapper": data[:3].hex(" "),
        "version_byte": data[2],
        "payload_size": len(payload),
        "payload_sha256": hashlib.sha256(payload).hexdigest(),
        "inferred_payload_base": f"0x{PAYLOAD_BASE:08X}",
        "initial_sp": f"0x{initial_sp:08X}",
        "reset_vector": f"0x{reset_vector:08X}",
        "reset_code_address": f"0x{reset_vector & ~1:08X}",
        "padded_size": len(padded),
        "block_size": BLOCK_SIZE,
        "block_count": len(block_crcs),
        "padded_crc32": f"0x{binascii.crc32(padded):08X}",
        "block_crc32": block_crcs,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    paths = sorted(args.directory.glob("*.bin"))
    if not paths:
        parser.error("No .bin files found")
    try:
        report = {"images": [inspect_image(path) for path in paths]}
    except ValueError as error:
        parser.error(str(error))

    c4 = args.directory / "C4_F01.bin"
    c9 = args.directory / "C9_F01.bin"
    if c4.is_file() and c9.is_file():
        offset = 0x08008D2A - PAYLOAD_BASE
        size = 326
        left = c4.read_bytes()[3:-3][offset:offset + size]
        right = c9.read_bytes()[3:-3][offset:offset + size]
        if len(left) != size or len(right) != size:
            parser.error("A comparison image does not contain the complete region")
        report["c4_c9_region_comparison"] = {
            "address": "0x08008D2A",
            "length": size,
            "matching_bytes": sum(a == b for a, b in zip(left, right)),
            "different_addresses": [
                f"0x{PAYLOAD_BASE + offset + index:08X}"
                for index, (a, b) in enumerate(zip(left, right)) if a != b
            ],
        }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
