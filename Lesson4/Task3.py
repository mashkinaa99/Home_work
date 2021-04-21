import random

a = input('hello: ').lower()
b = list(a)
i = 0
if i < 5:
    random.shuffle(b)
    c = ''.join(b)
    print(c.capitalize())
    i += 1