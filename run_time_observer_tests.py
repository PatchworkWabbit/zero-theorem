"""Extract the complete ZIP, open this runner in Pydroid3, press Run."""
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
import zipfile

ENGINE = 'zero_theoremV4.7.16.py'
PHONE_TESTS = [
    'test_start_at_zero_and_exact_elapsed_cpu_observation',
    'test_wall_clock_correction_does_not_reverse_elapsed',
    'test_restart_links_events_without_subtracting_old_timer',
    'test_zero_clock_origin_keeps_existing_space_as_boundary',
    'test_zero_clock_transforms_its_own_states_with_space_growth',
    'test_zero_clock_does_not_tick_for_elapsed_time',
    'test_zero_clock_survives_session_restart',
    'test_zero_clock_is_independent_of_wall_timer_and_role_grammar',
    'test_observation_preserves_math_records_queue_and_operation_counts',
    'test_adaptive_cycle_keeps_prefix_and_adds_time_events',
]

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def find_bundle_folder():
    """Pydroid's exec wrapper may supply its own __file__, not this runner's."""
    candidates = [Path(__file__).resolve().parent, Path.cwd()]
    if sys.argv and sys.argv[0]:
        candidates.append(Path(sys.argv[0]).expanduser().resolve().parent)
    def complete(folder):
        return all((folder / name).is_file() for name in
                   ('test_time_observer.py', ENGINE))
    for folder in candidates:
        if complete(folder):
            return folder
    print('Pydroid did not supply the extracted test folder.', flush=True)
    print('Paste the full folder path containing test_time_observer.py and ' + ENGINE,
          flush=True)
    while True:
        value = input('Extracted test folder (ENTER to cancel): ').strip().strip('\"\'')
        if not value:
            return None
        folder = Path(value).expanduser()
        if folder.is_file():
            folder = folder.parent
        if complete(folder):
            return folder.resolve()
        print('Required files are not together in that folder. Check the extraction destination.',
              flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--full', action='store_true')
    args = parser.parse_args()
    folder = find_bundle_folder()
    if folder is None:
        return 1
    print('Test folder:', folder, flush=True)
    module = load_module(folder / 'test_time_observer.py', 'clock_checks')
    with contextlib.ExitStack() as resources:
        if args.full:
            scratch = Path(resources.enter_context(tempfile.TemporaryDirectory()))
            with zipfile.ZipFile(folder / 'zero_theorem_task7_tests.zip') as bundle:
                bundle.extractall(scratch)
            # The previous tests retain their import filenames, but execute
            # the new engine bytes. No live user memory is copied or opened.
            shutil.copyfile(folder / ENGINE, scratch / 'zero_theoremV4.7.15.py')
            sys.path.insert(0, str(scratch))
            suite = unittest.TestSuite([
                unittest.defaultTestLoader.loadTestsFromModule(module),
                unittest.defaultTestLoader.loadTestsFromModule(load_module(scratch / 'test_recovery_retries.py', 'recovery_regression')),
                unittest.defaultTestLoader.loadTestsFromModule(load_module(scratch / 'test_large_memory_v4715.py', 'large_regression')),
                unittest.defaultTestLoader.discover(str(scratch / 'task7_regression'), pattern='test*.py'),
            ])
        else:
            suite = unittest.TestSuite(module.TimeObserverTests(name) for name in PHONE_TESTS)
        print('ZERO TIME OBSERVER |', ENGINE, '| disposable tests only', flush=True)
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
                  'scope': 'disposable observations and generated fixtures; no live user memory opened',
                  'details': log.getvalue()}
        output = folder / ('time_observer_full_results.json' if args.full else 'time_observer_phone_results.json')
        output.write_text(json.dumps(report, indent=2) + '\n')
        if not result.wasSuccessful():
            print(log.getvalue())
        print('\nTIME OBSERVER:', result.testsRun - len(result.failures) - len(result.errors), '/', result.testsRun, 'checks passed.')
        print('No live user memory opened. Results:', output)
        return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
