"""Archive growth must not trigger the damaged-text repair size limit."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('large_memory', Path(__file__).with_name('zero_theoremV4.7.14.py'))
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)

class LargeMemoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'memory.json'

    def load_large(self, text):
        self.path.write_text(text, encoding='utf-8')
        before = self.path.read_bytes()
        try:
            with patch.object(e, '_ZT_MAX_BYTES', 64):
                return e._zt_load_file(str(self.path))
        finally:
            self.assertEqual(self.path.read_bytes(), before)

    def test_valid_archive_above_repair_limit(self):
        memory = e.empty_memory()
        result = self.load_large(json.dumps(memory))
        self.assertEqual(result['expressions'], memory['expressions'])
        self.assertEqual(result['queue'], memory['queue'])
        self.assertEqual(result['zero_text_observation']['zero_nexus'], 'Z0')

    def test_duplicate_keys_still_rejected(self):
        with self.assertRaises(e.ZeroRecoveryPending):
            self.load_large('{"schema":1,"schema":1,"padding":"' + 'x'*100 + '"}')

    def test_malformed_text_preserved(self):
        with self.assertRaises(e.ZeroRecoveryPending):
            self.load_large('{"broken":' + ' '*100)

    def test_incorrect_arithmetic_still_rejected(self):
        memory = e.empty_memory()
        memory['expressions'][0]['value'] = '99'
        with self.assertRaises(e.ZeroRecoveryPending):
            self.load_large(json.dumps(memory))

if __name__ == '__main__':
    unittest.main()
