def reverse_string_algorithm1(s: str) -> str:
    chars: list[str] = []
    for char in s:
        chars.insert(0, char)
    return ''.join(chars)


def reverse_string(s: str) -> str:
    chars: list[str] = []
    index = len(s) - 1
    while index >= 0:
        current_char = s[index]
        chars.append(current_char)
        index -= 1
    return ''.join(chars)
