# V4.7.14: Valid archive growth past the text-repair limit

The adaptive regeneration checkpoint reached 26,292,851 bytes. V4.7.13 rejected it at the 24 MiB text loader gate even though its JSON was valid.

V4.7.14 validates oversized archives with the existing strict parser, whole-body validator, foundation checks, exact rational checks and archive-link audit, then observes text structure through Z0. Oversized valid adaptive sources use the same validator. Malformed oversized files remain unchanged and do not enter unbounded text repair. Existing queues, completion thresholds and prefix-preservation checks remain in force.

## Validation

- Four focused regression tests passed: valid grown archive loading, duplicate-key rejection, malformed-text rejection and arithmetic contradiction rejection. Each test verifies source preservation.
- A disposable copy of the supplied 26,292,851-byte checkpoint loaded with all 4,024 rational expressions.
- A real adaptive engine cycle continued from saved run 27 to run 28, reaching 4,197 rational expressions (173 added) and adding 337 total archive records.
- The cycle reported 90 processed tasks, zero archive-link issues, zero independent rational contradictions and preservation of every existing archive prefix.
- SHA-256 confirmed the uploaded source remained unchanged.
- Host runtime: Python with SymPy 1.14.0. Android execution has not yet been tested.

## Phone use

Place zero_theoremV4.7.14.py in the same folder used by the prior adaptive run, retaining the original source JSON and its complete .adaptive-work folder. Resume the same adaptive invocation using the new script filename. A normal Run uses the existing automatic recovery routing; the explicit command is:

```sh
python zero_theoremV4.7.14.py --adaptive-recovery "zero_theorem_rabbitholes_v41_memory.json"
```

Do not move the regeneration checkpoint over the original source: the adaptive state retains the source fingerprint and selects a replacement only after its existing completion checks pass. The patch does not reduce memory usage or establish an unlimited device capacity.
