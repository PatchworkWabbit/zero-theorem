# Zero Theorem — reconstruction blueprint

Prepared for Luk (“Bunny”) and Milo, 18 October 2026.

Purpose: preserve enough of the design, development sequence, data structures, rules, tests and unfinished work to rebuild Zero Theorem if its source code and working archive are lost. This document is a specification and development record, not a complete copy of the executable. Keep an independent copy alongside a source release and an intact memory snapshot when those are available.

Current audited implementation: zero_theoremV4.7.11.py. Runtime: Python 3 with Fraction for rational arithmetic and SymPy for exact algebraic expressions. SymPy 1.14.0 was used in the reported verification runs. Android/Pydroid3 is the user's working platform.

## 1. The idea to preserve

Start small: 0. Register what exists, apply explicit rules, record what follows, and feed newly constructed results back into exploration. Preserve the pathways as well as the answers. If a pathway is damaged, use surviving construction evidence to attempt its reconstruction. If exact recovery remains unresolved, a separately identified branch may start again from Z0 and resume exploration.

The conceptual shorthand is:

0 → registered states → positive and negative rational branches → real and imaginary branches → symbolic structures → roles and variables → calculus → reconstruction and regeneration.

This is a dependency outline, not a claim that these extensions arrived in one operation or that all mathematical rules follow from the numerical value zero alone. The program supplies the counting rule, arithmetic rules, representation grammar and domain extensions. The engine explores their consequences.

“Everything through 0” means a shared operation and archive entry point named zero_core, with Z0 as the persistent nexus. It does not mean multiply everything by zero or replace all values with zero. Ordinary passage preserves the expression, value, typed sources and lineage. A transformation requires its own explicit rule.

The complex extension explicitly introduces i and −i, with i² = −1 under the supplied complex arithmetic. Zero is 0+0i. The program does not assert 0=i or 0=−i. Positive and negative real numbers arise through the supplied arithmetic; the imaginary unit is a declared extension of the domain.

## 2. How we got here: chronological stages

The earliest stages below are reconstructed from the retained project record. Later stages are supported by section headers and functions in the surviving V4.7.11 source. Where intermediate version attribution is not established, use the stage order rather than inventing a release number.

| Stage / version | What we added | Why it was added |
| --- | --- | --- |
| V0.1–V1.1 | Preserve digits, retain zero, decompose representations, apply arithmetic, record routes and allow independent branches | Keep the construction and its available ingredients, rather than retaining only an answer |
| V1.2–V1.4 | The 00404 demonstration, breakdown into ones, positional maps, slots and lineage | Show that zeros, positions and repeated occurrences carry structure |
| V1.5–V1.6 | A zero seed, counting chain, persistent zero identity and fresh zero-use records | Model registration of new states without consuming the persistent nexus |
| V1.7–V1.8 | Target examples: inputs [1,2,3] and [0,1,2,3] finding routes to 5 | Establish that different constructions can reach the same result |
| V2.2 | Interconnected pathfinder, observer and target-free exploration with persistent memory | Continue exploring beyond a single requested answer |
| Foundation work, retained in V4.1 | Live state-count emergence, arithmetic reuse/consume/revisit, zero nexus transformations | Let later registered states and discoveries open further pathways |
| V4.2 | Result frontier, operation and position slots | Feed computed results back into the worker network; make positional ideas operational |
| V4.4 | Genesis journal, tangent ledger and exact complex branch, including i and −i | Record discovery events and explore beyond rational real values |
| V4.5–V4.5.1 | Convergence hubs, structural/conjugate echoes and read-only discovery index | Inspect which constructions converge without changing their mathematics |
| V4.6 family | Exact symbolic/algebraic constructions using SymPy, roots, powers, source imports and bridges | Represent values such as √2 without decimal approximation; connect domains |
| By V4.6.6 | Central zero dispatch and accepted-record passage across the mathematical archives | Make the common 0 design an actual shared code path |
| V4.7 family / role paths in V4.7.1 | Typed cross-archive integration, whole-engine accounting, role transformations, archived variables and polynomial calculus | Link domains while preserving origin; distinguish a name, a variable and a numeric state |
| V4.7.2 | Stable recovery slots and manifests; supported rational reconstruction | Repair missing constructions using evidence rather than substitute an equal-valued record |
| V4.7.3 | Text roles and bounded punctuation search | Attempt recovery when damage affects serialized JSON structure |
| V4.7.4 | Resumable recovery nexus and checkpoints | Continue bounded recovery work across launches |
| V4.7.5 | Whole-body maps, zero slots and evidence bridges | Use more surviving file structure and relationships during recovery |
| V4.7.6 | Exact calculator/archive cross-check | Compare stored results with recalculation |
| V4.7.7 | Nondestructive recovery-versus-regeneration planner | Assess an alternative when recovery costs more than restarting exploration |
| V4.7.8 | Verified approval, backup and same-run continuation | Close the loop from a saved candidate to a validated active memory |
| V4.7.9 | Independent rational checks and an executed verification-feedback worker | Turn some unresolved verification findings into bounded actual work |
| V4.7.10 | Measured recovery/regeneration trials, fresh-lineage continuation and active-branch selection | Test usable restart behavior while preserving the damaged source |
| V4.7.11 | Check retained rational recipes against intact records as well as digests | Detect a contradictory recovery recipe even when its archive record survives |

