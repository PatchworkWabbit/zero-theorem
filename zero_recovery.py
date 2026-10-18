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
