# regex to remove comment lines "( *?)#.*\n"

def add(value1: str, value2: str) -> str:
    result = []
    carry = 0
    i, j = len(value1) - 1, len(value2) - 1
    while i >= 0 or j >= 0:
        digit1 = int(value1[i]) if i >= 0 else 0
        digit2 = int(value2[j]) if j >= 0 else 0
        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(str(total % 10))
        i -= 1
        j -= 1
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])


def subtract(value1: str, value2: str) -> str:
    result = []
    carry = 0
    i, j = len(value1) - 1, len(value2) - 1
    while i >= 0 or j >= 0:
        digit1 = int(value1[i]) if i >= 0 else 0
        digit2 = int(value2[j]) if j >= 0 else 0
        total = digit1 - digit2 + carry
        carry = total // 10
        result.append(str(total % 10))
        i -= 1
        j -= 1
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])


def divide(value1: str, value2: str) -> str:
    result = []
    remainder = ""
    for i in range(len(value1)):
        remainder += value1[i]
        if len(remainder) == 1 and remainder[0] == '0':
            result.append("0")
        elif int(remainder) < int(value2):
            result.append("0")
        else:
            count = 0
            while int(remainder) >= int(value2):
                remainder = str(int(remainder) - int(value2))
                count += 1
            result.append(str(count))
    return ''.join(result).lstrip('0') or '0'


def multiply(value1: str, value2: str) -> str:
    result = []
    value1 = value1[::-1]
    value2 = value2[::-1]
    for i in range(len(value2)):
        digit = int(value2[i])
        carry = 0
        for j in range(len(value1)):
            total = digit * int(value1[j]) + carry
            carry = total // 10
            if i + j < len(result):
                total += int(result[i + j])
                carry += total // 10
                result[i + j] = str(total % 10)
            else:
                result.append(str(total % 10))
        if carry:
            result.append(str(carry))
    return ''.join(result[::-1])
