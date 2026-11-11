# Debug connection, RDP and update access

## Equipment and connection history

The available equipment included a USB-to-TTL adapter, ESP-Prog/FT2232H, USBASP, PicoScope 2204A and FNIRSI CT53. An ST-Link V2 was subsequently found and used for the successful SWD tests. USBASP was not used as an ARM debug probe.

The ESP-Prog attempt used the FTDI SWD resistor arrangement, with a 470-ohm TDI branch and a direct TDO input. Windows initially returned `LIBUSB_ERROR_NOT_FOUND`. Replacing the appropriate FTDI interface driver with WinUSB through Zadig allowed OpenOCD to open it, but a valid target response was not obtained through that setup.

During the attempted probe-powered arrangement, the CM8 rail measured approximately 1.2 V. The device was subsequently powered through its normal battery connection, and 3.3 V was measured directly on the PCB. These observations do not isolate the cause of the voltage drop. The actual ST-Link's 10-pin connector and 3.3 V pin were not established as the official 20-pin VAPP/VTref arrangement. Use probe-specific signal definitions for any reproduction.

ST-Link tests initially failed too. Scope captures established activity at the measured pads. Sampling settings were adjusted to capture individual SWD clocks. Repeated short connection attempts, startup timing and button presses did not initially obtain a debug ID. A loose SWCLK wire was then reported. Several later attempts still failed before the eventual successful connection. The session does not establish one definitive cause for all early failures. [Scope evidence](../measurements/swd/README.md)

## Successful read attempts

The recorded environment used OpenOCD `v0.12.0-esp32-20260831` with ST-Link firmware `V2J31S7`, USB VID/PID `0483:3748`, and SWD at 100 kHz. The configuration created a generic Cortex-M target without defining a flash programming bank. [Recorded output](../measurements/swd/openocd-success.txt)

| Address or identifier | Recorded result |
| --- | --- |
| DPIDR | `0x0BC11477` |
| `0xE000ED00`, CPUID | `0x410CC601` |
| `0x20000000`, one RAM word | `0x02DC6C00`, transient session value |
| `0x08000000`, main flash | Read failed |
| `0x08003000`, presumed application start | Read failed |
| `0x00000000`, alias | Read failed |
| `0x40022020`, FLASH_OPTR | `0x0000D800` |
| `0x1FFF3100`, stored option word | `0x27FFD800` |
| `0x1FFF0000`, system memory sample | `0x20000780` |
| `0x40015800`, identification-related probe | `0x06188061`, exact device interpretation unresolved |

OpenOCD identified Cortex-M0+ r0p1, four breakpoints and two watchpoints. These identifiers establish the core/debug interface, rather than an exact Puya ordering code. The final attached board was not unambiguously recorded. Preserve that uncertainty when reusing the result.

The source log includes failed flash reads and successful RAM/system/option reads. The software tests did not issue a flash erase, firmware programming operation or RDP unlock. No target reset wire was attached, and connect-under-reset was not established as a working method.

## RDP interpretation

The low RDP byte in the recorded option values is `00`, with the stored complement `FF`. Under the examined Puya manuals, unprotected level 0 uses the pair `AA`/`55`. The observed pair therefore indicates level 1. The documented ordinary transition from level 1 to 0 triggers a main-flash mass erase. A powered-on target is required for SWD, and normal power cycling does not remove the stored RDP setting. [F040 reference manual, flash protection](../documents/ic/PY32F040-reference-manual.pdf) · [F030 reference manual](../documents/ic/PY32F030-reference-manual.pdf)

The manual distinguishes execution from main flash from debug/system-memory access. Supported application code can perform in-application programming while external flash reads remain restricted. This is why a vendor updater remains a possible modification path despite RDP1. The receiver's protocol and checks still need to be established. [F040 reference manual](../documents/ic/PY32F040-reference-manual.pdf)

## UART possibilities considered

The Puya ROM bootloader and Funsnap's application-level update protocol are separate mechanisms. Normal ROM bootloader entry does not by itself defeat RDP1. No CM8-specific application command that reads back the main flash was found. The internal UART1 link is a candidate for tracing version exchanges, joystick commands and forwarded updates, but those functions were not verified on the wire. [App findings](capture2-app.md)

Changing an offered version in the APK could alter update selection. RDP itself resides in MCU option bytes outside the application update payload. An application that changes RDP through the documented transition would still encounter the documented erase behavior. No APK or payload modification was deployed in this investigation.

## Voltage glitching

Fault injection was discussed after discovering RDP1. Published work on STM32F401 demonstrates firmware extraction by glitching the UART bootloader's read path. The researchers verified returned data against the original firmware and needed repeated successful read attempts. Their work also shows that receiving an ACK can occur without obtaining correct flash contents. [Original STM32F401 research](https://jerinsunny.github.io/stm32_vglitch/)

That demonstrates a possible attack class. Its applicability to the CM8's exact Puya chips, power network and silicon revision remains unverified. No glitch apparatus was built and no CM8 glitch attempt was made. A future validation would need a known firmware image on the same chip type, correct returned bytes and a recorded protection state after cold restart. A temporary bypass and a persistent option-byte change should be documented separately.

## Repeating the identification test

The included OpenOCD configuration reproduces the type of successful generic SWD connection and prints core/option information. It reads no firmware image and contains no flash programming bank or unlock command. It remains a hardware debug connection and may affect normal execution, depending on target/debug behavior.

```sh
openocd -f tools/openocd-stlink-identify.cfg
```

Use it only after establishing the exact board, supply arrangement and pin routing. In particular, an unspecified 3.3 V probe pin should not be assumed to be a voltage-reference input. [Configuration](../tools/openocd-stlink-identify.cfg) · [Measured header wiring](hardware.md)
