# ============================================================
# ZERO THEOREM V4.6.2 - ZERO ARCHIVE ACCESS / LINEAGE / FEEDBACK
# A runnable continuation of V2.2's interconnected architecture
# ============================================================
# Python 3 + SymPy. Keeps V2.2/V3.x files untouched.
# Work is bounded PER RUN, with a persistent queue for continuation.
# This is a computational exploration model, not a mathematical proof.

import json
import os
import time
from collections import deque
from fractions import Fraction

VERSION = '4.1'  # Memory-format compatibility; runtime version is V4.6.2.
MEMORY_FILENAME = 'zero_theorem_rabbitholes_v41_memory.json'
WORK_PER_RUN = 90
COMPLEX_WORK_PER_RUN = 24
MAX_JOURNAL_EVENTS_PER_RUN = 2400
EMERGENCE_EVENTS_PER_RUN = 3
NEXUS_WORK_PER_RUN = 36
MAX_NEW_EXPRESSIONS_PER_RUN = 400
MAX_DEPTH = 4
MAX_BITS = 256
MAX_OBSERVER_PROPOSALS_PER_RUN = 160
OPERATIONS = ('+', '-', '*', '/')
REFERENCE_INPUT = '00404'
SYMBOLIC_WORK_PER_RUN = 24
SYMBOLIC_IMPORT_PER_RUN = 24  # per source archive; cursors persist
SYMBOLIC_MAX_NODES = 48
SYMBOLIC_MAX_POWER = 8
SYMBOLIC_MAX_ROOT_BITS = 32
SYMBOLIC_BINARY_OPERATIONS = ('*', '**', '+', '-', '/')


def number(value):
    if isinstance(value, Fraction):
        return value
    return Fraction(str(value))


def encode(value):
    value = number(value)
    return str(value.numerator) if value.denominator == 1 else str(value.numerator) + '/' + str(value.denominator)


def operate(a, op, b):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0: return None
        return a / b
    raise ValueError('Unsupported operation')


def digit_breakdown(text):
    if not text or not text.isdigit():
        raise ValueError('Expected digit string')
    return ''.join('0' if c == '0' else '1' * int(c) for c in text)


def positional_slots(text):
    if not text or not text.isdigit():
        raise ValueError('Expected digit string')
    slots = []
    for position, digit in enumerate(text, 1):
        if digit == '0':
            slots.append({'source_position': position, 'source_digit': digit,
                          'kind': 'persistent_zero', 'unit': None})
        else:
            for unit in range(1, int(digit) + 1):
                slots.append({'source_position': position, 'source_digit': digit,
                              'kind': 'unit_slot', 'unit': unit})
    return slots


def foundation():
    # The recognition of zero is registered without consuming the zero nexus.
    states = [0]
    zeros = [{'id': 'Z0', 'generation': 0, 'purpose': 'persistent_nexus'}]
    events = []
    for generation in range(1, 5):
        next_state = len(states)
        events.append({'event': 'RH-%03d' % generation,
                       'from': states[-1], 'to': next_state,
                       'rule': 'registered_state_count',
                       'zero_used': zeros[-1]['id']})
        states.append(next_state)
        zeros.append({'id': 'Z%d' % generation, 'generation': generation,
                      'purpose': 'fresh_zero_operation_record'})
    return {'states': states, 'trinity': [0, 1, 2],
            'zero_records': zeros, 'transitions': events,
            'rule': 'foundation_state_count_v3'}


def empty_memory():
    f = foundation()
    m = {'schema': 1, 'version': VERSION, 'runs': [], 'foundation': f,
         'expressions': [], 'queue': [], 'queue_head': 0,
         'known_expression_keys': [], 'results': {},
         'network': {'state_observations': 0, 'unique_states': {},
                     'operation_counts': {o: 0 for o in OPERATIONS},
                     'transitions': {}, 'tangents': {},
                     'zero_occurrences': 0, 'shared_counter_accesses': 0},
         'observer': {'proposals': [], 'variable_store': {},
                      'role_counts': {'value': 0, 'variable': 0,
                                      'operation': 0, 'combined': 0}},
         'blocked': [], 'zero_proposals': [], 'rule_registry': {
             'foundation_state_count_v3': {'status': 'established'},
             'consume_v1': {'status': 'active_exploration'},
             'reuse_v1': {'status': 'active_exploration'},
             'revisit_v1': {'status': 'active_exploration'},
             'zero_slot_proposal_v1': {'status': 'experimental_unapproved'},
             'observer_operation_selection_v22': {'status': 'candidate_only'}},
         'reference': {'input': REFERENCE_INPUT,
                       'breakdown': digit_breakdown(REFERENCE_INPUT),
                       'slots': positional_slots(REFERENCE_INPUT)}}
    # Start from zero alone; register later states as events.
    f['states'] = [0]
    f['zero_records'] = [f['zero_records'][0]]
    f['transitions'] = []
    m['emergence_events'] = []
    m['nexus_events'] = []
    m['nexus_pending'] = []
    for n in f['states']:
        add_expression(m, {'expr': str(n), 'value': str(n), 'tree': {'leaf': n},
                           'depth': 0, 'parents': [], 'leaves': [n],
                           'pathway': 'foundation_state_count_v3',
                           'ancestry': [], 'domain': 'rational'})
    # The first emergence and exploration opportunities are scheduled by
    # the registration mechanism, not hard-coded as five starting states.
    enqueue(m, {'kind': 'emerge'})
    return m


def add_expression(m, record):
    # A key includes the rule and construction tree. Numerical equality alone
    # must NEVER merge distinct expression trees.
    key = json.dumps([record['pathway'], record['tree']], sort_keys=True,
                     separators=(',', ':'))
    if key in m['_keys'] if '_keys' in m else key in m['known_expression_keys']:
        if 'genesis' in m:
            m['tangent_ledger']['duplicate_expressions'] = m['tangent_ledger'].get('duplicate_expressions', 0) + 1
            journal(m, 'duplicate_expression', value=record['value'], pathway=record['pathway'])
        return None
    if '_keys' in m: m['_keys'].add(key)
    m['known_expression_keys'].append(key)
    idx = len(m['expressions'])
    record['id'] = idx
    m['expressions'].append(record)
    m['results'].setdefault(record['value'], []).append(idx)
    if 'genesis' in m:
        journal(m, 'expression_created', expression_id=idx, value=record['value'], pathway=record['pathway'], parents=record.get('parents', []), first_value=(len(m['results'][record['value']]) == 1))
    if 'v45_observations' in m:
        observe_v45_real(m, record)
    if 'zero_runtime' in m:
        schedule_zero_sources(m)
    return idx


def task_key(task):
    return json.dumps(task, sort_keys=True, separators=(',', ':'))


def rebalance_queue(m):
    """Deduplicate pending tasks only, retaining their first occurrence.
    Previously completed work is never deleted from the archive.
    """
    pending = m['queue'][m['queue_head']:]
    kinds = ('symbolic_root', 'symbolic_pair', 'symbolic_nexus', 'symbolic_position', 'frontier', 'pair', 'nexus', 'zero_scan', 'zero_source', 'position', 'complex', 'complex_feedback', 'consume_op',
             'revisit', 'consume', 'emerge')
    buckets = {kind: deque() for kind in kinds}
    keys = set()
    removed = 0
    for task in pending:
        key = task_key(task)
        if key in keys:
            removed += 1
            continue
        keys.add(key)
        buckets[task['kind']].append(task)
    balanced = []
    while any(buckets.values()):
        for kind in kinds:
            if buckets[kind]:
                balanced.append(buckets[kind].popleft())
    m['queue'], m['queue_head'] = balanced, 0
    m['_pending_keys'] = keys
    return removed


def enqueue(m, task):
    key = task_key(task)
    keys = m.get('_pending_keys')
    if keys is not None:
        if key in keys:
            if 'tangent_ledger' in m:
                m['tangent_ledger']['duplicate_pending'] = m['tangent_ledger'].get('duplicate_pending', 0) + 1
                journal(m, 'duplicate_pending_tangent', task_key=key, kind=task['kind'])
            return False
        keys.add(key)
    m['queue'].append(task)
    if 'tangent_ledger' in m: tangent_generated(m, task)
    return True


def record_counters(m, left, right, op, result, pathway):
    net = m['network']
    before = json.dumps([left['value'], right['value']], separators=(',', ':'))
    after = result['value']
    tangent = json.dumps([before, op, after, pathway], separators=(',', ':'))
    net['state_observations'] += 1
    net['unique_states'][after] = net['unique_states'].get(after, 0) + 1
    net['operation_counts'][op] += 1
    net['transitions'][tangent] = net['transitions'].get(tangent, 0) + 1
    net['tangents'][tangent] = net['tangents'].get(tangent, 0) + 1
    net['zero_occurrences'] += int(number(left['value']) == 0) + int(number(right['value']) == 0)
    net['shared_counter_accesses'] += 1


def observe(m, rec, run_stats):
    if run_stats['observer_added'] >= MAX_OBSERVER_PROPOSALS_PER_RUN:
        return
    obs = m['observer']
    value = number(rec['value'])
    name = 'A_%d' % rec['id']
    selected = OPERATIONS[abs(value.numerator) % 4]
    proposal = {'source_id': rec['id'], 'source_expression': rec['expr'],
                'value': rec['value'], 'variable': name,
                'selected_operation': selected,
                'selection_rule': 'abs(numerator) modulo 4 (V2.2-inspired)',
                'roles': ['value', 'variable', 'operation', 'combined'],
                'status': 'evaluated_candidate_not_foundation_rule'}
    obs['proposals'].append(proposal)
    obs['variable_store'][name] = rec['value']
    for role in obs['role_counts']:
        obs['role_counts'][role] += 1
    run_stats['observer_added'] += 1
    if 'genesis' in m: journal(m, 'observer_proposal', source_id=rec['id'], selected_operation=selected, status=proposal['status'])


