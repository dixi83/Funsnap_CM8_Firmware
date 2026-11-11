# FCC and IC document archive

The local documents support hardware identification, pin numbering, flash-access interpretation and comparison between revisions. Source URLs, downloaded byte sizes and SHA-256 hashes are preserved in [sources.json](../sources.json). Filename versions on upstream servers can differ from the revision printed inside the PDF, so identify the archived bytes by hash.

## CM8 FCC exhibits

| Archived document | Contents |
| --- | --- |
| [CM8 internal photographs, exhibit 8078955](fcc/CM8-internal-photos-8078955.pdf) | Six-page internal-photo exhibit for FCC ID 2APVH-CM8 |
| [CM8 model-difference declaration, exhibit 8078952](fcc/CM8-model-difference-8078952.pdf) | Manufacturer's family declaration, dated 24 February 2025 |
| [CM8 BLE test report, exhibit 8078946](fcc/CM8-BT-test-report-8078946.pdf) | Report AiTDG-250121002W2, 36 pages |
| [CM8 user manual, exhibit 8078965](fcc/CM8-user-manual-8078965.pdf) | Public user manual from the CM8 filing |

The report was initially saved locally with a generic BT label. Its actual report number identifies the W2 BLE document. The internal photographs describe the earlier certification sample, while the owner photographed a later panel revision. [FCC filing index](https://fccid.io/2APVH-CM8)

## Puya IC documents

| Family | Datasheet | Reference manual | Relevance |
| --- | --- | --- | --- |
| PY32F030 | [83-page datasheet](ic/PY32F030-datasheet.pdf) | [442-page manual](ic/PY32F030-reference-manual.pdf) | Motor short marking F030EF28 and QFN20 pinout 2 |
| PY32F040 | [69-page datasheet](ic/PY32F040-datasheet.pdf) | [792-page manual](ic/PY32F040-reference-manual.pdf) | Visible panel MCU PY32F040C18T6, SWD and flash protection |
| PY32F403 | [77-page datasheet](ic/PY32F403-datasheet.pdf) | [759-page manual](ic/PY32F403-reference-manual.pdf) | Strong binary-derived F01 family candidate, physically unresolved |

The F030 reference PDF's cover contains a PY32F003 heading as well as its PY32F030 title. Its page headers and content identify the F030 manual. Consult the actual PDF content and exact package variants when applying a pinout or register definition.

Useful package drawings are F040 figure 3-3 on PDF page 24 and F030 figure 3-10 on PDF page 30. Flash protection and access tables are in each family's reference manual. The firmware target families remain subject to the hardware mapping described in [hardware notes](../docs/hardware.md).

## Model comparison

| Document | Use |
| --- | --- |
| [CM9 internal photographs](comparison/CM9-internal-photos.pdf) | DY-B03-02-V3 module comparison and later hardware revision |
| [Gadnic GIM00013 manual](comparison/Gadnic-GIM00013-user-manual.pdf) | CM8 Bluetooth name and Capture 2 rebrand evidence |
| [CM9 model-difference declaration](comparison/CM9-model-difference-8798614.pdf) | Separate later CM9 filing |
| [Capture2 internal photographs](comparison/Capture2-internal-photos-4462171.pdf) | Earlier Funsnap hardware examined during the search |
| [Capture2S internal photographs](comparison/Capture2S-internal-photos-7931913.pdf) | Earlier Funsnap hardware examined during the search |
| [Capture3 internal photographs](comparison/Capture3-internal-photos-5167609.pdf) | Board and radio marking comparison material |
| [Capture3 model-difference declaration](comparison/Capture3-model-difference-5167604.pdf) | Context for that earlier product family |

The VEVOR manual source is linked in the model notes. Its mirror returned HTTP 403 during archive assembly. [Related models](../docs/related-models.md)

The older Capture exhibits are retained as exploratory comparison sources. They do not establish that these earlier products share the owner's CM8 hardware or accept its firmware.
