from utils.logger import get_logger


logger = get_logger()

def execute_trade(signal):
    if signal == "buy":
        logger.info("Executing BUY trade")
    elif signal == "sell":
        logger.info("Executing SELL trade")
    else:
        logger.info("Holding position")