def zero_assist(m, left, right, op, pathway):
    # A blocked division is a concrete dead end for this operation.
    # Zero remains in the nexus; suggestions do NOT change theorem rules.
    blocked_key = (left['id'], right['id'], op, pathway)
    seen = m.setdefault('_blocked_keys', set())
    if blocked_key in seen: return
    seen.add(blocked_key)
    blocked_id = len(m['blocked'])
    m['blocked'].append({'id': blocked_id, 'left': left['id'],
                         'right': right['id'], 'operation': op,
                         'reason': 'division_by_zero', 'pathway': pathway,
                         'status': 'blocked'})
    if 'genesis' in m: journal(m, 'blocked_operation', blocked_id=blocked_id, left=left['id'], right=right['id'], operation=op, reason='division_by_zero')
    for replacement in sorted(set(m['foundation']['states']) | set(int(k) for k in m['results'] if '/' not in k and k.lstrip('-').isdigit()))[:24]:
        if replacement == 0: continue
        candidate = number(left['value']) / replacement
        m['zero_proposals'].append({
            'blocked_id': blocked_id, 'zero_record': 'Z0',
            'slot': 'denominator', 'replacement': replacement,
            'expression': '(' + left['expr'] + ' / ' + str(replacement) + ')',
            'result': encode(candidate), 'status': 'unapproved_observation',
            'construction_rule': 'zero_slot_proposal_v1'})


def combine(m, a_id, b_id, op, pathway, run_stats):
    left, right = m['expressions'][a_id], m['expressions'][b_id]
    a, b = number(left['value']), number(right['value'])
    result = operate(a, op, b)
    if result is None:
        zero_assist(m, left, right, op, pathway)
        return None
    if result.numerator.bit_length() > MAX_BITS or result.denominator.bit_length() > MAX_BITS:
        return None
    depth = max(left['depth'], right['depth']) + 1
    if depth > MAX_DEPTH: return None
    tree = {'op': op, 'left': left['tree'], 'right': right['tree']}
    expression = '(' + left['expr'] + ' ' + op + ' ' + right['expr'] + ')'
    rec = {'expr': expression, 'value': encode(result), 'tree': tree,
           'depth': depth, 'parents': [a_id, b_id],
           'leaves': left['leaves'] + right['leaves'],
           'pathway': pathway, 'domain': 'rational',
           'ancestry': left['ancestry'] + right['ancestry'] + [
               {'left_id': a_id, 'right_id': b_id, 'operation': op,
                'result': encode(result), 'rule': pathway}]}
    idx = add_expression(m, rec)
    if idx is None: return None
    record_counters(m, left, right, op, rec, pathway)
    schedule_frontier(m, idx)
    run_stats['new'] += 1
    observe(m, m['expressions'][idx], run_stats)
    # Revisit prior constructions using the newly discovered value. This is
    # bounded, deterministic and continues through the persisted task queue.
    if depth < MAX_DEPTH and len(m['queue']) - m['queue_head'] < 12000 and (result != 0 or depth == 1):
        enqueue(m, {'kind': 'revisit', 'new': idx, 'cursor': 0,
                    'rule': 'revisit_v1'})
    return idx


def work_pair(m, task, stats):
    a, b = task['left'], task['right']
    # Preserve both operand orders, even for commutative operations.
    for x, y in ((a, b), (b, a)):
        for op in OPERATIONS:
            if stats['new'] >= MAX_NEW_EXPRESSIONS_PER_RUN: return False
            combine(m, x, y, op, task['rule'], stats)
    return True


def work_consume(m, task, stats):
    items = task['items']
    if len(items) < 2 or task['depth'] >= MAX_DEPTH:
        return True
    # Schedule each construction separately so every task is atomic and
    # can be resumed without losing work or redoing partial branches.
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i], items[j]
            remaining = [v for k, v in enumerate(items) if k not in (i, j)]
            for x, y in ((a, b), (b, a)):
                for op in OPERATIONS:
                    enqueue(m, {'kind': 'consume_op', 'left': x, 'right': y,
                                'op': op, 'remaining': remaining,
                                'depth': task['depth'], 'path': task['path'],
                                'rule': 'consume_v1'})
    return True


def work_consume_op(m, task, stats):
    idx = combine(m, task['left'], task['right'], task['op'],
                  'consume_v1', stats)
    if idx is not None:
        enqueue(m, {'kind': 'consume',
                    'items': task['remaining'] + [idx],
                    'depth': task['depth'] + 1,
                    'path': task['path'] + [idx], 'rule': 'consume_v1'})
    return True


def work_revisit(m, task, stats):
    new = task['new']
    cursor = task['cursor']
    # One prior expression per task keeps scheduling fair.
    if cursor >= new: return True
    prior = cursor
    for a, b in ((new, prior), (prior, new)):
        for op in OPERATIONS:
            combine(m, a, b, op, 'revisit_v1', stats)
    if cursor + 1 < new:
        enqueue(m, {'kind': 'revisit', 'new': new,
                    'cursor': cursor + 1, 'rule': 'revisit_v1'})
    return True


# ============================================================
# V4.1 - LIVE EMERGENCE + ZERO NEXUS TRANSFORMATIONS
# ============================================================

def register_next_state(m):
    """Counting the registered states produces the next foundation state."""
    f = m['foundation']
    states = f['states']
    next_value = len(states)
    source = list(states)
    zero_id = f['zero_records'][-1]['id']
    event = {'id': 'E-%06d' % (len(m['emergence_events']) + 1),
             'counted_states': source, 'result': next_value,
             'zero_nexus': zero_id, 'rule': 'registered_state_count'}
    states.append(next_value)
    f['zero_records'].append({'id': 'Z%d' % next_value,
                              'generation': next_value,
                              'purpose': 'fresh_zero_operation_record'})
    f['transitions'].append({'event': event['id'], 'from': source[-1],
                              'to': next_value, 'rule': event['rule'],
                              'zero_used': zero_id})
    m['emergence_events'].append(event)
    if 'genesis' in m: journal(m, 'foundation_emergence', state=next_value, zero_nexus=zero_id, counted_states=source)
    idx = add_expression(m, {'expr': str(next_value),
              'value': str(next_value), 'tree': {'leaf': next_value},
              'depth': 0, 'parents': [], 'leaves': [next_value],
              'pathway': 'foundation_state_count_v3',
              'ancestry': [event], 'domain': 'rational'})
    schedule_frontier(m, idx)
    positional_nexus(m, next_value)
    # Every registration opens new arithmetic opportunities immediately.
    for prior in [m['results'][str(n)][0] for n in states]:
        enqueue(m, {'kind': 'pair', 'left': prior, 'right': idx,
                    'rule': 'reuse_v1'})
    # Consume path uses the distinct registered operand occurrences.
    if next_value <= 4:
        foundation_ids = [m['results'][str(n)][-1] for n in states]
        enqueue(m, {'kind': 'consume', 'items': foundation_ids,
                    'depth': 0, 'path': [], 'rule': 'consume_v1'})
    # Every new registered value can reach the whole existing archive.
    schedule_zero_foundation_scan(m, idx)
    enqueue(m, {'kind': 'emerge'})
    return event


def rational_tree_leaves(tree):
    if 'leaf' in tree:
        return [tree['leaf']]
    return rational_tree_leaves(tree['left']) + rational_tree_leaves(tree['right'])


def has_numeric_zero(tree):
    if 'leaf' in tree:
        return number(tree['leaf']) == 0
    return has_numeric_zero(tree['left']) or has_numeric_zero(tree['right'])


def foundation_expression_id(m, state):
    return next((idx for idx in m['results'].get(str(state), [])
                 if m['expressions'][idx]['pathway'] == 'foundation_state_count_v3'), None)


def schedule_zero_foundation_scan(m, value_id):
    runtime = m.get('zero_runtime')
    if runtime is None or value_id in runtime['foundation_scheduled']:
        return
    runtime['foundation_scheduled'].append(value_id)
    if number(m['expressions'][value_id]['value']) == 0:
        return
    enqueue(m, {'kind': 'zero_scan', 'value': value_id,
                'cursor': 0, 'stop': len(m['expressions'])})


def schedule_zero_sources(m):
    """Notify each new zero-bearing expression of already registered values."""
    runtime = m['zero_runtime']
    cursor = runtime['source_cursor']
    stop = len(m['foundation']['states'])
    while cursor < len(m['expressions']):
        rec = m['expressions'][cursor]
        if stop > 1 and has_numeric_zero(rec['tree']):
            enqueue(m, {'kind': 'zero_source', 'source': cursor,
                        'cursor': 1, 'stop': stop})
        cursor += 1
        runtime['source_cursor'] = cursor


def upgrade_zero_archive_access(m):
    runtime = m.setdefault('zero_runtime', {
        'version': 1, 'source_cursor': 0, 'foundation_scheduled': [],
        'leaf_metadata_backfilled': False, 'leaf_metadata_repairs': 0})
    if not runtime['leaf_metadata_backfilled']:
        # Leaves are derived metadata. Keep expression IDs, trees and events.
        for rec in m['expressions']:
            if rec['pathway'] != 'zero_nexus_transform_v1':
                continue
            leaves = rational_tree_leaves(rec['tree'])
            if rec['leaves'] != leaves:
                rec['leaves'] = leaves
                runtime['leaf_metadata_repairs'] += 1
                journal(m, 'zero_leaf_metadata_repaired', expression_id=rec['id'])
        runtime['leaf_metadata_backfilled'] = True
    schedule_zero_sources(m)
    for state in m['foundation']['states']:
        idx = foundation_expression_id(m, state)
        if idx is not None:
            schedule_zero_foundation_scan(m, idx)
    m['rule_registry'].setdefault('zero_archive_access_v462', {
        'status': 'active_exploration_not_foundation',
        'meaning': 'persistent_scans_for_existing_zero_slot_transformations'})


def work_zero_scan(m, task, stats):
    """Inspect one archived construction for a new registered value."""
    cursor = task['cursor']
    if cursor >= task['stop']:
        return True
    if has_numeric_zero(m['expressions'][cursor]['tree']):
        enqueue(m, {'kind': 'nexus', 'source': cursor, 'value': task['value'],
                    'rule': 'zero_nexus_transform_v1'})
    if cursor + 1 < task['stop']:
        enqueue(m, {**task, 'cursor': cursor + 1})
    return True


