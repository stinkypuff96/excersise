# Password generator

from random import randrange

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "+-_()*^$%#!@"
alphabet = lower_case + upper_case + digits + symbols
password_length = 24


def has_any(value: str | list[str], sigmabet: str) -> bool:
    for current in value:
        if current in sigmabet:
            return True

    return False


def pick_random(value: str) -> str:
    index = randrange(0, len(value))
    return value[index]


password = [pick_random(alphabet) for _ in range(0, password_length)]

while True:
    meets_requirements = True

    if not has_any(password, lower_case):
        password[randrange(0, password_length)] = pick_random(lower_case)
        meets_requirements = False

    if not has_any(password, upper_case):
        password[randrange(0, password_length)] = pick_random(upper_case)
        meets_requirements = False

    if not has_any(password, digits):
        password[randrange(0, password_length)] = pick_random(digits)
        meets_requirements = False

    if not has_any(password, symbols):
        password[randrange(0, password_length)] = pick_random(symbols)
        meets_requirements = False

    if meets_requirements:
        break

print("".join(password))