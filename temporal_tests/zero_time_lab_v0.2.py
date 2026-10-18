"""Zero Time Lab 0.2 — exact recovery requires a unique supported time.

Run without arguments for the blinded demo; --self-test runs verification.
Custom evidence: python zero_time_lab.py --input evidence.json
Optional --output report.json creates a NEW report (never overwrites).

This is a standalone experimental Z0 gateway, not a patch of the engine.
Timestamp observations are typed evidence, never numerical zero replacements.
"""
import argparse
import copy
import itertools
import json
from pathlib import Path
import random
import sys
import unittest

RULE = 'zero_temporal_constraints_lab_v1'
MAX_COORDINATES = 64
MAX_EVIDENCE = 512


def text(value):
    if not isinstance(value, str) or not value:
        raise ValueError('Expected nonempty identity string')
    return value


def integer(value):
    if type(value) is not int:
        raise ValueError('Times and bounds must be exact integers')
    return value


def zero_core(domain, *, operation, payload):
    """Only public solver entry: validate and pass copies through typed Z0.

    Identity passage preserves evidence. It supplies no missing information.
    Every edge and inferred result records its passage; proof IDs refer to the
    copied input evidence ledger. There is no hidden-reference argument.
    """
    if domain != 'temporal' or operation not in ('infer', 'explore'):
        raise ValueError('Unsupported temporal gateway operation')
    data = copy.deepcopy(payload)
    if operation == 'explore':
        return _explore(data)
    return _infer(data)


