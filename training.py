import random

a = int(random.randint(1, 9))
u_input = int(input('Enter a number between 1 and 9: '))
attempts = 0

while u_input < a:
    print('You are too low')
    print('Try again')
    u_input = int(input('Enter a number between 1 and 9: '))

while u_input > a:
    print('You are too high')
    print('Try again')
    u_input = int(input('Enter a number between 1 and 9: '))

if u_input == a:
    print('You win!')

for
    attempts += 1
    if attempts == 4:
        print('You lose!')
