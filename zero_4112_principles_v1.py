# V4.10.6 connected repairs; continues the existing v497 slot memory filename.
# Stops new legacy preset expansion, preserves archived jobs and constructions,
# saves command/exit receipts, and versions physical definedness assessments.
# Historical physical records stay unchanged; reassessments are retained via Z0.
# Diagnostic checks are external to this engine file.
# V4.9.7: strict retained-slot experiment is the default entry point below.
# The earlier general engine is preserved for audit; its signed/SymPy/seed
# construction workers are inactive in this separate fresh branch.
# Successor-only experiment: one natural-counter arithmetic primitive, executable role S.
# General symbolic algebra remains explicitly supplied; whole-engine reduction is incomplete.
# ============================================================
# ZERO THEOREM V4.9.6 - CONNECTED ZERO WORKFLOW
# A runnable continuation of V2.2's interconnected architecture
# ============================================================
# Python 3 + SymPy. Keeps V2.2/V3.x files untouched.
# Work is bounded PER RUN, with a persistent queue for continuation.
# This is a computational exploration model, not a mathematical proof.

_ZT17_MODULE_CODE = __import__('sys')._getframe().f_code

import json
import os
import time
from collections import deque
from fractions import Fraction

VERSION = '4.1'  # Legacy memory-format compatibility; runtime version is V4.11.2.
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



# CORE DESIGN, clarified 2026-10-16:
#   Reduce to our basics. Everything belongs under the 0 design.
#   Known results and new discoveries pass through the core 0 function.
# This implementation centralizes operation dispatch and archive passage.
# Passage does not imply multiplication by 0, a reset, or an automatic fix.
# Existing explicit nexus transformations retain their mathematical rules.
# Role transformations execute explicit representation rules through zero.
# They use registered counters as slots, and preserve every generated path.
# Naming/abstraction are supplied model rules, not consequences of arithmetic alone.
# Numerical cycles and different constructions must remain distinguishable.
# This release does not establish physical decay or exhaustive exploration.

ZERO_CORE_RULE = 'everything_through_zero_v1'
ZERO_CORE_DOMAINS = ('rational', 'complex', 'symbolic', 'calculus', 'roles')


def zero_core_state(m):
    state = m.setdefault('zero_core', {
        'schema': 1, 'rule': ZERO_CORE_RULE, 'zero_nexus': 'Z0',
        'record_passages': {}, 'historical_record_passages': {},
        'operation_passages': {},
        'boundary': {'previous_runs': len(m.get('runs', [])),
                     'historical_operations_reconstructed': False}})
    for field in ('record_passages', 'historical_record_passages'):
        for domain in ZERO_CORE_DOMAINS:
            state[field].setdefault(domain, 0)
    return state


def zero_core(m, domain, *, record=None, historical=False,
              operation=None, operands=()):
    """Shared entry for exact operations and every accepted archive record.

    Identity passage preserves values, constructions, and ancestry. Actual
    transformations use the existing explicit workers; none is invented here.
    Historical records pass NOW, without claiming past operations used this gate.
    """
    if record is not None:
        if domain not in ZERO_CORE_DOMAINS or operation is not None:
            raise ValueError('Invalid zero-core record passage')
        state = zero_core_state(m)
        marker = record.get('zero_core_passage')
        if marker is not None:
            expected = (ZERO_CORE_RULE, domain, record['id'])
            if (marker.get('rule'), marker.get('archive'), marker.get('id')) != expected:
                raise ValueError('Mismatched zero-core record passage')
            return record
        record['zero_core_passage'] = {
            'rule': ZERO_CORE_RULE, 'archive': domain, 'id': record['id'],
            'zero_nexus': 'Z0', 'historical_backfill': bool(historical),
            'effect': 'identity_preserves_construction'}
        state['record_passages'][domain] += 1
        if historical:
            state['historical_record_passages'][domain] += 1
        return record
    if domain == 'rational':
        a, b = operands
        result = _operate_rational_exact(a, operation, b)
    elif domain == 'complex':
        a, b = operands
        result = _complex_operate_exact(a, b, operation)
    elif domain == 'symbolic':
        a, b = operands
        result = _symbolic_apply_exact(a, operation, b)
    elif domain == 'roles' and operation == 'transform':
        source_id, target = operands
        if m is None:
            raise ValueError('Role transformations require saved construction context')
        result = _role_transition_exact(m, source_id, target)
    elif domain == 'calculus':
        if m is None:
            (coefficients,) = operands  # Pure arithmetic checks have no archive.
        else:
            coefficients, variable_id = operands
            role_variable(m, variable_id)  # Reject missing or incompatible bindings.
        result = _calculus_apply_exact(operation, coefficients)
    elif domain == 'foundation' and operation == 'registered_state_count':
        (states,) = operands
        result = len(states)
    else:
        raise ValueError('Unsupported zero-core operation domain')
    if m is not None:
        state = zero_core_state(m)
        counts = state['operation_passages'].setdefault(domain, {})
        counts[operation] = counts.get(operation, 0) + 1
    return result


def upgrade_zero_core(m):
    """Backfill passage metadata only; retain IDs, values and saved work."""
    zero_core_state(m)
    m['rule_registry'].setdefault(ZERO_CORE_RULE, {
        'status': 'active_design_rule',
        'scope': 'exact_operation_dispatch_and_accepted_archive_records',
        'passage': 'identity_unless_an_explicit_transformation_rule_is_applied'})
    for domain in ZERO_CORE_DOMAINS:
        records = (m.get('expressions', []) if domain == 'rational' else
                   m.get(domain + '_archive', {}).get('expressions', []))
        for rec in records:
            zero_core(m, domain, record=rec, historical=True)


def zero_core_report(m):
    """Read-only coverage check; numerical cycles are not provenance cycles."""
    report = {'rule': ZERO_CORE_RULE, 'archives': {}, 'complete': True}
    state = m.get('zero_core', {})
    for domain in ZERO_CORE_DOMAINS:
        records = (m.get('expressions', []) if domain == 'rational' else
                   m.get(domain + '_archive', {}).get('expressions', []))
        missing = []
        for rec in records:
            marker = rec.get('zero_core_passage', {})
            if (marker.get('rule') != ZERO_CORE_RULE or
                    marker.get('archive') != domain or
                    marker.get('id') != rec['id'] or
                    marker.get('zero_nexus') != 'Z0'):
                missing.append(rec['id'])
        counted = state.get('record_passages', {}).get(domain, 0)
        report['archives'][domain] = {
            'records': len(records), 'missing': missing,
            'counted_passages': counted}
        if missing or counted != len(records):
            report['complete'] = False
    return report


def number(value):
    if isinstance(value, Fraction):
        return value
    return Fraction(str(value))


def encode(value):
    value = number(value)
    return str(value.numerator) if value.denominator == 1 else str(value.numerator) + '/' + str(value.denominator)


def _operate_rational_exact(a, op, b):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0: return None
        return a / b
    raise ValueError('Unsupported operation')


def operate(a, op, b, tracking=None, context='arithmetic'):
    result = zero_core(tracking, 'rational', operation=op, operands=(a, b))
    record_kernel_operation(tracking, 'rational', op,
                            'blocked' if result is None else 'succeeded', context,
                            'division_by_zero' if result is None else None)
    return result


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
    zero_core(m, 'rational', record=record)
    m['expressions'].append(record)
    m['results'].setdefault(record['value'], []).append(idx)
    if 'genesis' in m:
        journal(m, 'expression_created', expression_id=idx, value=record['value'], pathway=record['pathway'], parents=record.get('parents', []), first_value=(len(m['results'][record['value']]) == 1))
    if 'v45_observations' in m:
        observe_v45_real(m, record)
    if 'zero_runtime' in m:
        schedule_zero_sources(m)
    if 'archive_integration' in m:
        sync_archive_records(m, 'rational')
    return idx


def task_key(task):
    return json.dumps(task, sort_keys=True, separators=(',', ':'))


def rebalance_queue(m):
    """Deduplicate pending tasks only, retaining their first occurrence.
    Previously completed work is never deleted from the archive.
    """
    pending = m['queue'][m['queue_head']:]
    kinds = ('symbolic_root', 'symbolic_pair', 'symbolic_nexus', 'symbolic_position', 'frontier', 'pair', 'nexus', 'zero_scan', 'zero_source', 'position', 'complex', 'complex_feedback', 'consume_op',
             'revisit', 'consume', 'emerge', 'z0_primitive', 'z0_macro')
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
        candidate = operate(number(left['value']), '/', Fraction(replacement),
                            tracking=m, context='zero_slot_proposal_v1')
        m['zero_proposals'].append({
            'blocked_id': blocked_id, 'zero_record': 'Z0',
            'slot': 'denominator', 'replacement': replacement,
            'expression': '(' + left['expr'] + ' / ' + str(replacement) + ')',
            'result': encode(candidate), 'status': 'unapproved_observation',
            'construction_rule': 'zero_slot_proposal_v1'})


def combine(m, a_id, b_id, op, pathway, run_stats):
    left, right = m['expressions'][a_id], m['expressions'][b_id]
    a, b = number(left['value']), number(right['value'])
    result = operate(a, op, b, tracking=m, context=pathway)
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


def work_arithmetic_pair(m, task, stats, a, b, rule):
    # Preserve both operand orders, even for commutative operations.
    steps = [(x, y, op) for x, y in ((a, b), (b, a)) for op in OPERATIONS]
    cursor = task.get('op_cursor', 0)
    while cursor < len(steps):
        if stats['new'] >= MAX_NEW_EXPRESSIONS_PER_RUN:
            task['op_cursor'] = cursor
            return False
        x, y, op = steps[cursor]
        combine(m, x, y, op, rule, stats)
        cursor += 1
        task['op_cursor'] = cursor
    return True


def work_pair(m, task, stats):
    return work_arithmetic_pair(m, task, stats, task['left'], task['right'], task['rule'])


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
    if not work_arithmetic_pair(m, task, stats, new, prior, 'revisit_v1'):
        return False
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
    next_value = zero_core(m, 'foundation', operation='registered_state_count',
                           operands=(states,))
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


def evaluate_tree(tree, tracking=None):
    if 'leaf' in tree:
        return number(tree['leaf']), str(tree['leaf'])
    a, ae = evaluate_tree(tree['left'], tracking)
    b, be = evaluate_tree(tree['right'], tracking)
    result = operate(a, tree['op'], b, tracking=tracking, context='zero_nexus_transform_v1')
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
    transformations = replace_one_zero(source['tree'], replacement)
    for cursor in range(task.get('zero_cursor', 0), len(transformations)):
        if stats['new'] >= MAX_NEW_EXPRESSIONS_PER_RUN:
            task['zero_cursor'] = cursor
            return False
        transformed = transformations[cursor]
        task['zero_cursor'] = cursor + 1
        try:
            result, expr = evaluate_tree(transformed, tracking=m)
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
    return work_arithmetic_pair(m, task, stats, task['left'], task['right'],
                                'result_feedback_v42')


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
    result = operate(Fraction(0), op, Fraction(value), tracking=m, context=task['rule'])
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


# Persistent memory belongs beside the saved script, not an editor runner.
# Set MEMORY_DIRECTORY explicitly only if the runner hides the source path.
MEMORY_DIRECTORY = None
_MEMORY_DIRECTORY_RESOLVED = None

def _memory_private_runner(path):
    path=os.path.abspath(path).replace('\\','/')
    return (path.startswith('/data/user/') or path.startswith('/data/data/')) and '/ru.iiec.pydroid3/' in path

def _memory_saved_script_candidates():
    import sys
    candidates=[globals().get('__file__')]
    if sys.argv:candidates.append(sys.argv[0])
    # Some editor wrappers retain the original filename in their launch frame.
    frame=sys._getframe()
    while frame is not None:
        for name in ('fakepyfile','original_script','script_path'):
            value=frame.f_locals.get(name)
            if isinstance(value,str):candidates.append(value)
        frame=frame.f_back
    for value in candidates:
        if not isinstance(value,str) or value.startswith('<') or not value.lower().endswith('.py'):continue
        path=os.path.realpath(os.path.expanduser(value))
        if os.path.isfile(path) and not _memory_private_runner(path):yield path

def _memory_folder_value(value):
    if not isinstance(value,str) or not value.strip():raise ValueError('A containing folder is required')
    value=value.strip().strip('"').strip("'")
    path=os.path.realpath(os.path.expanduser(value))
    if os.path.isfile(path) and path.lower().endswith('.py'):path=os.path.dirname(path)
    if not os.path.isdir(path):raise ValueError('Folder does not exist: '+path)
    return path

def _memory_bundle_digest(path):
    import hashlib
    digest=hashlib.sha256()
    if os.path.isfile(path):
        with open(path,'rb') as handle:
            for block in iter(lambda:handle.read(1024*1024),b''):digest.update(block)
    elif os.path.isdir(path):
        for directory,subdirs,files in os.walk(path):
            subdirs.sort()
            for name in sorted(files):
                child=os.path.join(directory,name)
                digest.update(os.path.relpath(child,path).encode('utf-8'))
                digest.update(_memory_bundle_digest(child).encode('ascii'))
    else:raise ValueError('Memory bundle item is not a regular file or directory')
    return digest.hexdigest()

def _memory_copy_bundle(source,target):
    """Copy retained state exactly; source stays intact and main installs last."""
    import shutil
    if os.path.abspath(source)==os.path.abspath(target) or not os.path.isfile(source):return
    if os.path.exists(target):return
    source_dir=os.path.dirname(source);target_dir=os.path.dirname(target);base=os.path.basename(source)
    names=sorted(n for n in os.listdir(source_dir) if n==base or n.startswith(base+'.'))
    marker=target+'.location-import.json'
    if os.path.isfile(marker):
        with open(marker,encoding='utf-8') as handle:manifest=json.load(handle)
        if manifest.get('source')!=source or manifest.get('target')!=target:
            raise ValueError('Different memory transfer is already pending in that folder')
        names=manifest['names']
    else:
        conflicts=[n for n in names if os.path.exists(os.path.join(target_dir,n))]
        if conflicts:raise ValueError('Destination has partial memory state; existing files preserved: '+', '.join(conflicts[:3]))
        manifest={'source':source,'target':target,'names':names,
            'digests':{n:_memory_bundle_digest(os.path.join(source_dir,n)) for n in names}}
        with open(marker,'x',encoding='utf-8') as handle:
            json.dump(manifest,handle,sort_keys=True);handle.flush();os.fsync(handle.fileno())
    for name in [n for n in names if n!=base]+[base]:
        original=os.path.join(source_dir,name);destination=os.path.join(target_dir,name)
        expected=manifest['digests'][name]
        if _memory_bundle_digest(original)!=expected:raise ValueError('Source memory changed during folder transfer')
        if os.path.exists(destination):
            if _memory_bundle_digest(destination)!=expected:raise ValueError('Destination memory changed; refusing overwrite')
            continue
        staging=destination+'.location-copy'
        if os.path.isdir(staging):shutil.rmtree(staging)
        elif os.path.exists(staging):os.unlink(staging)
        if os.path.isdir(original):shutil.copytree(original,staging)
        else:shutil.copy2(original,staging)
        if _memory_bundle_digest(staging)!=expected:raise ValueError('Memory transfer verification failed')
        os.replace(staging,destination)
    os.unlink(marker)
    print('Existing memory and sidecars copied to:',target_dir)

def memory_path():
    global _MEMORY_DIRECTORY_RESOLVED
    if _MEMORY_DIRECTORY_RESOLVED is not None:return os.path.join(_MEMORY_DIRECTORY_RESOLVED,MEMORY_FILENAME)
    original_dir=os.path.dirname(os.path.abspath(globals().get('__file__') or os.path.join(os.getcwd(),'engine.py')))
    locator=os.path.join(original_dir,'zero_theorem_memory_location.json')
    selected=None
    if MEMORY_DIRECTORY is not None:selected=_memory_folder_value(MEMORY_DIRECTORY)
    if selected is None:
        selected=next((os.path.dirname(p) for p in _memory_saved_script_candidates()),None)
    if selected is None and not _memory_private_runner(os.getcwd()):
        # The working directory is useful only if it already holds this memory
        # or a saved engine, not as a silent fallback to an arbitrary folder.
        cwd=os.getcwd()
        saved=any(n.startswith('zero_theorem') and n.endswith('.py') for n in os.listdir(cwd))
        if saved or os.path.isfile(os.path.join(cwd,MEMORY_FILENAME)):selected=cwd
    if selected is None and os.path.isfile(locator):
        with open(locator,encoding='utf-8') as handle:entry=json.load(handle)
        if entry.get('memory_filename')==MEMORY_FILENAME:
            selected=_memory_folder_value(entry['directory'])
    prompted=False
    while selected is None:
        print('The editor has hidden the saved script folder.')
        try:answer=input('Folder containing your saved engine .py: ')
        except EOFError as exc:raise RuntimeError('Set MEMORY_DIRECTORY to the saved script folder before running.') from exc
        try:selected=_memory_folder_value(answer)
        except ValueError as exc:print(str(exc));continue
        prompted=True
    target=os.path.join(selected,MEMORY_FILENAME)
    _memory_copy_bundle(os.path.join(original_dir,MEMORY_FILENAME),target)
    if prompted:
        temporary=locator+'.tmp'
        with open(temporary,'w',encoding='utf-8') as handle:
            json.dump({'directory':selected,'memory_filename':MEMORY_FILENAME},handle)
            handle.flush();os.fsync(handle.fileno())
        os.replace(temporary,locator)
    _MEMORY_DIRECTORY_RESOLVED=selected
    return target


def load_memory():
    path = memory_path()
    if not os.path.exists(path): return empty_memory()
    m = _zt_load_file(path)
    if m.get('schema') != 1 or m.get('version') != VERSION:
        raise ValueError('Incompatible memory; original file left untouched')
    return m


def save_memory(m):
    # Runtime-only hash set is rebuilt from persistent keys, never serialized.
    m.pop('_zero_reserved_primitive_budget', None)
    m.pop('_primitive_work_remaining', None)
    m.pop('_keys', None)
    m.pop('_pending_keys', None)
    m.pop('_blocked_keys', None)
    m.pop('_journal_run_count', None)
    m.pop('_v45_signatures', None)
    m.pop('_symbolic_keys', None)
    m.pop('_symbolic_values', None)
    m.pop('_symbolic_ref_ids', None)
    m.pop('_symbolic_nexus_keys', None)
    m.pop('_complex_constructions', None)
    m.pop('_canonical_keys', None)
    path = memory_path()
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(m, f, ensure_ascii=False, separators=(',', ':'))
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def query(m, text):
    if 'archive_integration' in m and query_unified(m, text):
        return
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
    kind = task['kind']
    if kind in ('position', 'symbolic_position'):
        return 'reference:%s:slot:%s' % (REFERENCE_INPUT, task['source_position'])
    domain = ('symbolic' if kind.startswith('symbolic_') else
              'complex' if kind in ('complex', 'complex_feedback') else 'rational')
    for key in ('source', 'new', 'left', 'value'):
        if key in task: return domain + ':' + str(task[key])
    if 'items' in task: return domain + ':set:' + ','.join(map(str, task['items']))
    return 'system:' + kind


def upgrade_tracking_namespaces(m):
    led = m['tangent_ledger']
    if led.get('parent_namespace_version') == 1:
        return
    # Old aggregate rows cannot be separated reliably without their full log.
    # Preserve them; all subsequent rows receive explicit archive prefixes.
    led['parent_namespace_version'] = 1
    led['parent_namespace_boundary'] = {
        'previous_generated': led['generated'],
        'previous_selected': led['selected'],
        'previous_completed': led['completed'],
        'legacy_untyped_rows_retained': True}
    led.setdefault('paused', 0)
    journal(m, 'typed_parent_tracking_boundary', **led['parent_namespace_boundary'])


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


def tangent_completed(m, task, selected_key=None):
    led = m['tangent_ledger']
    led['completed'] += 1
    parent = tangent_parent(task)
    slot = led['parents'].setdefault(parent, {'generated': 0, 'selected': 0, 'completed': 0})
    slot['completed'] += 1
    journal(m, 'tangent_completed', parent=parent, kind=task['kind'],
            task_key=selected_key if selected_key is not None else task_key(task))


def tangent_paused(m, task, selected_key):
    led = m['tangent_ledger']
    led['paused'] = led.get('paused', 0) + 1
    parent = tangent_parent(task)
    slot = led['parents'].setdefault(parent, {'generated': 0, 'selected': 0, 'completed': 0})
    slot['paused'] = slot.get('paused', 0) + 1
    journal(m, 'tangent_paused', parent=parent, kind=task['kind'],
            task_key=selected_key, resume_task_key=task_key(task),
            reason='expression_budget', resume_state=dict(task))


def complex_key(a, b):
    return encode(a) + ('+' if b >= 0 else '') + encode(b) + 'i'


def _complex_operate_exact(a, b, op):
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


def complex_operate(a, b, op, tracking=None, context='complex_arithmetic_v44'):
    result = zero_core(tracking, 'complex', operation=op, operands=(a, b))
    record_kernel_operation(tracking, 'complex', op,
                            'blocked' if result is None else 'succeeded', context,
                            'division_by_zero' if result is None else None)
    return result


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
    zero_core(m, 'complex', record=ca['expressions'][-1])
    first = key not in ca['results']
    ca['results'].setdefault(key, []).append(idx)
    journal(m, 'complex_expression', complex_id=idx, value=key, expr=expr,
            parents=parents, operation=op, first_value=first)
    if 'v45_observations' in m:
        observe_v45_complex(m, ca['expressions'][-1])
    if ca.get('feedback_version') == 1:
        schedule_complex_feedback(m)
    if 'archive_integration' in m:
        sync_archive_records(m, 'complex')
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
        result = complex_operate(a, b, op, tracking=m)
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
    if 'archive_integration' in m and query_unified(m, text):
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
        raise RuntimeError('SymPy is required for V4.6.4. In Pydroid3, open Pip, '
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


def _symbolic_apply_exact(a, op, b=None):
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


def symbolic_apply(a, op, b=None, tracking=None, context='exact_algebraic_v46'):
    result, reason = zero_core(tracking, 'symbolic', operation=op, operands=(a, b))
    blocked = {'zero_or_unresolved_denominator', 'zero_to_nonpositive_power',
               'zero_or_unresolved_base'}
    outcome = 'succeeded' if reason is None else ('blocked' if reason in blocked else 'limited')
    record_kernel_operation(tracking, 'symbolic', op, outcome, context, reason)
    return result, reason


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
    ensure_symbolic_construction(m, rec)
    zero_core(m, 'symbolic', record=rec)
    sa['expressions'].append(rec)
    sa['results'].setdefault(rec['value'], []).append(idx)
    m.setdefault('_symbolic_values', {})[idx] = value
    schedule_symbolic_feedback(m, rec)
    if sa.get('zero_nexus_version') == 1:
        schedule_symbolic_zero_feedback(m)
    if pathway in ('numeric_to_symbolic_v46', 'numeric_to_symbolic_v464') and len(sources) == 1:
        source = sources[0]
        if source['archive'] in ('rational', 'complex'):
            sa.setdefault('source_import_links', {'rational': {}, 'complex': {}})[source['archive']][str(source['id'])] = idx
    if 'archive_integration' in m:
        sync_archive_records(m, 'symbolic')
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
    upgrade_construction_imports(m)
    m['rule_registry'].setdefault('exact_algebraic_v46', {
        'status': 'active_exploration_not_foundation',
        'operations': ['+', '-', '*', '/', '**', 'sqrt'],
        'root_convention': 'principal_complex_root',
        'power_exponents': 'bounded_rationals'})


def upgrade_construction_imports(m):
    sa = m['symbolic_archive']
    if sa.get('construction_import_version') == 1:
        return
    sa['construction_import_version'] = 1
    sa['construction_import_cursors'] = {'rational': 0, 'complex': 0}
    sa['source_import_links'] = {'rational': {}, 'complex': {}}
    sa['source_import_kinds'] = {'rational': {}, 'complex': {}}
    sa['import_deferred'] = {'rational': {}, 'complex': {}}
    # Earlier representative imports remain valid records. Reuse them where
    # their construction is complete; scan source IDs from zero to fill gaps.
    for rec in sa['expressions']:
        if rec['pathway'] not in ('numeric_to_symbolic_v46', 'numeric_to_symbolic_v464'):
            continue
        if len(rec.get('sources', [])) == 1:
            ref = rec['sources'][0]
            if ref['archive'] in sa['source_import_links']:
                sa['source_import_links'][ref['archive']][str(ref['id'])] = rec['id']


def complex_symbolic_construction(m, idx):
    cache = m.setdefault('_complex_constructions', {})
    if idx in cache:
        return cache[idx]
    sp = sympy_module()
    rec = m['complex_archive']['expressions'][idx]
    if rec['parents'] and rec['operation'] in OPERATIONS:
        tree = {'op': rec['operation'], 'args': [
            complex_symbolic_construction(m, parent) for parent in rec['parents']]}
    elif rec['pathway'] == 'symbolic_to_complex_v46' and rec.get('sources'):
        tree = ensure_symbolic_construction(m,
            m['symbolic_archive']['expressions'][rec['sources'][0]['id']])
    else:
        ar, ai = number(rec['real']), number(rec['imaginary'])
        value = sp.Rational(ar.numerator, ar.denominator) + sp.I * sp.Rational(ai.numerator, ai.denominator)
        tree = {'exact': symbolic_pack(value)}
    cache[idx] = tree
    return tree


def import_numeric_construction(m, domain, source_id):
    sp = sympy_module()
    sa = m['symbolic_archive']
    upgrade_construction_imports(m)
    archive = m if domain == 'rational' else m['complex_archive']
    source = archive['expressions'][source_id]
    key = str(source_id)
    ref = {'archive': domain, 'id': source_id}
    # A numeric embedding is already the same construction represented in
    # another archive. Link its origin; importing a fresh wrapper repeatedly
    # would create an endless symbolic -> numeric -> symbolic mirror chain.
    if (source['pathway'] in ('symbolic_to_rational_v46', 'symbolic_to_complex_v46')
            and not source['parents'] and len(source.get('sources', [])) == 1
            and source['sources'][0]['archive'] == 'symbolic'):
        origin = source['sources'][0]['id']
        if type(origin) is not int or not 0 <= origin < len(sa['expressions']):
            raise ValueError('Numeric embedding has a missing symbolic origin')
        sa['source_import_links'][domain][key] = origin
        sa['source_import_kinds'][domain][key] = 'representation_link'
        sa['import_deferred'][domain].pop(key, None)
        return origin
    if domain == 'rational':
        q = number(source['value'])
        value = sp.Rational(q.numerator, q.denominator)
        tree = rational_symbolic_construction(m, source['tree'])
    else:
        ar, ai = number(source['real']), number(source['imaginary'])
        value = sp.Rational(ar.numerator, ar.denominator) + sp.I * sp.Rational(ai.numerator, ai.denominator)
        tree = complex_symbolic_construction(m, source_id)
    existing = sa['source_import_links'][domain].get(key)
    if existing is not None:
        rec = sa['expressions'][existing]
        if rec.get('construction') == tree and rec.get('sources') == [ref]:
            sa['source_import_kinds'][domain][key] = 'construction_import'
            sa['import_deferred'][domain].pop(key, None)
            return existing
    idx = symbolic_record(m, value, source['expr'], [], 'embed',
                          'numeric_to_symbolic_v464', sources=[ref],
                          depth=source['depth'], construction=tree)
    if idx is None:
        for candidate in sa['results'].get(str(value), []):
            rec = sa['expressions'][candidate]
            if rec.get('sources') == [ref] and rec.get('construction') == tree:
                idx = candidate
                break
    if idx is None:
        sa['import_deferred'][domain][key] = {
            'reason': 'depth_or_value_limit', 'source_depth': source['depth']}
        return None
    sa['source_import_links'][domain][key] = idx
    sa['source_import_kinds'][domain][key] = 'construction_import'
    sa['import_deferred'][domain].pop(key, None)
    return idx


def import_symbolic_sources(m):
    """Visit every source expression ID, with persisted per-archive cursors."""
    sa = m['symbolic_archive']
    upgrade_construction_imports(m)
    limits = [MAX_DEPTH, MAX_BITS, SYMBOLIC_MAX_NODES]
    previous = sa.get('construction_import_limits')
    if previous is not None and previous != limits:
        # Revisit explicitly deferred imports after configuration changes.
        # Existing source links prevent duplicate imports during the scan.
        sa['construction_import_cursors'] = {'rational': 0, 'complex': 0}
    sa['construction_import_limits'] = limits
    for domain, archive in (('rational', m), ('complex', m['complex_archive'])):
        cursor = sa['construction_import_cursors'][domain]
        stop = min(len(archive['expressions']), cursor + SYMBOLIC_IMPORT_PER_RUN)
        while cursor < stop:
            import_numeric_construction(m, domain, cursor)
            cursor += 1
            sa['construction_import_cursors'][domain] = cursor


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
    elif rec['pathway'] in ('numeric_to_symbolic_v46', 'numeric_to_symbolic_v464') and rec['sources']:
        source = rec['sources'][0]
        if source['archive'] == 'rational':
            tree = rational_symbolic_construction(m, m['expressions'][source['id']]['tree'])
        else:
            tree = complex_symbolic_construction(m, source['id'])
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


def evaluate_symbolic_construction(tree, tracking=None):
    if 'exact' in tree:
        value = symbolic_unpack(tree['exact'])
        return value, '(' + str(value) + ')', None
    children = [evaluate_symbolic_construction(child, tracking) for child in tree['args']]
    for _, _, reason in children:
        if reason:
            return None, '', reason
    op = tree['op']
    a, ae, _ = children[0]
    if op == 'sqrt':
        value, reason = symbolic_apply(a, op, tracking=tracking, context='zero_nexus_symbolic_v461')
        expr = 'sqrt(' + ae + ')'
    else:
        b, be, _ = children[1]
        value, reason = symbolic_apply(a, op, b, tracking=tracking, context='zero_nexus_symbolic_v461')
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
    value, expr, reason = evaluate_symbolic_construction(tree, tracking=m)
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
    idx = import_numeric_construction(m, 'rational', real_id)
    if idx is None:
        raise ValueError('Unable to reference foundation expression symbolically')
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
    result, reason = symbolic_apply(a, op, b, tracking=m)
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
    if words[0].lower() == 'symbolic' and 'archive_integration' in m:
        return query_unified(m, text)
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


def operation_counter():
    return {'attempts': 0, 'succeeded': 0, 'blocked': 0, 'limited': 0}


def record_kernel_operation(m, domain, op, outcome, context, reason=None):
    if m is None or 'archive_integration' not in m:
        return
    runtime = m['archive_integration']['runtime_operations']
    group = runtime['by_archive'].setdefault(domain, {
        **operation_counter(), 'by_operation': {}, 'by_context': {}})
    operation = group['by_operation'].setdefault(op, operation_counter())
    context_count = group['by_context'].setdefault(context, operation_counter())
    for counter in (runtime, group, operation, context_count):
        counter['attempts'] += 1
        counter[outcome] += 1
    if reason:
        runtime['reasons'][reason] = runtime['reasons'].get(reason, 0) + 1


def archive_records(m, domain):
    if domain == 'rational':
        return m['expressions']
    return m.get(domain + '_archive', {}).get('expressions', [])


def exact_lookup_key(value):
    sp = sympy_module()
    if value.is_Rational:
        return str(value)
    real, imaginary = value.as_real_imag()
    if real.is_Rational and imaginary.is_Rational:
        return str(real + sp.I * imaginary)
    return str(value)


def record_lookup_key(m, domain, rec):
    cache = m.setdefault('_canonical_keys', {})
    ref = (domain, rec['id'])
    if ref in cache:
        return cache[ref]
    sp = sympy_module()
    if domain == 'roles':
        return 'role:' + json.dumps([rec['kind'], rec['label'], rec['body']], sort_keys=True)
    if domain == 'calculus':
        value = calculus_value(rec['coefficients'])
    elif domain == 'rational':
        q = number(rec['value'])
        value = sp.Rational(q.numerator, q.denominator)
    elif domain == 'complex':
        ar, ai = number(rec['real']), number(rec['imaginary'])
        value = sp.Rational(ar.numerator, ar.denominator) + sp.I * sp.Rational(ai.numerator, ai.denominator)
    else:
        value = symbolic_value(m, rec['id'])
    cache[ref] = exact_lookup_key(value)
    return cache[ref]


def archived_record_category(rec):
    path = rec.get('pathway', '')
    if path == ROLE_RULE:
        return 'role_transition'
    if path in ('polynomial_calculus_v47', 'zero_slot_calculus_v471'):
        return 'calculus'
    if path == 'foundation_state_count_v3':
        return 'foundation'
    if rec.get('operation') == 'seed':
        return 'seed'
    if path in ('numeric_to_symbolic_v46', 'numeric_to_symbolic_v464',
                'symbolic_to_rational_v46', 'symbolic_to_complex_v46',
                'calculus_to_rational_v47',
                'rational_embedding_v44'):
        return 'representation'
    if 'nexus' in rec or path.startswith('zero_nexus_'):
        return 'nexus'
    return 'arithmetic'


def sync_archive_records(m, domain):
    state = m['archive_integration']
    totals = state['archive_totals']
    group = totals['by_archive'].setdefault(domain, {
        'records': 0, 'by_category': {}, 'by_outer_operation': {}})
    records = archive_records(m, domain)
    cursor = state['indexed_record_cursors'][domain]
    while cursor < len(records):
        rec = records[cursor]
        key = record_lookup_key(m, domain, rec)
        rec['unified_value_key'] = key
        bucket = m['unified_results'].setdefault(key, {'rational': [], 'complex': [], 'symbolic': []})
        bucket.setdefault(domain, []).append(cursor)
        category = archived_record_category(rec)
        group['records'] += 1
        totals['records'] += 1
        group['by_category'][category] = group['by_category'].get(category, 0) + 1
        totals['by_category'][category] = totals['by_category'].get(category, 0) + 1
        if category in ('arithmetic', 'nexus'):
            tree = rec.get('construction', rec.get('tree', {}))
            op = rec.get('operation')
            if op not in SYMBOLIC_BINARY_OPERATIONS + ('sqrt',):
                op = tree.get('op')
            if op is not None:
                group['by_outer_operation'][op] = group['by_outer_operation'].get(op, 0) + 1
                totals['by_outer_operation'][op] = totals['by_outer_operation'].get(op, 0) + 1
        cursor += 1
        state['indexed_record_cursors'][domain] = cursor


def upgrade_archive_integration(m):
    if 'archive_integration' not in m:
        m['archive_integration'] = {
            'schema': 1, 'indexed_record_cursors': {'rational': 0, 'complex': 0, 'symbolic': 0},
            'archive_totals': {'records': 0, 'by_category': {}, 'by_outer_operation': {}, 'by_archive': {}},
            'runtime_operations': {**operation_counter(), 'by_archive': {}, 'reasons': {},
                'boundary': {'previous_runs': len(m['runs']),
                             'historical_attempts_not_reconstructed': True}}}
        m['unified_results'] = {}
        journal(m, 'whole_engine_tracking_boundary', previous_runs=len(m['runs']))
    m['network']['scope'] = 'legacy_rational_recorded_transitions'
    for domain in ('rational', 'complex', 'symbolic'):
        sync_archive_records(m, domain)


def unified_query_value(text):
    import re
    words = text.strip().split(maxsplit=1)
    if words and words[0].lower() == 'symbolic':
        if len(words) != 2:
            raise ValueError('Enter a value or expression after symbolic')
        text = words[1]
    compact = text.replace(' ', '')
    # Preserve the existing a+bi query spelling, with the same safe parser.
    compact = re.sub(r'(?<=[0-9)])i\b', '*i', compact)
    return parse_symbolic_query(compact)


def query_unified(m, text):
    if 'archive_integration' not in m:
        return False
    try:
        value = unified_query_value(text)
        key = exact_lookup_key(value)
    except (ValueError, SyntaxError, ZeroDivisionError, OverflowError) as exc:
        if text.strip().lower().startswith('symbolic '):
            print('Value query:', exc)
            return True
        return False
    bucket = m['unified_results'].get(key, {'rational': [], 'complex': [], 'symbolic': []})
    print('\nValue %s: %d archive records across all branches' %
          (key, sum(len(ids) for ids in bucket.values())))
    for domain in ZERO_CORE_DOMAINS:
        ids = bucket.get(domain, [])
        print('  %s: %d records' % (domain, len(ids)))
        records = archive_records(m, domain)
        for idx in ids[:20]:
            rec = records[idx]
            print('    %s:%d %s [%s; %s]' %
                  (domain, idx, rec['expr'], rec['pathway'], archived_record_category(rec)))
        if len(ids) > 20:
            print('    ... %d more %s records' % (len(ids) - 20, domain))
    if value.is_Rational:
        qkey = encode(Fraction(int(value.p), int(value.q)))
        proposals = [p for p in m['zero_proposals'] if p['result'] == qkey]
        print('  Unapproved zero proposals:', len(proposals))
        for proposal in proposals[:3]:
            print('    PROPOSAL:', proposal['expression'])
    print('Representation records are labelled; record counts are not counts of unique formulas.')
    return True


def print_operation_totals(m):
    state = m['archive_integration']
    archive = state['archive_totals']
    runtime = state['runtime_operations']
    print('\nWHOLE-ENGINE OPERATION TOTALS')
    print('Runtime kernel calls since tracking boundary:', runtime['attempts'],
          'computed:', runtime['succeeded'], 'blocked:', runtime['blocked'],
          'resource-limited:', runtime['limited'])
    for domain in dict.fromkeys((*ZERO_CORE_DOMAINS, *runtime['by_archive'])):
        counts = runtime['by_archive'].get(domain, operation_counter())
        print('  %s: %d calls; %d computed; %d blocked; %d limited' %
              (domain, counts['attempts'], counts['succeeded'], counts['blocked'], counts['limited']))
        print('    Calls by operation:', {op: values['attempts']
              for op, values in counts.get('by_operation', {}).items()})
    print('Accepted archive records, including historical records:', archive['records'])
    print('Archive categories:', archive['by_category'])
    print('Archived constructions by outer operation:', archive['by_outer_operation'])
    print('Nexus records:', len(m['nexus_events']), 'rational;',
          len(m.get('symbolic_nexus_events', [])), 'symbolic')
    print('Past operation attempts are not inferred from stored results.')


def archive_link_audit(m):
    """Inspect saved references only. No evaluation, generation or writeback."""
    archives = {'rational': m.get('expressions', []),
                'complex': m.get('complex_archive', {}).get('expressions', []),
                'symbolic': m.get('symbolic_archive', {}).get('expressions', []),
                'calculus': m.get('calculus_archive', {}).get('expressions', []),
                'roles': m.get('roles_archive', {}).get('expressions', [])}
    nodes = {(domain, idx): rec for domain, records in archives.items()
             for idx, rec in enumerate(records)}
    dependencies = {node: set() for node in nodes}
    roots = set()
    issues, examples = 0, []

    def issue(message):
        nonlocal issues
        issues += 1
        if len(examples) < 20:
            examples.append(message)

    def reference(owner, domain, idx, context):
        target = (domain, idx) if isinstance(domain, str) and type(idx) is int else None
        if target not in nodes:
            issue('%s: missing %s reference %s:%s' % (owner, context, domain, idx))
            return
        if owner in dependencies:
            dependencies[owner].add(target)
            if owner[0] == domain and idx >= owner[1]:
                issue('%s: parent %s is not earlier in the same archive' % (owner, target))

    foundation_ids = {rec.get('value'): idx for idx, rec in enumerate(archives['rational'])
                      if rec.get('pathway') == 'foundation_state_count_v3'}
    states = m.get('foundation', {}).get('states', [])
    if states != list(range(len(states))):
        issue('Foundation states are not the consecutive registered sequence')
    for position, state in enumerate(states):
        idx = foundation_ids.get(str(state))
        if idx is None:
            issue('Missing foundation expression for state %s' % state)
            continue
        node = ('rational', idx)
        if state == 0:
            roots.add(node)
        else:
            # These are dependencies of the declared state-count rule,
            # not reconstructed timestamps or scheduler decisions.
            for previous in states[:position]:
                reference(node, 'rational', foundation_ids.get(str(previous)), 'state-count')

    for node, rec in nodes.items():
        domain, idx = node
        if rec.get('id') != idx:
            issue('%s: stored ID differs from archive position' % (node,))
        for parent in rec.get('parents', []):
            reference(node, domain, parent, 'parent')
        for source in rec.get('sources', []):
            reference(node, source.get('archive'), source.get('id'), 'source')
        if (rec.get('operation') == 'seed' and not rec.get('parents')
                and not rec.get('sources')):
            roots.add(node)
        if domain == 'complex' and rec.get('pathway') == 'rational_embedding_v44':
            reference(node, 'rational', foundation_ids.get(rec.get('real')), 'foundation embedding')
        if domain == 'symbolic':
            nexus = rec.get('nexus', {})
            for field in ('source_id', 'selected_value_id'):
                if field in nexus:
                    reference(node, 'symbolic', nexus[field], 'nexus ' + field)

    indexes = {'rational': m.get('results', {}),
               'complex': m.get('complex_archive', {}).get('results', {}),
               'symbolic': m.get('symbolic_archive', {}).get('results', {}),
               'calculus': m.get('calculus_archive', {}).get('results', {}),
               'roles': m.get('roles_archive', {}).get('results', {})}
    for domain, index in indexes.items():
        for value, ids in index.items():
            for idx in ids:
                owner = '%s result index %s' % (domain, value)
                reference(owner, domain, idx, 'result')
                if type(idx) is int and (domain, idx) in nodes:
                    if nodes[(domain, idx)].get('value') != value:
                        issue('%s: record %s is indexed under a different value' % (owner, idx))
    for (domain, idx), rec in nodes.items():
        if idx not in indexes[domain].get(rec.get('value'), []):
            issue('%s:%s: expression missing from its result index' % (domain, idx))
        if 'unified_value_key' in rec:
            bucket = m.get('unified_results', {}).get(rec['unified_value_key'], {})
            if idx not in bucket.get(domain, []):
                issue('%s:%s: expression missing from the unified result index' % (domain, idx))
    for value, bucket in m.get('unified_results', {}).items():
        for domain, ids in bucket.items():
            for idx in ids:
                reference('unified index %s' % value, domain, idx, 'result')
                if type(idx) is int and (domain, idx) in nodes:
                    if nodes[(domain, idx)].get('unified_value_key') != value:
                        issue('Unified index %s points to a record with a different lookup key' % value)
    imports = m.get('symbolic_archive', {}).get('source_import_links', {})
    import_kinds = m.get('symbolic_archive', {}).get('source_import_kinds', {})
    for domain, links in imports.items():
        for source_id, symbolic_id in links.items():
            try:
                source_number = int(source_id)
            except (ValueError, TypeError):
                issue('Import link has an invalid source ID %s:%s' % (domain, source_id))
                continue
            reference('import link %s:%s' % (domain, source_id), domain, source_number, 'source')
            reference('import link %s:%s' % (domain, source_id), 'symbolic', symbolic_id, 'symbolic target')
            if ((domain, source_number) in nodes and type(symbolic_id) is int
                    and ('symbolic', symbolic_id) in nodes):
                original = nodes[(domain, source_number)]
                target = nodes[('symbolic', symbolic_id)]
                if import_kinds.get(domain, {}).get(source_id) == 'representation_link':
                    if {'archive': 'symbolic', 'id': symbolic_id} not in original.get('sources', []):
                        issue('Import representation link %s:%s has a different symbolic origin' % (domain, source_id))
                elif {'archive': domain, 'id': source_number} not in target.get('sources', []):
                    issue('Construction import %s:%s points to another source construction' % (domain, source_id))

    zeros = m.get('foundation', {}).get('zero_records', [])
    zero_ids = {record.get('id') for record in zeros}
    if [record.get('id') for record in zeros] != ['Z%d' % i for i in range(len(states))]:
        issue('Zero-record IDs do not match the registered foundation states')
    for idx, proposal in enumerate(m.get('observer', {}).get('proposals', [])):
        reference('observer proposal %d' % idx, 'rational', proposal.get('source_id'), 'source')
    blocked = m.get('blocked', [])
    for idx, record in enumerate(blocked):
        if record.get('id') != idx:
            issue('Blocked record %d has a mismatched ID' % idx)
        for field in ('left', 'right'):
            reference('blocked record %d' % idx, 'rational', record.get(field), field)
    for idx, proposal in enumerate(m.get('zero_proposals', [])):
        blocked_id = proposal.get('blocked_id')
        if type(blocked_id) is not int or not 0 <= blocked_id < len(blocked):
            issue('Zero proposal %d has a missing blocked-operation ID' % idx)
        if proposal.get('zero_record') not in zero_ids:
            issue('Zero proposal %d has a missing zero-record reference' % idx)
    legacy_positional_observations = 0
    for domain, events, fields in (
            ('rational', m.get('nexus_events', []), ('source_id', 'registered_value_id', 'result_id')),
            ('symbolic', m.get('symbolic_nexus_events', []),
             ('source_id', 'selected_value_id', 'symbolic_result_id'))):
        for idx, event in enumerate(events):
            # V4.2 recorded positional observations without creating an
            # expression. A null result ID is intentional only for this
            # explicitly identified historical event format. Preserve it;
            # never invent a result link from numerical equality.
            legacy_observation = (
                domain == 'rational'
                and event.get('rule') == 'zero_nexus_position_operation_v42'
                and event.get('slot_kind') == 'reference_position_operation'
                and event.get('status') == 'positional_operation_observation'
                and 'result_id' in event and event['result_id'] is None)
            if legacy_observation:
                legacy_positional_observations += 1
                source = event.get('source')
                position = event.get('source_position')
                selected = event.get('selected_value')
                if (source != m.get('reference', {}).get('input')
                        or not isinstance(source, str)
                        or type(position) is not int
                        or not 1 <= position <= len(source)
                        or source[position - 1] != '0'
                        or type(selected) is not int or not 0 <= selected <= 9
                        or event.get('operation') not in OPERATIONS
                        or not isinstance(event.get('local_result'), str)
                        or event.get('transformed') != (
                            source[:position - 1] + str(selected) + source[position:])):
                    issue('rational nexus event %d: malformed legacy positional observation' % idx)
            for field in fields:
                if field in event:
                    if legacy_observation and field == 'result_id':
                        continue
                    reference('%s nexus event %d' % (domain, idx), domain, event[field], field)
            if event.get('zero_nexus') not in zero_ids:
                issue('%s nexus event %d has a missing zero-record reference' % (domain, idx))

    children = {node: set() for node in nodes}
    for node, parents in dependencies.items():
        for parent in parents:
            children[parent].add(node)

    def reachable(start):
        seen = set(start)
        pending = deque(start)
        while pending:
            for child in children[pending.popleft()]:
                if child not in seen:
                    seen.add(child)
                    pending.append(child)
        return seen

    indegrees = {node: len(parents) for node, parents in dependencies.items()}
    ready = deque(node for node, degree in indegrees.items() if degree == 0)
    ordered = 0
    while ready:
        node = ready.popleft()
        ordered += 1
        for child in children[node]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                ready.append(child)
    unresolved = len(nodes) - ordered
    if unresolved:
        issue('%d records are in or depend on a reference cycle' % unresolved)
    zero_id = foundation_ids.get('0')
    from_zero = reachable([('rational', zero_id)]) if zero_id is not None else set()
    from_roots = reachable(roots)
    unexplained = set(nodes) - from_roots
    if unexplained:
        issue('%d records have no path from zero or a declared seed' % len(unexplained))

    # Queue cursors are not generally expression IDs. Check only typed record
    # fields here, then check cursor ranges according to each worker's format.
    task_refs = {
        'frontier': ('rational', ('left', 'right')),
        'pair': ('rational', ('left', 'right')),
        'nexus': ('rational', ('source', 'value')),
        'revisit': ('rational', ('new',)),
        'consume': ('rational', ()),
        'consume_op': ('rational', ('left', 'right')),
        'zero_scan': ('rational', ('value',)),
        'zero_source': ('rational', ('source',)),
        'complex': ('complex', ('left', 'right')),
        'complex_feedback': ('complex', ('source',)),
        'symbolic_root': ('symbolic', ('source',)),
        'symbolic_pair': ('symbolic', ('source',)),
        'symbolic_nexus': ('symbolic', ('source',)),
        'z0_primitive': ('rational', ('source',)),
        'z0_macro': ('rational', ('source','origin'))}
    queue = m.get('queue', [])
    head = m.get('queue_head', 0)
    if type(head) is not int or not 0 <= head <= len(queue):
        issue('Queue head is outside the saved queue')
        head = 0
    known_kinds = set(task_refs) | {'emerge', 'position', 'symbolic_position'}
    for offset, task in enumerate(queue[head:], head):
        owner = 'queue[%d]' % offset
        kind = task.get('kind')
        if kind not in known_kinds:
            issue('%s: unknown task kind %s' % (owner, kind))
            continue
        if kind in task_refs:
            domain, fields = task_refs[kind]
            for field in fields:
                reference(owner, domain, task.get(field), field)
        if kind == 'z0_primitive' and task.get('primitive') not in (('S',) if m.get('z0_successor_bootstrapped') else ('S','P')):
            issue('%s: invalid Z0 primitive' % owner)
        if kind == 'z0_macro':
            seq=task.get('sequence')
            allowed={tuple(x['sequence']) for x in m.get('rule_registry',{}).get(
                'z0_discovered_successor_macros_v1',{}).get('observations',[])
                if x.get('status')=='validated_primitive_macro'}
            if not m.get('z0_successor_bootstrapped'):
                allowed.update(tuple(x['sequence']) for x in m.get('rule_registry',{}).get(
                    'z0_discovered_successor_macros_v1',{}).get('observations',[])
                    if x.get('status')=='validated_primitive_macro')
            if (not isinstance(seq,list) or tuple(seq) not in allowed or
                type(task.get('step')) is not int or not 0<=task['step']<len(seq)):
                issue('%s: invalid or unvalidated Z0 macro' % owner)
        if kind in ('consume', 'consume_op'):
            for field in ('items', 'remaining', 'path'):
                for idx in task.get(field, []):
                    reference(owner, 'rational', idx, field)
        if 'op_cursor' in task and (type(task['op_cursor']) is not int or
                                    not 0 <= task['op_cursor'] <= 2 * len(OPERATIONS)):
            issue('%s: invalid arithmetic resume cursor' % owner)
        if 'zero_cursor' in task and (type(task['zero_cursor']) is not int or task['zero_cursor'] < 0):
            issue('%s: invalid zero-slot resume cursor' % owner)
        if kind in ('zero_scan', 'zero_source'):
            limit = len(archives['rational']) if kind == 'zero_scan' else len(states)
            cursor, stop = task.get('cursor'), task.get('stop')
            if (type(cursor) is not int or type(stop) is not int
                    or not 0 <= cursor <= stop <= limit):
                issue('%s: invalid saved scan cursor/snapshot' % owner)
        if kind in ('complex_feedback', 'symbolic_pair', 'symbolic_nexus'):
            source, cursor = task.get('source'), task.get('cursor')
            if type(source) is not int or type(cursor) is not int or not 0 <= cursor <= source:
                issue('%s: invalid feedback cursor' % owner)
        if kind == 'symbolic_pair' and (type(task.get('step')) is not int or not 0 <= task['step'] < 10):
            issue('%s: invalid symbolic operation step' % owner)
        if kind == 'symbolic_nexus' and (task.get('direction') not in (0, 1)
                or type(task.get('slot')) is not int or task['slot'] < 0):
            issue('%s: invalid symbolic zero-slot cursor' % owner)

    ca = m.get('calculus_archive', {})
    cqueue, chead = ca.get('queue', []), ca.get('head', 0)
    if type(chead) is not int or not 0 <= chead <= len(cqueue):
        issue('Invalid calculus queue head')
        chead = 0
    for task in cqueue[chead:] + ca.get('deferred', []):
        reference('calculus pending task', 'calculus', task.get('source'), 'source')
        if task.get('operation') not in CALCULUS_OPERATIONS:
            issue('Invalid calculus operation in pending task')
    if not 0 <= ca.get('import_cursor', 0) <= len(archives['rational']):
        issue('Invalid calculus import cursor')

    ra = m.get('roles_archive', {})
    role_records = ra.get('expressions', [])
    rqueue, rhead = ra.get('queue', []), ra.get('head', 0)
    if type(rhead) is not int or not 0 <= rhead <= len(rqueue):
        issue('Invalid roles queue head')
        rhead = 0
    for task in rqueue[rhead:] + ra.get('deferred', []):
        reference('roles pending task', 'roles', task.get('source'), 'source')
        if type(task.get('cursor')) is not int or task['cursor'] < 0:
            issue('Invalid role target cursor')
    expected_variables = [rec['id'] for rec in role_records if rec.get('kind') == 'variable']
    if ra.get('variable_refs', []) != expected_variables:
        issue('Roles variable index differs from variable constructions')
    for idx, rec in enumerate(role_records):
        if idx == 0:
            expected_source = {'archive': 'rational', 'id': foundation_ids.get('0')}
            if (rec.get('rule') != 'reference_foundation_zero' or
                    rec.get('parents') != [] or rec.get('sources') != [expected_source] or
                    rec.get('path') != ['0'] or rec.get('depth') != 0 or
                    rec.get('body') != {'kind': 'numeric', 'value': '0'}):
                issue('Invalid roles origin')
            continue
        parents = rec.get('parents', [])
        if len(parents) != 1 or type(parents[0]) is not int or not 0 <= parents[0] < idx:
            issue('roles:%d: invalid transformation parent' % idx)
            continue
        parent = role_records[parents[0]]
        slot = rec.get('slot', {})
        counter = parent['depth']
        counter_id = foundation_ids.get(str(counter))
        if (slot != {'counter': counter, 'foundation_id': counter_id} or
                counter_id is None or rec.get('depth') != counter + 1 or
                {'archive': 'rational', 'id': counter_id} not in rec.get('sources', [])):
            issue('roles:%d: missing emergent counter slot backing' % idx)
        if rec.get('path') != parent['path'] + [rec.get('label')]:
            issue('roles:%d: incorrect construction path' % idx)
        if rec.get('rule') == 'bind_successor_operation_role':
            expected={'kind':'operation','primitive':rec.get('label'),'input':'natural_counter','output':'natural_counter','nexus':'Z0'}
            if rec.get('label') not in ('S','P') or rec.get('kind')!='operation' or rec.get('body')!=expected:
                issue('roles:%d: invalid primitive operation binding' % idx)
        elif rec.get('rule') in ('retain_zero_successor_context_v495','extend_counter_in_selected_role_v495'):
            if rec.get('kind')!='construction' or rec.get('body',{}).get('kind')!='successor_construction':
                issue('roles:%d: invalid successor construction body' % idx)
            if rec.get('body',{}).get('zero_nexus')!='Z0':
                issue('roles:%d: missing successor construction zero nexus' % idx)
        elif rec.get('rule') == 'bind_connected_repeat_operation_v1':
            if rec.get('kind')!='derived_operation' or rec.get('body',{}).get('kind')!='derived_operation':
                issue('roles:%d: invalid connected operation role' % idx)
            if rec.get('body',{}).get('zero_nexus')!='Z0':
                issue('roles:%d: connected operation bypasses zero' % idx)
        elif rec.get('rule') == 'bind_primitive_operation_role':
            expected={'kind':'operation','primitive':rec.get('label'),'input':'integer','output':'integer','nexus':'Z0'}
            if rec.get('label') not in ('S','P') or rec.get('kind')!='operation' or rec.get('body')!=expected:
                issue('roles:%d: invalid historical primitive role' % idx)
        elif rec.get('rule') == 'assign_name_preserve_payload':
            if rec.get('label') not in ('A', 'a') or rec.get('body') != parent['body'] or rec.get('kind') != 'named':
                issue('roles:%d: invalid name assignment' % idx)
        elif rec.get('rule') == 'introduce_free_variable':
            if rec.get('label') != 'x' or rec.get('body') != {'kind': 'variable', 'symbol': 'x'} or rec.get('kind') != 'variable':
                issue('roles:%d: invalid variable introduction' % idx)
        elif rec.get('rule') == 'select_registered_numeric_state':
            label = rec.get('label')
            numeric_id = foundation_ids.get(label)
            if (numeric_id is None or rec.get('kind') != 'numeric' or
                    rec.get('body') != {'kind': 'numeric', 'value': label} or
                    {'archive': 'rational', 'id': numeric_id} not in rec.get('sources', [])):
                issue('roles:%d: invalid registered state selection' % idx)
        else:
            issue('roles:%d: unknown transformation rule' % idx)
        try:
            if rec.get('value') != role_value(rec['kind'], rec['label'], rec['body']):
                issue('roles:%d: role value differs from its payload' % idx)
        except (KeyError, ValueError, TypeError):
            issue('roles:%d: invalid payload encoding' % idx)
    legacy_boundary = ca.get('role_origin_boundary', len(archives['calculus']))
    if type(legacy_boundary) is not int or not 0 <= legacy_boundary <= len(archives['calculus']):
        issue('Invalid calculus variable-origin migration boundary')
        legacy_boundary = 0
    for idx, rec in enumerate(archives['calculus']):
        if idx < legacy_boundary or rec.get('operation') == 'constant_import':
            continue
        binding = rec.get('variable_source', {})
        ref_id = binding.get('id')
        if binding not in rec.get('sources', []) or binding.get('archive') != 'roles':
            issue('calculus:%d: missing typed variable origin' % idx)
        elif type(ref_id) is not int or not 0 <= ref_id < len(role_records):
            issue('calculus:%d: missing variable construction' % idx)
        elif role_records[ref_id].get('kind') != 'variable':
            issue('calculus:%d: incompatible variable role' % idx)
    for task in cqueue[chead:] + ca.get('deferred', []):
        cursor = task.get('variable_cursor', 0)
        if type(cursor) is not int or not 0 <= cursor <= len(ra.get('variable_refs', [])):
            issue('Invalid calculus variable-path cursor')

    return {'issues': issues, 'examples': examples,
            'legacy_positional_observations': legacy_positional_observations,
            'records': {domain: len(records) for domain, records in archives.items()},
            'dependency_links': sum(len(parents) for parents in dependencies.values()),
            'declared_roots': sorted(roots), 'from_zero': len(from_zero),
            'from_all_declared_roots': len(from_roots),
            'unexplained_records': len(unexplained), 'cycle_or_dependent_records': unresolved,
            'pending_tasks': len(queue) - head}


def print_archive_link_audit(m):
    report = archive_link_audit(m)
    print('\nARCHIVE LINK AUDIT - READ ONLY; NO MATHEMATICAL EVALUATION')
    print('Records by archive:', report['records'])
    print('Typed dependency links:', report['dependency_links'])
    print('Declared roots:', report['declared_roots'])
    print('Records with a provenance path from zero:', report['from_zero'])
    print('Records reachable including declared seeds:', report['from_all_declared_roots'])
    print('Pending tasks inspected:', report['pending_tasks'])
    print('Legacy positional observations (no expression created):',
          report['legacy_positional_observations'])
    print('Structural issues:', report['issues'])
    for example in report['examples']:
        print('  ', example)
    print('Checks saved links and dependency order; does not enumerate all possible mathematical paths.')


ROLE_WORK_PER_RUN = 12
ROLE_MAX_DEPTH = 4
ROLE_RULE = 'zero_slot_role_transform_v471'


def role_body_text(body):
    if body['kind'] == 'numeric':
        return body['value']
    if body['kind'] == 'operation':
        kind=body.get('input')
        expected={'kind':'operation','primitive':body.get('primitive'),'input':kind,'output':kind,'nexus':'Z0'}
        if body!=expected or not (kind=='integer' and body['primitive'] in ('S','P') or
                                 kind=='natural_counter' and body['primitive']=='S'):
            raise ValueError('Invalid primitive operation role payload')
        return body['primitive']+'('+kind+')'
    if body['kind'] == 'variable' and body['symbol'] == 'x':
        return 'x'
    raise ValueError('Unsupported role payload')


def role_value(kind, label, body):
    text = role_body_text(body)
    return label + '[' + text + ']' if kind == 'named' else text


def role_variable(m, idx):
    records = m.get('roles_archive', {}).get('expressions', [])
    if type(idx) is not int or not 0 <= idx < len(records):
        raise ValueError('Calculus requires an archived zero-origin variable')
    rec = records[idx]
    if rec['kind'] != 'variable' or rec['body'] != {'kind': 'variable', 'symbol': 'x'}:
        raise ValueError('Calculus variable source must be a variable-role construction')
    return rec['body']['symbol']


def _role_transition_exact(m, source_id, target):
    """Explicit representation rules, not arithmetic equalities or physical laws.

    Naming preserves the payload. Abstraction introduces a free variable and
    retains the previous construction as its parent, without equating its value
    to x. Selection references a state already produced by the foundation.
    Each step occupies a slot backed by its registered foundation counter.
    """
    records = m['roles_archive']['expressions']
    if type(source_id) is not int or not 0 <= source_id < len(records):
        raise ValueError('Invalid role source')
    source = records[source_id]
    slot = source['depth']
    states = m['foundation']['states']
    if slot >= ROLE_MAX_DEPTH:
        return None, 'role_depth_limit'
    if slot >= len(states):
        return None, 'waiting_for_emergent_slot'
    counter_id = foundation_expression_id(m, states[slot])
    if counter_id is None:
        raise ValueError('Emergent slot has no foundation construction')
    sources = [{'archive': 'rational', 'id': counter_id}]
    if target == 'S':
        kind,label='operation',target
        body={'kind':'operation','primitive':target,'input':'natural_counter','output':'natural_counter','nexus':'Z0'}
        rule='bind_successor_operation_role'
    elif target in ('A', 'a'):
        kind, label, body = 'named', target, dict(source['body'])
        rule = 'assign_name_preserve_payload'
    elif target == 'x':
        kind, label, body = 'variable', 'x', {'kind': 'variable', 'symbol': 'x'}
        rule = 'introduce_free_variable'
    elif type(target) is int and target in states:
        numeric_id = foundation_expression_id(m, target)
        if numeric_id is None:
            raise ValueError('Selected state has no foundation construction')
        ref = {'archive': 'rational', 'id': numeric_id}
        if ref not in sources:
            sources.append(ref)
        kind, label, body = 'numeric', str(target), {'kind': 'numeric', 'value': str(target)}
        rule = 'select_registered_numeric_state'
    else:
        raise ValueError('Unsupported role target')
    return {'kind': kind, 'label': label, 'body': body,
            'value': role_value(kind, label, body), 'rule': rule,
            'parents': [source_id], 'sources': sources,
            'path': source['path'] + [label], 'depth': slot + 1,
            'slot': {'counter': slot, 'foundation_id': counter_id}}, None


def role_record(m, result, operation):
    ra = m['roles_archive']
    rec = dict(result)
    rec.update(id=len(ra['expressions']), expr=' -> '.join(result['path']),
               operation=operation, pathway=ROLE_RULE, formal_rule=ROLE_RULE)
    # Construction identity includes the parent and target; equal endpoints
    # never merge distinct paths. No task silently truncates a path.
    key = json.dumps([rec['parents'], rec['rule'], rec['label'], rec['sources']],
                     sort_keys=True, separators=(',', ':'))
    if key in ra['known_keys']:
        return None
    zero_core(m, 'roles', record=rec)
    ra['known_keys'].append(key)
    ra['expressions'].append(rec)
    ra['results'].setdefault(rec['value'], []).append(rec['id'])
    if rec['kind'] == 'variable':
        ra['variable_refs'].append(rec['id'])
    ra['queue'].append({'source': rec['id'], 'cursor': 0})
    if 'archive_integration' in m:
        sync_archive_records(m, 'roles')
    journal(m, 'zero_slot_role_transition', role_id=rec['id'],
            parents=rec['parents'], rule=rec['rule'], slot=rec.get('slot'))
    return rec['id']


def upgrade_roles(m):
    ra = m.setdefault('roles_archive', {
        'schema': 1, 'expressions': [], 'results': {}, 'known_keys': [],
        'variable_refs': [], 'queue': [], 'head': 0, 'deferred': [],
        'limits': [ROLE_MAX_DEPTH, len(m['foundation']['states'])]})
    limits = [ROLE_MAX_DEPTH, len(m['foundation']['states'])]
    if ra['limits'] != limits:
        ra['queue'].extend(ra['deferred'])
        ra['deferred'] = []
        ra['limits'] = limits
    m['rule_registry'].setdefault(ROLE_RULE, {
        'status': 'explicit_executable_representation_rules',
        'origin': 'archived foundation zero',
        'slot': 'transition k requires registered counter k and its foundation record',
        'targets': ['named A', 'named a', 'free variable x', 'registered numeric states'],
        'rules': ['assign_name_preserve_payload', 'introduce_free_variable',
                  'select_registered_numeric_state'],
        'semantics': 'representation transitions; not numerical equalities',
        'coverage': 'FIFO enumeration of this grammar; bounded depth; no all-mathematics claim'})
    if 'archive_integration' in m:
        m['archive_integration']['indexed_record_cursors'].setdefault('roles', 0)
        sync_archive_records(m, 'roles')
    if not ra['expressions']:
        zero_id = foundation_expression_id(m, 0)
        if zero_id is None:
            raise ValueError('Role exploration requires the archived foundation zero')
        role_record(m, {'kind': 'numeric', 'label': '0',
            'body': {'kind': 'numeric', 'value': '0'}, 'value': '0',
            'parents': [], 'sources': [{'archive': 'rational', 'id': zero_id}],
            'path': ['0'], 'depth': 0, 'rule': 'reference_foundation_zero'}, 'origin')


def work_roles(m):
    upgrade_roles(m)
    ra = m['roles_archive']
    before = len(ra['expressions'])
    for _ in range(ROLE_WORK_PER_RUN):
        if ra['head'] >= len(ra['queue']):
            break
        task = ra['queue'][ra['head']]
        source = ra['expressions'][task['source']]
        if source['depth'] >= min(ROLE_MAX_DEPTH, len(m['foundation']['states'])):
            ra['deferred'].append(dict(task))
        else:
            cursor = task['cursor']
            # Keep the cursor monotonic: future foundation states extend this
            # enumeration without replaying old choices or losing old parents.
            if cursor < 3 + len(m['foundation']['states']):
                target = ('A', 'a', 'x')[cursor] if cursor < 3 else cursor - 3
                result, reason = zero_core(m, 'roles', operation='transform',
                                          operands=(task['source'], target))
                record_kernel_operation(m, 'roles', 'transform',
                                        'limited' if reason else 'succeeded', ROLE_RULE, reason)
                if reason:
                    ra['deferred'].append(dict(task))
                else:
                    role_record(m, result, 'transform')
                    ra['queue'].append({'source': task['source'], 'cursor': cursor + 1})
            else:
                # Waiting for additional registered states is pending work.
                ra['queue'].append(dict(task))
        ra['head'] += 1
    if ra['head'] > 2000:
        ra['queue'] = ra['queue'][ra['head']:]
        ra['head'] = 0
    return {'new': len(ra['expressions']) - before,
            'variable_paths': len(ra['variable_refs']),
            'pending': len(ra['queue']) - ra['head'], 'deferred': len(ra['deferred'])}


def query_roles(m, text):
    words = text.strip().split()
    if not words or words[0].lower() not in ('roles', 'roles-index'):
        return False
    ra = m.get('roles_archive', {'expressions': []})
    if len(words) == 2 and words[1].isdigit():
        idx = int(words[1])
        if idx < len(ra['expressions']):
            print(json.dumps(ra['expressions'][idx], indent=2))
        else:
            print('No role construction with that ID.')
    else:
        print('Executable zero-slot role constructions (representation transitions):')
        for rec in ra['expressions'][-30:]:
            print('  roles:%d %s [%s; value=%s; slot=%s]' %
                  (rec['id'], rec['expr'], rec['rule'], rec['value'], rec.get('slot')))
        print('Use roles 7 (replace 7 with a record number) to inspect ancestry.')
    return True


CALCULUS_WORK_PER_RUN = 8
CALCULUS_IMPORT_PER_RUN = 2
CALCULUS_MAX_DEPTH = 4
CALCULUS_MAX_DEGREE = 8
CALCULUS_OPERATIONS = ('differentiate', 'integrate', 'limit_zero', 'multiply_x')


def calculus_coefficients(values):
    """Ascending exact rational coefficients, with a unique zero encoding."""
    values = [number(v) for v in values]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return [encode(v) for v in values] or ['0']


def calculus_value(coefficients, variable='x'):
    sp = sympy_module()
    x = sp.Symbol(variable, real=True)
    return sp.Add(*(sp.Rational(number(c).numerator, number(c).denominator) * x**i
                    for i, c in enumerate(coefficients)))


def _calculus_apply_exact(operation, coefficients):
    """Termwise polynomial rules; no substitution of x=0 for singular functions."""
    a = [number(v) for v in calculus_coefficients(coefficients)]
    if operation == 'differentiate':
        result = [i * a[i] for i in range(1, len(a))] or [Fraction(0)]
    elif operation == 'integrate':
        result = [Fraction(0)] + [c / (i + 1) for i, c in enumerate(a)]
    elif operation == 'limit_zero':
        result = [a[0]]  # Polynomials are continuous at zero.
    elif operation == 'multiply_x':
        result = [Fraction(0)] + a
    else:
        raise ValueError('Unsupported calculus operation')
    encoded = calculus_coefficients(result)
    if len(encoded) - 1 > CALCULUS_MAX_DEGREE:
        return None, 'calculus_degree_limit'
    if any(max(v.numerator.bit_length(), v.denominator.bit_length()) > MAX_BITS
           for v in result):
        return None, 'calculus_coefficient_limit'
    return encoded, None


def upgrade_calculus(m):
    ca = m.setdefault('calculus_archive', {
        'schema': 1, 'expressions': [], 'results': {}, 'known_keys': [],
        'import_cursor': 0, 'queue': [], 'head': 0, 'deferred': [],
        'limits': [CALCULUS_MAX_DEPTH, CALCULUS_MAX_DEGREE, MAX_BITS]})
    ca.setdefault('role_origin_boundary', len(ca['expressions']))
    m['rule_registry'].setdefault('zero_slot_calculus_v471', {
        'status': 'active_polynomial_exploration_with_zero_origin_variable',
        'variable': 'requires an executed zero-slot variable-role construction',
        'history': 'previous calculus records preserved without retroactive origin claims',
        'input': 'coefficients re-expressed in the selected archived variable role',
        'scope': 'rational polynomial derivatives, primitives, multiplication by x, limits at zero'})
    limits = [CALCULUS_MAX_DEPTH, CALCULUS_MAX_DEGREE, MAX_BITS]
    if ca['limits'] != limits:
        ca['queue'].extend(ca['deferred'])
        ca['deferred'] = []
        ca['limits'] = limits
    state = zero_core_state(m)
    for field in ('record_passages', 'historical_record_passages'):
        state[field].setdefault('calculus', 0)
    for rec in ca['expressions']:
        zero_core(m, 'calculus', record=rec, historical=True)
    m['rule_registry'].setdefault('polynomial_calculus_v47', {
        'status': 'explicit_formal_extension_not_foundation',
        'variable': 'x is a formal real variable, not an emerged number',
        'coefficients': 'imported archived rationals with typed source links',
        'operations': list(CALCULUS_OPERATIONS),
        'antiderivative': 'canonical representative with C=0; family P(x)+C',
        'limit': 'two-sided at zero, for polynomials only',
        'coverage': 'bounded exploration; no completeness claim'})
    if 'archive_integration' in m:
        m['archive_integration']['indexed_record_cursors'].setdefault('calculus', 0)
        sync_archive_records(m, 'calculus')


def calculus_record(m, coefficients, operation, parents=(), sources=(), depth=0):
    ca = m['calculus_archive']
    coefficients = calculus_coefficients(coefficients)
    variable_refs = [ref for ref in sources if ref['archive'] == 'roles']
    if operation != 'constant_import':
        if len(variable_refs) != 1 or len(parents) != 1:
            raise ValueError('New calculus constructions require a parent and one zero-origin variable')
        variable = role_variable(m, variable_refs[0]['id'])
    else:
        if len(coefficients) != 1:
            raise ValueError('A constant import cannot introduce a formal variable')
        variable = 'x'  # Not present in a constant polynomial.
    identity = json.dumps([operation, list(parents), list(sources), coefficients],
                          sort_keys=True, separators=(',', ':'))
    if identity in ca['known_keys']:
        return None
    rec = {'id': len(ca['expressions']), 'expr': str(calculus_value(coefficients, variable)),
           'value': str(calculus_value(coefficients, variable)), 'coefficients': coefficients,
           'operation': operation, 'parents': list(parents), 'sources': list(sources),
           'depth': depth,
           'pathway': 'polynomial_calculus_v47' if operation == 'constant_import' else 'zero_slot_calculus_v471',
           'formal_rule': 'polynomial_calculus_v47' if operation == 'constant_import' else 'zero_slot_calculus_v471'}
    if variable_refs:
        rec['variable_source'] = dict(variable_refs[0])
        rec['variable'] = variable
        rec['input_interpretation'] = 'polynomial coefficients expressed in this archived variable role'
    if operation == 'integrate':
        rec['integration_constant'] = 'C=0 representative; full family is result+C'
    if operation == 'limit_zero':
        rec['limit'] = {'point': '0', 'direction': 'two-sided',
                        'justification': 'polynomial continuity'}
    if parents:
        original = ca['expressions'][parents[0]]['coefficients']
        rec['proof'] = {'rule': operation, 'input_coefficients': original,
                        'output_coefficients': coefficients,
                        'formula': {'differentiate': 'a[k] -> k*a[k] at degree k-1',
                                    'integrate': 'a[k] -> a[k]/(k+1) at degree k+1',
                                    'limit_zero': 'sum a[k]*x^k -> a[0] as x -> 0',
                                    'multiply_x': 'a[k] -> a[k] at degree k+1'}[operation]}
    zero_core(m, 'calculus', record=rec)
    ca['known_keys'].append(identity)
    ca['expressions'].append(rec)
    ca['results'].setdefault(rec['value'], []).append(rec['id'])
    for op in CALCULUS_OPERATIONS:
        ca['queue'].append({'source': rec['id'], 'operation': op})
    if 'archive_integration' in m:
        sync_archive_records(m, 'calculus')
    # A constant calculus result is available to existing numerical workers.
    if len(coefficients) == 1 and coefficients[0] not in m['results']:
        q = number(coefficients[0])
        leaf = int(q) if q.denominator == 1 else encode(q)
        idx = add_expression(m, {
            'expr': encode(q), 'value': encode(q), 'tree': {'leaf': leaf, 'calculus_source': rec['id']},
            'depth': 0, 'parents': [], 'leaves': [leaf], 'domain': 'rational',
            'pathway': 'calculus_to_rational_v47',
            'sources': [{'archive': 'calculus', 'id': rec['id']}],
            'ancestry': [{'rule': 'exact_constant_polynomial_embedding'}]})
        if idx is not None:
            schedule_frontier(m, idx)
    journal(m, 'calculus_expression', calculus_id=rec['id'], operation=operation)
    return rec['id']


def work_calculus(m):
    """Persist each operation/variable-path combination without value merging."""
    upgrade_roles(m)
    upgrade_calculus(m)
    ca = m['calculus_archive']
    variable_paths = m['roles_archive']['variable_refs']
    before = len(ca['expressions'])
    stop = min(len(m['expressions']), ca['import_cursor'] + CALCULUS_IMPORT_PER_RUN)
    while ca['import_cursor'] < stop:
        idx = ca['import_cursor']
        calculus_record(m, [m['expressions'][idx]['value']], 'constant_import',
                        sources=[{'archive': 'rational', 'id': idx}])
        ca['import_cursor'] += 1
    processed = 0
    while processed < CALCULUS_WORK_PER_RUN and ca['head'] < len(ca['queue']):
        task = ca['queue'][ca['head']]
        source = ca['expressions'][task['source']]
        cursor = task.get('variable_cursor', 0)
        if source['depth'] >= CALCULUS_MAX_DEPTH:
            ca['deferred'].append(dict(task))
        elif cursor >= len(variable_paths):
            # Retain the task: future role constructions give new paths.
            ca['queue'].append(dict(task))
        else:
            variable_id = variable_paths[cursor]
            result, reason = zero_core(m, 'calculus', operation=task['operation'],
                                      operands=(source['coefficients'], variable_id))
            record_kernel_operation(m, 'calculus', task['operation'],
                                    'limited' if reason else 'succeeded',
                                    'zero_slot_calculus_v471', reason)
            if reason:
                ca['deferred'].append(dict(task))
            else:
                calculus_record(m, result, task['operation'], parents=[source['id']],
                                sources=[{'archive': 'roles', 'id': variable_id}],
                                depth=source['depth'] + 1)
                ca['queue'].append({**task, 'variable_cursor': cursor + 1})
        ca['head'] += 1
        processed += 1
    if ca['head'] > 2000:
        ca['queue'] = ca['queue'][ca['head']:]
        ca['head'] = 0
    legacy = sum(rec['operation'] != 'constant_import' and 'variable_source' not in rec
                 for rec in ca['expressions'][:ca['role_origin_boundary']])
    return {'new': len(ca['expressions']) - before, 'processed': processed,
            'pending': len(ca['queue']) - ca['head'], 'deferred': len(ca['deferred']),
            'legacy_operations_without_variable_origin': legacy}


def query_calculus(m, text):
    words = text.lower().split()
    if not words or words[0] not in ('calculus', 'calculus-index'):
        return False
    ca = m.get('calculus_archive', {'expressions': [], 'results': {}})
    if words[0] == 'calculus' and len(words) == 2 and words[1].isdigit():
        idx = int(words[1])
        if idx < len(ca['expressions']):
            print(json.dumps(ca['expressions'][idx], indent=2))
        else:
            print('No calculus record with that ID.')
    else:
        print('Polynomial calculus: formal real x; exact rational coefficients.')
        print('Antiderivatives show C=0 representatives; full families include +C.')
        print('Limits are two-sided at zero for polynomials only.')
        for rec in ca['expressions'][-30:]:
            print('  calculus:%d %s [%s; parents=%s; sources=%s]' %
                  (rec['id'], rec['value'], rec['operation'], rec['parents'], rec['sources']))
        print('Use calculus 7 (replace 7 with a record number) to inspect construction and proof.')
    return True



def run(*, interactive=True):
    try:
        sp = sympy_module()
    except RuntimeError as exc:
        print(exc)
        return
    m = load_memory()
    # Preserve the exact pre-upgrade bytes once, before any exploration.
    if os.path.exists(memory_path()):
        import shutil
        backup = memory_path() + '.pre-v471.bak'
        try:
            with open(backup, 'xb') as target, open(memory_path(), 'rb') as source:
                shutil.copyfileobj(source, target)
        except FileExistsError:
            pass
    f = m['foundation']
    assert f['states'] == list(range(len(f['states'])))
    assert [z['id'] for z in f['zero_records']] == ['Z%d' % i for i in range(len(f['states']))]
    assert digit_breakdown('00404') == '00111101111'
    assert number('1/2') + number('1/3') == Fraction(5, 6)
    upgrade_zero_core(m)
    m['_keys'] = set(m['known_expression_keys'])
    upgrade_runtime(m)
    upgrade_v44(m)
    upgrade_tracking_namespaces(m)
    upgrade_v45(m)
    upgrade_complex_feedback(m)
    upgrade_symbolic(m)
    upgrade_symbolic_zero_nexus(m)
    upgrade_zero_archive_access(m)
    upgrade_archive_integration(m)
    upgrade_calculus(m)
    upgrade_roles(m)
    m['_blocked_keys'] = {(b['left'], b['right'], b['operation'], b['pathway'])
                          for b in m['blocked']}
    stats = {'new': 0, 'observer_added': 0,
             'symbolic_new': 0, 'paused_tasks': 0,
             'processed': {'consume': 0, 'consume_op': 0, 'pair': 0, 'revisit': 0, 'nexus': 0, 'zero_scan': 0, 'zero_source': 0, 'emerge': 0, 'frontier': 0, 'position': 0, 'complex': 0, 'complex_feedback': 0, 'symbolic_root': 0, 'symbolic_pair': 0, 'symbolic_nexus': 0, 'symbolic_position': 0, 'z0_primitive': 0, 'z0_macro': 0}}
    print('ZERO THEOREM V4.9.6 - CONNECTED ZERO WORKFLOW')
    print('SymPy:', sp.__version__)
    print('Memory:', memory_path())
    print('Foundation:', f['states'])
    print('Zero records:', [z['id'] for z in f['zero_records']])
    print('00404 ->', m['reference']['breakdown'])
    print('Exact arithmetic and foundation checks: PASS')
    with _zt16_span(memory_path(), 'foundation_emergence'):
        emergence = []
        for _ in range(EMERGENCE_EVENTS_PER_RUN):
            emergence.append(register_next_state(m))
    print('New emergence events:', [(e['counted_states'], e['result']) for e in emergence])
    z0_bridge_bootstrap(m)
    # The constructor needs one S step. Service it before queue work can use
    # the run allowance, then retain it through the usual save/recovery path.
    try:
        m['zero_constructor_status']=zero_constructor_bootstrap(m)
        m.pop('zero_constructor_pending',None)
    except PrimitivePending as exc:
        m['zero_constructor_pending']={'status':'pending','reason':'S work budget','job':exc.job}
    upgrade_v44(m)
    import_symbolic_sources(m)
    schedule_symbolic_zero_positions(m)
    removed = rebalance_queue(m)
    journal(m, 'queue_rebalance', removed_duplicates=removed, pending=len(m['queue']))
    print('Duplicate pending tasks removed:', removed)
    _wf_before=len(m['expressions'])
    zero_core(m,'connected',operation='service',record_budget=8,execution_budget=1)
    stats['new']+=len(m['expressions'])-_wf_before
    zero_connected_reserve(m)
    # Work queue is persistent. Each task is removed only after completion.
    # Rotate through tasks to prevent any one pathway monopolising the run.
    # Count a bounded number of states first, so new values enter this run.
    with _zt16_span(memory_path(), 'queue_exploration'):
        processed = 0
        nexus_processed = 0
        complex_processed = 0
        symbolic_processed = 0
        primitive_processed = 0
        while processed < WORK_PER_RUN and m['queue_head'] < len(m['queue']):
            if stats['new'] >= MAX_NEW_EXPRESSIONS_PER_RUN: break
            task = m['queue'][m['queue_head']]
            kind = task['kind']
            if kind in ('z0_primitive', 'z0_macro') and primitive_processed >= Z0_BRIDGE_PER_RUN:
                m['queue'].append(dict(task))
                m['queue_head'] += 1
                processed += 1
                continue
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
            selected_key = task_key(task)
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
            elif kind == 'z0_primitive':
                completed = z0_bridge_work(m, task, stats)
                primitive_processed += 1
            elif kind == 'z0_macro':
                completed = z0_macro_work(m, task, stats)
                primitive_processed += 1
            elif kind == 'frontier': completed = work_frontier(m, task, stats)
            elif kind == 'pair': completed = work_pair(m, task, stats)
            elif kind == 'consume_op': completed = work_consume_op(m, task, stats)
            elif kind == 'consume': completed = work_consume(m, task, stats)
            elif kind == 'revisit': completed = work_revisit(m, task, stats)
            else: raise ValueError('Unknown queued work kind: ' + str(kind))
            if not completed:
                # The task remains at queue_head with its next operation/slot.
                # Save completed work and the resume cursor in the normal path.
                m['_pending_keys'].discard(selected_key)
                m['_pending_keys'].add(task_key(task))
                stats['paused_tasks'] += 1
                tangent_paused(m, task, selected_key)
                break
            tangent_completed(m, task, selected_key=selected_key)
            m['_pending_keys'].discard(selected_key)
            m['queue_head'] += 1
            stats['processed'][kind] += 1
            processed += 1
        # Compact consumed queue prefix without losing unfinished work.
        if m['queue_head'] > 2000:
            m['queue'] = m['queue'][m['queue_head']:]
            m['queue_head'] = 0
    role_stats = work_roles(m)
    calculus_stats = work_calculus(m)
    _wf_release_reserved(m)
    _wf_before=len(m['expressions'])
    zero_core(m,'connected',operation='service')
    stats['new']+=len(m['expressions'])-_wf_before
    m['_zero_connected_serviced_for_save']=True
    run_id = len(m['runs']) + 1
    journal(m, 'run_complete', run=run_id, expressions=len(m['expressions']), results=len(m['results']), pending=len(m['queue'])-m['queue_head'])
    m['runs'].append({'run': run_id, 'timestamp': time.time(),
                      'processed': stats['processed'], 'new': stats['new'],
                      'symbolic_new': stats['symbolic_new'],
                      'paused_tasks': stats['paused_tasks'],
                      'expressions_total': len(m['expressions'])})
    coverage = zero_core_report(m)
    if not coverage['complete']:
        raise ValueError('Zero-core archive passage coverage failed; memory not saved')
    z0_discovery = z0_discover_primitive_patterns(m)
    z0_macro_schedule(m)
    save_memory(m)
    print('Z0 primitive pattern discovery:', z0_discovery)
    print('Zero-core archive passage coverage:', coverage)
    print('Zero-slot role exploration:', role_stats)
    print('Calculus exploration:', calculus_stats)
    print('Run:', run_id, 'Tasks:', stats['processed'])
    print('New expressions:', stats['new'], 'Archive:', len(m['expressions']))
    print('Tasks paused at expression budget:', stats['paused_tasks'])
    print('Distinct results:', len(m['results']))
    print('Legacy rational recorded transitions:', len(m['network']['transitions']))
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
    print('Symbolic construction import cursors:', sa['construction_import_cursors'])
    print('Pending source construction imports:', {
        domain: max(0, len(archive_records(m, domain)) - cursor)
        for domain, cursor in sa['construction_import_cursors'].items()})
    print('Imports outside configured limits:', {domain: len(items) for domain, items in sa['import_deferred'].items()})
    print('Symbolic zero-nexus constructions:', len(m['symbolic_nexus_events']))
    print_v45_summary(m)
    print_operation_totals(m)
    print('Index commands: index, index -10 10, gaps -30 30, complex-index')
    print('Symbolic queries: symbolic-index, symbolic sqrt(2), symbolic 2**3, symbolic sqrt(-2)')
    print('All value queries include every archive; operations/totals shows whole-engine counters.')
    print('Role queries: roles-index, roles 7 (record number)')
    print('Calculus queries: calculus-index, calculus 7 (polynomials; integral families include +C)')
    print('Zero-core coverage command: zero-core')
    print('Saved. Re-run to continue exploring.')
    if not interactive:
        return m
    while True:
        try: text = input('\nQuery an archived value (ENTER to exit): ').strip()
        except (EOFError, KeyboardInterrupt): break
        if not text: break
        if text.lower() == 'zero-core':
            print(zero_core_report(m))
            continue
        if text.lower() == 'integrity':
            print_archive_link_audit(m)
            continue
        if text.lower() in ('operations', 'totals'):
            print_operation_totals(m)
            continue
        if query_roles(m, text): continue
        if query_calculus(m, text): continue
        if query_symbolic(m, text): continue
        if not query_v45(m, text): query(m, text)



# V4.7.2: zero recovery, stable slots and manifest.
"""Zero recovery slots for V4.7.1. Embedded by apply_zero_recovery_patch.py.

Checksums detect accidental inconsistency, not malicious replacement of both
records and manifests. Only verified rational binary constructions are rebuilt.
"""
import json
import os
import copy as _zr_copy
import hashlib as _zr_hashlib

_ZR_DOMAINS = ('rational', 'complex', 'symbolic', 'calculus', 'roles')
_ZR_ARITHMETIC = ('reuse_v1', 'result_feedback_v42', 'consume_v1', 'revisit_v1')
_ZR_MAX_SLOTS = 1000000
_ZR_MAX_GAPS = 4096


class ZeroRecoveryPending(ValueError):
    """No exploration or normal memory save is permitted yet."""


def _zr_digest(value):
    raw = json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    return _zr_hashlib.sha256(raw.encode('utf-8')).hexdigest()


def _zr_payload(rec):
    return {k: v for k, v in rec.items()
            if k not in ('zero_core_passage', 'unified_value_key')}


def _zr_records(m, domain):
    return m.get('expressions', []) if domain == 'rational' else m.get(
        domain + '_archive', {}).get('expressions', [])


def _zr_state(m):
    return m.setdefault('zero_recovery', {
        'schema': 1, 'zero_nexus': 'Z0', 'next_ids': {}, 'manifest': {},
        'events': [], 'status': 'ready', 'manifest_initialized': False,
        'scope': 'archive_damage; verified_rational_binary_reconstruction'})


def _zr_manifest_entry(domain, rec):
    entry = {'digest': _zr_digest(_zr_payload(rec)),
             'expr': rec.get('expr'), 'pathway': rec.get('pathway')}
    if domain == 'rational':
        entry['recipe'] = {key: _zr_copy.deepcopy(rec[key])
                           for key in ('tree', 'pathway', 'parents') if key in rec}
    return entry


def _zr_track_new(m):
    state = _zr_state(m)
    for domain in _ZR_DOMAINS:
        records = _zr_records(m, domain)
        start = state['next_ids'].get(domain, 0)
        if len(records) < start:
            raise ZeroRecoveryPending('Archive shortened during execution: ' + domain)
        manifest = state['manifest'].setdefault(domain, {})
        for idx in range(start, len(records)):
            rec = records[idx]
            if rec.get('id') != idx or rec.get('status') == 'zero_recovery_pending':
                raise ZeroRecoveryPending('Invalid new archive position: %s:%s' % (domain, idx))
            manifest[str(idx)] = _zr_manifest_entry(domain, rec)
        state['next_ids'][domain] = len(records)
    state['manifest_initialized'] = True


def _zr_event(m, domain, idx, status, reason):
    state = _zr_state(m)
    # A repeated unchanged unresolved slot is one incident, not unlimited work.
    event = {'archive': domain, 'id': idx, 'zero_nexus': 'Z0',
             'status': status, 'reason': reason}
    if event not in state['events']:
        state['events'].append(event)


def _zr_slot(domain, idx, reason):
    return {'id': idx, 'status': 'zero_recovery_pending',
            'zero_nexus': 'Z0', 'archive': domain,
            'value': None, 'reason': reason}


def _zr_legacy_recipe(m, idx):
    """Old keys are plans, not a backup or proof of original provenance."""
    keys = m.get('known_expression_keys', [])
    if idx >= len(keys):
        return None
    try:
        pathway, tree = json.loads(keys[idx])
    except (ValueError, TypeError):
        return None
    if pathway not in _ZR_ARITHMETIC:
        return None
    # Require an independent surviving creation event naming this exact ID.
    events = [event for event in m.get('genesis', {}).get('events', [])
              if event.get('type') == 'expression_created'
              and event.get('expression_id') == idx]
    unique = {_zr_digest({k: e.get(k) for k in ('value', 'pathway', 'parents')})
              for e in events}
    if len(unique) != 1:
        return None
    evidence = events[0]
    if evidence.get('pathway') != pathway:
        return None
    return {'tree': tree, 'pathway': pathway, 'parents': evidence.get('parents'),
            'expected_value': evidence.get('value')}


def _zr_reconstruct(m, idx, recipe, api):
    """Re-execute a supported rule; never copy another equal-valued path."""
    if not isinstance(recipe, dict) or recipe.get('pathway') not in _ZR_ARITHMETIC:
        return None
    parents = recipe.get('parents')
    if not isinstance(parents, list) or len(parents) != 2:
        return None
    records = m['expressions']
    if any(type(p) is not int or not 0 <= p < idx or p >= len(records) for p in parents):
        return None
    left, right = (records[p] for p in parents)
    if any(rec.get('status') == 'zero_recovery_pending' for rec in (left, right)):
        return None
    tree = recipe.get('tree', {})
    op = tree.get('op')
    if op not in ('+', '-', '*', '/'):
        return None
    expected_tree = {'op': op, 'left': left['tree'], 'right': right['tree']}
    if tree != expected_tree:
        return None
    # This dispatch calls the original mathematical zero gate, without
    # pretending the recovery attempt was an ordinary exploration task.
    result = api['zero_core'](m, 'rational', operation=op,
                             operands=(api['number'](left['value']), api['number'](right['value'])))
    if result is None:
        return None
    value = api['encode'](result)
    if 'expected_value' in recipe and recipe['expected_value'] != value:
        return None
    depth = max(left['depth'], right['depth']) + 1
    if depth > api['MAX_DEPTH'] or max(result.numerator.bit_length(),
                                      result.denominator.bit_length()) > api['MAX_BITS']:
        return None
    pathway = recipe['pathway']
    return {'expr': '(' + left['expr'] + ' ' + op + ' ' + right['expr'] + ')',
            'value': value, 'tree': expected_tree, 'depth': depth,
            'parents': list(parents), 'leaves': left['leaves'] + right['leaves'],
            'pathway': pathway, 'domain': 'rational',
            'ancestry': left['ancestry'] + right['ancestry'] + [{
                'left_id': parents[0], 'right_id': parents[1],
                'operation': op, 'result': value, 'rule': pathway}], 'id': idx}


def _zr_verify_rational(rec, api):
    """Re-evaluate embedded trees, including parent-independent leaf values."""
    def value(tree):
        if not isinstance(tree, dict):
            raise ValueError('Invalid rational tree')
        if 'leaf' in tree:
            return api['number'](tree['leaf'])
        a, b = value(tree['left']), value(tree['right'])
        result = api['zero_core'](None, 'rational', operation=tree['op'], operands=(a, b))
        if result is None:
            raise ValueError('Blocked rational construction')
        return result
    return api['encode'](value(rec['tree'])) == rec['value']


def _zr_preflight(m, api):
    """Normalize positions in a copy before any engine workers execute."""
    candidate = _zr_copy.deepcopy(m)
    state = _zr_state(candidate)
    had_manifest = state.get('manifest_initialized', False)
    if state.get('schema') != 1 or state.get('zero_nexus') != 'Z0':
        raise ZeroRecoveryPending('Unrecognized zero recovery metadata')
    if state.get('status') == 'blocked':
        raise ZeroRecoveryPending('Inspect blocked recovery checkpoint before continuing')
    for domain in _ZR_DOMAINS:
        records = _zr_records(candidate, domain)
        seen = {}
        for rec in records:
            idx = rec.get('id')
            if type(idx) is not int or not 0 <= idx < _ZR_MAX_SLOTS or idx in seen:
                raise ZeroRecoveryPending('Conflicting or invalid IDs in ' + domain)
            seen[idx] = rec
        highest = max(seen, default=-1) + 1
        if had_manifest:
            count = state['next_ids'].get(domain)
            manifest = state['manifest'].get(domain, {})
            if (type(count) is not int or not 0 <= count <= _ZR_MAX_SLOTS
                    or highest > count or len(manifest) != count
                    or any(str(i) not in manifest for i in range(count))):
                raise ZeroRecoveryPending('Inconsistent manifest/next counter: ' + domain)
        else:
            # Old passage totals and rational key order supply a bounded
            # migration baseline. They are not reconstructed history.
            old_count = candidate.get('zero_core', {}).get('record_passages', {}).get(domain, highest)
            if type(old_count) is not int or not 0 <= old_count <= _ZR_MAX_SLOTS:
                raise ZeroRecoveryPending('Invalid legacy passage count: ' + domain)
            count = max(highest, old_count)
            if domain == 'rational':
                count = max(count, len(candidate.get('known_expression_keys', [])))
            manifest = {}
        if count > _ZR_MAX_SLOTS or count - len(seen) > _ZR_MAX_GAPS:
            raise ZeroRecoveryPending('Recovery slot budget exceeded: ' + domain)
        normalized = []
        for idx in range(count):
            rec = seen.get(idx)
            if rec is not None and rec.get('status') != 'zero_recovery_pending':
                if had_manifest and _zr_digest(_zr_payload(rec)) != manifest[str(idx)]['digest']:
                    _zr_event(candidate, domain, idx, 'blocked', 'manifest_content_mismatch')
                    state['status'] = 'blocked'
                    return candidate, False
                normalized.append(rec)
            else:
                normalized.append(_zr_slot(domain, idx, 'missing_archive_record'))
                _zr_event(candidate, domain, idx, 'pending', 'missing_archive_record')
        if domain == 'rational':
            candidate['expressions'] = normalized
        elif domain + '_archive' in candidate:
            candidate[domain + '_archive']['expressions'] = normalized
        state['next_ids'][domain] = count
        state['manifest'].setdefault(domain, manifest)
    # Ascending ID order allows a later missing construction to depend on
    # a verified earlier recovery in this same bounded pass.
    for domain in _ZR_DOMAINS:
        for rec in _zr_records(candidate, domain):
            idx = rec['id']
            if rec.get('status') != 'zero_recovery_pending':
                continue
            entry = state['manifest'][domain].get(str(idx))
            recipe = entry.get('recipe') if entry else (
                _zr_legacy_recipe(candidate, idx) if domain == 'rational' else None)
            recovered = _zr_reconstruct(candidate, idx, recipe, api) if domain == 'rational' else None
            if recovered is None:
                continue
            if entry and _zr_digest(_zr_payload(recovered)) != entry['digest']:
                continue
            # Restore passage identity without counting a new accepted record.
            recovered['zero_core_passage'] = {
                'rule': api['ZERO_CORE_RULE'], 'archive': domain, 'id': idx,
                'zero_nexus': 'Z0', 'historical_backfill': False,
                'effect': 'identity_preserves_construction'}
            sp = api['sympy_module']()
            q = api['number'](recovered['value'])
            recovered['unified_value_key'] = api['exact_lookup_key'](sp.Rational(q.numerator, q.denominator))
            candidate['expressions'][idx] = recovered
            _zr_event(candidate, domain, idx, 'recovered',
                      'manifest_verified_reexecution' if entry else 'legacy_evidence_reexecution')
    pending = any(rec.get('status') == 'zero_recovery_pending'
                  for domain in _ZR_DOMAINS for rec in _zr_records(candidate, domain))
    if pending:
        state['status'] = 'pending'
        return candidate, False
    # Bootstrap only after structural and rational arithmetic checks succeed.
    # Never change existing counters/indices to make a damaged archive pass.
    try:
        for rec in candidate.get('expressions', []):
            if not _zr_verify_rational(rec, api):
                raise ValueError('Rational value does not match its tree')
        if candidate.get('runs'):
            coverage_check = api.get('zero_core_report')
            if coverage_check is not None:
                coverage = coverage_check(candidate)
                if not coverage['complete']:
                    state['coverage'] = coverage
                    raise ValueError('Zero-core passage coverage failed before exploration')
            audit = api['archive_link_audit'](candidate)
            if audit['issues']:
                state['audit'] = audit
                raise ValueError('Archive link audit failed')
    except (ValueError, KeyError, IndexError, TypeError, RecursionError) as exc:
        state['status'] = 'blocked'
        state['reason'] = str(exc)
        return candidate, False
    if not had_manifest:
        for domain in _ZR_DOMAINS:
            state['manifest'][domain] = {str(rec['id']): _zr_manifest_entry(domain, rec)
                                        for rec in _zr_records(candidate, domain)}
        state['migration'] = 'current_evidence_baseline_not_authenticated_history'
    state['manifest_initialized'] = True
    state['status'] = 'ready'
    return candidate, True


def _zr_write_checkpoint(m, api):
    path = api['memory_path']() + '.zero-recovery.json'
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as target:
        json.dump(m, target, ensure_ascii=False, separators=(',', ':'))
        target.flush()
        os.fsync(target.fileno())
    os.replace(tmp, path)
    return path


def install_zero_recovery(api):
    """Attach to V4.7.1 without changing its mathematical workers."""
    if api.get('_ZERO_RECOVERY_INSTALLED'):
        return
    original_core = api['zero_core']
    original_load = api['load_memory']
    original_save = api['save_memory']
    original_run = api['run']

    def core(m, domain, **kwargs):
        if domain == 'errors' and kwargs.get('operation') == 'recover_archive':
            return _zr_preflight(m, api)
        return original_core(m, domain, **kwargs)

    def load():
        original = original_load()
        try:
            candidate, ready = api['zero_core'](original, 'errors', operation='recover_archive')
        except (ZeroRecoveryPending, ValueError, KeyError, IndexError, TypeError, RecursionError) as exc:
            candidate = _zr_copy.deepcopy(original)
            state = _zr_state(candidate)
            state.update(status='blocked', reason=str(exc))
            ready = False
        if not ready:
            path = _zr_write_checkpoint(candidate, api)
            raise ZeroRecoveryPending('Zero recovery pending; exploration deferred. Checkpoint: ' + path)
        recovered = [e for e in _zr_state(candidate)['events'] if e['status'] == 'recovered']
        if recovered:
            print('Zero recovery verified:', [(e['archive'], e['id'], e['reason']) for e in recovered])
        return candidate

    def save(m):
        if _zr_state(m)['status'] != 'ready':
            raise ZeroRecoveryPending('Unresolved memory cannot use the normal save path')
        _zr_track_new(m)
        for domain in _ZR_DOMAINS:
            entries = _zr_state(m)['manifest'][domain]
            for rec in _zr_records(m, domain):
                if _zr_digest(_zr_payload(rec)) != entries[str(rec['id'])]['digest']:
                    raise ZeroRecoveryPending('Accepted archive construction changed: %s:%s' % (domain, rec['id']))
        original_save(m)

    def run():
        try:
            original_run()
        except ZeroRecoveryPending as exc:
            print(str(exc))

    api.update(zero_core=core, load_memory=load, save_memory=save, run=run)
    # Record constructors still allocate len(records); preflight guarantees
    # that this equals the saved next ID, and unresolved slots stop workers.
    for name in ('add_expression', 'complex_record', 'symbolic_record', 'role_record', 'calculus_record'):
        original = api[name]
        def tracked(m, *args, _original=original, **kwargs):
            result = _original(m, *args, **kwargs)
            _zr_track_new(m)
            return result
        api[name] = tracked
    api['_ZERO_RECOVERY_INSTALLED'] = True

_zg_engine_cycle = run
install_zero_recovery(globals())

# V4.7.3: text roles and bounded punctuation search through zero_core.
# Run normally in a TEST folder with the expected memory filename.
# Damaged input is NEVER overwritten: candidate files and a report are written
# beside it, then exploration stops. --repair-json [PATH] also inspects a file.
# Copy an inspected candidate into a separate test folder to continue testing.
# Grammar/Unicode are supplied representation rules, not discovered mathematics.
# Candidates are structurally plausible, NOT proof of original text recovery.

_ZT_MAX_BYTES = 24 * 1024 * 1024
_ZT_MAX_EDITS = 4
_ZT_MAX_NODES = 128
_ZT_MAX_CANDIDATES = 8
_ZT_WORK_CHAR_BUDGET = 32 * 1024 * 1024


def _zt_pairs(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError('Duplicate JSON key: ' + key)
        obj[key] = value
    return obj


def _zt_constant(value):
    raise ValueError('Non-JSON numeric constant: ' + value)


def _zt_parse(text):
    return json.loads(text, object_pairs_hook=_zt_pairs, parse_constant=_zt_constant)


def _zt_observe(text):
    """Observe symbols without treating punctuation inside strings as grammar."""
    roles, alphabet, transitions = {}, {}, {}
    inside, escaped, previous = False, False, None
    for char in text:
        if inside:
            if escaped:
                role = 'escape_payload'
                escaped = False
            elif char == '\\':
                role = 'escape_start'
                escaped = True
            elif char == '"':
                role = 'string_close'
                inside = False
            else:
                role = 'string_character'
        elif char == '"':
            role, inside = 'string_open', True
        elif char in '{}[]':
            role = {'{': 'object_open', '}': 'object_close',
                    '[': 'array_open', ']': 'array_close'}[char]
        elif char == ':':
            role = 'key_value_separator'
        elif char == ',':
            role = 'entry_separator'
        elif char.isspace():
            role = 'whitespace'
        else:
            role = 'literal_character'
        roles[role] = roles.get(role, 0) + 1
        # Bounded observed alphabet: Unicode code points are supplied encoding.
        code = str(ord(char))
        if code in alphabet or len(alphabet) < 512:
            alphabet[code] = alphabet.get(code, 0) + 1
        if previous is not None:
            pair = previous + ' -> ' + role
            transitions[pair] = transitions.get(pair, 0) + 1
        previous = role
    return {'zero_nexus': 'Z0', 'rule': 'text_roles_v1',
            'characters': len(text), 'role_counts': roles,
            'observed_codepoints': alphabet, 'role_transitions': transitions,
            'unterminated_string': inside,
            'supplied_rules': 'JSON grammar; Unicode encoding',
            'learned_observations': 'symbol counts and adjacent role frequencies',
            'boundary': 'observations do not establish missing content'}


def _zt_outside(text, position):
    inside, escaped = False, False
    for char in text[:position]:
        if inside:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == '"':
                inside = False
        elif char == '"':
            inside = True
    return not inside


def _zt_edits(text, exc):
    """Local punctuation hypotheses only; never invent letters or values."""
    pos = exc.pos
    if not _zt_outside(text, pos):
        return
    if exc.msg == "Expecting ':' delimiter":
        insertions = ':'
    elif exc.msg == "Expecting ',' delimiter":
        insertions = ',}]'
    elif exc.msg in ('Expecting property name enclosed in double quotes', 'Expecting value'):
        insertions = '}]'
    else:
        insertions = ''
    for char in insertions:
        yield (text[:pos] + char + text[pos:],
               {'action': 'insert', 'offset_in_previous_candidate': pos,
                'text': char, 'constraint': exc.msg})
    previous = pos - 1
    while previous >= 0 and text[previous].isspace():
        previous -= 1
    for index in dict.fromkeys((pos, previous)):
        if (0 <= index < len(text) and text[index] in ',:{}[]'
                and _zt_outside(text, index)):
            yield (text[:index] + text[index + 1:],
                   {'action': 'delete', 'offset_in_previous_candidate': index,
                    'text': text[index], 'constraint': exc.msg})


def _zt_search(text):
    """Breadth-first local grammar search; budgets are explicit and reported."""
    initial = _zt_observe(text)
    node_limit = min(_ZT_MAX_NODES, max(1, _ZT_WORK_CHAR_BUDGET // (len(text) + _ZT_MAX_EDITS + 1)))
    report = {'schema': 1, 'zero_nexus': 'Z0', 'operation': 'reconstruct_json',
              'source_sha256': _zr_hashlib.sha256(text.encode('utf-8')).hexdigest(),
              'observation': initial, 'status': 'unresolved', 'nodes_checked': 0,
              'limits': {'nodes': node_limit, 'edits': _ZT_MAX_EDITS,
                         'candidates': _ZT_MAX_CANDIDATES},
              'search_scope': 'local punctuation edits at strict decoder failures',
              'original_recovery_verified': False, 'candidates': []}
    frontier = [(text, [])]
    seen = {report['source_sha256']}
    solutions = []
    for depth in range(_ZT_MAX_EDITS + 1):
        failures = []
        for current, edits in frontier:
            if report['nodes_checked'] >= node_limit:
                report['budget_exhausted'] = True
                break
            report['nodes_checked'] += 1
            try:
                parsed = _zt_parse(current)
            except json.JSONDecodeError as exc:
                if depth == 0:
                    report['first_error'] = {'message': exc.msg, 'offset': exc.pos}
                failures.append((current, edits, exc))
            except (ValueError, RecursionError) as exc:
                if depth == 0:
                    report['first_error'] = {'message': str(exc)}
            else:
                solutions.append((parsed, edits, current))
                if len(solutions) >= _ZT_MAX_CANDIDATES:
                    report['candidate_limit_reached'] = True
                    break
        if solutions or report.get('budget_exhausted') or report.get('candidate_limit_reached'):
            break
        if depth == _ZT_MAX_EDITS:
            report['edit_limit_reached'] = bool(failures)
            break
        frontier = []
        for current, edits, exc in failures:
            for changed, edit in _zt_edits(current, exc):
                digest = _zr_hashlib.sha256(changed.encode('utf-8')).hexdigest()
                if digest in seen:
                    continue
                seen.add(digest)
                frontier.append((changed, edits + [edit]))
                if len(frontier) >= node_limit:
                    report['frontier_truncated'] = True
                    break
            if len(frontier) >= node_limit:
                break
        if not frontier:
            break
    report['status'] = ('already_valid' if solutions and not solutions[0][1]
                        else 'syntax_candidates' if solutions else 'unresolved')
    report['alternatives_found'] = len(solutions)
    report['boundary'] = ('Search is bounded and local. Even one candidate is not '
                          'proof of a unique repair or of the original content.')
    return report, solutions


def _zt_write_new(path, value):
    """Never replace an existing source, candidate, or report."""
    suffix = 0
    while True:
        selected = path if not suffix else path + '.' + str(suffix)
        try:
            target = open(selected, 'x', encoding='utf-8')
        except FileExistsError:
            suffix += 1
            continue
        with target:
            json.dump(value, target, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
            target.flush()
            os.fsync(target.fileno())
        return selected


def _zt_load_file(path, inspect_only=False):
    with open(path, 'rb') as source:
        raw = source.read(_ZT_MAX_BYTES + 1)
    if len(raw) > _ZT_MAX_BYTES:
        raise ZeroRecoveryPending('Text inspection byte budget exceeded; source unchanged')
    try:
        text = raw.decode('utf-8')
    except UnicodeError as exc:
        raise ZeroRecoveryPending('Invalid UTF-8; text repair unresolved; source unchanged') from exc
    try:
        parsed = _zt_parse(text)
    except (ValueError, RecursionError):
        report, solutions = zero_core(None, 'text', operation='reconstruct_json', operands=(text,))
        report['source_bytes_sha256'] = _zr_hashlib.sha256(raw).hexdigest()
        for number, (candidate, edits, repaired_text) in enumerate(solutions, 1):
            entry = {'number': number, 'edits': edits,
                     'syntax_valid': True, 'original_recovery_verified': False,
                     'repaired_text_sha256': _zr_hashlib.sha256(repaired_text.encode('utf-8')).hexdigest()}
            try:
                if not isinstance(candidate, dict) or candidate.get('schema') != 1 or candidate.get('version') != VERSION:
                    raise ValueError('Not a compatible engine memory')
                checked, ready = zero_core(candidate, 'errors', operation='recover_archive')
                entry['archive_preflight'] = 'ready' if ready else 'pending_or_blocked'
                if not ready:
                    entry['archive_reason'] = _zr_state(checked).get('reason', _zr_state(checked)['status'])
            except (ZeroRecoveryPending, ValueError, KeyError, TypeError, IndexError, RecursionError, AttributeError) as exc:
                entry['archive_preflight'] = 'blocked'
                entry['archive_reason'] = str(exc)
            # Save the syntax candidate as-is; preflight outcomes are evidence,
            # not permission to merge or silently overwrite the damaged memory.
            entry['path'] = _zt_write_new(path + '.zero-text-candidate-%d.json' % number, candidate)
            report['candidates'].append(entry)
        report_path = _zt_write_new(path + '.zero-text-report.json', report)
        print('Zero text check:', report['status'], '| candidates:', len(solutions))
        for entry in report['candidates']:
            print('Candidate:', entry['path'], '| archive:', entry['archive_preflight'])
        raise ZeroRecoveryPending('Text reconstruction requires review; exploration deferred. '
                                  'Source unchanged. Report: ' + report_path)
    if not isinstance(parsed, dict):
        raise ZeroRecoveryPending('Memory root must be an object; source unchanged')
    observation = zero_core(None, 'text', operation='observe_structure', operands=(text,))
    parsed['zero_text_observation'] = observation
    if inspect_only:
        print('Zero text check: valid JSON; structural observation complete. Source unchanged.')
    return parsed


def install_zero_text(api):
    previous = api['zero_core']
    def core(m, domain, **kwargs):
        if domain == 'text':
            operation = kwargs.get('operation')
            (text,) = kwargs.get('operands', ())
            if not isinstance(text, str):
                raise TypeError('Text zero gate expects a string')
            if operation == 'observe_structure':
                return _zt_observe(text)
            if operation == 'reconstruct_json':
                return _zt_search(text)
            raise ValueError('Unsupported text zero operation')
        return previous(m, domain, **kwargs)
    api['zero_core'] = core


install_zero_text(globals())


# V4.7.4: resumable recovery nexus. Supplied grammar remains explicit.
# A text candidate is a hypothesis; archive validation is a separate gate.
_ZN_RULES = {
    'version': 'zero_recovery_paths_v1',
    'encoding': 'UTF-8 / Unicode (supplied)',
    'grammar': 'JSON strings, escapes, literals, ordered arrays, unique object keys (supplied)',
    'punctuation': 'local insert/delete at strict decoder failure',
    'field_completion': 'observed key prefix + observed value; hypothesis only',
    'routing': 'failure -> Z0 -> evidence -> proposals -> strict parse -> archive check',
    'repeat_policy': 'retain every edge; share expansion of identical text in identical context; retry dead ends',
}
_ZN_NODES_PER_RUN = 32
_ZN_PROPOSALS_PER_NODE = 64


def _zn_evidence(text):
    """Read surviving field/value paths in lexical order; never fill from a template."""
    fields, i = {}, 0
    decoder = json.JSONDecoder(object_pairs_hook=_zt_pairs, parse_constant=_zt_constant)
    while i < len(text):
        if text[i] != '"':
            i += 1
            continue
        start = i
        i += 1
        escaped = False
        while i < len(text):
            char = text[i]
            i += 1
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == '"':
                break
        try:
            key = _zt_parse(text[start:i])
        except (ValueError, RecursionError):
            continue
        cursor = i
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
        if cursor >= len(text) or text[cursor] != ':' or len(key) > 128:
            continue
        cursor += 1
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
        try:
            value, end = decoder.raw_decode(text, cursor)
        except (ValueError, RecursionError):
            continue
        if end - cursor > 1024:
            continue
        body = text[cursor:end]
        choices = fields.setdefault(key, {})
        if body not in choices and len(choices) >= 32:
            continue
        choices.setdefault(body, []).append({'key_offset': start, 'value_offset': cursor})
    return fields


def _zn_apply(text, edits):
    for edit in edits:
        pos = edit['offset_in_previous_candidate']
        before = edit.get('before', '')
        if text[pos:pos + len(before)] != before:
            raise ValueError('Recovery path no longer matches its source')
        text = text[:pos] + edit['after'] + text[pos + len(before):]
    return text


def _zn_proposals(text, exc, fields):
    for changed, edit in _zt_edits(text, exc):
        pos = edit['offset_in_previous_candidate']
        yield changed, {'offset_in_previous_candidate': pos,
                        'before': edit['text'] if edit['action'] == 'delete' else '',
                        'after': edit['text'] if edit['action'] == 'insert' else '',
                        'rule': 'punctuation', 'constraint': exc.msg,
                        'zero_nexus': 'Z0'}
    if exc.msg != "Expecting ':' delimiter":
        return
    # Locate a lexically valid quoted key immediately before the failure.
    end = exc.pos
    while end and text[end - 1].isspace():
        end -= 1
    if not end or text[end - 1] != '"':
        return
    start = text.rfind('"', 0, end - 1)
    if start < 0 or not _zt_outside(text, start):
        return
    try:
        fragment = _zt_parse(text[start:end])
    except ValueError:
        return
    if not isinstance(fragment, str) or not fragment:
        return
    for key, values in fields.items():
        if not key.startswith(fragment):
            continue
        for value_text, sources in values.items():
            replacement = json.dumps(key, ensure_ascii=False) + ':' + value_text
            yield (text[:start] + replacement + text[end:],
                   {'offset_in_previous_candidate': start, 'before': text[start:end],
                    'after': replacement, 'rule': 'field_completion',
                    'evidence_key': key, 'evidence_paths': sources,
                    'constraint': exc.msg, 'zero_nexus': 'Z0',
                    'claim': 'observed field/value hypothesis; original content unverified'})


def _zn_search(text, state=None):
    digest = _zr_hashlib.sha256(text.encode('utf-8')).hexdigest()
    rules = zero_core(None, 'recovery', operation='construction_rules')
    context = _zr_digest(rules)
    if state is None:
        state = {'schema': 1, 'zero_nexus': 'Z0', 'source_sha256': digest,
                 'rules': rules, 'context': context,
                 'nodes': {digest: {'edits': [], 'status': 'pending', 'attempts': 0}},
                 'frontier': [digest], 'edges': [], 'runs': [], 'retry_cursor': 0}
    if state.get('source_sha256') != digest or state.get('schema') != 1:
        raise ZeroRecoveryPending('Recovery checkpoint belongs to a different source')
    if state.get('context') != context:
        state.update(context=context, rules=rules,
                     frontier=list(state['nodes']))
        for node in state['nodes'].values():
            node.pop('expanded_context', None)
            node['proposal_cursor'] = 0
    fields = zero_core(None, 'recovery', operation='observe_paths', operands=(text,))
    if not state['frontier']:
        dead = [key for key, node in state['nodes'].items() if node['status'] == 'dead_end']
        if dead:
            offset = state['retry_cursor'] % len(dead)
            batch = (dead[offset:] + dead[:offset])[:4]
            state['frontier'].extend(batch)
            state['retry_cursor'] += len(batch)
    limit = min(_ZN_NODES_PER_RUN, max(1, _ZT_WORK_CHAR_BUDGET // (len(text) + 1)))
    report = {'schema': 2, 'zero_nexus': 'Z0', 'operation': 'reconstruct_json',
              'source_sha256': digest, 'observation': _zt_observe(text),
              'rules': state['rules'], 'status': 'unresolved', 'nodes_checked': 0,
              'candidates': [], 'original_recovery_verified': False,
              'search_scope': 'punctuation and surviving field/value paths',
              'limits': {'nodes_per_run': limit, 'proposals_per_node': _ZN_PROPOSALS_PER_NODE}}
    solutions = []
    run_number = len(state['runs']) + 1
    while state['frontier'] and report['nodes_checked'] < limit:
        key = state['frontier'].pop(0)
        node = state['nodes'][key]
        current = _zn_apply(text, node['edits'])
        node['attempts'] += 1
        node['last_run'] = run_number
        report['nodes_checked'] += 1
        try:
            parsed = zero_core(None, 'recovery', operation='parse_text', operands=(current,))
        except json.JSONDecodeError as exc:
            node['error'] = {'message': exc.msg, 'offset': exc.pos,
                             'left_context': current[max(0, exc.pos - 96):exc.pos],
                             'right_context': current[exc.pos:exc.pos + 96]}
            if key == digest:
                report['first_error'] = node['error']
            proposals = zero_core(None, 'recovery', operation='propose_paths',
                                  operands=(current, exc, fields))
            # A cursor preserves proposals beyond the per-node work budget.
            cursor = node.get('proposal_cursor', 0)
            count = 0
            exhausted = True
            for index, (changed, edit) in enumerate(proposals):
                if index < cursor:
                    continue
                if count >= _ZN_PROPOSALS_PER_NODE:
                    exhausted = False
                    break
                count += 1
                node['proposal_cursor'] = index + 1
                target = _zr_hashlib.sha256(changed.encode('utf-8')).hexdigest()
                edge = {'from': key, 'to': target, 'edit': edit, 'zero_nexus': 'Z0',
                        'context': context, 'first_run': run_number, 'traversals': 1}
                old = next((e for e in state['edges'] if e['from'] == key and
                            e['to'] == target and e['edit'] == edit and e['context'] == context), None)
                if old is None:
                    state['edges'].append(edge)
                else:
                    old['traversals'] += 1
                if target not in state['nodes']:
                    state['nodes'][target] = {'edits': node['edits'] + [edit],
                                              'status': 'pending', 'attempts': 0}
                    state['frontier'].append(target)
            node['expanded_context'] = context
            if not exhausted:
                node['status'] = 'pending'
                state['frontier'].append(key)
            else:
                node['status'] = 'expanded' if node.get('proposal_cursor', 0) else 'dead_end'
                if node['status'] == 'dead_end':
                    node['proposal_cursor'] = 0
        except (ValueError, RecursionError) as exc:
            node.update(status='dead_end', error={'message': str(exc)}, proposal_cursor=0)
        else:
            node['status'] = 'syntax_candidate'
            solutions.append((parsed, node['edits'], current))
            if len(solutions) >= _ZT_MAX_CANDIDATES:
                break
    pending = len(state['frontier'])
    dead = sum(n['status'] == 'dead_end' for n in state['nodes'].values())
    report.update(status='syntax_candidates' if solutions else 'unresolved',
                  alternatives_found=len(solutions), pending_paths=pending,
                  retained_dead_ends=dead, total_path_edges=len(state['edges']),
                  continuation='resume_frontier' if pending else 'retry_dead_ends_on_next_run',
                  boundary='Supplied rules and observed fragments generate hypotheses; syntax does not prove original recovery.')
    state['runs'].append({'run': run_number, 'nodes_checked': report['nodes_checked'],
                          'pending_paths': pending, 'dead_ends': dead,
                          'syntax_candidates': len(solutions)})
    return report, solutions, state


def _zn_checkpoint(path, state):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as target:
        json.dump(state, target, ensure_ascii=False, separators=(',', ':'), allow_nan=False)
        target.flush()
        os.fsync(target.fileno())
    os.replace(tmp, path)


_zn_previous_load_text = _zt_load_file


def _zt_load_file(path, inspect_only=False):
    with open(path, 'rb') as source:
        raw = source.read(_ZT_MAX_BYTES + 1)
    if len(raw) > _ZT_MAX_BYTES:
        raise ZeroRecoveryPending('Text inspection byte budget exceeded')
    try:
        text = raw.decode('utf-8')
    except UnicodeError as exc:
        # Preserve byte-level failure evidence for a later encoding worker.
        evidence = {'schema': 1, 'zero_nexus': 'Z0', 'status': 'pending',
                    'source_sha256': _zr_hashlib.sha256(raw).hexdigest(),
                    'operation': 'decode_utf8', 'error': str(exc),
                    'byte_offset': exc.start, 'worker': 'not_implemented'}
        report_path = _zt_write_new(path + '.zero-byte-report.json', evidence)
        raise ZeroRecoveryPending('Encoding path returned to Z0. Report: ' + report_path) from exc
    try:
        zero_core(None, 'recovery', operation='parse_text', operands=(text,))
    except (ValueError, RecursionError):
        checkpoint_path = path + '.zero-nexus-search.json'
        state = None
        if os.path.exists(checkpoint_path):
            with open(checkpoint_path, encoding='utf-8') as source:
                state = _zt_parse(source.read())
        report, solutions, state = zero_core(state, 'recovery', operation='explore', operands=(text,))
        report['checkpoint'] = checkpoint_path
        for number, (candidate, edits, repaired_text) in enumerate(solutions, 1):
            entry = {'number': number, 'edits': edits, 'syntax_valid': True,
                     'original_recovery_verified': False}
            try:
                if not isinstance(candidate, dict) or candidate.get('schema') != 1 or candidate.get('version') != VERSION:
                    raise ValueError('Not a compatible engine memory')
                checked, ready = zero_core(candidate, 'errors', operation='recover_archive')
                entry['archive_preflight'] = 'ready' if ready else 'pending_or_blocked'
                entry['archive_reason'] = _zr_state(checked).get('reason', _zr_state(checked)['status'])
            except (ValueError, KeyError, TypeError, IndexError, RecursionError, AttributeError) as exc:
                entry.update(archive_preflight='blocked', archive_reason=str(exc))
            entry['path'] = _zt_write_new(path + '.zero-text-candidate-%d.json' % number, candidate)
            candidate_key = _zr_hashlib.sha256(repaired_text.encode('utf-8')).hexdigest()
            state['nodes'][candidate_key]['validation'] = entry
            if entry['archive_preflight'] != 'ready':
                state['nodes'][candidate_key]['status'] = 'dead_end'
                state['nodes'][candidate_key]['return_reason'] = 'archive_validation_unresolved'
            report['candidates'].append(entry)
        report['retained_dead_ends'] = sum(
            node['status'] == 'dead_end' for node in state['nodes'].values())
        state['runs'][-1]['dead_ends'] = report['retained_dead_ends']
        _zn_checkpoint(checkpoint_path, state)
        report_path = _zt_write_new(path + '.zero-text-report.json', report)
        print('Zero nexus:', report['status'], '| candidates:', len(solutions),
              '| pending paths:', report['pending_paths'], '| retained dead ends:', report['retained_dead_ends'])
        raise ZeroRecoveryPending('Recovery paths saved; run again to continue. Report: ' + report_path)
    return _zn_previous_load_text(path, inspect_only)


def install_zero_nexus_paths(api):
    previous = api['zero_core']
    def core(m, domain, **kwargs):
        if domain == 'recovery':
            operation = kwargs.get('operation')
            operands = kwargs.get('operands', ())
            if operation == 'construction_rules':
                return _zr_copy.deepcopy(_ZN_RULES)
            if operation == 'parse_text':
                return _zt_parse(*operands)
            if operation == 'observe_paths':
                return _zn_evidence(*operands)
            if operation == 'propose_paths':
                return _zn_proposals(*operands)
            if operation == 'explore':
                return _zn_search(operands[0], m)
            raise ValueError('Unsupported recovery nexus operation')
        if domain == 'errors' and kwargs.get('operation') == 'recover_archive':
            checked, ready = previous(m, domain, **kwargs)
            attempts = checked.setdefault('zero_nexus_archive_attempts', [])
            attempts.append({'attempt': len(attempts) + 1, 'zero_nexus': 'Z0',
                             'status': _zr_state(checked)['status'],
                             'ready': ready, 'reason': _zr_state(checked).get('reason'),
                             'continuation': 'normal_exploration' if ready else 'retained_for_recovery'})
            return checked, ready
        return previous(m, domain, **kwargs)
    api['zero_core'] = core


install_zero_nexus_paths(globals())


# V4.7.5: whole-body maps, zero slots, evidence bridges, continuous recovery.
import re as _zw_re
_ZW_RULE = 'whole_body_zero_slots_v1'
_ZW_SECONDS = None  # Recovery continues until a candidate, exhausted work, or interrupt.


def _zw_decode_at(text, offset):
    return json.JSONDecoder(object_pairs_hook=_zt_pairs,
                            parse_constant=_zt_constant).raw_decode(text, offset)


def _zw_map(text):
    """Lossless source + ordered spans. Lexical roles are tentative after damage."""
    lexemes, i = [], 0
    while i < len(text):
        start, ch = i, text[i]
        if ch == '"':
            i += 1
            escaped = False
            while i < len(text):
                c = text[i]; i += 1
                if escaped: escaped = False
                elif c == '\\': escaped = True
                elif c == '"': break
            role = 'quoted_symbol_sequence'
        elif ch in '{}[]:,':
            i += 1
            role = {'{':'object_open','}':'object_close','[':'array_open',']':'array_close',
                    ':':'key_value_separator',',':'ordered_separator'}[ch]
        else:
            i += 1
            while i < len(text) and text[i] not in '"{}[]:,': i += 1
            role = 'literal_or_whitespace'
        lexemes.append([start, i, role])
    # Independent decoding resynchronizes even when an earlier quote is damaged.
    records = []
    for hit in _zw_re.finditer(r'(?<!\\)\{\s*"(?:expr|id|seq|source|kind)"\s*:', text):
        try: rec, end = _zw_decode_at(text, hit.start())
        except (ValueError, RecursionError): continue
        if not isinstance(rec, dict): continue
        records.append({'start': hit.start(), 'end': end, 'record': rec,
                        'status': 'independently_parseable_not_authenticated',
                        'zero_nexus': 'Z0'})
    # Rational expression anchors are independently checked, not located by a
    # bracket count that assumes the damaged text is already well formed.
    boundary = text.find('"complex_archive":')
    boundary = len(text) if boundary < 0 else boundary
    starts = [h.start() for h in _zw_re.finditer(r'(?<!\\)\{"expr"\s*:', text[:boundary])]
    expressions = []
    for start in starts:
        try:
            rec, end = _zw_decode_at(text, start)
            good = (isinstance(rec, dict) and type(rec.get('id')) is int
                    and 'tree' in rec and 'parents' in rec)
        except (ValueError, RecursionError): rec, end, good = None, None, False
        expressions.append({'start': start, 'end': end, 'record': rec, 'complete': good})
    slots, edits = [], []
    for index, item in enumerate(expressions):
        if item['complete']: continue
        left = next((x for x in reversed(expressions[:index]) if x['complete']), None)
        right = next((x for x in expressions[index + 1:] if x['complete']), None)
        if left is None or right is None: continue
        if text[left['end']:item['start']].strip() != ',': continue
        lo, hi = left['record']['id'] + 1, right['record']['id']
        if not 0 <= lo < hi <= _ZR_MAX_SLOTS or hi - lo > _ZR_MAX_GAPS: continue
        if any(slot['start'] <= item['start'] < slot['end'] for slot in slots): continue
        around = [x for x in expressions[max(0,index-2):index+3] if x['complete']]
        refs = set(range(lo, hi))
        related = [x for x in expressions if x['complete'] and
                   (x['record']['id'] in refs or refs.intersection(x['record'].get('parents', [])))]
        slot = {'id': 'Z-slot-%d' % len(slots), 'zero_nexus': 'Z0',
                'kind': 'damaged_rational_expression_span', 'status': 'unknown',
                'start': item['start'], 'end': right['start'],
                'raw_fragment': text[item['start']:right['start']],
                'left_anchor': left, 'right_anchor': right,
                'surrounding_expressions': around, 'referencing_expressions': related,
                'candidate_ids': list(range(lo, hi)),
                'boundary_claim': 'candidate array-element span between independently parsed neighbours'}
        slots.append(slot)
        edits.append({'offset_in_previous_candidate': item['start'],
                      'before': text[item['start']:right['start']], 'after': '',
                      'rule': 'quarantine_span_in_candidate_only', 'slot': slot['id'],
                      'zero_nexus': 'Z0'})
    # Reverse offsets keep every edit relative to its actual preceding text.
    edits.sort(key=lambda x: x['offset_in_previous_candidate'], reverse=True)
    return {'schema': 1, 'rule': _ZW_RULE, 'zero_nexus': 'Z0',
            'source_sha256': _zr_hashlib.sha256(text.encode('utf-8')).hexdigest(),
            'source_text': text, 'offset_units': 'Unicode code points',
            'ordered_symbol_spans': lexemes,
            'alphabet': {str(ord(c)): c for c in sorted(set(text))},
            'complete_records': records, 'expression_map': expressions,
            'zero_slots': slots, 'candidate_skeleton_edits': edits,
            'rules': {'representation': 'supplied JSON / Unicode',
                      'alpha_roles': 'symbol identity, lexical role, position, order',
                      'reconstruction': 'surviving events + construction rules; unknowns remain explicit'},
            'boundary': 'Independent parsing and neighbouring positions do not authenticate original content.'}


def _zw_genesis(text):
    hit = _zw_re.search(r'(?<!\\)"genesis"\s*:\s*', text)
    if not hit: return None
    try: return _zw_decode_at(text, hit.end())[0]
    except (ValueError, RecursionError): return None


def _zw_constraints(text):
    """Proven contradictions stay recorded; guesses never become accepted evidence."""
    genesis = _zw_genesis(text)
    if not genesis: return []
    issues = []
    for event in genesis.get('events', []):
        if event.get('type') not in ('tangent_queued', 'tangent_selected', 'tangent_completed'): continue
        try:
            task = _zt_parse(event['task_key'])
            expected = tangent_parent(task)
            if event.get('parent') != expected or event.get('kind') != task['kind']:
                issues.append({'rule': 'saved_task_parent_and_kind', 'event_seq': event.get('seq'),
                               'expected_parent': expected, 'observed_parent': event.get('parent')})
        except (ValueError, KeyError, TypeError): continue
    return issues


def _zw_bridges(text, source, error):
    """Insert a surviving span only when both exact 16-symbol boundaries match."""
    found = {}
    for split in range(max(16,error.pos-100), min(len(text)-16,error.pos+20)):
        left, right = text[split-16:split], text[split:split+16]
        at = source.find(left)
        while at >= 0:
            start = at + 16
            end = source.find(right, start + 1, min(len(source), start + 1024))
            if end >= 0:
                gap = source[start:end]
                # Do not confuse repeated field snippets with intervening records.
                if not any(marker in gap for marker in ('},{"seq":', '},{"expr":')):
                    changed = text[:split] + gap + text[split:]
                    key = _zr_hashlib.sha256(changed.encode('utf-8')).hexdigest()
                    if key not in found:
                        try: _zt_parse(changed); progress = len(text)
                        except json.JSONDecodeError as exc: progress = exc.pos-len(gap)
                        except (ValueError, RecursionError): progress = -1
                        found[key] = [changed, {'offset_in_previous_candidate': split,
                            'before': '', 'after': gap, 'rule': 'two_sided_observed_bridge',
                            'left_anchor': left, 'right_anchor': right,
                            'evidence_spans': [], 'zero_nexus': 'Z0'}, progress]
                    found[key][1]['evidence_spans'].append([at,end+16])
            at = source.find(left,at+1)
    # Low-progress paths remain available in the fallback grammar search;
    # successful bridges are scheduled first, with all source occurrences kept.
    return [x[:2] for x in sorted(found.values(), key=lambda x:(-x[2],len(x[1]['after'])))
            if x[2] > error.pos]


def _zw_ledger_bridge(text):
    """Reconstruct a missing ledger row prefix from independent event counters."""
    genesis = _zw_genesis(text)
    if not genesis or genesis.get('suppressed_events') != 0: return []
    start = text.find('"tangent_ledger":')
    if start < 0: return []
    stop = text.find('"complex_archive":', start)
    stop = len(text) if stop < 0 else stop
    segment = text[start:stop]
    present = set(_zw_re.findall(r'"([^"]+)"\s*:\s*\{',segment))
    counters, events = {}, {}
    for ev in genesis.get('events', []):
        parent = ev.get('parent');kind = ev.get('type')
        if not isinstance(parent,str) or parent in present: continue
        if kind == 'tangent_queued' and type(ev.get('parent_generated')) is int:
            counters[parent] = max(counters.get(parent,0),ev['parent_generated'])
            events.setdefault(parent,[]).append(ev.get('seq'))
    pattern = r'\},(?P<tail>"selected":\d+,"completed":\d+\}),(?="(?:rational|complex):\d+":\{)'
    options=[]
    for match in _zw_re.finditer(pattern,segment):
        for parent,count in counters.items():
            split = start + match.start('tail')
            insert = json.dumps(parent)+':{"generated":'+str(count)+','
            options.append((text[:split]+insert+text[split:],
                            {'offset_in_previous_candidate':split,'before':'','after':insert,
                             'rule':'ledger_row_from_surviving_event_counter', 'zero_nexus':'Z0',
                             'event_sequences':events[parent], 'parent':parent,
                             'preserved_tail':match.group('tail')}))
    return options


def _zw_role_queue_bridge(text):
    """Replay the recorded FIFO grammar and require all intact tasks to agree."""
    marker=text.find('"roles_archive":')
    if marker<0:return []
    match=_zw_re.search(r'"expressions"\s*:\s*',text[marker:])
    if not match:return []
    try:records,end=_zw_decode_at(text,marker+match.end())
    except (ValueError,RecursionError):return []
    qmatch=_zw_re.search(r'"queue"\s*:\s*\[',text[end:])
    if not qmatch:return []
    qstart=end+qmatch.end()
    tail=_zw_re.search(r'\]\s*,\s*"head"\s*:\s*(\d+)',text[qstart:])
    if not tail:return []
    qend=qstart+tail.start();head=int(tail.group(1))
    fragment=text[qstart:qend]
    orphan=list(_zw_re.finditer(r'(?<=},)"cursor"\s*:\s*(\d+)\}',fragment))
    if len(orphan)!=1 or head>100000:return []
    gap=orphan[0];before=fragment[:gap.start()];after=fragment[gap.end():]
    try:
        prefix=_zt_parse('['+before.rstrip().rstrip(',')+']')
        suffix=_zt_parse('['+after.lstrip().lstrip(',')+']')
        # Decode independent fields, even while the full root remains damaged.
        context={}
        for field in ('foundation','expressions','results'):
            hit=_zw_re.search(r'"'+field+r'"\s*:\s*',text)
            if not hit:return []
            context[field]=_zw_decode_at(text,hit.end())[0]
    except (ValueError,RecursionError):return []
    context['roles_archive']={'expressions':records}
    if not records or records[0].get('rule')!='reference_foundation_zero':return []
    queue=[{'source':0,'cursor':0}];seen={0};next_id=1
    key=lambda r:json.dumps([r['parents'],r['rule'],r['label'],r['sources']],sort_keys=True,separators=(',',':'))
    lookup={key(r):r['id'] for r in records}
    try:
        for i in range(head):
            task=queue[i];rec=records[task['source']];cursor=task['cursor']
            if rec['depth']>=min(ROLE_MAX_DEPTH,len(context['foundation']['states'])):continue
            if cursor>=3+len(context['foundation']['states']):queue.append(dict(task));continue
            target=('A','a','x')[cursor] if cursor<3 else cursor-3
            result,reason=zero_core(context,'roles',operation='transform',operands=(task['source'],target))
            if reason:continue
            idx=lookup.get(key(result))
            if idx is None:return []
            if idx not in seen:
                if idx!=next_id:return []
                for field in ('parents','sources','rule','label','body','path','depth'):
                    if result[field]!=records[idx][field]:return []
                seen.add(idx);next_id+=1;queue.append({'source':idx,'cursor':0})
            queue.append({'source':task['source'],'cursor':cursor+1})
    except (KeyError,IndexError,ValueError,TypeError):return []
    n=len(prefix)
    if (len(queue)!=len(prefix)+1+len(suffix) or queue[:n]!=prefix or queue[n+1:]!=suffix
            or queue[n]['cursor']!=int(gap.group(1)) or next_id!=len(records)):return []
    split=qstart+gap.start();insert='{"source":'+str(queue[n]['source'])+','
    return [(text[:split]+insert+text[split:],
             {'offset_in_previous_candidate':split,'before':'','after':insert,
              'rule':'recorded_role_fifo_reexecution','zero_nexus':'Z0',
              'head':head,'queue_index':n,'intact_tasks_checked':len(prefix)+len(suffix),
              'recorded_role_constructions_checked':len(records)})]


def _zw_state(text, mapping):
    edits=mapping['candidate_skeleton_edits'];current=_zn_apply(text,edits)
    key=_zr_hashlib.sha256(current.encode('utf-8')).hexdigest()
    return {'schema':1,'rule':_ZW_RULE,'zero_nexus':'Z0','source_sha256':mapping['source_sha256'],
            'nodes':{key:{'edits':edits,'status':'pending','attempts':0}},'frontier':[key],
            'edges':[],'attempts':0,'candidates':[], 'status':'searching',
            'boundary':'Candidate skeleton quarantines fragments; it is never accepted memory.'}


def _zw_validate(parsed):
    if not isinstance(parsed,dict) or parsed.get('schema')!=1 or parsed.get('version')!=VERSION:
        checked=_zr_copy.deepcopy(parsed) if isinstance(parsed,dict) else {'unknown_root':parsed}
        _zr_state(checked).update(status='blocked',reason='Not a compatible engine memory')
        return checked,False,[{'rule':'engine_memory_schema','reason':'Not a compatible engine memory'}]
    # Pending slots restore only by independent recipes/events and exact execution.
    try:
        checked,ready=zero_core(parsed,'errors',operation='recover_archive')
    except (ValueError,KeyError,TypeError,IndexError,AttributeError,RecursionError) as error:
        checked=_zr_copy.deepcopy(parsed)
        _zr_state(checked).update(status='blocked',reason=str(error))
        return checked,False,[{'rule':'archive_preflight','reason':str(error)}]
    issues=_zw_constraints(json.dumps(parsed,ensure_ascii=False))
    if issues:ready=False
    return checked,ready,issues


def _zw_recover(path,text,seconds=None):
    map_path=path+'.zero-body-map.json';state_path=path+'.zero-body-search.json'
    digest=_zr_hashlib.sha256(text.encode('utf-8')).hexdigest()
    mapping=None;state=None
    for filename,name in ((map_path,'map'),(state_path,'state')):
        if os.path.exists(filename):
            with open(filename,encoding='utf-8') as stream:value=_zt_parse(stream.read())
            if value.get('source_sha256')!=digest or value.get('rule')!=_ZW_RULE:
                raise ZeroRecoveryPending('Whole-body checkpoint does not match source/rules: '+filename)
            if name=='map':mapping=value
            else:state=value
    if mapping is None:
        mapping=zero_core(None,'whole_body',operation='map',operands=(text,))
        _zn_checkpoint(map_path,mapping)
    if state is None:
        state=_zw_state(text,mapping)
        legacy_path=path+'.zero-nexus-search.json'
        if os.path.exists(legacy_path):
            with open(legacy_path,encoding='utf-8') as stream:legacy=_zt_parse(stream.read())
            if legacy.get('schema')==1 and legacy.get('source_sha256')==digest:
                state['grammar']=legacy
                state['retained_legacy_continuation']=legacy_path
    if state.get('status')=='candidate_ready':
        print('Recovery candidate already saved:',state['candidates'][-1]['path'])
        return state
    print('Zero body:',len(mapping['complete_records']),'readable records |',
          len(mapping['zero_slots']),'expression slots | continuous recovery',flush=True)
    begin=time.monotonic();last=begin
    try:
        while True:
            if seconds is not None and time.monotonic()-begin>=seconds:
                state['status']='paused_by_requested_time';break
            if not state['frontier']:
                # Preserve the earlier grammar search and all its paths. Recovery
                # loops internally; a checkpoint boundary no longer ends the run.
                report,solutions,grammar=zero_core(state.get('grammar'),'recovery',operation='explore',operands=(text,))
                state['grammar']=grammar
                for parsed,edits,repaired in solutions:
                    checked,ready,issues=zero_core(None,'whole_body',operation='validate',operands=(parsed,))
                    entry={'archive_ready':ready,'issues':issues,'original_recovery_verified':False,
                           'path':_zt_write_new(path+'.zero-body-candidate.json',checked)}
                    state['candidates'].append(entry)
                    if ready:state['status']='candidate_ready';break
                if state['status']=='candidate_ready':break
                if not grammar['frontier']:
                    state['status']='waiting_for_new_evidence';break
            else:
                key=state['frontier'][0];node=state['nodes'][key]
                current=_zn_apply(text,node['edits']);node['attempts']+=1;state['attempts']+=1
                constraints=zero_core(None,'whole_body',operation='constraints',operands=(current,))
                if constraints:
                    node.update(status='contradicted_by_saved_task',constraints=constraints)
                    state['frontier'].pop(0);continue
                try:parsed=_zt_parse(current)
                except json.JSONDecodeError as error:
                    node['error']={'message':error.msg,'offset':error.pos}
                    options=zero_core(None,'whole_body',operation='propose',operands=(current,text,error))
                    # Pop only after expansion finishes: interruption retries work safely.
                    for changed,edit in options:
                        target=_zr_hashlib.sha256(changed.encode('utf-8')).hexdigest()
                        edge={'from':key,'to':target,'edit':edit,'zero_nexus':'Z0'}
                        if edge not in state['edges']:state['edges'].append(edge)
                        if target not in state['nodes']:
                            state['nodes'][target]={'edits':node['edits']+[edit],'status':'pending','attempts':0}
                            state['frontier'].append(target)
                    node['status']='expanded' if options else 'unresolved_at_zero'
                    state['frontier'].pop(0)
                except (ValueError,RecursionError) as error:
                    node.update(status='unresolved_at_zero',error={'message':str(error)})
                    state['frontier'].pop(0)
                else:
                    checked,ready,issues=zero_core(None,'whole_body',operation='validate',operands=(parsed,))
                    checked['zero_body_recovery']={
                        'rule':_ZW_RULE,'zero_nexus':'Z0','source_sha256':digest,
                        'original_recovery_verified':False,'archive_ready':ready,
                        'edits':node['edits'],'map_file':map_path,
                        'zero_slots':mapping['zero_slots']}
                    entry={'archive_ready':ready,'issues':issues,'original_recovery_verified':False,
                           'recovered_ids':[ev['id'] for ev in _zr_state(checked)['events'] if ev['status']=='recovered'],
                           'path':_zt_write_new(path+'.zero-body-candidate.json',checked),'node':key}
                    node.update(status='candidate_ready' if ready else 'archive_pending',validation=entry)
                    state['candidates'].append(entry);state['frontier'].pop(0)
                    if ready:state['status']='candidate_ready';break
            now=time.monotonic()
            if now-last>=5:
                _zn_checkpoint(state_path,state);last=now
                print('Zero recovery: checked',state['attempts'],'| pending',len(state['frontier']),
                      '| candidates',len(state['candidates']), '| checkpoint saved',flush=True)
    except KeyboardInterrupt:
        state['status']='paused_by_user'
        print('\nRecovery paused; saving continuation.',flush=True)
    finally:
        _zn_checkpoint(state_path,state)
    print('Zero recovery:',state['status'],'| candidates:',len(state['candidates']),flush=True)
    for entry in state['candidates'][-3:]:
        print('Candidate:',entry['path'],'| archive ready:',entry['archive_ready'],
              '| reconstructed IDs:',entry.get('recovered_ids',[]),flush=True)
    return state


def install_zero_whole_body(api):
    previous=api['zero_core']
    def core(m,domain,**kwargs):
        if domain=='whole_body':
            op=kwargs.get('operation');args=kwargs.get('operands',())
            if op=='map':return _zw_map(*args)
            if op=='constraints':return _zw_constraints(*args)
            if op=='validate':return _zw_validate(*args)
            if op=='propose':
                text,source,error=args
                # All alternatives remain as separate edges, including equal texts.
                return _zw_role_queue_bridge(text)+_zw_ledger_bridge(text)+_zw_bridges(text,source,error)
            raise ValueError('Unknown whole-body zero operation')
        return previous(m,domain,**kwargs)
    api['zero_core']=core


install_zero_whole_body(globals())
_zw_previous_text_load=_zt_load_file


def _zt_load_file(path,inspect_only=False):
    with open(path,'rb') as stream:raw=stream.read(_ZT_MAX_BYTES+1)
    if len(raw) > _ZT_MAX_BYTES:
        # The bounded damaged-text search is not an archive growth limit.
        # Large memories may continue only after strict JSON, foundation,
        # arithmetic and cross-archive link validation. Malformed input stays
        # untouched and does not enter unbounded text repair.
        try:
            checked, report = _za_validate(path)
        except (ValueError, UnicodeError, RecursionError, KeyError, TypeError,
                IndexError, AttributeError) as exc:
            raise ZeroRecoveryPending(
                'Large memory failed validation; source unchanged. '
                'Damaged-text repair retains its byte budget: ' + str(exc)) from exc
        with open(path, encoding='utf-8') as stream:
            text = stream.read()
        checked['zero_text_observation'] = zero_core(
            None, 'text', operation='observe_structure', operands=(text,))
        if inspect_only:
            print('Zero text check: large JSON archive validated; source unchanged.')
        return checked
    try:text=raw.decode('utf-8')
    except UnicodeError:return _zw_previous_text_load(path,inspect_only)
    try:_zt_parse(text)
    except (ValueError,RecursionError):
        state=_zw_recover(path,text,_ZW_SECONDS)
        if state.get('status') == 'candidate_ready' and not inspect_only:
            return zero_approve_recovery(path, state)
        raise ZeroRecoveryPending('Recovery '+state['status']+'; source unchanged. Continuation: '+path+'.zero-body-search.json')
    return _zw_previous_text_load(path,inspect_only)



# ============================================================
# V4.7.6 - EXACT CALCULATOR / EMERGENT ARCHIVE CROSS-CHECK
# Read-only verification. Unresolved cases return as zero work proposals.
# ============================================================

def zero_verify_candidate(candidate_path):
    import hashlib
    from pathlib import Path
    from collections import defaultdict
    with open(candidate_path, encoding='utf-8') as f:
        m = json.load(f)
    if m.get('schema') != 1 or m.get('version') != VERSION:
        raise ValueError('Candidate schema/version incompatible')
    records = m.get('expressions', [])
    if not isinstance(records, list):
        raise ValueError('Expression archive missing')
    by_value = defaultdict(list)
    findings = []
    evidence = []
    for index, rec in enumerate(records):
        reasons = []
        try:
            if rec['id'] != index:
                reasons.append('id_position_mismatch')
            tree = rec['tree']
            # Independent exact evaluation through Fraction; never trust saved value.
            calculated, _ = evaluate_tree(tree)
            stored = number(rec['value'])
            if calculated != stored:
                reasons.append('calculator_archive_disagreement')
            leaves = rational_tree_leaves(tree)
            if leaves != rec.get('leaves'):
                reasons.append('tree_leaf_metadata_disagreement')
            parents = rec.get('parents', [])
            if not isinstance(parents, list) or any(
                not isinstance(p, int) or p < 0 or p >= len(records)
                for p in parents
            ):
                reasons.append('invalid_parent_reference')
            else:
                # Trace parent links; do not mistake multiple shared ancestors
                # for independent confirmation.
                if index in parents:
                    reasons.append('self_parent_reference')
            if not reasons:
                by_value[encode(calculated)].append(index)
        except (KeyError, ValueError, TypeError, ZeroDivisionError,
                IndexError, RecursionError, OverflowError) as error:
            reasons.append('unverifiable_expression:' + type(error).__name__)
        if reasons:
            findings.append({'id': index, 'status': 'contradiction',
                             'reasons': reasons, 'parents': rec.get('parents', []),
                             'pathway': rec.get('pathway')})
    for key, ids in by_value.items():
        # Agreement among distinct constructions is corroboration, not proof
        # of independent lineage.
        if len(ids) > 1:
            evidence.append({'value': key, 'supporting_ids': ids[:20],
                             'count': len(ids)})
    # Check archive index separately; it can also be corrupted.
    for value, ids in m.get('results', {}).items():
        for idx in ids:
            if not isinstance(idx, int) or idx < 0 or idx >= len(records) or \
                    records[idx].get('value') != value:
                findings.append({'id': idx, 'status': 'contradiction',
                                 'reasons': ['results_index_mismatch'],
                                 'indexed_value': value})
    # Candidate does not become accepted merely because its expressions agree.
    status = 'unresolved' if findings else 'arithmetic_consistent'
    report = {
        'schema': 1, 'rule': 'zero_double_verification_v476',
        'candidate': str(candidate_path),
        'candidate_sha256': hashlib.sha256(
            Path(candidate_path).read_bytes()).hexdigest(),
        'status': status, 'records_checked': len(records),
        'contradictions': findings,
        'archive_correlations': evidence[:100],
        'zero_feedback': [
            {'zero_nexus': 'Z0', 'kind': 'verification_revisit',
             'source_id': f['id'], 'reasons': f['reasons'],
             'status': 'proposed_not_executed'}
            for f in findings
        ],
        'continuation_verified': False,
        'warning': 'Arithmetic consistency is not a proof of historical recovery. '
                   'Zero feedback is quarantined until a recovery worker consumes it.'
    }
    output = str(candidate_path) + '.verification.json'
    _zn_checkpoint(output, report)
    print('Zero double verification:', status,
          '| checked:', len(records), '| contradictions:', len(findings))
    print('Report:', output)
    print('Continuation not yet verified; original source unchanged.')
    return report


# ============================================================
# V4.7.7 - NONDESTRUCTIVE ADAPTIVE RECOVERY PLANNER
# ============================================================

def zero_adaptive_recovery(candidate_path, baseline_path=None):
    """Assess recovery vs regeneration without changing either input file.

    A baseline is necessary to MEASURE missing records. Without one, only
    detected contradictions are reported; no loss percentage is invented.
    """
    import hashlib
    from pathlib import Path
    candidate_path = str(Path(candidate_path).resolve())
    with open(candidate_path, encoding='utf-8') as handle:
        candidate = json.load(handle)
    if not isinstance(candidate, dict) or not isinstance(candidate.get('expressions'), list):
        raise ValueError('Candidate needs a rational expression archive')
    records = candidate['expressions']
    baseline = None
    if baseline_path:
        baseline_path = str(Path(baseline_path).resolve())
        if baseline_path == candidate_path:
            raise ValueError('Baseline must differ from candidate')
        with open(baseline_path, encoding='utf-8') as handle:
            baseline = json.load(handle)
        if not isinstance(baseline, dict) or not isinstance(baseline.get('expressions'), list):
            raise ValueError('Baseline needs a rational expression archive')
    verification = zero_verify_candidate(candidate_path)
    # A missing or altered expression can be found using construction identity.
    # IDs alone are insufficient after deletion and renumbering.
    def identity(rec):
        return json.dumps([rec.get('pathway'), rec.get('tree')],
                          sort_keys=True, separators=(',', ':'))
    expected = {identity(rec) for rec in baseline['expressions']} if baseline else None
    present = {identity(rec) for rec in records}
    missing = len(expected - present) if expected is not None else None
    lost_fraction = (missing / len(expected) if expected else
                     (0.0 if expected is not None else None))
    # Foundation is checked against independently specified construction rules,
    # not inferred solely from the potentially corrupted candidate.
    f = candidate.get('foundation', {})
    states = f.get('states') if isinstance(f, dict) else None
    foundation_ok = (isinstance(states, list) and bool(states) and
                     all(type(n) is int and n == i for i, n in enumerate(states)) and
                     f.get('rule') == 'foundation_state_count_v3' and
                     isinstance(f.get('zero_records'), list) and
                     len(f['zero_records']) == len(states) and
                     all(isinstance(z, dict) and z.get('id') == 'Z%d' % i
                         for i, z in enumerate(f['zero_records'])))
    # These are transparent WORK PROXIES, not runtime forecasts.
    contradictions = len(verification['contradictions'])
    repair_proxy = None if missing is None else missing + contradictions
    regeneration_proxy = None if expected is None else len(expected)
    checkpoint = lost_fraction is not None and lost_fraction >= 0.50
    if not foundation_ok:
        decision = 'quarantine_foundation_verify_rules'
    elif lost_fraction is None:
        decision = 'insufficient_baseline_for_loss_estimate'
    elif checkpoint:
        decision = 'compare_recovery_and_regeneration'
    else:
        decision = 'targeted_recovery_first'
    report = {
        'rule': 'zero_adaptive_recovery_v477',
        'candidate': candidate_path, 'baseline': baseline_path,
        'candidate_sha256': hashlib.sha256(Path(candidate_path).read_bytes()).hexdigest(),
        'baseline_records': len(expected) if expected is not None else None,
        'candidate_records': len(records), 'missing_unique_constructions': missing,
        'lost_fraction': lost_fraction, 'fifty_percent_checkpoint': checkpoint,
        'foundation_rule_check': 'pass' if foundation_ok else 'uncertain',
        'contradictions': contradictions, 'repair_work_proxy': repair_proxy,
        'regeneration_work_proxy': regeneration_proxy,
        'decision': decision, 'originals_preserved': True,
        'automatic_reset': False, 'automatic_resume': False,
        'notes': [
            'Record-count work proxies do not measure actual runtime cost.',
            'Missing construction identity does not prove irrecoverable information loss.',
            'Foundation checks are necessary but not sufficient to trust all rules.',
            'Regeneration requires a separate verified-rule replay and continuation test.'
        ]}
    report_path = candidate_path + '.adaptive-report.json'
    _zn_checkpoint(report_path, report)
    print('Zero adaptive recovery:', decision)
    print('Measured archive loss:',
          ('unknown (baseline required)' if lost_fraction is None else
           '%.2f%%' % (100 * lost_fraction)))
    print('Foundation:', report['foundation_rule_check'],
          '| contradictions:', contradictions)
    print('Report:', report_path)
    print('No archive reset, overwrite, or automatic continuation performed.')
    return report

# ============================================================
# V4.7.8 - VERIFIED APPROVAL AND SAME-RUN RESUME
# Approval is operational acceptance, not authentication of lost history.
# ============================================================

def _za_validate(candidate_path):
    with open(candidate_path, encoding='utf-8') as stream:
        parsed = _zt_parse(stream.read())
    checked, ready, issues = zero_core(
        None, 'whole_body', operation='validate', operands=(parsed,))
    if not ready or issues:
        raise ZeroRecoveryPending('Candidate failed archive validation: ' +
                                  str(issues or _zr_state(checked).get('reason', 'pending')))
    f = checked.get('foundation', {})
    states = f.get('states')
    if (not isinstance(states, list) or not states or
            any(type(n) is not int or n != i for i, n in enumerate(states)) or
            f.get('rule') != 'foundation_state_count_v3' or
            [z.get('id') for z in f.get('zero_records', [])] !=
            ['Z%d' % i for i in range(len(states))]):
        raise ZeroRecoveryPending('Candidate failed foundation validation')
    # Check the validated copy, including any records rebuilt during preflight.
    # The verifier is intentionally read-only except for its separate report.
    report = _za_verify_memory(checked)
    if report['contradictions']:
        raise ZeroRecoveryPending('Candidate has expression/index contradictions: ' +
                                  str(report['contradictions'][:5]))
    audit = archive_link_audit(checked)
    if audit['issues']:
        raise ZeroRecoveryPending('Candidate failed archive link audit: ' + str(audit))
    return checked, report


def _za_verify_memory(m):
    findings = []
    records = m['expressions']
    for idx, rec in enumerate(records):
        try:
            value, expression = evaluate_tree(rec['tree'])
            if (type(rec['id']) is not int or rec['id'] != idx or
                    encode(value) != rec['value'] or expression != rec['expr'] or
                    rational_tree_leaves(rec['tree']) != rec['leaves']):
                findings.append({'id': idx, 'reason': 'expression_tree_metadata_mismatch'})
            parents = rec.get('parents')
            if (not isinstance(parents, list) or
                    any(type(p) is not int or not 0 <= p < idx for p in parents)):
                findings.append({'id': idx, 'reason': 'invalid_parent_reference'})
            if rec.get('pathway') in _ZR_ARITHMETIC:
                rebuilt = _zr_reconstruct(m, idx, {
                    'tree': rec['tree'], 'pathway': rec['pathway'],
                    'parents': parents}, globals())
                if rebuilt is None or _zr_payload(rebuilt) != _zr_payload(rec):
                    findings.append({'id': idx, 'reason': 'construction_reexecution_mismatch'})
        except (KeyError, TypeError, ValueError, IndexError, ZeroDivisionError,
                OverflowError, RecursionError) as error:
            findings.append({'id': idx, 'reason': type(error).__name__})
    return {'records_checked': len(records), 'contradictions': findings}


def _za_promote(candidate_path, target_path, expected_source_sha256=None):
    """Validate before writing; preserve exact old bytes before atomic install."""
    sympy_module()  # Check the execution dependency before replacing memory.
    candidate_path = os.path.abspath(candidate_path)
    target_path = os.path.abspath(target_path)
    with open(candidate_path, 'rb') as stream:
        candidate_raw = stream.read()
    checked, report = _za_validate(candidate_path)
    with open(candidate_path, 'rb') as stream:
        current_candidate_raw = stream.read()
    if candidate_raw != current_candidate_raw:
        raise ZeroRecoveryPending('Candidate changed during validation; retry')
    backup = None
    if os.path.exists(target_path):
        with open(target_path, 'rb') as stream:
            original_raw = stream.read()
        digest = _zr_hashlib.sha256(original_raw).hexdigest()
        if expected_source_sha256 is not None and digest != expected_source_sha256:
            raise ZeroRecoveryPending('Source changed during recovery approval; retry')
        backup = target_path + '.pre-v478-' + digest + '.bak'
        try:
            with open(backup, 'xb') as stream:
                stream.write(original_raw)
                stream.flush()
                os.fsync(stream.fileno())
        except FileExistsError:
            with open(backup, 'rb') as stream:
                if stream.read() != original_raw:
                    raise ZeroRecoveryPending('Recovery backup differs; target unchanged')
        # Avoid replacing memory if it changed while being checked.
        with open(target_path, 'rb') as stream:
            if stream.read() != original_raw:
                raise ZeroRecoveryPending('Memory changed during approval; retry')
    body = checked.get('zero_body_recovery', {})
    checked['zero_resume'] = {
        'rule': 'verified_candidate_resume_v478', 'zero_nexus': 'Z0',
        'status': 'approved_for_execution', 'candidate_path': candidate_path,
        'candidate_sha256': _zr_hashlib.sha256(candidate_raw).hexdigest(),
        'backup_path': backup, 'records_checked': report['records_checked'],
        'expression_approval': 'exact_tree_and_supported_construction_reexecution',
        'original_recovery_verified': body.get('original_recovery_verified', False),
        'unresolved_historical_slots': [s['id'] for s in body.get('zero_slots', [])
                                         if s.get('status') == 'unknown'],
        'continuation_verified': False}
    # Keep unknown raw spans as evidence. Do not relabel them as recovered.
    _zn_checkpoint(target_path, checked)
    print('Recovery approved:', report['records_checked'],
          'rational expressions; archive links and foundation passed.')
    if backup:
        print('Previous memory preserved:', backup)
    print('Resuming engine in this run.', flush=True)
    return checked


def zero_approve_recovery(path, state):
    with open(path, 'rb') as stream:
        digest = _zr_hashlib.sha256(stream.read()).hexdigest()
    if state.get('source_sha256') != digest:
        raise ZeroRecoveryPending('Recovery candidate belongs to a different source')
    entries = [e for e in state.get('candidates', []) if e.get('archive_ready')]
    # Equivalent candidates are one operational choice; retain all raw evidence.
    candidates = {}
    for entry in entries:
        checked, _ = _za_validate(entry['path'])
        comparable = {k: v for k, v in checked.items() if k not in (
            'zero_body_recovery', 'zero_nexus_archive_attempts', 'zero_text_observation')}
        candidates.setdefault(_zr_digest(comparable), entry['path'])
    if len(candidates) != 1:
        raise ZeroRecoveryPending('Recovery needs one unambiguous validated candidate; found ' +
                                  str(len(candidates)))
    return _za_promote(next(iter(candidates.values())), path, digest)


_za_previous_save = save_memory

def save_memory(m):
    resume = m.get('zero_resume')
    if resume and not resume.get('continuation_verified'):
        # run() calls save after its bounded queue work and run summary update.
        resume['continuation_verified'] = True
        resume['status'] = 'resumed_and_saved'
        resume['saved_run_count'] = len(m.get('runs', []))
        try:
            _za_previous_save(m)
        except BaseException:
            resume['continuation_verified'] = False
            resume['status'] = 'approved_for_execution'
            raise
        print('Recovery continuation verified: engine run completed and saved.')
    else:
        _za_previous_save(m)


# ============================================================
# V4.7.9 - INDEPENDENT CHECKS AND EXECUTED ZERO FEEDBACK
# Scope: rational constructions, their result index and foundation.
# Other domains still require the existing whole-archive link audit.
# ============================================================

def _zv_exact(tree, m=None, legacy_leaves=()):
    """Independent calculator: no engine evaluate_tree/operate dispatch."""
    if not isinstance(tree, dict):
        raise ValueError('invalid_tree')
    if 'leaf' in tree:
        leaf = tree['leaf']
        if set(tree) == {'leaf', 'calculus_source'} and m is not None:
            value = _z5_calculus_constant(m, tree['calculus_source'])
            if value != number(leaf): raise ValueError('calculus_source_disagreement')
            return value, str(leaf), [leaf], 0
        if set(tree) == {'leaf', 'symbolic_source'} and m is not None:
            idx = tree['symbolic_source']
            if type(idx) is not int or not 0 <= idx < len(m.get('symbolic_archive', {}).get('expressions', [])):
                raise ValueError('invalid_symbolic_source')
            origin = m['symbolic_archive']['expressions'][idx]
            replay = _zv_symbolic(origin['construction'])
            if replay != symbolic_unpack(origin['exact']) or replay != number(leaf):
                raise ValueError('symbolic_source_disagreement')
            return number(leaf), str(leaf), [leaf], origin['depth']
        if set(tree) == {'leaf'} and number(leaf) in legacy_leaves:
            return number(leaf), str(leaf), [leaf], 0
        if set(tree) != {'leaf'} or type(leaf) is not int:
            raise ValueError('invalid_foundation_leaf')
        return Fraction(leaf), str(leaf), [leaf], 0
    if set(tree) != {'op', 'left', 'right'}:
        raise ValueError('invalid_tree_shape')
    a, ae, al, ad = _zv_exact(tree['left'], m, legacy_leaves)
    b, be, bl, bd = _zv_exact(tree['right'], m, legacy_leaves)
    op = tree['op']
    if op == '+': value = a + b
    elif op == '-': value = a - b
    elif op == '*': value = a * b
    elif op == '/': value = a / b
    else: raise ValueError('unsupported_operation')
    return value, '(' + ae + ' ' + op + ' ' + be + ')', al + bl, max(ad, bd) + 1


def _zv_symbolic(tree):
    if set(tree) == {'exact'}: return symbolic_unpack(tree['exact'])
    args = [_zv_symbolic(child) for child in tree['args']]
    op = tree['op']
    if op == 'sqrt' and len(args) == 1: return sympy_module().sqrt(args[0])
    if len(args) != 2: raise ValueError('symbolic_arity')
    a, b = args
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/' and b != 0: return a / b
    if op == '**': return a ** b
    raise ValueError('unsupported_symbolic_construction')


def _zv_seed_leaves(tree):
    if 'leaf' in tree: return [] if 'symbolic_source' in tree or 'calculus_source' in tree else [tree['leaf']]
    return _zv_seed_leaves(tree['left']) + _zv_seed_leaves(tree['right'])


def _zv_symbolic_lineage(m, idx, visiting=None):
    visiting = set() if visiting is None else visiting
    token = ('symbolic', idx)
    if token in visiting: raise ValueError('cyclic_symbolic_lineage')
    visiting = visiting | {token}
    rec = m['symbolic_archive']['expressions'][idx]
    result = {token}
    for parent in rec.get('parents', []):
        if type(parent) is not int or not 0 <= parent < idx:
            raise ValueError('invalid_symbolic_parent')
        result.update(_zv_symbolic_lineage(m, parent, visiting))
    # Imported rational/complex records are shared origins, not independence.
    for source in rec.get('sources', []):
        result.add((source['archive'], source['id']))
    return result


def _zv_bridge_sources(m, tree):
    if 'calculus_source' in tree: return {('calculus', tree['calculus_source'])}
    if 'symbolic_source' in tree: return _zv_symbolic_lineage(m, tree['symbolic_source'])
    if 'leaf' in tree: return set()
    return _zv_bridge_sources(m, tree['left']) | _zv_bridge_sources(m, tree['right'])


def _zv_observe(m):
    records = m.get('expressions', [])
    if not isinstance(records, list):
        raise ValueError('Expression archive must be a list')
    findings, calculated_index, ancestors, groups = [], {}, {}, {}
    legacy_calculus_leaves = {}
    foundation = m.get('foundation', {})
    states = foundation.get('states')
    foundation_ok = (isinstance(states, list) and bool(states) and
        all(type(n) is int and n == i for i, n in enumerate(states)) and
        foundation.get('rule') == 'foundation_state_count_v3' and
        [z.get('id') for z in foundation.get('zero_records', [])] ==
        ['Z%d' % i for i in range(len(states or []))])
    if not foundation_ok:
        findings.append({'id': None, 'reasons': ['foundation_uncertain']})
    manifest = m.get('zero_recovery', {}).get('manifest', {}).get('rational', {})
    for idx, rec in enumerate(records):
        reasons = []
        try:
            if not isinstance(rec, dict):
                raise ValueError('record_not_object')
            inherited = set()
            for parent in rec.get('parents', []):
                if type(parent) is int: inherited.update(legacy_calculus_leaves.get(parent, set()))
            if rec.get('pathway') == 'calculus_to_rational_v47' and set(rec['tree']) == {'leaf'}:
                refs = rec.get('sources', [])
                if len(refs) != 1 or refs[0].get('archive') != 'calculus':
                    raise ValueError('invalid_legacy_calculus_source')
                q = _z5_calculus_constant(m, refs[0]['id'])
                if q != number(rec['tree']['leaf']): raise ValueError('legacy_calculus_source_disagreement')
                inherited.add(q)
            legacy_calculus_leaves[idx] = inherited
            value, expression, leaves, depth = _zv_exact(rec['tree'], m, inherited)
            key = encode(value)
            calculated_index.setdefault(key, []).append(idx)
            if type(rec.get('id')) is not int or rec['id'] != idx:
                reasons.append('id_position_mismatch')
            if (rec.get('value'), rec.get('expr'), rec.get('leaves'), rec.get('depth')) != (
                    key, expression, leaves, depth):
                reasons.append('independent_calculator_metadata_disagreement')
            if not foundation_ok or any(n not in states and number(n) not in inherited for n in _zv_seed_leaves(rec['tree'])):
                reasons.append('unregistered_foundation_leaf')
            parents = rec.get('parents')
            if (not isinstance(parents, list) or
                    any(type(p) is not int or not 0 <= p < idx for p in parents)):
                reasons.append('invalid_parent_reference')
            else:
                # Only verified ancestor closures count as lineage evidence.
                closure = _zv_bridge_sources(m, rec['tree'])
                if rec.get('pathway') == 'calculus_to_rational_v47':
                    closure.add(('calculus', rec['sources'][0]['id']))
                for p in parents:
                    if p not in ancestors:
                        reasons.append('unverified_parent_lineage')
                    else:
                        closure.update(ancestors[p])
                        if records[p].get('parents'):
                            closure.add(('rational', p))
                if rec.get('pathway') in _ZR_ARITHMETIC:
                    rebuilt = _zr_reconstruct({'expressions': records}, idx,
                        {k: rec.get(k) for k in ('tree', 'parents', 'pathway')}, globals())
                    if rebuilt is None or _zr_payload(rebuilt) != _zr_payload(rec):
                        reasons.append('construction_reexecution_mismatch')
                elif not parents and rec.get('pathway') not in ('foundation_state_count_v3', 'symbolic_to_rational_v46', 'calculus_to_rational_v47'):
                    reasons.append('unsupported_parentless_construction')
                if rec.get('pathway') == 'foundation_state_count_v3' and (
                        parents or set(rec['tree']) != {'leaf'} or len(leaves) != 1):
                    reasons.append('invalid_foundation_construction')
                if rec.get('pathway') == 'calculus_to_rational_v47' and (
                        parents or set(rec['tree']) not in ({'leaf'}, {'leaf', 'calculus_source'}) or
                        len(rec.get('sources', [])) != 1 or rec['sources'][0].get('archive') != 'calculus' or
                        ('calculus_source' in rec['tree'] and rec['sources'][0]['id'] != rec['tree']['calculus_source'])):
                    reasons.append('invalid_calculus_embedding')
                if rec.get('pathway') == 'symbolic_to_rational_v46' and (
                        parents or set(rec['tree']) != {'leaf', 'symbolic_source'} or
                        rec.get('sources') != [{'archive': 'symbolic', 'id': rec['tree']['symbolic_source']}]):
                    reasons.append('invalid_symbolic_embedding')
                if not reasons:
                    ancestors[idx] = closure
                    if parents and not any(token[0] != 'rational' for token in closure):
                        groups.setdefault(key, []).append(idx)
            entry = manifest.get(str(idx))
            if entry and _zr_digest(_zr_payload(rec)) != entry.get('digest'):
                reasons.append('manifest_content_mismatch')
                ancestors.pop(idx, None)
                if idx in groups.get(key, []): groups[key].remove(idx)
        except (KeyError, TypeError, ValueError, IndexError, ZeroDivisionError,
                OverflowError, RecursionError, AttributeError) as exc:
            reasons.append('unverifiable_expression:' + type(exc).__name__)
        if reasons:
            findings.append({'id': idx, 'reasons': sorted(set(reasons))})
    if m.get('results') != calculated_index:
        findings.append({'id': None, 'reasons': ['results_index_mismatch']})
    correlations = []
    for value, ids in groups.items():
        if len(ids) < 2: continue
        # Shared seed leaves are explicit common axioms. Independence here
        # concerns recorded non-foundation construction ancestry only.
        pairs = []
        for offset, left in enumerate(ids):
            for right in ids[offset+1:]:
                if not ((ancestors[left] | {('rational', left)}) & (ancestors[right] | {('rational', right)})):
                    pairs.append([left, right])
                    if len(pairs) >= 20: break
            if len(pairs) >= 20: break
        correlations.append({'value': value, 'supporting_ids': ids,
            'disjoint_construction_pairs': pairs,
            'independence_scope': 'rational_non_foundation_ancestry; shared_axioms_allowed; cross_archive_excluded'})
    return {'schema': 1, 'rule': 'zero_double_verification_v479',
        'status': 'unresolved' if findings else 'arithmetic_consistent',
        'records_checked': len(records), 'contradictions': findings,
        'archive_correlations': correlations,
        'verified_lineage': [{'id': idx, 'construction_ancestors': sorted(closure)}
                             for idx, closure in ancestors.items()],
        'scope': 'rational_exact_arithmetic_metadata_manifest_lineage_index_foundation',
        'construction_replay_scope': list(_ZR_ARITHMETIC),
        'other_rational_pathways': sorted({r.get('pathway', 'unknown') for r in records if isinstance(r, dict) and r.get('pathway') not in _ZR_ARITHMETIC}),
        'historical_identity_proven': False}


def _zv_explore(m, state, budget):
    """Consume saved slots; retain rejected hypotheses and exact old records."""
    processed = 0
    while state['head'] < len(state['tasks']) and processed < budget:
        task = state['tasks'][state['head']]
        idx = task['id']
        attempts = []
        if task.get('archive', 'rational') != 'rational':
            task['status'] = 'unresolved'
            task.setdefault('attempts', []).append([{'status':'unresolved', 'reason':'typed_repair_not_implemented'}])
            task['executions'] = task.get('executions', 0) + 1
            state['head'] += 1
            processed += 1
            continue
        if type(idx) is int and 0 <= idx < len(m['expressions']):
            before = _zr_copy.deepcopy(m['expressions'][idx])
            report = zero_core(m, 'verification', operation='observe')
            invalid = {f['id'] for f in report['contradictions'] if type(f['id']) is int and f.get('archive', 'rational') == 'rational'}
            candidates = {}
            entry = m.get('zero_recovery', {}).get('manifest', {}).get('rational', {}).get(str(idx))
            recipes = []
            if entry and entry.get('recipe'):
                recipes.append(('manifest', entry['recipe']))
            legacy = _zr_legacy_recipe(m, idx)
            if legacy: recipes.append(('creation_event_and_key', legacy))
            for origin, recipe in recipes:
                evidence = {'origin': origin, 'recipe': _zr_copy.deepcopy(recipe)}
                parents = recipe.get('parents', [])
                if not isinstance(parents, list) or any(type(p) is not int or p in invalid for p in parents):
                    evidence['status'] = 'unverified_parent'; attempts.append(evidence); continue
                try:
                    rebuilt = _zr_reconstruct(m, idx, recipe, globals())
                    if rebuilt is None:
                        raise ValueError('unsupported_or_inconsistent_recipe')
                    q, expr, leaves, depth = _zv_exact(rebuilt['tree'], m)
                    if (encode(q), expr, leaves, depth) != (
                            rebuilt['value'], rebuilt['expr'], rebuilt['leaves'], rebuilt['depth']):
                        raise ValueError('independent_check_failed')
                    if entry and _zr_digest(_zr_payload(rebuilt)) != entry['digest']:
                        raise ValueError('manifest_disagreement')
                    # Restore passage identity, preserving existing metadata.
                    rebuilt['zero_core_passage'] = _zr_copy.deepcopy(before.get('zero_core_passage', {
                        'rule': ZERO_CORE_RULE, 'archive': 'rational', 'id': idx,
                        'zero_nexus': 'Z0', 'historical_backfill': False,
                        'effect': 'identity_preserves_construction'}))
                    if 'unified_value_key' in before:
                        sp = sympy_module()
                        rebuilt['unified_value_key'] = exact_lookup_key(sp.Rational(q.numerator, q.denominator))
                    candidates[_zr_digest(_zr_payload(rebuilt))] = rebuilt
                    evidence['status'] = 'supported_candidate'
                except (ValueError, KeyError, TypeError, IndexError, ZeroDivisionError) as exc:
                    evidence.update(status='rejected', reason=str(exc))
                attempts.append(evidence)
            if len(candidates) == 1:
                rebuilt = next(iter(candidates.values()))
                m['expressions'][idx] = rebuilt
                task.update(status='reexecuted', before=before, after=_zr_copy.deepcopy(rebuilt))
            else:
                task['status'] = 'ambiguous' if candidates else 'unresolved'
        elif task['reasons'] == ['results_index_mismatch']:
            report = zero_core(m, 'verification', operation='observe')
            if not any(type(f['id']) is int and f.get('archive', 'rational') == 'rational' for f in report['contradictions']):
                index = {}
                for rec in m['expressions']:
                    key = encode(_zv_exact(rec['tree'], m)[0])
                    index.setdefault(key, []).append(rec['id'])
                task.update(status='reexecuted', before=_zr_copy.deepcopy(m.get('results')), after=index)
                m['results'] = index
            else: task['status'] = 'unresolved'
        else: task['status'] = 'unresolved'
        task.setdefault('attempts', []).append(attempts)
        task['executions'] = task.get('executions', 0) + 1
        state['head'] += 1
        processed += 1
    return processed


_zv_previous_core = zero_core

def zero_core(m, domain, *, operation=None, operands=(), **kwargs):
    if domain == 'verification':
        if operation == 'observe': return _zv_observe(m)
        if operation == 'explore': return _zv_explore(m, operands[0], operands[1])
        raise ValueError('Unsupported verification operation')
    return _zv_previous_core(m, domain, operation=operation, operands=operands, **kwargs)


def zero_verify_candidate(candidate_path, budget=None):
    """Execute feedback on an isolated copy; checkpoint all unresolved slots."""
    if budget is not None and (type(budget) is not int or budget < 1):
        raise ValueError('Positive work budget required')
    with open(candidate_path, 'rb') as stream: raw = stream.read()
    source = _zt_parse(raw.decode('utf-8'))
    if source.get('schema') != 1 or source.get('version') != VERSION:
        raise ValueError('Candidate schema/version incompatible')
    digest = _zr_hashlib.sha256(raw).hexdigest()
    state_path = str(candidate_path) + '.zero-verification-search.json'
    state = None
    if os.path.exists(state_path):
        with open(state_path, encoding='utf-8') as stream: previous = json.load(stream)
        if previous.get('source_sha256') == digest and previous.get('rule') == 'zero_verification_worker_v479':
            state = previous
    if state is None:
        initial = zero_core(source, 'verification', operation='observe')
        state = {'schema': 1, 'rule': 'zero_verification_worker_v479', 'zero_nexus': 'Z0',
            'source_sha256': digest, 'working_memory': _zr_copy.deepcopy(source),
            'initial_observation': initial, 'head': 0, 'passes': 0,
            'tasks': [dict(f, status='pending', zero_nexus='Z0') for f in initial['contradictions']]}
    m = state['working_memory']
    # Revisit retained dead ends on a later call; do not erase earlier attempts.
    if state['head'] >= len(state['tasks']) and state['tasks']:
        remaining = zero_core(m, 'verification', operation='observe')['contradictions']
        state['tasks'].extend(dict(f, status='pending', zero_nexus='Z0') for f in remaining)
    state['passes'] += 1
    processed = 0
    try:
        while state['head'] < len(state['tasks']):
            chunk = 32 if budget is None else min(32, budget - processed)
            if chunk <= 0: break
            processed += zero_core(m, 'verification', operation='explore', operands=(state, chunk))
            _zn_checkpoint(state_path, state)
            if state['head'] < len(state['tasks']):
                print('Zero verification checkpoint:', state['head'], '/', len(state['tasks']), flush=True)
    except BaseException:
        _zn_checkpoint(state_path, state)
        raise
    report = zero_core(m, 'verification', operation='observe')
    report.update(candidate=str(candidate_path), candidate_sha256=digest,
        executed_this_pass=processed, executed_total=sum(t.get('executions', 0) for t in state['tasks']),
        zero_feedback=state['tasks'], continuation_verified=False,
        status='unresolved' if report['contradictions'] else 'arithmetic_consistent')
    if not report['contradictions']:
        output = str(candidate_path) + '.zero-verified-candidate.json'
        _zn_checkpoint(output, m)
        try:
            _za_validate(output)
        except (ValueError, KeyError, TypeError, IndexError, RuntimeError) as exc:
            report.update(status='archive_validation_pending', archive_issue=str(exc))
        else:
            report.update(status='candidate_ready', validated_candidate=output)
    state['last_report'] = {k: v for k, v in report.items() if k != 'zero_feedback'}
    _zn_checkpoint(state_path, state)
    _zn_checkpoint(str(candidate_path) + '.verification.json', report)
    print('Zero verification:', report['status'], '| executed:', processed,
          '| contradictions:', len(report['contradictions']))
    if report.get('validated_candidate'): print('Verified candidate:', report['validated_candidate'])
    return report


_zv_previous_run = run

def run():
    path = memory_path()
    if os.path.exists(path):
        try:
            with open(path, encoding='utf-8') as stream: m = _zt_parse(stream.read())
        except (ValueError, UnicodeError):
            pass  # Existing whole-body text recovery owns syntax damage.
        else:
            report = zero_core(m, 'verification', operation='observe')
            if report['contradictions']:
                result = zero_verify_candidate(path)
                print('Verification feedback executed; source preserved. Status:', result['status'])
                print('Use --resume-candidate with the verified candidate after review.')
                return
    return _zv_previous_run()


_zv_previous_save = save_memory

def save_memory(m):
    report = zero_core(m, 'verification', operation='observe')
    if report['contradictions']:
        proposal = memory_path() + '.zero-verification-run-proposal.json'
        _zn_checkpoint(proposal, {k:v for k,v in m.items() if not k.startswith('_')})
        zero_verify_candidate(proposal)
        raise ZeroRecoveryPending('Run verification returned contradictions to Z0; normal memory preserved. Proposal: ' + proposal)
    return _zv_previous_save(m)


# ============================================================
# V4.7.10 - MEASURED ADAPTIVE RECOVERY / NEW-LINEAGE REGENERATION
# ============================================================
ADAPTIVE_RECOVERY_ENABLED = True
ADAPTIVE_TARGET_RECORDS = 128  # Operational floor when no trusted count survives.
ADAPTIVE_MAX_CYCLES = 8       # Persisted trial budget; later invocations continue.
ADAPTIVE_REPAIR_SECONDS = 2.0
ADAPTIVE_REGENERATION_MARGIN = 0.80


def _zg_read(path):
    with open(path, encoding='utf-8') as stream:
        return _zt_parse(stream.read())


def _zg_identity(rec):
    return _zr_digest([rec.get('pathway'), rec.get('tree')])


def _zg_rules():
    """Check the supplied executable rules independently of damaged memory."""
    sympy_module()
    examples = ((Fraction(0), '+', Fraction(1), Fraction(1)),
                (Fraction(2), '-', Fraction(3), Fraction(-1)),
                (Fraction(2, 3), '*', Fraction(3, 4), Fraction(1, 2)),
                (Fraction(1), '/', Fraction(2), Fraction(1, 2)),
                (Fraction(1), '/', Fraction(0), None))
    for a, op, b, expected in examples:
        if zero_core(None, 'rational', operation=op, operands=(a, b)) != expected:
            raise ZeroRecoveryPending('Executable rational rule check failed: ' + op)
    for states in ([0], [0, 1], [0, 1, 2]):
        if zero_core(None, 'foundation', operation='registered_state_count', operands=(states,)) != len(states):
            raise ZeroRecoveryPending('Executable foundation rule check failed')
    return {'status': 'pass', 'rational_examples': len(examples),
            'foundation_examples': 3, 'scope': 'supplied_rules; no authentication_of_source_code'}


def _zg_check(path):
    checked, _ = _za_validate(path)
    observation = zero_core(checked, 'verification', operation='observe')
    if observation['contradictions']:
        raise ZeroRecoveryPending('Independent adaptive check failed: ' + str(observation['contradictions'][:3]))
    return checked


def _zg_cycle(path):
    """One real noninteractive engine run, with the normal load/save gates."""
    import contextlib
    import io
    previous_path = memory_path
    before = _zg_check(path)
    old_runs = len(before.get('runs', []))
    old_records = {d: [_zr_digest(_zr_payload(r)) for r in _zr_records(before, d)] for d in _ZR_DOMAINS}
    old_core_operations = sum(sum(v.values()) for v in before.get('zero_core', {}).get('operation_passages', {}).values())
    output = io.StringIO()
    globals()['memory_path'] = lambda: path
    try:
        with contextlib.redirect_stdout(output):
            _zg_engine_cycle(interactive=False)
    finally:
        globals()['memory_path'] = previous_path
        with open(path + '.cycle.log', 'a', encoding='utf-8') as stream:
            stream.write(output.getvalue())
    after = _zg_check(path)
    if len(after.get('runs', [])) != old_runs + 1:
        raise ZeroRecoveryPending('Adaptive continuation did not complete and save one run')
    for domain, prefix in old_records.items():
        actual = [_zr_digest(_zr_payload(r)) for r in _zr_records(after, domain)[:len(prefix)]]
        if actual != prefix:
            raise ZeroRecoveryPending('Adaptive continuation altered existing constructions: ' + domain)
    operations = sum(sum(v.values()) for v in after.get('zero_core', {}).get('operation_passages', {}).values())
    return after, {'queue_tasks': sum(after['runs'][-1]['processed'].values()),
        'rational_records_added': len(after['expressions']) - len(before['expressions']),
        'archive_records_added': sum(len(_zr_records(after, d))-len(old_records[d]) for d in _ZR_DOMAINS),
        'zero_core_operations': operations - old_core_operations,
        'archive_link_issues': 0, 'independent_rational_contradictions': 0,
        'saved_run': len(after['runs']), 'prefix_preserved': True}


def _zg_checkpoint(state, root):
    _zn_checkpoint(os.path.join(root, 'state.json'), state)


def _zg_trial_paths(root, branch):
    folder = os.path.join(root, branch)
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, MEMORY_FILENAME)


def _zg_install_trial(state, branch, path, memory):
    memory = _zr_copy.deepcopy(memory)
    memory['zero_adaptive_lineage'] = {
        'rule': 'adaptive_lineage_v4710', 'zero_nexus': 'Z0',
        'branch': branch, 'source_sha256': state['source_sha256'],
        'source_snapshot': state['source_snapshot'],
        'historical_restoration': False,
        'history_status': ('new_emergence_from_Z0' if branch == 'regeneration' else
                          'survivors_and_evidence_supported_reconstruction'),
        'baseline_used_as_repair_evidence': False}
    _zn_checkpoint(path, memory)
    _zg_check(path)


def _zg_recover(state, root, seconds, max_feedback_batches=None, feedback_budget=32, retry_input_path=None):
    """Only surviving source evidence participates; the baseline is withheld."""
    import contextlib
    import io
    branch = state['trials']['recovery']
    path = _zg_trial_paths(root, 'recovery')
    branch['memory_path'] = path
    if os.path.exists(path):
        try:
            _zg_check(path)
            return
        except (ValueError, KeyError, TypeError, IndexError):
            branch['status'] = 'unresolved'
            branch['reason'] = 'Existing recovery checkpoint failed validation; preserved for inspection'
            return
    input_path = os.path.join(os.path.dirname(path), 'source-input.json')
    with open(state['source_snapshot'], 'rb') as stream: raw = stream.read()
    if not os.path.exists(input_path):
        temporary = input_path + '.tmp'
        with open(temporary, 'wb') as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
        os.replace(temporary, input_path)
    else:
        with open(input_path, 'rb') as stream:
            if stream.read() != raw:
                branch.update(status='unresolved', reason='Recovery trial input changed; preserved for inspection')
                return
    branch['repair_slice_seconds'] = seconds
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            try:
                parsed = _zg_read(retry_input_path or input_path)
            except (ValueError, UnicodeError, RecursionError):
                with open(input_path, encoding='utf-8') as stream: text = stream.read()
                body = _zw_recover(input_path, text, seconds)
                branch['recovery_search_status'] = body.get('status')
                candidates = {}
                for entry in body.get('candidates', []):
                    if not entry.get('archive_ready'): continue
                    try: checked = _zg_check(entry['path'])
                    except (ValueError, KeyError, TypeError, IndexError): continue
                    comparable = {k:v for k,v in checked.items() if k not in (
                        'zero_body_recovery', 'zero_nexus_archive_attempts', 'zero_text_observation')}
                    candidates[_zr_digest(comparable)] = checked
                if len(candidates) != 1:
                    branch.update(status='unresolved', reason='No unique verified whole-body candidate')
                    return
                parsed = next(iter(candidates.values()))
            checked, ready = zero_core(parsed, 'errors', operation='recover_archive')
            if ready:
                observation = zero_core(checked, 'verification', operation='observe')
                if not observation['contradictions']:
                    _zg_install_trial(state, 'recovery', path, checked)
                    branch['reconstructed_records'] = sum(e.get('status') == 'recovered'
                        for e in checked.get('zero_recovery', {}).get('events', []))
                    return
            # Preserve every partial reconstruction and unknown slot. A blocked
            # proposal is evidence only; a pending normalized archive can feed
            # the task-2 worker without renumbering surviving constructions.
            proposal_path = input_path + '.preflight-proposal.json'
            _zn_checkpoint(proposal_path, checked)
            branch['preflight_proposal'] = proposal_path
            branch['reconstructed_records'] = sum(e.get('status') == 'recovered'
                for e in checked.get('zero_recovery', {}).get('events', []))
            feedback_path = proposal_path if checked.get('zero_recovery', {}).get('status') == 'pending' else input_path
            branch['feedback_checkpoint'] = feedback_path + '.zero-verification-search.json'
            started = time.perf_counter()
            batches = 0
            while True:
                report = zero_verify_candidate(feedback_path, budget=feedback_budget)
                batches += 1
                branch['verification_feedback_executed'] = report['executed_total']
                if report.get('validated_candidate'):
                    checked = _zg_check(report['validated_candidate'])
                    _zg_install_trial(state, 'recovery', path, checked)
                    return
                continuation = _zg_read(feedback_path + '.zero-verification-search.json')
                if continuation['head'] >= len(continuation['tasks']): break
                if time.perf_counter() - started >= seconds: break
                if max_feedback_batches is not None and batches >= max_feedback_batches: break
            branch.update(status='unresolved', reason='Evidence replay has pending or unsupported slots; checkpoints retained')
    except (ValueError, KeyError, TypeError, IndexError, UnicodeError, RecursionError) as exc:
        branch.update(status='unresolved', reason=str(exc))
    finally:
        with open(input_path + '.recovery.log', 'a', encoding='utf-8') as stream:
            stream.write(buffer.getvalue())


def _zg_regenerate(state, root):
    path = _zg_trial_paths(root, 'regeneration')
    state['trials']['regeneration']['memory_path'] = path
    if not os.path.exists(path):
        # No records, trees, keys, queues or rules are copied from the source.
        memory = empty_memory()
        if memory['foundation']['states'] != [0] or len(memory['expressions']) != 1:
            raise ZeroRecoveryPending('Regeneration did not begin at the Z0 foundation')
        _zg_install_trial(state, 'regeneration', path, memory)
    else:
        _zg_check(path)


def _zg_advance(state, root, branch_name, max_cycles):
    branch = state['trials'][branch_name]
    path = branch.get('memory_path')
    if not path or not os.path.exists(path): return
    memory = _zg_check(path)
    branch.setdefault('initial_run_count', len(memory.get('runs', [])))
    cycle_count = 0
    while cycle_count < max_cycles:
        # Mark the goal boundary before the continuation test, even on restart.
        if branch.get('goal_boundary_run') is None and len(memory['expressions']) >= state['target_records']:
            branch['goal_boundary_run'] = len(memory.get('runs', []))
            branch['goal_boundary_records'] = len(memory['expressions'])
            _zg_checkpoint(state, root)
        if (branch.get('goal_boundary_run') is not None and
                len(memory.get('runs', [])) > branch['goal_boundary_run']):
            branch.update(status='ready', continuation_verified=True,
                          records=len(memory['expressions']), saved_runs=len(memory['runs']),
                          completed_engine_runs=len(memory['runs'])-branch['initial_run_count'],
                          cycle_metrics_complete=len(branch['cycles']) == len(memory['runs'])-branch['initial_run_count'])
            return
        memory, metric = _zg_cycle(path)
        branch.setdefault('cycles', []).append(metric)
        branch['records'] = len(memory['expressions'])
        cycle_count += 1
        branch['status'] = 'exploring'
        _zg_checkpoint(state, root)
        print('Zero adaptive:', branch_name, '| saved runs:', len(memory['runs']),
              '| rational records:', len(memory['expressions']), '| checkpoint saved', flush=True)
    if branch.get('goal_boundary_run') is None and len(memory['expressions']) >= state['target_records']:
        branch['goal_boundary_run'] = len(memory.get('runs', []))
        branch['goal_boundary_records'] = len(memory['expressions'])
    if (branch.get('goal_boundary_run') is not None and
            len(memory.get('runs', [])) > branch['goal_boundary_run']):
        branch.update(status='ready', continuation_verified=True,
                      records=len(memory['expressions']), saved_runs=len(memory['runs']),
                          completed_engine_runs=len(memory['runs'])-branch['initial_run_count'],
                          cycle_metrics_complete=len(branch['cycles']) == len(memory['runs'])-branch['initial_run_count'])
    else:
        branch.update(status='budget_checkpoint', continuation_verified=False)


def _zg_select(trials, lost_fraction):
    recovery, regeneration = trials['recovery'], trials['regeneration']
    rready, gready = recovery.get('status') == 'ready', regeneration.get('status') == 'ready'
    if rready and gready:
        # A loss checkpoint opens the measured comparison; it is not a reset rule.
        if (lost_fraction is not None and lost_fraction >= 0.5 and
                regeneration['elapsed_seconds'] < recovery['elapsed_seconds'] * ADAPTIVE_REGENERATION_MARGIN):
            return 'regeneration', 'operational_goal_met_with_measured_cost_advantage_at_loss_checkpoint'
        return 'recovery', 'verified_recovery_preferred_without_clear_regeneration_cost_advantage'
    if rready: return 'recovery', 'only_recovery_completed_verified_continuation'
    if gready: return 'regeneration', 'recovery_unresolved; verified_new_lineage_available'
    return None, 'trials_pending; retain_checkpoints'


_zg_previous_core = zero_core

def zero_core(m, domain, *, operation=None, operands=(), **kwargs):
    if domain == 'adaptive':
        if operation == 'validate_rules': return _zg_rules()
        if operation == 'recover': return _zg_recover(*operands)
        if operation == 'regenerate': return _zg_regenerate(*operands)
        if operation == 'advance': return _zg_advance(*operands)
        if operation == 'select': return _zg_select(*operands)
        raise ValueError('Unsupported adaptive zero operation')
    return _zg_previous_core(m, domain, operation=operation, operands=operands, **kwargs)


def zero_adaptive_recovery(candidate_path, baseline_path=None, *, max_cycles=ADAPTIVE_MAX_CYCLES,
                           target_records=None, recovery_seconds=None):
    """Benchmark isolated trials to a declared operational floor, then continue.

    Regeneration creates a new lineage. A baseline is used only to measure
    missing constructions and set a capability target, never as repair input.
    Both original input files remain byte-for-byte unchanged.
    """
    candidate_path = os.path.abspath(candidate_path)
    if type(max_cycles) is not int or max_cycles < 1: raise ValueError('Positive cycle budget required')
    if recovery_seconds is None:
        recovery_seconds = _ZW_SECONDS if _ZW_SECONDS is not None else ADAPTIVE_REPAIR_SECONDS
    if recovery_seconds <= 0: raise ValueError('Positive recovery time allowance required')
    if target_records is not None and (type(target_records) is not int or target_records < 1):
        raise ValueError('Positive target record count required')
    with open(candidate_path, 'rb') as stream: raw = stream.read()
    if len(raw) > _ZT_MAX_BYTES:
        # A valid grown archive is also a permitted adaptive source. The
        # damaged-text repair budget still applies to malformed sources.
        try:
            _za_validate(candidate_path)
        except (ValueError, UnicodeError, RecursionError, KeyError, TypeError,
                IndexError, AttributeError) as exc:
            raise ZeroRecoveryPending(
                'Large adaptive source failed validation; source unchanged: ' + str(exc)) from exc
    digest = _zr_hashlib.sha256(raw).hexdigest()
    rule_check = zero_core(None, 'adaptive', operation='validate_rules')
    try: source = _zt_parse(raw.decode('utf-8'))
    except (ValueError, UnicodeError, RecursionError): source = None
    if source is not None and (not isinstance(source, dict) or source.get('schema') != 1 or source.get('version') != VERSION):
        raise ValueError('Adaptive input must be compatible engine memory or its damaged text')
    # Resume a previously declared comparison without requiring phone users
    # to enter the intact-baseline argument again after an interruption.
    prior_state_path = os.path.join(candidate_path + '.adaptive-work', digest, 'state.json')
    if baseline_path is None and os.path.exists(prior_state_path):
        prior = _zg_read(prior_state_path)
        if prior.get('rule') == 'zero_adaptive_v4710' and prior.get('source_sha256') == digest:
            baseline_path = prior.get('baseline')
    baseline = None; baseline_digest = None; expected = None
    if baseline_path:
        baseline_path = os.path.abspath(baseline_path)
        if os.path.samefile(candidate_path, baseline_path): raise ValueError('Baseline must differ from candidate')
        baseline = _zg_check(baseline_path)
        with open(baseline_path, 'rb') as stream: baseline_digest = _zr_hashlib.sha256(stream.read()).hexdigest()
        expected = {_zg_identity(rec) for rec in baseline['expressions']}
    present = ({_zg_identity(rec) for rec in source.get('expressions', []) if isinstance(rec, dict)}
               if isinstance(source, dict) and isinstance(source.get('expressions'), list) else None)
    missing = len(expected-present) if expected is not None and present is not None else None
    loss = missing/len(expected) if expected and missing is not None else None
    root = os.path.join(candidate_path + '.adaptive-work', digest)
    os.makedirs(root, exist_ok=True)
    snapshot = os.path.join(root, 'source.snapshot')
    try:
        with open(snapshot, 'xb') as stream:
            stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    except FileExistsError:
        with open(snapshot, 'rb') as stream:
            if stream.read() != raw: raise ZeroRecoveryPending('Adaptive source snapshot differs')
    state_path = os.path.join(root, 'state.json')
    if os.path.exists(state_path):
        state = _zg_read(state_path)
        if (state.get('source_sha256') != digest or state.get('rule') != 'zero_adaptive_v4710' or
                state.get('baseline_sha256') != baseline_digest or
                (target_records is not None and target_records != state.get('target_records'))):
            raise ZeroRecoveryPending('Adaptive inputs or target changed; retain existing trial and use a separate test copy')
    else:
        manifest_count = source.get('zero_recovery', {}).get('next_ids', {}).get('rational') if isinstance(source, dict) else None
        count = len(baseline['expressions']) if baseline is not None else (
            manifest_count if type(manifest_count) is int and manifest_count > 0 else ADAPTIVE_TARGET_RECORDS)
        state = {'schema': 1, 'rule': 'zero_adaptive_v4710', 'zero_nexus': 'Z0',
            'source_sha256': digest, 'source_snapshot': snapshot, 'source': candidate_path,
            'baseline': baseline_path, 'baseline_sha256': baseline_digest,
            'target_records': target_records or count,
            'target_source': 'explicit' if target_records else ('baseline' if baseline is not None else
                             'surviving_manifest' if count == manifest_count else 'configured_default'),
            'missing_unique_constructions': missing, 'lost_fraction': loss,
            'goal': 'resume_verified_exploration_after_rational_record_floor',
            'trials': {name: {'status': 'pending', 'elapsed_seconds': 0.0, 'cycles': []}
                       for name in ('recovery', 'regeneration')}}
    state['rule_check'] = rule_check
    state['status'] = 'benchmarking'
    _zg_checkpoint(state, root)
    try:
        for name, operation, args in (
                ('recovery', 'recover', (state, root, recovery_seconds)),
                ('regeneration', 'regenerate', (state, root))):
            branch = state['trials'][name]
            if branch.get('status') == 'ready': continue
            started = time.perf_counter()
            try:
                zero_core(None, 'adaptive', operation=operation, operands=args)
                zero_core(None, 'adaptive', operation='advance', operands=(state, root, name, max_cycles))
            except (ValueError, KeyError, TypeError, IndexError, UnicodeError, RecursionError) as exc:
                branch.update(status='unresolved', reason=str(exc))
            finally:
                branch['elapsed_seconds'] += time.perf_counter() - started
                _zg_checkpoint(state, root)
    except KeyboardInterrupt:
        state['status'] = 'interrupted_checkpoint_saved'
        _zg_checkpoint(state, root)
        print('Adaptive recovery interrupted; source preserved and trial checkpoints saved.')
        return state
    selected, reason = zero_core(None, 'adaptive', operation='select', operands=(state['trials'], state['lost_fraction']))
    state.update(selected_branch=selected, decision_reason=reason,
                 status='selected_and_resumed' if selected else 'pending',
                 original_source_preserved=True, historical_identity_proven=False,
                 new_lineage=(selected == 'regeneration'))
    # Detect input changes before activating any branch.
    with open(candidate_path, 'rb') as stream:
        if stream.read() != raw: raise ZeroRecoveryPending('Source changed during trials; no branch activated')
    if baseline_path:
        with open(baseline_path, 'rb') as stream:
            if _zr_hashlib.sha256(stream.read()).hexdigest() != baseline_digest:
                raise ZeroRecoveryPending('Baseline changed during trials; no branch activated')
    if selected:
        path = _zg_trial_paths(root, selected)
        selected_memory = _zg_check(path)
        selected_ids = {_zg_identity(rec) for rec in selected_memory['expressions']}
        state['selected_missing_baseline_constructions'] = len(expected-selected_ids) if expected is not None else None
        state['active_memory'] = path
        _zn_checkpoint(candidate_path + '.adaptive-active.json', {
            'rule': 'adaptive_active_v4710', 'source_sha256': digest, 'branch': selected,
            'new_lineage': selected == 'regeneration'})
    _zg_checkpoint(state, root)
    report_path = candidate_path + '.adaptive-report.json'
    _zn_checkpoint(report_path, state)
    print('Zero adaptive:', state['status'], '| branch:', selected or 'none')
    for name, branch in state['trials'].items():
        print(' ', name, '|', branch['status'], '| seconds:', round(branch['elapsed_seconds'], 4),
              '| saved cycles:', len(branch['cycles']), '| rational records:', branch.get('records', 0))
    if selected:
        print('Active memory:', state['active_memory'])
        print('New lineage from Z0.' if state['new_lineage'] else 'Surviving archive lineage retained with supported repairs.')
        print('Continuation verified; rerun normally to continue this branch.')
    print('Source preserved. Report:', report_path)
    return state


_zg_previous_run = run

def run():
    path = memory_path()
    if not os.path.exists(path): return _zg_previous_run()
    with open(path, 'rb') as stream: raw = stream.read()
    digest = _zr_hashlib.sha256(raw).hexdigest()
    active_path = path + '.adaptive-active.json'
    if os.path.exists(active_path):
        active = _zg_read(active_path)
        if active.get('rule') == 'adaptive_active_v4710' and active.get('source_sha256') == digest:
            branch = active.get('branch')
            if branch not in ('recovery', 'regeneration'):
                raise ZeroRecoveryPending('Invalid adaptive active branch')
            root = os.path.join(path + '.adaptive-work', digest)
            chosen = _zg_trial_paths(root, branch)
            selected_memory = _zg_check(chosen)
            if branch == 'regeneration' and RECOVERY_RETRY_ENABLED:
                try:
                    zero_core(None, 'recovery_feedback', operation='retry', operands=(path, chosen, selected_memory))
                except (ValueError, OSError, RuntimeError, KeyError, TypeError, IndexError) as exc:
                    print('Zero recovery retry deferred:', str(exc), '| regeneration continues.')
            print('Continuing adaptive', branch, 'branch:', chosen)
            previous = memory_path
            globals()['memory_path'] = lambda: chosen
            try: return _zg_previous_run()
            finally: globals()['memory_path'] = previous
    if ADAPTIVE_RECOVERY_ENABLED:
        try:
            m = _zt_parse(raw.decode('utf-8'))
            observation = zero_core(m, 'verification', operation='observe')
            damaged = bool(observation['contradictions'])
            if not damaged:
                _zg_check(path)  # Include non-rational manifest/link failures.
        except (ValueError, UnicodeError, KeyError, TypeError, IndexError, RecursionError, AttributeError):
            damaged = True
        if damaged:
            return zero_adaptive_recovery(path)
    return _zg_previous_run()


# ============================================================
# V4.7.11 - VERIFY SURVIVING RECOVERY RECIPES AGAINST THEIR RECORDS
# A contradictory recipe stays evidence, even if its record is intact.
# ============================================================

def _z4_manifest_findings(m):
    findings = []
    records = m.get('expressions', [])
    manifest = m.get('zero_recovery', {}).get('manifest', {}).get('rational', {})
    for rec in records:
        if not isinstance(rec, dict) or 'tree' not in rec:
            continue  # Missing records remain recovery slots, not known recipes.
        idx = rec.get('id')
        entry = manifest.get(str(idx))
        if not isinstance(entry, dict) or 'recipe' not in entry:
            continue
        expected = {key: _zr_copy.deepcopy(rec[key]) for key in ('tree', 'pathway', 'parents') if key in rec}
        if rec.get('pathway','').startswith('zero_connected_repeat_add_v1_src_'):
            expected['execution']=_zr_copy.deepcopy(rec['execution'])
        if entry['recipe'] != expected:
            findings.append({'id': idx, 'reasons': ['manifest_recipe_record_disagreement']})
    return findings


_z4_previous_observe = _zv_observe

def _zv_observe(m):
    report = _z4_previous_observe(m)
    report['contradictions'].extend(_z4_manifest_findings(m))
    if report['contradictions']:
        report['status'] = 'unresolved'
    report['recipe_consistency_rule'] = 'manifest_recipe_record_consistency_v4711'
    return report


_z4_previous_approval_verify = _za_verify_memory

def _za_verify_memory(m):
    report = _z4_previous_approval_verify(m)
    report['contradictions'].extend(
        {'id': f['id'], 'reason': f['reasons'][0]} for f in _z4_manifest_findings(m))
    return report


# ============================================================
# V4.7.12 - INDEPENDENT TYPED DOMAIN REPLAY
# Read-only checks: Fraction formulas are separate from exploration kernels.
# Symbolic replay uses the shared SymPy backend; it is not a formal proof system.
# ============================================================

class _Z5Replay:
    def __init__(self, memory):
        self.m = memory
        self.cache, self.active, self.errors = {}, set(), {}
        self.legacy_calculus = []
        self.legacy_leaves = {}

    @staticmethod
    def require(condition, reason):
        if not condition:
            raise ValueError(reason)

    def record(self, domain, idx):
        self.require(domain in _ZR_DOMAINS and type(idx) is int, 'invalid_typed_reference')
        records = _zr_records(self.m, domain)
        self.require(0 <= idx < len(records), 'missing_typed_reference')
        rec = records[idx]
        self.require(type(rec.get('id')) is int and rec['id'] == idx, 'id_position_mismatch')
        return rec

    def source(self, ref):
        self.require(isinstance(ref, dict) and set(ref) == {'archive', 'id'}, 'invalid_source')
        return self.get(ref['archive'], ref['id'])

    def get(self, domain, idx):
        self.require(isinstance(domain, str) and domain in _ZR_DOMAINS and type(idx) is int, 'invalid_typed_reference')
        token = (domain, idx)
        if token in self.cache:
            return self.cache[token]
        self.require(token not in self.active, 'cyclic_typed_lineage')
        if token in self.errors:
            raise ValueError('unverified_dependency:%s:%s' % token)
        self.active.add(token)
        try:
            rec = self.record(domain, idx)
            parents = rec.get('parents')
            self.require(isinstance(parents, list) and all(
                type(p) is int and 0 <= p < idx for p in parents), 'invalid_parent_reference')
            values = [self.get(domain, p) for p in parents]
            refs = rec.get('sources', [])
            self.require(isinstance(refs, list), 'invalid_sources')
            sources = [self.source(ref) for ref in refs]
            value = getattr(self, domain)(rec, values, sources)
            self.cache[token] = value
            return value
        except (ValueError, KeyError, TypeError, IndexError, ZeroDivisionError,
                OverflowError, RecursionError, AttributeError) as exc:
            self.errors[token] = str(exc) or type(exc).__name__
            raise ValueError(self.errors[token]) from exc
        finally:
            self.active.discard(token)

    @staticmethod
    def arithmetic(a, op, b):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/' and b != 0: return a / b
        raise ValueError('undefined_or_unsupported_operation')

    def rational_tree(self, tree, allowed=()):
        if 'leaf' in tree:
            if set(tree) == {'leaf', 'calculus_source'}:
                coeff = self.get('calculus', tree['calculus_source'])
                self.require(len(coeff) == 1 and coeff[0] == Fraction(str(tree['leaf'])),
                             'calculus_bridge_disagreement')
                return coeff[0]
            if set(tree) == {'leaf', 'symbolic_source'}:
                value = self.get('symbolic', tree['symbolic_source'])
                q = Fraction(str(tree['leaf']))
                self.require(value == self.spq(q), 'symbolic_bridge_disagreement')
                return q
            if set(tree) == {'leaf'} and Fraction(str(tree['leaf'])) in allowed:
                return Fraction(str(tree['leaf']))
            self.require(set(tree) == {'leaf'} and type(tree['leaf']) is int,
                         'invalid_foundation_leaf')
            self.require(tree['leaf'] in self.m['foundation']['states'], 'unregistered_foundation_leaf')
            return Fraction(tree['leaf'])
        self.require(set(tree) == {'op', 'left', 'right'}, 'invalid_rational_tree')
        return self.arithmetic(self.rational_tree(tree['left'], allowed), tree['op'], self.rational_tree(tree['right'], allowed))

    def rational(self, rec, parents, sources):
        allowed = set()
        for parent in rec['parents']: allowed.update(self.legacy_leaves.get(parent, set()))
        if rec.get('pathway') == 'calculus_to_rational_v47':
            refs = rec.get('sources', [])
            self.require(not parents and len(refs) == 1 and refs[0]['archive'] == 'calculus',
                         'invalid_calculus_embedding')
            coeff = sources[0]
            self.require(len(coeff) == 1, 'nonconstant_calculus_embedding')
            tree = rec['tree']
            self.require(set(tree) in ({'leaf'}, {'leaf', 'calculus_source'}), 'invalid_calculus_tree')
            if 'calculus_source' in tree:
                self.require(tree['calculus_source'] == refs[0]['id'], 'calculus_source_disagreement')
            value = coeff[0]
            if set(tree) == {'leaf'}: allowed.add(value)
            self.require(Fraction(str(tree['leaf'])) == value, 'calculus_bridge_disagreement')
        else:
            value = self.rational_tree(rec['tree'], allowed)
        self.legacy_leaves[rec['id']] = allowed
        self.require(str(value) == rec['value'], 'rational_value_disagreement')
        return value

    @staticmethod
    def spq(value):
        return sympy_module().Rational(value.numerator, value.denominator)

    def exact(self, tree, depth=0):
        self.require(isinstance(tree, dict) and depth <= 128, 'invalid_exact_tree')
        if set(tree) == {'q'}:
            q = tree['q']
            self.require(isinstance(q, list) and len(q) == 2, 'invalid_rational_encoding')
            return self.spq(Fraction(int(q[0]), int(q[1])))
        if set(tree) == {'i'} and tree['i'] is True:
            return sympy_module().I
        self.require(set(tree) == {'fn', 'args'} and isinstance(tree['args'], list), 'invalid_exact_encoding')
        args = [self.exact(t, depth + 1) for t in tree['args']]
        sp = sympy_module()
        if tree['fn'] == 'add' and len(args) >= 2: return sp.Add(*args)
        if tree['fn'] == 'mul' and len(args) >= 2: return sp.Mul(*args)
        if tree['fn'] == 'pow' and len(args) == 2: return self.symop('**', args)
        raise ValueError('invalid_exact_constructor')

    def symop(self, op, args):
        sp = sympy_module()
        if op == 'sqrt' and len(args) == 1: result = sp.sqrt(args[0])
        elif op == '**' and len(args) == 2:
            a, b = args
            self.require(b.is_Rational is True and not (a == 0 and b <= 0), 'undefined_symbolic_power')
            self.require(abs(int(b.p)) <= 4096 and int(b.q) <= 4096, 'symbolic_replay_resource_limit')
            result = a ** b
        elif len(args) == 2: result = self.arithmetic(args[0], op, args[1])
        else: raise ValueError('invalid_symbolic_arity')
        self.require(not result.has(sp.nan, sp.zoo, sp.oo, -sp.oo), 'nonfinite_symbolic_value')
        return result

    def symtree(self, tree, depth=0):
        self.require(isinstance(tree, dict) and depth <= 128, 'invalid_construction_tree')
        if set(tree) == {'exact'}: return self.exact(tree['exact'])
        self.require(set(tree) == {'op', 'args'} and isinstance(tree['args'], list), 'invalid_symbolic_tree')
        return self.symop(tree['op'], [self.symtree(t, depth + 1) for t in tree['args']])

    def equal(self, a, b):
        return a == b or sympy_module().simplify(a - b) == 0

    def complex(self, rec, parents, sources):
        a, b = Fraction(rec['real']), Fraction(rec['imaginary'])
        op, pathway = rec['operation'], rec['pathway']
        if pathway == 'complex_unit_v44':
            self.require(not parents and not sources and op == 'seed' and
                         rec['id'] in (0, 1), 'invalid_complex_seed')
            expected = (Fraction(0), Fraction(1 if rec['id'] == 0 else -1))
            self.require(rec['expr'] == ('i' if rec['id'] == 0 else '-i') and rec['depth'] == 0,
                         'invalid_complex_seed_metadata')
        elif pathway == 'rational_embedding_v44':
            self.require(not parents and not sources and op == 'embed' and
                         a.denominator == 1 and int(a) in self.m['foundation']['states'] and b == 0,
                         'invalid_real_axis_embedding')
            expected = (a, Fraction(0))
            self.require(rec['expr'] == str(a) and rec['depth'] == 0, 'invalid_real_axis_metadata')
        elif pathway == 'symbolic_to_complex_v46':
            self.require(not parents and op == 'embed' and len(sources) == 1 and
                         rec['sources'][0]['archive'] == 'symbolic', 'invalid_complex_embedding')
            expected = sources[0].as_real_imag()
            origin = self.record('symbolic', rec['sources'][0]['id'])
            self.require(rec['depth'] == origin['depth'], 'complex_embedding_depth')
        else:
            self.require(pathway == 'complex_arithmetic_v44' and len(parents) == 2 and not sources,
                         'unsupported_complex_rule')
            (ar, ai), (br, bi) = parents
            if op == '+': expected = (ar + br, ai + bi)
            elif op == '-': expected = (ar - br, ai - bi)
            elif op == '*': expected = (ar * br - ai * bi, ar * bi + ai * br)
            elif op == '/':
                denominator = br * br + bi * bi
                self.require(denominator != 0, 'complex_division_by_zero')
                expected = ((ar * br + ai * bi) / denominator, (ai * br - ar * bi) / denominator)
            else: raise ValueError('unsupported_complex_operation')
            original = [self.record('complex', p) for p in rec['parents']]
            self.require(rec['depth'] == 1 + max(r['depth'] for r in original), 'complex_depth_disagreement')
            self.require(rec['expr'] == '(' + original[0]['expr'] + ' ' + op + ' ' + original[1]['expr'] + ')',
                         'complex_expression_disagreement')
        self.require((a, b) == expected, 'complex_arithmetic_disagreement')
        key = str(a) + ('+' if b >= 0 else '') + str(b) + 'i'
        self.require(rec['value'] == key, 'complex_value_key_disagreement')
        return a, b

    def construction(self, domain, idx):
        rec = self.record(domain, idx)
        if domain == 'symbolic': return rec['construction']
        if domain == 'complex':
            if rec['parents']:
                return {'op':rec['operation'], 'args':[self.construction(domain, p) for p in rec['parents']]}
            if rec['pathway'] == 'symbolic_to_complex_v46':
                return self.construction('symbolic', rec['sources'][0]['id'])
            ar, ai = self.get(domain, idx)
            return {'exact':symbolic_pack(self.spq(ar) + sympy_module().I * self.spq(ai))}
        def visit(tree):
            if 'symbolic_source' in tree: return self.construction('symbolic', tree['symbolic_source'])
            if 'leaf' in tree: return {'exact':symbolic_pack(self.spq(Fraction(str(tree['leaf']))))}
            return {'op':tree['op'], 'args':[visit(tree['left']), visit(tree['right'])]}
        return visit(rec['tree'])

    def display(self, tree):
        if 'exact' in tree: return '(' + str(self.exact(tree['exact'])) + ')'
        args = [self.display(t) for t in tree['args']]
        return 'sqrt(' + args[0] + ')' if tree['op'] == 'sqrt' else (
            '(' + args[0] + ' ' + tree['op'] + ' ' + args[1] + ')')

    def symbolic(self, rec, parents, sources):
        value = self.symtree(rec['construction'])
        self.require(self.equal(value, self.exact(rec['exact'])) and rec['value'] == str(self.exact(rec['exact'])),
                     'symbolic_value_disagreement')
        op, pathway = rec['operation'], rec['pathway']
        original = [self.record('symbolic', p) for p in rec['parents']]
        if pathway in ('numeric_to_symbolic_v46', 'numeric_to_symbolic_v464'):
            self.require(op == 'embed' and not parents and len(sources) == 1, 'invalid_symbolic_import')
            ref = rec['sources'][0]
            self.require(ref['archive'] in ('rational', 'complex'), 'unsupported_symbolic_source')
            expected = self.spq(sources[0]) if ref['archive'] == 'rational' else (
                self.spq(sources[0][0]) + sympy_module().I * self.spq(sources[0][1]))
            self.require(self.equal(value, expected), 'symbolic_import_disagreement')
            if pathway == 'numeric_to_symbolic_v464':
                self.require(rec['construction'] == self.construction(ref['archive'], ref['id']), 'symbolic_import_construction_disagreement')
                self.require(rec['expr'] == self.record(ref['archive'], ref['id'])['expr'], 'symbolic_import_expression_disagreement')
            self.require(rec['depth'] == self.record(ref['archive'], ref['id'])['depth'], 'symbolic_import_depth')
        elif pathway == 'exact_algebraic_v46':
            self.require(not sources and op in ('sqrt', '+', '-', '*', '/', '**'), 'unsupported_symbolic_rule')
            self.require(len(parents) == (1 if op == 'sqrt' else 2), 'symbolic_parent_arity')
            expected_tree = {'op': op, 'args': [r['construction'] for r in original]}
            self.require(rec['construction'] == expected_tree, 'symbolic_parent_construction_disagreement')
            self.require(self.equal(value, self.symop(op, parents)), 'symbolic_arithmetic_disagreement')
            self.require(rec['depth'] == 1 + max(r['depth'] for r in original), 'symbolic_depth_disagreement')
            expr = 'sqrt(' + original[0]['expr'] + ')' if op == 'sqrt' else (
                '(' + original[0]['expr'] + ' ' + op + ' ' + original[1]['expr'] + ')')
            self.require(rec['expr'] == expr, 'symbolic_expression_disagreement')
        elif op == 'zero_slot_construction':
            event = rec['nexus']
            self.require(not sources and event['zero_nexus'] == 'Z0', 'invalid_symbolic_nexus')
            if pathway == 'zero_nexus_symbolic_v461':
                self.require(len(parents) == 2 and rec['parents'] == [event['source_id'], event['selected_value_id']],
                             'symbolic_nexus_parent_disagreement')
                path = event['zero_slot_path']
                self.require(isinstance(path, list), 'invalid_zero_path')
                def replace(tree, route):
                    if not route:
                        self.require(tree == {'exact': {'q': ['0', '1']}}, 'nexus_source_not_zero')
                        return original[1]['construction']
                    self.require(set(tree) == {'op', 'args'} and type(route[0]) is int and
                                 0 <= route[0] < len(tree['args']), 'invalid_zero_path')
                    args = list(tree['args']); args[route[0]] = replace(args[route[0]], route[1:])
                    return {'op': tree['op'], 'args': args}
                expected_tree = replace(original[0]['construction'], path)
            else:
                self.require(pathway == 'zero_nexus_symbolic_position_v461_slot_' + str(event['source_position']) and
                             event['source'] == '00404' and event['source_position'] in (1, 2, 4),
                             'invalid_symbolic_position')
                self.require(event['selected_value'] in self.m['foundation']['states'] and
                             0 <= event['selected_value'] <= 9, 'unregistered_position_selection')
                operation, order = event['operation'], event['order']
                if operation == 'sqrt': expected_values = [sympy_module().Integer(0)]
                elif order == 'zero_first': expected_values = [sympy_module().Integer(0), sympy_module().Integer(event['selected_value'])]
                elif order == 'zero_last': expected_values = [sympy_module().Integer(event['selected_value']), sympy_module().Integer(0)]
                else: raise ValueError('unsupported_position_order')
                self.require(parents == expected_values, 'symbolic_position_parent_disagreement')
                expected_tree = {'op': operation, 'args': [r['construction'] for r in original]}
            self.require(rec['construction'] == expected_tree, 'symbolic_nexus_construction_disagreement')
            self.require(rec['expr'] == self.display(expected_tree), 'symbolic_nexus_expression_disagreement')
            def depth(t): return 0 if 'exact' in t else 1 + max(depth(a) for a in t['args'])
            self.require(rec['depth'] == max(depth(expected_tree), max(r['depth'] for r in original)),
                         'symbolic_nexus_depth_disagreement')
        else: raise ValueError('unsupported_symbolic_pathway')
        return value

    def calculus(self, rec, parents, sources):
        encoded = rec['coefficients']
        self.require(isinstance(encoded, list) and bool(encoded), 'invalid_polynomial')
        coeff = [Fraction(v) for v in encoded]
        while len(coeff) > 1 and coeff[-1] == 0: coeff.pop()
        self.require(encoded == [str(v) for v in coeff], 'noncanonical_polynomial')
        op = rec['operation']
        if op == 'constant_import':
            self.require(not parents and len(sources) == 1 and rec['sources'][0]['archive'] == 'rational',
                         'invalid_constant_import')
            expected = [sources[0]]
            self.require(rec['depth'] == 0, 'constant_import_depth')
        else:
            self.require(len(parents) == 1, 'calculus_parent_arity')
            a = parents[0]
            if op == 'differentiate': expected = [i * a[i] for i in range(1, len(a))] or [Fraction(0)]
            elif op == 'integrate': expected = [Fraction(0)] + [v / (i + 1) for i, v in enumerate(a)]
            elif op == 'multiply_x': expected = [Fraction(0)] + a
            elif op == 'limit_zero': expected = [a[0]]
            else: raise ValueError('unsupported_calculus_rule')
            while len(expected) > 1 and expected[-1] == 0: expected.pop()
            self.require(rec['depth'] == self.record('calculus', rec['parents'][0])['depth'] + 1,
                         'calculus_depth_disagreement')
            if 'variable_source' in rec:
                self.require(rec['sources'] == [rec['variable_source']] and rec['variable_source']['archive'] == 'roles' and
                             sources == [{'kind': 'variable', 'symbol': 'x'}] and rec['variable'] == 'x',
                             'invalid_calculus_variable')
            else:
                boundary = self.m['calculus_archive'].get('role_origin_boundary', 0)
                self.require(rec['id'] < boundary, 'missing_calculus_variable')
                self.legacy_calculus.append(rec['id'])
            proof = rec.get('proof')
            if proof is not None:
                self.require(proof.get('rule') == op and
                    proof.get('input_coefficients') == [str(v) for v in a] and
                    proof.get('output_coefficients') == encoded, 'calculus_proof_metadata_disagreement')
            if op == 'integrate':
                self.require(rec.get('integration_constant') == 'C=0 representative; full family is result+C',
                             'missing_integral_family_qualification')
            if op == 'limit_zero':
                self.require(rec.get('limit') == {'point':'0', 'direction':'two-sided', 'justification':'polynomial continuity'},
                             'invalid_polynomial_limit_qualification')
        self.require(coeff == expected, 'calculus_coefficient_disagreement')
        x = sympy_module().Symbol('x')
        expr = str(sum((self.spq(v) * x ** i for i, v in enumerate(coeff)), sympy_module().Integer(0)))
        self.require(rec['expr'] == expr and rec['value'] == expr, 'calculus_expression_disagreement')
        return coeff

    def roles(self, rec, parents, sources):
        rule, kind, label = rec['rule'], rec['kind'], rec['label']
        if rule == 'reference_foundation_zero':
            self.require(rec['id'] == 0 and not parents and rec['sources'] == [{'archive':'rational','id':0}] and
                         sources == [Fraction(0)] and rec['depth'] == 0 and rec['operation'] == 'origin' and
                         kind == 'numeric' and label == '0' and rec['path'] == ['0'], 'invalid_role_origin')
            body = {'kind':'numeric', 'value':'0'}
        else:
            self.require(len(parents) == 1 and rec['operation'] == 'transform', 'invalid_role_transition')
            parent = self.record('roles', rec['parents'][0]); slot = parent['depth']
            self.require(rec['depth'] == slot + 1 and rec['slot']['counter'] == slot and
                         slot in self.m['foundation']['states'], 'invalid_role_slot')
            foundation_id = rec['slot']['foundation_id']
            foundation_rec = self.record('rational', foundation_id)
            self.require(foundation_rec['pathway'] == 'foundation_state_count_v3' and
                         self.get('rational', foundation_id) == slot and
                         {'archive':'rational', 'id':foundation_id} in rec['sources'], 'invalid_slot_backing')
            self.require(rec['path'] == parent['path'] + [label], 'invalid_role_path')
            if rule == 'bind_successor_operation_role':
                self.require(kind=='operation' and label in ('S','P'), 'invalid_primitive_operation_role')
                body={'kind':'operation','primitive':label,'input':'natural_counter','output':'natural_counter','nexus':'Z0'}
            elif rule == 'bind_primitive_operation_role':
                self.require(kind=='operation' and label in ('S','P'), 'invalid_historical_primitive_role')
                body={'kind':'operation','primitive':label,'input':'integer','output':'integer','nexus':'Z0'}
            elif rule == 'assign_name_preserve_payload':
                self.require(kind == 'named' and label in ('A','a'), 'invalid_role_name')
                body = parents[0]
            elif rule == 'introduce_free_variable':
                self.require(kind == 'variable' and label == 'x', 'invalid_variable_role')
                body = {'kind':'variable', 'symbol':'x'}
            elif rule == 'select_registered_numeric_state':
                q = Fraction(label)
                self.require(kind == 'numeric' and q.denominator == 1 and int(q) in self.m['foundation']['states'] and
                             any(ref['archive'] == 'rational' and self.record('rational', ref['id'])['pathway'] ==
                                 'foundation_state_count_v3' and value == q for ref,value in zip(rec['sources'], sources)),
                             'invalid_role_numeric_selection')
                body = {'kind':'numeric', 'value':str(q)}
            else: raise ValueError('unsupported_role_rule')
        self.require(rec['body'] == body and rec['expr'] == ' -> '.join(rec['path']), 'role_payload_disagreement')
        body_text = role_body_text(body)
        value = label + '[' + body_text + ']' if kind == 'named' else body_text
        self.require(rec['value'] == value, 'role_value_disagreement')
        return body

    def report(self):
        counts = {}
        for domain in _ZR_DOMAINS:
            counts[domain] = len(_zr_records(self.m, domain))
            for idx in range(counts[domain]):
                try: self.get(domain, idx)
                except ValueError: pass
        findings = [{'archive':d, 'id':i, 'reasons':[reason]}
                    for (d,i),reason in sorted(self.errors.items())]
        for domain in _ZR_DOMAINS:
            owner = self.m if domain == 'rational' else self.m.get(domain + '_archive')
            if owner is None: continue
            index = {}
            for rec in _zr_records(self.m, domain):
                if isinstance(rec, dict) and isinstance(rec.get('value'), str) and type(rec.get('id')) is int:
                    index.setdefault(rec['value'], []).append(rec['id'])
            if owner.get('results') != index:
                findings.append({'archive':domain, 'id':None, 'reasons':['typed_results_index_mismatch']})
        return {'rule':'independent_typed_replay_v4712', 'records_checked':counts,
                'contradictions':findings, 'legacy_calculus_without_variable_origin':sorted(set(self.legacy_calculus)),
                'scope':'recorded supported arithmetic and representation rules; shared SymPy backend; no novelty or formal-proof claim'}


def _z5_calculus_constant(m, idx):
    coeff = _Z5Replay(m).get('calculus', idx)
    if len(coeff) != 1: raise ValueError('nonconstant_calculus_embedding')
    return coeff[0]


_z5_previous_observe = _zv_observe

def _zv_observe(m):
    report = _z5_previous_observe(m)
    typed = _Z5Replay(m).report()
    report['typed_replay'] = typed
    report['contradictions'].extend(typed['contradictions'])
    report['status'] = 'unresolved' if report['contradictions'] else 'arithmetic_consistent'
    report['scope'] += '; independent_typed_domain_replay_v4712'
    return report


_z5_previous_approval_verify = _za_verify_memory

def _za_verify_memory(m):
    report = _z5_previous_approval_verify(m)
    typed = _Z5Replay(m).report()
    report['typed_replay'] = typed
    report['contradictions'].extend(typed['contradictions'])
    return report


# ============================================================
# V4.7.13 - TYPED RECONSTRUCTION FROM RETAINED RECIPES
# Recipes describe operands/rules/representation layout, not saved answers.
# Reexecution must match the retained content digest and independent replay.
# ============================================================


def _z6_recipe(domain, rec):
    recipe = {'schema':1, 'archive':domain, 'operation':rec['operation'],
              'pathway':rec['pathway'], 'parents':list(rec['parents']),
              'sources':_zr_copy.deepcopy(rec.get('sources', [])),
              'passage_historical_backfill':bool(rec.get('zero_core_passage', {}).get('historical_backfill', False))}
    if domain == 'complex' and rec['pathway'] == 'rational_embedding_v44':
        recipe['foundation_state'] = rec['expr']
    if domain == 'symbolic':
        if 'nexus' in rec: recipe['nexus'] = _zr_copy.deepcopy(rec['nexus'])
        recipe['import_style'] = 'source' if rec['pathway'] != 'numeric_to_symbolic_v46' or 'op' in rec['construction'] else 'literal'
    if domain == 'roles':
        recipe['rule'], recipe['label'] = rec['rule'], rec['label']
    if domain == 'calculus':
        recipe['variable_bound'] = 'variable_source' in rec
        recipe['proof_present'] = 'proof' in rec
    return recipe


_z6_previous_manifest_entry = _zr_manifest_entry

def _zr_manifest_entry(domain, rec):
    entry = _z6_previous_manifest_entry(domain, rec)
    if domain in ('complex', 'symbolic', 'calculus', 'roles'):
        entry['typed_recipe'] = _z6_recipe(domain, rec)
    return entry


def _z6_legacy_recipe(m, domain, idx):
    """Bounded legacy key/event evidence; never use stored output coefficients."""
    archive = m.get(domain + '_archive', {})
    keys = archive.get('known_keys', [])
    if not 0 <= idx < len(keys): return None
    try:
        key = json.loads(keys[idx])
        recipe = {'schema':1, 'archive':domain, 'passage_historical_backfill':False}
        if domain == 'complex':
            expr, pathway, parents = key
            recipe.update(pathway=pathway, parents=parents, sources=[])
            if pathway == 'complex_unit_v44': recipe['operation'] = 'seed'
            elif pathway == 'rational_embedding_v44':
                recipe.update(operation='embed', foundation_state=expr)
            elif pathway == 'complex_arithmetic_v44':
                a,b = [archive['expressions'][p]['expr'] for p in parents]
                operations = [op for op in OPERATIONS if expr == '(' + a + ' ' + op + ' ' + b + ')']
                if len(operations) != 1: return None
                recipe['operation'] = operations[0]
            else:
                # Historical symbolic embeddings did not retain source IDs in
                # complex keys. Their origin is not inferred from equal values.
                return None
        elif domain == 'symbolic':
            pathway, op, parents, sources, _expr = key
            recipe.update(pathway=pathway, operation=op, parents=parents, sources=sources, import_style='source')
            if op == 'zero_slot_construction':
                events = [event for event in m.get('symbolic_nexus_events', []) if event.get('symbolic_result_id') == idx]
                if len(events) != 1: return None
                recipe['nexus'] = {k:v for k,v in events[0].items() if k != 'symbolic_result_id'}
        elif domain == 'roles':
            parents, rule, label, sources = key
            recipe.update(pathway=ROLE_RULE, operation='transform' if parents else 'origin',
                          parents=parents, rule=rule, label=label, sources=sources)
        elif domain == 'calculus':
            op, parents, sources, _ignored_output = key
            bound = any(ref.get('archive') == 'roles' for ref in sources)
            recipe.update(operation=op, parents=parents, sources=sources, variable_bound=bound,
                          proof_present=bool(parents), pathway='zero_slot_calculus_v471' if bound else 'polynomial_calculus_v47')
        else: return None
        return recipe
    except (ValueError, KeyError, TypeError, IndexError): return None


def _z6_build(m, domain, idx, recipe):
    """Build in memory only. Do not append, schedule, rewrite indexes or keys."""
    if not isinstance(recipe, dict) or recipe.get('schema') != 1 or recipe.get('archive') != domain:
        return None
    try:
        parents, refs = recipe['parents'], recipe['sources']
        if (not isinstance(parents, list) or any(type(p) is not int or not 0 <= p < idx for p in parents)
                or not isinstance(refs, list)): return None
        verifier = _Z5Replay(m)
        values = [verifier.get(domain,p) for p in parents]
        sources = [verifier.source(ref) for ref in refs]
        original = [_zr_records(m,domain)[p] for p in parents]
        op, pathway = recipe['operation'], recipe['pathway']
        rec = {'id':idx, 'parents':list(parents), 'operation':op, 'pathway':pathway}
        if domain == 'complex':
            if pathway == 'complex_unit_v44' and not parents and not refs and op == 'seed' and idx in (0,1):
                ar,ai = Fraction(0), Fraction(1 if idx == 0 else -1)
                expr,depth = ('i' if idx == 0 else '-i'),0
            elif pathway == 'rational_embedding_v44' and op == 'embed' and not parents and not refs:
                ar,ai = Fraction(recipe['foundation_state']),Fraction(0)
                if ar.denominator != 1 or int(ar) not in m['foundation']['states']:return None
                expr,depth = str(ar),0
            elif pathway == 'symbolic_to_complex_v46' and op == 'embed' and not parents and len(refs) == 1 and refs[0]['archive'] == 'symbolic':
                re,im = sources[0].as_real_imag()
                if re.is_Rational is not True or im.is_Rational is not True:return None
                ar,ai = Fraction(int(re.p),int(re.q)),Fraction(int(im.p),int(im.q))
                expr,depth = str(sources[0]),_zr_records(m,'symbolic')[refs[0]['id']]['depth']
                rec['sources'] = _zr_copy.deepcopy(refs)
            elif pathway == 'complex_arithmetic_v44' and len(parents) == 2 and not refs and op in OPERATIONS:
                result = zero_core(m,'complex',operation=op,operands=tuple(values))
                if result is None:return None
                ar,ai = result; expr='(' + original[0]['expr'] + ' ' + op + ' ' + original[1]['expr'] + ')'
                depth = 1 + max(r['depth'] for r in original)
            else:return None
            rec.update(expr=expr,real=encode(ar),imaginary=encode(ai),value=complex_key(ar,ai),depth=depth)
        elif domain == 'symbolic':
            sp = sympy_module()
            if pathway in ('numeric_to_symbolic_v46','numeric_to_symbolic_v464') and op == 'embed' and not parents and len(refs) == 1:
                ref=refs[0]
                if ref['archive'] == 'rational':value=verifier.spq(sources[0])
                elif ref['archive'] == 'complex':value=verifier.spq(sources[0][0])+sp.I*verifier.spq(sources[0][1])
                else:return None
                source=_zr_records(m,ref['archive'])[ref['id']]
                tree=verifier.construction(ref['archive'],ref['id']) if recipe.get('import_style') == 'source' else {'exact':symbolic_pack(value)}
                expr,depth=source['expr'],source['depth']
            elif pathway == 'exact_algebraic_v46' and not refs and len(parents) == (1 if op == 'sqrt' else 2):
                operands=(values[0],None if op == 'sqrt' else values[1])
                value,reason=zero_core(m,'symbolic',operation=op,operands=operands)
                if reason:return None
                tree={'op':op,'args':[r['construction'] for r in original]}
                expr='sqrt('+original[0]['expr']+')' if op == 'sqrt' else '('+original[0]['expr']+' '+op+' '+original[1]['expr']+')'
                depth=1+max(r['depth'] for r in original)
            elif op == 'zero_slot_construction' and not refs:
                event=recipe['nexus']
                if pathway == 'zero_nexus_symbolic_v461' and len(parents) == 2:
                    if parents != [event['source_id'],event['selected_value_id']]:return None
                    tree=replace_symbolic_slot(original[0]['construction'],event['zero_slot_path'],original[1]['construction'])
                elif pathway.startswith('zero_nexus_symbolic_position_v461_slot_') and parents:
                    tree={'op':event['operation'],'args':[r['construction'] for r in original]}
                else:return None
                value,expr,reason=evaluate_symbolic_construction(tree,tracking=m)
                if reason:return None
                depth=max(symbolic_construction_depth(tree),max(r['depth'] for r in original))
                rec['nexus']=_zr_copy.deepcopy(event)
            else:return None
            if not symbolic_within_limits(value) or depth > MAX_DEPTH:return None
            rec.update(expr=expr,value=str(value),exact=symbolic_pack(value),sources=_zr_copy.deepcopy(refs),depth=depth,construction=_zr_copy.deepcopy(tree))
        elif domain == 'roles':
            if op == 'origin' and idx == 0 and not parents and recipe['rule'] == 'reference_foundation_zero':
                zero_id=foundation_expression_id(m,0)
                result={'kind':'numeric','label':'0','body':{'kind':'numeric','value':'0'},'value':'0',
                        'parents':[],'sources':[{'archive':'rational','id':zero_id}],
                        'path':['0'],'depth':0,'rule':'reference_foundation_zero'}
            elif op == 'transform' and len(parents) == 1:
                target=recipe['label']
                if recipe['rule'] == 'select_registered_numeric_state':target=int(target)
                result,reason=zero_core(m,'roles',operation='transform',operands=(parents[0],target))
                if reason:return None
            else:return None
            if result['rule'] != recipe['rule'] or result['label'] != recipe['label'] or result['sources'] != refs:return None
            rec=dict(result)
            rec.update(id=idx,expr=' -> '.join(result['path']),operation=op,pathway=pathway,formal_rule=pathway)
        elif domain == 'calculus':
            if op == 'constant_import' and not parents and len(refs) == 1 and refs[0]['archive'] == 'rational':
                coeff=[str(sources[0])];depth=0
            elif op in CALCULUS_OPERATIONS and len(parents) == 1:
                if recipe.get('variable_bound'):
                    if len(refs) != 1 or refs[0]['archive'] != 'roles':return None
                    coeff,reason=zero_core(m,'calculus',operation=op,operands=(original[0]['coefficients'],refs[0]['id']))
                else:
                    coeff,reason=zero_core(None,'calculus',operation=op,operands=(original[0]['coefficients'],))
                if reason:return None
                depth=original[0]['depth']+1
            else:return None
            expr=str(calculus_value(coeff,'x'))
            rec.update(expr=expr,value=expr,coefficients=coeff,sources=_zr_copy.deepcopy(refs),depth=depth,formal_rule=pathway)
            if recipe.get('variable_bound'):
                rec.update(variable_source=_zr_copy.deepcopy(refs[0]),variable='x',
                           input_interpretation='polynomial coefficients expressed in this archived variable role')
            if op == 'integrate':rec['integration_constant']='C=0 representative; full family is result+C'
            if op == 'limit_zero':rec['limit']={'point':'0','direction':'two-sided','justification':'polynomial continuity'}
            if recipe.get('proof_present'):
                rec['proof']={'rule':op,'input_coefficients':original[0]['coefficients'],'output_coefficients':coeff,
                    'formula':{'differentiate':'a[k] -> k*a[k] at degree k-1','integrate':'a[k] -> a[k]/(k+1) at degree k+1',
                               'limit_zero':'sum a[k]*x^k -> a[0] as x -> 0','multiply_x':'a[k] -> a[k] at degree k+1'}[op]}
        else:return None
        return rec
    except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError,OverflowError,RecursionError,AttributeError):return None


def _z6_findings(m):
    findings=[]
    for domain in ('complex','symbolic','calculus','roles'):
        manifest=m.get('zero_recovery',{}).get('manifest',{}).get(domain,{})
        for rec in _zr_records(m,domain):
            recipe=manifest.get(str(rec.get('id')),{}).get('typed_recipe')
            if recipe is None:continue
            try:agrees=recipe == _z6_recipe(domain,rec)
            except (ValueError,KeyError,TypeError,IndexError):agrees=False
            if not agrees:findings.append({'archive':domain,'id':rec.get('id'),'reasons':['typed_manifest_recipe_record_disagreement']})
    return findings


_z6_previous_observe=_zv_observe

def _zv_observe(m):
    report=_z6_previous_observe(m)
    report['contradictions'].extend(_z6_findings(m))
    if report['contradictions']:report['status']='unresolved'
    report['typed_recipe_consistency_rule']='typed_recipe_record_consistency_v4713'
    return report


_z6_previous_approval=_za_verify_memory

def _za_verify_memory(m):
    report=_z6_previous_approval(m)
    report['contradictions'].extend(_z6_findings(m))
    return report


def _z6_lookup(domain, rec, value):
    # Avoid record_lookup_key's runtime caches in a serializable checkpoint.
    sp=sympy_module()
    if domain == 'roles':return 'role:' + json.dumps([rec['kind'],rec['label'],rec['body']],sort_keys=True)
    if domain == 'rational':value=sp.Rational(value.numerator,value.denominator)
    elif domain == 'complex':value=sp.Rational(value[0].numerator,value[0].denominator)+sp.I*sp.Rational(value[1].numerator,value[1].denominator)
    elif domain == 'calculus':
        x=sp.Symbol('x');value=sum((sp.Rational(q.numerator,q.denominator)*x**i for i,q in enumerate(value)),sp.Integer(0))
    return exact_lookup_key(value)


def _z6_attempt(state, domain, idx, outcome, reason=None):
    tracking=state.setdefault('typed_reconstruction_attempts',{})
    row=tracking.setdefault(domain+':'+str(idx),{'attempts':0,'outcomes':[]})
    row['attempts']+=1
    event={'status':outcome,'reason':reason}
    if event not in row['outcomes']:row['outcomes'].append(event)


_z6_previous_preflight=_zr_preflight

def _zr_preflight(m,api):
    candidate,ready=_z6_previous_preflight(m,api)
    state=_zr_state(candidate)
    if state.get('status') == 'blocked':return candidate,False
    pending=[(domain,rec['id']) for domain in _ZR_DOMAINS for rec in _zr_records(candidate,domain)
             if rec.get('status') == 'zero_recovery_pending']
    # A finite fixed point permits dependencies crossing archive order. A cycle
    # or absent evidence stops with explicit pending slots, not invented values.
    for _ in range(len(pending)+1):
        progress=False
        for domain,idx in pending:
            records=_zr_records(candidate,domain)
            if records[idx].get('status') != 'zero_recovery_pending':continue
            if domain == 'rational':
                entry=state['manifest'][domain].get(str(idx))
                recipe=entry.get('recipe') if entry else _zr_legacy_recipe(candidate,idx)
                try:rebuilt=_zr_reconstruct(candidate,idx,recipe,api)
                except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError):rebuilt=None
            else:
                entry=state['manifest'][domain].get(str(idx))
                if not entry:continue
                recipe=entry.get('typed_recipe')
                if recipe is None:recipe=_z6_legacy_recipe(candidate,domain,idx)
                rebuilt=_z6_build(candidate,domain,idx,recipe)
            if rebuilt is None:
                _z6_attempt(state,domain,idx,'pending','unsupported_recipe_or_dependency_pending');continue
            if entry and _zr_digest(_zr_payload(rebuilt)) != entry.get('digest'):
                _z6_attempt(state,domain,idx,'pending','retained_digest_disagreement');continue
            placeholder=records[idx];records[idx]=rebuilt
            try:
                verified_value=_Z5Replay(candidate).get(domain,idx)
                rebuilt['zero_core_passage']={'rule':ZERO_CORE_RULE,'archive':domain,'id':idx,'zero_nexus':'Z0',
                    'historical_backfill':bool(recipe.get('passage_historical_backfill',False)),
                    'effect':'identity_preserves_construction'}
                rebuilt['unified_value_key']=_z6_lookup(domain,rebuilt,verified_value)
            except (ValueError,KeyError,TypeError,IndexError,ZeroDivisionError,RecursionError) as exc:
                records[idx]=placeholder
                _z6_attempt(state,domain,idx,'pending','independent_check_failed:'+str(exc));continue
            _zr_event(candidate,domain,idx,'recovered',
                      'typed_manifest_verified_reexecution' if domain != 'rational' else 'manifest_verified_reexecution')
            _z6_attempt(state,domain,idx,'recovered','digest_and_independent_replay_agree')
            progress=True
        if not progress:break
    if any(rec.get('status') == 'zero_recovery_pending' for domain in _ZR_DOMAINS for rec in _zr_records(candidate,domain)):
        state['status']='pending';return candidate,False
    state['status']='ready'
    candidate,ready=_z6_previous_preflight(candidate,api)
    if not ready:return candidate,False
    observation=_zv_observe(candidate)
    if observation['contradictions']:
        _zr_state(candidate).update(status='blocked',reason='independent_typed_validation_failed:'+str(observation['contradictions'][:3]),
                                   typed_findings=observation['contradictions'])
        return candidate,False
    state=_zr_state(candidate)
    for domain in ('complex','symbolic','calculus','roles'):
        for rec in _zr_records(candidate,domain):
            entry=state['manifest'][domain][str(rec['id'])]
            if 'typed_recipe' not in entry:entry['typed_recipe']=_z6_recipe(domain,rec)
    state.setdefault('typed_recipe_boundary',{'rule':'typed_reconstruction_recipes_v4713',
        'scope':'validated_current_construction_evidence; no authenticated historical chronology'})
    state['scope']='archive_damage; rational_binary_and_typed_domain_reexecution'
    return candidate,True


# ============================================================
# V4.7.15 - EVIDENCE-TRIGGERED RECOVERY ALONGSIDE NEW-LINEAGE EXPLORATION
# ============================================================
RECOVERY_RETRY_ENABLED = True
RECOVERY_RETRY_WORK_PER_RUN = 8
RECOVERY_RETRY_SECONDS = 2.0  # Cooperative allowance, not a hard CPU deadline.
_Z7_RULE = 'persistent_recovery_feedback_v4715'


def _z7_hash_file(path):
    digest = _zr_hashlib.sha256()
    with open(path, 'rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def _z7_rules_signature():
    # A changed executable is a conservative reason to revisit unsupported
    # rules. Paths/timestamps do not affect this fingerprint.
    return _z7_hash_file(__file__)


def _z7_checkpoint_signature(branch):
    paths = [branch.get('preflight_proposal'), branch.get('feedback_checkpoint')]
    return _zr_digest([(path, _z7_hash_file(path)) for path in paths
                       if path and os.path.isfile(path)])


def _z7_feedback_input(branch):
    path = branch.get('feedback_checkpoint')
    suffix = '.zero-verification-search.json'
    if path and path.endswith(suffix) and os.path.isfile(path):
        return path[:-len(suffix)]
    return None


def _z7_feedback_pending(branch):
    path = branch.get('feedback_checkpoint')
    if not path or not os.path.isfile(path):
        return False
    saved = _zg_read(path)
    return saved.get('head', 0) < len(saved.get('tasks', []))


def _z7_evidence_candidates(memory, active_memory):
    """Only identical retained payload digests qualify; values alone never do."""
    found = []
    manifests = memory.get('zero_recovery', {}).get('manifest', {})
    for domain in _ZR_DOMAINS:
        records = {r['id']: r for r in _zr_records(memory, domain)}
        missing = {int(key): entry for key, entry in manifests.get(domain, {}).items()
                   if records.get(int(key), {}).get('status') == 'zero_recovery_pending'
                   or int(key) not in records}
        expected = {entry['digest']: idx for idx, entry in missing.items() if 'digest' in entry}
        for rec in _zr_records(active_memory, domain):
            digest = _zr_digest(_zr_payload(rec))
            idx = expected.get(digest)
            if idx is None or rec.get('id') != idx:
                continue
            field = 'recipe' if domain == 'rational' else 'typed_recipe'
            # A surviving contradictory recipe is never overwritten.
            if field not in missing[idx]:
                found.append((domain, idx, digest, rec))
    return found


def _z7_supply_recipes(memory, candidates, budget):
    """Supply proposals only. Existing preflight must independently replay them."""
    proposed = _zr_copy.deepcopy(memory)
    offered = []
    manifests = proposed['zero_recovery']['manifest']
    for domain, idx, digest, rec in candidates[:budget]:
        entry = manifests[domain][str(idx)]
        field = 'recipe' if domain == 'rational' else 'typed_recipe'
        evidence = _zr_manifest_entry(domain, rec)
        if field not in entry and field in evidence and entry.get('digest') == digest:
            entry[field] = evidence[field]
            offered.append({'archive': domain, 'id': idx, 'retained_digest': digest,
                            'status': 'recipe_proposal_requires_reexecution'})
    return proposed, offered


def _z7_recovery_memory(branch, source):
    proposal = branch.get('preflight_proposal')
    # Partial repairs in a verifier checkpoint take precedence over an older
    # preflight proposal, but only when bound to the unchanged verifier input.
    feedback = _z7_feedback_input(branch)
    if feedback and os.path.isfile(feedback):
        saved = _zg_read(branch['feedback_checkpoint'])
        if (saved.get('rule') == 'zero_verification_worker_v479' and
                saved.get('source_sha256') == _z7_hash_file(feedback)):
            return saved['working_memory']
    if proposal and os.path.isfile(proposal):
        return _zg_read(proposal)
    try:
        return _zg_read(source)
    except (ValueError, UnicodeError, RecursionError):
        return None


def _z7_retry(source_path, active_path, active_memory, *, work_budget=None, seconds=None):
    """One cooperative recovery slice. Never select or replace an active branch.

    At most work_budget recipe proposals and work_budget verifier executions
    are admitted. Parsing, preflight and final validation are indivisible, so
    the time allowance is cooperative rather than a wall-clock guarantee.
    """
    budget = RECOVERY_RETRY_WORK_PER_RUN if work_budget is None else work_budget
    seconds = RECOVERY_RETRY_SECONDS if seconds is None else seconds
    if type(budget) is not int or budget < 1 or seconds <= 0:
        raise ValueError('Positive recovery retry work/time allowances required')
    digest = _z7_hash_file(source_path)
    root = os.path.join(source_path + '.adaptive-work', digest)
    state_path = os.path.join(root, 'state.json')
    ledger_path = os.path.join(root, 'recovery-retry-state.json')
    report_path = source_path + '.recovery-retry-report.json'
    state = _zg_read(state_path)
    pointer_path = source_path + '.adaptive-active.json'
    pointer = _zg_read(pointer_path)
    snapshot = os.path.join(root, 'source.snapshot')
    expected_active = os.path.join(root, 'regeneration', MEMORY_FILENAME)
    if (state.get('source_sha256') != digest or state.get('rule') != 'zero_adaptive_v4710'
            or state.get('selected_branch') != 'regeneration'
            or pointer.get('rule') != 'adaptive_active_v4710'
            or pointer.get('branch') != 'regeneration' or pointer.get('source_sha256') != digest
            or os.path.abspath(active_path) != os.path.abspath(expected_active)
            or os.path.abspath(state.get('source_snapshot', '')) != os.path.abspath(snapshot)
            or _z7_hash_file(snapshot) != digest):
        raise ZeroRecoveryPending('Recovery retry binding failed; active selection unchanged')
    branch = state['trials']['recovery']
    # Recovery paths must stay in this source's isolated recovery directory.
    recovery_root = os.path.realpath(os.path.join(root, 'recovery'))
    os.makedirs(recovery_root, exist_ok=True)
    for key in ('preflight_proposal', 'feedback_checkpoint', 'memory_path'):
        path = branch.get(key)
        if path and os.path.commonpath((recovery_root, os.path.realpath(path))) != recovery_root:
            raise ZeroRecoveryPending('Recovery checkpoint outside its trial directory')
    if os.path.exists(ledger_path):
        ledger = _zg_read(ledger_path)
        if not isinstance(ledger, dict):
            raise ValueError('Invalid recovery retry ledger object; preserved')
        if ledger.get('rule') != _Z7_RULE or ledger.get('source_sha256') != digest:
            raise ZeroRecoveryPending('Recovery retry ledger does not match source')
    else:
        ledger = {'schema': 1, 'rule': _Z7_RULE, 'zero_nexus': 'Z0', 'source_sha256': digest,
                  'attempts': [], 'status': 'pending', 'historical_identity_proven': False,
                  'regenerated_values_are_historical_evidence': False}
    if (type(ledger.get('schema')) is not int or ledger['schema'] != 1
            or ledger.get('zero_nexus') != 'Z0' or not isinstance(ledger.get('attempts'), list)
            or not isinstance(ledger.get('status'), str)
            or any(not isinstance(item, dict) or type(item.get('attempt')) is not int
                   or item['attempt'] != index for index,item in enumerate(ledger.get('attempts', []), 1))):
        raise ValueError('Invalid recovery retry ledger; bytes preserved; retry deferred')
    if ledger.get('status') == 'candidate_ready':
        candidate = ledger.get('candidate')
        if (candidate and os.path.isfile(candidate) and _z7_hash_file(candidate) == ledger.get('candidate_sha256')
                and ledger.get('rules_signature') == _z7_rules_signature()):
            print('Zero recovery retry: verified candidate retained; regeneration remains active.')
            return ledger
        ledger['status'] = 'candidate_changed_requires_recheck'
    memory = _z7_recovery_memory(branch, snapshot)
    candidates = _z7_evidence_candidates(memory, active_memory) if isinstance(memory, dict) else []
    evidence_signature = _zr_digest([(d, i, h) for d, i, h, _ in candidates])
    rules_signature = _z7_rules_signature()
    checkpoint_signature = _z7_checkpoint_signature(branch)
    triggers = []
    if not ledger['attempts']: triggers.append('first_recheck_after_regeneration')
    if ledger.get('rules_signature') not in (None, rules_signature): triggers.append('executable_rules_changed')
    if candidates and ledger.get('evidence_signature') != evidence_signature:
        triggers.append('new_constructions_matching_retained_payload_digests')
    if ledger.get('checkpoint_signature') not in (None, checkpoint_signature):
        triggers.append('recovery_checkpoint_changed')
    if ledger.get('status') in ('running', 'interrupted'): triggers.append('interrupted_slice')
    if ledger.get('status') == 'candidate_changed_requires_recheck': triggers.append('recovery_candidate_changed')
    if _z7_feedback_pending(branch): triggers.append('saved_feedback_work_remaining')
    if not triggers:
        print('Zero recovery retry: waiting for relevant evidence or changed rules; checkpoints retained.')
        return ledger
    event = {'attempt': len(ledger['attempts']) + 1, 'zero_nexus': 'Z0', 'triggers': triggers,
             'active_saved_run': len(active_memory.get('runs', [])), 'work_budget': budget,
             'seconds_allowance': seconds, 'status': 'running', 'recipe_proposals': [],
             'source_preserved': True, 'active_selection_unchanged': True}
    ledger['attempts'].append(event)
    ledger['status'] = 'running'
    _zn_checkpoint(ledger_path, ledger)  # An interruption is itself resumable.
    protected = {p: _z7_hash_file(p) for p in (source_path, snapshot, pointer_path, active_path)}
    started = time.perf_counter()
    try:
        retry_input = None
        fresh = any(t in triggers for t in ('first_recheck_after_regeneration', 'executable_rules_changed',
                    'new_constructions_matching_retained_payload_digests', 'recovery_checkpoint_changed', 'recovery_candidate_changed'))
        if 'interrupted_slice' in triggers and not _z7_feedback_input(branch):
            fresh = True
        if fresh and memory is not None:
            proposed, offered = _z7_supply_recipes(memory, candidates, budget)
            event['recipe_proposals'] = offered
            retry_input = os.path.join(recovery_root, 'retry-input.json')
            _zn_checkpoint(retry_input, proposed)
        feedback = _z7_feedback_input(branch)
        if not fresh and feedback and os.path.isfile(feedback):
            result = zero_verify_candidate(feedback, budget=budget)
            branch['verification_feedback_executed'] = result['executed_total']
            event['verification_executions'] = result['executed_this_pass']
            if result.get('validated_candidate'):
                checked = _zg_check(result['validated_candidate'])
                _zg_install_trial(state, 'recovery', _zg_trial_paths(root, 'recovery'), checked)
        else:
            zero_core(None, 'adaptive', operation='recover',
                      operands=(state, root, seconds, 1, budget, retry_input))
        candidate = _zg_trial_paths(root, 'recovery')
        if os.path.isfile(candidate):
            checked = _zg_check(candidate)
            event['reconstructed_records'] = sum(e.get('status') == 'recovered'
                for e in checked.get('zero_recovery', {}).get('events', []))
            ledger.update(status='candidate_ready', candidate=candidate,
                          candidate_sha256=_z7_hash_file(candidate))
            branch.update(status='candidate_ready', continuation_verified=False,
                          records=len(checked['expressions']))
            event['status'] = 'candidate_ready'
        else:
            ledger['status'] = 'pending'
            event.update(status='pending', reason=branch.get('reason', 'Recovery evidence still incomplete'))
    except KeyboardInterrupt:
        ledger['status'] = event['status'] = 'interrupted'
        raise
    except (ValueError, KeyError, TypeError, IndexError, UnicodeError, RecursionError, OSError, RuntimeError) as exc:
        ledger['status'] = event['status'] = 'pending'
        event['reason'] = str(exc)
    finally:
        event['elapsed_seconds'] = round(time.perf_counter() - started, 6)
        branch['elapsed_seconds'] = branch.get('elapsed_seconds', 0) + event['elapsed_seconds']
        ledger.update(rules_signature=rules_signature, evidence_signature=evidence_signature,
                      checkpoint_signature=_z7_checkpoint_signature(branch))
        changed = [p for p, before in protected.items() if not os.path.isfile(p) or _z7_hash_file(p) != before]
        if changed:
            ledger['status'] = event['status'] = 'blocked'
            event.update(reason='Protected input changed during retry', source_preserved=False)
        state['recovery_retry'] = {'rule': _Z7_RULE, 'status': ledger['status'],
            'attempts': len(ledger['attempts']), 'last_attempt': event, 'ledger': ledger_path,
            'historical_identity_proven': False, 'active_branch': 'regeneration'}
        _zn_checkpoint(ledger_path, ledger)
        _zg_checkpoint(state, root)
        _zn_checkpoint(source_path + '.adaptive-report.json', state)
        _zn_checkpoint(report_path, ledger)
    print('Zero recovery retry:', ledger['status'], '| attempt:', event['attempt'],
          '| triggers:', ', '.join(triggers), '| regeneration remains active.', flush=True)
    return ledger


_z7_previous_core = zero_core

def zero_core(m, domain, *, operation=None, operands=(), **kwargs):
    if domain == 'recovery_feedback':
        if operation == 'retry': return _z7_retry(*operands, **kwargs)
        raise ValueError('Unsupported recovery feedback zero operation')
    return _z7_previous_core(m, domain, operation=operation, operands=operands, **kwargs)


# ============================================================
# V4.7.17 - TIME OBSERVATIONS THROUGH Z0 (SEPARATE FROM MATH MEMORY)
# ============================================================
import datetime as _zt16_datetime
import functools as _zt16_functools
import uuid as _zt16_uuid

TIME_OBSERVER_ENABLED = True
_ZT16_RULE = 'zero_time_observer_v1'
_ZT16_SESSION = _zt16_uuid.uuid4().hex
_ZT16_STACK = []
_ZT16_WARNED = set()


def _zt16_sample():
    return time.time_ns(), time.monotonic_ns(), time.process_time_ns()


def _zt16_utc(wall_ns):
    seconds, ns = divmod(wall_ns, 1000000000)
    return _zt16_datetime.datetime.fromtimestamp(seconds, _zt16_datetime.timezone.utc).replace(
        microsecond=ns // 1000).isoformat(timespec='microseconds').replace('+00:00', 'Z')


def _zt16_path(memory):
    return os.path.abspath(memory) + '.time-observer.json'


def _zt16_read(memory):
    path = _zt16_path(memory)
    if not os.path.exists(path):
        return {'schema': 1, 'rule': _ZT16_RULE, 'zero_nexus': 'Z0', 'next_seq': 1,
                'events': [], 'open_spans': {}, 'totals': {}, 'last_session': None,
                'clock_sources': {'wall': 'system_UTC', 'elapsed': 'monotonic_ns', 'cpu': 'process_time_ns'},
                'boundary': 'observer only; clocks supplied by this device; no historical timing backfill',
                'totals_scope': 'inclusive per stage; nested durations must not be added as overall runtime'}
    state = _zg_read(path)
    if (state.get('rule') != _ZT16_RULE or state.get('zero_nexus') != 'Z0'
            or state.get('schema') != 1 or not isinstance(state.get('events'), list)
            or state.get('next_seq') != len(state['events']) + 1
            or not isinstance(state.get('open_spans'), dict) or not isinstance(state.get('totals'), dict)):
        raise ValueError('Invalid time observer ledger; existing file preserved')
    return state


def _zt16_event(state, kind, sample, **fields):
    wall, monotonic, cpu = sample
    seq = state['next_seq']
    event = {'seq': seq, 'previous_event_seq': seq - 1 if seq > 1 else None,
             'zero_nexus': 'Z0', 'session': _ZT16_SESSION, 'kind': kind,
             'utc': _zt16_utc(wall), 'wall_ns': wall, 'monotonic_ns': monotonic,
             'process_cpu_ns': cpu, **fields}
    state['events'].append(event)
    state['next_seq'] += 1
    return event


def _zt16_begin(memory, stage):
    state = _zt16_read(memory)
    sample = _zt16_sample()
    previous_session = state['last_session']
    if previous_session is not None and previous_session != _ZT16_SESSION:
        # Monotonic/CPU counters are never compared across process sessions.
        unfinished = list(state['open_spans'])
        previous_wall = state['events'][-1]['wall_ns'] if state['events'] else None
        _zt16_event(state, 'session_boundary', sample, previous_session=previous_session,
                    prior_unfinished_spans=unfinished, elapsed_ns=None, cpu_elapsed_ns=None,
                    wall_gap_ns=None if previous_wall is None else sample[0] - previous_wall,
                    boundary='wall gap only; unobserved work duration is unknown')
        for row in state['open_spans'].values():
            state['totals'][row['stage']]['unfinished_after_restart'] += 1
        state['open_spans'] = {}
    state['last_session'] = _ZT16_SESSION
    observer = _zt16_path(memory)
    span = _ZT16_SESSION + ':' + _zr_hashlib.sha256(observer.encode()).hexdigest()[:12] + ':' + str(state['next_seq'])
    parent = _ZT16_STACK[-1] if _ZT16_STACK else None
    event = _zt16_event(state, 'start', sample, stage=stage, span=span,
                        parent_span=parent['span'] if parent else None,
                        parent_observer=parent['observer'] if parent else None,
                        elapsed_ns=0, cpu_elapsed_ns=0)
    state['open_spans'][span] = {'stage': stage, 'session': _ZT16_SESSION, 'start_event_seq': event['seq']}
    totals = state['totals'].setdefault(stage, {'started': 0, 'finished': 0, 'errors': 0, 'interrupted': 0,
        'unfinished_after_restart': 0, 'observed_elapsed_ns': 0, 'observed_cpu_ns': 0})
    totals['started'] += 1
    _zn_checkpoint(observer, state)
    return {'memory': os.path.abspath(memory), 'observer': observer, 'span': span, 'stage': stage,
            'session': _ZT16_SESSION, 'start': sample}


def _zt16_end(token, outcome='completed'):
    if token['session'] != _ZT16_SESSION:
        raise ValueError('Cannot time a span from a different process session')
    if outcome not in ('completed', 'error', 'interrupted'):
        raise ValueError('Unknown observed process outcome')
    state = _zt16_read(token['memory'])
    if token['span'] not in state['open_spans']:
        raise ValueError('Time span already closed or unavailable')
    sample = _zt16_sample()
    wall_elapsed = sample[0] - token['start'][0]
    elapsed = sample[1] - token['start'][1]
    cpu_elapsed = sample[2] - token['start'][2]
    if elapsed < 0 or cpu_elapsed < 0:
        raise ValueError('Timing counters moved backwards within a session')
    event = _zt16_event(state, 'finish', sample, stage=token['stage'], span=token['span'], outcome=outcome,
                        elapsed_ns=elapsed, cpu_elapsed_ns=cpu_elapsed, wall_elapsed_ns=wall_elapsed,
                        clock_delta_disagreement_ns=wall_elapsed - elapsed)
    state['open_spans'].pop(token['span'])
    totals = state['totals'][token['stage']]
    totals['finished'] += 1
    totals['errors'] += outcome == 'error'
    totals['interrupted'] += outcome == 'interrupted'
    totals['observed_elapsed_ns'] += elapsed
    totals['observed_cpu_ns'] += cpu_elapsed
    _zn_checkpoint(token['observer'], state)
    return event


class _zt16_span:
    """Observation failures do not change the engine's computation outcome."""
    def __init__(self, memory, stage):
        self.memory, self.stage, self.token, self.finished = memory, stage, None, None

    def warn(self, exc):
        path = _zt16_path(self.memory)
        if path not in _ZT16_WARNED:
            _ZT16_WARNED.add(path)
            print('Time observer unavailable; engine work continues:', str(exc))

    def __enter__(self):
        if TIME_OBSERVER_ENABLED:
            try:
                self.token = zero_core(None, 'time', operation='begin', operands=(self.memory, self.stage))
                _ZT16_STACK.append(self.token)
            except Exception as exc:
                self.warn(exc)
        return self

    def __exit__(self, kind, exc, traceback):
        if self.token is not None:
            try:
                outcome = 'interrupted' if kind is not None and issubclass(kind, KeyboardInterrupt) else 'error' if kind else 'completed'
                self.finished = zero_core(None, 'time', operation='end', operands=(self.token, outcome))
            except Exception as observer_error:
                self.warn(observer_error)
            finally:
                if _ZT16_STACK and _ZT16_STACK[-1] is self.token:
                    _ZT16_STACK.pop()
        return False


def _zt16_wrap(function, stage, path_selector):
    @_zt16_functools.wraps(function)
    def observed(*args, **kwargs):
        if not TIME_OBSERVER_ENABLED:
            return function(*args, **kwargs)
        with _zt16_span(path_selector(args, kwargs), stage):
            return function(*args, **kwargs)
    return observed


_zt16_previous_core = zero_core

def zero_core(m, domain, *, operation=None, operands=(), **kwargs):
    if domain == 'time':
        if operation == 'begin': return _zt16_begin(*operands)
        if operation == 'end': return _zt16_end(*operands)
        if operation == 'report': return _zt16_read(*operands)
        if operation == 'space': return _zt16_space(*operands)
        raise ValueError('Unsupported zero time observation')
    return _zt16_previous_core(m, domain, operation=operation, operands=operands, **kwargs)


# Coarse process spans avoid per-operation journal growth. None of these
# observations feed back into mathematical rules or queue selection.
load_memory = _zt16_wrap(load_memory, 'load_memory', lambda args, kwargs: memory_path())
save_memory = _zt16_wrap(save_memory, 'validate_and_save', lambda args, kwargs: memory_path())
work_roles = _zt16_wrap(work_roles, 'roles_exploration', lambda args, kwargs: memory_path())
work_calculus = _zt16_wrap(work_calculus, 'calculus_exploration', lambda args, kwargs: memory_path())
_zg_cycle = _zt16_wrap(_zg_cycle, 'adaptive_cycle', lambda args, kwargs: args[0])
_zg_recover = _zt16_wrap(_zg_recover, 'recovery_slice', lambda args, kwargs: args[0]['source_snapshot'])
_z7_retry = _zt16_wrap(_z7_retry, 'recovery_retry', lambda args, kwargs: args[0])
zero_verify_candidate = _zt16_wrap(zero_verify_candidate, 'candidate_verification', lambda args, kwargs: args[0])
zero_adaptive_recovery = _zt16_wrap(zero_adaptive_recovery, 'adaptive_recovery', lambda args, kwargs: args[0])
run = _zt16_wrap(run, 'process_including_queries', lambda args, kwargs: memory_path())


# The zero time clock has its own origin T0 and state transformations. Its
# logical states expand with accepted mathematical space; elapsed clocks are
# separate observations and do not generate or schedule these states.
ZERO_CLOCK_ENABLED = True
_ZT16_ZERO_CLOCK_RULE = 'independent_zero_time_clock_v1'


def _zt16_zero_path(memory):
    return os.path.abspath(memory) + '.zero-clock.json'


def _zt16_space_ids(memory):
    spaces = {'foundation': sorted(set(memory.get('foundation', {}).get('states', [])))}
    for domain in _ZR_DOMAINS:
        spaces[domain] = sorted({r['id'] for r in _zr_records(memory, domain)
                                 if type(r.get('id')) is int and r.get('status') != 'zero_recovery_pending'})
    return spaces


def _zt16_space(memory_path_value, memory, boundary):
    path = _zt16_zero_path(memory_path_value)
    current = _zt16_space_ids(memory)
    if os.path.isfile(path):
        clock = _zg_read(path)
        if (clock.get('rule') != _ZT16_ZERO_CLOCK_RULE or type(clock.get('tick')) is not int
                or set(clock.get('seen_ids', {})) != set(current)
                or clock.get('registered_states') != clock['tick'] + 1
                or sum(clock.get('coordinates', {}).values()) != clock['tick']):
            raise ValueError('Invalid independent zero clock; existing file preserved')
        growth = {d: sorted(set(ids) - set(clock['seen_ids'][d])) for d, ids in current.items()}
        delta = sum(len(ids) for ids in growth.values())
        if delta:
            before = clock['tick']
            contributions = []
            for domain, ids in growth.items():
                if not ids:
                    continue
                clock['seen_ids'][domain] = sorted(set(clock['seen_ids'][domain]).union(ids))
                clock['coordinates'][domain] += len(ids)
                contributions.append({'space': domain, 'count': len(ids), 'ids': ids})
            # Register a contiguous range of new clock states compactly.
            # Starting from 0, counting registered states yields 1, then 2, ...
            clock['tick'] = before + delta
            clock['registered_states'] = clock['tick'] + 1
            clock['events'].append({'seq': len(clock['events']) + 1, 'zero_reference': 'T0',
                'kind': 'expansion', 'from': before, 'to': clock['tick'],
                'transformation': 'count_registered_clock_states', 'growth': contributions,
                'coordinates': dict(clock['coordinates']), 'observation_boundary': boundary,
                'order_scope': 'one observed growth batch; no inferred construction interleaving'})
        clock['current_extent'] = {d: len(ids) for d, ids in current.items()}
    else:
        # An existing space establishes a new reference boundary, not an
        # invented history. A fresh engine begins here with its zero seed.
        extent = {d: len(ids) for d, ids in current.items()}
        clock = {'schema': 1, 'rule': _ZT16_ZERO_CLOCK_RULE,
                 'origin': 0, 'zero_reference': 'T0', 'source_zero_nexus': 'Z0',
                 'tick': 0, 'registered_states': 1, 'coordinates': {d: 0 for d in current},
                 'seen_ids': current, 'baseline_extent': extent, 'current_extent': extent,
                 'state_encoding': 'contiguous_integer_clock_states_0_through_tick',
                 'transformation': 'next_state_is_registered_clock_state_count',
                 'boundary': 'first observed valid space; no historical time backfill',
                 'scope': 'new foundation states and accepted archive IDs; includes representations',
                 'events': [{'seq': 1, 'zero_reference': 'T0', 'kind': 'origin', 'from': None, 'to': 0,
                             'observation_boundary': boundary}]}
    _zn_checkpoint(path, clock)
    return _zr_copy.deepcopy(clock)


def _zt16_observe_space_safely(path, memory, boundary):
    if not ZERO_CLOCK_ENABLED:
        return
    try:
        return zero_core(None, 'time', operation='space', operands=(path, memory, boundary))
    except Exception as exc:
        name = _zt16_zero_path(path)
        if name not in _ZT16_WARNED:
            _ZT16_WARNED.add(name)
            print('Zero clock unavailable; engine work continues:', str(exc))


_zt16_timed_load = load_memory
_zt16_timed_save = save_memory


def load_memory():
    memory = _zt16_timed_load()
    _zt16_observe_space_safely(memory_path(), memory, 'verified_load')
    return memory


def save_memory(memory):
    result = _zt16_timed_save(memory)
    _zt16_observe_space_safely(memory_path(), memory, 'committed_save')
    return result


def print_zero_clock_report(path):
    filename = _zt16_zero_path(path)
    if not os.path.isfile(filename):
        print('Zero clock has no observed space yet:', filename)
        return None
    clock = _zg_read(filename)
    print('ZERO TIME CLOCK | origin T0 = 0 | current state:', clock['tick'])
    print('Registered clock states:', clock['registered_states'])
    print('Space expansion coordinates:', clock['coordinates'])
    print('Current accepted-space extent:', clock['current_extent'])
    print('Logical units from observed space expansion; elapsed seconds are recorded separately.')
    return clock


def print_time_report(path):
    state = zero_core(None, 'time', operation='report', operands=(path,))
    print('EXACT TEMPORAL RECOVERY | Z0 |', _zt16_path(path))
    print('Events:', len(state['events']), '| open spans:', len(state['open_spans']))
    for stage, row in state['totals'].items():
        print(' ', stage, '| finished:', row['finished'], '| elapsed seconds:',
              round(row['observed_elapsed_ns'] / 1e9, 6), '| CPU seconds:', round(row['observed_cpu_ns'] / 1e9, 6))
    print('Inclusive stage durations overlap. Across restarts, only wall-clock gaps are recorded.')
    return state


_zt16_previous_query = query
_zt16_previous_query_v45 = query_v45

def query_v45(m, text):
    # Named clock commands must reach their handler before complex parsing.
    if text.strip().lower() in ('time', 'time-report', 'zero-clock', 'zero-time'):
        query(m, text)
        return True
    return _zt16_previous_query_v45(m, text)

def query(m, text):
    if text.strip().lower() in ('zero-clock', 'zero-time'):
        print_zero_clock_report(memory_path())
        return
    if text.strip().lower() in ('time', 'time-report'):
        print_time_report(memory_path())
        return
    return _zt16_previous_query(m, text)



_ZT17_WORKER_SOURCE = 'import copy\n\nRULE = \'zero_temporal_constraints_v4717\'\n\nMAX_COORDINATES = 64\n\nMAX_EVIDENCE = 512\n\ndef text(value):\n    if not isinstance(value, str) or not value:\n        raise ValueError(\'Expected nonempty identity string\')\n    return value\n\ndef integer(value):\n    if type(value) is not int:\n        raise ValueError(\'Times and bounds must be exact integers\')\n    return value\n\ndef zero_core(domain, *, operation, payload):\n    """Only public solver entry: validate and pass copies through typed Z0.\n\n    Identity passage preserves evidence. It supplies no missing information.\n    Every edge and inferred result records its passage; proof IDs refer to the\n    copied input evidence ledger. There is no hidden-reference argument.\n    """\n    if domain != \'temporal\' or operation not in (\'infer\', \'explore\'):\n        raise ValueError(\'Unsupported temporal gateway operation\')\n    data = copy.deepcopy(payload)\n    if operation == \'explore\':\n        return _explore(data)\n    return _infer(data)\n\ndef _infer(data):\n    if not isinstance(data, dict) or type(data.get(\'schema\')) is not int or data[\'schema\'] != 1:\n        raise ValueError(\'Expected temporal schema 1\')\n    clocks, events, evidence = data[\'clocks\'], data[\'events\'], data[\'evidence\']\n    if not isinstance(clocks, dict) or not isinstance(events, list) or not isinstance(evidence, list):\n        raise ValueError(\'Invalid ledger collections\')\n    if len(evidence) > MAX_EVIDENCE:\n        raise ValueError(\'Lab evidence limit exceeded\')\n    for clock_id, clock in clocks.items():\n        text(clock_id)\n        if clock[\'kind\'] not in (\'wall\', \'monotonic\', \'cpu\', \'logical\'):\n            raise ValueError(\'Unknown clock kind\')\n        for field in (\'unit\', \'session\', \'epoch\'):\n            text(clock[field])\n        # Each ID identifies a fixed unit/session/epoch. No implicit conversions.\n    nodes, identities, event_map = [], set(), {}\n    for event in events:\n        event_id = text(event[\'id\'])\n        if event_id in event_map:\n            raise ValueError(\'Duplicate event ID\')\n        if event[\'kind\'] not in (\'creation\', \'use\', \'operation\', \'boundary\'):\n            raise ValueError(\'Unknown event kind\')\n        if not isinstance(event[\'records\'], list):\n            raise ValueError(\'Expected typed record references\')\n        for record in event[\'records\']:\n            text(record[\'archive\'])\n            integer(record[\'id\'])\n            if record[\'id\'] < 0:\n                raise ValueError(\'Negative archive ID\')\n        if not isinstance(event[\'clocks\'], list) or not event[\'clocks\']:\n            raise ValueError(\'Expected event clock identities\')\n        for clock in event[\'clocks\']:\n            if clock not in clocks or (event_id, clock) in identities:\n                raise ValueError(\'Unknown or duplicate event clock\')\n            identities.add((event_id, clock))\n            nodes.append((event_id, clock))\n        event_map[event_id] = event\n    if len(nodes) > MAX_COORDINATES:\n        raise ValueError(\'Lab coordinate limit exceeded\')\n    # Node 0 is a mathematical reference for absolute bounds, not an observation.\n    indices = {node: i + 1 for i, node in enumerate(nodes)}\n    n = len(nodes) + 1\n    distances = [[None] * n for _ in range(n)]\n    proofs = [[[] for _ in range(n)] for _ in range(n)]\n    for i in range(n):\n        distances[i][i] = 0\n    passages = []\n    ledger, seen = [], set()\n\n    def endpoint(value):\n        key = (value[\'event\'], value[\'clock\'])\n        if key not in indices:\n            raise ValueError(\'Unknown event coordinate\')\n        return indices[key]\n\n    def edge(a, b, bound, evidence_id):\n        # x[b] - x[a] <= bound\n        current = distances[a][b]\n        if current is None or bound < current:\n            distances[a][b] = bound\n            proofs[a][b] = [evidence_id]\n        passages.append({\'zero_nexus\': \'Z0\', \'rule\': RULE,\n                         \'evidence\': evidence_id, \'effect\': \'identity_constraint_passage\'})\n\n    for row in evidence:\n        evidence_id = text(row[\'id\'])\n        if evidence_id in seen:\n            raise ValueError(\'Duplicate evidence ID\')\n        seen.add(evidence_id)\n        text(row[\'source\'])\n        ledger.append(row)\n        kind = row[\'kind\']\n        if kind == \'bound\':\n            target = endpoint(row[\'at\'])\n            lower, upper = row.get(\'lower\'), row.get(\'upper\')\n            if lower is None and upper is None:\n                raise ValueError(\'Empty bound evidence\')\n            if lower is not None:\n                edge(target, 0, -integer(lower), evidence_id)\n            if upper is not None:\n                edge(0, target, integer(upper), evidence_id)\n        elif kind in (\'difference\', \'bridge\'):\n            a, b = endpoint(row[\'a\']), endpoint(row[\'b\'])\n            ca, cb = row[\'a\'][\'clock\'], row[\'b\'][\'clock\']\n            if kind == \'difference\' and ca != cb:\n                raise ValueError(\'Cross-clock relation requires explicit bridge evidence\')\n            if kind == \'bridge\':\n                if ca == cb or clocks[ca][\'unit\'] != clocks[cb][\'unit\']:\n                    raise ValueError(\'Bridge requires distinct clocks with matching units\')\n            lower, upper = row.get(\'lower\'), row.get(\'upper\')\n            if lower is None and upper is None:\n                raise ValueError(\'Empty difference evidence\')\n            if lower is not None:\n                edge(b, a, -integer(lower), evidence_id)\n            if upper is not None:\n                edge(a, b, integer(upper), evidence_id)\n        else:\n            raise ValueError(\'Unknown evidence kind\')\n\n    # All-pairs difference-constraint closure. Integer arithmetic is exact.\n    # Caps make this O(n^3) experiment bounded on a phone.\n    for k in range(n):\n        for i in range(n):\n            if distances[i][k] is None:\n                continue\n            for j in range(n):\n                if distances[k][j] is None:\n                    continue\n                candidate = distances[i][k] + distances[k][j]\n                if distances[i][j] is None or candidate < distances[i][j]:\n                    distances[i][j] = candidate\n                    proofs[i][j] = list(dict.fromkeys(proofs[i][k] + proofs[k][j]))\n        conflicts = [i for i in range(n) if distances[i][i] < 0]\n        if conflicts:\n            return {\'schema\': 1, \'rule\': RULE, \'zero_nexus\': \'Z0\',\n                    \'status\': \'contradiction\', \'intervals\': [],\n                    \'conflict_evidence\': sorted({p for i in conflicts for p in proofs[i][i]}),\n                    \'evidence\': ledger, \'passages\': passages,\n                    \'note\': \'Conflicting evidence retained; no repaired timestamp accepted.\'}\n\n    intervals = []\n    for node, i in indices.items():\n        lower = None if distances[i][0] is None else -distances[i][0]\n        upper = distances[0][i]\n        status = (\'unknown\' if lower is None and upper is None else\n                  \'exact\' if lower is not None and lower == upper else \'bounded\')\n        intervals.append({\'event\': node[0], \'clock\': node[1], \'lower\': lower,\n                          \'upper\': upper, \'status\': status,\n                          \'lower_evidence\': proofs[i][0], \'upper_evidence\': proofs[0][i],\n                          \'zero_core_passage\': {\'zero_nexus\': \'Z0\', \'rule\': RULE,\n                                                \'effect\': \'derived_temporal_constraint\'}})\n    relations = []\n    for a, ai in indices.items():\n        for b, bi in indices.items():\n            if a >= b or a[1] != b[1]:\n                continue\n            lo = None if distances[bi][ai] is None else -distances[bi][ai]\n            hi = distances[ai][bi]\n            if lo is None and hi is None:\n                continue\n            relations.append({\'a\': a[0], \'b\': b[0], \'clock\': a[1],\n                              \'difference_lower\': lo, \'difference_upper\': hi,\n                              \'a_before_or_at_b\': lo is not None and lo >= 0,\n                              \'b_before_or_at_a\': hi is not None and hi <= 0,\n                              \'lower_evidence\': proofs[bi][ai],\n                              \'upper_evidence\': proofs[ai][bi],\n                              \'zero_nexus\': \'Z0\', \'rule\': RULE})\n    return {\'schema\': 1, \'rule\': RULE, \'zero_nexus\': \'Z0\', \'status\': \'consistent\',\n            \'intervals\': intervals, \'evidence\': ledger, \'passages\': passages,\n            \'clocks\': clocks, \'relative_constraints\': relations,\n            \'boundary\': \'Conditional on supplied evidence; no target, no historical backfill.\'}\n\ndef infer(data):\n    return zero_core(\'temporal\', operation=\'infer\', payload=data)\n\ndef explore(data, target, initial_ids, *, batch_size=2, max_batches=100):\n    """Process a finite surviving evidence queue; no hidden original is accepted.\n\n    An interval is unresolved. Exact support is accepted only after all supplied\n    evidence has been checked. Every pass computes full constraint closure for\n    the evidence inspected so far; repeating a pass alone adds no information.\n    """\n    return zero_core(\'temporal\', operation=\'explore\', payload={\n        \'data\': data, \'target\': target, \'initial_ids\': list(initial_ids),\n        \'batch_size\': batch_size, \'max_batches\': max_batches})\n\ndef _explore(request):\n    data = request[\'data\']\n    for key in (\'batch_size\', \'max_batches\'):\n        integer(request[key])\n        if request[key] < 1:\n            raise ValueError(\'Positive exploration budgets required\')\n    ids = [r[\'id\'] for r in data[\'evidence\']]\n    if len(set(ids)) != len(ids):\n        raise ValueError(\'Duplicate evidence ID\')\n    initial_ids = request[\'initial_ids\']\n    if len(set(initial_ids)) != len(initial_ids) or not set(initial_ids) <= set(ids):\n        raise ValueError(\'Invalid initial evidence IDs\')\n    # Preserve the supplied queue order; never schedule by the hidden answer.\n    active = [r for r in data[\'evidence\'] if r[\'id\'] in initial_ids]\n    pending = [r for r in data[\'evidence\'] if r[\'id\'] not in initial_ids]\n    history, batches = [], 0\n    while True:\n        current = dict(data, evidence=active)\n        result = infer(current)\n        if result[\'status\'] == \'contradiction\':\n            return {\'status\': \'contradiction\', \'accepted_timestamp\': None,\n                    \'trace\': history, \'result\': result,\n                    \'pending_evidence_ids\': [r[\'id\'] for r in pending]}\n        target = request[\'target\']\n        row = lookup(result, target[\'event\'], target[\'clock\'])\n        history.append({\'step\': batches, \'lower\': row[\'lower\'], \'upper\': row[\'upper\'],\n                        \'uniquely_supported\': row[\'status\'] == \'exact\',\n                        \'lower_evidence\': row[\'lower_evidence\'],\n                        \'upper_evidence\': row[\'upper_evidence\'],\n                        \'checked_evidence_count\': len(active),\n                        \'pending_evidence_count\': len(pending),\n                        \'zero_nexus\': \'Z0\', \'rule\': RULE})\n        if not pending or batches >= request[\'max_batches\']:\n            complete = not pending\n            accepted = complete and row[\'status\'] == \'exact\'\n            return {\'status\': \'exact_supported\' if accepted else \'unresolved\',\n                    \'accepted_timestamp\': row[\'lower\'] if accepted else None,\n                    \'stop_reason\': \'supplied_evidence_exhausted\' if complete else \'work_budget\',\n                    \'trace\': history, \'result\': result,\n                    \'pending_evidence_ids\': [r[\'id\'] for r in pending]}\n        count = request[\'batch_size\']\n        active = active + pending[:count]\n        pending = pending[count:]\n        batches += 1\n\ndef lookup(result, identity, clock_id=\'m\'):\n    return next(r for r in result[\'intervals\']\n                if (r[\'event\'], r[\'clock\']) == (identity, clock_id))'
_ZT17_SOLVER = {"__name__":"zero_temporal_worker"}
exec(compile(_ZT17_WORKER_SOURCE, "<zero-temporal-rules>", "exec"), _ZT17_SOLVER)

# V4.7.17 — temporal evidence through the shared Z0 gateway.
# This file is embedded before the engine entry point by build_revision.py.
import types as _zt17_types

TEMPORAL_RECORDING_ENABLED = True
TEMPORAL_MAX_EVENTS_PER_RUN = 1600
_ZT17_RULE = 'zero_temporal_observations_v4717'
_ZT17_CONTEXTS = {}
_ZT17_WARNED = set()


def _zt17_int(value, nonnegative=True):
    if type(value) is not int or (nonnegative and value < 0):
        raise ValueError('Invalid temporal integer')
    return value


def _zt17_validate_observer(state):
    """Replay ledger invariants without repairing or overwriting any bytes."""
    if (not isinstance(state, dict) or type(state.get('schema')) is not int
            or state['schema'] != 1 or state.get('rule') != _ZT16_RULE
            or state.get('zero_nexus') != 'Z0' or not isinstance(state.get('events'), list)):
        raise ValueError('Invalid time observer identity')
    opens, totals, starts = {}, {}, {}
    if not isinstance(state.get('totals'), dict):
        raise ValueError('Invalid process totals')
    for stage_totals in state['totals'].values():
        if not isinstance(stage_totals, dict):
            raise ValueError('Invalid process stage totals')
        for count in stage_totals.values():
            _zt17_int(count)
    previous_session = None
    for seq, row in enumerate(state['events'], 1):
        if (type(row.get('seq')) is not int or row['seq'] != seq
                or row.get('previous_event_seq') != (seq - 1 if seq > 1 else None)
                or row.get('zero_nexus') != 'Z0' or not isinstance(row.get('session'), str)
                or not row['session']):
            raise ValueError('Invalid time observer event sequence or identity')
        for key in ('monotonic_ns', 'process_cpu_ns'):
            _zt17_int(row.get(key))
        _zt17_int(row.get('wall_ns'), False)
        if row.get('utc') != _zt16_utc(row['wall_ns']):
            raise ValueError('UTC observation disagreement')
        kind = row.get('kind')
        session = row['session']
        if row.get('previous_event_seq') is not None:
            _zt17_int(row['previous_event_seq'])
        for field in ('elapsed_ns','cpu_elapsed_ns','wall_elapsed_ns','clock_delta_disagreement_ns','wall_gap_ns'):
            if field in row and row[field] is not None:
                _zt17_int(row[field], field in ('elapsed_ns','cpu_elapsed_ns'))
        if kind == 'session_boundary':
            if (previous_session is None or session == previous_session
                    or row.get('previous_session') != previous_session
                    or row.get('prior_unfinished_spans') != list(opens)
                    or row.get('elapsed_ns') is not None or row.get('cpu_elapsed_ns') is not None
                    or row.get('wall_gap_ns') != row['wall_ns'] - state['events'][seq-2]['wall_ns']):
                raise ValueError('Invalid process session boundary')
            for old in opens.values():
                totals[old['stage']]['unfinished_after_restart'] += 1
            opens = {}
        elif kind == 'start':
            if previous_session is not None and session != previous_session:
                raise ValueError('Missing process session boundary')
            span, stage = row.get('span'), row.get('stage')
            if (not isinstance(span, str) or not span or span in starts
                    or not isinstance(stage, str) or not stage
                    or row.get('elapsed_ns') != 0 or row.get('cpu_elapsed_ns') != 0
                    or row.get('parent_span') == span):
                raise ValueError('Invalid process span start')
            starts[span] = row
            opens[span] = {'stage': stage, 'session': session, 'start_event_seq': seq}
            total = totals.setdefault(stage, {'started': 0, 'finished': 0, 'errors': 0,
                'interrupted': 0, 'unfinished_after_restart': 0,
                'observed_elapsed_ns': 0, 'observed_cpu_ns': 0})
            total['started'] += 1
        elif kind == 'finish':
            span = row.get('span')
            if span not in opens or row.get('outcome') not in ('completed', 'error', 'interrupted'):
                raise ValueError('Invalid process span finish')
            start = starts[span]
            if session != start['session'] or row.get('stage') != start['stage']:
                raise ValueError('Process span linkage disagreement')
            elapsed = row['monotonic_ns'] - start['monotonic_ns']
            cpu = row['process_cpu_ns'] - start['process_cpu_ns']
            wall = row['wall_ns'] - start['wall_ns']
            if (elapsed < 0 or cpu < 0 or row.get('elapsed_ns') != elapsed
                    or row.get('cpu_elapsed_ns') != cpu or row.get('wall_elapsed_ns') != wall
                    or row.get('clock_delta_disagreement_ns') != wall - elapsed):
                raise ValueError('Process duration disagreement')
            opens.pop(span)
            total = totals[start['stage']]
            total['finished'] += 1
            total['errors'] += row['outcome'] == 'error'
            total['interrupted'] += row['outcome'] == 'interrupted'
            total['observed_elapsed_ns'] += elapsed
            total['observed_cpu_ns'] += cpu
        else:
            raise ValueError('Unknown process event kind')
        previous_session = session
    if (type(state.get('next_seq')) is not int or state['next_seq'] != len(state['events']) + 1
            or state.get('last_session') != previous_session
            or state.get('open_spans') != opens or state.get('totals') != totals
            or state.get('clock_sources') != {'wall': 'system_UTC', 'elapsed': 'monotonic_ns', 'cpu': 'process_time_ns'}):
        raise ValueError('Time observer derived totals or links disagree')
    return state


def _zt17_validate_space(clock):
    domains = {'foundation', *_ZR_DOMAINS}
    if (not isinstance(clock, dict) or type(clock.get('schema')) is not int or clock['schema'] != 1
            or clock.get('rule') != _ZT16_ZERO_CLOCK_RULE or type(clock.get('origin')) is not int
            or clock['origin'] != 0 or clock.get('zero_reference') != 'T0'
            or clock.get('source_zero_nexus') != 'Z0'):
        raise ValueError('Invalid zero-clock origin')
    tick = _zt17_int(clock.get('tick'))
    _zt17_int(clock.get('registered_states'))
    if clock['registered_states'] != tick + 1:
        raise ValueError('Invalid registered zero-clock states')
    for key in ('coordinates', 'seen_ids', 'baseline_extent', 'current_extent'):
        if not isinstance(clock.get(key), dict) or set(clock[key]) != domains:
            raise ValueError('Invalid zero-clock domain keys')
    for domain in domains:
        ids = clock['seen_ids'][domain]
        if not isinstance(ids, list) or any(type(i) is not int or i < 0 for i in ids) or ids != sorted(set(ids)):
            raise ValueError('Invalid zero-clock ID collection')
        coordinate = _zt17_int(clock['coordinates'][domain])
        baseline = _zt17_int(clock['baseline_extent'][domain])
        extent = _zt17_int(clock['current_extent'][domain])
        if len(ids) != baseline + coordinate or extent > len(ids):
            raise ValueError('Zero-clock extent disagreement')
    if sum(clock['coordinates'].values()) != tick or not isinstance(clock.get('events'), list) or not clock['events']:
        raise ValueError('Invalid zero-clock totals')
    prior, growth_counts, grown_ids = 0, {d: 0 for d in domains}, {d: set() for d in domains}
    for seq, row in enumerate(clock['events'], 1):
        if type(row.get('seq')) is not int or row['seq'] != seq or row.get('zero_reference') != 'T0':
            raise ValueError('Invalid zero-clock event sequence')
        _zt17_int(row.get('to'))
        if seq == 1:
            if row.get('kind') != 'origin' or row.get('from') is not None or row.get('to') != 0:
                raise ValueError('Missing zero-clock origin event')
            continue
        if row.get('kind') != 'expansion' or row.get('from') != prior or not isinstance(row.get('growth'), list):
            raise ValueError('Invalid zero-clock expansion link')
        _zt17_int(row.get('from'))
        batch_domains, delta = set(), 0
        for part in row['growth']:
            d, ids = part.get('space'), part.get('ids')
            _zt17_int(part.get('count'))
            if d not in domains or d in batch_domains or not isinstance(ids, list) or not ids:
                raise ValueError('Invalid zero-clock growth batch')
            if any(type(i) is not int or i < 0 for i in ids) or ids != sorted(set(ids)):
                raise ValueError('Invalid zero-clock growth IDs')
            if (part.get('count') != len(ids) or grown_ids[d].intersection(ids)
                    or not set(ids) <= set(clock['seen_ids'][d])):
                raise ValueError('Repeated or mismatched zero-clock growth')
            batch_domains.add(d)
            grown_ids[d].update(ids)
            growth_counts[d] += len(ids)
            delta += len(ids)
        if (not delta or row.get('to') != prior + delta or row.get('coordinates') != growth_counts
                or row.get('transformation') != 'count_registered_clock_states'):
            raise ValueError('Zero-clock expansion totals disagree')
        prior += delta
    if prior != tick or growth_counts != clock['coordinates']:
        raise ValueError('Zero-clock event history disagrees with totals')
    return clock


_zt17_previous_read = _zt16_read
def _zt16_read(memory):
    return _zt17_validate_observer(_zt17_previous_read(memory))


_zt17_previous_space = _zt16_space
def _zt16_space(path, memory, boundary):
    name = _zt16_zero_path(path)
    if os.path.exists(name):
        _zt17_validate_space(_zg_read(name))
    return _zt17_validate_space(_zt17_previous_space(path, memory, boundary))


def print_zero_clock_report(path):
    name = _zt16_zero_path(path)
    if not os.path.isfile(name):
        print('Zero clock has no observed space yet:', name)
        return None
    clock = _zt17_validate_space(_zg_read(name))
    print('ZERO TIME CLOCK | origin T0 = 0 | current state:', clock['tick'])
    print('Registered clock states:', clock['registered_states'])
    print('Space expansion coordinates:', clock['coordinates'])
    print('Current accepted-space extent:', clock['current_extent'])
    return clock


def _zt17_path(path):
    return os.path.abspath(path) + '.temporal.json'


def _zt17_new_ledger(path):
    return {'schema': 1, 'rule': _ZT17_RULE, 'zero_nexus': 'Z0',
            'memory_path': os.path.abspath(path), 'next_seq': 1, 'events': [],
            'batches': [], 'gaps': [],
            'boundary': 'new acceptance observations only; prior creation times unknown',
            'logical_clock': 'Z0-origin observed acceptance-event count; distinct from space-growth clock'}


def _zt17_validate_records(state, *, missing=None):
    if (not isinstance(state, dict) or type(state.get('schema')) is not int or state['schema'] != 1
            or state.get('rule') != _ZT17_RULE or state.get('zero_nexus') != 'Z0'
            or not isinstance(state.get('memory_path'), str) or not isinstance(state.get('events'), list)
            or not isinstance(state.get('batches'), list) or not isinstance(state.get('gaps'), list)):
        raise ValueError('Invalid temporal observation ledger')
    previous = None
    all_refs = set()
    samples = ('wall_ns', 'monotonic_ns', 'process_cpu_ns')
    for seq, row in enumerate(state['events'], 1):
        if (type(row.get('seq')) is not int or row['seq'] != seq
                or row.get('previous_event_seq') != (seq-1 if seq > 1 else None)
                or row.get('zero_nexus') != 'Z0' or row.get('kind') != 'acceptance'
                or not isinstance(row.get('session'), str) or not row['session']
                or type(row.get('logical_tick')) is not int or row['logical_tick'] != seq
                or not isinstance(row.get('uses'), list)):
            raise ValueError('Invalid temporal event identity')
        record = row.get('record', {})
        for digest_key in ('record_digest', 'observed_record_digest'):
            digest = row.get(digest_key)
            if not isinstance(digest, str) or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
                raise ValueError('Invalid temporal record fingerprint')
        if record.get('archive') not in _ZR_DOMAINS:
            raise ValueError('Invalid temporal archive reference')
        _zt17_int(record.get('id'))
        key = (row['batch'], record['archive'], record['id'])
        if key in all_refs:
            raise ValueError('Duplicate observed acceptance in one commit batch')
        all_refs.add(key)
        for use in row['uses']:
            if use.get('archive') not in _ZR_DOMAINS:
                raise ValueError('Invalid temporal use reference')
            _zt17_int(use.get('id'))
            digest=use.get('record_digest')
            if not isinstance(digest,str) or len(digest)!=64:
                raise ValueError('Missing temporal use identity fingerprint')
        for field in samples:
            if missing != (seq, field):
                _zt17_int(row.get(field), field != 'wall_ns')
        delta = row.get('delta_from_previous')
        if previous is None or previous['session'] != row['session']:
            if delta is not None:
                raise ValueError('Cannot subtract temporal clocks across sessions')
        else:
            if delta is not None and (not isinstance(delta, dict) or set(delta) != set(samples)):
                raise ValueError('Missing temporal difference evidence')
            for field in samples:
                if delta is not None:
                    _zt17_int(delta[field], field != 'wall_ns')
                if missing not in ((seq, field), (seq-1, field)):
                    actual=row[field]-previous[field]
                    if (delta is not None and actual != delta[field]) or (field!='wall_ns' and actual<0):
                        raise ValueError('Temporal sample/difference contradiction')
        previous = row
    if type(state.get('next_seq')) is not int or state['next_seq'] != len(state['events']) + 1:
        raise ValueError('Invalid temporal next sequence')
    expected_start = 1
    batch_ids = set()
    for batch in state['batches']:
        if (type(batch.get('from_seq')) is not int or batch['from_seq'] != expected_start
                or not isinstance(batch.get('id'), str) or not batch['id'] or batch['id'] in batch_ids
                or type(batch.get('to_seq')) is not int
                or not expected_start <= batch['to_seq'] < state['next_seq']
                or not isinstance(batch.get('memory_sha256'), str) or len(batch['memory_sha256']) != 64):
            raise ValueError('Invalid committed temporal batch')
        batch_ids.add(batch['id'])
        for row in state['events'][expected_start-1:batch['to_seq']]:
            if row.get('batch') != batch.get('id'):
                raise ValueError('Temporal event batch mismatch')
        expected_start = batch['to_seq'] + 1
    if expected_start != state['next_seq']:
        raise ValueError('Uncommitted temporal observations')
    return state


def _zt17_begin_records(memory, path):
    if not TEMPORAL_RECORDING_ENABLED or not TIME_OBSERVER_ENABLED:
        return
    path = os.path.abspath(path)
    name = _zt17_path(path)
    try:
        state = _zt17_validate_records(_zg_read(name)) if os.path.exists(name) else _zt17_new_ledger(path)
        if state['memory_path'] != path:
            raise ValueError('Temporal memory-path binding mismatch')
        if state['batches'] and os.path.isfile(path) and state['batches'][-1]['memory_sha256'] != _z7_hash_file(path):
            # New external archive boundary: preserve history and mark the gap.
            state['gaps'].append({'after_seq': state['next_seq']-1,
                                 'reason': 'memory changed outside the recorded commit boundary'})
        _ZT17_CONTEXTS[id(memory)] = {'memory': memory, 'path': path, 'state': state,
            'new': [], 'payloads': {}, 'batch': _zt16_uuid.uuid4().hex, 'dropped': 0}
    except Exception as exc:
        _zt17_warn(path, exc)
        # A missing single timestamp can be proposed automatically. The damaged
        # history remains preserved; a candidate never becomes implicit evidence.
        try:
            if os.path.exists(name):
                damaged = _zg_read(name)
                missing = [(row.get('seq'), field) for row in damaged.get('events', [])
                           for field in ('wall_ns','monotonic_ns','process_cpu_ns')
                           if row.get(field) is None]
                if len(missing) == 1:
                    seq, field = missing[0]
                    zero_core(None, 'temporal', operation='recover', operands=(name,seq,field))
        except Exception as recovery_error:
            _zt17_warn(path + ':recovery', recovery_error)


def _zt17_warn(path, exc):
    if path not in _ZT17_WARNED:
        _ZT17_WARNED.add(path)
        print('Temporal observation unavailable; mathematical work continues:', str(exc))


def _zt17_accept(memory, domain, record):
    context = _ZT17_CONTEXTS.get(id(memory))
    if context is None or context['memory'] is not memory:
        return
    if len(context['new']) >= TEMPORAL_MAX_EVENTS_PER_RUN:
        context['dropped'] += 1
        return
    state = context['state']
    seq = state['next_seq'] + len(context['new'])
    previous = context['new'][-1] if context['new'] else (state['events'][-1] if state['events'] else None)
    uses = [{'archive': domain, 'id': p} for p in record.get('parents', [])]
    uses.extend(_zr_copy.deepcopy(record.get('sources', [])))
    samples = dict(zip(('wall_ns', 'monotonic_ns', 'process_cpu_ns'),
                       (time.time_ns(), time.monotonic_ns(), time.process_time_ns())))
    delta = ({k: samples[k] - previous[k] for k in samples}
             if previous and previous['session'] == _ZT16_SESSION else None)
    row = {'seq': seq, 'previous_event_seq': seq-1 if seq > 1 else None,
           'zero_nexus': 'Z0', 'kind': 'acceptance', 'session': _ZT16_SESSION,
           'batch': context['batch'], 'record': {'archive': domain, 'id': record['id']},
           'record_digest': _zr_digest(_zr_payload(record)), 'uses': uses,
           'logical_tick': seq, 'delta_from_previous': delta, **samples}
    context['new'].append(row)
    context['payloads'][seq] = _zr_copy.deepcopy(_zr_payload(record))


def _zt17_commit_records(memory):
    context = _ZT17_CONTEXTS.pop(id(memory), None)
    if context is None or context['memory'] is not memory or not context['new']:
        return
    path, state = context['path'], context['state']
    try:
        # Commit only if every recorded acceptance really exists in saved math.
        archives = {d:{r['id']:r for r in _zr_records(memory,d)} for d in _ZR_DOMAINS}
        for row in context['new']:
            ref = row['record']
            rec = archives[ref['archive']].get(ref['id'])
            before = context['payloads'][row['seq']]
            after = _zr_payload(rec) if rec is not None else {}
            # Some workers add construction annotations after their zero gate.
            # Preserve the gate digest and separately bind the completed record.
            if rec is None or any(key not in after or after[key] != value for key,value in before.items()):
                raise ValueError('Observed record does not match committed archive')
            row['observed_record_digest'] = row['record_digest']
            row['record_digest'] = _zr_digest(after)
            for use in row['uses']:
                parent=archives[use['archive']].get(use['id'])
                if parent is None:
                    raise ValueError('Observed use has no committed source record')
                use['record_digest']=_zr_digest(_zr_payload(parent))
        start = state['next_seq']
        state['events'].extend(context['new'])
        state['next_seq'] += len(context['new'])
        state['batches'].append({'id': context['batch'], 'from_seq': start,
            'to_seq': state['next_seq']-1, 'memory_sha256': _z7_hash_file(path)})
        if context['dropped']:
            state['gaps'].append({'after_seq': state['next_seq']-1,
                                 'reason': 'observation work cap', 'unobserved_acceptances': context['dropped']})
        _zt17_validate_records(state)
        _zn_checkpoint(_zt17_path(path), state)
    except Exception as exc:
        _zt17_warn(path, exc)


def _zt17_recover(path, seq, field):
    """Exact-only proposal; source and mathematical memory are never written."""
    if field not in ('wall_ns', 'monotonic_ns', 'process_cpu_ns'):
        raise ValueError('Supported fields: wall_ns, monotonic_ns, process_cpu_ns')
    _zt17_int(seq)
    state = _zg_read(path)
    if seq < 1 or seq > len(state.get('events', [])):
        raise ValueError('Unknown temporal event sequence')
    row = state['events'][seq-1]
    if field in row and row[field] is not None:
        raise ValueError('Requested timestamp is present; mask it in a disposable copy first')
    _zt17_validate_records(state, missing=(seq, field))
    # A two-neighbour component is sufficient for stored adjacent-delta evidence.
    # The final full-ledger validation prevents local consistency hiding a conflict.
    selected_ids = set(range(max(1,seq-1),min(len(state['events']),seq+1)+1))
    creators, causal_links = {}, []
    for item in state['events']:
        for use in item['uses']:
            key=(use['archive'],use['id'],use['record_digest'])
            parent=creators.get(key)
            if parent is not None:
                causal_links.append((parent,item['seq']))
        ref=item['record']
        creators[ref['archive'],ref['id'],item['record_digest']]=item['seq']
    # Follow recorded creation/use links while keeping the local solver bounded.
    for a,b in causal_links:
        if (a in selected_ids or b in selected_ids) and len(selected_ids)<48:
            selected_ids.update((a,b))
    selected=[r for r in state['events'] if r['seq'] in selected_ids]
    clocks, events, evidence = {}, [], []
    for item in selected:
        identity = str(item['seq'])
        c = item['session'] + ':' + field
        clocks[c] = {'kind': {'wall_ns':'wall', 'monotonic_ns':'monotonic', 'process_cpu_ns':'cpu'}[field],
                     'unit': 'ns', 'session': item['session'], 'epoch': item['session']}
        events.append({'id': identity, 'kind': 'creation', 'clocks': [c], 'records': [item['record']]})
        if item.get(field) is not None:
            evidence.append({'id': 'stamp:'+identity, 'kind': 'bound', 'at': {'event':identity, 'clock':c},
                             'lower':item[field], 'upper':item[field], 'source':'surviving recorded sample'})
    for item in selected:
        if item['seq']-1 in selected_ids and state['events'][item['seq']-2]['session']==item['session']:
            c = item['session'] + ':' + field
            delta = item['delta_from_previous']
            if delta is not None or field!='wall_ns':
                evidence.append({'id':'delta:'+str(item['seq']), 'kind':'difference',
                    'a':{'event':str(item['seq']-1), 'clock':c},
                    'b':{'event':str(item['seq']), 'clock':c},
                    'lower':delta[field] if delta is not None else 0,
                    'upper':delta[field] if delta is not None else None,
                    'source':'surviving adjacent difference' if delta is not None else 'recorded sequential observation order'})
    if field!='wall_ns':
        for a,b in causal_links:
            if a in selected_ids and b in selected_ids:
                ra,rb=state['events'][a-1],state['events'][b-1]
                if ra['session']==rb['session']:
                    c=ra['session']+':'+field
                    evidence.append({'id':'use:'+str(a)+':'+str(b),'kind':'difference',
                        'a':{'event':str(a),'clock':c},'b':{'event':str(b),'clock':c},
                        'lower':0,'upper':None,'source':'recorded typed source acceptance before its use'})
    # Several parents may repeat a link; keep one evidence identity per link.
    evidence=list({entry['id']:entry for entry in evidence}.values())
    data = {'schema':1, 'clocks':clocks, 'events':events, 'evidence':evidence}
    result = zero_core(None, 'temporal', operation='explore', operands=({
        'data':data, 'target':{'event':str(seq), 'clock':row['session']+':'+field},
        'initial_ids':[], 'batch_size':2, 'max_batches':100},))
    report = {'schema':1, 'rule':_ZT17_RULE, 'zero_nexus':'Z0',
              'source_sha256':_z7_hash_file(path), 'source_preserved':True,
              'target':{'seq':seq, 'field':field}, 'inference':result,
              'status':result['status'], 'historical_identity_proven':False}
    if result['status'] == 'exact_supported':
        candidate = _zr_copy.deepcopy(state)
        candidate['events'][seq-1][field] = result['accepted_timestamp']
        _zt17_validate_records(candidate)
        candidate_path = path + '.time-candidate.json'
        if os.path.exists(candidate_path):
            if _zg_read(candidate_path) != candidate:
                raise ValueError('Different temporal candidate already exists; preserved')
        else:
            # Exclusive create protects existing candidates; never promote automatically.
            with open(candidate_path, 'x', encoding='utf-8') as stream:
                json.dump(candidate, stream, indent=2)
        report['candidate'] = candidate_path
        report['accepted_timestamp'] = result['accepted_timestamp']
    _zn_checkpoint(path + '.time-recovery-report.json', report)
    print('Temporal recovery:', report['status'], '| timestamp:', report.get('accepted_timestamp'),
          '| source preserved; candidate is separate.')
    return report


_zt17_previous_core = zero_core
def zero_core(m, domain, *, operation=None, operands=(), **kwargs):
    if domain == 'temporal':
        if operation == 'infer':
            return _ZT17_SOLVER['_infer'](_zr_copy.deepcopy(operands[0]))
        if operation == 'explore':
            return _ZT17_SOLVER['_explore'](_zr_copy.deepcopy(operands[0]))
        if operation == 'recover':
            return _zt17_recover(*operands)
        raise ValueError('Unsupported shared-zero temporal operation')
    record = kwargs.get('record')
    fresh = (m is not None and domain in _ZR_DOMAINS and record is not None
             and record.get('zero_core_passage') is None and not kwargs.get('historical', False))
    result = _zt17_previous_core(m, domain, operation=operation, operands=operands, **kwargs)
    if fresh:
        try:
            _zt17_accept(m, domain, record)
        except Exception as exc:
            _zt17_warn(memory_path(), exc)
    return result


# Repeated inference passes re-enter the engine's actual gateway.
_ZT17_SOLVER['zero_core'] = lambda domain, *, operation, payload: zero_core(
    None, domain, operation=operation, operands=(payload,))

_zt17_previous_load = load_memory
def load_memory():
    memory = _zt17_previous_load()
    _zt17_begin_records(memory, memory_path())
    return memory

_zt17_previous_save = save_memory
def save_memory(memory):
    result = _zt17_previous_save(memory)
    _zt17_commit_records(memory)
    return result


def _zt17_code_identity(code):
    return [code.co_code.hex(), code.co_names, code.co_varnames, code.co_argcount,
            code.co_kwonlyargcount, code.co_posonlyargcount, code.co_flags,
            code.co_freevars, code.co_cellvars,
            [_zt17_code_identity(c) if isinstance(c, _zt17_types.CodeType) else
             (sorted(map(repr,c)) if isinstance(c,frozenset) else repr(c)) for c in code.co_consts]]


def _z7_rules_signature():
    # Loaded function code + scalar rule/configuration constants. No __file__,
    # launcher path, filenames, source line numbers, timestamps, or session IDs.
    functions = _ZT17_LOADED_FUNCTION_IDENTITIES
    config = {name:value for name,value in globals().items() if name.isupper()
              and name not in ('_ZT16_SESSION','_ZT17_WORKER_SOURCE')
              and isinstance(value,(str,int,float,bool,tuple))}
    return _zr_digest({'functions':functions, 'config':config, 'temporal_worker':_ZT17_WORKER_SOURCE})


_zt17_previous_query = query
_zt17_previous_query_v45 = query_v45
def query_v45(m, text):
    if text.strip().lower() == 'temporal' or text.strip().lower().startswith('temporal-recover '):
        query(m, text)
        return True
    return _zt17_previous_query_v45(m, text)

def query(m, text):
    if text.strip().lower().startswith('temporal-recover '):
        parts = text.split()
        if len(parts) != 3:
            raise ValueError('Usage: temporal-recover SEQ FIELD')
        return zero_core(None,'temporal',operation='recover',operands=(
            _zt17_path(memory_path()),int(parts[1]),parts[2]))
    if text.strip().lower() == 'temporal':
        path = _zt17_path(memory_path())
        if not os.path.exists(path):
            print('No committed temporal acceptance observations yet; prior creation times remain unknown.')
            return
        state = _zt17_validate_records(_zg_read(path))
        print('ZERO TEMPORAL | Z0 | events:',len(state['events']),'| gaps:',len(state['gaps']))
        print('Creation/use links observed at acceptance; exact-only recovery, no historical backfill.')
        return state
    return _zt17_previous_query(m, text)


# Bind code identity when this engine is loaded. Temporary instrumentation and
# mocks are not executable-source revisions. Reloading edited engine code creates
# a new identity even when a launcher's __file__ remains unchanged.
_ZT17_LOADED_FUNCTION_IDENTITIES = {'module':_zt17_code_identity(_ZT17_MODULE_CODE)}



# ============================================================
# V4.8 EXPERIMENTAL INTEGRATED OPERATION DISCOVERY
# Entire engine continues unchanged; discovery follows committed saves.
# A separate memory lineage protects the original V4.7.17 archive.
# ============================================================
MEMORY_FILENAME = 'zero_theorem_v497_slot_memory.json'

"""Zero Theorem operation-discovery worker (experimental, read-only input).

Reads an existing V4.7.17 JSON archive; writes ONLY a separate candidate sidecar.
Does not import/run the engine, modify archives, or trust candidate operations.
Run: python zero_operation_discovery_worker.py PATH_TO_MEMORY.json
"""
import json
import os
import sys
from collections import defaultdict
from fractions import Fraction

RULE = "zero_operation_discovery_v1"
MAX_SCAN = 30000
MAX_CANDIDATES = 2000


def fingerprint(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def flatten_add(tree):
    if not isinstance(tree, dict):
        return None
    if tree.get("op") == "+" and "left" in tree and "right" in tree:
        a, b = flatten_add(tree["left"]), flatten_add(tree["right"])
        return None if a is None or b is None else a + b
    if "leaf" in tree:
        return [tree]
    return [tree]  # Treat a non-add subtree as an indivisible repeated term.


def candidate_for(record):
    tree = record.get("tree")
    if not isinstance(tree, dict) or tree.get("op") != "+":
        return None
    terms = flatten_add(tree)
    if not terms or len(terms) < 2:
        return None
    key = fingerprint(terms[0])
    if any(fingerprint(term) != key for term in terms[1:]):
        return None
    try:
        observed = Fraction(str(record["value"]))
    except (ValueError, TypeError, KeyError, ZeroDivisionError):
        return None
    return {"operation": "repeat", "term": terms[0],
            "count": len(terms), "observed_value": str(observed),
            "source_ids": [record["id"]], "status": "untrusted",
            "rule": RULE, "nexus": "Z0",
            "verification": "pattern_observation_only"}


def _integrated_discover(memory):
    if not isinstance(memory, dict) or not isinstance(memory.get("expressions"), list):
        raise ValueError("Expected Zero Theorem memory with expressions list")
    records = memory["expressions"]
    findings = []
    seen = set()
    for rec in records[:MAX_SCAN]:
        if not isinstance(rec, dict) or not isinstance(rec.get("id"), int):
            continue
        proposal = candidate_for(rec)
        if proposal is None:
            continue
        key = (fingerprint(proposal["term"]), proposal["count"], tuple(proposal["source_ids"]))
        if key in seen:
            continue
        seen.add(key)
        findings.append(proposal)
        if len(findings) >= MAX_CANDIDATES:
            break
    by_shape = defaultdict(list)
    for idx, proposal in enumerate(findings):
        by_shape[(fingerprint(proposal["term"]), proposal["count"])].append(idx)
    relationships = [
        {"candidate_indices": ids, "kind": "shared_repetition_structure",
         "nexus": "Z0", "status": "untrusted"}
        for ids in by_shape.values() if len(ids) > 1
    ]
    return {"schema": 1, "rule": RULE, "nexus": "Z0",
            "source_records_scanned": min(len(records), MAX_SCAN),
            "source_records_total": len(records),
            "scan_complete": len(records) <= MAX_SCAN,
            "candidate_limit_reached": len(findings) >= MAX_CANDIDATES,
            "candidates": findings, "relationships": relationships,
            "trusted_rules_added": 0, "source_unchanged": True,
            "note": "Read-only candidate extraction; not independent operation invention or proof."}



_zt48_previous_save_memory = save_memory

def save_memory(memory):
    # Preserve the engine's original save, clocks, recovery and temporal hooks.
    result = _zt48_previous_save_memory(memory)
    try:
        report = _integrated_discover(memory)
        # Verify observed repetition arithmetically without promoting rules.
        checked = []
        for candidate in report['candidates']:
            term = candidate['term']
            if 'leaf' in term:
                try:
                    expected = Fraction(str(term['leaf'])) * candidate['count']
                    observed = Fraction(candidate['observed_value'])
                    candidate['arithmetic_consistent'] = expected == observed
                except (ValueError, TypeError, ZeroDivisionError):
                    candidate['arithmetic_consistent'] = False
            else:
                candidate['arithmetic_consistent'] = None
            checked.append(candidate)
        report['integration'] = 'v48_experimental_same_run_after_save'
        report['promotion'] = 'none; all candidates remain untrusted'
        report['new_candidates'] = len(checked)
        destination = memory_path() + '.operation-discovery-candidates.json'
        temp = destination + '.tmp'
        with open(temp, 'w', encoding='utf-8') as handle:
            json.dump(report, handle, indent=2)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, destination)
        print('Z0 integrated discovery | scanned:', report['source_records_scanned'],
              '| candidates:', len(checked), '| relationships:', len(report['relationships']))
        print('Untrusted candidates saved separately:', destination)
    except Exception as exc:
        print('Z0 discovery deferred; committed engine memory preserved:', str(exc))
    return result


# ============================================================
# V4.9 EXPERIMENTAL — ENERGY THROUGH Z0
# Reuses rational constructions, time/space metadata and provenance.
# Records ALL four formal branches; does not assert physical laws.
# Energy is an observational role, not a replacement arithmetic kernel.
# ============================================================
_ZE_RULE = 'energy_through_zero_v1'
_ZE_BRANCHES = ('+1', '-1', '+i', '-i')
_ZE_BATCH = 32  # processing budget only; unvisited records remain queued
_ZE_ENERGY_SEED = '1'  # dimensionless exploratory energy token, NOT joules

def _ze_atomic_json(path, data):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)

def _ze_sidecar_path():
    return memory_path() + '.energy-pathways.json'

def _ze_record_signature(record):
    import hashlib
    payload = json.dumps(record, sort_keys=True, separators=(',', ':'), default=str)
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()

def _ze_integrate(memory):
    """Record observational energy pathways from existing Z0 rational constructions.
    Four distinct formal transformations are preserved even if results coincide.
    No candidate is promoted to a physical law or trusted arithmetic operation.
    """
    from fractions import Fraction
    path = _ze_sidecar_path()
    if os.path.isfile(path):
        with open(path, encoding='utf-8') as f:
            state = json.load(f)
        if state.get('rule') != _ZE_RULE or state.get('nexus') != 'Z0':
            raise ValueError('Unrecognized energy sidecar; refusing to overwrite')
    else:
        state = {'schema': 1, 'rule': _ZE_RULE, 'nexus': 'Z0',
                 'energy_seed': {'value': _ZE_ENERGY_SEED, 'unit': 'formal',
                                 'physical_unit_assigned': False},
                 'pathways': [], 'next_source_index': 0,
                 'physical_laws_proven': False,
                 'note': 'Exploratory formal energy roles, not validated physics.'}
    records = memory.get('expressions', [])
    cursor = state['next_source_index']
    end = min(cursor + _ZE_BATCH, len(records))
    for index in range(cursor, end):
        source = records[index]
        if not isinstance(source, dict):
            continue
        base = {'nexus': 'Z0', 'rule': _ZE_RULE,
                'source_archive': 'rational', 'source_index': index,
                'source_id': source.get('id'), 'source_digest': _ze_record_signature(source),
                'source_tree': source.get('tree'), 'source_parents': source.get('parents'),
                'source_ancestry': source.get('ancestry'),
                'source_zero_passage': source.get('zero_core_passage'),
                'source_observer': source.get('observer'),
                'source_spatial': source.get('spatial'),
                'source_temporal': source.get('temporal'),
                'energy_role': 'formal_observation', 'physical_status': 'unverified'}
        for branch in _ZE_BRANCHES:
            event = dict(base)
            event['path_id'] = 'ZE:%s:%s' % (index, branch)
            event['branch'] = branch
            event['energy_input'] = _ZE_ENERGY_SEED
            try:
                value = Fraction(str(source['value']))
                real, imag = _pr_energy_step(value, Fraction(0), branch, memory)
                event['primitive_jobs'] = [p['job'] for p in memory['primitive_reduction']['passages'][-1:]]
                event['formal_output'] = {'real': str(real), 'imag': str(imag)}
                event['status'] = 'candidate_observation'
            except (ValueError, KeyError, TypeError, ZeroDivisionError) as exc:
                event['formal_output'] = None
                event['status'] = 'blocked'
                event['block_reason'] = type(exc).__name__
            state['pathways'].append(event)
    state['next_source_index'] = end
    state['source_records_available'] = len(records)
    state['pending_source_records'] = max(0, len(records)-end)
    state['total_pathways_preserved'] = len(state['pathways'])
    state['engine_runs_observed'] = memory.get('runs')
    _ze_atomic_json(path, state)
    print('Z0 energy | pathways:', len(state['pathways']),
          '| source records processed:', end, '/', len(records),
          '| pending:', state['pending_source_records'])
    print('Formal energy observations saved separately:', path)
    return state

_ze_previous_save_memory = save_memory
def save_memory(memory):
    result = _ze_previous_save_memory(memory)
    try:
        _ze_integrate(memory)
    except Exception as exc:
        print('Z0 energy observation deferred; engine memory preserved:', str(exc))
    return result


# ============================================================
# V4.9.1 — CROSS-CORE ENERGY / READ-ONLY PHYSICS REFERENCES
# Preserves legacy V4.9 energy sidecar, cursors and every pathway.
# ============================================================
_ZE_DOMAINS = ('rational', 'complex', 'symbolic', 'calculus', 'roles')
_ZE_PHYSICS = {
    'kinetic': {'equation':'m*v**2/2','variables':{'m':'kg','v':'m/s'},'result_unit':'J'},
    'gravitational_potential': {'equation':'m*g*h','variables':{'m':'kg','g':'m/s**2','h':'m'},'result_unit':'J'},
    'work': {'equation':'F*d*cos(theta)','variables':{'F':'N','d':'m','theta':'rad'},'result_unit':'J'},
    'mass_energy': {'equation':'m*c**2','variables':{'m':'kg','c':'m/s'},'result_unit':'J'},
    'photon': {'equation':'h*f','variables':{'h':'J*s','f':'1/s'},'result_unit':'J'},
    'electric_potential': {'equation':'q*V','variables':{'q':'C','V':'J/C'},'result_unit':'J'},
}

def _ze_records(m, domain):
    return m.get('expressions', []) if domain == 'rational' else m.get(domain+'_archive', {}).get('expressions', [])

def _ze_exact_value(rec, domain):
    # Numeric parsing is intentionally conservative; unresolved structures are kept.
    from fractions import Fraction
    if domain == 'rational':
        x = Fraction(str(rec['value']))
        return x, Fraction(0)
    if domain == 'complex':
        # Existing complex archive stores exact rational components.
        for pair in (('real','imag'), ('re','im')):
            if pair[0] in rec and pair[1] in rec:
                return Fraction(str(rec[pair[0]])), Fraction(str(rec[pair[1]]))
    raw = rec.get('value', rec.get('exact', rec.get('expr')))
    if not isinstance(raw, (str,int,float)):
        raise ValueError('non-scalar exact value')
    # sympify restricted to known mathematical symbols; never eval user code.
    # Do not parse arbitrary expressions with sympify/parse_expr (execution risk).
    import re
    value = str(raw).strip()
    if re.fullmatch(r'[+-]?\d+(?:/\d+)?', value):
        return Fraction(value), Fraction(0)
    if value in ('I','i'): return Fraction(0), Fraction(1)
    if value in ('-I','-i'): return Fraction(0), Fraction(-1)
    match = re.fullmatch(r'([+-]?\d+(?:/\d+)?)\s*([+-])\s*(\d+(?:/\d+)?)\s*\*?\s*[Ii]',value)
    if match:
        return Fraction(match.group(1)), Fraction(match.group(3))*(1 if match.group(2)=='+' else -1)
    raise ValueError('symbolic or variable value: preserved without numeric reduction')

def _ze_crosscore_integrate(m):
    path = _ze_sidecar_path()
    if not os.path.isfile(path):
        raise ValueError('V4.9 energy sidecar missing; run V4.9 observation first')
    with open(path, encoding='utf-8') as f: state=json.load(f)
    if state.get('rule') != _ZE_RULE or state.get('nexus') != 'Z0':
        raise ValueError('Unexpected energy sidecar identity')
    # Legacy rational cursor remains the authority for pre-upgrade records.
    cursors=state.setdefault('cross_core_cursors', {'rational':int(state.get('next_source_index',0)),
                                                    'complex':0,'symbolic':0,'calculus':0,'roles':0})
    for domain in _ZE_DOMAINS:
        records=_ze_records(m,domain)
        start=int(cursors.get(domain,0))
        if start > len(records):
            raise ValueError('Archive shrank for '+domain+'; preserve sidecar and investigate')
        end=min(start+_ZE_BATCH,len(records))
        for i in range(start,end):
            rec=records[i]
            if not isinstance(rec,dict): continue
            base={'rule':_ZE_RULE,'nexus':'Z0','source_archive':domain,'source_index':i,
                  'source_id':rec.get('id'),'source_digest':_ze_record_signature(rec),
                  'source_tree':rec.get('tree'),'source_expr':rec.get('expr'),
                  'source_parents':rec.get('parents'),'source_sources':rec.get('sources'),
                  'source_ancestry':rec.get('ancestry'),
                  'source_zero_passage':rec.get('zero_core_passage'),
                  'source_observer':rec.get('observer'),'source_spatial':rec.get('spatial'),
                  'source_temporal':rec.get('temporal'),
                  'energy_role':'formal_observation','physical_status':'unverified'}
            for branch in _ZE_BRANCHES:
                event=dict(base,path_id='ZE:%s:%s:%s'%(domain,i,branch),branch=branch,
                           energy_input=_ZE_ENERGY_SEED)
                try:
                    re,im=_ze_exact_value(rec,domain)
                    re,im=_pr_energy_step(re,im,branch,m)
                    event['primitive_jobs']=[p['job'] for p in m['primitive_reduction']['passages'][-1:]]
                    event.update(formal_output={'real':str(re),'imag':str(im)},status='candidate_observation')
                except (ValueError,TypeError,KeyError,ZeroDivisionError,OverflowError) as e:
                    event.update(formal_output=None,status='unresolved',
                                 block_reason=str(e)[:160])
                state['pathways'].append(event)
        cursors[domain]=end
    # Do not discard or rewrite V4.9 rows, and don't repeat its first 64 sources.
    state['next_source_index']=cursors['rational']
    state['source_records_available']=len(_ze_records(m,'rational'))
    state['pending_source_records']=max(0,state['source_records_available']-cursors['rational'])
    state['cross_core_pending']={d:len(_ze_records(m,d))-cursors[d] for d in _ZE_DOMAINS}
    state['total_pathways_preserved']=len(state['pathways'])
    state['physics_reference_version']='v491_read_only'
    _ze_atomic_json(path,state)
    print('Z0 cross-core energy | total pathways:',len(state['pathways']),
          '| pending by core:',state['cross_core_pending'])
    return state

def _ze_read_state():
    path=_ze_sidecar_path()
    if not os.path.exists(path):
        print('No energy sidecar yet:',path)
        return None
    with open(path,encoding='utf-8') as f: state=json.load(f)
    if state.get('rule')!=_ZE_RULE or state.get('nexus')!='Z0':
        raise ValueError('Unrecognized energy sidecar')
    return state

def _ze_print_index(state,limit=16):
    from collections import Counter
    rows=state['pathways']
    print('ENERGY INDEX | Z0 | pathways:',len(rows),'| by source:',dict(Counter(r['source_archive'] for r in rows)))
    print('Statuses:',dict(Counter(r['status'] for r in rows)))
    print('Pending:',state.get('cross_core_pending',{'rational':state.get('pending_source_records')}))
    for row in rows[-limit:]:
        print(' ',row['path_id'],'|',row['status'],'|',row.get('formal_output'),
              '| source:',row['source_archive'],row['source_id'])
    print('Use energy-index 50, energy-path PATH_ID, physics-index, physics-match')

def _ze_physics_match(state):
    # Never use this reference set to create or promote an engine construction.
    from collections import Counter
    outputs=Counter()
    for row in state['pathways']:
        v=row.get('formal_output')
        if isinstance(v,dict): outputs[(v.get('real'),v.get('imag'))]+=1
    print('PHYSICS REFERENCE COMPARISON | READ ONLY')
    print('Known formulas require typed physical variables, units and assumptions.')
    print('Formal numeric values alone do NOT establish a physical-law match.')
    for name,ref in _ZE_PHYSICS.items():
        print(' ',name,':',ref['equation'],'|',ref['result_unit'],
              '| typed variables:',ref['variables'],'| verified structural matches: 0')
    print('Formal outputs:',sum(outputs.values()),'| unique exact output pairs:',len(outputs))
    print('Physical matches: UNASSESSED — dimensional physical roles not yet assigned.')

def _ze_query(m,text):
    parts=text.strip().split()
    if not parts or parts[0].lower() not in ('energy','energy-index','energy-path','energy-integrity','physics-index','physics-match'):
        return False
    cmd=parts[0].lower()
    if cmd=='physics-index':
        for name,ref in _ZE_PHYSICS.items():
            print(name,':',ref['equation'],'| unit:',ref['result_unit'],'| variables:',ref['variables'])
        return True
    state=_ze_read_state()
    if state is None:return True
    if cmd in ('energy','energy-index'):
        count=16
        if len(parts)==2:
            try: count=max(1,min(100,int(parts[1])))
            except ValueError: print('Usage: energy-index [1..100]');return True
        _ze_print_index(state,count)
    elif cmd=='energy-path':
        if len(parts)!=2: print('Usage: energy-path ZE:rational:0:+1');return True
        row=next((r for r in state['pathways'] if r['path_id']==parts[1]),None)
        print(json.dumps(row,indent=2) if row else 'Path not found')
    elif cmd=='physics-match': _ze_physics_match(state)
    elif cmd=='energy-integrity':
        ids=[r.get('path_id') for r in state['pathways']]
        invalid=[r.get('path_id') for r in state['pathways'] if r.get('nexus')!='Z0' or r.get('rule')!=_ZE_RULE]
        duplicates=len(ids)-len(set(ids))
        missing=[];changed=[]
        for row in state['pathways']:
            domain=row.get('source_archive');i=row.get('source_index')
            records=_ze_records(m,domain)
            if not isinstance(i,int) or i<0 or i>=len(records):missing.append(row.get('path_id'))
            elif _ze_record_signature(records[i])!=row.get('source_digest'):changed.append(row.get('path_id'))
        print('ENERGY INTEGRITY | paths:',len(ids),'| duplicate IDs:',duplicates,
              '| invalid nexus/rule:',len(invalid),'| missing source:',len(missing),
              '| changed source:',len(changed))
        if missing:print('Missing examples:',missing[:10])
        if changed:print('Changed examples:',changed[:10])
        print('Read-only link audit; does not prove physical correctness.')
    return True

# V4.9 already processes rational sources in its original save hook.
# On upgrade, disable only the old rational observer to prevent duplicate rows.
# Keep its earlier pathways and cursor in the same sidecar unchanged.
_ze_v49_save_memory=save_memory
_ze_original_v48_save_memory=_ze_previous_save_memory
def save_memory(memory):
    result=_ze_original_v48_save_memory(memory)
    try:
        if not os.path.isfile(_ze_sidecar_path()):
            _ze_integrate(memory)
        _ze_crosscore_integrate(memory)
    except Exception as exc:
        print('Z0 cross-core energy deferred; main memory preserved:',str(exc))
    return result

_ze_prior_query_v45=query_v45
def query_v45(m,text):
    if _ze_query(m,text):return True
    return _ze_prior_query_v45(m,text)

# ============================================================
# V4.9.2 — EMERGENT PHYSICAL FOUNDATIONS OBSERVER
# Read-only observation of mathematical constructions, NOT physics
# invention. No physical units are injected into the exploration.
# ============================================================
_ZF_RULE = 'emergent_foundations_observer_v1'
_ZF_BATCH = 256
_ZF_REFERENCE = {
    'zero': ('0', 'dimensionless reference'),
    'unity': ('1', 'dimensionless reference'),
    'half': ('1/2', 'dimensionless reference'),
    'pi_approx': ('3.141592653589793', 'dimensionless mathematical constant'),
    'e_approx': ('2.718281828459045', 'dimensionless mathematical constant'),
    'standard_gravity_magnitude': ('9.80665', 'm/s^2; magnitude only'),
    'speed_of_light_magnitude': ('299792458', 'm/s; magnitude only'),
    'planck_constant_magnitude': ('6.62607015e-34', 'J*s; magnitude only'),
}

def _zf_path():
    return memory_path()+'.foundation-candidates.json'

def _zf_pair(value):
    from fractions import Fraction
    if not isinstance(value,dict): return None
    try: return Fraction(str(value['real'])),Fraction(str(value['imag']))
    except (ValueError,KeyError,TypeError,ZeroDivisionError): return None

def _zf_key(pair):
    return str(pair[0])+'|'+str(pair[1])

def _zf_observe(memory):
    # Source archive and energy observer remain untouched.
    source=_ze_read_state()
    if source is None: return
    dest=_zf_path()
    if os.path.exists(dest):
        with open(dest,encoding='utf-8') as f: state=json.load(f)
        if state.get('rule')!=_ZF_RULE or state.get('nexus')!='Z0':
            raise ValueError('Unknown foundation sidecar; refusing overwrite')
    else:
        state={'schema':1,'rule':_ZF_RULE,'nexus':'Z0','cursor':0,
               'observations':[],'reference_is_read_only':True,
               'physical_quantities_verified':0,
               'note':'Mathematical candidate observations; not identified physical quantities.'}
    rows=source.get('pathways',[])
    cursor=state['cursor']
    if cursor>len(rows):raise ValueError('Energy sidecar shrank; foundation cursor preserved')
    stop=min(cursor+_ZF_BATCH,len(rows))
    for index in range(cursor,stop):
        row=rows[index]
        pair=_zf_pair(row.get('formal_output'))
        observation={'energy_path_id':row.get('path_id'),
                     'energy_path_index':index,'source_archive':row.get('source_archive'),
                     'source_index':row.get('source_index'),
                     'source_digest':row.get('source_digest'),
                     'nexus':'Z0','status':'unresolved' if pair is None else 'formal_candidate',
                     'exact_value':None if pair is None else {'real':str(pair[0]),'imag':str(pair[1])},
                     'physical_identity':None,'physical_units':None}
        state['observations'].append(observation)
    state['cursor']=stop
    state['pending']=len(rows)-stop
    state['energy_paths_available']=len(rows)
    _ze_atomic_json(dest,state)
    print('Z0 foundations | observations:',len(state['observations']),
          '| pending:',state['pending'],'| physical identities assigned: 0')

def _zf_read():
    path=_zf_path()
    if not os.path.isfile(path):
        print('No foundations sidecar yet. Run the engine to generate it.');return None
    with open(path,encoding='utf-8') as f: state=json.load(f)
    if state.get('rule')!=_ZF_RULE or state.get('nexus')!='Z0':
        raise ValueError('Unrecognized foundations sidecar')
    return state

def _zf_groups(state):
    from collections import defaultdict
    groups=defaultdict(list)
    for row in state['observations']:
        pair=_zf_pair(row.get('exact_value'))
        if pair is not None:groups[_zf_key(pair)].append(row)
    return groups

def _zf_query(memory,command):
    from collections import Counter
    from fractions import Fraction
    parts=command.strip().split()
    if not parts or parts[0].lower() not in ('foundation-index','foundation-candidate','foundation-match','foundation-integrity'):
        return False
    state=_zf_read()
    if state is None:return True
    groups=_zf_groups(state)
    cmd=parts[0].lower()
    if cmd=='foundation-index':
        limit=20
        if len(parts)>1:
            try:limit=max(1,min(100,int(parts[1])))
            except ValueError:print('Usage: foundation-index [1..100]');return True
        print('EMERGENT FOUNDATIONS | Z0 | observations:',len(state['observations']),
              '| pending:',state.get('pending'),'| unique exact pairs:',len(groups))
        print('Sources:',dict(Counter(r['source_archive'] for r in state['observations'])))
        print('Candidate outputs, sorted by recurrence; NOT verified physical quantities:')
        for key,items in sorted(groups.items(),key=lambda item:(-len(item[1]),item[0]))[:limit]:
            domains=sorted(set(r['source_archive'] for r in items))
            print(' ',key,'| paths:',len(items),'| cores:',','.join(domains),
                  '| example:',items[0]['energy_path_id'])
        print('Use foundation-candidate REAL [IMAG], foundation-match, foundation-integrity')
    elif cmd=='foundation-candidate':
        if len(parts) not in (2,3):print('Usage: foundation-candidate REAL [IMAG]');return True
        try:key=_zf_key((Fraction(parts[1]),Fraction(parts[2]) if len(parts)==3 else Fraction(0)))
        except (ValueError,ZeroDivisionError):print('Use exact rational values, e.g. 1/2');return True
        matches=groups.get(key,[])
        print('FOUNDATION CANDIDATE',key,'| recorded paths:',len(matches))
        for r in matches[:40]:print(' ',r['energy_path_id'],'|',r['source_archive'],r['source_index'])
        if len(matches)>40:print(' ...',len(matches)-40,'more preserved in sidecar')
        print('Mathematical value only; physical identity not established.')
    elif cmd=='foundation-match':
        print('READ-ONLY REFERENCE MAGNITUDES | numerical comparisons only')
        for name,(raw,units) in _ZF_REFERENCE.items():
            try:
                # Fraction of decimal scientific notation is exact for the written decimal.
                target=Fraction(raw)
                matches=groups.get(_zf_key((target,Fraction(0))),[])
                print(' ',name,'| reference:',raw,'|',units,'| exact numeric coincidences:',len(matches))
            except ValueError:continue
        print('No dimensional or physical identification is inferred from a number.')
    else:
        energy=_ze_read_state()
        original=energy.get('pathways',[]) if energy else []
        missing=changed=bad=0
        seen=set()
        for row in state['observations']:
            idx=row.get('energy_path_index')
            if not isinstance(idx,int) or idx<0 or idx>=len(original):missing+=1;continue
            src=original[idx]
            if row.get('energy_path_id')!=src.get('path_id') or row.get('source_digest')!=src.get('source_digest'):
                changed+=1
            if idx in seen or row.get('nexus')!='Z0':bad+=1
            seen.add(idx)
        print('FOUNDATION INTEGRITY | observations:',len(state['observations']),
              '| missing energy paths:',missing,'| changed links:',changed,
              '| duplicate/invalid:',bad,'| pending:',state.get('pending'))
        print('Structural checks only; no physical quantity has been verified.')
    return True

_zf_previous_save_memory=save_memory
def save_memory(memory):
    result=_zf_previous_save_memory(memory)
    try:_zf_observe(memory)
    except Exception as exc:print('Z0 foundations deferred; main memory preserved:',str(exc))
    return result

_zf_previous_query_v45=query_v45
def query_v45(m,text):
    if _zf_query(m,text):return True
    return _zf_previous_query_v45(m,text)


# ==== Z0 PRIMITIVE CONSTRUCTIONS IN THE MAIN PERSISTENT SCHEDULER ====
# This worker generates S/P paths from the archive root without requested
# targets or higher-operation labels. Each distinct tree remains a record.
# Historical operations are retained as historical evidence, not reclassified.
Z0_BRIDGE_PER_RUN = 8

def z0_bridge_bootstrap(m):
    queue=m.get('queue',[])
    head=m.get('queue_head',0)
    retained=queue[:head]
    history=m.setdefault('historical_primitive_tasks',[])
    for task in queue[head:]:
        if ((not m.get('z0_successor_bootstrapped') and task.get('kind') in ('z0_primitive','z0_macro')) or
            (task.get('kind')=='z0_primitive' and task.get('primitive')!='S') or
            (task.get('kind')=='z0_macro' and any(p!='S' for p in task.get('sequence',[])))):
            history.append({'task':_pr_copy.deepcopy(task),'status':'retained_not_executed',
                'reason':'successor_only_experiment'})
        else:retained.append(task)
    m['queue']=retained
    registry = m.setdefault('rule_registry', {})
    registry.setdefault('z0_successor_open_v1', {'status':'active_exploration',
        'primitives':['S'], 'target_free':True})
    if m.get('z0_successor_bootstrapped'):
        return
    roots = m.get('results', {}).get('0', [])
    if not roots:
        raise ValueError('Z0 rational root missing')
    if not m.get('results', {}).get('1'):
        raise ValueError('Z0 primitive unit foundation missing')
    enqueue(m, {'kind':'z0_primitive', 'source':roots[0], 'primitive':'S'})
    m['z0_successor_bootstrapped'] = True

def z0_bridge_work(m, task, stats, *, return_id=False):
    source_id = task['source']
    if not isinstance(source_id,int) or source_id < 0 or source_id >= len(m['expressions']):
        raise ValueError('Broken Z0 primitive source ID')
    source = m['expressions'][source_id]
    primitive = task['primitive']
    if primitive != 'S':
        raise ValueError('Unknown Z0 primitive')
    # Exact integers are sufficient for the primitive frontier; rational and
    # symbolic transformations remain separate higher-level constructions.
    value = Fraction(source['value'])
    if value.denominator != 1:
        raise ValueError('Non-integer Z0 primitive source')
    step = 1 if primitive == 'S' else -1
    result = _pr_qop(value, "+", step, m)
    tree = {'op':'+' if primitive=='S' else '-',
            'left':source['tree'], 'right':{'leaf':1}}
    rec = {'expr':'('+source['expr']+(' + 1)' if primitive=='S' else ' - 1)'),
           'value':encode(result), 'tree':tree,
           'depth':source.get('depth',0)+1,
           'parents':[source_id, m['results']['1'][0]],
           'leaves':list(source.get('leaves',[]))+[1],
           'pathway':'z0_successor_open_v1',
           'ancestry':list(source.get('ancestry',[]))+[{
               'rule':'z0_successor_open_v1', 'zero_nexus':'Z0',
               'source_id':source_id, 'primitive':primitive}],
           'domain':'rational'}
    idx = add_expression(m, rec)
    if idx is not None:
        stats['new'] += 1
        # This is an *open* successor/predecessor frontier, never a target.
        enqueue(m, {'kind':'z0_primitive','source':idx,'primitive':'S'})
        journal(m,'z0_primitive_construction',source_id=source_id,
                result_id=idx,primitive=primitive)
    if idx is None and return_id:
        # Reuse only this exact construction and parents, never an equal value.
        # The macro journal retains its own traversal edge.
        idx=next((r['id'] for r in m['expressions']
            if r.get('pathway')==rec['pathway'] and r.get('tree')==rec['tree']
            and r.get('parents')==rec['parents']),None)
    return idx if return_id else True

# ==== EVIDENCE-LED PRIMITIVE PATTERN DISCOVERY ====
# Observe *existing* S/P paths; never request an arithmetic answer.
# A macro is a compressed traversal, NOT a new primitive or a proof of +/*.
def z0_discover_primitive_patterns(m, *, min_distinct_sources=2):
    from collections import defaultdict
    expressions=m['expressions']
    paths={}
    evidence=defaultdict(list)
    for rec in expressions:
        if rec.get('pathway')!='z0_successor_open_v1':
            continue
        ancestry=rec.get('ancestry', [])
        if not ancestry or ancestry[-1].get('rule')!='z0_successor_open_v1':
            continue
        parent_id=ancestry[-1].get('source_id')
        if not isinstance(parent_id,int) or not 0<=parent_id<len(expressions):
            continue
        op=ancestry[-1].get('primitive')
        if op != 'S':
            continue
        parent=expressions[parent_id]
        # Require actual primitive ancestry and independently recompute the edge.
        delta=1 if op=='S' else -1
        if Fraction(rec['value'])!=Fraction(parent['value'])+delta:
            raise ValueError('Z0 primitive archive evidence mismatch')
        prefix=paths.get(parent_id, ())
        sequence=prefix+(op,)
        paths[rec['id']]=sequence
        for width in (2,3):
            if len(sequence)<width: continue
            # The source is the ancestor at the beginning of this exact suffix.
            ancestor_id=rec['id']
            for _ in range(width):
                ancestor_id=expressions[ancestor_id]['ancestry'][-1]['source_id']
            evidence[sequence[-width:]].append((ancestor_id,rec['id']))
    observed=[]
    validated=[]
    for sequence, pairs in sorted(evidence.items()):
        starts={expressions[a]['value'] for a,_ in pairs}
        item={'sequence':list(sequence),'occurrences':len(pairs),
              'distinct_source_values':len(starts),
              'evidence_ids':[b for _,b in pairs[:32]],
              'status':'observed_not_validated'}
        if len(starts)>=min_distinct_sources:
            for a,b in pairs:
                value=Fraction(expressions[a]['value'])
                for op in sequence:
                    value=value+(1 if op=='S' else -1)
                if value!=Fraction(expressions[b]['value']):
                    raise ValueError('Z0 discovered pattern failed replay')
            item['status']='validated_primitive_macro'
            validated.append(item)
        observed.append(item)
    registry=m.setdefault('rule_registry',{})
    registry['z0_discovered_successor_macros_v1']={
        'status':'evidence_led','target_free':True,
        'primitive_basis':['S'],'observations':observed,
        'validated_count':len(validated),
        'note':'Macros expand into primitive steps; no higher arithmetic identity inferred.'}
    return {'observed':len(observed),'validated':len(validated)}

def z0_replay_discovered_macro(m, sequence, source_id):
    """Executable macro; returns the full primitive trace, never a direct shortcut."""
    registered=m.get('rule_registry',{}).get('z0_discovered_successor_macros_v1',{})
    allowed={tuple(x['sequence']) for x in registered.get('observations',[])
             if x['status']=='validated_primitive_macro'}
    sequence=tuple(sequence)
    if sequence not in allowed:
        raise ValueError('Unvalidated primitive pattern')
    if not isinstance(source_id,int) or not 0<=source_id<len(m['expressions']):
        raise ValueError('Invalid primitive macro source')
    value=Fraction(m['expressions'][source_id]['value'])
    trace=[]
    for op in sequence:
        value=_pr_qop(value,'+',1 if op=='S' else -1,m)
        trace.append({'primitive':op,'value':encode(value),'zero_nexus':'Z0'})
    return {'source_id':source_id,'sequence':list(sequence),
            'result':encode(value),'primitive_trace':trace,
            'status':'verified_expansion_not_new_primitive'}

# ==== AUTOMATIC, BOUNDED, EVIDENCE-LED MACRO SCHEDULING ====
# A macro is never a new mathematical primitive. It is a persisted plan to
# expand a discovered sequence one S/P step at a time, with full ancestry.
Z0_MACRO_SCHEDULE_PER_RUN = 2

def z0_macro_schedule(m):
    registry=m.get('rule_registry',{}).get('z0_discovered_successor_macros_v1',{})
    validated=[tuple(item['sequence']) for item in registry.get('observations',[])
               if item.get('status')=='validated_primitive_macro']
    if not validated:
        return 0
    sources=[r['id'] for r in m['expressions']
             if r.get('pathway')=='z0_successor_open_v1']
    if not sources:
        return 0
    # Fair persistent cursor; choose the next *source*, not a target value.
    cursor=m.setdefault('z0_macro_cursor',0)
    created=0
    for offset in range(min(Z0_MACRO_SCHEDULE_PER_RUN,len(sources))):
        source=sources[(cursor+offset)%len(sources)]
        sequence=validated[(cursor+offset)%len(validated)]
        task={'kind':'z0_macro','source':source,'sequence':list(sequence),
              'step':0,'origin':source}
        if enqueue(m,task): created+=1
    m['z0_macro_cursor']=cursor+Z0_MACRO_SCHEDULE_PER_RUN
    return created

def z0_macro_work(m,task,stats):
    registry=m.get('rule_registry',{}).get('z0_discovered_successor_macros_v1',{})
    allowed={tuple(x['sequence']) for x in registry.get('observations',[])
             if x.get('status')=='validated_primitive_macro'}
    seq=tuple(task.get('sequence',()))
    step=task.get('step')
    if seq not in allowed or not isinstance(step,int) or not 0<=step<len(seq):
        raise ValueError('Invalid or unvalidated Z0 macro task')
    source=task['source']
    if not isinstance(source,int) or not 0<=source<len(m['expressions']):
        raise ValueError('Invalid Z0 macro source')
    # Reuse the primitive archive worker: no direct arithmetic macro result.
    new_id=z0_bridge_work(m,{'source':source,'primitive':seq[step]},
                          stats,return_id=True)
    if new_id is not None and step+1<len(seq):
        enqueue(m,{'kind':'z0_macro','source':new_id,'sequence':list(seq),
                   'step':step+1,'origin':task['origin']})
    journal(m,'z0_macro_primitive_expansion',source_id=source,
            result_id=new_id,primitive=seq[step],step=step,
            sequence=list(seq),origin=task['origin'])
    return True

# ==== Z0 TARGET-FREE TWO-PRIMITIVE EXPLORATION (V4.9.2 work order) ====
# Independent exploration: never requests a target value or a higher operation.
# Existing archive, five-state foundation, recovery and time machinery are intact.

def z0_open_explore(path, *, cycles=1, frontier_limit=64, value_bound=128, role_bindings=None):
    """Target-free, bounded-work breadth-first S/P construction through Z0.

    frontier_limit is a per-cycle work budget, not a maximum frontier size.
    Deferred work remains in the checkpoint; equal results retain distinct IDs.
    """
    import json as _json
    import os as _os
    from collections import Counter as _Counter
    if cycles < 0 or frontier_limit < 1 or value_bound < 1:
        raise ValueError('Invalid exploration limits')
    if _os.path.exists(path):
        with open(path, encoding='utf-8') as _f:
            state = _json.load(_f)
        if state.get('schema') not in ('z0_open_successor_v1', 'z0_open_successor_v2'):
            raise ValueError('Unknown exploration checkpoint schema')
    else:
        state = {'schema':'z0_open_successor_v2', 'nexus':'Z0',
                 'primitives':['S'], 'generation':0, 'next_id':1,
                 'records':[{'id':'Z0:0', 'parent':None, 'value':0,
                             'generation':0, 'operation':'seed',
                             'through_zero':'Z0', 'path':[]}],
                 'frontier':['Z0:0'], 'blocked':[], 'patterns':[]}
    bindings=_pr_bind_roles(None) if role_bindings is None else role_bindings
    existing=state.get('operation_roles')
    if existing is not None and existing!=bindings:
        raise ValueError('Exploration operation role bindings changed')
    state['operation_roles']=bindings
    records = state['records']
    by_id = {r['id']:r for r in records}
    if (len(by_id)!=len(records) or not records or
        by_id.get('Z0:0',{}).get('value')!=0 or
        state.get('nexus')!='Z0' or state.get('primitives')!=['S']):
        raise ValueError('Invalid exploration root or records')
    # The IDs are also an append-only ordering invariant. Never reassign them.
    for i,r in enumerate(records):
        if r.get('id')!='Z0:'+str(i):
            raise ValueError('Noncontiguous or reordered exploration IDs')
        if i==0:
            if r.get('parent') is not None or r.get('path')!=[]:
                raise ValueError('Altered root')
            continue
        parent=by_id.get(r.get('parent'))
        if (parent is None or parent.get('generation',0)>=r.get('generation',0)
            or r.get('operation') != 'S'):
            raise ValueError('Broken primitive ancestry')
        delta=1 if r['operation']=='S' else -1
        if (r.get('value')!=parent['value']+delta or
            r.get('path')!=parent['path']+[r['operation']] or
            r.get('through_zero')!='Z0'):
            raise ValueError('Altered primitive evidence')
    if state.get('next_id')!=len(records):
        raise ValueError('Invalid exploration next ID')
    frontier=state.get('frontier')
    if not isinstance(frontier,list) or len(set(frontier))!=len(frontier) or any(x not in by_id for x in frontier):
        raise ValueError('Invalid exploration frontier')
    # V1 checkpoints could drop parents when a frontier cap was reached.
    # Recover only parents that have not generated both branches; retain all
    # historical evidence and never rewrite an existing construction.
    if state['schema']=='z0_open_successor_v1':
        children={(r['parent'],r['operation']) for r in records[1:]}
        unfinished=[r['id'] for r in records if any((r['id'],op) not in children for op in ('S',))]
        frontier=list(dict.fromkeys(frontier+unfinished))
        state['schema']='z0_open_successor_v2'
    child_ops={}
    for r in records[1:]:
        child_ops.setdefault(r['parent'],set()).add(r['operation'])
    # One frontier item is one parent; it creates up to two unique children.
    # No value-based pruning: bounded *work* instead of bounded *results*.
    for _ in range(cycles):
        if not frontier:
            break
        parents=frontier[:frontier_limit]
        frontier=frontier[frontier_limit:]
        generation=state['generation']+1
        for parent_id in parents:
            parent=by_id[parent_id]
            existing=child_ops.setdefault(parent_id,set())
            for primitive,delta in (('S',1),):
                if primitive in existing:
                    continue
                ident='Z0:'+str(state['next_id'])
                state['next_id']+=1
                row={'id':ident,'parent':parent_id,'value':_pr_execute_binding(bindings[primitive],parent['value']),
                     'operation_role':{'archive':bindings[primitive]['archive'],'id':bindings[primitive]['id']},
                     'generation':generation,'operation':primitive,
                     'through_zero':'Z0','path':parent['path']+[primitive]}
                records.append(row)
                existing.add(primitive)
                by_id[ident]=row
                frontier.append(ident)
        state['generation']=generation
    state['frontier']=frontier
    counts=_Counter(tuple(r['path'][-2:]) for r in records if len(r['path'])>=2)
    state['patterns']=[{'sequence':list(k),'occurrences':v,
                        'status':'observed_not_validated'}
                       for k,v in sorted(counts.items()) if v>=2]
    directory=_os.path.dirname(_os.path.abspath(path))
    _os.makedirs(directory,exist_ok=True)
    tmp=path+'.tmp'
    with open(tmp,'w',encoding='utf-8') as _f:
        _json.dump(state,_f,indent=2,ensure_ascii=False)
        _f.flush()
        _os.fsync(_f.fileno())
    _os.replace(tmp,path)
    return {'generation':state['generation'],'records':len(records),
            'frontier':len(frontier),'blocked':len(state['blocked']),
            'observed_patterns':len(state['patterns']),'checkpoint':path}

# ==== AUTOMATIC Z0 EXPLORATION ON NORMAL ENGINE SAVES ====
# This is an independent, target-free sidecar attached to the existing run.
# It does not change the legacy scheduler or claim its operations have emerged.
_Z0_AUTO_CYCLES = 1
_Z0_AUTO_FRONTIER_LIMIT = 64
_Z0_AUTO_VALUE_BOUND = 128

_z0_previous_save_memory = save_memory
def save_memory(memory):
    result = _z0_previous_save_memory(memory)
    # Only progress exploration after the original archive save succeeds.
    # The sidecar never writes into or replaces the original memory archive.
    try:
        checkpoint = memory_path() + '.z0-successor-exploration.json'
        report = z0_open_explore(checkpoint, cycles=_Z0_AUTO_CYCLES,
                                 frontier_limit=_Z0_AUTO_FRONTIER_LIMIT,
                                 value_bound=_Z0_AUTO_VALUE_BOUND, role_bindings=_pr_bind_roles(memory))
        print('Z0 open exploration | generation:', report['generation'],
              '| paths:', report['records'], '| frontier:', report['frontier'],
              '| blocked:', report['blocked'])
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print('Z0 open exploration deferred; main archive preserved:', str(exc))
    return result

# ============================================================
# V4.9.5 — SUCCESSOR-ONLY NUMERIC CONSTRUCTION GATEWAY
# Arithmetic primitive: natural S. Signed moves are expanded scans. Copy and branching
# are explicit machine/control rules. Fractions and pairs are
# representations; roots and free symbols retain declared rules.
# ============================================================
import copy as _pr_copy
import hashlib as _pr_hashlib

PRIMITIVE_WORK_PER_CALL = 2048
PRIMITIVE_SCHEMA = 'z0_successor_register_machine_v1'
_PR_MEMORY = None
_PR_LOCAL = {}

class PrimitivePending(ArithmeticError):
    def __init__(self, job):
        self.job = job
        super().__init__('Successor construction pending: ' + job)

def _pr_assemble(rows):
    labels = {}
    code = []
    for row in rows:
        if row[0] == ':': labels[row[1]] = len(code)
        else: code.append(row)
    return [[labels.get(x[1:], x) if isinstance(x, str) and x.startswith('@') else x
             for x in row] for row in code]

_PR_PROGRAMS = {
 'stepS': [('natS','a'),('ret','a')],
 'add': [('copy','x','a'),('zero','counter'),('magnitude','limit','b'),
         (':','loop'),('jlt','counter','limit','@unit'),('ret','x'),
         (':','unit'),('jneg','b','@negative'),('signed_up','x'),('jump','@count'),
         (':','negative'),('signed_down','x'),(':','count'),('natS','counter'),('jump','@loop')],
 'sub': [('copy','x','a'),('zero','counter'),('magnitude','limit','b'),
         (':','loop'),('jlt','counter','limit','@unit'),('ret','x'),
         (':','unit'),('jneg','b','@negative'),('signed_down','x'),('jump','@count'),
         (':','negative'),('signed_up','x'),(':','count'),('natS','counter'),('jump','@loop')],
 'neg': [('zero','z'),('call','sub',['z','a'],['x']),('ret','x')],
 'abs': [('jneg','a','@negative'),('ret','a'),(':','negative'),
         ('call','neg',['a'],['x']),('ret','x')],
 # Multiplication has no product instruction. Its complete derivation is
 # repeated calls to addition, with an S-driven repetition counter.
 'mul': [('zero','x'),('zero','counter'),('magnitude','limit','b'),('copy','term','a'),
         ('jneg','b','@negative'),('jump','@loop'),
         (':','negative'),('call','neg',['a'],['term']),
         (':','loop'),('jlt','counter','limit','@unit'),('ret','x'),
         (':','unit'),('call','add',['x','term'],['x']),('natS','counter'),('jump','@loop')],
 'div': [('jzero','b','@bad'),('call','abs',['a'],['r']),('call','abs',['b'],['d']),
         ('zero','q'),(':','loop'),('jlt','r','d','@sign'),
         ('call','sub',['r','d'],['r']),('natS','q'),('jump','@loop'),
         (':','sign'),('jneg','a','@aneg'),('jneg','b','@qneg'),('jump','@end'),
         (':','aneg'),('call','neg',['r'],['r']),('jneg','b','@end'),
         (':','qneg'),('call','neg',['q'],['q']),(':','end'),('ret','q','r'),
         (':','bad'),('error','division_by_zero')],
 'gcd': [('call','abs',['a'],['x']),('call','abs',['b'],['y']),(':','loop'),
         ('jzero','y','@end'),('call','div',['x','y'],['q','r']),
         ('copy','x','y'),('copy','y','r'),('jump','@loop'),(':','end'),('ret','x')],
 'norm': [('jzero','b','@bad'),('jneg','b','@negative'),('jump','@gcd'),
          (':','negative'),('call','neg',['a'],['a']),('call','neg',['b'],['b']),
          (':','gcd'),('call','gcd',['a','b'],['g']),
          ('call','div',['a','g'],['n','r']),('call','div',['b','g'],['d','r']),
          ('ret','n','d'),(':','bad'),('error','division_by_zero')],
}

for _pr_op in ('add','sub','mul','div'):
    if _pr_op in ('add','sub'):
        _pr_rows = [('call','mul',['a','d'],['x']),('call','mul',['c','b'],['y']),
                    ('call',_pr_op,['x','y'],['n']),('call','mul',['b','d'],['den'])]
    elif _pr_op == 'mul':
        _pr_rows = [('call','mul',['a','c'],['n']),('call','mul',['b','d'],['den'])]
    else:
        _pr_rows = [('call','mul',['a','d'],['n']),('call','mul',['b','c'],['den'])]
    _PR_PROGRAMS['q'+_pr_op] = _pr_rows + [('call','norm',['n','den'],['n','den']),('ret','n','den')]
_PR_PROGRAMS = {k:_pr_assemble(v) for k,v in _PR_PROGRAMS.items()}
_PR_PROGRAM_DIGEST = _pr_hashlib.sha256(json.dumps(_PR_PROGRAMS,sort_keys=True).encode()).hexdigest()

def _pr_frame(name, args, outputs=None):
    if name not in _PR_PROGRAMS or any(type(x) is not int for x in args):
        raise ValueError('Invalid primitive machine call')
    return {'name':name,'pc':0,'registers':dict(zip(('a','b','c','d'),args)),
            'outputs':outputs}

def _pr_role_body(primitive):
    return {'kind':'operation','primitive':primitive,'input':'natural_counter','output':'natural_counter','nexus':'Z0'}

def _pr_bind_roles(memory):
    if memory is None or 'foundation' not in memory:
        return {p:{'archive':'local_operation_roles','id':p,'body':_pr_role_body(p)} for p in ('S',)}
    upgrade_roles(memory)
    archive=memory['roles_archive']
    refs=archive.setdefault('successor_role_refs',{})
    rule=memory['rule_registry'][ROLE_RULE]
    if 'operation S' not in rule['targets']:rule['targets'].append('operation S')
    if 'bind_successor_operation_role' not in rule['rules']:rule['rules'].append('bind_successor_operation_role')
    bindings={}
    for primitive in ('S',):
        idx=refs.get(primitive)
        if idx is None:
            # A declared primitive is bound through the existing role gateway.
            result,reason=zero_core(memory,'roles',operation='transform',operands=(0,primitive))
            if reason:raise ValueError('Primitive role binding unavailable: '+reason)
            idx=role_record(memory,result,'transform')
            if idx is None:
                idx=next((r['id'] for r in archive['expressions']
                    if r.get('rule')=='bind_successor_operation_role' and
                    r.get('parents')==[0] and r.get('label')==primitive),None)
            if idx is None:raise ValueError('Primitive operation role was not archived')
            refs[primitive]=idx
        if type(idx) is not int or not 0<=idx<len(archive['expressions']):
            raise ValueError('Broken primitive role reference')
        rec=archive['expressions'][idx]
        if (rec.get('kind')!='operation' or rec.get('rule')!='bind_successor_operation_role' or
            rec.get('label')!=primitive or rec.get('body')!=_pr_role_body(primitive)):
            raise ValueError('Changed primitive operation role')
        bindings[primitive]={'archive':'roles','id':idx,'body':_pr_copy.deepcopy(rec['body'])}
    return bindings

def primitive_begin(name, args, role_bindings=None):
    if name not in _PR_PROGRAMS:
        raise ValueError('Unknown primitive program')
    bindings=_pr_bind_roles(None) if role_bindings is None else role_bindings
    if (not isinstance(bindings,dict) or set(bindings)!={'S'} or
        any(bindings[p].get('body')!=_pr_role_body(p) or
            bindings[p].get('archive') not in ('roles','local_operation_roles') for p in bindings)):
        raise ValueError('Invalid executable primitive role bindings')
    work={'schema':PRIMITIVE_SCHEMA,'program_digest':_PR_PROGRAM_DIGEST,
            'nexus':'Z0','primitives':['S'],'program':name,'inputs':list(args),
            'operation_roles':_pr_copy.deepcopy(bindings),
            'stack':[_pr_frame(name,args)],'trace':[],'derived_moves':[],'call_edges':[],'micro':None,'status':'pending'}
    return _pr_advance(work,0)

def _pr_advance(work, budget):
    used = 0
    while work['stack']:
        frame = work['stack'][-1]
        registers = frame['registers']
        instruction = _PR_PROGRAMS[frame['name']][frame['pc']]
        op, *args = instruction
        if op in ('signed_up','signed_down','natS'):
            register=args[0]
            before=registers[register]
            micro=work['micro']
            if micro is None:
                negative,magnitude=_pr_signed_parts(before)
                if op=='natS' and negative:
                    raise ValueError('Natural successor requires a nonnegative magnitude')
                search=(op=='signed_up' and negative) or (op=='signed_down' and before>0)
                negative_result=(negative if search else op=='signed_down')
                micro={'instruction':op,'register':register,'input':before,
                    'mode':'previous_search' if search else 'increase',
                    'target':magnitude,'counter':0 if search else magnitude,'previous':0,
                    'negative_result':negative_result,'trace_start':len(work['trace'])}
                work['micro']=micro
            binding=work['operation_roles']['S']
            # The only numeric update here is executable-role S on a natural
            # counter. A decrease in a signed magnitude is an S-driven search
            # whose previous state is copied, never a native decrement.
            while True:
                if used>=budget:return work
                counter_before=micro['counter']
                micro['previous']=counter_before
                micro['counter']=_pr_execute_binding(binding,counter_before)
                work['trace'].append({'frame_depth':len(work['stack']),
                    'program':frame['name'],'pc':frame['pc'],'register':register,
                    'primitive':'S','operation_role':{'archive':binding['archive'],'id':binding['id']},
                    'before':counter_before,'after':micro['counter'],
                    'derived_instruction':op,'mode':micro['mode']})
                used+=1
                if micro['mode']=='increase' or micro['counter']==micro['target']:break
            magnitude=micro['counter'] if micro['mode']=='increase' else micro['previous']
            registers[register]=_pr_signed_value(micro['negative_result'],magnitude)
            work['derived_moves'].append({'instruction':op,'input':before,
                'result':registers[register],'mode':micro['mode'],
                'trace_start':micro['trace_start'],'trace_end':len(work['trace']),
                'representation':'explicit_sign_and_natural_magnitude'})
            work['micro']=None
        elif op == 'zero': registers[args[0]] = 0
        elif op == 'copy': registers[args[0]] = registers[args[1]]
        elif op == 'magnitude': registers[args[0]] = _pr_signed_parts(registers[args[1]])[1]
        elif op == 'jump':
            frame['pc'] = args[0]; continue
        elif op in ('jzero','jpos','jneg'):
            v = registers[args[0]]
            matched = v == 0 if op == 'jzero' else v > 0 if op == 'jpos' else v < 0
            if matched: frame['pc'] = args[1]; continue
        elif op == 'jlt':
            if registers[args[0]] < registers[args[1]]:
                frame['pc'] = args[2]; continue
        elif op == 'call':
            work['call_edges'].append({'caller':frame['name'],'pc':frame['pc'],'callee':args[0],
                'inputs':[registers[r] for r in args[1]],'trace_start':len(work['trace'])})
            frame['pc'] += 1
            work['stack'].append(_pr_frame(args[0],[registers[r] for r in args[1]],args[2]))
            continue
        elif op == 'ret':
            values = [registers[r] for r in args]
            work['stack'].pop()
            if work['stack']:
                if len(values) != len(frame['outputs']): raise ValueError('Primitive return arity')
                work['stack'][-1]['registers'].update(zip(frame['outputs'],values))
            else:
                work['result'] = values
                work['status'] = 'complete'
            continue
        elif op == 'error': raise ZeroDivisionError(args[0])
        else: raise ValueError('Unknown primitive instruction')
        frame['pc'] += 1
    return work

def primitive_validate(work):
    if (not isinstance(work,dict) or work.get('schema') != PRIMITIVE_SCHEMA or
        work.get('program_digest') != _PR_PROGRAM_DIGEST or work.get('nexus') != 'Z0' or
        work.get('primitives') != ['S'] or not isinstance(work.get('trace'),list)):
        raise ValueError('Invalid primitive checkpoint')
    replay = primitive_begin(work['program'],work['inputs'],work.get('operation_roles'))
    _pr_advance(replay,len(work['trace']))
    if replay != work:
        raise ValueError('Primitive checkpoint does not replay exactly')
    return work

def primitive_continue(work, budget=PRIMITIVE_WORK_PER_CALL):
    if type(budget) is not int or budget < 1: raise ValueError('Positive primitive budget required')
    primitive_validate(work)
    return _pr_advance(_pr_copy.deepcopy(work),budget)

def _pr_state(memory):
    if memory is None: return _PR_LOCAL
    old=memory.get('primitive_reduction')
    if old and old.get('schema')!=PRIMITIVE_SCHEMA:
        memory.setdefault('historical_primitive_reductions',[]).append(old)
        del memory['primitive_reduction']
    return memory.setdefault('primitive_reduction', {
        'schema':PRIMITIVE_SCHEMA,'nexus':'Z0','jobs':{},'passages':[],
        'declarations':{
            'arithmetic_primitives':['S'],
            'control_rules':['copy','zero','comparison','branch','call','return','remember_previous'],
            'derived_signed_moves':'successor scan of magnitudes; no native decrement',
            'multiplication':'repeated addition; declared algorithm, not claimed autonomous discovery',
            'representations':['signed_magnitude_integer','normalized_rational_pair','real_imaginary_pair',
                'polynomial_coefficient_list','registered_role','principal_algebraic_expression'],
            'symbolic_backend':'explicit SymPy algebraic rules; not fully reduced to S',
            'historical_records':'preserved; never relabelled as primitive-generated',
            'whole_engine_reduced':False}})['jobs']

def _pr_request(name,args,memory=None):
    bindings=_pr_bind_roles(memory)
    jobs = _pr_state(memory)
    key = _pr_hashlib.sha256(json.dumps([name,list(args),bindings],sort_keys=True,separators=(',',':')).encode()).hexdigest()
    state = jobs.get(key)
    if state is None: state = primitive_begin(name,args,bindings)
    elif state.get('operation_roles')!=bindings:raise ValueError('Primitive checkpoint role binding changed')
    budget = PRIMITIVE_WORK_PER_CALL
    if memory is not None:
        budget=min(budget,memory.setdefault('_primitive_work_remaining',16384))
    if budget <= 0 and state['status'] != 'complete': raise PrimitivePending(key)
    before=len(state['trace'])
    state = primitive_continue(state,max(1,budget))
    if memory is not None:
        memory['_primitive_work_remaining'] -= len(state['trace'])-before
    jobs[key] = state
    if memory is not None:
        passages = memory['primitive_reduction']['passages']
        passages.append({'job':key,'status':state['status'],'nexus':'Z0'})
    if state['status'] != 'complete': raise PrimitivePending(key)
    if memory is not None:
        memory['primitive_reduction'].get('deferred',{}).pop(key,None)
    return state['result']

def _pr_qop(a,op,b,memory=None):
    a,b = number(a),number(b)
    if op == '/' and b == 0: return None
    names = {'+':'qadd','-':'qsub','*':'qmul','/':'qdiv'}
    if op not in names: raise ValueError('Unsupported primitive rational operation')
    n,d = _pr_request(names[op],(a.numerator,a.denominator,b.numerator,b.denominator),memory)
    # Fraction is the interchange encoding ONLY. The VM has already generated
    # the numerator, positive denominator and gcd-normalized result.
    return Fraction(n,d)

def _operate_rational_exact(a,op,b):
    return _pr_qop(a,op,b,_PR_MEMORY)

def _complex_operate_exact(a,b,op):
    q = lambda x,o,y:_pr_qop(x,o,y,_PR_MEMORY)
    ar,ai=a; br,bi=b
    if op in ('+','-'): return q(ar,op,br),q(ai,op,bi)
    if op == '*':
        return q(q(ar,'*',br),'-',q(ai,'*',bi)),q(q(ar,'*',bi),'+',q(ai,'*',br))
    if op == '/':
        den=q(q(br,'*',br),'+',q(bi,'*',bi))
        if den == 0: return None
        return q(q(q(ar,'*',br),'+',q(ai,'*',bi)),'/',den),q(q(q(ai,'*',br),'-',q(ar,'*',bi)),'/',den)
    raise ValueError('Unsupported primitive complex operation')

def _calculus_apply_exact(operation,coefficients):
    a = [number(v) for v in calculus_coefficients(coefficients)]
    q=lambda x,o,y:_pr_qop(x,o,y,_PR_MEMORY)
    if operation == 'differentiate': result=[q(i,'*',a[i]) for i in range(1,len(a))] or [Fraction(0)]
    elif operation == 'integrate': result=[Fraction(0)]+[q(c,'/',i+1) for i,c in enumerate(a)]
    elif operation == 'limit_zero': result=[a[0]]
    elif operation == 'multiply_x': result=[Fraction(0)]+a
    else: raise ValueError('Unsupported calculus operation')
    encoded=calculus_coefficients(result)
    if len(encoded)-1>CALCULUS_MAX_DEGREE: return None,'calculus_degree_limit'
    if any(max(v.numerator.bit_length(),v.denominator.bit_length())>MAX_BITS for v in result):
        return None,'calculus_coefficient_limit'
    return encoded,None

_pr_prior_symbolic_apply = _symbolic_apply_exact
def _symbolic_apply_exact(a,op,b=None):
    # Rational inputs do not bypass the primitive numeric gateway. Algebraic
    # roots and general symbolic transformations retain the supplied rules.
    if op in ('+','-','*','/') and a.is_Rational and b.is_Rational:
        result=_pr_qop(Fraction(int(a.p),int(a.q)),op,Fraction(int(b.p),int(b.q)),_PR_MEMORY)
        if result is None: return None,'zero_or_unresolved_denominator'
        return sympy_module().Rational(result.numerator,result.denominator),None
    if _PR_MEMORY is not None:
        _pr_state(_PR_MEMORY)
        _PR_MEMORY['primitive_reduction'].setdefault('supplied_symbolic_rules',[]).append({
            'operation':op,'operands':[symbolic_pack(a)]+([] if b is None else [symbolic_pack(b)]),
            'status':'explicit_algebraic_rule_not_primitive_reduction','nexus':'Z0'})
    return _pr_prior_symbolic_apply(a,op,b)

_pr_prior_zero_core = zero_core
def zero_core(m,domain,*,operation=None,operands=(),**kwargs):
    global _PR_MEMORY
    prior=_PR_MEMORY
    _PR_MEMORY=m
    try:
        if domain=='roles' and operation=='execute':
            if m is None or len(operands)!=2:raise ValueError('Role execution needs archive context')
            role_id,value=operands
            if type(role_id) is not int or type(value) is not int or value<0:
                raise ValueError('Primitive role execution requires integer arguments')
            bindings=_pr_bind_roles(m)
            primitive=next((p for p,b in bindings.items() if b['id']==role_id),None)
            if primitive is None:raise ValueError('Role is not a bound primitive operation')
            return _pr_request('step'+primitive,(value,),m)[0]
        if domain == 'foundation' and operation == 'registered_state_count':
            count=0
            for unused in operands[0]:
                count=_pr_request('add',(count,1),m)[0]
            return count
        if kwargs.get('record') is not None and not kwargs.get('historical',False):
            rec=kwargs['record']
            if m is not None and m.get('primitive_reduction'):
                operations=m['primitive_reduction'].get('operations',[])
                if operations and operations[-1]['domain']==domain:
                    last=operations[-1]
                    expected=(rec.get('value') if domain=='rational' else
                              [rec.get('real'),rec.get('imaginary')] if domain=='complex' else None)
                    if last['result']==expected:
                        m['primitive_reduction'].setdefault('record_proofs',{}).setdefault(domain,{})[str(rec['id'])]={
                            'nexus':'Z0','operation_id':last['id'],
                            'scope':'numeric_gateway','whole_engine_reduced':False}
        before=len(m.get('primitive_reduction',{}).get('passages',[])) if m is not None else 0
        result=_pr_prior_zero_core(m,domain,operation=operation,operands=operands,**kwargs)
        if m is not None and operation is not None and domain in ('rational','complex','calculus','symbolic'):
            _pr_state(m)
            state=m['primitive_reduction']
            operations=state.setdefault('operations',[])
            encoded=(str(result) if domain=='rational' else
                     [str(v) for v in result] if domain=='complex' and result is not None else None)
            operations.append({'id':len(operations),'domain':domain,'operation':operation,
                'operands':[str(v) for v in operands],'result':encoded,
                'jobs':[p['job'] for p in state['passages'][before:] if p['status']=='complete'],
                'nexus':'Z0','scope':'numeric_gateway' if domain!='symbolic' or
                    (operation in ('+','-','*','/') and all(v.is_Rational for v in operands))
                    else 'declared_symbolic_rule'})
        return result
    finally: _PR_MEMORY=prior

def primitive_report(memory):
    state=memory.get('primitive_reduction',{})
    jobs=state.get('jobs',{})
    return {'runtime':'4.9.6','schema':PRIMITIVE_SCHEMA,'nexus':'Z0',
        'numeric_primitives':['S'],'active_frontier_primitives':['S'],'native_predecessor':False,
        'multiplication_derivation':'repeated addition with full S traces','jobs':len(jobs),
        'operation_role_refs':memory.get('roles_archive',{}).get('successor_role_refs',{}),
        'complete_jobs':sum(v['status']=='complete' for v in jobs.values()),
        'pending_jobs':sum(v['status']=='pending' for v in jobs.values()),
        'primitive_steps':sum(len(v['trace']) for v in jobs.values()),
        'supplied_symbolic_operations':len(state.get('supplied_symbolic_rules',[])),
        'whole_engine_reduced':False,
        'remaining':'principal roots and general symbolic algebra retain declared SymPy rules'}

# Primitive records participate in the existing manifest/recovery mechanism.
# A recipe is replayed from the exact parent construction and declared unit.
_ZR_ARITHMETIC=tuple(_ZR_ARITHMETIC)+('z0_primitive_open_v1','z0_successor_open_v1')
_pr_prior_reconstruct=_zr_reconstruct
def _zr_reconstruct(memory,idx,recipe,api):
    if not isinstance(recipe,dict) or recipe.get('pathway') not in ('z0_primitive_open_v1','z0_successor_open_v1'):
        return _pr_prior_reconstruct(memory,idx,recipe,api)
    parents=recipe.get('parents')
    if (not isinstance(parents,list) or len(parents)!=2 or
        any(type(p) is not int or not 0<=p<idx for p in parents)):
        return None
    records=memory['expressions']
    if any(p>=len(records) for p in parents):return None
    source,unit=(records[p] for p in parents)
    tree=recipe.get('tree',{})
    op=tree.get('op')
    if (op not in ('+','-') or unit.get('tree')!={'leaf':1} or
        unit.get('value')!='1' or tree!={'op':op,'left':source['tree'],'right':{'leaf':1}}):
        return None
    value=_pr_qop(source['value'],op,1,memory)
    if 'expected_value' in recipe and recipe['expected_value']!=encode(value):return None
    primitive='S' if op=='+' else 'P'
    return {'id':idx,'expr':'('+source['expr']+(' + 1)' if primitive=='S' else ' - 1)'),
        'value':encode(value),'tree':tree,'depth':source.get('depth',0)+1,
        'parents':parents,'leaves':list(source.get('leaves',[]))+[1],
        'pathway':recipe['pathway'],'domain':'rational',
        'ancestry':list(source.get('ancestry',[]))+[{'rule':recipe['pathway'],
            'zero_nexus':'Z0','source_id':source['id'],'primitive':primitive}]}

def _pr_energy_step(real,imag,branch,memory):
    if branch not in _ZE_BRANCHES: raise ValueError('Unknown energy branch')
    if branch in ('+1','-1'):
        real=_pr_qop(real,'+' if branch=='+1' else '-',1,memory)
    else:
        imag=_pr_qop(imag,'+' if branch=='+i' else '-',1,memory)
    return real,imag

def _pr_signed_parts(value):
    """Declared sign/magnitude representation, not an arithmetic operation."""
    if type(value) is not int:raise ValueError('Exact signed integer required')
    text=str(value)
    negative=text.startswith('-')
    return negative,int(text[1:] if negative else text)

def _pr_signed_value(negative,magnitude):
    if type(magnitude) is not int or magnitude<0:
        raise ValueError('Invalid natural magnitude')
    return int(('-' if negative and magnitude else '')+str(magnitude))

def _pr_int_step(value,primitive):
    if type(value) is not int or value<0 or primitive!='S':
        raise ValueError('The sole arithmetic primitive is S on natural counters')
    return value+1

def _pr_execute_binding(binding,value):
    if not isinstance(binding,dict):raise ValueError('Invalid executable role')
    body=binding.get('body',{})
    primitive=body.get('primitive')
    if primitive != 'S' or body!=_pr_role_body(primitive):
        raise ValueError('Primitive role signature mismatch')
    return _pr_int_step(value,primitive)

def _pr_guard_worker(function):
    def guarded(memory,*args,**kwargs):
        try: return function(memory,*args,**kwargs)
        except PrimitivePending as exc:
            if kwargs.get('return_id'): raise
            memory.setdefault('primitive_reduction',{}).setdefault('deferred',{})[exc.job]={
                'status':'pending','reason':'primitive_work_budget','nexus':'Z0'}
            return False
    return guarded

for _pr_worker_name in ('work_arithmetic_pair','work_consume','work_consume_op','work_revisit',
    'work_nexus','work_zero_scan','work_zero_source','work_position','work_complex',
    'work_complex_feedback','work_symbolic','work_symbolic_nexus','work_symbolic_position',
    'z0_bridge_work','z0_macro_work'):
    globals()[_pr_worker_name]=_pr_guard_worker(globals()[_pr_worker_name])

_pr_prior_work_calculus=work_calculus
def work_calculus(memory):
    try: return _pr_prior_work_calculus(memory)
    except PrimitivePending as exc:
        return {'status':'pending','reason':'primitive_work_budget','job':exc.job,
                'pending':len(memory['calculus_archive']['queue'])-memory['calculus_archive']['head']}

_pr_prior_load_memory=load_memory
def load_memory():
    memory=_pr_prior_load_memory()
    path=memory_path()+'.successor-work.json'
    if not os.path.exists(path) and os.path.exists(memory_path()+'.primitive-work.json'):
        path=memory_path()+'.primitive-work.json'
    if os.path.exists(path) and os.path.exists(memory_path()):
        with open(path,encoding='utf-8') as handle: checkpoint=json.load(handle)
        if checkpoint.get('source_sha256')==_z7_hash_file(memory_path()):
            state=checkpoint.get('primitive_reduction')
            if not isinstance(state,dict) or state.get('schema') not in (PRIMITIVE_SCHEMA,'z0_sp_register_machine_v1'):
                raise ValueError('Invalid primitive continuation state')
            # Each job is fully replayed on use. Never accept an unvalidated result.
            memory['primitive_reduction']=state
    memory['_primitive_work_remaining']=16384
    return memory

_pr_prior_save_memory=save_memory
def save_memory(memory):
    global _PR_MEMORY
    prior=_PR_MEMORY
    _PR_MEMORY=memory
    remaining=memory.pop('_primitive_work_remaining',16384)
    try:
        # Keep the original archive, manifest, temporal ledger and observers.
        # Observer arithmetic gets its own bounded allowance after commit.
        result=_pr_prior_save_memory(memory)
        _ze_atomic_json(memory_path()+'.successor-work.json',{
            'schema':PRIMITIVE_SCHEMA,'source_sha256':_z7_hash_file(memory_path()),
            'primitive_reduction':memory.get('primitive_reduction',{})})
        print('Z0 primitive construction:',primitive_report(memory))
        return result
    finally:
        _PR_MEMORY=prior
        memory['_primitive_work_remaining']=remaining




# Typed replay of historical S/P role definitions remains available solely
# for archive recovery. These definitions are never active primitive bindings.
_s_prior_z6_build=_z6_build
def _z6_build(memory,domain,idx,recipe):
    if domain!='roles' or not isinstance(recipe,dict) or recipe.get('rule')!='bind_primitive_operation_role':
        return _s_prior_z6_build(memory,domain,idx,recipe)
    try:
        parents=recipe['parents'];label=recipe['label']
        if len(parents)!=1 or label not in ('S','P') or recipe['operation']!='transform':return None
        parent=memory['roles_archive']['expressions'][parents[0]]
        slot=parent['depth'];counter_id=foundation_expression_id(memory,slot)
        refs=[{'archive':'rational','id':counter_id}]
        if counter_id is None or refs!=recipe['sources']:return None
        path=parent['path']+[label]
        body={'kind':'operation','primitive':label,'input':'integer','output':'integer','nexus':'Z0'}
        return {'id':idx,'kind':'operation','label':label,'body':body,'value':label+'(integer)',
            'rule':'bind_primitive_operation_role','parents':parents,'sources':refs,'path':path,
            'depth':slot+1,'slot':{'counter':slot,'foundation_id':counter_id},
            'expr':' -> '.join(path),'operation':'transform','pathway':recipe['pathway'],
            'formal_rule':recipe['pathway']}
    except (KeyError,IndexError,TypeError,ValueError):return None

_s_prior_discover=z0_discover_primitive_patterns
def z0_discover_primitive_patterns(memory,**kwargs):
    report=_s_prior_discover(memory,**kwargs)
    records=memory['expressions']
    paths={}
    observations=[]
    for rec in records:
        if rec.get('pathway')!='z0_successor_open_v1':continue
        edge=rec['ancestry'][-1]
        parent=edge['source_id']
        if edge.get('primitive')!='S':raise ValueError('Non-S successor frontier evidence')
        prefix=paths.get(parent,[])
        path=prefix+[rec['id']]
        paths[rec['id']]=path
        for width in (2,3):
            remaining=list(path);blocks=[]
            while len(remaining)>=width:
                block=remaining[:width];remaining=remaining[width:]
                start=records[block[0]]['ancestry'][-1]['source_id']
                blocks.append({'source_id':start,'result_id':block[-1],
                    'primitive_record_ids':block,'successor_count':width})
            if remaining or len(blocks)<2:continue
            observations.append({'source_id':blocks[0]['source_id'],'result_id':rec['id'],
                'increment':width,'repetitions':len(blocks),'blocks':blocks,
                'observed_result':rec['value'],'primitive_basis':['S'],'nexus':'Z0',
                'status':'observed_repeated_addition_path',
                'scope':'grouping existing S paths; not a discovered general multiplication law'})
    memory.setdefault('rule_registry',{})['z0_successor_repeated_addition_v1']={
        'status':'evidence_led_observer','primitive_basis':['S'],'observations':observations,
        'grouping_rule':'partition existing paths into blocks of two or three S steps',
        'general_multiplication_claim':False}
    report['repeated_addition_observations']=len(observations)
    return report

# ============================================================
# V4.9.5 — RETAINED Z0 -> S0 -> S1i CONSTRUCTION
# Counter extension and role selection share the central zero gateway.
# The imaginary coordinate interpretation is an explicit representation rule.
# ============================================================
CONSTRUCTOR_RULE = 'zero_successor_role_constructor_v495'
CONSTRUCTOR_CONTEXT_RULE = 'retain_zero_successor_context_v495'
CONSTRUCTOR_CHILD_RULE = 'extend_counter_in_selected_role_v495'
CONSTRUCTOR_COMPLEX_RULE = 'successor_role_to_complex_v495'

def _ctx_body(counter,role,operation_role,job=None):
    if type(counter) is not int or counter<0 or role not in ('context','real','imaginary'):
        raise ValueError('Invalid successor construction payload')
    coordinates=(None if role=='context' else
                 {'real':str(counter),'imaginary':'0'} if role=='real' else
                 {'real':'0','imaginary':str(counter)})
    return {'kind':'successor_construction','counter':counter,'role':role,
        'operation_role':operation_role,'coordinates':coordinates,
        'primitive_job':job,'zero_nexus':'Z0'}

_ctx_prior_body_text=role_body_text
def role_body_text(body):
    if body.get('kind')!='successor_construction':return _ctx_prior_body_text(body)
    expected=_ctx_body(body.get('counter'),body.get('role'),body.get('operation_role'),body.get('primitive_job'))
    if body!=expected:raise ValueError('Changed successor construction payload')
    return 'S'+str(body['counter'])+('i' if body['role']=='imaginary' else '')

_ctx_prior_transition=_role_transition_exact
def _role_transition_exact(memory,source_id,target):
    if not isinstance(target,dict) or target.get('constructor') not in ('successor_context','successor_child'):
        return _ctx_prior_transition(memory,source_id,target)
    records=memory['roles_archive']['expressions']
    if type(source_id) is not int or not 0<=source_id<len(records):raise ValueError('Invalid construction source')
    source=records[source_id]
    slot=source['depth']
    if slot>=ROLE_MAX_DEPTH:return None,'role_depth_limit'
    if slot>=len(memory['foundation']['states']):return None,'waiting_for_emergent_slot'
    counter_id=foundation_expression_id(memory,slot)
    if counter_id is None:raise ValueError('Construction slot has no foundation backing')
    binding=_pr_bind_roles(memory)['S']
    operation_role=binding['id']
    if target['constructor']=='successor_context':
        if target!={'constructor':'successor_context'} or source_id!=0 or source['rule']!='reference_foundation_zero':
            raise ValueError('S0 requires the retained zero-origin construction')
        body=_ctx_body(0,'context',operation_role)
        rule=CONSTRUCTOR_CONTEXT_RULE
    else:
        if set(target)!={'constructor','role'} or target['role'] not in ('real','imaginary'):
            raise ValueError('Unknown successor placement role')
        parent_body=source['body']
        if source.get('kind')!='construction' or parent_body.get('kind')!='successor_construction':
            raise ValueError('Successor extension requires a retained construction context')
        # Counter and role are committed in ONE child. There is no S1 record
        # inserted between S0 and S1i. The S computation itself retains its trace.
        counter=zero_core(memory,'roles',operation='execute',operands=(operation_role,parent_body['counter']))
        job=memory['primitive_reduction']['passages'][-1]['job']
        body=_ctx_body(counter,target['role'],operation_role,job)
        rule=CONSTRUCTOR_CHILD_RULE
    label=role_body_text(body)
    return {'kind':'construction','label':label,'body':body,'value':label,'rule':rule,
        'parents':[source_id],
        'sources':[{'archive':'rational','id':counter_id},{'archive':'roles','id':operation_role}],
        'path':source['path']+[label],'depth':slot+1,
        'slot':{'counter':slot,'foundation_id':counter_id}},None

def _ctx_record(memory,parent,target):
    result,reason=zero_core(memory,'roles',operation='transform',operands=(parent,target))
    if reason:return None,reason
    idx=role_record(memory,result,'transform')
    if idx is None:
        idx=next((r['id'] for r in memory['roles_archive']['expressions']
            if r.get('parents')==[parent] and r.get('rule')==result['rule'] and
               r.get('body')==result['body'] and r.get('sources')==result['sources']),None)
    if idx is None:raise ValueError('Construction insertion did not retain an exact record')
    return idx,None

def zero_constructor_bootstrap(memory):
    upgrade_roles(memory)
    memory['rule_registry'].setdefault(CONSTRUCTOR_RULE,{
        'status':'explicit_executable_construction_rules','nexus':'Z0',
        'arithmetic_primitive':['S'],'source_policy':'retain every source',
        'counter_and_role':'one direct child construction',
        'role_placements':{'real':'(counter,0)','imaginary':'(0,counter)'},
        'physical_dimension_claim':False,'imaginary_role_is_supplied':True})
    context,reason=_ctx_record(memory,0,{'constructor':'successor_context'})
    if reason:return {'status':'pending','reason':reason}
    child,reason=_ctx_record(memory,context,{'constructor':'successor_child','role':'imaginary'})
    if reason:return {'status':'pending','reason':reason}
    source=memory['roles_archive']['expressions'][child]
    coordinates=source['body']['coordinates']
    # This is an embedding of this particular construction, not a substitution
    # of the older seeded i. Its typed source points to the S1i role record.
    embedded=complex_record(memory,(number(coordinates['real']),number(coordinates['imaginary'])),
        'S1i',[],'embed',CONSTRUCTOR_COMPLEX_RULE,depth=source['depth'],
        sources=[{'archive':'roles','id':child}])
    if embedded is None:
        embedded=next((r['id'] for r in memory['complex_archive']['expressions']
            if r.get('pathway')==CONSTRUCTOR_COMPLEX_RULE and r.get('sources')==[{'archive':'roles','id':child}]),None)
    if embedded is None:raise ValueError('Constructed imaginary value has no typed embedding')
    memory['zero_constructor_path']={'rule':CONSTRUCTOR_RULE,'nexus':'Z0',
        'nodes':[{'name':'Z0','archive':'roles','id':0},
                 {'name':'S0','archive':'roles','id':context},
                 {'name':'S1i','archive':'roles','id':child}],
        'complex_embedding':embedded,'retained':True,
        'zero_alias':'existing numeric-role origin backed by foundation zero'}
    return zero_constructor_report(memory)

def zero_constructor_report(memory):
    path=memory.get('zero_constructor_path')
    if path is None:return memory.get('zero_constructor_pending',{'status':'not_created'})
    records=memory['roles_archive']['expressions']
    refs=[node['id'] for node in path['nodes']]
    origin,context,child=(records[i] for i in refs)
    valid=(origin['rule']=='reference_foundation_zero' and context['parents']==[refs[0]] and
        child['parents']==[refs[1]] and context['label']=='S0' and child['label']=='S1i' and
        child['body']['counter']==1 and child['body']['role']=='imaginary' and
        all(rec.get('zero_core_passage',{}).get('zero_nexus')=='Z0' for rec in (origin,context,child)))
    return {'status':'constructed' if valid else 'invalid','path':['Z0','S0','S1i'],
        'role_record_ids':refs,'all_retained':valid,'direct_child':child['parents']==[context['id']],
        'counter':child['body']['counter'],'role':child['body']['role'],
        'coordinates':child['body']['coordinates'],'arithmetic_primitives':['S'],
        'primitive_job':child['body']['primitive_job'],'complex_embedding':path['complex_embedding'],
        'interpretation':'explicit imaginary role placement; not spontaneous discovery of complex axioms'}

# Independent archive replay verifies the typed links, role placement and the
# retained S execution. It does not trust labels or coordinate strings alone.
_ctx_prior_replay_roles=_Z5Replay.roles
def _ctx_replay_roles(self,rec,parents,sources):
    if rec.get('rule') not in (CONSTRUCTOR_CONTEXT_RULE,CONSTRUCTOR_CHILD_RULE):
        return _ctx_prior_replay_roles(self,rec,parents,sources)
    self.require(len(parents)==1 and rec['operation']=='transform' and rec['kind']=='construction',
        'invalid_successor_constructor_transition')
    parent=self.record('roles',rec['parents'][0]);slot=parent['depth']
    foundation_id=rec['slot']['foundation_id']
    self.require(rec['depth']==slot+1 and rec['slot']['counter']==slot and
        self.record('rational',foundation_id)['pathway']=='foundation_state_count_v3' and
        self.get('rational',foundation_id)==slot,'invalid_constructor_slot')
    body=rec['body'];rid=body['operation_role']
    expected_sources=[{'archive':'rational','id':foundation_id},{'archive':'roles','id':rid}]
    self.require(rec['sources']==expected_sources and len(sources)==2,
        'invalid_constructor_typed_sources')
    self.require(sources[1]=={'kind':'operation','primitive':'S','input':'natural_counter',
        'output':'natural_counter','nexus':'Z0'},'invalid_constructor_executable_role')
    if rec['rule']==CONSTRUCTOR_CONTEXT_RULE:
        self.require(parent['id']==0 and parents[0]=={'kind':'numeric','value':'0'},'invalid_S0_origin')
        expected={'kind':'successor_construction','counter':0,'role':'context',
            'operation_role':rid,'coordinates':None,'primitive_job':None,'zero_nexus':'Z0'}
    else:
        self.require(parent['kind']=='construction' and parents[0]['kind']=='successor_construction',
            'invalid_successor_parent_context')
        self.require(body['role'] in ('real','imaginary') and type(body['counter']) is int,
            'invalid_constructor_role')
        job=self.m['primitive_reduction']['jobs'][body['primitive_job']]
        primitive_validate(job)
        self.require(job['status']=='complete' and job['program']=='stepS' and
            job['inputs']==[parents[0]['counter']] and job['result']==[body['counter']] and
            job['primitives']==['S'] and job['operation_roles']['S']['archive']=='roles' and
            job['operation_roles']['S']['id']==rid,'invalid_constructor_S_evidence')
        # Independent mathematical check, separate from the execution engine.
        self.require(body['counter']==parents[0]['counter']+1,'constructor_counter_disagreement')
        coords=({'real':str(body['counter']),'imaginary':'0'} if body['role']=='real' else
                {'real':'0','imaginary':str(body['counter'])})
        expected={'kind':'successor_construction','counter':body['counter'],'role':body['role'],
            'operation_role':rid,'coordinates':coords,'primitive_job':body['primitive_job'],'zero_nexus':'Z0'}
    label='S'+str(expected['counter'])+('i' if expected['role']=='imaginary' else '')
    self.require(body==expected and rec['label']==label and rec['value']==label and
        rec['path']==parent['path']+[label] and rec['expr']==' -> '.join(rec['path']),
        'constructor_payload_or_path_disagreement')
    return expected
_Z5Replay.roles=_ctx_replay_roles

_ctx_prior_replay_complex=_Z5Replay.complex
def _ctx_replay_complex(self,rec,parents,sources):
    if rec.get('pathway')!=CONSTRUCTOR_COMPLEX_RULE:
        return _ctx_prior_replay_complex(self,rec,parents,sources)
    self.require(not parents and rec['operation']=='embed' and len(sources)==1 and
        rec['sources'][0]['archive']=='roles','invalid_constructor_complex_embedding')
    body=sources[0]
    self.require(body.get('kind')=='successor_construction' and body.get('role') in ('real','imaginary'),
        'invalid_constructor_complex_source')
    origin=self.record('roles',rec['sources'][0]['id'])
    pair=Fraction(body['coordinates']['real']),Fraction(body['coordinates']['imaginary'])
    self.require((Fraction(rec['real']),Fraction(rec['imaginary']))==pair and
        rec['value']==complex_key(*pair) and rec['expr']==origin['label'] and rec['depth']==origin['depth'],
        'constructor_complex_embedding_disagreement')
    return pair
_Z5Replay.complex=_ctx_replay_complex

_ctx_prior_recipe=_z6_recipe
def _z6_recipe(domain,rec):
    recipe=_ctx_prior_recipe(domain,rec)
    if domain=='roles' and rec.get('rule') in (CONSTRUCTOR_CONTEXT_RULE,CONSTRUCTOR_CHILD_RULE):
        recipe['constructor_target']=({'constructor':'successor_context'} if rec['rule']==CONSTRUCTOR_CONTEXT_RULE
            else {'constructor':'successor_child','role':rec['body']['role']})
    return recipe

_ctx_prior_build=_z6_build
def _z6_build(memory,domain,idx,recipe):
    if not isinstance(recipe,dict):return _ctx_prior_build(memory,domain,idx,recipe)
    try:
        if domain=='roles' and recipe.get('rule') in (CONSTRUCTOR_CONTEXT_RULE,CONSTRUCTOR_CHILD_RULE):
            if recipe['operation']!='transform' or len(recipe['parents'])!=1:return None
            result,reason=zero_core(memory,'roles',operation='transform',
                operands=(recipe['parents'][0],recipe['constructor_target']))
            if reason or result['sources']!=recipe['sources'] or result['rule']!=recipe['rule']:return None
            result.update(id=idx,expr=' -> '.join(result['path']),operation='transform',
                pathway=recipe['pathway'],formal_rule=recipe['pathway'])
            return result
        if domain=='complex' and recipe.get('pathway')==CONSTRUCTOR_COMPLEX_RULE:
            if recipe['parents'] or len(recipe['sources'])!=1 or recipe['sources'][0]['archive']!='roles':return None
            ref=recipe['sources'][0];verifier=_Z5Replay(memory);body=verifier.source(ref)
            source=memory['roles_archive']['expressions'][ref['id']]
            if body.get('kind')!='successor_construction' or body['coordinates'] is None:return None
            re=body['coordinates']['real'];im=body['coordinates']['imaginary']
            return {'id':idx,'expr':source['label'],'real':re,'imaginary':im,
                'value':complex_key(number(re),number(im)),'parents':[],'operation':'embed',
                'pathway':CONSTRUCTOR_COMPLEX_RULE,'depth':source['depth'],'sources':recipe['sources']}
    except (ValueError,KeyError,IndexError,TypeError,PrimitivePending):return None
    return _ctx_prior_build(memory,domain,idx,recipe)

_ctx_prior_energy_value=_ze_exact_value
def _ze_exact_value(rec,domain):
    if domain=='roles' and rec.get('body',{}).get('kind')=='successor_construction':
        body=rec['body'];role_body_text(body)
        if body['coordinates'] is None:raise ValueError('Successor context has no numeric placement yet')
        return number(body['coordinates']['real']),number(body['coordinates']['imaginary'])
    return _ctx_prior_energy_value(rec,domain)

_ctx_prior_work_roles=work_roles
def work_roles(memory):
    try:report=zero_constructor_bootstrap(memory)
    except PrimitivePending as exc:
        memory['zero_constructor_pending']={'status':'pending','reason':'S work budget','job':exc.job}
        return {'constructor':memory['zero_constructor_pending']}
    result=_ctx_prior_work_roles(memory)
    result['constructor']=report
    return result

_ctx_prior_query=query_v45
def query_v45(memory,text):
    if text.strip().lower()=='constructor':
        report=zero_constructor_report(memory)
        print('ZERO CONSTRUCTOR:',report)
        if report.get('status')=='constructed':
            for name,idx in zip(('Z0','S0','S1i'),report['role_record_ids']):
                print('  '+name+': roles '+str(idx))
        return True
    return _ctx_prior_query(memory,text)

# ============================================================
# V4.9.6 — CONNECTED ZERO WORKFLOW
# Applicable functions share one gateway and persistent feedback. Handlers
# have explicit domains; observation never implies blanket mutation/repair.
# ============================================================
ZERO_CONNECTED_RULE='zero_connected_workflow_v1'
ZERO_CONNECTED_MACRO='zero_connected_repeat_add_v1'
ZERO_CONNECTED_RECORD_BUDGET=512
ZERO_CONNECTED_CANDIDATE_BUDGET=4
ZERO_CONNECTED_EXECUTION_BUDGET=2
ZERO_CONNECTED_RESERVED_STEPS=2048
_WF_ACTIVE_MEMORY=None
_WF_STACK=[]
_WF_CAPTURE_SUSPENDED=0

def _wf_memory(memory):
    return isinstance(memory,dict) and memory.get('schema')==1 and isinstance(memory.get('foundation'),dict)

def _wf_state(memory):
    state=memory.setdefault('zero_connections',{'schema':1,'nexus':'Z0','rule':ZERO_CONNECTED_RULE,
        'events':[],'record_queue':[],'record_head':0,'admissions':{},'archive_cursors':{},
        'candidates':{},'candidate_order':[],'candidate_cursor':0,
        'execution_queue':[],'execution_head':0,'registered':{},'feedback':[],
        'handler_calls':{},'rejected':[],'max_call_depth':0,'checkpoints':0})
    if state.get('schema')!=1 or state.get('rule')!=ZERO_CONNECTED_RULE or state.get('nexus')!='Z0':
        raise ValueError('Incompatible connected-zero checkpoint')
    return state

def _wf_pack(value):
    if value is None or isinstance(value,(str,int,float,bool)):return value
    if isinstance(value,Fraction):return {'rational':str(value)}
    if isinstance(value,(list,tuple)) and len(value)<=8:
        return [_wf_pack(v) for v in value]
    return {'type':type(value).__name__,'digest':_pr_hashlib.sha256(
        json.dumps(value,sort_keys=True,default=str,separators=(',',':')).encode()).hexdigest()}

def _wf_event(memory,domain,operation,kind,payload=None):
    state=_wf_state(memory);idx=len(state['events'])
    parent=next((event for owner,event in reversed(_WF_STACK) if owner==id(memory)),None)
    event={'id':idx,'nexus':'Z0','domain':domain,'operation':operation,'kind':kind,
        'parent_event':parent,'payload':payload,'status':'entered'}
    state['events'].append(event)
    key=domain+':'+str(operation if operation is not None else kind)
    state['handler_calls'][key]=state['handler_calls'].get(key,0)+1
    return event

def _wf_admit(memory,domain,record,event,historical=False):
    state=_wf_state(memory);key=domain+':'+str(record['id']);digest=_zr_digest(_zr_payload(record))
    previous=state['admissions'].get(key)
    if previous is not None:
        if previous['digest']!=digest:raise ValueError('Accepted construction changed after zero admission: '+key)
        return
    admission={'archive':domain,'id':record['id'],'digest':digest,'event':event,
        'historical_observation':bool(historical),'status':'pending','stages':{}}
    state['admissions'][key]=admission
    state['record_queue'].append(key)

def _wf_seed_existing(memory):
    state=_wf_state(memory)
    for domain in _ZR_DOMAINS:
        records=archive_records(memory,domain);start=state['archive_cursors'].get(domain,0)
        if start>len(records):raise ValueError('Connected archive cursor exceeds retained records')
        for rec in records[start:]:
            key=domain+':'+str(rec['id'])
            if key not in state['admissions']:
                event=_wf_event(memory,domain,None,'historical_record_observation',{'id':rec['id']})
                _wf_admit(memory,domain,rec,event['id'],historical=True)
                event['status']='completed'
        state['archive_cursors'][domain]=len(records)

def zero_connected_reserve(memory):
    if '_zero_reserved_primitive_budget' in memory:return
    available=memory.setdefault('_primitive_work_remaining',16384)
    reserve=min(ZERO_CONNECTED_RESERVED_STEPS,available)
    memory['_primitive_work_remaining']=available-reserve
    memory['_zero_reserved_primitive_budget']=reserve

def _wf_release_reserved(memory):
    memory['_primitive_work_remaining']=memory.get('_primitive_work_remaining',0)+memory.pop('_zero_reserved_primitive_budget',0)

def _wf_pattern(rec):
    if rec.get('pathway','').startswith(ZERO_CONNECTED_MACRO+'_src_'):return None
    return candidate_for(rec)

def _wf_discover_record(memory,rec):
    proposal=_wf_pattern(rec)
    if proposal is None:return None
    state=_wf_state(memory)
    key=_pr_hashlib.sha256(fingerprint([proposal['term'],proposal['count']]).encode()).hexdigest()
    candidate=state['candidates'].get(key)
    if candidate is None:
        candidate={'id':key,'term':_pr_copy.deepcopy(proposal['term']),'count':proposal['count'],
            'evidence':[],'validated_sources':[],'scheduled_sources':[],'executed_sources':[],
            'status':'observed_untrusted','validation':None,'nexus':'Z0'}
        state['candidates'][key]=candidate;state['candidate_order'].append(key)
    if rec['id'] not in candidate['evidence']:candidate['evidence'].append(rec['id'])
    return key

def _wf_process_record(memory,key,verifier):
    state=_wf_state(memory);admission=state['admissions'][key]
    domain=admission['archive'];idx=admission['id'];records=archive_records(memory,domain)
    if type(idx) is not int or not 0<=idx<len(records):raise ValueError('Connected admission refers to a missing record')
    rec=records[idx];stages=admission['stages']
    if _zr_digest(_zr_payload(rec))!=admission['digest']:raise ValueError('Admitted construction payload changed')
    stages['provenance']={'parents':list(rec.get('parents',[])),'sources':_pr_copy.deepcopy(rec.get('sources',[]))}
    stages['roles']={'status':'typed_role_checked' if domain=='roles' else 'typed_domain_context',
        'domain':domain,'kind':rec.get('kind')}
    proposal=None
    if domain=='rational':proposal=_wf_discover_record(memory,rec)
    stages['discovery']={'candidate':proposal,'status':'observed_untrusted' if proposal else 'no_matching_repeat_pattern'}
    verifier.get(domain,idx)
    stages['validation']={'status':'independently_replayed','rule':'independent_typed_domain_replay'}
    if proposal:
        candidate=state['candidates'][proposal]
        if idx not in candidate['validated_sources']:candidate['validated_sources'].append(idx)
        if candidate['status']=='observed_untrusted':candidate['status']='pending_primitive_validation'
    stages['registry']={'status':'pending_primitive_expansion' if proposal else 'not_applicable'}
    stages['feedback']={'status':'retained_in_connected_evidence','nexus':'Z0'}
    admission['status']='verified'
    return admission

def _wf_begin_expansion(memory,candidate,source_id):
    verifier=_Z5Replay(memory);verifier.get('rational',source_id)
    source=memory['expressions'][source_id]
    proposal=candidate_for(source)
    if (proposal is None or proposal['term']!=candidate['term'] or proposal['count']!=candidate['count']):
        raise ValueError('Candidate no longer matches its source construction')
    term,term_expression=evaluate_tree(candidate['term'],tracking=memory)
    if term is None:raise ValueError('Repeated term is undefined')
    return {'source_id':source_id,'term':_pr_copy.deepcopy(candidate['term']),
        'term_value':str(term),'count':candidate['count'],'step':0,'accumulator':'0','addition_jobs':[]}

def _wf_continue_expansion(memory,progress):
    # Each completed addition has the actual S-only register-machine evidence.
    # The cursor and incomplete VM job both persist if the allowance expires.
    while progress['step']<progress['count']:
        result=zero_core(memory,'rational',operation='+',
            operands=(number(progress['accumulator']),number(progress['term_value'])))
        job=memory['primitive_reduction']['passages'][-1]['job']
        progress['addition_jobs'].append(job)
        progress['accumulator']=str(result);progress['step']+=1
    return progress

def _wf_validate_candidate(memory,key):
    state=_wf_state(memory);candidate=state['candidates'][key]
    if not candidate['validated_sources']:return {'status':'awaiting_verified_source'}
    if candidate['status']=='registered':
        _wf_bind_operation_role(memory,candidate)
        return {'status':'registered'}
    if candidate['validation'] is None:
        candidate['validation']=_wf_begin_expansion(memory,candidate,candidate['validated_sources'][0])
    progress=_wf_continue_expansion(memory,candidate['validation'])
    expected=memory['expressions'][progress['source_id']]['value']
    if progress['accumulator']!=expected:raise ValueError('Repeated addition disagrees with archived evidence')
    candidate['status']='registered'
    state['registered'][key]={'id':key,'operation':'repeat_add','term':_pr_copy.deepcopy(candidate['term']),
        'count':candidate['count'],'evidence':list(candidate['validated_sources']),
        'validation_jobs':list(progress['addition_jobs']),'status':'validated_concrete_expansion',
        'primitive_basis':['S'],'nexus':'Z0','scope':'this observed term construction and repeat count'}
    registry=memory['rule_registry'].setdefault(ZERO_CONNECTED_MACRO,{
        'status':'executable_validated_concrete_expansions','primitive_basis':['S'],
        'entries':[],'general_operation_invention_claim':False})
    if key not in registry['entries']:registry['entries'].append(key)
    _wf_bind_operation_role(memory,candidate)
    return {'status':'registered','candidate':key}

def _wf_schedule_registered(memory):
    state=_wf_state(memory)
    for key in state['candidate_order']:
        candidate=state['candidates'][key]
        if candidate['status']!='registered':continue
        for source in candidate['validated_sources']:
            if source in candidate['scheduled_sources']:continue
            state['execution_queue'].append({'candidate':key,'source_id':source,'progress':None,'status':'pending'})
            candidate['scheduled_sources'].append(source)

def _wf_record_from_plan(memory,idx,plan):
    source=memory['expressions'][plan['source_id']]
    return {'id':idx,'expr':source['expr'],'value':plan['result'],'tree':_pr_copy.deepcopy(source['tree']),
        'depth':source['depth'],'parents':[source['id']],'leaves':list(source['leaves']),
        'pathway':ZERO_CONNECTED_MACRO+'_src_'+str(source['id']),'domain':'rational',
        'operation':'repeat_add','execution':_pr_copy.deepcopy(plan),
        'ancestry':_pr_copy.deepcopy(source['ancestry'])+[{'rule':ZERO_CONNECTED_MACRO,
            'candidate':plan['candidate'],'source_id':source['id'],'result':plan['result'],
            'addition_jobs':list(plan['addition_jobs']),'zero_nexus':'Z0'}]}

def _wf_execute(memory,task):
    state=_wf_state(memory);candidate=state['candidates'][task['candidate']]
    if candidate['status']!='registered':raise ValueError('Attempted execution of an unvalidated operation')
    if task['source_id'] not in candidate['validated_sources']:raise ValueError('Unverified operation source')
    if task['progress'] is None:task['progress']=_wf_begin_expansion(memory,candidate,task['source_id'])
    progress=_wf_continue_expansion(memory,task['progress'])
    if progress['accumulator']!=memory['expressions'][task['source_id']]['value']:
        raise ValueError('Operation execution disagrees with its source')
    plan={'candidate':candidate['id'],'source_id':task['source_id'],'term':_pr_copy.deepcopy(candidate['term']),
        'term_value':progress['term_value'],'count':candidate['count'],'result':progress['accumulator'],
        'addition_jobs':list(progress['addition_jobs']),'primitive_basis':['S'],'zero_nexus':'Z0'}
    rec=_wf_record_from_plan(memory,len(memory['expressions']),plan);rec.pop('id')
    idx=add_expression(memory,rec)
    if idx is None:
        idx=next((r['id'] for r in memory['expressions'] if r.get('pathway')==rec['pathway'] and
            r.get('tree')==rec['tree'] and r.get('parents')==rec['parents']),None)
    if idx is None:raise ValueError('Connected operation construction was not retained')
    zero_core(memory,'connected',operation='feedback_record',operands=(idx,))
    task.update(status='complete',result_id=idx)
    if task['source_id'] not in candidate['executed_sources']:candidate['executed_sources'].append(task['source_id'])
    return idx

def _wf_feedback_record(memory,idx):
    # Rejoin the actual existing queue, archive observers and cross-domain
    # import machinery. This is not a report-only candidate sidecar.
    schedule_frontier(memory,idx)
    schedule_zero_foundation_scan(memory,idx)
    enqueue(memory,{'kind':'revisit','new':idx,'cursor':0,'rule':'revisit_v1'})
    observe(memory,memory['expressions'][idx],{'observer_added':0})
    _wf_state(memory)['feedback'].append({'kind':'executed_construction','archive':'rational','id':idx,
        'targets':['frontier','zero_foundation_scan','revisit','observer','symbolic_import_cursor'],
        'nexus':'Z0'})
    return {'scheduled':idx}

def zero_connected_service(memory,record_budget=ZERO_CONNECTED_RECORD_BUDGET,execution_budget=ZERO_CONNECTED_EXECUTION_BUDGET):
    state=_wf_state(memory);_wf_seed_existing(memory)
    verifier=_Z5Replay(memory)
    processed=0
    while processed<record_budget and state['record_head']<len(state['record_queue']):
        key=state['record_queue'][state['record_head']]
        try:zero_core(memory,'connected',operation='process_record',operands=(key,verifier))
        except (ValueError,KeyError,IndexError,TypeError) as exc:
            state['admissions'][key]['status']='rejected'
            state['rejected'].append({'record':key,'reason':str(exc),'nexus':'Z0'})
            raise ZeroRecoveryPending('Connected-zero validation rejected '+key+': '+str(exc)) from exc
        state['record_head']+=1;processed+=1
    candidate_count=len(state['candidate_order'])
    for unused in range(min(ZERO_CONNECTED_CANDIDATE_BUDGET,candidate_count)):
        key=state['candidate_order'][state['candidate_cursor']%candidate_count]
        state['candidate_cursor']+=1
        try:zero_core(memory,'connected',operation='validate_candidate',operands=(key,))
        except PrimitivePending:break
    zero_core(memory,'connected',operation='schedule_registered')
    executed=0
    while executed<execution_budget and state['execution_head']<len(state['execution_queue']):
        task=state['execution_queue'][state['execution_head']]
        try:zero_core(memory,'connected',operation='execute_candidate',operands=(task,))
        except PrimitivePending:break
        state['execution_head']+=1;executed+=1
    return zero_connections_report(memory)

# Preserve a standalone, independently replayable construction recipe for the
# new executable records. Registry labels alone are not acceptance evidence.
_wf_old_rational_replay=_Z5Replay.rational
def _wf_replay_rational(self,rec,parents,sources):
    value=_wf_old_rational_replay(self,rec,parents,sources)
    if not rec.get('pathway','').startswith(ZERO_CONNECTED_MACRO+'_src_'):return value
    plan=rec['execution'];source=self.record('rational',plan['source_id'])
    _wf_check_expansion(self,plan)
    proposal=candidate_for(source)
    self.require(rec['parents']==[source['id']] and rec['operation']=='repeat_add' and
        rec['tree']==source['tree'] and rec['expr']==source['expr'] and rec['depth']==source['depth'] and
        rec['leaves']==source['leaves'] and not sources,'invalid_connected_execution_lineage')
    self.require(proposal is not None and plan['term']==proposal['term'] and plan['count']==proposal['count'] and
        plan['primitive_basis']==['S'] and plan['zero_nexus']=='Z0' and len(plan['addition_jobs'])==plan['count'],
        'invalid_connected_execution_plan')
    allowed=self.legacy_leaves.get(source['id'],set())
    term=self.rational_tree(plan['term'],allowed)
    self.require(str(term)==plan['term_value'],'connected_term_value_disagreement')
    acc=Fraction(0)
    for key in plan['addition_jobs']:
        job=self.m['primitive_reduction']['jobs'][key];primitive_validate(job)
        self.require(job['status']=='complete' and job['program']=='qadd' and job['primitives']==['S'] and
            job['inputs']==[acc.numerator,acc.denominator,term.numerator,term.denominator],
            'invalid_connected_addition_evidence')
        acc=Fraction(*job['result'])
    self.require(acc==value and str(acc)==plan['result'] and value==parents[0],
        'connected_expansion_result_disagreement')
    self.require(rec['pathway']==ZERO_CONNECTED_MACRO+'_src_'+str(source['id']),
        'connected_execution_identity_disagreement')
    return value
_Z5Replay.rational=_wf_replay_rational

_wf_old_manifest=_zr_manifest_entry
def _zr_manifest_entry(domain,rec):
    result=_wf_old_manifest(domain,rec)
    if domain=='rational' and rec.get('pathway','').startswith(ZERO_CONNECTED_MACRO+'_src_'):
        result['recipe']={'tree':_pr_copy.deepcopy(rec['tree']),'parents':list(rec['parents']),
            'pathway':rec['pathway'],'execution':_pr_copy.deepcopy(rec['execution'])}
    return result

_wf_old_reconstruct=_zr_reconstruct
def _zr_reconstruct(memory,idx,recipe,api):
    if not isinstance(recipe,dict) or not recipe.get('pathway','').startswith(ZERO_CONNECTED_MACRO+'_src_'):
        return _wf_old_reconstruct(memory,idx,recipe,api)
    try:
        plan=recipe['execution'];source=plan['source_id']
        if type(source) is not int or not 0<=source<idx or recipe['parents']!=[source]:return None
        _Z5Replay(memory).get('rational',source)
        rec=_wf_record_from_plan(memory,idx,plan)
        if rec['pathway']!=recipe['pathway'] or rec['tree']!=recipe['tree']:return None
        # Validate the hypothetical restored slot without modifying the source.
        probe=dict(memory);probe['expressions']=list(memory['expressions']);probe['expressions'][idx]=rec
        _Z5Replay(probe).get('rational',idx)
        return rec
    except (ValueError,KeyError,TypeError,IndexError):return None

def zero_connections_report(memory):
    state=memory.get('zero_connections',{})
    return {'rule':ZERO_CONNECTED_RULE,'nexus':'Z0','events':len(state.get('events',[])),
        'admitted_records':len(state.get('admissions',{})),
        'verified_records':sum(r['status']=='verified' for r in state.get('admissions',{}).values()),
        'pending_records':len(state.get('record_queue',[]))-state.get('record_head',0),
        'candidate_patterns':len(state.get('candidates',{})),
        'registered_operations':len(state.get('registered',{})),
        'operation_roles':{key:c['role_id'] for key,c in state.get('candidates',{}).items() if 'role_id' in c},
        'executed_operations':sum(t['status']=='complete' for t in state.get('execution_queue',[])),
        'pending_executions':len(state.get('execution_queue',[]))-state.get('execution_head',0),
        'feedback_edges':len(state.get('feedback',[])),'rejected':len(state.get('rejected',[])),
        'handler_calls':dict(state.get('handler_calls',{})),
        'connected_functions':['typed_archives','roles','constructor','discovery','independent_validation',
            'operation_registry','primitive_execution','main_scheduler','zero_feedback','energy',
            'foundations','time','temporal','recovery','adaptive','storage'],
        'scope':'applicable handlers only; concrete repeated-addition execution; symbolic algebra remains supplied'}

# Existing callers now enter the same zero function. The raw handlers are
# captured once so a handler cannot recursively dispatch itself.
_WF_RAW={
    ('discovery','observe_archive'):_integrated_discover,
    ('discovery','primitive_patterns'):z0_discover_primitive_patterns,
    ('scheduler','primitive_macros'):z0_macro_schedule,
    ('energy','observe_rational'):_ze_integrate,
    ('energy','observe_cross_domain'):_ze_crosscore_integrate,
    ('foundations','observe'):_zf_observe,
    ('constructor','bootstrap'):zero_constructor_bootstrap,
    ('successor','open_explore'):z0_open_explore,
    ('storage','save'):save_memory,
    ('storage','load'):load_memory,
}
_wf_prior_core=zero_core

def _wf_storage_load():
    global _WF_CAPTURE_SUSPENDED
    _WF_CAPTURE_SUSPENDED+=1
    try:memory=_WF_RAW[('storage','load')]()
    finally:_WF_CAPTURE_SUSPENDED-=1
    checkpoint=memory_path()+'.zero-connections.json'
    if os.path.isfile(checkpoint) and os.path.isfile(memory_path()):
        data=_zg_read(checkpoint)
        if data.get('source_sha256')==_z7_hash_file(memory_path()):
            memory['zero_connections']=data['zero_connections']
    if 'zero_connections' in memory:_wf_state(memory)
    return memory

def _wf_storage_save(memory):
    if not memory.pop('_zero_connected_serviced_for_save',False):
        _wf_release_reserved(memory)
        zero_core(memory,'connected',operation='service')
    memory.pop('_primitive_work_remaining',None)
    return _WF_RAW[('storage','save')](memory)

def _wf_dispatch(memory,domain,operation,operands,kwargs):
    if domain=='connected':
        if operation=='report':return zero_connections_report(memory)
        if operation=='service':return zero_connected_service(memory,**kwargs)
        if operation=='process_record':return _wf_process_record(memory,*operands)
        if operation=='validate_candidate':return _wf_validate_candidate(memory,*operands)
        if operation=='schedule_registered':return _wf_schedule_registered(memory)
        if operation=='execute_candidate':
            task=operands[0];candidate=_wf_state(memory)['candidates'][task['candidate']]
            _wf_bind_operation_role(memory,candidate)
            return zero_core(memory,'roles',operation='execute',operands=(candidate['role_id'],task))
        if operation=='feedback_record':return _wf_feedback_record(memory,*operands)
        raise ValueError('Unknown connected-zero operation')
    key=(domain,operation)
    if key==('roles','execute') and memory is not None and len(operands)==2:
        rid,task=operands
        records=memory.get('roles_archive',{}).get('expressions',[])
        if type(rid) is int and 0<=rid<len(records) and records[rid].get('rule')==ZERO_CONNECTED_ROLE_RULE:
            if not isinstance(task,dict) or records[rid]['body']['candidate']!=task.get('candidate'):
                raise ValueError('Derived operation role received an incompatible execution task')
            _Z5Replay(memory).get('roles',rid)
            return _wf_execute(memory,task)
    if key==('storage','load'):return _wf_storage_load()
    if key==('storage','save'):return _wf_storage_save(memory)
    if key==('successor','open_explore'):
        path,options=operands
        return _WF_RAW[key](path,**options)
    if key==('discovery','primitive_patterns'):
        return _WF_RAW[key](memory,**(operands[0] if operands else {}))
    if key in _WF_RAW:return _WF_RAW[key](memory)
    return _wf_prior_core(memory,domain,operation=operation,operands=operands,**kwargs)

def zero_core(memory,domain,*,operation=None,operands=(),**kwargs):
    global _WF_ACTIVE_MEMORY
    if domain=='connected' and operation=='report':return zero_connections_report(memory)
    effective=memory if _wf_memory(memory) else _WF_ACTIVE_MEMORY
    capture=_wf_memory(effective) and not _WF_CAPTURE_SUSPENDED
    rec=kwargs.get('record');event=None;prior=_WF_ACTIVE_MEMORY
    if capture:
        payload=({'id':rec.get('id'),'historical':bool(kwargs.get('historical'))} if rec is not None else _wf_pack(operands))
        event=_wf_event(effective,domain,operation,'record' if rec is not None else 'operation',payload)
        _WF_STACK.append((id(effective),event['id']));_WF_ACTIVE_MEMORY=effective
        state=_wf_state(effective);state['max_call_depth']=max(state['max_call_depth'],len(_WF_STACK))
    try:
        result=_wf_dispatch(memory,domain,operation,operands,kwargs)
        if domain=='storage' and operation=='load' and _wf_memory(result):
            loaded=_wf_event(result,'storage','load','operation',{'status':'validated_load'})
            loaded['status']='completed'
        if event is not None:
            event['status']='completed';event['result']=_wf_pack(result)
            if rec is not None and domain in _ZR_DOMAINS:
                _wf_admit(effective,domain,rec,event['id'],kwargs.get('historical',False))
            elif domain in ('rational','complex','symbolic','calculus','roles'):
                outcome='computed'
                if result is None:outcome='blocked'
                elif isinstance(result,tuple) and len(result)==2 and result[0] is None:
                    outcome='blocked_or_limited'
                event['outcome']=outcome
                if outcome!='computed':_wf_state(effective)['feedback'].append({
                    'kind':outcome,'event':event['id'],'domain':domain,'operation':operation,
                    'nexus':'Z0','status':'evidence_retained_no_automatic_rule_change'})
        return result
    except PrimitivePending as exc:
        if event is not None:event.update(status='pending',job=exc.job,reason='primitive_work_budget')
        if capture:_wf_state(effective)['feedback'].append({'kind':'pending_primitive_work','event':event['id'],
            'job':exc.job,'nexus':'Z0','status':'retained_for_continuation'})
        raise
    except Exception as exc:
        if event is not None:event.update(status='failed',reason=str(exc),exception=type(exc).__name__)
        raise
    finally:
        if capture:_WF_STACK.pop();_WF_ACTIVE_MEMORY=prior

def _integrated_discover(memory):return zero_core(memory,'discovery',operation='observe_archive')
def z0_discover_primitive_patterns(memory,**kwargs):return zero_core(memory,'discovery',operation='primitive_patterns',operands=(kwargs,))
def z0_macro_schedule(memory):return zero_core(memory,'scheduler',operation='primitive_macros')
def _ze_integrate(memory):return zero_core(memory,'energy',operation='observe_rational')
def _ze_crosscore_integrate(memory):return zero_core(memory,'energy',operation='observe_cross_domain')
def _zf_observe(memory):return zero_core(memory,'foundations',operation='observe')
def zero_constructor_bootstrap(memory):return zero_core(memory,'constructor',operation='bootstrap')
def z0_open_explore(path,**kwargs):return zero_core(_WF_ACTIVE_MEMORY,'successor',operation='open_explore',operands=(path,kwargs))
def load_memory():return zero_core(None,'storage',operation='load')

def save_memory(memory):
    try:result=zero_core(memory,'storage',operation='save')
    except ZeroRecoveryPending:
        proposal=memory_path()+'.zero-connected-proposal.json'
        _zn_checkpoint(proposal,{k:v for k,v in memory.items() if not k.startswith('_')})
        raise
    state=_wf_state(memory);state['checkpoints']+=1
    _ze_atomic_json(memory_path()+'.zero-connections.json',{
        'source_sha256':_z7_hash_file(memory_path()),'zero_connections':state})
    print('Zero connected workflow:',zero_connections_report(memory))
    return result

_wf_prior_query=query_v45
def query_v45(memory,text):
    if text.strip().lower() in ('connections','zero-connections'):
        print(json.dumps(zero_core(memory,'connected',operation='report'),indent=2))
        return True
    return _wf_prior_query(memory,text)

# Validated expansions are themselves executable roles in the SAME archive.
ZERO_CONNECTED_ROLE_RULE='bind_connected_repeat_operation_v1'

def _wf_derived_body(candidate):
    validation=candidate['validation']
    return {'kind':'derived_operation','operation':'repeat_add','candidate':candidate['id'],
        'term':_pr_copy.deepcopy(candidate['term']),'count':candidate['count'],
        'validation':{'source_id':validation['source_id'],'term_value':validation['term_value'],
            'result':validation['accumulator'],'addition_jobs':list(validation['addition_jobs'])},
        'input':'matching_rational_construction','output':'retained_rational_construction',
        'arithmetic_primitives':['S'],'zero_nexus':'Z0'}

def _wf_derived_role_result(memory,parent_id,body):
    parent=memory['roles_archive']['expressions'][parent_id]
    if parent.get('kind')!='construction' or parent.get('label')!='S0':
        raise ValueError('A derived operation needs the retained S0 construction context')
    slot=parent['depth'];foundation_id=foundation_expression_id(memory,slot)
    if foundation_id is None:raise ValueError('Derived operation has no registered slot backing')
    rid=_pr_bind_roles(memory)['S']['id'];source=body['validation']['source_id']
    label='repeat_add_'+body['candidate'][:12]
    return {'kind':'derived_operation','label':label,'body':_pr_copy.deepcopy(body),'value':label,
        'rule':ZERO_CONNECTED_ROLE_RULE,'parents':[parent_id],
        'sources':[{'archive':'rational','id':foundation_id},{'archive':'roles','id':rid},
                   {'archive':'rational','id':source}],
        'path':parent['path']+[label],'depth':slot+1,'slot':{'counter':slot,'foundation_id':foundation_id}}

def _wf_bind_operation_role(memory,candidate):
    if candidate['status']!='registered':raise ValueError('Unvalidated operation cannot become executable')
    if 'role_id' in candidate:
        record=memory['roles_archive']['expressions'][candidate['role_id']]
        if record.get('body')!=_wf_derived_body(candidate):raise ValueError('Derived operation binding changed')
        return candidate['role_id']
    if not memory.get('zero_constructor_path'):zero_constructor_bootstrap(memory)
    parent=memory['zero_constructor_path']['nodes'][1]['id']
    result,reason=zero_core(memory,'roles',operation='transform',
        operands=(parent,{'connected_operation':candidate['id']}))
    if reason:raise ValueError(reason)
    idx=role_record(memory,result,'transform')
    if idx is None:
        idx=next((r['id'] for r in memory['roles_archive']['expressions']
            if r.get('rule')==ZERO_CONNECTED_ROLE_RULE and r.get('body')==result['body'] and r.get('parents')==[parent]),None)
    if idx is None:raise ValueError('Executable derived operation role was not retained')
    candidate['role_id']=idx
    return idx

_wf_old_role_transition=_role_transition_exact
def _role_transition_exact(memory,source_id,target):
    if not isinstance(target,dict) or set(target)!={'connected_operation'}:
        return _wf_old_role_transition(memory,source_id,target)
    candidate=_wf_state(memory)['candidates'][target['connected_operation']]
    if candidate['status']!='registered':raise ValueError('Connected operation has not passed primitive validation')
    return _wf_derived_role_result(memory,source_id,_wf_derived_body(candidate)),None

_wf_old_role_body_text=role_body_text
def role_body_text(body):
    if body.get('kind')=='derived_operation':return 'repeat_add_'+body['candidate'][:12]
    return _wf_old_role_body_text(body)

def _wf_check_expansion(verifier,plan):
    source=verifier.record('rational',plan['source_id'])
    verifier.get('rational',source['id'])
    proposal=candidate_for(source)
    verifier.require(proposal is not None and proposal['term']==plan['term'] and proposal['count']==plan['count'],
        'derived_operation_pattern_disagreement')
    expected_key=_pr_hashlib.sha256(fingerprint([proposal['term'],proposal['count']]).encode()).hexdigest()
    verifier.require(plan['candidate']==expected_key,'derived_operation_identity_disagreement')
    term=verifier.rational_tree(plan['term'],verifier.legacy_leaves.get(source['id'],set()))
    verifier.require(str(term)==plan['term_value'] and len(plan['addition_jobs'])==plan['count'],
        'derived_operation_term_disagreement')
    acc=Fraction(0)
    for key in plan['addition_jobs']:
        job=verifier.m['primitive_reduction']['jobs'][key];primitive_validate(job)
        verifier.require(job['status']=='complete' and job['program']=='qadd' and job['primitives']==['S'] and
            job['inputs']==[acc.numerator,acc.denominator,term.numerator,term.denominator],
            'derived_operation_primitive_evidence_disagreement')
        binding=job['operation_roles']['S']
        verifier.require(binding['archive']=='roles' and verifier.get('roles',binding['id'])==
            {'kind':'operation','primitive':'S','input':'natural_counter','output':'natural_counter','nexus':'Z0'},
            'derived_operation_S_role_disagreement')
        acc=Fraction(*job['result'])
    verifier.require(str(acc)==plan['result'] and source['value']==plan['result'],
        'derived_operation_result_disagreement')
    return acc

_wf_old_role_replay=_Z5Replay.roles
def _wf_replay_derived_role(self,rec,parents,sources):
    if rec.get('rule')!=ZERO_CONNECTED_ROLE_RULE:return _wf_old_role_replay(self,rec,parents,sources)
    self.require(len(parents)==1 and rec['kind']=='derived_operation' and rec['operation']=='transform',
        'invalid_derived_operation_role')
    body=rec['body'];parent=self.record('roles',rec['parents'][0]);slot=parent['depth']
    self.require(parent.get('label')=='S0' and parent.get('kind')=='construction' and
        rec['depth']==slot+1 and rec['slot']['counter']==slot and len(sources)==3 and sources[0]==slot,
        'invalid_derived_operation_role_context')
    self.require(body['kind']=='derived_operation' and body['operation']=='repeat_add' and
        body['arithmetic_primitives']==['S'] and body['zero_nexus']=='Z0' and
        body['input']=='matching_rational_construction' and body['output']=='retained_rational_construction',
        'invalid_derived_operation_signature')
    validation=body['validation']
    plan={**validation,'candidate':body['candidate'],'term':body['term'],'count':body['count']}
    _wf_check_expansion(self,plan)
    self.require(rec['sources']==[{'archive':'rational','id':rec['slot']['foundation_id']},
        {'archive':'roles','id':rec['sources'][1]['id']},{'archive':'rational','id':validation['source_id']}],
        'invalid_derived_operation_sources')
    self.require(self.record('rational',rec['slot']['foundation_id'])['pathway']=='foundation_state_count_v3' and
        sources[1]=={'kind':'operation','primitive':'S','input':'natural_counter','output':'natural_counter','nexus':'Z0'},
        'invalid_derived_operation_slot_or_primitive')
    label='repeat_add_'+body['candidate'][:12]
    self.require(rec['label']==label and rec['value']==label and rec['path']==parent['path']+[label] and
        rec['expr']==' -> '.join(rec['path']),'derived_operation_role_label_disagreement')
    return body
_Z5Replay.roles=_wf_replay_derived_role

_wf_old_role_recipe=_z6_recipe
def _z6_recipe(domain,rec):
    result=_wf_old_role_recipe(domain,rec)
    if domain=='roles' and rec.get('rule')==ZERO_CONNECTED_ROLE_RULE:
        result['connected_body']=_pr_copy.deepcopy(rec['body'])
    return result

_wf_old_role_build=_z6_build
def _z6_build(memory,domain,idx,recipe):
    if domain!='roles' or not isinstance(recipe,dict) or recipe.get('rule')!=ZERO_CONNECTED_ROLE_RULE:
        return _wf_old_role_build(memory,domain,idx,recipe)
    try:
        if recipe['operation']!='transform' or len(recipe['parents'])!=1:return None
        rec=_wf_derived_role_result(memory,recipe['parents'][0],recipe['connected_body'])
        if rec['sources']!=recipe['sources']:return None
        rec.update(id=idx,expr=' -> '.join(rec['path']),operation='transform',
            pathway=recipe['pathway'],formal_rule=recipe['pathway'])
        probe=dict(memory);probe['roles_archive']=dict(memory['roles_archive'])
        probe['roles_archive']['expressions']=list(memory['roles_archive']['expressions'])
        probe['roles_archive']['expressions'][idx]=rec
        _Z5Replay(probe).get('roles',idx)
        return rec
    except (ValueError,KeyError,TypeError,IndexError):return None

# ============================================================
# V4.9.7 — STRICT RETAINED SLOT / FORMAL i COMPOSITION EXPERIMENT
# Uses the earlier slot schema: retained parent, depth, counter, foundation_id,
# typed sources and a path from zero. No four-cycle or opposite map is assumed.
# i adds one formal role layer. Until an interaction rule is established, i^2
# is an unevaluated slot construction, NOT a supplied complex number or -1.
# ============================================================
SLOT_RULE='zero_retained_slot_experiment_v497'
SLOT_DOMAINS=('rational','complex','symbolic','calculus','roles')
SLOT_WORK=64
SLOT_MAX_DEPTH=8
SLOT_MAX_UNITS=16
_SLOT_PRIOR_CORE=zero_core


def _slot_rows(m,domain):
    return m['expressions'] if domain=='rational' else m[domain+'_archive']['expressions']


def _slot_ref(domain,idx):return {'archive':domain,'id':idx}


def _slot_S(m,value):return zero_core(m,'rational',operation='S',operands=(value,))


def _slot_declarations():
    return {'numeric_primitive':'natural-counter S','structural_rules':['retain source','copy payload','concatenate units',
        'append an i-role layer','compose role paths','typed slot reference'],
        'slot_backing':'each slot counter references its retained S-built natural foundation record',
        'imaginary_role':'formal i label and retained placement; complex multiplication law is not supplied',
        'excluded':['subtraction','signed-number codec','negative seeds','four-turn cycle','opposite cancellation',
                    'SymPy construction','built-in complex arithmetic'],
        'scope':'formal role constructions; no claim that i*i=-1 follows from slot position alone'}


def _slot_record(m,domain,record):
    rows=_slot_rows(m,domain);rec=_pr_copy.deepcopy(record);rec['id']=len(rows)
    for p in rec.get('parents',[]):
        if type(p) is not int or not 0<=p<len(rows):raise ValueError('Missing retained parent')
    for source in rec.get('sources',[]):
        if not 0<=source['id']<len(_slot_rows(m,source['archive'])):raise ValueError('Missing typed source')
    rec['zero_core_passage']={'rule':SLOT_RULE,'zero_nexus':'Z0','archive':domain,'id':rec['id']}
    rows.append(rec);m['recipes'][domain].append(_pr_copy.deepcopy(rec))
    if domain=='complex':zero_core(m,'connected',operation='feedback',operands=(rec['id'],))
    return rec['id']


def _slot_ensure_counter(m,value):
    if type(value) is not int or value<0:raise ValueError('Slot counters must be natural')
    rows=m['expressions']
    while len(rows)<=value:
        parent=rows[-1];result=_slot_S(m,parent['value']);event=m['events'][-1]['id']
        zero_core(m,'rational',operation='record',record={'operation':'S','parents':[parent['id']],
            'sources':[_slot_ref('roles',1)],'value':result,'successor_event':event})
        m['foundation']['states'].append(result)
        m['foundation']['zero_records'].append({'id':'Z'+str(result),'counter':result,'nexus':'Z0'})
    return value


def _slot_apply_i(m,word):
    # Slot positions retain the number of composed role layers. There is no
    # wrap at a resource limit, no sign codec, and no imported complex value.
    result=[];proof=[]
    for token in word:
        value=_slot_S(m,token);proof.append(m['events'][-1]['id'])
        _slot_ensure_counter(m,value);result.append(value)
    return {'word':sorted(result),'successor_events':proof}


def _slot_product(m,a,b):
    accumulator=[];expansion=[];repetition=0
    for layers in b:
        term=list(a);cursor=0;turns=[]
        while cursor<layers:
            step=zero_core(m,'roles',operation='execute_i',operands=(term,));term=step['word'];turns.append(step)
            cursor=_slot_S(m,cursor)
        accumulator=zero_core(m,'complex',operation='join',operands=(accumulator,term))
        repetition=_slot_S(m,repetition)
        expansion.append({'layers':layers,'turns':turns,'term':term,'accumulator':list(accumulator),'counter':repetition})
    return {'word':accumulator,'expansion':expansion}


def _slot_queue(m,operation,parents):
    key=json.dumps([operation,parents],separators=(',',':'))
    if key in m['scheduled']:return
    m['scheduled'].append(key);m['queue'].append({'key':key,'operation':operation,'parents':list(parents),'status':'pending'})


def _slot_feedback(m,idx):
    rec=_slot_rows(m,'complex')[idx]
    if rec['depth']<SLOT_MAX_DEPTH:
        _slot_queue(m,'i',[idx])
        for peer in _slot_rows(m,'complex')[:3]:
            _slot_queue(m,'add',[idx,peer['id']]);_slot_queue(m,'multiply',[idx,peer['id']])
    # Compare all ancestors of an actual role-composition chain. There is no
    # preferred second/fourth slot and no desired negative value in scheduling.
    ancestor=rec
    while ancestor['operation']=='i':
        ancestor=_slot_rows(m,'complex')[ancestor['parents'][0]]
        _slot_queue(m,'relate',[ancestor['id'],idx])
    m['feedback'].append({'source':_slot_ref('complex',idx),'targets':['roles','addition','repeated_addition','path_relations'],
                          'zero_nexus':'Z0'})
    zero_core(m,'discovery',operation='observe',operands=(idx,))


def _slot_observe(m,idx):
    rec=_slot_rows(m,'complex')[idx]
    if rec['operation']=='add' and all(_slot_rows(m,'complex')[p]['word'] for p in rec['parents']):
        evidence={'construction':idx,'parents':list(rec['parents']),'result_units':len(rec['word']),
            'status':'nonempty_sum_retained','zero_nexus':'Z0'}
        m['interaction_evidence'].append(evidence)
    if rec['operation']=='multiply':
        key=json.dumps(rec['parents'])
        if key not in m['derived_operations']:
            # This operation is a concrete expansion with an actual role body,
            # sources and slot backing. It is not general multiplication novelty.
            slot=_slot_ensure_counter(m,1)
            role={'kind':'derived_operation','label':'repeat_path_'+str(idx),
                'operation':'bind_repeated_composition','rule':'observed_repeated_role_addition',
                'parents':[2],'sources':[_slot_ref('rational',slot),_slot_ref('complex',idx)],
                'body':{'operation':'replay_concrete_product','source':idx,'inputs':list(rec['parents'])},
                'path':['0','S0','repeat_path_'+str(idx)],'depth':2,
                'slot':{'counter':slot,'foundation_id':slot}}
            rid=zero_core(m,'roles',operation='record',record=role)
            m['derived_operations'][key]=rid;_slot_queue(m,'execute_role',[rid])


def _slot_dispatch(m,domain,operation,operands,kwargs):
    if operation=='record':return _slot_record(m,domain,kwargs['record'])
    if domain=='rational' and operation=='S':
        n=operands[0]
        if type(n) is not int or n<0:raise ValueError('Natural-counter S only')
        return n+1
    if domain=='roles' and operation=='execute_i':return _slot_apply_i(m,operands[0])
    if domain=='complex' and operation=='join':return sorted(list(operands[0])+list(operands[1]))
    if domain=='complex' and operation=='product':return _slot_product(m,*operands)
    if domain=='connected' and operation=='feedback':return _slot_feedback(m,*operands)
    if domain=='discovery' and operation=='observe':return _slot_observe(m,*operands)
    if domain=='validation' and operation=='archive':return _slot_replay(m)
    if domain=='roles' and operation=='execute_derived':
        rid=operands[0];role=_slot_rows(m,'roles')[rid]
        if role.get('rule')!='observed_repeated_role_addition':raise ValueError('Not an executable derived role')
        zero_core(m,'validation',operation='archive')
        a,b=(_slot_rows(m,'complex')[i]['word'] for i in role['body']['inputs'])
        return _slot_product(m,a,b)
    raise ValueError('No supplied implementation in strict slot branch: '+domain+':'+str(operation))


def zero_core(memory,domain,*,operation=None,operands=(),**kwargs):
    if not isinstance(memory,dict) or memory.get('experiment')!=SLOT_RULE:
        return _SLOT_PRIOR_CORE(memory,domain,operation=operation,operands=operands,**kwargs)
    event={'id':len(memory['events']),'domain':domain,'operation':operation,'zero_nexus':'Z0',
           'parent':memory.get('_active_event'),'status':'running'}
    if operation=='S':event['before']=operands[0]
    memory['events'].append(event);prior=memory.get('_active_event');memory['_active_event']=event['id']
    try:
        result=_slot_dispatch(memory,domain,operation,operands,kwargs);event['status']='complete'
        if operation=='S':event['after']=result
        return result
    except Exception as exc:
        event.update(status='blocked',reason=str(exc));raise
    finally:
        if prior is None:memory.pop('_active_event',None)
        else:memory['_active_event']=prior


def _slot_new():
    m={'schema':1,'experiment':SLOT_RULE,'version':'4.9.7','foundation':{'states':[0],
        'zero_records':[{'id':'Z0','counter':0,'nexus':'Z0'}]},'expressions':[],
        'queue':[],'queue_head':0,'scheduled':[],'lane_heads':{},'lane_cursor':0,
        'runs':[],'events':[],'recipes':{d:[] for d in SLOT_DOMAINS},'feedback':[],
        'interaction_evidence':[],'derived_operations':{},'declared_rules':_slot_declarations(),
        'deferred':['signed interpretation','rational division','roots and general symbolic algebra','calculus','physical identities']}
    for d in SLOT_DOMAINS:
        if d!='rational':m[d+'_archive']={'expressions':[]}
    record=lambda d,r:zero_core(m,d,operation='record',record=r)
    record('rational',{'operation':'zero','parents':[],'sources':[],'value':0})
    record('roles',{'kind':'numeric','label':'0','operation':'origin','rule':'reference_foundation_zero',
        'body':{'kind':'numeric','value':'0'},'parents':[],'sources':[_slot_ref('rational',0)],'depth':0,'path':['0']})
    record('roles',{'kind':'operation','label':'S','operation':'transform','rule':'bind_successor_operation_role',
        'body':{'kind':'operation','primitive':'S','input':'natural_counter','output':'natural_counter','nexus':'Z0'},
        'parents':[0],'sources':[_slot_ref('rational',0)],'depth':1,'path':['0','S'],'slot':{'counter':0,'foundation_id':0}})
    record('roles',{'kind':'construction','label':'S0','operation':'transform','rule':'retain_zero_successor_context_v495',
        'body':_ctx_body(0,'context',1),'parents':[0],'sources':[_slot_ref('rational',0),_slot_ref('roles',1)],
        'depth':1,'path':['0','S0'],'slot':{'counter':0,'foundation_id':0}})
    _slot_ensure_counter(m,1)
    record('roles',{'kind':'construction','label':'S1i','operation':'transform','rule':'extend_counter_in_selected_role_v495',
        'body':_ctx_body(1,'imaginary',1),'parents':[2],'sources':[_slot_ref('rational',1),_slot_ref('roles',1)],
        'depth':2,'path':['0','S0','S1i'],'slot':{'counter':1,'foundation_id':1}})
    record('roles',{'kind':'operation','label':'i-compose','operation':'transform','rule':'compose_retained_i_role',
        'body':{'operation':'append_i_layer','source_role':3,'arithmetic_primitive':'S','closure_rule':None},
        'parents':[2],'sources':[_slot_ref('rational',1),_slot_ref('roles',3)],'depth':2,
        'path':['0','S0','i-compose'],'slot':{'counter':1,'foundation_id':1}})
    record('complex',{'operation':'zero','parents':[],'sources':[_slot_ref('rational',0)],'word':[],'depth':0,'expr':'Z0'})
    record('complex',{'operation':'unit','parents':[],'sources':[_slot_ref('rational',1)],'word':[0],'depth':0,'expr':'S(0)'})
    record('complex',{'operation':'role_embedding','parents':[],'sources':[_slot_ref('roles',3)],'word':[1],'depth':0,'expr':'S1i'})
    return m


def _slot_task(m,task):
    if task['operation']=='execute_pathway':
        return zero_core(m,'pathways',operation='execute',operands=tuple(task['parents']))['status']
    op=task['operation'];parents=task['parents'];records=_slot_rows(m,'complex');sources=[];proof={}
    if op=='execute_role':
        rid=parents[0];role=_slot_rows(m,'roles')[rid];parents=list(role['body']['inputs'])
        result=zero_core(m,'roles',operation='execute_derived',operands=(rid,));word=result['word']
        proof={'expansion':result['expansion']};sources=[_slot_ref('roles',rid)]
    else:
        rows=[records[i] for i in parents]
        if op=='i':
            result=zero_core(m,'roles',operation='execute_i',operands=(rows[0]['word'],))
            word=result['word'];proof={'successor_events':result['successor_events']};sources=[_slot_ref('roles',4)]
        elif op in ('add','relate'):
            op='add'
            if len(rows[0]['word'])+len(rows[1]['word'])>SLOT_MAX_UNITS:return 'size_deferred'
            word=zero_core(m,'complex',operation='join',operands=(rows[0]['word'],rows[1]['word']))
        elif op=='multiply':
            if len(rows[0]['word'])*len(rows[1]['word'])>SLOT_MAX_UNITS:return 'size_deferred'
            result=zero_core(m,'complex',operation='product',operands=(rows[0]['word'],rows[1]['word']))
            word=result['word'];proof={'expansion':result['expansion']}
        else:raise ValueError('Unknown slot task')
    depth=_slot_S(m,max(records[i]['depth'] for i in parents))
    if depth>SLOT_MAX_DEPTH:return 'depth_deferred'
    magnitudes={};magnitude_events={}
    for layer in sorted(set(word)):
        count=0;evidence=[]
        for token in word:
            if token==layer:count=_slot_S(m,count);evidence.append(m['events'][-1]['id'])
        magnitudes[str(layer)]=count;magnitude_events[str(layer)]=evidence
    rec={'operation':op,'parents':list(parents),'sources':sources,'word':word,'depth':depth,
         'expr':op+'('+','.join(map(str,parents))+')','magnitudes':magnitudes,'magnitude_events':magnitude_events,**proof}
    zero_core(m,'complex',operation='record',record=rec)
    return 'complete'


def _slot_replay(m):
    # Independent arithmetic checker: validation does not construct explorer
    # values. It checks the retained formal words and every linked S event.
    def require(ok,message):
        if not ok:raise ValueError('Strict slot replay: '+message)
    require(m['declared_rules']==_slot_declarations(),'changed declared rules')
    def S_evidence(idx,before,after):
        e=m['events'][idx]
        require(e['domain']=='rational' and e['operation']=='S' and e['status']=='complete' and
            e['before']==before and e['after']==after and after==before+1,'S evidence mismatch')
    for idx,e in enumerate(m['events']):
        require(e['id']==idx and e['zero_nexus']=='Z0','event identity')
        if e['domain']=='rational':require(e['operation'] in ('S','record'),'forbidden arithmetic')
        if e['operation']=='S' and e['status']=='complete':
            require(type(e['before']) is int and e['before']>=0 and e['after']==e['before']+1,'non-natural S')
    natural=m['expressions'];roles=_slot_rows(m,'roles');complex_rows=_slot_rows(m,'complex')
    require(m['foundation']['states']==list(range(len(natural))),'slot counter order')
    require(m['foundation']['zero_records']==[{'id':'Z'+str(i),'counter':i,'nexus':'Z0'} for i in range(len(natural))],'zero retention')
    for idx,r in enumerate(natural):
        require(r['id']==idx and r['value']==idx,'natural backing')
        if idx==0:require(r['operation']=='zero' and not r['parents'] and not r['sources'],'zero root')
        else:
            require(r['operation']=='S' and r['parents']==[idx-1] and r['sources']==[_slot_ref('roles',1)],'counter provenance')
            S_evidence(r['successor_event'],idx-1,idx)
    require(len(roles)>=5,'missing constructor roles')
    for idx,r in enumerate(roles):
        require(r['id']==idx,'role identity')
        for p in r['parents']:require(type(p) is int and 0<=p<idx,'role parent order')
        if idx:
            parent=roles[r['parents'][0]];counter=parent['depth']
            require(r['slot']=={'counter':counter,'foundation_id':counter} and counter<len(natural) and
                _slot_ref('rational',counter) in r['sources'],'slot is not backed by retained counter')
            require(r['depth']==counter+1 and r['path']==parent['path']+[r['label']],'role path')
        if idx==0:require(r['body']=={'kind':'numeric','value':'0'} and r['sources']==[_slot_ref('rational',0)],'role origin')
        elif idx==1:require(r['body']=={'kind':'operation','primitive':'S','input':'natural_counter','output':'natural_counter','nexus':'Z0'},'S binding')
        elif idx in (2,3):require(r['body']==_ctx_body(0,'context',1) if idx==2 else r['body']==_ctx_body(1,'imaginary',1),'constructor payload')
        elif idx==4:require(r['body']=={'operation':'append_i_layer','source_role':3,'arithmetic_primitive':'S','closure_rule':None},'hidden closure rule')
        elif r.get('rule')=='zero_physical_quantity_roles_v1':
            _qty_role_check(m,r)
        elif r.get('rule')=='retain_answer_in_new_slot_v1':
            _six_role_check(m,r)
        elif r.get('rule')=='declared_complex_i_action_v497':
            _i_law_check(m,r)
        elif r.get('rule')=='Zi_retained_expression_stage_v1':
            _z1_role_check(m,r)
        elif r.get('rule') in ('retained_unary_pathway_role_v1','retained_pathway_execution_v1'):
            _path_role_check(m,r)
        elif r.get('rule')=='Zi_observed_slot_policy_v1':
            _zi_role_check(m,r)
        else:
            require(r['rule']=='observed_repeated_role_addition' and r['body']['operation']=='replay_concrete_product','unvalidated operation role')
            source=complex_rows[r['body']['source']]
            require(source['operation']=='multiply' and source['parents']==r['body']['inputs'] and
                r['sources']==[_slot_ref('rational',1),_slot_ref('complex',source['id'])],'derived role evidence')
    for idx,r in enumerate(complex_rows):
        require(r['id']==idx and isinstance(r['word'],list) and all(type(t) is int and 0<=t<len(natural) for t in r['word']),'formal slot word')
        ps=r['parents'];require(all(type(p) is int and 0<=p<idx for p in ps),'word parent order')
        op=r['operation'];words=[complex_rows[p]['word'] for p in ps]
        if op=='answer_feedback_embedding':expected=_six_embedding_check(m,r)
        elif op=='zero':expected=[];require(ps==[] and r['sources']==[_slot_ref('rational',0)],'word zero')
        elif op=='unit':expected=[0];require(ps==[] and r['sources']==[_slot_ref('rational',1)],'unit source')
        elif op=='role_embedding':expected=[1];require(ps==[] and r['sources']==[_slot_ref('roles',3)],'i role source')
        elif op=='i':
            require(len(words)==1 and r['sources']==[_slot_ref('roles',4)],'i operation signature')
            expected=sorted(t+1 for t in words[0]);require(len(r['successor_events'])==len(words[0]),'missing role S proof')
            for t,event in zip(words[0],r['successor_events']):S_evidence(event,t,t+1)
        elif op=='add':
            require(len(words)==2 and not r['sources'],'addition signature');expected=sorted(words[0]+words[1])
        elif op in ('multiply','execute_role'):
            require(len(words)==2,'product signature');expected=sorted(a+b for a in words[0] for b in words[1])
            if op=='execute_role':
                require(len(r['sources'])==1 and r['sources'][0]['archive']=='roles','execution binding')
                binding=roles[r['sources'][0]['id']]
                require(binding['rule']=='observed_repeated_role_addition' and binding['body']['inputs']==ps,'wrong executable role')
            else:require(not r['sources'],'product sources')
            require(len(r['expansion'])==len(words[1]),'product expansion length')
            acc=[]
            for counter,(layers,step) in enumerate(zip(words[1],r['expansion']),1):
                term=list(words[0]);require(step['layers']==layers and len(step['turns'])==layers,'role expansion')
                for turn in step['turns']:
                    require(turn['word']==sorted(t+1 for t in term) and len(turn['successor_events'])==len(term),'expanded i step')
                    for t,event in zip(term,turn['successor_events']):S_evidence(event,t,t+1)
                    term=turn['word']
                acc=sorted(acc+term)
                require(step['term']==term and step['accumulator']==acc and step['counter']==counter,'repeated addition proof')
        else:raise ValueError('Strict slot replay: unknown construction operation')
        require(r['word']==expected,'formal value mismatch')
        if ps:
            require(r['depth']==1+max(complex_rows[p]['depth'] for p in ps),'construction depth')
            expected_counts={str(t):r['word'].count(t) for t in set(r['word'])}
            require(r['magnitudes']==expected_counts,'magnitude mismatch')
            for layer,count in expected_counts.items():
                evidence=r['magnitude_events'][layer];require(len(evidence)==count,'magnitude evidence missing')
                for before,event in enumerate(evidence):S_evidence(event,before,before+1)
    for domain in SLOT_DOMAINS:
        rows=_slot_rows(m,domain)
        if domain=='symbolic':
            for row in rows:_sym_check(m,row)
        if domain=='calculus':
            for row in rows:_zstruct_calculus_check(m,row)
        require(rows==m['recipes'][domain],'construction recipe disagreement')
        for r in rows:
            require(r['zero_core_passage']=={'rule':SLOT_RULE,'zero_nexus':'Z0','archive':domain,'id':r['id']},'zero passage')
            for source in r.get('sources',[]):
                require(source['archive'] in SLOT_DOMAINS and type(source['id']) is int and 0<=source['id']<len(_slot_rows(m,source['archive'])),'typed dependency')
    return {'status':'PASS','records':{d:len(_slot_rows(m,d)) for d in SLOT_DOMAINS},'numeric_primitive':['S']}


def _slot_report(m):
    counts={}
    for e in m['events']:
        key=e['domain']+':'+str(e['operation']);counts[key]=counts.get(key,0)+1
    return {'rule':SLOT_RULE,'numeric_primitives':['S'],'records':{d:len(_slot_rows(m,d)) for d in SLOT_DOMAINS},
        'retained_slots':len(m['expressions']),'derived_operation_roles':len(m['derived_operations']),
        'pending_tasks':len(m['queue'])-m['queue_head'],'handler_calls':counts,
        'negative_values_constructed':0,'closure_rules_supplied':0,'subtraction_calls':counts.get('rational:-',0),
        'blocker':'Current slot rules retain and compose roles but provide no additive cancellation or equivalent return-to-zero interaction.',
        'invariant':'Joining nonempty unit words stays nonempty; no length of these forward compositions creates an additive inverse.',
        'deferred':m['deferred'],'whole_engine_reduced':False,
        'scope':'Strict slot branch. The earlier general engine remains in the source but its supplied arithmetic workers are inactive.'}


def _slot_display(word):
    if not word:return '0'
    parts=[]
    for layer in sorted(set(word)):
        n=word.count(layer);term='1' if layer==0 else 'i' if layer==1 else 'i^'+str(layer)
        parts.append(str(n) if layer==0 else ('' if n==1 else str(n)+'·')+term)
    return '+'.join(parts)


def _slot_next(m):
    lanes=('i','relate','add','multiply','execute_role','execute_pathway')
    for unused in lanes:
        kind=lanes[m['lane_cursor']];m['lane_cursor']=(m['lane_cursor']+1)%len(lanes)
        cursor=m['lane_heads'].get(kind,0)
        while cursor<len(m['queue']):
            task=m['queue'][cursor];cursor+=1
            if task['operation']==kind and task['status']=='pending':m['lane_heads'][kind]=cursor;return task
        m['lane_heads'][kind]=cursor
    return None


def _slot_load(path):
    if not os.path.exists(path):return _slot_new()
    with open(path,encoding='utf-8') as handle:m=json.load(handle)
    if m.get('experiment')!=SLOT_RULE:raise ValueError('A separate fresh slot-experiment memory is required')
    candidate=_pr_copy.deepcopy(m);damaged=_zstruct_recover_extensions(candidate)
    for domain in SLOT_DOMAINS:
        rows=_slot_rows(candidate,domain);recipes=candidate['recipes'][domain];by_id={r['id']:r for r in rows}
        if len(by_id)!=len(rows):raise ValueError('Duplicate IDs; source preserved')
        restored=[]
        for recipe in recipes:
            current=by_id.get(recipe['id'])
            if current is not None and current!=recipe:raise ValueError('Record/recipe conflict; source preserved')
            restored.append(_pr_copy.deepcopy(recipe) if current is None else current);damaged=damaged or current is None
        if len(by_id)>len(recipes):raise ValueError('Untracked record; source preserved')
        rows[:]=restored
    zero_core(candidate,'validation',operation='archive')
    if damaged:
        target=path+'.slot-recovery-candidate.json';_ze_atomic_json(target,candidate)
        raise ValueError('Restored missing slot construction in separate candidate: '+target)
    return candidate


def _slot_save(m,path):
    zero_core(m,'validation',operation='archive');_ze_atomic_json(path,{k:v for k,v in m.items() if not k.startswith('_')})


def _slot_query(m,text):
    command=text.strip().lower()
    if command in ('construction','construct','constructor'):
        print('Retained path: Z0 -> S0 -> S1i | roles:',[0,2,3]);return
    if command in ('rules','assumptions'):print(json.dumps(m['declared_rules'],indent=2));return
    if command in ('connections','operations','totals','primitives'):print(json.dumps(_slot_report(m),indent=2));return
    if command in ('zero-core','integrity'):print(zero_core(m,'validation',operation='archive'));return
    if command=='slots':
        for r in m['expressions']:print('slot',r['value'],'| foundation_id:',r['id'],'|',r['operation'],'| parents:',r['parents'])
        return
    if command in ('time','temporal','zero-clock'):print('Zero event count:',len(m['events']),'| clocks:',m['runs'][-1] if m['runs'] else {});return
    if command=='roles-index':
        for r in _slot_rows(m,'roles'):print('roles:'+str(r['id']),' -> '.join(r['path']),'| slot:',r.get('slot'),'|',r['rule'])
        return
    if command.startswith('roles '):
        try:print(json.dumps(_slot_rows(m,'roles')[int(command.split()[1])],indent=2))
        except (ValueError,IndexError):print('Use roles RECORD_NUMBER')
        return
    if command in ('index','complex-index'):
        groups={}
        for r in _slot_rows(m,'complex'):groups.setdefault(_slot_display(r['word']),[]).append(r['id'])
        for value,ids in groups.items():print(value,'| constructions:',len(ids),'| first:',ids[0])
        return
    if command in ('physics-match','physics-index','energy-index','calculus-index','symbolic-index'):
        print('Deferred in strict slot experiment:',m['deferred']);return
    if command in ('help','?'):
        print('constructor, slots, rules, connections, Zi, Zi-example, Z1i, Z1i-example, i-action-example, answers, feedback, roles-index, roles N, index, integrity, zero-core, zero-clock, VALUE');return
    if command=='-0':command='0'
    if command=='1i':command='i'
    rows=[r for r in _slot_rows(m,'complex') if _slot_display(r['word']).lower()==command]
    print('Value',command,'| retained constructions:',len(rows))
    for r in rows[:20]:print('complex:'+str(r['id']),r['expr'],'|',r['operation'],'| parents:',r['parents'])
    if not rows:print('No matching stored value. Pending constructions continue on the saved frontier; enter help for commands.')


def run_slots(*,interactive=True):
    path,m=_principles_load_for_run()
    zero_core(m,'principles',operation='begin')
    print('ZERO THEOREM V4.11.2 - PRINCIPLED OPEN EXPLORATION')
    print('Memory:',path);print('Natural S counters; explicit archived i-action role. No subtraction, signed codec, negative seed or SymPy construction.')
    print('0 structures remain experimental. Polynomial derivative identities use an explicit exact verifier, not a discovered calculus axiom.')
    clocks={'wall_ns':time.time_ns(),'monotonic_ns':time.monotonic_ns(),'performance_ns':time.perf_counter_ns(),'process_ns':time.process_time_ns(),
        'clock_session':_ZSTRUCT_SESSION,'event_start':len(m['events'])}
    for unused in range(SLOT_WORK):
        task=_slot_next(m)
        if task is None:break
        task['status']=_slot_task(m,task);m['queue_head']=_slot_S(m,m['queue_head'])
    m['runs'].append(clocks)
    zero_core(m,'principles',operation='pair_service',budget=4)
    zero_core(m,'principles',operation='pathway_service',budget=4)
    zero_core(m,'principles',operation='interpretation_service',budget=4)
    zero_core(m,'connected',operation='slot_mixes')
    _i_bootstrap(m)
    zero_core(m,'pathways',operation='observe_archive',budget=16)
    zero_core(m,'connected',operation='Zi_counter_walk')
    zero_core(m,'connected',operation='answer_feedback')
    zero_core(m,'0-structures',operation='service',budget=4)
    zero_core(m,'0-structures',operation='open_service',budget=12)
    zero_core(m,'symbolic',operation='service',budget=12)
    zero_core(m,'quantities',operation='service',budget=12)
    zero_core(m,'physical',operation='service',budget=4)
    for clock,value in _zstruct_stamps().items():clocks['finished_'+clock]=value
    clocks['event_end']=len(m['events'])
    _slot_save(m,path)
    _opportunity_export(m,path)
    print('Independent slot replay: PASS');print('Connected zero:',json.dumps(_slot_report(m)))
    print('Saved. Re-run continues. Enter help for commands; ENTER exits queries.')
    if interactive:
        try:
            while True:
                try:text=input('\nQuery an archived value (ENTER to exit): ').strip()
                except EOFError:break
                if not text:break
                _slot_query(m,text)
        finally:
            _slot_save(m,path)
    return m


def run():return run_slots()
# ============================================================
# Zi — RETAINED, TYPED SLOT TRANSFORMATIONS THROUGH ZERO
# Zi is a declared structural constructor. Reusable permutation policies are
# registered only after independent validation of distinct retained examples.
# A switched expression has its own construction identity and evaluated value.
# ============================================================
ZI_RULE='Zi_typed_slot_constructor_v1'
ZI_ROLE_RULE='Zi_observed_slot_policy_v1'
ZI_POLICIES=((2,1,0,3),(1,2,3,0),(2,3,0,1),(3,0,1,2))
ZI_FRAME_BUDGET=2


def _zi_state(m):
    return m.setdefault('Zi',{'rule':ZI_RULE,'frames':[],'attempts':[],'attempt_recipes':[],
        'enumeration_cursor':0,'policies':{},'role_executions':[],
        'declaration':'supplied structural slot permutation; no equality of switched values assumed',
        'schema':['value','operation','value','natural power on right slot']})


def _zi_frame(left,operation,right,power):
    return [{'kind':'value','ref':_slot_ref('complex',left)},
            {'kind':'operation','symbol':operation},
            {'kind':'value','ref':_slot_ref('complex',right)},
            {'kind':'power','ref':_slot_ref('rational',power),'binding':'right_slot'}]


def _zi_frame_error(m,frame):
    if not isinstance(frame,list) or len(frame)!=4:return 'Zi expects four retained slots'
    if [s.get('kind') if isinstance(s,dict) else None for s in frame]!=['value','operation','value','power']:
        return 'slot kinds moved: a value/operation reinterpretation rule is required'
    if frame[1]!= {'kind':'operation','symbol':frame[1].get('symbol')} or frame[1]['symbol'] not in ('add','multiply'):
        return 'operation has no strict executable binding'
    for position in (0,2):
        ref=frame[position].get('ref',{})
        if (set(frame[position])!={'kind','ref'} or ref.get('archive')!='complex' or type(ref.get('id')) is not int or
            not 0<=ref['id']<len(_slot_rows(m,'complex'))):return 'value slot has no retained typed source'
    ref=frame[3].get('ref',{})
    if (set(frame[3])!={'kind','ref','binding'} or frame[3]['binding']!='right_slot' or
        ref.get('archive')!='rational' or type(ref.get('id')) is not int or
        not 0<=ref['id']<len(m['expressions'])):return 'power slot lacks its retained natural counter'
    return None


def _zi_permute(frame,permutation):
    if (not isinstance(frame,list) or len(frame)!=4 or len(permutation)!=4 or
        any(type(i) is not int for i in permutation) or sorted(permutation)!=[0,1,2,3]):
        raise ValueError('Zi requires a bijection of its four slot positions')
    return [_pr_copy.deepcopy(frame[i]) for i in permutation]


def _zi_build_arithmetic(m,operation,parents):
    before=len(_slot_rows(m,'complex'))
    status=_slot_task(m,{'operation':operation,'parents':parents})
    if status!='complete' or len(_slot_rows(m,'complex'))!=before+1:
        raise ValueError('Zi expansion deferred by '+status)
    return before


def _zi_evaluate(m,frame):
    error=_zi_frame_error(m,frame)
    if error:raise ValueError(error)
    left=frame[0]['ref']['id'];right=frame[2]['ref']['id'];power=frame[3]['ref']['id']
    count=m['expressions'][power]['value'];cursor=0;accumulator=1;steps=[]
    # The power is a natural repetition counter. Products themselves expand
    # into role composition and repeated addition through the existing gateway.
    while cursor<count:
        accumulator=_zi_build_arithmetic(m,'multiply',[accumulator,right]);steps.append(accumulator)
        cursor=_slot_S(m,cursor)
    result=_zi_build_arithmetic(m,frame[1]['symbol'],[left,accumulator])
    return {'result_id':result,'power_steps':steps,'power_counter':power}


def _zi_check_evaluation(m,frame,proof):
    error=_zi_frame_error(m,frame)
    if error:raise ValueError('Zi replay: '+error)
    records=_slot_rows(m,'complex');left=frame[0]['ref']['id'];right=frame[2]['ref']['id']
    count=m['expressions'][frame[3]['ref']['id']]['value'];accumulator=1
    if proof['power_counter']!=frame[3]['ref']['id'] or len(proof['power_steps'])!=count:
        raise ValueError('Zi replay: power counter disagreement')
    for idx in proof['power_steps']:
        r=records[idx]
        if r['operation']!='multiply' or r['parents']!=[accumulator,right]:raise ValueError('Zi replay: missing power expansion')
        accumulator=idx
    result=records[proof['result_id']]
    if result['operation']!=frame[1]['symbol'] or result['parents']!=[left,accumulator]:
        raise ValueError('Zi replay: expression disagrees with retained arithmetic')
    return result['word']


def _zi_attempt(m,frame,permutation,role_id=None):
    state=_zi_state(m);input_frame=_pr_copy.deepcopy(frame)
    if _zi_frame_error(m,input_frame):raise ValueError('Zi input needs an executable typed frame')
    output=zero_core(m,'roles',operation='Zi',operands=(input_frame,permutation))
    # Keep a raw rotated frame even when it has no numerical interpretation.
    attempt={'id':len(state['attempts']),'execution_policy':_principles_current(),'input':input_frame,'permutation':list(permutation),
        'output':output,'zero_nexus':'Z0','rule':ZI_RULE,'role_id':role_id}
    error=_zi_frame_error(m,output)
    if error:attempt.update(status='needs_role_rule',reason=error)
    else:
        try:
            first=zero_core(m,'Zi',operation='evaluate',operands=(input_frame,))
            second=zero_core(m,'Zi',operation='evaluate',operands=(output,))
        except ValueError as exc:attempt.update(status='resource_deferred',reason=str(exc))
        else:
            attempt.update(status='validated',input_evaluation=first,output_evaluation=second,
                same_formal_value=_slot_rows(m,'complex')[first['result_id']]['word']==_slot_rows(m,'complex')[second['result_id']]['word'])
    state['attempts'].append(attempt);state['attempt_recipes'].append(_pr_copy.deepcopy(attempt))
    m['feedback'].append({'source':{'constructor':'Zi','id':attempt['id']},
        'targets':['typed_role_observer','Zi_policy_registry','retained_arithmetic_frontier'],
        'zero_nexus':'Z0','status':attempt['status']})
    return attempt


def _zi_register(m):
    state=_zi_state(m);groups={}
    for a in state['attempts']:
        if a['status']=='validated' and a['role_id'] is None:
            groups.setdefault(json.dumps(a['permutation']),[]).append(a)
    for key,attempts in groups.items():
        if key in state['policies']:continue
        unique={json.dumps(a['input'],sort_keys=True):a for a in attempts}
        if len(unique)<2:continue
        evidence=[a['id'] for a in list(unique.values())[:2]]
        for idx in evidence:_zi_check_attempt(m,state['attempts'][idx])
        permutation=state['attempts'][evidence[0]]['permutation']
        refs=[_slot_ref('rational',1)]
        for idx in evidence:
            for side in ('input_evaluation','output_evaluation'):
                ref=_slot_ref('complex',state['attempts'][idx][side]['result_id'])
                if ref not in refs:refs.append(ref)
        label='Zi_policy_'+str(len(state['policies']))
        body={'operation':'Zi_permute','permutation':permutation,'evidence':evidence,
            'input_schema':list(state['schema']),'semantic_claim':'new construction; no value equality required'}
        role={'kind':'derived_operation','label':label,'operation':'bind_Zi_policy','rule':ZI_ROLE_RULE,
            'parents':[2],'sources':refs,'body':body,'path':['0','S0',label],'depth':2,
            'slot':{'counter':1,'foundation_id':1}}
        rid=zero_core(m,'roles',operation='record',record=role)
        state['policies'][key]={'role_id':rid,'permutation':permutation,'evidence':evidence,
            'scope':'this typed four-slot grammar; supplied permutation constructor'}


def _zi_check_attempt(m,a):
    if (a['rule']!=ZI_RULE or a['zero_nexus']!='Z0' or
        a['output']!=_zi_permute(a['input'],a['permutation']) or _zi_frame_error(m,a['input'])):
        raise ValueError('Zi replay: slot transformation disagreement')
    error=_zi_frame_error(m,a['output'])
    if a['status']=='validated':
        if error:raise ValueError('Zi replay: untyped frame accepted')
        x=_zi_check_evaluation(m,a['input'],a['input_evaluation'])
        y=_zi_check_evaluation(m,a['output'],a['output_evaluation'])
        if a['same_formal_value']!=(x==y):raise ValueError('Zi replay: false equality annotation')
    elif a['status']=='needs_role_rule':
        if not error:raise ValueError('Zi replay: false type blockage')
    elif a['status']!='resource_deferred':raise ValueError('Zi replay: unknown status')
    if a['role_id'] is not None:
        role=_slot_rows(m,'roles')[a['role_id']]
        if role.get('rule')!=ZI_ROLE_RULE or role['body']['permutation']!=a['permutation']:
            raise ValueError('Zi replay: execution did not use its archived operation role')


def _zi_role_check(m,role):
    state=m.get('Zi',{});body=role['body'];evidence=body.get('evidence',[])
    if (role.get('kind')!='derived_operation' or role['operation']!='bind_Zi_policy' or role['parents']!=[2] or
        body.get('operation')!='Zi_permute' or len(evidence)!=2 or len(set(evidence))!=2 or
        body.get('input_schema')!=state.get('schema') or
        body.get('semantic_claim')!='new construction; no value equality required'):
        raise ValueError('Zi replay: invalid operation role')
    seen=set();refs=[_slot_ref('rational',1)]
    for idx in evidence:
        a=state['attempts'][idx];_zi_check_attempt(m,a)
        if a['status']!='validated' or a['permutation']!=body['permutation'] or a['role_id'] is not None:
            raise ValueError('Zi replay: unsupported policy evidence')
        seen.add(json.dumps(a['input'],sort_keys=True))
        for side in ('input_evaluation','output_evaluation'):
            ref=_slot_ref('complex',a[side]['result_id'])
            if ref not in refs:refs.append(ref)
    if len(seen)!=2 or role['sources']!=refs:raise ValueError('Zi replay: missing distinct typed examples')


def _zi_service(m,budget=ZI_FRAME_BUDGET):
    state=_zi_state(m);_slot_ensure_counter(m,2)
    # Insertion-order enumeration of available small retained values, operators,
    # and natural powers. No negative value or desired equality is a target.
    frames=[_zi_frame(a,operation,b,power) for a in range(min(3,len(_slot_rows(m,'complex'))))
        for b in range(min(3,len(_slot_rows(m,'complex'))))
        for operation in ('add','multiply') for power in range(min(3,len(m['expressions'])))]
    for unused in range(budget):
        if state['enumeration_cursor']>=len(frames):break
        frame=frames[state['enumeration_cursor']];state['frames'].append(_pr_copy.deepcopy(frame))
        for policy in ZI_POLICIES:
            zero_core(m,'Zi',operation='attempt',operands=(frame,policy))
        state['enumeration_cursor']+=1
    zero_core(m,'Zi',operation='register')
    # Exercise learned roles on a later retained frame, with independent input
    # validation. No direct shortcut bypasses the Zi constructor.
    for policy in state['policies'].values():
        rid=policy['role_id']
        if any(x['role_id']==rid for x in state['role_executions']):continue
        if not state['frames']:continue
        attempt=zero_core(m,'roles',operation='execute_Zi',operands=(rid,state['frames'][-1]))
        state['role_executions'].append({'role_id':rid,'attempt_id':attempt['id']})
    return _zi_report(m)


def _zi_report(m):
    s=m.get('Zi',{});attempts=s.get('attempts',[])
    return {'constructor':'Zi','frames':len(s.get('frames',[])),'attempts':len(attempts),
        'validated':sum(a['status']=='validated' for a in attempts),
        'awaiting_role_interpretation':sum(a['status']=='needs_role_rule' for a in attempts),
        'resource_deferred':sum(a['status']=='resource_deferred' for a in attempts),
        'registered_policies':len(s.get('policies',{})),'executed_policy_roles':len(s.get('role_executions',[])),
        'scope':'supplied structural constructor; observed reusable policies; switched expressions retain distinct values'}


_zi_previous_dispatch=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='roles' and operation=='Zi':return _zi_permute(*operands)
    if domain=='connected' and operation=='slot_mixes':return _zi_service(m,**kwargs)
    if domain=='Zi':
        if operation=='attempt':return _zi_attempt(m,*operands)
        if operation=='evaluate':return _zi_evaluate(m,*operands)
        if operation=='register':return _zi_register(m)
        raise ValueError('Unknown Zi operation')
    if domain=='roles' and operation=='execute_Zi':
        rid,frame=operands;role=_slot_rows(m,'roles')[rid]
        if role.get('rule')!=ZI_ROLE_RULE:raise ValueError('Expected an archived Zi operation role')
        zero_core(m,'validation',operation='archive');_zi_role_check(m,role)
        return zero_core(m,'Zi',operation='attempt',operands=(frame,role['body']['permutation'],rid))
    return _zi_previous_dispatch(m,domain,operation,operands,kwargs)


_zi_previous_replay=_slot_replay
def _slot_replay(m):
    result=_zi_previous_replay(m);state=m.get('Zi')
    if state is not None:
        if state.get('rule')!=ZI_RULE or state.get('schema')!=['value','operation','value','natural power on right slot']:
            raise ValueError('Zi replay: changed frame grammar')
        if state['attempts']!=state['attempt_recipes']:raise ValueError('Zi replay: retained attempt recipe disagreement')
        for idx,a in enumerate(state['attempts']):
            if a['id']!=idx:raise ValueError('Zi replay: attempt identity')
            _zi_check_attempt(m,a)
        for key,policy in state['policies'].items():
            if key!=json.dumps(policy['permutation']):raise ValueError('Zi replay: policy identity')
            role=_slot_rows(m,'roles')[policy['role_id']];_zi_role_check(m,role)
            if policy['permutation']!=role['body']['permutation'] or policy['evidence']!=role['body']['evidence']:
                raise ValueError('Zi replay: policy/role disagreement')
        for execution in state['role_executions']:
            a=state['attempts'][execution['attempt_id']]
            if a['role_id']!=execution['role_id']:raise ValueError('Zi replay: policy execution evidence')
    return result


_zi_previous_report=_slot_report
def _slot_report(m):
    report=_zi_previous_report(m);report['Zi']=_zi_report(m);return report


_zi_previous_query=_slot_query
def _slot_query(m,text):
    if text.strip().lower() in ('zi','zi-index'):
        print(json.dumps(_zi_report(m),indent=2));return
    if text.strip().lower()=='zi-example':
        _slot_ensure_counter(m,2)
        frame=_zi_frame(1,'add',2,2)
        attempt=zero_core(m,'Zi',operation='attempt',operands=(frame,ZI_POLICIES[0]))
        _slot_save(m,memory_path())
        if attempt['status']=='validated':
            records=_slot_rows(m,'complex')
            print('Zi: 1 + i^2 -> i + 1^2')
            print('Original:',_slot_display(records[attempt['input_evaluation']['result_id']]['word']))
            print('Switched:',_slot_display(records[attempt['output_evaluation']['result_id']]['word']))
            print('Both constructions retained; equal values:',attempt['same_formal_value'])
        else:print(attempt['status'],attempt.get('reason'))
        return
    return _zi_previous_query(m,text)
# ============================================================
# Zi -> Z1i -> Z2i ... : retained S counters and expression-slot extenders.
# Symbolic powers are valid constructions even when no value rule is available.
# Per-run work is bounded; persistent unresolved branches remain eligible to mix.
# ============================================================
Z1I_RULE='Zi_retained_counter_extenders_v1'
Z1I_ROLE_RULE='Zi_retained_expression_stage_v1'
Z1I_ACTIONS=('expand_i_power','interpret_i','exchange_power_slots','split_counter_zero','append_zero','00404_slots','switch_operation','optional_place','optional_reorder','optional_merge','optional_combine','optional_apply_role')
Z1I_MAX_STAGE=4
Z1I_MAX_NODES=64
Z1I_WORK=5


def _z1_state(m):
    return _zi_state(m).setdefault('walk',{'rule':Z1I_RULE,'nodes':[],'roots':{},'root_cursor':0,
        'queue':[],'scheduled':[],'lane_heads':{},'lane_cursor':0,'completed':0,'feedback':[],
        'structural_cycles':[],'declarations':{
            'second_counter':'Zi stage 0; retained S(0) stage 1 is Z1i; subsequent stages retain their parents',
            'power_switch':'exchange base and exponent as syntax; no value equality assumed',
            'split':'natural n -> a retained zero plus n retained units',
            '00404':'existing positional template 00111101111 supplies copy/zero positions; this is an extender, not an equality',
            'evaluation':'only supported natural powers are evaluated; other powers stay symbolic and continue mixing'}})


def _z1_ref(ref):return {'kind':'reference','ref':_pr_copy.deepcopy(ref)}
def _z1_call(op,a,b):return {'kind':'call','operation':op,'args':[_pr_copy.deepcopy(a),_pr_copy.deepcopy(b)]}


def _z1_from_frame(frame):
    return _z1_call(frame[1]['symbol'],_z1_ref(frame[0]['ref']),
        _z1_call('power',_z1_ref(frame[2]['ref']),_z1_ref(frame[3]['ref'])))


def _z1_walk(tree,path=()):
    yield path,tree
    if tree.get('kind') in ('call','pathway_call'):
        for idx,child in enumerate(tree['args']):yield from _z1_walk(child,path+(idx,))


def _z1_check_tree(m,tree):
    count=0
    for path,node in _z1_walk(tree):
        count+=1
        if node.get('kind')=='reference':
            ref=node.get('ref',{})
            if (set(node)!={'kind','ref'} or set(ref)!={'archive','id'} or ref['archive'] not in ('rational','complex') or
                type(ref['id']) is not int or not 0<=ref['id']<len(_slot_rows(m,ref['archive']))):
                raise ValueError('Z1i replay: invalid retained slot reference')
        elif node.get('kind')=='pathway_call':
            _zstruct_check_path_node(m,node)
        elif (node.get('kind')!='call' or set(node)!={'kind','operation','args'} or
              node['operation'] not in ('add','multiply','power') or not isinstance(node['args'],list) or len(node['args'])!=2):
            raise ValueError('Z1i replay: unsupported expression node')
    if count>Z1I_MAX_NODES:raise ValueError('Z1i expression slot budget')
    return count


def _z1_replace(tree,path,node):
    if not path:return _pr_copy.deepcopy(node)
    result=_pr_copy.deepcopy(tree)
    result['args'][path[0]]=_z1_replace(result['args'][path[0]],path[1:],node)
    return result


def _z1_variants(m,tree,kind):
    result=[]
    if kind in ('append_zero','00404_slots'):return [{'kind':kind,'path':[]}]
    for path,node in _z1_walk(tree):
        if kind=='exchange_power_slots' and node.get('operation')=='power':result.append({'kind':kind,'path':list(path)})
        if kind=='split_counter_zero' and node.get('kind')=='reference' and node['ref']['archive']=='rational':
            value=m['expressions'][node['ref']['id']]['value']
            if 1<value<=SLOT_MAX_UNITS:result.append({'kind':kind,'path':list(path)})
        if kind=='switch_operation' and node.get('kind')=='call':
            for op in ('add','multiply','power'):
                if op!=node['operation']:result.append({'kind':kind,'path':list(path),'operation':op})
    return result


def _z1_at(tree,path):
    for idx in path:tree=tree['args'][idx]
    return tree


def _z1_transform(m,tree,action):
    kind=action['kind'];path=action['path'];node=_z1_at(tree,path);evidence={}
    if kind=='exchange_power_slots':
        if node.get('operation')!='power':raise ValueError('Z1i needs a retained power construction')
        replacement=_z1_call('power',node['args'][1],node['args'][0])
    elif kind=='split_counter_zero':
        if node.get('kind')!='reference' or node['ref']['archive']!='rational':raise ValueError('Z1i can split only retained natural counters')
        value=m['expressions'][node['ref']['id']]['value'];counter=0;steps=[]
        if not 1<value<=SLOT_MAX_UNITS:raise ValueError('Z1i split unit budget')
        replacement=_z1_ref(_slot_ref('rational',0))
        while counter<value:
            replacement=_z1_call('add',replacement,_z1_ref(_slot_ref('rational',1)))
            counter=_slot_S(m,counter);steps.append(m['events'][-1]['id'])
        evidence={'source_counter':node['ref']['id'],'unit_counter_events':steps,'retained_zero':_slot_ref('rational',0)}
    elif kind=='append_zero':
        if path:raise ValueError('Z1i zero extender expects the complete retained construction')
        replacement=_z1_call('add',tree,_z1_ref(_slot_ref('rational',0)))
        evidence={'retained_zero':_slot_ref('rational',0)}
    elif kind=='00404_slots':
        if path:raise ValueError('00404 extender expects the complete retained construction')
        # Reuse the existing digit expansion, preserving a distinct backed slot
        # for every zero or copy. Each copy is a fresh construction occurrence.
        pattern=digit_breakdown('00404');slots=[];counter=0;replacement=_z1_ref(_slot_ref('rational',0))
        for character in pattern:
            counter=_slot_S(m,counter);event=m['events'][-1]['id'];_slot_ensure_counter(m,counter)
            payload=_z1_ref(_slot_ref('rational',0)) if character=='0' else tree
            slots.append({'counter':counter,'foundation_id':counter,'successor_event':event,
                          'kind':'zero' if character=='0' else 'copy','source':'Z0' if character=='0' else 'parent_expression'})
            replacement=_z1_call('add',replacement,payload)
        evidence={'template':'00404','expansion':pattern,'slots':slots,'value_equality_claim':False}
    elif kind=='switch_operation':
        if node.get('kind')!='call' or action.get('operation') not in ('add','multiply','power') or action['operation']==node['operation']:
            raise ValueError('Z1i operation needs an available distinct binding')
        replacement=_z1_call(action['operation'],*node['args'])
    else:raise ValueError('Unknown Z1i mixing action')
    result=_z1_replace(tree,path,replacement);_z1_check_tree(m,result)
    return {'expression':result,'evidence':evidence}


def _z1_eval(m,tree):
    # Construct supported values through the same zero gateway. A symbolic
    # exponent is not read as a natural repetition counter and is not guessed.
    if tree['kind']=='reference':
        ref=tree['ref']
        if ref['archive']=='complex':return {'status':'evaluated_formal','word':list(_slot_rows(m,'complex')[ref['id']]['word'])}
        value=m['expressions'][ref['id']]['value'];word=[];counter=0
        if value>SLOT_MAX_UNITS:return {'status':'resource_deferred','reason':'natural unit budget'}
        while counter<value:word.append(0);counter=_slot_S(m,counter)
        return {'status':'evaluated_formal','word':word}
    left=zero_core(m,'Zi',operation='evaluate_expression',operands=(tree['args'][0],))
    right=zero_core(m,'Zi',operation='evaluate_expression',operands=(tree['args'][1],))
    for result in (left,right):
        if result['status']!='evaluated_formal':return dict(result)
    a,b=left['word'],right['word'];op=tree['operation']
    if op=='add':
        if len(a)+len(b)>SLOT_MAX_UNITS:return {'status':'resource_deferred','reason':'joined unit budget'}
        word=zero_core(m,'complex',operation='join',operands=(a,b))
    elif op=='multiply':
        if len(a)*len(b)>SLOT_MAX_UNITS:return {'status':'resource_deferred','reason':'product unit budget'}
        word=zero_core(m,'complex',operation='product',operands=(a,b))['word']
    else:
        if any(t!=0 for t in b):return {'status':'unresolved','reason':'symbolic exponent has no derived numeric action'}
        count=0
        for unused in b:count=_slot_S(m,count)
        if count>SLOT_MAX_DEPTH:return {'status':'resource_deferred','reason':'natural power budget'}
        word=[0];cursor=0
        while cursor<count:
            if len(word)*len(a)>SLOT_MAX_UNITS:return {'status':'resource_deferred','reason':'power unit budget'}
            word=zero_core(m,'complex',operation='product',operands=(word,a))['word'];cursor=_slot_S(m,cursor)
    return {'status':'evaluated_formal','word':word}


def _z1_expected(m,tree):
    # Independent natural-polynomial oracle for checking, not construction.
    if tree['kind']=='reference':
        ref=tree['ref']
        if ref['archive']=='complex':return {'status':'evaluated_formal','word':list(_slot_rows(m,'complex')[ref['id']]['word'])}
        value=m['expressions'][ref['id']]['value']
        if value>SLOT_MAX_UNITS:return {'status':'resource_deferred','reason':'natural unit budget'}
        return {'status':'evaluated_formal','word':[0]*value}
    left=_z1_expected(m,tree['args'][0]);right=_z1_expected(m,tree['args'][1])
    for result in (left,right):
        if result['status']!='evaluated_formal':return result
    a,b=left['word'],right['word'];op=tree['operation']
    if op=='add':
        if len(a)+len(b)>SLOT_MAX_UNITS:return {'status':'resource_deferred','reason':'joined unit budget'}
        word=sorted(a+b)
    elif op=='multiply':
        if len(a)*len(b)>SLOT_MAX_UNITS:return {'status':'resource_deferred','reason':'product unit budget'}
        word=sorted(x+y for x in a for y in b)
    else:
        if any(t!=0 for t in b):return {'status':'unresolved','reason':'symbolic exponent has no derived numeric action'}
        if len(b)>SLOT_MAX_DEPTH:return {'status':'resource_deferred','reason':'natural power budget'}
        word=[0]
        for unused in b:
            if len(word)*len(a)>SLOT_MAX_UNITS:return {'status':'resource_deferred','reason':'power unit budget'}
            word=sorted(x+y for x in word for y in a)
    return {'status':'evaluated_formal','word':word}


def _z1_sources(tree,slot,stage):
    refs=[_slot_ref('rational',slot)]
    for ref in [_slot_ref('rational',stage)]+[n['ref'] for p,n in _z1_walk(tree) if n['kind'] in ('reference','pathway_call')]:
        if ref not in refs:refs.append(_pr_copy.deepcopy(ref))
    return refs


def _z1_enqueue(m,rid,kind,cursor=0):
    state=_z1_state(m);key=json.dumps([rid,kind,cursor])
    if key not in state['scheduled']:
        state['scheduled'].append(key);state['queue'].append({'source':rid,'kind':kind,'cursor':cursor,'status':'pending'})


def _z1_emit(m,parent,tree,action,evidence,feedback_slot=None):
    _z1_check_tree(m,tree);state=_z1_state(m);roles=_slot_rows(m,'roles');source=roles[parent]
    if action['kind']=='seed_frame':stage=0;event=None
    else:
        stage=_slot_S(m,source['body']['counter']);event=m['events'][-1]['id']
    _slot_ensure_counter(m,stage);slot=_slot_ensure_counter(m,source['depth'])
    label='Zi' if stage==0 else 'Z'+str(stage)+'i'
    evaluation=zero_core(m,'Zi',operation='evaluate_expression',operands=(tree,))
    body={'counter':stage,'successor_event':event,'expression':_pr_copy.deepcopy(tree),
        'action':_pr_copy.deepcopy(action),'evidence':_pr_copy.deepcopy(evidence),'evaluation':evaluation,'zero_nexus':'Z0'}
    body['optional_slots']=_optional_layout_after(m,parent,action,evidence)
    sources=_z1_sources(tree,slot,stage)
    for ref in _optional_sources(body['optional_slots']):
        if ref not in sources:sources.append(ref)
    if feedback_slot is not None:
        body['feedback_slot']=_slot_ref('roles',feedback_slot);sources.append(_slot_ref('roles',feedback_slot))
    if action['kind']=='interpret_i':sources.append(_pr_copy.deepcopy(evidence['answer_slot']['law_source']))
    rec={'kind':'construction','label':label,'operation':'extend_Zi_counter','rule':Z1I_ROLE_RULE,
        'parents':[parent],'sources':sources,'body':body,'path':source['path']+[label],
        'depth':slot+1,'slot':{'counter':slot,'foundation_id':slot}}
    rid=zero_core(m,'roles',operation='record',record=rec);state['nodes'].append(rid)
    for kind in Z1I_ACTIONS:_z1_enqueue(m,rid,kind)
    state['feedback'].append({'source':_slot_ref('roles',rid),'status':evaluation['status'],
        'targets':['Zi_counter_frontier','role_composition','slot_extenders','structural_relation_observer'],'zero_nexus':'Z0'})
    if source.get('rule')==Z1I_ROLE_RULE:
        previous=roles[source['parents'][0]]
        if previous.get('rule')==Z1I_ROLE_RULE and previous['body']['expression']==tree:
            state['structural_cycles'].append({'roles':[previous['id'],parent,rid],
                'rule':'observed_return_to_same_expression_structure','numeric_equality_claim':False})
    return rid


def _z1_seed(m,index):
    state=_z1_state(m);key=str(index)
    if key in state['roots']:return state['roots'][key]
    frame=_zi_state(m)['frames'][index]
    if _zi_frame_error(m,frame):raise ValueError('Z1i seed lacks a valid retained frame')
    rid=_z1_emit(m,2,_z1_from_frame(frame),{'kind':'seed_frame','frame_index':index},{})
    state['roots'][key]=rid;return rid


def _z1_next(m):
    state=_z1_state(m)
    for unused in Z1I_ACTIONS:
        kind=Z1I_ACTIONS[state['lane_cursor']];state['lane_cursor']=(state['lane_cursor']+1)%len(Z1I_ACTIONS)
        cursor=state['lane_heads'].get(kind,0)
        while cursor<len(state['queue']):
            task=state['queue'][cursor];cursor+=1
            if task['kind']==kind and task['status']=='pending':state['lane_heads'][kind]=cursor;return task
        state['lane_heads'][kind]=cursor
    return None


def _z1_service(m,budget=Z1I_WORK):
    state=_z1_state(m);frames=_zi_state(m)['frames']
    if state['root_cursor']<len(frames):
        _z1_seed(m,state['root_cursor']);state['root_cursor']+=1
    for unused in range(budget):
        task=_z1_next(m)
        if task is None:break
        tree=_slot_rows(m,'roles')[task['source']]['body']['expression']
        variants=_z1_variants(m,tree,task['kind'],source=task['source']);cursor=task['cursor']
        if cursor>=len(variants):task['status']='no_applicable_slots'
        else:
            action=variants[cursor]
            try:result=zero_core(m,'Zi',operation='extend_slots',operands=(tree,action))
            except ValueError as exc:
                if str(exc)!='Z1i expression slot budget':raise
                task.update(status='size_deferred',reason=str(exc))
                task['proposal']=zero_core(m,'opportunities',operation='retain_deferred',
                    operands=(task['source'],action,getattr(exc,'retained_proposal',None),str(exc)))
            else:
                rid=_z1_emit(m,task['source'],result['expression'],action,result['evidence'])
                task.update(status='complete',result_role=rid)
            next_cursor=_slot_S(m,cursor)
            if next_cursor<len(variants):_z1_enqueue(m,task['source'],task['kind'],next_cursor)
        state['completed']+=1
    return _z1_report(m)


def _z1_role_check(m,role):
    if (role['kind']!='construction' or role['operation']!='extend_Zi_counter' or len(role['parents'])!=1):
        raise ValueError('Z1i replay: construction signature')
    body=role['body'];parent=_slot_rows(m,'roles')[role['parents'][0]];action=body['action'];tree=body['expression']
    _z1_check_tree(m,tree)
    if action['kind']=='seed_frame':
        frame=_zi_state(m)['frames'][action['frame_index']]
        if role['parents']!=[2] or body['counter']!=0 or body['successor_event'] is not None or tree!=_z1_from_frame(frame) or body['evidence']!={}:
            raise ValueError('Z1i replay: seed origin')
    else:
        if parent.get('rule')!=Z1I_ROLE_RULE:raise ValueError('Z1i replay: parent counter line')
        prior=parent['body']['counter'];event=m['events'][body['successor_event']]
        if (body['counter']!=prior+1 or event['domain']!='rational' or event['operation']!='S' or
            event['status']!='complete' or event['before']!=prior or event['after']!=body['counter']):
            raise ValueError('Z1i replay: second counter S evidence')
        original=parent['body']['expression'];kind=action['kind'];path=action['path'];node=_z1_at(original,path);evidence=body['evidence']
        if kind in OPTIONAL_ACTIONS:
            replacement,expected_evidence=_optional_transition(m,role['parents'][0],action,construct=False)
            if kind=='reserve_optional':expected_evidence['counter_events']=evidence['counter_events']
        elif kind in ('expand_i_power','interpret_i'):
            expected_tree=_i_transition_check(m,parent,action,evidence)
            replacement=_z1_at(expected_tree,path);expected_evidence=evidence
        elif kind=='exchange_power_slots':
            if node.get('operation')!='power':raise ValueError('Z1i replay: expected power slots')
            replacement=_z1_call('power',node['args'][1],node['args'][0]);expected_evidence={}
        elif kind=='split_counter_zero':
            ref=node['ref'];value=m['expressions'][ref['id']]['value']
            if ref['archive']!='rational' or not 1<value<=SLOT_MAX_UNITS:raise ValueError('Z1i replay: split source')
            steps=evidence['unit_counter_events']
            if len(steps)!=value:raise ValueError('Z1i replay: split count')
            replacement=_z1_ref(_slot_ref('rational',0))
            for before,event_id in enumerate(steps):
                e=m['events'][event_id]
                if e['domain']!='rational' or e['operation']!='S' or e['status']!='complete' or e['before']!=before or e['after']!=before+1:
                    raise ValueError('Z1i replay: split S steps')
                replacement=_z1_call('add',replacement,_z1_ref(_slot_ref('rational',1)))
            expected_evidence={'source_counter':ref['id'],'unit_counter_events':steps,'retained_zero':_slot_ref('rational',0)}
        elif kind=='append_zero':
            if path:raise ValueError('Z1i replay: zero placement')
            replacement=_z1_call('add',original,_z1_ref(_slot_ref('rational',0)));expected_evidence={'retained_zero':_slot_ref('rational',0)}
        elif kind=='00404_slots':
            if path or evidence.get('template')!='00404' or evidence.get('expansion')!='00111101111' or evidence.get('value_equality_claim') is not False:
                raise ValueError('Z1i replay: extender template')
            slots=evidence['slots']
            if len(slots)!=11:raise ValueError('Z1i replay: extender slot count')
            replacement=_z1_ref(_slot_ref('rational',0))
            for before,(character,slot) in enumerate(zip('00111101111',slots)):
                counter=before+1;e=m['events'][slot['successor_event']]
                expected={'counter':counter,'foundation_id':counter,'successor_event':slot['successor_event'],
                    'kind':'zero' if character=='0' else 'copy','source':'Z0' if character=='0' else 'parent_expression'}
                if slot!=expected or counter>=len(m['expressions']) or e['domain']!='rational' or e['operation']!='S' or e['status']!='complete' or e['before']!=before or e['after']!=counter:
                    raise ValueError('Z1i replay: unbacked extender slot')
                replacement=_z1_call('add',replacement,_z1_ref(_slot_ref('rational',0)) if character=='0' else original)
            expected_evidence={'template':'00404','expansion':'00111101111','slots':slots,'value_equality_claim':False}
        elif kind=='switch_operation':
            if node.get('kind')!='call' or action.get('operation') not in ('add','multiply','power') or action['operation']==node['operation']:
                raise ValueError('Z1i replay: operation binding')
            replacement=_z1_call(action['operation'],*node['args']);expected_evidence={}
        else:raise ValueError('Z1i replay: unknown transition')
        if tree!=_z1_replace(original,path,replacement) or evidence!=expected_evidence:
            raise ValueError('Z1i replay: slot transition disagreement')
    stage=body['counter'];label='Zi' if stage==0 else 'Z'+str(stage)+'i'
    expected_sources=_z1_sources(tree,role['slot']['counter'],stage)
    expected_layout=_optional_layout_after(m,role['parents'][0],action,body['evidence'])
    if 'optional_slots' in body:
        if body['optional_slots']!=expected_layout:raise ValueError('Optional slot replay: changed retained placement')
        for ref in _optional_sources(expected_layout):
            if ref not in expected_sources:expected_sources.append(ref)
    elif action['kind'] in OPTIONAL_ACTIONS:
        raise ValueError('Optional slot replay: missing placement record')
    if body.get('feedback_slot') is not None:
        ref=body['feedback_slot'];retained=_slot_rows(m,'roles')[ref['id']]
        if (ref['archive']!='roles' or ref['id']>=role['id'] or retained.get('rule')!='retain_answer_in_new_slot_v1' or
            retained['parents']!=role['parents']):raise ValueError('Z1i replay: lost saved feedback source')
        expected_sources.append(ref)
    if action['kind']=='interpret_i':expected_sources.append(_pr_copy.deepcopy(body['evidence']['answer_slot']['law_source']))
    if role['label']!=label or role['sources']!=expected_sources or body['zero_nexus']!='Z0':
        raise ValueError('Z1i replay: retained constructor context')
    if body['evaluation']!=_z1_expected(m,tree):raise ValueError('Z1i replay: invented expression value')


def _z1_report(m):
    state=m.get('Zi',{}).get('walk',{});roles=_slot_rows(m,'roles');counts={}
    for rid in state.get('nodes',[]):
        status=roles[rid]['body']['evaluation']['status'];counts[status]=counts.get(status,0)+1
    return {'constructors':'Zi -> Z1i -> Z2i ...','retained_nodes':len(state.get('nodes',[])),
        'statuses':counts,'pending_mixes':sum(t['status']=='pending' for t in state.get('queue',[])),
        'structural_cycles':len(state.get('structural_cycles',[])),
        'actions':list(Z1I_ACTIONS),'negative_values_derived':0,
        'scope':'retained expression exploration; unresolved powers keep mixing; no supplied negative or complex-power backend'}


def _z1_text(m,tree):
    if tree['kind']=='reference':
        ref=tree['ref']
        return str(m['expressions'][ref['id']]['value']) if ref['archive']=='rational' else _slot_display(_slot_rows(m,'complex')[ref['id']]['word'])
    a,b=(_z1_text(m,c) for c in tree['args']);symbol={'add':'+','multiply':'*','power':'^'}[tree['operation']]
    return '('+a+symbol+b+')'


_z1_previous_dispatch=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='connected' and operation=='Zi_counter_walk':return _z1_service(m,**kwargs)
    if domain=='Zi' and operation=='extend_slots':return _z1_transform(m,*operands)
    if domain=='Zi' and operation=='evaluate_expression':return _z1_eval(m,*operands)
    return _z1_previous_dispatch(m,domain,operation,operands,kwargs)


_z1_previous_replay=_slot_replay
def _slot_replay(m):
    result=_z1_previous_replay(m);state=m.get('Zi',{}).get('walk')
    if state is not None:
        if state.get('rule')!=Z1I_RULE or len(set(state['nodes']))!=len(state['nodes']):raise ValueError('Z1i replay: retained node identities')
        expected_nodes=[r['id'] for r in _slot_rows(m,'roles') if r.get('rule')==Z1I_ROLE_RULE]
        if state['nodes']!=expected_nodes:raise ValueError('Z1i replay: missing retained stage')
        if state['root_cursor']<0 or state['root_cursor']>len(_zi_state(m)['frames']):raise ValueError('Z1i replay: root cursor')
        for rid in state['nodes']:
            r=_slot_rows(m,'roles')[rid]
            if r.get('rule')!=Z1I_ROLE_RULE:raise ValueError('Z1i replay: node type')
        for index,rid in state['roots'].items():
            r=_slot_rows(m,'roles')[rid]
            if rid not in state['nodes'] or r['body']['action']!={'kind':'seed_frame','frame_index':int(index)}:
                raise ValueError('Z1i replay: root source')
        for cycle in state['structural_cycles']:
            a,b,c=(_slot_rows(m,'roles')[rid] for rid in cycle['roles'])
            if (b['parents']!=[a['id']] or c['parents']!=[b['id']] or a['body']['expression']!=c['body']['expression'] or
                cycle['numeric_equality_claim'] is not False):raise ValueError('Z1i replay: false structural cycle')
    return result


_z1_previous_report=_slot_report
def _slot_report(m):
    report=_z1_previous_report(m);report['Z1i']=_z1_report(m);return report


_z1_previous_query=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    if command in ('z1i','zi-walk'):
        print(json.dumps(_z1_report(m),indent=2));return
    if command=='z1i-example':
        _slot_ensure_counter(m,2);frames=_zi_state(m)['frames'];index=len(frames);frames.append(_zi_frame(1,'add',2,2))
        root=_z1_seed(m,index);roles=_slot_rows(m,'roles');tree=roles[root]['body']['expression']
        action={'kind':'exchange_power_slots','path':[1]}
        transformed=zero_core(m,'Zi',operation='extend_slots',operands=(tree,action))
        second=_z1_emit(m,root,transformed['expression'],action,transformed['evidence'])
        tree=roles[second]['body']['expression'];split={'kind':'split_counter_zero','path':[1,0]}
        transformed=zero_core(m,'Zi',operation='extend_slots',operands=(tree,split))
        third=_z1_emit(m,second,transformed['expression'],split,transformed['evidence'])
        for rid in (root,second,third):
            r=roles[rid];print(r['label'],'| roles:'+str(rid),'|',_z1_text(m,r['body']['expression']),'|',r['body']['evaluation'])
        _slot_save(m,memory_path());print('Parents, counters and slot splits retained; unresolved forms remain queued.');return
    return _z1_previous_query(m,text)
# ============================================================
# EXECUTABLE COMPLEX i ROLE + RETAINED FIFTH LOGICAL-ANSWER SLOT
# The complex interaction of i is now an openly declared role law. It is not
# claimed to have been discovered from a label. No subtraction, sign codec,
# negative seed, native complex arithmetic, or SymPy constructs these answers.
# ============================================================
I_ACTION_RULE='declared_complex_i_action_v497'
I_TAGS=('unit','i_unit','opposite_unit','opposite_i_unit')
I_NEXT={'unit':'i_unit','i_unit':'opposite_unit','opposite_unit':'opposite_i_unit','opposite_i_unit':'unit'}
I_OPPOSITE={'unit':'opposite_unit','opposite_unit':'unit','i_unit':'opposite_i_unit','opposite_i_unit':'i_unit'}


def _i_law_body():
    return {'operation':'apply_complex_i','rule':'two applications of i reverse a retained unit role',
        'transitions':dict(I_NEXT),'zero_return':'opposite unit roles cancel in pairs',
        'numeric_primitive':'S','status':'declared_complex_role_law_not_discovered_axiom'}


def _i_law_check(m,role):
    if (role['kind']!='operation' or role['label']!='i-action' or role['operation']!='declare_i_action' or
        role['body']!=_i_law_body() or role['parents']!=[2] or role['sources']!=[_slot_ref('rational',1),_slot_ref('roles',3)]):
        raise ValueError('i-action replay: changed declared role law')


def _i_ensure(m):
    state=_zi_state(m);rid=state.get('i_action_role')
    if rid is not None:
        _i_law_check(m,_slot_rows(m,'roles')[rid]);return rid
    _slot_ensure_counter(m,1)
    role={'kind':'operation','label':'i-action','operation':'declare_i_action','rule':I_ACTION_RULE,
        'parents':[2],'sources':[_slot_ref('rational',1),_slot_ref('roles',3)],'body':_i_law_body(),
        'path':['0','S0','i-action'],'depth':2,'slot':{'counter':1,'foundation_id':1}}
    rid=zero_core(m,'roles',operation='record',record=role);state['i_action_role']=rid;return rid


def _i_display(word):
    parts=[]
    for tag in I_TAGS:
        count=word.count(tag)
        if not count:continue
        if tag=='unit':part=str(count)
        elif tag=='i_unit':part=('' if count==1 else str(count))+'i'
        elif tag=='opposite_unit':part='-'+str(count)
        else:part='-'+('' if count==1 else str(count))+'i'
        parts.append(part)
    return '+'.join(parts).replace('+-','-') if parts else '0'


def _i_answer(m,evaluation):
    law=_i_ensure(m);answer={'slot':5,'kind':'logical_answer','law_source':_slot_ref('roles',law),
        'assumption':'declared complex i action and opposite-role zero return'}
    if evaluation['status']!='evaluated_formal':
        return {**answer,'status':evaluation['status'],'reason':evaluation['reason']}
    if not isinstance(evaluation.get('word'),list) or any(type(d) is not int or d<0 for d in evaluation['word']):
        raise ValueError('i action requires natural role-composition counts')
    retained=[];turns=[];cancellations=[]
    for degree in evaluation['word']:
        tag='unit';counter=0;steps=[]
        while counter<degree:
            before=tag;tag=zero_core(m,'roles',operation='apply_complex_i',operands=(law,tag));event=m['events'][-1]['id']
            counter=_slot_S(m,counter);steps.append({'before':before,'after':tag,'role_event':event,'counter_event':m['events'][-1]['id']})
        turns.append({'degree':degree,'steps':steps,'result_role':tag})
        match=next((idx for idx,old in enumerate(retained) if old==I_OPPOSITE[tag]),None)
        if match is None:retained.append(tag)
        else:
            opposite=retained[match]
            zero_core(m,'roles',operation='i_zero_return',operands=(law,opposite,tag))
            cancellations.append({'left':opposite,'right':tag,'event':m['events'][-1]['id'],'result':'Z0'})
            retained=[old for idx,old in enumerate(retained) if idx!=match]
    word=[tag for tag in I_TAGS for old in retained if old==tag]
    return {**answer,'status':'evaluated_under_declared_i_role','input_formal_word':list(evaluation['word']),
        'turns':turns,'zero_returns':cancellations,'word':word,'value':_i_display(word)}


def _i_answer_check(m,evaluation,answer):
    law=answer['law_source'];_i_law_check(m,_slot_rows(m,'roles')[law['id']])
    if (law['archive']!='roles' or answer['slot']!=5 or answer['kind']!='logical_answer' or
        answer['assumption']!='declared complex i action and opposite-role zero return'):
        raise ValueError('fifth-slot replay: invalid logical binding')
    if evaluation['status']!='evaluated_formal':
        if answer['status']!=evaluation['status'] or answer['reason']!=evaluation['reason']:
            raise ValueError('fifth-slot replay: invented unresolved value')
        if 'value' in answer or 'word' in answer:raise ValueError('fifth-slot replay: unsupported numeric answer')
        return
    if answer['status']!='evaluated_under_declared_i_role' or answer['input_formal_word']!=evaluation['word']:
        raise ValueError('fifth-slot replay: wrong input')
    if len(answer['turns'])!=len(evaluation['word']):raise ValueError('fifth-slot replay: missing i path')
    counts={tag:0 for tag in I_TAGS}
    for degree,turn in zip(evaluation['word'],answer['turns']):
        expected=I_TAGS[degree%4]
        if turn['degree']!=degree or len(turn['steps'])!=degree or turn['result_role']!=expected:
            raise ValueError('fifth-slot replay: i path length')
        tag='unit'
        for counter,step in enumerate(turn['steps']):
            event=m['events'][step['role_event']];successor=m['events'][step['counter_event']]
            if (step['before']!=tag or step['after']!=I_NEXT[tag] or event['domain']!='roles' or
                event['operation']!='apply_complex_i' or event['status']!='complete' or
                successor['domain']!='rational' or successor['operation']!='S' or successor['status']!='complete' or
                successor['before']!=counter or successor['after']!=counter+1):raise ValueError('fifth-slot replay: broken executable i trace')
            tag=step['after']
        counts[expected]+=1
    required_cancellations=0
    for a,b in [('unit','opposite_unit'),('i_unit','opposite_i_unit')]:
        matched=min(counts[a],counts[b]);counts[a]-=matched;counts[b]-=matched;required_cancellations+=matched
    cancellations=answer['zero_returns']
    if len(cancellations)!=required_cancellations:raise ValueError('fifth-slot replay: missing zero return')
    used={'unit':0,'i_unit':0}
    for c in cancellations:
        ev=m['events'][c['event']]
        if (I_OPPOSITE[c['left']]!=c['right'] or c['result']!='Z0' or ev['domain']!='roles' or
            ev['operation']!='i_zero_return' or ev['status']!='complete'):raise ValueError('fifth-slot replay: false cancellation')
        used['unit' if c['left'] in ('unit','opposite_unit') else 'i_unit']+=1
    original={tag:sum(I_TAGS[d%4]==tag for d in evaluation['word']) for tag in I_TAGS}
    if used!={'unit':min(original['unit'],original['opposite_unit']),
              'i_unit':min(original['i_unit'],original['opposite_i_unit'])}:raise ValueError('fifth-slot replay: cancellation role mismatch')
    expected=[tag for tag in I_TAGS for unused in range(counts[tag])]
    if answer['word']!=expected or answer['value']!=_i_display(expected):raise ValueError('fifth-slot replay: incorrect logical answer')


def _i_power_expansion(m,node):
    exponent=node['args'][1]
    if node.get('operation')!='power' or exponent.get('kind')!='reference' or exponent['ref']['archive']!='rational':
        raise ValueError('i power expansion needs a retained natural repetition counter')
    count=m['expressions'][exponent['ref']['id']]['value']
    if count>SLOT_MAX_DEPTH:raise ValueError('i power expansion counter budget')
    base=node['args'][0];result=_z1_ref(_slot_ref('complex',1));counter=0;events=[]
    while counter<count:
        result=_pr_copy.deepcopy(base) if counter==0 else _z1_call('multiply',result,base)
        counter=_slot_S(m,counter);events.append(m['events'][-1]['id'])
    return result,{'power_counter':exponent['ref'],'repetition_events':events}


def _i_transition_check(m,parent,action,evidence):
    tree=parent['body']['expression']
    if action['kind']=='interpret_i':
        if action['path']!=[]:raise ValueError('fifth-slot replay: answer must bind the complete expression')
        _i_answer_check(m,parent['body']['evaluation'],evidence['answer_slot']);return tree
    node=_z1_at(tree,action['path']);exponent=node['args'][1]
    if node.get('operation')!='power' or exponent.get('kind')!='reference' or exponent['ref']['archive']!='rational':
        raise ValueError('fifth-slot replay: power expansion origin')
    n=m['expressions'][exponent['ref']['id']]['value'];events=evidence['repetition_events']
    if evidence['power_counter']!=exponent['ref'] or len(events)!=n:raise ValueError('fifth-slot replay: expansion repetition count')
    result=_z1_ref(_slot_ref('complex',1))
    for k,event_id in enumerate(events):
        ev=m['events'][event_id]
        if ev['domain']!='rational' or ev['operation']!='S' or ev['status']!='complete' or ev['before']!=k or ev['after']!=k+1:
            raise ValueError('fifth-slot replay: power counter trace')
        result=_pr_copy.deepcopy(node['args'][0]) if k==0 else _z1_call('multiply',result,node['args'][0])
    return _z1_replace(tree,action['path'],result)


_i_prior_variants=_z1_variants
def _z1_variants(m,tree,kind):
    if kind=='interpret_i':return [{'kind':'interpret_i','path':[]}]
    if kind=='expand_i_power':
        return [{'kind':'expand_i_power','path':list(path)} for path,node in _z1_walk(tree)
            if node.get('operation')=='power' and node['args'][1].get('kind')=='reference' and
               node['args'][1]['ref']['archive']=='rational' and
               m['expressions'][node['args'][1]['ref']['id']]['value']<=SLOT_MAX_DEPTH]
    return _i_prior_variants(m,tree,kind)


_i_prior_transform=_z1_transform
def _z1_transform(m,tree,action):
    if action['kind']=='interpret_i':
        if action['path']!=[]:raise ValueError('logical answer binds the complete expression')
        evaluation=zero_core(m,'Zi',operation='evaluate_expression',operands=(tree,))
        answer=zero_core(m,'Zi',operation='logical_answer',operands=(evaluation,))
        return {'expression':_pr_copy.deepcopy(tree),'evidence':{'answer_slot':answer}}
    if action['kind']=='expand_i_power':
        node=_z1_at(tree,action['path']);replacement,evidence=_i_power_expansion(m,node)
        expression=_z1_replace(tree,action['path'],replacement);_z1_check_tree(m,expression)
        return {'expression':expression,'evidence':evidence}
    return _i_prior_transform(m,tree,action)


_i_prior_dispatch=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='Zi' and operation=='logical_answer':return _i_answer(m,*operands)
    if domain=='roles' and operation=='apply_complex_i':
        rid,tag=operands;_i_law_check(m,_slot_rows(m,'roles')[rid])
        if tag not in I_TAGS:raise ValueError('i action requires a retained unit role')
        return I_NEXT[tag]
    if domain=='roles' and operation=='i_zero_return':
        rid,a,b=operands;_i_law_check(m,_slot_rows(m,'roles')[rid])
        if a not in I_TAGS or I_OPPOSITE[a]!=b:raise ValueError('i zero return requires opposite unit roles')
        return 'Z0'
    return _i_prior_dispatch(m,domain,operation,operands,kwargs)


def _i_bootstrap(m):
    _i_ensure(m)
    for rid in list(_z1_state(m)['nodes']):
        # Existing saved expressions gain access to the new action too.
        if _slot_rows(m,'roles')[rid]['body']['action']['kind']!='interpret_i':
            _z1_enqueue(m,rid,'interpret_i')


def _i_answers(m):
    return [r for r in _slot_rows(m,'roles') if r.get('rule')==Z1I_ROLE_RULE and
        r.get('body',{}).get('action',{}).get('kind')=='interpret_i']


_i_prior_replay=_slot_replay
def _slot_replay(m):
    result=_i_prior_replay(m);rid=m.get('Zi',{}).get('i_action_role')
    if rid is not None:_i_law_check(m,_slot_rows(m,'roles')[rid])
    return result


_i_prior_report=_slot_report
def _slot_report(m):
    report=_i_prior_report(m);answers=_i_answers(m)
    evaluated=[r['body']['evidence']['answer_slot'] for r in answers if r['body']['evidence']['answer_slot']['status']=='evaluated_under_declared_i_role']
    report['formal_slot_invariant']=report.get('invariant')
    report['invariant']='retained constructions; logical answers replayed under the archived i role'
    report['blocker']='general symbolic exponents, rational division and general algebra remain deferred'
    report['closure_rules_supplied']=1 if m.get('Zi',{}).get('i_action_role') is not None else 0
    report['deferred']=[x for x in report['deferred'] if x!='signed interpretation']
    report['fifth_slot']={'answers':len(answers),'evaluated':len(evaluated),
        'negative_real_answers':sum(bool(a['word']) and all(t=='opposite_unit' for t in a['word']) for a in evaluated),
        'minus_i_answers':sum(bool(a['word']) and all(t=='opposite_i_unit' for t in a['word']) for a in evaluated),
        'role_law':'declared executable complex i action; not an axiom discovered from S alone'}
    report['negative_values_constructed']=report['fifth_slot']['negative_real_answers']
    if 'Z1i' in report:report['Z1i']['negative_values_derived']=report['fifth_slot']['negative_real_answers']
    return report


_i_prior_z1_report=_z1_report
def _z1_report(m):
    report=_i_prior_z1_report(m)
    answers=[r['body']['evidence']['answer_slot'] for r in _i_answers(m)]
    report['negative_values_derived']=sum(a.get('status')=='evaluated_under_declared_i_role' and bool(a.get('word')) and
        all(t=='opposite_unit' for t in a['word']) for a in answers)
    report['scope']='retained mixing plus explicit complex i action; symbolic exponents remain unresolved'
    return report


_i_prior_query=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    if command in ('rules','assumptions'):
        rid=m.get('Zi',{}).get('i_action_role')
        print(json.dumps({'formal_constructor_rules':m['declared_rules'],
            'active_answer_role':None if rid is None else {'archive':'roles','id':rid,'declared_law':_i_law_body()}},indent=2));return
    if command in ('answers','fifth-slot'):
        for r in _i_answers(m):
            a=r['body']['evidence']['answer_slot'];print('roles:'+str(r['id']),_z1_text(m,r['body']['expression']),'->',a.get('value',a['status']))
        return
    if command=='i-action-example':
        _slot_ensure_counter(m,2);_i_bootstrap(m);frames=_zi_state(m)['frames']
        for operation in ('multiply','add'):
            index=len(frames);frames.append(_zi_frame(1,operation,2,2));root=_z1_seed(m,index)
            parent=root
            for action in ({'kind':'expand_i_power','path':[1]},{'kind':'interpret_i','path':[]}):
                tree=_slot_rows(m,'roles')[parent]['body']['expression']
                transformed=zero_core(m,'Zi',operation='extend_slots',operands=(tree,action))
                parent=_z1_emit(m,parent,transformed['expression'],action,transformed['evidence'])
            r=_slot_rows(m,'roles')[parent];answer=r['body']['evidence']['answer_slot']
            print(r['label'],'|',_z1_text(m,r['body']['expression']),'->',answer.get('value',answer['status']),'| fifth slot | roles:'+str(parent))
        _slot_save(m,memory_path());return
    matches=[r for r in _i_answers(m) if r['body']['evidence']['answer_slot'].get('value')==command]
    if matches:
        for r in matches:print('roles:'+str(r['id']),_z1_text(m,r['body']['expression']),'->',command,'| fifth-slot answer under declared i role')
        return
    return _i_prior_query(m,text)
# ============================================================
# RETAIN ANSWER IN A NEW SLOT, CHECKPOINT IT, THEN FEED BY REFERENCE.
# Fifth answers are immutable. Slot 6 (then 7, 8, ...) is independently backed
# by S and saved before its payload enters any feedback operation.
# ============================================================
SIX_RULE='retained_answer_feedback_slots_v1'
SIX_ROLE_RULE='retain_answer_in_new_slot_v1'
SIX_LANES=('double','rotate','add','multiply','Zi','symbolic')
SIX_IMPORT_BUDGET=4
SIX_WORK=10


def _six_state(m):
    return m.setdefault('answer_feedback',{'rule':SIX_RULE,'answer_cursor':0,'entries':{},'receipts':[],
        'queue':[],'scheduled':[],'lane_heads':{},'lane_cursor':0,'origins':{},'completed':0,
        'ordering':'retain new slot -> durable checkpoint -> feed retained reference through Z0'})


def _six_event(m,idx,operation,domain):
    e=m['events'][idx]
    if e['domain']!=domain or e['operation']!=operation or e['status']!='complete':raise ValueError('answer feedback replay: missing gateway event')
    return e


def _six_retain(m,answer_id):
    state=_six_state(m);key=str(answer_id)
    if key in state['entries']:return state['entries'][key]['slot_role']
    roles=_slot_rows(m,'roles');source=roles[answer_id]
    if source.get('rule')!=Z1I_ROLE_RULE or source['body']['action']['kind']!='interpret_i':raise ValueError('feedback needs a retained fifth-slot answer')
    answer=source['body']['evidence']['answer_slot'];_i_answer_check(m,source['body']['evaluation'],answer)
    previous=_six_previous_slot(m,answer_id)
    before=5 if previous is None else roles[previous]['body']['slot_number']
    _slot_ensure_counter(m,before);number=_slot_S(m,before);event=m['events'][-1]['id'];_slot_ensure_counter(m,number)
    counter=_slot_ensure_counter(m,source['depth']);label='slot'+str(number)
    refs=[_slot_ref('rational',counter),_slot_ref('rational',number),_pr_copy.deepcopy(answer['law_source'])]
    if previous is not None:refs.append(_slot_ref('roles',previous))
    # No conversion, arithmetic or slot roulette consumes this payload yet.
    # Its original logical word and its source are copied into a fresh record.
    body={'slot_number':number,'slot_counter_event':event,'answer_source':_slot_ref('roles',answer_id),
        'previous_slot':None if previous is None else _slot_ref('roles',previous),
        'word':None if 'word' not in answer else list(answer['word']),'value':answer.get('value'),
        'answer_status':answer['status'],'logical_payload':_pr_copy.deepcopy(answer),'law_source':_pr_copy.deepcopy(answer['law_source']),
        'zero_nexus':'Z0'}
    body['optional_slots']=_optional_layout(m,answer_id)
    rec={'kind':'construction','label':label,'operation':'retain_answer_slot','rule':SIX_ROLE_RULE,
        'parents':[answer_id],'sources':refs,'body':body,'path':source['path']+[label],'depth':counter+1,
        'slot':{'counter':counter,'foundation_id':counter}}
    rid=zero_core(m,'roles',operation='record',record=rec)
    record_event=m['events'][-1]['id'];entry={'answer_role':answer_id,'slot_role':rid,'status':'retained','embedding':None}
    state['entries'][key]=entry
    receipt={'slot_role':rid,'record_digest':_zr_digest(_zr_payload(roles[rid])),
        'retention_event':record_event,'event_boundary':len(m['events']),'ordering':'saved_before_payload_feedback'}
    state['receipts'].append(receipt);entry['receipt']=len(state['receipts'])-1
    # This call returns only after atomic write completes. A failure prevents
    # feeding. Resume sees this retained slot and continues from its reference.
    _slot_save(m,memory_path())
    return rid


def _six_role_check(m,role):
    if role.get('kind')!='construction' or role['operation']!='retain_answer_slot' or len(role['parents'])!=1:
        raise ValueError('answer feedback replay: new slot signature')
    body=role['body'];aid=role['parents'][0];source=_slot_rows(m,'roles')[aid]
    if source.get('rule')!=Z1I_ROLE_RULE or source['body']['action']['kind']!='interpret_i':raise ValueError('answer feedback replay: source is not fifth answer')
    answer=source['body']['evidence']['answer_slot'];_i_answer_check(m,source['body']['evaluation'],answer)
    if 'optional_slots' in body and body['optional_slots']!=_optional_layout(m,aid):
        raise ValueError('answer feedback replay: lost optional placement properties')
    if body['logical_payload']!=answer or body['answer_status']!=answer['status']:
        raise ValueError('answer feedback replay: logical answer payload changed')
    previous=body['previous_slot'];before=5
    refs=[_slot_ref('rational',role['slot']['counter']),_slot_ref('rational',body['slot_number']),_pr_copy.deepcopy(answer['law_source'])]
    if previous is not None:
        if previous['archive']!='roles' or previous['id']>=aid:raise ValueError('answer feedback replay: prior slot order')
        parent=_slot_rows(m,'roles')[previous['id']]
        if parent.get('rule')!=SIX_ROLE_RULE:raise ValueError('answer feedback replay: prior slot type')
        before=parent['body']['slot_number'];refs.append(previous)
    expected_previous=_six_previous_slot(m,aid)
    if previous!=(None if expected_previous is None else _slot_ref('roles',expected_previous)):
        raise ValueError('answer feedback replay: lost prior slot lineage')
    event=_six_event(m,body['slot_counter_event'],'S','rational')
    if (body['slot_number']!=before+1 or event['before']!=before or event['after']!=before+1 or
        body['answer_source']!=_slot_ref('roles',aid) or body['word']!=answer.get('word') or body['value']!=answer.get('value') or
        body['law_source']!=answer['law_source'] or body['zero_nexus']!='Z0' or
        role['label']!='slot'+str(body['slot_number']) or role['sources']!=refs):
        raise ValueError('answer feedback replay: retained slot payload or counter changed')


def _six_convert(m,rid):
    roles=_slot_rows(m,'roles');role=roles[rid];_six_role_check(m,role)
    state=_six_state(m);entry=state['entries'][str(role['parents'][0])];receipt=state['receipts'][entry['receipt']]
    # The retained record has already passed a durable checkpoint. This is the
    # first payload-processing gateway, and its proof cites that saved slot.
    feed_event=m['_active_event']
    if feed_event<receipt['event_boundary']:raise ValueError('feedback began before retention')
    if role['body']['answer_status']!='evaluated_under_declared_i_role':return _six_feed_symbolic(m,rid,entry,receipt)
    formal=[];conversion=[]
    for tag in role['body']['word']:
        phase='unit';count=0;steps=[]
        while phase!=tag:
            before=phase;phase=zero_core(m,'roles',operation='apply_complex_i',operands=(role['body']['law_source']['id'],phase))
            i_event=m['events'][-1]['id'];count=_slot_S(m,count);event=m['events'][-1]['id']
            steps.append({'before':before,'after':phase,'i_event':i_event,'counter_event':event})
        _slot_ensure_counter(m,count);formal.append(count);conversion.append({'source_role':tag,'degree':count,'steps':steps})
    rec={'operation':'answer_feedback_embedding','parents':[],'sources':[_slot_ref('roles',rid)],
        'word':sorted(formal),'depth':0,'expr':'retained_answer(roles:'+str(rid)+')',
        'feedback_conversion':{'receipt':entry['receipt'],'feed_event':feed_event,'tokens':conversion}}
    idx=zero_core(m,'complex',operation='record',record=rec)
    entry.update(status='fed',embedding=idx)
    _six_schedule(m,rid,idx)
    return idx


def _six_embedding_check(m,rec):
    if rec['parents'] or len(rec['sources'])!=1 or rec['sources'][0]['archive']!='roles':raise ValueError('answer feedback replay: embedding signature')
    rid=rec['sources'][0]['id'];role=_slot_rows(m,'roles')[rid];_six_role_check(m,role)
    proof=rec['feedback_conversion'];state=m['answer_feedback'];receipt=state['receipts'][proof['receipt']]
    if receipt['slot_role']!=rid or receipt['record_digest']!=_zr_digest(_zr_payload(role)):
        raise ValueError('answer feedback replay: retention receipt disagrees')
    _six_event(m,receipt['retention_event'],'record','roles');feed=_six_event(m,proof['feed_event'],'feed_retained_answer','roles')
    if proof['feed_event']<receipt['event_boundary'] or receipt['retention_event']>=receipt['event_boundary']:
        raise ValueError('answer feedback replay: processing preceded retention checkpoint')
    if len(proof['tokens'])!=len(role['body']['word']):raise ValueError('answer feedback replay: missing conversion units')
    expected=[]
    for tag,token in zip(role['body']['word'],proof['tokens']):
        degree=I_TAGS.index(tag)
        if token['source_role']!=tag or token['degree']!=degree or len(token['steps'])!=degree:
            raise ValueError('answer feedback replay: answer role conversion')
        phase='unit'
        for before,step in enumerate(token['steps']):
            e=_six_event(m,step['counter_event'],'S','rational');_six_event(m,step['i_event'],'apply_complex_i','roles')
            if (step['before']!=phase or step['after']!=I_NEXT[phase] or e['before']!=before or e['after']!=before+1 or
                step['i_event']<=proof['feed_event'] or step['counter_event']<=proof['feed_event']):
                raise ValueError('answer feedback replay: conversion trace/order')
            phase=step['after']
        expected.append(degree)
    if rec['word']!=sorted(expected) or rec['expr']!='retained_answer(roles:'+str(rid)+')':raise ValueError('answer feedback replay: embedding value')
    return sorted(expected)


def _six_job(m,slot,kind,parents,permutation=None):
    state=_six_state(m);key=json.dumps([slot,kind,parents,permutation])
    if key not in state['scheduled']:
        state['scheduled'].append(key);state['queue'].append({'source_slot':slot,'kind':kind,'parents':parents,'permutation':permutation,'status':'pending'})


def _six_schedule(m,rid,idx):
    state=_six_state(m);peers=list(range(min(3,len(_slot_rows(m,'complex')))))
    for entry in list(state['entries'].values())[-3:]:
        if entry['embedding'] is not None and entry['embedding'] not in peers:peers.append(entry['embedding'])
    _six_job(m,rid,'double',[idx,idx]);_six_job(m,rid,'rotate',[idx])
    for other in peers:
        _six_job(m,rid,'add',[idx,other]);_six_job(m,rid,'multiply',[idx,other])
    for permutation in ZI_POLICIES:_six_job(m,rid,'Zi',[idx,idx],list(permutation))


def _six_feed(m,rid):
    state=_six_state(m);role=_slot_rows(m,'roles')[rid];entry=state['entries'][str(role['parents'][0])]
    if entry['status'] in ('fed','symbolically_fed'):return entry['embedding']
    return _six_convert(m,rid)


def _six_next(m):
    state=_six_state(m)
    for unused in SIX_LANES:
        kind=SIX_LANES[state['lane_cursor']];state['lane_cursor']=(state['lane_cursor']+1)%len(SIX_LANES)
        cursor=state['lane_heads'].get(kind,0)
        while cursor<len(state['queue']):
            job=state['queue'][cursor];cursor+=1
            if job['kind']==kind and job['status']=='pending':state['lane_heads'][kind]=cursor;return job
        state['lane_heads'][kind]=cursor
    return None


def _six_execute(m,job):
    if job['kind']=='symbolic':return _six_execute_symbolic(m,job)
    state=_six_state(m);rid=job['source_slot'];role=_slot_rows(m,'roles')[rid]
    entry=state['entries'][str(role['parents'][0])]
    if entry['status']!='fed' or entry['embedding']!=job['parents'][0]:raise ValueError('feedback job lacks a retained fed slot')
    kind=job['kind'];parents=job['parents'];before=len(_slot_rows(m,'complex'))
    operation='add' if kind in ('double','add') else 'multiply' if kind=='multiply' else 'i'
    if kind=='Zi':
        frame=_zi_frame(parents[0],'add',parents[1],1)
        attempt=zero_core(m,'Zi',operation='attempt',operands=(frame,job.get('permutation') or ZI_POLICIES[0]))
        if attempt['status']!='validated':job.update(status='deferred',reason=attempt['status']);return
        job['Zi_attempt']=attempt['id'];result=attempt['output_evaluation']['result_id'];frame=attempt['output']
    else:
        status=_slot_task(m,{'operation':operation,'parents':parents})
        if status!='complete':job.update(status='deferred',reason=status);return
        result=before
        frame=_zi_frame(parents[0],operation,parents[1],1) if len(parents)==2 else _zi_frame(result,'add',0,1)
    frame_index=len(_zi_state(m)['frames']);_zi_state(m)['frames'].append(frame)
    _zi_state(m).setdefault('optional_frame_sources',{})[str(frame_index)]=role['parents'][0]
    root=_z1_seed(m,frame_index);tree=_slot_rows(m,'roles')[root]['body']['expression']
    action={'kind':'interpret_i','path':[]};transformed=zero_core(m,'Zi',operation='extend_slots',operands=(tree,action))
    answer=_z1_emit(m,root,transformed['expression'],action,transformed['evidence'])
    state['origins'][str(answer)]=rid
    job.update(status='complete',result_complex=result,frame_index=frame_index,answer_role=answer)


def _six_service(m,import_budget=SIX_IMPORT_BUDGET,work_budget=SIX_WORK):
    state=_six_state(m);answers=_i_answers(m);imported=0
    # Resume slots retained by an earlier checkpoint before importing new ones.
    for entry in list(state['entries'].values()):
        if entry['status']=='retained':zero_core(m,'roles',operation='feed_retained_answer',operands=(entry['slot_role'],))
    while imported<import_budget and state['answer_cursor']<len(answers):
        source=answers[state['answer_cursor']];answer=source['body']['evidence']['answer_slot']
        rid=_six_retain(m,source['id'])
        zero_core(m,'roles',operation='feed_retained_answer',operands=(rid,));imported+=1
        state['answer_cursor']+=1
    for unused in range(work_budget):
        job=_six_next(m)
        if job is None:break
        zero_core(m,'connected',operation='answer_mix',operands=(job,));state['completed']+=1
    return _six_report(m)


def _six_report(m):
    state=m.get('answer_feedback',{});entries=state.get('entries',{})
    return {'ordering':'retain -> save -> feed reference through Z0','retained_slots':len(entries),
        'fed_slots':sum(e['status'] in ('fed','symbolically_fed') for e in entries.values()),
        'symbolic_slots':sum(e['status']=='symbolically_fed' for e in entries.values()),
        'completed_mixes':sum(j['status']=='complete' for j in state.get('queue',[])),
        'pending_mixes':sum(j['status']=='pending' for j in state.get('queue',[])),
        'largest_slot_number':max([5]+[_slot_rows(m,'roles')[e['slot_role']]['body']['slot_number'] for e in entries.values()])}


_six_prior_dispatch=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='connected' and operation=='answer_feedback':return _six_service(m,**kwargs)
    if domain=='connected' and operation=='answer_mix':return _six_execute(m,*operands)
    if domain=='roles' and operation=='feed_retained_answer':return _six_feed(m,*operands)
    return _six_prior_dispatch(m,domain,operation,operands,kwargs)


_six_prior_replay=_slot_replay
def _slot_replay(m):
    result=_six_prior_replay(m);state=m.get('answer_feedback')
    if state is not None:
        if state.get('rule')!=SIX_RULE:raise ValueError('answer feedback replay: checkpoint schema')
        slots=[e['slot_role'] for e in state['entries'].values()]
        expected=[r['id'] for r in _slot_rows(m,'roles') if r.get('rule')==SIX_ROLE_RULE]
        if sorted(slots)!=expected:raise ValueError('answer feedback replay: missing retained slot')
        for key,entry in state['entries'].items():
            role=_slot_rows(m,'roles')[entry['slot_role']];receipt=state['receipts'][entry['receipt']]
            if (str(entry['answer_role'])!=key or role['parents']!=[entry['answer_role']] or receipt['slot_role']!=role['id'] or
                receipt['record_digest']!=_zr_digest(_zr_payload(role)) or receipt['ordering']!='saved_before_payload_feedback'):
                raise ValueError('answer feedback replay: retention receipt or source mismatch')
            if entry['status']=='fed':
                embedding=_slot_rows(m,'complex')[entry['embedding']]
                if embedding['sources']!=[_slot_ref('roles',role['id'])]:raise ValueError('answer feedback replay: feedback reference mismatch')
            elif entry['status']=='symbolically_fed':
                event=_six_event(m,entry['symbolic_feed_event'],'feed_retained_answer','roles')
                if entry['symbolic_feed_event']<receipt['event_boundary'] or entry['embedding'] is not None:
                    raise ValueError('answer feedback replay: unresolved answer processing order')
            elif entry['status']!='retained' or entry['embedding'] is not None:raise ValueError('answer feedback replay: invalid phase')
        for job in state['queue']:
            if job['status']!='complete':continue
            source=_slot_rows(m,'roles')[job['source_slot']];entry=state['entries'][str(source['parents'][0])]
            if job['kind']=='symbolic':
                if entry['status']!='symbolically_fed':raise ValueError('answer feedback replay: symbolic source phase')
                child=_slot_rows(m,'roles')[job['symbolic_result_role']]
                variants=_z1_variants(m,_slot_rows(m,'roles')[source['parents'][0]]['body']['expression'],job['action_kind'],
                    source=None if job['action']['kind']=='00404_slots' else source['parents'][0])
                if (child['parents']!=source['parents'] or child['body'].get('feedback_slot')!=_slot_ref('roles',source['id']) or
                    child['body']['action']!=job['action'] or job['action']!=variants[job['cursor']]):
                    raise ValueError('answer feedback replay: symbolic result source')
                continue
            if entry['embedding']!=job['parents'][0]:raise ValueError('answer feedback replay: job input')
            r=_slot_rows(m,'complex')[job['result_complex']]
            if job['kind']=='Zi':
                attempt=_zi_state(m)['attempts'][job['Zi_attempt']]
                if (attempt['input']!=_zi_frame(job['parents'][0],'add',job['parents'][1],1) or
                    attempt['permutation']!=list(job.get('permutation') or ZI_POLICIES[0]) or attempt['output_evaluation']['result_id']!=r['id']):raise ValueError('answer feedback replay: Zi result')
                frame=attempt['output']
            else:
                operation='add' if job['kind'] in ('double','add') else 'multiply' if job['kind']=='multiply' else 'i'
                if r['operation']!=operation or r['parents']!=job['parents']:raise ValueError('answer feedback replay: arithmetic path')
                frame=_zi_frame(job['parents'][0],operation,job['parents'][1],1) if len(job['parents'])==2 else _zi_frame(r['id'],'add',0,1)
            if _zi_state(m)['frames'][job['frame_index']]!=frame:raise ValueError('answer feedback replay: continuation frame')
            answer=_slot_rows(m,'roles')[job['answer_role']]
            root=_slot_rows(m,'roles')[answer['parents'][0]]
            if (root['body']['action']!={'kind':'seed_frame','frame_index':job['frame_index']} or
                answer['body']['action']!={'kind':'interpret_i','path':[]} or state['origins'].get(str(answer['id']))!=source['id']):
                raise ValueError('answer feedback replay: output answer ancestry')
        for key,previous in state['origins'].items():
            if not any((j.get('answer_role')==int(key) or j.get('symbolic_result_role')==int(key)) and j['source_slot']==previous and j['status']=='complete' for j in state['queue']):
                raise ValueError('answer feedback replay: unsupported continuing slot lineage')
    return result


_six_prior_report=_slot_report
def _slot_report(m):
    report=_six_prior_report(m);report['answer_feedback']=_six_report(m);return report


def _six_value_entries(m):
    entries=[]
    for r in _slot_rows(m,'complex'):
        entries.append({'value':_slot_display(r['word']),'archive':'complex','id':r['id'],'kind':'formal construction','expr':r['expr']})
    for r in _i_answers(m):
        a=r['body']['evidence']['answer_slot']
        if a.get('status')=='evaluated_under_declared_i_role':
            entries.append({'value':a['value'],'archive':'roles','id':r['id'],'kind':'fifth answer','expr':_z1_text(m,r['body']['expression'])})
    for r in _slot_rows(m,'roles'):
        if r.get('rule')==SIX_ROLE_RULE and r['body']['value'] is not None:entries.append({'value':r['body']['value'],'archive':'roles','id':r['id'],
            'kind':'retained slot '+str(r['body']['slot_number']),'expr':'source roles:'+str(r['parents'][0])})
    return entries


_six_prior_query=_slot_query
def _slot_query(m,text):
    command=text.strip().lower().replace(' ','')
    if command=='-0':command='0'
    if command=='1i':command='i'
    if command in ('feedback','sixth-slot'):
        print(json.dumps(_six_report(m),indent=2));return
    if command in ('index','complex-index'):
        groups={}
        for e in _six_value_entries(m):groups.setdefault(e['value'],[]).append(e)
        for value,rows in groups.items():
            kinds={}
            for row in rows:kinds[row['kind']]=kinds.get(row['kind'],0)+1
            print(value,'| retained paths:',len(rows),'|',kinds)
        return
    matches=[r for r in _six_value_entries(m) if r['value'].lower()==command]
    if matches:
        print('Value',command,'| retained paths:',len(matches))
        for row in matches[:30]:print(row['archive']+':'+str(row['id']),row['expr'],'|',row['kind'])
        return
    return _six_prior_query(m,text)

# Unresolved answer payloads also receive a retained slot, then return through
# the zero gateway to structural functions. They are never silently discarded.
def _six_previous_slot(m,answer_id):
    state=_six_state(m)
    if str(answer_id) in state['origins']:return state['origins'][str(answer_id)]
    roles=_slot_rows(m,'roles');current=roles[answer_id];seen=set()
    while current.get('rule')==Z1I_ROLE_RULE and current['id'] not in seen:
        seen.add(current['id'])
        if current['body'].get('feedback_slot') is not None:return current['body']['feedback_slot']['id']
        if not current['parents']:break
        current=roles[current['parents'][0]]
    return None


def _six_symbolic_job(m,rid,kind,cursor=0):
    state=_six_state(m);key=json.dumps([rid,'symbolic',kind,cursor])
    if key not in state['scheduled']:
        state['scheduled'].append(key);state['queue'].append({'source_slot':rid,'kind':'symbolic',
            'action_kind':kind,'cursor':cursor,'parents':[],'status':'pending'})


def _six_feed_symbolic(m,rid,entry,receipt):
    if m['_active_event']<receipt['event_boundary']:raise ValueError('symbolic feedback preceded retention')
    entry.update(status='symbolically_fed',symbolic_feed_event=m['_active_event'])
    for kind in Z1I_ACTIONS:_six_symbolic_job(m,rid,kind)
    return {'retained_slot':rid,'numeric_value':'unresolved','route':'Zi structural transformations'}


def _six_execute_symbolic(m,job):
    state=_six_state(m);rid=job['source_slot'];slot=_slot_rows(m,'roles')[rid];aid=slot['parents'][0]
    entry=state['entries'][str(aid)]
    if entry['status']!='symbolically_fed':raise ValueError('unresolved answer lacks its saved feedback slot')
    source=_slot_rows(m,'roles')[aid];tree=source['body']['expression'];variants=_z1_variants(m,tree,job['action_kind'],source=aid)
    cursor=job['cursor']
    if cursor>=len(variants):job['status']='no_applicable_slots';return
    action=variants[cursor]
    try:out=zero_core(m,'Zi',operation='extend_slots',operands=(tree,action))
    except ValueError as exc:
        if str(exc)!='Z1i expression slot budget':raise
        job.update(status='deferred',reason=str(exc))
        job['proposal']=zero_core(m,'opportunities',operation='retain_deferred',
            operands=(aid,action,getattr(exc,'retained_proposal',None),str(exc)))
    else:
        result=_z1_emit(m,aid,out['expression'],action,out['evidence'],feedback_slot=rid)
        job.update(status='complete',symbolic_result_role=result,action=action)
        if action['kind']=='interpret_i':state['origins'][str(result)]=rid
    next_cursor=_slot_S(m,cursor)
    if next_cursor<len(variants):_six_symbolic_job(m,rid,job['action_kind'],next_cursor)

# Optional spaces retain placement provenance without introducing numeric zeros.
# Existing filled 00404 constructions retain their historical interpretation.
OPTIONAL_ACTIONS=('reserve_optional','optional_place','optional_reorder','optional_merge','optional_combine','optional_apply_role')

def _optional_layout(m,rid):
    return _pr_copy.deepcopy(_slot_rows(m,'roles')[rid]['body'].get('optional_slots',[]))

def _optional_sources(layout):
    refs=[]
    for slot in layout:
        for member in slot['members']:
            ref=_slot_ref('rational',member)
            if ref not in refs:refs.append(ref)
        payload=slot['payload']
        if payload and 'ref' in payload and payload['ref'] not in refs:refs.append(payload['ref'])
    return refs

def _optional_transition(m,rid,action,construct=False):
    source=_slot_rows(m,'roles')[rid];tree=source['body']['expression'];layout=_optional_layout(m,rid)
    if action.get('source_role')!=rid or action.get('path')!=[]:raise ValueError('Optional slot source or path')
    kind=action['kind'];evidence={'zero_nexus':'Z0','blank_is_numeric_zero':False}
    if kind=='reserve_optional':
        if layout:raise ValueError('Optional slot capacity already retained')
        pattern=digit_breakdown('00404');steps=[];counter=0
        for char in pattern:
            if construct:
                counter=_slot_S(m,counter);steps.append(m['events'][-1]['id']);_slot_ensure_counter(m,counter)
            else:counter+=1
            layout.append({'members':[counter],'template':char,'payload':None})
        evidence.update(template='00404',expansion=pattern)
        if construct:evidence['counter_events']=steps
    elif kind=='optional_place':
        pos=action['position']
        if type(pos) is not int or not 0<=pos<len(layout) or layout[pos]['payload'] is not None:
            raise ValueError('Optional placement requires a blank')
        payload=action['payload']
        if payload.get('kind')=='value':
            if set(payload)!={'kind','ref'}:raise ValueError('Optional value payload')
            _z1_check_tree(m,_z1_ref(payload['ref']))
        elif payload.get('kind')=='operation' and 'ref' in payload:
            _zstruct_check_role_ref(m,payload['ref'])
            if set(payload)!={'kind','ref','mode'} or payload['mode']!='apply_current':raise ValueError('Optional unary role placement binding')
        elif payload not in ({'kind':'operation','symbol':'add'},{'kind':'operation','symbol':'multiply'}):
            raise ValueError('Optional operation has no executable binding')
        layout[pos]['payload']=_pr_copy.deepcopy(payload)
    elif kind=='optional_reorder':
        order=action['order']
        if len(order)!=len(layout) or any(type(i) is not int for i in order) or sorted(order)!=list(range(len(layout))):
            raise ValueError('Optional placement order must retain every group')
        layout=[layout[i] for i in order]
    elif kind=='optional_merge':
        a,b=action['positions']
        if (type(a) is not int or type(b) is not int or not 0<=a<b<len(layout) or
            layout[a]['payload'] is not None or layout[b]['payload'] is not None):raise ValueError('Only blank spaces may merge')
        layout[a]={'members':layout[a]['members']+layout[b]['members'],'template':'reserved_group','payload':None}
        del layout[b]
    elif kind=='optional_apply_role':
        pos=action['position'];payload=layout[pos]['payload']
        if not payload or payload.get('mode')!='apply_current':raise ValueError('No retained unary role in this slot')
        _zstruct_check_role_ref(m,payload['ref']);tree=_zstruct_path_call(payload['ref'],tree)
        layout[pos]['payload']=None;evidence['used_placements']=[pos]
    elif kind=='optional_combine':
        oi,vi=action['operation_position'],action['value_position']
        if any(type(i) is not int or not 0<=i<len(layout) for i in (oi,vi)) or oi==vi:raise ValueError('Optional combination positions')
        op=layout[oi]['payload'];value=layout[vi]['payload']
        if not op or op.get('kind')!='operation' or not value or value.get('kind')!='value':
            raise ValueError('Optional combination needs a placed operation and value')
        tree=_z1_call(op['symbol'],tree,_z1_ref(value['ref']))
        evidence['used_placements']=[oi,vi]
        # Parent retains the occupied arrangement. These same spaces are now
        # blank and available on this new path; the source is never overwritten.
        layout[oi]['payload']=None;layout[vi]['payload']=None
    else:raise ValueError('Unknown optional slot action')
    _z1_check_tree(m,tree);evidence['layout']=layout
    return tree,evidence

def _optional_layout_after(m,parent,action,evidence):
    if action['kind']=='seed_frame':
        source=_zi_state(m).get('optional_frame_sources',{}).get(str(action['frame_index']))
        return [] if source is None else _optional_layout(m,source)
    if action['kind'] in OPTIONAL_ACTIONS:return _pr_copy.deepcopy(evidence['layout'])
    return _optional_layout(m,parent)

_optional_old_transform=_z1_transform
def _z1_transform(m,tree,action):
    if action['kind'] not in OPTIONAL_ACTIONS:return _optional_old_transform(m,tree,action)
    rid=action['source_role']
    if _slot_rows(m,'roles')[rid]['body']['expression']!=tree:raise ValueError('Optional slot expression source')
    result,evidence=_optional_transition(m,rid,action,construct=True)
    return {'expression':result,'evidence':evidence}

_optional_old_variants=_z1_variants
def _z1_variants(m,tree,kind,source=None):
    if source is None:return _optional_old_variants(m,tree,kind)
    layout=_optional_layout(m,source);base={'source_role':source,'path':[]}
    if kind=='00404_slots':return [dict(base,kind='reserve_optional')] if not layout else []
    if kind=='optional_place':
        blanks=[i for i,s in enumerate(layout) if s['payload'] is None]
        if not blanks:return []
        payloads=[{'kind':'value','ref':_slot_ref('complex',i)} for i in range(len(_slot_rows(m,'complex')))]
        payloads += [{'kind':'operation','symbol':op} for op in ('add','multiply')]
        payloads += [{'kind':'operation','ref':_slot_ref('roles',rid),'mode':'apply_current'} for rid in _zstruct_available_roles(m)]
        return [dict(base,kind=kind,position=position,payload=p) for position in blanks for p in payloads]
    if kind=='optional_reorder':return [dict(base,kind=kind,order=list(range(1,len(layout)))+[0])] if len(layout)>1 else []
    if kind=='optional_merge':
        blanks=[i for i,s in enumerate(layout) if s['payload'] is None]
        return [dict(base,kind=kind,positions=blanks[:2])] if len(blanks)>1 else []
    if kind=='optional_combine':
        ops=[i for i,s in enumerate(layout) if s['payload'] and s['payload']['kind']=='operation' and 'symbol' in s['payload']]
        vals=[i for i,s in enumerate(layout) if s['payload'] and s['payload']['kind']=='value']
        return [dict(base,kind=kind,operation_position=o,value_position=v) for o in ops for v in vals]
    if kind=='optional_apply_role':
        return [dict(base,kind=kind,position=i) for i,s in enumerate(layout) if s['payload'] and s['payload'].get('mode')=='apply_current']
    return _optional_old_variants(m,tree,kind)

_optional_old_role_check=_z1_role_check
def _z1_role_check(m,role):
    action=role['body']['action'];evidence=role['body']['evidence']
    if action['kind']=='reserve_optional':
        steps=evidence['counter_events']
        if len(steps)!=len(digit_breakdown('00404')):raise ValueError('Optional slot counter count')
        for before,idx in enumerate(steps):
            event=_six_event(m,idx,'S','rational')
            if event['before']!=before or event['after']!=before+1:raise ValueError('Optional slot counter evidence')
    return _optional_old_role_check(m,role)

_optional_old_report=_slot_report
def _slot_report(m):
    report=_optional_old_report(m);layouts=[r['body']['optional_slots'] for r in _slot_rows(m,'roles') if r.get('body',{}).get('optional_slots')]
    report['optional_slots']={'retained_layouts':len(layouts),'blank_occurrences':sum(s['payload'] is None for l in layouts for s in l),
        'occupied_occurrences':sum(s['payload'] is not None for l in layouts for s in l),
        'rule':'blank is available space, not numeric zero; parent placements and zero provenance retained'}
    return report

_optional_old_replay=_slot_replay
def _slot_replay(m):
    result=_optional_old_replay(m)
    for frame,source in m.get('Zi',{}).get('optional_frame_sources',{}).items():
        matches=[j for j in m.get('answer_feedback',{}).get('queue',[]) if j.get('frame_index')==int(frame) and j.get('status')=='complete']
        if len(matches)!=1 or _slot_rows(m,'roles')[matches[0]['source_slot']]['parents']!=[source]:
            raise ValueError('Optional slot replay: continuation frame source')
    return result

_optional_old_query=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    if command in ('optional','optional-slots'):
        print(json.dumps(_slot_report(m)['optional_slots'],indent=2));return
    result=_optional_old_query(m,text)
    if command in ('help','?'):print('optional-slots: inspect retained blank and occupied spaces')
    return result

# ============================================================
# OPPORTUNITIES: evidence index and retained deferred proposals.
# Observations do not create numeric values or promote operation laws.
# ============================================================
_opportunity_prior_check_tree=_z1_check_tree
def _z1_check_tree(m,tree):
    try:return _opportunity_prior_check_tree(m,tree)
    except ValueError as exc:
        if str(exc)=='Z1i expression slot budget':exc.retained_proposal=_pr_copy.deepcopy(tree)
        raise

def _opportunity_expected(m,source,action):
    original=_slot_rows(m,'roles')[source]['body']['expression'];kind=action['kind'];path=action['path']
    lane='00404_slots' if kind=='reserve_optional' else kind
    if action not in _z1_variants(m,original,lane,source=source):
        raise ValueError('Deferred proposal is not an eligible transformation of its source')
    if kind in OPTIONAL_ACTIONS:
        try:return _optional_transition(m,source,action,construct=False)[0]
        except ValueError as exc:
            if str(exc)=='Z1i expression slot budget':return exc.retained_proposal
            raise
    node=_z1_at(original,path)
    if kind=='append_zero':replacement=_z1_call('add',original,_z1_ref(_slot_ref('rational',0)))
    elif kind=='00404_slots':
        replacement=_z1_ref(_slot_ref('rational',0))
        for char in digit_breakdown('00404'):
            replacement=_z1_call('add',replacement,_z1_ref(_slot_ref('rational',0)) if char=='0' else original)
    elif kind=='switch_operation':replacement=_z1_call(action['operation'],*node['args'])
    elif kind=='exchange_power_slots':replacement=_z1_call('power',node['args'][1],node['args'][0])
    elif kind=='split_counter_zero':
        replacement=_z1_ref(_slot_ref('rational',0))
        for unused in range(m['expressions'][node['ref']['id']]['value']):
            replacement=_z1_call('add',replacement,_z1_ref(_slot_ref('rational',1)))
    elif kind=='expand_i_power':
        replacement=_z1_ref(_slot_ref('complex',1))
        for counter in range(m['expressions'][node['args'][1]['ref']['id']]['value']):
            replacement=_pr_copy.deepcopy(node['args'][0]) if counter==0 else _z1_call('multiply',replacement,node['args'][0])
    else:raise ValueError('Deferred proposal has no reconstructible placement recipe')
    return _z1_replace(original,path,replacement)

_opportunity_prior_dispatch=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain!='opportunities':return _opportunity_prior_dispatch(m,domain,operation,operands,kwargs)
    if operation!='retain_deferred':raise ValueError('Unknown opportunity operation')
    source,action,tree,reason=operands
    if tree is None or tree!=_opportunity_expected(m,source,action):raise ValueError('Missing deferred proposal formula')
    pool=m.setdefault('opportunity_proposals',{'rule':'retained_deferred_formula_v1','records':[],'recipes':[]})
    record={'id':len(pool['records']),'source_role':source,'action':_pr_copy.deepcopy(action),
        'expression':_pr_copy.deepcopy(tree),'reason':reason,'status':'reserved',
        'eligibility':'reconsider when expression capacity or placement rules change',
        'zero_nexus':'Z0','retention_event':m['_active_event']}
    pool['records'].append(record);pool['recipes'].append(_pr_copy.deepcopy(record))
    m['feedback'].append({'source':{'constructor':'retained_deferred_formula','id':record['id']},
        'targets':['opportunity_observer','reserved_formula_pool'],'zero_nexus':'Z0','status':'reserved'})
    return record['id']

_opportunity_prior_replay=_slot_replay
def _slot_replay(m):
    result=_opportunity_prior_replay(m);pool=m.get('opportunity_proposals')
    if pool is not None:
        if pool.get('rule')!='retained_deferred_formula_v1' or pool['records']!=pool['recipes']:
            raise ValueError('Opportunity replay: retained proposal recipe conflict')
        for idx,row in enumerate(pool['records']):
            if row['id']!=idx or row['expression']!=_opportunity_expected(m,row['source_role'],row['action']):
                raise ValueError('Opportunity replay: changed proposal construction')
            if row['status']!='reserved' or row['reason']!='Z1i expression slot budget':
                raise ValueError('Opportunity replay: changed deferred status')
            event=m['events'][row['retention_event']]
            if event['domain']!='opportunities' or event['operation']!='retain_deferred' or event['status']!='complete' or row['zero_nexus']!='Z0':
                raise ValueError('Opportunity replay: missing proposal passage through zero')
        tasks=m.get('Zi',{}).get('walk',{}).get('queue',[])+m.get('answer_feedback',{}).get('queue',[])
        for task in tasks:
            if 'proposal' not in task:continue
            row=pool['records'][task['proposal']]
            if task.get('source',_slot_rows(m,'roles')[task['source_slot']]['parents'][0] if 'source_slot' in task else None)!=row['source_role']:
                raise ValueError('Opportunity replay: deferred task source')
    return result

def _opportunity_report(m):
    roles=_slot_rows(m,'roles');complex_rows=_slot_rows(m,'complex');costs=[]
    # Structural node counts compare retained descriptions. They are not
    # timing measurements or proofs of a universally faster algorithm.
    for row in complex_rows:costs.append(1+sum(costs[p] for p in row['parents']))
    def cost(tree):
        if tree['kind']=='reference':
            ref=tree['ref'];return costs[ref['id']] if ref['archive']=='complex' else 1
        return 1+sum(cost(child) for child in tree['args'])
    groups={};unresolved=[];logical_lookup={}
    for row in roles:
        if row.get('rule')!=Z1I_ROLE_RULE:continue
        body=row['body'];evaluation=body['evaluation']
        if evaluation['status']!='evaluated_formal':
            unresolved.append({'role':row['id'],'status':evaluation['status'],'reason':evaluation.get('reason'),
                'expression':body['expression'],'zero_nexus':body['zero_nexus']})
        if body['action']['kind']!='interpret_i':continue
        answer=body['evidence']['answer_slot']
        if answer['status']!='evaluated_under_declared_i_role':continue
        logical_lookup[tuple(answer['input_formal_word'])]=tuple(answer['word'])
        entry={'role':row['id'],'expression':_z1_text(m,body['expression']),
            'construction_nodes':cost(body['expression']),
            'signature':json.dumps(body['expression'],sort_keys=True,separators=(',',':'))}
        groups.setdefault(tuple(answer['word']),{'value':answer['value'],'entries':[]})['entries'].append(entry)
    shortcuts=[]
    for group in groups.values():
        entries=group['entries'];signatures={r['signature'] for r in entries}
        if len(signatures)<2:continue
        ordered=sorted(entries,key=lambda r:(r['construction_nodes'],r['role']));best=ordered[0]
        shortcuts.append({'value':group['value'],'answer_roles':[r['role'] for r in entries],
            'distinct_retained_structures':len(signatures),
            'shortest_observed':{k:v for k,v in best.items() if k!='signature'},
            'largest_observed_node_count':ordered[-1]['construction_nodes'],
            'status':'candidate_for_cross_input_testing','universal_rule_established':False})
    zi=m.get('Zi',{});contrasts=[];pending=[]
    for attempt in zi.get('attempts',[]):
        if attempt['status']=='validated' and not attempt['same_formal_value']:
            input_word=tuple(complex_rows[attempt['input_evaluation']['result_id']]['word'])
            output_word=tuple(complex_rows[attempt['output_evaluation']['result_id']]['word'])
            logical_relation='not_evaluated_as_pair'
            if input_word in logical_lookup and output_word in logical_lookup:
                logical_relation='=' if logical_lookup[input_word]==logical_lookup[output_word] else '!='
            contrasts.append({'attempt':attempt['id'],'input':attempt['input'],'output':attempt['output'],
                'input_result':attempt['input_evaluation']['result_id'],
                'output_result':attempt['output_evaluation']['result_id'],
                'relation':'different formal words; logical equality not inferred here',
                'logical_relation_from_retained_answers':logical_relation,
                'use':'retain as distinct constructions; do not treat slot permutation as an equality'})
        elif attempt['status']!='validated':
            pending.append({'attempt':attempt['id'],'status':attempt['status'],'reason':attempt.get('reason'),
                'input':attempt['input'],'output':attempt['output'],'zero_nexus':attempt['zero_nexus']})
    reserved=_pr_copy.deepcopy(m.get('opportunity_proposals',{}).get('records',[]))
    # Old deferred tasks still retain their source and transformation recipe;
    # label them honestly when the old version did not store the full candidate.
    legacy=[]
    for task in zi.get('walk',{}).get('queue',[]):
        if task['status']=='size_deferred' and 'proposal' not in task:
            legacy.append({'source_role':task['source'],'kind':task['kind'],'cursor':task['cursor'],
                'reason':task.get('reason'),'full_proposal_retained':False})
    return {'rule':'opportunities_evidence_index_v1','scope':'observations under the declared i law; no new arithmetic laws promoted',
        'summary':{'matching_endpoint_groups':len(shortcuts),'distinct_formal_outcomes':len(contrasts),
            'awaiting_interpretation_or_capacity':len(pending),'unresolved_expression_records':len(unresolved),
            'full_reserved_proposals':len(reserved),'older_deferred_recipes_only':len(legacy)},
        'shortcut_candidates':shortcuts,'nonmatching_formal_constructions':contrasts,
        'pending_placement_proposals':pending,'unresolved_expressions':unresolved,'reserved_formulas':reserved,
        'older_deferred_recipes':legacy,
        'calculus':{'status':'not_established','numeric_branch_records':len(m.get('calculus_archive',{}).get('expressions',[])),
            'needed_evidence':['linked input changes and displacements','equal-part refinements or exact ratios',
                'rate or accumulation constructions','comparison across refinements with validity conditions'],
            'note':'More complex expressions alone do not establish calculus structures.'},
        'reuse':'References remain in their existing queues or reserved pool; reservation does not guarantee every possible reuse is scheduled.',
        'cost_measure':'expanded retained description nodes; not measured runtime'}

def _opportunity_export(m,path):
    report=_opportunity_report(m);_ze_atomic_json(str(path)+'.opportunities.json',report);return report

_opportunity_prior_report=_slot_report
def _slot_report(m):
    report=_opportunity_prior_report(m);report['opportunities']=_opportunity_report(m)['summary'];return report

_opportunity_prior_query=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    sections={'shortcuts':'shortcut_candidates','proposals':'pending_placement_proposals',
              'unequal':'nonmatching_formal_constructions','reserved':'reserved_formulas','calculus':'calculus'}
    if command=='opportunities' or command.startswith('opportunities '):
        report=_opportunity_export(m,memory_path());part=command.partition(' ')[2]
        if part and part not in sections:
            print('opportunities [shortcuts | proposals | unequal | reserved | calculus]');return
        print(json.dumps(report[sections[part]] if part else {
            'summary':report['summary'],'calculus':report['calculus']['status'],
            'commands':'opportunities shortcuts / proposals / unequal / reserved / calculus',
            'report':str(memory_path())+'.opportunities.json'},indent=2));return
    result=_opportunity_prior_query(m,text)
    if command in ('help','?'):print('opportunities: matching paths, different outcomes, reserved formulas and calculus evidence')
    return result

# ============================================================
# RETAINED PATH -> EXECUTABLE ROLE (bounded unary-i experiment).
# Path bodies come from archived steps; no half-turn answer is seeded.
# ============================================================
PATH_ROLE='retained_unary_pathway_role_v1'
PATH_EXEC='retained_pathway_execution_v1'

def _path_state(m):
    return m.setdefault('pathway_operations',{'rule':'pathway_binding_experiment_v1','candidates':{},
        'executions':[],'comparisons':[],'comparison_recipes':[],'reuses':[],'archive_cursor':0})

def _path_chain(m,idx):
    records=_slot_rows(m,'complex');path=[];current=idx
    while records[current]['operation']=='i':
        path.append(current);current=records[current]['parents'][0]
    return current,list(reversed(path))

def _path_bind(m,idx):
    root,path=_path_chain(m,idx)
    if not 2<=len(path):return None
    state=_path_state(m);key=str(len(path))
    if key in state['candidates']:return state['candidates'][key]
    counter=_slot_ensure_counter(m,1);label='path_i_'+key
    body={'operations':['i' for _ in path],'source_input':root,'source_path':path,
        'scope':'retained unary i-composition; bounded by existing depth and unit limits',
        'general_law_discovered':False,'zero_nexus':'Z0'}
    rec={'kind':'operation','label':label,'operation':'bind_retained_pathway','rule':PATH_ROLE,
        'parents':[2],'sources':[_slot_ref('rational',counter),_slot_ref('roles',4)]+
            [_slot_ref('complex',p) for p in [root]+path],
        'body':body,'path':['0','S0',label],'depth':2,'slot':{'counter':counter,'foundation_id':counter}}
    rid=zero_core(m,'roles',operation='record',record=rec);state['candidates'][key]=rid
    # Testing the role on distinct inputs does not promote a universal rule.
    for input_id in dict.fromkeys([0,1,2,root]):_slot_queue(m,'execute_pathway',[rid,input_id])
    m['feedback'].append({'source':_slot_ref('roles',rid),'targets':['pathway_tester','operation_frontier'],
        'zero_nexus':'Z0','status':'candidate_bound'})
    return rid

_path_prior_observe=_slot_observe
def _slot_observe(m,idx):
    result=_path_prior_observe(m,idx);_path_bind(m,idx);return result

def _path_answer(m,result):
    frames=_zi_state(m)['frames'];idx=len(frames);frames.append(_zi_frame(result,'add',0,1))
    parent=_z1_seed(m,idx);action={'kind':'interpret_i','path':[]}
    out=zero_core(m,'Zi',operation='extend_slots',operands=(_slot_rows(m,'roles')[parent]['body']['expression'],action))
    return _z1_emit(m,parent,out['expression'],action,out['evidence'])

def _path_compare(m,left,right,context):
    roles=_slot_rows(m,'roles');a=roles[left]['body'];b=roles[right]['body']
    if a['status']!='complete' or b['status']!='complete' or a['input']!=b['input']:
        raise ValueError('Pathway comparison requires completed executions of the same input')
    def word(body):return roles[body['answer_role']]['body']['evidence']['answer_slot']['word']
    state=_path_state(m);row={'id':len(state['comparisons']),'left_execution':left,'right_execution':right,
        'context':context,'relation':'=' if word(a)==word(b) else '!=','zero_nexus':'Z0','event':m['_active_event']}
    state['comparisons'].append(row);state['comparison_recipes'].append(_pr_copy.deepcopy(row))
    m['feedback'].append({'source':{'constructor':'pathway_comparison','id':row['id']},
        'targets':['pathway_observer','operation_evidence'],'zero_nexus':'Z0','status':row['relation']})
    return row['id']

def _path_execute(m,rid,input_id):
    roles=_slot_rows(m,'roles');role=roles[rid];_path_role_check(m,role)
    if role['rule']!=PATH_ROLE:raise ValueError('Not a retained pathway operation')
    records=_slot_rows(m,'complex')
    if type(input_id) is not int or not 0<=input_id<len(records):raise ValueError('Missing retained pathway input')
    state=_path_state(m)
    for previous in state['executions']:
        cached=roles[previous]
        if cached['parents']==[rid] and cached['body']['input']==input_id and cached['body']['status']=='complete' and cached['body']['relation']=='=':
            _path_role_check(m,cached)
            state.setdefault('reuses',[]).append({'operation_role':rid,'input':input_id,'execution_role':previous,
                'event':m['_active_event'],'zero_nexus':'Z0'})
            return {'status':'complete','execution_role':previous,'answer_role':cached['body']['answer_role'],'relation':'=','reused':True}
    traces=[];status='complete';reason=None
    # The executable body and the original archived template are read
    # separately. Both routes retain every newly constructed intermediate.
    for operations in (role['body']['operations'],[records[p]['operation'] for p in role['body']['source_path']]):
        cursor=input_id;trace=[]
        for op in operations:
            before=len(records);step_status=_slot_task(m,{'operation':op,'parents':[cursor]})
            if step_status!='complete':status=step_status;reason='existing construction bound';break
            cursor=before;trace.append(cursor)
        traces.append(trace)
        if status!='complete':break
    while len(traces)<2:traces.append([])
    body={'input':input_id,'trace':traces[0],'reference_trace':traces[1],'status':status,'reason':reason,
        'answer_role':None,'reference_answer_role':None,'relation':None,'zero_nexus':'Z0'}
    if status=='complete':
        body['answer_role']=_path_answer(m,traces[0][-1]);body['reference_answer_role']=_path_answer(m,traces[1][-1])
        answers=[roles[body[k]]['body']['evidence']['answer_slot'] for k in ('answer_role','reference_answer_role')]
        if all(answer['status']=='evaluated_under_declared_i_role' for answer in answers):
            body['relation']='=' if answers[0]['word']==answers[1]['word'] else '!='
        else:
            body.update(status='size_deferred',reason='retained answer awaits a larger recorded work allowance',answer_role=None,reference_answer_role=None)
            status='size_deferred'
    counter=_slot_ensure_counter(m,role['depth']);label='path_execution_'+str(len(_path_state(m)['executions']))
    refs=[_slot_ref('rational',counter),_slot_ref('complex',input_id)]
    for idx in traces[0]+traces[1]:
        ref=_slot_ref('complex',idx)
        if ref not in refs:refs.append(ref)
    for key in ('answer_role','reference_answer_role'):
        if body[key] is not None:refs.append(_slot_ref('roles',body[key]))
    rec={'kind':'construction','label':label,'operation':'execute_retained_pathway','rule':PATH_EXEC,
        'parents':[rid],'sources':refs,'body':body,'path':role['path']+[label],
        'depth':counter+1,'slot':{'counter':counter,'foundation_id':counter}}
    execution=zero_core(m,'roles',operation='record',record=rec);state=_path_state(m)
    prior=list(state['executions']);state['executions'].append(execution)
    if status=='complete':
        alternatives=[other for other in prior if roles[other]['body']['status']=='complete' and
            roles[other]['body']['input']==input_id and roles[other]['parents']!=[rid]]
        for other in alternatives:
            zero_core(m,'pathways',operation='compare',operands=(execution,other,'different_retained_pathways'))
    m['feedback'].append({'source':_slot_ref('roles',execution),
        'targets':['pathway_evidence','retained_answer_frontier'],'zero_nexus':'Z0','status':status})
    return {'status':status,'execution_role':execution,'answer_role':body['answer_role'],'relation':body['relation']}

def _path_role_check(m,role):
    records=_slot_rows(m,'complex');roles=_slot_rows(m,'roles');body=role['body']
    if role['rule']==PATH_ROLE:
        root,path=_path_chain(m,body['source_path'][-1])
        expected_refs=[_slot_ref('rational',1),_slot_ref('roles',4)]+[_slot_ref('complex',p) for p in [root]+path]
        if (body['operations']!=['i' for _ in path] or body['source_path']!=path or body['source_input']!=root or
            not 2<=len(path) or role['parents']!=[2] or role['sources']!=expected_refs or
            body['general_law_discovered'] is not False or body['zero_nexus']!='Z0'):
            raise ValueError('Pathway replay: changed bound path body or provenance')
        return
    if role['rule']!=PATH_EXEC:raise ValueError('Unknown pathway role')
    parent=roles[role['parents'][0]]
    if parent['rule']!=PATH_ROLE:raise ValueError('Pathway execution has no bound operation')
    operations=parent['body']['operations'];expected_refs=[_slot_ref('rational',role['slot']['counter']),_slot_ref('complex',body['input'])]
    for trace in (body['trace'],body['reference_trace']):
        if len(trace)>len(operations):raise ValueError('Pathway execution has extra steps')
        previous=body['input']
        for operation,idx in zip(operations,trace):
            row=records[idx]
            if row['operation']!=operation or row['parents']!=[previous]:raise ValueError('Pathway execution lost an intermediate')
            ref=_slot_ref('complex',idx)
            if ref not in expected_refs:expected_refs.append(ref)
            previous=idx
    if body['status']=='complete':
        if any(len(t)!=len(operations) for t in (body['trace'],body['reference_trace'])):raise ValueError('Incomplete pathway accepted')
        words=[]
        for trace,key in ((body['trace'],'answer_role'),(body['reference_trace'],'reference_answer_role')):
            answer=roles[body[key]]
            expected=_z1_from_frame(_zi_frame(trace[-1],'add',0,1))
            if (answer['rule']!=Z1I_ROLE_RULE or answer['body']['action']!={'kind':'interpret_i','path':[]} or
                answer['body']['expression']!=expected):raise ValueError('Pathway answer is not linked to its result')
            words.append(answer['body']['evidence']['answer_slot']['word']);expected_refs.append(_slot_ref('roles',body[key]))
        if body['relation']!=('=' if words[0]==words[1] else '!='):raise ValueError('Changed pathway comparison verdict')
    elif (body['status'] not in ('depth_deferred','size_deferred') or body['answer_role'] is not None or
          body['reference_answer_role'] is not None or body['relation'] is not None):
        raise ValueError('Pathway failure evidence missing')
    if role['sources']!=expected_refs or body['zero_nexus']!='Z0':raise ValueError('Changed pathway execution sources')

_path_prior_dispatch=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain!='pathways':return _path_prior_dispatch(m,domain,operation,operands,kwargs)
    if operation=='execute':return _path_execute(m,*operands)
    if operation=='compare':return _path_compare(m,*operands)
    if operation=='observe_archive':
        state=_path_state(m)
        for unused in range(kwargs.get('budget',16)):
            if state['archive_cursor']>=len(_slot_rows(m,'complex')):break
            _path_bind(m,state['archive_cursor']);state['archive_cursor']+=1
        return _path_report(m)
    raise ValueError('Unknown retained pathway operation')

_path_prior_replay=_slot_replay
def _slot_replay(m):
    result=_path_prior_replay(m);state=m.get('pathway_operations')
    if state is None:return result
    roles=_slot_rows(m,'roles')
    if state['rule']!='pathway_binding_experiment_v1' or sorted(state['candidates'].values())!=[r['id'] for r in roles if r.get('rule')==PATH_ROLE]:
        raise ValueError('Pathway registry disagrees with retained operations')
    if state['executions']!=[r['id'] for r in roles if r.get('rule')==PATH_EXEC] or state['comparisons']!=state['comparison_recipes']:
        raise ValueError('Lost pathway execution or comparison evidence')
    for key,rid in state['candidates'].items():
        if key!=str(len(roles[rid]['body']['operations'])):raise ValueError('Changed pathway registry binding')
    for reuse in state.get('reuses',[]):
        row=roles[reuse['execution_role']];event=m['events'][reuse['event']]
        if (row['rule']!=PATH_EXEC or row['parents']!=[reuse['operation_role']] or row['body']['input']!=reuse['input'] or
            row['body']['status']!='complete' or row['body']['relation']!='=' or reuse['zero_nexus']!='Z0' or
            event['domain']!='pathways' or event['operation']!='execute' or event['status']!='complete'):
            raise ValueError('Changed verified pathway reuse reference')
    for idx,row in enumerate(state['comparisons']):
        left,right=(roles[row[key]] for key in ('left_execution','right_execution'))
        if any(r.get('rule')!=PATH_EXEC or r['body']['status']!='complete' for r in (left,right)) or left['body']['input']!=right['body']['input']:
            raise ValueError('Pathway comparison has incompatible inputs')
        words=[roles[r['body']['answer_role']]['body']['evidence']['answer_slot']['word'] for r in (left,right)]
        event=m['events'][row['event']]
        if (row['id']!=idx or row['relation']!=('=' if words[0]==words[1] else '!=') or row['zero_nexus']!='Z0' or
            event['domain']!='pathways' or event['operation']!='compare' or event['status']!='complete'):
            raise ValueError('Changed pathway comparison or zero passage')
    return result

def _path_report(m):
    state=m.get('pathway_operations',{});roles=_slot_rows(m,'roles');items=[]
    for key,rid in state.get('candidates',{}).items():
        trials=[roles[x] for x in state['executions'] if roles[x]['parents']==[rid]]
        completed=[r for r in trials if r['body']['status']=='complete']
        inputs={tuple(_slot_rows(m,'complex')[r['body']['input']]['word']) for r in completed}
        items.append({'role':rid,'steps':len(roles[rid]['body']['operations']),'source_path':roles[rid]['body']['source_path'],
            'completed_trials':len(completed),'distinct_formal_inputs':len(inputs),
            'matching_replays':sum(r['body']['relation']=='=' for r in completed),
            'deferred_trials':len(trials)-len(completed),'status':'checked_on_multiple_inputs' if len(inputs)>=3 else 'candidate'})
    comparisons=state.get('comparisons',[])
    return {'scope':'unary i paths bound from actual archived constructions; declared i law retained; no general arithmetic law promotion',
        'operations':items,'equal_comparisons':sum(r['relation']=='=' for r in comparisons),
        'unequal_comparisons':sum(r['relation']=='!=' for r in comparisons),
        'verified_result_reuses':len(state.get('reuses',[])),
        'answer_feedback':'logical answers join the retained answer frontier; original paths remain archived'}

_path_prior_report=_slot_report
def _slot_report(m):
    report=_path_prior_report(m);report['pathway_operations']=_path_report(m);return report

_path_prior_query=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    if command=='pathways':print(json.dumps(_path_report(m),indent=2));return
    if command=='pathways unequal':
        print(json.dumps([r for r in m.get('pathway_operations',{}).get('comparisons',[]) if r['relation']=='!='],indent=2));return
    if command=='pathway-example':
        # Construct and observe an actual two-step path before binding it.
        first=_zi_build_arithmetic(m,'i',[1]);second=_zi_build_arithmetic(m,'i',[first]);rid=_path_bind(m,second)
        two=_zi_build_arithmetic(m,'add',[1,1])
        for input_id in (1,two):
            result=zero_core(m,'pathways',operation='execute',operands=(rid,input_id))
            if result['status']=='complete':
                answer=_slot_rows(m,'roles')[result['answer_role']]['body']['evidence']['answer_slot']
                print('roles:'+str(rid),'| input:',_slot_display(_slot_rows(m,'complex')[input_id]['word']),'| answer:',answer['value'],
                    '| replay:',result['relation'],'| execution roles:'+str(result['execution_role']))
            else:print(result)
        _slot_save(m,memory_path());_opportunity_export(m,memory_path());return
    result=_path_prior_query(m,text)
    if command in ('help','?'):print('pathways / pathway-example / pathways unequal: inspect or exercise retained pathway roles')
    return result

# Connected unary operation slots have an explicit binding: with zero in the
# context slot, the role acts on the powered right slot. Other arrangements
# stay experimental rather than silently discarding a value.
def _zstruct_check_role_ref(m,ref):
    if not isinstance(ref,dict) or set(ref)!={'archive','id'} or ref['archive']!='roles' or type(ref['id']) is not int:
        raise ValueError('Operation slot needs a typed retained role reference')
    rows=_slot_rows(m,'roles')
    if not 0<=ref['id']<len(rows) or rows[ref['id']].get('rule')!=PATH_ROLE:raise ValueError('Operation slot role is not executable')
    _path_role_check(m,rows[ref['id']]);return rows[ref['id']]

def _zstruct_path_call(ref,arg):return {'kind':'pathway_call','ref':_pr_copy.deepcopy(ref),'args':[_pr_copy.deepcopy(arg)]}
def _zstruct_check_path_node(m,node):
    if set(node)!={'kind','ref','args'} or not isinstance(node['args'],list) or len(node['args'])!=1:
        raise ValueError('Malformed unary pathway construction')
    _zstruct_check_role_ref(m,node['ref'])
def _zstruct_available_roles(m):
    return [item['role'] for item in _path_report(m)['operations'] if item['status']=='checked_on_multiple_inputs']

_connected_frame=_zi_frame
def _zi_frame(left,operation,right,power):
    frame=_connected_frame(left,operation,right,power)
    if isinstance(operation,dict):frame[1]={'kind':'operation','ref':_pr_copy.deepcopy(operation),'binding':'powered_right_with_zero_context'}
    return frame
_connected_frame_error=_zi_frame_error
def _zi_frame_error(m,frame):
    if isinstance(frame,list) and len(frame)==4 and isinstance(frame[1],dict) and 'ref' in frame[1]:
        slot=frame[1]
        if set(slot)!={'kind','ref','binding'} or slot['kind']!='operation' or slot['binding']!='powered_right_with_zero_context':return 'unary operation binding missing'
        try:_zstruct_check_role_ref(m,slot['ref'])
        except (ValueError,IndexError,KeyError) as exc:return str(exc)
        surrogate=_pr_copy.deepcopy(frame);surrogate[1]={'kind':'operation','symbol':'add'}
        error=_connected_frame_error(m,surrogate)
        if error:return error
        if _slot_rows(m,'complex')[frame[0]['ref']['id']]['word']!=[]:return 'unary operation requires retained zero context; other placements await interpretation'
        return None
    return _connected_frame_error(m,frame)
_connected_evaluate=_zi_evaluate
def _zi_evaluate(m,frame):
    if 'ref' not in frame[1]:return _connected_evaluate(m,frame)
    error=_zi_frame_error(m,frame)
    if error:raise ValueError(error)
    right=frame[2]['ref']['id'];power=frame[3]['ref']['id'];steps=[];accumulator=1;counter=0
    while counter<m['expressions'][power]['value']:
        accumulator=_zi_build_arithmetic(m,'multiply',[accumulator,right]);steps.append(accumulator);counter=_slot_S(m,counter)
    execution=zero_core(m,'pathways',operation='execute',operands=(frame[1]['ref']['id'],accumulator))
    if execution['status']!='complete':raise ValueError('Pathway slot '+execution['status'])
    row=_slot_rows(m,'roles')[execution['execution_role']]
    return {'result_id':row['body']['trace'][-1],'power_steps':steps,'power_counter':power,
        'operation_role':frame[1]['ref'],'path_execution_role':execution['execution_role']}
_connected_check=_zi_check_evaluation
def _zi_check_evaluation(m,frame,proof):
    if 'ref' not in frame[1]:return _connected_check(m,frame,proof)
    error=_zi_frame_error(m,frame)
    if error:raise ValueError(error)
    accumulator=1;records=_slot_rows(m,'complex');power=frame[3]['ref']['id']
    if proof['power_counter']!=power or len(proof['power_steps'])!=m['expressions'][power]['value']:raise ValueError('Unary slot power proof')
    for idx in proof['power_steps']:
        if records[idx]['operation']!='multiply' or records[idx]['parents']!=[accumulator,frame[2]['ref']['id']]:raise ValueError('Unary slot power path')
        accumulator=idx
    row=_slot_rows(m,'roles')[proof['path_execution_role']];_path_role_check(m,row)
    if (row['parents']!=[frame[1]['ref']['id']] or row['body']['input']!=accumulator or row['body']['status']!='complete' or
        proof['result_id']!=row['body']['trace'][-1] or proof['operation_role']!=frame[1]['ref']):raise ValueError('Unary slot execution proof')
    return records[proof['result_id']]['word']
_connected_from_frame=_z1_from_frame
def _z1_from_frame(frame):
    if 'ref' in frame[1]:return _zstruct_path_call(frame[1]['ref'],_z1_call('power',_z1_ref(frame[2]['ref']),_z1_ref(frame[3]['ref'])))
    return _connected_from_frame(frame)
_connected_eval=_z1_eval
def _z1_eval(m,tree):
    if tree['kind']!='pathway_call':return _connected_eval(m,tree)
    _zstruct_check_path_node(m,tree);result=zero_core(m,'Zi',operation='evaluate_expression',operands=(tree['args'][0],))
    if result['status']!='evaluated_formal':return result
    word=result['word']
    for op in _zstruct_check_role_ref(m,tree['ref'])['body']['operations']:
        word=zero_core(m,'roles',operation='execute_i',operands=(word,))['word']
    return {'status':'evaluated_formal','word':word}
_connected_expected=_z1_expected
def _z1_expected(m,tree):
    if tree['kind']!='pathway_call':return _connected_expected(m,tree)
    _zstruct_check_path_node(m,tree);result=_z1_expected(m,tree['args'][0])
    if result['status']!='evaluated_formal':return result
    count=len(_slot_rows(m,'roles')[tree['ref']['id']]['body']['operations'])
    return {'status':'evaluated_formal','word':[degree+count for degree in result['word']]}
_connected_text=_z1_text
def _z1_text(m,tree):
    if tree['kind']=='pathway_call':return 'roles:'+str(tree['ref']['id'])+'('+_z1_text(m,tree['args'][0])+')'
    return _connected_text(m,tree)
_connected_service=_zi_service
def _zi_service(m):
    result=_connected_service(m);available=_zstruct_available_roles(m)
    if available:
        state=_zi_state(m);cursor=state.get('pathway_frame_cursor',0);rid=available[cursor%len(available)]
        # Real and imaginary inputs are retained separately; new frame records
        # are not merged even when their numerical answers agree.
        inputs=[1,2];input_id=inputs[(cursor//len(available))%len(inputs)]
        frame=_zi_frame(0,_slot_ref('roles',rid),input_id,1);state['frames'].append(frame)
        zero_core(m,'Zi',operation='attempt',operands=(frame,[0,1,2,3]));state['pathway_frame_cursor']=cursor+1
    return _zi_report(m)

# Four observed clocks per gateway passage, including open passages captured
# by a checkpoint. Missing timestamps are recovered only from retained copies.
import uuid as _zstruct_uuid
_ZSTRUCT_SESSION=_zstruct_uuid.uuid4().hex
def _zstruct_stamps():return {'wall_ns':time.time_ns(),'monotonic_ns':time.monotonic_ns(),
    'performance_ns':time.perf_counter_ns(),'process_ns':time.process_time_ns()}
_connected_core=zero_core
def zero_core(memory,domain,*,operation=None,operands=(),**kwargs):
    if not isinstance(memory,dict) or memory.get('experiment')!=SLOT_RULE:
        return _connected_core(memory,domain,operation=operation,operands=operands,**kwargs)
    state=memory.setdefault('zero_clock_archive',{'rule':'four_clock_gateway_receipts_v1','records':{},'recipes':{}})
    idx=len(memory['events']);key=str(idx);event={'id':idx,'domain':domain,'operation':operation,'zero_nexus':'Z0',
        'parent':memory.get('_active_event'),'status':'running'}
    memory.setdefault('zero_clock_origin',idx)
    if operation=='S':event['before']=operands[0]
    row={'event':idx,'session':_ZSTRUCT_SESSION,'start':_zstruct_stamps(),'end':None,'event_recipe':event,'zero_nexus':'Z0'}
    state['records'][key]=row;state['recipes'][key]=_pr_copy.deepcopy(row)
    try:return _connected_core(memory,domain,operation=operation,operands=operands,**kwargs)
    finally:
        row['end']=_zstruct_stamps();row['event_recipe']=_pr_copy.deepcopy(memory['events'][idx])
        state['recipes'][key]=_pr_copy.deepcopy(row)

def _zstruct_recover_extensions(m):
    changed=False
    for field,recipes in (('frames',m.get('zero_frame_recipes',{})),('runs',m.get('zero_run_recipes',{}))):
        if not recipes:continue
        rows=m.setdefault('Zi',{}).setdefault('frames',[]) if field=='frames' else m['runs']
        # Lists can be rebuilt exactly from the saved indexed copies. Reject
        # changed payloads; only absent entries are reconstruction candidates.
        if rows==[recipes[str(i)] for i in range(len(recipes))]:continue
        expected=[recipes[str(i)] for i in range(len(recipes))]
        cursor=0
        for row in rows:
            while cursor<len(expected) and expected[cursor]!=row:cursor+=1
            if cursor==len(expected):raise ValueError('Changed '+field+' metadata; source preserved')
            cursor+=1
        rows[:]=_pr_copy.deepcopy(expected);changed=True
    zi=m.get('Zi',{})
    if 'attempt_recipes' in zi:
        by_id={row['id']:row for row in zi.get('attempts',[])};restored=[]
        for recipe in zi['attempt_recipes']:
            row=by_id.pop(recipe['id'],None)
            if row is None:restored.append(_pr_copy.deepcopy(recipe));changed=True
            elif row!=recipe:raise ValueError('Changed slot attempt; source preserved')
            else:restored.append(row)
        if by_id:raise ValueError('Untracked slot attempt')
        zi['attempts']=restored
    for name in ('zero_clock_archive','zero_structures'):
        state=m.get(name)
        if state is None:continue
        if name=='zero_clock_archive':
            def retained_subset(actual,recipe):
                if isinstance(actual,dict) and isinstance(recipe,dict):
                    return all(key in recipe and retained_subset(value,recipe[key]) for key,value in actual.items())
                return actual==recipe
            for key,recipe in state['recipes'].items():
                if key not in state['records']:state['records'][key]=_pr_copy.deepcopy(recipe);changed=True
                elif state['records'][key]!=recipe:
                    if retained_subset(state['records'][key],recipe):state['records'][key]=_pr_copy.deepcopy(recipe);changed=True
                    else:raise ValueError('Changed clock evidence; source preserved')
            events={e['id']:e for e in m['events']}
            for row in state['recipes'].values():
                event=row['event_recipe'];idx=event['id']
                if idx not in events:events[idx]=_pr_copy.deepcopy(event);changed=True
                elif events[idx]!=event:raise ValueError('Changed clock-linked gateway event; source preserved')
            if sorted(events)!=list(range(len(events))):raise ValueError('Missing older gateway event without retained clock evidence; source preserved')
            m['events']=[events[i] for i in range(len(events))]
        else:
            for field,recipe_field in (('records','recipes'),('checks','check_recipes'),('work','work_recipes')):
                rows=state[field];by_id={row['id']:row for row in rows};recipes=state[recipe_field]
                if len(by_id)!=len(rows):raise ValueError('Duplicate 0 structure identity')
                restored=[]
                for recipe in recipes:
                    old=by_id.pop(recipe['id'],None)
                    if old is None:restored.append(_pr_copy.deepcopy(recipe));changed=True
                    elif old!=recipe:raise ValueError('Changed 0 structure evidence; source preserved')
                    else:restored.append(old)
                if by_id:raise ValueError('Untracked 0 structure evidence')
                state[field]=restored
    return changed

def _zstruct_clock_check(m):
    state=m.get('zero_clock_archive')
    if state is None:return
    if state['records']!=state['recipes']:raise ValueError('Clock archive evidence conflict')
    origin=m.get('zero_clock_origin')
    if type(origin) is not int or not 0<=origin<=len(m['events']) or any(str(idx) not in state['records'] for idx in range(origin,len(m['events']))):
        raise ValueError('Missing four-clock gateway coverage')
    for key,row in state['records'].items():
        if key!=str(row['event']) or row['event_recipe']!=m['events'][row['event']] or row['zero_nexus']!='Z0':raise ValueError('Clock event reference changed')
        if (row['end'] is None)!=(row['event_recipe']['status']=='running'):raise ValueError('Missing clock completion evidence')
        for stamp in (row['start'],row['end']):
            if stamp is not None and (set(stamp)!={'wall_ns','monotonic_ns','performance_ns','process_ns'} or any(type(v) is not int or v<0 for v in stamp.values())):raise ValueError('Invalid observed clock stamp')
        if row['end'] is not None and any(row['end'][clock]<row['start'][clock] for clock in ('monotonic_ns','performance_ns','process_ns')):
            raise ValueError('Clock interval reversed within its session')

# Unique temporary files avoid collisions between writers. Validate a complete
# JSON document before publishing it; a failed write leaves the old path intact.
def _ze_atomic_json(path,data):
    import tempfile
    directory=os.path.dirname(os.path.abspath(path));os.makedirs(directory,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix='.'+os.path.basename(path)+'.',suffix='.tmp',dir=directory)
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as handle:
            json.dump(data,handle,indent=2,ensure_ascii=False);handle.flush();os.fsync(handle.fileno())
        with open(tmp,encoding='utf-8') as handle:json.load(handle)
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)

# 0 structures store constructed syntax, including unsupported mathematics.
# The generator is bounded and persistent; it does not enumerate all possible
# mathematics at once. Calculus verification is a separately declared checker.
def _zstruct_state(m):
    return m.setdefault('zero_structures',{'rule':'retained_zero_structures_v1','records':[],'recipes':[],
        'checks':[],'check_recipes':[],'work':[],'work_recipes':[],'work_done':[],
        'index':{},'scan':{'role':0,'Zi':0,'reserved':0,'comparison':0}})

def _zstruct_snapshot(m,source):
    kind=source['kind'];idx=source.get('id')
    if kind=='role':
        body=_slot_rows(m,'roles')[idx]['body']
        return {'kind':'expression','tree':_pr_copy.deepcopy(body['expression']),
            'optional_slots':_pr_copy.deepcopy(body.get('optional_slots',[])),
            'source_outcome':body['evaluation']['status']}
    if kind=='Zi':return {'kind':'slot_frame_attempt','attempt':_pr_copy.deepcopy(m['Zi']['attempts'][idx])}
    if kind=='reserved':return {'kind':'resource_deferred','proposal':_pr_copy.deepcopy(m['opportunity_proposals']['records'][idx])}
    if kind=='comparison':return {'kind':'pathway_comparison','comparison':_pr_copy.deepcopy(m['pathway_operations']['comparisons'][idx])}
    if kind=='generated':return _zstruct_variants(m,source['parent'])[source['variant']]
    raise ValueError('Unknown 0 structure source')

def _zstruct_work(m,sid,action,cursor=0):
    state=_zstruct_state(m);row={'id':len(state['work']),'structure':sid,'action':action,'cursor':cursor,'zero_nexus':'Z0'}
    state['work'].append(row);state['work_recipes'].append(_pr_copy.deepcopy(row));return row['id']

def _zstruct_record(m,source,parent=None):
    state=_zstruct_state(m);key=json.dumps(source,sort_keys=True)
    if key in state['index']:return state['index'][key]
    payload=_zstruct_snapshot(m,source);sid=len(state['records'])
    if parent is not None and not 0<=parent<sid:raise ValueError('0 structure parent must already be retained')
    depth=0 if parent is None else state['records'][parent]['generation_depth']+1
    labels=['0 structures']
    if payload['kind'] in ('derivative_relation','experimental_calculus_shape','typed_physical_derivative'):labels.append('0 calculus')
    row={'id':sid,'source':_pr_copy.deepcopy(source),'parent':parent,'payload':payload,'labels':labels,
        'status':'experimental','generation_depth':depth,'zero_nexus':'Z0','retention_event':m['_active_event']}
    state['records'].append(row);state['recipes'].append(_pr_copy.deepcopy(row));state['index'][key]=sid
    _zstruct_work(m,sid,'check')
    if depth<2 and payload['kind'] in ('expression','derivative_relation'):_zstruct_work(m,sid,'expand')
    m['feedback'].append({'source':{'constructor':'0 structure','id':sid},
        'targets':['experimental_structure_observer','persistent_structure_work'],'zero_nexus':'Z0','status':'experimental'})
    return sid

def _zstruct_variants(m,sid):
    row=_zstruct_state(m)['records'][sid];payload=row['payload'];x={'kind':'variable','name':'x'}
    constants=[{'kind':'constant','value':0},{'kind':'constant','value':1},x,{'kind':'call','operation':'add','args':[x,x]}]
    result=[]
    if payload['kind']=='expression':
        tree=payload['tree']
        # Every leaf position is a separate placement candidate. Positions
        # with the same value retain separate paths and source identities.
        for path,node in _z1_walk(tree):
            if node['kind']!='reference':continue
            function=_z1_replace(tree,list(path),x)
            for proposed in constants:
                result.append({'kind':'derivative_relation','variable':'x','function':function,
                    'candidate':_pr_copy.deepcopy(proposed),'placement':list(path)})
        for shape in ('rate','accumulation','refinement','integral'):
            result.append({'kind':'experimental_calculus_shape','shape':shape,'variable':'x',
                'source_expression':_pr_copy.deepcopy(tree),'interpretation':'not_established'})
    elif payload['kind']=='derivative_relation':
        for proposed in constants:
            item=_pr_copy.deepcopy(payload);item['candidate']=_pr_copy.deepcopy(proposed);result.append(item)
    return result

class _ZeroStructureUnsupported(Exception):pass
def _zstruct_poly(m,node):
    def trim(p):
        p={degree:c for degree,c in p.items() if c}
        if any(degree>_principles_limit('degree',8) or abs(c)>_principles_limit('coefficient',4096) for degree,c in p.items()):raise _ZeroStructureUnsupported('polynomial certificate budget')
        return p
    def add(a,b):
        result=dict(a)
        for k,v in b.items():result[k]=result.get(k,0)+v
        return trim(result)
    def multiply(a,b):
        result={}
        for ka,va in a.items():
            for kb,vb in b.items():result[ka+kb]=result.get(ka+kb,0)+va*vb
        return trim(result)
    kind=node.get('kind')
    if kind=='variable':
        if node.get('name')!='x':raise _ZeroStructureUnsupported('unbound variable')
        return {1:1}
    if kind=='constant':
        value=node.get('value')
        if type(value) is not int:raise _ZeroStructureUnsupported('nonintegral constant')
        return trim({0:value})
    if kind=='reference':
        ref=node['ref']
        if ref['archive']=='rational':return trim({0:m['expressions'][ref['id']]['value']})
        if ref['archive']!='complex':raise _ZeroStructureUnsupported('reference has no polynomial interpretation')
        word=_slot_rows(m,'complex')[ref['id']]['word']
        if any(degree%4 in (1,3) for degree in word):raise _ZeroStructureUnsupported('imaginary coefficient checker not supplied')
        return trim({0:sum(1 if degree%4==0 else -1 for degree in word)})
    if kind=='pathway_call':
        role=_zstruct_check_role_ref(m,node['ref']);turns=len(role['body']['operations'])%4
        if turns in (1,3):raise _ZeroStructureUnsupported('imaginary polynomial transform not supplied')
        value=_zstruct_poly(m,node['args'][0]);return value if turns==0 else {k:-v for k,v in value.items()}
    if kind!='call' or len(node.get('args',[]))!=2:raise _ZeroStructureUnsupported('structure has no polynomial interpretation')
    a,b=(_zstruct_poly(m,n) for n in node['args']);op=node['operation']
    if op=='add':return add(a,b)
    if op=='multiply':return multiply(a,b)
    if op=='power':
        if any(k!=0 for k in b) or not 0<=b.get(0,0)<=_principles_limit('power',6):raise _ZeroStructureUnsupported('power outside finite polynomial checker')
        result={0:1}
        for unused in range(b.get(0,0)):result=multiply(result,a)
        return result
    raise _ZeroStructureUnsupported('operation is not interpreted by polynomial checker')

def _zstruct_certificate(m,payload):
    if payload.get('kind')!='derivative_relation':return {'outcome':'unresolved','reason':'no verifier for this structure kind'}
    if payload.get('variable')!='x':return {'outcome':'unresolved','reason':'variable not bound'}
    try:function=_zstruct_poly(m,payload['function']);candidate=_zstruct_poly(m,payload['candidate'])
    except _ZeroStructureUnsupported as exc:return {'outcome':'unresolved','reason':str(exc)}
    # Explicit exact verifier, not a numerical constructor. Expand
    # (F(x+h)-F(x))/h as a finite polynomial; h-positive terms tend to zero.
    from math import comb
    quotient={}
    for degree,coefficient in function.items():
        for j in range(1,degree+1):quotient[str(degree-j)+','+str(j-1)]=coefficient*comb(degree,j)
    limit={int(key.split(',')[0]):value for key,value in quotient.items() if key.endswith(',0') and value}
    encode=lambda p:{str(k):v for k,v in sorted(p.items())}
    return {'outcome':'verified' if candidate==limit else 'nonmatching',
        'validator':'explicit_finite_polynomial_difference_quotient_v1','assumptions':['real variable x','finite polynomial','h tends to zero','retained coefficients interpreted under the declared i law'],
        'function_coefficients':encode(function),'candidate_coefficients':encode(candidate),
        'difference_quotient_coefficients_x_h':quotient,'limit_coefficients':encode(limit),
        'justification':'finite polynomial; positive powers of h tend to zero'}

def _zstruct_payload_refs(payload):
    refs=[]
    def walk(value):
        if isinstance(value,dict):
            if 'ref' in value and value['ref'] not in refs:refs.append(_pr_copy.deepcopy(value['ref']))
            for child in value.values():walk(child)
        elif isinstance(value,list):
            for child in value:walk(child)
    walk(payload);return refs

def _zstruct_check(m,sid):
    state=_zstruct_state(m);structure=state['records'][sid];proof=_zstruct_certificate(m,structure['payload'])
    row={'id':len(state['checks']),'execution_policy':_principles_current(),'structure':sid,'proof':proof,'zero_nexus':'Z0','event':m['_active_event']}
    state['checks'].append(row);state['check_recipes'].append(_pr_copy.deepcopy(row))
    if proof['outcome']=='verified' and not any(r.get('zero_structure')==sid for r in _slot_rows(m,'calculus')):
        record={'kind':'verified_derivative_identity','operation':'verified_polynomial_derivative',
            'parents':[],'sources':_zstruct_payload_refs(structure['payload']),'zero_structure':sid,
            'check':row['id'],'expression':_pr_copy.deepcopy(structure['payload']),'certificate':_pr_copy.deepcopy(proof),
            'classification':['calculus','0 calculus','0 structures']}
        zero_core(m,'calculus',operation='record',record=record)
    m['feedback'].append({'source':{'constructor':'0 structure check','id':row['id']},
        'targets':['experimental_structure_history','calculus_evidence_index'],'zero_nexus':'Z0','status':proof['outcome']})
    return row['id']

def _zstruct_calculus_check(m,row):
    structure=_zstruct_state(m)['records'][row['zero_structure']];proof=_zstruct_certificate(m,structure['payload'])
    check=_zstruct_state(m)['checks'][row['check']]
    if (proof['outcome']!='verified' or proof!=row['certificate'] or row['expression']!=structure['payload'] or
        check['structure']!=structure['id'] or check['proof']!=proof or row['sources']!=_zstruct_payload_refs(structure['payload']) or
        row['classification']!=['calculus','0 calculus','0 structures']):raise ValueError('Unverified calculus classification or lost 0 structure history')

def _zstruct_service(m,budget=4):
    state=_zstruct_state(m)
    for kind,rows in (('role',_slot_rows(m,'roles')),('Zi',m.get('Zi',{}).get('attempts',[])),
                      ('reserved',m.get('opportunity_proposals',{}).get('records',[])),
                      ('comparison',m.get('pathway_operations',{}).get('comparisons',[]))):
        cursor=state['scan'][kind];limit=min(len(rows),cursor+8)
        while cursor<limit:
            if kind!='role' or rows[cursor].get('rule')==Z1I_ROLE_RULE:
                zero_core(m,'0-structures',operation='record',operands=({'kind':kind,'id':cursor},))
            cursor+=1
        state['scan'][kind]=cursor
    completed=set(state['work_done']);count=0;lanes=('calculus','expand','observe')
    def lane(task):
        if task['action']=='expand':return 'expand'
        return 'calculus' if state['records'][task['structure']]['payload']['kind']=='derivative_relation' else 'observe'
    while count<budget:
        task=None
        for unused in lanes:
            cursor=state.get('lane_cursor',0);wanted=lanes[cursor];state['lane_cursor']=(cursor+1)%len(lanes)
            task=next((row for row in state['work'] if row['id'] not in completed and lane(row)==wanted),None)
            if task is not None:break
        if task is None:break
        sid=task['structure']
        if task['action']=='check':zero_core(m,'0-structures',operation='check',operands=(sid,))
        else:
            variants=_zstruct_variants(m,sid);cursor=task['cursor']
            if cursor<len(variants):
                zero_core(m,'0-structures',operation='record',operands=({'kind':'generated','parent':sid,'variant':cursor},sid))
                if cursor+1<len(variants):_zstruct_work(m,sid,'expand',cursor+1)
        state['work_done'].append(task['id']);completed.add(task['id']);count+=1
    return _zstruct_report(m)

_structures_dispatch=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='0-structures':
        if operation=='record':return _zstruct_record(m,*operands)
        if operation=='check':return _zstruct_check(m,*operands)
        if operation=='service':return _zstruct_service(m,**kwargs)
        if operation=='capture_metadata':
            for key,rows in (('zero_frame_recipes',m.get('Zi',{}).get('frames',[])),('zero_run_recipes',m['runs'])):
                recipes=m.setdefault(key,{})
                for idx,row in enumerate(rows):recipes[str(idx)]=_pr_copy.deepcopy(row)
            return True
        raise ValueError('Unknown 0 structure operation')
    result=_structures_dispatch(m,domain,operation,operands,kwargs)
    if domain=='opportunities' and operation=='retain_deferred':
        zero_core(m,'0-structures',operation='record',operands=({'kind':'reserved','id':result},))
    if domain=='pathways' and operation=='compare':
        zero_core(m,'0-structures',operation='record',operands=({'kind':'comparison','id':result},))
    return result

_structures_emit=_z1_emit
def _z1_emit(m,*args,**kwargs):
    rid=_structures_emit(m,*args,**kwargs)
    zero_core(m,'0-structures',operation='record',operands=({'kind':'role','id':rid},));return rid
_structures_attempt=_zi_attempt
def _zi_attempt(m,*args,**kwargs):
    result=_structures_attempt(m,*args,**kwargs)
    zero_core(m,'0-structures',operation='record',operands=({'kind':'Zi','id':result['id']},));return result

_structures_replay=_slot_replay
def _slot_replay(m):
    result=_structures_replay(m);_zstruct_clock_check(m);state=m.get('zero_structures')
    for field,rows in (('zero_frame_recipes',m.get('Zi',{}).get('frames',[])),('zero_run_recipes',m['runs'])):
        for key,recipe in m.get(field,{}).items():
            if not 0<=int(key)<len(rows) or rows[int(key)]!=recipe:raise ValueError('Clock/run/frame checkpoint evidence changed')
    if state is None:return result
    if state['rule']!='retained_zero_structures_v1':raise ValueError('Unknown 0 structure schema')
    for field,recipes in (('records','recipes'),('checks','check_recipes'),('work','work_recipes')):
        if state[field]!=state[recipes]:raise ValueError('0 structure recipe conflict')
        if [r['id'] for r in state[field]]!=list(range(len(state[field]))):raise ValueError('0 structure identity lost')
    expected_index={}
    for row in state['records']:
        key=json.dumps(row['source'],sort_keys=True);expected_index[key]=row['id']
        if (row['payload']!=_zstruct_snapshot(m,row['source']) or row['status']!='experimental' or
            row['zero_nexus']!='Z0' or (row['parent'] is not None and not 0<=row['parent']<row['id'])):
            raise ValueError('0 structure lost its source, placement or experimental history')
        expected_labels=['0 structures']+(['0 calculus'] if row['payload']['kind'] in ('derivative_relation','experimental_calculus_shape','typed_physical_derivative') else [])
        depth=0 if row['parent'] is None else state['records'][row['parent']]['generation_depth']+1
        if row['labels']!=expected_labels or row['generation_depth']!=depth or (row['source']['kind']=='generated' and row['source']['parent']!=row['parent']):
            raise ValueError('0 structure classification or ancestry changed')
        event=m['events'][row['retention_event']]
        if event['domain']!='0-structures' or event['operation']!='record' or event['status']!='complete':raise ValueError('0 structure missing gateway evidence')
    if state['index']!=expected_index:raise ValueError('0 structure index mismatch')
    for row in state['checks']:
        event=m['events'][row['event']]
        if (row['proof']!=_principles_check_certificate(m,row) or
            event['domain']!='0-structures' or event['operation']!='check' or event['status']!='complete'):
            raise ValueError('0 calculus check or its clock-linked event changed')
    if len(set(state['work_done']))!=len(state['work_done']) or any(not 0<=idx<len(state['work']) for idx in state['work_done']):raise ValueError('0 structure work queue changed')
    return result

_structures_save=_slot_save
def _slot_save(m,path):
    zero_core(m,'0-structures',operation='capture_metadata')
    return _structures_save(m,path)

def _zstruct_report(m):
    state=m.get('zero_structures',{});checks=state.get('checks',[]);facts=_slot_rows(m,'calculus');lineage=[]
    for fact in facts:
        sid=fact['zero_structure'];ancestors=[];current=state['records'][sid]['parent']
        while current is not None:ancestors.append(current);current=state['records'][current]['parent']
        lineage.append({'calculus_record':fact['id'],'zero_structure':sid,'experimental_ancestors':ancestors})
    clocks=m.get('zero_clock_archive',{}).get('records',{})
    return {'retained_0_structures':len(state.get('records',[])),
        '0_calculus_candidates':sum('0 calculus' in r['labels'] for r in state.get('records',[])),
        'nonmatching_checks_retained':sum(r['proof']['outcome']=='nonmatching' for r in checks),
        'unresolved_checks_retained':sum(r['proof']['outcome']=='unresolved' for r in checks),
        'verified_calculus_records':len(facts),'dual_classification_links':lineage,
        'pending_structure_work':len(state.get('work',[]))-len(state.get('work_done',[])),
        'clock_receipts':len(clocks),'clock_sessions':len({r['session'] for r in clocks.values()}),
        'scope':'bounded constructed candidates; no exhaustive enumeration; explicit polynomial derivative verifier; experimental history retained'}

_structures_report=_slot_report
def _slot_report(m):
    report=_structures_report(m);report['zero_structures']=_zstruct_report(m)
    report['deferred']=[s for s in report['deferred'] if s!='calculus']+['general calculus beyond the supplied polynomial verifier']
    report['scope']='Connected retained roles, experimental 0 structures, four-clock receipts, and explicitly verified polynomial derivative identities; general engine reduction remains incomplete.'
    return report
_structures_opportunity_report=_opportunity_report
def _opportunity_report(m):
    report=_structures_opportunity_report(m);facts=_slot_rows(m,'calculus')
    report['calculus'].update(status='verified_polynomial_cases' if facts else 'not_established',numeric_branch_records=len(facts),
        note='Only explicitly checked finite polynomial derivative identities enter calculus. Every experimental source remains in 0 structures / 0 calculus.')
    return report
_structures_query=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    if command in ('0-structures','0-calculus','calculus','zero-clock'):
        print(json.dumps(_zstruct_report(m),indent=2))
        if command=='zero-clock':
            rows=m.get('zero_clock_archive',{}).get('records',{})
            if rows:print(json.dumps(rows[max(rows,key=int)],indent=2))
        if command=='calculus':print(json.dumps(_slot_rows(m,'calculus'),indent=2))
        return
    if command.startswith('0-structure '):
        try:idx=int(command.split()[1]);print(json.dumps(_zstruct_state(m)['records'][idx],indent=2))
        except (ValueError,IndexError):print('Use 0-structure N with a retained structure ID.')
        return
    if command.startswith('0-retry '):
        idx=int(command.split()[1]);_zstruct_state(m)['records'][idx];_zstruct_work(m,idx,'check');_slot_save(m,memory_path());print('Retained structure queued for another check:',idx);return
    result=_structures_query(m,text)
    if command in ('help','?'):print('0-structures / 0-calculus / calculus / zero-clock / 0-structure N / 0-retry N')
    return result

# Open-ended structural exploration: finite work per run, no terminal generation depth.
# This grammar supplies syntax, not new arithmetic/calculus axioms.
OPEN_RULE='zero_open_structural_frontier_v1'
OPEN_BINARY=('add','multiply','power','substitute_x','apply_role','derivative_relation')
OPEN_UNARY=('formal_derivative','left_child','right_child')

def _open_state(m):
    return m.setdefault('open_exploration',{'rule':OPEN_RULE,'records':[],'recipes':[]})

def _open_ref(idx):return {'kind':'open_reference','id':idx}

def _open_cursor_next(cursor):
    shell,position=cursor;position+=1
    total=len(OPEN_UNARY)+len(OPEN_BINARY)*(2*shell+1)
    return [shell+1,0] if position==total else [shell,position]

def _open_cursor_recipe(cursor):
    shell,position=cursor
    if position<len(OPEN_UNARY):return OPEN_UNARY[position],[shell]
    position-=len(OPEN_UNARY);pair,op=divmod(position,len(OPEN_BINARY))
    parents=[shell,pair] if pair<=shell else [pair-shell-1,shell]
    return OPEN_BINARY[op],parents

def _open_tree(m,idx):
    row=_open_state(m)['records'][idx];op=row['operation'];parents=row['parents']
    args=[_open_ref(p) for p in parents]
    if op=='seed_zero':return {'kind':'reference','ref':{'archive':'rational','id':0}}
    if op=='seed_one':return {'kind':'reference','ref':{'archive':'rational','id':1}}
    if op=='variable':return {'kind':'variable','name':'x'}
    if op=='import_structure':
        source=_zstruct_state(m)['records'][row['source']['id']]['payload']
        return _pr_copy.deepcopy(source.get('tree',source))
    if op=='import_calculus_result':
        return _pr_copy.deepcopy(_slot_rows(m,'calculus')[row['source']['id']]['expression']['candidate'])
    if op=='import_role':return {'kind':'operation_role','ref':{'archive':'roles','id':row['source']['id']}}
    if op in ('add','multiply','power'):return {'kind':'call','operation':op,'args':args}
    if op in ('left_child','right_child'):
        source=_open_state(m)['records'][parents[0]]
        if source['parents']:
            return _open_ref(source['parents'][0 if op=='left_child' else -1])
        return {'kind':'unresolved_projection','operation':op,'args':args}
    if op=='apply_role':
        role=_open_state(m)['records'][parents[0]]
        if role['operation']=='import_role':return _zstruct_path_call({'archive':'roles','id':role['source']['id']},args[1])
        return {'kind':'unresolved_role_application','args':args}
    if op=='derivative_relation':return {'kind':'derivative_relation','variable':'x','function':args[0],'candidate':args[1]}
    if op=='formal_derivative':return {'kind':'formal_derivative','variable':'x','args':args}
    if op=='substitute_x':return {'kind':'substitution','variable':'x','args':args}
    raise ValueError('Unknown open structural role')

def _open_payload(m,idx):
    row=_open_state(m)['records'][idx]
    if row['operation']=='derivative_relation':return _open_tree(m,idx)
    return {'kind':'expression','tree':_open_ref(idx),'source_outcome':'experimental'}

def _open_record(m,operation,parents=(),source=None,cursor=None):
    state=_open_state(m);idx=len(state['records'])
    if any(type(p)is not int or not 0<=p<idx for p in parents):raise ValueError('Open parents must already be retained')
    row={'id':idx,'operation':operation,'parents':list(parents),'source':source,'cursor':cursor,
         'zero_nexus':'Z0','event':m['_active_event'],'status':'experimental'}
    state['records'].append(row);state['recipes'].append(_pr_copy.deepcopy(row))
    sid=zero_core(m,'0-structures',operation='record',operands=({'kind':'open','id':idx},))
    # Check every generated proposal once; failures and unsupported syntax remain archived.
    zero_core(m,'0-structures',operation='check',operands=(sid,))
    return idx

def _open_service(m,budget=12):
    if type(budget)is not int or not 0<=budget<=1000:raise ValueError('Use a work budget from 0 to 1000')
    state=_open_state(m)
    if not state['records']:
        for op in ('seed_zero','seed_one','variable'):
            zero_core(m,'0-structures',operation='open_record',operation_name=op)
    # A fixed amount of import work and a separate expansion budget prevent new
    # incoming material from starving the persistent diagonal composition frontier.
    imported={(r['operation'],r['source']['id']) for r in state['records'] if r['source'] is not None}
    lanes=[('import_structure',[r['id'] for r in _zstruct_state(m)['records'] if r['source']['kind']!='open']),
           ('import_role',[r['id'] for r in _slot_rows(m,'roles') if r.get('rule')==PATH_ROLE]),
           ('import_calculus_result',[r['id'] for r in _slot_rows(m,'calculus')])]
    for unused in range(4):
        selected=None
        for offset in range(len(lanes)):
            op,ids=lanes[(len(imported)+offset)%len(lanes)]
            idx=next((idx for idx in ids if (op,idx) not in imported),None)
            if idx is not None:selected=(op,idx);break
        if selected is None:break
        op,idx=selected
        zero_core(m,'0-structures',operation='open_record',operation_name=op,source={'id':idx})
        imported.add((op,idx))
    scheduled=[r for r in state['records'] if r['cursor'] is not None]
    cursor=_open_cursor_next(scheduled[-1]['cursor']) if scheduled else [0,0]
    for unused in range(budget):
        op,parents=_open_cursor_recipe(cursor)
        if max(parents)>=len(state['records']):break
        zero_core(m,'0-structures',operation='open_record',operation_name=op,parents=parents,cursor=cursor)
        cursor=_open_cursor_next(cursor)
    return _open_report(m)

_open_snapshot_previous=_zstruct_snapshot
def _zstruct_snapshot(m,source):
    if source['kind']=='open':return _open_payload(m,source['id'])
    return _open_snapshot_previous(m,source)

# Do not send new open nodes back into the former four-answer/two-level creator.
# The old jobs remain retained and serviceable for checkpoint compatibility.
_open_work_previous=_zstruct_work
def _zstruct_work(m,sid,action,cursor=0):
    if _zstruct_state(m)['records'][sid]['source']['kind']=='open':return None
    return _open_work_previous(m,sid,action,cursor)

_open_poly_previous=_zstruct_poly
def _zstruct_poly(m,node):
    outer='_open_check_remaining' not in m
    if outer:m['_open_check_remaining']=_principles_limit('interpretation',256)
    try:
        m['_open_check_remaining']-=1
        if m['_open_check_remaining']<0:raise _ZeroStructureUnsupported('interpretation work budget; structure retained')
        if node.get('kind')=='open_reference':return _zstruct_poly(m,_open_tree(m,node['id']))
        if node.get('kind')=='substitution':
            # Polynomial composition evaluates a retained substitution without
            # mutating or expanding its DAG into an exponentially large tree.
            a,b=(_zstruct_poly(m,n) for n in node['args']);result={}
            for degree,coefficient in a.items():
                term={0:coefficient}
                for unused in range(degree):
                    product={}
                    for ka,va in term.items():
                        for kb,vb in b.items():product[ka+kb]=product.get(ka+kb,0)+va*vb
                    if any(k>_principles_limit('degree',8) or abs(v)>_principles_limit('coefficient',4096) for k,v in product.items()):raise _ZeroStructureUnsupported('polynomial certificate budget')
                    term=product
                for k,v in term.items():result[k]=result.get(k,0)+v
            if any(k>_principles_limit('degree',8) or abs(v)>_principles_limit('coefficient',4096) for k,v in result.items()):raise _ZeroStructureUnsupported('polynomial certificate budget')
            return {k:v for k,v in result.items() if v}
        return _open_poly_previous(m,node)
    finally:
        if outer:m.pop('_open_check_remaining',None)

_open_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='0-structures' and operation=='open_record':
        options=dict(kwargs);op=options.pop('operation_name');return _open_record(m,op,**options)
    if domain=='0-structures' and operation=='open_service':return _open_service(m,**kwargs)
    return _open_dispatch_previous(m,domain,operation,operands,kwargs)

_open_recover_previous=_zstruct_recover_extensions
def _zstruct_recover_extensions(m):
    changed=False;state=m.get('open_exploration')
    if state is not None:
        actual={r['id']:r for r in state['records']}
        if len(actual)!=len(state['records']):raise ValueError('Duplicate open node')
        restored=[]
        for recipe in state['recipes']:
            row=actual.pop(recipe['id'],None)
            if row is None:row=_pr_copy.deepcopy(recipe);changed=True
            elif row!=recipe:raise ValueError('Changed open structure; source preserved')
            restored.append(row)
        if actual:raise ValueError('Untracked open node')
        state['records']=restored
    return _open_recover_previous(m) or changed

_open_replay_previous=_slot_replay
def _slot_replay(m):
    state=m.get('open_exploration')
    if state is not None:
        if state['rule']!=OPEN_RULE or state['records']!=state['recipes']:raise ValueError('Open recipe conflict')
        cursor=[0,0]
        for idx,row in enumerate(state['records']):
            if row['id']!=idx or row['status']!='experimental' or row['zero_nexus']!='Z0':raise ValueError('Open identity changed')
            if any(type(p)is not int or not 0<=p<idx for p in row['parents']):raise ValueError('Open ancestry changed')
            if idx<3 and row['operation']!=('seed_zero','seed_one','variable')[idx]:raise ValueError('Open seed changed')
            if row['cursor'] is not None:
                op,parents=_open_cursor_recipe(cursor)
                if row['cursor']!=cursor or row['operation']!=op or row['parents']!=parents:raise ValueError('Open frontier changed')
                cursor=_open_cursor_next(cursor)
            elif idx>=3:
                if row['operation'] not in ('import_structure','import_role','import_calculus_result','import_symbolic','import_quantity','import_physical','import_physical_reassessment','import_math','import_open_math_syntax','import_principles_assessment') or row['parents'] or row['source'] is None:raise ValueError('Untracked open import')
            event=m['events'][row['event']]
            if event['domain']!='0-structures' or event['operation']!='open_record' or event['status']!='complete':raise ValueError('Open gateway evidence lost')
            _open_tree(m,idx)
    return _open_replay_previous(m)

def _open_report(m):
    rows=m.get('open_exploration',{}).get('records',[]);scheduled=[r for r in rows if r['cursor'] is not None]
    return {'mode':'open-ended structural exploration','retained_nodes':len(rows),
            'next_cursor':_open_cursor_next(scheduled[-1]['cursor']) if scheduled else [0,0],
            'generation_depth_limit':None,'work_per_run':12,
            'grammar':list(OPEN_UNARY+OPEN_BINARY),
            'symbolic_status':'experimental syntax retained in 0 structures; dedicated legacy symbolic workers inactive',
            'scope':'fair diagonal enumeration within this declared grammar; finite work per run; no exhaustive mathematics claim; supplied polynomial verifier unchanged in scope'}

_open_report_previous=_slot_report
def _slot_report(m):
    report=_open_report_previous(m);report['open_exploration']=_open_report(m);return report

_open_query_previous=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    if command in ('open','symbolic','symbolic-index'):
        print(json.dumps(_open_report(m),indent=2));return
    if command.startswith('open-run '):
        try:budget=int(command.split()[1])
        except ValueError:print('Use open-run N, N from 0 to 1000');return
        zero_core(m,'0-structures',operation='open_service',budget=budget)
        _slot_save(m,memory_path());print(json.dumps(_open_report(m),indent=2));return
    result=_open_query_previous(m,text)
    if command in ('help','?'):print('open / open-run N: saved open exploration; symbolic: experimental symbolic status')
    return result


# Symbolic archive connection. Expressions are syntax with retained provenance;
# the finite-polynomial interpreter remains an explicit supplied checker.
SYMBOLIC_ZERO_RULE='retained_symbolic_zero_connection_v1'

def _sym_ref(idx):return {'kind':'symbolic_reference','id':idx}

def _sym_expression(m,operation,parents,open_node=None):
    if operation=='retain_open_structure':
        return _open_tree(m,open_node) if _open_state(m)['records'][open_node]['operation']=='derivative_relation' else _open_ref(open_node)
    args=[_sym_ref(idx) for idx in parents]
    if operation in ('add','multiply','power'):return {'kind':'call','operation':operation,'args':args}
    if operation=='substitute_x':return {'kind':'substitution','variable':'x','args':args}
    if operation=='formal_derivative':return {'kind':'formal_derivative','variable':'x','args':args}
    if operation=='derivative_relation':return {'kind':'derivative_relation','variable':'x','function':args[0],'candidate':args[1]}
    raise ValueError('Symbolic construction must use a declared structural operation')

def _sym_assess(m,expression):
    if expression.get('kind')=='derivative_relation':return _zstruct_certificate(m,expression)
    try:coefficients=_zstruct_poly(m,expression)
    except _ZeroStructureUnsupported as exc:return {'outcome':'unresolved','reason':str(exc)}
    return {'outcome':'interpreted_finite_polynomial','coefficients':{str(k):v for k,v in sorted(coefficients.items())},
            'validator':'explicit_finite_polynomial_interpreter; not a discovered symbolic axiom'}

def _sym_find_open(m,idx):
    return next((r['id'] for r in _slot_rows(m,'symbolic') if r.get('operation')=='retain_open_structure' and r['open_node']==idx),None)

def _sym_retain_open(m,idx):
    old=_sym_find_open(m,idx)
    if old is not None:return old
    node=_open_state(m)['records'][idx];parents=[]
    for parent in node['parents']:
        found=_sym_find_open(m,parent)
        if found is None:found=zero_core(m,'symbolic',operation='retain_open',operands=(parent,))
        parents.append(found)
    sources=[]
    if node['operation']=='import_role':sources=[_slot_ref('roles',node['source']['id'])]
    if node['operation']=='import_calculus_result':sources=[_slot_ref('calculus',node['source']['id'])]
    if node['operation']=='import_symbolic':sources=[_slot_ref('symbolic',node['source']['id'])]
    return _sym_record(m,'retain_open_structure',parents,open_node=idx,sources=sources)

def _sym_record(m,operation,parents,open_node=None,sources=()):
    expression=_sym_expression(m,operation,parents,open_node)
    record={'rule':SYMBOLIC_ZERO_RULE,'operation':operation,'parents':list(parents),'sources':list(sources),
            'open_node':open_node,'expression':expression,'status':'experimental',
            'assessment':_sym_assess(m,expression),'retention_event':m['_active_event']}
    idx=zero_core(m,'symbolic',operation='record',record=record)
    m['feedback'].append({'source':_slot_ref('symbolic',idx),'zero_nexus':'Z0',
                          'targets':['symbolic_archive','open_structural_frontier','reconstruction_recipes'],
                          'status':record['assessment']['outcome']})
    return idx

def _sym_compose(m,operation,parents):
    expected=1 if operation=='formal_derivative' else 2
    if operation not in ('add','multiply','power','substitute_x','formal_derivative','derivative_relation','quotient') or len(parents)!=expected:
        raise ValueError('Use a declared symbolic operation with its arity')
    if any(type(p)is not int or not 0<=p<len(_slot_rows(m,'symbolic')) for p in parents):raise ValueError('Missing retained symbolic input')
    idx=_sym_record(m,operation,parents)
    sid=zero_core(m,'0-structures',operation='record',operands=({'kind':'symbolic','id':idx},))
    zero_core(m,'0-structures',operation='check',operands=(sid,))
    zero_core(m,'0-structures',operation='open_record',operation_name='import_symbolic',source={'id':idx})
    return idx

def _sym_check(m,row):
    rows=_slot_rows(m,'symbolic');idx=row['id'];parents=row['parents'];op=row['operation']
    if row.get('rule')!=SYMBOLIC_ZERO_RULE or row.get('status')!='experimental':raise ValueError('Untracked symbolic worker or status')
    if any(type(p)is not int or not 0<=p<idx for p in parents):raise ValueError('Symbolic ancestry lost')
    if op=='retain_open_structure':
        node=_open_state(m)['records'][row['open_node']]
        if [_slot_rows(m,'symbolic')[p].get('open_node') for p in parents]!=node['parents']:raise ValueError('Symbolic/open ancestry disagreement')
        sources=[]
        domain={'import_role':'roles','import_calculus_result':'calculus','import_symbolic':'symbolic'}.get(node['operation'])
        if domain:sources=[_slot_ref(domain,node['source']['id'])]
        if row['sources']!=sources:raise ValueError('Symbolic typed source changed')
    else:
        if op not in ('add','multiply','power','substitute_x','formal_derivative','derivative_relation','quotient') or len(parents)!=(1 if op=='formal_derivative' else 2) or row['open_node'] is not None or row['sources']:
            raise ValueError('Symbolic operation or arity changed')
    expression=_sym_expression(m,op,parents,row['open_node'])
    if row['expression']!=expression or row['assessment']!=_sym_assess(m,expression):raise ValueError('Symbolic expression or check changed')
    event=m['events'][row['retention_event']]
    if event['domain']!='symbolic' or event['operation'] not in ('retain_open','compose','service') or event['status']!='complete':raise ValueError('Symbolic gateway evidence missing')

_sym_poly_previous=_zstruct_poly
def _zstruct_poly(m,node):
    # Symbolic references use the same interpretation-work budget as open DAGs.
    if node.get('kind')=='symbolic_reference':
        outer='_open_check_remaining' not in m
        if outer:m['_open_check_remaining']=_principles_limit('interpretation',256)
        try:
            m['_open_check_remaining']-=1
            if m['_open_check_remaining']<0:raise _ZeroStructureUnsupported('interpretation work budget; structure retained')
            return _zstruct_poly(m,_slot_rows(m,'symbolic')[node['id']]['expression'])
        finally:
            if outer:m.pop('_open_check_remaining',None)
    return _sym_poly_previous(m,node)

_sym_tree_previous=_open_tree
def _open_tree(m,idx):
    node=_open_state(m)['records'][idx]
    if node['operation']=='import_symbolic':return _sym_ref(node['source']['id'])
    return _sym_tree_previous(m,idx)

_sym_snapshot_previous=_zstruct_snapshot
def _zstruct_snapshot(m,source):
    if source['kind']=='symbolic':
        expression=_pr_copy.deepcopy(_slot_rows(m,'symbolic')[source['id']]['expression'])
        return expression if expression['kind']=='derivative_relation' else {'kind':'expression','tree':expression,'source_outcome':'experimental'}
    return _sym_snapshot_previous(m,source)

_sym_work_previous=_zstruct_work
def _zstruct_work(m,sid,action,cursor=0):
    if _zstruct_state(m)['records'][sid]['source']['kind']=='symbolic':return None
    return _sym_work_previous(m,sid,action,cursor)

_sym_open_record_previous=_open_record
def _open_record(m,*args,**kwargs):
    idx=_sym_open_record_previous(m,*args,**kwargs)
    zero_core(m,'symbolic',operation='retain_open',operands=(idx,))
    return idx

def _sym_service(m,budget=12):
    if type(budget)is not int or not 0<=budget<=1000:raise ValueError('Symbolic service budget from 0 to 1000')
    missing=[r['id'] for r in _open_state(m)['records'] if _sym_find_open(m,r['id']) is None]
    for idx in missing[:budget]:zero_core(m,'symbolic',operation='retain_open',operands=(idx,))
    # Resume any symbolic proposal whose return path was interrupted before save.
    imported={r['source']['id'] for r in _open_state(m)['records'] if r['operation']=='import_symbolic'}
    for row in [r for r in _slot_rows(m,'symbolic') if r['operation']!='retain_open_structure' and r['id'] not in imported][:budget]:
        zero_core(m,'0-structures',operation='open_record',operation_name='import_symbolic',source={'id':row['id']})
    return _sym_report(m)

_sym_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='symbolic':
        if operation=='retain_open':return _sym_retain_open(m,*operands)
        if operation=='compose':return _sym_compose(m,*operands)
        if operation=='service':return _sym_service(m,**kwargs)
        if operation=='record':
            if kwargs['record'].get('rule')!=SYMBOLIC_ZERO_RULE:raise ValueError('Legacy symbolic workers remain excluded')
    return _sym_dispatch_previous(m,domain,operation,operands,kwargs)

def _sym_report(m):
    rows=_slot_rows(m,'symbolic')
    return {'connected_through':'Z0','retained_records':len(rows),
            'interpreted_polynomials':sum(r['assessment']['outcome']=='interpreted_finite_polynomial' for r in rows),
            'unresolved_retained':sum(r['assessment']['outcome']=='unresolved' for r in rows),
            'scope':'retained symbolic syntax, composition, substitution and experimental derivative proposals; explicit polynomial checking; general symbolic algebra remains unresolved'}

_sym_report_previous=_slot_report
def _slot_report(m):
    report=_sym_report_previous(m);report['symbolic_connection']=_sym_report(m)
    report['open_exploration']['symbolic_status']='symbolic archive connected through Z0; legacy SymPy workers inactive'
    return report

_sym_query_previous=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    if command in ('symbolic','symbolic-index'):
        print(json.dumps(_sym_report(m),indent=2))
        if command=='symbolic-index':
            for row in _slot_rows(m,'symbolic'):print('symbolic:'+str(row['id']),row['operation'],row['assessment']['outcome'],'parents:',row['parents'])
        return
    if command=='calculus-index':return _sym_query_previous(m,'calculus')
    if command.startswith('symbolic '):
        try:print(json.dumps(_slot_rows(m,'symbolic')[int(command.split()[1])],indent=2))
        except (ValueError,IndexError):print('Use symbolic N with a retained ID')
        return
    if command.startswith('symbolic-compose '):
        parts=command.split()
        try:
            idx=zero_core(m,'symbolic',operation='compose',operands=(parts[1],[int(p) for p in parts[2:]]))
        except (ValueError,IndexError) as exc:print('Symbolic proposal not submitted:',str(exc));return
        _slot_save(m,memory_path());print('Retained symbolic proposal:',idx);return
    result=_sym_query_previous(m,text)
    if command in ('help','?'):print('symbolic / symbolic-index / symbolic N / symbolic-compose OP PARENT_ID ...')
    return result

_sym_open_report_previous=_open_report
def _open_report(m):
    report=_sym_open_report_previous(m)
    report['symbolic_status']='symbolic archive connected through Z0; legacy SymPy workers inactive'
    return report


# Quantity roles and dimensional exploration are supplied physical metadata.
# They introduce no numeric primitive and do not promote unit matches to laws.
QUANTITY_RULE='zero_physical_quantity_roles_v1'
QUANTITY_DEFINITIONS=(
 ('mass','kg',('M',),()),('length','m',('L',),()),('duration','s',('T',),()),
 ('area','m^2',('L','L'),()),('volume','m^3',('L','L','L'),()),
 ('velocity','m/s',('L',),('T',)),('acceleration','m/s^2',('L',),('T','T')),
 ('pressure','Pa',('M',),('L','T','T')),('force','N',('M','L'),('T','T')),
 ('energy','J',('M','L','L'),('T','T')))
QUANTITY_OPERATIONS=('multiply','quotient','add','compare')

def _qty_dimensions(numerator,denominator):
    top=list(numerator);bottom=list(denominator)
    for symbol in ('M','L','T'):
        while symbol in top and symbol in bottom:top.remove(symbol);bottom.remove(symbol)
    return {'numerator':sorted(top),'denominator':sorted(bottom)}

def _qty_state(m):return m.setdefault('quantity_exploration',{'rule':QUANTITY_RULE,'records':[],'recipes':[]})

def _qty_role_body(definition):
    name,unit,top,bottom=definition
    return {'kind':'physical_quantity_role','name':name,'unit':unit,'dimensions':_qty_dimensions(top,bottom),
            'status':'supplied_dimension_definition','numeric_primitive':None,'zero_nexus':'Z0'}

def _qty_role_check(m,role):
    definition=next((d for d in QUANTITY_DEFINITIONS if d[0]==role['label']),None)
    if definition is None or role['body']!=_qty_role_body(definition) or role['parents']!=[0] or role['sources']!=[_slot_ref('rational',0)]:
        raise ValueError('Physical role definition or provenance changed')

def _qty_cursor_next(cursor):
    shell,position=cursor;position+=1
    return [shell+1,0] if position==len(QUANTITY_OPERATIONS)*(2*shell+1) else [shell,position]

def _qty_cursor_recipe(cursor):
    shell,position=cursor;pair,op=divmod(position,len(QUANTITY_OPERATIONS))
    return QUANTITY_OPERATIONS[op],([shell,pair] if pair<=shell else [pair-shell-1,shell])

def _qty_expected(m,operation,parents,role):
    if operation=='quantity':
        return {'status':'dimensioned_placeholder','dimensions':_pr_copy.deepcopy(_slot_rows(m,'roles')[role]['body']['dimensions']),
                'physical_law_verified':False}
    rows=_qty_state(m)['records'];a,b=(rows[p]['assessment'].get('dimensions') for p in parents)
    if a is None or b is None:return {'status':'unresolved_input_dimensions','dimensions':None,'physical_law_verified':False}
    if operation=='compare':return {'status':'dimensions_match' if a==b else 'dimensions_differ','dimensions':None,'physical_law_verified':False}
    if operation=='add':return {'status':'dimensionally_compatible' if a==b else 'dimensionally_incompatible',
                               'dimensions':_pr_copy.deepcopy(a) if a==b else None,'physical_law_verified':False}
    top=a['numerator']+(b['numerator'] if operation=='multiply' else b['denominator'])
    bottom=a['denominator']+(b['denominator'] if operation=='multiply' else b['numerator'])
    if len(top)+len(bottom)>_principles_limit('dimensions',256):return {'status':'dimension_work_deferred','dimensions':None,'physical_law_verified':False}
    result=_qty_dimensions(top,bottom)
    matches=[name for name,unit,n,d in QUANTITY_DEFINITIONS if _qty_dimensions(n,d)==result]
    return {'status':'dimensionally_constructed','dimensions':result,'matching_quantity_roles':matches,'physical_law_verified':False,
            'condition':'dimension algebra only; quotient of quantities additionally requires a nonzero denominator'}

def _qty_record(m,operation,parents=(),role=None,cursor=None):
    state=_qty_state(m);idx=len(state['records'])
    if any(type(p)is not int or not 0<=p<idx for p in parents):raise ValueError('Quantity parents must be retained first')
    row={'id':idx,'execution_policy':_principles_current(),'operation':operation,'parents':list(parents),'role':role,'cursor':cursor,
         'assessment':_qty_expected(m,operation,parents,role),'zero_nexus':'Z0','event':m['_active_event']}
    state['records'].append(row);state['recipes'].append(_pr_copy.deepcopy(row))
    # Register an ordinary open node. Its symbolic mirror and experimental
    # 0-structure/check are handled by the existing connected gateway.
    zero_core(m,'0-structures',operation='open_record',operation_name='import_quantity',source={'id':idx})
    m['feedback'].append({'source':{'archive':'quantity_exploration','id':idx},'zero_nexus':'Z0',
                          'targets':['dimension_observer','symbolic_archive','open_structural_frontier'],
                          'status':row['assessment']['status']})
    return idx

def _qty_service(m,budget=12):
    if type(budget)is not int or not 0<=budget<=1000:raise ValueError('Quantity work budget from 0 to 1000')
    state=_qty_state(m)
    for definition in QUANTITY_DEFINITIONS:
        name=definition[0];role=next((r['id'] for r in _slot_rows(m,'roles') if r.get('rule')==QUANTITY_RULE and r['label']==name),None)
        if role is None:
            role=zero_core(m,'roles',operation='record',record={'kind':'physical_quantity','label':name,'operation':'quantity_role',
                'rule':QUANTITY_RULE,'body':_qty_role_body(definition),'parents':[0],'sources':[_slot_ref('rational',0)],
                'depth':1,'path':['0',name],'slot':{'counter':0,'foundation_id':0}})
        if not any(r['operation']=='quantity' and r['role']==role for r in state['records']):
            zero_core(m,'quantities',operation='record',operation_name='quantity',role=role)
    scheduled=[r for r in state['records'] if r['cursor'] is not None]
    cursor=_qty_cursor_next(scheduled[-1]['cursor']) if scheduled else [0,0]
    for unused in range(budget):
        operation,parents=_qty_cursor_recipe(cursor)
        zero_core(m,'quantities',operation='record',operation_name=operation,parents=parents,cursor=cursor)
        cursor=_qty_cursor_next(cursor)
    return _qty_report(m)

_qty_tree_previous=_open_tree
def _open_tree(m,idx):
    row=_open_state(m)['records'][idx]
    if row['operation']=='import_quantity':return {'kind':'quantity_reference','id':row['source']['id']}
    return _qty_tree_previous(m,idx)

_qty_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='quantities':
        if operation=='service':return _qty_service(m,**kwargs)
        if operation=='record':
            options=dict(kwargs);op=options.pop('operation_name');return _qty_record(m,op,**options)
    return _qty_dispatch_previous(m,domain,operation,operands,kwargs)

_qty_recover_previous=_zstruct_recover_extensions
def _zstruct_recover_extensions(m):
    changed=False;state=m.get('quantity_exploration')
    if state is not None:
        actual={r['id']:r for r in state['records']}
        if len(actual)!=len(state['records']):raise ValueError('Duplicate quantity ID')
        restored=[]
        for recipe in state['recipes']:
            row=actual.pop(recipe['id'],None)
            if row is None:row=_pr_copy.deepcopy(recipe);changed=True
            elif row!=recipe:raise ValueError('Quantity evidence changed')
            restored.append(row)
        if actual:raise ValueError('Untracked quantity record')
        state['records']=restored
    return _qty_recover_previous(m) or changed

_qty_replay_previous=_slot_replay
def _slot_replay(m):
    state=m.get('quantity_exploration')
    if state is not None:
        if state['rule']!=QUANTITY_RULE or state['records']!=state['recipes']:raise ValueError('Quantity recipe conflict')
        cursor=[0,0];seed=0
        for idx,row in enumerate(state['records']):
            if row['id']!=idx or row['zero_nexus']!='Z0' or any(type(p)is not int or not 0<=p<idx for p in row['parents']):raise ValueError('Quantity identity or ancestry changed')
            if row['operation']=='quantity':
                if row['parents'] or row['cursor'] is not None or seed>=len(QUANTITY_DEFINITIONS):raise ValueError('Invalid quantity declaration')
                role=_slot_rows(m,'roles')[row['role']];_qty_role_check(m,role)
                if role['label']!=QUANTITY_DEFINITIONS[seed][0]:raise ValueError('Quantity declaration order changed')
                seed+=1
            else:
                op,parents=_qty_cursor_recipe(cursor)
                if row['operation']!=op or row['parents']!=parents or row['cursor']!=cursor or row['role'] is not None:raise ValueError('Quantity frontier changed')
                cursor=_qty_cursor_next(cursor)
            if row['assessment']!=_principles_qty_expected(m,row):raise ValueError('Quantity dimensional assessment changed')
            event=m['events'][row['event']]
            if event['domain']!='quantities' or event['operation']!='record' or event['status']!='complete':raise ValueError('Quantity clock-linked gateway lost')
        for row in _open_state(m)['records']:
            if row['operation']=='import_quantity' and not 0<=row['source']['id']<len(state['records']):raise ValueError('Quantity return source missing')
    return _qty_replay_previous(m)

def _qty_report(m):
    rows=m.get('quantity_exploration',{}).get('records',[])
    return {'quantity_roles':len([r for r in _slot_rows(m,'roles') if r.get('rule')==QUANTITY_RULE]),
            'retained_constructions':len(rows),'dimension_matches':sum(r['assessment']['status']=='dimensions_match' for r in rows),
            'incompatible_or_different_retained':sum(r['assessment']['status'] in ('dimensions_differ','dimensionally_incompatible') for r in rows),
            'energy_dimension_candidates':[r['id'] for r in rows if 'energy' in r['assessment'].get('matching_quantity_roles',[])],
            'physical_laws_verified':0,'numeric_primitives':['S'],
            'scope':'supplied mass/length/duration-based SI dimensions; open retained dimension proposals; no new numerical division or physical-law discovery claimed'}

_qty_report_previous=_slot_report
def _slot_report(m):
    report=_qty_report_previous(m);report['quantities']=_qty_report(m);return report

_qty_query_previous=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    if command in ('quantities','mass','physics-index'):
        print(json.dumps(_qty_report(m),indent=2));return
    if command=='quantities-index':
        for row in _qty_state(m)['records']:print(row['id'],row['operation'],row['parents'],json.dumps(row['assessment']))
        return
    if command.startswith('quantities-run '):
        try:budget=int(command.split()[1])
        except ValueError:print('Use quantities-run N');return
        zero_core(m,'quantities',operation='service',budget=budget);_slot_save(m,memory_path());print(json.dumps(_qty_report(m),indent=2));return
    result=_qty_query_previous(m,text)
    if command in ('help','?'):print('quantities / quantities-index / quantities-run N / mass')
    return result


# Typed physical calculations: magnitudes use the connected symbolic workers;
# dimensions and physical assumptions remain explicit supplied metadata.
PHYSICAL_RULE='zero_typed_physical_execution_v1'

def _physical_state(m):return m.setdefault('physical_calculations',{'rule':PHYSICAL_RULE,'records':[],'recipes':[]})

def _physical_dimensions(a,b,quotient=False):
    if a is None or b is None:return None
    top=a['numerator']+(b['denominator'] if quotient else b['numerator'])
    bottom=a['denominator']+(b['numerator'] if quotient else b['denominator'])
    return None if len(top)+len(bottom)>_principles_limit('dimensions',256) else _qty_dimensions(top,bottom)

def _physical_expected(m,row):
    state=_physical_state(m);op=row['operation'];parents=[state['records'][p] for p in row['parents']]
    if op=='bind':
        quantity=_qty_state(m)['records'][row['quantity']]
        return {'status':'declared_magnitude_binding','dimensions':quantity['assessment']['dimensions'],
                'physical_law_verified':False,'assumption':'symbolic magnitude in the declared quantity units; not a measured value'}
    valid=('declared_magnitude_binding','dimensionally_valid_operation','verified_polynomial_derivative')
    if any(p['assessment']['status'] not in valid for p in parents):
        return {'status':'unresolved_input','dimensions':None,'physical_law_verified':False}
    a,b=(p['assessment']['dimensions'] for p in parents)
    if op=='add':
        return {'status':'dimensionally_valid_operation' if a==b else 'dimensionally_incompatible',
                'dimensions':a if a==b else None,'physical_law_verified':False}
    dimensions=_physical_dimensions(a,b,op in ('quotient','derivative'))
    if dimensions is None:return {'status':'dimension_work_deferred','dimensions':None,'physical_law_verified':False}
    if op=='derivative':
        variable=_zstruct_poly(m,_sym_ref(parents[1]['magnitude']))
        if variable!={1:1}:return {'status':'unresolved_independent_variable','dimensions':dimensions,'physical_law_verified':False}
        proposal={'kind':'derivative_relation','variable':'x','function':_sym_ref(parents[0]['magnitude']),
                  'candidate':_sym_ref(row['candidate'])}
        proof=_zstruct_certificate(m,proposal)
        return {'status':'verified_polynomial_derivative' if proof['outcome']=='verified' else proof['outcome'],
                'dimensions':dimensions,'certificate':proof,'physical_law_verified':False,
                'assumptions':['derivative of magnitude with respect to the declared x coordinate',
                               'quantity dimensions divide by independent-variable dimensions']}
    return {'status':'dimensionally_valid_operation','dimensions':dimensions,'physical_law_verified':False,
            'condition':'formal quotient requires a nonzero magnitude denominator' if op=='quotient' else 'declared symbolic magnitude multiplication'}

def _physical_record(m,operation,parents=(),quantity=None,magnitude=None,candidate=None,dimension_source=None):
    rows=_physical_state(m)['records'];idx=len(rows);symbolic=_slot_rows(m,'symbolic')
    if any(type(p)is not int or not 0<=p<idx for p in parents):raise ValueError('Missing retained physical input')
    if operation=='bind':
        if parents or type(quantity)is not int or not 0<=quantity<len(_qty_state(m)['records']) or type(magnitude)is not int or not 0<=magnitude<len(symbolic):raise ValueError('Bind a retained quantity to a retained symbolic magnitude')
    else:
        if operation not in ('add','multiply','quotient','derivative') or len(parents)!=2:raise ValueError('Physical operator requires two retained inputs')
        if any(rows[p]['magnitude'] is None for p in parents):raise ValueError('Physical input has no magnitude expression')
        if operation=='derivative':
            if type(candidate)is not int or not 0<=candidate<len(symbolic):raise ValueError('Derivative requires a retained symbolic candidate')
            magnitude=candidate
        else:
            magnitude=zero_core(m,'symbolic',operation='compose',operands=(operation,[rows[p]['magnitude'] for p in parents]))
    row={'id':idx,'execution_policy':_principles_current(),'rule':PHYSICAL_RULE,'assessment_rule':PHYSICAL_ASSESSMENT_RULE,'operation':operation,'parents':list(parents),'quantity':quantity,
         'magnitude':magnitude,'candidate':candidate,'dimension_source':dimension_source,'zero_nexus':'Z0','event':m['_active_event']}
    try:row['assessment']=_physical_expected(m,row)
    except _ZeroStructureUnsupported as exc:row['assessment']={'status':'unresolved','dimensions':None,'reason':str(exc),'physical_law_verified':False}
    rows.append(row);_physical_state(m)['recipes'].append(_pr_copy.deepcopy(row))
    zero_core(m,'0-structures',operation='open_record',operation_name='import_physical',source={'id':idx})
    m['feedback'].append({'source':{'archive':'physical_calculations','id':idx},'zero_nexus':'Z0',
                          'targets':['symbolic_magnitudes','physical_dimension_checks','open_structural_frontier','calculus_proposals'],
                          'status':row['assessment']['status']})
    if operation=='derivative':
        sid=zero_core(m,'0-structures',operation='record',operands=({'kind':'physical','id':idx},))
        zero_core(m,'0-structures',operation='check',operands=(sid,))
    return idx

def _physical_service(m,budget=4):
    # Unit magnitudes are declared unit constructions, not observed data.
    if type(budget)is not int or not 0<=budget<=1000:raise ValueError('Physical work budget from 0 to 1000')
    one=_sym_find_open(m,1)
    if one is None:return _physical_report(m)
    rows=_physical_state(m)['records'];bound={r['quantity']:r['id'] for r in rows if r['operation']=='bind' and r['magnitude']==one}
    bound.update({r['dimension_source']:r['id'] for r in rows if r.get('dimension_source') is not None})
    count=0
    for quantity in _qty_state(m)['records']:
        if count>=budget:break
        qid=quantity['id']
        if qid in bound:continue
        if quantity['operation']=='quantity':
            idx=zero_core(m,'physical',operation='bind',operands=(qid,one))
        elif quantity['operation'] in ('add','multiply','quotient') and all(p in bound for p in quantity['parents']):
            idx=zero_core(m,'physical',operation='apply',operands=(quantity['operation'],[bound[p] for p in quantity['parents']]),dimension_source=qid)
        else:continue
        bound[qid]=idx;count+=1
    return _physical_report(m)

_physical_sym_expression_previous=_sym_expression
def _sym_expression(m,operation,parents,open_node=None):
    if operation=='quotient':return {'kind':'formal_quotient','args':[_sym_ref(p) for p in parents]}
    return _physical_sym_expression_previous(m,operation,parents,open_node)

_physical_tree_previous=_open_tree
def _open_tree(m,idx):
    node=_open_state(m)['records'][idx]
    if node['operation']=='import_physical':return {'kind':'physical_reference','id':node['source']['id']}
    return _physical_tree_previous(m,idx)

_physical_snapshot_previous=_zstruct_snapshot
def _zstruct_snapshot(m,source):
    if source['kind']=='physical':return {'kind':'typed_physical_derivative','physical_record':source['id']}
    return _physical_snapshot_previous(m,source)

_physical_certificate_previous=_zstruct_certificate
def _zstruct_certificate(m,payload):
    if payload.get('kind')=='typed_physical_derivative':
        row=_physical_state(m)['records'][payload['physical_record']];assessment=row['assessment']
        if assessment['status']=='verified_polynomial_derivative':
            proof=_pr_copy.deepcopy(assessment['certificate'])
            proof.update(physical_record=row['id'],dimensions=_pr_copy.deepcopy(assessment['dimensions']),physical_law_verified=False)
            proof['assumptions']+=assessment['assumptions']
            return proof
        return {'outcome':'nonmatching' if assessment['status']=='nonmatching' else 'unresolved',
                'reason':'typed derivative proposal retained with dimensional and magnitude evidence',
                'physical_record':row['id'],'typed_status':assessment['status']}
    return _physical_certificate_previous(m,payload)

_physical_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='physical':
        if operation=='bind':return _physical_record(m,'bind',quantity=operands[0],magnitude=operands[1])
        if operation=='apply':return _physical_record(m,operands[0],parents=operands[1],**kwargs)
        if operation=='derivative':return _physical_record(m,'derivative',parents=operands[:2],candidate=operands[2])
        if operation=='service':return _physical_service(m,**kwargs)
    return _physical_dispatch_previous(m,domain,operation,operands,kwargs)

_physical_recover_previous=_zstruct_recover_extensions
def _zstruct_recover_extensions(m):
    changed=False;state=m.get('physical_calculations')
    if state is not None:
        actual={r['id']:r for r in state['records']}
        if len(actual)!=len(state['records']):raise ValueError('Duplicate typed physical record')
        restored=[]
        for recipe in state['recipes']:
            row=actual.pop(recipe['id'],None)
            if row is None:row=_pr_copy.deepcopy(recipe);changed=True
            elif row!=recipe:raise ValueError('Physical execution evidence changed')
            restored.append(row)
        if actual:raise ValueError('Untracked physical record')
        state['records']=restored
    return _physical_recover_previous(m) or changed

_physical_replay_previous=_slot_replay
def _slot_replay(m):
    state=m.get('physical_calculations')
    if state is not None:
        if state['rule']!=PHYSICAL_RULE or state['records']!=state['recipes']:raise ValueError('Physical recipe conflict')
        for idx,row in enumerate(state['records']):
            if row['id']!=idx or row['rule']!=PHYSICAL_RULE or row['zero_nexus']!='Z0' or any(type(p)is not int or not 0<=p<idx for p in row['parents']):raise ValueError('Physical ancestry changed')
            if not 0<=row['magnitude']<len(_slot_rows(m,'symbolic')):raise ValueError('Physical magnitude missing')
            if row['operation']=='bind':
                if row['parents'] or row['candidate'] is not None or not 0<=row['quantity']<len(_qty_state(m)['records']):raise ValueError('Physical binding changed')
            else:
                if row['operation'] not in ('add','multiply','quotient','derivative') or len(row['parents'])!=2 or row['quantity'] is not None:raise ValueError('Physical execution signature changed')
                if row['operation']=='derivative':
                    if row['magnitude']!=row['candidate']:raise ValueError('Physical derivative candidate changed')
                else:
                    magnitude=_slot_rows(m,'symbolic')[row['magnitude']]
                    if magnitude['operation']!=row['operation'] or magnitude['parents']!=[state['records'][p]['magnitude'] for p in row['parents']]:raise ValueError('Physical magnitude operation changed')
            try:expected=_physical_expected(m,row)
            except _ZeroStructureUnsupported as exc:expected={'status':'unresolved','dimensions':None,'reason':str(exc),'physical_law_verified':False}
            source=row.get('dimension_source')
            if source is not None:
                quantity=_qty_state(m)['records'][source]
                source_parents=[state['records'][p]['quantity'] if state['records'][p]['operation']=='bind' else state['records'][p].get('dimension_source') for p in row['parents']]
                if quantity['operation']!=row['operation'] or quantity['parents']!=source_parents:raise ValueError('Physical dimension-frontier linkage changed')
            if row['assessment']!=expected:raise ValueError('Physical dimensions or calculus certificate changed')
            event=m['events'][row['event']]
            if event['domain']!='physical' or event['operation'] not in ('bind','apply','derivative','service') or event['status']!='complete':raise ValueError('Physical clock gateway lost')
        for node in _open_state(m)['records']:
            if node['operation']=='import_physical' and not 0<=node['source']['id']<len(state['records']):raise ValueError('Physical return source missing')
    return _physical_replay_previous(m)

def _physical_report(m):
    rows=m.get('physical_calculations',{}).get('records',[])
    return {'retained_calculations':len(rows),'verified_polynomial_derivatives':sum(r['assessment']['status']=='verified_polynomial_derivative' for r in rows),
            'numeric_primitives':['S'],'connections':['Z0','symbolic magnitudes','quantity dimensions','typed derivative proposals','open frontier','feedback','clocks','replay','recovery'],
            'scope':'explicit unit bindings and typed symbolic calculations; no empirical physics law promotion; general numerical division remains unresolved'}

_physical_report_previous=_slot_report
def _slot_report(m):
    report=_physical_report_previous(m);report['physical_execution']=_physical_report(m);return report

_physical_query_previous=_slot_query
def _slot_query(m,text):
    command=text.strip().lower();parts=command.split()
    if command=='physical':print(json.dumps(_physical_report(m),indent=2));return
    if command=='physical-index':
        for row in _physical_state(m)['records']:print(row['id'],row['operation'],'magnitude:',row['magnitude'],json.dumps(row['assessment']))
        return
    if parts and parts[0] in ('physical-bind','physical-apply','physical-derivative'):
        try:
            if parts[0]=='physical-bind':idx=zero_core(m,'physical',operation='bind',operands=(int(parts[1]),int(parts[2])))
            elif parts[0]=='physical-apply':idx=zero_core(m,'physical',operation='apply',operands=(parts[1],[int(parts[2]),int(parts[3])]))
            else:idx=zero_core(m,'physical',operation='derivative',operands=tuple(int(p) for p in parts[1:4]))
        except (ValueError,IndexError) as exc:print('Physical proposal not submitted:',str(exc));return
        _slot_save(m,memory_path());print('Retained physical calculation:',idx);return
    result=_physical_query_previous(m,text)
    if command in ('help','?'):print('physical / physical-index / physical-bind QUANTITY SYMBOLIC / physical-apply OP LEFT RIGHT / physical-derivative FUNCTION VARIABLE CANDIDATE_SYMBOLIC')
    return result


# Open physical proposal scheduling. Outcome checks never select the next tuple.
PHYSICAL_FRONTIER_RULE='zero_untargeted_physical_frontier_v1'
PHYSICAL_FRONTIER_LANES=('bind','multiply','quotient','add','derivative')

def _pf_state(m):return m.setdefault('physical_frontier',{'rule':PHYSICAL_FRONTIER_RULE,'records':[],'recipes':[]})

def _pf_arity(lane):return 3 if lane=='derivative' else 2

def _pf_next(cursor,arity):
    shell,offset=cursor;offset+=1
    return [shell+1,0] if offset==(shell+1)**arity-shell**arity else [shell,offset]

def _pf_tuple(cursor,arity):
    # Unrank all tuples whose maximum retained input ID equals shell, in a
    # fixed order, without choosing an expression or a desired output.
    shell,rank=cursor;result=[];seen=False
    for position in range(arity):
        remaining=arity-position-1
        for value in range(shell+1):
            includes=seen or value==shell
            count=(shell+1)**remaining if includes else (shell+1)**remaining-shell**remaining
            if rank<count:result.append(value);seen=includes;break
            rank-=count
        else:raise ValueError('Invalid physical frontier tuple rank')
    return result

def _pf_counts(m,event=None):
    arrays=(_qty_state(m)['records'],_slot_rows(m,'symbolic'),_physical_state(m)['records'])
    fields=('event','retention_event','event')
    return [len(rows) if event is None else sum(r[field]<event for r in rows) for rows,field in zip(arrays,fields)]

def _pf_step(m):
    state=_pf_state(m);idx=len(state['records']);lane=PHYSICAL_FRONTIER_LANES[idx%len(PHYSICAL_FRONTIER_LANES)]
    earlier=next((r for r in reversed(state['records']) if r['lane']==lane),None)
    cursor=([0,0] if earlier is None else _pf_next(earlier['cursor'],_pf_arity(lane)) if earlier['advanced'] else earlier['cursor'])
    inputs=_pf_tuple(cursor,_pf_arity(lane));counts=_pf_counts(m)
    limits=([counts[0],counts[1]] if lane=='bind' else [counts[2],counts[2],counts[1]] if lane=='derivative' else [counts[2],counts[2]])
    available=all(value<limit for value,limit in zip(inputs,limits));result=None
    if not available:status='awaiting_retained_inputs'
    elif lane=='bind' and _qty_state(m)['records'][inputs[0]]['assessment'].get('dimensions') is None:
        status='unresolved_input_dimensions'
    else:
        if lane=='bind':result=zero_core(m,'physical',operation='bind',operands=tuple(inputs))
        elif lane=='derivative':result=zero_core(m,'physical',operation='derivative',operands=tuple(inputs))
        else:result=zero_core(m,'physical',operation='apply',operands=(lane,inputs))
        status='retained_physical_proposal'
    row={'id':idx,'lane':lane,'cursor':list(cursor),'inputs':inputs,'available_counts':counts,'advanced':available,
         'status':status,'result':result,'event':m['_active_event'],'zero_nexus':'Z0'}
    state['records'].append(row);state['recipes'].append(_pr_copy.deepcopy(row))
    m['feedback'].append({'source':{'archive':'physical_frontier','id':idx},'zero_nexus':'Z0',
                          'targets':['retained_proposal_history','open_physical_frontier'],'status':status})
    return idx

def _physical_service(m,budget=4):
    if type(budget)is not int or not 0<=budget<=1000:raise ValueError('Physical exploration budget from 0 to 1000')
    for unused in range(budget):zero_core(m,'physical',operation='explore_step')
    return _physical_report(m)

_pf_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='physical' and operation=='explore_step':return _pf_step(m)
    return _pf_dispatch_previous(m,domain,operation,operands,kwargs)

_pf_recover_previous=_zstruct_recover_extensions
def _zstruct_recover_extensions(m):
    changed=False;state=m.get('physical_frontier')
    if state is not None:
        actual={r['id']:r for r in state['records']}
        if len(actual)!=len(state['records']):raise ValueError('Duplicate physical proposal receipt')
        restored=[]
        for recipe in state['recipes']:
            row=actual.pop(recipe['id'],None)
            if row is None:row=_pr_copy.deepcopy(recipe);changed=True
            elif row!=recipe:raise ValueError('Physical proposal receipt changed')
            restored.append(row)
        if actual:raise ValueError('Untracked physical proposal receipt')
        state['records']=restored
    return _pf_recover_previous(m) or changed

_pf_replay_previous=_slot_replay
def _slot_replay(m):
    state=m.get('physical_frontier')
    if state is not None:
        if state['rule']!=PHYSICAL_FRONTIER_RULE or state['records']!=state['recipes']:raise ValueError('Physical frontier recipe conflict')
        cursors={lane:[0,0] for lane in PHYSICAL_FRONTIER_LANES}
        for idx,row in enumerate(state['records']):
            lane=PHYSICAL_FRONTIER_LANES[idx%len(PHYSICAL_FRONTIER_LANES)];cursor=cursors[lane]
            inputs=_pf_tuple(cursor,_pf_arity(lane));counts=_pf_counts(m,row['event'])
            limits=([counts[0],counts[1]] if lane=='bind' else [counts[2],counts[2],counts[1]] if lane=='derivative' else [counts[2],counts[2]])
            available=all(value<limit for value,limit in zip(inputs,limits))
            expected_status='awaiting_retained_inputs' if not available else 'unresolved_input_dimensions' if lane=='bind' and _qty_state(m)['records'][inputs[0]]['assessment'].get('dimensions') is None else 'retained_physical_proposal'
            if (row['id']!=idx or row['lane']!=lane or row['cursor']!=cursor or row['inputs']!=inputs or row['available_counts']!=counts or row['advanced']!=available or row['status']!=expected_status or row['zero_nexus']!='Z0'):
                raise ValueError('Physical proposal order or retained inputs changed')
            if expected_status=='retained_physical_proposal':
                result=_physical_state(m)['records'][row['result']]
                if result['operation']!=lane or not row['event']<result['event']:raise ValueError('Physical proposal result changed')
                if lane=='bind':
                    if [result['quantity'],result['magnitude']]!=inputs:raise ValueError('Physical binding proposal changed')
                elif lane=='derivative':
                    if result['parents']!=inputs[:2] or result['candidate']!=inputs[2]:raise ValueError('Physical derivative proposal changed')
                elif result['parents']!=inputs:raise ValueError('Physical arithmetic proposal changed')
            elif row['result'] is not None:raise ValueError('Unexecuted proposal has an invented result')
            event=m['events'][row['event']]
            if event['domain']!='physical' or event['operation']!='explore_step' or event['status']!='complete':raise ValueError('Physical proposal zero-clock evidence lost')
            if available:cursors[lane]=_pf_next(cursor,_pf_arity(lane))
    return _pf_replay_previous(m)

_pf_report_previous=_physical_report
def _physical_report(m):
    report=_pf_report_previous(m);rows=m.get('physical_frontier',{}).get('records',[])
    report.update(exploration='fixed fair tuple enumeration of retained inputs; outcomes do not steer scheduling',
                  retained_proposals=len(rows),automatic_lanes=list(PHYSICAL_FRONTIER_LANES),
                  desired_answer=None,success_stop_condition=None)
    return report

_pf_query_previous=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    if command.startswith('physical-run '):
        try:budget=int(command.split()[1])
        except ValueError:print('Use physical-run N');return
        zero_core(m,'physical',operation='service',budget=budget);_slot_save(m,memory_path());print(json.dumps(_physical_report(m),indent=2));return
    result=_pf_query_previous(m,text)
    if command in ('help','?'):print('physical-run N: resume automatic physical proposal exploration')
    return result


# ============================================================
# V4.10.5 audit repairs. Historical records and recipes stay intact.
# Old generator syntax remains available only for replaying old evidence.
# ============================================================
PHYSICAL_ASSESSMENT_RULE='typed_physical_definedness_v2'
PHYSICAL_REASSESSMENT_RULE='retained_physical_reassessments_v1'

_audit_work_previous=_zstruct_work
def _zstruct_work(m,sid,action,cursor=0):
    if action=='expand':return None
    return _audit_work_previous(m,sid,action,cursor)

# Observe and check retained evidence without executing archived preset jobs.
def _zstruct_service(m,budget=4):
    if type(budget)is not int or not 0<=budget<=1000:raise ValueError('Structure work budget from 0 to 1000')
    state=_zstruct_state(m)
    for kind,rows in (('role',_slot_rows(m,'roles')),('Zi',m.get('Zi',{}).get('attempts',[])),
                      ('reserved',m.get('opportunity_proposals',{}).get('records',[])),
                      ('comparison',m.get('pathway_operations',{}).get('comparisons',[]))):
        cursor=state['scan'][kind];limit=min(len(rows),cursor+8)
        while cursor<limit:
            if kind!='role' or rows[cursor].get('rule')==Z1I_ROLE_RULE:
                zero_core(m,'0-structures',operation='record',operands=({'kind':kind,'id':cursor},))
            cursor+=1
        state['scan'][kind]=cursor
    done=set(state['work_done']);count=0
    for task in state['work']:
        if count>=budget:break
        if task['id'] in done or task['action']!='check':continue
        zero_core(m,'0-structures',operation='check',operands=(task['structure'],))
        state['work_done'].append(task['id']);done.add(task['id']);count+=1
    return _zstruct_report(m)

_audit_structure_report_previous=_zstruct_report
def _zstruct_report(m):
    report=_audit_structure_report_previous(m);state=m.get('zero_structures',{});done=set(state.get('work_done',[]))
    report.update(legacy_preset_expansion='disabled; archived jobs retained for history',
                  retained_inactive_expansion_jobs=sum(r['action']=='expand' and r['id'] not in done for r in state.get('work',[])),
                  active_pending_structure_checks=sum(r['action']=='check' and r['id'] not in done for r in state.get('work',[])))
    return report

_audit_physical_expected_v1=_physical_expected

def _physical_assess_v2(m,row,parents):
    op=row['operation'];result={'physical_law_verified':False}
    if op=='bind':
        dimensions=_qty_state(m)['records'][row['quantity']]['assessment']['dimensions']
        result.update(status='declared_magnitude_binding' if dimensions is not None else 'unresolved_input_dimensions',
                      dimensions=_pr_copy.deepcopy(dimensions),
                      assumption='symbolic magnitude in the declared quantity units; not a measured value')
        return result
    assessments=[p['assessment'] for p in parents]
    # No missing dimensions are ever equated or cancelled.
    if any(p['dimensions'] is None for p in assessments):
        return dict(result,status='unresolved_input_dimensions',dimensions=None)
    valid=('declared_magnitude_binding','dimensionally_valid_operation','verified_polynomial_derivative')
    if any(p['status'] not in valid for p in assessments):
        return dict(result,status='unresolved_input',dimensions=None,
                    reason='a parent has unresolved, incompatible or undefined physical semantics')
    a,b=(p['dimensions'] for p in assessments)
    if op=='add':
        return dict(result,status='dimensionally_valid_operation' if a==b else 'dimensionally_incompatible',
                    dimensions=_pr_copy.deepcopy(a) if a==b else None)
    dimensions=_physical_dimensions(a,b,op in ('quotient','derivative'))
    if dimensions is None:return dict(result,status='dimension_work_deferred',dimensions=None)
    if op=='quotient':
        # A nonconstant polynomial need not be nonzero everywhere. Preserve the
        # condition unless a retained nonzero constant establishes it exactly.
        try:denominator=_zstruct_poly(m,_sym_ref(parents[1]['magnitude']))
        except _ZeroStructureUnsupported:denominator=None
        if denominator=={}:
            return dict(result,status='undefined_zero_denominator',dimensions=dimensions,
                        dimension_status='compatible',definedness='undefined',
                        reason='retained denominator magnitude is identically zero')
        if denominator is not None and set(denominator)=={0} and denominator[0]!=0:
            return dict(result,status='dimensionally_valid_operation',dimensions=dimensions,
                        dimension_status='compatible',definedness='defined',
                        condition='retained constant denominator is nonzero')
        return dict(result,status='conditional_operation',dimensions=dimensions,
                    dimension_status='compatible',definedness='unresolved',
                    condition='formal quotient requires a nonzero magnitude denominator')
    # Existing derivative verification is still supplied, with corrected parent
    # assessments. No new derivative identity or physical law is introduced.
    if op=='derivative':
        shadow=_pr_copy.deepcopy(row)
        return _physical_expected_with_parents_v1(m,shadow,parents)
    return dict(result,status='dimensionally_valid_operation',dimensions=dimensions,
                condition='declared symbolic magnitude multiplication')

def _physical_expected_with_parents_v1(m,row,parents):
    # Reproduce the declared derivative checker without substituting archive rows.
    dimensions=_physical_dimensions(parents[0]['assessment']['dimensions'],parents[1]['assessment']['dimensions'],True)
    variable=_zstruct_poly(m,_sym_ref(parents[1]['magnitude']))
    if variable!={1:1}:return {'status':'unresolved_independent_variable','dimensions':dimensions,'physical_law_verified':False}
    proof=_zstruct_certificate(m,{'kind':'derivative_relation','variable':'x',
        'function':_sym_ref(parents[0]['magnitude']),'candidate':_sym_ref(row['candidate'])})
    return {'status':'verified_polynomial_derivative' if proof['outcome']=='verified' else proof['outcome'],
            'dimensions':dimensions,'certificate':proof,'physical_law_verified':False,
            'assumptions':['derivative of magnitude with respect to the declared x coordinate',
                           'quantity dimensions divide by independent-variable dimensions']}

def _physical_current_assessments(m,limit=None):
    rows=_physical_state(m)['records'];limit=len(rows) if limit is None else limit;current=[]
    for row in rows[:limit]:
        parents=[dict(rows[p],assessment=current[p]) for p in row['parents']]
        try:assessment=_physical_assess_v2(m,row,parents)
        except _ZeroStructureUnsupported as exc:
            assessment={'status':'unresolved','dimensions':None,'reason':str(exc),'physical_law_verified':False}
        current.append(assessment)
    return current

def _physical_expected(m,row):
    rule=row.get('assessment_rule')
    if rule is None:return _audit_physical_expected_v1(m,row)
    if rule!=PHYSICAL_ASSESSMENT_RULE:raise ValueError('Unknown physical assessment rule')
    current=_physical_current_assessments(m,row['id'])
    parents=[dict(_physical_state(m)['records'][p],assessment=current[p]) for p in row['parents']]
    return _physical_assess_v2(m,row,parents)

def _physical_reassessment_state(m):
    return m.setdefault('physical_reassessments',{'rule':PHYSICAL_REASSESSMENT_RULE,'records':[],'recipes':[]})

def _physical_reassess(m):
    state=_physical_reassessment_state(m);rows=_physical_state(m)['records'];current=_physical_current_assessments(m)
    retained={r['physical_record'] for r in state['records']}
    for row in rows:
        if row.get('assessment_rule') is not None or row['id'] in retained:continue
        revision={'id':len(state['records']),'rule':PHYSICAL_ASSESSMENT_RULE,'physical_record':row['id'],
                  'archived_assessment':_pr_copy.deepcopy(row['assessment']),
                  'assessment':_pr_copy.deepcopy(current[row['id']]),'event':m['_active_event'],'zero_nexus':'Z0'}
        state['records'].append(revision);state['recipes'].append(_pr_copy.deepcopy(revision))
        m['feedback'].append({'source':{'archive':'physical_reassessments','id':revision['id']},
            'zero_nexus':'Z0','targets':['physical_assessment_history'],'status':revision['assessment']['status']})
    return len(state['records'])

_audit_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='physical' and operation=='reassess':return _physical_reassess(m)
    return _audit_dispatch_previous(m,domain,operation,operands,kwargs)

_audit_recovery_previous=_zstruct_recover_extensions
def _zstruct_recover_extensions(m):
    changed=_audit_recovery_previous(m);state=m.get('physical_reassessments')
    if state is None:return changed
    actual={r['id']:r for r in state['records']}
    if len(actual)!=len(state['records']):raise ValueError('Duplicate physical reassessment')
    restored=[]
    for recipe in state['recipes']:
        row=actual.pop(recipe['id'],None)
        if row is None:row=_pr_copy.deepcopy(recipe);changed=True
        elif row!=recipe:raise ValueError('Physical reassessment evidence changed')
        restored.append(row)
    if actual:raise ValueError('Untracked physical reassessment')
    state['records']=restored;return changed

_audit_replay_previous=_slot_replay
def _slot_replay(m):
    result=_audit_replay_previous(m);state=m.get('physical_reassessments')
    if state is None:return result
    if state['rule']!=PHYSICAL_REASSESSMENT_RULE or state['records']!=state['recipes']:raise ValueError('Physical reassessment recipe conflict')
    current=_physical_current_assessments(m);seen=set();rows=_physical_state(m)['records']
    for idx,revision in enumerate(state['records']):
        rid=revision['physical_record']
        if type(rid)is not int or not 0<=rid<len(rows) or rid in seen:raise ValueError('Physical reassessment identity changed')
        seen.add(rid);row=rows[rid];event=m['events'][revision['event']]
        if (revision['id']!=idx or revision['rule']!=PHYSICAL_ASSESSMENT_RULE or revision['zero_nexus']!='Z0' or
            row.get('assessment_rule') is not None or revision['archived_assessment']!=row['assessment'] or
            revision['assessment']!=current[rid] or event['domain']!='physical' or event['operation']!='reassess' or
            event['status']!='complete' or revision['event']<=row['event']):
            raise ValueError('Physical reassessment or gateway evidence changed')
    return result

_audit_save_previous=_slot_save
def _slot_save(m,path):
    # Validation and atomic publication remain in the existing save chain.
    # A blocked command is saved too; invalid archives never replace the source.
    rows=m.get('physical_calculations',{}).get('records',[])
    retained={r['physical_record'] for r in m.get('physical_reassessments',{}).get('records',[])}
    if any(r.get('assessment_rule') is None and r['id'] not in retained for r in rows):
        zero_core(m,'physical',operation='reassess')
    return _audit_save_previous(m,path)

_audit_report_previous=_physical_report
def _physical_report(m):
    report=_audit_report_previous(m);current=_physical_current_assessments(m)
    report.update(assessment_rule=PHYSICAL_ASSESSMENT_RULE,
        retained_legacy_reassessments=len(m.get('physical_reassessments',{}).get('records',[])),
        corrected_legacy_assessments=sum(r['assessment']!=r['archived_assessment'] for r in m.get('physical_reassessments',{}).get('records',[])),
        verified_polynomial_derivatives=sum(r['status']=='verified_polynomial_derivative' for r in current))
    return report

_audit_query_previous=_slot_query
def _slot_query(m,text):
    command=text.strip().lower()
    try:
        if command=='physical-index':
            current=_physical_current_assessments(m)
            for row in _physical_state(m)['records']:
                print(row['id'],row['operation'],'magnitude:',row['magnitude'],json.dumps(current[row['id']]))
                if current[row['id']]!=row['assessment']:
                    print('  archived assessment (superseded):',json.dumps(row['assessment']))
            return
        if command=='physical-reassessments':
            print(json.dumps(_physical_reassessment_state(m),indent=2));return
        result=_audit_query_previous(m,text)
        if command in ('help','?'):print('physical-reassessments: retained current assessments and superseded historical labels')
        return result
    finally:
        # All command paths, including read-only inspection and caught/rethrown
        # errors, publish their completed/blocked gateway receipts before return.
        _slot_save(m,memory_path())



# ============================================================
# V4.10.6: connected retries, typed open interpretation and recovery entry points.
# Polynomial magnitude interpretation remains the supplied bounded checker.
# Dimensions are never discarded to obtain an untyped numerical answer.
# ============================================================
TYPED_OPEN_RULE='zero_typed_open_interpretation_v1'

def _zstruct_work(m,sid,action,cursor=0,requested=False):
    state=_zstruct_state(m)
    if type(sid)is not int or not 0<=sid<len(state['records']):raise ValueError('Use a retained nonnegative structure ID')
    if action=='expand':return None
    if action!='check':raise ValueError('Unknown retained structure work action')
    if not requested and state['records'][sid]['source']['kind'] in ('open','symbolic'):return None
    row={'id':len(state['work']),'structure':sid,'action':action,'cursor':cursor,'zero_nexus':'Z0'}
    state['work'].append(row);state['work_recipes'].append(_pr_copy.deepcopy(row));return row['id']

_connected_open_tree_previous=_open_tree
def _open_tree(m,idx):
    row=_open_state(m)['records'][idx]
    if row['operation']=='import_physical_reassessment':return {'kind':'physical_reassessment_reference','id':row['source']['id']}
    return _connected_open_tree_previous(m,idx)

def _typed_state(m):return m.setdefault('typed_open_interpretation',{'rule':TYPED_OPEN_RULE,'records':[],'recipes':[]})

def _typed_expected(m,open_id):
    remaining=[_principles_limit('interpretation',256)];seen=set()
    def unresolved(reason,dimensions=None):return {'status':'unresolved','dimensions':dimensions,'reason':reason,'physical_law_verified':False}
    def value(dimensions,polynomial=None,origin='retained_typed_expression'):
        return {'status':'interpreted_magnitude' if polynomial is not None else 'dimensionally_interpreted',
                'dimensions':_pr_copy.deepcopy(dimensions),'magnitude_coefficients':None if polynomial is None else {str(k):v for k,v in sorted(polynomial.items())},
                'magnitude_scope':'supplied bounded finite-polynomial interpretation',
                'origin':origin,'physical_law_verified':False}
    def magnitude(idx):
        try:return _zstruct_poly(m,_sym_ref(idx))
        except _ZeroStructureUnsupported:return None
    def physical(row,assessment):
        status=assessment['status'];dimensions=assessment['dimensions']
        if status not in ('declared_magnitude_binding','dimensionally_valid_operation','verified_polynomial_derivative'):
            return dict(unresolved('physical assessment: '+status,dimensions),physical_status=status)
        return value(dimensions,magnitude(row['magnitude']),'retained_physical_magnitude')
    def walk(node):
        remaining[0]-=1
        if remaining[0]<0:return unresolved('typed interpretation work budget; source retained')
        kind=node.get('kind')
        if kind=='open_reference':
            idx=node['id']
            if idx in seen:return unresolved('cyclic typed reference')
            seen.add(idx)
            try:return walk(_open_tree(m,idx))
            finally:seen.remove(idx)
        if kind=='principles_assessment_reference':return _principles_typed_reference(m,node['id'])
        if kind=='quantity_reference':
            assessment=_qty_state(m)['records'][node['id']]['assessment'];dimensions=assessment['dimensions']
            return unresolved('quantity dimensions unresolved') if dimensions is None else value(dimensions,None,'declared_quantity_dimensions; magnitude not supplied')
        if kind=='physical_reference':
            row=_physical_state(m)['records'][node['id']]
            return physical(row,_physical_current_assessments(m,row['id']+1)[row['id']])
        if kind=='physical_reassessment_reference':
            revision=_physical_reassessment_state(m)['records'][node['id']]
            return physical(_physical_state(m)['records'][revision['physical_record']],revision['assessment'])
        if kind=='symbolic_reference':return walk(_slot_rows(m,'symbolic')[node['id']]['expression'])
        if kind=='call' and node.get('operation') in ('add','multiply'):
            a,b=(walk(n) for n in node['args'])
            if a['status']=='unresolved' or b['status']=='unresolved':return unresolved('unresolved typed operand')
            if node['operation']=='add':
                if a['dimensions']!=b['dimensions']:return unresolved('incompatible addition dimensions')
                dimensions=a['dimensions']
            else:dimensions=_physical_dimensions(a['dimensions'],b['dimensions'])
            if dimensions is None:return unresolved('dimension interpretation work budget')
            pa,pb=a['magnitude_coefficients'],b['magnitude_coefficients'];poly=None
            if pa is not None and pb is not None:
                pa={int(k):v for k,v in pa.items()};pb={int(k):v for k,v in pb.items()};poly={}
                if node['operation']=='add':
                    poly=dict(pa)
                    for k,v in pb.items():poly[k]=poly.get(k,0)+v
                else:
                    for ka,va in pa.items():
                        for kb,vb in pb.items():poly[ka+kb]=poly.get(ka+kb,0)+va*vb
                poly={k:v for k,v in poly.items() if v}
                if any(k>_principles_limit('degree',8) or abs(v)>_principles_limit('coefficient',4096) for k,v in poly.items()):poly=None
            return value(dimensions,poly)
        # The scalar checker is deliberately unable to strip typed wrappers.
        try:return value({'numerator':[],'denominator':[]},_zstruct_poly(m,node),'dimensionless_polynomial')
        except _ZeroStructureUnsupported as exc:return unresolved(str(exc))
    return walk(_open_ref(open_id))

def _typed_assess(m,open_id):
    state=_typed_state(m)
    if type(open_id)is not int or not 0<=open_id<len(_open_state(m)['records']):raise ValueError('Missing open input for typed interpretation')
    old=next((r['id'] for r in state['records'] if r['open_node']==open_id),None)
    if old is not None:return old
    row={'id':len(state['records']),'execution_policy':_principles_current(),'open_node':open_id,'rule':TYPED_OPEN_RULE,
         'assessment':_typed_expected(m,open_id),'event':m['_active_event'],'zero_nexus':'Z0'}
    state['records'].append(row);state['recipes'].append(_pr_copy.deepcopy(row))
    m['feedback'].append({'source':{'archive':'typed_open_interpretation','id':row['id']},'zero_nexus':'Z0',
        'targets':['typed_open_evidence'],'status':row['assessment']['status']})
    return row['id']

_connected_open_record_previous=_open_record
def _open_record(m,*args,**kwargs):
    idx=_connected_open_record_previous(m,*args,**kwargs)
    zero_core(m,'typed-open',operation='assess',operands=(idx,));return idx

# The original node is already in the frontier. Correction records are imported
# separately so history, corrected meaning and their subsequent paths coexist.
def _connected_returns(m,budget=12):
    state=_open_state(m)
    if not state['records']:return
    imported={r['source']['id'] for r in state['records'] if r['operation']=='import_physical_reassessment'}
    for revision in [r for r in _physical_reassessment_state(m)['records'] if r['id'] not in imported][:budget]:
        zero_core(m,'0-structures',operation='open_record',operation_name='import_physical_reassessment',source={'id':revision['id']})
    assessed={r['open_node'] for r in _typed_state(m)['records']}
    for node in [r for r in state['records'] if r['id'] not in assessed][:budget]:
        zero_core(m,'typed-open',operation='assess',operands=(node['id'],))

_connected_open_service_previous=_open_service
def _open_service(m,budget=12):
    report=_connected_open_service_previous(m,budget=budget)
    _connected_returns(m,budget);return report

_connected_reassess_previous=_physical_reassess
def _physical_reassess(m):
    count=_connected_reassess_previous(m);_connected_returns(m);return count

_connected_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='typed-open':
        if operation=='assess':return _typed_assess(m,*operands)
        if operation=='service':return _connected_returns(m,**kwargs)
        raise ValueError('Unknown typed interpretation operation')
    return _connected_dispatch_previous(m,domain,operation,operands,kwargs)

_connected_recover_previous=_zstruct_recover_extensions
def _zstruct_recover_extensions(m):
    changed=_connected_recover_previous(m);state=m.get('typed_open_interpretation')
    if state is None:return changed
    actual={r['id']:r for r in state['records']}
    if len(actual)!=len(state['records']):raise ValueError('Duplicate typed open assessment')
    restored=[]
    for recipe in state['recipes']:
        row=actual.pop(recipe['id'],None)
        if row is None:row=_pr_copy.deepcopy(recipe);changed=True
        elif row!=recipe:raise ValueError('Changed typed interpretation evidence')
        restored.append(row)
    if actual:raise ValueError('Untracked typed interpretation')
    state['records']=restored;return changed

_connected_replay_previous=_slot_replay
def _slot_replay(m):
    result=_connected_replay_previous(m);state=m.get('typed_open_interpretation')
    for node in _open_state(m)['records']:
        if node['operation']=='import_physical_reassessment':
            rid=node['source']['id'];rows=_physical_reassessment_state(m)['records']
            if type(rid)is not int or not 0<=rid<len(rows) or rows[rid]['event']>=node['event']:
                raise ValueError('Physical reassessment return provenance changed')
    if state is None:return result
    if state['rule']!=TYPED_OPEN_RULE or state['records']!=state['recipes']:raise ValueError('Typed open recipe conflict')
    seen=set()
    for idx,row in enumerate(state['records']):
        oid=row['open_node']
        if type(oid)is not int or not 0<=oid<len(_open_state(m)['records']) or oid in seen:raise ValueError('Typed open source changed')
        seen.add(oid);event=m['events'][row['event']]
        if (row['id']!=idx or row['rule']!=TYPED_OPEN_RULE or row['zero_nexus']!='Z0' or
            row['assessment']!=_principles_typed_expected(m,row) or row['event']<=_open_state(m)['records'][oid]['event'] or
            event['domain']!='typed-open' or event['operation']!='assess' or event['status']!='complete'):
            raise ValueError('Typed open interpretation or gateway changed')
    return result

_connected_report_previous=_slot_report
def _slot_report(m):
    report=_connected_report_previous(m);rows=m.get('typed_open_interpretation',{}).get('records',[])
    report['typed_open_interpretation']={'rule':TYPED_OPEN_RULE,'retained_assessments':len(rows),
        'interpreted_magnitudes':sum(r['assessment']['status']=='interpreted_magnitude' for r in rows),
        'dimension_only':sum(r['assessment']['status']=='dimensionally_interpreted' for r in rows),
        'scope':'typed quantity/physical references, addition and multiplication; supplied bounded polynomial magnitudes; unsupported forms retained'}
    return report

_connected_query_previous=_slot_query
def _slot_query(m,text):
    command=text.strip().lower();parts=command.split()
    try:
        if parts and parts[0]=='0-retry':
            if len(parts)!=2:raise ValueError('Use 0-retry N with a retained nonnegative structure ID')
            sid=int(parts[1]);wid=_zstruct_work(m,sid,'check',requested=True)
            print('Retained structure queued for another check:',sid,'| work:',wid);return
        if command in ('typed','typed-index'):
            zero_core(m,'typed-open',operation='service',budget=12)
            for row in _typed_state(m)['records']:print(row['id'],'open:',row['open_node'],json.dumps(row['assessment']))
            return
        if command.endswith('-example') or command.endswith('-examples'):
            print('Selected example commands are retired; use retained indexes and open exploration.');return
        result=_connected_query_previous(m,text)
        if command in ('help','?'):print('typed / typed-index: retained dimensional and magnitude interpretation; 0-retry N queues a real check')
        return result
    finally:_slot_save(m,memory_path())

# Strict recovery never invokes the legacy target-based adaptive worker.
# Both recovery and regeneration write to separate candidates and preserve input.
def _strict_recovery_cli(mode,source,cycles=1):
    import hashlib,tempfile
    source=os.path.abspath(source)
    with open(source,'rb') as handle:raw=handle.read()
    digest=hashlib.sha256(raw).hexdigest();folder=tempfile.mkdtemp(prefix=os.path.basename(source)+'.strict-'+mode+'-',dir=os.path.dirname(source))
    report={'mode':mode,'source':source,'source_sha256':digest,'zero_nexus':'Z0','desired_answer':None,'success_stop_condition':None}
    target=os.path.join(folder,MEMORY_FILENAME)
    try:
        if mode=='recover':
            damaged=json.loads(raw.decode('utf-8'))
            if damaged.get('experiment')!=SLOT_RULE:raise ValueError('Strict recovery requires a retained slot archive; use its original engine for legacy-format memory')
            temporary=os.path.join(folder,'source-copy.json')
            with open(temporary,'wb') as handle:handle.write(raw)
            try:m=_slot_load(temporary)
            except ValueError:
                candidate=temporary+'.slot-recovery-candidate.json'
                if not os.path.isfile(candidate):raise
                m=_slot_load(candidate)
            _slot_save(m,target);report.update(status='candidate_verified',candidate=target,
                scope='retained construction and recipe recovery; no absent evidence invented')
        else:
            if type(cycles)is not int or not 1<=cycles<=1000:raise ValueError('Regeneration cycles from 1 to 1000')
            # Fixed work allowance, never a record count, desired identity or score.
            previous=globals().get('_MEMORY_DIRECTORY_RESOLVED');globals()['_MEMORY_DIRECTORY_RESOLVED']=folder
            try:
                for unused in range(cycles):run_slots(interactive=False)
            finally:globals()['_MEMORY_DIRECTORY_RESOLVED']=previous
            report.update(status='fresh_lineage_verified',candidate=target,cycles=cycles,
                scope='new exploration from Z0; historical IDs, missing facts and timestamps are not claimed recovered')
    except (ValueError,KeyError,IndexError,UnicodeError,OSError) as exc:
        report.update(status='unresolved',reason=str(exc))
    finally:
        with open(source,'rb') as handle:
            if hashlib.sha256(handle.read()).hexdigest()!=digest:raise ValueError('Recovery input changed externally')
        report['source_preserved']=True
        _ze_atomic_json(os.path.join(folder,'report.json'),report)
    print(json.dumps(report,indent=2));return report

def _strict_main():
    import argparse
    parser=argparse.ArgumentParser(description='Strict Z0 exploration; separate source-preserving recovery/regeneration candidates')
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--slot-recover',metavar='MEMORY_JSON')
    group.add_argument('--slot-regenerate',metavar='MEMORY_JSON')
    parser.add_argument('--cycles',type=int,default=1,help='fixed regeneration work cycles; no desired-answer target')
    args=parser.parse_args()
    if args.slot_recover:return _strict_recovery_cli('recover',args.slot_recover)
    if args.slot_regenerate:return _strict_recovery_cli('regenerate',args.slot_regenerate,args.cycles)
    if args.cycles!=1:parser.error('--cycles requires --slot-regenerate')
    return run_slots()


# ============================================================
# V4.11.0 exact symbolic execution through Z0.
# Numeric construction still uses S. Quotients and algebraic roots are exact
# retained syntax. Calculus transformations are supplied roles, not discovered
# axioms. Deferred work receives further effort through a fair saved frontier.
# ============================================================
MATH_RULE='zero_exact_symbolic_execution_v1'
MATH_LANES=('simplify','differentiate','integrate','expand','root','divide')
MATH_EFFORT_PER_ATTEMPT=256
class _MathDeferred(Exception):pass
class _MathUndefined(Exception):pass

def _math_state(m):return m.setdefault('exact_math',{'rule':MATH_RULE,'records':[],'recipes':[],
    'attempts':[],'attempt_recipes':[],'frontier':[],'frontier_recipes':[]})

def _math_call(op,*args):return {'kind':'call','operation':op,'args':list(args)}
def _math_key(node):return json.dumps(node,sort_keys=True,separators=(',',':'))

class _MathArithmetic:
    def __init__(self,m,effort,recording):self.m=m;self.remaining=effort;self.recording=recording;self.conditions=[];self.rules=[]
    def tick(self):
        if self.remaining<=0:raise _MathDeferred('saved work allowance exhausted; eligible for a later larger allowance')
        self.remaining-=1
    def succ(self,n):
        self.tick();return _slot_S(self.m,n) if self.recording else n+1
    def nat(self,n):
        if type(n)is not int or n<0:raise _MathUndefined('natural construction requires a nonnegative integer')
        value=0
        for unused in range(n):value=self.succ(value)
        if self.recording:_slot_ensure_counter(self.m,value)
        return {'kind':'reference','ref':{'archive':'rational','id':value}}
    def number(self,node):
        if node.get('kind')=='reference' and node['ref']['archive']=='rational':return node['ref']['id']
        return None
    def add(self,a,b):
        result=a
        for unused in range(b):result=self.succ(result)
        return result
    def remaining_after(self,total,used):
        if used>total:raise _MathUndefined('retained unit cancellation order')
        result=0;cursor=used
        while cursor<total:cursor=self.succ(cursor);result=self.succ(result)
        return result
    def mul(self,a,b):
        result=0
        for unused in range(b):result=self.add(result,a)
        return result
    def divmod(self,a,b):
        if b==0:raise _MathUndefined('division by zero')
        q=0;r=0
        for unused in range(a):
            r=self.succ(r)
            if r==b:q=self.succ(q);r=0
        return q,r
    def gcd(self,a,b):
        while b:
            self.tick();unused,r=self.divmod(a,b);a,b=b,r
        return a
    def power(self,a,b):
        result=1
        for unused in range(b):result=self.mul(result,a)
        return result
    def condition(self,text):
        if text not in self.conditions:self.conditions.append(text)
    def rule(self,text):
        if text not in self.rules:self.rules.append(text)
    def opposite(self,node):
        self.rule('declared archived i action: opposite retained unit role')
        role=next((r['id'] for r in _slot_rows(self.m,'roles') if r.get('rule')=='declared_complex_i_action_v497'),None)
        if role is None:raise _MathDeferred('archived i-action role not yet available')
        return {'kind':'opposite_role','role':{'archive':'roles','id':role},'arg':node}
    def imaginary(self):
        role=next((r['id'] for r in _slot_rows(self.m,'roles') if r.get('rule')=='declared_complex_i_action_v497'),None)
        if role is None:raise _MathDeferred('archived i-action role not yet available')
        return {'kind':'imaginary_unit_role','role':{'archive':'roles','id':role}}
    def rotate(self,phase):
        self.tick();self.rule('supplied archived complex i action')
        return zero_core(self.m,'roles',operation='apply_complex_i',operands=(self.imaginary()['role']['id'],phase)) if self.recording else I_NEXT[phase]
    def fraction(self,node):
        n=self.number(node)
        if n is not None:return n,1
        if node.get('kind')=='call' and node['operation']=='quotient':
            a,b=(self.number(x) for x in node['args'])
            if a is not None and b is not None:return a,b
        return None
    def ratio(self,n,d):
        if d==0:raise _MathUndefined('division by zero')
        if n==0:return self.nat(0)
        g=self.gcd(n,d);n,unused=self.divmod(n,g);d,unused=self.divmod(d,g)
        return self.nat(n) if d==1 else _math_call('quotient',self.nat(n),self.nat(d))

# Safe mathematical input grammar: no eval, imports, attributes or executable code.
def _math_parse(a,text):
    import ast
    def walk(n):
        a.tick()
        if isinstance(n,ast.Constant) and type(n.value)is int:return a.nat(n.value)
        if isinstance(n,ast.Name):return a.imaginary() if n.id=='I' else {'kind':'variable','name':n.id}
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return a.opposite(walk(n.operand))
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.UAdd):return walk(n.operand)
        if isinstance(n,ast.BinOp):
            op={ast.Add:'add',ast.Mult:'multiply',ast.Div:'quotient',ast.Pow:'power'}.get(type(n.op))
            if isinstance(n.op,ast.Sub):return _math_call('add',walk(n.left),a.opposite(walk(n.right)))
            if op:return _math_call(op,walk(n.left),walk(n.right))
        if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and not n.keywords:
            name=n.func.id
            if name=='sqrt' and len(n.args)==1:return _math_call('root',walk(n.args[0]),a.nat(2))
            if name=='root' and len(n.args)==2:return _math_call('root',*(walk(x) for x in n.args))
            if name in ('sin','cos','exp','log','abs') and len(n.args)==1:return _math_call(name,walk(n.args[0]))
        raise _MathUndefined('supported input: integer literals, variables, + - * / **, root/sqrt, sin/cos/exp/log/abs')
    return walk(ast.parse(text,mode='eval').body)

def _math_resolve(a,node,attempts,seen=None):
    a.tick();seen=set() if seen is None else seen;kind=node.get('kind')
    if kind=='open_reference':return _math_resolve(a,_open_tree(a.m,node['id']),attempts,seen)
    if kind=='symbolic_reference':return _math_resolve(a,_slot_rows(a.m,'symbolic')[node['id']]['expression'],attempts,seen)
    if kind=='math_reference':
        rid=node['id']
        if rid in seen:raise _MathUndefined('cyclic exact-math source')
        row=_math_state(a.m)['attempts'][node['attempt']] if 'attempt' in node else attempts.get(rid)
        if row is None or row['status'] not in ('exact','exact_symbolic','conditional_symbolic','unresolved_formal'):raise _MathDeferred('referenced exact-math result is not yet executable')
        for condition in row['conditions']:a.condition(condition)
        seen.add(rid)
        try:return _math_resolve(a,row['result'],attempts,seen)
        finally:seen.remove(rid)
    if kind=='reference':
        ref=node['ref']
        if ref['archive']=='rational':return a.nat(a.m['expressions'][ref['id']]['value'])
        # A non-real formal coefficient is retained rather than silently coerced.
        raise _MathDeferred('complex coefficient remains under its archived role; scalar worker does not erase it')
    if kind=='constant':return a.nat(node['value'])
    if kind=='variable':return _pr_copy.deepcopy(node)
    if kind=='imaginary_unit_role':return a.imaginary()
    if kind=='algebraic_root':
        result=_pr_copy.deepcopy(node);result['radicand']=_math_resolve(a,node['radicand'],attempts,seen);result['degree']=_math_resolve(a,node['degree'],attempts,seen);return result
    if kind=='opposite_role':return a.opposite(_math_resolve(a,node['arg'],attempts,seen))
    if kind=='call':return _math_call(node['operation'],*(_math_resolve(a,n,attempts,seen) for n in node['args']))
    if kind=='substitution':
        left,right=(_math_resolve(a,n,attempts,seen) for n in node['args'])
        return _math_substitute(left,node['variable'],right)
    if kind in ('formal_derivative','formal_integral'):
        return dict(node,args=[_math_resolve(a,n,attempts,seen) for n in node['args']])
    raise _MathDeferred('typed or unsupported source retained; scalar execution cannot discard units or roles')

def _math_substitute(node,variable,replacement):
    if node.get('kind')=='variable' and node['name']==variable:return _pr_copy.deepcopy(replacement)
    result=_pr_copy.deepcopy(node)
    if 'args' in node:result['args']=[_math_substitute(n,variable,replacement) for n in node['args']]
    if 'arg' in node:result['arg']=_math_substitute(node['arg'],variable,replacement)
    if 'radicand' in node:result['radicand']=_math_substitute(node['radicand'],variable,replacement)
    return result

def _math_depends(node,variable):
    if node.get('kind')=='variable':return node['name']==variable
    return any(_math_depends(n,variable) for n in node.get('args',[])) or ('arg'in node and _math_depends(node['arg'],variable)) or ('radicand'in node and _math_depends(node['radicand'],variable))

def _math_simplify(a,node):
    a.tick();kind=node.get('kind')
    if kind=='opposite_role':
        arg=_math_simplify(a,node['arg'])
        if a.number(arg)==0:return arg
        if arg.get('kind')=='opposite_role':a.rule('two opposite actions restore the retained role');return arg['arg']
        return a.opposite(arg)
    if kind!='call':return node
    op=node['operation'];args=[_math_simplify(a,n) for n in node['args']]
    if op in ('add','multiply','quotient','power','root'):
        x,y=args;nx,ny=a.number(x),a.number(y);fx,fy=a.fraction(x),a.fraction(y)
        if op=='add':
            if nx==0:return y
            if ny==0:return x
            if y.get('kind')=='opposite_role' and fx is not None and a.fraction(y['arg']) is not None:
                other=a.fraction(y['arg']);left=a.mul(fx[0],other[1]);right=a.mul(other[0],fx[1]);denominator=a.mul(fx[1],other[1])
                a.rule('declared opposite-role cancellation counted through S')
                return a.ratio(a.remaining_after(left,right),denominator) if left>=right else a.opposite(a.ratio(a.remaining_after(right,left),denominator))
            if x.get('kind')=='opposite_role' and fy is not None:return _math_simplify(a,_math_call('add',y,x))
            if x.get('kind')=='opposite_role' and x['arg']==y or y.get('kind')=='opposite_role' and y['arg']==x:
                a.rule('declared opposite-role cancellation');return a.nat(0)
            if fx is not None and fy is not None:return a.ratio(a.add(a.mul(fx[0],fy[1]),a.mul(fy[0],fx[1])),a.mul(fx[1],fy[1]))
            if x==y:return _math_call('multiply',a.nat(2),x)
            # Combine equal retained factors without merging their source records.
            if x.get('kind')=='call' and y.get('kind')=='call' and x['operation']==y['operation']=='multiply' and x['args'][1]==y['args'][1]:
                c=_math_simplify(a,_math_call('add',x['args'][0],y['args'][0]));return _math_simplify(a,_math_call('multiply',c,x['args'][1]))
        if op=='multiply':
            if nx==0 or ny==0:return a.nat(0)
            if nx==1:return y
            if ny==1:return x
            if x.get('kind')==y.get('kind')=='imaginary_unit_role':
                if a.rotate('i_unit')!='opposite_unit':raise _MathUndefined('archived i-action changed')
                return a.opposite(a.nat(1))
            if fx is not None and fy is not None:return a.ratio(a.mul(fx[0],fy[0]),a.mul(fx[1],fy[1]))
            if x.get('kind')=='opposite_role':return _math_simplify(a,a.opposite(_math_call('multiply',x['arg'],y)))
            if y.get('kind')=='opposite_role':return _math_simplify(a,a.opposite(_math_call('multiply',x,y['arg'])))
            if x==y:return _math_call('power',x,a.nat(2))
            if fy is not None and fx is None:return _math_call('multiply',y,x)
        if op=='quotient':
            if ny==0:raise _MathUndefined('division by a retained zero magnitude')
            if fy is None:a.condition(_math_key(y)+' != 0')
            if nx==0:return a.nat(0)
            if ny==1:return x
            if x==y:return a.nat(1)
            if fx is not None and fy is not None:return a.ratio(a.mul(fx[0],fy[1]),a.mul(fx[1],fy[0]))
            if x.get('kind')=='opposite_role':return _math_simplify(a,a.opposite(_math_call('quotient',x['arg'],y)))
            if y.get('kind')=='opposite_role':return _math_simplify(a,a.opposite(_math_call('quotient',x,y['arg'])))
        if op=='power':
            if ny==0:
                if nx==0:a.condition('0**0 uses the declared empty-product convention')
                return a.nat(1)
            if ny==1:return x
            if x.get('kind')=='imaginary_unit_role' and ny is not None:
                phase='unit'
                for unused in range(ny):phase=a.rotate(phase)
                return {'unit':lambda:a.nat(1),'i_unit':a.imaginary,'opposite_unit':lambda:a.opposite(a.nat(1)),
                        'opposite_i_unit':lambda:a.opposite(a.imaginary())}[phase]()
            if nx is not None and ny is not None:return a.nat(a.power(nx,ny))
            if y.get('kind')=='opposite_role':return _math_simplify(a,_math_call('quotient',a.nat(1),_math_call('power',x,y['arg'])))
            if fy is not None and fy[1]!=1:return _math_simplify(a,_math_call('root',_math_call('power',x,a.nat(fy[0])),a.nat(fy[1])))
        if op=='root':
            if ny is None:raise _MathDeferred('root degree needs a retained natural interpretation')
            if ny<2:raise _MathUndefined('root degree must be at least two')
            if nx in (0,1):return x
            if x.get('kind')=='opposite_role':
                unused,remainder=a.divmod(ny,2)
                if remainder==1:return _math_simplify(a,a.opposite(_math_call('root',x['arg'],y)))
                if ny==2 and a.fraction(x['arg']) is not None:
                    a.rule('principal complex square root under the archived i role')
                    return _math_simplify(a,_math_call('multiply',a.imaginary(),_math_call('root',x['arg'],y)))
                a.rule('principal complex algebraic-root branch explicitly supplied')
                return {'kind':'algebraic_root','radicand':x,'degree':y,'branch':'principal_complex','relation':'z**degree = radicand'}
            if fx is not None:
                roots=[]
                for target in fx:
                    k=0
                    while True:
                        power=a.power(k,ny)
                        if power>=target:break
                        k=a.succ(k)
                    roots.append(k if power==target else None)
                if all(r is not None for r in roots):return a.ratio(*roots)
                a.rule('principal real algebraic root retained exactly; no decimal approximation')
            else:
                unused,remainder=a.divmod(ny,2)
                if remainder==0:a.condition(_math_key(x)+' >= 0 for the principal real root')
    if op=='log':
        if a.number(args[0])==0 or args[0].get('kind')=='opposite_role' and a.fraction(args[0]['arg']) is not None:
            raise _MathUndefined('real logarithm requires a strictly positive magnitude')
        a.condition(_math_key(args[0])+' > 0')
        if a.number(args[0])==1:return a.nat(0)
    if op=='exp' and a.number(args[0])==0:return a.nat(1)
    if op=='sin' and a.number(args[0])==0:return a.nat(0)
    if op=='cos' and a.number(args[0])==0:return a.nat(1)
    if op=='abs' and a.number(args[0]) is not None:return args[0]
    return _math_call(op,*args)

def _math_expand(a,node):
    a.tick()
    if node.get('kind')=='opposite_role':return a.opposite(_math_expand(a,node['arg']))
    if node.get('kind')!='call':return node
    args=[_math_expand(a,n) for n in node['args']];op=node['operation']
    if op=='multiply':
        for side in (0,1):
            if args[side].get('kind')=='call' and args[side]['operation']=='add':
                other=args[1 if side==0 else 0]
                return _math_expand(a,_math_call('add',*(_math_call('multiply',n,other) for n in args[side]['args'])))
    if op=='power':
        n=a.number(args[1])
        if n is not None:
            result=a.nat(1)
            for unused in range(n):result=_math_expand(a,_math_call('multiply',result,args[0]));a.tick()
            return _math_simplify(a,result)
    return _math_simplify(a,_math_call(op,*args))

def _math_derivative(a,node,variable):
    a.tick()
    if not _math_depends(node,variable):return a.nat(0)
    if node.get('kind')=='variable':return a.nat(1)
    if node.get('kind')=='opposite_role':return a.opposite(_math_derivative(a,node['arg'],variable))
    if node.get('kind')=='formal_integral' and node['variable']==variable:
        a.condition('integrand continuous on the selected real interval')
        a.rule('supplied fundamental antiderivative relation on the stated domain');return node['args'][0]
    if node.get('kind')!='call':return {'kind':'formal_derivative','variable':variable,'args':[node]}
    op=node['operation'];x=node['args'][0];dx=_math_derivative(a,x,variable)
    if op=='add':a.rule('supplied derivative sum rule');return _math_call('add',dx,_math_derivative(a,node['args'][1],variable))
    if op=='multiply':
        y=node['args'][1];a.rule('supplied derivative product rule')
        return _math_call('add',_math_call('multiply',dx,y),_math_call('multiply',x,_math_derivative(a,y,variable)))
    if op=='quotient':
        y=node['args'][1];a.condition(_math_key(y)+' != 0');a.rule('supplied quotient and chain rules')
        top=_math_call('add',_math_call('multiply',dx,y),a.opposite(_math_call('multiply',x,_math_derivative(a,y,variable))))
        return _math_call('quotient',top,_math_call('power',y,a.nat(2)))
    if op=='power':
        y=node['args'][1];a.rule('supplied power and chain rules')
        if not _math_depends(y,variable):
            return _math_call('multiply',_math_call('multiply',y,_math_call('power',x,_math_call('add',y,a.opposite(a.nat(1))))),dx)
        a.condition(_math_key(x)+' > 0 for real variable exponents')
        return _math_call('multiply',node,_math_call('add',_math_call('multiply',_math_derivative(a,y,variable),_math_call('log',x)),_math_call('multiply',y,_math_call('quotient',dx,x))))
    if op=='root':
        n=node['args'][1];degree=a.number(n)
        unused,remainder=a.divmod(degree,2) if degree is not None else (0,0)
        a.condition(_math_key(x)+(' != 0' if remainder else ' > 0'));a.rule('supplied implicit root derivative')
        return _math_call('quotient',dx,_math_call('multiply',n,_math_call('power',node,_math_call('add',n,a.opposite(a.nat(1))))))
    if op in ('sin','cos','exp','log'):
        a.rule('supplied elementary-function chain rule')
        if op=='log' and x.get('kind')=='call' and x['operation']=='abs':
            u=x['args'][0];a.condition(_math_key(u)+' != 0')
            return _math_call('quotient',_math_derivative(a,u,variable),u)
        factor={'sin':lambda:_math_call('cos',x),'cos':lambda:a.opposite(_math_call('sin',x)),
                'exp':lambda:node,'log':lambda:_math_call('quotient',a.nat(1),x)}[op]()
        if op=='log':a.condition(_math_key(x)+' > 0')
        return _math_call('multiply',factor,dx)
    return {'kind':'formal_derivative','variable':variable,'args':[node]}

def _math_integral(a,node,variable):
    a.tick();x={'kind':'variable','name':variable}
    if not _math_depends(node,variable):a.rule('supplied constant antiderivative');return _math_call('multiply',node,x)
    if node==x:a.rule('supplied natural-power antiderivative');return _math_call('quotient',_math_call('power',x,a.nat(2)),a.nat(2))
    if node.get('kind')=='opposite_role':return a.opposite(_math_integral(a,node['arg'],variable))
    if node.get('kind')=='call':
        op=node['operation'];args=node['args'];u=args[0]
        if op=='add':a.rule('supplied integral linearity');return _math_call('add',*(_math_integral(a,n,variable) for n in args))
        if op=='multiply':
            for side in (0,1):
                if not _math_depends(args[side],variable):
                    a.rule('supplied constant factor rule');return _math_call('multiply',args[side],_math_integral(a,args[1 if side==0 else 0],variable))
        if op=='quotient' and not _math_depends(args[1],variable):
            a.condition(_math_key(args[1])+' != 0');return _math_call('quotient',_math_integral(a,u,variable),args[1])
        if op=='quotient' and a.number(u)==1 and args[1]==x:
            a.condition(_math_key(x)+' != 0');a.rule('supplied logarithmic antiderivative');return _math_call('log',_math_call('abs',x))
        if op=='quotient' and not _math_depends(u,variable):
            return _math_call('multiply',u,_math_integral(a,_math_call('power',args[1],a.opposite(a.nat(1))),variable))
        if op=='root':return _math_integral(a,_math_call('power',u,_math_call('quotient',a.nat(1),args[1])),variable)
        if op=='power' and not _math_depends(args[1],variable):
            slope=_math_simplify(a,_math_derivative(a,u,variable))
            if not _math_depends(slope,variable) and a.number(slope)!=0:
                exponent=_math_simplify(a,_math_call('add',args[1],a.nat(1)))
                if a.fraction(slope) is None:a.condition(_math_key(slope)+' != 0')
                if a.number(exponent)==0:
                    a.condition(_math_key(u)+' != 0');a.rule('supplied affine logarithmic antiderivative')
                    return _math_call('quotient',_math_call('log',_math_call('abs',u)),slope)
                a.rule('supplied constant-exponent affine antiderivative')
                if a.number(args[1]) is None:a.condition(_math_key(u)+' > 0 on the selected real branch')
                return _math_call('quotient',_math_call('power',u,exponent),_math_call('multiply',exponent,slope))
        if op in ('sin','cos','exp'):
            slope=_math_simplify(a,_math_derivative(a,u,variable))
            if _math_depends(slope,variable) or a.number(slope)==0:return {'kind':'formal_integral','variable':variable,'args':[node]}
            if a.fraction(slope) is None:a.condition(_math_key(slope)+' != 0')
            a.rule('supplied elementary antiderivative')
            result=a.opposite(_math_call('cos',u)) if op=='sin' else _math_call('sin',u) if op=='cos' else node
            return _math_call('quotient',result,slope)
    return {'kind':'formal_integral','variable':variable,'args':[node]}

def _math_has_formal(node):
    return node.get('kind') in ('formal_integral','formal_derivative') or any(_math_has_formal(n) for n in node.get('args',[])) or ('arg'in node and _math_has_formal(node['arg']))

def _math_attempts_before(m,event):
    result={}
    for row in _math_state(m)['attempts']:
        if row['event']<event:result[row['request']]=row
    return result

def _math_compute(m,request,parent_attempts,effort,recording,event):
    a=_MathArithmetic(m,effort,recording);tree=None;op=request['operation'];latest=_math_attempts_before(m,event)
    try:
        if op=='parse':tree=_math_parse(a,request['text'])
        elif op=='import_symbolic':tree=_math_resolve(a,_sym_ref(request['source']),latest)
        else:
            trees=[]
            for pid in parent_attempts:
                if pid is None:raise _MathDeferred('parent work remains retained and unresolved')
                parent=_math_state(m)['attempts'][pid]
                if parent['status'] not in ('exact','exact_symbolic','conditional_symbolic','unresolved_formal'):raise _MathDeferred('parent work remains retained and unresolved')
                for condition in parent['conditions']:a.condition(condition)
                trees.append(_pr_copy.deepcopy(parent['result']))
            if op=='divide':tree=_math_call('quotient',*trees)
            elif op=='root':tree=_math_call('root',trees[0],a.nat(request['degree']))
            else:tree=trees[0]
        tree=_math_resolve(a,tree,latest)
        if op=='differentiate':tree=_math_derivative(a,tree,request['variable'])
        elif op=='integrate':tree=_math_integral(a,tree,request['variable'])
        elif op=='expand':tree=_math_expand(a,tree)
        tree=_math_simplify(a,tree)
        status='unresolved_formal' if _math_has_formal(tree) else 'conditional_symbolic' if a.conditions else 'exact' if a.fraction(tree) is not None else 'exact_symbolic'
        result={'status':status,'result':tree,'conditions':a.conditions,'rules':a.rules,
                'scope':'exact retained syntax and supplied symbolic transformations; not a discovered axiom or a physical law'}
        if op=='integrate':result['integration_constant']={'kind':'arbitrary_constant','independent_of':request['variable']}
        return result
    except (_MathDeferred,RecursionError) as exc:return {'status':'resource_deferred','result':None,'conditions':a.conditions,'rules':a.rules,'reason':str(exc) or 'interpreter recursion capacity; source retained'}
    except (_MathUndefined,SyntaxError) as exc:return {'status':'undefined','result':tree,'conditions':a.conditions,'rules':a.rules,'reason':str(exc)}

def _math_request(m,operation,parents=(),text=None,source=None,degree=None,variable='x',automatic=None):
    state=_math_state(m)
    if operation not in ('parse','import_symbolic')+MATH_LANES:raise ValueError('Unknown exact-math operation')
    arity=0 if operation in ('parse','import_symbolic') else 2 if operation=='divide' else 1
    if len(parents)!=arity or any(type(p)is not int or not 0<=p<len(state['records']) for p in parents):raise ValueError('Use retained math input IDs with the operator arity')
    if operation=='parse' and not isinstance(text,str):raise ValueError('Use math-parse EXPRESSION')
    if operation=='root' and (type(degree)is not int or degree<2):raise ValueError('Use a natural root degree of at least two')
    if operation=='import_symbolic' and (type(source)is not int or not 0<=source<len(_slot_rows(m,'symbolic'))):raise ValueError('Missing symbolic import')
    if not isinstance(variable,str) or not variable.isidentifier():raise ValueError('Use an identifier for the variable')
    row={'id':len(state['records']),'rule':MATH_RULE,'operation':operation,'parents':list(parents),'text':text,
         'source':source,'degree':degree,'variable':variable,'automatic':automatic,'event':m['_active_event'],'zero_nexus':'Z0'}
    state['records'].append(row);state['recipes'].append(_pr_copy.deepcopy(row));return row['id']

def _math_attempt(m,rid):
    state=_math_state(m);request=state['records'][rid];prior=[r for r in state['attempts'] if r['request']==rid]
    effort=MATH_EFFORT_PER_ATTEMPT*(len(prior)+1);latest=_math_attempts_before(m,m['_active_event']);parents=[latest[p]['id'] if p in latest else None for p in request['parents']]
    start=len(m['events']);assessment=_math_compute(m,request,parents,effort,True,m['_active_event'])
    row={'id':len(state['attempts']),'request':rid,'parent_attempts':parents,'effort':effort,
         'event':m['_active_event'],'successor_events':[e['id'] for e in m['events'][start:] if e['domain']=='rational' and e['operation']=='S'],
         'zero_nexus':'Z0',**assessment}
    state['attempts'].append(row);state['attempt_recipes'].append(_pr_copy.deepcopy(row))
    # Each attempt gets its own return node. Failed/deferred paths remain visible.
    zero_core(m,'0-structures',operation='open_record',operation_name='import_math',source={'id':row['id']})
    m['feedback'].append({'source':{'archive':'exact_math_attempts','id':row['id']},'zero_nexus':'Z0',
        'targets':['open_structural_frontier','symbolic_archive','math_work_history'],'status':row['status']})
    return row['id']

def _math_frontier_step(m):
    state=_math_state(m);idx=len(state['frontier']);last=state['frontier'][-1] if idx else None
    cursor=[0,0] if last is None else _pf_next(last['cursor'],2) if last['advanced'] else last['cursor']
    rid,ordinal=_pf_tuple(cursor,2);attempt=None;status='awaiting_retained_input';available=rid<len(state['records'])
    if available:
        previous=[r for r in state['attempts'] if r['request']==rid]
        if previous and previous[-1]['status'] in ('exact','exact_symbolic','conditional_symbolic','undefined'):status='completed_request_retained'
        elif ordinal==len(previous):attempt=zero_core(m,'math',operation='attempt',operands=(rid,));status='attempt_retained'
        else:status='prior_or_later_attempt_position'
    receipt={'id':idx,'cursor':cursor,'request':rid,'ordinal':ordinal,'attempt':attempt,'status':status,
             'advanced':available,'event':m['_active_event'],'zero_nexus':'Z0'}
    state['frontier'].append(receipt);state['frontier_recipes'].append(_pr_copy.deepcopy(receipt));return idx


def _math_service(m,budget=4):
    if type(budget)is not int or not 0<=budget<=1000:raise ValueError('Math work allowance from 0 to 1000')
    state=_math_state(m);imported={r['source'] for r in state['records'] if r['operation']=='import_symbolic'}
    # Import existing expressions, never a selected list of expected answers.
    for source in [r['id'] for r in _slot_rows(m,'symbolic') if r['id'] not in imported][:2]:
        zero_core(m,'math',operation='request',operation_name='import_symbolic',source=source)
    if not state['records']:return _math_report(m)
    for unused in range(budget):zero_core(m,'math',operation='frontier_step')
    # Operator input enumeration is separate from effort/retry enumeration.
    n=sum(r['automatic'] is not None for r in state['records']);lane=MATH_LANES[n%len(MATH_LANES)]
    earlier=[r for r in state['records'] if r['automatic'] is not None and r['operation']==lane]
    cursor=[0,0] if not earlier else _pf_next(earlier[-1]['automatic'],2)
    pair=_pf_tuple(cursor,2)
    if max(pair)<len(state['records']):
        parents=pair if lane=='divide' else [pair[0]]
        zero_core(m,'math',operation='request',operation_name=lane,parents=parents,
                  degree=pair[1]+2 if lane=='root' else None,automatic=cursor)
    return _math_report(m)

def _math_report(m):
    state=_math_state(m);latest={r['request']:r for r in state['attempts']};counts={}
    for row in latest.values():counts[row['status']]=counts.get(row['status'],0)+1
    return {'requests':len(state['records']),'retained_attempts':len(state['attempts']),'latest_statuses':counts,
            'numeric_primitives':['S'],'automatic_lanes':list(MATH_LANES),'desired_answer':None,'success_stop_condition':None,
            'terminal_effort_limit':None,'scope':'exact rational ratios, real algebraic roots, symbolic algebra, declared differentiation and selected antiderivatives; unsupported forms retained and fairly revisited'}

_math_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='math':
        if operation=='request':
            options=dict(kwargs);op=options.pop('operation_name');return _math_request(m,op,**options)
        if operation=='attempt':return _math_attempt(m,*operands)
        if operation=='frontier_step':return _math_frontier_step(m)
        if operation=='service':return _math_service(m,**kwargs)
        raise ValueError('Unknown exact-math gateway operation')
    return _math_dispatch_previous(m,domain,operation,operands,kwargs)

_math_tree_previous=_open_tree
def _open_tree(m,idx):
    row=_open_state(m)['records'][idx]
    if row['operation']=='import_math':return {'kind':'math_reference','id':_math_state(m)['attempts'][row['source']['id']]['request'],'attempt':row['source']['id']}
    return _math_tree_previous(m,idx)

_math_poly_previous=_zstruct_poly
def _zstruct_poly(m,node):
    if node.get('kind')=='math_reference':
        attempt=_math_state(m)['attempts'][node['attempt']]
        if attempt['status'] not in ('exact','exact_symbolic'):raise _ZeroStructureUnsupported('exact-math conditions or pending work retained')
        tree=attempt['result']
        if tree.get('kind')=='opposite_role':return {k:-v for k,v in _zstruct_poly(m,tree['arg']).items()}
        return _math_poly_previous(m,tree)
    return _math_poly_previous(m,node)

_math_recover_previous=_zstruct_recover_extensions
def _zstruct_recover_extensions(m):
    changed=_math_recover_previous(m);state=m.get('exact_math')
    if state is None:return changed
    for field,recipes in (('records','recipes'),('attempts','attempt_recipes'),('frontier','frontier_recipes')):
        actual={r['id']:r for r in state[field]}
        if len(actual)!=len(state[field]):raise ValueError('Duplicate exact-math evidence')
        restored=[]
        for recipe in state[recipes]:
            row=actual.pop(recipe['id'],None)
            if row is None:row=_pr_copy.deepcopy(recipe);changed=True
            elif row!=recipe:raise ValueError('Changed exact-math evidence')
            restored.append(row)
        if actual:raise ValueError('Untracked exact-math evidence')
        state[field]=restored
    return changed

_math_replay_previous=_slot_replay
def _slot_replay(m):
    state=m.get('exact_math')
    if state is not None:
        if state['rule']!=MATH_RULE:raise ValueError('Unknown exact-math schema')
        for field,recipes in (('records','recipes'),('attempts','attempt_recipes'),('frontier','frontier_recipes')):
            if state[field]!=state[recipes] or [r['id'] for r in state[field]]!=list(range(len(state[field]))):raise ValueError('Exact-math recipe or identity conflict')
        for row in state['records']:
            op=row['operation'];arity=0 if op in ('parse','import_symbolic') else 2 if op=='divide' else 1
            if (row['rule']!=MATH_RULE or row['zero_nexus']!='Z0' or op not in ('parse','import_symbolic')+MATH_LANES or len(row['parents'])!=arity or
                any(type(p)is not int or not 0<=p<row['id'] for p in row['parents']) or
                not isinstance(row['variable'],str) or not row['variable'].isidentifier()):raise ValueError('Exact-math request ancestry changed')
            if op=='parse' and not isinstance(row['text'],str):raise ValueError('Exact-math input text changed')
            if op=='root' and (type(row['degree'])is not int or row['degree']<2):raise ValueError('Exact-math root degree changed')
            if op=='import_symbolic':
                source=row['source'];symbolic=_slot_rows(m,'symbolic')
                if type(source)is not int or not 0<=source<len(symbolic) or symbolic[source]['retention_event']>=row['event']:raise ValueError('Exact-math symbolic source changed')
            event=m['events'][row['event']]
            if event['domain']!='math' or event['operation']!='request' or event['status']!='complete':raise ValueError('Exact-math request lost its gateway')
        for row in state['attempts']:
            rid=row['request']
            if type(rid)is not int or not 0<=rid<len(state['records']):raise ValueError('Exact-math attempt request changed')
            request=state['records'][rid];previous=[r for r in state['attempts'][:row['id']] if r['request']==rid]
            latest=_math_attempts_before(m,row['event']);parents=[latest[p]['id'] if p in latest else None for p in request['parents']]
            if row['parent_attempts']!=parents or row['effort']!=MATH_EFFORT_PER_ATTEMPT*(len(previous)+1):raise ValueError('Exact-math effort or parent history changed')
            expected=_math_compute(m,request,parents,row['effort'],False,row['event'])
            if any(row.get(k)!=v for k,v in expected.items()) or set(row)!=set(expected)|{'id','request','parent_attempts','effort','event','successor_events','zero_nexus'}:raise ValueError('Exact-math result or conditions changed')
            if row['zero_nexus']!='Z0' or row['event']<=request['event']:raise ValueError('Exact-math attempt source changed')
            event=m['events'][row['event']]
            if event['domain']!='math' or event['operation']!='attempt' or event['status']!='complete':raise ValueError('Exact-math attempt gateway changed')
            if row['successor_events']!=[e['id'] for e in m['events'] if e.get('parent')==row['event'] and e['domain']=='rational' and e['operation']=='S']:
                raise ValueError('Exact-math successor trace incomplete')
            for eid in row['successor_events']:
                event=m['events'][eid]
                if eid<=row['event'] or event['domain']!='rational' or event['operation']!='S' or event['status']!='complete' or event['after']!=event['before']+1:raise ValueError('Exact-math S construction evidence changed')
        cursor=[0,0]
        for row in state['frontier']:
            if row['cursor']!=cursor or [row['request'],row['ordinal']]!=_pf_tuple(cursor,2):raise ValueError('Exact-math fair frontier changed')
            available=sum(r['event']<row['event'] for r in state['records'])>row['request']
            previous=[r for r in state['attempts'] if r['request']==row['request'] and r['event']<row['event']]
            status='awaiting_retained_input' if not available else 'completed_request_retained' if previous and previous[-1]['status'] in ('exact','exact_symbolic','conditional_symbolic','undefined') else 'attempt_retained' if row['ordinal']==len(previous) else 'prior_or_later_attempt_position'
            event=m['events'][row['event']]
            if (row['advanced']!=available or row['status']!=status or row['zero_nexus']!='Z0' or
                event['domain']!='math' or event['operation']!='frontier_step' or event['status']!='complete'):
                raise ValueError('Exact-math scheduling evidence changed')
            if (row['attempt'] is not None)!=(status=='attempt_retained'):raise ValueError('Exact-math scheduled attempt missing')
            if row['attempt'] is not None:
                attempt=state['attempts'][row['attempt']]
                if attempt['request']!=row['request'] or attempt['event']<=row['event']:raise ValueError('Exact-math scheduled attempt changed')
            cursor=_pf_next(cursor,2) if row['advanced'] else cursor
    return _math_replay_previous(m)

_math_report_previous=_slot_report
def _slot_report(m):
    report=_math_report_previous(m);report['exact_math']=_math_report(m)
    report['deferred']=[item for item in report['deferred'] if item not in ('rational division','roots and general symbolic algebra','general calculus beyond the supplied polynomial verifier')]
    report['deferred']+=['unsupported symbolic forms and antiderivatives; retained for continuing work','whole-engine reduction to S remains incomplete']
    report['blocker']='exact scalar workers active; general symbolic decision procedures remain incomplete'
    return report

def _math_display(node):
    if node is None:return 'pending retained work'
    kind=node.get('kind')
    if kind=='reference':return str(node['ref']['id']) if node['ref']['archive']=='rational' else str(node['ref'])
    if kind=='variable':return node['name']
    if kind=='imaginary_unit_role':return 'I'
    if kind=='opposite_role':return '-('+_math_display(node['arg'])+')'
    if kind=='algebraic_root':return 'principal_complex_root('+_math_display(node['radicand'])+','+_math_display(node['degree'])+')'
    if kind in ('formal_derivative','formal_integral'):return kind+'('+_math_display(node['args'][0])+', '+node['variable']+')'
    if kind=='call':
        op=node['operation'];args=[_math_display(n) for n in node['args']]
        if op in ('add','multiply','quotient','power'):return '('+args[0]+{'add':'+','multiply':'*','quotient':'/','power':'**'}[op]+args[1]+')'
        return op+'('+', '.join(args)+')'
    return json.dumps(node)

_math_query_previous=_slot_query
def _slot_query(m,text):
    command=text.strip();parts=command.split();head=parts[0].lower() if parts else ''
    try:
        if head in ('math','math-index') and len(parts)==1:
            print(json.dumps(_math_report(m),indent=2))
            if head=='math-index':
                latest={r['request']:r for r in _math_state(m)['attempts']}
                for row in _math_state(m)['records']:
                    attempt=latest.get(row['id'],{'status':'queued','result':None})
                    print(row['id'],row['operation'],'|',attempt['status'],'|',_math_display(attempt['result'])+(' + C' if 'integration_constant' in attempt else ''))
            return
        if head=='math' and len(parts)==2:print(json.dumps(_math_state(m)['records'][int(parts[1])],indent=2));return
        if head=='math-run':
            zero_core(m,'math',operation='service',budget=int(parts[1]));print(json.dumps(_math_report(m),indent=2));return
        names={'math-parse':'parse','math-simplify':'simplify','math-expand':'expand','math-divide':'divide',
               'math-root':'root','math-differentiate':'differentiate','math-integrate':'integrate','math-import':'import_symbolic'}
        if head in names:
            op=names[head];options={}
            def request_id(token):return len(_math_state(m)['records'])-1 if token.lower()=='last' else int(token)
            if op=='parse':options['text']=command.partition(' ')[2].strip()
            elif op=='import_symbolic':options['source']=int(parts[1])
            else:
                options['parents']=[request_id(p) for p in parts[1:3]] if op=='divide' else [request_id(parts[1])]
                if op=='root':options['degree']=int(parts[2])
                if op in ('differentiate','integrate'):options['variable']=parts[2] if len(parts)>2 else 'x'
            rid=zero_core(m,'math',operation='request',operation_name=op,**options)
            aid=zero_core(m,'math',operation='attempt',operands=(rid,));attempt=_math_state(m)['attempts'][aid]
            print('Retained math request:',rid,'|',attempt['status'],'|',_math_display(attempt['result'])+(' + C' if 'integration_constant' in attempt else ''))
            if attempt['conditions']:print('Conditions:',json.dumps(attempt['conditions']))
            if attempt.get('reason'):print('Retained reason:',attempt['reason'])
            return
        result=_math_query_previous(m,text)
        if head in ('help','?'):print('math / math-index / math N: historical supplied-solver records; new math-* requests are retained unresolved. Use open/open-run for untargeted syntax; principles shows the active policy.')
        return result
    except (ValueError,IndexError) as exc:print('Math command not submitted:',str(exc))
    finally:_slot_save(m,memory_path())

_math_open_service_previous=_open_service
def _open_service(m,budget=12):
    report=_math_open_service_previous(m,budget=budget)
    zero_core(m,'open-syntax',operation='service',budget=4)
    return report


# ============================================================
# V4.11.1: open syntax is the default. Supplied scalar solvers are explicit
# command tools only. Existing solver history stays retained and replayable.
# No terminal generation depth, desired answer or success-stop condition.
# ============================================================
OPEN_MATH_SYNTAX_RULE='zero_open_math_syntax_v1'
OPEN_MATH_SYNTAX_UNARY=('formal_integral',)
OPEN_MATH_SYNTAX_BINARY=('quotient','root')

def _open_math_syntax_state(m):return m.setdefault('open_math_syntax',{'rule':OPEN_MATH_SYNTAX_RULE,'records':[],'recipes':[]})

def _open_math_syntax_next(cursor):
    shell,position=cursor;position+=1
    count=len(OPEN_MATH_SYNTAX_UNARY)+len(OPEN_MATH_SYNTAX_BINARY)*(2*shell+1)
    return [shell+1,0] if position==count else [shell,position]

def _open_math_syntax_recipe(cursor):
    shell,position=cursor
    if position<len(OPEN_MATH_SYNTAX_UNARY):return OPEN_MATH_SYNTAX_UNARY[position],[shell]
    position-=len(OPEN_MATH_SYNTAX_UNARY);pair,operator=divmod(position,len(OPEN_MATH_SYNTAX_BINARY))
    return OPEN_MATH_SYNTAX_BINARY[operator],([shell,pair] if pair<=shell else [pair-shell-1,shell])

def _open_math_syntax_record(m,cursor):
    state=_open_math_syntax_state(m);expected=[0,0] if not state['records'] else _open_math_syntax_next(state['records'][-1]['cursor'])
    if cursor!=expected:raise ValueError('Open mathematical syntax cursor changed')
    op,parents=_open_math_syntax_recipe(cursor)
    if any(type(p)is not int or not 0<=p<len(_open_state(m)['records']) for p in parents):raise ValueError('Open syntax requires retained parent structures')
    row={'id':len(state['records']),'rule':OPEN_MATH_SYNTAX_RULE,'operation':op,'parents':parents,
         'cursor':list(cursor),'event':m['_active_event'],'zero_nexus':'Z0','status':'experimental_syntax'}
    state['records'].append(row);state['recipes'].append(_pr_copy.deepcopy(row))
    zero_core(m,'0-structures',operation='open_record',operation_name='import_open_math_syntax',source={'id':row['id']})
    m['feedback'].append({'source':{'archive':'open_math_syntax','id':row['id']},'zero_nexus':'Z0',
        'targets':['open_structural_frontier','symbolic_archive'],'status':'experimental_syntax'})
    return row['id']

def _open_math_syntax_service(m,budget=4):
    if type(budget)is not int or not 0<=budget<=1000:raise ValueError('Open syntax work allowance from 0 to 1000')
    for unused in range(budget):
        state=_open_math_syntax_state(m);cursor=[0,0] if not state['records'] else _open_math_syntax_next(state['records'][-1]['cursor'])
        unused,parents=_open_math_syntax_recipe(cursor)
        if max(parents)>=len(_open_state(m)['records']):break
        zero_core(m,'open-syntax',operation='record',operands=(cursor,))
    return len(_open_math_syntax_state(m)['records'])

_open_default_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='open-syntax':
        if operation=='service':return _open_math_syntax_service(m,**kwargs)
        if operation=='record':return _open_math_syntax_record(m,*operands)
        raise ValueError('Unknown open mathematical syntax operation')
    return _open_default_dispatch_previous(m,domain,operation,operands,kwargs)

_open_default_tree_previous=_open_tree
def _open_tree(m,idx):
    node=_open_state(m)['records'][idx]
    if node['operation']=='import_open_math_syntax':
        syntax=_open_math_syntax_state(m)['records'][node['source']['id']];args=[_open_ref(p) for p in syntax['parents']]
        if syntax['operation']=='formal_integral':return {'kind':'formal_integral','variable':'x','args':args}
        return _math_call(syntax['operation'],*args)
    return _open_default_tree_previous(m,idx)

_open_default_recover_previous=_zstruct_recover_extensions
def _zstruct_recover_extensions(m):
    changed=_open_default_recover_previous(m);state=m.get('open_math_syntax')
    if state is None:return changed
    actual={r['id']:r for r in state['records']}
    if len(actual)!=len(state['records']):raise ValueError('Duplicate open syntax identity')
    restored=[]
    for recipe in state['recipes']:
        row=actual.pop(recipe['id'],None)
        if row is None:row=_pr_copy.deepcopy(recipe);changed=True
        elif row!=recipe:raise ValueError('Open syntax evidence changed')
        restored.append(row)
    if actual:raise ValueError('Untracked open syntax evidence')
    state['records']=restored;return changed

_open_default_replay_previous=_slot_replay
def _slot_replay(m):
    state=m.get('open_math_syntax')
    if state is not None:
        if state['rule']!=OPEN_MATH_SYNTAX_RULE or state['records']!=state['recipes']:raise ValueError('Open mathematical syntax recipe conflict')
        cursor=[0,0];nodes=_open_state(m)['records']
        for idx,row in enumerate(state['records']):
            op,parents=_open_math_syntax_recipe(cursor);event=m['events'][row['event']]
            if (row['id']!=idx or row['rule']!=OPEN_MATH_SYNTAX_RULE or row['cursor']!=cursor or row['operation']!=op or row['parents']!=parents or
                row['status']!='experimental_syntax' or row['zero_nexus']!='Z0' or event['domain']!='open-syntax' or event['operation']!='record' or event['status']!='complete' or
                any(not 0<=p<len(nodes) or nodes[p]['event']>=row['event'] for p in parents)):
                raise ValueError('Open syntax enumeration or provenance changed')
            cursor=_open_math_syntax_next(cursor)
        for node in nodes:
            if node['operation']=='import_open_math_syntax':
                rid=node['source']['id']
                if type(rid)is not int or not 0<=rid<len(state['records']) or state['records'][rid]['event']>=node['event']:
                    raise ValueError('Open syntax return source changed')
    return _open_default_replay_previous(m)

_open_default_math_report_previous=_math_report
def _math_report(m):
    report=_open_default_math_report_previous(m)
    report.update(execution_mode='explicit math commands only',automatic_in_default_run=False,
                  scope='optional supplied scalar transformations; retained solver history is not an emergence claim')
    return report

_open_default_report_previous=_slot_report
def _slot_report(m):
    report=_open_default_report_previous(m);state=m.get('open_math_syntax',{});rows=state.get('records',[])
    report['open_exploration'].update(mode='open-ended structural exploration',
        additional_grammar=list(OPEN_MATH_SYNTAX_UNARY+OPEN_MATH_SYNTAX_BINARY),
        additional_syntax_nodes=len(rows),additional_next_cursor=_open_math_syntax_next(rows[-1]['cursor']) if rows else [0,0],
        supplied_scalar_solvers_automatic=False,desired_answer=None,success_stop_condition=None)
    report['blocker']='uninterpreted constructions remain retained; open syntax generation continues without a terminal depth'
    report['scope']='Open structural, symbolic and typed physical exploration through Z0; supplied scalar solver tools require explicit commands; existing declared verifiers remain explicit.'
    return report


# ============================================================
# V4.11.2: saved open scheduling and versioned work allowances.
# Historical algorithms remain for replay; new scalar-solver execution is
# retained as an unresolved request rather than used as a discovery worker.
# ============================================================
from contextlib import contextmanager as _principles_contextmanager
PRINCIPLES_RULE='z0_open_scheduling_and_allowances_v1'
_PRINCIPLES_CONTEXT=None
_PRINCIPLES_VALIDATING=False

def _principles_limits(scale):
    if type(scale)is not int or scale<1:raise ValueError('Invalid exploration allowance scale')
    return {'rule':PRINCIPLES_RULE,'scale':scale,'depth':8*scale,'units':16*scale,
        'nodes':64*scale,'interpretation':256*scale,'degree':8*scale,
        'coefficient':4096*scale,'power':6*scale,'dimensions':256*scale}

def _principles_current():return _pr_copy.deepcopy(_PRINCIPLES_CONTEXT)
def _principles_limit(name,legacy):return legacy if _PRINCIPLES_CONTEXT is None else _PRINCIPLES_CONTEXT[name]

@_principles_contextmanager
def _principles_scope(policy):
    global _PRINCIPLES_CONTEXT,SLOT_MAX_DEPTH,SLOT_MAX_UNITS,Z1I_MAX_NODES
    previous=(_PRINCIPLES_CONTEXT,SLOT_MAX_DEPTH,SLOT_MAX_UNITS,Z1I_MAX_NODES)
    if policy is not None and policy!=_principles_limits(policy.get('scale')):
        raise ValueError('Changed recorded exploration allowance')
    _PRINCIPLES_CONTEXT=policy
    SLOT_MAX_DEPTH=8 if policy is None else policy['depth']
    SLOT_MAX_UNITS=16 if policy is None else policy['units']
    Z1I_MAX_NODES=64 if policy is None else policy['nodes']
    try:yield
    finally:_PRINCIPLES_CONTEXT,SLOT_MAX_DEPTH,SLOT_MAX_UNITS,Z1I_MAX_NODES=previous

def _principles_state(m):
    return m.setdefault('principles',{'rule':PRINCIPLES_RULE,'records':[],'recipes':[]})

def _principles_receipt(m,kind,**payload):
    state=_principles_state(m)
    row={'id':len(state['records']),'kind':kind,'zero_nexus':'Z0','event':m['_active_event'],**_pr_copy.deepcopy(payload)}
    state['records'].append(row);state['recipes'].append(_pr_copy.deepcopy(row));return row

def _principles_last(m,kind,lane=None):
    for row in reversed(m.get('principles',{}).get('records',[])):
        if row['kind']==kind and (lane is None or row.get('lane')==lane):return row
    return None

def _principles_epoch(m):
    row=_principles_last(m,'epoch')
    return row['policy'] if row else None

# These entry points interpret a single retained record under the allowance
# recorded with it. Untagged historical records always use their old allowance.
def _principles_record_checker(function):
    def check(m,row,*args,**kwargs):
        with _principles_scope(row.get('execution_policy')):return function(m,row,*args,**kwargs)
    return check
_zi_check_attempt=_principles_record_checker(_zi_check_attempt)
_z1_role_check=_principles_record_checker(_z1_role_check)
_six_role_check=_principles_record_checker(_six_role_check)
_path_role_check=_principles_record_checker(_path_role_check)
_sym_check=_principles_record_checker(_sym_check)
_zstruct_calculus_check=_principles_record_checker(_zstruct_calculus_check)
_physical_expected=_principles_record_checker(_physical_expected)

def _principles_check_certificate(m,row):
    with _principles_scope(row.get('execution_policy')):
        return _zstruct_certificate(m,_zstruct_state(m)['records'][row['structure']]['payload'])

def _principles_qty_expected(m,row):
    with _principles_scope(row.get('execution_policy')):
        return _qty_expected(m,row['operation'],row['parents'],row['role'])

def _principles_typed_expected(m,row):
    with _principles_scope(row.get('execution_policy')):return _typed_expected(m,row['open_node'])

def _physical_current_assessments(m,limit=None):
    rows=_physical_state(m)['records'];limit=len(rows) if limit is None else limit;current=[]
    for row in rows[:limit]:
        parents=[dict(rows[p],assessment=current[p]) for p in row['parents']]
        with _principles_scope(row.get('execution_policy')):
            try:assessment=_physical_assess_v2(m,row,parents)
            except _ZeroStructureUnsupported as exc:
                assessment={'status':'unresolved','dimensions':None,'reason':str(exc),'physical_law_verified':False}
        current.append(assessment)
    return current

# Core construction feedback queues no selected peers and has no terminal depth.
def _slot_feedback(m,idx):
    rec=_slot_rows(m,'complex')[idx];_slot_queue(m,'i',[idx]);ancestor=rec
    while ancestor['operation']=='i':
        ancestor=_slot_rows(m,'complex')[ancestor['parents'][0]]
        _slot_queue(m,'relate',[ancestor['id'],idx])
    m['feedback'].append({'source':_slot_ref('complex',idx),
        'targets':['roles','open_pair_frontier','path_relations'],'zero_nexus':'Z0'})
    zero_core(m,'discovery',operation='observe',operands=(idx,))

# Bind from an actual archived path; schedule all retained inputs separately.
def _path_bind(m,idx):
    root,path=_path_chain(m,idx)
    if len(path)<2:return None
    state=_path_state(m);key=str(len(path))
    if key in state['candidates']:return state['candidates'][key]
    counter=_slot_ensure_counter(m,1);label='path_i_'+key
    body={'operations':['i' for _ in path],'source_input':root,'source_path':path,
        'scope':'retained unary i-composition; continuing work allowances',
        'general_law_discovered':False,'zero_nexus':'Z0'}
    rec={'kind':'operation','label':label,'operation':'bind_retained_pathway','rule':PATH_ROLE,
        'parents':[2],'sources':[_slot_ref('rational',counter),_slot_ref('roles',4)]+
            [_slot_ref('complex',p) for p in [root]+path],
        'body':body,'path':['0','S0',label],'depth':2,'slot':{'counter':counter,'foundation_id':counter}}
    rid=zero_core(m,'roles',operation='record',record=rec);state['candidates'][key]=rid
    m['feedback'].append({'source':_slot_ref('roles',rid),'targets':['open_pathway_frontier'],
        'zero_nexus':'Z0','status':'candidate_bound'});return rid

# A diagonal over (task ID, revisit ordinal) gives every retained job repeated
# opportunities. Completed jobs are skipped; deferred evidence stays archived.
def _principles_select(m,lane):
    queue=m['queue'] if lane=='core' else _z1_state(m)['queue'] if lane=='z1' else _six_state(m)['queue']
    last=_principles_last(m,'selection',lane);cursor=[0,0] if last is None else last['next_cursor']
    selected=None;steps=[]
    for unused in range(32):
        index,visit=_pf_tuple(cursor,2)
        if index>=len(queue):
            steps.append({'cursor':cursor,'available':False,'queue_length':len(queue)})
            cursor=_pf_next(cursor,2);continue
        task=queue[index];status=task['status']
        eligible=status in ('pending','size_deferred','depth_deferred','resource_deferred','deferred') or (lane=='z1' and status=='no_applicable_slots')
        steps.append({'cursor':cursor,'available':True,'queue_length':len(queue),'index':index,
            'visit':visit,'status':status,'eligible':eligible,
            'source':{key:_pr_copy.deepcopy(value) for key,value in task.items() if key in ('operation','kind','parents','source','source_slot','cursor','permutation','key')}})
        cursor=_pf_next(cursor,2)
        if eligible:selected=index;break
    _principles_receipt(m,'selection',lane=lane,steps=steps,next_cursor=cursor,selected=selected)
    return None if selected is None else queue[selected]

def _slot_next(m):return zero_core(m,'principles',operation='select',operands=('core',))
def _z1_next(m):return zero_core(m,'principles',operation='select',operands=('z1',))
def _six_next(m):return zero_core(m,'principles',operation='select',operands=('six',))

_principles_task_previous=_slot_task
def _slot_task(m,task):return zero_core(m,'principles',operation='core_attempt',operands=(task,))

def _principles_core_attempt(m,task):
    signature={'operation':task['operation'],'parents':list(task['parents'])}
    attempts=sum(row['kind']=='core_attempt' and row.get('task')==signature for row in _principles_state(m)['records'])
    epoch=_principles_epoch(m);scale=max(attempts+1,(epoch or {'scale':1})['scale'])
    policy=_principles_limits(scale);start=len(_slot_rows(m,'complex'))
    with _principles_scope(policy):status=_principles_task_previous(m,task)
    _principles_receipt(m,'core_attempt',task=signature,policy=policy,status=status,
        result_range=[start,len(_slot_rows(m,'complex'))])
    return status

# Enumerate ordered retained pairs. The operation order is fixed, never scored.
def _principles_pairs(m,budget):
    for unused in range(budget):
        last=_principles_last(m,'pair');cursor=[0,0] if last is None else last['next_cursor']
        operator=0 if last is None else last['next_operator'];left,right,visit=_pf_tuple(cursor,3);parents=[left,right]
        available=max(parents)<len(_slot_rows(m,'complex'));op=('add','multiply')[operator]
        if available:_slot_queue(m,op,parents)
        _principles_receipt(m,'pair',cursor=cursor,parents=parents,operation=op,available=available,
            next_cursor=_pf_next(cursor,3) if operator==1 else cursor,
            next_operator=(operator+1)%2)

def _principles_pathways(m,budget):
    for unused in range(budget):
        last=_principles_last(m,'pathway_input');cursor=[0,0] if last is None else last['next_cursor']
        choice,input_id,visit=_pf_tuple(cursor,3);roles=[r['id'] for r in _slot_rows(m,'roles') if r.get('rule')==PATH_ROLE]
        available=choice<len(roles) and input_id<len(_slot_rows(m,'complex'))
        rid=roles[choice] if choice<len(roles) else None
        if available:_slot_queue(m,'execute_pathway',[rid,input_id])
        _principles_receipt(m,'pathway_input',cursor=cursor,role=rid,input=input_id,available=available,
            next_cursor=_pf_next(cursor,3))

# Self-pairs and all peers belong to the same saved enumeration, with no
# first-three/last-three sample pool in answer feedback.
def _six_schedule(m,rid,idx):
    _six_job(m,rid,'double',[idx,idx]);_six_job(m,rid,'rotate',[idx])
    for permutation in ZI_POLICIES:_six_job(m,rid,'Zi',[idx,idx],list(permutation))
    m['feedback'].append({'source':_slot_ref('roles',rid),'targets':['open_answer_pair_frontier'],
        'zero_nexus':'Z0','status':'retained_for_enumeration'})

def _principles_answer_pairs(m,budget):
    for unused in range(budget):
        last=_principles_last(m,'answer_pair');cursor=[0,0] if last is None else last['next_cursor']
        operator=0 if last is None else last['next_operator'];choice,peer,visit=_pf_tuple(cursor,3)
        entries=list(_six_state(m)['entries'].values());available=choice<len(entries) and peer<len(_slot_rows(m,'complex'))
        entry=entries[choice] if choice<len(entries) else None
        ready=available and entry['status']=='fed' and entry['embedding'] is not None
        if ready:_six_job(m,entry['slot_role'],('add','multiply')[operator],[entry['embedding'],peer])
        # Unavailable and unfed tuples recur on later diagonal visits.
        _principles_receipt(m,'answer_pair',cursor=cursor,operator=operator,available=available,ready=ready,
            slot_role=None if entry is None else entry['slot_role'],peer=peer,
            next_cursor=_pf_next(cursor,3) if operator==1 else cursor,
            next_operator=(operator+1)%2)

# Fair Zi generation includes every retained left/right/power tuple. The old
# selected i-action demonstration frames are no longer injected by this service.
def _zi_service(m,budget=ZI_FRAME_BUDGET):
    return zero_core(m,'principles',operation='zi_service',budget=budget)

def _principles_zi_service(m,budget=ZI_FRAME_BUDGET):
    for unused in range(budget):
        last=_principles_last(m,'zi_frame');cursor=[0,0] if last is None else last['next_cursor']
        operator=0 if last is None else last['next_operator'];left,right,power,visit=_pf_tuple(cursor,4)
        available=max(left,right)<len(_slot_rows(m,'complex')) and power<len(m['expressions'])
        frame_id=None;attempts=[]
        if available:
            frame=_zi_frame(left,('add','multiply')[operator],right,power)
            frame_id=len(_zi_state(m)['frames']);_zi_state(m)['frames'].append(_pr_copy.deepcopy(frame))
            for permutation in ZI_POLICIES:
                attempts.append(zero_core(m,'Zi',operation='attempt',operands=(frame,permutation))['id'])
        _principles_receipt(m,'zi_frame',cursor=cursor,operator=operator,inputs=[left,right,power],
            available=available,frame=frame_id,attempts=attempts,
            next_cursor=_pf_next(cursor,4) if operator==1 else cursor,
            next_operator=(operator+1)%2)
    # Revisit all saved attempts by (attempt ID, revisit ordinal); only an
    # unresolved/resource-deferred input needs another retained interpretation.
    last=_principles_last(m,'zi_retry');cursor=[0,0] if last is None else last['next_cursor']
    idx,visit=_pf_tuple(cursor,2);attempts=_zi_state(m)['attempts'];available=idx<len(attempts);result=None
    if available and attempts[idx]['status'] in ('resource_deferred','needs_role_rule'):
        old=attempts[idx];result=zero_core(m,'Zi',operation='attempt',operands=(old['input'],old['permutation'],old['role_id']))['id']
    _principles_receipt(m,'zi_retry',cursor=cursor,source=idx,visit=visit,available=available,result=result,
        next_cursor=_pf_next(cursor,2))
    zero_core(m,'Zi',operation='register');return _zi_report(m)

# Reassessments are separate immutable receipts. Original meanings and outcomes
# are preserved, including unresolved syntax with no supplied interpreter.
def _principles_interpretation_expected(m,lane,idx,policy):
    with _principles_scope(policy):
        if lane=='symbolic':return _sym_assess(m,_slot_rows(m,'symbolic')[idx]['expression'])
        if lane=='typed':return _typed_expected(m,_typed_state(m)['records'][idx]['open_node'])
        if lane=='quantity':
            row=_qty_state(m)['records'][idx];return _qty_expected(m,row['operation'],row['parents'],row['role'])
        if lane=='physical':
            row=dict(_physical_state(m)['records'][idx],execution_policy=policy,assessment_rule=PHYSICAL_ASSESSMENT_RULE)
            return _physical_expected(m,row)
    raise ValueError('Unknown retained interpretation domain')

def _principles_interpretation_service(m,budget):
    lanes=('symbolic','typed','quantity','physical')
    for unused in range(budget):
        last=_principles_last(m,'interpretation');ordinal=0 if last is None else last['ordinal']+1
        lane=lanes[ordinal%len(lanes)];prior=_principles_last(m,'interpretation',lane)
        cursor=[0,0] if prior is None else prior['next_cursor'];idx,visit=_pf_tuple(cursor,2)
        rows=(_slot_rows(m,'symbolic') if lane=='symbolic' else _typed_state(m)['records'] if lane=='typed'
              else _qty_state(m)['records'] if lane=='quantity' else _physical_state(m)['records'])
        available=idx<len(rows);policy=_principles_current() or _principles_limits(1);assessment=None
        if available:
            try:assessment=_principles_interpretation_expected(m,lane,idx,policy)
            except _ZeroStructureUnsupported as exc:assessment={'status':'unresolved','reason':str(exc)}
        row=_principles_receipt(m,'interpretation',ordinal=ordinal,lane=lane,cursor=cursor,
            source=idx,visit=visit,available=available,assessment=assessment,policy=policy,next_cursor=_pf_next(cursor,2))
        if available:
            zero_core(m,'0-structures',operation='open_record',operation_name='import_principles_assessment',source={'id':row['id']})
            m['feedback'].append({'source':{'archive':'principles','id':row['id']},
                'targets':['retained_interpretation_history','open_structural_frontier'],
                'zero_nexus':'Z0','status':'reassessment_retained'})
    # Independent of the assessment outcome, revisit the structure/check frontier.
    last=_principles_last(m,'structure_retry');cursor=[0,0] if last is None else last['next_cursor']
    sid,visit=_pf_tuple(cursor,2);available=sid<len(_zstruct_state(m)['records']);result=None
    if available:result=zero_core(m,'0-structures',operation='check',operands=(sid,))
    return _principles_receipt(m,'structure_retry',cursor=cursor,source=sid,visit=visit,
        available=available,result=result,next_cursor=_pf_next(cursor,2))


def _principles_schedule_replay(m,rows):
    cursors={};operators={};ordinal=0
    arities={'pair':3,'pathway_input':3,'answer_pair':3,'zi_frame':4,'zi_retry':2,'structure_retry':2,'interpretation':2}
    for row in rows:
        kind=row['kind']
        if kind=='selection':
            lane=row['lane'];key=(kind,lane);cursor=cursors.get(key,[0,0]);selected=None
            queue=m['queue'] if lane=='core' else _z1_state(m)['queue'] if lane=='z1' else _six_state(m)['queue'] if lane=='six' else None
            if queue is None or not 1<=len(row['steps'])<=32:raise ValueError('Changed selector lane or work allowance')
            for step in row['steps']:
                if step['cursor']!=cursor:raise ValueError('Changed selector cursor')
                index,visit=_pf_tuple(cursor,2);count=step['queue_length']
                if type(count)is not int or not 0<=count<=len(queue) or step['available']!=(index<count):raise ValueError('Changed selector availability')
                if step['available']:
                    source={key:_pr_copy.deepcopy(value) for key,value in queue[index].items() if key in ('operation','kind','parents','source','source_slot','cursor','permutation','key')}
                    eligible=step['status'] in ('pending','size_deferred','depth_deferred','resource_deferred','deferred') or (lane=='z1' and step['status']=='no_applicable_slots')
                    if step['index']!=index or step['visit']!=visit or step['source']!=source or step['eligible']!=eligible:
                        raise ValueError('Changed selector source or retained outcome')
                    if eligible:
                        if step is not row['steps'][-1]:raise ValueError('Selector skipped an eligible retained job')
                        selected=index
                cursor=_pf_next(cursor,2)
            if row['next_cursor']!=cursor or row['selected']!=selected:raise ValueError('Changed selector continuation')
            cursors[key]=cursor;continue
        if kind not in arities:continue
        key=(kind,row.get('lane'));cursor=cursors.get(key,[0,0]);arity=arities[kind]
        if row['cursor']!=cursor:raise ValueError('Changed saved exploration order')
        values=_pf_tuple(cursor,arity);operator=operators.get(key,0)
        if kind in ('pair','answer_pair','zi_frame'):
            if kind=='pair':
                if row['parents']!=values[:2] or row['operation']!=('add','multiply')[operator]:raise ValueError('Changed retained pair proposal')
            elif row['operator']!=operator:raise ValueError('Changed declared operation order')
            if kind=='zi_frame' and row['inputs']!=values[:3]:raise ValueError('Changed Zi input enumeration')
            expected=_pf_next(cursor,arity) if operator==1 else cursor
            operators[key]=(operator+1)%2
            if row['next_operator']!=operators[key]:raise ValueError('Changed operation continuation')
        else:
            expected=_pf_next(cursor,arity)
            if kind=='pathway_input' and row['input']!=values[1]:raise ValueError('Changed pathway input enumeration')
            if kind in ('zi_retry','structure_retry','interpretation') and [row['source'],row['visit']]!=values:raise ValueError('Changed retained revisit')
        if row['next_cursor']!=expected:raise ValueError('Changed saved frontier continuation')
        cursors[key]=expected
        if kind=='interpretation':
            if row['ordinal']!=ordinal or row['lane']!=('symbolic','typed','quantity','physical')[ordinal%4]:raise ValueError('Changed interpretation order')
            ordinal+=1
            if row['available']:
                try:expected=_principles_interpretation_expected(m,row['lane'],row['source'],row['policy'])
                except _ZeroStructureUnsupported as exc:expected={'status':'unresolved','reason':str(exc)}
                if row['assessment']!=expected:raise ValueError('Changed retained reassessment')
            elif row['assessment'] is not None:raise ValueError('Invented reassessment without a retained source')

# Return every reassessment as a distinct open input with an exact source link.
# A typed magnitude keeps its dimensions; no wrapper is stripped to a scalar.
_principles_tree_previous=_open_tree
def _open_tree(m,idx):
    row=_open_state(m)['records'][idx]
    if row['operation']=='import_principles_assessment':
        return {'kind':'principles_assessment_reference','id':row['source']['id']}
    return _principles_tree_previous(m,idx)

def _principles_assessment_source(m,idx):
    rows=_principles_state(m)['records']
    if type(idx)is not int or not 0<=idx<len(rows):raise ValueError('Missing retained reassessment source')
    row=rows[idx]
    if row['kind']!='interpretation' or not row['available']:raise ValueError('Reassessment reference lacks an interpreted source')
    return row

def _principles_typed_reference(m,idx):
    row=_principles_assessment_source(m,idx);lane=row['lane'];assessment=row['assessment']
    if lane=='typed':return _pr_copy.deepcopy(assessment)
    dimensions=None;poly=None
    if lane=='symbolic':
        if assessment.get('outcome')=='interpreted_finite_polynomial':
            dimensions={'numerator':[],'denominator':[]};poly=_pr_copy.deepcopy(assessment['coefficients'])
    elif lane=='quantity':dimensions=assessment.get('dimensions')
    elif lane=='physical':
        if assessment.get('status') in ('declared_magnitude_binding','dimensionally_valid_operation','verified_polynomial_derivative'):
            dimensions=assessment.get('dimensions');source=_physical_state(m)['records'][row['source']]
            try:poly={str(k):v for k,v in _zstruct_poly(m,_sym_ref(source['magnitude'])).items()}
            except _ZeroStructureUnsupported:pass
    if dimensions is None:
        return {'status':'unresolved','dimensions':None,'reason':'retained reassessment remains unresolved','physical_law_verified':False}
    return {'status':'interpreted_magnitude' if poly is not None else 'dimensionally_interpreted',
        'dimensions':_pr_copy.deepcopy(dimensions),'magnitude_coefficients':poly,
        'magnitude_scope':'supplied finite-polynomial interpretation with recorded allowance',
        'origin':'retained_principles_reassessment','physical_law_verified':False}

_principles_poly_previous=_zstruct_poly
def _zstruct_poly(m,node):
    if node.get('kind')=='principles_assessment_reference':
        row=_principles_assessment_source(m,node['id'])
        if row['lane']!='symbolic':raise _ZeroStructureUnsupported('typed reassessment keeps quantity dimensions')
        return _zstruct_poly(m,_slot_rows(m,'symbolic')[row['source']]['expression'])
    return _principles_poly_previous(m,node)

# Role availability follows retained executable bodies, never an input-sample
# count or a preferred result. Integrity checking still checks those bodies.
def _zstruct_available_roles(m):
    return [row['id'] for row in _slot_rows(m,'roles') if row.get('rule')==PATH_ROLE]

_principles_dispatch_previous=_slot_dispatch
def _slot_dispatch(m,domain,operation,operands,kwargs):
    if domain=='principles':
        if operation=='begin':
            last=_principles_last(m,'epoch');scale=1 if last is None else last['policy']['scale']+1
            row=_principles_receipt(m,'epoch',policy=_principles_limits(scale))
            for rid in list(_z1_state(m)['nodes']):
                for kind in Z1I_ACTIONS:_z1_enqueue(m,rid,kind)
            return row
        if operation=='zi_service':return _principles_zi_service(m,kwargs.get('budget',ZI_FRAME_BUDGET))
        if operation=='interpretation_service':return _principles_interpretation_service(m,kwargs.get('budget',4))
        if operation=='select':return _principles_select(m,*operands)
        if operation=='core_attempt':return _principles_core_attempt(m,*operands)
        if operation=='pair_service':return _principles_pairs(m,kwargs.get('budget',4))
        if operation=='pathway_service':
            _principles_answer_pairs(m,kwargs.get('budget',4));return _principles_pathways(m,kwargs.get('budget',4))
        if operation=='retain_request':return _principles_receipt(m,'unresolved_request',request={'operands':list(operands),**kwargs},
            status='retained_unresolved',reason='supplied scalar algorithms are historical replay tools; open syntax continues')
        raise ValueError('Unknown open scheduling operation')
    if domain=='math' and operation in ('request','attempt','service') and not _PRINCIPLES_VALIDATING:
        zero_core(m,'principles',operation='retain_request',request_domain=domain,requested_operation=operation,
            operands=list(operands),options=kwargs)
        raise ValueError('Request retained unresolved; use open/open-run for continuing structural exploration')
    return _principles_dispatch_previous(m,domain,operation,operands,kwargs)

_principles_core_previous=zero_core
def zero_core(memory,domain,*,operation=None,operands=(),**kwargs):
    global _PRINCIPLES_VALIDATING
    if not isinstance(memory,dict) or memory.get('experiment')!=SLOT_RULE:
        return _principles_core_previous(memory,domain,operation=operation,operands=operands,**kwargs)
    validating=domain=='validation' and operation=='archive'
    previous=_PRINCIPLES_VALIDATING
    if validating:_PRINCIPLES_VALIDATING=True
    policy=None if _PRINCIPLES_VALIDATING else (_principles_current() or _principles_epoch(memory))
    if operation=='record' and domain in SLOT_DOMAINS and policy is not None:
        kwargs=dict(kwargs);kwargs['record']=dict(kwargs['record'],execution_policy=_pr_copy.deepcopy(policy))
    try:
        with _principles_scope(policy):
            return _principles_core_previous(memory,domain,operation=operation,operands=operands,**kwargs)
    finally:_PRINCIPLES_VALIDATING=previous

_principles_recover_previous=_zstruct_recover_extensions
def _zstruct_recover_extensions(m):
    changed=False;state=m.get('principles')
    if state is not None:
        actual={row['id']:row for row in state['records']}
        if len(actual)!=len(state['records']):raise ValueError('Duplicate open scheduling receipt')
        restored=[]
        for recipe in state['recipes']:
            row=actual.pop(recipe['id'],None)
            if row is None:row=_pr_copy.deepcopy(recipe);changed=True
            elif row!=recipe:raise ValueError('Changed open scheduling receipt; source preserved')
            restored.append(row)
        if actual:raise ValueError('Untracked open scheduling receipt')
        state['records']=restored
    return _principles_recover_previous(m) or changed

_principles_replay_previous=_slot_replay
def _slot_replay(m):
    state=m.get('principles');scale=0
    if state is not None:
        if state['rule']!=PRINCIPLES_RULE or state['records']!=state['recipes']:raise ValueError('Open scheduling recipe conflict')
        active=set();current=m.get('_active_event')
        while current is not None:
            if current in active:raise ValueError('Cyclic Z0 event ancestry')
            active.add(current);current=m['events'][current].get('parent')
        for idx,row in enumerate(state['records']):
            event=m['events'][row['event']]
            passage_complete=event['status']=='complete' or (event['status']=='running' and row['event'] in active)
            if row['id']!=idx or row['zero_nexus']!='Z0' or event['domain']!='principles' or not passage_complete:
                raise ValueError('Open scheduling receipt lost its Z0 passage')
            if row['kind']=='epoch':
                scale+=1
                if row['policy']!=_principles_limits(scale):raise ValueError('Changed work epoch')
            if row.get('policy') is not None and row['policy']!=_principles_limits(row['policy'].get('scale')):raise ValueError('Changed task allowance')
        _principles_schedule_replay(m,state['records'])
        for node in _open_state(m)['records']:
            if node['operation']=='import_principles_assessment':
                source=_principles_assessment_source(m,node['source']['id'])
                if source['event']>=node['event']:raise ValueError('Reassessment return provenance changed')
    arrays=[_slot_rows(m,domain) for domain in SLOT_DOMAINS]
    arrays += [m.get('Zi',{}).get('attempts',[]),m.get('zero_structures',{}).get('checks',[]),
        _qty_state(m)['records'],_physical_state(m)['records'],_typed_state(m)['records']]
    for rows in arrays:
        for row in rows:
            policy=row.get('execution_policy')
            if policy is not None and policy!=_principles_limits(policy.get('scale')):raise ValueError('Changed record allowance')
    with _principles_scope(None):return _principles_replay_previous(m)

# Source-preserving recovery remains an explicit candidate handoff. A load
# failure never silently starts a fresh lineage or overwrites the source.
def _principles_load_for_run():
    path=memory_path();return path,_slot_load(path)

_principles_query_previous=_slot_query
def _slot_query(m,text):
    parts=text.strip().split();head=parts[0].lower() if parts else ''
    if head.startswith('math-'):
        row=zero_core(m,'principles',operation='retain_request',command=text.strip())
        _slot_save(m,memory_path());print('Retained unresolved request:',row['id'],'| open/open-run continues untargeted syntax exploration.');return
    if head=='principles' and len(parts)==1:print(json.dumps(_principles_report(m),indent=2));return
    if head=='principles-index':
        for row in _principles_state(m)['records']:print(row['id'],row['kind'],'|',row.get('lane',''),'|',row.get('status','retained'))
        return
    if head=='principles':
        try:
            idx=int(parts[1]);rows=_principles_state(m)['records']
            if not 0<=idx<len(rows):raise ValueError('No retained receipt with that ID')
            print(json.dumps(rows[idx],indent=2))
        except (ValueError,IndexError):print('Use principles, principles-index, or principles RECORD_NUMBER')
        return
    return _principles_query_previous(m,text)

def _principles_report(m):
    epoch=_principles_epoch(m)
    return {'rule':PRINCIPLES_RULE,'current_work_allowance':epoch,
        'desired_answer':None,'success_stop_condition':None,
        'scheduling':'saved enumeration of retained inputs and repeated deferred-work opportunities',
        'terminal_generation_depth':None,'historical_records':'original policy preserved; no retagging',
        'supplied_scalar_workers':'historical replay only; new requests retained unresolved',
        'declared_semantics':['complex i action','finite polynomial verifier','quantity dimensions'],
        'verification':'static source review only for V4.11.2; user behavioral testing pending'}

_principles_report_previous=_slot_report
def _slot_report(m):
    report=_principles_report_previous(m);report['principles']=_principles_report(m)
    report['exact_math'].update(execution_mode='historical replay only; new requests retained unresolved',automatic_in_default_run=False)
    report['scope']='Open retained exploration through Z0 with recorded increasing work allowances; declared i, polynomial and dimensional semantics remain supplied.'
    report['deferred']+=['general division, roots and calculus interpretation from retained constructions']
    return report


if __name__ == '__main__':
    try:_strict_main()
    except (ValueError,KeyError,IndexError,OSError) as exc:print('Strict slot exploration paused; saved source preserved:',str(exc))
