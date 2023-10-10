import re

from src.operators.math_basic import add, subtract, multiply, divide
from src.operators.comp_basic import equals, over, under, over_equals, under_equals, not_equals

OPERATIONS = {
    "+": add,
    "-": subtract,
    "×": multiply,
    "÷": divide,
    "=": equals,
    ">": over,
    "<": under,
    "≥": over_equals,
    "≤": under_equals,
    "≠": not_equals
}


class Runner:
    def __init__(self, logger, params):
        self.params = params
        self.logger = logger
        self.data = {}


    def __is_function(self, value: str) -> (bool, str):
        function_name = re.search(r"([a-zA-Z_][a-zA-Z0-9_]*)\(", value)
        if function_name is None:
            return False, ""
        function_name = function_name.group(1)
        if not function_name in self.data["functions"].keys():
            return False, ""
        return True, function_name


    def __substitute_arguments(self, body, args, arg_values) -> list[str]:
        restart: bool = True
        while restart:
            restart = False
            for step in range(len(body)):
                for arg in args:
                    if body[step].endswith(arg):
                        body[step] = [body[step][:-len(arg)], "×", arg_values[args.index(arg)]]
                        body[step] = self.__sub_run_step(body[step])
                        restart = True
                        break
                if restart:
                    break
        return body


    def __resolve_function(self, call: str, function_name: str) -> str:
        function = self.data["functions"][function_name]
        body = function["body"]
        args = function["args"]
        arg_values = []
        call = call[len(function_name) + 1:-1]
        call = call.split(",")
        call = [arg.strip() for arg in call]
        for arg in call:
            arg_values.append(self.__resolve(arg))
        body = self.__substitute_arguments(body, args, arg_values)
        return self.__sub_run_step(body)


    def __resolve(self, value: str) -> str:
        is_function, function_name = self.__is_function(value)
        if is_function:
            return self.__resolve_function(value, function_name)
        if value.isnumeric():
            return value
        return "0"


    def __sub_run_step(self, step: list[str]) -> str:
        restart = True
        while restart:
            restart = False
            for item in range(len(step)):
                if step[item] in OPERATIONS:
                    try:
                        calculation = OPERATIONS[step[item]](self.__resolve(step[item - 1]), self.__resolve(step[item + 1]))
                        step[item] = calculation
                        del step[item + 1]
                        del step[item - 1]
                        restart = True
                        break
                    except:
                        return "0"
        return step[0] if len(step) == 1 else step


    def __run_step(self, step: list[str]) -> bool:
        restart = True
        while restart:
            restart = False
            for item in range(len(step)):
                if step[item] in OPERATIONS:
                    try:
                        calculation = OPERATIONS[step[item]](self.__resolve(step[item - 1]), self.__resolve(step[item + 1]))
                        step[item] = calculation
                        del step[item + 1]
                        del step[item - 1]
                        restart = True
                        break
                    except Exception as e:
                        print(e)
                        return False
        return True


    def run(self, data: dict) -> bool:
        try:
            self.data = data
            program = data["program"]

            for step in program:
                initial_step = step.copy()
                if not self.__run_step(step):
                    return False
                else:
                    print(f"{''.join(initial_step)} → {step[0] if len(step) == 1 else step}")
        except:
            return False
        return True
