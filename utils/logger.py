import rich


class Logger:
    class Colors:
        HIGHLIGHT = "#dea909"
        VERBOSE = "#a9a9a9"
        INFO = "#6ccbeb"
        WARNING = "#f5d222"
        ERROR = "#e82042"


    class LogLevel:
        VERBOSE = -1
        INFO = 0
        WARNING = 1
        ERROR = 2
        NONE = 3


    def __init__(self, prefix: str, level: LogLevel.INFO, outputFunc: callable = rich.print):
        self.prefix = prefix
        self.outputFunc = outputFunc
        self.level = level


    def __display_level(self, level: LogLevel) -> str:
        match level:
            case self.LogLevel.VERBOSE:
                return f"[bold {self.Colors.VERBOSE}]VERBOSE[/bold {self.Colors.VERBOSE}]"
            case self.LogLevel.INFO:
                return f"[bold {self.Colors.INFO}]INFO[/bold {self.Colors.INFO}]"
            case self.LogLevel.WARNING:
                return f"[bold {self.Colors.WARNING}]WARNING[/bold {self.Colors.WARNING}]"
            case self.LogLevel.ERROR:
                return f"[bold {self.Colors.ERROR}]ERROR[/bold {self.Colors.ERROR}]"
            case _:
                return f"[bold {self.Colors.ERROR}]UNKNOWN[/bold {self.Colors.ERROR}]"


    def log(self, msg: str, level: LogLevel = LogLevel.INFO):
        if self.level > level or self.level == self.LogLevel.NONE:
            return
        if self.outputFunc == rich.print:
            self.outputFunc(f"[bold {self.Colors.HIGHLIGHT}]{self.prefix}[/bold {self.Colors.HIGHLIGHT}]: ", end="")
            self.outputFunc(self.__display_level(level), end=" ")
            print(msg)
            return
        self.outputFunc(f"{self.prefix}: {msg}")

LOG_LEVELS = {
    "verbose": Logger.LogLevel.VERBOSE,
    "info": Logger.LogLevel.INFO,
    "warning": Logger.LogLevel.WARNING,
    "error": Logger.LogLevel.ERROR,
    "none": Logger.LogLevel.NONE
}
