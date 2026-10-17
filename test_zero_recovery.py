"""Recovery and installer tests. V4.7.1 is not yet checked into this repo.

The fixture uses the checked-in V4.6.5 arithmetic workers with the V4.7.1
zero-gate contract. Full V4.7.1 roles/calculus regression remains a release check.
"""
import copy
import contextlib
import io
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import zero_recovery as zr
from apply_zero_recovery_patch import patch

ROOT = Path(__file__).parent


def engine():
    spec = importlib.util.spec_from_file_location('recovery_fixture', ROOT / 'zero_theoremV4.6.5.py')
    e = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(e)
    e.ZERO_CORE_RULE = 'everything_through_zero_v1'
    def zero_core(m, domain, *, record=None, operation=None, operands=(), **kwargs):
        if record is not None:
            state = m.setdefault('zero_core', {'record_passages': {}})
            if 'zero_core_passage' not in record:
                record['zero_core_passage'] = {
                    'rule': e.ZERO_CORE_RULE, 'archive': domain, 'id': record['id'],
                    'zero_nexus': 'Z0', 'historical_backfill': False,
                    'effect': 'identity_preserves_construction'}
                counts = state['record_passages']
                counts[domain] = counts.get(domain, 0) + 1
            return record
        if domain != 'rational':
            raise ValueError('Fixture gate covers rational arithmetic only')
        a, b = operands
        return e.operate(a, operation, b)
    e.zero_core = zero_core
    # Required constructor contract; the fixture does not claim to execute
    # V4.7.1 role/calculus workers.
    e.role_record = lambda *a, **k: None
    e.calculus_record = lambda *a, **k: None
    return e


def memory(e):
    m = e.empty_memory()
    m['_keys'] = set(m['known_expression_keys'])
    e.upgrade_runtime(m)
    e.upgrade_v44(m)
    e.upgrade_tracking_namespaces(m)
    e.upgrade_v45(m)
    e.upgrade_complex_feedback(m)
    e.upgrade_symbolic(m)
    e.upgrade_symbolic_zero_nexus(m)
    e.upgrade_zero_archive_access(m)
    e.upgrade_archive_integration(m)
    e.register_next_state(m)
    stats = {'new': 0, 'observer_added': 0}
    idx = e.combine(m, 0, 1, '-', 'result_feedback_v42', stats)
    # Real V4.7.1 constructors perform this gate for every archive record.
    for domain in zr._ZR_DOMAINS:
        for rec in zr._zr_records(m, domain):
            e.zero_core(m, domain, record=rec)
    return m, idx


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.e = engine()
        self.m, self.idx = memory(self.e)

    def preflight(self, m):
        return zr._zr_preflight(m, vars(self.e))

    def baseline(self):
        result, ready = self.preflight(self.m)
        self.assertTrue(ready)
        return result

    def test_intact_bootstrap_and_repeated_check_preserve_records(self):
        original = copy.deepcopy(self.m)
        baseline = self.baseline()
        self.assertEqual(self.m, original)
        again, ready = self.preflight(baseline)
        self.assertTrue(ready)
        self.assertEqual(again, baseline)
        self.assertEqual(baseline['expressions'], self.m['expressions'])

    def test_passage_mismatch_routes_to_pending_before_workers(self):
        self.m['runs'] = [{'run': 1}]
        self.e.zero_core_report = lambda m: {'complete': False, 'archives': {}}
        result, ready = self.preflight(self.m)
        self.assertFalse(ready)
        self.assertIn('coverage', result['zero_recovery'])

    def test_saved_run_checks_archive_links(self):
        self.m['runs'] = [{'run': 1}]
        result, ready = self.preflight(self.m)
        self.assertTrue(ready, result['zero_recovery'].get('audit'))

    def test_manifest_middle_deletion_restores_same_id_and_construction(self):
        m = self.baseline()
        # Add a later record to expose the position shift after deletion.
        stats = {'new': 0, 'observer_added': 0}
        self.e.combine(m, 0, 1, '+', 'result_feedback_v42', stats)
        zr._zr_track_new(m)
        expected = copy.deepcopy(m['expressions'])
        del m['expressions'][self.idx]
        repaired, ready = self.preflight(m)
        self.assertTrue(ready)
        self.assertEqual(repaired['expressions'], expected)
        self.assertEqual([r['id'] for r in repaired['expressions']], list(range(len(expected))))

    def test_manifest_tail_deletion_does_not_reuse_id(self):
        m = self.baseline()
        next_id = m['zero_recovery']['next_ids']['rational']
        del m['expressions'][-1]
        repaired, ready = self.preflight(m)
        self.assertTrue(ready)
        self.assertEqual(len(repaired['expressions']), next_id)
        stats = {'new': 0, 'observer_added': 0}
        created = self.e.combine(repaired, 1, 1, '+', 'result_feedback_v42', stats)
        self.assertEqual(created, next_id)

    def test_legacy_deletion_uses_key_and_independent_creation_event(self):
        original = copy.deepcopy(self.m['expressions'][self.idx])
        del self.m['expressions'][self.idx]
        repaired, ready = self.preflight(self.m)
        self.assertTrue(ready)
        self.assertEqual(repaired['expressions'][self.idx], original)
        self.assertEqual(repaired['zero_recovery']['events'][-1]['reason'], 'legacy_evidence_reexecution')

    def test_insufficient_evidence_reserves_unknown_slot(self):
        self.m['genesis']['events'] = []
        del self.m['expressions'][self.idx]
        result, ready = self.preflight(self.m)
        self.assertFalse(ready)
        slot = result['expressions'][self.idx]
        self.assertEqual(slot['status'], 'zero_recovery_pending')
        self.assertIsNone(slot['value'])
        self.assertEqual(slot['id'], self.idx)
        self.assertEqual(result['queue'], self.m['queue'])
        again, ready = self.preflight(result)
        self.assertFalse(ready)
        self.assertEqual(again['zero_recovery']['events'], result['zero_recovery']['events'])

    def test_duplicate_ids_block_without_mutating_input(self):
        self.m['expressions'].append(copy.deepcopy(self.m['expressions'][0]))
        original = copy.deepcopy(self.m)
        with self.assertRaises(zr.ZeroRecoveryPending):
            self.preflight(self.m)
        self.assertEqual(original, self.m)

    def test_forged_existing_value_fails_manifest(self):
        m = self.baseline()
        m['expressions'][self.idx]['value'] = '99'
        result, ready = self.preflight(m)
        self.assertFalse(ready)
        self.assertEqual(result['zero_recovery']['status'], 'blocked')

    def test_forged_legacy_value_fails_tree_evaluation(self):
        self.m['expressions'][self.idx]['value'] = '99'
        _, ready = self.preflight(self.m)
        self.assertFalse(ready)

    def test_conflicting_legacy_creation_evidence_stays_pending(self):
        events = self.m['genesis']['events']
        event = next(e for e in events if e.get('type') == 'expression_created' and e.get('expression_id') == self.idx)
        forged = copy.deepcopy(event)
        forged['value'] = '99'
        events.append(forged)
        del self.m['expressions'][self.idx]
        _, ready = self.preflight(self.m)
        self.assertFalse(ready)

    def test_unsupported_construction_stays_pending(self):
        m = self.baseline()
        # The foundation origin has no binary recipe. Never fabricate it.
        del m['expressions'][0]
        result, ready = self.preflight(m)
        self.assertFalse(ready)
        self.assertIsNone(result['expressions'][0]['value'])

    def test_counter_mismatch_is_not_silently_reset(self):
        m = self.baseline()
        m['zero_recovery']['next_ids']['rational'] += 1
        with self.assertRaises(zr.ZeroRecoveryPending):
            self.preflight(m)

    def test_load_pending_writes_checkpoint_and_preserves_main_bytes(self):
        e = self.e
        self.m['genesis']['events'] = []
        del self.m['expressions'][self.idx]
        # Remove runtime sets for a normal persistent JSON file.
        raw = json.dumps({k: v for k, v in self.m.items() if not k.startswith('_')}).encode()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'memory.json'
            path.write_bytes(raw)
            e.memory_path = lambda: str(path)
            zr.install_zero_recovery(vars(e))
            with self.assertRaises(zr.ZeroRecoveryPending):
                e.load_memory()
            self.assertEqual(path.read_bytes(), raw)
            checkpoint = json.loads(Path(str(path) + '.zero-recovery.json').read_text())
            self.assertEqual(checkpoint['expressions'][self.idx]['status'], 'zero_recovery_pending')

    def test_saved_manifest_survives_roundtrip(self):
        e = self.e
        m = self.baseline()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'memory.json'
            e.memory_path = lambda: str(path)
            zr.install_zero_recovery(vars(e))
            e.save_memory(m)
            loaded = e.load_memory()
            self.assertEqual(loaded['zero_recovery']['next_ids'], m['zero_recovery']['next_ids'])
            self.assertEqual(loaded['expressions'], m['expressions'])

    def test_rational_constructor_tracks_next_id(self):
        e = self.e
        m = self.baseline()
        zr.install_zero_recovery(vars(e))
        stats = {'new': 0, 'observer_added': 0}
        idx = e.combine(m, 1, 1, '+', 'result_feedback_v42', stats)
        self.assertEqual(m['zero_recovery']['next_ids']['rational'], idx + 1)
        self.assertIn(str(idx), m['zero_recovery']['manifest']['rational'])