def _infer(data):
    if not isinstance(data, dict) or type(data.get('schema')) is not int or data['schema'] != 1:
        raise ValueError('Expected temporal schema 1')
    clocks, events, evidence = data['clocks'], data['events'], data['evidence']
    if not isinstance(clocks, dict) or not isinstance(events, list) or not isinstance(evidence, list):
        raise ValueError('Invalid ledger collections')
    if len(evidence) > MAX_EVIDENCE:
        raise ValueError('Lab evidence limit exceeded')
    for clock_id, clock in clocks.items():
        text(clock_id)
        if clock['kind'] not in ('wall', 'monotonic', 'cpu', 'logical'):
            raise ValueError('Unknown clock kind')
        for field in ('unit', 'session', 'epoch'):
            text(clock[field])
        # Each ID identifies a fixed unit/session/epoch. No implicit conversions.
    nodes, identities, event_map = [], set(), {}
    for event in events:
        event_id = text(event['id'])
        if event_id in event_map:
            raise ValueError('Duplicate event ID')
        if event['kind'] not in ('creation', 'use', 'operation', 'boundary'):
            raise ValueError('Unknown event kind')
        if not isinstance(event['records'], list):
            raise ValueError('Expected typed record references')
        for record in event['records']:
            text(record['archive'])
            integer(record['id'])
            if record['id'] < 0:
                raise ValueError('Negative archive ID')
        if not isinstance(event['clocks'], list) or not event['clocks']:
            raise ValueError('Expected event clock identities')
        for clock in event['clocks']:
            if clock not in clocks or (event_id, clock) in identities:
                raise ValueError('Unknown or duplicate event clock')
            identities.add((event_id, clock))
            nodes.append((event_id, clock))
        event_map[event_id] = event
    if len(nodes) > MAX_COORDINATES:
        raise ValueError('Lab coordinate limit exceeded')
    # Node 0 is a mathematical reference for absolute bounds, not an observation.
    indices = {node: i + 1 for i, node in enumerate(nodes)}
    n = len(nodes) + 1
    distances = [[None] * n for _ in range(n)]
    proofs = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    passages = []
    ledger, seen = [], set()

    def endpoint(value):
        key = (value['event'], value['clock'])
        if key not in indices:
            raise ValueError('Unknown event coordinate')
        return indices[key]

    def edge(a, b, bound, evidence_id):
        # x[b] - x[a] <= bound
        current = distances[a][b]
        if current is None or bound < current:
            distances[a][b] = bound
            proofs[a][b] = [evidence_id]
        passages.append({'zero_nexus': 'Z0', 'rule': RULE,
                         'evidence': evidence_id, 'effect': 'identity_constraint_passage'})

    for row in evidence:
        evidence_id = text(row['id'])
        if evidence_id in seen:
            raise ValueError('Duplicate evidence ID')
        seen.add(evidence_id)
        text(row['source'])
        ledger.append(row)
        kind = row['kind']
        if kind == 'bound':
            target = endpoint(row['at'])
            lower, upper = row.get('lower'), row.get('upper')
            if lower is None and upper is None:
                raise ValueError('Empty bound evidence')
            if lower is not None:
                edge(target, 0, -integer(lower), evidence_id)
            if upper is not None:
                edge(0, target, integer(upper), evidence_id)
        elif kind in ('difference', 'bridge'):
            a, b = endpoint(row['a']), endpoint(row['b'])
            ca, cb = row['a']['clock'], row['b']['clock']
            if kind == 'difference' and ca != cb:
                raise ValueError('Cross-clock relation requires explicit bridge evidence')
            if kind == 'bridge':
                if ca == cb or clocks[ca]['unit'] != clocks[cb]['unit']:
                    raise ValueError('Bridge requires distinct clocks with matching units')
            lower, upper = row.get('lower'), row.get('upper')
            if lower is None and upper is None:
                raise ValueError('Empty difference evidence')
            if lower is not None:
                edge(b, a, -integer(lower), evidence_id)
            if upper is not None:
                edge(a, b, integer(upper), evidence_id)
        else:
            raise ValueError('Unknown evidence kind')

    # All-pairs difference-constraint closure. Integer arithmetic is exact.
    # Caps make this O(n^3) experiment bounded on a phone.
    for k in range(n):
        for i in range(n):
            if distances[i][k] is None:
                continue
            for j in range(n):
                if distances[k][j] is None:
                    continue
                candidate = distances[i][k] + distances[k][j]
                if distances[i][j] is None or candidate < distances[i][j]:
                    distances[i][j] = candidate
                    proofs[i][j] = list(dict.fromkeys(proofs[i][k] + proofs[k][j]))
        conflicts = [i for i in range(n) if distances[i][i] < 0]
        if conflicts:
            return {'schema': 1, 'rule': RULE, 'zero_nexus': 'Z0',
                    'status': 'contradiction', 'intervals': [],
                    'conflict_evidence': sorted({p for i in conflicts for p in proofs[i][i]}),
                    'evidence': ledger, 'passages': passages,
                    'note': 'Conflicting evidence retained; no repaired timestamp accepted.'}

    intervals = []
    for node, i in indices.items():
        lower = None if distances[i][0] is None else -distances[i][0]
        upper = distances[0][i]
        status = ('unknown' if lower is None and upper is None else
                  'exact' if lower is not None and lower == upper else 'bounded')
        intervals.append({'event': node[0], 'clock': node[1], 'lower': lower,
                          'upper': upper, 'status': status,
                          'lower_evidence': proofs[i][0], 'upper_evidence': proofs[0][i],
                          'zero_core_passage': {'zero_nexus': 'Z0', 'rule': RULE,
                                                'effect': 'derived_temporal_constraint'}})
    relations = []
    for a, ai in indices.items():
        for b, bi in indices.items():
            if a >= b or a[1] != b[1]:
                continue
            lo = None if distances[bi][ai] is None else -distances[bi][ai]
            hi = distances[ai][bi]
            if lo is None and hi is None:
                continue
            relations.append({'a': a[0], 'b': b[0], 'clock': a[1],
                              'difference_lower': lo, 'difference_upper': hi,
                              'a_before_or_at_b': lo is not None and lo >= 0,
                              'b_before_or_at_a': hi is not None and hi <= 0,
                              'lower_evidence': proofs[bi][ai],
                              'upper_evidence': proofs[ai][bi],
                              'zero_nexus': 'Z0', 'rule': RULE})
    return {'schema': 1, 'rule': RULE, 'zero_nexus': 'Z0', 'status': 'consistent',
            'intervals': intervals, 'evidence': ledger, 'passages': passages,
            'clocks': clocks, 'relative_constraints': relations,
            'boundary': 'Conditional on supplied evidence; no target, no historical backfill.'}


def clock(kind='monotonic', session='lab-session', unit='ns', epoch='lab-epoch'):
    return dict(kind=kind, session=session, unit=unit, epoch=epoch)


