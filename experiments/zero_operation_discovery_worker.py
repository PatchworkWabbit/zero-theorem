"""Zero Theorem operation-discovery worker (experimental, read-only input).

Reads an existing V4.7.17 JSON archive; writes ONLY a separate candidate sidecar.
Does not import/run the engine, modify archives, or trust candidate operations.
Run: python zero_operation_discovery_worker.py PATH_TO_MEMORY.json
"""
import json
import os
import sys
from collections import defaultdict
from fractions import Fraction

RULE = "zero_operation_discovery_v1"
MAX_SCAN = 30000
MAX_CANDIDATES = 2000


def fingerprint(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def flatten_add(tree):
    if not isinstance(tree, dict):
        return None
    if tree.get("op") == "+" and "left" in tree and "right" in tree:
        a, b = flatten_add(tree["left"]), flatten_add(tree["right"])
        return None if a is None or b is None else a + b
    if "leaf" in tree:
        return [tree]
    return [tree]  # Treat a non-add subtree as an indivisible repeated term.


def candidate_for(record):
    tree = record.get("tree")
    if not isinstance(tree, dict) or tree.get("op") != "+":
        return None
    terms = flatten_add(tree)
    if not terms or len(terms) < 2:
        return None
    key = fingerprint(terms[0])
    if any(fingerprint(term) != key for term in terms[1:]):
        return None
    try:
        observed = Fraction(str(record["value"]))
    except (ValueError, TypeError, KeyError, ZeroDivisionError):
        return None
    return {"operation": "repeat", "term": terms[0],
            "count": len(terms), "observed_value": str(observed),
            "source_ids": [record["id"]], "status": "untrusted",
            "rule": RULE, "nexus": "Z0",
            "verification": "pattern_observation_only"}


def discover(memory):
    if not isinstance(memory, dict) or not isinstance(memory.get("expressions"), list):
        raise ValueError("Expected Zero Theorem memory with expressions list")
    records = memory["expressions"]
    findings = []
    seen = set()
    for rec in records[:MAX_SCAN]:
        if not isinstance(rec, dict) or not isinstance(rec.get("id"), int):
            continue
        proposal = candidate_for(rec)
        if proposal is None:
            continue
        key = (fingerprint(proposal["term"]), proposal["count"], tuple(proposal["source_ids"]))
        if key in seen:
            continue
        seen.add(key)
        findings.append(proposal)
        if len(findings) >= MAX_CANDIDATES:
            break
    by_shape = defaultdict(list)
    for idx, proposal in enumerate(findings):
        by_shape[(fingerprint(proposal["term"]), proposal["count"])].append(idx)
    relationships = [
        {"candidate_indices": ids, "kind": "shared_repetition_structure",
         "nexus": "Z0", "status": "untrusted"}
        for ids in by_shape.values() if len(ids) > 1
    ]
    return {"schema": 1, "rule": RULE, "nexus": "Z0",
            "source_records_scanned": min(len(records), MAX_SCAN),
            "source_records_total": len(records),
            "scan_complete": len(records) <= MAX_SCAN,
            "candidate_limit_reached": len(findings) >= MAX_CANDIDATES,
            "candidates": findings, "relationships": relationships,
            "trusted_rules_added": 0, "source_unchanged": True,
            "note": "Read-only candidate extraction; not independent operation invention or proof."}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python zero_operation_discovery_worker.py MEMORY.json")
    source = os.path.abspath(sys.argv[1])
    destination = source + ".operation-discovery-candidates.json"
    if os.path.exists(destination):
        raise SystemExit("Candidate sidecar already exists; refusing to overwrite: " + destination)
    with open(source, "r", encoding="utf-8") as handle:
        memory = json.load(handle)
    report = discover(memory)
    with open(destination, "x", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
    print("Z0 operation discovery | scanned:", report["source_records_scanned"],
          "| candidates:", len(report["candidates"]),
          "| relationships:", len(report["relationships"]))
    print("Source unchanged. Candidate sidecar:", destination)


if __name__ == "__main__":
    main()
