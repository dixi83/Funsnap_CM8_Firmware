# Research record

This technical record incorporates corrected observations from the discussion and retained files. Owner-reported behavior, photographed markings, continuity measurements, tool results and software inferences are distinguished throughout. The chronology covers the work performed on 9–10 November 2026.

## 9 November 2026

1. Searched for CM8 firmware work, teardown material and hardware rebrands. Located the CM8 FCC exhibits, VEVOR CM8 and Gadnic GIM00013. The owner's CM8_Action_Gateway was identified as an external ESP32 gateway by the same author.
2. Downloaded and statically examined Capture 2 for Android. Established the CM8 device-type branch, C4_F01/F04 assets, file sizes and wrapper bytes. Compared two APK samples and found the same C4 assets.
3. Investigated payload vectors, Thumb code, interrupt tables and peripheral addresses. Inferred application base `0x08003000`, M4/FPU code in F01 and M0+ code in F04. Proposed Puya F403/F040 family matches.
4. Defined the reported tilt problem from the owner's account. PF and L exhibited similar loss of compensation and upward joystick control before the mechanical limit. No calibrated angle measurement was made.
5. Followed an F01 v8 routine that uses ±25° in radians, state-dependent stores and angle differences. Its purpose remained unresolved.
6. Discussed upload behavior, missing update UI and call-home traffic. These were research questions, with runtime capture still outstanding.

## 10 November 2026

1. Recorded Gimbal Version `1.10.9` and Bluetooth Version `260507`. Traced the formatter and established F01 10 / F04 9 under the examined app logic. Both installed component numbers exceed the bundled 8/7 values.
2. Examined six owner photographs. Identified the panel's PY32F040C18T6 and DY-B03-02-V3 module, plus F030EF28 on the C03 motor board. Established that the photographed F030 cannot run the archived M4/FPU F01 image.
3. Compared C03 PCB markings with C3/C4 app routing. Confirmed C3 belongs to a different app route and preserved it for comparison. Found a close local C4_F01/C9_F01 routine match, reproduced as 324 matching bytes of 326 at `0x08008D2A`.
4. Followed a queued message construction near `0x08008D84`, with bytes `64 61 14 03` and CRC-8. The message meaning and physical transport remained unknown.
5. Recorded owner continuity measurements between visible boards over UART1 and from both four-pad headers to the SWD-capable MCU pins. Corrected the panel middle-pair pin numbers to 34/37.
6. Attempted ESP-Prog SWD and addressed the Windows driver error using Zadig/WinUSB. Recorded a rail collapse to about 1.2 V in the attempted probe-powered arrangement and later a normal 3.3 V PCB measurement.
7. Switched to ST-Link V2. Adjusted PicoScope acquisition settings and saved two CSV captures plus a PSDATA file. Early captures showed an incomplete reset sequence and unsuccessful request/response windows.
8. Tried repeated connections around power-up and button presses. A loose SWCLK wire was reported during troubleshooting. A later ST-Link connection at 100 kHz returned DPIDR `0x0BC11477` and Cortex-M0+ identification.
9. Read core, RAM, system-memory and option information. Main-flash reads failed. Recorded FLASH_OPTR `0x0000D800` and stored option word `0x27FFD800`, consistent with RDP1. No flashdump or ordinary RDP downgrade was performed.
10. Followed more of Capture 2's updater. Established wrapper removal, 1,024-byte padding and CRC-32 calculations. Proposed an instrumented version-check experiment, which was not executed.
11. Reviewed voltage-glitching literature. Found an applicable attack class demonstrated on STM32, while the corresponding Puya result remained unverified. Hardware fault injection was not attempted.
12. Ended active hardware investigation with the tilt behavior, installed firmware recovery and modified upload unresolved.

## Corrections retained in this archive

| Early interpretation | Evidence-led correction |
| --- | --- |
| CM8_Action_Gateway might be independent CM8 firmware work | Same owner, external ESP32 gateway |
| FCC Barrot radio identification might describe the owner's unit | Owner's later board has DY-B03-02-V3, exact radio silicon unresolved |
| C03 marking might directly select C3 firmware | Analyzed CM8 updater explicitly selects C4 |
| Photographed motor MCU might be the F01 target | F030 M0+ cannot run archived M4/FPU F01 v8 |
| Panel edge signals initially reported as pins 25/22 | Corrected by owner to pins 34/37 and annotated |
| ±25° constants might identify the symptom's limit | Axis and purpose unresolved, symptom angle unmeasured |
| Early lack of ACK might indicate RDP | Debug-port access and flash access are separate, later SWD works with flash restricted |
| Ordinary RDP unlock is the only possible route | Fault injection can bypass checks on other chips, Puya applicability unverified |

## Continuation

The most useful missing artifacts are a labelled complete hardware topology, a confirmed F01 target, the installed component images, both UART1 directions during version queries and tilt behavior, and a complete vendor update trace. Preserve board revision and target identity with every new measurement.

Any future firmware experiment should document the exact stock and patched hashes, changed instructions, selected component, device validation and recovery method. If glitching is pursued, validate successful returned bytes against a known image on an equivalent test chip before drawing conclusions about the CM8.

For new reports, include the visible CM8 model/revision, gimbal and Bluetooth versions, app version, mode, reproducible action, mechanical clearance, clear chip photographs and raw captures. Record estimated angles as estimates. A report with a confirmed different hardware revision is useful even if it has the same product name.
