import logging.config
import json

with open('logger_config.json') as f:
    logger_config = json.load(f)

logging.config.dictConfig(config=logger_config)


class Logger:
    def __init__(self, logger_name) -> None:
        self.logger = logging.getLogger(logger_name)

    @staticmethod
    def get_logger(logger_name):
        logger = Logger(logger_name)
        return logger.logger
    

logger = Logger("pytesting").get_logger("pytesting")