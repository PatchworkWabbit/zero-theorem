# Zero Theorem

Emergent Information Engine

Project status: Experimental research software
Current development version: V4.7.16 (independent zero time clock and process-time observations)
Original concept: 2012
Repository: PatchworkWabbit/zero-theorem

Latest audit: [V4.7.16 repository and resilience audit](AUDIT_V4.7.16.md).
The current development files are on `feature/zero-time-observer`; `main`
still contains V4.7.13 pending review of stacked draft PRs #3, #4 and #5.

## V4.7.16: Independent zero clock and time observer

- [Current engine: zero_theoremV4.7.16.py](zero_theoremV4.7.16.py)
- [Time observer phone tests](https://github.com/PatchworkWabbit/zero-theorem/raw/refs/heads/feature/zero-time-observer/zero_theorem_time_observer_tests.zip): extract in its own folder, open **run_time_observer_tests.py**, press Run. Expect **TIME OBSERVER: 11 / 11 checks passed**.
- [Timing semantics, validation and phone instructions](VALIDATION_V4.7.16.md)

The independent zero clock starts at **T0 = 0** and registers further clock states as newly observed foundation states and accepted constructions expand mathematical space. It has its own `.zero-clock.json` ledger and state transformations. It does not use the role grammar or wall timers to generate its states. Use **zero-clock** at the query prompt to inspect it. Existing projects establish a fresh observation boundary at zero; earlier clock history is not invented.

Separately, process phases send clock observations through Z0: UTC timestamps, elapsed time relative to a fresh zero, CPU duration and persistent event order. A restart links to the previous session while leaving any unobserved duration unknown. Timing records are stored in separate `.time-observer.json` files beside the observed memory or recovery input. Mathematical construction records and queue rules are unchanged.

The observer covers loading, foundation emergence, queue exploration, role/calculus work, verification/saving and adaptive recovery/retry phases. It does not timestamp every arithmetic call. Use **time** at the query prompt to inspect the current memory's timings. Stage durations include nested work, so they must not be added together as total runtime. Normal process duration includes time at interactive query prompts.

V4.7.16 includes the prior Task 7 retry feature. After the disposable phone tests, place its engine script in the existing **Maths** folder beside the original JSON and complete `.adaptive-work` folder, then open that script and press Run.

## V4.7.15: Task 7 recovery feedback

- [Current engine: zero_theoremV4.7.15.py](zero_theoremV4.7.15.py)
- [Phone test bundle](https://github.com/PatchworkWabbit/zero-theorem/raw/refs/heads/feature/task7-recovery-retries/zero_theorem_task7_tests.zip): extract in its own folder, open **run_task7_tests.py**, press Run. Expect **TASK 7: 10 / 10 checks passed**.
- [Validation and phone installation](VALIDATION_V4.7.15.md)

Normal runs of the selected regenerated branch now service preserved recovery checkpoints. Retries are triggered by changed executable rules, changed recovery checkpoints, newly available constructions matching retained payload digests, or unfinished feedback work. Matching numbers alone do not supply historical evidence. Exact-matching constructions supply recipe proposals; the existing workers independently reexecute and validate them.

A verified recovery candidate is retained separately. The active regenerated branch continues, and the original source and active selection remain unchanged. No authenticated historical chronology is claimed. Each retry admits at most eight recipe proposals and eight verifier executions. Parsing and validation are indivisible, so the two-second allowance is cooperative.

After the phone tests, put the latest engine (currently **zero_theoremV4.7.16.py**, which includes this feature) in the existing **Maths** folder beside the original memory JSON and its complete `.adaptive-work` folder; open that script in Pydroid3 and press Run. It follows the existing active pointer and automatically services the old recovery trial. On 18 October 2026 the user confirmed retry attempt 1 remained pending while the established regeneration branch completed run 33. A recovered candidate or memory merge was not demonstrated by that run.

## V4.7.14: Continue valid memories beyond 24 MiB

- [Current engine: zero_theoremV4.7.14.py](zero_theoremV4.7.14.py)
- The 24 MiB damaged-text search allowance no longer blocks valid growing memories or valid adaptive sources.
- Oversized memories must pass strict JSON, archive, foundation, arithmetic and link validation. Text observations still pass through Z0.
- Damaged oversized input remains unchanged; this change does not remove the text-repair search budget.
- Existing adaptive checkpoints and pending queues continue through the existing resume workflow. Keep the script alongside the original memory and its `.adaptive-work` folder; do not replace the source with a regeneration trial.
- User-provided Android output confirmed V4.7.14 selected regeneration and continued through normal run 32.

## V4.7.13: Task 6 typed-domain reconstruction

- [Current engine: zero_theoremV4.7.13.py](zero_theoremV4.7.13.py)
- [Task 6 phone test ZIP](https://github.com/PatchworkWabbit/zero-theorem/raw/refs/heads/main/zero_theorem_task6_tests.zip)
- [Validation, reconstruction scope and phone instructions](VALIDATION_V4.7.13.md)
- [88-test regression result](task6_regression_results.txt)
- [Reconstruction case evidence](task6_case_results.json)

Typed recipes now support missing complex, symbolic, polynomial-calculus and role records. The engine reexecutes rules from retained parents and sources, requires the original construction digest, then independently checks the result. Stable IDs and accepted-record passage counts are preserved. Missing dependencies, contradictory evidence and unsupported legacy cases remain pending.

All 88 release tests passed, including individual deletion/reconstruction of every one of the fixture's 258 non-rational records and reconstruction when all four non-rational record lists were missing while their recipes and supporting structures remained. Cross-domain chains, faulty-kernel rejection, source preservation, adaptive recovery selection and actual saved continuation were tested. These are constrained reconstruction results, not recovery after erasing all information.

Extract the Task 6 ZIP in a separate folder, open **run_task6_tests.py** in Pydroid3, and press Run. Its 10 selected checks pass in the extracted bundle on the host; user-device confirmation of V4.7.13 remains outstanding. Disposable fixtures are used and no live user memory is opened. The prior adaptive regeneration trial can remain in its own folder.

## V4.7.12: Task 5 independent domain verification

- [Current engine: zero_theoremV4.7.12.py](zero_theoremV4.7.12.py)
- [Task 5 phone test ZIP](https://github.com/PatchworkWabbit/zero-theorem/raw/refs/heads/main/zero_theorem_task5_tests.zip)
- [Validation, scope and phone instructions](VALIDATION_V4.7.12.md)
- [66-check host regression result](task5_regression_results.txt)
- [Reproduced audit probes](task5_probe_results.json)

Read-only replay now checks supported rational, complex, symbolic, calculus and role constructions against their parents and typed sources. Incorrect complex/calculus outputs identified by the V4.7.11 audit are rejected even with internally consistent digests. The valid calculus chain `7 → 7x → 7x² → 14x → 14` now creates a verified rational bridge and completes a saved continuation. Legacy bridge evidence is preserved. Non-rational findings stay separate from the rational repair queue.

All 66 host regression tests pass. The user's Android run independently confirmed **10 / 10 selected checks passed**; see [phone confirmation](task5_android_confirmation.txt). Extract the ZIP in a separate folder, open **run_task5_tests.py** in Pydroid3 and press Run. It uses disposable fixtures and does not open live user memory. The bundle includes the engine, all test code and fixtures for the full suite. The existing adaptive trial can remain in its own folder.

The V4.7.11 audit below remains a historical checkpoint. General non-rational reconstruction, automatic evidence-triggered recovery retries, alternate-parent retention and consistent resource-deferred retries remain subsequent work. Symbolic verification shares the SymPy backend; these checks are not a formal proof or novelty claim.

## Reconstruction blueprint and zero-functionality audit

- [Reconstruction blueprint: development stages, architecture and rebuild tests](docs/ZERO_THEOREM_RECONSTRUCTION_BLUEPRINT.md)
- [V4.7.11 zero-functionality audit: confirmed coverage, reproducible probes and remaining work](docs/ZERO_CORE_AUDIT_V4.7.11.md)

The blueprint explains how the engine was built and how to reconstruct its design. The audit distinguishes tested recovery/regeneration behavior from remaining verification, reconstruction and feedback gaps. These documents describe the V4.7.11 checkpoint; they do not change the engine.

## V4.7.11: controlled damage experiments

- [Current engine: zero_theoremV4.7.11.py](zero_theoremV4.7.11.py)
- [Task 4 phone test ZIP](https://github.com/PatchworkWabbit/zero-theorem/raw/refs/heads/main/zero_theorem_task4_tests.zip)
- [Task 4 results, scope and instructions](TASK4_RESULTS.md)
- [Machine-readable results](task4_results.json)

The 15-case matrix covered deleted paths, dependent paths, altered values/parents, duplicate IDs, contradictory recovery recipes, number-data erasure for 4/1/0 with and without selected recovery evidence, and a reproducible byte cut. Six damaged cases restored the baseline's archived record content; eight used validated fresh-lineage regeneration; the control continued normally. All selected branches validated, continued and saved. Forty regression checks passed.

V4.7.11 also closes a recipe-consistency gap found by these tests: a saved rational recovery recipe must agree with its intact expression record before approval. For the phone confirmation, extract the ZIP and run `run_task4_tests.py`; it creates independent copies and checks three representative cases.

## V4.7.10: verification and adaptive recovery

- [Current engine: zero_theoremV4.7.10.py](zero_theoremV4.7.10.py)
- [Download the complete phone demo and test ZIP](https://github.com/PatchworkWabbit/zero-theorem/raw/refs/heads/main/zero_theoremV4.7.10_adaptive_tests.zip)
- [Validation, scope and instructions](VALIDATION_V4.7.10.md)

For the phone demonstration, extract the ZIP into a separate folder, open `run_task3_demo.py` in Pydroid3, and press Run. The ZIP includes the engine, fixture, demo and 38 passing tests. Python 3 and SymPy are required.

This version executes independent rational verification feedback and compares isolated recovery and Z0 regeneration trials using measured elapsed time and a declared operational record floor. Each ready branch must validate and complete a further saved exploration run. The original source and comparison baseline are preserved. Regeneration carries a new-lineage marker; it is not presented as restored historical provenance.

## Overview

Zero Theorem is an experimental mathematical and computational engine exploring how states, operations, and interconnected pathways can emerge from a minimal foundation.

The project begins with zero as a persistent operational nexus.

Rather than requiring a predetermined mathematical destination, the engine explores the results generated by its defined rules, records their ancestry, and preserves observations for subsequent investigation.

The central research question is:

What mathematical structures and computational behaviours can be generated from a precise foundational system of zero, state emergence, and reusable operations?

## V4.7.8 recovery and same-run resume

The latest standalone script is [zero_theoremV4.7.8.py](zero_theoremV4.7.8.py).
Install SymPy once, then open this script in Pydroid3 and press Run, or use:

```bash
python3 -m pip install -r requirements.txt
python3 zero_theoremV4.7.8.py
```

Memory lives beside the script as `zero_theorem_rabbitholes_v41_memory.json`.
For a fresh experiment, use a writable folder without an existing memory.
For recovery experiments, use a test copy of damaged memory and keep its
recovery sidecars beside it. Existing V4.7.5 candidate-ready checkpoints are supported.

When recovery finds one unambiguous candidate that passes validation, V4.7.8
checks the foundation, archive links, rational trees, metadata and supported
construction re-execution; preserves the exact damaged bytes in a
`.pre-v478-<SHA256>.bak` file; atomically installs the approved memory; and
continues normal exploration **in the same run**. The saved memory records
successful continuation only after the engine completes and saves its run.
Normal exploration remains bounded per run and ends at the archive query prompt.

To approve an explicit candidate and continue, optionally choosing the output memory:

```bash
python3 zero_theoremV4.7.8.py --resume-candidate CANDIDATE.json
python3 zero_theoremV4.7.8.py --resume-candidate CANDIDATE.json MEMORY.json
# Inspection/recovery without promoting a candidate:
python3 zero_theoremV4.7.8.py --repair-json /path/to/test-memory.json --seconds 60
# Read-only candidate arithmetic report:
python3 zero_theoremV4.7.8.py --verify-candidate CANDIDATE.json
# Assessment only; does not reset or resume:
python3 zero_theoremV4.7.8.py --adaptive-recovery CANDIDATE.json INTACT-BACKUP.json
# Reproducible tests, without user memory:
python3 -m unittest -v test_zero_body_recovery test_zero_resume
```

A candidate that fails validation, a stale source fingerprint, or conflicting
ready candidates blocks automatic approval. Recovery checkpoints retain paused
work. Exact historical restoration is distinct from operational acceptance:
unknown damaged spans remain recorded, and this release does not claim that
every original byte or historical event has been restored.

On the damaged test memory, expressions **20, 22, 23, 116 and 117** were
reconstructed from surviving evidence. Fresh recovery and the saved-candidate
handoff both resumed successfully, grew the rational archive from **132 to 296**
records, and saved. A further run reached **437** rational records.
The user's Android V4.7.8 run independently reported successful continuation,
complete zero-core passage coverage across all **554** archive records, and
**zero structural issues**. No user memory is included in this repository.

See [VALIDATION_V4.7.8.md](VALIDATION_V4.7.8.md) for verification scope.
Earlier scripts and [V4.7.5 validation](VALIDATION_V4.7.5.md) remain available.

## Previous V4.6.5 release

## Running V4.6.5

The runnable file is [zero_theoremV4.6.5.py](zero_theoremV4.6.5.py). It uses Python 3 and SymPy for exact algebraic calculations. Install the dependency once:

```bash
python3 -m pip install -r requirements.txt
```

On Android, open Pydroid3's Pip screen and install `sympy`. Then open and run the script. After installation, exploration works offline with no API key or subscription. The extension was tested with SymPy 1.14.0.

V4.6.5 is a separate script; the earlier script is retained as a code backup.

Download the file into a writable folder. From that folder, run:

```bash
python3 zero_theoremV4.6.5.py
```

If your Python 3 command is `python`, use `python zero_theoremV4.6.5.py`. On Android, open the saved file in Pydroid3 and run it.

Each execution performs a bounded exploration batch, saves memory, and then opens an archive query prompt. Press Enter on an empty line to exit. Run the same file again to continue the saved exploration.

Memory is stored beside the script as `zero_theorem_rabbitholes_v41_memory.json`, regardless of the terminal's working directory. A fresh run starts with foundation `[0]` and registers three further states, reaching `[0, 1, 2, 3]` before saving. The foundation printed at startup is the state before that run's new emergence events.

The script's internal `VERSION = '4.1'` and the `v41` memory filename are retained for memory compatibility; the runtime banner identifies V4.6.5. Do not rename the memory file or change the version value just to match the script filename. Loading requires memory schema `1` and version `4.1`; this check alone does not guarantee compatibility with every historical file.

For a separate fresh experiment, put a copy of the script in another writable folder without an existing memory file. Back up existing memory before experimenting with it.

### V4.6.5 legacy positional observation audit

Older V4.2 memories include explicitly labelled positional observations with `result_id: null`: those events did not create archived expressions. The audit now identifies and counts that historical format separately, checks its position/source/transformed-text metadata and zero reference, and continues rejecting invalid expression references. No memory migration, guessed result links, or arithmetic-rule changes are required.

Validation: 30 regression tests pass. An uploaded run-14 memory with 3,961 expression records produced 108 false alarms under V4.6.4; V4.6.5 reports 108 legacy observations and zero structural issues on the same unchanged memory. A continuation of a temporary copy reached run 15 and passed the audit, preserving every pre-existing expression record and nexus event exactly. The user's memory is not included in this repository.

### V4.6.4 construction-complete imports, unified queries and whole-engine tracking

V4.6.4 addresses archive and tracking connections while retaining the definitions of the mathematical operations. Validation includes **25 passing regression tests**, actual continuation runs, upgrade exercises and interactive/standalone command checks. See [VALIDATION_V4.6.4.md](VALIDATION_V4.6.4.md) for the scope and limits.

#### Every source construction can enter symbolic exploration

Imports now scan **expression IDs**, rather than taking one representative per value. Two records with equal values retain separate source links and symbolic records when they represent different constructions. Their operand order, construction trees, zero leaves, source IDs and inherited depth are retained.

Both rational and complex source constructions are included. Old representative imports remain archived. Where an older complex import retained only a simplified value, a separate complete import is added; the older record and any historical nexus references remain unchanged.

The source-to-symbolic link map is explicit and persistent. Numeric records that merely embed an existing symbolic construction link back to that symbolic origin, preventing endless symbolic-to-numeric-to-symbolic copies. These representation links do not collapse distinct arithmetic constructions.

Imports are bounded by `SYMBOLIC_IMPORT_PER_RUN` source records per numeric archive. Persisted construction cursors cover the backlog across subsequent runs. Records outside configured depth/value limits remain in their source archive and are listed in `import_deferred`; changes to import-relevant limits restart a source scan so those records can be reconsidered. Imported records at the exploration depth limit remain archived under the existing feedback limits.

#### Value queries include all archives

An ordinary query such as `2` now includes rational, complex and symbolic records for that value. A symbolic construction `sqrt(2)*sqrt(2)` remains visible even when `2` was already known in the native numeric archives. Queries such as `2+0i` and `symbolic sqrt(2)**2` use the same lookup.

The unified index retains typed archive IDs rather than merging the records themselves. Representation records are labelled, so totals are not presented as counts of algebraically unique formulas. Exact Gaussian-rational results are normalized consistently across branches; general algebraic equivalence is not completely decided by this index.

The existing domain-specific discovery indexes remain available. Value queries and counter reports are read-only and do not launch new exploration.

#### Complete accounting with explicit historical scope

The original `network` counters remain as legacy rational recorded-transition counters. The new `archive_integration` tracking distinguishes:

- **Accepted archive records:** rebuilt from all stored rational, complex and symbolic records, with categories for foundations, seeds, representations, arithmetic and nexus constructions.
- **Runtime mathematical kernel calls:** counted from the tracking boundary onward across all three domains, with computed, blocked and resource-limited outcomes, operation names and execution contexts.
- **Nexus records and task activity:** retained in their existing event/ledger structures and displayed alongside the new totals.

A recorded construction's outer operation and an actual runtime call are different measurements. Repeated calculations, blocked operations and nexus tree reevaluations contribute runtime calls even when no new expression is accepted. Mathematical proposal calculations retain their proposal context; they are not promoted into accepted discoveries. Backend implementation steps inside Fraction or SymPy are not counted as separate engine operations.

Counters continue updating when journal details are suppressed. Historical accepted-record totals are reconstructible; historical attempted/failed calls are not fabricated from surviving expressions.

Use `operations` or `totals` at the query prompt to inspect these measurements.

### V4.6.3 resumable budgets, typed tracking and link audit

At the V4.6.3 release, this patch had only been inspected statically. The later V4.6.4 validation includes actual V4.6.3 baseline executions and link audits, plus the current regression suite.

A work budget means a workload allowance per execution. The phone-oriented limits remain configurable. They are separate from the bug where a partially completed arithmetic pair could abort before saving the run.

Pair, frontier and revisit workers now keep an `op_cursor`; rational zero transformations keep a `zero_cursor`. When the expression budget is reached partway through one of these tasks, the current task remains pending with its next operation/slot. The normal save path preserves both completed expressions and the resume position. A paused task receives a pause event rather than a completion event. This handles the known expression-budget exit; it is not a guarantee against unrelated crashes, storage failures or interrupted processes.

New parent-ledger rows use archive-qualified labels such as `rational:17`, `complex:17` and `symbolic:17`. Positional tasks use a qualified reference-slot label. Existing expression IDs stay stable. Earlier untyped ledger rows remain preserved as historical totals; the code does not guess an archive assignment for old mixed aggregates. A boundary record identifies the change.

The new read-only structural command is:

```bash
python3 zero_theoremV4.6.5.py --integrity
```

It loads existing saved memory without launching exploration, upgrading memory, saving changes or evaluating mathematical expressions. This command alone uses the standard library; normal exploration still requires SymPy. With no saved memory, it reports that there is no archive to inspect. `integrity` is also available at the interactive query prompt, after a normal exploration run.

The checker builds a typed dependency graph from recorded expression parents and cross-archive source references. It adds dependencies of the declared foundational state-count rule and treats explicitly seeded elements such as `i` and `-i` as declared roots.

Its report covers stored ID positions, missing parent/source references, same-archive parent order, result-index references, zero-record identities, observer and zero-proposal references, nexus-event references, pending task references and selected resume-cursor ranges. A topological walk identifies records in or depending on cycles. Reachability is reported from zero and from the full set of declared roots.

The checker inspects the currently saved graph. It does not enumerate all possible mathematical paths, prove expressions correct, reconstruct suppressed historical events, renumber records or repair broken links. Numeric ID order across different archives is not treated as execution order.

### V4.6.2 zero archive access, lineage and feedback

At this release, execution and regression tests were deferred. The later V4.6.4 validation covers the continued zero-archive-access implementation.

The rational zero-nexus scheduler no longer checks only the first 30 expressions or searches expression text for the character `0`. It inspects numerical leaves in construction trees. A leaf with value 10 is therefore not confused with a zero operand.

Two saved cursor tasks connect the existing zero-slot mechanism across time:

- `zero_scan`: a new registered foundation value scans the archive present at its registration, one expression per task.
- `zero_source`: a new zero-bearing expression receives previously registered nonzero foundation values, one value per task.

Previously archived expressions and foundation values are also scheduled when this runtime extension is first enabled. These are bounded scheduling passes, not a claim of exhaustive mathematical coverage. Scans share `NEXUS_WORK_PER_RUN` with the original nexus transformation worker, and queued work can take many runs to complete.

The underlying transformation remains `zero_nexus_transform_v1`: replace one numerical zero leaf with a selected registered integer and evaluate the resulting expression using ordinary arithmetic. Fractional and algebraic selections remain supported by the symbolic zero-nexus branch introduced in V4.6.1.

New rational nexus results now notify the result-feedback frontier as well as the existing revisit mechanism. The leaf list is calculated from the transformed tree. A one-time metadata augmentation recalculates incorrect leaf lists in older rational nexus records, retaining their IDs, expression trees and ancestry; repairs are recorded as current augmentation events.

Deferred nexus tasks remain pending and keep their deduplication keys. They are not logged as completed transformations when their per-run budget is exhausted.

This patch adds persisted task kinds. After it saves memory, continue with V4.6.2 for that memory. The earlier scripts remain code backups.

### V4.6.1 zero-nexus connection

This patch connected the exact powers/root branch to zero-slot constructions. Tests were deferred at that release; the later V4.6.4 validation covers the continued implementation.

The extension retains a construction tree separately from each simplified symbolic value. A construction that evaluates to zero still retains its original zero leaves, operators and operand order. Existing V4.6 records receive these trees using their stored parents and source references.

The zero-nexus worker can replace one numerical zero leaf in a construction with an available symbolic construction. It evaluates the resulting expression using the same standard arithmetic, power and principal-root definitions. For example, the mechanism permits constructing `sqrt(2)` from a `sqrt(0)` construction by selecting `2` for its zero slot. This is a recorded expression substitution, not the numerical assertion `0 = 2`.

Positional zero slots from `00404` retain their existing arithmetic pathways and gain `0**n`, `n**0`, and unary `sqrt(0)` constructions. Positional digit selections use registered states 0 through 9, matching the earlier positional scope. General symbolic zero-slot feedback can select other available exact values, including fractions and complex/algebraic values within the existing limits.

New symbolic nexus tasks retain pair, direction and slot cursors between runs. They share the existing symbolic task budget. Successful constructions enter the same symbolic feedback and numeric archive bridges as other symbolic results. A construction already recorded under the same nexus pathway is not repeatedly archived solely because a different chain of parent IDs rediscovered it; duplicate attempts are journaled within the existing journal cap.

Zero-nexus provenance is attached to each new nexus record: the persistent `Z0` reference, the source construction and selected value IDs or original positional slot, and the selected zero path. Symbolic value queries display this metadata when present.

The foundation's state-count rule and ordinary meanings of the mathematical operations are retained. Domain restrictions and resource limits still apply. The actual behaviour of this unexecuted patch remains to be validated later.

After V4.6.1 saves its new task kinds, continue with V4.6.1 for that memory; previous scripts do not recognize those task kinds.

### V4.6 exact powers, roots and symbolic feedback

V4.6 adds an exact algebraic archive using SymPy. Its active operations are `+`, `-`, `*`, `/`, rational powers `**`, and principal square roots `sqrt`. Expressions such as `sqrt(2)` remain exact rather than becoming rounded decimals. This first integration does not enable all SymPy capabilities: free variables, equation solving, trigonometry and calculus are not yet exploration operations.

Each eligible symbolic expression is queued for a square root and resumable binary feedback. Self-pairs are visited first, followed by earlier expressions; distinct operands retain both orders. One operation is attempted per symbolic task. Construction expressions and parent IDs remain separate from simplified result forms, so `sqrt(2)*sqrt(2)` records its construction even when its value simplifies to `2`.

In V4.6 through V4.6.3, the rational and complex archives contributed representative values through import cursors. V4.6.4 replaces that selection with construction-by-construction source scans, as described above. Every original expression stays in its source archive.

Symbolic results that evaluate exactly to a new rational value or a complex value with rational components are embedded into the corresponding numeric archive. Typed source references retain their symbolic origins, and construction depth is preserved across the bridge. Existing numeric values keep their original entries; further symbolic derivations remain in the symbolic archive.

Resource limits include:

- `SYMBOLIC_WORK_PER_RUN = 24` operation tasks, plus bounded source imports.
- The existing `MAX_DEPTH = 4` and `MAX_BITS = 256`.
- At most 48 nodes in a simplified symbolic value.
- Power exponents must be rational, with absolute numerator at most 8 and denominator at most 8.
- Root operations involving rational components above 32 bits are skipped and counted as resource-limited operations.
- Division requires a denominator established as nonzero. Zero to a nonpositive power is skipped, including the convention-dependent `0**0`.

The limits bound scheduled work and expression size; they are not hard wall-clock or global-memory guarantees. Square roots and fractional powers use the principal complex branch; for example, `sqrt(-2) = sqrt(2)*I`. No branch-unsafe simplification is forced.

Symbolic values are stored as JSON trees using only rational numbers, `I`, sums, products and powers. Queries use a restricted arithmetic parser; query text and saved expressions are not executed as Python code.

The existing memory filename, schema and version are retained. After V4.6 saves symbolic tasks, continue with V4.6: older scripts do not recognize those tasks. Keep a copy of pre-upgrade memory if you want to resume an older engine separately.

Symbolic index keys are simplified expression forms, not a proof that different keys represent different mathematical values. Algebraically equivalent forms can have separate keys.

### Earlier complex feedback fix

V4.5.2 connected generated complex expressions to subsequent complex calculations, including self-pairs such as `i*i`. V4.6 retains that feedback, persistent pair cursors and depth checks. Existing archived expressions are preserved with their IDs and parent links.

### Regression checks

```bash
python3 -m unittest discover -p 'test_*.py' -v
```

The 30 current checks target V4.6.5. They cover exact arithmetic, feedback, archive bridges, distinct equal-valued constructions, complex operand order, unified queries, cross-domain counters, older-memory upgrades, serialization, forced budget pauses, import-loop prevention, deferred imports and structural audits. Details are in [VALIDATION_V4.6.4.md](VALIDATION_V4.6.4.md).

### Archive queries

Enter these at the prompt after a run, rather than as command-line arguments:

| Input | Behaviour |
| --- | --- |
| `5`, `1/2`, `.8` | Look up the value and matching records across all three archives |
| `i`, `-i`, `2+3i`, `1/2-4i` | Look up a complex value across all three archives |
| `index` or `values` | List archived rational values (up to 120 entries) |
| `index -10 10` | List rational values within an inclusive range |
| `gaps -30 30` | List integers in the range that are absent from the rational archive |
| `complex-index` | List complex values (up to 100 entries) |
| `operations` or `totals` | Show cross-domain runtime and accepted-archive totals |
| `integrity` | Inspect saved record links and dependency structure without generating expressions |
| `symbolic-index` | List up to 100 stored exact algebraic forms |
| `symbolic sqrt(2)`, `symbolic 2**3`, `symbolic sqrt(-2)` | Look up exact algebraic forms and their recorded constructions |
| `hubs` or `attractors` | Show observational convergence and echo counts |
| `echoes` | Show the summary plus retained echo examples |

Queries browse existing records; they do not launch a search for the entered value. An absent value is not evidence of unreachability.

## 1. Foundational Principles

The original model establishes the following sequence:

1. Begin with zero as a persistent operational nexus.
2. Register the transition from 0 to 1.
3. Preserve the recognised zero in a separate counter.
4. Make 2 available through the registered state count.
5. Recognise [0, 1, 2] as the first trinity, whose count is 3.
6. Continue the state-count emergence mechanism.
7. Assign each generation a fresh zero-operation record.
8. Explore mathematical pathways without automatically promoting observations into foundational rules.

The foundation is intended to remain stable while experimental modules are developed around it.

## 2. Numerical Transformation

One defined transformation expands numerical values into corresponding unit slots while preserving zero positions.

Example:

```text
Input:  00404
Output: 00111101111
```

Each nonzero digit is expanded into that number of unit symbols. Zero positions remain represented.

This operation is investigated as a numerical representation and transformation mechanism.

## 3. Zero Lifecycle

Zero operations receive distinct identities so their usage and availability can be recorded across generations.

Example record identifiers:

Z0, Z1, Z2, Z3, ...

The system distinguishes the persistent foundational concept of zero from individual operational records.

## 4. Mathematical Pathways

The engine explores alternative arithmetic routes and records their relationships.

Pathway exploration includes:

- Target-free tangent exploration. Earlier V2.x versions included target-based searches; this V4.6 script has no target-search command.
- Interconnected results and reusable values.
- Candidate operations derived from observations.
- Path ancestry and provenance.
- Bounded search for practical execution.
- Exact rational arithmetic, including negative results.
- A separate exact complex branch using rational real and imaginary components. The elements `i` and `-i` are explicitly seeded extensions, not derived from zero or the state-count rule.
- Exact algebraic powers and roots, with symbolic feedback and typed numeric archive bridges.
- Observational convergence hubs, real structural echoes (matching operator-tree shapes with opposite results), and complex conjugate echoes.

Different pathways producing the same numerical result are not automatically treated as equivalent computational histories. Rational expression identity includes both the construction tree and pathway rule; archive counts are not counts of algebraically unique formulas.

Observer proposals record value, variable, and operation-selection roles. They are candidates, not automatically adopted foundational rules. Zero-assisted denominator replacements are also recorded as unapproved observations; division by zero is blocked.

## 5. Persistent Memory and Indexing

The engine supports persistent JSON memory and indexed records to retain information across executions.

These records support exploration continuity, repeated-route identification, and inspection of earlier results. The queue and archives persist between runs. Work per run is bounded, but accumulated memory size and load/save time are not globally capped.

The genesis journal records logical event order with a per-run event cap; excess journal events are counted as suppressed. Earlier precise event ordering is not reconstructed when older memory is upgraded. Expression ancestry and the discovery index do not constitute a complete historical event log.

### V4.5.1 Reported Milestone

A recorded execution reported:

```text
Foundation: 0 through 21
Zero records: Z0 through Z21
Exact arithmetic and foundation checks: PASS
```

These results describe a previously reported continued execution, not the expected output of a fresh first run. The startup PASS message checks the consecutive foundation sequence, matching zero-record IDs, the `00404` transformation, and one exact fraction addition. It is not a full validation of every archived expression or subsystem. Broader independent validation remains future work.

## 6. Research Directions

Planned or proposed investigations include:

- Broader validation and exploration of the implemented negative and complex branches.
- Unbounded and symbolic exploration.
- Mathematical pattern identification.
- Candidate-operation validation.
- Computational complexity experiments.
- Algorithmic pathway comparison.
- Applications to economic simulation and other computational systems.

These directions are research objectives, not claims of completed capabilities.

## 7. Mathematical Status

Zero Theorem is currently an experimental computational framework.

Successful executions and internal consistency checks demonstrate specific implemented behaviours. They do not independently establish a new mathematical theorem or resolve an open complexity-theory problem.

The project is intended to support reproducible experimentation, rigorous testing, and mathematical investigation.

## 8. Development Philosophy

Precise foundations. Emergent possibilities. Preserved information.

The development approach prioritises:

- Maintaining established foundational rules.
- Minimising unnecessary changes.
- Preserving working versions.
- Separating observations from validated rules.
- Recording computational ancestry.
- Allowing results to be discovered rather than forced.

## 9. Publication

The V4.6 engine and the earlier V4.5.1/V4.5.2 prototype script are included in this repository. Further examples, test results, and technical documentation will be added as they are prepared and verified.

Contribution ideas, questions, and fixes are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

Licence: GNU General Public License v3.0 (GPLv3); see [LICENSE](LICENSE).

---

Zero Theorem — Emergent Information Engine

Original concept developed in 2012. Computational implementation and ongoing research developed subsequently.