def work_zero_source(m, task, stats):
    """Offer one prior registered value to a newly archived zero slot."""
    cursor = task['cursor']
    if cursor >= task['stop']:
        return True
    state = m['foundation']['states'][cursor]
    value_id = foundation_expression_id(m, state)
    if value_id is not None:
        enqueue(m, {'kind': 'nexus', 'source': task['source'], 'value': value_id,
                    'rule': 'zero_nexus_transform_v1'})
    if cursor + 1 < task['stop']:
        enqueue(m, {**task, 'cursor': cursor + 1})
    return True


def replace_one_zero(tree, replacement):
    """Generate structurally distinct trees by replacing one zero leaf."""
    if 'leaf' in tree:
        return [{'leaf': replacement}] if number(tree['leaf']) == 0 else []
    if 'op' not in tree:
        return []
    out = []
    for left in replace_one_zero(tree['left'], replacement):
        out.append({'op': tree['op'], 'left': left, 'right': tree['right']})
    for right in replace_one_zero(tree['right'], replacement):
        out.append({'op': tree['op'], 'left': tree['left'], 'right': right})
    return out


def evaluate_tree(tree):
    if 'leaf' in tree:
        return number(tree['leaf']), str(tree['leaf'])
    a, ae = evaluate_tree(tree['left'])
    b, be = evaluate_tree(tree['right'])
    result = operate(a, tree['op'], b)
    if result is None:
        raise ZeroDivisionError('Zero-assisted branch is blocked')
    return result, '(' + ae + ' ' + tree['op'] + ' ' + be + ')'


def work_nexus(m, task, stats):
    """Zero is an operational reference; it does not assert 0 = value."""
    source = m['expressions'][task['source']]
    value_record = m['expressions'][task['value']]
    replacement = number(value_record['value'])
    if replacement.denominator != 1:
        return True  # positional unit transformations use integer slots
    replacement = int(replacement)
    for transformed in replace_one_zero(source['tree'], replacement):
        try:
            result, expr = evaluate_tree(transformed)
        except ZeroDivisionError:
            continue
        if max(result.numerator.bit_length(),
               result.denominator.bit_length()) > MAX_BITS:
            continue
        event = {'zero_nexus': m['foundation']['zero_records'][0]['id'],
                 'source_id': source['id'], 'registered_value_id': value_record['id'],
                 'selected_value': replacement, 'slot_kind': 'numeric_zero_leaf',
                 'reference_slots': len(m['reference']['slots']),
                 'rule': 'zero_nexus_transform_v1'}
        rec = {'expr': expr, 'value': encode(result), 'tree': transformed,
               'depth': source['depth'], 'parents': [source['id'], value_record['id']],
               'leaves': rational_tree_leaves(transformed), 'pathway': 'zero_nexus_transform_v1',
               'ancestry': source['ancestry'] + [event], 'domain': 'rational'}
        idx = add_expression(m, rec)
        if idx is not None:
            m['nexus_events'].append({'result_id': idx, **event})
            if 'genesis' in m: journal(m, 'nexus_transformation', result_id=idx, source_id=source['id'], selected_value=replacement)
            stats['new'] += 1
            schedule_frontier(m, idx)
            observe(m, m['expressions'][idx], stats)
            if rec['depth'] < MAX_DEPTH:
                enqueue(m, {'kind': 'revisit', 'new': idx, 'cursor': 0,
                            'rule': 'revisit_v1'})
    return True


# ============================================================
# V4.2 PATCH - RESULT FRONTIER / OPERATION AND POSITION SLOTS
# ============================================================

def schedule_frontier(m, idx):
    """Each newly seen result can be combined with earlier distinct values."""
    value = m['expressions'][idx]['value']
    if m['results'][value][0] != idx:
        return
    m.setdefault('frontier_seen', []).append(idx)
    prior = m['frontier_seen'][-32:-1]
    # Include original foundation values even when outside recent window.
    seed = [m['results'][str(n)][0] for n in m['foundation']['states']
            if str(n) in m['results']]
    for other in dict.fromkeys(seed + prior):
        enqueue(m, {'kind': 'frontier', 'left': idx, 'right': other,
                    'rule': 'result_feedback_v42'})


def work_frontier(m, task, stats):
    for a, b in ((task['left'], task['right']),
                 (task['right'], task['left'])):
        for op in OPERATIONS:
            combine(m, a, b, op, 'result_feedback_v42', stats)
    return True


def positional_nexus(m, state):
    """Schedule genuine candidate expressions for original 00404 zero slots.
    Positional ancestry is kept separately from numerical equality.
    """
    if not 0 <= state <= 9: return
    for slot in m['reference']['slots']:
        if slot['kind'] == 'persistent_zero':
            for op in OPERATIONS:
                enqueue(m, {'kind': 'position', 'source_position':
                    slot['source_position'], 'selected_value': state,
                    'op': op, 'rule': 'zero_nexus_position_operation_v43'})


def work_position(m, task, stats):
    value = task['selected_value']
    op = task['op']
    result = operate(Fraction(0), op, Fraction(value))
    if result is None: return True
    zero_id = m['results']['0'][0]
    value_id = m['results'][str(value)][0]
    # A distinct provenance-bearing pathway; do not equate the original
    # positional string with an arithmetic expression.
    tree = {'op': op, 'left': {'leaf': 0}, 'right': {'leaf': value}}
    event = {'zero_nexus': 'Z0', 'source': REFERENCE_INPUT,
             'source_position': task['source_position'],
             'selected_value': value, 'operation': op,
             'rule': task['rule']}
    pathway = task['rule'] + '_slot_' + str(task['source_position'])
    rec = {'expr': '(0 ' + op + ' ' + str(value) + ')',
           'value': encode(result), 'tree': tree, 'depth': 1,
           'parents': [zero_id, value_id], 'leaves': [0, value],
           'pathway': pathway, 'ancestry': [event], 'domain': 'rational'}
    idx = add_expression(m, rec)
    if idx is not None:
        stats['new'] += 1
        m['nexus_events'].append({'result_id': idx, **event})
        if 'genesis' in m: journal(m, 'positional_transformation', result_id=idx, source_position=task['source_position'], selected_value=value, operation=op)
        record_counters(m, m['expressions'][zero_id],
                        m['expressions'][value_id], op, rec, pathway)
        schedule_frontier(m, idx)
        observe(m, m['expressions'][idx], stats)
    return True


def upgrade_runtime(m):
    """In-place compatible augmentation of existing V4.1 memory."""
    m.setdefault('frontier_seen', [])
    m.setdefault('nexus_events', [])
    m.setdefault('emergence_events', [])
    m['rule_registry'].setdefault('result_feedback_v42',
                                  {'status': 'active_exploration'})
    m['rule_registry'].setdefault('zero_nexus_position_operation_v42',
                                  {'status': 'experimental_observation'})
    # Backfill only unique values already archived; do not replay old work.
    if not m.get('frontier_bootstrapped'):
        for value, ids in list(m['results'].items()):
            if ids:
                schedule_frontier(m, ids[0])
        m['frontier_bootstrapped'] = True


def memory_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), MEMORY_FILENAME)


def load_memory():
    path = memory_path()
    if not os.path.exists(path): return empty_memory()
    with open(path, 'r', encoding='utf-8') as f: m = json.load(f)
    if m.get('schema') != 1 or m.get('version') != VERSION:
        raise ValueError('Incompatible memory; original file left untouched')
    return m


def save_memory(m):
    # Runtime-only hash set is rebuilt from persistent keys, never serialized.
    m.pop('_keys', None)
    m.pop('_pending_keys', None)
    m.pop('_blocked_keys', None)
    m.pop('_journal_run_count', None)
    m.pop('_v45_signatures', None)
    m.pop('_symbolic_keys', None)
    m.pop('_symbolic_values', None)
    m.pop('_symbolic_ref_ids', None)
    m.pop('_symbolic_nexus_keys', None)
    path = memory_path()
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(m, f, ensure_ascii=False, separators=(',', ':'))
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def query(m, text):
    try: key = encode(number(text))
    except Exception:
        print('Please enter a number such as 5, 1/2 or .8')
        return
    ids = m['results'].get(key, [])
    proposals = [p for p in m['zero_proposals'] if p['result'] == key]
    print('\nValue %s: %d archived expressions, %d unapproved zero proposals' %
          (key, len(ids), len(proposals)))
    for idx in ids[:20]:
        rec = m['expressions'][idx]
        print('  #%d %s [%s]' % (idx, rec['expr'], rec['pathway']))
    if len(ids) > 20: print('  ... %d more' % (len(ids) - 20))
    for p in proposals[:3]: print('  PROPOSAL:', p['expression'])
    print('Archive query only; results are not an exhaustive proof.')


# ============================================================
# V4.4 - GENESIS JOURNAL, TANGENT LEDGER, EXACT COMPLEX BRANCH
# ============================================================

def journal(m, event_type, **details):
    """Persistent logical ordering, not a fabricated history timestamp."""
    g = m.get('genesis')
    if g is None: return
    count = m.get('_journal_run_count', 0)
    if count >= MAX_JOURNAL_EVENTS_PER_RUN:
        g['suppressed_events'] += 1
        return
    seq = g['next_seq']
    g['next_seq'] += 1
    g['events'].append({'seq': seq, 'run': len(m['runs']) + 1,
                        'type': event_type, **details})
    m['_journal_run_count'] = count + 1


def tangent_parent(task):
    for key in ('source', 'new', 'left', 'value'):
        if key in task: return str(task[key])
    if 'items' in task: return 'set:' + ','.join(map(str, task['items']))
    return 'system'


def tangent_generated(m, task):
    led = m['tangent_ledger']
    led['generated'] += 1
    parent = tangent_parent(task)
    slot = led['parents'].setdefault(parent, {'generated': 0, 'selected': 0, 'completed': 0})
    slot['generated'] += 1
    journal(m, 'tangent_queued', parent=parent, kind=task['kind'],
            task_key=task_key(task), parent_generated=slot['generated'])


def tangent_selected(m, task):
    led = m['tangent_ledger']
    led['selected'] += 1
    parent = tangent_parent(task)
    slot = led['parents'].setdefault(parent, {'generated': 0, 'selected': 0, 'completed': 0})
    slot['selected'] += 1
    journal(m, 'tangent_selected', parent=parent, kind=task['kind'],
            task_key=task_key(task), reason='balanced_queue_order',
            parent_selection=slot['selected'], pending=len(m['queue'])-m['queue_head'])


