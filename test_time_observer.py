"""Time is supplied observation; these tests never infer unobserved durations."""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('zero_time_engine', ROOT / 'zero_theoremV4.7.16.py')
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
WALL = 1700000000000000000


class TimeObserverTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = str(Path(self.temp.name) / e.MEMORY_FILENAME)
        e._ZT16_STACK.clear()
        e._ZT16_WARNED.clear()

    def read(self):
        return json.loads(Path(e._zt16_path(self.path)).read_text())

    def test_start_at_zero_and_exact_elapsed_cpu_observation(self):
        with patch.object(e, '_zt16_sample', side_effect=[(WALL, 100, 50), (WALL + 20, 130, 60)]):
            with e._zt16_span(self.path, 'example'):
                pass
        state = self.read()
        self.assertEqual(state['events'][0]['elapsed_ns'], 0)
        self.assertEqual(state['events'][1]['elapsed_ns'], 30)
        self.assertEqual(state['events'][1]['cpu_elapsed_ns'], 10)
        self.assertEqual(state['events'][0]['utc'], '2023-11-14T22:13:20.000000Z')
        self.assertTrue(all(event['zero_nexus'] == 'Z0' for event in state['events']))
        self.assertEqual(state['open_spans'], {})

    def test_wall_clock_correction_does_not_reverse_elapsed(self):
        with patch.object(e, '_zt16_sample', side_effect=[(WALL, 100, 50), (WALL - 5000000000, 2000000100, 70)]):
            with e._zt16_span(self.path, 'clock_change'):
                pass
        event = self.read()['events'][-1]
        self.assertEqual(event['elapsed_ns'], 2000000000)
        self.assertEqual(event['wall_elapsed_ns'], -5000000000)
        self.assertEqual(event['clock_delta_disagreement_ns'], -7000000000)

    def test_restart_links_events_without_subtracting_old_timer(self):
        with patch.object(e, '_ZT16_SESSION', 'process-one'), patch.object(e, '_zt16_sample', return_value=(WALL, 9000000, 500)):
            old = e.zero_core(None, 'time', operation='begin', operands=(self.path, 'work'))
        with patch.object(e, '_ZT16_SESSION', 'process-two'), patch.object(e, '_zt16_sample', side_effect=[(WALL + 9000, 1, 1), (WALL + 9010, 11, 4)]):
            token = e.zero_core(None, 'time', operation='begin', operands=(self.path, 'work'))
            event = e.zero_core(None, 'time', operation='end', operands=(token,))
        state = self.read()
        boundary = state['events'][1]
        self.assertEqual(boundary['kind'], 'session_boundary')
        self.assertIsNone(boundary['elapsed_ns'])
        self.assertEqual(boundary['prior_unfinished_spans'], [old['span']])
        self.assertEqual(boundary['wall_gap_ns'], 9000)
        self.assertEqual(state['events'][2]['elapsed_ns'], 0)
        self.assertEqual(event['elapsed_ns'], 10)
        self.assertEqual(state['totals']['work']['unfinished_after_restart'], 1)
        self.assertEqual([v['seq'] for v in state['events']], [1, 2, 3, 4])

    def test_event_order_remains_distinct_with_identical_clock_readings(self):
        with patch.object(e, '_zt16_sample', return_value=(WALL, 100, 50)):
            for _ in range(2):
                with e._zt16_span(self.path, 'same_tick'):
                    pass
        events = self.read()['events']
        self.assertEqual([v['seq'] for v in events], [1, 2, 3, 4])
        self.assertEqual([v['previous_event_seq'] for v in events], [None, 1, 2, 3])
        self.assertNotEqual(events[0]['span'], events[2]['span'])

    def test_interruption_records_known_duration_and_propagates(self):
        with self.assertRaises(KeyboardInterrupt):
            with e._zt16_span(self.path, 'interrupted'):
                raise KeyboardInterrupt()
        state = self.read()
        self.assertEqual(state['events'][-1]['outcome'], 'interrupted')
        self.assertGreaterEqual(state['events'][-1]['elapsed_ns'], 0)
        self.assertEqual(state['totals']['interrupted']['interrupted'], 1)
        self.assertFalse(e._ZT16_STACK)

    def test_nested_spans_record_parent_without_summing_as_total(self):
        with e._zt16_span(self.path, 'outer'):
            with e._zt16_span(self.path, 'inner'):
                pass
        state = self.read()
        self.assertEqual(state['events'][1]['parent_span'], state['events'][0]['span'])
        self.assertEqual(state['events'][1]['parent_observer'], e._zt16_path(self.path))
        self.assertIn('nested durations must not be added', state['totals_scope'])

    def test_observer_write_failure_does_not_block_work(self):
        result = []
        with patch.object(e, '_zn_checkpoint', side_effect=OSError('disposable simulated disk failure')), contextlib.redirect_stdout(io.StringIO()):
            with e._zt16_span(self.path, 'failure'):
                result.append(42)
        self.assertEqual(result, [42])
        self.assertFalse(e._ZT16_STACK)

    def test_invalid_observer_ledger_is_preserved(self):
        path = Path(e._zt16_path(self.path))
        raw = b'{"do_not_overwrite":true}'
        path.write_bytes(raw)
        with contextlib.redirect_stdout(io.StringIO()):
            with e._zt16_span(self.path, 'work'):
                answer = 7
        self.assertEqual(answer, 7)
        self.assertEqual(path.read_bytes(), raw)

    def test_disabled_observer_creates_no_file(self):
        with patch.object(e, 'TIME_OBSERVER_ENABLED', False):
            with e._zt16_span(self.path, 'disabled'):
                pass
        self.assertFalse(Path(e._zt16_path(self.path)).exists())

    def test_timer_token_cannot_finish_in_another_session(self):
        with patch.object(e, '_ZT16_SESSION', 'first'):
            token = e.zero_core(None, 'time', operation='begin', operands=(self.path, 'work'))
        with patch.object(e, '_ZT16_SESSION', 'second'), self.assertRaisesRegex(ValueError, 'different process'):
            e.zero_core(None, 'time', operation='end', operands=(token,))

    def normal_run(self, path, enabled=True):
        with patch.object(e, 'memory_path', return_value=str(path)), patch.object(e, 'TIME_OBSERVER_ENABLED', enabled), \
                patch('builtins.input', return_value=''), contextlib.redirect_stdout(io.StringIO()):
            e.run()
        return json.loads(path.read_text())

    def test_observation_preserves_math_records_queue_and_operation_counts(self):
        observed = Path(self.path)
        plain = observed.with_name('plain.json')
        yes = self.normal_run(observed)
        no = self.normal_run(plain, False)
        for domain in e._ZR_DOMAINS:
            self.assertEqual([e._zr_payload(r) for r in e._zr_records(yes, domain)],
                             [e._zr_payload(r) for r in e._zr_records(no, domain)], domain)
        self.assertEqual(yes['queue'], no['queue'])
        self.assertEqual(yes['queue_head'], no['queue_head'])
        self.assertEqual(yes['foundation'], no['foundation'])
        self.assertEqual(yes['archive_integration']['runtime_operations'], no['archive_integration']['runtime_operations'])
        self.assertNotIn('time_observer', yes)
        self.assertFalse(Path(e._zt16_path(str(plain))).exists())
        stages = self.read()['totals']
        for stage in ['load_memory', 'foundation_emergence', 'queue_exploration', 'roles_exploration',
                      'calculus_exploration', 'validate_and_save', 'process_including_queries']:
            self.assertIn(stage, stages)

    def test_adaptive_cycle_keeps_prefix_and_adds_time_events(self):
        path = Path(self.path)
        first = self.normal_run(path)
        before = len(self.read()['events'])
        memory, metric = e._zg_cycle(str(path))
        self.assertEqual(len(memory['runs']), len(first['runs']) + 1)
        self.assertTrue(metric['prefix_preserved'])
        state = self.read()
        self.assertGreater(len(state['events']), before)
        self.assertEqual(state['totals']['adaptive_cycle']['finished'], 1)

    def read_clock(self):
        return json.loads(Path(e._zt16_zero_path(self.path)).read_text())

    def space(self, memory, boundary='test_snapshot'):
        return e.zero_core(None, 'time', operation='space', operands=(self.path, memory, boundary))

    def seed_space(self):
        return {'foundation': {'states': [0]}, 'expressions': [{'id': 0}],
                'roles_archive': {'expressions': []}}

    def test_zero_clock_origin_keeps_existing_space_as_boundary(self):
        memory = self.seed_space()
        memory['expressions'].append({'id': 1})
        clock = self.space(memory)
        self.assertEqual(clock['tick'], 0)
        self.assertEqual(clock['origin'], 0)
        self.assertEqual(clock['zero_reference'], 'T0')
        self.assertEqual(clock['registered_states'], 1)
        self.assertEqual(clock['baseline_extent']['rational'], 2)
        self.assertTrue(all(v == 0 for v in clock['coordinates'].values()))
        self.assertEqual(self.read_clock()['events'][-1]['to'], 0)

    def test_zero_clock_transforms_its_own_states_with_space_growth(self):
        memory = self.seed_space()
        self.space(memory)
        memory['foundation']['states'].append(1)
        memory['expressions'].append({'id': 1})
        memory['roles_archive']['expressions'].append({'id': 0})
        clock = self.space(memory)
        self.assertEqual(clock['tick'], 3)
        self.assertEqual(clock['coordinates']['foundation'], 1)
        self.assertEqual(clock['coordinates']['rational'], 1)
        self.assertEqual(clock['coordinates']['roles'], 1)
        event = self.read_clock()['events'][-1]
        self.assertEqual(event['from'], 0)
        self.assertEqual(event['to'], 3)
        self.assertEqual(clock['registered_states'], 4)
        self.assertEqual(event['transformation'], 'count_registered_clock_states')
        self.assertTrue(all(v['zero_reference'] == 'T0' for v in self.read_clock()['events']))

    def test_zero_clock_does_not_tick_for_elapsed_time(self):
        memory = self.seed_space()
        self.space(memory)
        with patch.object(e, '_zt16_sample', side_effect=[(WALL, 10, 10), (WALL + 300000000000, 1000, 30)]):
            with e._zt16_span(self.path, 'waiting'):
                pass
        self.assertEqual(self.space(memory)['tick'], 0)

    def test_zero_clock_does_not_double_count_repeated_or_recovered_ids(self):
        memory = self.seed_space()
        self.space(memory)
        memory['expressions'].append({'id': 1})
        self.assertEqual(self.space(memory)['tick'], 1)
        self.assertEqual(self.space(memory)['tick'], 1)
        memory['expressions'].pop()
        contracted = self.space(memory)
        self.assertEqual(contracted['tick'], 1)
        self.assertEqual(contracted['current_extent']['rational'], 1)
        memory['expressions'].append({'id': 1})
        self.assertEqual(self.space(memory)['tick'], 1)
        memory['expressions'].append({'id': 2})
        self.assertEqual(self.space(memory)['tick'], 2)

    def test_zero_clock_survives_session_restart(self):
        memory = self.seed_space()
        with patch.object(e, '_ZT16_SESSION', 'old-observer'):
            with e._zt16_span(self.path, 'session'):
                self.space(memory)
                memory['expressions'].append({'id': 1})
                self.assertEqual(self.space(memory)['tick'], 1)
        with patch.object(e, '_ZT16_SESSION', 'new-observer'):
            with e._zt16_span(self.path, 'session'):
                clock = self.space(memory)
        self.assertEqual(clock['tick'], 1)
        self.assertEqual(len([v for v in self.read_clock()['events'] if v['kind'] == 'origin']), 1)

    def test_pending_slots_do_not_expand_zero_clock(self):
        memory = self.seed_space()
        self.space(memory)
        memory['expressions'].append({'id': 1, 'status': 'zero_recovery_pending'})
        self.assertEqual(self.space(memory)['tick'], 0)
        memory['expressions'][1].pop('status')
        self.assertEqual(self.space(memory)['tick'], 1)

    def test_failed_save_does_not_advance_zero_clock(self):
        memory = self.seed_space()
        self.space(memory)
        before = Path(e._zt16_zero_path(self.path)).read_bytes()
        memory['expressions'].append({'id': 1})
        with patch.object(e, 'memory_path', return_value=self.path), \
                patch.object(e, '_zt16_timed_save', side_effect=OSError('simulated math save failure')), \
                self.assertRaises(OSError):
            e.save_memory(memory)
        self.assertEqual(Path(e._zt16_zero_path(self.path)).read_bytes(), before)

    def test_saved_engine_clock_matches_committed_growth(self):
        self.normal_run(Path(self.path))
        clock = self.read_clock()
        self.assertGreater(clock['tick'], 0)
        expected = sum(clock['current_extent'][d] - clock['baseline_extent'][d] for d in clock['coordinates'])
        self.assertEqual(clock['tick'], expected)
        self.assertEqual(clock['tick'], sum(clock['coordinates'].values()))
        self.assertEqual(self.read_clock()['events'][-1]['kind'], 'expansion')

    def test_zero_clock_is_independent_of_wall_timer_and_role_grammar(self):
        memory = self.seed_space()
        with patch.object(e, 'TIME_OBSERVER_ENABLED', False), \
                patch.object(e, '_zt16_sample', side_effect=AssertionError('wall timer must not drive zero clock')), \
                patch.object(e, '_role_transition_exact', side_effect=AssertionError('role grammar must not drive zero clock')):
            self.assertEqual(self.space(memory)['tick'], 0)
            memory['expressions'].append({'id': 1})
            self.assertEqual(self.space(memory)['tick'], 1)
        self.assertTrue(Path(e._zt16_zero_path(self.path)).is_file())
        self.assertFalse(Path(e._zt16_path(self.path)).exists())

    def test_time_query_reads_observations_without_changing_memory(self):
        memory = e.empty_memory()
        before = copy.deepcopy(memory)
        with e._zt16_span(self.path, 'sample'):
            pass
        raw = Path(e._zt16_path(self.path)).read_bytes()
        with patch.object(e, 'memory_path', return_value=self.path), contextlib.redirect_stdout(io.StringIO()):
            e.query(memory, 'time')
        self.assertEqual(memory, before)
        self.assertEqual(Path(e._zt16_path(self.path)).read_bytes(), raw)


    def test_interactive_clock_commands_precede_complex_parser(self):
        memory = e.empty_memory()
        for command in ('time', 'time-report', 'zero-clock', 'zero-time'):
            handler = 'print_time_report' if command.startswith('time') else 'print_zero_clock_report'
            with self.subTest(command=command), patch.object(e, handler) as report, \
                    patch.object(e, 'parse_complex_query', side_effect=AssertionError('clock reached complex parser')), \
                    patch.object(e, 'memory_path', return_value=self.path):
                for early in (e.query_roles, e.query_calculus, e.query_symbolic):
                    self.assertFalse(early(memory, command))
                self.assertTrue(e.query_v45(memory, command))
                report.assert_called_once_with(self.path)


if __name__ == '__main__':
    unittest.main()
