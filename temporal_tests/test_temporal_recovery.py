"""Integration checks use disposable normal engine runs and actual clock samples."""
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
spec = importlib.util.spec_from_file_location('temporal_integrated', ROOT/'zero_theoremV4.7.17.py')
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)


class TemporalRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.path = Path(cls.temp.name)/e.MEMORY_FILENAME
        with patch.object(e,'memory_path',return_value=str(cls.path)), patch('builtins.input',return_value=''), contextlib.redirect_stdout(io.StringIO()):
            e.run()
        cls.memory = json.loads(cls.path.read_text())
        cls.ledger = json.loads(Path(e._zt17_path(str(cls.path))).read_text())

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)/'damaged.temporal.json'

    def recover(self,state,seq,field):
        self.path.write_text(json.dumps(state))
        before = self.path.read_bytes()
        math_before = self.__class__.path.read_bytes()
        with contextlib.redirect_stdout(io.StringIO()):
            result = e.zero_core(None,'temporal',operation='recover',operands=(str(self.path),seq,field))
        self.assertEqual(self.path.read_bytes(),before)
        self.assertEqual(self.__class__.path.read_bytes(),math_before)
        return result

    def test_recorded_acceptances_bind_to_saved_records_and_actual_uses(self):
        self.assertGreater(len(self.ledger['events']),100)
        self.assertTrue(any(row['uses'] for row in self.ledger['events']))
        for row in self.ledger['events']:
            ref=row['record']
            record=e._zr_records(self.memory,ref['archive'])[ref['id']]
            self.assertEqual(row['record_digest'],e._zr_digest(e._zr_payload(record)))
        self.assertEqual(self.ledger['batches'][-1]['memory_sha256'],e._z7_hash_file(self.__class__.path))

    def test_mask_actual_clock_samples_and_compare_held_out_original(self):
        for seq in (1,len(self.ledger['events'])//2,len(self.ledger['events'])):
            for field in ('wall_ns','monotonic_ns','process_cpu_ns'):
                with self.subTest(seq=seq,field=field):
                    state=copy.deepcopy(self.ledger)
                    original=state['events'][seq-1].pop(field)
                    # Distinct temporary paths prevent candidate collisions.
                    self.path=Path(self.temp.name)/('mask-'+str(seq)+'-'+field+'.json')
                    result=self.recover(state,seq,field)
                    self.assertEqual(result['status'],'exact_supported')
                    self.assertEqual(result['accepted_timestamp'],original)
                    candidate=json.loads(Path(result['candidate']).read_text())
                    self.assertEqual(candidate,self.ledger)
                    self.assertFalse(result['historical_identity_proven'])

    def test_unanchored_single_observation_stays_unresolved(self):
        state=copy.deepcopy(self.ledger)
        state['events']=state['events'][:1]
        state['events'][0].pop('monotonic_ns')
        state['next_seq']=2
        state['batches']=state['batches'][:1]
        state['batches'][0]['to_seq']=1
        result=self.recover(state,1,'monotonic_ns')
        self.assertEqual(result['status'],'unresolved')
        self.assertNotIn('candidate',result)

    def test_kept_timestamps_but_missing_durations_produce_unresolved_range(self):
        state=copy.deepcopy(self.ledger)
        state['events'][1].pop('monotonic_ns')
        state['events'][1]['delta_from_previous']=None
        state['events'][2]['delta_from_previous']=None
        result=self.recover(state,2,'monotonic_ns')
        self.assertEqual(result['status'],'unresolved')
        final=result['inference']['trace'][-1]
        self.assertIsNotNone(final['lower']);self.assertIsNotNone(final['upper'])
        self.assertLess(final['lower'],final['upper'])
        self.assertNotIn('candidate',result)

    def test_normal_load_proposes_recovery_without_promoting_damaged_ledger(self):
        memory_path=Path(self.temp.name)/'memory.json'
        memory_path.write_bytes(self.__class__.path.read_bytes())
        state=copy.deepcopy(self.ledger);state['memory_path']=str(memory_path)
        original=state['events'][1].pop('monotonic_ns')
        temporal=Path(e._zt17_path(str(memory_path)));temporal.write_text(json.dumps(state))
        before=temporal.read_bytes()
        with patch.object(e,'memory_path',return_value=str(memory_path)),contextlib.redirect_stdout(io.StringIO()):
            loaded=e.load_memory()
        self.assertEqual(temporal.read_bytes(),before)
        candidate=json.loads(Path(str(temporal)+'.time-candidate.json').read_text())
        self.assertEqual(candidate['events'][1]['monotonic_ns'],original)
        self.assertNotIn(id(loaded),e._ZT17_CONTEXTS)

    def test_conflicting_difference_rejected_without_source_change(self):
        state=copy.deepcopy(self.ledger)
        state['events'][1].pop('monotonic_ns')
        state['events'][1]['delta_from_previous']['monotonic_ns']+=1
        self.path.write_text(json.dumps(state));before=self.path.read_bytes()
        with contextlib.redirect_stdout(io.StringIO()):
            result=e.zero_core(None,'temporal',operation='recover',operands=(str(self.path),2,'monotonic_ns'))
        self.assertEqual(result['status'],'contradiction')
        self.assertEqual(self.path.read_bytes(),before)
        self.assertFalse(Path(str(self.path)+'.time-candidate.json').exists())

    def test_present_timestamp_is_not_used_as_a_recovery_target(self):
        self.path.write_text(json.dumps(self.ledger));before=self.path.read_bytes()
        with self.assertRaisesRegex(ValueError,'present'):
            e.zero_core(None,'temporal',operation='recover',operands=(str(self.path),2,'wall_ns'))
        self.assertEqual(self.path.read_bytes(),before)

    def test_other_candidate_never_overwritten(self):
        state=copy.deepcopy(self.ledger);state['events'][1].pop('monotonic_ns')
        candidate=Path(str(self.path)+'.time-candidate.json');candidate.write_text('{"retained":true}')
        with self.assertRaisesRegex(ValueError,'already exists'):
            self.recover(state,2,'monotonic_ns')
        self.assertEqual(candidate.read_text(),'{"retained":true}')

    def test_real_recorded_clock_rollback_is_allowed(self):
        state=copy.deepcopy(self.ledger)
        # A wall correction is signed; duration evidence remains internally exact.
        for row in state['events'][1:]: row['wall_ns']-=10**15
        state['events'][1]['delta_from_previous']['wall_ns']-=10**15
        e._zt17_validate_records(state)
        original=state['events'][1].pop('wall_ns')
        result=self.recover(state,2,'wall_ns')
        self.assertEqual(result['accepted_timestamp'],original)

    def test_cross_session_delta_is_not_invented(self):
        state=copy.deepcopy(self.ledger)
        state['events']=state['events'][:1]
        state['next_seq']=2;state['batches']=state['batches'][:1];state['batches'][0]['to_seq']=1
        state['events'][0]['session']='new-session'
        state['events'][0]['delta_from_previous']=None
        state['events'][0].pop('wall_ns')
        result=self.recover(state,1,'wall_ns')
        self.assertEqual(result['status'],'unresolved')

    def test_worker_reenters_actual_shared_zero_gateway(self):
        state=copy.deepcopy(self.ledger);state['events'][1].pop('monotonic_ns')
        with patch.object(e,'zero_core',wraps=e.zero_core) as gateway:
            result=self.recover(state,2,'monotonic_ns')
        operations=[call.kwargs.get('operation') for call in gateway.call_args_list]
        self.assertIn('recover',operations);self.assertIn('explore',operations);self.assertIn('infer',operations)
        self.assertEqual(result['status'],'exact_supported')

    def test_loaded_rule_signature_ignores_launcher_file(self):
        before=e._z7_rules_signature()
        launcher=Path(self.temp.name)/'launcher.py';launcher.write_text('first')
        with patch.object(e,'__file__',str(launcher)):
            self.assertEqual(e._z7_rules_signature(),before)
            launcher.write_text('second')
            self.assertEqual(e._z7_rules_signature(),before)
        with patch.object(e,'MAX_DEPTH',e.MAX_DEPTH+1):
            self.assertNotEqual(e._z7_rules_signature(),before)

    def test_loaded_function_change_refreshes_signature(self):
        source=(ROOT/'zero_theoremV4.7.17.py').read_text()
        before={'__name__':'identity_probe','__file__':'unchanged-launcher.py'}
        after={'__name__':'identity_probe','__file__':'unchanged-launcher.py'}
        exec(compile(source,'<engine>','exec'),before)
        exec(compile(source.replace("'Invalid temporal integer'","'Revised temporal integer rule'",1),'<engine>','exec'),after)
        self.assertNotEqual(before['_z7_rules_signature'](),after['_z7_rules_signature']())

    def test_new_boundary_does_not_invent_old_creation_times(self):
        with patch.object(e,'memory_path',return_value=str(self.__class__.path)),contextlib.redirect_stdout(io.StringIO()):
            memory=e.load_memory()
        context=e._ZT17_CONTEXTS.pop(id(memory))
        self.assertEqual(context['new'],[])

    def test_recording_cap_marks_gap_and_preserves_mathematical_work(self):
        path=Path(self.temp.name)/'capped.json'
        with patch.object(e,'memory_path',return_value=str(path)),patch.object(e,'TEMPORAL_MAX_EVENTS_PER_RUN',2),patch('builtins.input',return_value=''),contextlib.redirect_stdout(io.StringIO()):e.run()
        state=e._zt17_validate_records(json.loads(Path(e._zt17_path(str(path))).read_text()))
        self.assertEqual(len(state['events']),2)
        self.assertEqual(state['gaps'][-1]['reason'],'observation work cap')
        self.assertGreater(len(json.loads(path.read_text())['expressions']),2)

    def test_disabled_temporal_observation_has_identical_math(self):
        path=Path(self.temp.name)/'unobserved.json'
        with patch.object(e,'memory_path',return_value=str(path)),patch.object(e,'TEMPORAL_RECORDING_ENABLED',False),patch('builtins.input',return_value=''),contextlib.redirect_stdout(io.StringIO()):e.run()
        plain=json.loads(path.read_text())
        for domain in e._ZR_DOMAINS:
            self.assertEqual([e._zr_payload(r) for r in e._zr_records(plain,domain)],
                             [e._zr_payload(r) for r in e._zr_records(self.memory,domain)])
        self.assertEqual(plain['queue'],self.memory['queue'])
        self.assertEqual(plain['zero_core'],self.memory['zero_core'])
        self.assertFalse(Path(e._zt17_path(str(path))).exists())

    def test_process_sequence_corruption_rejected_by_report(self):
        memory=str(Path(self.temp.name)/'clock-memory.json')
        with e._zt16_span(memory,'probe'):pass
        name=Path(e._zt16_path(memory));state=json.loads(name.read_text())
        state['events'][0]['seq']=999;name.write_text(json.dumps(state));before=name.read_bytes()
        with self.assertRaises(ValueError):e.print_time_report(memory)
        self.assertEqual(name.read_bytes(),before)

    def test_process_totals_corruption_rejected(self):
        memory=str(Path(self.temp.name)/'clock-memory.json')
        with e._zt16_span(memory,'probe'):pass
        state=json.loads(Path(e._zt16_path(memory)).read_text())
        state['totals']['probe']['observed_elapsed_ns']+=1
        with self.assertRaises(ValueError):e._zt17_validate_observer(state)

    def test_negative_zero_clock_rejected_by_update_and_report(self):
        memory=str(Path(self.temp.name)/'clock-memory.json')
        e.zero_core(None,'time',operation='space',operands=(memory,e.empty_memory(),'test'))
        name=Path(e._zt16_zero_path(memory));state=json.loads(name.read_text())
        state['tick']=-1;state['registered_states']=0;state['coordinates']['rational']=-1
        name.write_text(json.dumps(state));before=name.read_bytes()
        with self.assertRaises(ValueError):e.print_zero_clock_report(memory)
        with self.assertRaises(ValueError):e.zero_core(None,'time',operation='space',operands=(memory,e.empty_memory(),'test'))
        self.assertEqual(name.read_bytes(),before)


if __name__=='__main__':unittest.main(verbosity=2)
