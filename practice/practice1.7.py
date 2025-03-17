# Cows and Bulls
from random import randint

solution = [randint(0, 9) for _ in range(0, 4)]
guess_count = 0
while True:
    user_input = input("Make your guess: ")
    guess = [int(c) for c in user_input]
    guess_count += 1

    if solution == guess:
        print(f"You got it in {guess_count} attempts!")
        break

    if guess_count == 15:
        print('You fucking suck! :P')
        print(f'The correct answer was {"".join([str(x) for x in solution])}')
        break

    cows = 0
    bulls = 0

    for i in range(0, 4):
        if solution[i] == guess[i]:
            cows += 1
        elif guess[i] in solution:
            bulls += 1

    print(f'Cows: {cows}, Bulls: {bulls}')
