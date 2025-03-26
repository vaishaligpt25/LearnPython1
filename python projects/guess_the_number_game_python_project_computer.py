# https://www.freecodecamp.org/news/python-projects-for-beginners

import random

def guess(x):
    random_number = random.randint(1, x)
    guess: int = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        if guess < random_number:
            print("Sorry, Guess again, Too Low")
        elif guess > random_number:
            print("Sorry, Guess again, Too high")
    print("Yay, You have guessed a number.")

if __name__ == '__main__':
    guess(10)





