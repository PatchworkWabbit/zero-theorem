"""Pydroid3: extract the Task 7 ZIP, open this file, press Run."""
import argparse
import importlib.util
import io
import json
from pathlib import Path
import sys
import time
import unittest

ENGINE = 'zero_theoremV4.7.15.py'
PHONE_TESTS = [
    'test_matching_digest_supplies_recipe_then_independent_replay',
    'test_same_value_different_construction_never_supplies_recipe',
    'test_matching_digest_still_requires_correct_reexecution',
    'test_later_matching_evidence_reopens_pending_recovery',
    'test_unchanged_evidence_does_not_repeat_exhausted_work',
    'test_changed_rules_trigger_new_attempt',
    'test_feedback_cursor_is_bounded_and_resumes',
    'test_interruption_preserves_cursor_and_restarts',
    'test_normal_run_services_recovery_and_continues_regeneration',
    'test_candidate_ready_is_retained_without_switching',
]


def bundle_folder():
    choices = [Path(__file__).resolve().parent, Path.cwd()]
    for name in ('Download', 'Downloads'):
        downloads = Path('/storage/emulated/0') / name
        if downloads.is_dir():
            choices.extend(sorted(downloads.glob('zero_theorem_task7*'),
                                  key=lambda p: p.stat().st_mtime, reverse=True))
    for folder in choices:
        if (folder / ENGINE).is_file() and (folder / 'task7_fixture/baseline.json').is_file():
            return folder
    raise FileNotFoundError('Extract the complete Task 7 ZIP; open run_task7_tests.py inside that folder.')


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', action='store_true')
    args = parser.parse_args()
    folder = bundle_folder()
    sys.path.insert(0, str(folder))
    module = load_module(folder / 'test_recovery_retries.py', 'task7_checks')
    if args.full:
        suite = unittest.TestSuite([
            unittest.defaultTestLoader.loadTestsFromModule(module),
            unittest.defaultTestLoader.loadTestsFromModule(load_module(folder / 'test_large_memory_v4715.py', 'large_checks')),
            unittest.defaultTestLoader.discover(str(folder / 'task7_regression'), pattern='test*.py'),
        ])
    else:
        suite = unittest.TestSuite(module.RecoveryRetryTests(name) for name in PHONE_TESTS)
    print('TASK 7 | engine:', ENGINE, '| disposable fixtures only', flush=True)
    log = io.StringIO()
    started = time.perf_counter()
    class LiveResult(unittest.TextTestResult):
        def addSuccess(self, test):
            super().addSuccess(test)
            print('  PASS |', test._testMethodName, flush=True)
        def addFailure(self, test, err):
            super().addFailure(test, err)
            print('  FAIL |', test._testMethodName, flush=True)
        def addError(self, test, err):
            super().addError(test, err)
            print('  ERROR |', test._testMethodName, flush=True)
    result = unittest.TextTestRunner(stream=log, verbosity=2, resultclass=LiveResult).run(suite)
    report = {'engine': ENGINE, 'tests': result.testsRun, 'failures': len(result.failures),
              'errors': len(result.errors), 'passed': result.wasSuccessful(),
              'seconds': round(time.perf_counter() - started, 4),
              'scope': 'disposable generated fixtures; no live user memory opened', 'details': log.getvalue()}
    output = folder / 'task7_phone_results.json'
    output.write_text(json.dumps(report, indent=2) + '\n')
    if not result.wasSuccessful():
        print(log.getvalue())
    print('\nTASK 7:', result.testsRun - len(result.failures) - len(result.errors), '/', result.testsRun, 'checks passed.')
    print('No live user memory opened. Results:', output)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
