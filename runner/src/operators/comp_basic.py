def equals(value1: str, value2: str) -> str:
    return str(int(value1 == value2))

def over(value1: str, value2: str) -> str:
    return str(int(value1 > value2))

def under(value1: str, value2: str) -> str:
    return str(int(value1 < value2))

def over_equals(value1: str, value2: str) -> str:
    return str(int(value1 >= value2))

def under_equals(value1: str, value2: str) -> str:
    return str(int(value1 <= value2))

def not_equals(value1: str, value2: str) -> str:
    return str(int(value1 != value2))
