import logging


LOG_RECORD_BUILTIN_ATTRS = {
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
    "taskName",
}


class FilterContent(logging.Filter):
    """

    """
    def filter(self, record: logging.LogRecord) -> bool | logging.LogRecord:
        """

        :param record:
        :return:
        """
        return record.levelno > logging.INFO


class FilterContents(logging.Filter):
    """

    """
    def filter(self, record: logging.LogRecord) -> bool | logging.LogRecord:
        """

        :param record:
        :return:
        """
        return record.levelno <= logging.INFO
