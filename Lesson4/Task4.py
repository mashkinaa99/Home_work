b = 4
v = 5
c = b + v
a = int(input(f'{b} + {v} = '))
while a == c:
    print(f'Yes you are right! It\'s really {c}')
    break
else:
    print(f'No, the correct answer is {c}')