# Original APK firmware assets

The `capture2-2.6.74` directory contains unmodified update assets extracted from `assets/firmware/` in the examined Capture 2 v2.6.74 APK. C3 and C9 files were retained as comparison material alongside C4. Their presence here does not establish compatibility with a particular physical CM8 revision.

| Asset group | Why archived |
| --- | --- |
| `C4_F01.bin`, `C4_F04.bin` | CM8 updater targets in the examined app |
| `C3_F01*`, `C3_F04.bin` | Capture π route, compared because the owner PCBs bear C03 markings |
| `C9_F01*`, `C9_F04*` | CM9 routes and variants, including the close local F01 routine match |

The two C4 files are F01 v8 and F04 v7. The examined physical CM8 reports F01 v10 and F04 v9. Installed-version images, bootloader dumps and calibration backups remain unavailable.

The `C9_*_puran_360*` filenames use a `CB` model byte in their wrappers. These variant markers are preserved as found and are supported by the inspection tool. A filename prefix alone does not establish the wrapper model.

[sources.json](../sources.json) records hashes and paths for each archived asset. The [full inventory](../analysis/apk/firmware-inventory.json) covers all firmware files found in the APK, including files outside this comparison set. Bluetooth-named assets in the APK were not conclusively assigned to the owner's radio module.

Use the [offline tools](../tools/README.md) for extraction and inspection. The [analysis notes](../docs/firmware-analysis.md) describe wrapper removal and the inferred application base. Directly treating a wrapped update file as a full-chip image would use the wrong layout and omit the unarchived initial flash region.
