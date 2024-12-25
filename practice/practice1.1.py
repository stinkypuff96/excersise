# is the number prime

def is_prime(num):
    if num % 2 == 0:
        print('The number you chose is a prime number')
    else:
        print('The number you chose is not a prime number')


player_num = int(input('Choose a number: '))
is_prime(player_num)
