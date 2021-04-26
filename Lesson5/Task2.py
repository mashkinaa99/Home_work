import random


x = []
y = []
i = 0

while i < 10:
    x.append(random.randint(0, 10))
    y.append(random.randint(0, 10))
    i += 1

x_set = set(x)
y_set = set(y)

print(x, y, list(x_set & y_set), sep='\n')