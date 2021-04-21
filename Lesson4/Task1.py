import random

user_nmb = input('Guess the number from 1 to 10: ')
numbers = random.randint(1, 10)
if int(user_nmb) != numbers:
    print(f'You were close, but the correct answer {numbers}')
else:
    print('Wow, you guessed it!')

