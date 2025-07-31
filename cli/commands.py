from bot.strategy import generate_signal
from bot.executor import execute_trade
from utils.logger import get_logger


logger = get_logger()

def run_bot():
    logger.info("Running the trading bot...")
    
    dummy_data = {
        "price": 20000,
        "sma_short": 19800,
        "sma_long": 20500
    }

    signal = generate_signal(dummy_data)
    logger.info(f"Generated signal: {signal}")

    execute_trade(signal)


def train_model():
    logger.info("Training model... (placeholder)")
    # TODO: load data, train model, save weights

def evaluate_results():
    logger.info("Evaluating results with LLM... (placeholder)")
    # TODO: load logs, summarize results using LLM
