"""Historical observations are not expression links; actual links stay checked."""
import copy
import unittest

from test_archive_integration import load_engine, memory

engine = load_engine('zero_theoremV4.6.5.py', 'legacy_audit_engine')


def observation():
    return {'result_id': None, 'zero_nexus': 'Z0',
            'slot_kind': 'reference_position_operation', 'source': '00404',
            'source_position': 1, 'selected_value': 1, 'operation': '+',
            'local_result': '1', 'transformed': '10404',
            'status': 'positional_operation_observation',
            'rule': 'zero_nexus_position_operation_v42'}


class LegacyPositionalAuditTests(unittest.TestCase):
    def test_explicit_legacy_observation_is_read_only_and_reported(self):
        m = memory()
        m['nexus_events'].append(observation())
        before = copy.deepcopy(m)
        report = engine.archive_link_audit(m)
        self.assertEqual(report['issues'], 0)
        self.assertEqual(report['legacy_positional_observations'], 1)
        self.assertEqual(m, before)

    def test_null_expression_link_still_fails(self):
        m = memory()
        m['nexus_events'].append({'result_id': None, 'zero_nexus': 'Z0',
                                 'rule': 'zero_nexus_transform_v1'})
        self.assertGreater(engine.archive_link_audit(m)['issues'], 0)

    def test_invalid_nonnull_legacy_result_still_fails(self):
        m = memory()
        event = observation()
        event['result_id'] = 999999
        m['nexus_events'].append(event)
        self.assertGreater(engine.archive_link_audit(m)['issues'], 0)

    def test_malformed_legacy_metadata_still_fails(self):
        for field, value in [('source_position', 3), ('source_position', None),
                             ('selected_value', 12), ('transformed', 'bogus'),
                             ('source', None), ('operation', 'bogus'),
                             ('local_result', None), ('zero_nexus', 'missing')]:
            with self.subTest(field=field):
                m = memory()
                event = observation()
                event[field] = value
                m['nexus_events'].append(event)
                self.assertGreater(engine.archive_link_audit(m)['issues'], 0)

    def test_other_legacy_event_references_still_checked(self):
        m = memory()
        event = observation()
        event['source_id'] = 999999
        m['nexus_events'].append(event)
        self.assertGreater(engine.archive_link_audit(m)['issues'], 0)


if __name__ == '__main__':
    unittest.main()
