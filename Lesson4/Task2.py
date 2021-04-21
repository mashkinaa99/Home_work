name = input('Name: ')
old = int(input('Old: '))

while old == int(old):
    old += 1
    print(f'Hello {name}, on your next birthday you’ll be {old} years')
    break
