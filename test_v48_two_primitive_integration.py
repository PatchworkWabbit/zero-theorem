"""Regression checks for integrated V4.8 Z0 two-primitive candidate."""
import importlib.util
from fractions import Fraction

spec = importlib.util.spec_from_file_location("zero_engine", "zero_theoremV4.8_integrated_experimental.py")
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)

cases = [
    (Fraction(3), '+', Fraction(4), Fraction(7)),
    (Fraction(3), '-', Fraction(4), Fraction(-1)),
    (Fraction(3), '*', Fraction(4), Fraction(12)),
    (Fraction(12), '/', Fraction(4), Fraction(3)),
    (Fraction(1,2), '+', Fraction(1,3), Fraction(5,6)),
    (Fraction(-2,3), '*', Fraction(3,4), Fraction(-1,2)),
    (Fraction(1), '/', Fraction(0), None),
]
for a, op, b, expected in cases:
    actual = engine._operate_rational_exact(a, op, b)
    assert actual == expected, (a, op, b, actual, expected)
assert engine._Z0_PRIMITIVE_EVIDENCE, "No primitive construction evidence recorded"
for entry in engine._Z0_PRIMITIVE_EVIDENCE:
    assert entry['root'] == 'Z0'
    assert set(entry['steps']) <= {'S','P'}
print("Integrated Z0 rational primitive regression checks passed.")
