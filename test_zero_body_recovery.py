"""Reproducible V4.7.5 checks; no user memory or hosted fixture required."""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    'zero_theorem_v475', Path(__file__).with_name('zero_theoremV4.7.5.py'))
engine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(engine)


class WholeBodyRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with tempfile.TemporaryDirectory() as directory:
            memory = Path(directory) / engine.MEMORY_FILENAME
            with patch.object(engine, 'memory_path', return_value=str(memory)), \
                    patch('builtins.input', return_value=''), \
                    contextlib.redirect_stdout(io.StringIO()):
                engine.run()
            cls.memory = json.loads(memory.read_text(encoding='utf-8'))

    def test_lossless_ordered_symbol_map(self):
        text = '{"alpha":"λ🐰","ordered":[0,1,0]}'
        mapped = engine.zero_core(None, 'whole_body', operation='map', operands=(text,))
        self.assertEqual(mapped['source_text'], text)
        self.assertEqual(''.join(text[a:b] for a, b, _ in mapped['ordered_symbol_spans']), text)
        self.assertEqual(mapped['alphabet'][str(ord('λ'))], 'λ')

    def test_damaged_expression_keeps_full_neighbours(self):
        def record(idx):
            return {'expr': str(idx), 'value': str(idx), 'tree': {'leaf': idx},
                    'parents': [], 'id': idx}
        left = json.dumps(record(0), separators=(',', ':'))
        right = json.dumps(record(3), separators=(',', ':'))
        text = '{"expressions":[' + left + ',{"expr":"broken","tree":,' + right + ']}'
        mapped = engine._zw_map(text)
        self.assertEqual(len(mapped['zero_slots']), 1)
        slot = mapped['zero_slots'][0]
        self.assertEqual(slot['candidate_ids'], [1, 2])
        self.assertEqual(slot['left_anchor']['record'], record(0))
        self.assertEqual(slot['right_anchor']['record'], record(3))
        self.assertEqual(slot['raw_fragment'], text[slot['start']:slot['end']])
        skeleton = engine._zt_parse(engine._zn_apply(text, mapped['candidate_skeleton_edits']))
        self.assertEqual(skeleton['expressions'], [record(0), record(3)])
        self.assertIn('broken', mapped['source_text'])

    def test_two_sided_bridge_preserves_evidence(self):
        roles = '"roles":["value","variable","operation","combined"]'
        text = '{' + roles.replace('variable"', 'varia') + ',"other":{' + roles + '}}'
        with self.assertRaises(json.JSONDecodeError) as caught:
            engine._zt_parse(text)
        proposals = engine._zw_bridges(text, text, caught.exception)
        self.assertTrue(proposals)
        valid = [(candidate, edit) for candidate, edit in proposals
                 if edit['after'] == 'ble"']
        self.assertTrue(valid)
        parsed = engine._zt_parse(valid[0][0])
        self.assertEqual(parsed['roles'], parsed['other']['roles'])
        for start, end in valid[0][1]['evidence_spans']:
            self.assertEqual(text[start+16:end-16], valid[0][1]['after'])

    def test_task_identity_rejects_wrong_parent(self):
        task = {'kind': 'frontier', 'left': 2, 'right': 0}
        event = {'type': 'tangent_queued', 'seq': 1, 'kind': 'frontier',
                 'task_key': json.dumps(task), 'parent': 'rational:3'}
        issues = engine._zw_constraints(json.dumps({'genesis': {'events': [event]}}))
        self.assertEqual(issues[0]['expected_parent'], 'rational:2')
        self.assertEqual(issues[0]['event_seq'], 1)

    def test_ledger_uses_event_counter_not_neighbour_value(self):
        prefix = json.dumps({'genesis': {'suppressed_events': 0, 'events': [
            {'type': 'tangent_queued', 'parent': 'rational:2',
             'parent_generated': 7, 'seq': 4}]}}, separators=(',', ':'))[:-1]
        text = prefix + ',"tangent_ledger":{"parents":{' \
            '"rational:1":{"generated":1,"selected":0,"completed":0},' \
            '"selected":0,"completed":0},' \
            '"rational:3":{"generated":1,"selected":0,"completed":0}}}}'
        options = engine._zw_ledger_bridge(text)
        self.assertEqual(len(options), 1)
        repaired = engine._zt_parse(options[0][0])
        self.assertEqual(repaired['tangent_ledger']['parents']['rational:2']['generated'], 7)
        self.assertFalse(engine._zw_ledger_bridge(text.replace('"suppressed_events":0', '"suppressed_events":1')))

    def test_role_queue_replay_matches_every_surviving_task(self):
        memory = copy.deepcopy(self.memory)
        archive = memory['roles_archive']
        index = next(i for i in range(archive['head'], len(archive['queue']))
                     if archive['queue'][i]['cursor'] > 0)
        task = archive['queue'][index]
        encoded = json.dumps(archive['queue'], separators=(',', ':'))
        old = json.dumps(task, separators=(',', ':'))
        broken = encoded.replace(old, '"cursor":' + str(task['cursor']) + '}', 1)
        text = json.dumps(memory, separators=(',', ':')).replace(encoded, broken, 1)
        proposals = engine._zw_role_queue_bridge(text)
        self.assertEqual(len(proposals), 1)
        self.assertEqual(engine._zt_parse(proposals[0][0]), memory)
        self.assertEqual(proposals[0][1]['intact_tasks_checked'], len(archive['queue']) - 1)

    def test_saved_manifest_reexecutes_missing_record(self):
        memory = copy.deepcopy(self.memory)
        idx = next(r['id'] for r in memory['expressions']
                   if r.get('pathway') in engine._ZR_ARITHMETIC)
        expected = copy.deepcopy(memory['expressions'][idx])
        del memory['expressions'][idx]
        checked, ready, issues = engine._zw_validate(memory)
        self.assertTrue(ready, engine._zr_state(checked))
        self.assertFalse(issues)
        self.assertEqual(checked['expressions'][idx], expected)
        self.assertEqual(engine.archive_link_audit(checked)['issues'], 0)

    def test_pause_resume_and_source_fingerprint(self):
        text = '{"x":1,,"y":2}'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'memory.json'
            path.write_text(text, encoding='utf-8')
            with contextlib.redirect_stdout(io.StringIO()):
                first = engine._zw_recover(str(path), text, seconds=0)
                second = engine._zw_recover(str(path), text, seconds=0)
            self.assertEqual(first['frontier'], second['frontier'])
            self.assertEqual(first['status'], 'paused_by_requested_time')
            with self.assertRaises(engine.ZeroRecoveryPending):
                engine._zw_recover(str(path), text + ' ', seconds=0)
            self.assertEqual(path.read_text(encoding='utf-8'), text)

    def test_invalid_engine_candidate_is_blocked(self):
        for candidate in ({'x': 1}, [], None):
            with self.subTest(candidate=candidate):
                _, ready, issues = engine._zw_validate(candidate)
                self.assertFalse(ready)
                self.assertTrue(issues)


if __name__ == '__main__':
    unittest.main()