### Stage A — preserve the representation before exploring it

The reference input is the string `00404`, not integer 404. The leading zeros must survive. Its retained breakdown is `00111101111`: each 4 expands to four occurrences of 1, while each original 0 remains. Keep a map back to the original digit positions and distinguish a numeric zero leaf from a positional slot.

Repeated operand occurrences matter. Two occurrences of 1 may have equal values and distinct places in a construction. Preserve both facts.

### Stage B — register new states from the zero foundation

A fresh current-model memory starts with states [0], rational record 0 and zero record Z0. Counting the registered states gives the next state:

- [0] has one registered state: register 1.
- [0,1] has two: register 2.
- [0,1,2] has three: register 3.
- [0,1,2,3] has four: register 4.

The “trinity” [0,1,2] is part of the project's conceptual vocabulary. The executable rule is state counting; do not implement it as the arithmetic assertion 0+1+2=4.

For each registration record the prior state list, result, rule, zero reference and event identity. Add Zn for the new generation. Z0 remains the persistent nexus. Registering a state also schedules fresh exploration. Current fresh initialization resets an older bootstrap helper's prefilled states to [0]; a clean rebuild should initialize [0] directly.

### Stage C — arithmetic opens signed and fractional branches

Use exact rational numbers, not floating-point tolerances:

- 0+1 gives 1.
- 0−1 gives −1.
- 1+1 gives 2 after 1 is available.
- 1÷2 gives 1/2 after 2 is available.
- Products, differences and quotients extend the network.

Division by zero is blocked and recorded. A proposed replacement of an operand creates a different construction; it does not make the original undefined quotient valid.

Keep separate pathways: reuse permits repeated access to registered/archive operands; consume tracks selected operand occurrences; revisit combines a new discovery with earlier work. Targeted examples were early demonstrations, not the permanent exploration objective. The retained early counts of 7 and 121 routes depend on those versions' rules and identity conventions; they are historical examples rather than universal acceptance counts for a new implementation.

### Stage D — retain discoveries and send them back

Use a persistent task queue and saved cursors. New results schedule further combinations, and newly registered foundation states schedule scans across existing constructions. Save remaining work after each bounded run.

A zero-nexus transformation replaces one numeric zero leaf with an available registered state under a named rule, then evaluates and archives the resulting new construction. Preserve the original record. This is a new expression branch, not an equality asserting that zero and the replacement state are interchangeable.

Position workers must create explicit constructions if they claim execution. Keep historical positional observations separate from executed expression records.

### Stage E — add exact complex arithmetic

Represent a complex number as a pair of rational numbers (real, imaginary). Declare seed records i=(0,1) and −i=(0,−1). Embed registered rational states on the real axis. Link embeddings to their rational origins wherever represented by the data model.

