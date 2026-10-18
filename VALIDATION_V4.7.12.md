# V4.7.12 — Task 5: independent domain verification

V4.7.12 adds read-only mathematical replay across the five existing archives and fixes calculus results entering rational exploration. Existing exploration kernels, seed rules and archive identities remain in place. The memory compatibility version stays `4.1`.

## What changed

- `_Z5Replay` independently traverses typed parents and cross-archive sources, detects cycles, checks archive-local ID order, and validates each domain's result index.
- Rational replay uses Fraction arithmetic and validates symbolic/calculus sources. The existing independent rational metadata, foundation, recipe, manifest and lineage checks remain active.
- Complex results are recalculated using separate rational-pair formulas for addition, subtraction, multiplication and division. Seed identities, real-axis embeddings, symbolic bridges, expressions and depths are checked.
- Symbolic results are replayed from allowlisted construction trees and checked against their exact encoding. Ordinary operation trees must match recorded parents. Current construction imports must retain source construction structure. Zero-slot and positional nexus records must match their declared transformation. Historical representative imports retain their older scope.
- Polynomial calculus is recalculated from coefficient lists using separate Fraction formulas. Imports, parents, variable-role bindings, expressions, depth, optional proof metadata, integral-family qualification and polynomial zero-limit justification are checked. Legacy operations before the saved role-origin boundary are identified separately rather than assigned invented variable origins.
- Role replay checks the zero origin, names, payload preservation, variable introduction, numeric selection, paths and foundation-backed slots.
- All these checks feed the existing zero-core verification operation, candidate approval and normal-save gate. A wrong new record is rejected even if its newly created manifest digest agrees with it.
- A constant calculus result now carries `calculus_source` in its rational leaf. The rational verifier validates that source instead of requiring the result to be an emergent foundation integer. Legacy plain-leaf bridges and their rational descendants are supported through recorded parent/source evidence without rewriting their archived trees.
- Non-rational verification findings retain archive-qualified identity. The older rational repair worker leaves those cases unresolved instead of attempting to repair a rational record with the same integer ID. General non-rational repair is a later task.
- Rejected normal runs can save diagnostic proposals after excluding runtime-only caches; the active memory remains unchanged.

## Reproduced audit failures: before and after

| Probe | V4.7.11 audit | V4.7.12 |
| --- | --- | --- |
| Fault-injected complex sum: expected 0+i, stored 123+0i | Accepted | Rejected |
| Fault-injected derivative: derivative of 1 stored as 1 | Accepted | Rejected |
| Valid 7 → 7x → 7x² → 14x → 14, creating a new rational 14 | Rejected | Accepted; actual continuation saved |
| Wrong symbolic value/tree made internally consistent but unsupported by its parents | Incomplete general checking | Rejected |
| Distinct alternate parents for the same rational tree | Deduplicated | Unchanged; separate backlog item |
| Missing non-rational construction | Pending | Unchanged; separate reconstruction task |

Fault injection demonstrates verifier behavior, not that the ordinary exploration kernels produced the injected wrong calculations.

## Validation performed

Host runtime: Python 3.12, SymPy 1.14.0.

**66 regression tests passed:** the preceding 40 release checks redirected to V4.7.12, plus 26 domain-focused checks. Runtime was about 41 seconds on the development host; this is not a phone timing estimate.

The domain checks include all four complex binary operations and all four calculus operations with deliberately wrong outputs and matching manifest digests; symbolic value/parent/import/nexus disagreement; role payload/variable faults; cross-domain cycles; every domain's result index; legacy calculus boundaries and bridges; integer and fractional calculus outputs; rational feedback from the new bridge; and normal-save refusal that preserves the active file.

The replay checker was also run with exploration kernels replaced by functions that raise if called, confirming that its formulas do not dispatch back into those kernels. Symbolic replay still shares SymPy with exploration: this is separate replay logic using a common algebra backend, not a separate formal-proof implementation.

A real engine continuation after the new rational 14 bridge validated and saved, preserving the existing record prefix. Prior adaptive tests also exercised recovery, regeneration, interruption/resume, source preservation, branch selection and saved continuation.

The exact 10-check phone runner passed locally. User-device confirmation of this release remains outstanding.

## Phone instructions

1. Download `zero_theorem_task5_tests.zip` from this repository.
2. Extract it into its own folder. Keep the included files and fixture subfolders together.
3. In Pydroid3, open **run_task5_tests.py** and press Run.
4. Expect `TASK 5: 10 / 10 checks passed.` A detailed `task5_phone_results.json` is saved in the extracted folder.

The runner uses disposable fixture copies and never opens the user's live memory or an existing adaptive-work folder. SymPy is required, as in the previous engine bundle. Do not move the ongoing 2,252-record adaptive trial into this test bundle; it is a separate experiment.

For all 66 checks on a suitable environment:

```bash
python3 run_task5_tests.py --full
```

For a read-only observation from Python:

```python
report = engine.zero_core(memory, 'verification', operation='observe')
print(report['typed_replay'])
```

The existing `--verify-candidate PATH` command performs verification feedback on an isolated copy and writes reports/candidates; it does not overwrite the supplied source.

## Scope and remaining work

The checker verifies recorded, supported operations against declared rules. It does not establish novelty, exhaustive exploration, arbitrary expression equivalence, authenticated historical restoration, or a new mathematical theorem. It uses supplied seeds and operation definitions. Symbolic replay has a defensive exponent allowance of numerator magnitude/denominator at most 4,096; work beyond that returns unresolved rather than attempting an unbounded power. Normal exploration retains its existing tighter settings.

A legacy plain-leaf bridge is accepted only with a verified typed calculus source and inherited parent evidence. Records without adequate evidence remain unresolved. The stored historical role-origin boundary marks earlier data; it is not an externally authenticated historical fact.

The original V4.7.11 audit remains a historical checkpoint. This release addresses its first priority. General reconstruction across domains, automatic old-recovery retries, alternate-parent retention, and consistent resource-deferred retries remain subsequent tasks. It does not silently change those exploration policies.
