def change():
    a = input('Enter the first number: ')
    b = input('Enter the second number (not equal to 0): ')

    try:
        c = int(a) ** 2 / int(b)
        print(c)

    except ValueError:
        print('Please enter only numbers')

    except ZeroDivisionError:
        print('Please enter a second non-zero number')


change()
