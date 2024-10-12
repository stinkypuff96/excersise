def max_element(numbers: list[int]) -> int:
    min_num = min(numbers)
    for n in numbers:
        if n > min_num:
            min_num = n
    return min_num