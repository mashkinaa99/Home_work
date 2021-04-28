def make_operation(sign, *args):
    plus = 0
    multiplication = 1
    minus = args[0]

    if sign == '+':
        for n in args:
            plus += n
        print(f'Sum of all entered numbers = {plus}')

    if sign == '*':
        for n in args:
            multiplication *= n
        print(f'Multiplication of all entered numbers = {multiplication}')

    if sign == '-':
        for n in args[1:]:
            minus -= n
        print(f'Subtracting all entered numbers = {minus}')


make_operation('-', 10, 2, 6)