def event(identity, kind='operation', clocks=('m',), record_id=1):
    return dict(id=identity, kind=kind, clocks=list(clocks),
                records=[{'archive': 'rational', 'id': record_id}])


def bound(identity, target, lower=None, upper=None, clock_id='m'):
    return dict(id=identity, kind='bound', at={'event': target, 'clock': clock_id},
                lower=lower, upper=upper, source='lab recorded observation')


def difference(identity, a, b, lower=0, upper=None, clock_id='m'):
    return dict(id=identity, kind='difference', a={'event': a, 'clock': clock_id},
                b={'event': b, 'clock': clock_id}, lower=lower, upper=upper,
                source='lab recorded causal relation')


def infer(data):
    return zero_core('temporal', operation='infer', payload=data)


def explore(data, target, initial_ids, *, batch_size=2, max_batches=100):
    """Process a finite surviving evidence queue; no hidden original is accepted.

    An interval is unresolved. Exact support is accepted only after all supplied
    evidence has been checked. Every pass computes full constraint closure for
    the evidence inspected so far; repeating a pass alone adds no information.
    """
    return zero_core('temporal', operation='explore', payload={
        'data': data, 'target': target, 'initial_ids': list(initial_ids),
        'batch_size': batch_size, 'max_batches': max_batches})


def _explore(request):
    data = request['data']
    for key in ('batch_size', 'max_batches'):
        integer(request[key])
        if request[key] < 1:
            raise ValueError('Positive exploration budgets required')
    ids = [r['id'] for r in data['evidence']]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate evidence ID')
    initial_ids = request['initial_ids']
    if len(set(initial_ids)) != len(initial_ids) or not set(initial_ids) <= set(ids):
        raise ValueError('Invalid initial evidence IDs')
    # Preserve the supplied queue order; never schedule by the hidden answer.
    active = [r for r in data['evidence'] if r['id'] in initial_ids]
    pending = [r for r in data['evidence'] if r['id'] not in initial_ids]
    history, batches = [], 0
    while True:
        current = dict(data, evidence=active)
        result = infer(current)
        if result['status'] == 'contradiction':
            return {'status': 'contradiction', 'accepted_timestamp': None,
                    'trace': history, 'result': result,
                    'pending_evidence_ids': [r['id'] for r in pending]}
        target = request['target']
        row = lookup(result, target['event'], target['clock'])
        history.append({'step': batches, 'lower': row['lower'], 'upper': row['upper'],
                        'uniquely_supported': row['status'] == 'exact',
                        'lower_evidence': row['lower_evidence'],
                        'upper_evidence': row['upper_evidence'],
                        'checked_evidence_count': len(active),
                        'pending_evidence_count': len(pending),
                        'zero_nexus': 'Z0', 'rule': RULE})
        if not pending or batches >= request['max_batches']:
            complete = not pending
            accepted = complete and row['status'] == 'exact'
            return {'status': 'exact_supported' if accepted else 'unresolved',
                    'accepted_timestamp': row['lower'] if accepted else None,
                    'stop_reason': 'supplied_evidence_exhausted' if complete else 'work_budget',
                    'trace': history, 'result': result,
                    'pending_evidence_ids': [r['id'] for r in pending]}
        count = request['batch_size']
        active = active + pending[:count]
        pending = pending[count:]
        batches += 1


def fixture():
    # IDs distinguish the creation and separate uses of rational record #1.
    return {'schema': 1, 'clocks': {'m': clock()},
            'events': [event('boundary', 'boundary'), event('create-1', 'creation'),
                       event('use-1-A', 'use'), event('use-1-B', 'use')],
            'evidence': [bound('observed-boundary', 'boundary', 100, 100),
                         bound('observed-use-A', 'use-1-A', 140, 140),
                         bound('observed-use-B', 'use-1-B', 160, 160),
                         difference('boundary-before-creation', 'boundary', 'create-1'),
                         difference('created-before-use-A', 'create-1', 'use-1-A'),
                         difference('created-before-use-B', 'create-1', 'use-1-B')]}


def lookup(result, identity, clock_id='m'):
    return next(r for r in result['intervals']
                if (r['event'], r['clock']) == (identity, clock_id))


