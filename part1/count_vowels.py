def count_vowels(value: str) -> int:
    vowels = 'aeiouAEIOU'
    num_of_vow = 0

    for i in value:
        if i in vowels:
            num_of_vow += 1

    return num_of_vow