Supply exact +, −, × and ÷ rules, reject a zero complex denominator, and retain parents and operations. Example checks: i+(−i)=0; i×i=−1; (−i)×(−i)=−1; i×(−i)=1. Complex feedback lets earlier results participate in later operations. Do not infer historical derivation of the declared seeds from rational zero.

### Stage F — observe without changing the exploration rules

The genesis journal records new events; the tangent ledger records generated, selected and completed opportunities. Convergence hubs show how different archived parents and expressions reach a common result. Structural echoes and complex conjugate echoes are observations, not newly established mathematical laws.

Discovery indexes query existing records across domains. Observation must not silently discard unexplored branches or promote a pattern into an executable rule. If scheduling changes, preserve deferred work and state the reason.

### Stage G — exact symbolic structures and domain bridges

Use a safe, explicit expression encoding for rationals, the imaginary unit and allowed algebraic operations. Do not evaluate arbitrary text as Python. Preserve construction trees and typed source references even when SymPy simplifies two expressions to the same mathematical value.

Support the current explicit operations: square root and binary +, −, ×, ÷, exponentiation, subject to resource and domain checks. Preserve the difference between a construction and its simplified result. Source-import cursors connect rational and complex constructions to the symbolic archive. A symbolic result that is exactly rational or complex may create a typed numeric embedding; the embedding must retain its source.

### Stage H — zero slots become roles, then variables support calculus

Roles are explicit representation rules. A role can preserve a payload while naming it A or a, introduce free variable x, or select an already registered numeric state. Its position/depth is backed by a registered foundation counter. An abstraction to x is not an assertion that its prior numeric payload equals x.

Keep the role origin, parent, slot backing, rule, body, label and sources. Current supported names are A and a; arbitrary A–Z/word formation remains a proposed extension, not a completed feature.

Calculus uses rational polynomial coefficient lists, in increasing degree order. For example [2,3,1] means 2+3x+x². Variables come from archived variable-role constructions. Explicit operations are differentiate, integrate, multiply by x and limit at zero for polynomials. Integrals store a C=0 representative and acknowledge the full +C family. Polynomial continuity justifies the current zero-limit rule; it must not be applied to arbitrary singular functions.

When a calculus output is constant, a typed bridge exposes it to rational workers. Validate the source construction before accepting that bridge. This last requirement is not fully satisfied by V4.7.11; see the audit backlog below.

### Stage I — preserve enough evidence to attempt repair

Distinguish record ID, mathematical value, construction identity and historical lineage. A missing record must keep its stable slot. Do not shift later IDs or replace it with another record solely because both evaluate to 5.

Store content digests, archive next-ID counters and reconstruction recipes. Current rational recipes contain tree, parents and pathway. Reconstruct only if the named rule, dependencies and computed output support it. Contradictory recipes remain evidence of a conflict.

For serialized damage, use explicit JSON/text grammar, bounded searches, whole-body maps and surviving references. Save search checkpoints. Report unresolved ambiguities and preserve the original bytes. The recovery code is not a universal method for recovering arbitrary erased text.

### Stage J — validate, activate and continue

Keep the damaged source, candidate, report and backup separate. Before activation check compatible format, foundation sequence, archive slots, typed links, indexes, construction mathematics and retained recovery recipes. Save a backup of the previous memory. Only a validated candidate becomes active. Continue and save an actual engine run; a parseable candidate alone does not demonstrate continuation.

V4.7.9 adds a rational verification worker with persisted tasks. A work proposal and a completed repair are different statuses. Retained suggestions must not be reported as executed exploration.

### Stage K — compare exact recovery with a fresh start

Run isolated recovery and regeneration trials. Regeneration begins from the supplied program rules and fresh Z0, without copying the damaged archive's constructions. An intact baseline, when supplied, measures the comparison and record-count goal; it is not a hidden recovery payload.

