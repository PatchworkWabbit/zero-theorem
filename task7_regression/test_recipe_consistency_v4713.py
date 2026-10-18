import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec=importlib.util.spec_from_file_location('recipe_engine',(Path(__file__).resolve().parents[1]/'zero_theoremV4.7.15.py'))
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)

class RecipeConsistencyTests(unittest.TestCase):
    def setUp(self):
        self.m=json.loads((Path(__file__).parent/'task4_fixture/baseline.json').read_text())
        recipe=self.m['zero_recovery']['manifest']['rational']['20']['recipe']
        recipe['tree']['op']='+' if recipe['tree']['op']!='+' else '*'
    def test_latent_recipe_conflict_is_detected_read_only(self):
        before=copy.deepcopy(self.m)
        report=e.zero_core(self.m,'verification',operation='observe')
        self.assertTrue(any(f['id']==20 and 'manifest_recipe_record_disagreement' in f['reasons'] for f in report['contradictions']))
        self.assertEqual(self.m,before)
    def test_candidate_approval_refuses_conflicting_recipe(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'bad.json';raw=json.dumps(self.m).encode();path.write_bytes(raw)
            with self.assertRaisesRegex(e.ZeroRecoveryPending,'manifest_recipe_record_disagreement'):
                e._za_validate(str(path))
            self.assertEqual(path.read_bytes(),raw)

if __name__=='__main__':unittest.main()
