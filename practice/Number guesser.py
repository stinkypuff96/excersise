from random import randrange

# generating a random number and setting a count
gen_num = randrange(0, 100)
count = 0

print(
    'Welcome to my Number Guessing Game!\nTry guessing the number between 0 and 99. You have 15 attempts.\nGood luck!')
while True:
    # validate user input
    try:
        user_choice = int(input('Enter a number between 0 and 99: '))
    except ValueError:
        print('You need to enter a number!')
        continue

    count += 1  # increasing attempt count
    print(f'Attempt number {count}')
    if count == 15:  # implement a lose state
        print(f'You lose! The correct number was {gen_num} ')
        break
    # check user guess
    if user_choice < 0 or user_choice > 99:
        print('You have to pick between 0 and 99')
        continue

    if user_choice > gen_num:
        print('Too high. Try again!')

    elif user_choice < gen_num:
        print('Too low. Try again.')

    else:
        print(f'Congratulations! You guessed the number {gen_num} in {count} attempts!')
        break
