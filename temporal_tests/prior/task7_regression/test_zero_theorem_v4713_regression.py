import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('engine', (Path(__file__).resolve().parents[1]/'zero_theoremV4.7.15.py'))
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)
FIXTURE = Path(__file__).parent / 'task2_source/zero_theorem_rabbitholes_v41_memory.json.zero-body-candidate.json'

class VerificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.master = json.loads(FIXTURE.read_text())

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'memory.json'
        self.memory = copy.deepcopy(self.master)

    def write(self):
        self.path.write_text(json.dumps(self.memory))
        return self.path.read_bytes()

    def verify(self, budget=32):
        with contextlib.redirect_stdout(io.StringIO()):
            return e.zero_verify_candidate(str(self.path), budget)

    def test_real_candidate_independent_check_is_read_only(self):
        before=copy.deepcopy(self.memory)
        report=e.zero_core(self.memory, 'verification', operation='observe')
        self.assertEqual(report['contradictions'], [])
        self.assertEqual(self.memory,before)

    def test_healthy_candidate_archive_validation(self):
        before=self.write();r=self.verify()
        self.assertEqual(r['status'],'candidate_ready')
        self.assertEqual(r['executed_total'],0)
        self.assertEqual(self.path.read_bytes(),before)

    def test_wrong_value_is_reconstructed_from_manifest(self):
        self.memory['expressions'][20]['value']='12345'
        before=self.write();r=self.verify()
        self.assertEqual(r['status'],'candidate_ready')
        fixed=json.loads(Path(r['validated_candidate']).read_text())
        self.assertEqual(e._zr_payload(fixed['expressions'][20]),e._zr_payload(self.master['expressions'][20]))
        self.assertGreater(r['executed_total'],0)
        self.assertEqual(self.path.read_bytes(),before)

    def test_independent_calculator_does_not_trust_engine_evaluator(self):
        old=e.evaluate_tree
        e.evaluate_tree=lambda tree: (e.Fraction(999),'fake')
        try:
            r=e.zero_core(self.memory,'verification',operation='observe')
            self.assertFalse(r['contradictions'])
        finally:e.evaluate_tree=old

    def test_corrupted_tree_uses_surviving_recipe(self):
        self.memory['expressions'][20]['tree']['op']='+'
        self.write();r=self.verify()
        self.assertEqual(r['status'],'candidate_ready')
        self.assertTrue(any(t['status']=='reexecuted' for t in r['zero_feedback']))

    def test_no_evidence_retains_unknown_and_retries(self):
        self.memory['expressions'][20]['value']='12345'
        del self.memory['zero_recovery']['manifest']['rational']['20']
        self.memory['known_expression_keys'][20]='invalid'
        self.write();r=self.verify()
        self.assertEqual(r['status'],'unresolved')
        second=self.verify()
        self.assertGreater(second['executed_total'],r['executed_total'])
        self.assertTrue(any(t['status']=='unresolved' for t in second['zero_feedback']))

    def test_budget_continues_saved_tasks(self):
        for idx in [20,22,23]:self.memory['expressions'][idx]['value']='999'
        self.write();first=self.verify(1)
        self.assertEqual(first['executed_total'],1)
        for _ in range(8):
            final=self.verify(1)
            if final['status']=='candidate_ready':break
        self.assertEqual(final['status'],'candidate_ready')
        self.assertGreater(final['executed_total'],1)

    def test_wrong_result_index_is_rebuilt_from_checked_trees(self):
        self.memory['results']['0'].remove(20)
        self.write();r=self.verify()
        self.assertEqual(r['status'],'candidate_ready')
        fixed=json.loads(Path(r['validated_candidate']).read_text())
        self.assertEqual(fixed['results'],self.master['results'])

    def test_foundation_uncertainty_stays_unresolved(self):
        self.memory['foundation']['states'][1]=99
        self.write();r=self.verify()
        self.assertEqual(r['status'],'unresolved')
        self.assertTrue(any('foundation_uncertain' in f['reasons'] for f in r['contradictions']))

    def test_conflicting_recipe_is_rejected(self):
        self.memory['expressions'][20]['value']='999'
        self.memory['zero_recovery']['manifest']['rational']['20']['recipe']['tree']['op']='+'
        self.memory['known_expression_keys'][20]='invalid'
        self.write();r=self.verify()
        self.assertEqual(r['status'],'unresolved')
        self.assertTrue(any(a.get('status')=='rejected' for t in r['zero_feedback'] for batch in t.get('attempts',[]) for a in batch))

    def test_changed_source_does_not_reuse_old_state(self):
        self.memory['expressions'][20]['value']='999'
        self.write();self.verify(1)
        self.memory=copy.deepcopy(self.master);self.write();r=self.verify()
        self.assertEqual(r['executed_total'],0)
        self.assertEqual(r['status'],'candidate_ready')

    def test_shared_ancestor_not_independent(self):
        r=e.zero_core(self.memory,'verification',operation='observe')
        for group in r['archive_correlations']:
            for a,b in group['disjoint_construction_pairs']:
                def closure(idx):
                    out={idx}
                    for parent in self.memory['expressions'][idx]['parents']:
                        if self.memory['expressions'][parent]['parents']:
                            out.update(closure(parent))
                    return out
                self.assertFalse(closure(a) & closure(b))

    def test_kernel_disagreement_is_detected(self):
        original=e._operate_rational_exact
        e._operate_rational_exact=lambda a,op,b:e.Fraction(12345)
        try:
            report=e.zero_core(self.memory,'verification',operation='observe')
            self.assertTrue(any('construction_reexecution_mismatch' in f['reasons'] for f in report['contradictions']))
        finally:e._operate_rational_exact=original

    def test_interruption_checkpoints_executed_feedback(self):
        self.memory['expressions'][20]['value']='999'
        self.write()
        original=e._zv_explore
        def interrupt(m,state,budget):
            original(m,state,1)
            raise KeyboardInterrupt()
        e._zv_explore=interrupt
        try:
            with self.assertRaises(KeyboardInterrupt):self.verify()
        finally:e._zv_explore=original
        state=json.loads(Path(str(self.path)+'.zero-verification-search.json').read_text())
        self.assertEqual(state['head'],1)
        self.assertEqual(self.verify()['status'],'candidate_ready')

    def test_save_gate_preserves_normal_memory_on_contradiction(self):
        original=self.write()
        self.memory['expressions'][20]['value']='999'
        old=e.memory_path;e.memory_path=lambda:str(self.path)
        try:
            with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(e.ZeroRecoveryPending):
                e.save_memory(self.memory)
            self.assertEqual(self.path.read_bytes(),original)
            self.assertTrue(Path(str(self.path)+'.zero-verification-run-proposal.json.verification.json').exists())
        finally:e.memory_path=old

    def test_actual_normal_run_and_reload(self):
        self.write()
        old=e.memory_path;e.memory_path=lambda:str(self.path)
        try:
            with contextlib.redirect_stdout(io.StringIO()):e.run()
            saved=json.loads(self.path.read_text())
            self.assertGreater(len(saved['expressions']),len(self.master['expressions']))
            self.assertGreater(len(saved['runs']),len(self.master['runs']))
            self.assertFalse(e.zero_core(saved,'verification',operation='observe')['contradictions'])
            with contextlib.redirect_stdout(io.StringIO()):loaded=e.load_memory()
            self.assertEqual(len(loaded['expressions']),len(saved['expressions']))
        finally:e.memory_path=old

    def test_repaired_candidate_promote_resume_and_reload(self):
        self.memory['expressions'][20]['value']='999'
        self.write();r=self.verify()
        old=e.memory_path;e.memory_path=lambda:str(self.path)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                e._za_promote(r['validated_candidate'],str(self.path));e.run()
                saved=e.load_memory()
            self.assertTrue(saved['zero_resume']['continuation_verified'])
            self.assertFalse(e.zero_core(saved,'verification',operation='observe')['contradictions'])
        finally:e.memory_path=old

if __name__=='__main__':unittest.main()
