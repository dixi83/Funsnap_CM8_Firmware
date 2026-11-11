# Offline analysis tools

Both Python tools use the Python 3 standard library. Run them from a clone of this repository. They operate on local files and have no device communication.

## Extract firmware from an APK

```sh
python tools/extract_firmware.py /path/to/capture.apk /path/to/extracted
```

This extracts the immediate files under `assets/firmware/`, writes a SHA-256 inventory and records the APK hash. The optional `--payloads` flag also saves wrapper-stripped C3/C4/C9 payloads under `payloads/` for disassembly.

```sh
python tools/extract_firmware.py /path/to/capture.apk /path/to/extracted --payloads
```

Existing files are accepted when byte-identical. A conflicting destination causes an error. The optional payload extraction validates a matching three-byte wrapper, recognized model and F01/F04 component markers. Use those payloads for research with the documented memory base, rather than as full-chip backups.

## Inspect firmware and reproduce the comparison

```sh
python tools/inspect_firmware.py firmware/capture2-2.6.74
```

The JSON report includes wrapped and payload hashes, version markers, initial SP, reset vector, 1,024-byte padded size, per-block CRC-32 and the whole padded payload CRC. If the C4_F01 and C9_F01 files are present, it also compares 326 bytes at payload address `0x08008D2A`.

The assembled archive retains that tool's output at [analysis/firmware/inspection.json](../analysis/firmware/inspection.json). The local C4_F01 region disassembly was generated with Capstone 5.0.7 in little-endian Thumb/M-class mode, using base `0x08003000`, and is retained alongside it.

## OpenOCD identification

```sh
openocd -f tools/openocd-stlink-identify.cfg
```

The OpenOCD configuration is reconstructed from the successful session commands. It selects ST-Link SWD at 100 kHz, creates a generic Cortex-M target and attempts core/option-word reads. It defines no flash bank and performs no erase, unlock or firmware programming operation. It has not been rerun against the owner's hardware during archive assembly. [Connection history and measured pinout](../docs/debugging.md)

The successful session used the Espressif OpenOCD build `v0.12.0-esp32-20260831`. ST-Link transport names differ between OpenOCD builds. If a build does not support the selected `swd` transport with `interface/stlink.cfg`, consult that build's ST-Link configuration rather than assuming its target setup is equivalent.
