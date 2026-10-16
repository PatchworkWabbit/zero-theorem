# V4.6.4 validation

Validated in isolated temporary directories with Python 3 and SymPy 1.14.0. The user's phone memory was not available for inspection.

## Results

- Regression suite: **25 tests passed**.
- Command: `python3 -m unittest discover -s zero-theorem -p 'test_*.py' -v`.
- Actual V4.6.3 baseline: three normal runs and three continued runs with a deliberately low expression cap; link audits reported zero issues and pauses were retained.
- Initial V4.6.4 execution: three continued runs; link audit reported zero issues. Archive totals matched all 793 stored records. Runtime counters contained rational, complex and symbolic calls.
- Interactive command smoke check: three unified value queries, operation totals and the link audit completed with exit status 0.
- Standalone `--integrity` command: exit status 0, zero reported structural issues, saved memory bytes unchanged.

## What the regression suite exercises

The integration tests establish that equal-valued rational constructions keep separate symbolic source IDs and different zero-slot trees. Complex imports preserve operand order and their complete recorded construction.

Queries for an already-known numeric result include new symbolic routes. An unexpanded symbolic Gaussian power is grouped with its exact numeric result.

Numeric embeddings link to their symbolic origins without producing endless import wrappers. Repeated import passes settle for a finite unchanged source snapshot.

Kernel totals distinguish computed, blocked and limited outcomes across domains and include zero-nexus contexts. Accepted archive totals remain consistent when journal details are suppressed and are not duplicated by repeated synchronization.

An upgrade starts with actual V4.6.3 memory. Existing IDs, expressions, values, parents, pathways and existing symbolic construction trees are retained. All source records in the exercised snapshot receive source links after the import backlog is processed. Saving and reloading preserves counts and links.

Continued runs with a deliberately low expression cap save paused work and retain valid archive/index references. Source records outside a configured depth limit remain explicitly listed and can be reconsidered after that limit changes.

The structural checker detects a deliberately substituted equal-value source link and leaves the inspected memory unchanged.

The earlier mathematical regression checks also run against V4.6.4, including exact roots/powers, generated-result feedback, complex division blocks, resource limits, persistence and read-only queries.

## Limits of these results

These are implementation and integration checks, not a proof of the research hypothesis or exhaustive mathematical exploration. They do not establish performance on an Android phone, validate the user's actual JSON, recover suppressed historical journal details or decide all algebraic equivalences.

Imports and exploration remain bounded per run. A growing archive can have a persistent import/work backlog. Runtime operation history begins at the explicit tracking boundary; earlier failed or discarded attempts are not reconstructed.
