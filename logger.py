import logging
import logging.config
from config import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)


class Logger:
    def __init__(self, logger_name: object) -> object:
        self.logger = logging.getLogger(logger_name)

    @staticmethod
    def get_logger(logger_name):
        logger = Logger(logger_name)
        return logger.logger
    