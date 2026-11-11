# Sources, provenance and evidence

The technical record was reconstructed from the full research conversation, saved command output, photographs, measurements and downloaded files. Later corrections take precedence over superseded interpretations. Public documents and extracted update assets retain their original authorship. The repository adds analysis and indexing around that material.

## Evidence conventions

| Evidence type | Meaning |
| --- | --- |
| Owner report | A described observation, such as tilt behavior or displayed versions |
| Photograph | Visible marking or physical layout, tied to the photographed unit |
| Continuity measurement | Owner-reported electrical connection, including the corrected pin numbers |
| Tool output | Retained software measurement, such as a register read or APK disassembly |
| Binary inference | Interpretation of instructions, vectors or register addresses |
| Hypothesis or proposed experiment | An unresolved explanation or action that was discussed |

The owner unit's unidentified F01 target, final debug target identity, exact angle and Bluetooth radio chip are deliberately left unresolved. Runtime network data, a UART protocol capture, a modified APK test and a successful custom firmware upload were not produced.

## Archived primary material

[`sources.json`](../sources.json) records the local path, source URL or owner provenance, byte size and SHA-256 for photographs, annotations, scope captures, public documents and original firmware assets. [`apk-hashes.json`](../analysis/apk/apk-hashes.json) identifies the two examined APK samples. [`firmware-inventory.json`](../analysis/apk/firmware-inventory.json) inventories every firmware asset in the v2.6.74 sample, including those outside the C3/C4/C9 comparison set.

The six JPEG files are copies of the owner's original camera files, using descriptive archive names. The annotated headers and scope screenshots are the owner-supplied attachments. The scope CSVs preserve original semicolon delimiters, decimal commas and units. OpenOCD output was recovered from tool records, with local session metadata and USB serial identifiers excluded.

The APK method text files are analysis outputs retained from the original session. They include overlapping selections and obfuscated method names. The ARM region disassembly and inspection JSON were regenerated from the archived bytes during assembly to check the stated offsets and comparison result.

## Public reference entry points

- [CM8 FCC filing](https://fccid.io/2APVH-CM8)
- [Puya PY32F040C18T6 product page](https://www.puyasemi.com/gongye/2827.html)
- [OpenPuya PY32F040 SDK and startup code](https://github.com/OpenPuya/PY32F040_Firmware)
- [OpenPuya PY32F4xx SDK and startup code](https://github.com/OpenPuya/PY32F4xx_Firmware)
- [Arm CMSIS startup file documentation](https://arm-software.github.io/CMSIS_6/main/Core/startup_c_pg.html)
- [OpenOCD FTDI SWD resistor arrangement](https://github.com/arduino/OpenOCD/blob/master/tcl/interface/ftdi/swd-resistor-hack.cfg)
- [Espressif ESP-Prog documentation](https://documentation.espressif.com/espressif-esp-dev-kits/en/latest/other/esp-prog/user_guide.html)
- [ST-LINK/V2 hardware manual](https://www.st.com/resource/en/user_manual/um1075-stsw-link007.pdf)
- [Arm debug-interface specification used for SWD ACK interpretation](https://documentation-service.arm.com/static/622222b2e6f58973271ebc21)
- [STM32F401 voltage fault-injection research](https://jerinsunny.github.io/stm32_vglitch/)
- [Fraunhofer STM32 firmware-protection research](https://www.aisec.fraunhofer.de/en/FirmwareProtection.html)
- [Owner's CM8_Action_Gateway](https://github.com/dixi83/CM8_Action_Gateway)

The absence of an independently verified CM8 replacement-firmware project is a search outcome from this investigation, rather than a claim that such work cannot exist.
