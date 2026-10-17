# V4.7.5: whole-body recovery experiment

Status: experimental. Tested 17 October 2026 with Python 3 and SymPy 1.14.0.

## Observed recovery

One user-provided damaged memory failed strict JSON parsing. V4.7.5 mapped 2,409
independently parseable record objects and identified two damaged rational
expression spans. The worker produced a complete candidate with rational
expression IDs **20, 22, 23, 116, and 117** reconstructed.

The evidence consisted of surviving construction keys, independent creation
events, parent expressions, repeated text, and the existing executable engine
rules. No intact master was supplied to the recovery worker. Exploratory edits
made during development were confined to scratch copies; the final worker was
then executed on a fresh copy of the damaged input without hand-entered offsets
or replacement values.

Additional reconstructed structure:

- A truncated observer role name: matching 16-character boundaries around a
  surviving text span provided the insertion hypothesis.
- A journal event: repeated text proposed several parents; the saved task's
  parent/kind rule contradicted three alternatives, leaving the supported one.
- The `rational:113` ledger row prefix: surviving event counters supplied
  `generated = 15`, rather than copying a neighbouring row's count.
- A damaged role queue item: replay of the recorded FIFO construction rules
  agreed with 24 intact tasks and 13 recorded role constructions.

The resulting candidate had 132 rational expression records. Every rational
record passed tree re-evaluation; the archive link audit reported **zero issues**;
zero-core archive passage coverage passed; journal task parent/kind constraints
passed; and summed parent generation counts matched the ledger's total.

The candidate loaded successfully, continued normal exploration, saved, and
loaded again. Previously accepted rational record payloads remained unchanged
through that continuation. The damaged source bytes remained unchanged. The
user subsequently reported `candidate_ready`, `archive ready: True`, and the
same five reconstructed IDs from their Android/Pydroid3 run.

An exact comparison with the intact master is **still outstanding**. Internal
consistency and successful continuation support this candidate; they do not
prove that every byte or historical detail equals the original file.

The user memory, candidate, and full evidence sidecars are not published in this
repository. The public tests below are reproducible without those files.

## Representation and recovery rules

`zero_core(..., 'whole_body', ...)` dispatches mapping, relationship constraints,
proposal generation, and candidate validation. The full original body is retained
in the map, together with an ordered symbol-span stream and an alphabet keyed by
Unicode code point. Symbols are not numerically collapsed into indistinguishable
zeros. Lexical roles after a damaged quote are tentative; independently decoded
records provide additional resynchronization anchors.

Current expression slots cover bounded rational spans between independently
parseable expression neighbours. Each slot retains its raw fragment, full left
and right neighbours, surrounding complete expressions, candidate IDs, and
complete expressions referring to those IDs. Quarantining a span changes only a
candidate skeleton; the original fragment stays in the map. Removing a damaged
span is not itself recovery. Missing IDs are accepted only when the archive
reconstruction and validation gates succeed.

Observed text bridges use both boundaries and retain their source occurrences.
Saved task identities constrain journal parents. Ledger counter evidence and
role FIFO replay supply two additional executable reconstruction rules. JSON,
Unicode, and the mathematical/scheduling rules are supplied definitions, not
rules proven to emerge from arithmetic alone.

## Execution and persistence

Recovery loops continuously. Normal exploration keeps its pre-existing workload
limits. The optional `--seconds N` flag requests a pause; it is not required.
Checkpoints are written about every five seconds between search steps and on a
handled interruption. A single step may take longer than five seconds. A forced
process kill or storage failure can lose work since the last checkpoint.

Files are saved beside the damaged input:

- `.zero-body-map.json`: complete source, ordered representation, readable records,
  damaged spans, and their neighbours.
- `.zero-body-search.json`: pending work, distinct recorded edges, attempts,
  contradicted hypotheses, fallback grammar continuation, and validation results.
- `.zero-body-candidate.json` (with a suffix if needed): a separately saved
  candidate, including reconstruction provenance.

Existing matching V4.7.4 `.zero-nexus-search.json` continuation is retained for the
fallback grammar worker. A source fingerprint mismatch refuses a checkpoint.
Keep the source and sidecars together. Do not reuse a checkpoint with an edited
source. The worker does not replace the damaged source automatically. Run an
inspected candidate in a separate test folder under the expected memory filename.

Equal candidate text shares expansion, while distinct incoming edges and
repeated supporting occurrences remain recorded. Contradicted hypotheses remain
in the search record. The current workers are not an exhaustive enumeration of
all possible reconstructions.

## Reproducible checks

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest -v test_zero_body_recovery
```

**9 tests passed**, covering:

1. Lossless ordered symbol mapping, including non-ASCII symbols.
2. Damaged expression slots retaining complete neighbours and original fragments.
3. Two-sided observed bridges and their source evidence.
4. Saved task identity contradicting a wrong parent hypothesis.
5. Ledger reconstruction using an independent event counter, with suppressed-log
   evidence refusing the inference.
6. Role queue replay agreeing with every surviving task.
7. Manifest-backed exact re-execution of a removed arithmetic record.
8. Time-requested pause/resume and source-fingerprint rejection.
9. Blocking incompatible candidates without crashing validation.

The tests generate a fresh bounded engine memory in a temporary directory. They
do not require a user fixture. Separate hosted checks covered the supplied damaged
case, candidate continuation, source-byte preservation, and saving a live frontier
on interruption. Earlier repository tests continue targeting the earlier scripts;
these nine tests target V4.7.5.

## Limits and next checks

- Compare the recovered candidate with the intact master, separating reconstructed
  record content from newly added recovery metadata.
- Broaden corruption fixtures: deleted/reordered records, misleading repetitions,
  damaged manifests, missing evidence, Unicode damage, and non-rational archives.
- Record mapping and accumulated search state have no global memory-growth bound.
  The 24 MiB input guard remains; continuous work does not remove representation
  limits or provide a hard wall-clock guarantee.
- Observed bridges currently inspect a local failure window, require 16-character
  boundary matches, and search for inserted spans up to 1,024 characters away in
  the observed source. The priority worker selects parser-advancing insertions.
- The fallback grammar worker retains its existing proposal/representation limits.
  It is not a general theorem prover or a complete JSON repair algorithm.
- Arithmetic reconstruction is limited to supported rational binary constructions
  with sufficient evidence. Other damaged archive records can remain pending.
- Checksums detect inconsistency; they do not authenticate history if both the
  records and their evidence/manifest were replaced.
- A ready candidate is evidence-supported, not proof of unique historical recovery.
  Arbitrary Python source-code repair and recovery of information with no surviving
  constraints have not been demonstrated.
