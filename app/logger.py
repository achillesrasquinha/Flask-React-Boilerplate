# imports - standard imports
import logging

def get_logger():
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s | %(message)s", "%H:%M:%S")

        handler   = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger