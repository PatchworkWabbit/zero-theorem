"""Experiment 001: append-only operation candidates through Z0.

Standalone, disposable proof-of-architecture. No imports of the live engine,
no live-memory access, no mutation of V4.7.17 or its JSON archives.
Candidate 'repeat' is a *proposed* abstraction, not trusted multiplication.
"""
from fractions import Fraction
import json

RULE = "zero_operation_discovery_v1"


def leaf(value):
    return {"op": "leaf", "value": str(Fraction(value))}


def add(left, right):
    return {"op": "add", "args": [left, right]}


def evaluate_add_only(tree):
    if tree["op"] == "leaf":
        return Fraction(tree["value"])
    if tree["op"] == "add":
        a, b = tree["args"]
        return evaluate_add_only(a) + evaluate_add_only(b)
    raise ValueError("Untrusted operation is not executable in the trusted evaluator")


def flatten_add(tree):
    if tree["op"] == "add":
        left, right = tree["args"]
        return flatten_add(left) + flatten_add(right)
    return [tree]


class ZeroDiscovery:
    def __init__(self):
        self.records = []
        self.events = []

    def zero_core(self, event, **details):
        entry = {"sequence": len(self.events), "nexus": "Z0",
                 "event": event, **details}
        self.events.append(entry)
        return entry

    def archive_construction(self, tree):
        value = evaluate_add_only(tree)
        record = {"id": len(self.records), "kind": "construction",
                  "tree": tree, "value": str(value),
                  "status": "verified_by_addition"}
        self.zero_core("construction_accepted", record_id=record["id"])
        self.records.append(record)
        return record

    def discover(self, source_id):
        source = self.records[source_id]
        if source["kind"] != "construction":
            raise ValueError("Discovery requires an existing construction")
        leaves = flatten_add(source["tree"])
        if len(leaves) < 2 or any(x != leaves[0] for x in leaves[1:]):
            return None
        # The proposed rule is inferred from a repeated *structure*.
        # It is not executed, nor inserted into the trusted operation registry.
        candidate = {"id": len(self.records), "kind": "operation_candidate",
                     "operation": "repeat", "arguments": {
                         "term": leaves[0], "count": len(leaves)},
                     "observed_value": source["value"],
                     "source_ids": [source_id],
                     "rule": RULE, "status": "untrusted",
                     "verification": "single_observation_not_general_proof"}
        self.zero_core("operation_candidate_discovered",
                       source_id=source_id, candidate_id=candidate["id"])
        self.records.append(candidate)
        return candidate

    def inspect(self):
        return {"events": self.events, "records": self.records}


def demo():
    z = ZeroDiscovery()
    one = leaf(1)
    left_associated = z.archive_construction(add(add(one, one), one))
    right_associated = z.archive_construction(add(one, add(one, one)))
    candidate = z.discover(left_associated["id"])
    assert candidate["status"] == "untrusted"
    assert candidate["source_ids"] == [left_associated["id"]]
    assert len(z.records) == 3
    assert z.records[0]["tree"] != z.records[1]["tree"]
    assert all(e["nexus"] == "Z0" for e in z.events)
    assert evaluate_add_only(z.records[0]["tree"]) == Fraction(3)
    try:
        evaluate_add_only({"op": "repeat", "args": [one, leaf(3)]})
    except ValueError:
        pass
    else:
        raise AssertionError("Untrusted candidate leaked into trusted evaluator")
    print(json.dumps(z.inspect(), indent=2))
    print("Experiment 001: checks passed (not a mathematical proof)")


if __name__ == "__main__":
    demo()
