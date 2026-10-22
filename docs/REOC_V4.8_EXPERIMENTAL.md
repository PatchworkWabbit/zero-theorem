# V4.8 Experimental — Reduced Emergent Operations Core (REOC)

**Status:** Experimental development / user-reported Android Pydroid3 run, 20 October 2026. Not a mathematical proof or independently reproduced benchmark.

## Purpose

REOC extends the Zero Theorem's Z0-centered construction archive with **operation-candidate discovery**. A bounded scanner examines preserved arithmetic expression trees for repeated-addition patterns, records source constructions and candidate relationships, and saves the candidates to a separate JSON sidecar. Candidate operations remain **untrusted**; this version does not autonomously approve or execute them as new trusted operations.

The integration is built on V4.7.17's existing adaptive regeneration, exact temporal recovery, archival provenance, zero-core coverage and integrity machinery. The runtime may still display the original V4.7.17 banner.

## Android run evidence (user-provided terminal transcript)

- Adaptive regeneration checkpointed 31 cycles, growing the rational archive from **132** to **4,701** records; regeneration was **selected_and_resumed**.
- A subsequent normal continuation completed **run 32**, reaching **4,864 rational constructions**.
- Integrated operation discovery reported **4,864 scanned records**, **15 candidates**, and **4 relationships**; the untrusted candidate sidecar was saved separately.
- Accepted archive records across rational, complex, symbolic, calculus and role domains: **9,914**.
- Read-only integrity audit: **22,143 typed dependency links**, **61,566 pending tasks**, **0 structural issues**.
- Zero-core passage coverage: **complete** for the five archived construction domains, with **no missing passages**.
- Provenance audit: **9,373** records with a path from zero; **9,914** reachable when declared seeds are included.
- Zero temporal query: **9,913 events**, **0 gaps**. Zero-clock query: current state **10009**, **10010 registered states**.
- A symbolic query for `sqrt(2)` returned **20 distinct preserved construction records**, demonstrating representation/path retention rather than unique-form counts.

The transcript also reports **15,044 runtime kernel calls**, of which **14,713 computed**, **324 blocked**, and **7 resource-limited**. These are runtime counters, not mathematical proof.

## Architectural boundaries

1. All accepted archive records retain the implemented `everything_through_zero_v1` passage bookkeeping.
2. Distinct expression trees and provenance paths are not collapsed solely because values match.
3. Candidate operations are separate from approved/executable rules.
4. Regeneration creates a **new lineage from Z0**; it does not claim exact restoration of lost historical provenance.
5. Adaptive checkpoints and sidecar reports are distinct from the original source memory. No private user memory is included in this document.

## Current limitations / next work

- Candidate discovery currently identifies a narrow repeated-addition family, not arbitrary mathematical operations.
- The integrated discovery hook runs after a memory save; it does not yet make new candidate rules executable.
- No generality, mathematical novelty, consciousness, or formal proof claim follows from these logs.
- Preserve V4.7.17 and existing release artifacts while reviewing and packaging the experimental engine separately.
- Next implementation milestone: a constrained candidate-to-executable proposal path with independent arithmetic verification, provenance, explicit approval status, and rollback protections.

## Running the experiment

The experimental script uses `zero_theorem_v48_experimental_memory.json` alongside the script in a writable Pydroid3 folder. Its adaptive recovery may create an active branch under a `.adaptive-work/` directory. Preserve both original V4.7.17 code and its original memory; do not rename or overwrite the source memory.

**Evidence provenance:** Values transcribed from the user's Android console output. A full code release and reproducible fixture should be added separately after repository packaging and review.