Save every completed cycle and resume the same trial across launches. The operational goal is a rational-record floor followed by another validated, saved continuation run. This count goal is a capability measure, not evidence that original historical paths were recovered. Select a ready branch under the declared policy; never silently overwrite the original input. If neither is ready, report pending and retain checkpoints.

The current default is up to eight engine cycles per branch per invocation. A budget checkpoint is a bounded stop, not a crash or a declaration of impossible recovery.

## 3. Minimal architecture for a rebuild

Separate these components, even if the first implementation is one Python file:

1. Foundation registration and zero identities.
2. Exact operation kernels and an allowlisted rule registry.
3. Central zero_core dispatch and record passage.
4. Five typed append-only construction archives.
5. Persistent scheduler, task identities, cursors and deferred work.
6. Cross-archive source links and result lookup indexes.
7. Observers, journals, counters and read-only queries.
8. Independent mathematical and structural validation.
9. Evidence-based reconstruction and bounded text recovery.
10. Isolated adaptive trials, branch activation and verified continuation.

The surviving source accumulated wrappers across releases. Rebuild these responsibilities with explicit interfaces; reproducing the wrapper stack is unnecessary if behavior and compatibility are preserved.

### Central flow

```text
request = typed domain + named operation + operands + context
result = zero_core(request)
if mathematically blocked:
    retain attempt and reason
elif resource limited:
    retain resumable task and its retry condition
else:
    form a construction with parents, sources, value and rule
    check identity and retain any alternative derivation
    pass accepted record through zero_core
    append record, update indexes, schedule further work
independently validate the completed checkpoint
save atomically
```

This is a specification, not runnable code. Consistent resource deferral and alternative-derivation retention are required improvements over V4.7.11.

### Archive record contract

Every record needs an archive-local stable ID, expression/representation, exact value, named operation or rule, parent IDs, typed cross-domain sources where needed, pathway, depth and zero passage marker. Seeds and embeddings must declare their special origin rather than pretend to have ordinary binary parents.

Rational records also retain a binary tree, ordered leaves and ancestry. Complex records retain exact real and imaginary parts. Symbolic records retain a safe exact-value encoding and construction. Role records retain kind, label, body, path, slot and rule. Calculus records retain coefficient lists, variable source, operation and any integral/limit qualifications.

A typed reference has the form:

```json
{"archive":"calculus","id":24}
```

A rational construction example is:

```json
{
  "id": 3,
  "domain": "rational",
  "expr": "(0 - 1)",
  "value": "-1",
  "tree": {"op":"-","left":{"leaf":0},"right":{"leaf":1}},
  "parents": [0,1],
  "leaves": [0,1],
  "depth": 1,
  "pathway": "reuse_v1",
  "sources": [],
  "ancestry": [{"left_id":0,"right_id":1,"operation":"-","result":"-1","rule":"reuse_v1"}]
}
```

IDs in this example are illustrative. Real IDs are allocated by archive append order. The central passage adds its own marker; do not hand-copy another record's passage identity.

### Persistent memory contract

Retain schema/runtime compatibility information; foundation; runs; rational expressions and value index; task queue and head; identity keys; complex, symbolic, role and calculus archives; cross-archive integration; rule registry; zero-core coverage; blocked attempts and proposals; genesis/tangent/observer records; recovery manifests and pending slots.

The surviving filename is `zero_theorem_rabbitholes_v41_memory.json`. Its format compatibility version is `'4.1'` even though the runtime is V4.7.11. Do not confuse those numbers or change the format without a migration plan.

Store rationals canonically as strings such as `-1`, `2/3`; keep IDs as integers. Rebuild runtime caches after loading and exclude them from JSON. Use safe decoding, temporary-file write, flush/fsync and atomic replacement. Keep backups and hash original experimental inputs.

Value indexes answer “which records equal this?” They do not define construction identity. Pending tasks may be deduplicated by full task identity. Alternate derivations need retained edges or distinct construction records, even when a shared tree is stored once.

### Scheduling and limits

Preserve queue fairness and completed cursors. Each new state/result opens opportunities. Work budgets bound one run; the saved queue supports later runs. Limits do not establish exhaustive exploration.

