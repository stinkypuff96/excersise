import random
from random import randint


def dice_roll() -> int:
    roll = randint(1, 6)
    roll2 = randint(1, 6)
    roll3 = randint(1, 6)
    all_dice = roll + roll2 + roll3
    print(f'You rolled {roll}, {roll2}, {roll3} which equals {all_dice}')


dice_roll()
