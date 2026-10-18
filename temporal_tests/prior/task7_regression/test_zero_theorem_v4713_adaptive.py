import builtins
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

spec=importlib.util.spec_from_file_location('engine4710',(Path(__file__).resolve().parents[1]/'zero_theoremV4.7.15.py'))
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
FIXTURE=Path(__file__).parent/'task2_source/zero_theorem_rabbitholes_v41_memory.json.zero-body-candidate.json'

class AdaptiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.master=json.loads(FIXTURE.read_text())
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.source=Path(self.tmp.name)/'source.json'
        self.baseline=Path(self.tmp.name)/'baseline.json'
        self.memory=copy.deepcopy(self.master)
        self.source.write_text(json.dumps(self.memory));self.baseline.write_bytes(self.source.read_bytes())
    def write(self):self.source.write_text(json.dumps(self.memory))
    def adaptive(self,baseline=False,**kwargs):
        with contextlib.redirect_stdout(io.StringIO()),patch.object(builtins,'input',side_effect=AssertionError('trial requested input')):
            return e.zero_adaptive_recovery(str(self.source),str(self.baseline) if baseline else None,**kwargs)
    def damage(self):
        self.memory['expressions']=self.memory['expressions'][:4]
        self.write()
    def test_real_trials_preserve_inputs_and_validate_continuation(self):
        original=self.source.read_bytes();baseline=self.baseline.read_bytes()
        report=self.adaptive(baseline=True)
        self.assertEqual(report['status'],'selected_and_resumed')
        self.assertEqual(report['selected_branch'],'recovery')
        self.assertEqual(report['lost_fraction'],0)
        self.assertEqual(self.source.read_bytes(),original);self.assertEqual(self.baseline.read_bytes(),baseline)
        for name,branch in report['trials'].items():
            self.assertEqual(branch['status'],'ready')
            self.assertTrue(branch['continuation_verified'])
            self.assertGreater(branch['elapsed_seconds'],0)
            self.assertGreaterEqual(branch['records'],report['target_records'])
            memory=e._zg_check(branch['memory_path'])
            self.assertGreater(len(memory['runs']),branch['goal_boundary_run'])
            self.assertTrue(all(c['prefix_preserved'] for c in branch['cycles']))
    def test_heavy_loss_regenerates_without_using_baseline_as_evidence(self):
        self.damage();original=self.source.read_bytes();baseline=self.baseline.read_bytes()
        report=self.adaptive(baseline=True)
        self.assertGreaterEqual(report['lost_fraction'],0.5)
        self.assertEqual(report['selected_branch'],'regeneration')
        self.assertTrue(report['new_lineage']);self.assertFalse(report['historical_identity_proven'])
        self.assertTrue(Path(report['trials']['recovery']['preflight_proposal']).exists())
        self.assertGreater(report['trials']['recovery']['reconstructed_records'],0)
        memory=e._zg_check(report['active_memory'])
        self.assertEqual(memory['zero_adaptive_lineage']['history_status'],'new_emergence_from_Z0')
        self.assertFalse(memory['zero_adaptive_lineage']['baseline_used_as_repair_evidence'])
        self.assertEqual(self.source.read_bytes(),original);self.assertEqual(self.baseline.read_bytes(),baseline)
    def test_no_baseline_does_not_invent_loss_percentage(self):
        self.damage();report=self.adaptive()
        self.assertIsNone(report['lost_fraction']);self.assertIsNone(report['missing_unique_constructions'])
        self.assertEqual(report['selected_branch'],'regeneration')
    def test_feedback_recovery_processes_multiple_chunks_automatically(self):
        changed=0
        for rec in self.memory['expressions']:
            if rec['pathway'] in e._ZR_ARITHMETIC:
                rec['value']='123456'
                changed+=1
        self.assertGreater(changed,32)
        self.write();report=self.adaptive(recovery_seconds=10)
        self.assertEqual(report['trials']['recovery']['status'],'ready')
        self.assertGreater(report['trials']['recovery']['verification_feedback_executed'],32)

    def test_uncertain_foundation_does_not_seed_regeneration(self):
        self.memory['foundation']['states']=[999];self.write()
        report=self.adaptive(target_records=8)
        self.assertEqual(report['selected_branch'],'regeneration')
        memory=e._zg_check(report['active_memory'])
        self.assertEqual(memory['foundation']['states'][:4],[0,1,2,3])
        self.assertNotIn(999,memory['foundation']['states'])
    def test_unreadable_text_retained_while_new_lineage_runs(self):
        raw=b'not-json\xff';self.source.write_bytes(raw)
        report=self.adaptive(target_records=8)
        self.assertEqual(report['selected_branch'],'regeneration')
        self.assertEqual(self.source.read_bytes(),raw)
        self.assertEqual(Path(report['source_snapshot']).read_bytes(),raw)
    def test_cycle_budget_checkpoints_and_next_call_continues(self):
        first=self.adaptive(target_records=132,max_cycles=1)
        self.assertEqual(first['trials']['regeneration']['status'],'budget_checkpoint')
        second=self.adaptive(target_records=132,max_cycles=1)
        self.assertEqual(second['trials']['regeneration']['status'],'ready')
        self.assertEqual(len(second['trials']['regeneration']['cycles']),2)
    def test_both_pending_does_not_activate_any_branch(self):
        report=self.adaptive(target_records=10000,max_cycles=1)
        self.assertEqual(report['status'],'pending');self.assertIsNone(report['selected_branch'])
        self.assertFalse(Path(str(self.source)+'.adaptive-active.json').exists())
    def test_interruption_saves_trial_state_and_resumes(self):
        original=e._zg_cycle
        def interrupt(path):original(path);raise KeyboardInterrupt()
        with patch.object(e,'_zg_cycle',interrupt):report=self.adaptive(target_records=132,max_cycles=1)
        self.assertEqual(report['status'],'interrupted_checkpoint_saved')
        self.assertTrue(Path(report['source_snapshot']).exists())
        continued=self.adaptive(target_records=132,max_cycles=2)
        self.assertEqual(continued['status'],'selected_and_resumed')
    def test_regeneration_begins_with_one_zero_and_no_source_metadata(self):
        self.memory['do_not_copy']='private-original-history';self.write()
        seeds=[];original=e.empty_memory
        def seed():
            result=original();seeds.append(copy.deepcopy(result));return result
        with patch.object(e,'empty_memory',seed):report=self.adaptive(target_records=8)
        self.assertTrue(seeds)
        for item in seeds:
            self.assertEqual(item['foundation']['states'],[0]);self.assertEqual(len(item['expressions']),1)
        generated=e._zg_check(report['trials']['regeneration']['memory_path'])
        self.assertNotIn('do_not_copy',generated)
    def test_failed_rule_check_stops_before_any_work_is_written(self):
        original=e._operate_rational_exact
        with patch.object(e,'_operate_rational_exact',lambda a,op,b:e.Fraction(999)):
            with self.assertRaises(e.ZeroRecoveryPending):self.adaptive()
        self.assertFalse(Path(str(self.source)+'.adaptive-work').exists())
    def test_input_change_prevents_activation(self):
        original=e._zg_cycle
        def change(path):
            result=original(path);self.source.write_bytes(b'changed externally');return result
        with patch.object(e,'_zg_cycle',change),self.assertRaisesRegex(e.ZeroRecoveryPending,'Source changed'):
            self.adaptive(target_records=8)
        self.assertFalse(Path(str(self.source)+'.adaptive-active.json').exists())
    def test_active_regeneration_branch_continues_on_normal_run(self):
        self.damage();original=self.source.read_bytes();report=self.adaptive(target_records=8)
        before=e._zg_check(report['active_memory'])
        old=e.memory_path;e.memory_path=lambda:str(self.source)
        try:
            with contextlib.redirect_stdout(io.StringIO()),patch.object(builtins,'input',return_value=''):
                e.run()
        finally:e.memory_path=old
        after=e._zg_check(report['active_memory'])
        self.assertGreater(len(after['runs']),len(before['runs']))
        self.assertEqual(self.source.read_bytes(),original)
    def test_default_phone_run_handles_damage_without_terminal_arguments(self):
        self.damage();original=self.source.read_bytes();old=e.memory_path;e.memory_path=lambda:str(self.source)
        try:
            with contextlib.redirect_stdout(io.StringIO()),patch.object(builtins,'input',side_effect=AssertionError('unexpected query')):
                report=e.run()
        finally:e.memory_path=old
        self.assertEqual(report['selected_branch'],'regeneration')
        self.assertEqual(self.source.read_bytes(),original)
    def test_non_rational_damage_also_enters_adaptive_workflow(self):
        self.memory['complex_archive']['expressions'][2]['value']='damaged'
        self.write();original=self.source.read_bytes()
        old=e.memory_path;e.memory_path=lambda:str(self.source)
        try:
            with contextlib.redirect_stdout(io.StringIO()),patch.object(builtins,'input',return_value=''):
                report=e.run()
        finally:e.memory_path=old
        self.assertEqual(report['selected_branch'],'regeneration')
        self.assertEqual(self.source.read_bytes(),original)

    def test_saved_baseline_is_reused_on_continuation(self):
        first=self.adaptive(baseline=True,target_records=132,max_cycles=1)
        second=self.adaptive(target_records=132,max_cycles=1)
        self.assertEqual(first['baseline_sha256'],second['baseline_sha256'])
        self.assertEqual(second['trials']['regeneration']['status'],'ready')

    def test_wrong_baseline_stops_without_modifying_input(self):
        self.baseline.write_text('{"schema":999}')
        original=self.source.read_bytes()
        with self.assertRaises((ValueError,KeyError,TypeError)):self.adaptive(baseline=True)
        self.assertEqual(self.source.read_bytes(),original)
    def test_same_file_baseline_rejected(self):
        with self.assertRaisesRegex(ValueError,'Baseline must differ'):
            e.zero_adaptive_recovery(str(self.source),str(self.source))
    def test_selection_uses_measured_cost_only_at_loss_checkpoint(self):
        trials={'recovery':{'status':'ready','elapsed_seconds':10},'regeneration':{'status':'ready','elapsed_seconds':1}}
        self.assertEqual(e.zero_core(None,'adaptive',operation='select',operands=(trials,0.6))[0],'regeneration')
        self.assertEqual(e.zero_core(None,'adaptive',operation='select',operands=(trials,0.1))[0],'recovery')
        self.assertEqual(e.zero_core(None,'adaptive',operation='select',operands=(trials,None))[0],'recovery')
    def test_regeneration_cost_margin_avoids_near_tie_switch(self):
        trials={'recovery':{'status':'ready','elapsed_seconds':10},'regeneration':{'status':'ready','elapsed_seconds':9}}
        self.assertEqual(e._zg_select(trials,0.9)[0],'recovery')
    def test_stale_active_pointer_does_not_bind_changed_source(self):
        self.damage();first=self.adaptive(target_records=8)
        self.memory=copy.deepcopy(self.master);self.write()
        before=len(self.memory['runs']);old=e.memory_path;e.memory_path=lambda:str(self.source)
        try:
            with contextlib.redirect_stdout(io.StringIO()),patch.object(builtins,'input',return_value=''):e.run()
        finally:e.memory_path=old
        after=e._zg_check(str(self.source));self.assertGreater(len(after['runs']),before)
        self.assertEqual(len(e._zg_check(first['active_memory'])['runs']),first['trials']['regeneration']['saved_runs'])

if __name__=='__main__':unittest.main()
