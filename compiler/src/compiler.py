import sys
import re
from utils.logger import Logger

class Compiler:
    def __init__(self, logger: Logger, params: dict):
        self.params = params
        self.logger = logger
        self.compiled = {
            "functions": {},
            "program": []
        }


    def __lex(self, lines: list[str]) -> bool:
        for line in lines:
            if line.startswith("func"):
                if not self.__lex_function(line):
                    return False
            else:
                if not self.__lex_statement(line):
                    return False
        return True


    def __lex_function(self, line: str) -> bool:
        try:
            line = line[4:].strip()

            name = line[:line.find("(")]
            args = line[line.find("(")+1:line.find(")")].split(",")
            for i in range(len(args)):
                args[i] = args[i].strip()
            body = line.split("=")[1].strip().split(" ")

            self.compiled["functions"][name] = {
                "args": args,
                "body": body
            }
        except:
            self.logger.log(f"Invalid function declaration: {line}", Logger.LogLevel.ERROR)
            return False
        return True


    def __lex_statement(self, line: str) -> bool:
        try:
            tokens = []
            current_token = ""
            for char in line:
                if char.isalnum() or char in ('(', ')'):
                    current_token += char
                else:
                    if current_token:
                        tokens.append(current_token)
                    current_token = ""
                    if char != " ":
                        tokens.append(char)
            if current_token:
                tokens.append(current_token)
            self.compiled["program"].append(tokens)
        except:
            self.logger.log(f"Invalid statement: {line}", Logger.LogLevel.ERROR)
            return False
        return True


    def compile(self, file: str) -> bool:
        if not (file.endswith(".guh") or file.endswith(".g")):
            self.logger.log(f"file {file} should end with .guh or .g file extension", Logger.LogLevel.WARNING)
        self.logger.log(f"Compiling {file}", Logger.LogLevel.VERBOSE)

        # Read file contents
        with open(file, "r") as f:
            contents = f.read()

        # Remove comments ('//' until end of line including newline and '/* */')
        contents = re.sub(r"//.*\n", "", contents)
        contents = re.sub(r"/\*.*\*/", "", contents)

        tmp = contents.split("\n")
        tmp = list(filter(lambda x: x != "", tmp))

        # Lex
        err = not self.__lex(tmp)

        return err