def tangent_completed(m, task):
    led = m['tangent_ledger']
    led['completed'] += 1
    parent = tangent_parent(task)
    slot = led['parents'].setdefault(parent, {'generated': 0, 'selected': 0, 'completed': 0})
    slot['completed'] += 1
    journal(m, 'tangent_completed', parent=parent, kind=task['kind'], task_key=task_key(task))


def complex_key(a, b):
    return encode(a) + ('+' if b >= 0 else '') + encode(b) + 'i'


def complex_operate(a, b, op):
    ar, ai = a
    br, bi = b
    if op == '+': return ar + br, ai + bi
    if op == '-': return ar - br, ai - bi
    if op == '*': return ar*br-ai*bi, ar*bi+ai*br
    if op == '/':
        denominator = br*br+bi*bi
        if denominator == 0: return None
        return (ar*br+ai*bi)/denominator, (ai*br-ar*bi)/denominator
    raise ValueError(op)


def complex_record(m, value, expr, parents, op, pathway, depth=None, sources=None):
    ar, ai = value
    if max(ar.numerator.bit_length(), ar.denominator.bit_length(),
           ai.numerator.bit_length(), ai.denominator.bit_length()) > MAX_BITS:
        return None
    ca = m['complex_archive']
    if depth is None:
        depth = 0 if not parents else 1 + max(ca['expressions'][p]['depth'] for p in parents)
    if depth > MAX_DEPTH:
        return None
    key = complex_key(ar, ai)
    identity = json.dumps([expr, pathway, parents], separators=(',', ':'))
    if identity in ca['known_keys']: return None
    ca['known_keys'].append(identity)
    idx = len(ca['expressions'])
    ca['expressions'].append({'id': idx, 'expr': expr, 'real': encode(ar),
        'imaginary': encode(ai), 'value': key, 'parents': parents,
        'operation': op, 'pathway': pathway, 'depth': depth})
    if sources is not None:
        ca['expressions'][-1]['sources'] = sources
    first = key not in ca['results']
    ca['results'].setdefault(key, []).append(idx)
    journal(m, 'complex_expression', complex_id=idx, value=key, expr=expr,
            parents=parents, operation=op, first_value=first)
    if 'v45_observations' in m:
        observe_v45_complex(m, ca['expressions'][-1])
    if ca.get('feedback_version') == 1:
        schedule_complex_feedback(m)
    return idx


def schedule_complex_feedback(m):
    """One resumable cursor per eligible expression, including old records.

    Pair each expression with every earlier expression and itself. Later
    expressions handle their pairs with this one. This avoids creating an
    entire quadratic list of pending pairs at once.
    """
    ca = m['complex_archive']
    cursor = ca.get('feedback_scheduled_count', 0)
    while cursor < len(ca['expressions']):
        rec = ca['expressions'][cursor]
        if rec['depth'] < MAX_DEPTH:
            enqueue(m, {'kind': 'complex_feedback', 'source': cursor,
                        'cursor': 0})
        cursor += 1
        ca['feedback_scheduled_count'] = cursor


def upgrade_complex_feedback(m):
    """Add feedback without deleting or renumbering archived expressions."""
    ca = m['complex_archive']
    # Existing V4.4/V4.5 records have no depth. Their parents precede them.
    for rec in ca['expressions']:
        if 'depth' not in rec:
            rec['depth'] = (0 if not rec['parents'] else
                            1 + max(ca['expressions'][p]['depth']
                                    for p in rec['parents']))
    ca['feedback_version'] = 1
    schedule_complex_feedback(m)
    m['rule_registry'].setdefault('complex_feedback_v452',
                                  {'status': 'active_exploration_not_foundation'})


def work_complex_feedback(m, task, stats):
    source, cursor = task['source'], task['cursor']
    if cursor > source:
        return True
    # Include self-pairs once; retain both orders for distinct operands.
    pairs = [(source, cursor)]
    if source != cursor:
        pairs.append((cursor, source))
    for left, right in pairs:
        work_complex(m, {'left': left, 'right': right}, stats)
    if cursor < source:
        enqueue(m, {'kind': 'complex_feedback', 'source': source,
                    'cursor': cursor + 1})
    return True


def work_complex(m, task, stats):
    ca = m['complex_archive']
    left = ca['expressions'][task['left']]
    right = ca['expressions'][task['right']]
    if max(left['depth'], right['depth']) + 1 > MAX_DEPTH:
        return True
    a = number(left['real']), number(left['imaginary'])
    b = number(right['real']), number(right['imaginary'])
    for op in OPERATIONS:
        result = complex_operate(a, b, op)
        if result is None:
            journal(m, 'complex_blocked', left=left['id'], right=right['id'], operation=op, reason='zero_denominator')
            continue
        expr = '(' + left['expr'] + ' ' + op + ' ' + right['expr'] + ')'
        complex_record(m, result, expr, [left['id'], right['id']], op,
                       'complex_arithmetic_v44')
    return True


def upgrade_v44(m):
    if 'genesis' not in m:
        m['genesis'] = {'next_seq': 1, 'events': [], 'suppressed_events': 0,
            'historical_boundary': {'previous_runs': len(m['runs']),
             'previous_expressions': len(m['expressions']),
             'note': 'Earlier precise event ordering unavailable; not reconstructed'}}
    if 'tangent_ledger' not in m:
        m['tangent_ledger'] = {'generated': 0, 'selected': 0, 'completed': 0,
                               'parents': {}, 'duplicate_expressions': 0, 'duplicate_pending': 0,
                               'historical_counts_not_reconstructed': True}
    if 'complex_archive' not in m:
        m['complex_archive'] = {'expressions': [], 'results': {}, 'known_keys': []}
    # Prepare historical depths before any new records are constructed.
    for rec in m['complex_archive']['expressions']:
        if 'depth' not in rec:
            rec['depth'] = (0 if not rec['parents'] else
                            1 + max(m['complex_archive']['expressions'][p]['depth']
                                    for p in rec['parents']))
    m['rule_registry'].setdefault('complex_arithmetic_v44', {'status': 'active_exploration_not_foundation'})
    if not m.get('v44_initialized'):
        journal(m, 'v44_boundary', **m['genesis']['historical_boundary'])
        # i and -i are explicitly seeded candidate domain elements, NOT
        # derived from the rational state-count foundation or 0=i.
        complex_record(m, (Fraction(0), Fraction(1)), 'i', [], 'seed', 'complex_unit_v44')
        complex_record(m, (Fraction(0), Fraction(-1)), '-i', [], 'seed', 'complex_unit_v44')
        # Rational values are represented exactly on the real axis.
        for n in m['foundation']['states'][:8]:
            complex_record(m, (Fraction(n), Fraction(0)), str(n), [], 'embed', 'rational_embedding_v44')
        m['v44_initialized'] = True
    # Add newly emerged rational foundation values without duplicating seeds.
    ca = m['complex_archive']
    for n in m['foundation']['states']:
        complex_record(m, (Fraction(n), Fraction(0)), str(n), [], 'embed', 'rational_embedding_v44')
    # Bounded new complex work: each new real-axis element is connected
    # to i/-i; previous pending tasks survive runs.
    seeded = m.setdefault('v44_complex_scheduled', [])
    for item in ca['expressions']:
        if item['pathway'] != 'rational_embedding_v44' or item['id'] in seeded:
            continue
        seeded.append(item['id'])
        for imaginary_id in (0, 1):
            enqueue(m, {'kind': 'complex', 'left': item['id'], 'right': imaginary_id})
            enqueue(m, {'kind': 'complex', 'left': imaginary_id, 'right': item['id']})


# ============================================================
# V4.5 - OBSERVATIONAL CONVERGENCE HUBS AND STRUCTURAL ECHOES
# Neither is a claim of physical attraction or mathematical emergence.
# ============================================================


def v45_signature(tree):
    """Shape + operators, ignoring leaf values; never merges real paths."""
    if isinstance(tree, dict):
        if 'leaf' in tree:
            return ['leaf']
        return {str(k): v45_signature(v) for k, v in sorted(tree.items())}
    if isinstance(tree, list):
        return [v45_signature(x) for x in tree]
    return tree


def v45_signature_key(tree):
    return json.dumps(v45_signature(tree), sort_keys=True, separators=(',', ':'))


def v45_result_sign(value):
    v = number(value)
    return 1 if v > 0 else (-1 if v < 0 else 0)


def observe_v45_real(m, record, historical=False):
    obs = m['v45_observations']
    value = record['value']
    hub = obs['hubs'].setdefault(value, {'expressions': 0, 'distinct_parent_ids': [], 'first_expression': record['id']})
    hub['expressions'] += 1
    for parent in record.get('parents', []):
        if parent not in hub['distinct_parent_ids']:
            hub['distinct_parent_ids'].append(parent)
    sign = v45_result_sign(value)
    if not sign: return
    sig = v45_signature_key(record['tree'])
    signatures = m['_v45_signatures']
    bucket = signatures.setdefault(sig, {})
    other_id = bucket.get(encode(-number(value)))
    bucket.setdefault(value, record['id'])
    if other_id is not None:
        other = m['expressions'][other_id]
        obs['real_echo_events'] += 1
        if len(obs['real_echo_examples']) < 100:
            pair = [min(other_id, record['id']), max(other_id, record['id'])]
            if pair not in obs['real_echo_examples']:
                obs['real_echo_examples'].append(pair)
        if not historical:
            journal(m, 'real_structural_echo', expression_id=record['id'],
                    mirror_id=other_id, value=value, mirror_value=other['value'],
                    definition='same operator tree shape and opposite numerical result')


def observe_v45_complex(m, record, historical=False):
    obs = m['v45_observations']
    ar, ai = number(record['real']), number(record['imaginary'])
    if ai == 0: return
    conjugate = complex_key(ar, -ai)
    ids = m['complex_archive']['results'].get(conjugate, [])
    mirror = next((i for i in ids if i != record['id']), None)
    if mirror is None: return
    obs['conjugate_echo_events'] += 1
    if len(obs['conjugate_examples']) < 100:
        pair = [min(mirror, record['id']), max(mirror, record['id'])]
        if pair not in obs['conjugate_examples']:
            obs['conjugate_examples'].append(pair)
    if not historical:
        journal(m, 'complex_conjugate_echo', complex_id=record['id'], mirror_id=mirror,
                value=record['value'], mirror_value=conjugate)


