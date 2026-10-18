# V4.7.15 — Task 7: recovery feedback after regeneration

An adaptive run previously retained its unresolved recovery trial after choosing regeneration, but normal continuation never serviced that trial. Task 7 connects those saved checkpoints to normal runs of the regenerated branch.

## Behaviour

Before the next normal exploration run, one recovery slice is considered through the Z0 recovery-feedback gateway. It executes when the service is first installed, executable code changes, relevant recovery checkpoints change, new matching construction evidence becomes available, a verified candidate changes, or unfinished/interrupted work remains. Unchanged exhausted work waits without adding repeated attempts.

A construction from the active regenerated archive qualifies to suggest a missing recipe only if its complete retained payload digest and archive ID match the old manifest. The payload includes construction and provenance metadata; passage bookkeeping and unified lookup keys are excluded as in the existing manifest format. An equal number or a different construction is insufficient. Surviving conflicting recipes are never overwritten. Suggested recipes enter an isolated working input and must pass existing deterministic reconstruction, retained digest comparison, independent domain checking, foundation checks and archive-link validation.

The original source, immutable snapshot, active pointer and active regenerated memory are read-only during the recovery slice. Their hashes are checked afterward. Successful recovery creates a separate verified candidate and reports `candidate_ready`; it does not switch the active branch, rewrite the original source, or claim authenticated historical chronology. Normal regenerated exploration then proceeds and saves as before.

## Work and persistence

Default allowances are eight proposed recipes and eight verifier task executions per normal invocation, with one feedback batch. The two-second time allowance is cooperative: parsing, archive preflight, one verifier batch and final validation are indivisible and can take longer. This is not a hard real-time CPU or memory limit.

Existing verification work resumes at its saved cursor without resetting completed tasks. Retry attempts retain trigger names, work allowance, active saved-run number, recipe evidence, outcome, reason, elapsed time and preservation flags. An interrupted slice retains its checkpoint and is retried. The service and evidence matching do not broaden the currently supported reconstruction operations.

Files created alongside the original adaptive workspace:

- `<source>.adaptive-work/<source-hash>/recovery-retry-state.json`: persistent attempt ledger.
- `<source>.recovery-retry-report.json`: readable copy of the ledger.
- `<source>.adaptive-report.json` and the existing `state.json`: updated recovery status and retry summary.
- The isolated recovery folder retains recipe proposals, verification checkpoints and any validated candidate.

## Validation

All **108 distinct checks** passed on the development host:

- 16 Task 7 checks: exact-digest recipe proposals and independent replay; rejection of equal-valued or replay-inconsistent constructions; later evidence reopening recovery; unchanged-work suppression; changed-rule triggers; conflicting recipe retention; bounded cursor continuation; interruption and restart; repeated slices reaching a verified candidate; normal exploration continuing; candidate retention and tamper rechecking; snapshot binding; disabling retries; and proposal budgeting.
- Four V4.7.14 loader regression checks retargeted to V4.7.15: valid oversized archive loading, duplicate-key rejection, malformed-text preservation and arithmetic contradiction rejection.
- The previous 88-check recovery/domain/adaptive regression suite executed against V4.7.15, including all 258 individual typed-deletion probes inside its exhaustive recovery test. It passed in 149.148 seconds on the host.

The ten selected phone-runner checks also passed on the host. A clean extraction of the published ZIP is checked before delivery. Android execution of Task 7 remains unconfirmed. No live user memory was opened by these tests; fixtures are disposable copies of a previously generated public test baseline. These tests do not promise recovery of every damaged record in the user's preserved source.

## Phone instructions

1. Extract **zero_theorem_task7_tests.zip** into its own **Task7 tests** folder. Keep all extracted contents together.
2. In Pydroid3, open **run_task7_tests.py** in that folder and press Run. Expect **TASK 7: 10 / 10 checks passed**. Results are written to `task7_phone_results.json` in that test folder.
3. To use the feature on the existing project, copy **zero_theoremV4.7.15.py** into `/storage/emulated/0/Documents/Lucky/Maths/`, beside the original memory JSON and its full `.adaptive-work` folder.
4. Open that script and press Run. Recovery feedback is automatic when following the existing regenerated branch. Keep using this same script/folder for subsequent runs.

Do not copy the generated trial memory over the original damaged source. Its existing active-pointer mechanism already selects the working branch.

For the full disposable regression suite after extracting the ZIP:

```sh
python run_task7_tests.py --full
```

Known limits remain: unsupported historical pathways, lost evidence without a matching retained digest, ambiguity, contradictions and unimplemented reconstruction rules remain pending. The retained digests are supplied evidence rather than external historical authentication. A new matching value alone does not restore an old identity. Task 7 does not add alternate-parent retention, general contradiction repair in non-rational domains or new mathematics.
