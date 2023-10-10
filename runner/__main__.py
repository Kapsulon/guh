import argparse
import json
import sys
from os import path
from src.runner import Runner

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from utils.logger import Logger, LOG_LEVELS

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", help="files to be compiled", nargs="+", default=["out.json"])
    parser.add_argument("-L", "--log-level", help="select logging level", choices=LOG_LEVELS.keys(), default="info")

    args = parser.parse_args()
    logger = Logger("guh", level=LOG_LEVELS[args.log_level])
    runner = Runner(logger, {})
    for file in args.files:
        try:
            with open(file, "r") as f:
                data = json.load(f)
            if not runner.run(data):
                logger.log(f"Failed to run {file}", Logger.LogLevel.ERROR)
                quit(1)
        except FileNotFoundError:
            logger.log(f"File {file} not found", Logger.LogLevel.ERROR)
            continue
        except json.JSONDecodeError:
            logger.log(f"File {file} is not a valid json file", Logger.LogLevel.ERROR)
            continue
    quit(0)
