# Experimental zero recovery slots (V4.7.2 installer)

A missing archive record currently shifts list positions while saved IDs stay
unchanged. This patch checks positions **before upgrades and exploration**, routes
archive damage through `zero_core(..., 'errors', operation='recover_archive')`,
and reserves missing IDs with explicit unresolved slots. A slot's value is
`null`, never the arithmetic number zero.

## Install on a phone

The repository currently contains engines through V4.6.5. This installer targets
the complete V4.7.1 engine used in the recent phone test; it does not downgrade
that engine or replace any of its workers.

1. Put `apply_zero_recovery_patch.py`, `zero_recovery.py`, and your
   `zero_theoremV4.7.1.py` together in the test folder.
2. Run `apply_zero_recovery_patch.py` in Pydroid3. It creates the standalone
   `zero_theoremV4.7.2.py` without overwriting an existing file.
3. Run the new engine in the test folder with a test memory file. The two patch
   files are no longer required by the generated engine.

The installer only creates code. It does not run the engine or edit memory.
Use the same installed SymPy dependency as V4.7.1.

## What is recorded

`zero_recovery.next_ids` stores each archive's next unused ID, including a
missing tail record. `zero_recovery.manifest` maps each ID to an expression,
pathway and construction checksum. Rational entries also retain a reconstruction
recipe (tree, pathway, parents), rather than a full second copy of each record.
The manifest increases JSON size, and checking uses a temporary copy of memory.
Phone memory and timing on a sustained archive still need measurement.

Supported rational binary paths (`reuse_v1`, `result_feedback_v42`, `consume_v1`,
`revisit_v1`) are re-executed through zero using earlier surviving parents.
Reconstructed payloads must match their manifest checksum. New execution is
logged as recovery, without inventing old scheduler timestamps. Restoring record
identity does not count a new archive record. Actual re-execution does pass
through the operation gate.

During migration of an older archive, an ordered known-expression key and an
independent surviving creation event may supply a recipe. The calculated value,
parent construction trees, and declared depth/size bounds must agree. This is
labelled `legacy_evidence_reexecution`, separately from manifest-verified work.
It is evidence-based reconstruction, not proof of an unavailable historical
record. A suppressed journal or insufficient evidence leaves recovery pending.

## Pending and conflicting work

This first patch **defers all exploration** if any record remains unresolved;
it preserves queued work rather than attempting partial execution with missing
operands. It writes the candidate with its slots and incident log to
`MEMORY_FILENAME.zero-recovery.json`, atomically. The original memory bytes are
left unchanged. A repeated attempt on unchanged evidence does not append an
unlimited list of identical incidents. Changing/adding evidence allows a new
preflight. A pending checkpoint is diagnostic; the engine reads its normal
memory path on the next run, not that side file.

Conflicting IDs, malformed counters, changed manifested payloads and excessive
slot requests block continuation. Supported recovered records retain their
original IDs. Unsupported rational rules and missing complex, symbolic, role or
calculus records remain pending. This is an archive-recovery expansion, not a
handler for every possible Python exception or an exhaustive repair algorithm.

Counters and indexes are never silently reset to pass validation. Existing
saved runs receive an archive-link audit before exploration. The engine's normal
zero-core coverage check remains enabled before save.

The manifest detects accidental disagreement. It is stored in editable JSON and
is **not authenticated**. An attacker replacing both records and manifest is not
prevented by checksums. Rational trees are independently evaluated at preflight;
this patch does not independently prove all other domains' results.

## Validation and release boundary

Run `python -m unittest discover -q` with SymPy 1.14.0.

Recovery tests cover intact continuation, middle and tail deletion, stable next
IDs, reconstruction, insufficient/contradictory evidence, duplicate IDs, changed
values, unchanged original bytes, checkpoints, and the installer. The fixture
uses the repository's real V4.6.5 arithmetic workers with the V4.7.1 zero-gate
contract, plus a two-run continuation smoke test. It does not substitute dummy
role/calculus workers for a claimed full V4.7.1 regression.

**Draft release:** the complete V4.7.1 source is not yet checked into this
repository. Full V4.7.1 first-run, continued-run, role/calculus and record-19
integration checks remain required before merging/releasing this installer.
