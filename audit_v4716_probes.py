"""Read-only engine audit using disposable data; no project memory is opened.

Prints confirmed gaps, not an assertion that malformed input is supported.
Run from an extracted repository checkout with the Task 7 fixture available.
"""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
from unittest.mock import patch


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    root = Path(__file__).resolve().parent
    e = load('audited_engine', root / 'zero_theoremV4.7.16.py')
    findings = []
    with tempfile.TemporaryDirectory() as directory:
        path = str(Path(directory) / 'memory.json')
        memory = e.empty_memory()
        clock = e._zt16_space(path, memory, 'audit')
        clock.update(tick=-1, registered_states=0)
        clock['coordinates']['foundation'] = -1
        Path(e._zt16_zero_path(path)).write_text(json.dumps(clock))
        accepted = e._zt16_space(path, memory, 'audit')
        findings.append({'probe': 'negative_zero_clock', 'observed_tick': accepted['tick'],
                         'gap_reproduced': accepted['tick'] < 0})

        timed = str(Path(directory) / 'timed.json')
        with e._zt16_span(timed, 'audit'):
            pass
        state = e._zt16_read(timed)
        state['events'][0]['seq'] = 999
        Path(e._zt16_path(timed)).write_text(json.dumps(state))
        accepted = e._zt16_read(timed)
        findings.append({'probe': 'broken_observer_event_chain',
                         'observed_first_sequence': accepted['events'][0]['seq'],
                         'gap_reproduced': accepted['events'][0]['seq'] != 1})

        launcher = Path(directory) / 'launcher.py'
        launcher.write_text('launcher revision one')
        with patch.object(e, '__file__', str(launcher)):
            first = e._z7_rules_signature()
            launcher.write_text('launcher revision two')
            second = e._z7_rules_signature()
        findings.append({'probe': 'launcher_supplied_file_fingerprint',
                         'scope': 'conditional on launcher supplying its own __file__; not proven on user engine launch',
                         'gap_reproduced': first != second})

    # Reuse the public disposable fixture and adaptive-state setup, but execute
    # the current V4.7.16 engine rather than the fixture's original V4.7.15.
    fixture = load('audit_fixture', root / 'test_recovery_retries.py')
    fixture.e = e
    fixture.RecoveryRetryTests.setUpClass()
    case = fixture.RecoveryRetryTests()
    case.setUp()
    try:
        case.missing_recipe()
        case.install()
        e._zn_checkpoint(str(case.root / 'recovery-retry-state.json'), {
            'rule': e._Z7_RULE, 'source_sha256': e._z7_hash_file(case.source),
            'status': 'pending', 'attempts': None})
        before = {str(p): p.read_bytes() for p in (case.source, case.snapshot, case.active, case.pointer)}
        with patch.object(e, 'memory_path', return_value=str(case.source)), \
                patch.object(e, '_zg_previous_run', return_value='continued'), \
                contextlib.redirect_stdout(io.StringIO()):
            try:
                result = e.run()
                failure = None
            except Exception as exc:
                result = None
                failure = type(exc).__name__ + ': ' + str(exc)
        findings.append({'probe': 'malformed_retry_ledger_stops_normal_run',
                         'exception': failure, 'continued': result == 'continued',
                         'protected_bytes_unchanged': all(Path(p).read_bytes() == raw for p, raw in before.items()),
                         'gap_reproduced': failure is not None})
    finally:
        case.doCleanups()
    print(json.dumps({'scope': 'disposable audit probes; no live memory opened',
                      'findings': findings}, indent=2))


if __name__ == '__main__':
    main()
