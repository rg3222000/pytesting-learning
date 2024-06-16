# Press the green button in the gutter to run the script.
from logger import Logger


if __name__ == '__main__':
    logger = Logger("pytest_service").get_logger("pytest_service")
    logger.error("hello")
    logger.debug("test debug")
    logger.info("info")
