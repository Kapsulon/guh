import argparse
import sys
from os import path
import json
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from src.compiler import Compiler
from utils.logger import Logger, LOG_LEVELS

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", help="files to be compiled", nargs="+")
    parser.add_argument("-L", "--log-level", help="select logging level", choices=LOG_LEVELS.keys(), default="info")
    parser.add_argument("-o", "--output", help="output file", default="out.json")
    args = parser.parse_args()
    logger = Logger("guh", level=LOG_LEVELS[args.log_level])
    logger.log(f"Compiling {len(args.files)} file{'s' if len(args.files) > 1 else ''}")
    compiler = Compiler(logger, {})
    final_count: int = 0
    for file in args.files:
        err = compiler.compile(file)
        if err:
            logger.log(f"Failed to compile {file}", Logger.LogLevel.ERROR)
        else:
            final_count += 1
    logger.log(f"Compiled {final_count}/{len(args.files)} file{'s' if len(args.files) > 1 else ''}", Logger.LogLevel.INFO)
    if final_count == len(args.files):
        logger.log("Compilation successful", Logger.LogLevel.INFO)
        with open(args.output, "w") as f:
            json.dump(compiler.compiled, f, indent=4)
        quit(0)
    else:
        logger.log("Compilation failed somewhere", Logger.LogLevel.ERROR)
        quit(1)
