"""Task 6: exact typed slot recovery, preserved evidence and continuation."""
import contextlib,copy,hashlib,importlib.util,io,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('engine4713',ROOT.parent/'zero_theoremV4.7.15.py')
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
DOMAINS=('complex','symbolic','calculus','roles')

class TypedRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.legacy=json.loads((ROOT/'task4_fixture/baseline.json').read_text())
        cls.base,ready=e._zr_preflight(cls.legacy,vars(e))
        if not ready:raise AssertionError('baseline migration failed')
    def setUp(self):
        self.m=copy.deepcopy(self.base)
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
    def remove(self,domain,ids):
        records=e._zr_records(self.m,domain)
        records[:]=[r for r in records if r['id'] not in ids]
    def recover(self):return e.zero_core(self.m,'errors',operation='recover_archive')
    def equal_payloads(self,candidate,baseline=None):
        baseline=baseline or self.base
        for d in e._ZR_DOMAINS:
            self.assertEqual([e._zr_payload(r) for r in e._zr_records(candidate,d)],[e._zr_payload(r) for r in e._zr_records(baseline,d)],d)
    def pending(self,candidate,domain,idx):
        self.assertEqual(e._zr_records(candidate,domain)[idx].get('status'),'zero_recovery_pending')
    def test_migration_adds_recipes_without_mutating_original_records(self):
        before=copy.deepcopy(self.legacy);candidate,ready=e._zr_preflight(self.legacy,vars(e))
        self.assertTrue(ready);self.assertEqual(self.legacy,before);self.equal_payloads(candidate,self.legacy)
        for d in DOMAINS:
            self.assertTrue(all('typed_recipe' in v for v in candidate['zero_recovery']['manifest'][d].values()))
    def test_last_record_of_each_domain_recovers_exactly(self):
        for d in DOMAINS:self.remove(d,[len(e._zr_records(self.base,d))-1])
        before=copy.deepcopy(self.m);candidate,ready=self.recover()
        self.assertTrue(ready);self.equal_payloads(candidate);self.assertEqual(self.m,before)
    def test_every_record_individually_recovers(self):
        for d in DOMAINS:
            for original in e._zr_records(self.base,d):
                with self.subTest(domain=d,id=original['id']):
                    self.m=copy.deepcopy(self.base);self.remove(d,[original['id']])
                    candidate,ready=self.recover();self.assertTrue(ready)
                    self.assertEqual(e._zr_payload(e._zr_records(candidate,d)[original['id']]),e._zr_payload(original))
    def test_dependent_gaps_within_each_domain(self):
        for d in DOMAINS:
            self.m=copy.deepcopy(self.base)
            rec=next(r for r in e._zr_records(self.m,d) if r['parents'])
            self.remove(d,[rec['parents'][0],rec['id']])
            candidate,ready=self.recover();self.assertTrue(ready,d);self.equal_payloads(candidate)
    def test_cross_archive_chain_role_to_calculus(self):
        calc=next(r for r in e._zr_records(self.m,'calculus') if 'variable_source' in r)
        var=calc['variable_source']['id']
        self.remove('roles',[0,var]);self.remove('calculus',[calc['parents'][0],calc['id']])
        candidate,ready=self.recover();self.assertTrue(ready);self.equal_payloads(candidate)
    def test_cross_archive_symbolic_complex_bridge(self):
        bridge=next(r for r in e._zr_records(self.m,'complex') if r['pathway']=='symbolic_to_complex_v46')
        origin=bridge['sources'][0]['id'];parent=e._zr_records(self.m,'symbolic')[origin]['parents'][0]
        self.remove('symbolic',[parent,origin]);self.remove('complex',[bridge['id']])
        candidate,ready=self.recover();self.assertTrue(ready);self.equal_payloads(candidate)
    def test_all_four_nonrational_archives_can_be_missing_with_recipes(self):
        for d in DOMAINS:self.remove(d,[r['id'] for r in e._zr_records(self.m,d)])
        candidate,ready=self.recover();self.assertTrue(ready);self.equal_payloads(candidate)
    def test_no_output_values_in_recovery_recipes(self):
        forbidden={'value','real','imaginary','coefficients','body','exact','construction','expr','proof'}
        for d in DOMAINS:
            for entry in self.m['zero_recovery']['manifest'][d].values():
                self.assertFalse(forbidden.intersection(entry['typed_recipe']))
    def test_absent_recipe_and_key_retains_pending(self):
        self.remove('complex',[125]);self.m['zero_recovery']['manifest']['complex']['125'].pop('typed_recipe')
        self.m['complex_archive']['known_keys']=[]
        candidate,ready=self.recover();self.assertFalse(ready);self.pending(candidate,'complex',125)
    def test_legacy_key_evidence_recovers_each_supported_domain(self):
        self.m=copy.deepcopy(self.legacy)
        for d in DOMAINS:self.remove(d,[len(e._zr_records(self.legacy,d))-1])
        candidate,ready=self.recover();self.assertTrue(ready);self.equal_payloads(candidate)
    def test_legacy_complex_embedding_does_not_guess_equal_valued_origin(self):
        self.m=copy.deepcopy(self.legacy)
        bridge=next(r for r in e._zr_records(self.m,'complex') if r['pathway']=='symbolic_to_complex_v46')
        self.remove('complex',[bridge['id']]);candidate,ready=self.recover()
        self.assertFalse(ready);self.pending(candidate,'complex',bridge['id'])
    def test_conflicting_recipe_never_replaces_missing_slot(self):
        recipe=self.m['zero_recovery']['manifest']['complex']['125']['typed_recipe']
        recipe['operation']='+' if recipe['operation']!='+' else '-'
        self.remove('complex',[125]);candidate,ready=self.recover()
        self.assertFalse(ready);self.pending(candidate,'complex',125)
    def test_intact_record_with_conflicting_recipe_is_blocked(self):
        self.m['zero_recovery']['manifest']['roles']['23']['typed_recipe']['label']='A?'
        before=copy.deepcopy(self.m);candidate,ready=self.recover()
        self.assertFalse(ready);self.assertEqual(candidate['zero_recovery']['status'],'blocked');self.assertEqual(self.m,before)
        findings=e.zero_core(self.m,'verification',operation='observe')['contradictions']
        self.assertTrue(any('typed_manifest_recipe_record_disagreement' in f['reasons'] for f in findings))
    def test_wrong_record_digest_does_not_get_repaired_as_missing(self):
        self.m['complex_archive']['expressions'][125]['real']='999'
        candidate,ready=self.recover();self.assertFalse(ready)
        self.assertEqual(candidate['zero_recovery']['status'],'blocked')
    def test_invalid_dependency_is_pending(self):
        self.m['zero_recovery']['manifest']['calculus']['19']['typed_recipe']['sources']=[{'archive':'roles','id':99999}]
        self.remove('calculus',[19]);candidate,ready=self.recover();self.assertFalse(ready);self.pending(candidate,'calculus',19)
    def test_duplicate_ids_are_rejected_without_mutation(self):
        self.m['roles_archive']['expressions'][2]['id']=1;before=copy.deepcopy(self.m)
        with self.assertRaises(e.ZeroRecoveryPending):self.recover()
        self.assertEqual(self.m,before)
    def test_recipe_cycle_remains_pending(self):
        self.remove('complex',[25]);self.remove('symbolic',[15])
        self.m['zero_recovery']['manifest']['symbolic']['15']['typed_recipe'].update(
            operation='embed',pathway='numeric_to_symbolic_v464',parents=[],sources=[{'archive':'complex','id':25}])
        candidate,ready=self.recover();self.assertFalse(ready)
        self.pending(candidate,'complex',25);self.pending(candidate,'symbolic',15)
    def test_recovery_does_not_increment_archive_passage_counts(self):
        counts=copy.deepcopy(self.m['zero_core']['record_passages'])
        for d in DOMAINS:self.remove(d,[len(e._zr_records(self.m,d))-1])
        candidate,ready=self.recover();self.assertTrue(ready);self.assertEqual(candidate['zero_core']['record_passages'],counts)
        self.assertTrue(e.zero_core_report(candidate)['complete'])
    def test_independent_checker_rejects_faulty_reconstruction_kernel(self):
        rec=next(r for r in e._zr_records(self.m,'complex') if r['operation']=='+')
        self.remove('complex',[rec['id']])
        with patch.object(e,'_complex_operate_exact',return_value=(e.Fraction(123),e.Fraction(0))):
            entry=self.m['zero_recovery']['manifest']['complex'][str(rec['id'])]
            wrong=e._z6_build(self.m,'complex',rec['id'],entry['typed_recipe'])
            self.assertIsNotNone(wrong);entry['digest']=e._zr_digest(e._zr_payload(wrong))
            candidate,ready=self.recover()
        self.assertFalse(ready);self.pending(candidate,'complex',rec['id'])
        outcomes=candidate['zero_recovery']['typed_reconstruction_attempts']['complex:'+str(rec['id'])]['outcomes']
        self.assertTrue(any('independent_check_failed' in row['reason'] for row in outcomes))
    def test_source_bytes_preserved_then_recovered_copy_continues(self):
        for d in DOMAINS:self.remove(d,[len(e._zr_records(self.m,d))-1])
        source=Path(self.tmp.name)/'damaged.json';source.write_text(json.dumps(self.m));before=source.read_bytes()
        candidate,ready=self.recover();self.assertTrue(ready);self.equal_payloads(candidate)
        path=Path(self.tmp.name)/'recovered.json';path.write_text(json.dumps(candidate))
        with contextlib.redirect_stdout(io.StringIO()):after,metrics=e._zg_cycle(str(path))
        self.assertEqual(source.read_bytes(),before);self.assertTrue(metrics['prefix_preserved'])
        self.assertGreater(len(after['expressions']),len(candidate['expressions']))
    def test_adaptive_chooses_verified_recovery_for_typed_loss(self):
        self.remove('roles',[23]);source=Path(self.tmp.name)/'damaged.json';source.write_text(json.dumps(self.m));before=source.read_bytes()
        with contextlib.redirect_stdout(io.StringIO()):report=e.zero_adaptive_recovery(str(source),target_records=296)
        self.assertEqual(report['selected_branch'],'recovery');self.assertFalse(report['new_lineage'])
        self.assertEqual(source.read_bytes(),before)
    def test_no_hidden_baseline_file_is_used_as_repair_input(self):
        self.remove('calculus',[19]);original=e._z6_build
        with patch.object(e,'open',side_effect=AssertionError('unexpected file access'),create=True):
            candidate,ready=self.recover()
        self.assertTrue(ready);self.equal_payloads(candidate)

if __name__=='__main__':unittest.main()
