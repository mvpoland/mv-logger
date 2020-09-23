from logstash_async.formatter import DjangoLogstashFormatter


class Formatter(DjangoLogstashFormatter):
    def _stringify(self, s):
        if isinstance(s, str):
            try:
                s = s.decode("utf-8", "ignore")
            except AttributeError:
                pass

        return str(s)

    def _get_extra_fields(self, record):
        fields = super(Formatter, self)._get_extra_fields(record)

        skip_list = (
            "args",
            "asctime",
            "created",
            "exc_info",
            "exc_text",
            "filename",
            "funcName",
            "id",
            "levelname",
            "levelno",
            "lineno",
            "module",
            "msecs",
            "msecs",
            "message",
            "msg",
            "name",
            "pathname",
            "process",
            "processName",
            "relativeCreated",
            "thread",
            "threadName",
            "extra",
            "auth_token",
            "password",
        )

        easy_types = (str, bool, dict, float, int, list, type(None))

        for key, value in list(record.__dict__.items()):
            if key not in skip_list:
                if isinstance(value, easy_types):
                    fields[key] = value
                else:
                    fields[key] = repr(value)

        return fields

    def format(self, record):
        # Create message dict
        message = {
            "@timestamp": self._format_timestamp(record.created),
            "@version": "1",
            "host": self._host,
            "tags2": self._tags,
            "message": record.getMessage(),
            # Extra Fields
            "level": record.levelname,
            "process": record.process,
            "thread": record.thread,
            "ex": {
                k: self._stringify(v) for k, v in self._get_extra_fields(record).items()
            },
        }
        return self._serialize(message)
