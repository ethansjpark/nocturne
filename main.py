import argparse
from cli.commands import run_bot, train_model, evaluate_results
from utils.logger import get_logger

logger = get_logger()


def main():
    parser = argparse.ArgumentParser(description = "Crypto AI HFT Bot")
    parser.add_argument("command", choices = ["run", "train", "evaluate"], help = "Command to execute")
    args = parser.parse_args()

    if args.command == "run":
        run_bot()
    elif args.command == "train":
        train_model()
    elif args.command == "evaluate":
        evaluate_results()

if __name__ == "__main__":
    main()
    
