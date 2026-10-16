"""Exact algebraic feedback, archive bridges and safe persistence."""
import contextlib
import copy
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest import mock
from fractions import Fraction

import sympy as sp


SOURCE = Path(__file__).with_name('zero_theoremV4.6.py')
spec = importlib.util.spec_from_file_location('symbolic_engine', SOURCE)
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)


def memory():
    m = engine.empty_memory()
    engine.upgrade_runtime(m)
    engine.upgrade_v44(m)
    engine.upgrade_v45(m)
    engine.upgrade_complex_feedback(m)
    engine.upgrade_symbolic(m)
    engine.rebalance_queue(m)
    return m


def seed(m, value):
    return engine.symbolic_record(m, sp.sympify(value), str(value), [],
                                  'test_seed', 'test')


class SymbolicMathTests(unittest.TestCase):
    def test_exact_root_is_fed_back_with_provenance(self):
        m = memory()
        two = seed(m, 2)
        stats = {'new': 0}
        engine.work_symbolic(m, {'kind': 'symbolic_root', 'source': two}, stats)
        sa = m['symbolic_archive']
        root_id = sa['results']['sqrt(2)'][0]
        root = sa['expressions'][root_id]
        self.assertFalse(engine.symbolic_value(m, root_id).has(sp.Float))
        self.assertIn({'kind': 'symbolic_pair', 'source': root_id,
                       'cursor': 0, 'step': 0}, m['queue'])
        engine.work_symbolic(m, {'kind': 'symbolic_pair', 'source': root_id,
                                'cursor': 0, 'step': 0}, stats)
        rec = sa['expressions'][-1]
        self.assertEqual(rec['value'], '2')
        self.assertEqual(rec['parents'], [root_id, root_id])
        self.assertEqual(rec['depth'], 2)
        self.assertEqual(root['exact'], {'fn': 'pow', 'args': [
            {'q': ['2', '1']}, {'q': ['1', '2']}]})

    def test_exact_powers_and_principal_complex_roots(self):
        for a, op, b, expected in (
                (sp.Integer(2), '**', sp.Integer(3), sp.Integer(8)),
                (sp.Integer(2), '**', sp.Rational(1, 2), sp.sqrt(2)),
                (sp.Integer(2), '**', sp.Integer(-3), sp.Rational(1, 8)),
                (sp.Integer(-2), 'sqrt', None, sp.I * sp.sqrt(2)),
                (sp.sqrt(2) * sp.I, '**', sp.Integer(2), sp.Integer(-2)),
                (1 + sp.sqrt(2), '*', sp.sqrt(2) - 1, sp.Integer(1))):
            value, reason = engine.symbolic_apply(a, op, b)
            self.assertIsNone(reason)
            self.assertEqual(value, expected)
            self.assertEqual(engine.symbolic_unpack(engine.symbolic_pack(value)), value)

    def test_generated_numbers_return_to_numeric_branches(self):
        m = memory()
        three, two = seed(m, 3), seed(m, 2)
        stats = {'new': 0}
        # Cursor 1 visits earlier record 0; step 6 reverses operands for power.
        engine.work_symbolic(m, {'kind': 'symbolic_pair', 'source': two,
                                'cursor': three + 1, 'step': 6}, stats)
        sa = m['symbolic_archive']
        nine = sa['results']['9'][0]
        real = m['expressions'][m['results']['9'][0]]
        gaussian = m['complex_archive']['expressions'][
            m['complex_archive']['results']['9+0i'][0]]
        for rec in (real, gaussian):
            self.assertEqual(rec['sources'], [{'archive': 'symbolic', 'id': nine}])
            self.assertEqual(rec['depth'], 1)
        engine.work_complex(m, {'left': gaussian['id'], 'right': 0}, {})
        self.assertIn('0+9i', m['complex_archive']['results'])
        self.assertEqual(m['foundation']['states'], [0])

    def test_imports_existing_rational_and_complex_results(self):
        m = memory()
        real_id = len(m['expressions'])
        engine.add_expression(m, {'expr': '1/3', 'value': '1/3',
            'tree': {'leaf': '1/3'}, 'parents': [], 'leaves': ['1/3'],
            'depth': 0, 'ancestry': [], 'domain': 'rational', 'pathway': 'test'})
        complex_id = engine.complex_record(m, (Fraction(2), Fraction(3)),
                                          '(2+3i)', [], 'seed', 'test')
        before = copy.deepcopy(m['expressions'])
        engine.import_symbolic_sources(m)
        sa = m['symbolic_archive']
        third = sa['expressions'][sa['results']['1/3'][0]]
        gaussian = sa['expressions'][sa['results']['2 + 3*I'][0]]
        self.assertEqual(third['sources'], [{'archive': 'rational', 'id': real_id}])
        self.assertEqual(gaussian['sources'], [{'archive': 'complex', 'id': complex_id}])
        self.assertEqual(m['expressions'][:len(before)], before)
        count = len(sa['expressions'])
        engine.import_symbolic_sources(m)
        self.assertEqual(len(sa['expressions']), count)

    def test_limits_and_undefined_operations(self):
        cases = [(sp.Integer(1), '/', sp.Integer(0)),
                 (sp.Integer(0), '**', sp.Integer(0)),
                 (sp.Integer(0), '**', sp.Integer(-1)),
                 (sp.Integer(2), '**', sp.Integer(1000000)),
                 (sp.Integer(2), '**', sp.sqrt(2)),
                 (sp.Integer(1 << 100), 'sqrt', None)]
        for a, op, b in cases:
            result, reason = engine.symbolic_apply(a, op, b)
            self.assertIsNone(result)
            self.assertIsNotNone(reason)
        m = memory()
        first = seed(m, 2)
        current = first
        for depth in range(1, engine.MAX_DEPTH + 1):
            current = engine.symbolic_record(m, sp.sqrt(2), 'root%d' % depth,
                                            [current], 'sqrt', 'test')
        rec = m['symbolic_archive']['expressions'][current]
        self.assertEqual(rec['depth'], engine.MAX_DEPTH)
        self.assertFalse(any(t.get('source') == current and t['kind'].startswith('symbolic_')
                             for t in m['queue']))
        self.assertIsNone(engine.symbolic_record(m, sp.sqrt(2), 'too_deep',
                                                [current], 'sqrt', 'test'))

    def test_safe_exact_queries_are_read_only(self):
        self.assertEqual(engine.parse_symbolic_query('sqrt(2)^2'), 2)
        self.assertEqual(engine.parse_symbolic_query('0.1 + 1/5'), sp.Rational(3, 10))
        self.assertEqual(engine.parse_symbolic_query('sqrt(-2)'), sp.I * sp.sqrt(2))
        for text in ('__import__("os")', '(1).__class__', '[1][0]',
                     '2**100000000', 'sqrt(2,3)', 'lambda: 1', '1e999999'):
            with self.assertRaises((ValueError, SyntaxError)):
                engine.parse_symbolic_query(text)
        m = memory()
        seed(m, sp.sqrt(2))
        before = copy.deepcopy(m['symbolic_archive'])
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertTrue(engine.query_symbolic(m, 'symbolic sqrt(2)'))
        self.assertEqual(m['symbolic_archive'], before)

    def test_json_resume_preserves_exact_values_and_task_steps(self):
        m = memory()
        two = seed(m, 2)
        engine.work_symbolic(m, {'kind': 'symbolic_root', 'source': two}, {'new': 0})
        root_id = m['symbolic_archive']['results']['sqrt(2)'][0]
        engine.work_symbolic(m, {'kind': 'symbolic_pair', 'source': root_id,
                                'cursor': 0, 'step': 0}, {'new': 0})
        with tempfile.TemporaryDirectory() as folder:
            with mock.patch.object(engine, 'memory_path', return_value=str(Path(folder) / 'm.json')):
                engine.save_memory(m)
                restored = engine.load_memory()
        tasks = copy.deepcopy(restored['queue'])
        records = copy.deepcopy(restored['symbolic_archive']['expressions'])
        engine.upgrade_symbolic(restored)
        self.assertEqual(restored['queue'], tasks)
        self.assertEqual(restored['symbolic_archive']['expressions'], records)
        self.assertEqual(engine.symbolic_value(restored, root_id), sp.sqrt(2))
        self.assertIn({'kind': 'symbolic_pair', 'source': root_id,
                       'cursor': 0, 'step': 1}, restored['queue'])

    def test_actual_runs_upgrade_old_memory_and_obey_budgets(self):
        m = memory()
        m.pop('symbolic_archive')
        m.pop('_symbolic_keys')
        m.pop('_symbolic_values')
        # Simulate V4.5.1 complex records, before depth metadata existed.
        for rec in m['complex_archive']['expressions']:
            rec.pop('depth')
        foundation_before = copy.deepcopy(m['foundation'])
        with tempfile.TemporaryDirectory() as folder:
            path = str(Path(folder) / 'memory.json')
            with mock.patch.object(engine, 'memory_path', return_value=path):
                engine.save_memory(m)
                for _ in range(6):
                    with contextlib.redirect_stdout(io.StringIO()), mock.patch('builtins.input', return_value=''):
                        engine.run()
                    restored = engine.load_memory()
                    counts = restored['runs'][-1]['processed']
                    self.assertLessEqual(counts['symbolic_root'] + counts['symbolic_pair'],
                                         engine.SYMBOLIC_WORK_PER_RUN)
                    self.assertLessEqual(counts['complex'] + counts['complex_feedback'],
                                         engine.COMPLEX_WORK_PER_RUN)
                self.assertIn('sqrt(2)', restored['symbolic_archive']['results'])
                self.assertTrue(any(r['operation'] == '**'
                                    for r in restored['symbolic_archive']['expressions']))
                self.assertTrue(any(r['depth'] > 1 for r in restored['symbolic_archive']['expressions']))
                self.assertEqual(restored['foundation']['states'][:1], foundation_before['states'])
                self.assertEqual(restored['version'], '4.1')

    def test_missing_dependency_does_not_touch_memory(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'memory.json'
            path.write_text('original memory', encoding='utf-8')
            with mock.patch.object(engine, 'memory_path', return_value=str(path)):
                with mock.patch.object(engine, 'sympy_module', side_effect=RuntimeError('Install sympy')):
                    with contextlib.redirect_stdout(io.StringIO()):
                        engine.run()
            self.assertEqual(path.read_text(encoding='utf-8'), 'original memory')


if __name__ == '__main__':
    unittest.main()
