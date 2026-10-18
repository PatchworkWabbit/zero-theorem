# Zero Theorem V4.7.17 — exact temporal recovery

This revision integrates the temporal experiment into the engine's shared
`zero_core` gateway. The memory-format version remains `4.1` for compatibility.
It retains existing mathematical exploration, recovery, and clock features.

## Phone instructions

1. Extract the complete bundle into a separate folder.
2. Open `run_temporal_tests.py` in Pydroid3 and press Run. It generates disposable
   mathematical memories and records actual clock samples, then masks samples
   and compares reconstructed candidates with the untouched originals. It does
   not open your main memory. SymPy 1.14.0 must be available as for the engine.
3. After checking the phone results, place `zero_theoremV4.7.17.py` beside the
   existing `zero_theorem_rabbitholes_v41_memory.json` and run that engine file
   to continue normal mathematical work. Keep your existing backups.

The runner's default includes temporal, audit, clock, and lab checks. The
optional `--full` flag also executes the existing 108 recovery/archive checks
on their generated fixtures; this takes several minutes on the host and may
take longer on a phone. Nothing requires manually damaging live files.

## Recorded evidence and zero

New accepted archive records pass the actual shared `zero_core` gateway.
Their acceptance observations include typed archive/record IDs, references to
parents and sources used by the construction, committed record fingerprints,
session identity, wall/monotonic/CPU samples, and an event sequence count.
The observed milestone is the acceptance gate; it is not a measurement of
every instruction or the start of an operation. Calls that produce no new
accepted record do not receive individual observations in this revision.

Observations are buffered and committed separately only after a successful
normal mathematical save. Existing records establish a boundary; their past
creation/use times remain unknown. Mathematical record payloads, operation
counters and queue choices do not acquire temporal fields or feedback.

The new sidecar is `MEMORY_PATH.temporal.json`. Its sequence begins at the
zero-origin event count. This sequence is distinct from the existing
space-growth zero-clock. Existing process-span observations and the independent
space clock remain in their original sidecars.

Adjacent sample differences are explicitly recorded as redundant evidence.
Same-session monotonic/CPU event order and typed parent/source acceptance-use
links also supply constraints. Wall time is allowed to move backwards.
No timer values are subtracted across process sessions. There is no implicit
conversion between elapsed time, CPU time, event sequence, or space growth.

The recorder admits at most 1,600 new acceptance observations per run; a reached
cap records a gap and leaves mathematical work running. It retains prior
observations. A failed observation does not roll back mathematical work or
pretend a complete history was recorded. Total sidecar growth and phone-scale
performance still require observation on the user's workload.

## Exact-only timestamp reconstruction

The first integrated recovery worker supports one absent recorded field
(`wall_ns`, `monotonic_ns`, or `process_cpu_ns`) in a temporal ledger. Its
bounded local evidence component includes adjacent observations and recorded
creation/use links. All inference passes re-enter the shared zero gateway.

An interval with different endpoints is **unresolved**, even if a test's hidden
original happens to lie inside it. Only a unique coordinate supported by the
inspected evidence is accepted, and the complete resulting ledger must also
pass validation. Contradictions produce no candidate. Budget exhaustion does
not become success. The hidden original is never supplied to this worker.

When normal loading detects a single missing temporal sample, it attempts a
separate proposal automatically. It preserves the damaged ledger; it does not
promote the proposal or fabricate new observations on top of damaged history.
Mathematical work continues. Candidates and reports are saved separately as
`.time-candidate.json` and `.time-recovery-report.json`. A different existing
candidate is never overwritten. Candidate identity is not a proof of original
chronology or an authenticated physical time source.

Explicit command on a disposable damaged ledger:

```sh
python zero_theoremV4.7.17.py --time-recover DAMAGED_LEDGER.json 2 monotonic_ns
```

Interactive commands:

```text
temporal
temporal-recover 2 monotonic_ns
```

The latter uses the current memory's temporal sidecar. A present timestamp is
refused as a recovery target. This worker does not repair arbitrary missing
events, erased duration histories, earlier unobserved expression times, or
multiple missing timestamps. Those remain future work. Recovery here uses
surviving recorded redundancy and relations; zero passage adds no lost facts.

## Audit corrections included

- **A1:** validate retry-ledger collections before use. Malformed retry state
  is preserved and deferred while an independently validated active branch
  continues. A normal-run regression covers `attempts: null` and checks the
  source, source snapshot, active pointer, and malformed ledger bytes.
- **A2:** process event sequences, span links, session boundaries, samples,
  durations, derived totals and open-span state are replay-validated. Zero-clock
  origin, counters, domain keys, ID collections, growth batches and totals are
  checked. Report queries use the validators and preserve invalid bytes.
- **A3:** fingerprint the actual executing module code and rule/configuration
  constants, independently of launcher `__file__`. Defaults and nested code are
  included; source filenames, line numbers and random session IDs are excluded.
  Loaded code identity is fixed at module load so temporary instrumentation does
  not masquerade as a source revision. Reload edited rules to refresh their code
  identity. Exec-wrapper regressions cover launcher edits and engine edits.

These corrections were tested on the host. Android execution of this integrated
revision is now confirmed by the user: 68/68 selected checks passed, followed
by a saved normal run on the intended Maths regeneration branch. See
ANDROID_V4.7.17.md for the reported evidence and path correction.

## Validation contents

The package includes the tested single-file engine, a phone runner, integration
tests, the 0.2 lab tests, prior disposable recovery fixtures/tests, host result
JSON, and a member fingerprint manifest. The old import filenames are recreated
in a temporary folder by the runner and execute the new engine bytes; they are
not older engines delivered for live use.

New engine-run tests mask first, middle and final recorded events across all
three sampled clocks: nine exact comparisons against separately held originals.
Further checks retain surrounding timestamps but remove duration evidence and
verify a nonzero interval stays unresolved. Other checks cover contradictions,
source preservation, candidate preservation, actual shared-gateway routing,
recording caps, disabled-observer mathematical equivalence and audit failures.

No live user memory was opened during development. The tested revision is now
published on `feature/exact-temporal-recovery` for review; the existing runtime
files and main branch are preserved. See ANDROID_V4.7.17.md for subsequent
user-reported device confirmation.

The original engine and this revision are distributed under GPL v3; see LICENSE.
