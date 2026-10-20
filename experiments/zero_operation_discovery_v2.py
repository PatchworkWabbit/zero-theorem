"""Experiment 002: mathematical core dive — append-only Z0 evidence.

Standalone Python 3 standard library. Does not open or change engine archives.
The pattern recognizer is explicitly supplied; this tests candidate bookkeeping,
not autonomous invention or proof of multiplication.
"""
from fractions import Fraction
import json

RULE = "zero_operation_discovery_v1"


def leaf(n):
    return {"op": "leaf", "value": str(Fraction(n))}


def plus(a, b):
    return {"op": "add", "args": [a, b]}


def add_value(tree):
    if tree["op"] == "leaf":
        return Fraction(tree["value"])
    if tree["op"] == "add":
        return sum((add_value(t) for t in tree["args"]), Fraction(0))
    raise ValueError("Untrusted operation cannot execute")


def repeated_terms(tree):
    if tree["op"] == "add":
        return repeated_terms(tree["args"][0]) + repeated_terms(tree["args"][1])
    return [tree]


def build(term, count, right=False):
    if count < 2:
        raise ValueError("count >= 2 required")
    result = term
    for _ in range(count - 1):
        result = plus(term, result) if right else plus(result, term)
    return result


class Z0:
    def __init__(self):
        self.records = []
        self.events = []

    def passage(self, kind, record_id):
        self.events.append({"seq": len(self.events), "nexus": "Z0",
                            "kind": kind, "record_id": record_id})

    def record(self, data):
        entry = {"id": len(self.records), **data}
        self.records.append(entry)
        self.passage(entry["kind"], entry["id"])
        return entry

    def construction(self, tree):
        return self.record({"kind": "construction", "tree": tree,
                            "value": str(add_value(tree)),
                            "status": "verified_by_add_only"})

    def candidate(self, source_id):
        src = self.records[source_id]
        if src["kind"] != "construction":
            raise ValueError("Candidate evidence must be trusted construction")
        terms = repeated_terms(src["tree"])
        if len(terms) < 2 or any(t != terms[0] for t in terms[1:]):
            return None
        signature = json.dumps(terms[0], sort_keys=True)
        return self.record({"kind": "candidate", "operation": "repeat",
                            "signature": signature, "term": terms[0],
                            "count": len(terms), "observed_value": src["value"],
                            "source_ids": [source_id], "status": "untrusted",
                            "rule": RULE})

    def relationship(self, candidate_ids):
        candidates = [self.records[i] for i in candidate_ids]
        if len(candidates) < 2 or any(c["kind"] != "candidate" for c in candidates):
            raise ValueError("Need at least two candidate observations")
        return self.record({"kind": "candidate_relationship",
                            "candidate_ids": list(candidate_ids),
                            "source_ids": [i for c in candidates for i in c["source_ids"]],
                            "proposal": "repeat_structure_generalization",
                            "status": "untrusted",
                            "reason": "examples_do_not_prove_universal_rule",
                            "rule": RULE})


def test():
    z = Z0()
    a = z.construction(build(leaf(1), 3))
    b = z.construction(build(leaf(1), 3, right=True))
    c = z.construction(build(leaf(2), 3))
    d = z.construction(build(leaf(3), 4))
    e = z.construction(plus(leaf(1), leaf(2)))  # Not a repeated term
    ca, cb, cc, cd = (z.candidate(x["id"]) for x in (a, b, c, d))
    assert z.candidate(e["id"]) is None
    assert len({json.dumps(x["tree"], sort_keys=True) for x in (a, b, c, d)}) == 4
    assert a["value"] == b["value"] == "3"
    assert c["value"] == "6" and d["value"] == "12"
    assert ca["source_ids"] != cb["source_ids"]
    rel = z.relationship([ca["id"], cb["id"], cc["id"], cd["id"]])
    assert rel["status"] == "untrusted"
    assert len(z.records) == 10  # 5 constructions + 4 candidates + 1 relationship
    assert all(x["nexus"] == "Z0" for x in z.events)
    assert all(x["status"] == "untrusted" for x in z.records if x["kind"] != "construction")
    print(json.dumps({"records": len(z.records), "z0_events": len(z.events),
                      "constructions": 5, "candidates": 4,
                      "candidate_relationships": 1, "preserved_paths": True,
                      "general_rule_proven": False}, indent=2))
    print("Experiment 002: checks passed (not a mathematical proof)")


if __name__ == "__main__":
    test()
