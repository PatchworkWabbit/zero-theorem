# Task 4: controlled damage experiments — V4.7.11

15 cases met their acceptance criteria: six damaged cases reconstructed the baseline's archived record content, eight used validated regeneration, and the untouched control continued normally. All selected archives continued, saved and reloaded with zero structural issues and zero independent rational-check contradictions. Baseline and damaged source bytes remained unchanged.

40 regression checks passed as well. Passing the matrix means correct validation, supported recovery or explicit new-lineage fallback; it does not mean every damaged archive was repaired.

## Phone confirmation

[Download the phone test ZIP](https://github.com/PatchworkWabbit/zero-theorem/raw/refs/heads/main/zero_theorem_task4_tests.zip), extract it, open **run_task4_tests.py** in Pydroid3, and press Run. It runs three representative cases: a single deleted path, zero-data deletion with selected recovery evidence removed, and a duplicate-ID conflict.

The runner locates the extracted folder, including Android Download locations, and creates its own test workspace. It does not open your normal engine memory. Keep the extracted folder together. If automatic discovery cannot locate it, the runner asks for the folder path.

## What was tested

The original 132-record fixture had foundation states 0–3. A copy completed one normal engine cycle to register 4, 5 and 6, producing the frozen 296-record rational baseline used here. The original fixture stayed unchanged. Its hash and the expansion checks are included in `task4_fixture/baseline_origin.json`.

Deletion cases preserve record ID labels rather than renumber survivors. The `records` variants retain redundant recipes and creation evidence. The `evidence` variants additionally redact the removed records' manifest contents, rational construction keys and rational creation events. Each mutation has an action log, exact removed IDs and source hashes.

Number erasure covers rational results/leaves, complex components, symbolic numeric constants/results, calculus coefficients, numeric role bodies, and their typed descendants. This is broader than deleting a single expression. IDs, counters, the foundation registry, other surviving journals and executable rules remain available. It is not a claim that every occurrence or mathematical trace of a number was erased.

The byte-damage case deletes 31 bytes at a reproducible, seed-404 position inside expression record 20. It tests that cut, not every possible byte deletion.

| Case | Records erased across archives | Selected outcome | Rational records after continuation |
|---|---:|---|---:|
| `control` | 0 | Control continued | 437 |
| `single_path_manifest` | 1 | Exact archive reconstruction | 437 |
| `single_path_legacy` | 1 | Exact archive reconstruction | 437 |
| `dependent_paths` | 2 | Exact archive reconstruction | 437 |
| `value_conflict` | 0 | Exact archive reconstruction | 437 |
| `parent_conflict` | 0 | Exact archive reconstruction | 437 |
| `duplicate_id_conflict` | 0 | New Z0 lineage | 437 |
| `manifest_recipe_conflict` | 0 | New Z0 lineage | 437 |
| `erase_4_records` | 78 | New Z0 lineage | 437 |
| `erase_4_evidence` | 78 | New Z0 lineage | 437 |
| `erase_1_records` | 342 | New Z0 lineage | 437 |
| `erase_1_evidence` | 342 | New Z0 lineage | 437 |
| `erase_0_records` | 404 | New Z0 lineage | 437 |
| `erase_0_evidence` | 404 | New Z0 lineage | 437 |
| `random_byte_span_404` | 0 | Exact archive reconstruction | 437 |

## Exact comparison and regeneration

For the six recovered damage cases, every original archived record payload across the rational, complex, symbolic, calculus and roles archives matched the frozen baseline after recovery and continuation. New records were also generated. Comparison excludes the zero-core passage marker and unified lookup-key metadata, matching the engine's manifest payload definition.

The regenerated branches also reproduced the baseline record payloads in these deterministic runs, then continued to 437 rational records. They remain explicitly marked as fresh Z0 lineages. This demonstrates repeatable generation under the retained program rules and scheduling; it does not authenticate the lost run's original chronology or prove arbitrary information recovery.

The intact baseline was supplied only to measure loss, define the operational floor and compare outputs. Regeneration seeded from the normal Z0 constructor, without copying baseline expressions into the new archive.

Number-erasure and conflicting-evidence cases remained unresolved as historical recovery during the work performed. Their snapshots, partial reconstructions and pending evidence were retained while the separate regenerated branch supplied operational continuation.

## Gap found and fixed

V4.7.10 did not report a contradiction when a saved recovery recipe was changed while its expression record stayed intact. The probe altered record 20's manifest recipe from multiplication to addition and observed zero reported contradictions.

V4.7.11 now compares each surviving rational manifest recipe with its record's tree, pathway and parents. Both independent verification and candidate approval reject disagreement. The contradictory recipe remains preserved as evidence rather than being silently rewritten. The conflict case selects a separately validated regenerated lineage.

This check detects internal recipe/record inconsistency. It does not authenticate coordinated edits to both records and all their evidence.

## Evidence and reproduction

The phone ZIP includes the engine, runner, frozen fixtures, case change logs, CSV/JSON summaries and regression tests. A separate full checkpoint evidence ZIP is saved with the experiment and preserves the actual source snapshots, partial candidates, trial memories, worker continuations and engine logs from the complete matrix. Extracted checkpoint evidence occupies approximately 155 MiB; it is not needed for the phone confirmation.

```bash
python run_task4_tests.py --all
python -m unittest -v test_zero_theorem_v4711_adaptive.py test_zero_theorem_v4711_regression.py test_recipe_consistency_v4711.py
```

Results are finite tests with the supplied executable rules preserved. Timings are local observations and were collected under test workload; they are not performance forecasts or proofs that unresolved paths cannot succeed later.

Engine SHA-256: `43a098ce73f051e48cbbd96f6b43ac295f13b003c234c218e1c44773435e9f7b`

Baseline SHA-256: `5d105759ce2655437c6177ac779c70a9dae8dfffcade67eee54d2e0d107ec900`

Full evidence ZIP SHA-256: `1bbaebe7c55aff9880b1ea8d814a391f2fa78261db075f88abf7cd3fb0c7000c`
