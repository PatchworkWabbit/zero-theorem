# V4.7.13 — Task 6: typed-domain reconstruction

This release extends evidence-based missing-record reconstruction to the complex, symbolic, polynomial-calculus and role archives. Recovered records retain their archive-local IDs; subsequent records, indexes, queues and construction identities are not renumbered. Existing rational binary reconstruction remains available.

## Reconstruction mechanism

1. Normalize records into stable slots on a copy. Duplicate IDs, inconsistent manifest counters and changed surviving records still block recovery.
2. Read a typed recipe describing operation, pathway, parent IDs, typed sources and necessary representation options. Recipes do not store computed outputs such as values, polynomial coefficients, symbolic exact values, role payloads or full construction trees.
3. Verify surviving dependencies with the independent Task 5 checker, then reexecute the declared rule through the existing zero core. Rebuild the expression and metadata from its inputs.
4. Require the rebuilt construction payload to match its retained SHA-256 digest. Independently replay the rebuilt construction as well. A faulty operation kernel is rejected even if the retained digest was made to agree with its wrong output.
5. Restore the original slot and its derived unified lookup key without appending a new construction or incrementing accepted-record passage counts.
6. Repeat while progress is made, allowing dependencies to cross archive order. Missing evidence, unsupported rules, cyclic dependencies and disagreements remain pending. Failed attempts retain their outcome/reason in the recovery state.
7. Once all slots are resolved, repeat the existing structural checks and full independent observation before permitting normal exploration or approval.

The fixed-point pass is finite and bounded by the number of missing slots and the existing archive/gap limits. It is not an unbounded mathematical search. Resource restrictions on the supplied operation kernels still apply.

### Supported typed recipes

| Archive | Reconstructed construction types |
| --- | --- |
| Complex | Explicit i/−i seeds, registered real-axis embeddings, exact +/−/×/÷, typed symbolic-to-complex embeddings |
| Symbolic | Numeric construction imports, ordinary supported algebraic operations, symbolic zero-slot substitutions and positional constructions |
| Calculus | Typed rational constant imports, differentiation, integration, multiply-by-x and polynomial limit at zero, including variable binding and output qualifications |
| Roles | Foundation-zero origin, naming while preserving payload, variable introduction and registered numeric selection with foundation-backed slots |

Seed reconstruction reapplies supplied seed rules. It is not discovery of the imaginary unit without a definition or authentication of an erased event history.

### Existing archives and legacy evidence

On a healthy load, V4.7.13 validates the archive before augmenting surviving non-rational manifest entries with typed recipes. Existing construction payloads are unchanged. New records receive recipes as they are tracked. A supplied typed recipe must agree with its intact record; contradictions block acceptance.

For older missing records that lack a typed recipe, bounded reconstruction can use retained construction keys and, for symbolic nexus work, a matching retained event. Stored calculus output coefficients in old identity keys are deliberately ignored as repair answers; outputs are recalculated from sources/parents. Digest and independent checks still apply.

Legacy complex symbolic embeddings lack source IDs in their construction keys. If their typed recipe is absent, the engine leaves them pending rather than choosing an equal-valued symbolic origin. Missing both a recipe and usable legacy evidence also remains pending. A healthy current checkpoint therefore provides stronger future repair evidence than an already damaged legacy file.

Retained digests and recipes are evidence from this memory, not externally authenticated proof of chronology. No intact baseline file is read by the typed repair functions. Recovery does not reconstruct arbitrary erased data without surviving constraints.

## Validation

The frozen fixture contains 296 rational records and **258 non-rational records**: 126 complex, 88 symbolic, 20 calculus and 24 roles.

The release suite consists of **88 tests**: the 66 preceding release checks redirected to V4.7.13 and 22 new recovery tests. One recovery test separately deletes and reconstructs each of the 258 non-rational records, checking its original construction payload. The new suite also covers:

- simultaneous missing records in all four added domains;
- missing parent/child chains within each domain;
- role-to-calculus and symbolic-to-complex dependency chains;
- deletion of all 258 non-rational records while their recipes, rational archive and supporting archive structures remain;
- absence of output payloads in typed recipes;
- supported legacy-key recovery and deliberate unresolved legacy ambiguity;
- contradictory recipes, changed surviving records, missing references and duplicate IDs;
- recipe cycles that remain pending;
- unchanged accepted-record passage counts and complete passage coverage;
- a fault-injected reconstruction kernel whose wrong result also matches the modified retained digest, rejected independently;
- source-byte preservation, exact restored payloads and a real saved continuation of the recovered copy;
- adaptive selection of the recovery branch for supported typed damage;
- no repair-time file access to a hidden baseline.

These tests establish the tested construction types and fixtures, not arbitrary corruption recovery. The test that deletes entire non-rational record lists retains recipes, indexes, keys, queues, the rational archive and program rules; it is not deletion of all information.

All 88 regression tests passed on the development host in about 113 seconds. Two focused legacy/passage checks also passed after finalizing the restored passage metadata. The extracted 10-check phone runner passes locally before publication. User-device confirmation of V4.7.13 remains outstanding. Task 5/V4.7.12 was independently confirmed on the user's Android device: 10/10 selected checks passed.

See `task6_regression_results.txt` and `task6_case_results.json` for release evidence.

## Phone instructions

1. Download `zero_theorem_task6_tests.zip` from this repository.
2. Extract it into its own folder, keeping the fixture subfolders beside the runner.
3. Open **run_task6_tests.py** in Pydroid3 and press Run.
4. Expect **TASK 6: 10 / 10 checks passed.** Results are saved as `task6_phone_results.json` in the extracted folder.

The runner uses disposable copies of the bundled fixtures. It does not open live user memory or the separate ongoing adaptive regeneration trial. Python 3 and SymPy are required, as before.

For the complete suite:

```bash
python3 run_task6_tests.py --full
```

The full suite includes all 258 individual deletion probes, so allow more time than the selected phone checks. Timings on the development host do not predict phone timings.

## Remaining work

This release addresses the four added archive domains. It does not add general recovery of every rational positional/nexus/foundation pathway, automatic evidence-triggered retries of an old recovery trial after regeneration is selected, alternate-parent retention for deduplicated rational trees, or consistent reactivation of every resource-limited construction. Those remain separate tasks. General non-rational contradiction repair is also distinct from missing-slot reexecution; a changed surviving record continues to block rather than being silently replaced.

The previous audit and blueprint remain historical checkpoint documents. No operation meanings or new mathematical domains were added here.
