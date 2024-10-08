def count_vowels(value: str) -> int:
    vowels = 'aeiouAEIOU'
    text = input('Enter text: ')
    num_of_vow = 0

    for i in text:
        if i in vowels:
            num_of_vow += 1

    print(num_of_vow)