V4.7.11 reference settings:

| Setting | Value |
| --- | ---: |
| General work per run | 90 |
| Complex work per run | 24 |
| New expressions per run budget | 400 |
| Emergence events per run | 3 |
| Nexus work per run | 36 |
| Rational/complex maximum depth | 4 |
| Rational/complex integer bit bound | 256 |
| Symbolic work per run | 24 |
| Symbolic import allowance per source archive/run | 24 |
| Symbolic node limit | 48 |
| Symbolic power limit | 8 |
| Symbolic root bit limit | 32 |
| Role work per run / depth | 12 / 4 |
| Calculus work per run / import allowance | 8 / 2 |
| Calculus maximum depth / degree | 4 / 8 |
| Observer proposal allowance per run | 160 |
| Genesis journal event allowance per run | 2,400 |

These are reproducibility settings, not fundamental constants. Record suppressed journal event counts rather than imply a complete history. Increasing a limit must explicitly reactivate affected deferred work in a corrected rebuild.

## 4. What the tests established

### Earlier recovery loop

The phone approved a 132-rational-record candidate, retained the previous memory backup, reexecuted supported damaged rational constructions, resumed the engine and saved. The resulting second run held 296 rational, 126 complex, 88 symbolic, 20 calculus and 24 role records: 554 mathematical archive records in total. The read-only structural audit reported zero issues for that tested archive.

### Task 3: controlled heavy loss

The damaged copy retained 4 of 132 rational records. Exact recovery remained unresolved. Regeneration produced a fresh lineage from Z0, reached 132 records, then 296 with verified continuation. Archive validation passed; damaged source and baseline were preserved.

### Task 4: varied damage

The development matrix covered 15 scenarios, including controls, missing paths, dependent paths, value/parent conflicts, duplicate IDs, recipe conflicts, targeted number removals and a byte-span deletion. Depending on evidence, cases used supported exact recovery or explicit regeneration. Selected archives reached 437 rational records with tested validation and continuation. Forty regression checks passed in that release workflow.

The phone's three-case bundle passed single_path_manifest via recovery, erase_0_evidence via regeneration, and duplicate_id_conflict via regeneration. All three preserved original inputs.

Deleting zero-related archive records did not delete the program's supplied zero seed or arithmetic rules. The zero-erasure demonstration established fresh regeneration under those surviving rules, not recovery of information from literal absence of all information and machinery.

### Ongoing phone trial reported after the audit

Two successive invocations saved runs 1–8 and then 9–16. Regeneration grew from 132 to 2,252 rational records. Recovery remained unresolved; regeneration reported budget_checkpoint; no branch had yet been selected. The specific target_records value was not provided in those logs. Those logs demonstrate saved progress and restart, not completion of that trial.

## 5. Independent acceptance tests for a reconstruction

Implement these before trusting a rebuild:

1. Fresh memory has only registered state 0 and Z0 before scheduled emergence; counting yields 1,2,3,4 with explicit events.
2. `00404` preserves its zeros, produces `00111101111`, and retains positional mapping.
3. Exact rational operations, negative outputs and fractions replay correctly. Division by zero is blocked.
4. Complex seed origin is explicit; the four i/−i examples above pass; zero complex division is blocked.
5. Distinct trees with equal values remain distinct. Identical trees with different legitimate parent histories retain their alternate derivations.
6. Every accepted construction in each domain has a consistent zero passage marker. Coverage totals agree with archive lengths.
7. Every operation is independently replayed against typed parents and sources, rather than checked only by its own stored value or digest.
8. Symbolic safe encoding round-trips, resource checks work, and cross-domain numeric embeddings preserve and validate their sources.
9. Role naming preserves payload, variable abstraction is explicit and slot backing exists. Invalid role/source combinations are rejected.
10. Polynomial differentiation/integration/limit/multiply_x agree with exact coefficient rules, including variable binding and +C qualifications.
11. Valid calculus chain 7 → 7x → 7x² → 14x → 14 is accepted and creates a correctly sourced rational embedding even when 14 is a new rational result.
12. Injecting wrong complex or calculus constructor outputs is rejected even if their indexes and newly computed manifest digests agree.
13. Typed links, seeds, indexes, dependency order and manifest recipes are checked. A structural PASS alone must not stand in for mathematical replay.
14. Deleting one supported rational record restores that exact slot from valid evidence; a conflicting recipe blocks acceptance. Extend this to each domain.
15. Irrecoverable/ambiguous damage remains explicit; equal value never silently substitutes for lost history.
16. Interrupt/restart preserves task cursors, pending evidence and saved archive prefixes. No task is declared complete solely because a resource limit was reached.
17. Adaptive regeneration starts with supplied Z0 rules, preserves original input bytes, reaches its declared operational floor, completes another saved run and activates the selected branch explicitly.
18. Later relevant evidence requeues unresolved recovery within a bounded allowance, without authenticating old history merely from a regenerated equal value.

