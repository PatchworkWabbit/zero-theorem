import importlib.util, tempfile, contextlib, io, json, copy
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parent
def load(version):
    s=importlib.util.spec_from_file_location('engine_'+version,ROOT/('zero_theoremV'+version+'.py'))
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def run(e):
    out=io.StringIO()
    with contextlib.redirect_stdout(out),patch('builtins.input',return_value=''):
        e.run()
    return out.getvalue()
import unittest

class ActualRecoveryTests(unittest.TestCase):
    def test_actual_v471_migration_and_repeated_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
        
            folder=Path(tmp)
            old=load('4.7.1'); new=load('4.7.2')
            p=folder/'legacy.json'; old.memory_path=lambda:str(p)
            run(old)
            original=json.loads(p.read_text())
            assert original['expressions'][19]['id']==19
            expected=copy.deepcopy(original['expressions'][19])
            print('Legacy first-run archives:', {d:len(old.archive_records(original,d)) for d in old.ZERO_CORE_DOMAINS})
            # Use a second file for independent fresh patched execution.
            q=folder/'new.json';new.memory_path=lambda:str(q)
            output=run(new)
            assert q.exists(),output
            fresh=json.loads(q.read_text())
            assert fresh['zero_recovery']['status']=='ready',output
            print('Patched fresh run: PASS')
            # Exact original experiment, migrating the pre-manifest memory.
            damaged=copy.deepcopy(original);del damaged['expressions'][19]
            p.write_text(json.dumps(damaged));new.memory_path=lambda:str(p)
            output=run(new)
            healed=json.loads(p.read_text())
            assert len(healed['runs'])==2,output
            assert healed['expressions'][19]==expected,(healed['expressions'][19],expected)
            assert new.zero_core_report(healed)['complete']
            audit=new.archive_link_audit(healed)
            assert audit['issues']==0,audit
            print('Legacy record 19 deletion/recovery/continued run: PASS')
            print('Recovered:',healed['expressions'][19]['expr'],healed['expressions'][19]['pathway'])
            print('Coverage: PASS; link audit issues:',audit['issues'])
            # Manifest-backed repeat, including later dependent records.
            del healed['expressions'][19];p.write_text(json.dumps(healed))
            output=run(new)
            healed_again=json.loads(p.read_text())
            assert len(healed_again['runs'])==3,output
            assert healed_again['expressions'][19]==expected
            assert new.archive_link_audit(healed_again)['issues']==0
            print('Manifest record 19 deletion/recovery/third run: PASS')
