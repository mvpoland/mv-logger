import json
import logging
import unittest

from mv_logger.logstash import Formatter


class FormatterTestCase(unittest.TestCase):
    def test_format(self):
        record = logging.LogRecord("test", "INFO", "/tmp", 1, "I'm, dummy", [], None)
        formatter = Formatter()

        formatted = formatter.format(record)
        formatted_json = json.loads(formatted)

        self.assertEqual(formatted_json["message"], "I'm, dummy")
