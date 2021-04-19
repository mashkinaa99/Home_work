txt = input('Enter the string: ')
if len(txt) < 2:
    print()
else:
    result = txt[:2] + txt[-2:]
    print(f'Result: {result}')
