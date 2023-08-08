import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Too Low')
        elif guess > random_number:
            print('Sorry, Too High')
    
    print(f'Congratulations. You Gussed the numbe{random_number} correctly')

















