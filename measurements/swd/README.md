# SWD measurements

These files record connection troubleshooting on 10 November 2026. PicoScope channel A was connected to SWCLK, channel B to SWDIO, with shared target GND. The instrument shown is a PicoScope 2204A using PicoScope 7 T&M. The screenshot labels show x1 scaling, DC coupling and ±5 V ranges during the captured setup.

| File | Scope |
| --- | --- |
| [20261110.csv](20261110.csv) | First short capture. Session analysis found about 25 rising clock edges, data high on each and approximately 96 kHz clock. The request/ACK interval was outside this capture |
| [20261110-0002.csv](20261110-0002.csv) | Longer capture of an unsuccessful connection. Session analysis identified four 0xA5 DPIDR requests with 000 response bits |
| [20261110-0002.psdata](20261110-0002.psdata) | Associated native PicoScope file |
| [openocd-success.txt](openocd-success.txt) | Later successful identification, failed flash reads and successful option-register reads |

The CSVs use semicolon separators and decimal commas. The first row names Time, Channel A and Channel B. The second row specifies milliseconds and volts. Preserve the raw files before conversion.

The unsuccessful capture does not establish why the target failed to respond. A loose SWCLK connection was subsequently reported, and eventual SWD identification succeeded. These waveforms are SWD troubleshooting data. Internal UART1 and tilt-behavior recordings remain outstanding.

## Screenshots

The screenshots preserve the acquisition process and include settings that were later changed. Refer to a CSV's actual sample spacing when analyzing it.

| Screenshot | Description |
| --- | --- |
| [01](scope-01-waiting.png) | Scope waiting for trigger at a long timebase |
| [02](scope-02-triggered.png) | Triggered capture with digital activity |
| [03](scope-03-sampling.png) | Activity at a shorter timebase, still with limited sample density |
| [04](scope-04-rate-settings.png) | Target sample-rate configuration |
| [05](scope-05-buffer-settings.png) | Buffer-memory priority configuration |

No waveform of the eventual successful exchange was recorded. The successful OpenOCD logs are the retained evidence for the final connection and RDP interpretation. [Debugging notes](../../docs/debugging.md)