Treat failed tests as implementation work, not permission to change expected mathematics or conceal unresolved evidence.

## 6. Known unfinished work at the V4.7.11 checkpoint

The audit used disposable copies and did not modify the engine or baseline. Its priorities are:

1. Complete mathematical verification across currently supported domains and fix calculus-to-rational validation. Fault-injected wrong complex/calculus outputs passed _zg_check; the correct new constant 14 bridge failed independent rational verification.
2. Extend typed reconstruction recipes and replay across complex, symbolic, calculus and roles and remaining rational pathways. In the deletion probes, rational record 20 rebuilt; the four tested non-rational records remained pending.
3. Automatically revisit retained recovery when relevant evidence arrives. The selected adaptive branch's normal continuation currently does not service the abandoned recovery trial automatically.
4. Preserve alternate derivations. Current rational identity is keyed by pathway and tree, so a distinct parent history for the same tree can be dropped.
5. Persist and retry resource-deferred work consistently. Some rational/complex limit exits advance worker progress without a durable retry construction.
6. Recheck phone restart, interruption, file-path handling and reporting after these changes.

After those: extend supported operations/representations with explicit rules and provenance; study the planned convergence checkpoints; compare candidate findings with existing mathematics before claiming novelty. Planned pattern checkpoints include 1–11, 100–111, 200–211 and repeated-digit milestones 222 through 1111. Bunny-agent integration and KAELIDOSCOPE remain separate follow-on projects.

The current engine does not implement arbitrary language formation, every known mathematical operation, exhaustive exploration or automatic authentication of erased historical information. Those boundaries must be recorded so a future builder knows what remains to implement.

## 7. Recovery package to preserve independently

If only this blueprint survives, rebuild in the stage order above and use the acceptance tests. If more files survive, the most useful reconstruction package is:

- This blueprint and the current zero-functionality audit.
- A full source release, including its dependencies and runtime version.
- One validated intact memory snapshot, with its SHA-256 and the matching source release.
- Test runner, frozen fixtures, exact change logs and pass/fail evidence.
- For unfinished trials: the damaged source, adaptive report, active pointer if present, and complete adaptive-work directory together.
- License and authorship information. The project's published license choice is GPL v3; preserve the actual license text when available.

Historical repository location: https://github.com/PatchworkWabbit/zero-theorem . Treat it as a recovery location, not a replacement for independent copies. Working files on a single phone or copies inside one synchronized account do not provide independence from that device/account's loss.

Do not label all sidecar JSON files “temporary.” Reports are evidence, pending-search files contain continuation state, and adaptive-work holds regenerated archives. Separate completed historical experiments from the active trial before cleanup. Relocating an active trial requires updating or preserving its path relationships.

## 8. Final design instruction to the next builder

Preserve the seed, the rules, the constructions and the unfinished paths. Start from 0, register what follows, keep signed and imaginary branches explicit, and let discoveries open further exploration through the common core. Keep observation, mathematical validation, reconstruction and fresh regeneration distinguishable in both code and reports.

If something is unknown, retain the question and the evidence. If a new branch starts, retain its new identity. Reconstruct what the evidence supports, and keep exploring what remains open.