class ContinuationSmokeTests(unittest.TestCase):
    def test_existing_engine_runs_twice_with_manifest_hooks(self):
        e = engine()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'memory.json'
            e.memory_path = lambda: str(path)
            zr.install_zero_recovery(vars(e))
            with contextlib.redirect_stdout(io.StringIO()), mock.patch('builtins.input', return_value=''):
                e.run()
                e.run()
            saved = json.loads(path.read_text())
            self.assertEqual(len(saved['runs']), 2)
            self.assertEqual(saved['zero_recovery']['status'], 'ready')
            self.assertEqual(saved['zero_recovery']['next_ids']['rational'], len(saved['expressions']))


class InstallerTests(unittest.TestCase):
    def source(self):
        names = ('zero_core', 'run', 'load_memory', 'save_memory', 'role_record',
                 'calculus_record', 'archive_link_audit', 'exact_lookup_key',
                 'add_expression', 'complex_record', 'symbolic_record')
        return ('ZERO_CORE_RULE="everything_through_zero_v1"\n' +
                '\n'.join('def %s(*args, **kwargs): pass' % name for name in names) +
                '\nif __name__ == "__main__":\n    run()\n')

    def test_generated_engine_compiles_and_installs_before_main(self):
        result = patch(self.source(), (ROOT / 'zero_recovery.py').read_text())
        namespace = {'__name__': 'test_generated'}
        exec(compile(result, '<generated>', 'exec'), namespace)
        self.assertTrue(namespace['_ZERO_RECOVERY_INSTALLED'])
        with self.assertRaises(ValueError):
            patch(result, '')

    def test_old_engine_is_rejected(self):
        with self.assertRaises(ValueError):
            patch((ROOT / 'zero_theoremV4.6.5.py').read_text(), '')


if __name__ == '__main__':
    unittest.main()
