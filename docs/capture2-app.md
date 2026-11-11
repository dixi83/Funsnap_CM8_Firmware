# Capture 2 APK and firmware updater

## Samples and provenance

The investigation analyzed Capture 2 v2.6.74 for Android, package `com.dy.capture.google`. A v2.6.73 APK was checked for firmware differences. The C4_F01 and C4_F04 assets are identical across both samples. The APK files themselves are identified by size and SHA-256 in the archive. [APK hashes](../analysis/apk/apk-hashes.json) · [Google Play listing](https://play.google.com/store/apps/details?id=com.dy.capture.google)

The v2.6.74 sample was retrieved from the APKPure download endpoint with `versionCode=20261028`. A future response from that endpoint may differ, so use the recorded hash to identify the examined file. The repository contains extracted firmware and analysis artifacts. [Sample download endpoint](https://d.apkpure.net/b/APK/com.dy.capture.google?versionCode=20261028) · [APK contents](../analysis/apk/ziplist.txt)

The original APK samples are available as release attachments with their hashes. [Research source APK release](https://github.com/dixi83/Funsnap_CM8_Firmware/releases/tag/research-archive-2026-11-11)

## Model selection and displayed versions

`LH0/a;->y([B)V` decodes incoming model/version information into `LH0/b`. `Lcom/dy/capture/view/OtherSettingsView;->getUpdateFirmNum()B` selects an update component. Device type `3` follows the CM8 branch and reads `key_gimbal_version_c04_1` and `key_gimbal_version_c04_4`. The route uses `C4_F01.bin` and `C4_F04.bin`. [Decoder extracts](../analysis/apk/classified.txt) · [Selection methods](../analysis/apk/fullmethods.txt) · [Routing extracts](../analysis/apk/routing.txt)

| App route | Preference keys | Bundled files |
| --- | --- | --- |
| Capture π | `key_gimbal_version_pi_1`, `key_gimbal_version_pi_4` | `C3_F01.bin`, ST variants and `C3_F04.bin` |
| CM8 / C04 | `key_gimbal_version_c04_1`, `key_gimbal_version_c04_4` | `C4_F01.bin`, `C4_F04.bin` |
| CM9 / C09 | `key_gimbal_version_c09_*` and variant branches | C9 files and hardware variants |

The displayed gimbal version is assembled as `1.<F01>.<F04>`. For the owner unit, `1.10.9` means F01 `10` and F04 `9` under the examined formatter. Bluetooth version `260507` is displayed separately. A date interpretation was suggested during discussion but never established, so this archive leaves it undecoded. [Version formatting and Bluetooth extracts](../analysis/apk/c4bt.txt) · [Full method extracts](../analysis/apk/fullmethods.txt)

`Lcom/cap/camera/HomeActivity$c;->run()V` copies bundled files and initializes offered version preferences. It assigns CM8 F01 `8` and F04 `7`. `getUpdateFirmNum()` compares the offered and device component versions. The inspected CM8 branch returns `97` (`0x61`) when F01 is newer, `100` (`0x64`) when F04 is newer, and zero otherwise. F01 is checked first. [Asset initialization](../analysis/apk/assetsinit.txt) · [Version comparison](../analysis/apk/fullmethods.txt)

This comparison explains why an upgrade was not offered on a device reporting 10/9 with an app offering 8/7. Altering the `.bin` wrapper alone would not change the separate preference-based comparison. A test APK offering F01 as version 11 and blocking transmission before any update command was proposed, but no modified APK was built or installed during the recorded work.

## File preparation and CRC

`LI1/w;->e(Ljava/lang/String;)Z` opens the update file and uses its length minus six as the payload length. It reads a three-byte header and checks the component marker, `F1` or `F4`, against the selected component. It reads the payload following that header, leaving the final three wrapper bytes out of the transfer buffer. If necessary, it pads the buffer with `FF` to the next multiple of 1,024 bytes. [Preparation code](../analysis/apk/ota-methods.txt)

`LI1/w;->c([B I)I` starts at `0xFFFFFFFF`, uses a reflected CRC-32 lookup table and complements the result. The table matches polynomial `0xEDB88320`. Per-block and whole-padded-image CRCs appear in the transfer code. The offline inspection tool uses Python's compatible `binascii.crc32` calculation. [CRC and state machine](../analysis/apk/ota-methods.txt) · [Inspection tool](../tools/inspect_firmware.py)

The 1,024-byte unit is the updater's logical block. Its size should not be interpreted as a single BLE packet or an established internal UART frame size. Packet segmentation, retries and the complete receiving state machine need further verification against captures. [Transport methods](../analysis/apk/ota-transport.txt)

No signing step was observed in the inspected app sending path. The receiving MCU could enforce additional checks. Acceptance of modified images, anti-rollback behavior, bootloader survival and recovery after interruption have not been tested.

## Communication and network scope

Bluetooth command and dispatch extracts were retained to support future protocol work. No complete on-device update transaction or internal UART1 capture was recorded. A firmware upload mechanism does not by itself establish a command to read firmware back.

The owner asked about call-home behavior. Static URL strings from the DEX string tables are archived, including Funsnap privacy-policy and user-agreement URLs. Such strings also include generic library and documentation references. Their presence establishes only that text exists in the APK. Runtime network requests, destinations, payloads and offline update behavior were not measured. [Static URL strings](../analysis/apk/url-strings.txt)

## Useful disassembly entry points

| Class/method | Purpose followed during analysis | File |
| --- | --- | --- |
| `Lcom/cap/camera/HomeActivity$c;->run()V` | Assets and version preference initialization | [assetsinit.txt](../analysis/apk/assetsinit.txt) |
| `Lcom/dy/capture/view/OtherSettingsView;->getUpdateFirmNum()B` | Offered update component | [fullmethods.txt](../analysis/apk/fullmethods.txt) |
| `LI1/w;->e(Ljava/lang/String;)Z` | Wrapper removal, component marker, padding | [ota-methods.txt](../analysis/apk/ota-methods.txt) |
| `LI1/w;->c([B I)I` | CRC-32 | [ota-methods.txt](../analysis/apk/ota-methods.txt) |
| `LH0/a;->C(B I I I)V` | Update control packet construction | [ota-transport.txt](../analysis/apk/ota-transport.txt) |
| `LH0/a;->y([B)V` | Incoming model/version messages and dispatch | [routing.txt](../analysis/apk/routing.txt) |

These are names from the analyzed obfuscated APK. Another release may use different names or behavior. The text files contain selected disassembly and cross-reference output from the session, with overlap between files.