def demo():
    # The original is in the harness only. No truth field reaches infer().
    original = 125
    intact = fixture()
    intact['evidence'].append(bound('hidden-creation-time', 'create-1', original, original))
    damaged = copy.deepcopy(intact)
    damaged['evidence'] = [r for r in damaged['evidence'] if r['id'] != 'hidden-creation-time']
    result = infer(damaged)
    row = lookup(result, 'create-1')
    result['held_out_check'] = {
        'original_hidden_from_solver': original,
        'interval_contains_original': row['lower'] <= original <= row['upper'],
        'exact_restoration': row['lower'] == row['upper'] == original,
        'scope': 'Synthetic blinded experiment; no live memory used.'}
    return result


def progressive_fixture():
    """Predeclared synthetic observations, all generated before any masking.

    None of these individual uncertain duration observations fixes creation
    uniquely. Their intersection does. Every timestamp is retained except the
    selected creation timestamp, which the harness holds outside the solver.
    """
    data = fixture()
    initial_ids = [r['id'] for r in data['evidence']]
    for name, stamp, gap_lower, gap_upper in (
            ('tangent-A', 135, 5, 15), ('operation-B', 150, 24, 26),
            ('reuse-C', 160, 34, 35), ('tangent-D', 180, 55, 56)):
        data['events'].append(event(name, 'use' if name == 'reuse-C' else 'operation'))
        data['evidence'].append(bound('stamp-' + name, name, stamp, stamp))
        data['evidence'].append(difference('gap-' + name, 'create-1', name,
                                           gap_lower, gap_upper))
    return data, initial_ids


def progressive_demo():
    original = 125  # Test harness only; not passed to explore or infer.
    intact, initial_ids = progressive_fixture()
    intact['evidence'].append(bound('hidden-creation-time', 'create-1', original, original))
    damaged = copy.deepcopy(intact)
    damaged['evidence'] = [r for r in damaged['evidence'] if r['id'] != 'hidden-creation-time']
    result = explore(damaged, {'event': 'create-1', 'clock': 'm'}, initial_ids)
    result['held_out_check'] = {
        'original_hidden_from_solver': original,
        'exact_recovery_verified': result['status'] == 'exact_supported'
                                   and result['accepted_timestamp'] == original,
        'scope': 'Synthetic test only; matching an interval is not recovery success.'}
    return result


