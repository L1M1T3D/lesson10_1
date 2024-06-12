import logging


def setup_logging(name: str, log_file: str) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging_formatter = logging.Formatter(f"%(asctime)s - ({name}) %(levelname)s: %(message)s")
    logging_handler = logging.FileHandler(log_file, mode="w")
    logging_handler.setFormatter(logging_formatter)
    logger.addHandler(logging_handler)
    return logger
