# V4.7.16 — Independent zero time clock and process observations

This addition supplies an independent zero time clock and separately measures process activity with three device clocks and persistent event order. It includes V4.7.15 recovery feedback and the V4.7.14 valid-archive size fix.

## Independent zero time clock

The clock has its own origin **T0 = 0**, its own registered states and its own `.zero-clock.json` file. Its transformation rule counts registered clock states: the registered state 0 yields the next state 1, then states 0 and 1 yield state 2, and so on. Contiguous ranges are stored compactly rather than expanding an unnecessary list of every clock state.

Newly observed foundation states and accepted construction IDs register additional clock states. Expansion coordinates retain the contribution of each mathematical domain. The rule counts accepted constructions, including representations, rather than unique values or unique formulas. Rejected operations, pending slots and elapsed waiting alone do not advance this clock. Re-observing an already seen ID does not count it again. Deletion does not reverse the clock; re-observing that same ID after reconstruction does not double count the earlier expansion.

This is a separate zero clock. The role system was an analogy for a zero transformation, not its implementation dependency. The clock calls neither the role grammar nor the device clock sampler to generate states. `ZERO_CLOCK_ENABLED` controls it independently of `TIME_OBSERVER_ENABLED`.

A verified load establishes the first observation boundary at zero, with existing accepted space recorded as its baseline. Successful saves supply committed growth observations. Loading later can also reveal growth committed before an interrupted observation. Growth is recorded as an observed batch, with no fabricated scheduler interleaving or prior elapsed times. A fresh engine begins from its zero seed; installing the feature into an existing project establishes a fresh zero reference at that existing space. Clock units are logical registered states; elapsed seconds remain separate observations.

The clock enters through `zero_core`'s `time` domain with the `space` operation, referencing mathematical Z0 as its source while retaining its own T0 reference. Its state never feeds back into task selection or mathematical rules. Clock-observation failure preserves the mathematical work outcome and existing invalid clock file.

## Measurements

Every observed phase starts with elapsed time zero. Its start and finish record:

| Field | Meaning |
| --- | --- |
| UTC / wall nanoseconds | Device clock reading; UTC gives an unambiguous calendar timestamp |
| Elapsed nanoseconds | Difference between monotonic readings within the same observer session |
| CPU nanoseconds | Process CPU consumed during the phase |
| Sequence / previous event | Persistent order within that observation ledger, even when clock readings tie |
| Span / parent span | Phase identity and nesting; parents may reference another observation file |
| Outcome | Completed, error or interrupted |

Clock readings are sampled sequentially. Nanosecond storage does not promise nanosecond physical precision. Wall-clock corrections can yield negative wall durations while monotonic elapsed time remains positive. The recorded difference is diagnostic data, not proof of what caused a clock discrepancy. All clock sources belong to the device; no independent external clock is authenticated.

Across restarts a new session begins at elapsed zero. A session-boundary event links to the earlier session and records the wall-clock gap. Old monotonic and CPU counters are never subtracted from new ones. If an earlier span had no recorded finish, its duration remains unknown and it is marked unfinished after restart. No earlier run's timings are invented or backfilled.

Inclusive durations for nested phases overlap. Per-stage totals accumulate only observed intervals, including observed error/interruption intervals. They exclude unobserved gaps. The top-level `process_including_queries` span includes user interaction time at the query prompt; its CPU duration distinguishes process CPU use from elapsed waiting.

## Integration and storage

The new `time` domain enters through `zero_core`. Automatic spans cover loading, foundation emergence, the queue exploration phase, role exploration, calculus exploration, verification/saving, adaptive cycles, recovery slices, recovery retries, candidate verification and the top-level process.

Observations are stored separately at `<observed-path>.time-observer.json`. During adaptive work there can be separate ledgers beside the original source, the selected branch memory, the recovery snapshot and verification inputs. Parent-span references connect nested phases across files. Sequence order is local to each ledger, not an assertion of global chronological order across devices or files.

Atomic checkpoints preserve starts, finishes, open spans and accumulated totals. Observation-file failures are reported and do not block mathematical work or overwrite an invalid observer file. Original mathematical records, source snapshots, arithmetic rules and queue budgets are not changed by the observer. Recording timings adds some I/O overhead; existing wall-time-based recovery budgets can still be affected by execution cost. `TIME_OBSERVER_ENABLED = False` disables automatic device-clock observations; the independent zero clock retains its own enable switch.

This is coarse process observation, not an unbounded timestamp journal for every arithmetic operation. Observation ledgers retain their events and grow with observed phases; no event-retention guarantee is made for runs before this feature was installed. The observer shares the engine's single-active-process usage model.

## Validation

The device-clock focused suite covers 13 behaviours: zero-relative starts and exact recorded deltas; clock corrections; restart boundaries and unknown durations; tied-clock logical ordering; interruption; nested parents; observer write failure; invalid-ledger preservation; disabling observation; rejecting cross-session timer tokens; observed/unobserved mathematical equivalence; real adaptive continuation with prefix preservation; and read-only timing queries.

The equivalence check compares every mathematical record payload across all five archives, the pending queue and cursor, foundation metadata and operation counters between a timed and untimed normal run. They are identical. These generated test runs do not contain user memory.

Nine additional zero-clock checks cover its independent origin and state transformations, growth coordinates, no ticks from elapsed waiting, no double counting after repeated observations or reconstruction, persistence across sessions, exclusion of pending slots, failed-save preservation, actual committed growth and independence from wall timers and the role grammar.

The inherited 108-check suite is also executed against the new engine. The combined full suite passed **131 / 131 checks** on the development host. The full runner extracts the prior Task 7 bundle to a temporary folder and substitutes V4.7.16 bytes under its previous import filename so the original assertions and public fixtures are retained. The complete result is saved in `time_observer_full_results.json`.

The user confirmed the original ten selected checks on Android and normal engine continuation. A follow-up regression checks the actual interactive routing for all four clock commands before complex-number parsing; the updated phone runner contains eleven checks. Android confirmation of this routing fix is pending.

## Phone use

1. Extract **zero_theorem_time_observer_tests.zip** into a separate **Time tests** folder.
2. Open **run_time_observer_tests.py** there in Pydroid3 and press Run. If Pydroid supplies its internal launcher location, the runner asks for the full extraction folder path; paste the folder containing the runner, test file and engine. Expect **TIME OBSERVER: 11 / 11 checks passed**. It uses disposable files and opens no live project memory.
3. Copy the top-level **zero_theoremV4.7.16.py** into `/storage/emulated/0/Documents/Lucky/Maths/`, beside the original memory JSON and the complete `.adaptive-work` folder.
4. Open that script and press Run. The independent zero clock, device-time observation and prior Task 7 recovery retry behaviour are automatic.
5. At the normal archived-value query prompt, type **zero-clock** for the independent zero clock, or **time** for elapsed/UTC/CPU observations. Their separate files are saved beside the active memory.

For read-only reports outside the engine:

```sh
python zero_theoremV4.7.16.py --zero-clock "PATH-TO-MEMORY.json"
python zero_theoremV4.7.16.py --time-report "PATH-TO-MEMORY.json"
```

For the complete disposable regression suite in the extracted bundle:

```sh
python run_time_observer_tests.py --full
```
