import random


word_list = ["smile", "hike", "motorcycle", "bathtub", "orange", "Uzbekistan", "warehouse", "balcony", "royalty",
             "keyboard"]
guess_count = 0
word = random.choice(word_list)
shuffled = list(word)
random.shuffle(shuffled)
shuffled_word = "".join(shuffled)
print(shuffled_word)
print(guess_count)
while True:
    u_input = input('Guess the word: ')

    if u_input == "quit":
        print(f'The correct word was: {word}')
        break

    guess_count += 1
    if u_input.lower() == word.lower():
        print(f"You guessed the word in {guess_count} guess/es!")

        if guess_count == 1:
            print('Excellent!')
        elif 2 <= guess_count <= 3:
            print('Very Good!')
        elif 4 <= guess_count <= 5:
            print('Good')
        else:
            print('Try Harder.')
        break

    else:
        print("That is wrong!")
        print(f'You have made {guess_count} guesses.')
