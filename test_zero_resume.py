"""V4.7.8 approval/resume regression checks using generated memory only."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    'zero_resume_v478', Path(__file__).with_name('zero_theoremV4.7.8.py'))
e = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(e)


class ResumeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'memory.json'
            with patch.object(e, 'memory_path', return_value=str(path)), \
                    patch('builtins.input', return_value=''), \
                    contextlib.redirect_stdout(io.StringIO()):
                e.run()
            cls.generated = json.loads(path.read_text())

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.candidate = self.root / 'candidate.json'
        self.candidate.write_text(json.dumps(self.generated))
        self.target = self.root / 'memory.json'
        self.damaged = b'{"deliberately": broken}'
        self.target.write_bytes(self.damaged)

    def test_approval_backup_and_actual_continuation(self):
        with contextlib.redirect_stdout(io.StringIO()):
            approved = e._za_promote(str(self.candidate), str(self.target))
            self.assertFalse(approved['zero_resume']['continuation_verified'])
            with patch.object(e, 'memory_path', return_value=str(self.target)), \
                    patch('builtins.input', return_value=''):
                e.run()
        saved = json.loads(self.target.read_text())
        self.assertTrue(saved['zero_resume']['continuation_verified'])
        self.assertEqual(len(saved['runs']), len(self.generated['runs']) + 1)
        self.assertGreater(len(saved['expressions']), len(self.generated['expressions']))
        self.assertEqual(e.archive_link_audit(saved)['issues'], 0)
        self.assertEqual(Path(saved['zero_resume']['backup_path']).read_bytes(), self.damaged)
        self.assertEqual(json.loads(self.candidate.read_text()), self.generated)

    def test_invalid_candidates_preserve_active_memory(self):
        for category in ('arithmetic', 'foundation', 'parent'):
            with self.subTest(category=category):
                value = copy.deepcopy(self.generated)
                if category == 'arithmetic': value['expressions'][10]['value'] = '999'
                if category == 'foundation': value['foundation']['states'].append(99)
                if category == 'parent': value['expressions'][10]['parents'] = [99999]
                self.candidate.write_text(json.dumps(value))
                with self.assertRaises(e.ZeroRecoveryPending):
                    e._za_promote(str(self.candidate), str(self.target))
                self.assertEqual(self.target.read_bytes(), self.damaged)

    def test_saved_ready_loader_returns_to_engine(self):
        state = {'source_sha256': hashlib.sha256(self.damaged).hexdigest(),
                 'status': 'candidate_ready',
                 'candidates': [{'archive_ready': True, 'path': str(self.candidate)}]}
        with patch.object(e, '_zw_recover', return_value=state), \
                contextlib.redirect_stdout(io.StringIO()):
            accepted = e._zt_load_file(str(self.target))
        self.assertEqual(accepted['zero_resume']['status'], 'approved_for_execution')
        self.assertEqual(Path(accepted['zero_resume']['backup_path']).read_bytes(), self.damaged)

    def test_inspection_does_not_promote(self):
        state = {'status': 'candidate_ready'}
        with patch.object(e, '_zw_recover', return_value=state), \
                self.assertRaises(e.ZeroRecoveryPending):
            e._zt_load_file(str(self.target), inspect_only=True)
        self.assertEqual(self.target.read_bytes(), self.damaged)

    def test_stale_checkpoint_is_rejected(self):
        with self.assertRaises(e.ZeroRecoveryPending):
            e.zero_approve_recovery(str(self.target), {'source_sha256': 'stale'})
        self.assertEqual(self.target.read_bytes(), self.damaged)

    def test_conflicting_ready_candidates_are_rejected(self):
        other = self.root / 'other.json'
        value = copy.deepcopy(self.generated)
        value['queue_head'] += 1
        other.write_text(json.dumps(value))
        state = {'source_sha256': hashlib.sha256(self.damaged).hexdigest(),
                 'candidates': [{'archive_ready': True, 'path': str(p)}
                                for p in (self.candidate, other)]}
        with self.assertRaisesRegex(e.ZeroRecoveryPending, 'unambiguous'):
            e.zero_approve_recovery(str(self.target), state)
        self.assertEqual(self.target.read_bytes(), self.damaged)

    def test_failed_save_does_not_claim_continuation(self):
        with contextlib.redirect_stdout(io.StringIO()):
            value = e._za_promote(str(self.candidate), str(self.target))
        with patch.object(e, '_za_previous_save', side_effect=OSError('test storage failure')):
            with self.assertRaises(OSError): e.save_memory(value)
        self.assertFalse(value['zero_resume']['continuation_verified'])
        self.assertFalse(json.loads(self.target.read_text())['zero_resume']['continuation_verified'])


if __name__ == '__main__':
    unittest.main()
