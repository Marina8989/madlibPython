import random

num = int(input('enter a number: '))
def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x} "))

        if guess < random_number:
            print('Sorry, try again. Too low.')
        elif guess > random_number:
            print('Sorry, try again. Too high.')

    print(f"Yay you guessed the correct number.")            

guess(num)
