# Zero Theorem — Reconstruction and provenance ledger (V4.9.2)

**Created:** 2026-10-21. **Purpose:** preserve independently inspectable source identity, design transitions, and a roadmap for faithful future reconstruction. This is not a verbatim restoration of inaccessible chat messages.

## Immutable source identities verified by GitHub fetch

Branch: `experimental/energy-through-z0-v4-9`

| Version | Path | Git blob SHA | Lines |
|---|---|---|---:|
| V4.9 | `zero_theoremV4.9_energy_experimental.py` | `e7d2b1b9108042fd5e568bff07f88d180f62b175` | 7929 |
| V4.9.1 | `zero_theoremV4.9.1_crosscore_energy.py` | `316f6be1b50f76d2a8c1c1ac67ce99e6a87dbeff` | 8126 |
| V4.9.2 | `zero_theoremV4.9.2_emergent_foundations.py` | `821533b20448df7f35a953f82b0f28cbab167258` | 8283 |

These are Git blob identifiers, not SHA-256 file digests. The files were read without modifying them.

## Reconstruction map from source inspection

- **Inherited engine through V4.7.17:** central `zero_core` operation and record passage; rational, complex, symbolic, calculus, and role archives; exact arithmetic, typed construction provenance, saved continuation and recovery safeguards. Inherited code is present in the V4.9 series; individual historical design motivations require separate records.
- **V4.9:** new section begins near line 7781. `_ZE_RULE = 'energy_through_zero_v1'`; `_ZE_BRANCHES = ('+1', '-1', '+i', '-i')`; `_ZE_BATCH = 32` (per-run processing budget); `_ZE_ENERGY_SEED = '1'` (dimensionless exploratory token, explicitly not joules).
- **V4.9.1:** new section begins near line 7888. Cross-core energy coverage includes `('rational', 'complex', 'symbolic', 'calculus', 'roles')` and read-only physics references. Reference comparisons do not establish physical identity.
- **V4.9.2:** new section begins near line 8084. `_ZF_RULE = 'emergent_foundations_observer_v1'`; `_ZF_BATCH = 256`; the observer is described in source as read-only mathematical observation, not invention of physics. Its integrity output explicitly says structural checks do not verify physical quantities.

## Reported run evidence — provenance pending

Previously reported Android values: 1,356 energy pathways; 256 foundation observations; 1,100 pending; 57 rational outputs; 65 complex outputs; 41 symbolic outputs; Z0 coverage complete; integrity checks clean. These figures must be matched to original console output and sidecar files before treating them as independently reproduced.

## What must be preserved for future reconstruction

1. Original source blobs and their Git commit history, without rewriting history.
2. Exact command lines, Python and SymPy versions, phone environment, configuration, archive snapshots and input-file hashes.
3. Energy and foundation observer JSON sidecars, including provenance links and any pending work.
4. Raw console logs and error reports; label missing logs as missing, not passed.
5. The original reasoning/design conversation where accessible; distinguish direct quotes from retrospective reconstruction.
6. A version-by-version functional diff, showing added entry points, hooks, schemas, rule names and side effects; do not rely on filenames alone.

## Claims and uncertainty

**Verified:** source file existence, byte-identity Git blob SHA, code-section anchors, and explicit rule constants.

**Reported, not reproduced in this record:** Android numerical results.

**Not established:** a cause for any missing chat content; copying or theft by a company or individual; novel physical laws; exhaustive mathematical proofs.

## Safe continuation rule

Never overwrite the three V4.9 source files or their original archives. Continue on a new branch or a separate file; preserve old outputs. Every future code change should link the previous version, specify why it changed, include reproducible commands, and record the evidence obtained.
