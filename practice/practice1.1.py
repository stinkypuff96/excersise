def is_prime():
    return int(input('Give me a number: '))


num = is_prime()
if num % 2 == 0:
    print('The number you chose is a prime number.')
else:
    print('The number you chose is not a prime number.')