def upgrade_v45(m):
    if 'v45_observations' not in m:
        m['v45_observations'] = {
            'historical_boundary': {'previous_runs': len(m['runs']),
                'previous_real_expressions': len(m['expressions']),
                'previous_complex_expressions': len(m['complex_archive']['expressions'])},
            'hubs': {}, 'real_echo_events': 0, 'real_echo_examples': [],
            'conjugate_echo_events': 0, 'conjugate_examples': []}
        # Historical structural indexes can be reconstructed; execution
        # order, eligible choices and timestamps are NOT invented.
        m['_v45_signatures'] = {}
        for rec in m['expressions']:
            observe_v45_real(m, rec, historical=True)
        for rec in m['complex_archive']['expressions']:
            observe_v45_complex(m, rec, historical=True)
        journal(m, 'v45_boundary', **m['v45_observations']['historical_boundary'])
    else:
        m['_v45_signatures'] = {}
        for rec in m['expressions']:
            sign = v45_result_sign(rec['value'])
            if not sign: continue
            bucket = m['_v45_signatures'].setdefault(v45_signature_key(rec['tree']), {})
            bucket.setdefault(rec['value'], rec['id'])
    m['rule_registry'].setdefault('convergence_hub_v45', {'status': 'observational_not_dynamical_attractor'})
    m['rule_registry'].setdefault('structural_echo_v45', {'status': 'observational_not_numerical_identity'})


def print_v45_summary(m):
    obs = m['v45_observations']
    hubs = sorted(obs['hubs'].items(), key=lambda item: (-len(item[1]['distinct_parent_ids']),
                          -item[1]['expressions'], item[0]))[:8]
    print('V4.5 convergence hubs (distinct parent IDs / expressions):')
    for val, info in hubs:
        print('  %s: %d / %d' % (val, len(info['distinct_parent_ids']), info['expressions']))
    print('Real structural echo observations:', obs['real_echo_events'])
    print('Complex conjugate echo observations:', obs['conjugate_echo_events'])
    print('Echo examples retained:', len(obs['real_echo_examples']), 'real;',
          len(obs['conjugate_examples']), 'complex')


def parse_complex_query(text):
    import re
    compact = text.replace(' ', '').lower()
    if 'i' not in compact: return None
    if compact.count('i') != 1 or not compact.endswith('i'): raise ValueError('Expected a+bi, i or -i')
    body = compact[:-1]
    split = None
    for pos in range(1, len(body)):
        if body[pos] in '+-': split = pos
    if split is None:
        real, imaginary = Fraction(0), body
    else:
        real, imaginary = number(body[:split]), body[split:]
    if imaginary in ('', '+'): imaginary = '1'
    if imaginary == '-': imaginary = '-1'
    return complex_key(number(real), number(imaginary))


# ============================================================
# V4.5.1 - READ-ONLY DISCOVERY INDEX (NO ARCHIVE MIGRATION)
# ============================================================

def discovery_index(m, command):
    """Browse recorded results; missing values are not proof of unreachability."""
    import re
    words = command.strip().lower().split()
    if not words or words[0] not in ('index', 'values', 'gaps', 'complex-index'):
        return False
    kind = words[0]
    if kind == 'complex-index':
        results = m.get('complex_archive', {}).get('results', {})
        print('\nCOMPLEX DISCOVERY INDEX: %d distinct values' % len(results))
        for key, ids in sorted(results.items(), key=lambda kv: kv[0])[:100]:
            print('  %-22s %d expressions' % (key, len(ids)))
        if len(results) > 100: print('  ... %d more; use i or a+bi to query individual values' % (len(results)-100))
        return True
    if kind == 'gaps':
        if len(words) != 3:
            print('Usage: gaps MIN MAX (example: gaps -30 30)')
            return True
        try:
            lo, hi = int(words[1]), int(words[2])
        except ValueError:
            print('Please use integer endpoints, e.g. gaps -30 30')
            return True
        if hi < lo or hi-lo > 1000:
            print('Choose an ascending range of at most 1001 integers.')
            return True
        absent = [n for n in range(lo, hi+1) if encode(Fraction(n)) not in m['results']]
        print('\nNOT ARCHIVED in [%d, %d]: %d integers' % (lo, hi, len(absent)))
        print(', '.join(map(str, absent)) if absent else '(none)')
        print('Not archived does not mean impossible or never attempted.')
        return True
    entries = []
    for key, ids in m['results'].items():
        if not ids: continue
        try: value = Fraction(key)
        except (ValueError, ZeroDivisionError): continue
        entries.append((value, ids))
    entries.sort(key=lambda item: item[0])
    if len(words) == 3:
        try: lo, hi = Fraction(words[1]), Fraction(words[2])
        except (ValueError, ZeroDivisionError):
            print('Usage: index [MIN MAX], e.g. index -10 10')
            return True
        entries = [(value, ids) for value, ids in entries if lo <= value <= hi]
    elif len(words) != 1:
        print('Usage: index [MIN MAX], e.g. index -10 10')
        return True
    print('\nREAL DISCOVERY INDEX: %d archived values' % len(entries))
    for value, ids in entries[:120]:
        first = m['expressions'][ids[0]]
        print('  %-12s paths=%-5d first=#%-5d %s' %
              (str(value), len(ids), ids[0], first.get('pathway', '?')))
    if len(entries) > 120:
        print('  ... %d more. Narrow with index MIN MAX.' % (len(entries)-120))
    print('First=# is archive insertion order, not historical scheduler decision order.')
    return True


def query_v45(m, text):
    if discovery_index(m, text): return True
    if text.lower() in ('hubs', 'attractors', 'echoes'):
        print_v45_summary(m)
        if text.lower() == 'echoes':
            for a, b in m['v45_observations']['real_echo_examples'][:8]:
                x, y = m['expressions'][a], m['expressions'][b]
                print('  Real echo: #%d %s = %s | #%d %s = %s' %
                      (a, x['expr'], x['value'], b, y['expr'], y['value']))
            for a, b in m['v45_observations']['conjugate_examples'][:8]:
                x, y = m['complex_archive']['expressions'][a], m['complex_archive']['expressions'][b]
                print('  Complex echo: %s | %s' % (x['value'], y['value']))
        return True
    try: key = parse_complex_query(text)
    except (ValueError, ZeroDivisionError) as exc:
        print('Complex query format: i, -i, 2+3i, 1/2-4i. Error:', exc)
        return True
    if key is None: return False
    ca = m['complex_archive']
    ids = ca['results'].get(key, [])
    print('Complex value %s: %d archived expressions' % (key, len(ids)))
    for idx in ids[:20]:
        rec = ca['expressions'][idx]
        print('  C#%d %s [%s]' % (idx, rec['expr'], rec['pathway']))
    if len(ids) > 20: print('  ... %d more' % (len(ids) - 20))
    return True


# ============================================================
# V4.6 - EXACT ALGEBRAIC EXPRESSIONS WITH SYMPY
# New operations are extensions, not changes to the foundation.
# ============================================================

def sympy_module():
    try:
        import sympy
    except ImportError as exc:
        raise RuntimeError('SymPy is required for V4.6.2. In Pydroid3, open Pip, '
                           'install sympy, then run this script again. '
                           'Your saved memory has not been changed.') from exc
    return sympy


def symbolic_pack(value):
    """JSON-safe exact expression tree; never serialize executable code."""
    sp = sympy_module()
    if value.is_Rational:
        return {'q': [str(value.p), str(value.q)]}
    if value == sp.I:
        return {'i': True}
    names = {sp.Add: 'add', sp.Mul: 'mul', sp.Pow: 'pow'}
    if value.func not in names:
        raise ValueError('Unsupported exact symbolic object')
    return {'fn': names[value.func],
            'args': [symbolic_pack(v) for v in value.args]}


def symbolic_unpack(tree, depth=0):
    """Rebuild only the explicitly supported mathematical constructors."""
    sp = sympy_module()
    if depth > SYMBOLIC_MAX_NODES:
        raise ValueError('Symbolic tree exceeds the nesting limit')
    if 'q' in tree:
        return sp.Rational(int(tree['q'][0]), int(tree['q'][1]))
    if tree.get('i') is True:
        return sp.I
    constructors = {'add': sp.Add, 'mul': sp.Mul, 'pow': sp.Pow}
    constructor = constructors.get(tree.get('fn'))
    if constructor is None:
        raise ValueError('Unknown symbolic constructor')
    return constructor(*(symbolic_unpack(v, depth + 1) for v in tree['args']))


def symbolic_within_limits(value):
    sp = sympy_module()
    nodes = list(sp.preorder_traversal(value))
    if len(nodes) > SYMBOLIC_MAX_NODES:
        return False
    if value.has(sp.nan, sp.zoo, sp.oo, -sp.oo) or value.is_finite is False:
        return False
    return all(max(int(v.p).bit_length(), int(v.q).bit_length()) <= MAX_BITS
               for v in nodes if v.is_Rational)


