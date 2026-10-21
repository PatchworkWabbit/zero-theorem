# ============================================================
# ZERO THEOREM V4.7.17 - EXACT TEMPORAL RECOVERY
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

VERSION = '4.1'  # Memory-format compatibility; runtime version is V4.7.17.
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


# Two arithmetic movement cores: successor and predecessor.
# All finite rational operations below construct exact integer numerators and
# denominators using these two moves. Fraction normalizes representation only.
# The trace is a bounded observational journal, not a claim of shortcut discovery.
_TWO_CORE_RULE = 'successor_predecessor_arithmetic_v1'
_TWO_CORE_STEP_BUDGET = 200000
_TWO_CORE_LAST_PATH = None

def _two_core_integer(a, b, op, budget):
    if type(a) is not int or type(b) is not int:
        raise TypeError('Two-core arithmetic requires exact integers')
    steps = [0]
    def move(n, direction):
        steps[0] += 1
        if steps[0] > budget:
            raise ArithmeticError('Two-core construction budget exceeded; no direct-operation fallback')
        return n + 1 if direction > 0 else n - 1
    def add(x, y):
        value = x
        direction = 1 if y >= 0 else -1
        for _ in range(abs(y)):
            value = move(value, direction)
        return value
    def negate(x):
        return add(0, -x) if False else _negate(x)
    def _negate(x):
        value = 0
        for _ in range(abs(x)):
            value = move(value, -1 if x > 0 else 1)
        return value
    def multiply(x, y):
        value = 0
        term = x if y >= 0 else _negate(x)
        for _ in range(abs(y)):
            value = add(value, term)
        return value
    if op == '+': result = add(a,b)
    elif op == '-': result = add(a,_negate(b))
    elif op == '*': result = multiply(a,b)
    else: raise ValueError(op)
    return result, steps[0]

def _operate_rational_exact(a, op, b):
    global _TWO_CORE_LAST_PATH
    from fractions import Fraction as _TwoCoreFraction
    a, b = _TwoCoreFraction(a), _TwoCoreFraction(b)
    if op == '/' and b == 0:
        _TWO_CORE_LAST_PATH = {'rule': _TWO_CORE_RULE, 'zero_nexus':'Z0',
                               'operation':op, 'blocked':'division_by_zero'}
        return None
    if op not in ('+', '-', '*', '/'):
        raise ValueError('Unsupported operation')
    # Build a rational as numerator/denominator. Each component is a path
    # of successor/predecessor moves; Fraction is used only to canonicalize.
    components = []
    def construct(x,y,operation):
        value, steps = _two_core_integer(x,y,operation,_TWO_CORE_STEP_BUDGET)
        components.append({'op':operation,'left':x,'right':y,'result':value,
                           'movement_steps':steps,'zero_nexus':'Z0'})
        return value
    an,ad,bn,bd = a.numerator,a.denominator,b.numerator,b.denominator
    if op in ('+','-'):
        left=construct(an,bd,'*')
        right=construct(bn,ad,'*')
        numerator=construct(left,right,op)
        denominator=construct(ad,bd,'*')
    elif op == '*':
        numerator=construct(an,bn,'*')
        denominator=construct(ad,bd,'*')
    else:
        numerator=construct(an,bd,'*')
        denominator=construct(ad,bn,'*')
    _TWO_CORE_LAST_PATH = {'rule':_TWO_CORE_RULE,'zero_nexus':'Z0',
                           'operation':op,'inputs':(str(a),str(b)),
                           'components':components,
                           'shortcut_discovered':False}
    return _TwoCoreFraction(numerator,denominator)


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


def memory_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), MEMORY_FILENAME)


