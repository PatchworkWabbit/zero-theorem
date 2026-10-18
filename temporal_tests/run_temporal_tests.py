"""Unzip the full bundle; open this runner in Pydroid3 and press Run.

Tests create disposable engine runs and mask their recorded clock samples.
They never open your real memory. --full adds the existing recovery suite.
"""
import argparse
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import time
import unittest

ENGINE='zero_theoremV4.7.17.py'

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def folder():
    candidates=[Path(__file__).resolve().parent,Path.cwd()]
    if sys.argv and sys.argv[0]:candidates.append(Path(sys.argv[0]).expanduser().resolve().parent)
    def complete(p):return (p/ENGINE).is_file() and (p/'test_temporal_recovery.py').is_file()
    for p in candidates:
        if complete(p):return p
    print('Paste the extracted folder containing '+ENGINE+' and this runner.')
    while True:
        value=input('Folder (ENTER cancels): ').strip().strip('\"\'')
        if not value:return None
        p=Path(value).expanduser()
        if p.is_file():p=p.parent
        if complete(p):return p.resolve()
        print('Those files were not found together. Check the extraction folder.')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true')
    args=parser.parse_args();root=folder()
    if root is None:return 1
    started=time.perf_counter()
    with tempfile.TemporaryDirectory() as tmp:
        work=Path(tmp)
        for name in ['test_temporal_recovery.py','test_retry_audit.py','test_time_observer.py','zero_time_lab_v0.2.py']:
            shutil.copyfile(root/name,work/name)
        shutil.copytree(root/'prior',work/'prior',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        for name in [ENGINE,'zero_theoremV4.7.16.py','prior/zero_theoremV4.7.15.py']:
            shutil.copyfile(root/ENGINE,work/name)
        suite=unittest.TestSuite()
        modules=[('test_temporal_recovery.py','new_temporal'),('test_retry_audit.py','new_audit'),
                 ('test_time_observer.py','clock_regression'),('zero_time_lab_v0.2.py','lab_regression')]
        if args.full:
            modules += [('prior/test_recovery_retries.py','retry_regression'),
                        ('prior/test_large_memory_v4715.py','large_regression')]
        for name,identity in modules:
            suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(load(work/name,identity)))
        if args.full:
            suite.addTests(unittest.defaultTestLoader.discover(str(work/'prior/task7_regression'),pattern='test*.py'))
        log=io.StringIO()
        class Live(unittest.TextTestResult):
            def addSuccess(self,test):
                super().addSuccess(test);print('PASS | '+test._testMethodName,flush=True)
            def addError(self,test,error):
                super().addError(test,error);print('ERROR | '+test._testMethodName,flush=True)
            def addFailure(self,test,error):
                super().addFailure(test,error);print('FAIL | '+test._testMethodName,flush=True)
        print('ZERO TEMPORAL V4.7.17 | disposable tests only',flush=True)
        result=unittest.TextTestRunner(stream=log,verbosity=2,resultclass=Live).run(suite)
        report={'engine':ENGINE,'tests':result.testsRun,'failures':len(result.failures),
                'errors':len(result.errors),'passed':result.wasSuccessful(),
                'seconds':round(time.perf_counter()-started,4),
                'scope':'disposable generated engine runs; actual host clock samples; no live memory',
                'details':log.getvalue()}
    output=root/('temporal_full_results.json' if args.full else 'temporal_phone_results.json')
    output.write_text(json.dumps(report,indent=2)+'\n')
    if not result.wasSuccessful():print(log.getvalue())
    print('\nTEMPORAL:',result.testsRun-len(result.failures)-len(result.errors),'/',result.testsRun,'passed.')
    print('No live memory opened. Results:',output)
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':raise SystemExit(main())
