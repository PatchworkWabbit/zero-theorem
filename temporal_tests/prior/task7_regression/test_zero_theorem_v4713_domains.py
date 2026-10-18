"""Task 5: independent replay, typed bridges and non-destructive rejection."""
import contextlib
import copy
from fractions import Fraction
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('task5_engine',ROOT.parent/'zero_theoremV4.7.15.py')
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)

class DomainReplayTests(unittest.TestCase):
    def setUp(self):
        self.m=json.loads((ROOT/'task4_fixture/baseline.json').read_text())
        e.upgrade_v45(self.m)
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.path=Path(self.tmp.name)/'memory.json'
    def write(self):
        clean={k:v for k,v in self.m.items() if not k.startswith('_')}
        self.path.write_text(json.dumps(clean))
    def refresh(self):
        # Deliberately make the digest agree: replay must find the mathematical fault.
        for d in e._ZR_DOMAINS:
            for r in e._zr_records(self.m,d):
                self.m['zero_recovery']['manifest'][d][str(r['id'])]=e._zr_manifest_entry(d,r)
    def observe(self):return e.zero_core(self.m,'verification',operation='observe')
    def rejected(self,domain):
        r=self.observe()
        self.assertTrue(any(f.get('archive')==domain for f in r['contradictions']),r['contradictions'])
        self.write();before=self.path.read_bytes()
        with self.assertRaises(e.ZeroRecoveryPending):e._zg_check(str(self.path))
        self.assertEqual(self.path.read_bytes(),before)
    def calc_chain(self,start='7'):
        rid=next(r['id'] for r in self.m['expressions'] if r['value']==start)
        idx=e.calculus_record(self.m,[start],'constant_import',sources=[{'archive':'rational','id':rid}])
        variable=self.m['roles_archive']['variable_refs'][0]
        for depth,op in enumerate(['multiply_x','multiply_x','differentiate','differentiate'],1):
            coeff,reason=e.zero_core(self.m,'calculus',operation=op,operands=(self.m['calculus_archive']['expressions'][idx]['coefficients'],variable))
            self.assertIsNone(reason)
            idx=e.calculus_record(self.m,coeff,op,parents=[idx],sources=[{'archive':'roles','id':variable}],depth=depth)
        return idx
    def test_frozen_baseline_all_five_domains_pass_read_only(self):
        before=copy.deepcopy(self.m);r=self.observe()
        self.assertFalse(r['contradictions']);self.assertEqual(self.m,before)
        self.assertEqual(r['typed_replay']['records_checked'],{'rational':296,'complex':126,'symbolic':88,'calculus':20,'roles':24})
    def test_replay_does_not_call_exploration_kernels(self):
        names=['operate','evaluate_tree','_operate_rational_exact','_complex_operate_exact','_symbolic_apply_exact','_calculus_apply_exact','_role_transition_exact']
        with contextlib.ExitStack() as stack:
            for name in names:stack.enter_context(patch.object(e,name,side_effect=AssertionError(name)))
            self.assertFalse(e._Z5Replay(self.m).report()['contradictions'])
    def test_all_complex_binary_operations_checked_with_matching_digest(self):
        baseline=copy.deepcopy(self.m)
        for op in ['+','-','*','/']:
            with self.subTest(op=op):
                self.m=copy.deepcopy(baseline)
                rec=next(r for r in self.m['complex_archive']['expressions'] if r['operation']==op)
                rec['real']=str(Fraction(rec['real'])+123);rec['value']=e.complex_key(Fraction(rec['real']),Fraction(rec['imaginary']))
                self.refresh();self.rejected('complex')
    def test_wrong_complex_constructor_rejected(self):
        p=[125,0];rs=self.m['complex_archive']['expressions']
        idx=e.complex_record(self.m,(Fraction(123),Fraction(0)),'('+rs[125]['expr']+' + '+rs[0]['expr']+')',p,'+','complex_arithmetic_v44')
        self.assertIsNotNone(idx);self.rejected('complex')
    def test_complex_seed_is_not_an_arbitrary_value(self):
        self.m['complex_archive']['expressions'][0]['real']='1';self.refresh();self.rejected('complex')
    def test_symbolic_wrong_standalone_value_rejected(self):
        r=self.m['symbolic_archive']['expressions'][15]
        r['exact']={'q':['0','1']};r['value']='0';self.refresh();self.rejected('symbolic')
    def test_symbolic_matching_value_and_tree_still_requires_parents(self):
        r=self.m['symbolic_archive']['expressions'][15]
        r['exact']={'q':['0','1']};r['value']='0';r['construction']={'exact':r['exact']}
        self.refresh();self.rejected('symbolic')
    def test_symbolic_import_cannot_replace_source_construction(self):
        r=next(r for r in self.m['symbolic_archive']['expressions'] if r['pathway']=='numeric_to_symbolic_v464' and 'op' in r['construction'])
        r['construction']={'exact':r['exact']};self.refresh();self.rejected('symbolic')
    def test_symbolic_nexus_must_replace_an_actual_zero_slot(self):
        r=next(r for r in self.m['symbolic_archive']['expressions'] if r['pathway']=='zero_nexus_symbolic_v461')
        r['nexus']['zero_slot_path']=[99];self.refresh();self.rejected('symbolic')
    def test_all_calculus_operations_checked_with_matching_digest(self):
        baseline=copy.deepcopy(self.m)
        for op in e.CALCULUS_OPERATIONS:
            with self.subTest(op=op):
                self.m=copy.deepcopy(baseline)
                r=next(r for r in self.m['calculus_archive']['expressions'] if r['operation']==op)
                r['coefficients']=['1'];r['value']=r['expr']='1';r['proof']['output_coefficients']=['1']
                self.refresh();self.rejected('calculus')
    def test_wrong_calculus_constructor_rejected(self):
        var=self.m['roles_archive']['variable_refs'][0]
        parent=next(r['id'] for r in self.m['calculus_archive']['expressions'] if r['operation']=='constant_import' and r['coefficients']==['1'])
        idx=e.calculus_record(self.m,['1'],'differentiate',parents=[parent],sources=[{'archive':'roles','id':var}],depth=1)
        self.assertIsNotNone(idx);self.rejected('calculus')
    def test_calculus_constant_import_checks_its_rational_source(self):
        r=self.m['calculus_archive']['expressions'][0];r['coefficients']=['1'];r['value']=r['expr']='1'
        self.refresh();self.rejected('calculus')
    def test_new_integer_bridge_accepted_and_saved_continuation(self):
        idx=self.calc_chain();bridge=self.m['expressions'][-1]
        self.assertEqual(bridge['value'],'14');self.assertEqual(bridge['tree'],{'leaf':14,'calculus_source':idx})
        self.assertFalse(self.observe()['contradictions'])
        self.write();before=copy.deepcopy(bridge)
        with contextlib.redirect_stdout(io.StringIO()):memory,metrics=e._zg_cycle(str(self.path))
        self.assertTrue(metrics['prefix_preserved']);self.assertEqual(memory['expressions'][before['id']],before)
    def test_new_fractional_bridge_accepted(self):
        # 5/6 is archived in the fixture? Select an available fraction with a new double.
        start=next(q for q in self.m['results'] if Fraction(q).denominator>1 and str(2*Fraction(q)) not in self.m['results'])
        idx=self.calc_chain(start)
        self.assertEqual(self.m['expressions'][-1]['value'],str(2*Fraction(start)))
        self.assertEqual(self.m['expressions'][-1]['tree']['calculus_source'],idx)
        self.assertFalse(self.observe()['contradictions'])
    def test_bridge_operand_can_participate_in_rational_feedback(self):
        self.calc_chain();idx=len(self.m['expressions'])-1
        e.combine(self.m,idx,1,'+','reuse_v1',{'new':0,'observer_added':0})
        self.assertEqual(self.m['expressions'][-1]['value'],'15');self.assertFalse(self.observe()['contradictions'])
    def test_bridge_wrong_source_rejected(self):
        self.calc_chain();self.m['expressions'][-1]['tree']['calculus_source']=0
        self.refresh();self.rejected('rational')
    def test_cross_domain_cycle_rejected(self):
        self.calc_chain();bridge=self.m['expressions'][-1]
        first=next(r for r in self.m['calculus_archive']['expressions'] if r['coefficients']==['7'] and r['operation']=='constant_import')
        first['sources']=[{'archive':'rational','id':bridge['id']}]
        self.refresh();self.assertTrue(self.observe()['typed_replay']['contradictions'])
    def test_named_role_must_preserve_payload(self):
        self.m['roles_archive']['expressions'][1]['body']={'kind':'numeric','value':'1'}
        self.refresh();self.rejected('roles')
    def test_variable_origin_cannot_be_disguised(self):
        var=self.m['roles_archive']['variable_refs'][0]
        self.m['roles_archive']['expressions'][var]['body']={'kind':'numeric','value':'0'}
        self.refresh();self.rejected('roles')
    def test_typed_feedback_never_overwrites_same_number_rational_id(self):
        rec=self.m['complex_archive']['expressions'][6];rec['real']='123';self.refresh()
        before=copy.deepcopy(self.m['expressions']);self.write()
        with contextlib.redirect_stdout(io.StringIO()):report=e.zero_verify_candidate(str(self.path),budget=2)
        state=json.loads(Path(str(self.path)+'.zero-verification-search.json').read_text())
        self.assertEqual(state['working_memory']['expressions'],before)
        typed=[t for t in report['zero_feedback'] if t.get('archive')=='complex']
        self.assertTrue(typed);self.assertTrue(all(t['status']=='unresolved' for t in typed[:2]))
    def test_normal_save_blocks_bad_record_and_preserves_active_file(self):
        self.write();before=self.path.read_bytes()
        rs=self.m['complex_archive']['expressions']
        e.complex_record(self.m,(Fraction(123),Fraction(0)),'('+rs[125]['expr']+' + '+rs[0]['expr']+')',[125,0],'+','complex_arithmetic_v44')
        with patch.object(e,'memory_path',return_value=str(self.path)),contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(e.ZeroRecoveryPending):e.save_memory(self.m)
        self.assertEqual(self.path.read_bytes(),before)
        self.assertTrue(Path(str(self.path)+'.zero-verification-run-proposal.json.verification.json').exists())
    def test_symbolic_replay_excessive_power_is_unresolved_before_computing(self):
        with self.assertRaisesRegex(ValueError,'replay_resource_limit'):
            e._Z5Replay(self.m).symtree({'op':'**','args':[{'exact':{'q':['2','1']}},{'exact':{'q':['999999999999','1']}}]})
    def test_legacy_calculus_boundary_is_explicit(self):
        r=self.m['calculus_archive']['expressions'][2]
        for key in ['variable_source','variable','input_interpretation']:r.pop(key,None)
        r['sources']=[];self.m['calculus_archive']['role_origin_boundary']=3;self.refresh()
        report=e._Z5Replay(self.m).report()
        self.assertFalse(report['contradictions']);self.assertIn(2,report['legacy_calculus_without_variable_origin'])
    def test_legacy_plain_leaf_bridge_and_descendant_remain_valid(self):
        self.calc_chain();bridge=self.m['expressions'][-1]
        bridge['tree'].pop('calculus_source')
        e.combine(self.m,bridge['id'],1,'+','reuse_v1',{'new':0,'observer_added':0})
        self.refresh();self.assertFalse(self.observe()['contradictions'])
        self.write();e._zg_check(str(self.path))
    def test_each_domain_index_is_checked(self):
        baseline=copy.deepcopy(self.m)
        for domain in e._ZR_DOMAINS:
            with self.subTest(domain=domain):
                self.m=copy.deepcopy(baseline)
                owner=self.m if domain=='rational' else self.m[domain+'_archive']
                owner['results'].clear()
                self.assertTrue(any(f.get('archive')==domain and 'typed_results_index_mismatch' in f['reasons'] for f in self.observe()['contradictions']))
    def test_forged_new_calculus_without_variable_is_rejected(self):
        r=self.m['calculus_archive']['expressions'][2]
        for key in ['variable_source','variable','input_interpretation']:r.pop(key,None)
        r['sources']=[];self.refresh();self.rejected('calculus')

if __name__=='__main__':unittest.main()