def symbolic_apply(a, op, b=None):
    """Exact arithmetic, bounded rational powers, principal square roots."""
    sp = sympy_module()
    if op == 'sqrt':
        # Factoring an arbitrary 256-bit integer inside sqrt can be costly.
        # This is a resource bound, not a restriction of mathematics.
        if any(max(int(v.p).bit_length(), int(v.q).bit_length()) > SYMBOLIC_MAX_ROOT_BITS
               for v in sp.preorder_traversal(a) if v.is_Rational):
            return None, 'root_resource_limit'
        result = sp.sqrt(a)
    elif op == '+': result = a + b
    elif op == '-': result = a - b
    elif op == '*': result = a * b
    elif op == '/':
        if b.is_zero is not False:
            return None, 'zero_or_unresolved_denominator'
        result = a / b
    elif op == '**':
        if not b.is_Rational or abs(b.p) > SYMBOLIC_MAX_POWER or b.q > SYMBOLIC_MAX_POWER:
            return None, 'power_exponent_limit'
        if a.is_zero is True and b <= 0:
            return None, 'zero_to_nonpositive_power'
        if b < 0 and a.is_zero is not False:
            return None, 'zero_or_unresolved_base'
        if b.q != 1 and any(
                max(int(v.p).bit_length(), int(v.q).bit_length()) > SYMBOLIC_MAX_ROOT_BITS
                for v in sp.preorder_traversal(a) if v.is_Rational):
            return None, 'root_resource_limit'
        # Avoid constructing giant rational powers before checking size.
        if a.is_Rational and max(int(a.p).bit_length(), int(a.q).bit_length()) * abs(int(b.p)) > MAX_BITS:
            return None, 'power_resource_limit'
        result = a ** b
    else:
        raise ValueError('Unsupported symbolic operation')
    if not symbolic_within_limits(result):
        return None, 'symbolic_resource_limit'
    # Distribute products so (sqrt(2)+1)*(sqrt(2)-1) can return to 1.
    expanded = sp.expand_mul(result)
    if symbolic_within_limits(expanded):
        result = expanded
    return result, None


def symbolic_value(m, idx):
    cache = m.setdefault('_symbolic_values', {})
    if idx not in cache:
        cache[idx] = symbolic_unpack(m['symbolic_archive']['expressions'][idx]['exact'])
    return cache[idx]


def schedule_symbolic_feedback(m, rec):
    if rec['depth'] < MAX_DEPTH:
        enqueue(m, {'kind': 'symbolic_root', 'source': rec['id']})
        enqueue(m, {'kind': 'symbolic_pair', 'source': rec['id'],
                    'cursor': 0, 'step': 0})


def bridge_symbolic_result(m, rec, value, stats=None):
    """Embed new exact numeric values with typed cross-archive provenance."""
    ref = {'archive': 'symbolic', 'id': rec['id']}
    if value.is_Rational:
        key = encode(Fraction(int(value.p), int(value.q)))
        if key not in m['results']:
            leaf = int(value.p) if value.q == 1 else key
            idx = add_expression(m, {
                'expr': key, 'value': key,
                'tree': {'leaf': leaf, 'symbolic_source': rec['id']},
                'depth': rec['depth'], 'parents': [], 'leaves': [leaf],
                'pathway': 'symbolic_to_rational_v46', 'domain': 'rational',
                'sources': [ref], 'ancestry': [{'rule': 'exact_numeric_embedding',
                    'source': ref, 'source_expression': rec['expr']}]})
            if idx is not None:
                schedule_frontier(m, idx)
                if rec['depth'] < MAX_DEPTH:
                    enqueue(m, {'kind': 'revisit', 'new': idx, 'cursor': 0,
                                'rule': 'revisit_v1'})
                if stats is not None:
                    stats['new'] += 1
    real, imaginary = value.as_real_imag()
    if real.is_Rational and imaginary.is_Rational:
        ar = Fraction(int(real.p), int(real.q))
        ai = Fraction(int(imaginary.p), int(imaginary.q))
        if complex_key(ar, ai) not in m['complex_archive']['results']:
            complex_record(m, (ar, ai), str(value), [], 'embed',
                           'symbolic_to_complex_v46', depth=rec['depth'],
                           sources=[ref])


def symbolic_record(m, value, expr, parents, operation, pathway,
                    sources=None, depth=None, stats=None, construction=None, nexus=None):
    if not symbolic_within_limits(value):
        return None
    sa = m['symbolic_archive']
    if depth is None:
        depth = 0 if not parents else 1 + max(sa['expressions'][p]['depth'] for p in parents)
    if depth > MAX_DEPTH:
        return None
    sources = sources or []
    identity = json.dumps([pathway, operation, parents, sources, expr],
                          sort_keys=True, separators=(',', ':'))
    keys = m.get('_symbolic_keys')
    if keys is None:
        keys = set(sa['known_keys'])
        m['_symbolic_keys'] = keys
    if identity in keys:
        return None
    keys.add(identity)
    sa['known_keys'].append(identity)
    idx = len(sa['expressions'])
    rec = {'id': idx, 'expr': expr, 'value': str(value),
           'exact': symbolic_pack(value), 'parents': parents,
           'operation': operation, 'pathway': pathway,
           'sources': sources, 'depth': depth}
    if construction is not None:
        rec['construction'] = construction
    if nexus is not None:
        rec['nexus'] = nexus
    sa['expressions'].append(rec)
    ensure_symbolic_construction(m, rec)
    sa['results'].setdefault(rec['value'], []).append(idx)
    m.setdefault('_symbolic_values', {})[idx] = value
    schedule_symbolic_feedback(m, rec)
    if sa.get('zero_nexus_version') == 1:
        schedule_symbolic_zero_feedback(m)
    journal(m, 'symbolic_expression', symbolic_id=idx, value=rec['value'],
            parents=parents, sources=sources, operation=operation)
    bridge_symbolic_result(m, rec, value, stats)
    return idx


def upgrade_symbolic(m):
    sympy_module()  # Fail before mutating or saving memory if unavailable.
    sa = m.setdefault('symbolic_archive', {
        'schema': 1, 'expressions': [], 'results': {}, 'known_keys': [],
        'import_cursors': {'rational': 0, 'complex': 0}, 'skipped': {}})
    m['_symbolic_keys'] = set(sa['known_keys'])
    m['_symbolic_values'] = {}
    m['rule_registry'].setdefault('exact_algebraic_v46', {
        'status': 'active_exploration_not_foundation',
        'operations': ['+', '-', '*', '/', '**', 'sqrt'],
        'root_convention': 'principal_complex_root',
        'power_exponents': 'bounded_rationals'})


def import_symbolic_sources(m):
    """Import representative values in bounded, persisted source order.

    Every source expression remains in its original archive. A representative
    is imported per indexed value; this is not a copy of every derivation.
    New values and any import backlog are picked up on subsequent runs.
    """
    sp = sympy_module()
    sa = m['symbolic_archive']
    for domain, archive in (('rational', m), ('complex', m['complex_archive'])):
        entries = list(archive['results'].items())
        cursor = sa['import_cursors'][domain]
        stop = min(len(entries), cursor + SYMBOLIC_IMPORT_PER_RUN)
        while cursor < stop:
            _, ids = entries[cursor]
            source = archive['expressions'][ids[0]]
            if domain == 'rational':
                q = number(source['value'])
                value = sp.Rational(q.numerator, q.denominator)
            else:
                ar, ai = number(source['real']), number(source['imaginary'])
                value = (sp.Rational(ar.numerator, ar.denominator) +
                         sp.I * sp.Rational(ai.numerator, ai.denominator))
            symbolic_record(m, value, str(value), [], 'embed',
                            'numeric_to_symbolic_v46',
                            sources=[{'archive': domain, 'id': source['id']}],
                            depth=source['depth'])
            cursor += 1
            sa['import_cursors'][domain] = cursor


def rational_symbolic_construction(m, tree):
    """Keep original zero leaves when importing a rational construction."""
    sp = sympy_module()
    if 'symbolic_source' in tree:
        origin = m['symbolic_archive']['expressions'][tree['symbolic_source']]
        return ensure_symbolic_construction(m, origin)
    if 'leaf' in tree:
        q = number(tree['leaf'])
        return {'exact': symbolic_pack(sp.Rational(q.numerator, q.denominator))}
    return {'op': tree['op'], 'args': [
        rational_symbolic_construction(m, tree['left']),
        rational_symbolic_construction(m, tree['right'])]}


def ensure_symbolic_construction(m, rec):
    """Construction order is independent of the simplified exact value."""
    if 'construction' in rec:
        return rec['construction']
    if rec['operation'] in SYMBOLIC_BINARY_OPERATIONS + ('sqrt',) and rec['parents']:
        tree = {'op': rec['operation'], 'args': [
            ensure_symbolic_construction(m, m['symbolic_archive']['expressions'][p])
            for p in rec['parents']]}
    elif rec['pathway'] == 'numeric_to_symbolic_v46' and rec['sources']:
        source = rec['sources'][0]
        if source['archive'] == 'rational':
            tree = rational_symbolic_construction(m, m['expressions'][source['id']]['tree'])
        else:
            tree = {'exact': rec['exact']}
    else:
        tree = {'exact': rec['exact']}
    rec['construction'] = tree
    return tree


def symbolic_zero_paths(tree, path=()):
    if 'exact' in tree:
        return [path] if tree['exact'] == {'q': ['0', '1']} else []
    paths = []
    for idx, child in enumerate(tree['args']):
        paths.extend(symbolic_zero_paths(child, path + (idx,)))
    return paths


def replace_symbolic_slot(tree, path, replacement):
    if not path:
        return replacement
    args = list(tree['args'])
    args[path[0]] = replace_symbolic_slot(args[path[0]], path[1:], replacement)
    return {'op': tree['op'], 'args': args}


def symbolic_construction_depth(tree):
    if 'exact' in tree:
        return 0
    return 1 + max(symbolic_construction_depth(child) for child in tree['args'])


def evaluate_symbolic_construction(tree):
    if 'exact' in tree:
        value = symbolic_unpack(tree['exact'])
        return value, '(' + str(value) + ')', None
    children = [evaluate_symbolic_construction(child) for child in tree['args']]
    for _, _, reason in children:
        if reason:
            return None, '', reason
    op = tree['op']
    a, ae, _ = children[0]
    if op == 'sqrt':
        value, reason = symbolic_apply(a, op)
        expr = 'sqrt(' + ae + ')'
    else:
        b, be, _ = children[1]
        value, reason = symbolic_apply(a, op, b)
        expr = '(' + ae + ' ' + op + ' ' + be + ')'
    return value, expr, reason


def schedule_symbolic_zero_feedback(m):
    sa = m['symbolic_archive']
    cursor = sa.get('zero_feedback_scheduled_count', 0)
    while cursor < len(sa['expressions']):
        rec = sa['expressions'][cursor]
        if rec['depth'] < MAX_DEPTH:
            enqueue(m, {'kind': 'symbolic_nexus', 'source': cursor,
                        'cursor': 0, 'direction': 0, 'slot': 0})
        cursor += 1
        sa['zero_feedback_scheduled_count'] = cursor


