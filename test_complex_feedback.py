"""Regression checks for persisted, exact complex feedback (standard library)."""
import contextlib
import copy
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from fractions import Fraction


SOURCE = Path(__file__).with_name('zero_theoremV4.6.py')
spec = importlib.util.spec_from_file_location('zero_theorem', SOURCE)
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)


def memory():
    m = engine.empty_memory()
    engine.upgrade_runtime(m)
    engine.upgrade_v44(m)
    engine.upgrade_v45(m)
    engine.upgrade_complex_feedback(m)
    engine.rebalance_queue(m)
    return m


class ComplexFeedbackTests(unittest.TestCase):
    def test_generated_result_becomes_operand(self):
        m = memory()
        engine.work_complex_feedback(m, {'source': 0, 'cursor': 0}, {})
        ca = m['complex_archive']
        negative_one = next(r for r in ca['expressions']
                            if r['expr'] == '(i * i)')
        self.assertEqual(negative_one['value'], '-1+0i')
        self.assertEqual(negative_one['depth'], 1)
        task = {'kind': 'complex_feedback', 'source': negative_one['id'],
                'cursor': 0}
        self.assertIn(task, m['queue'][m['queue_head']:])
        engine.work_complex_feedback(m, task, {})
        child = next(r for r in ca['expressions']
                     if r['expr'] == '((i * i) * i)')
        self.assertEqual(child['value'], '0-1i')
        self.assertEqual(child['parents'], [negative_one['id'], 0])
        self.assertEqual(child['depth'], 2)
        reverse = next(r for r in ca['expressions']
                       if r['expr'] == '(i * (i * i))')
        self.assertEqual(reverse['parents'], [0, negative_one['id']])

    def test_old_archive_backfill_is_idempotent(self):
        m = memory()
        engine.work_complex(m, {'left': 0, 'right': 1}, {})
        ca = m['complex_archive']
        before = copy.deepcopy(ca['expressions'])
        ca.pop('feedback_version')
        ca.pop('feedback_scheduled_count')
        for rec in ca['expressions']:
            rec.pop('depth')
        m['queue'] = [t for t in m['queue'] if t['kind'] != 'complex_feedback']
        engine.rebalance_queue(m)
        engine.upgrade_complex_feedback(m)
        self.assertEqual(ca['expressions'], before)
        pending = copy.deepcopy(m['queue'])
        engine.upgrade_complex_feedback(m)
        self.assertEqual(m['queue'], pending)
        self.assertEqual(ca['feedback_scheduled_count'], len(before))

    def test_saved_cursor_resumes_without_rescheduling(self):
        m = memory()
        engine.work_complex_feedback(m, {'source': 1, 'cursor': 0}, {})
        cursor_task = {'kind': 'complex_feedback', 'source': 1, 'cursor': 1}
        self.assertIn(cursor_task, m['queue'])
        with tempfile.TemporaryDirectory() as folder:
            original_path = engine.memory_path
            engine.memory_path = lambda: str(Path(folder) / 'memory.json')
            try:
                engine.save_memory(m)
                restored = engine.load_memory()
            finally:
                engine.memory_path = original_path
        before = copy.deepcopy(restored['queue'])
        engine.upgrade_complex_feedback(restored)
        self.assertEqual(restored['queue'], before)
        self.assertIn(cursor_task, restored['queue'])
        self.assertEqual(restored['version'], '4.1')
        self.assertEqual(restored['schema'], 1)

    def test_depth_bits_and_zero_division(self):
        m = memory()
        ca = m['complex_archive']
        idx = 0
        for _ in range(engine.MAX_DEPTH):
            idx = engine.complex_record(m, (Fraction(0), Fraction(1)),
                                        'nested(%d)' % idx, [idx], '*', 'test')
        self.assertEqual(ca['expressions'][idx]['depth'], engine.MAX_DEPTH)
        count = len(ca['expressions'])
        engine.work_complex(m, {'left': idx, 'right': 0}, {})
        self.assertEqual(len(ca['expressions']), count)
        self.assertFalse(any(t['kind'] == 'complex_feedback' and t['source'] == idx
                             for t in m['queue']))
        self.assertIsNone(engine.complex_record(
            m, (Fraction(1 << engine.MAX_BITS), Fraction(0)), 'oversize', [],
            'seed', 'test'))
        zero_id = next(r['id'] for r in ca['expressions'] if r['value'] == '0+0i')
        engine.work_complex(m, {'left': 0, 'right': zero_id}, {})
        self.assertFalse(any(r['expr'] == '(i / 0)' for r in ca['expressions']))

    def test_actual_runs_preserve_queue_and_complex_budget(self):
        with tempfile.TemporaryDirectory() as folder:
            original_path = engine.memory_path
            engine.memory_path = lambda: str(Path(folder) / 'memory.json')
            import unittest.mock
            try:
                for _ in range(4):
                    with contextlib.redirect_stdout(io.StringIO()):
                        with unittest.mock.patch('builtins.input', return_value=''):
                            engine.run()
                    m = engine.load_memory()
                    processed = m['runs'][-1]['processed']
                    self.assertLessEqual(processed['complex'] + processed['complex_feedback'],
                                         engine.COMPLEX_WORK_PER_RUN)
                    self.assertTrue(all(r['depth'] <= engine.MAX_DEPTH
                                        for r in m['complex_archive']['expressions']))
                self.assertEqual(len(m['runs']), 4)
                self.assertIn('-1+0i', m['complex_archive']['results'])
                self.assertTrue(any(r['depth'] >= 2
                                    for r in m['complex_archive']['expressions']))
            finally:
                engine.memory_path = original_path


if __name__ == '__main__':
    unittest.main()