class LabTests(unittest.TestCase):
    def test_progressive_exact_recovery(self):
        result = progressive_demo()
        self.assertEqual([(r['lower'], r['upper']) for r in result['trace']],
                         [(100, 140), (120, 130), (124, 126), (125, 126), (125, 125)])
        self.assertEqual(result['status'], 'exact_supported')
        self.assertTrue(result['held_out_check']['exact_recovery_verified'])
        self.assertNotIn('hidden-creation-time',
                         [r['id'] for r in result['result']['evidence']])

    def test_interval_is_not_success(self):
        data = fixture()
        result = explore(data, {'event': 'create-1', 'clock': 'm'},
                         [r['id'] for r in data['evidence']])
        self.assertEqual(result['status'], 'unresolved')
        self.assertIsNone(result['accepted_timestamp'])

    def test_budget_preserves_unresolved_evidence(self):
        data, ids = progressive_fixture()
        before = copy.deepcopy(data)
        result = explore(data, {'event': 'create-1', 'clock': 'm'}, ids, max_batches=1)
        self.assertEqual(data, before)
        self.assertEqual(result['status'], 'unresolved')
        self.assertEqual(result['stop_reason'], 'work_budget')
        self.assertEqual(len(result['pending_evidence_ids']), 6)

    def test_later_conflict_prevents_acceptance(self):
        data, ids = progressive_fixture()
        data['evidence'].append(bound('conflicting-late-evidence', 'create-1', 126, 126))
        result = explore(data, {'event': 'create-1', 'clock': 'm'}, ids)
        self.assertEqual(result['status'], 'contradiction')
        self.assertIsNone(result['accepted_timestamp'])

    def test_exact_before_budget_not_yet_accepted(self):
        data, ids = progressive_fixture()
        data['evidence'].append(bound('late-consistent-evidence', 'use-1-A', 140, 140))
        result = explore(data, {'event': 'create-1', 'clock': 'm'}, ids, max_batches=4)
        self.assertTrue(result['trace'][-1]['uniquely_supported'])
        self.assertEqual(result['status'], 'unresolved')
        self.assertIsNone(result['accepted_timestamp'])

    def test_interval_and_proof(self):
        r = infer(fixture())
        row = lookup(r, 'create-1')
        self.assertEqual((row['lower'], row['upper']), (100, 140))
        self.assertEqual(set(row['lower_evidence']),
                         {'observed-boundary', 'boundary-before-creation'})
        self.assertEqual(set(row['upper_evidence']),
                         {'observed-use-A', 'created-before-use-A'})

    def test_no_invented_lower_bound(self):
        data = fixture()
        data['evidence'] = data['evidence'][1:3] + data['evidence'][4:]
        self.assertIsNone(lookup(infer(data), 'create-1')['lower'])

    def test_no_anchors_unknown(self):
        data = fixture()
        data['evidence'] = data['evidence'][3:]
        result = infer(data)
        self.assertEqual(lookup(result, 'create-1')['status'], 'unknown')
        relation = next(r for r in result['relative_constraints']
                        if r['a'] == 'create-1' and r['b'] == 'use-1-A')
        self.assertTrue(relation['a_before_or_at_b'])

    def test_exact_from_recorded_duration(self):
        data = fixture()
        data['evidence'].append(difference('observed-gap', 'create-1', 'use-1-A', 15, 15))
        row = lookup(infer(data), 'create-1')
        self.assertEqual((row['lower'], row['upper']), (125, 125))

    def test_conflict_no_output_times(self):
        data = fixture()
        data['evidence'].append(bound('bad-creation', 'create-1', 150, 150))
        result = infer(data)
        self.assertEqual(result['status'], 'contradiction')
        self.assertEqual(result['intervals'], [])
        self.assertIn('bad-creation', result['conflict_evidence'])

    def test_negative_cycle_without_anchors(self):
        data = fixture()
        data['evidence'] = [difference('ab', 'create-1', 'use-1-A', 1),
                            difference('ba', 'use-1-A', 'create-1', 1)]
        self.assertEqual(infer(data)['status'], 'contradiction')

    def test_clocks_never_implicitly_connected(self):
        data = fixture()
        data['clocks']['w'] = clock('wall')
        data['events'][1]['clocks'].append('w')
        self.assertEqual(lookup(infer(data), 'create-1', 'w')['status'], 'unknown')

    def test_explicit_bridge_with_uncertainty(self):
        data = fixture()
        data['clocks']['w'] = clock('wall')
        data['events'][1]['clocks'].append('w')
        data['evidence'].append(dict(id='calibration', kind='bridge',
            a={'event': 'create-1', 'clock': 'm'},
            b={'event': 'create-1', 'clock': 'w'}, lower=1000, upper=1005,
            source='explicit recorded calibration interval'))
        row = lookup(infer(data), 'create-1', 'w')
        self.assertEqual((row['lower'], row['upper']), (1100, 1145))

    def test_cross_session_unconnected(self):
        data = fixture()
        data['clocks']['next'] = clock(session='next-session')
        data['events'].append(event('restart', clocks=('next',)))
        self.assertEqual(lookup(infer(data), 'restart', 'next')['status'], 'unknown')

    def test_wall_jump_not_ordered_by_list(self):
        data = {'schema': 1, 'clocks': {'w': clock('wall')},
                'events': [event('earlier', clocks=('w',)), event('later', clocks=('w',))],
                'evidence': [bound('a', 'earlier', 200, 200, 'w'),
                             bound('b', 'later', 100, 100, 'w')]}
        self.assertEqual(infer(data)['status'], 'consistent')

    def test_four_clock_types(self):
        data = {'schema': 1, 'clocks': {k: clock(k, unit='tick' if k == 'logical' else 'ns')
                for k in ('wall', 'monotonic', 'cpu', 'logical')},
                'events': [event('x', clocks=('wall', 'monotonic', 'cpu', 'logical'))],
                'evidence': [bound('anchor', 'x', 7, 7, 'logical')]}
        result = infer(data)
        self.assertEqual(sum(r['status'] == 'unknown' for r in result['intervals']), 3)

    def test_no_source_mutation(self):
        data = fixture()
        before = copy.deepcopy(data)
        infer(data)
        self.assertEqual(data, before)

    def test_bad_types_and_duplicate_ids(self):
        for value in (True, 1.5, '100'):
            data = fixture()
            data['evidence'][0]['lower'] = value
            with self.assertRaises(ValueError): infer(data)
        data = fixture()
        data['events'].append(copy.deepcopy(data['events'][0]))
        with self.assertRaises(ValueError): infer(data)

    def test_bad_links_and_units(self):
        data = fixture()
        data['evidence'][0]['at']['event'] = 'missing'
        with self.assertRaises(ValueError): infer(data)
        data = fixture()
        data['clocks']['tick'] = clock('logical', unit='tick')
        data['events'][0]['clocks'].append('tick')
        data['evidence'].append(dict(id='invalid', kind='bridge', source='test',
            a={'event': 'boundary', 'clock': 'm'},
            b={'event': 'boundary', 'clock': 'tick'}, lower=0))
        with self.assertRaises(ValueError): infer(data)

    def test_blind_demo(self):
        result = demo()
        self.assertTrue(result['held_out_check']['interval_contains_original'])
        self.assertFalse(result['held_out_check']['exact_restoration'])

    def test_unknown_record_not_merged_by_value(self):
        data = fixture()
        data['events'].append(event('another-1', 'creation', record_id=2))
        self.assertEqual(lookup(infer(data), 'another-1')['status'], 'unknown')

    def test_permutation_invariance(self):
        data = fixture()
        expected = [(r['lower'], r['upper']) for r in infer(data)['intervals']]
        data['evidence'].reverse()
        self.assertEqual([(r['lower'], r['upper']) for r in infer(data)['intervals']], expected)

    def test_budget(self):
        data = fixture()
        data['events'] = [event(str(i)) for i in range(MAX_COORDINATES + 1)]
        with self.assertRaises(ValueError): infer(data)

    def test_exhaustive_independent_oracle(self):
        # Independent exhaustive enumeration, not another shortest-path solver.
        # 80 randomized networks, 125 candidate assignments each.
        rng = random.Random(1019)
        for _ in range(80):
            names = ('a', 'b', 'c')
            rows = [bound('box-' + x, x, 0, 4) for x in names]
            relations = []
            for index in range(4):
                a, b = rng.sample(range(3), 2)
                lo = rng.randint(-4, 4)
                hi = rng.randint(lo, 4)
                relations.append((a, b, lo, hi))
                rows.append(difference('d' + str(index), names[a], names[b], lo, hi))
            solutions = [v for v in itertools.product(range(5), repeat=3)
                         if all(lo <= v[b] - v[a] <= hi for a, b, lo, hi in relations)]
            result = infer({'schema': 1, 'clocks': {'m': clock()},
                            'events': [event(x) for x in names], 'evidence': rows})
            if not solutions:
                self.assertEqual(result['status'], 'contradiction')
            else:
                self.assertEqual(result['status'], 'consistent')
                for i, x in enumerate(names):
                    row = lookup(result, x)
                    self.assertEqual((row['lower'], row['upper']),
                                     (min(v[i] for v in solutions), max(v[i] for v in solutions)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(LabTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1
    report = infer(json.loads(args.input.read_text(encoding='utf-8'))) if args.input else progressive_demo()
    rendered = json.dumps(report, indent=2)
    if args.output:
        # Exclusive creation also rejects input aliases, existing reports/symlinks.
        with args.output.open('x', encoding='utf-8') as stream:
            stream.write(rendered + '\n')
    if args.input:
        print(rendered)
    else:
        print('ZERO TIME LAB 0.2 | Z0 | synthetic blinded exact-recovery experiment')
        for row in report['trace']:
            print('Step', row['step'], '| creation interval:', row['lower'], '..', row['upper'],
                  '| evidence still queued:', row['pending_evidence_count'])
        print('Recovery status:', report['status'])
        print('Accepted timestamp:', report['accepted_timestamp'])
        print('Held-out original:', report['held_out_check']['original_hidden_from_solver'], 'ns')
        print('Exact recovery independently checked:', report['held_out_check']['exact_recovery_verified'])
        print('Lab only. No engine memory opened or changed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
