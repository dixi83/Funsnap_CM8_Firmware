# Archived firmware analysis

## Image layout

The C4 assets have a three-byte model/component/version wrapper repeated at the beginning and end. The bytes between those wrappers contain recognizable little-endian ARM Cortex-M vectors and Thumb instructions. The updater uses that interior payload. Both images were analyzed with a payload base of `0x08003000`. [Updater preparation](../analysis/apk/ota-methods.txt) · [Firmware inventory](../analysis/apk/firmware-inventory.json)

| Property | C4_F01 v8 | C4_F04 v7 |
| --- | --- | --- |
| Asset size | 100,542 bytes | 32,218 bytes |
| Interior payload size | 100,536 bytes | 32,212 bytes |
| Wrapper | `C4 F1 08` | `C4 F4 07` |
| Initial SP | `0x200048A0` | `0x20001AD8` |
| Reset vector including Thumb bit | `0x08003145` | `0x080030D9` |
| Reset code address | `0x08003144` | `0x080030D8` |
| Inferred architecture | Cortex-M4 with floating-point instructions | Cortex-M0+ |
| Strong family candidate | Puya PY32F403 | Puya PY32F040 |

Family identification used the vector/interrupt layout, literal-loaded peripheral addresses and executable instruction set. Startup source and device manuals provide comparison material. The physical target of F01 remains unknown. Mapping F04 to the photographed panel is plausible, but the installed F04 v9 has not been read out. [PY32F403 startup source](https://github.com/OpenPuya/PY32F4xx_Firmware/blob/main/Projects/PY32F403-STK/Applications/FreeRTOS/FreeRTOS_EventGroup/MDK-ARM/startup_py32f403xx.s) · [PY32F040 startup source](https://github.com/OpenPuya/PY32F040_Firmware/blob/master/Projects/PY32F040-STK/Applications/FreeRTOS/FreeRTOS_EventGroup/MDK-ARM/startup_py32f040xx.s)

At the inferred load address, the update begins 12 KiB after main flash base. This indicates that the bundled image does not cover the initial flash region, where a bootloader may reside. The update asset also does not establish the location or contents of device calibration. A complete stock backup was never obtained.

## Candidate angle routine

An early investigation of `C4_F01.bin` v8 located a routine around `0x08008D2A` that uses float constants corresponding to +25° and −25° in radians. Store instructions at `0x08008DD8` and `0x08008EDC` were followed as writing a common field in different states. The function also calculates angle differences. Its axis, state meanings and connection to joystick/stabilization behavior remain unresolved. [Saved disassembly](../analysis/firmware/C4_F01-angle-region.txt)

The owner's observed angle was a visual estimate and was subsequently withdrawn as a numeric search target. The constants are retained as a code-navigation lead. They do not prove a measured limit or the cause of the reported behavior.

Comparison with C3_F01 variants did not establish a strong match for this region. In `C9_F01.bin`, **324 of 326 bytes** match C4_F01 at the same payload address starting at `0x08008D2A`. The archived binaries reproduce that local comparison. It establishes shared code in this region, while firmware interchangeability remains untested. [C4/C9 comparison](../analysis/firmware/inspection.json) · [Archived comparison assets](../firmware/capture2-2.6.74)

## Communication lead

Around `0x08008D84`, the F01 code constructs bytes `64 61 14 03`, adds a CRC-8 and queues a message. Queueing and CRC processing were followed during the session. The meaning, outgoing peripheral and physical destination remain unknown. A future investigation should trace the queue consumer to hardware register writes, then correlate those messages with a real UART capture. [Region disassembly](../analysis/firmware/C4_F01-angle-region.txt)

## Reproduce offline

Run the provided script from the repository root.

```sh
python tools/inspect_firmware.py firmware/capture2-2.6.74
```

It reports file/payload hashes, wrapper bytes, initial SP/reset vectors, padded sizes, per-block CRCs and the C4/C9 region comparison. For importing into Ghidra, obtain the payload using the extractor's optional payload output and select little-endian ARM Cortex-M/Thumb at `0x08003000`. Enter the reset routine at the reset-vector address with bit 0 cleared and preserve Thumb context. Treat vectors and literal pools as data where appropriate. [Tools](../tools/README.md)

## Remaining work

The next code-analysis step is tracing joystick input and stabilization correction through the actual installed firmware, then checking what reaches the axis controllers. A candidate patch should identify its affected component and state, reproduce the symptom on that version and have a recovery path. No validated patch, replacement source firmware, buildable CM8 motor controller or completed Ghidra project resulted from this investigation.