def schedule_symbolic_zero_positions(m):
    seen = m.setdefault('symbolic_zero_positions_scheduled', [])
    for state in m['foundation']['states']:
        if state > 9 or state in seen:
            continue
        for slot in m['reference']['slots']:
            if slot['kind'] != 'persistent_zero':
                continue
            common = {'kind': 'symbolic_position', 'source_position': slot['source_position'],
                      'selected_value': state}
            enqueue(m, {**common, 'op': '**', 'order': 'zero_first'})
            enqueue(m, {**common, 'op': '**', 'order': 'zero_last'})
            if state == 0:
                enqueue(m, {**common, 'op': 'sqrt', 'order': 'unary_zero'})
        seen.append(state)


def upgrade_symbolic_zero_nexus(m):
    sa = m['symbolic_archive']
    for rec in sa['expressions']:
        ensure_symbolic_construction(m, rec)
    sa['zero_nexus_version'] = 1
    if 'zero_nexus_keys' not in sa:
        sa['zero_nexus_keys'] = [json.dumps([rec['pathway'], rec['construction']],
            sort_keys=True, separators=(',', ':'))
            for rec in sa['expressions'] if 'nexus' in rec]
    m['_symbolic_nexus_keys'] = set(sa['zero_nexus_keys'])
    m.setdefault('symbolic_nexus_events', [])
    schedule_symbolic_zero_feedback(m)
    schedule_symbolic_zero_positions(m)
    m['rule_registry'].setdefault('zero_nexus_symbolic_v461', {
        'status': 'active_exploration_not_foundation',
        'meaning': 'replace_one_numeric_zero_slot_with_available_expression',
        'operations': list(SYMBOLIC_BINARY_OPERATIONS) + ['sqrt']})


def record_symbolic_nexus(m, tree, parents, event, pathway, stats):
    sa = m['symbolic_archive']
    # Match the existing nexus policy: one record per construction and rule.
    # Replacing bare zero with the same value repeatedly must not create
    # unbounded depth-zero copies distinguished only by their parent IDs.
    identity = json.dumps([pathway, tree], sort_keys=True, separators=(',', ':'))
    keys = m.get('_symbolic_nexus_keys')
    if keys is None:
        keys = set(sa.setdefault('zero_nexus_keys', []))
        m['_symbolic_nexus_keys'] = keys
    if identity in keys:
        sa['zero_nexus_duplicates'] = sa.get('zero_nexus_duplicates', 0) + 1
        journal(m, 'duplicate_symbolic_nexus', parents=parents, **event)
        return
    # Embedding/import depth must not be reset by a slot transformation.
    depth = max(symbolic_construction_depth(tree),
                max(sa['expressions'][p]['depth'] for p in parents))
    if depth > MAX_DEPTH:
        return
    value, expr, reason = evaluate_symbolic_construction(tree)
    if reason:
        sa['skipped'][reason] = sa['skipped'].get(reason, 0) + 1
        journal(m, 'symbolic_nexus_blocked', reason=reason, **event)
        return
    idx = symbolic_record(m, value, expr, parents, 'zero_slot_construction',
                          pathway, depth=depth, stats=stats,
                          construction=tree, nexus=event)
    if idx is not None:
        keys.add(identity)
        sa['zero_nexus_keys'].append(identity)
        m['symbolic_nexus_events'].append({'symbolic_result_id': idx, **event})
        stats['symbolic_new'] = stats.get('symbolic_new', 0) + 1
        journal(m, 'symbolic_nexus_transformation', symbolic_result_id=idx, **event)


def work_symbolic_nexus(m, task, stats):
    """One zero-slot replacement per task, with a persistent pair cursor."""
    sa = m['symbolic_archive']
    new, cursor = task['source'], task['cursor']
    direction, slot = task['direction'], task['slot']
    source_id, value_id = (new, cursor) if direction == 0 else (cursor, new)
    source, selected = sa['expressions'][source_id], sa['expressions'][value_id]
    paths = symbolic_zero_paths(source['construction'])
    if slot + 1 < len(paths):
        enqueue(m, {**task, 'slot': slot + 1})
    elif direction == 0 and new != cursor:
        enqueue(m, {**task, 'direction': 1, 'slot': 0})
    elif cursor < new:
        enqueue(m, {**task, 'cursor': cursor + 1, 'direction': 0, 'slot': 0})
    if slot >= len(paths) or symbolic_value(m, value_id).is_zero is True:
        return True
    path = paths[slot]
    transformed = replace_symbolic_slot(source['construction'], path, selected['construction'])
    event = {'zero_nexus': 'Z0', 'source_id': source_id,
             'selected_value_id': value_id, 'zero_slot_path': list(path),
             'rule': 'zero_nexus_symbolic_v461'}
    record_symbolic_nexus(m, transformed, [source_id, value_id], event,
                          'zero_nexus_symbolic_v461', stats)
    return True


def symbolic_rational_reference(m, real_id):
    cache = m.setdefault('_symbolic_ref_ids', {})
    if real_id in cache:
        return cache[real_id]
    sp = sympy_module()
    original = m['expressions'][real_id]
    q = number(original['value'])
    value = sp.Rational(q.numerator, q.denominator)
    source = {'archive': 'rational', 'id': real_id}
    sa = m['symbolic_archive']
    for idx in sa['results'].get(str(value), []):
        rec = sa['expressions'][idx]
        if rec['pathway'] == 'numeric_to_symbolic_v46' and rec['sources'] == [source]:
            cache[real_id] = idx
            return idx
    idx = symbolic_record(m, value, str(value), [], 'embed',
                          'numeric_to_symbolic_v46', sources=[source],
                          depth=original['depth'])
    if idx is None:
        raise ValueError('Unable to reference foundation expression symbolically')
    cache[real_id] = idx
    return idx


def work_symbolic_position(m, task, stats):
    state = task['selected_value']
    real_id = next(idx for idx in m['results'][str(state)]
                   if m['expressions'][idx]['pathway'] == 'foundation_state_count_v3')
    zero_real = next(idx for idx in m['results']['0']
                     if m['expressions'][idx]['pathway'] == 'foundation_state_count_v3')
    selected = symbolic_rational_reference(m, real_id)
    zero = symbolic_rational_reference(m, zero_real)
    parents = [zero] if task['op'] == 'sqrt' else (
        [zero, selected] if task['order'] == 'zero_first' else [selected, zero])
    sa = m['symbolic_archive']
    tree = {'op': task['op'], 'args': [sa['expressions'][p]['construction'] for p in parents]}
    event = {'zero_nexus': 'Z0', 'source': REFERENCE_INPUT,
             'source_position': task['source_position'], 'selected_value': state,
             'operation': task['op'], 'order': task['order'],
             'rule': 'zero_nexus_symbolic_position_v461'}
    pathway = event['rule'] + '_slot_' + str(task['source_position'])
    record_symbolic_nexus(m, tree, parents, event, pathway, stats)
    return True


def work_symbolic(m, task, stats):
    sa = m['symbolic_archive']
    source = sa['expressions'][task['source']]
    if task['kind'] == 'symbolic_root':
        parents, op = [source['id']], 'sqrt'
        a, b = symbolic_value(m, source['id']), None
        expr = 'sqrt(' + source['expr'] + ')'
    else:
        cursor, step = task['cursor'], task['step']
        # Visit self first, then earlier expressions in insertion order.
        # This exposes squares/powers promptly without starving other pairs.
        other_id = source['id'] if cursor == 0 else cursor - 1
        other = sa['expressions'][other_id]
        left, right = (source, other) if step < 5 else (other, source)
        op = SYMBOLIC_BINARY_OPERATIONS[step % 5]
        parents = [left['id'], right['id']]
        a, b = symbolic_value(m, left['id']), symbolic_value(m, right['id'])
        expr = '(' + left['expr'] + ' ' + op + ' ' + right['expr'] + ')'
        # One operation per task. Cursor/step survive interruption between runs.
        end = 5 if cursor == 0 else 10
        if step + 1 < end:
            enqueue(m, {**task, 'step': step + 1})
        elif cursor < source['id']:
            enqueue(m, {**task, 'cursor': cursor + 1, 'step': 0})
    depth = 1 + max(sa['expressions'][p]['depth'] for p in parents)
    if depth > MAX_DEPTH:
        return True
    result, reason = symbolic_apply(a, op, b)
    if result is None:
        sa['skipped'][reason] = sa['skipped'].get(reason, 0) + 1
        journal(m, 'symbolic_operation_skipped', parents=parents,
                operation=op, reason=reason)
        return True
    idx = symbolic_record(m, result, expr, parents, op,
                          'exact_algebraic_v46', stats=stats)
    if idx is not None:
        stats['symbolic_new'] = stats.get('symbolic_new', 0) + 1
    return True


def parse_symbolic_query(text):
    """Parse a restricted arithmetic grammar; never eval/sympify user text."""
    import ast
    sp = sympy_module()
    text = text.strip().replace('^', '**')
    if len(text) > 500:
        raise ValueError('Query too long')
    tree = ast.parse(text, mode='eval')
    if sum(1 for _ in ast.walk(tree)) > SYMBOLIC_MAX_NODES:
        raise ValueError('Query too complex')
    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            token = ast.get_source_segment(text, node)
            # Fractions accepts decimal/exponent text exactly, without floats.
            if len(token) > 80 or ('e' in token.lower() and abs(int(token.lower().split('e')[1])) > 80):
                raise ValueError('Number exceeds query limit')
            q = Fraction(token)
            value = sp.Rational(q.numerator, q.denominator)
        elif isinstance(node, ast.Name) and node.id in ('i', 'I'):
            value = sp.I
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            child = visit(node.operand)
            value = child if isinstance(node.op, ast.UAdd) else -child
        elif isinstance(node, ast.BinOp):
            op = {ast.Add: '+', ast.Sub: '-', ast.Mult: '*',
                  ast.Div: '/', ast.Pow: '**'}.get(type(node.op))
            if op is None:
                raise ValueError('Unsupported query operation')
            value, reason = symbolic_apply(visit(node.left), op, visit(node.right))
            if reason:
                raise ValueError(reason)
        elif (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
              and node.func.id == 'sqrt' and len(node.args) == 1 and not node.keywords):
            value, reason = symbolic_apply(visit(node.args[0]), 'sqrt')
            if reason:
                raise ValueError(reason)
        else:
            raise ValueError('Use numbers, i, sqrt(...), + - * / and **')
        if not symbolic_within_limits(value):
            raise ValueError('Query exceeds symbolic limits')
        return value
    return visit(tree.body)