def load_memory():
    path = memory_path()
    if not os.path.exists(path): return empty_memory()
    m = _zt_load_file(path)
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
    zero_core(m, 'symbolic', record=rec)
    sa['expressions'].append(rec)
    ensure_symbolic_construction(m, rec)
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
        'symbolic_nexus': ('symbolic', ('source',))}
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
        if rec.get('rule') == 'assign_name_preserve_payload':
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
    if target in ('A', 'a'):
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
             'processed': {'consume': 0, 'consume_op': 0, 'pair': 0, 'revisit': 0, 'nexus': 0, 'zero_scan': 0, 'zero_source': 0, 'emerge': 0, 'frontier': 0, 'position': 0, 'complex': 0, 'complex_feedback': 0, 'symbolic_root': 0, 'symbolic_pair': 0, 'symbolic_nexus': 0, 'symbolic_position': 0}}
    print('ZERO THEOREM V4.7.17 - EXACT TEMPORAL RECOVERY')
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
    upgrade_v44(m)
    import_symbolic_sources(m)
    schedule_symbolic_zero_positions(m)
    removed = rebalance_queue(m)
    journal(m, 'queue_rebalance', removed_duplicates=removed, pending=len(m['queue']))
    print('Duplicate pending tasks removed:', removed)
    # Work queue is persistent. Each task is removed only after completion.
    # Rotate through tasks to prevent any one pathway monopolising the run.
    # Count a bounded number of states first, so new values enter this run.
    with _zt16_span(memory_path(), 'queue_exploration'):
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
    save_memory(m)
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
            if rule == 'assign_name_preserve_payload':
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
        body_text = body['value'] if body['kind'] == 'numeric' else body['symbol']
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
MEMORY_FILENAME = 'zero_theorem_v48_experimental_memory.json'

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

if __name__ == '__main__':
    import sys
    if '--seconds' in sys.argv:
        index=sys.argv.index('--seconds')
        _ZW_SECONDS=float(sys.argv[index+1])
        if _ZW_SECONDS<=0:raise ValueError('--seconds must be positive')
        del sys.argv[index:index+2]
    if sys.argv[1:2] == ['--time-recover'] and len(sys.argv) == 5:
        zero_core(None, 'temporal', operation='recover', operands=(sys.argv[2], int(sys.argv[3]), sys.argv[4]))
    elif sys.argv[1:2] == ['--zero-clock'] and len(sys.argv) in (2, 3):
        print_zero_clock_report(sys.argv[2] if len(sys.argv) == 3 else memory_path())
    elif sys.argv[1:2] == ['--time-report'] and len(sys.argv) in (2, 3):
        print_time_report(sys.argv[2] if len(sys.argv) == 3 else memory_path())
    elif sys.argv[1:2] == ['--adaptive-recovery'] and len(sys.argv) in (3, 4):
        zero_adaptive_recovery(sys.argv[2], sys.argv[3] if len(sys.argv) == 4 else None)
    elif sys.argv[1:2] == ['--resume-candidate'] and len(sys.argv) in (3, 4):
        target = sys.argv[3] if len(sys.argv) == 4 else memory_path()
        target = os.path.abspath(target)
        try:
            _za_promote(sys.argv[2], target)
            # Point the existing load/save workers at the approved memory.
            globals()['memory_path'] = lambda: target
            run()
        except (ZeroRecoveryPending, OSError, ValueError, RuntimeError) as exc:
            print('Recovery not resumed:', str(exc))
    elif sys.argv[1:2] == ['--verify-candidate'] and len(sys.argv) == 3:
        zero_verify_candidate(sys.argv[2])
    elif sys.argv[1:2] == ['--repair-json'] and len(sys.argv) in (2, 3):
        path = sys.argv[2] if len(sys.argv) == 3 else memory_path()
        try:
            _zt_load_file(path, inspect_only=True)
        except (ZeroRecoveryPending, OSError, UnicodeError) as exc:
            print(str(exc))
    elif sys.argv[1:] == ['--integrity']:
        if os.path.exists(memory_path()):
            print_archive_link_audit(load_memory())
        else:
            print('No saved memory found to inspect.')
    elif sys.argv[1:]:
        print('Usage: python zero_theoremV4.7.17.py [--time-recover LEDGER SEQ FIELD | --zero-clock [PATH] | --time-report [PATH] | --integrity | --repair-json [PATH] | --verify-candidate PATH | --adaptive-recovery CANDIDATE [BASELINE] | --resume-candidate CANDIDATE [MEMORY]] [--seconds N]')
    else:
        run()

