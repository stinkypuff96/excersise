import random

while True:
    choice = input('Do you roll? Y/N: ')
    if choice.lower() == 'y':
        user = random.randint(1, 6)
        print(f'You rolled a {user}')
        cpu = random.randint(1, 6)
        print(f'Your opponent rolled a {cpu}')
        if user > cpu:
            print('You win!')
        elif user < cpu:
            print('You lose.')
        else:
            print("It's a draw!")
    elif choice.lower() == 'n':
        print('Bye')
        break
    else:
        print('Error! Please press Y/N!')