import random


def computer_guess(x):
    low: int = 1
    high: int = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), is too low (L), or correct (C)')
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f'Yay! Computer guessed number, {guess}, correctly')

computer_guess(10)