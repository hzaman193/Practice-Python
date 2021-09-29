def decimal_to_octal(n):
    tmp = n
    result = 0
    base = 1
    while tmp > 0:
        remainder = tmp % 8
        tmp = int(tmp / 8)
        result = result + (remainder * base)
        base = base * 10
    return result


def decimal_to_binary(n):
    tmp = n
    result = 0
    base = 1
    while tmp > 0:
        remainder = tmp % 2
        tmp = int(tmp / 2)
        result = result + (remainder * base)
        base = base * 10
    return result


def decimal_to_hex(n):
    tmp = n
    result = 0
    base = 1
    while tmp > 0:
        remainder = tmp % 16
        tmp = int(tmp / 16)
        result = result + (remainder * base)
        base = base * 10
    return result


num = int(input())
print(f"Octal Number is {decimal_to_octal(num)}")
print(f"Binary Number is {decimal_to_binary(num)}")
print(f"Hex Number is {decimal_to_hex(num)}")












