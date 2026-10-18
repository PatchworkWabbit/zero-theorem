"""Task 7 uses only disposable copies of a generated public test fixture."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('task7_engine', ROOT / 'zero_theoremV4.7.15.py')
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)


class RecoveryRetryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = ROOT / 'task7_fixture/baseline.json'
        if fixture.is_file():
            legacy = json.loads(fixture.read_text())
        else:
            with zipfile.ZipFile(ROOT / 'zero_theorem_task6_tests.zip') as bundle:
                legacy = json.loads(bundle.read('task4_fixture/baseline.json'))
        cls.base, ready = e._zr_preflight(legacy, vars(e))
        assert ready

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / 'memory.json'
        self.active_memory = copy.deepcopy(self.base)
        self.memory = copy.deepcopy(self.base)

    def missing_recipe(self):
        idx = len(self.memory['complex_archive']['expressions']) - 1
        self.memory['complex_archive']['expressions'].pop()
        self.memory['zero_recovery']['manifest']['complex'][str(idx)].pop('typed_recipe')
        self.memory['complex_archive']['known_keys'] = []
        return idx

    def install(self):
        self.source.write_text(json.dumps(self.memory))
        digest = e._z7_hash_file(self.source)
        self.root = Path(str(self.source) + '.adaptive-work') / digest
        self.root.mkdir(parents=True)
        self.snapshot = self.root / 'source.snapshot'
        self.snapshot.write_bytes(self.source.read_bytes())
        self.active = self.root / 'regeneration' / e.MEMORY_FILENAME
        self.active.parent.mkdir()
        e._zn_checkpoint(str(self.active), self.active_memory)
        self.state = {'schema': 1, 'rule': 'zero_adaptive_v4710', 'source': str(self.source),
                      'source_sha256': digest, 'source_snapshot': str(self.snapshot),
                      'selected_branch': 'regeneration', 'status': 'selected_and_resumed',
                      'new_lineage': True, 'historical_identity_proven': False,
                      'trials': {k: {'status': 'unresolved' if k == 'recovery' else 'ready',
                                    'elapsed_seconds': 0, 'cycles': []} for k in ('recovery', 'regeneration')}}
        e._zg_checkpoint(self.state, str(self.root))
        self.pointer = Path(str(self.source) + '.adaptive-active.json')
        e._zn_checkpoint(str(self.pointer), {'rule': 'adaptive_active_v4710',
                         'source_sha256': digest, 'branch': 'regeneration', 'new_lineage': True})
        self.protected = {p: p.read_bytes() for p in (self.source, self.snapshot, self.pointer, self.active)}

    def retry(self, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            report = e.zero_core(None, 'recovery_feedback', operation='retry',
                                 operands=(str(self.source), str(self.active), self.active_memory), **kwargs)
        for path, raw in self.protected.items():
            self.assertEqual(path.read_bytes(), raw, str(path))
        return report

    def test_matching_digest_supplies_recipe_then_independent_replay(self):
        idx = self.missing_recipe()
        self.install()
        report = self.retry()
        self.assertEqual(report['status'], 'candidate_ready')
        recovered = e._zg_check(report['candidate'])
        self.assertEqual(e._zr_payload(recovered['complex_archive']['expressions'][idx]),
                         e._zr_payload(self.base['complex_archive']['expressions'][idx]))
        self.assertEqual(report['attempts'][0]['recipe_proposals'][0]['retained_digest'],
                         self.memory['zero_recovery']['manifest']['complex'][str(idx)]['digest'])
        self.assertFalse(report['historical_identity_proven'])
        self.assertFalse(report['regenerated_values_are_historical_evidence'])

    def test_same_value_different_construction_never_supplies_recipe(self):
        idx = self.missing_recipe()
        target = self.active_memory['complex_archive']['expressions'][idx]
        target['expr'] += ' different construction'
        self.install()
        report = self.retry()
        self.assertEqual(report['status'], 'pending')
        self.assertEqual(report['attempts'][0]['recipe_proposals'], [])
        self.assertFalse((self.root / 'recovery' / e.MEMORY_FILENAME).exists())

    def test_unchanged_evidence_does_not_repeat_exhausted_work(self):
        self.missing_recipe()
        self.active_memory['complex_archive']['expressions'].pop()
        self.install()
        first = self.retry()
        # Drain any queued verifier tasks without changing the evidence.
        for _ in range(5):
            second = self.retry()
            if len(second['attempts']) == len(first['attempts']): break
            first = second
        self.assertEqual(len(self.retry()['attempts']), len(second['attempts']))

    def test_changed_rules_trigger_new_attempt(self):
        self.missing_recipe()
        self.active_memory['complex_archive']['expressions'].pop()
        self.install()
        with patch.object(e, '_z7_rules_signature', return_value='rules-one'):
            first = self.retry()
        with patch.object(e, '_z7_rules_signature', return_value='rules-two'):
            second = self.retry()
        self.assertGreater(len(second['attempts']), len(first['attempts']))
        self.assertIn('executable_rules_changed', second['attempts'][-1]['triggers'])

    def test_later_matching_evidence_reopens_pending_recovery(self):
        self.missing_recipe()
        self.active_memory['complex_archive']['expressions'].pop()
        self.install()
        first = self.retry()
        self.assertEqual(first['status'], 'pending')
        self.active_memory = copy.deepcopy(self.base)
        e._zn_checkpoint(str(self.active), self.active_memory)
        self.protected[self.active] = self.active.read_bytes()
        second = self.retry()
        self.assertEqual(second['status'], 'candidate_ready')
        self.assertIn('new_constructions_matching_retained_payload_digests', second['attempts'][-1]['triggers'])

    def test_conflicting_surviving_recipe_is_not_replaced(self):
        idx = self.missing_recipe()
        self.memory['zero_recovery']['manifest']['complex'][str(idx)]['typed_recipe'] = {'schema': 999}
        self.install()
        report = self.retry()
        self.assertEqual(report['status'], 'pending')
        self.assertEqual(report['attempts'][0]['recipe_proposals'], [])

    def corrupt_many(self):
        rows = [r for r in self.memory['expressions'] if r['pathway'] in e._ZR_ARITHMETIC][:24]
        assert len(rows) == 24
        for rec in rows: rec['value'] = '123456'
        self.install()

    def test_feedback_cursor_is_bounded_and_resumes(self):
        self.corrupt_many()
        first = self.retry(work_budget=2)
        state = e._zg_read(str(self.root / 'state.json'))
        feedback = state['trials']['recovery']['feedback_checkpoint']
        saved1 = e._zg_read(feedback)
        self.assertLessEqual(saved1['head'], 2)
        second = self.retry(work_budget=2)
        saved2 = e._zg_read(feedback)
        self.assertGreater(saved2['head'], saved1['head'])
        self.assertLessEqual(saved2['head'] - saved1['head'], 2)
        self.assertIn('saved_feedback_work_remaining', second['attempts'][-1]['triggers'])
        self.assertEqual(saved2['source_sha256'], saved1['source_sha256'])

    def test_interruption_preserves_cursor_and_restarts(self):
        self.corrupt_many()
        previous = e.zero_verify_candidate
        def interrupted(*args, **kwargs):
            previous(*args, **kwargs)
            raise KeyboardInterrupt()
        with patch.object(e, 'zero_verify_candidate', side_effect=interrupted), self.assertRaises(KeyboardInterrupt):
            self.retry(work_budget=1)
        ledger = e._zg_read(str(self.root / 'recovery-retry-state.json'))
        self.assertEqual(ledger['status'], 'interrupted')
        report = self.retry(work_budget=1)
        self.assertIn('interrupted_slice', report['attempts'][-1]['triggers'])
        self.assertEqual(report['attempts'][-1]['verification_executions'], 1)

    def test_normal_run_services_recovery_and_continues_regeneration(self):
        self.missing_recipe()
        self.install()
        before = len(self.active_memory['runs'])
        with patch.object(e, 'memory_path', return_value=str(self.source)), \
                patch('builtins.input', return_value=''), contextlib.redirect_stdout(io.StringIO()):
            e.run()
        after = e._zg_check(str(self.active))
        self.assertEqual(len(after['runs']), before + 1)
        ledger = e._zg_read(str(self.root / 'recovery-retry-state.json'))
        self.assertEqual(ledger['status'], 'candidate_ready')
        self.assertEqual(self.source.read_bytes(), self.protected[self.source])
        self.assertEqual(self.pointer.read_bytes(), self.protected[self.pointer])

    def test_candidate_ready_is_retained_without_switching(self):
        self.missing_recipe()
        self.install()
        first = self.retry()
        second = self.retry()
        self.assertEqual(len(second['attempts']), len(first['attempts']))
        state = e._zg_read(str(self.root / 'state.json'))
        self.assertEqual(state['selected_branch'], 'regeneration')
        self.assertFalse(state['trials']['recovery']['continuation_verified'])

    def test_changed_ready_candidate_is_rechecked_and_preserved(self):
        self.missing_recipe()
        self.install()
        first = self.retry()
        candidate = Path(first['candidate'])
        data = json.loads(candidate.read_text())
        data['expressions'][0]['value'] = '99'
        candidate.write_text(json.dumps(data))
        before = candidate.read_bytes()
        second = self.retry()
        self.assertEqual(second['status'], 'pending')
        self.assertIn('recovery_candidate_changed', second['attempts'][-1]['triggers'])
        self.assertEqual(candidate.read_bytes(), before)

    def test_changed_snapshot_blocks_recovery(self):
        self.missing_recipe()
        self.install()
        self.snapshot.write_bytes(b'changed snapshot')
        with self.assertRaisesRegex(e.ZeroRecoveryPending, 'binding failed'):
            self.retry()

    def test_matching_digest_still_requires_correct_reexecution(self):
        idx = self.missing_recipe()
        forged = self.active_memory['complex_archive']['expressions'][idx]
        forged['value'] = '999'
        self.memory['zero_recovery']['manifest']['complex'][str(idx)]['digest'] = e._zr_digest(e._zr_payload(forged))
        self.install()
        report = self.retry()
        self.assertEqual(report['status'], 'pending')
        self.assertEqual(len(report['attempts'][0]['recipe_proposals']), 1)
        self.assertFalse((self.root / 'recovery' / e.MEMORY_FILENAME).exists())

    def test_repeated_bounded_feedback_reaches_verified_candidate(self):
        self.corrupt_many()
        report = self.retry(work_budget=8)
        for _ in range(10):
            if report['status'] == 'candidate_ready': break
            report = self.retry(work_budget=8)
        self.assertEqual(report['status'], 'candidate_ready')
        e._zg_check(report['candidate'])

    def test_retry_can_be_disabled_without_stopping_exploration(self):
        self.missing_recipe()
        self.install()
        with patch.object(e, 'memory_path', return_value=str(self.source)), \
                patch.object(e, 'RECOVERY_RETRY_ENABLED', False), \
                patch('builtins.input', return_value=''), contextlib.redirect_stdout(io.StringIO()):
            e.run()
        self.assertFalse((self.root / 'recovery-retry-state.json').exists())
        self.assertEqual(len(e._zg_check(str(self.active))['runs']), len(self.active_memory['runs']) + 1)

    def test_new_matching_proposals_obey_work_budget(self):
        for idx in (123, 124, 125):
            self.memory['complex_archive']['expressions'] = [r for r in self.memory['complex_archive']['expressions'] if r['id'] != idx]
            self.memory['zero_recovery']['manifest']['complex'][str(idx)].pop('typed_recipe')
        self.memory['complex_archive']['known_keys'] = []
        self.install()
        first = self.retry(work_budget=1)
        self.assertLessEqual(len(first['attempts'][0]['recipe_proposals']), 1)
        report = first
        for _ in range(4):
            if report['status'] == 'candidate_ready': break
            report = self.retry(work_budget=1)
            self.assertLessEqual(len(report['attempts'][-1]['recipe_proposals']), 1)
        self.assertEqual(report['status'], 'candidate_ready')


if __name__ == '__main__':
    unittest.main()
