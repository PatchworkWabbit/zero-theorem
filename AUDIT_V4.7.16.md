# V4.7.16 repository and resilience audit

Date: 18 October 2026 (Australia/Perth).

## Repository status

Audited GitHub development commit: `ed945041b7c35fb669c4786a71a9520b71ed6a43`
on `feature/zero-time-observer`. All 68 tracked local files matched GitHub blob
IDs, including the corrected clock-query routing, engine, runners, results and ZIP.
The six ZIP members also matched their individual repository files exactly and
passed ZIP CRC checks. There were no missing development uploads.

The default `main` branch remains at `7c5d9e21be02008a8330ca39ff63dd5d6eae00f8`
with V4.7.13. PRs [#3](https://github.com/PatchworkWabbit/zero-theorem/pull/3),
[#4](https://github.com/PatchworkWabbit/zero-theorem/pull/4) and
[#5](https://github.com/PatchworkWabbit/zero-theorem/pull/5) are drafts, stacked
V4.7.14 -> V4.7.15 -> V4.7.16. No merges were performed during this audit.
PR #1 is an older open draft, not the current release path.

Engine SHA256:
`844c9a77f0ea1f6915521bed82ca36bafe8fb5bcdb83eea25b9b92d51a1a36ef`.
It matches the engine fingerprint in the existing **131/131 passing host checks**.
Those checks were not rerun unnecessarily against identical runtime bytes.

## Findings

### A1 — High: malformed retry state can stop otherwise healthy regeneration

Location: `_z7_retry`, before the protected retry block, and the adaptive `run`
retry exception handler in `zero_theoremV4.7.16.py`.

A correctly bound retry ledger with `attempts: null` passes the ledger identity
gate, then raises `TypeError` at `len(ledger['attempts'])`. The normal adaptive
run catches only `ValueError`, `OSError` and `RuntimeError` around the retry,
so this exception stops the run before regeneration continues.

The disposable audit reproduced the exception through normal `run()`, with
the source, source snapshot, active memory and pointer bytes unchanged.
This is an availability failure, not demonstrated mathematical corruption.

Recommended correction: validate retry-state types and required fields before
use; preserve an invalid ledger, report a deferred retry, and continue the
already independently validated active branch. Add a normal-run regression for
malformed retry state. Avoid silently treating malformed state as recovered.

### A2 — Medium: observation ledgers lack complete invariant checks

Locations: `_zt16_read`, `_zt16_space`, `print_zero_clock_report`.

The independent clock accepts `tick=-1`, `registered_states=0` and a negative
coordinate when the limited arithmetic equality checks agree. The process-time
reader accepts an event whose first sequence is 999 while `next_seq` still
equals the list length plus one. The zero-clock report reads directly without
running the update-time validation.

These results make malformed clock files appear valid. They do not alter the
mathematical archive or scheduling, because observations remain separate.
Automatic hooks already preserve mathematical work on many observer failures.

Recommended correction: validate schema, origin, nonnegative integer counters,
domain keys, ID collections, event sequence/links and derived totals, and share
the read validator with report queries. Preserve invalid bytes; do not rebuild
an apparently authoritative clock history without an explicit new boundary.

### A3 — Medium, conditional: executable fingerprint trusts launcher `__file__`

Location: `_z7_rules_signature`.

It hashes the path in module `__file__`. If a launcher executes the engine with
its own filename in that variable, the signature describes the launcher rather
than the engine. A controlled probe changed only a supplied launcher file and
observed the purported executable-rules signature change. Under the same
condition, editing the engine without changing the launcher would not refresh
that signature.

The earlier test-runner failure demonstrated a Pydroid filename-location issue,
but does not establish this condition for the user's successful engine launch.
The engine found the correct Maths memory path in that run. This finding is
therefore conditional, not a claim that phone recovery triggers already failed.

Recommended correction: bind the executable identity to the actual engine
source or a deterministic fingerprint of loaded rules, with an exec-wrapper
regression. Do not infer executable identity solely from a launcher filename.

### A4 — Low: stale device confirmation text (corrected in audit documentation)

README still said Task 7 device confirmation was pending; the validation notes
still said the corrected time command was unconfirmed. Updated to the evidence
the user supplied: Android run 33, successful clock reports, retry pending,
regeneration active. This does not claim a recovered candidate or memory merge.

## Evidence and boundaries

`audit_v4716_probes.py` reproduces A1–A3 using temporary files and the generated
public fixture. `audit_v4716_results.json` records outcomes. No live user memory
was opened. Existing 131 passing tests cover supported behaviour; these new
malformed-state probes expose gaps outside that coverage.

The user's Android output independently showed: arithmetic/foundation PASS;
all five archive passage categories complete; 10,243 accepted records;
23,026 typed dependency links; zero structural issues; independent clock 332;
successful `time` report; retry attempt 1 pending. A link audit is structural,
not a proof that every possible path was explored or historical identity recovered.

Timing showed 37.15 seconds within `load_memory`, 0.12 seconds within queue
exploration and 3.57 seconds within validation/save. This identifies a measured
stage, not its internal cause. Additional validation and recovery checks occur
outside that stage and nested durations overlap. Profile before optimizing;
retain arithmetic, foundation and link checks.

## Recommended order

1. Fix A1, then A2; verify their failure paths leave mathematical files intact.
2. Resolve A3 under an emulated launcher and an Android launch.
3. Rerun the full suite plus new regressions and package the reviewed revision.
4. Review and promote stacked PRs in order. Keep memory merging as a separate
   task requiring identity, dependency and conflict validation.

Runtime code was not changed during this audit. Findings remain open.
