import logging

def get_logger(name: str = "nocturne"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        logger.addHandler(ch)

    return logger