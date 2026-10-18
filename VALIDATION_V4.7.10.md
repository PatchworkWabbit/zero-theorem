# Zero Theorem V4.7.10 — adaptive recovery and Z0 regeneration

## Start on your phone

Extract the test ZIP into a separate folder. Open **run_task3_demo.py** in Pydroid3 and press Run. SymPy is already installed on your phone.

The demo creates its own working folder and a controlled damaged copy of the included 132-record fixture, retaining four rational records. It measures the missing constructions against a separate intact fixture, runs the trials, validates the selected branch and confirms saved continuation. Its output reports the active memory path and whether both inputs stayed unchanged. Your existing engine memory is not used by this demo.

For everyday use, put **zero_theoremV4.7.10.py** beside your test memory and run it as usual. Consistent memory continues normally. Damaged memory enters adaptive work automatically. After selection, subsequent normal runs use the selected branch; the source remains preserved.

Keep the generated `.adaptive-work` folder and `.adaptive-active.json` beside the source memory. They retain trial memories, partial reconstructions, unresolved slots, search evidence, measurements, logs and the active-branch selection.

## What is implemented

1. Validate the supplied executable arithmetic and foundation rules through 0, independently of the damaged memory.
2. Snapshot the damaged source and create separate recovery and regeneration trials.
3. Recovery uses the surviving archive's recipes, construction keys, creation events and checkpoints. Partial reconstructions are retained even when the complete archive remains unresolved.
4. Regeneration invokes the normal engine's initial memory constructor: one rational zero record, foundation `[0]`, and its emergence queue. Original records, queues and archive history are not transplanted.
5. Both branches must reach the same declared rational-record floor and then complete another genuine engine run. Exact checks, manifests, dependency audits, preservation of existing constructions, saving and reloading are verified.
6. Record elapsed time, completed runs, queue-task counts, generated record counts and zero-core operation counts. Select a validated branch according to the explicit policy below.
7. Continue the selected branch on later normal runs. The new branch carries an explicit lineage marker. Pending recovery work remains available for later adaptive invocations.

The intact baseline is used solely for loss measurement and the operational target. It is withheld from both the recovery worker and the regeneration seed.

## Selection policy and measured goal

The operational goal is **resume verified mathematical exploration after reaching a rational-record floor**. This is not a historical-equivalence goal.

The target comes from the intact baseline's rational record count, otherwise a surviving positive manifest count, otherwise the configured default of 128. A function caller can supply an explicit target.

- Prefer a ready recovery branch when both branches are ready.
- At a measured loss of at least 50%, choose regeneration instead only when its measured elapsed cost is below 80% of recovery's elapsed cost.
- When only one branch has completed validated continuation, select that ready branch.
- When neither is ready, preserve the checkpoints and continue trials on a later invocation.

Loss is measured using missing `(pathway, tree)` construction identities against the intact baseline. Without a readable baseline/source comparison it stays unknown. Missing constructions and provenance are reported separately from new operational capability.

The record floor is a practical benchmark, not proof that two archives contain equivalent mathematics. Timing is a local observation, not a performance forecast. An unresolved recovery trial is not declared impossible or exhausted merely because its current slice ends.

## Checkpoints and budgets

Recovery automatically processes feedback in chunks, checkpointing continuation. Its default comparison slice is two seconds; `--seconds N` changes that allowance. Parsing, validation and an already-running chunk can take longer. The existing unrestricted `--repair-json` workflow remains available.

Each trial allows eight normal engine cycles per adaptive invocation. Normal engine work limits stay unchanged. A trial that reaches its budget remains checkpointed. Rerunning continues it; saved baseline metadata is reused. Ctrl+C preserves trial state and completed memory saves. If interruption occurs between a save and metric recording, the report marks incomplete cycle metrics.

When regeneration is selected, history is explicitly `new_emergence_from_Z0`. The original archive, snapshot and partial recovery evidence remain preserved. A fresh lineage is not labelled as restored historical provenance, even when deterministic exploration produces familiar constructions.

## Optional terminal commands

```bash
python zero_theoremV4.7.10.py --adaptive-recovery "DAMAGED.json" "INTACT.json"
python zero_theoremV4.7.10.py --adaptive-recovery "DAMAGED.json"
python zero_theoremV4.7.10.py --adaptive-recovery "DAMAGED.json" "INTACT.json" --seconds 10
```

A previously saved trial must keep its source, baseline contents and target consistent. Changed source bytes receive a separate workspace. Existing source and baseline files are never overwritten by adaptive selection.

## Validation

38 tests pass, including all 17 task-2 regression tests. The new tests exercise real recovery/regeneration trials, substantial record deletion, uncertain foundation data, unreadable text, non-rational corruption, repeated normal Run continuation, automatic multi-chunk feedback, input preservation, saved-baseline reuse, interrupts, pending budgets, rule failures, source changes and measured selection policy.

Run after extracting the ZIP:

```bash
python -m unittest -v test_zero_theorem_v4710.py test_zero_theorem_v4710_regression.py
```

The separate phone demo was also run successfully here: a new Z0 lineage generated 132 rational records in its first saved run and reached 296 after the saved continuation run. The damaged source and intact baseline stayed byte-for-byte unchanged. See the included demo output and test log.

The demonstration measures newly generated operational state. It does not claim arbitrary code repair, recovery of every deleted relationship, or authentication of lost history.