def query_symbolic(m, text):
    words = text.strip().split(maxsplit=1)
    if not words or words[0].lower() not in ('symbolic', 'symbolic-index'):
        return False
    sa = m['symbolic_archive']
    if words[0].lower() == 'symbolic-index':
        print('\nSYMBOLIC INDEX: %d stored exact forms' % len(sa['results']))
        for value, ids in list(sa['results'].items())[:100]:
            print('  %s: %d expressions' % (value, len(ids)))
        if len(sa['results']) > 100: print('  ... use symbolic EXPRESSION to query a value')
        return True
    try:
        if len(words) != 2:
            raise ValueError('Usage: symbolic sqrt(2), symbolic 2**3, symbolic sqrt(-2)')
        key = str(parse_symbolic_query(words[1]))
    except (ValueError, SyntaxError, ZeroDivisionError, OverflowError) as exc:
        print('Symbolic query:', exc)
        return True
    ids = sa['results'].get(key, [])
    print('\nExact form %s: %d archived expressions' % (key, len(ids)))
    for idx in ids[:20]:
        rec = sa['expressions'][idx]
        print('  S#%d %s [%s; parents=%s; sources=%s]' %
              (idx, rec['expr'], rec['pathway'], rec['parents'], rec['sources']))
        if 'nexus' in rec:
            print('    Zero nexus:', rec['nexus'])
    print('Archive lookup only; equivalent algebraic forms may have separate keys.')
    return True


def run():
    try:
        sp = sympy_module()
    except RuntimeError as exc:
        print(exc)
        return
    m = load_memory()
    f = m['foundation']
    assert f['states'] == list(range(len(f['states'])))
    assert [z['id'] for z in f['zero_records']] == ['Z%d' % i for i in range(len(f['states']))]
    assert digit_breakdown('00404') == '00111101111'
    assert number('1/2') + number('1/3') == Fraction(5, 6)
    m['_keys'] = set(m['known_expression_keys'])
    upgrade_runtime(m)
    upgrade_v44(m)
    upgrade_v45(m)
    upgrade_complex_feedback(m)
    upgrade_symbolic(m)
    upgrade_symbolic_zero_nexus(m)
    upgrade_zero_archive_access(m)
    m['_blocked_keys'] = {(b['left'], b['right'], b['operation'], b['pathway'])
                          for b in m['blocked']}
    stats = {'new': 0, 'observer_added': 0,
             'symbolic_new': 0,
             'processed': {'consume': 0, 'consume_op': 0, 'pair': 0, 'revisit': 0, 'nexus': 0, 'zero_scan': 0, 'zero_source': 0, 'emerge': 0, 'frontier': 0, 'position': 0, 'complex': 0, 'complex_feedback': 0, 'symbolic_root': 0, 'symbolic_pair': 0, 'symbolic_nexus': 0, 'symbolic_position': 0}}
    print('ZERO THEOREM V4.6.2 - ZERO ARCHIVE ACCESS / LINEAGE / FEEDBACK')
    print('SymPy:', sp.__version__)
    print('Memory:', memory_path())
    print('Foundation:', f['states'])
    print('Zero records:', [z['id'] for z in f['zero_records']])
    print('00404 ->', m['reference']['breakdown'])
    print('Exact arithmetic and foundation checks: PASS')
    emergence = []
    for _ in range(EMERGENCE_EVENTS_PER_RUN):
        emergence.append(register_next_state(m))
    print('New emergence events:', [(e['counted_states'], e['result']) for e in emergence])
    upgrade_v44(m)
    import_symbolic_sources(m)
    schedule_symbolic_zero_positions(m)
    removed = rebalance_queue(m)
    journal(m, 'queue_rebalance', removed_duplicates=removed, pending=len(m['queue']))
    print('Duplicate pending tasks removed:', removed)
    # Work queue is persistent. Each task is removed only after completion.
    # Rotate through tasks to prevent any one pathway monopolising the run.
    # Count a bounded number of states first, so new values enter this run.
    processed = 0
    nexus_processed = 0
    complex_processed = 0
    symbolic_processed = 0
    while processed < WORK_PER_RUN and m['queue_head'] < len(m['queue']):
        if stats['new'] >= MAX_NEW_EXPRESSIONS_PER_RUN: break
        task = m['queue'][m['queue_head']]
        kind = task['kind']
        if kind in ('nexus', 'zero_scan', 'zero_source') and nexus_processed >= NEXUS_WORK_PER_RUN:
            # Deferred work stays pending; it is not a completed operation.
            m['queue'].append(dict(task))
            m['queue_head'] += 1
            processed += 1
            continue
        if kind in ('symbolic_root', 'symbolic_pair', 'symbolic_nexus', 'symbolic_position') and symbolic_processed >= SYMBOLIC_WORK_PER_RUN:
            m['queue'].append(dict(task))
            m['queue_head'] += 1
            processed += 1
            continue
        if kind in ('complex', 'complex_feedback') and complex_processed >= COMPLEX_WORK_PER_RUN:
            # Keep the task pending, including its deduplication key. A
            # deferred task has not been selected or completed.
            m['queue'].append(dict(task))
            m['queue_head'] += 1
            processed += 1
            continue
        tangent_selected(m, task)
        if kind in ('symbolic_root', 'symbolic_pair', 'symbolic_nexus', 'symbolic_position'):
            if kind == 'symbolic_nexus':
                completed = work_symbolic_nexus(m, task, stats)
            elif kind == 'symbolic_position':
                completed = work_symbolic_position(m, task, stats)
            else:
                completed = work_symbolic(m, task, stats)
            symbolic_processed += 1
        elif kind == 'emerge':
            # The emergence event has already been handled this run.
            completed = True
        elif kind in ('nexus', 'zero_scan', 'zero_source'):
            if kind == 'zero_scan':
                completed = work_zero_scan(m, task, stats)
            elif kind == 'zero_source':
                completed = work_zero_source(m, task, stats)
            else:
                completed = work_nexus(m, task, stats)
            nexus_processed += 1
        elif kind == 'position': completed = work_position(m, task, stats)
        elif kind in ('complex', 'complex_feedback'):
            worker = work_complex_feedback if kind == 'complex_feedback' else work_complex
            completed = worker(m, task, stats)
            complex_processed += 1
        elif kind == 'frontier': completed = work_frontier(m, task, stats)
        elif kind == 'pair': completed = work_pair(m, task, stats)
        elif kind == 'consume_op': completed = work_consume_op(m, task, stats)
        elif kind == 'consume': completed = work_consume(m, task, stats)
        elif kind == 'revisit': completed = work_revisit(m, task, stats)
        else: raise ValueError('Unknown queued work kind: ' + str(kind))
        if not completed:
            raise RuntimeError('Task exceeded expression budget; memory not saved')
        tangent_completed(m, task)
        m['_pending_keys'].discard(task_key(task))
        m['queue_head'] += 1
        stats['processed'][kind] += 1
        processed += 1
    # Compact consumed queue prefix without losing unfinished work.
    if m['queue_head'] > 2000:
        m['queue'] = m['queue'][m['queue_head']:]
        m['queue_head'] = 0
    run_id = len(m['runs']) + 1
    journal(m, 'run_complete', run=run_id, expressions=len(m['expressions']), results=len(m['results']), pending=len(m['queue'])-m['queue_head'])
    m['runs'].append({'run': run_id, 'timestamp': time.time(),
                      'processed': stats['processed'], 'new': stats['new'],
                      'symbolic_new': stats['symbolic_new'],
                      'expressions_total': len(m['expressions'])})
    save_memory(m)
    print('Run:', run_id, 'Tasks:', stats['processed'])
    print('New expressions:', stats['new'], 'Archive:', len(m['expressions']))
    print('Distinct results:', len(m['results']))
    print('Observed transitions:', len(m['network']['transitions']))
    print('Observer proposals:', len(m['observer']['proposals']))
    print('Blocked operations:', len(m['blocked']))
    print('Zero-assisted proposals (NOT approved):', len(m['zero_proposals']))
    print('Nexus transformations:', len(m['nexus_events']))
    print('Zero leaf metadata repairs:', m['zero_runtime']['leaf_metadata_repairs'])
    print('Total emergence events:', len(m['emergence_events']))
    print('Executed positional pathways:', stats['processed']['position'])
    print('Feedback frontier values:', len(m.get('frontier_seen', [])))
    print('Remaining queued tasks:', len(m['queue']) - m['queue_head'])
    print('Genesis journal events:', m['genesis']['next_seq'] - 1)
    print('Tangent opportunities:', m['tangent_ledger']['generated'], 'selected:', m['tangent_ledger']['selected'], 'completed:', m['tangent_ledger']['completed'])
    print('Duplicate expressions observed:', m['tangent_ledger'].get('duplicate_expressions', 0), 'duplicate pending attempts:', m['tangent_ledger'].get('duplicate_pending', 0))
    print('Exact complex results:', len(m['complex_archive']['results']), 'complex expressions:', len(m['complex_archive']['expressions']))
    sa = m['symbolic_archive']
    print('Exact symbolic forms:', len(sa['results']), 'expressions:', len(sa['expressions']),
          'new operation expressions:', stats['symbolic_new'])
    print('Symbolic source import cursors:', sa['import_cursors'])
    print('Symbolic zero-nexus constructions:', len(m['symbolic_nexus_events']))
    print_v45_summary(m)
    print('Index commands: index, index -10 10, gaps -30 30, complex-index')
    print('Symbolic queries: symbolic-index, symbolic sqrt(2), symbolic 2**3, symbolic sqrt(-2)')
    print('Saved. Re-run to continue exploring.')
    while True:
        try: text = input('\nQuery an archived value (ENTER to exit): ').strip()
        except (EOFError, KeyboardInterrupt): break
        if not text: break
        if query_symbolic(m, text): continue
        if not query_v45(m, text): query(m, text)


if __name__ == '__main__':
    run()



