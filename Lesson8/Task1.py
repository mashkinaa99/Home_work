def oops():
    a = [1, 3, 5, 7]
    b = a[5]


def again():
    try:
        oops()
    except IndexError:
        print('There is no required value in this list')


again()

