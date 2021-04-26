import random


x = []
i = 0

while i < 10:
    x.append(random.randint(0, 100))
    i += 1

print(x, max(x), sep='\n')
