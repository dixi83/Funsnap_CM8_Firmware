# Analysis artifacts

`apk/` preserves selected method disassembly and cross-reference output from the Capture 2 analysis. The source is the v2.6.74 APK identified in [apk-hashes.json](apk/apk-hashes.json). Files overlap because different selections were saved during investigation.

| File | Main use |
| --- | --- |
| [assetsinit.txt](apk/assetsinit.txt) | Bundled assets and offered version preferences |
| [fullmethods.txt](apk/fullmethods.txt) | Full selected methods, including updater and version comparison |
| [classified.txt](apk/classified.txt), [routing.txt](apk/routing.txt) | Device classification and routing |
| [bt.txt](apk/bt.txt), [c4bt.txt](apk/c4bt.txt) | Bluetooth and component/version context |
| [ota-methods.txt](apk/ota-methods.txt) | Firmware preparation, CRC and updater state machine |
| [ota-transport.txt](apk/ota-transport.txt) | Sending and packet construction |
| [xref.txt](apk/xref.txt) | Firmware-related cross-reference output |
| [ziplist.txt](apk/ziplist.txt) | APK archive file listing |
| [firmware-inventory.json](apk/firmware-inventory.json) | Complete firmware asset sizes, hashes and wrapper bytes |
| [url-strings.txt](apk/url-strings.txt) | Static URL strings, without runtime traffic attribution |

`firmware/` contains the inspection tool's reproducible JSON output and a linear Capstone disassembly of the candidate C4_F01 angle/message region. Literal data can decode as instructions in a linear sweep. Function boundaries and semantics remain research questions. [Firmware notes](../docs/firmware-analysis.md) · [Tools](../tools/README.md)
