def reverse_string(s: str) -> str:
    for i in s:
        return s[::-1]
    if s[::-1] == '':
        return s
