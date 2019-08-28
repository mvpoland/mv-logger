from __future__ import absolute_import

from logstash_async.formatter import DjangoLogstashFormatter


class Formatter(DjangoLogstashFormatter):
    def _stringify(self, s):
        if isinstance(s, unicode):
            s = s.decode('utf-8', 'ignore')

        return str(s)

    def format(self, record):
        # Create message dict
        message = {
            '@timestamp': self._format_timestamp(record.created),
            '@version': '1',
            'host': self._host,
            'tags2': self._tags,
            'message': record.getMessage(),
            # Extra Fields
            'level': record.levelname,
            'process': record.process,
            'thread': record.thread,
            'ex': {k: self._stringify(v) for k, v in self._get_extra_fields(record).iteritems()},
        }

        return self._serialize(message)
