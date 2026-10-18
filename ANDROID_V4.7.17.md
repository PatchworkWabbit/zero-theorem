# V4.7.17 Android confirmation

Date: 19 October 2026 (Australia/Perth).

Evidence source: the user pasted Pydroid3 runner and engine output into the
project conversation. The phone's result JSON was not separately uploaded or
byte-inspected. The supplied engine/source hash remains the host-tested build;
no device-side executable checksum is claimed.

## Disposable runner

The user reported **TEMPORAL: 68 / 68 passed** and `[Program finished]`.
The runner reported no live memory opened. Its selected groups are 19 temporal
integration checks, two retry/launcher checks, 23 existing clock checks and
24 lab checks. The timestamp-masking test contains nine comparisons spanning
first/middle/final events and wall/monotonic/CPU samples from generated engine
runs. These are disposable integration experiments, not damage tests on the
user's live memory.

The initial folder prompt was caused by Pydroid's launcher path context.
The working entered path was:

```text
/storage/emulated/0/Download/zero_theoremV4.7.17_temporal_tests/zero_theoremV4.7.17
```

Android's file-manager label `Internal storage` is not the literal filesystem
prefix. The actual extracted folder name has no underscore between `theorem`
and `V4.7.17`.

## Intended memory continuation

An initial normal run used Pydroid's private application directory. The user
then ran V4.7.17 on the intended `Documents/Lucky/Maths` source and its existing
adaptive regeneration branch. The later output reported:

- V4.7.17; SymPy 1.14.0; saved run 34.
- Original-memory recovery retry attempt 2 pending, triggered by changed
  executable rules and remaining saved feedback work; regeneration remained
  selected and continued.
- Exact arithmetic/foundation PASS; new foundation states 100, 101 and 102.
- Complete zero-core passage coverage across all five archives.
- Rational 5,196; complex 2,668; symbolic 2,089; calculus 340; roles 265:
  **10,558 accepted archive records** in total.
- Structural audit: **23,883 typed dependency links, zero structural issues**.
- Independent zero-space clock: tick 650, 651 registered clock states.
- Process-time report available; 25 events, zero open spans in that ledger.
- `temporal`: **315 acceptance/use observation events, zero reported gaps**.

The clock's zero is an observation boundary, so tick 650 is not the archive
record count. Process timing includes multiple finished stages/runs and nested
work; reported stage totals are not a single-run runtime measurement.

This confirms normal Android continuation and the new recorder on the intended
branch. Original-memory recovery remains pending; the output does not establish
restoration of the original historical archive or an actual live timestamp
repair. The separate disposable tests demonstrate the supported reconstruction.

## Published package identity

The engine and test ZIP are the same bytes supplied before Android testing.
Their packaged validation notes therefore retain the earlier device-pending
checkpoint. Current confirmation is recorded here and in the root release notes.
No live memory, device paths beyond the instructions above, or private JSON
contents are included in this upload.
