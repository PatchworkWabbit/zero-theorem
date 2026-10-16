"""Construction coverage, complete counters, unified lookup and continuation."""
import contextlib
import copy
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest import mock
from fractions import Fraction

import sympy as sp


ROOT = Path(__file__).parent


def load_engine(filename, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


engine = load_engine('zero_theoremV4.6.4.py', 'integrated_engine')


def memory():
    m = engine.empty_memory()
    m['_keys'] = set(m['known_expression_keys'])
    for upgrade in (engine.upgrade_runtime, engine.upgrade_v44,
                    engine.upgrade_tracking_namespaces, engine.upgrade_v45,
                    engine.upgrade_complex_feedback, engine.upgrade_symbolic,
                    engine.upgrade_symbolic_zero_nexus,
                    engine.upgrade_zero_archive_access,
                    engine.upgrade_archive_integration):
        upgrade(m)
    engine.rebalance_queue(m)
    return m


def foundation(m, maximum):
    while len(m['foundation']['states']) <= maximum:
        engine.register_next_state(m)
    engine.upgrade_v44(m)
    return [engine.foundation_expression_id(m, n) for n in range(maximum + 1)]


def drain_imports(m):
    for _ in range(200):
        engine.import_symbolic_sources(m)
        cursors = m['symbolic_archive']['construction_import_cursors']
        if all(cursors[domain] == len(engine.archive_records(m, domain))
               for domain in ('rational', 'complex')):
            return
    raise AssertionError('Source import queue failed to settle')


def run_quietly(module):
    with contextlib.redirect_stdout(io.StringIO()), mock.patch('builtins.input', return_value=''):
        module.run()


class ArchiveIntegrationTests(unittest.TestCase):
    def test_equal_values_keep_distinct_trees_and_zero_slots(self):
        m = memory()
        zero, one, two = foundation(m, 2)
        stats = {'new': 0, 'observer_added': 0}
        sources = [engine.combine(m, zero, two, '+', 'route_a', stats),
                   engine.combine(m, one, one, '+', 'route_b', stats),
                   engine.combine(m, two, one, '*', 'route_c', stats)]
        drain_imports(m)
        sa = m['symbolic_archive']
        imported = [sa['source_import_links']['rational'][str(idx)] for idx in sources]
        self.assertEqual(len(set(imported)), 3)
        records = [sa['expressions'][idx] for idx in imported]
        self.assertEqual([r['value'] for r in records], ['2', '2', '2'])
        self.assertTrue(engine.symbolic_zero_paths(records[0]['construction']))
        self.assertFalse(engine.symbolic_zero_paths(records[1]['construction']))
        self.assertNotEqual(records[0]['construction'], records[1]['construction'])
        pending = m['queue'][m['queue_head']:]
        for source, sid in zip(sources, imported):
            self.assertEqual(sa['expressions'][sid]['sources'], [{'archive': 'rational', 'id': source}])
            self.assertTrue(any(t['kind'] == 'symbolic_nexus' and t['source'] == sid for t in pending))
        self.assertEqual(engine.archive_link_audit(m)['issues'], 0)

    def test_complex_imports_keep_operand_order_and_full_construction(self):
        m = memory()
        foundation(m, 2)
        ca = m['complex_archive']
        two = ca['results']['2+0i'][0]
        engine.work_complex(m, {'left': two, 'right': 0}, {})
        engine.work_complex(m, {'left': 0, 'right': two}, {})
        source_ids = list(ca['results']['2+1i'])
        self.assertEqual(len(source_ids), 2)
        drain_imports(m)
        sa = m['symbolic_archive']
        ids = [sa['source_import_links']['complex'][str(idx)] for idx in source_ids]
        self.assertNotEqual(ids[0], ids[1])
        trees = [sa['expressions'][idx]['construction'] for idx in ids]
        self.assertEqual([t['op'] for t in trees], ['+', '+'])
        self.assertNotEqual(trees[0]['args'], trees[1]['args'])
        self.assertEqual(engine.archive_link_audit(m)['issues'], 0)

    def test_audit_detects_equal_value_source_mixups_without_modifying_memory(self):
        m = memory()
        zero, one, two = foundation(m, 2)
        stats = {'new': 0, 'observer_added': 0}
        a = engine.combine(m, zero, two, '+', 'path_a', stats)
        b = engine.combine(m, one, one, '+', 'path_b', stats)
        drain_imports(m)
        links = m['symbolic_archive']['source_import_links']['rational']
        links[str(a)] = links[str(b)]
        before = copy.deepcopy(m)
        report = engine.archive_link_audit(m)
        self.assertGreater(report['issues'], 0)
        self.assertTrue(any('another source construction' in example for example in report['examples']))
        self.assertEqual(m, before)

    def test_numeric_queries_include_symbolic_routes_to_existing_values(self):
        m = memory()
        _, _, two = foundation(m, 2)
        sid = engine.import_numeric_construction(m, 'rational', two)
        stats = {'new': 0}
        engine.work_symbolic(m, {'kind': 'symbolic_root', 'source': sid}, stats)
        root = m['symbolic_archive']['results']['sqrt(2)'][0]
        engine.work_symbolic(m, {'kind': 'symbolic_pair', 'source': root,
                                 'cursor': 0, 'step': 0}, stats)
        square = m['symbolic_archive']['expressions'][-1]['id']
        self.assertIn(square, m['unified_results']['2']['symbolic'])
        before = copy.deepcopy(m)
        for query in ('2', '2+0i', 'symbolic sqrt(2)**2'):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertTrue(engine.query_unified(m, query))
            self.assertIn('symbolic:%d' % square, out.getvalue())
            self.assertIn('(sqrt(2) * sqrt(2))', out.getvalue())
            self.assertIn('rational:', out.getvalue())
        self.assertEqual(m, before)

    def test_gaussian_power_and_numeric_query_share_one_lookup(self):
        m = memory()
        _, one, _, three = foundation(m, 3)
        a = engine.import_numeric_construction(m, 'rational', one)
        b = engine.import_numeric_construction(m, 'complex', 0)
        c = engine.import_numeric_construction(m, 'rational', three)
        base = engine.symbolic_record(m, 1 + sp.I, '(1+i)', [a, b], '+', 'test_arithmetic')
        power = engine.symbolic_record(m, (1 + sp.I)**3, '((1+i)**3)', [base, c], '**', 'test_arithmetic')
        key = engine.exact_lookup_key(-2 + 2 * sp.I)
        self.assertIn(power, m['unified_results'][key]['symbolic'])
        self.assertTrue(m['unified_results'][key]['complex'])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertTrue(engine.query_v45(m, '-2+2i'))
        self.assertIn('symbolic:%d' % power, out.getvalue())
        self.assertIn('complex:', out.getvalue())

    def test_representation_links_do_not_create_import_mirror_loops(self):
        m = memory()
        _, _, two, three = foundation(m, 3)
        a = engine.import_numeric_construction(m, 'rational', three)
        b = engine.import_numeric_construction(m, 'rational', two)
        power = engine.symbolic_record(m, sp.Integer(9), '(3**2)', [a, b], '**', 'test_arithmetic')
        real_alias = m['results']['9'][0]
        complex_alias = m['complex_archive']['results']['9+0i'][0]
        count = len(m['symbolic_archive']['expressions'])
        self.assertEqual(engine.import_numeric_construction(m, 'rational', real_alias), power)
        self.assertEqual(engine.import_numeric_construction(m, 'complex', complex_alias), power)
        self.assertEqual(len(m['symbolic_archive']['expressions']), count)
        drain_imports(m)
        count = len(m['symbolic_archive']['expressions'])
        drain_imports(m)
        self.assertEqual(len(m['symbolic_archive']['expressions']), count)
        self.assertEqual(engine.archive_link_audit(m)['issues'], 0)

    def test_kernel_totals_cover_domains_outcomes_and_nexus_context(self):
        m = memory()
        engine.operate(Fraction(2), '+', Fraction(3), tracking=m)
        engine.complex_operate((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)), '*', tracking=m)
        engine.symbolic_apply(sp.Integer(2), 'sqrt', tracking=m)
        engine.operate(Fraction(1), '/', Fraction(0), tracking=m)
        engine.symbolic_apply(sp.Integer(2), '**', sp.Integer(100), tracking=m)
        engine.evaluate_tree({'op': '+', 'left': {'leaf': 0}, 'right': {'leaf': 1}}, tracking=m)
        runtime = m['archive_integration']['runtime_operations']
        self.assertEqual((runtime['attempts'], runtime['succeeded'], runtime['blocked'], runtime['limited']), (6, 4, 1, 1))
        self.assertEqual({d: c['attempts'] for d, c in runtime['by_archive'].items()},
                         {'rational': 3, 'complex': 1, 'symbolic': 2})
        self.assertEqual(runtime['by_archive']['rational']['by_context']['zero_nexus_transform_v1']['attempts'], 1)
        self.assertEqual(runtime['attempts'], sum(runtime[k] for k in ('succeeded', 'blocked', 'limited')))
        before = copy.deepcopy(runtime)
        with contextlib.redirect_stdout(io.StringIO()):
            engine.query_unified(m, 'sqrt(2)')
            engine.print_operation_totals(m)
        self.assertEqual(runtime, before)

    def test_archive_totals_survive_journal_suppression_and_reindex(self):
        m = memory()
        zero, one = foundation(m, 1)
        with mock.patch.object(engine, 'MAX_JOURNAL_EVENTS_PER_RUN', 0):
            engine.combine(m, zero, one, '+', 'tracked_route', {'new': 0, 'observer_added': 0})
        counts = m['archive_integration']['archive_totals']
        self.assertEqual(counts['records'], sum(len(engine.archive_records(m, d)) for d in ('rational', 'complex', 'symbolic')))
        self.assertGreater(m['archive_integration']['runtime_operations']['attempts'], 0)
        before = copy.deepcopy(counts)
        engine.upgrade_archive_integration(m)
        self.assertEqual(counts, before)
        self.assertGreater(m['genesis']['suppressed_events'], 0)

    def test_deferred_import_is_visible_and_retried_after_limit_change(self):
        m = memory()
        _, one = foundation(m, 1)
        idx = engine.combine(m, one, one, '+', 'deep_legacy', {'new': 0, 'observer_added': 0})
        m['expressions'][idx]['depth'] = engine.MAX_DEPTH + 1
        drain_imports(m)
        self.assertIn(str(idx), m['symbolic_archive']['import_deferred']['rational'])
        with mock.patch.object(engine, 'MAX_DEPTH', engine.MAX_DEPTH + 2):
            drain_imports(m)
        self.assertNotIn(str(idx), m['symbolic_archive']['import_deferred']['rational'])
        self.assertIn(str(idx), m['symbolic_archive']['source_import_links']['rational'])

    def test_real_upgrade_preserves_old_records_and_fills_all_source_links(self):
        old = load_engine('zero_theoremV4.6.3.py', 'legacy_engine_for_upgrade')
        with tempfile.TemporaryDirectory() as folder:
            path = str(Path(folder) / 'memory.json')
            with mock.patch.object(old, 'memory_path', return_value=path):
                run_quietly(old)
                run_quietly(old)
                original = old.load_memory()
            with mock.patch.object(engine, 'memory_path', return_value=path):
                run_quietly(engine)
                m = engine.load_memory()
                for domain in ('rational', 'complex', 'symbolic'):
                    for before, after in zip(engine.archive_records(original, domain), engine.archive_records(m, domain)):
                        for field in ('id', 'expr', 'value', 'parents', 'pathway'):
                            self.assertEqual(before[field], after[field])
                        if 'construction' in before:
                            self.assertEqual(before['construction'], after['construction'])
                drain_imports(m)
                for domain in ('rational', 'complex'):
                    self.assertEqual(len(m['symbolic_archive']['source_import_links'][domain]),
                                     len(engine.archive_records(m, domain)))
                self.assertEqual(engine.archive_link_audit(m)['issues'], 0)
                self.assertEqual(m['archive_integration']['runtime_operations']['boundary']['previous_runs'], 2)
                self.assertTrue(m['archive_integration']['runtime_operations']['boundary']['historical_attempts_not_reconstructed'])
                totals = copy.deepcopy(m['archive_integration']['archive_totals'])
                engine.save_memory(m)
                reloaded = engine.load_memory()
                engine.upgrade_symbolic(reloaded)
                engine.upgrade_archive_integration(reloaded)
                self.assertEqual(reloaded['archive_integration']['archive_totals'], totals)
                self.assertEqual(engine.archive_link_audit(reloaded)['issues'], 0)

    def test_actual_continuation_and_forced_budget_pauses_keep_all_indexes_valid(self):
        with tempfile.TemporaryDirectory() as folder:
            with mock.patch.object(engine, 'memory_path', return_value=str(Path(folder) / 'm.json')):
                for _ in range(5):
                    run_quietly(engine)
                with mock.patch.object(engine, 'MAX_NEW_EXPRESSIONS_PER_RUN', 3):
                    for _ in range(3):
                        run_quietly(engine)
                m = engine.load_memory()
                self.assertEqual(len(m['runs']), 8)
                self.assertGreater(m['tangent_ledger']['paused'], 0)
                self.assertEqual(engine.archive_link_audit(m)['issues'], 0)
                totals = m['archive_integration']['archive_totals']
                self.assertEqual(totals['records'], sum(len(engine.archive_records(m, d)) for d in ('rational', 'complex', 'symbolic')))
                runtime = m['archive_integration']['runtime_operations']
                self.assertEqual(runtime['attempts'], sum(c['attempts'] for c in runtime['by_archive'].values()))
                self.assertTrue(all(runtime['by_archive'][d]['attempts'] > 0 for d in ('rational', 'complex', 'symbolic')))


if __name__ == '__main__':
    unittest.main()
