import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('retry_audit_helpers',ROOT/'prior/test_recovery_retries.py')
helpers=importlib.util.module_from_spec(spec);spec.loader.exec_module(helpers)
e=helpers.e

class RetryAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):helpers.RecoveryRetryTests.setUpClass()

    def test_malformed_retry_attempts_defers_and_normal_regeneration_continues(self):
        helper=helpers.RecoveryRetryTests('test_matching_digest_supplies_recipe_then_independent_replay')
        helper.setUp();self.addCleanup(helper.doCleanups)
        helper.missing_recipe();helper.install()
        path=helper.root/'recovery-retry-state.json'
        ledger={'schema':1,'rule':e._Z7_RULE,'zero_nexus':'Z0',
                'source_sha256':e._z7_hash_file(helper.source),'attempts':None,'status':'pending'}
        path.write_text(json.dumps(ledger));before=path.read_bytes()
        old_runs=len(json.loads(helper.active.read_text())['runs'])
        with patch.object(e,'memory_path',return_value=str(helper.source)),patch('builtins.input',return_value=''),contextlib.redirect_stdout(io.StringIO()) as out:e.run()
        self.assertIn('retry deferred',out.getvalue())
        self.assertEqual(path.read_bytes(),before)
        for protected in (helper.source,helper.snapshot,helper.pointer):
            self.assertEqual(protected.read_bytes(),helper.protected[protected])
        self.assertEqual(len(json.loads(helper.active.read_text())['runs']),old_runs+1)

    def test_exec_wrapper_fingerprint_tracks_loaded_engine_not_launcher(self):
        with tempfile.TemporaryDirectory() as d:
            launcher=Path(d)/'launcher.py';launcher.write_text('version one')
            source=(ROOT/'zero_theoremV4.7.17.py').read_text()
            namespace={'__name__':'wrapper_test','__file__':str(launcher)}
            exec(compile(source,'<engine-wrapper>','exec'),namespace)
            first=namespace['_z7_rules_signature']()
            launcher.write_text('version two')
            self.assertEqual(namespace['_z7_rules_signature'](),first)
            changed={'__name__':'wrapper_test','__file__':str(launcher)}
            exec(compile(source.replace('MAX_DEPTH = 4','MAX_DEPTH = 5',1),'<engine-wrapper>','exec'),changed)
            self.assertNotEqual(changed['_z7_rules_signature'](),first)

if __name__=='__main__':unittest.main(verbosity=2)
